# DFT functional comparison for P(OH)3 isomer energetics

## Problem background
Phosphorous acid, P(OH)₃, can adopt several structural isomers: a C₁ low‑symmetry form, a Cₛ form, and the previously known C₃ symmetric structure. Close‑lying minima and low interconversion barriers make the ordering extremely sensitive to the level of theory and zero‑point energy corrections. This task investigates the relative energetic ordering of these isomers and the heights of the barriers that separate them, using a reference high‑level coupled‑cluster method to benchmark two popular density‑functional approximations, B3PW91 and B3LYP.

## Approach
The computational strategy follows well‑established quantum‑chemistry protocols. First, perform full geometry optimizations for the five stationary points – the C₁, Cₛ, and C₃ minima and the transition states TS_C₁-Cₛ and TS_Cₛ-C₃ – at three levels of theory: B3PW91, B3LYP, and MP2, each with the augmented correlation‑consistent polarized valence triple‑ζ basis set (aug‑cc‑pVTZ). From the optimized structures, calculate harmonic vibrational frequencies at the MP2/aug‑cc‑pVTZ level; extract the zero‑point energies (ZPE) and confirm that each transition state possesses exactly one imaginary frequency. To obtain a high‑accuracy reference, carry out single‑point energy calculations at the CCSD(T)/aug‑cc‑pVTZ level using the MP2‑optimized geometries. Finally, from the electronic and ZPE‑corrected energies, compute the energy differences (using the C₁ minimum as the zero reference) and barrier heights for all four methods, both with and without ZPE. The resulting data set will allow a direct comparison of the B3PW91 and B3LYP functionals against the CCSD(T) benchmark.

## Reproduction target
Compute, for each of the five structures (C₁, Cₛ, C₃, TS_C₁-Cₛ, TS_Cₛ-C₃) and for each method (B3PW91, B3LYP, MP2, CCSD(T)), the relevant energy differences in kcal·mol⁻¹:

- The energies of Cₛ and C₃ relative to C₁ (C₁ = 0 kcal·mol⁻¹).
- The barrier heights of TS_C₁-Cₛ and TS_Cₛ-C₃ (reference the lower of the two connected minima for each TS).

All quantities must be reported with and without zero‑point energy corrections. Pack these results into a single JSON file `/app/outputs/relative_energies_and_barriers.json` according to the schema described in the Output Contract. The primary goal is to produce reliable CCSD(T) reference values and to determine, from the computed values, which density functional (B3PW91 or B3LYP) yields smaller deviations from the CCSD(T) results.

## Assets

- PySCF (open-source quantum chemistry package): pyscf

## Workflow steps

### Step 1: Geometry optimization of stationary points
- Role: process
- Action: Perform geometry optimizations for the five stationary points (C1, Cs, C3 minima and the transition states TS_C1_Cs, TS_Cs_C3) of P(OH)3 at the B3PW91/AVTZ, B3LYP/AVTZ, and MP2/AVTZ levels of theory using an open-source quantum chemistry package. For transition states, use a saddle-point search algorithm and verify the presence of a single imaginary frequency.
- Evidence: `/app/outputs/geometries.log`

### Step 2: Harmonic vibrational frequency calculation and ZPE extraction
- Role: process
- Action: Calculate harmonic vibrational frequencies for all optimized structures at the MP2/AVTZ level. Extract zero-point energies (ZPE) from the harmonic frequencies. Verify that the transition states have exactly one imaginary frequency.
- Evidence: `/app/outputs/frequencies.log`

### Step 3: CCSD(T) single-point energy calculation
- Role: process
- Action: Perform single-point energy calculations at the CCSD(T)/aug-cc-pVTZ level using the MP2/AVTZ optimized geometries. Record total electronic energies.
- Evidence: `/app/outputs/ccsd_t_energies.log`

### Step 4: Compute relative energies and barriers
- Role: scored (load-bearing)
- Action: Using the electronic energies from all methods (B3PW91, B3LYP, MP2, CCSD(T)) and the ZPE corrections, compute the relative energies (C1 as reference) for Cs and C3, and the barrier heights for TS_C1_Cs and TS_Cs_C3, both with and without ZPE. Output the results in a structured JSON file as specified.
- Output file: `/app/outputs/relative_energies_and_barriers.json`
- Format: json
- Contract: {"results": [{"structure": "string", "method": "string", "basis": "string", "zpe_corrected": "boolean", "value": "float (kcal/mol)"}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies_and_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies_and_barriers.json
- path: `/app/outputs/relative_energies_and_barriers.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed relative energies (with respect to C1 isomer) and barrier heights for P(OH)3 isomers at the B3PW91/AVTZ, B3LYP/AVTZ, MP2/AVTZ, and CCSD(T)/AVTZ levels, both with and without ZPE corrections.
- schema:
  - `type`: object
  - `required`: `results`
  - `properties`:
    - `results`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `structure`, `method`, `basis`, `zpe_corrected`, `value`
        - `properties`:
          - `structure`:
            - `type`: string
            - `enum`: `C1`, `Cs`, `C3`, `TS_C1_Cs`, `TS_Cs_C3`
          - `method`:
            - `type`: string
            - `enum`: `B3PW91`, `B3LYP`, `MP2`, `CCSD(T)`
          - `basis`:
            - `type`: string
            - `const`: AVTZ
          - `zpe_corrected`:
            - `type`: boolean
          - `value`:
            - `type`: number
            - `unit`: kcal/mol

Notes: Only AVTZ results are scored. The agent must compute quantities for all five structures and four methods, with and without ZPE. The checker compares individual values to reference data, checks the sign of the Cs relative energy without ZPE for different methods, and verifies that B3PW91’s mean absolute deviation from CCSD(T) is smaller than B3LYP’s.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies_and_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "results"
        ],
        "properties": {
          "results": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "structure",
                "method",
                "basis",
                "zpe_corrected",
                "value"
              ],
              "properties": {
                "structure": {
                  "type": "string",
                  "enum": [
                    "C1",
                    "Cs",
                    "C3",
                    "TS_C1_Cs",
                    "TS_Cs_C3"
                  ]
                },
                "method": {
                  "type": "string",
                  "enum": [
                    "B3PW91",
                    "B3LYP",
                    "MP2",
                    "CCSD(T)"
                  ]
                },
                "basis": {
                  "type": "string",
                  "const": "AVTZ"
                },
                "zpe_corrected": {
                  "type": "boolean"
                },
                "value": {
                  "type": "number",
                  "unit": "kcal/mol"
                }
              }
            }
          }
        }
      },
      "description": "Computed relative energies (with respect to C1 isomer) and barrier heights for P(OH)3 isomers at the B3PW91/AVTZ, B3LYP/AVTZ, MP2/AVTZ, and CCSD(T)/AVTZ levels, both with and without ZPE corrections."
    }
  ],
  "notes": "Only AVTZ results are scored. The agent must compute quantities for all five structures and four methods, with and without ZPE. The checker compares individual values to reference data, checks the sign of the Cs relative energy without ZPE for different methods, and verifies that B3PW91’s mean absolute deviation from CCSD(T) is smaller than B3LYP’s."
}
```

## How you are scored
A hidden verifier will parse your `relative_energies_and_barriers.json` and compare every reported value to a set of reference numbers using a tolerance‑based check. It will also verify qualitative aspects: the sign of the Cₛ energy difference (without ZPE) for each method, and the overall trend that the B3PW91 energies should lie closer to the CCSD(T) reference than the B3LYP energies. The verifier computes a weighted score where the greatest weight is placed on the accuracy of the CCSD(T) quantities, followed by the correct qualitative trends and the functional ranking. Submitting figures that happen to match the hidden gold without having executed the prescribed computational workflow will not receive full credit – the scoring expects values derived from the actual geometry optimizations, frequency calculations, and single‑point computations.
