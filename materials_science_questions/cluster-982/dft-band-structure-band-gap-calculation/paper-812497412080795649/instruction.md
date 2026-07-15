# First-Principles DFT Calculation of Band Gaps, SHG Tensors, and Birefringence for Two Selenite Fluorides

## Problem background
Two noncentrosymmetric selenite fluoride compounds, LiBa3Bi6(SeO3)7F11 (LBBSF) and Ba3Bi6.5(SeO3)7F10.5O0.5 (BBSF), have been reported. Aliovalent cation substitution between them is believed to modulate the layer structure and influence the second-harmonic generation (SHG) efficiency. To understand the structure–property relationship, first‑principles density functional theory (DFT) calculations are needed to compute the electronic band structure, the second‑order nonlinear optical susceptibility, and the optical birefringence for both materials.

## Approach
Start from the published crystal structures of LBBSF and BBSF. Perform plane‑wave pseudopotential DFT calculations using a generalized‑gradient approximation (GGA) functional. For each compound, compute the electronic band structure along the high‑symmetry k‑path of space group P3_1m, extract the uncorrected band gap (valence band maximum to conduction band minimum) in eV, and determine whether the gap is quasi‑direct. Then apply a scissor correction by shifting the conduction band energies by 0.062 eV (LBBSF) and 1.747 eV (BBSF), which correspond to the difference between the experimental band gaps (3.80 eV and 3.56 eV) and the uncorrected GGA gaps. Using the scissor‑corrected eigenvalues, compute the static second‑order nonlinear susceptibility tensor d_ij under Kleinman symmetry and identify the largest tensor component. Finally, compute the refractive index dispersion and report the birefringence Δn = n_o – n_e at a wavelength of 546.1 nm. All results are written to a single JSON output file.

## Reproduction target
Using the crystal structure files for LBBSF (CCDC 2053035) and BBSF (CCDC 2053036) and an open‑source plane‑wave DFT code, reproduce the uncorrected band gap (eV), the band gap type with the k‑point locations of the VBM and CBM, the largest static SHG tensor component (d_element and value in pm/V), and the birefringence at 546.1 nm for both compounds. Report all quantities in JSON format as described in the workflow steps.

## Assets

- Crystal structure of LBBSF (CCDC 2053035): https://www.ccdc.cam.ac.uk/structures/
- Crystal structure of BBSF (CCDC 2053036): https://www.ccdc.cam.ac.uk/structures/
- Quantum ESPRESSO (or equivalent plane-wave DFT code): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Prepare crystal structure inputs
- Role: process
- Action: Download the CIF files for LBBSF (CCDC 2053035) and BBSF (CCDC 2053036) from the Cambridge Structural Database and convert them into the input geometry format required by the chosen plane-wave DFT code.
- Evidence: `/app/outputs/geometry_inputs.log`

### Step 2: DFT SCF and band structure calculations
- Role: process
- Action: For each compound, run self-consistent field (SCF) calculations with a GGA functional and appropriate pseudopotentials, then compute the band structure along the high-symmetry k-path of space group P3_1m. Keep the self-consistent charge density and the Kohn-Sham eigenvalues.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 3: Compute band gaps, SHG tensor, and birefringence
- Role: scored (load-bearing)
- Action: From the DFT results, extract the valence band maximum (VBM) and conduction band minimum (CBM) to obtain the uncorrected band gap in eV and identify whether it is quasi-direct (VBM within ~0.02 eV of the CBM k-point). Next, apply a scissor correction to the conduction bands by shifting them up by 0.062 eV for LBBSF and 1.747 eV for BBSF. Using the scissor‑corrected band structure, compute the static second-order nonlinear susceptibility tensor (d_ij) under Kleinman symmetry and select the largest element (d33 for LBBSF, d22 for BBSF). Compute the refractive index dispersion and report the birefringence Δn = n_o − n_e at 546.1 nm. Write all results to step_01_results.json.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: JSON object with keys 'LBBSF' and 'BBSF'. Each value is an object with fields: 'band_gap_uncorrected_ev' (float, eV), 'band_gap_type' (string), 'cbm_kpoint' (string), 'vbm_kpoint' (string), 'shg_tensor_largest' (object with 'element' string and 'value_pm_per_V' float), 'birefringence_546nm' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Combined results file containing the DFT-computed uncorrected band gap, band gap type with k-point locations, largest static SHG tensor component (Kleinman symmetry), and birefringence at 546.1 nm for both LBBSF and BBSF. The SHG tensor and birefringence are computed after scissor correction.
- schema:
  - `type`: object
  - `required`: `LBBSF`, `BBSF`
  - `properties`:
    - `LBBSF`:
      - `type`: object
      - `required`: `band_gap_uncorrected_ev`, `band_gap_type`, `cbm_kpoint`, `vbm_kpoint`, `shg_tensor_largest`, `birefringence_546nm`
      - `properties`:
        - `band_gap_uncorrected_ev`:
          - `type`: number
          - `unit`: eV
        - `band_gap_type`:
          - `type`: string
        - `cbm_kpoint`:
          - `type`: string
        - `vbm_kpoint`:
          - `type`: string
        - `shg_tensor_largest`:
          - `type`: object
          - `required`: `element`, `value_pm_per_V`
          - `properties`:
            - `element`:
              - `type`: string
            - `value_pm_per_V`:
              - `type`: number
              - `unit`: pm/V
        - `birefringence_546nm`:
          - `type`: number
    - `BBSF`:
      - `type`: object
      - `required`: `band_gap_uncorrected_ev`, `band_gap_type`, `cbm_kpoint`, `vbm_kpoint`, `shg_tensor_largest`, `birefringence_546nm`
      - `properties`:
        - `band_gap_uncorrected_ev`:
          - `type`: number
          - `unit`: eV
        - `band_gap_type`:
          - `type`: string
        - `cbm_kpoint`:
          - `type`: string
        - `vbm_kpoint`:
          - `type`: string
        - `shg_tensor_largest`:
          - `type`: object
          - `required`: `element`, `value_pm_per_V`
          - `properties`:
            - `element`:
              - `type`: string
            - `value_pm_per_V`:
              - `type`: number
              - `unit`: pm/V
        - `birefringence_546nm`:
          - `type`: number

Notes: The reference values for scoring are taken from the paper's reported uncorrected band gaps, SHG tensor components, and birefringence, with tolerances appropriate for DFT method spread. The checker compares each submitted value to the hidden reference under the tolerances declared in the hidden grading spec.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "LBBSF",
          "BBSF"
        ],
        "properties": {
          "LBBSF": {
            "type": "object",
            "required": [
              "band_gap_uncorrected_ev",
              "band_gap_type",
              "cbm_kpoint",
              "vbm_kpoint",
              "shg_tensor_largest",
              "birefringence_546nm"
            ],
            "properties": {
              "band_gap_uncorrected_ev": {
                "type": "number",
                "unit": "eV"
              },
              "band_gap_type": {
                "type": "string"
              },
              "cbm_kpoint": {
                "type": "string"
              },
              "vbm_kpoint": {
                "type": "string"
              },
              "shg_tensor_largest": {
                "type": "object",
                "required": [
                  "element",
                  "value_pm_per_V"
                ],
                "properties": {
                  "element": {
                    "type": "string"
                  },
                  "value_pm_per_V": {
                    "type": "number",
                    "unit": "pm/V"
                  }
                }
              },
              "birefringence_546nm": {
                "type": "number"
              }
            }
          },
          "BBSF": {
            "type": "object",
            "required": [
              "band_gap_uncorrected_ev",
              "band_gap_type",
              "cbm_kpoint",
              "vbm_kpoint",
              "shg_tensor_largest",
              "birefringence_546nm"
            ],
            "properties": {
              "band_gap_uncorrected_ev": {
                "type": "number",
                "unit": "eV"
              },
              "band_gap_type": {
                "type": "string"
              },
              "cbm_kpoint": {
                "type": "string"
              },
              "vbm_kpoint": {
                "type": "string"
              },
              "shg_tensor_largest": {
                "type": "object",
                "required": [
                  "element",
                  "value_pm_per_V"
                ],
                "properties": {
                  "element": {
                    "type": "string"
                  },
                  "value_pm_per_V": {
                    "type": "number",
                    "unit": "pm/V"
                  }
                }
              },
              "birefringence_546nm": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Combined results file containing the DFT-computed uncorrected band gap, band gap type with k-point locations, largest static SHG tensor component (Kleinman symmetry), and birefringence at 546.1 nm for both LBBSF and BBSF. The SHG tensor and birefringence are computed after scissor correction."
    }
  ],
  "notes": "The reference values for scoring are taken from the paper's reported uncorrected band gaps, SHG tensor components, and birefringence, with tolerances appropriate for DFT method spread. The checker compares each submitted value to the hidden reference under the tolerances declared in the hidden grading spec."
}
```

## How you are scored
A hidden verifier reads your submitted step_01_results.json file. It compares the six required quantities (band gap, SHG value, and birefringence for each compound) to reference values obtained from the literature, using tolerances that account for typical DFT implementation spread. The band gap type and the reported k‑point labels must also be correct. Each compound’s three quantities are scored independently, and the final reward is the average across all six checkpoints (each correct checkpoint contributes 1/6).
