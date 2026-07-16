# Polarizable electron-density force field: water dimer interaction energy prediction

## Problem background
High-energy molecular interactions demand accurate force fields that can replace expensive ab initio calculations. This work develops a polarizable force field based on electron densities: atomic valence electron contributions are represented by Gaussian densities, and repeated application of the Laplace operator generates fictitious electron clouds used in exchange and correlation terms. The model includes polarization by adjusting atomic valence contributions to match Mulliken charges via a self-energy minimization. The task is to reproduce the force field’s predictions for water dimer interaction energy curves and assess their accuracy against high-level quantum chemistry benchmarks.

## Approach
Implement the force field model from the method description: electron–electron, electron–nuclei, and nuclei–nuclei Coulomb terms, plus exchange–correlation contributions with both spherically symmetric and non‑spherical (dipole‑like) components. The exchange–correlation coefficients are constrained to follow alternating factorial expressions, reducing the free parameters to four amplitudes (A, B, C, D) for the interaction model and another four for the polarization model. Atomic density parameters (Gaussian coefficients) are provided for the elements. Two variants are used: all‑electron and effective core potential (ECP). The model is calibrated on a water dimer grid (CCSD(T)/cc‑pVTZ and CCSD(T)/CEP‑31G reference energies and Mulliken charges) by simultaneously fitting the eight parameters via least‑squares, first with Nelder–Mead then L‑BFGS, respecting charge‑conservation constraints. After fitting, the model is used to compute interaction energy curves for two water dimer configurations (H‑O hydrogen‑bonded and O‑O facing) at zero rotation, over distances from 1.0 Å to 5.0 Å.

## Reproduction target
Produce four tab‑separated energy curve files containing predicted interaction energies (in kJ/mol) for the water dimer as a function of distance (in Å): all‑electron H‑O, all‑electron O‑O, ECP H‑O, ECP O‑O. The goal is to achieve low mean absolute deviation when these predictions are compared to accurate CCSD(T) benchmark calculations for the same configurations and distances.

## Assets

- PolElectronDensityForceModel GitHub repository (code + calibration dataset): https://github.com/JoseRodriguezRomero/PolElectronDensityForceModel
- Supplementary Table S1 – atomic valence electron density parameters: 10.1063/5.0210949

## Workflow steps

### Step 1: Implement force field model
- Role: process
- Action: Implement the polarizable electron‑density force field model as described in the paper, including naive Coulomb contributions (electron‑electron, electron‑nuclei, nuclei‑nuclei) and exchange‑correlation terms with both spherically symmetric and non‑spherical (electron‑dipole, nuclei‑dipole) contributions. Constrain the exchange‑correlation coefficients according to Eq. 15 so that only four amplitudes (A, B, C, D) per model need fitting.
- Evidence: none

### Step 2: Load atomic density parameters
- Role: process
- Action: Read the atomic valence electron density parameters (Gaussian amplitudes cₙ and decay coefficients λₙ for each element) from the supplementary material (Table S1). These parameters define the non‑interacting atomic ground‑state eigendensities used by the force field.
- Evidence: none

### Step 3: Fit model parameters on calibration dataset
- Role: process
- Action: From the GitHub repository, load the water‑dimer calibration grid (geometries with reference CCSD(T)/cc‑pVTZ and CCSD(T)/CEP‑31G interaction energies and Mulliken charges). Using the implemented force field, optimize the 8 interaction and 8 polarization parameters (A, B, C, D) for both the all‑electron and ECP variants. Minimize a least‑squares objective that simultaneously fits these parameters, starting with Nelder‑Mead simplex and refining with L‑BFGS, respecting the equality constraint of Eq. 14 and the coefficient constraints of Eq. 15. Save the optimized parameters for later use.
- Evidence: `/app/outputs/fitted_params.json`

### Step 4: Compute all‑electron H‑O energy curve
- Role: scored (load-bearing)
- Action: Using the fitted all‑electron parameters, construct the water dimer in the hydrogen‑bonded (H‑O) configuration with zero rotation. Vary the H‑O distance from 1.0 Å to 5.0 Å and compute the interaction energy at each distance. Write a TSV file with columns: distance_AA (in Å) and predicted_energy_kJ_per_mol.
- Output file: `/app/outputs/all_electron_H_O_energies.tsv`
- Format: tsv
- Contract: distance_AA\tpredicted_energy_kJ_per_mol
- Scoring: scored by hidden verifier

### Step 5: Compute all‑electron O‑O energy curve
- Role: scored (load-bearing)
- Action: Using the fitted all‑electron parameters, construct the water dimer in the oxygen‑facing (O‑O) configuration with zero rotation. Vary the O‑O distance from 1.0 Å to 5.0 Å and compute the interaction energy at each distance. Write a TSV file with columns: distance_AA (in Å) and predicted_energy_kJ_per_mol.
- Output file: `/app/outputs/all_electron_O_O_energies.tsv`
- Format: tsv
- Contract: distance_AA\tpredicted_energy_kJ_per_mol
- Scoring: scored by hidden verifier

### Step 6: Compute ECP H‑O energy curve
- Role: scored (load-bearing)
- Action: Using the fitted ECP (effective core potential) parameters, construct the water dimer in the hydrogen‑bonded (H‑O) configuration with zero rotation. Vary the H‑O distance from 1.0 Å to 5.0 Å and compute the interaction energy at each distance. Write a TSV file with columns: distance_AA (in Å) and predicted_energy_kJ_per_mol.
- Output file: `/app/outputs/ecp_H_O_energies.tsv`
- Format: tsv
- Contract: distance_AA\tpredicted_energy_kJ_per_mol
- Scoring: scored by hidden verifier

### Step 7: Compute ECP O‑O energy curve
- Role: scored (load-bearing)
- Action: Using the fitted ECP parameters, construct the water dimer in the oxygen‑facing (O‑O) configuration with zero rotation. Vary the O‑O distance from 1.0 Å to 5.0 Å and compute the interaction energy at each distance. Write a TSV file with columns: distance_AA (in Å) and predicted_energy_kJ_per_mol.
- Output file: `/app/outputs/ecp_O_O_energies.tsv`
- Format: tsv
- Contract: distance_AA\tpredicted_energy_kJ_per_mol
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/all_electron_H_O_energies.tsv`
- `/app/outputs/all_electron_O_O_energies.tsv`
- `/app/outputs/ecp_H_O_energies.tsv`
- `/app/outputs/ecp_O_O_energies.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### all_electron_H_O_energies.tsv
- path: `/app/outputs/all_electron_H_O_energies.tsv`
- format: tsv
- purpose: scored
- target_policy: threshold_or_better
- description: All‑electron variant interaction energy curve for the hydrogen‑bonded water dimer. The checker computes mean absolute deviation against a hidden reference curve and awards credit on a threshold‑or‑better basis.
- schema:
  - `type`: table
  - `required_columns`: `distance_AA`, `predicted_energy_kJ_per_mol`
  - `units`:
    - `distance_AA`: Å
    - `predicted_energy_kJ_per_mol`: kJ/mol

### all_electron_O_O_energies.tsv
- path: `/app/outputs/all_electron_O_O_energies.tsv`
- format: tsv
- purpose: scored
- target_policy: threshold_or_better
- description: All‑electron variant interaction energy curve for the oxygen‑facing water dimer. The checker computes mean absolute deviation against a hidden reference curve and awards credit on a threshold‑or‑better basis.
- schema:
  - `type`: table
  - `required_columns`: `distance_AA`, `predicted_energy_kJ_per_mol`
  - `units`:
    - `distance_AA`: Å
    - `predicted_energy_kJ_per_mol`: kJ/mol

### ecp_H_O_energies.tsv
- path: `/app/outputs/ecp_H_O_energies.tsv`
- format: tsv
- purpose: scored
- target_policy: threshold_or_better
- description: ECP variant interaction energy curve for the hydrogen‑bonded water dimer. The checker computes mean absolute deviation against a hidden reference curve and awards credit on a threshold‑or‑better basis.
- schema:
  - `type`: table
  - `required_columns`: `distance_AA`, `predicted_energy_kJ_per_mol`
  - `units`:
    - `distance_AA`: Å
    - `predicted_energy_kJ_per_mol`: kJ/mol

### ecp_O_O_energies.tsv
- path: `/app/outputs/ecp_O_O_energies.tsv`
- format: tsv
- purpose: scored
- target_policy: threshold_or_better
- description: ECP variant interaction energy curve for the oxygen‑facing water dimer. The checker computes mean absolute deviation against a hidden reference curve and awards credit on a threshold‑or‑better basis.
- schema:
  - `type`: table
  - `required_columns`: `distance_AA`, `predicted_energy_kJ_per_mol`
  - `units`:
    - `distance_AA`: Å
    - `predicted_energy_kJ_per_mol`: kJ/mol

Notes: The checker compares each submitted energy curve against a hidden reference derived from the paper's Fig. 3. It computes the mean absolute deviation (MAD) in kJ/mol and assigns full credit if MAD ≤ a hidden tolerance, decreasing linearly as MAD increases. The four curves are scored independently and the final reward is their weighted average.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "all_electron_H_O_energies.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_AA",
          "predicted_energy_kJ_per_mol"
        ],
        "units": {
          "distance_AA": "Å",
          "predicted_energy_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "All‑electron variant interaction energy curve for the hydrogen‑bonded water dimer. The checker computes mean absolute deviation against a hidden reference curve and awards credit on a threshold‑or‑better basis."
    },
    {
      "file": "all_electron_O_O_energies.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_AA",
          "predicted_energy_kJ_per_mol"
        ],
        "units": {
          "distance_AA": "Å",
          "predicted_energy_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "All‑electron variant interaction energy curve for the oxygen‑facing water dimer. The checker computes mean absolute deviation against a hidden reference curve and awards credit on a threshold‑or‑better basis."
    },
    {
      "file": "ecp_H_O_energies.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_AA",
          "predicted_energy_kJ_per_mol"
        ],
        "units": {
          "distance_AA": "Å",
          "predicted_energy_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "ECP variant interaction energy curve for the hydrogen‑bonded water dimer. The checker computes mean absolute deviation against a hidden reference curve and awards credit on a threshold‑or‑better basis."
    },
    {
      "file": "ecp_O_O_energies.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "distance_AA",
          "predicted_energy_kJ_per_mol"
        ],
        "units": {
          "distance_AA": "Å",
          "predicted_energy_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "ECP variant interaction energy curve for the oxygen‑facing water dimer. The checker computes mean absolute deviation against a hidden reference curve and awards credit on a threshold‑or‑better basis."
    }
  ],
  "notes": "The checker compares each submitted energy curve against a hidden reference derived from the paper's Fig. 3. It computes the mean absolute deviation (MAD) in kJ/mol and assigns full credit if MAD ≤ a hidden tolerance, decreasing linearly as MAD increases. The four curves are scored independently and the final reward is their weighted average."
}
```

## How you are scored
A hidden verifier will load each of your four energy curve files and compare them to reference curves derived from high‑accuracy ab initio data. For each curve, the verifier computes the mean absolute deviation (MAD) between your predicted energies and the reference values at corresponding distance points. Scoring uses a threshold‑or‑better policy: full credit is awarded if the MAD is within a hidden tolerance; credit decreases linearly for larger deviations. The final reward is the weighted average of the scores for the four curves. Reporting numbers without executing the model will not suffice – the verifier expects physically plausible energy curves that result from correctly implementing and fitting the force field.
