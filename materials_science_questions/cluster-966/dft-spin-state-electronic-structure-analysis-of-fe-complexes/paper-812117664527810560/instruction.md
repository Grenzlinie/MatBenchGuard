# Computational normal mode analysis of an iron-sulfur cubane cluster

## Problem background
The cubane-like [Fe4S4(SPh)4]2− cluster is a well-known synthetic model for the 4Fe‑4S clusters found in ferredoxins, high‑potential iron proteins (HiPIPs), and many other biological systems. Understanding its vibrational dynamics — the normal‑mode frequencies and the character of iron motion — is essential for interpreting experimental spectra (IR, Raman, nuclear resonance vibrational spectroscopy) and for linking the cluster’s structure to its function. This task focuses on the computational prediction of the cluster’s vibrational frequencies, using two complementary approaches: density functional theory (DFT) calculations and an empirical Urey‑Bradley force field (UBFF) normal mode analysis. By computing the frequencies for both the natural‑abundance (32S) and the 36S‑substituted bridging‑sulfur isotopologues, the task provides a quantitative test of the computational models.

## Approach
The study will be performed on the full [Fe4S4(SPh)4]2− anion using two independent computational methods:

1) DFT normal mode analysis: A spin‑unrestricted broken‑symmetry DFT calculation is carried out using an open‑source quantum chemistry code (e.g., ORCA or NWChem). The geometry is taken from the published low‑temperature crystal structure (Excoffon et al. 1991). Two calculations are performed: one with natural‑abundance sulfur isotopes (32S) for all sulfur atoms, and one where the bridging sulfide positions are replaced with 36S. Diagonalisation of the Hessian yields the vibrational normal modes, from which the frequencies and iron mode composition factors (e²) are extracted.

2) Urey‑Bradley force field (UBFF) normal mode analysis: A GF‑matrix normal mode calculation is implemented in Python. The Urey‑Bradley force constants (K, H, F) are **not** given a priori; instead, they must be fitted to reproduce the experimental vibrational frequencies of the cluster. A set of target frequencies (cm⁻¹) for the two isotopic compositions is provided below. The agent should implement a least‑squares optimisation (or an equivalent numerical method) to adjust the force constants so that the computed normal‑mode frequencies match the targets as closely as possible.

Experimental target frequencies (cm⁻¹):
```json
[
  {"mode_id": 1, "frequency_32S": 433, "frequency_36S": 433, "description": "Ligand + Fe–Sᵗ stretch"},
  {"mode_id": 2, "frequency_32S": 395, "frequency_36S": 388, "description": "Fe–Sᵗ stretch"},
  {"mode_id": 3, "frequency_32S": 400, "frequency_36S": 386, "description": "Mixed Fe–S stretch"},
  {"mode_id": 4, "frequency_32S": 381, "frequency_36S": 367, "description": "mostly Fe–Sᵇ stretch"},
  {"mode_id": 5, "frequency_32S": 382, "frequency_36S": 372, "description": "mostly Fe–Sᵇ stretch"},
  {"mode_id": 6, "frequency_32S": 376, "frequency_36S": 356, "description": "mostly Fe–Sᵇ stretch"},
  {"mode_id": 7, "frequency_32S": 358, "frequency_36S": 345, "description": "mostly Fe–Sᵇ stretch"},
  {"mode_id": 8, "frequency_32S": 290, "frequency_36S": 283, "description": "Fe–Sᵇ stretch"},
  {"mode_id": 9, "frequency_32S": 288, "frequency_36S": 279, "description": "Fe–Sᵇ stretch"},
  {"mode_id": 10, "frequency_32S": 267, "frequency_36S": 261, "description": "Fe–Sᵇ stretch"},
  {"mode_id": 11, "frequency_32S": 237, "frequency_36S": 232, "description": "S–Fe–S bend"},
  {"mode_id": 12, "frequency_32S": 226, "frequency_36S": 220, "description": "S–Fe–S bend"},
  {"mode_id": 13, "frequency_32S": 157, "frequency_36S": 155, "description": "bending"},
  {"mode_id": 14, "frequency_32S": 149, "frequency_36S": 145, "description": "breathing (A1Fe)"},
  {"mode_id": 15, "frequency_32S": 136, "frequency_36S": 135, "description": "bending"},
  {"mode_id": 16, "frequency_32S": 103, "frequency_36S": 101, "description": "S–Fe–S bend"}
]
```
After obtaining the fitted constants, build the G matrix from the atomic masses and the crystal geometry; solve the secular equation |GF – λI| = 0 to obtain the vibrational frequencies for the two isotopic compositions. No symmetry constraints are imposed, although the cluster’s approximate symmetry may be used for labelling the modes.

## Reproduction target
Produce two output files in JSON format:

- /app/outputs/dft_frequencies.json: an array of objects, each with the fields mode_id, symmetry, frequency_32S_cm⁻¹, frequency_36S_cm⁻¹, e_squared, and an optional label. The file must contain all real normal modes computed from the DFT calculations for both isotopologues.

- /app/outputs/ubff_frequencies.json: an array of objects, each with the fields mode_id, frequency_32S_cm⁻¹, frequency_36S_cm⁻¹, and symmetry. The file must report all normal‑mode frequencies obtained from the UBFF GF‑matrix calculation for both isotopic compositions.

The exact schemas are specified in the Output contract section of this document.

## Assets

- Low-temperature crystal structure of [Fe4S4(SPh)4]2- (Excoffon et al. 1991): 10.1021/ic00014a019
- Open-source quantum chemistry package (e.g., ORCA or NWChem): https://orcaforum.kofo.mpg.de/
- Python with NumPy: python

## Workflow steps

### Step 1: Prepare molecular model from crystal structure
- Role: process
- Action: Obtain the crystal structure of the [Fe4S4(SPh)4]2- anion and build two molecular models: one with natural-abundance sulfur isotopes (32S) and one with 36S isotopes substituted at the bridging sulfur positions.
- Evidence: `/app/outputs/prepared_structure.xyz`

### Step 2: DFT normal mode calculation
- Role: scored (load-bearing)
- Action: Perform a broken-symmetry DFT calculation on the cluster for both isotopic compositions using an appropriate exchange-correlation functional and basis set. Compute the vibrational normal-mode frequencies and Fe mode composition factors (e²) for all real normal modes. Write the results to dft_frequencies.json.
- Output file: `/app/outputs/dft_frequencies.json`
- Format: json
- Contract: {"type":"array","items":{"type":"object","properties":{"mode_id":{"type":"integer"},"symmetry":{"type":"string"},"frequency_32S_cm-1":{"type":"number"},"frequency_36S_cm-1":{"type":"number"},"e_squared":{"type":"number"},"label":{"type":"string"}},"required":["mode_id","frequency_32S_cm-1","frequency_36S_cm-1"]}}
- Scoring: scored by hidden verifier

### Step 3: Fit Urey‑Bradley force constants
- Role: process
- Action: Fit the Urey‑Bradley force field parameters (K, H, F) to the experimental target frequencies listed in the Approach section. Use the geometry from Step 1 with the correct atomic masses for each isotopologue. Numerically optimise the parameters to minimise the differences between the computed GF‑matrix frequencies and the supplied experimental frequencies for both isotopologues.
- Evidence: `/app/outputs/fitted_ubff_constants.json`

### Step 4: Urey‑Bradley force field normal mode analysis
- Role: scored
- Action: Using the fitted UBFF force constants from Step 3 and the geometry from Step 1, perform a normal mode analysis (GF matrix method) to compute the vibrational frequencies for both isotopic compositions. Write the results to ubff_frequencies.json.
- Output file: `/app/outputs/ubff_frequencies.json`
- Format: json
- Contract: {"type":"array","items":{"type":"object","properties":{"mode_id":{"type":"integer"},"frequency_32S_cm-1":{"type":"number"},"frequency_36S_cm-1":{"type":"number"},"symmetry":{"type":"string"}},"required":["mode_id","frequency_32S_cm-1","frequency_36S_cm-1"]}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_frequencies.json`
- `/app/outputs/ubff_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_frequencies.json
- path: `/app/outputs/dft_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-computed normal-mode frequencies and Fe mode composition factors for the natural‑abundance (32S) and the 36S‑substituted bridging‑sulfur clusters.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `mode_id`:
        - `type`: integer
      - `symmetry`:
        - `type`: string
      - `frequency_32S_cm-1`:
        - `type`: number
      - `frequency_36S_cm-1`:
        - `type`: number
      - `e_squared`:
        - `type`: number
      - `label`:
        - `type`: string
    - `required`: `mode_id`, `frequency_32S_cm-1`, `frequency_36S_cm-1`

### ubff_frequencies.json
- path: `/app/outputs/ubff_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Urey‑Bradley force field computed vibrational frequencies for the two isotopic compositions.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `mode_id`:
        - `type`: integer
      - `frequency_32S_cm-1`:
        - `type`: number
      - `frequency_36S_cm-1`:
        - `type`: number
      - `symmetry`:
        - `type`: string
    - `required`: `mode_id`, `frequency_32S_cm-1`, `frequency_36S_cm-1`

Notes: The agent must use the provided Urey‑Bradley force constants and the public crystal structure; the DFT calculation may use any open‑source quantum chemistry code.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "mode_id": {
              "type": "integer"
            },
            "symmetry": {
              "type": "string"
            },
            "frequency_32S_cm-1": {
              "type": "number"
            },
            "frequency_36S_cm-1": {
              "type": "number"
            },
            "e_squared": {
              "type": "number"
            },
            "label": {
              "type": "string"
            }
          },
          "required": [
            "mode_id",
            "frequency_32S_cm-1",
            "frequency_36S_cm-1"
          ]
        }
      },
      "description": "DFT-computed normal-mode frequencies and Fe mode composition factors for the natural‑abundance (32S) and the 36S‑substituted bridging‑sulfur clusters."
    },
    {
      "file": "ubff_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "mode_id": {
              "type": "integer"
            },
            "frequency_32S_cm-1": {
              "type": "number"
            },
            "frequency_36S_cm-1": {
              "type": "number"
            },
            "symmetry": {
              "type": "string"
            }
          },
          "required": [
            "mode_id",
            "frequency_32S_cm-1",
            "frequency_36S_cm-1"
          ]
        }
      },
      "description": "Urey‑Bradley force field computed vibrational frequencies for the two isotopic compositions."
    }
  ],
  "notes": "The agent must use the provided Urey‑Bradley force constants and the public crystal structure; the DFT calculation may use any open‑source quantum chemistry code."
}
```

## How you are scored
A hidden verifier scores your submission by comparing the reported frequencies (and, for DFT, the Fe mode composition factors) in each output file against reference results that follow from the same computational protocols. The assessment is performed separately for dft_frequencies.json and ubff_frequencies.json, with each contribution weighted. The final reward is a number between 0 (no match) and 1 (all checked modes within tolerance), computed as a weighted sum of the individual scores.

Reporting the expected numbers is not sufficient; the outputs must be consistent with the computational pipelines described in the workflow steps. The verifier checks the structure of the files and applies tolerance windows to frequency values and isotope shifts; the precise tolerances are not disclosed.
