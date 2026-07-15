# QEq Method for Predicting Atomic Charges and Dipole Moments

## Problem background
Knowledge of charge distributions within molecules is critical for computing electrostatic energies in molecular simulations, yet reliable charges are often unavailable for many systems. This task addresses the challenge by implementing a charge equilibration (QEq) method that predicts atomic partial charges and molecular dipole moments from molecular geometry and experimental atomic properties (ionization potentials, electron affinities, and covalent radii). The target is to compute charges and dipole moments for a given set of test molecules.

## Approach
The QEq method models the total electrostatic energy of a molecule as a sum over atoms of a charge-dependent energy (up to second order) plus pairwise shielded Coulomb interactions. The key idea is that at equilibrium, the atomic chemical potentials (the derivative of the energy with respect to charge) must be equal across all atoms. The atomic energy parameters—electronegativities and idempotentials—are derived from experimental atomic data. Interatomic Coulomb integrals are computed using Slater-type atomic orbitals, with a shielding correction calibrated by a universal scaling factor (λ = 0.5). For hydrogen, the scheme uses charge-dependent parameters that require self-consistent iteration. The method solves a system of linear equations subject to charge range constraints to obtain equilibrium partial charges. For diatomic molecules, the dipole moment is calculated directly from the charge and bond length. In this task, you will implement this QEq procedure for a set of test molecules using provided atomic parameters and experimental equilibrium geometries. The predicted atomic charges and (where applicable) dipole moments are the final output.

## Reproduction target
Implement the charge equilibration method as described. Using the provided atomic parameters and the equilibrium geometries of the following test molecules: NaCl, KCl, KBr, RbCl, RbI, CsCl, CsI, H₂O, NH₃, CH₄, and HF, compute the equilibrium partial atomic charges and dipole moments (for diatomic molecules). Write the results to a CSV file (`qeq_results.csv`) with columns: `molecule`, `atom`, `predicted_charge` (in electrons), `predicted_dipole_moment` (in Debye; NaN for non-diatomics).

## Assets
### Atomic Parameters
The following atomic parameters (Table I from the paper) are used in the QEq calculations.

| element | χ (eV) | J (eV) | R (Å) | ζ (au) |
|---------|--------|--------|-------|--------|
| Li      | 3.006  | 4.772  | 1.557 | 0.4174 |
| C       | 5.343  | 10.126 | 0.759 | 0.8563 |
| N       | 6.899  | 11.760 | 0.715 | 0.9089 |
| O       | 8.741  | 13.364 | 0.669 | 0.9745 |
| F       | 10.874 | 14.948 | 0.706 | 0.9206 |
| Na      | 2.843  | 4.592  | 2.085 | 0.4364 |
| Si      | 4.168  | 6.974  | 1.176 | 0.7737 |
| P       | 5.463  | 8.000  | 1.102 | 0.8257 |
| S       | 6.928  | 8.972  | 1.047 | 0.8690 |
| Cl      | 8.564  | 9.892  | 0.994 | 0.9154 |
| K       | 2.421  | 3.840  | 2.586 | 0.4524 |
| Br      | 7.790  | 8.850  | 1.141 | 1.0253 |
| Rb      | 2.331  | 3.692  | 2.770 | 0.5162 |
| I       | 6.822  | 7.524  | 1.333 | 1.0726 |
| Cs      | 2.183  | 3.422  | 2.984 | 0.5663 |
| H       | 4.5280*| 13.8904*|0.371| 1.0698 |

*Values for Q_H = 0; for charge-dependent H parameters see equations (20) and (21) in the method description.

### Molecular Geometries
**Diatomic molecules** (bond length, Å):
- NaCl: 2.3606
- KCl: 2.6667
- KBr: 2.8208
- RbCl: 2.7874
- RbI: 3.1769
- CsCl: 2.9063
- CsI: 3.3150
- HF: 0.9168

**Polyatomic molecules** (bond lengths in Å, angles in degrees):
- H₂O: O–H = 0.9572, H–O–H = 104.52
- NH₃: N–H = 1.012, H–N–H = 106.67
- CH₄: C–H = 1.091, tetrahedral angle 109.47

### Tools
No external datasets beyond standard numerical libraries (NumPy, SciPy) are required.

## Workflow steps

### Step 1: QEq charge and dipole moment calculation
- Role: scored
- Action: Implement the QEq method: construct atomic electronegativities, idempotentials, and shielded Coulomb integrals using the provided parameters (Table I from the paper) and the Slater-type orbital shielding formula with λ=0.5. For hydrogen, use the charge-dependent parameters (χ_H^0 = 4.5280 eV, J_HH^0 = 13.8904 eV) and iterate to self-consistency. For each test molecule (NaCl, KCl, KBr, RbCl, RbI, CsCl, CsI, H2O, NH3, CH4, HF), build interatomic distances from provided experimental geometries, solve the linear equations with charge range constraints, and obtain equilibrium partial charges. For diatomic molecules, compute the dipole moment via μ = (1/4.80324) * Q * R. Write the results to qeq_results.csv.
- Output file: `/app/outputs/qeq_results.csv`
- Format: csv
- Contract: molecule (string), atom (string), predicted_charge (float, electrons), predicted_dipole_moment (float, Debye; NaN for non-diatomics)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/qeq_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### qeq_results.csv
- path: `/app/outputs/qeq_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV file with predicted atomic charges (in electrons) and dipole moments (in Debye) for the test molecules. The hidden checker recomputes the mean absolute error for charges across all atoms and for dipole moments across diatomic molecules, comparing to paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `atom`, `predicted_charge`, `predicted_dipole_moment`

Notes: The hidden checker computes mean absolute error (MAE) for charges and for dipole moments separately, using paper-reported values as gold. No tolerance or gold values are revealed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "qeq_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "atom",
          "predicted_charge",
          "predicted_dipole_moment"
        ]
      },
      "description": "CSV file with predicted atomic charges (in electrons) and dipole moments (in Debye) for the test molecules. The hidden checker recomputes the mean absolute error for charges across all atoms and for dipole moments across diatomic molecules, comparing to paper-reported values."
    }
  ],
  "notes": "The hidden checker computes mean absolute error (MAE) for charges and for dipole moments separately, using paper-reported values as gold. No tolerance or gold values are revealed."
}
```

## How you are scored
A hidden verifier reads your submitted `qeq_results.csv`. It compares your predicted atomic charges and dipole moments to reference values (derived from the original study). The reward is based on the accuracy of your predictions across all atoms and molecules (for example, using mean absolute error). The closer your computed values are to the references, the higher your score. Simply reporting numbers from the literature is not sufficient; the verifier checks the values you actually computed.
