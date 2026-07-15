# DFT Calculations of Ferromagnetic Stability and V Magnetic Moments in Li(ZnV)As with Li Vacancies

## Problem background
Li(ZnV)As is a diluted magnetic semiconductor (DMS) based on the cubic LiZnAs host, where V atoms substitute Zn. Li vacancy defects introduce hole carriers that can alter the electronic occupation of $p$-$d$ hybrid orbitals, potentially affecting the magnetic coupling between V dopants and the local magnetic moment on V. This task investigates, using first-principles density functional theory, how the ferromagnetic stability (energy difference $\Delta E = E_{\text{AFM}} - E_{\text{FM}}$) and the atomic magnetic moment of V evolve as the Li vacancy concentration is varied from 0% to 18.75%.

## Approach
Spin-polarized DFT calculations are performed with the GGA-PBE functional. A $2\times2\times1$ supercell of LiZnAs (48 atoms) is constructed, and two Zn atoms are replaced by V at four different V-V separations (denoted V@(0,1) to V@(0,4), ranging from approximately 4.16 Å to 8.45 Å). For each V-V configuration, Li vacancies are created by removing 0, 1, 2, or 3 Li atoms near the V impurities, giving Li vacancy concentrations of 0%, 6.25%, 12.50%, and 18.75%. For every combination of V-V separation and vacancy concentration, total energies are calculated for ferromagnetic (FM) and antiferromagnetic (AFM) spin arrangements of the two V atoms after full geometry relaxation. The ferromagnetic stability is evaluated as $\Delta E = E_{\text{AFM}} - E_{\text{FM}}$, and the atomic magnetic moment on V is extracted from the spin-resolved charge density. Optionally, the total and projected density of states are computed for the V@(0,1) configurations to analyze the $p$-$d$ orbital occupation.

## Reproduction target
Produce two CSV files containing the computed quantities for all 16 configurations (4 V-V separations $\times$ 4 Li vacancy concentrations):
- `delta_E.csv`: columns `configuration`, `Li_vacancy_concentration` (numeric, %), `delta_E_eV` (float).
- `magnetic_moments.csv`: columns `configuration`, `Li_vacancy_concentration` (numeric, %), `V_magnetic_moment_uB` (float).
The values should be obtained from fully relaxed DFT calculations following the prescribed protocol.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- LiZnAs crystal structure

## Workflow steps

### Step 1: Generate supercells and defect configurations
- Role: process
- Action: Build a 2×2×1 supercell of LiZnAs (48 atoms) from the cubic F-43m structure. Create V@(0,N) configurations by substituting two Zn atoms at sites yielding V-V separations of approximately 4.158, 5.966, 7.312, and 8.446 Å. For each V-V separation, introduce Li vacancies by removing 1, 2, or 3 Li atoms near V dopants to achieve Li vacancy concentrations of 6.25%, 12.50%, and 18.75% (plus the no-vacancy case 0%). Produce initial structure files (CIF or other) for all 16 doped/vacancy configurations and the pristine supercell.
- Evidence: `/app/outputs/initial_structures`

### Step 2: Relax pristine LiZnAs supercell
- Role: process
- Action: Perform spin-polarized DFT geometry optimization of the pristine 2×2×1 LiZnAs supercell using GGA-PBE. Record the total energy and optimized lattice parameters.
- Evidence: `/app/outputs/pristine_relax`

### Step 3: DFT relaxations for all doped/vacancy configurations
- Role: process
- Action: For each of the 16 configurations (4 V-V distances × 4 Li vacancy concentrations), perform spin-polarized DFT geometry optimization in both FM and AFM spin arrangements. Use consistent computational parameters (plane-wave cutoff, k-point grid). Save total energies (E_FM, E_AFM), forces, stresses, and optimized geometries.
- Evidence: `/app/outputs/relax_outputs`

### Step 4: Compute ferromagnetic stability ΔE
- Role: scored (load-bearing)
- Action: From the relaxation outputs of step 3, compute ΔE = E_AFM - E_FM for each of the 16 configurations. Write a CSV file delta_E.csv with columns: configuration, Li_vacancy_concentration, delta_E_eV.
- Output file: `/app/outputs/delta_E.csv`
- Format: csv
- Contract: CSV with columns: configuration (string, e.g., V@(0,1)), Li_vacancy_concentration (numeric, %), delta_E_eV (float, eV).
- Scoring: scored by hidden verifier

### Step 5: Extract V atomic magnetic moments
- Role: scored (load-bearing)
- Action: Extract the atomic magnetic moment on V for each configuration from the relaxation outputs of step 3. Write a CSV file magnetic_moments.csv with columns: configuration, Li_vacancy_concentration, V_magnetic_moment_uB.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: CSV with columns: configuration (string), Li_vacancy_concentration (numeric, %), V_magnetic_moment_uB (float, μB).
- Scoring: scored by hidden verifier

### Step 6: Compute density of states for V@(0,1) configurations (optional, not scored)
- Role: process
- Action: For the V@(0,1) configurations at each Li vacancy concentration (0%, 6.25%, 12.50%, 18.75%), perform static DFT calculations to compute spin-polarized total and projected density of states (DOS). Save DOS data for qualitative analysis.
- Evidence: `/app/outputs/dos_outputs`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/delta_E.csv`
- `/app/outputs/magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### delta_E.csv
- path: `/app/outputs/delta_E.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ferromagnetic stability energy difference (ΔE) for each V-doping configuration and Li vacancy concentration.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `Li_vacancy_concentration`, `delta_E_eV`
  - `units`:
    - `delta_E_eV`: eV

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Atomic magnetic moment of V for each V-doping configuration and Li vacancy concentration.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `Li_vacancy_concentration`, `V_magnetic_moment_uB`
  - `units`:
    - `V_magnetic_moment_uB`: μB

Notes: The checker will compare ΔE and V magnetic moments to paper-reported reference values with tolerances, and verify the monotonic decrease of ΔE with increasing Li vacancy concentration for each V-V configuration. Values for 25% Li vacancy concentration are excluded because the paper states those configurations are unstable; only 0%, 6.25%, 12.50%, and 18.75% are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "delta_E.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "Li_vacancy_concentration",
          "delta_E_eV"
        ],
        "units": {
          "delta_E_eV": "eV"
        }
      },
      "description": "Ferromagnetic stability energy difference (ΔE) for each V-doping configuration and Li vacancy concentration."
    },
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "Li_vacancy_concentration",
          "V_magnetic_moment_uB"
        ],
        "units": {
          "V_magnetic_moment_uB": "μB"
        }
      },
      "description": "Atomic magnetic moment of V for each V-doping configuration and Li vacancy concentration."
    }
  ],
  "notes": "The checker will compare ΔE and V magnetic moments to paper-reported reference values with tolerances, and verify the monotonic decrease of ΔE with increasing Li vacancy concentration for each V-V configuration. Values for 25% Li vacancy concentration are excluded because the paper states those configurations are unstable; only 0%, 6.25%, 12.50%, and 18.75% are scored."
}
```

## How you are scored
Your outputs will be evaluated by a hidden automated verifier. The verifier will check both the numerical values in `delta_E.csv` and `magnetic_moments.csv` against reference expectations and the presence of expected physical trends (e.g., how $\Delta E$ and the V magnetic moment depend on Li vacancy concentration and V-V separation). Each scored artifact carries a weight, and the final reward is a weighted combination. Reporting any numbers is not sufficient; they must be physically consistent results from a genuine DFT workflow. The verifier does not disclose the reference values or tolerances.
