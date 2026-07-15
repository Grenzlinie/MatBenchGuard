# Density functional theory benchmarking for potassium-ether complexes

## Problem background
Crown ethers selectively bind metal cations, but predicting their binding energies and structures accurately is challenging for computational chemistry. Density functional theory (DFT) offers a practical approach, yet its performance depends strongly on the choice of exchange-correlation functional. This work benchmarks three functionals — SVWN, BP86, and BLYP — for potassium complexes with dimethyl ether (DME), 12-crown-4 (12c4), and 18-crown-6 (18c6). The goal is to assess how well each functional reproduces binding energies and K-O bond lengths, providing insight into the reliability of DFT for cation-ether interactions.

## Approach
The approach uses DFT with three functionals: SVWN (local density approximation), BP86 (gradient-corrected), and BLYP (gradient-corrected). For each complex, a geometry optimization is performed followed by a single-point energy calculation. Supermolecule and fragment calculations are done at the same level of theory: K+, the neutral ether, and the complex. The binding energy is computed as the difference E(complex) - E(ether) - E(K+). The shortest K-O distance is extracted from the optimized complex geometry. Calculations for DME use the aug-cc-pVDZ basis set; for 12c4 and 18c6 the cc-pVDZ basis set is used. The open-source package NWChem is used for all DFT runs. The computed values for each complex/functional combination are collected into a CSV file for analysis. The relative performance of the functionals is then assessed by comparing binding energies and bond lengths across the three methods.

## Reproduction target
Perform DFT geometry optimizations and single-point energy calculations for K+:DME, K+:12c4 (S4 conformation), and K+:18c6 (D3d conformation) with SVWN, BP86, and BLYP, using aug-cc-pVDZ for DME and cc-pVDZ for 12c4/18c6. For each complex/functional combination, report the electronic binding energy (kcal/mol) and the K-O distance (Å) in a CSV file. The relative trends between functionals — for example, whether one functional consistently gives stronger binding or shorter bonds than another — should be examined.

## Assets

- NWChem: https://github.com/nwchemgit/nwchem
- Correlation consistent basis sets (cc-pVDZ, aug-cc-pVDZ): https://www.basissetexchange.org

## Workflow steps

### Step 1: Run DFT calculations for K+-ether complexes
- Role: process
- Action: Construct initial molecular geometries for K+:DME, K+:12c4 (S4 conformation), and K+:18c6 (D3d conformation). Generate NWChem input files, specifying the SVWN, BP86, and BLYP functionals with aug-cc-pVDZ basis set for DME and cc-pVDZ basis set for 12c4/18c6. Run geometry optimizations and single-point energy calculations for each complex/functional combination and for the isolated fragments (K+ and neutral ether) at the same level of theory.
- Evidence: `/app/outputs/dft_outputs.tar.gz`

### Step 2: Compile DFT binding energies and K-O distances
- Role: scored (load-bearing)
- Action: From the output files of step 1, compute the binding energy for each complex as E(complex) - E(ether) - E(K+). Extract the shortest K-O distance or average K-O distance. Write dft_results.csv with one row per (complex, functional) combination.
- Output file: `/app/outputs/dft_results.csv`
- Format: csv
- Contract: Columns: complex (string), functional (string), basis (string), binding_energy_kcal_mol (float), K_O_distance_angstrom (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.csv
- path: `/app/outputs/dft_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed DFT binding energies and K-O bond lengths. Checker compares each value to hidden gold tolerances and verifies relative trends: BLYP binding energy for K+:12c4 is at least 4 kcal/mol less negative than SVWN, and SVWN K-O distance is at least 0.05 Å shorter than BP86 for the same complex.
- schema:
  - `type`: table
  - `required_columns`: `complex`, `functional`, `basis`, `binding_energy_kcal_mol`, `K_O_distance_angstrom`
  - `units`:
    - `binding_energy_kcal_mol`: kcal/mol
    - `K_O_distance_angstrom`: angstrom

Notes: All values are electronic binding energies (BSSE-uncorrected) as reported in the paper. Scoring also checks the qualitative trends described in the notes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "complex",
          "functional",
          "basis",
          "binding_energy_kcal_mol",
          "K_O_distance_angstrom"
        ],
        "units": {
          "binding_energy_kcal_mol": "kcal/mol",
          "K_O_distance_angstrom": "angstrom"
        }
      },
      "description": "Computed DFT binding energies and K-O bond lengths. Checker compares each value to hidden gold tolerances and verifies relative trends: BLYP binding energy for K+:12c4 is at least 4 kcal/mol less negative than SVWN, and SVWN K-O distance is at least 0.05 Å shorter than BP86 for the same complex."
    }
  ],
  "notes": "All values are electronic binding energies (BSSE-uncorrected) as reported in the paper. Scoring also checks the qualitative trends described in the notes."
}
```

## How you are scored
Your CSV file is evaluated by a hidden verifier that compares each binding energy and K-O bond length to reference values obtained from the original study. Values must fall within tolerances that account for normal differences between DFT codes and convergence settings. In addition to absolute values, the verifier checks that the relative ordering of binding energies and bond lengths across functionals follows the expected trends. Each combination contributes to the final reward, providing full credit when all results are within tolerance. The verifier does not merely check whether you reported numbers — it evaluates their accuracy and consistency with the underlying physics.
