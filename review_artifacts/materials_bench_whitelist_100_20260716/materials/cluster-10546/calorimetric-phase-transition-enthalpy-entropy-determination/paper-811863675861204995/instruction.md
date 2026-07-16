# DFT Vibrational Frequencies of Organic Cation in Hybrid Perovskite

## Problem background
Hybrid organic–inorganic layered perovskites of the form (CH₃–(CH₂)ₙ₋₁–NH₃)₂MnCl₄ exhibit a first‑order solid–solid phase transition associated with a colossal barocaloric effect. The entropy change originates from an order–disorder transformation of the long organic chains. Density functional theory (DFT) calculations of the vibrational frequencies of the (CH₃–(CH₂)₉–NH₃)⁺ cation in its low‑temperature ordered conformer provide a reference for interpreting experimental IR spectra and for determining how each chain component — the NH₃ head, CH₂ body, and CH₃ tail — contributes to the transition. Computing the harmonic vibrational frequencies at the B3LYP/6‑311G* level of theory is therefore a well‑defined computational target that supports the mechanistic understanding of these materials.

## Approach
The computational approach proceeds in three stages. First, the crystal structure of the low‑temperature phase (monoclinic P2₁/c) is obtained from the Cambridge Crystallographic Data Centre (CCDC deposition 2126878), and the atomic coordinates of one isolated (CH₃–(CH₂)₉–NH₃)⁺ organic cation are extracted. Second, a DFT geometry optimization is performed on the isolated cation at the B3LYP/6‑311G* level, starting from the experimental coordinates, to locate an optimized all‑trans rigid conformer. Third, a harmonic vibrational frequency calculation is carried out on the optimized geometry at the same level of theory, and the resulting wavenumbers are scaled by a correction factor of 0.97305. Six specific vibrational modes are then identified and reported: two CH₂ scissoring bands, the NH₃ asymmetric bending band, the C–NH₃⁺ stretching band, the CH₃ symmetric deforming band, and the CH₃ asymmetric stretching band. No comparison to experimental data is performed within this task; the computed wavenumbers are the final deliverable.

## Reproduction target
Produce the corrected harmonic vibrational frequencies (in cm⁻¹) for the (CH₃–(CH₂)₉–NH₃)⁺ organic cation in its low‑temperature (298 K) all‑trans conformation. Use the crystal structure from CCDC deposition 2126878 to obtain the initial atomic coordinates of the cation, perform a DFT geometry optimization at the B3LYP/6‑311G* level, and then run a harmonic frequency calculation at the optimized geometry. Apply the frequency correction factor 0.97305 to all wavenumbers. Identify and report the following modes: CH₂ scissoring (two distinct bands), NH₃ asymmetric bending, C–NH₃⁺ stretching, CH₃ symmetric deforming, and CH₃ asymmetric stretching. Write the six corrected wavenumbers as a JSON file with the exact keys specified in the output contract.

## Assets

- (CH3-(CH2)9-NH3)2MnCl4 low-temperature crystal structure (298 K, monoclinic P21/c): https://www.ccdc.cam.ac.uk/structures/
- DFT package supporting B3LYP/6-311G*: ORCA (open-source) or any equivalent quantum chemistry package

## Workflow steps

### Step 1: Obtain crystal structure and isolate organic cation
- Role: process
- Action: Retrieve the crystal structure from CCDC deposition 2126878 (download the CIF file). Extract the atomic coordinates of one (CH3-(CH2)9-NH3)+ organic cation (all atoms of the chain, excluding the inorganic framework).
- Evidence: `/app/outputs/structure_extraction.log`

### Step 2: DFT geometry optimization (low-temperature conformer)
- Role: process
- Action: Perform a DFT geometry optimization of the isolated organic cation at the B3LYP/6-311G* level of theory. Start from the experimental coordinates to obtain an optimized all‑trans rigid conformer consistent with the low‑temperature phase. Ensure the optimization converges to a stable minimum.
- Evidence: `/app/outputs/optimization.log`

### Step 3: DFT harmonic frequency calculation and mode extraction
- Role: scored (load-bearing)
- Action: Run a harmonic vibrational frequency calculation on the optimized geometry at the B3LYP/6-311G* level. Apply a frequency correction factor of 0.97305. Identify the vibrational modes: (1) CH2 scissoring (two bands), (2) NH3 asymmetric bending, (3) C-NH3+ stretching, (4) CH3 symmetric deforming, (5) CH3 asymmetric stretching. Report their corrected wavenumbers (in cm⁻¹) in a JSON file.
- Output file: `/app/outputs/step_01_vibrational_frequencies.json`
- Format: json
- Contract: {
  "CH2_scissoring_1": <float>,
  "CH2_scissoring_2": <float>,
  "NH3_asymmetric_bending": <float>,
  "C_NH3_stretching": <float>,
  "CH3_symmetric_deforming": <float>,
  "CH3_asymmetric_stretching": <float>
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_vibrational_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_vibrational_frequencies.json
- path: `/app/outputs/step_01_vibrational_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Harmonic vibrational frequencies (cm⁻¹) for selected modes of the low‑temperature organic cation computed at B3LYP/6-311G* with a correction factor of 0.97305.
- schema:
  - `type`: object
  - `required`: `CH2_scissoring_1`, `CH2_scissoring_2`, `NH3_asymmetric_bending`, `C_NH3_stretching`, `CH3_symmetric_deforming`, `CH3_asymmetric_stretching`
  - `properties`:
    - `CH2_scissoring_1`:
      - `type`: number
    - `CH2_scissoring_2`:
      - `type`: number
    - `NH3_asymmetric_bending`:
      - `type`: number
    - `C_NH3_stretching`:
      - `type`: number
    - `CH3_symmetric_deforming`:
      - `type`: number
    - `CH3_asymmetric_stretching`:
      - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_vibrational_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "CH2_scissoring_1",
          "CH2_scissoring_2",
          "NH3_asymmetric_bending",
          "C_NH3_stretching",
          "CH3_symmetric_deforming",
          "CH3_asymmetric_stretching"
        ],
        "properties": {
          "CH2_scissoring_1": {
            "type": "number"
          },
          "CH2_scissoring_2": {
            "type": "number"
          },
          "NH3_asymmetric_bending": {
            "type": "number"
          },
          "C_NH3_stretching": {
            "type": "number"
          },
          "CH3_symmetric_deforming": {
            "type": "number"
          },
          "CH3_asymmetric_stretching": {
            "type": "number"
          }
        }
      },
      "description": "Harmonic vibrational frequencies (cm⁻¹) for selected modes of the low‑temperature organic cation computed at B3LYP/6-311G* with a correction factor of 0.97305."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently checks the reported wavenumbers in the JSON output. The verifier compares each of the six values against a hidden reference. All six modes must fall within an allowed tolerance to earn full credit; missing or incorrect modes reduce the score. The final reward is a combination of the per‑mode checks, with the scored step carrying the full reward weight. The verifier does not re‑run any DFT calculation; it relies solely on the numbers you provide in the output file.
