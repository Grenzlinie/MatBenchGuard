# LiPdH Electron-Phonon Coupling Estimation via Rigid Muffin-Tin Approximation

## Problem background
LiPdH is a candidate ionic superconductor. To assess its potential, one estimates the McMillan-Hopfield parameters η and the electron-phonon coupling constant λ. η quantifies the electron-ion scattering strength at the Fermi level, and λ (derived from η) indicates the attractiveness of the material for superconductivity. This task requires you to compute η and λ for each atom in LiPdH using first-principles electronic structure methods combined with the rigid muffin-tin approximation (RMTA).

## Approach
Use an all-electron full-potential linearized augmented plane-wave (LAPW) code such as Elk. First, perform a self-consistent LAPW calculation for LiPdH at the equilibrium lattice parameters a=2.751 Å and c=3.826 Å, with muffin-tin radii R_Pd=2.3 a.u., R_Li=2.0 a.u., R_H=1.25 a.u., plane-wave cutoff K_max=4.8, and a 40 k-point mesh in the irreducible Brillouin zone. From the converged Kohn-Sham potential, extract the site- and angular-momentum-resolved density of states at the Fermi level, the single-scatterer densities of states, and the scattering phase shifts. Then apply the Gaspari-Gyorffy expression (the RMTA) to compute the McMillan-Hopfield parameter η for Li, Pd, and H. Finally, convert η to the electron-phonon coupling λ for each atom using the relation λ = η / (M⟨ω²⟩) with the provided values: M⟨ω²⟩_Pd = 4.951 eV/Å², M⟨ω²⟩_H = 1.062 eV/Å², and M⟨ω²⟩_Li = 1.062 eV/Å². Sum the atomic λ to obtain the total λ.

## Reproduction target
Produce a CSV file containing the McMillan-Hopfield parameter η (in eV/Å²) and the electron-phonon coupling λ (dimensionless) for each atom (Li, Pd, H) and for the total (sum of λ). The CSV must have three columns: `atom`, `eta`, `lambda`. Rows should be provided for 'Li', 'Pd', 'H', and 'total'. The total row should report the total λ as the sum of the per-atom λ values; its η entry can be left empty or set to the sum of per-atom η.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.net/

## Workflow steps

### Step 1: Self-consistent LAPW electronic structure calculation
- Role: process
- Action: Perform a self-consistent LAPW calculation for LiPdH at equilibrium lattice parameters a=2.751 Å and c=3.826 Å with muffin-tin radii R_Pd=2.3 a.u., R_Li=2.0 a.u., R_H=1.25 a.u., plane-wave cutoff K_max=4.8, and 40 k-points in the irreducible Brillouin zone. Obtain the self-consistent Kohn-Sham potential, site- and angular-momentum-resolved density of states at the Fermi level, and scattering phase shifts.
- Evidence: `/app/outputs/scf_convergence.log`

### Step 2: RMTA calculation of McMillan-Hopfield parameters and electron-phonon coupling
- Role: scored (load-bearing)
- Action: From the converged LAPW results, extract the site angular momentum DOS at the Fermi level, the single-scatterer densities of states, and the scattering phase shifts. Compute the McMillan-Hopfield parameter η for each atom using the Gaspari-Gyorffy expression. Then compute the electron-phonon coupling λ for each atom using λ = η / (M⟨ω²⟩), with the given values: M⟨ω²⟩_Pd=4.951 eV/Å², M⟨ω²⟩_H=1.062 eV/Å², M⟨ω²⟩_Li=1.062 eV/Å². Output the per-atom η and λ, and include a row for the total λ sum. Write a CSV file.
- Output file: `/app/outputs/rmta_parameters.csv`
- Format: csv
- Contract: Columns: atom (string), eta (float, eV/Å²), lambda (float). Rows: atom='Li', 'Pd', 'H', and 'total' (with lambda as sum of others).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rmta_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rmta_parameters.csv
- path: `/app/outputs/rmta_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: McMillan-Hopfield parameter η and electron-phonon coupling λ per atom and total for LiPdH.
- schema:
  - `type`: table
  - `required_columns`: `atom`, `eta`, `lambda`
  - `units`:
    - `eta`: eV/Å²
    - `lambda`: dimensionless
  - `notes`: Rows: Li, Pd, H, total. total row lambda = sum of per-atom lambda.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rmta_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom",
          "eta",
          "lambda"
        ],
        "units": {
          "eta": "eV/Å²",
          "lambda": "dimensionless"
        },
        "notes": "Rows: Li, Pd, H, total. total row lambda = sum of per-atom lambda."
      },
      "description": "McMillan-Hopfield parameter η and electron-phonon coupling λ per atom and total for LiPdH."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your `rmta_parameters.csv` and compare each reported η and λ value against reference values obtained from a correct execution of this protocol. The comparison uses appropriate tolerances that account for legitimate numerical and implementation differences. Each atomic η and λ, as well as the total λ, is checked individually, and the final score is a weighted combination of these checks. Merely writing down the expected numbers without performing the required self-consistent LAPW and RMTA steps will not pass the verifier. The exact tolerances and the reference values are not disclosed.
