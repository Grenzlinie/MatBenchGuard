# DFT Band Gap Calculation for a New Germanium Oxysulfide

## Problem background
Germanium oxysulfide La4(GeS2O2)3 is a wide-gap insulator composed of unusual GeS2O2 tetrahedra and La-centered polyhedra. Its electronic structure—specifically the band gap between the valence band maximum (dominated by S 3p orbitals) and the conduction band minimum (a mix of La, Ge, and S states)—governs its optical properties. First-principles density functional theory (DFT) with hybrid functionals can predict the band gap and gap type, providing insight into potential applications such as photocatalysis or non-linear optics. In this task you will compute the electronic band gap of La4(GeS2O2)3 from its published crystal structure.

## Approach
The approach is a first-principles DFT calculation using a hybrid functional (e.g., HSE06 or HSEsol) to obtain the relaxed ground-state crystal structure and then compute the electronic band structure along high-symmetry k‑points. From the band structure you will extract the band gap value and determine whether it is direct or indirect. The procedure follows the standard computational solid-state physics workflow: geometry optimization (lattice parameters and atomic positions) followed by a band-paths calculation. Any open-source DFT package that supports hybrid functionals is suitable; the outcome should be independent of specific numerical settings provided they are adequate for convergence.

## Reproduction target
Using the provided crystal structure CIF file of La4(GeS2O2)3, you will perform a DFT geometry optimization with a hybrid functional, then compute the electronic band structure along high-symmetry k‑points. From the band structure, determine the band gap (in eV) and whether it is direct or indirect. Write the results to the file band_gap_results.json as a JSON object with keys "band_gap_eV" (a float), "band_gap_type" (the string "direct" or "indirect"), and "method" (a string describing the DFT code and functional used).

## Assets

- Crystal structure CIF for La4(GeS2O2)3: https://doi.org/10.1021/acs.cgd.0c00332
- Open-source DFT package supporting hybrid functionals

## Workflow steps

### Step 1: Geometry Optimization
- Role: process
- Action: Perform DFT geometry optimization (lattice parameters and atomic positions) of the La4(GeS2O2)3 structure from the provided CIF file using a hybrid functional (e.g., HSE06 or HSEsol). Save the relaxed structure for the band gap step.
- Evidence: `/app/outputs/relaxed_structure.json`

### Step 2: Band Gap and Gap Type
- Role: scored (load-bearing)
- Action: Using the relaxed structure, compute the electronic band structure along high-symmetry k-points. Determine the band gap value (eV) and whether it is direct or indirect. Write the results to band_gap_results.json with fields: band_gap_eV (float), band_gap_type (string "direct" or "indirect"), method (string describing the DFT code and functional used).
- Output file: `/app/outputs/band_gap_results.json`
- Format: json
- Contract: {"type":"object","required":["band_gap_eV","band_gap_type","method"],"properties":{"band_gap_eV":{"type":"number","description":"Computed band gap in eV"},"band_gap_type":{"type":"string","enum":["direct","indirect"]},"method":{"type":"string","description":"DFT code and functional used"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap_results.json
- path: `/app/outputs/band_gap_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gap value and type computed by DFT. The checker compares the numeric gap against the paper's reported value (with a tolerance) and the gap type against the expected type (indirect).
- schema:
  - `type`: object
  - `required`: `band_gap_eV`, `band_gap_type`, `method`
  - `properties`:
    - `band_gap_eV`:
      - `type`: number
      - `description`: Computed band gap in eV
    - `band_gap_type`:
      - `type`: string
      - `enum`: `direct`, `indirect`
      - `description`: Whether the band gap is direct or indirect
    - `method`:
      - `type`: string
      - `description`: Description of the DFT code and functional used

Notes: The hidden checker uses the paper-reported values (4.01 eV, indirect) with an appropriate tolerance for the gap value. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap_eV",
          "band_gap_type",
          "method"
        ],
        "properties": {
          "band_gap_eV": {
            "type": "number",
            "description": "Computed band gap in eV"
          },
          "band_gap_type": {
            "type": "string",
            "enum": [
              "direct",
              "indirect"
            ],
            "description": "Whether the band gap is direct or indirect"
          },
          "method": {
            "type": "string",
            "description": "Description of the DFT code and functional used"
          }
        }
      },
      "description": "Band gap value and type computed by DFT. The checker compares the numeric gap against the paper's reported value (with a tolerance) and the gap type against the expected type (indirect)."
    }
  ],
  "notes": "The hidden checker uses the paper-reported values (4.01 eV, indirect) with an appropriate tolerance for the gap value. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Your submission is scored by a hidden verifier that inspects band_gap_results.json. It compares your computed band_gap_eV against a reference value derived from the original study, using an appropriate tolerance to account for differences in code and functional implementation. It also checks that your reported band_gap_type matches the expected type (direct or indirect) exactly. Both criteria must be met to receive full credit; partial credit is awarded if only one is correct. The verifier does not require any particular DFT code or pseudopotential choice, and there is no penalty for reporting a better‑than‑paper metric—your result is judged on its own merit. No other artifacts are scored.
