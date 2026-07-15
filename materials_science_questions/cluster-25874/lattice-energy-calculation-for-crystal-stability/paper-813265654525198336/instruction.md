## Problem background

Understanding the impact sensitivity of energetic materials is crucial for their safe handling and application. Nitro group charge ($-Q_{\mathrm{NO_2}}$), derived from Mulliken population analysis, is a widely used descriptor that correlates with impact sensitivity: higher negative charge on the nitro group indicates lower electron‑withdrawing ability, making the R–NO₂ trigger bond more stable and the compound less sensitive to impact. This task focuses on the computational prediction of $-Q_{\mathrm{NO_2}}$ for a set of 15 tautomers of a substituted triazol‑5‑one‑N‑oxide compound.

## Approach

Perform density functional theory (DFT) calculations at the B3LYP/aug‑cc‑pVDZ level for each of the 15 tautomers. For each tautomer:
1. Generate an initial 3D molecular geometry from its SMILES string.
2. Optimize the geometry and obtain Mulliken atomic charges.
3. Compute $-Q_{\mathrm{NO_2}}$ as the sum of the net Mulliken charges on the nitrogen and the two oxygen atoms of the nitro group ($-Q_{\mathrm{NO_2}} = Q_{\mathrm{N}} + Q_{\mathrm{O1}} + Q_{\mathrm{O2}}$).

All calculations can be performed with the open‑source quantum chemistry package Psi4. Initial coordinates can be built with RDKit.

## Reproduction target

Compute the nitro group charge $-Q_{\mathrm{NO_2}}$ (in electrons) for the 15 tautomers named ANTONO‑1 through ANTONO‑15. Report the results in a CSV file with one row per tautomer. The hidden verifier will compare your computed values against a set of reference charges and will also check that the tautomers predicted to be highly insensitive have $-Q_{\mathrm{NO_2}} \geq 0.5$ e while the least insensitive tautomer has $-Q_{\mathrm{NO_2}} \leq 0.1$ e. You do not need to reproduce any other properties (detonation velocity, density, etc.).

## Assets

- **Psi4** – open‑source quantum chemistry package (installable via conda/pip). Used for DFT geometry optimization and Mulliken charge analysis.
- **RDKit** – cheminformatics toolkit (installable via pip). Used to generate initial 3D coordinates from SMILES strings.
- **aug‑cc‑pVDZ basis set** – included with Psi4, no separate download needed.
- **Tautomer SMILES file** – a JSON file mapping tautomer names (ANTONO‑1 … ANTONO‑15) to their isomeric SMILES strings. This file is provided in the task resources at `/app/resources/tautomer_smiles.json`.

## Workflow steps

### Step 1: Generate initial 3D geometries
- Role: process
- Action: Read the tautomer SMILES from `/app/resources/tautomer_smiles.json`. For each tautomer, generate a reasonable initial 3D conformation (e.g., using RDKit's ETKDG or similar) and save it in a format suitable for DFT input (XYZ or Psi4 native). The generated structures are required for the subsequent DFT calculations.
- Evidence: `/app/outputs/initial_geometries/` (directory containing the generated structure files)

### Step 2: DFT optimization, charge analysis, and $-Q_{\mathrm{NO_2}}$ computation
- Role: scored (load‑bearing)
- Action: For each of the 15 tautomers, perform a geometry optimization at the DFT‑B3LYP/aug‑cc‑pVDZ level using Psi4. After convergence, perform a Mulliken population analysis to obtain atomic charges. Identify the nitrogen and two oxygen atoms of the nitro group for each tautomer, sum their charges to obtain $-Q_{\mathrm{NO_2}}$, and write the results to the output CSV.
- Output file: `/app/outputs/nitro_group_charges.csv`
- Format: csv
- Contract:
  - Columns: `tautomer` (string), `q_NO2` (float)
  - Must contain exactly 15 rows, one per tautomer (ANTONO‑1, ANTONO‑2, …, ANTONO‑15).
  - `q_NO2` is in units of elementary charge (e).
- Scoring: scored by hidden verifier

## Output files

- `/app/outputs/nitro_group_charges.csv` – the scored artifact.
- `/app/outputs/initial_geometries/` – directory with the generated starting structures (process evidence; not scored).

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nitro_group_charges.csv
- path: `/app/outputs/nitro_group_charges.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nitro group charges (-Q_NO2) for the 15 tautomers, computed from Mulliken charges at B3LYP/aug‑cc‑pVDZ level.
- schema:
  - `type`: table
  - `required_columns`: `tautomer`, `q_NO2`
  - `units`:
    - `q_NO2`: e (elementary charge)

Notes: The hidden verifier will compare the reported q_NO2 values against a set of reference charges (derived from the paper) with an appropriate tolerance, and will also verify the correct ordering of high‑insensitivity tautomers (q_NO2 ≥ 0.5 e) and the least insensitive tautomer (q_NO2 ≤ 0.1 e).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nitro_group_charges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "tautomer",
          "q_NO2"
        ],
        "units": {
          "q_NO2": "e (elementary charge)"
        }
      },
      "description": "Nitro group charges (-Q_NO2) for the 15 tautomers, computed from Mulliken charges at B3LYP/aug‑cc‑pVDZ level."
    }
  ],
  "notes": "The hidden verifier will compare the reported q_NO2 values against a set of reference charges (derived from the paper) with an appropriate tolerance, and will also verify the correct ordering of high‑insensitivity tautomers (q_NO2 ≥ 0.5 e) and the least insensitive tautomer (q_NO2 ≤ 0.1 e)."
}
```

## How you are scored

A hidden verifier reads your `nitro_group_charges.csv`. It compares each `q_NO2` value against a set of reference charges (with a tolerance) and checks that the tautomers predicted to be highly insensitive have values ≥0.5 e while the least insensitive tautomer is ≤0.1 e. The final reward is a weighted combination of (1) the fraction of charges within tolerance and (2) the correctness of the relative insensitivity ranking. Reporting the paper’s numbers without real computation will not pass because the verifier uses its own reference values and tolerances derived from the actual computational method.
