# Bulk modulus and lattice parameter of δ-TiNx from DFT

## Problem background
Substoichiometric titanium nitrides (δ‑TiNₓ) formed by multiple‑energy ion implantation exhibit interesting physical properties, and understanding how nitrogen vacancies influence their elastic behaviour and lattice parameter is important. The paper uses density‑functional‑theory (DFT) calculations to determine the equilibrium lattice parameter and bulk modulus for three compositions (TiN₁.₀₀, TiN₀.₇₅, TiN₀.₅₀) and compares these with experimental nanoindentation data. This task focuses on reproducing the theoretical DFT results.

## Approach
The approach constructs periodic supercells of the rock‑salt (NaCl) TiN structure for three nitrogen compositions: TiN₁.₀₀ (no vacancies), TiN₀.₇₅ (one quarter of nitrogen sites vacant), and TiN₀.₅₀ (half of nitrogen sites vacant). Each vacant nitrogen site is left as empty space (empty sphere). Plane‑wave pseudopotential DFT calculations are performed with the GGA‑PW exchange‑correlation functional. For each composition a full structural relaxation and an equation‑of‑state (E‑V) fitting are carried out. From the fitted E‑V curve the equilibrium lattice parameter (a₀) and bulk modulus (B₀) are extracted. The workflow reproduces the theoretical component; experimental nanoindentation data are not required.

## Reproduction target
Perform DFT structural relaxation and equation‑of‑state fitting for δ‑TiNₓ compositions with x = 1.00, 0.75, 0.50. Extract the equilibrium lattice parameter a₀ (in Å) and the bulk modulus B₀ (in GPa) for each composition. Write the results to a CSV file results.csv with columns composition, lattice_parameter_angstrom, bulk_modulus_GPa, containing one row per composition.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- GGA pseudopotentials for titanium and nitrogen: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: DFT calculations for δ-TiNx
- Role: process
- Action: Construct supercells for δ-TiN compositions TiN1.00, TiN0.75, TiN0.50 (NaCl structure), removing nitrogen atoms from the fcc nitrogen sublattice and leaving vacancy sites empty. Perform full DFT structural relaxation and equation-of-state (E-V) fitting using an open-source plane-wave pseudopotential code (e.g., Quantum ESPRESSO) with the GGA-PW exchange-correlation functional and appropriate pseudopotentials. Extract the equilibrium lattice parameter (a0) and bulk modulus (B0) for each composition from the E-V curve.
- Evidence: `/app/outputs/dft_summary.txt`

### Step 2: Compile final results
- Role: scored (load-bearing)
- Action: Write the extracted lattice parameters (in Å) and bulk moduli (in GPa) for the three compositions into a CSV file.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: Header: composition,lattice_parameter_angstrom,bulk_modulus_GPa. Three rows for TiN1.00, TiN0.75, TiN0.50, each with two numeric values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Equilibrium lattice parameters and bulk moduli from DFT equation-of-state fitting for three TiN compositions.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `lattice_parameter_angstrom`, `bulk_modulus_GPa`
  - `units`:
    - `lattice_parameter_angstrom`: Å
    - `bulk_modulus_GPa`: GPa

Notes: The hidden checker compares the reported values against the paper’s FP‑LMTO theoretical results using generous tolerances. The trend is not scored separately but is implicitly captured by the tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "lattice_parameter_angstrom",
          "bulk_modulus_GPa"
        ],
        "units": {
          "lattice_parameter_angstrom": "Å",
          "bulk_modulus_GPa": "GPa"
        }
      },
      "description": "Equilibrium lattice parameters and bulk moduli from DFT equation-of-state fitting for three TiN compositions."
    }
  ],
  "notes": "The hidden checker compares the reported values against the paper’s FP‑LMTO theoretical results using generous tolerances. The trend is not scored separately but is implicitly captured by the tolerances."
}
```

## How you are scored
A hidden verifier reads your results.csv and compares each reported lattice parameter and bulk modulus against reference values with generous tolerances that account for differences in DFT code and pseudopotentials. The score is the average of the lattice parameter score and the bulk modulus score: each value within the hidden tolerance earns full credit for that point; values outside the tolerance earn partial or no credit. Simply copying numbers from the paper is not enough— the verifier expects values consistent with a genuine DFT calculation carried out as described. The final reward is a single float between 0 and 1.
