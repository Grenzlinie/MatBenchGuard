# PTA-based MD simulation of uniaxial tension in Al nanocrystals

## Problem background
Molecular dynamics (MD) simulations of crystalline solids under slow loading are severely limited by the huge separation between atomic vibration timescales (femtoseconds) and experimentally relevant deformation rates (seconds). The Practical Time Averaging (PTA) framework overcomes this limitation by defining slow variables as running-time averages of fast atomistic state functions and evolving them on the loading timescale, avoiding explicit integration of the full fast dynamics. This work applies PTA to MD simulations of face‑centered cubic (FCC) aluminum nanocrystals to obtain stress–strain curves and yield strengths at quasi‑static strain rates, and to examine how mechanical response depends on sample size.

## Approach
The PTA method treats the MD system as a singularly perturbed evolution with fast (atomistic) and slow (loading) timescales. For a given applied strain, short MD bursts are run to converge running-time averages of three state functions: kinetic energy, potential energy, and normal reaction stress in the loading direction. These averages are used to extrapolate the slow variables forward in slow time, and the extrapolation is validated or replaced by a higher-accuracy reconstruction that uses additional averages and Simpson's rule. Jumps in the invariant measure – corresponding to events such as dislocation nucleation – are detected and handled by accepting a direct running-time average instead of the extrapolated prediction.

The simulation is implemented in LAMMPS with the embedded‑atom method (EAM) potential for aluminum developed by Mishin et al. Two cubic samples of side lengths 8 nm and 20 nm, with [100] crystal orientation and a lattice parameter of 4.05 Å, are prepared. After thermal relaxation to a stress‑free state at 300 K, uniaxial tension is applied along the x‑direction at a constant engineering strain rate of 10⁻³ s⁻¹. The left boundary atoms remain fixed while the right boundary atoms are displaced stepwise; at each step the PTA protocol is executed to evolve the averaged normal stress. The simulation is carried out up to at least 20 % strain. By comparing the stress–strain response and yield strengths of the two sizes, the size effect can be assessed.

## Reproduction target
Perform the PTA‑guided MD simulations described above for both the 8 nm and 20 nm Al nanocrystals under uniaxial tension at a strain rate of 10⁻³ s⁻¹. From each simulation, produce a stress–strain curve (strain vs. averaged normal stress in GPa) and determine the yield strength – the stress at which the first significant load drop associated with dislocation nucleation occurs. Save the two stress–strain curves as CSV files and the two yield strengths as a JSON file (keys "8nm" and "20nm"). The results should reveal the mechanical response and allow assessment of the size effect on yield strength.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/download.html
- Mishin EAM potential for Al: https://www.ctcms.nist.gov/potentials/entry/1999--Mishin-Y-Farkas-D-Mehl-M-J-Papaconstantopoulos-D-A--Al/

## Workflow steps

### Step 1: Generate initial atomistic configurations
- Role: process
- Action: Create FCC Al blocks of side length 8 nm and 20 nm with lattice parameter 4.05 Å, crystal orientation [100] along x, y, z. Assign initial atomic velocities from a Maxwell–Boltzmann distribution at 300 K. Produce initial LAMMPS data files for each sample.
- Evidence: none

### Step 2: Thermal relaxation to stress-free state
- Role: process
- Action: For each sample, run MD with left boundary atoms fixed and right boundary free until the reaction force on the right boundary vanishes, using the Mishin EAM potential. Output stress-free atomic configurations (LAMMPS restart files) for later loading.
- Evidence: none

### Step 3: PTA-guided MD simulation under uniaxial tension
- Role: process
- Action: For each sample (8 nm and 20 nm), apply uniaxial tensile loading at a constant strain rate of 10^{-3} s^{-1} along the x-direction using the Practical Time Averaging algorithm (see Approach section). At each slow step, run short MD bursts to converge running-time averages of the state functions (potential energy, kinetic energy, normal reaction stress). Advance the slow time with extrapolation and acceptance/reconstruction via Simpson’s rule and jump detection. Simulate up to at least 20% strain. Record the strain and the corresponding averaged normal stress at each accepted slow step.
- Evidence: none

### Step 4: Extract stress–strain curve for 8 nm sample
- Role: scored (load-bearing)
- Action: From the PTA simulation output of the 8 nm sample, collect the strain and the corresponding averaged normal stress (in GPa) at every accepted slow step. Write a CSV file with columns strain, stress_GPa.
- Output file: `/app/outputs/step_04a_stress_strain_8nm.csv`
- Format: csv
- Contract: CSV with header: strain,stress_GPa. Each row contains a strain value (dimensionless) and the averaged normal stress in GPa (float).
- Scoring: scored by hidden verifier

### Step 5: Extract stress–strain curve for 20 nm sample
- Role: scored (load-bearing)
- Action: From the PTA simulation output of the 20 nm sample, collect the strain and the corresponding averaged normal stress (in GPa) at every accepted slow step. Write a CSV file with columns strain, stress_GPa.
- Output file: `/app/outputs/step_04b_stress_strain_20nm.csv`
- Format: csv
- Contract: CSV with header: strain,stress_GPa. Each row contains a strain value (dimensionless) and the averaged normal stress in GPa (float).
- Scoring: scored by hidden verifier

### Step 6: Determine yield strengths
- Role: scored
- Action: From the two stress–strain curves, determine the yield strength for each sample as the stress value (in GPa) at the first significant load drop (corresponding to dislocation nucleation). Write a JSON file with keys "8nm" and "20nm" and their respective yield strengths.
- Output file: `/app/outputs/step_05_yield_strengths.json`
- Format: json
- Contract: JSON object: {"8nm": <yield stress in GPa> (float), "20nm": <yield stress in GPa> (float)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04a_stress_strain_8nm.csv`
- `/app/outputs/step_04b_stress_strain_20nm.csv`
- `/app/outputs/step_05_yield_strengths.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04a_stress_strain_8nm.csv
- path: `/app/outputs/step_04a_stress_strain_8nm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress–strain curve for 8 nm sample under uniaxial tension at 10^{-3} s^{-1}. Scored via structural audit of curve shape (non‑negative stress, elastic rise, peak, load drop, etc.).
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_GPa`
  - `units`:
    - `strain`: dimensionless
    - `stress_GPa`: GPa

### step_04b_stress_strain_20nm.csv
- path: `/app/outputs/step_04b_stress_strain_20nm.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Stress–strain curve for 20 nm sample under uniaxial tension at 10^{-3} s^{-1}. Scored via structural audit of curve shape (non‑negative stress, elastic rise, peak, load drop, etc.).
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_GPa`
  - `units`:
    - `strain`: dimensionless
    - `stress_GPa`: GPa

### step_05_yield_strengths.json
- path: `/app/outputs/step_05_yield_strengths.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Yield strengths for 8 nm and 20 nm samples. Scored by checking that the values fall within hidden reference ranges and that the size ordering is physically plausible.
- schema:
  - `type`: object
  - `required`: `8nm`, `20nm`
  - `properties`:
    - `8nm`:
      - `type`: number
      - `units`: GPa
    - `20nm`:
      - `type`: number
      - `units`: GPa

Notes: The scored artifacts verify the paper's main mechanical response claim. The stress–strain CSVs are load‑bearing and evaluated by structural audit; the yield strengths are derived from those curves and provide an additional size‑ordering check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04a_stress_strain_8nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_GPa"
        ],
        "units": {
          "strain": "dimensionless",
          "stress_GPa": "GPa"
        }
      },
      "description": "Stress–strain curve for 8 nm sample under uniaxial tension at 10^{-3} s^{-1}. Scored via structural audit of curve shape (non‑negative stress, elastic rise, peak, load drop, etc.)."
    },
    {
      "file": "step_04b_stress_strain_20nm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_GPa"
        ],
        "units": {
          "strain": "dimensionless",
          "stress_GPa": "GPa"
        }
      },
      "description": "Stress–strain curve for 20 nm sample under uniaxial tension at 10^{-3} s^{-1}. Scored via structural audit of curve shape (non‑negative stress, elastic rise, peak, load drop, etc.)."
    },
    {
      "file": "step_05_yield_strengths.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "8nm",
          "20nm"
        ],
        "properties": {
          "8nm": {
            "type": "number",
            "units": "GPa"
          },
          "20nm": {
            "type": "number",
            "units": "GPa"
          }
        }
      },
      "description": "Yield strengths for 8 nm and 20 nm samples. Scored by checking that the values fall within hidden reference ranges and that the size ordering is physically plausible."
    }
  ],
  "notes": "The scored artifacts verify the paper's main mechanical response claim. The stress–strain CSVs are load‑bearing and evaluated by structural audit; the yield strengths are derived from those curves and provide an additional size‑ordering check."
}
```

## How you are scored
Each scored artifact – the two CSV stress–strain curves and the JSON yield strengths – is evaluated independently by a hidden verifier. For the stress–strain curves, the verifier performs a structural audit of the curve shape (non‑negative stress, elastic rise, peak, load drop, etc.) rather than a pointwise comparison against a reference. The yield strengths are checked against hidden reference ranges and additionally verified to obey a size ordering that is consistent with the underlying physics. The weighted sum of these checks yields the overall reproduction reward. Reporting a number without genuinely executing the PTA pipeline will not suffice; the verifier expects physically plausible stress–strain curves that can only be obtained by running the described simulations.
