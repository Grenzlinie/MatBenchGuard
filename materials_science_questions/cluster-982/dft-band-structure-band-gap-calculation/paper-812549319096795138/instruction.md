# Band Structure and Band Gap of an Organic-Inorganic Hybrid Perovskite

## Problem background
Hybrid organic–inorganic perovskites are at the forefront of materials research because they can combine desirable electrical and optical properties. A recently reported Pb-based layered perovskite, (C₆H₁₂N)₂Pb(NO₃)₄, was found to display both above-room-temperature dielectric switching and semiconducting behaviour. To gain theoretical understanding of its electronic structure, a first-principles calculation was performed. This task reproduces that computational study: using the crystal structure determined at 293 K, you will run a density-functional theory (DFT) calculation to compute the electronic band gap, determine whether it is direct or indirect, and locate the band edges in reciprocal space. The result quantifies the material’s predicted semiconducting character and provides a theoretical counterpart to the experimental optical measurement.

## Approach
The calculation follows a standard plane‑wave DFT workflow with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional. The atomic positions and cell parameters are taken directly from the experimental crystal structure (monoclinic P2₁/c, 293 K), which is available as a CIF file. After an initial self‑consistent field (SCF) calculation to obtain the ground‑state charge density, a non‑self‑consistent band structure calculation is performed along a high‑symmetry k‑path that includes the A and Γ points. The resulting band energies are then analysed to locate the valence‑band maximum (VBM) and conduction‑band minimum (CBM) and to decide whether the gap is direct or indirect. Standard PBE pseudopotentials for all elements are used, and the energy cutoff and k‑point sampling are chosen to ensure a well‑converged result. Any open‑source plane‑wave DFT code that supports PBE and band‑structure calculations may be employed.

## Reproduction target
Produce a JSON file, band_structure_results.json, containing the computed electronic band gap (in eV), a label indicating whether the gap is direct or indirect, and the fractional k‑point coordinates of the VBM and CBM. The target is to faithfully reproduce the headline DFT result that characterises the semiconducting nature of this material, using only the publicly available crystal structure and a PBE plane‑wave calculation.

## Assets

- Crystal structure CIF for (C6H12N)2Pb(NO3)4 at 293 K: 10.1039/D0DT03206A
- Open-source plane-wave DFT code: https://www.quantum-espresso.org
- PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/accuracy/pbe

## Workflow steps

### Step 1: Run DFT band structure calculation
- Role: process
- Action: Using the crystal structure CIF as input, set up and run a plane-wave DFT calculation with the PBE exchange-correlation functional. Perform a self-consistent field (SCF) calculation followed by a non-self-consistent band structure calculation along a high-symmetry path that includes the A and Gamma points. Save the computed band energies along the k-points to a file.
- Evidence: `/app/outputs/bands.dat`

### Step 2: Extract band gap and band edges
- Role: scored (load-bearing)
- Action: Analyze the computed band structure to identify the valence band maximum (VBM) and conduction band minimum (CBM). Determine the electronic band gap value (eV), whether it is direct or indirect, and the fractional k-point coordinates of VBM and CBM. Write these results to band_structure_results.json.
- Output file: `/app/outputs/band_structure_results.json`
- Format: json
- Contract: JSON object with keys: band_gap_ev (float), direct_or_indirect (string, 'direct' or 'indirect'), vbm_kpoint (list of three floats, fractional coordinates), cbm_kpoint (list of three floats, fractional coordinates).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_structure_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_structure_results.json
- path: `/app/outputs/band_structure_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The electronic band gap (eV), gap character, and k-space locations of the VBM and CBM computed from the DFT band structure.
- schema:
  - `type`: object
  - `required`: `band_gap_ev`, `direct_or_indirect`, `vbm_kpoint`, `cbm_kpoint`
  - `properties`:
    - `band_gap_ev`:
      - `type`: number
    - `direct_or_indirect`:
      - `type`: string
      - `enum`: `direct`, `indirect`
    - `vbm_kpoint`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3
    - `cbm_kpoint`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 3
      - `maxItems`: 3

Notes: The checker compares the submitted values against a hidden reference (the paper's own DFT results) using tolerances appropriate for code-to-code variability. All fields must be present and syntactically valid; the hidden grading tolerances are not disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_structure_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "band_gap_ev",
          "direct_or_indirect",
          "vbm_kpoint",
          "cbm_kpoint"
        ],
        "properties": {
          "band_gap_ev": {
            "type": "number"
          },
          "direct_or_indirect": {
            "type": "string",
            "enum": [
              "direct",
              "indirect"
            ]
          },
          "vbm_kpoint": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          },
          "cbm_kpoint": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 3,
            "maxItems": 3
          }
        }
      },
      "description": "The electronic band gap (eV), gap character, and k-space locations of the VBM and CBM computed from the DFT band structure."
    }
  ],
  "notes": "The checker compares the submitted values against a hidden reference (the paper's own DFT results) using tolerances appropriate for code-to-code variability. All fields must be present and syntactically valid; the hidden grading tolerances are not disclosed."
}
```

## How you are scored
A hidden verifier compares your submitted band_gap_ev, direct_or_indirect, vbm_kpoint, and cbm_kpoint against a reference derived from the original DFT calculation. The verifier applies tolerances appropriate for code‑to‑code variability; the exact tolerances are not disclosed. The band gap value and gap character together carry the majority of the weight, while the k‑point coordinates carry a smaller weight. Reporting a number without executing the underlying calculation is not sufficient; the verifier checks that the submitted results correspond to a genuine DFT band‑structure run.
