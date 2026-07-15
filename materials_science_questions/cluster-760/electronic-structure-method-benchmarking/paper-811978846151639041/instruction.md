# Computed vibrational frequencies and geometries of CCP and CCAs radicals

## Problem background
The dicarbide free radicals CCP and CCAs have recently been identified for the first time using laser-induced fluorescence and emission spectroscopy. The experimental assignments of their ground-state spectroscopic constants were supported by density functional theory (DFT) calculations, which predicted equilibrium geometries and harmonic vibrational frequencies. These theoretical predictions provide critical validation of the spectral assignments. This task reproduces the supporting computational stage: the DFT-based prediction of ground-state structures and vibrational frequencies for the CCP and CCAs radicals and their isotopomers.

## Approach
Use the B3LYP hybrid density functional with the aug-cc-pVTZ basis set. Build linear initial geometries for the CCP (C-C-P) and CCAs (C-C-As) radicals, both in the ²Π electronic state. For each species, perform a gas-phase geometry optimization followed by a harmonic vibrational frequency calculation. Compute the properties for the normal ¹²C¹²C isotopomer and for the ¹³C¹³C isotopomer by setting the appropriate atomic masses. From the optimized geometry, extract the equilibrium bond lengths r(C-C) and r(C-X) (in Å). From the frequency calculation, identify the stretching vibrations: ν₁ (the C-C stretch) and ν₃ (the C-X stretch), both in cm⁻¹. For the bending mode ν₂, the Renner–Teller effect splits the doubly degenerate mode into two non-degenerate components; report their arithmetic average as ν₂_avg (in cm⁻¹). Collect all results into a structured JSON file, as specified in the output contract. An open-source quantum chemistry package that supports B3LYP/aug-cc-pVTZ (e.g., Psi4) can be used.

## Reproduction target
Compute, via DFT at the B3LYP/aug-cc-pVTZ level, the equilibrium bond lengths and harmonic vibrational frequencies of the linear CCP and CCAs radicals. Provide the results for both the ¹²C¹²C and ¹³C¹³C isotopomers. The output must be a single JSON file with the keys "CCP_12C12CP", "CCP_13C13CP", "CCAs_12C12CAs", and "CCAs_13C13CAs". For each species report the stretching frequencies ν₁ and ν₃ (in cm⁻¹), the average bending frequency ν₂_avg (in cm⁻¹), and the bond lengths r_CC and r_CX (in Å). The JSON schema is detailed in the output contract.

## Assets

- Psi4 quantum chemistry package: https://psicode.org/

## Workflow steps

### Step 1: DFT geometry optimization and harmonic frequency calculation
- Role: scored (load-bearing)
- Action: Build linear initial geometries for CCP (C-C-P) and CCAs (C-C-As) in the ²Π electronic state. For each species, perform gas-phase geometry optimization and harmonic vibrational frequency calculation at the B3LYP/aug-cc-pVTZ level. Compute properties for both ¹²C¹²C and ¹³C¹³C isotopomers by setting the appropriate atomic masses. Extract equilibrium bond lengths r(C-C) and r(C-X) in Å; harmonic stretching frequencies v₁ (C-C stretch) and v₃ (C-X stretch) in cm⁻¹; for the bending mode v₂, obtain the two Renner–Teller components and report their arithmetic average as v₂_avg in cm⁻¹. Collect all results into a structured JSON file.
- Output file: `/app/outputs/step_01_computed_params.json`
- Format: json
- Contract: A JSON object with top-level keys: "CCP_12C12CP", "CCP_13C13CP", "CCAs_12C12CAs", "CCAs_13C13CAs". Each value is an object with numeric fields: "v1" (cm⁻¹), "v2_avg" (cm⁻¹), "v3" (cm⁻¹), "r_CC" (Å), "r_CX" (Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_computed_params.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_computed_params.json
- path: `/app/outputs/step_01_computed_params.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed ground-state parameters (vibrational frequencies and bond lengths) for CCP and CCAs isotopomers.
- schema:
  - `type`: object
  - `properties`:
    - `CCP_12C12CP`:
      - `type`: object
      - `properties`:
        - `v1`:
          - `type`: number
          - `units`: cm^-1
        - `v2_avg`:
          - `type`: number
          - `units`: cm^-1
        - `v3`:
          - `type`: number
          - `units`: cm^-1
        - `r_CC`:
          - `type`: number
          - `units`: Å
        - `r_CX`:
          - `type`: number
          - `units`: Å
      - `required`: `v1`, `v2_avg`, `v3`, `r_CC`, `r_CX`
    - `CCP_13C13CP`:
      - `type`: object
      - `properties`:
        - `v1`:
          - `type`: number
          - `units`: cm^-1
        - `v2_avg`:
          - `type`: number
          - `units`: cm^-1
        - `v3`:
          - `type`: number
          - `units`: cm^-1
        - `r_CC`:
          - `type`: number
          - `units`: Å
        - `r_CX`:
          - `type`: number
          - `units`: Å
      - `required`: `v1`, `v2_avg`, `v3`, `r_CC`, `r_CX`
    - `CCAs_12C12CAs`:
      - `type`: object
      - `properties`:
        - `v1`:
          - `type`: number
          - `units`: cm^-1
        - `v2_avg`:
          - `type`: number
          - `units`: cm^-1
        - `v3`:
          - `type`: number
          - `units`: cm^-1
        - `r_CC`:
          - `type`: number
          - `units`: Å
        - `r_CX`:
          - `type`: number
          - `units`: Å
      - `required`: `v1`, `v2_avg`, `v3`, `r_CC`, `r_CX`
    - `CCAs_13C13CAs`:
      - `type`: object
      - `properties`:
        - `v1`:
          - `type`: number
          - `units`: cm^-1
        - `v2_avg`:
          - `type`: number
          - `units`: cm^-1
        - `v3`:
          - `type`: number
          - `units`: cm^-1
        - `r_CC`:
          - `type`: number
          - `units`: Å
        - `r_CX`:
          - `type`: number
          - `units`: Å
      - `required`: `v1`, `v2_avg`, `v3`, `r_CC`, `r_CX`
  - `required`: `CCP_12C12CP`, `CCP_13C13CP`, `CCAs_12C12CAs`, `CCAs_13C13CAs`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_computed_params.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "CCP_12C12CP": {
            "type": "object",
            "properties": {
              "v1": {
                "type": "number",
                "units": "cm^-1"
              },
              "v2_avg": {
                "type": "number",
                "units": "cm^-1"
              },
              "v3": {
                "type": "number",
                "units": "cm^-1"
              },
              "r_CC": {
                "type": "number",
                "units": "Å"
              },
              "r_CX": {
                "type": "number",
                "units": "Å"
              }
            },
            "required": [
              "v1",
              "v2_avg",
              "v3",
              "r_CC",
              "r_CX"
            ]
          },
          "CCP_13C13CP": {
            "type": "object",
            "properties": {
              "v1": {
                "type": "number",
                "units": "cm^-1"
              },
              "v2_avg": {
                "type": "number",
                "units": "cm^-1"
              },
              "v3": {
                "type": "number",
                "units": "cm^-1"
              },
              "r_CC": {
                "type": "number",
                "units": "Å"
              },
              "r_CX": {
                "type": "number",
                "units": "Å"
              }
            },
            "required": [
              "v1",
              "v2_avg",
              "v3",
              "r_CC",
              "r_CX"
            ]
          },
          "CCAs_12C12CAs": {
            "type": "object",
            "properties": {
              "v1": {
                "type": "number",
                "units": "cm^-1"
              },
              "v2_avg": {
                "type": "number",
                "units": "cm^-1"
              },
              "v3": {
                "type": "number",
                "units": "cm^-1"
              },
              "r_CC": {
                "type": "number",
                "units": "Å"
              },
              "r_CX": {
                "type": "number",
                "units": "Å"
              }
            },
            "required": [
              "v1",
              "v2_avg",
              "v3",
              "r_CC",
              "r_CX"
            ]
          },
          "CCAs_13C13CAs": {
            "type": "object",
            "properties": {
              "v1": {
                "type": "number",
                "units": "cm^-1"
              },
              "v2_avg": {
                "type": "number",
                "units": "cm^-1"
              },
              "v3": {
                "type": "number",
                "units": "cm^-1"
              },
              "r_CC": {
                "type": "number",
                "units": "Å"
              },
              "r_CX": {
                "type": "number",
                "units": "Å"
              }
            },
            "required": [
              "v1",
              "v2_avg",
              "v3",
              "r_CC",
              "r_CX"
            ]
          }
        },
        "required": [
          "CCP_12C12CP",
          "CCP_13C13CP",
          "CCAs_12C12CAs",
          "CCAs_13C13CAs"
        ]
      },
      "description": "Computed ground-state parameters (vibrational frequencies and bond lengths) for CCP and CCAs isotopomers."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your output file and compare each reported value to reference values derived from the original study. Each numerical field is scored individually based on how closely it matches the reference, using tolerances that account for legitimate spread between different implementations and computational settings. The final reward is a weighted combination of these comparisons. A correct re‑run that arrives at values through the specified procedure will score highly, while merely guessing or fabricating numbers will not.
