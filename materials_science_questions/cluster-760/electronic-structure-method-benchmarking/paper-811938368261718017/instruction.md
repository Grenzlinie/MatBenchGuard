# DFT 1JCH coupling constants for halocyclohexanes and tetrahydropyrans

## Problem background
This task investigates the accuracy of density functional theory (DFT) for computing one-bond carbon–hydrogen spin–spin coupling constants (¹JCH) in halocyclohexanes and electron-rich tetrahydropyrans. Computing ¹JCH from first principles is a demanding test of exchange-correlation functionals; the accuracy of different functionals depends on the electron richness of the system, with some functionals performing well for standard organic molecules while others are required for electron-rich environments. You will reproduce a computational protocol that evaluates three widely used functionals by calculating ¹JCH values for two representative compounds: fluorocyclohexane (an electron-non-rich halocyclohexane) and 2-chloropyran (an electron-rich tetrahydropyran). The task is to compute the coupling constants for the axial and equatorial C–H bonds of fluorocyclohexane and for the anomeric C–H bond of 2-chloropyran, using a standardised quantum‑chemical workflow. The hidden checker will compare your computed values against experimental reference data to assess functional performance.

## Approach
The computational workflow consists of two stages. First, the molecular geometries of fluorocyclohexane and 2-chloropyran are optimized at the MP2/cc-pVTZ level of theory. Then, with those geometries fixed, one-bond ¹JCH coupling constants (in Hz) are computed using density functional theory with the hybrid B3LYP functional, its pure-GGA counterpart BLYP, and the PBEPBE functional. Calculations include all four Ramsey contributions (Fermi contact, spin-dipole, diamagnetic and paramagnetic spin-orbit) and use a mixed basis set: EPR‑III for carbon and hydrogen, and cc-pVTZ for oxygen, fluorine, and chlorine. Solvent effects are included via the polarizable continuum model (PCM) with dichloromethane as the solvent. This protocol mirrors the computational procedure used in the systematic study that first examined the system-dependence of functional accuracy for ¹JCH. Your goal is to produce the computed J values for the axial and equatorial C–H bonds of fluorocyclohexane and for the anomeric C–H bond of 2-chloropyran, under each of the three functionals.

## Reproduction target
Compute ¹JCH coupling constants for fluorocyclohexane (axial and equatorial C–H bonds) and 2-chloropyran (anomeric C–H bond) using the B3LYP, BLYP, and PBEPBE functionals with the described MP2/cc-pVTZ optimized geometries, the EPR‑III/cc-pVTZ basis combination, PCM(CH₂Cl₂) solvation, and all four Ramsey terms. Report the computed J values (Hz) in a CSV file with columns: molecule, position, functional, J_calc. The hidden checker will compute deviations from hidden experimental reference values and evaluate whether the pattern of errors across functionals is consistent with the expected relative performance for electron-non-rich versus electron-rich systems.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Optimize molecular geometries of fluorocyclohexane and 2-chloropyran at the MP2/cc-pVTZ level of theory.
- Evidence: `/app/outputs/step_00_geometries.log`

### Step 2: Compute 1JCH coupling constants
- Role: scored (load-bearing)
- Action: Using the optimized geometries, compute one-bond C-H spin-spin coupling constants (1JCH, in Hz) with DFT functionals B3LYP, BLYP, and PBEPBE. Include all four Ramsey terms: Fermi contact (FC), spin-dipole (SD), diamagnetic spin-orbit (DSO) and paramagnetic spin-orbit (PSO). Use the EPR-III basis set for C and H, cc-pVTZ for O, F, Cl, and the PCM solvation model with CH2Cl2 as solvent. Report the computed J values for the axial and equatorial C-H bonds of fluorocyclohexane and the anomeric C-H bond of 2-chloropyran.
- Output file: `/app/outputs/step_01_j_coupling_results.csv`
- Format: csv
- Contract: CSV with columns: molecule (string: 'fluorocyclohexane' or '2-chloropyran'), position (string: 'axial' or 'equatorial' for fluorocyclohexane, 'anomeric' for 2-chloropyran), functional (string: 'B3LYP', 'BLYP', 'PBEPBE'), J_calc (float, units Hz).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_j_coupling_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_j_coupling_results.csv
- path: `/app/outputs/step_01_j_coupling_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed 1JCH coupling constants in Hz. The hidden checker will compare each reported J_calc against experimental reference values, computing the deviation ΔJ = J_calc − J_exp. The score is based on whether the deviations fall within predetermined tolerance bands and reflect the expected functional performance trends.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `position`, `functional`, `J_calc`
  - `units`:
    - `J_calc`: Hz

Notes: The hidden checker holds experimental 1JCH values for fluorocyclohexane (axial and equatorial) and 2-chloropyran (anomeric C-H). The tolerances are set to accommodate legitimate method-dependent variations arising from using ORCA instead of Gaussian 03.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_j_coupling_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "position",
          "functional",
          "J_calc"
        ],
        "units": {
          "J_calc": "Hz"
        }
      },
      "description": "Computed 1JCH coupling constants in Hz. The hidden checker will compare each reported J_calc against experimental reference values, computing the deviation ΔJ = J_calc − J_exp. The score is based on whether the deviations fall within predetermined tolerance bands and reflect the expected functional performance trends."
    }
  ],
  "notes": "The hidden checker holds experimental 1JCH values for fluorocyclohexane (axial and equatorial) and 2-chloropyran (anomeric C-H). The tolerances are set to accommodate legitimate method-dependent variations arising from using ORCA instead of Gaussian 03."
}
```

## How you are scored
Your submitted CSV (`step_01_j_coupling_results.csv`) is the sole scored artifact. The hidden checker compares each computed `J_calc` against a hidden experimental reference value and computes the deviation `ΔJ = J_calc − J_exp`. Scoring rewards entries whose deviations fall within predetermined tolerance windows and where the error pattern across functionals and molecules agrees with the expected performance ordering (i.e., which functional yields the smallest deviation for each type of system). Meeting the tolerance yields full credit for that entry; larger errors receive lower credit. The overall reward is a weighted sum over all rows. No other artifacts are scored, but you must execute the geometry optimization step because the subsequent coupling-constant calculations depend on its output.
