# DFT calculation of gas-phase basicities and acidities for ethyl-, vinyl-, and ethynylarsine

## Problem background
The intrinsic gas‑phase acid‑base properties of arsenic‑containing compounds are not well characterized, yet they are central to understanding substituent effects in third‑row element chemistry. This task investigates how unsaturation of the substituent (ethyl, vinyl, ethynyl) influences the proton affinity and deprotonation energy of the arsine functional group. By computing gas‑phase basicities and deprotonation Gibbs free energies using density functional theory, we aim to provide a computational benchmark that complements experimental measurements and helps resolve ambiguities in protonation sites.

## Approach
The computational approach employs hybrid density functional theory (B3LYP) with a two‑tier basis set strategy. For each molecule (ethylarsine, vinylarsine, ethynylarsine) and its arsenic‑protonated and arsenic‑deprotonated forms, a geometry optimization and harmonic vibrational frequency calculation are first performed at the B3LYP/6‑311G(d) level (with diffuse functions, 6‑311+G(d,p), added for the deprotonated anions). Zero‑point energies and thermal corrections are obtained from the frequency calculation (T = 298.15 K). A single‑point energy refinement is then carried out at the B3LYP/6‑311+G(3df,2p) level on the optimized geometry. The total free energy G is computed as G = E_single_point + ZPE + thermal corrections. From these free energies, gas‑phase basicity (GB) is calculated as GB = G(neutral) + G(H⁺) − G(As‑protonated) and the deprotonation Gibbs free energy (Δ_acidG°) as Δ_acidG° = G(As‑deprotonated) + G(H⁺) − G(neutral), using the free energy of a proton G(H⁺) = −6.28 kcal/mol. Only protonation and deprotonation at the arsenic atom are considered. All quantum chemistry calculations are run with an open‑source package such as ORCA.

## Reproduction target
Compute the gas‑phase basicities (GB) and deprotonation Gibbs free energies (Δ_acidG°) for ethylarsine (EA), vinylarsine (VA), and ethynylarsine (ETA) at the B3LYP/6‑311+G(3df,2p)//B3LYP/6‑311G(d) level of theory. Only arsenic‑centred protonation and deprotonation are included. Report the six values in a CSV file with columns: molecule (one of EA, VA, ETA), property (GB or delta_acid_G), value (kcal/mol), and method (the string “B3LYP/6-311+G(3df,2p)”).

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de
- Open Babel: https://openbabel.org

## Workflow steps

### Step 1: Optimize geometries, compute vibrational frequencies and single-point energies
- Role: process
- Action: For each of the nine species (EA, EAH, EAD; VA, VAHa, VADa; ETA, ETAHa, ETADa), generate an initial 3D geometry from the SMILES strings (AsH2CC, AsH2C=C, AsH2C#C) or manually. Optimize the geometry at B3LYP/6-311G(d) for neutral and As-protonated species, and at B3LYP/6-311+G(d,p) for As-deprotonated species using ORCA. Perform a harmonic vibrational frequency calculation at the same level to obtain zero-point energy (ZPE) and thermal corrections (T=298.15 K). Run a single-point energy calculation at B3LYP/6-311+G(3df,2p) on the optimized geometry. Compute the total free energy G = E_single_point + ZPE + thermal corrections for each species. Save all computed total, single-point, ZPE, and thermal energies to energies.json.
- Evidence: `/app/outputs/energies.json`

### Step 2: Compute gas-phase basicities and acidities from the energies
- Role: scored (load-bearing)
- Action: Read the total free energies from energies.json. For each molecule, compute gas-phase basicity GB = G(neutral) + G(H+) - G(protonated) and deprotonation Gibbs free energy Δ_acidG° = G(deprotonated) + G(H+) - G(neutral), using G(H+) = -6.28 kcal/mol. Write a CSV file computed_gb_acidity.csv with columns: molecule (one of EA, VA, ETA), property (GB or delta_acid_G), value (kcal/mol), method (B3LYP/6-311+G(3df,2p)). Include one row per (molecule, property) pair.
- Output file: `/app/outputs/computed_gb_acidity.csv`
- Format: csv
- Contract: molecule: string (EA, VA, ETA); property: string (GB, delta_acid_G); value: float (kcal/mol); method: string (B3LYP/6-311+G(3df,2p))
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_gb_acidity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_gb_acidity.csv
- path: `/app/outputs/computed_gb_acidity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Gas-phase basicities (GB) and acidities (Δ_acidG°) for ethylarsine (EA), vinylarsine (VA), and ethynylarsine (ETA), computed at B3LYP/6-311+G(3df,2p)//B3LYP/6-311G(d). Each row holds one computed value.
- schema:
  - `type`: table
  - `required_columns`: `molecule`, `property`, `value`, `method`

Notes: The hidden checker will compare each of the six numeric values (three GB, three Δ_acidG°) to the corresponding B3LYP/6-311+G(3df,2p) results for As-protonated and As-deprotonated species reported in the source paper. The reward is the fraction of values matching within a predefined tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_gb_acidity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule",
          "property",
          "value",
          "method"
        ]
      },
      "description": "Gas-phase basicities (GB) and acidities (Δ_acidG°) for ethylarsine (EA), vinylarsine (VA), and ethynylarsine (ETA), computed at B3LYP/6-311+G(3df,2p)//B3LYP/6-311G(d). Each row holds one computed value."
    }
  ],
  "notes": "The hidden checker will compare each of the six numeric values (three GB, three Δ_acidG°) to the corresponding B3LYP/6-311+G(3df,2p) results for As-protonated and As-deprotonated species reported in the source paper. The reward is the fraction of values matching within a predefined tolerance."
}
```

## How you are scored
Your submission is scored by an automated verifier. It first checks that the file `/app/outputs/computed_gb_acidity.csv` exists and contains exactly six rows with the correct columns. It then compares each reported GB and Δ_acidG° value to a hidden reference (the paper’s own B3LYP/6‑311+G(3df,2p) computed result for the corresponding species). The final reward is the fraction of the six values (0.0–1.0) that fall within a pre‑defined tolerance of the reference. The tolerance is chosen to accept the legitimate spread that arises from using a different electronic‑structure code (ORCA vs. Gaussian) while still requiring a faithful reproduction of the underlying physics. Intermediate energies, logs, and other artifacts are not graded; only the numerical entries in the CSV affect your score.
