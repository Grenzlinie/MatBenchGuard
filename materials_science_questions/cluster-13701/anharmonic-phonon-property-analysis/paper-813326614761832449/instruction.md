# DFPT phonon frequencies of CoSb₂

## Problem background
CoSb₂ is a semiconductor with an arsenopyrite crystal structure (space group P2₁/c). It serves as a prototype for many transition-metal pnictides and is closely related to the Kondo-like semiconductor FeSb₂. Understanding its phonon properties is important for interpreting transport, thermoelectric behaviour, and the role of phonons in the Fe₁₋ₓCoₓSb₂ alloy system. At the zone centre, group theory predicts 18 Raman-active phonon modes (9 A_g and 9 B_g). These modes have been measured experimentally by polarized Raman spectroscopy on single crystals. This task asks you to reproduce the first-principles lattice dynamics calculation that yields the theoretical Raman-active phonon frequencies and provides a basis for interpreting the experimental spectra.

## Approach
The calculation uses density functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO. The electron exchange and correlation are treated within the local density approximation (LDA) using the Perdew–Zunger parametrization. Ultrasoft pseudopotentials describe the valence electrons of Co (4s¹3d⁸4p⁰) and Sb (5s²5p³). The calculation takes as input the experimentally determined monoclinic unit cell with Co and Sb atoms occupying 4e Wyckoff positions. After obtaining the self-consistent electronic ground state, the dynamical matrix is computed on a Monkhorst–Pack k‑point grid, and the phonon frequencies and eigenvectors at the Γ point are obtained. The symmetry of each eigenmode is then identified, allowing the Raman-active A_g and B_g modes to be separated from the infrared-active A_u and B_u modes. The predicted frequencies for all 18 Raman-active modes (9 A_g and 9 B_g) are then extracted.

## Reproduction target
Perform a DFPT calculation for CoSb₂ with the protocol described in the workflow step and produce a JSON file containing the predicted Γ‑point phonon frequencies for the nine A_g and nine B_g symmetry Raman-active modes. All 18 frequencies must be reported, even if some of them have not been observed experimentally. The output file must follow the exact format and schema specified in the workflow step and the output contract below.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Co ultrasoft pseudopotential (4s¹ 3d⁸ 4p⁰): https://www.quantum-espresso.org/pseudopotentials
- Sb ultrasoft pseudopotential (5s² 5p³): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: DFPT phonon calculation
- Role: scored (load-bearing)
- Action: Perform a DFPT calculation for CoSb₂ using Quantum ESPRESSO with the experimental monoclinic crystal structure (space group P2₁/c, a=0.65051 nm, b=0.63833 nm, c=0.65410 nm, β=117.65°, all atoms in 4e Wyckoff positions). Use the LDA functional (Perdew–Zunger) and ultrasoft pseudopotentials for Co and Sb. Compute phonon frequencies at the Γ point, identify Raman‑active modes (A_g and B_g symmetries), and output the predicted frequencies for all 18 Raman‑active modes (9 A_g and 9 B_g) as JSON.
- Output file: `/app/outputs/calculated_raman_frequencies.json`
- Format: json
- Contract: A JSON object with two arrays: 'ag_modes' (9 entries) and 'bg_modes' (9 entries). Each entry is an object with 'label' (string, e.g. 'A_g^1') and 'frequency' (number, the calculated energy in cm⁻¹).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/calculated_raman_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### calculated_raman_frequencies.json
- path: `/app/outputs/calculated_raman_frequencies.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The agent's computed Raman‑active phonon frequencies. The hidden checker extracts the 16 experimentally observed modes and computes the mean absolute error (MAE) against hidden experimental values.
- schema:
  - `type`: object
  - `required`:
    - `ag_modes`: array of 9 objects
    - `bg_modes`: array of 9 objects
  - `items`:
    - `label`: string
    - `frequency`: number
  - `units`:
    - `frequency`: cm⁻¹
  - `description`: Both arrays must contain 9 entries each. Each entry has a 'label' (string, e.g. 'A_g^1', 'B_g^1') and a 'frequency' (float, the calculated Γ‑point phonon energy in cm⁻¹). All 18 entries must be present.

Notes: Only the zero‑temperature DFPT calculation is scored. Temperature‑dependent anharmonic fitting is excluded per the task scope. The agent must install Quantum ESPRESSO and obtain pseudopotentials; the DFPT run may be computationally intensive but is feasible.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "calculated_raman_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "ag_modes": "array of 9 objects",
          "bg_modes": "array of 9 objects"
        },
        "items": {
          "label": "string",
          "frequency": "number"
        },
        "units": {
          "frequency": "cm⁻¹"
        },
        "description": "Both arrays must contain 9 entries each. Each entry has a 'label' (string, e.g. 'A_g^1', 'B_g^1') and a 'frequency' (float, the calculated Γ‑point phonon energy in cm⁻¹). All 18 entries must be present."
      },
      "description": "The agent's computed Raman‑active phonon frequencies. The hidden checker extracts the 16 experimentally observed modes and computes the mean absolute error (MAE) against hidden experimental values."
    }
  ],
  "notes": "Only the zero‑temperature DFPT calculation is scored. Temperature‑dependent anharmonic fitting is excluded per the task scope. The agent must install Quantum ESPRESSO and obtain pseudopotentials; the DFPT run may be computationally intensive but is feasible."
}
```

## How you are scored
A hidden verifier will read your `calculated_raman_frequencies.json` file. It will extract the frequencies you computed for those Raman-active modes that have been experimentally observed and compare them, mode by mode, to a hidden set of experimentally measured reference values. The verifier will compute the mean absolute error (MAE) between your computed frequencies and the hidden experimental values. Your reward is based on how small this MAE is: a smaller error yields a higher reward. Reporting a complete set of 18 modes with correct mode assignments is necessary, because missing or mislabelled modes reduce the proportion of modes that can be scored. The reward is designed so that improving the accuracy of your calculation always increases your score — you are never penalized for computing a frequency that is closer to the experimental reference than the threshold that defines full credit. You must follow the workflow step exactly and produce the required output file; no other outputs are scored.
