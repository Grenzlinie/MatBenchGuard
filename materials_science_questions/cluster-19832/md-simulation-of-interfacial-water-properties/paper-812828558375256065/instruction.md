# Hydration Layer Oscillatory Forces in AFM via MD Simulation

## Problem background
Atomic force microscopy (AFM) is widely used to probe hydration layers on solid surfaces, yet the molecular origin of the oscillatory forces often observed in force–distance curves remains debated. All-atom molecular dynamics (MD) simulations can provide molecular-level insight by directly modelling an AFM tip approaching a surface in water. This study investigates the potential of mean force and the force on the tip for four tip–surface combinations with different wettabilities, aiming to understand the relationship between the confined water structure and the resulting force behaviour.

## Approach
The simulation approach constructs four model AFM systems: a hemispherical tip (radius 1.0 nm) of either Au (hydrophilic) or C (hydrophobic) positioned above a flat two-layer slab of Au or C, immersed in liquid water described by the SPC/E model. For each combination, umbrella sampling is performed at a series of tip–surface distances using harmonic restraints, yielding the potential of mean force (PMF) as a function of the distance. The corresponding force is derived as the negative gradient of the PMF. The PMF and force curves are then analyzed to locate (meta)stable hydration configurations (tri-, bi-, monolayer and tip–surface contact), to quantify the force oscillation amplitudes, and to determine the oscillation periods. Additionally, the local water density and the molecular dipole orientation in the first hydration layer are examined as a function of tip–surface separation.

## Reproduction target
You will produce four CSV files that capture the key quantitative outcomes of the simulation workflow:

1. `pmf_minima.csv` – the distances at the minima of the PMF and force curves (in Å) for each (meta)stable configuration present in each system.
2. `force_amplitudes.csv` – the force oscillation amplitudes (in pN) near each configuration.
3. `oscillation_periods.csv` – the oscillation periods (in Å) for the PMF and force curves for each transition between configurations.
4. `orientation_peak.csv` – the peak of the water dipole orientation distribution P(cosθ) for the Au/Au system at tip–surface distance D = 6.0 Å.

The required columns and data types are specified in the workflow steps below. All output files must be placed under `/app/outputs` and must conform exactly to the described schemas.

## Assets

- LAMMPS: https://lammps.sandia.gov
- PLUMED: https://www.plumed.org

## Workflow steps

### Step 1: System preparation and equilibration
- Role: process
- Action: Build four simulation systems (Au tip on Au surface, Au tip on C surface, C tip on Au surface, C tip on C surface). Each consists of a hemispherical tip (radius 1.0 nm) above a two-layer slab, solvated with 8342 SPC/E water molecules. Equilibrate each system at 300 K and 1 atm (NVT then NPT) until bulk water density converges.
- Evidence: `/app/outputs/equilibration_final.log`

### Step 2: Umbrella sampling simulations
- Role: process
- Action: For each of the four systems, run restrained MD at 66 target distances D (15.6 Å to 2.6 Å, step 0.2 Å) using harmonic bias potentials. Each window: 4 ns simulation, discard first 0.2 ns for equilibration. Record the reaction coordinate D and corresponding forces for PMF reconstruction.
- Evidence: `/app/outputs/umbrella_histograms.csv`

### Step 3: Potential of mean force reconstruction
- Role: process
- Action: Use the variational free-energy profile (vFEP) method (or WHAM) with the umbrella histograms to reconstruct the PMF curve as a function of D for each tip-surface combination. Account for the Jacobian correction.
- Evidence: `/app/outputs/pmf_curves.csv`

### Step 4: Force-distance curve derivation
- Role: process
- Action: Compute the average force on the tip as the negative numerical gradient of the PMF for each system. Produce smooth force vs. D curves.
- Evidence: `/app/outputs/force_curves.csv`

### Step 5: Extract PMF and force minima positions
- Role: scored (load-bearing)
- Action: From the PMF and force curves, locate the minima corresponding to tri-, bi-, monolayer and tip-contact configurations for each system. Report the D values at minima in a CSV file.
- Output file: `/app/outputs/pmf_minima.csv`
- Format: csv
- Contract: columns: system (string: Au_Au, Au_C, C_Au, C_C), configuration (string: trilayer, bilayer, monolayer, contact), D_PMF (float, Å), D_force (float, Å). Only configurations existing for a given system are listed; missing ones are omitted.
- Scoring: scored by hidden verifier

### Step 6: Compute force oscillation amplitudes
- Role: scored (load-bearing)
- Action: For each system and configuration, calculate the amplitude of oscillation in the force as the difference between the nearest maximum and minimum. Output the amplitudes in a CSV.
- Output file: `/app/outputs/force_amplitudes.csv`
- Format: csv
- Contract: columns: system (string), configuration (string), amplitude_pN (float). Include all (meta)stable configurations present for each system.
- Scoring: scored by hidden verifier

### Step 7: Extract oscillation periods
- Role: scored
- Action: Compute the distance between neighbouring PMF minima and between neighbouring force minima to obtain the oscillation periods for each transition. Write the periods to a CSV.
- Output file: `/app/outputs/oscillation_periods.csv`
- Format: csv
- Contract: columns: system (string), transition (string, e.g. 'trilayer_to_bilayer'), period_PMF (float, Å), period_force (float, Å). Include all relevant transitions present for each system.
- Scoring: scored by hidden verifier

### Step 8: Dipole orientation peak at close proximity
- Role: scored
- Action: For the Au tip on Au surface system at D=6 Å, extract the dipole orientation of water molecules in the first hydration layer on the surface. Compute the distribution P(cosθ) and report the peak position (cosθ). Write one row to a CSV.
- Output file: `/app/outputs/orientation_peak.csv`
- Format: csv
- Contract: columns: system (string: Au_Au), D_Angstrom (float: 6.0), peak_cosθ (float). The peak corresponds to the maximum of the P(cosθ) distribution.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pmf_minima.csv`
- `/app/outputs/force_amplitudes.csv`
- `/app/outputs/oscillation_periods.csv`
- `/app/outputs/orientation_peak.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pmf_minima.csv
- path: `/app/outputs/pmf_minima.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Positions (D) of PMF and force minima for each (meta)stable configuration.
- schema:
  - `type`: table
  - `required_columns`: `system`, `configuration`, `D_PMF`, `D_force`
  - `units`:
    - `D_PMF`: Å
    - `D_force`: Å

### force_amplitudes.csv
- path: `/app/outputs/force_amplitudes.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Force oscillation amplitudes near each hydration configuration.
- schema:
  - `type`: table
  - `required_columns`: `system`, `configuration`, `amplitude_pN`
  - `units`:
    - `amplitude_pN`: pN

### oscillation_periods.csv
- path: `/app/outputs/oscillation_periods.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Oscillation periods for PMF and force curves.
- schema:
  - `type`: table
  - `required_columns`: `system`, `transition`, `period_PMF`, `period_force`
  - `units`:
    - `period_PMF`: Å
    - `period_force`: Å

### orientation_peak.csv
- path: `/app/outputs/orientation_peak.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Peak of the dipole orientation distribution for Au/Au at D=6 Å.
- schema:
  - `type`: table
  - `required_columns`: `system`, `D_Angstrom`, `peak_cosθ`
  - `units`:
    - `D_Angstrom`: Å
    - `peak_cosθ`: dimensionless

Notes: The checker compares each entry to hidden reference values with domain-appropriate tolerances. Exact_match policy is used because these are fixed physical quantities where 'better' is undefined; comparison is against the paper's reported values within tolerance windows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pmf_minima.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "configuration",
          "D_PMF",
          "D_force"
        ],
        "units": {
          "D_PMF": "Å",
          "D_force": "Å"
        }
      },
      "description": "Positions (D) of PMF and force minima for each (meta)stable configuration."
    },
    {
      "file": "force_amplitudes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "configuration",
          "amplitude_pN"
        ],
        "units": {
          "amplitude_pN": "pN"
        }
      },
      "description": "Force oscillation amplitudes near each hydration configuration."
    },
    {
      "file": "oscillation_periods.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "transition",
          "period_PMF",
          "period_force"
        ],
        "units": {
          "period_PMF": "Å",
          "period_force": "Å"
        }
      },
      "description": "Oscillation periods for PMF and force curves."
    },
    {
      "file": "orientation_peak.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "D_Angstrom",
          "peak_cosθ"
        ],
        "units": {
          "D_Angstrom": "Å",
          "peak_cosθ": "dimensionless"
        }
      },
      "description": "Peak of the dipole orientation distribution for Au/Au at D=6 Å."
    }
  ],
  "notes": "The checker compares each entry to hidden reference values with domain-appropriate tolerances. Exact_match policy is used because these are fixed physical quantities where 'better' is undefined; comparison is against the paper's reported values within tolerance windows."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. For each of the four output files, the verifier compares your reported numbers to a hidden reference using domain-appropriate tolerance windows. Every file contributes a predetermined fraction to the total reward (the two main files, `pmf_minima.csv` and `force_amplitudes.csv`, carry the largest weight). The verifier only inspects the final CSV files; it does not read your simulation logs or intermediate data. To achieve a high score you must faithfully execute the umbrella‑sampling and free‑energy‑reconstruction pipeline. Providing numbers without running the simulations will not meet the required accuracy.
