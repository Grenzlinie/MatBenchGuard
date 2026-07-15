# DFT Calculation of HOMO-LUMO Gap for Mn-doped Polyoxotitanate Nanocluster

## Problem background
Titanium dioxide (TiO₂) photocatalysts are limited by a wide band gap (~3.2 eV) that restricts photo‑activity to ultraviolet light. Transition‑metal doping is a widely explored strategy to introduce mid‑gap states and reduce the effective band gap, potentially enabling visible‑light photocatalysis. A large manganese‑doped polyoxotitanate nanocluster, Ti₁₄MnO₁₄(OH)₂(OEt)₂₈, has been synthesized, and its electronic structure was studied by density functional theory (DFT) to understand the effect of Mn doping on the band gap. The key quantity of interest is the HOMO–LUMO energy gap, which serves as a theoretical band gap and quantifies the reduction relative to undoped analogues.

## Approach
The experimental crystal structure of Ti₁₄MnO₁₄(OH)₂(OEt)₂₈, refined from single‑crystal X‑ray diffraction and deposited as CCDC 930833, provides the atomic coordinates. A single‑point DFT calculation is performed on this geometry using the B3LYP functional and the 6‑31G basis set. The manganese centre is treated as high‑spin Mn²⁺ in a sextet configuration (multiplicity 7). To keep the reproduction fully open, an open‑source quantum‑chemistry package (e.g., ORCA, NWChem, or CP2K) is used instead of proprietary software. The HOMO–LUMO energy gap is extracted directly from the orbital energies printed in the output of the single‑point calculation.

## Reproduction target
Obtain the CIF file for Ti₁₄MnO₁₄(OH)₂(OEt)₂₈ (CCDC 930833). Using an open‑source DFT code, run a single‑point calculation at the B3LYP/6‑31G level of theory with the Mn centre in a sextet state. Extract the HOMO–LUMO energy gap (in eV) from the computed orbital energies. Write the result to a JSON file at /app/outputs/homo_lumo_gap.json with the key "homo_lumo_gap_ev" and a float value representing the gap in electronvolts.

## Assets

- Crystal structure of Ti14MnO14(OH)2(OEt)28 (CCDC 930833): http://www.ccdc.cam.ac.uk/conts/retrieving.html
- Open-source DFT software (e.g., ORCA, NWChem, CP2K)

## Workflow steps

### Step 1: DFT single-point calculation and HOMO-LUMO extraction
- Role: scored
- Action: Obtain the CIF for Ti14MnO14(OH)2(OEt)28 from CCDC 930833. Using an open-source DFT code, perform a single-point energy calculation at the B3LYP/6-31G level with Mn treated as a high-spin sextet (multiplicity 7). Extract the HOMO-LUMO energy gap in eV from the orbital energies, and write the value to the output file.
- Output file: `/app/outputs/homo_lumo_gap.json`
- Format: json
- Contract: {"homo_lumo_gap_ev": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homo_lumo_gap.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homo_lumo_gap.json
- path: `/app/outputs/homo_lumo_gap.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The HOMO-LUMO energy gap computed from the DFT calculation.
- schema:
  - `type`: object
  - `required`:
    - `homo_lumo_gap_ev`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `homo_lumo_gap_ev`: eV

Notes: Only the DFT HOMO-LUMO gap is reproduced; experimental band gaps and crystal structure refinement are not within scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homo_lumo_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "homo_lumo_gap_ev": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "homo_lumo_gap_ev": "eV"
        }
      },
      "description": "The HOMO-LUMO energy gap computed from the DFT calculation."
    }
  ],
  "notes": "Only the DFT HOMO-LUMO gap is reproduced; experimental band gaps and crystal structure refinement are not within scope."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the file /app/outputs/homo_lumo_gap.json, extracts the numeric value of "homo_lumo_gap_ev", and compares it to a reference value for the correct HOMO–LUMO gap of this cluster. Full credit is awarded when the computed gap is sufficiently close to the expected value; the verifier may apply an undisclosed tolerance. The verifier runs automatically and returns a single reward between 0 and 1. No other artifacts or intermediate outputs are scored, so the final reward is based entirely on this one result.
