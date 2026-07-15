# Phonon dynamical stability of Na2Ti2As2O

## Problem background
The compound Na2Ti2As2O undergoes a structural phase transition around 150 K that breaks the four-fold in-plane symmetry observed at room temperature. First-principles phonon calculations play a key role in understanding this transition: the normal-state phonon spectrum can reveal a dynamical instability through the presence of imaginary phonon modes (negative frequencies). The key computational question is whether the high-temperature phase (space group I4/mmm) is dynamically stable, and whether any unstable modes are consistent with a structural distortion.

## Approach
First-principles density-functional theory (DFT) is used to compute the phonon properties of Na2Ti2As2O in its high-symmetry structure. The workflow consists of three stages. First, the crystal structure (I4/mmm, with published lattice parameters and atomic coordinates) is relaxed to obtain the ground-state geometry. Second, phonon frequencies at the Brillouin-zone centre (Γ) are computed using density-functional perturbation theory (DFPT) or the finite-displacement method; symmetry analysis then identifies the Raman-active A1g and Eg modes. Third, the full phonon band structure is calculated along high-symmetry lines that include Σ(½,0,0), Σ₁(½,0,½) and L(½,½,0), and the most negative (imaginary) phonon frequency is extracted. The calculations rely on open-source tools: Quantum ESPRESSO for DFT (with a suitable exchange-correlation functional such as GGA-PBE) and Phonopy for phonon post-processing. Standard pseudopotentials for Ti, Na, As, and O are used.

## Reproduction target
Produce two quantitative outputs:

1. **Γ‑point Raman‑active mode frequencies** – The phonon frequencies (in cm⁻¹) of the four Raman‑active modes (A1g(1), A1g(2), Eg(1), Eg(2)) in the high‑temperature I4/mmm phase, written to `gamma_frequencies.json`.

2. **Phonon dispersion minimum** – The full phonon dispersion along high‑symmetry lines that include Σ(½,0,0), Σ₁(½,0,½) and L(½,½,0). From it, report the minimum (most negative) phonon frequency, along with the corresponding q‑point and its label, written to `minimum_phonon_frequency.json`.

The scoring evaluates how well your computed Γ‑point frequencies agree with known experimental Raman mode frequencies for this material, and whether your dispersion confirms the presence of imaginary modes (negative frequencies) that signal a lattice instability.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Pseudopotentials for Ti, Na, As, O: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: DFT structural relaxation
- Role: process
- Action: Set up the Na2Ti2As2O crystal structure using the published lattice parameters (a=b=4.124 Å, c=15.84 Å, space group I4/mmm, atomic positions from Adam & Schuster 1990). Perform a full structural relaxation (cell parameters and atomic coordinates) with Quantum ESPRESSO using a suitable exchange-correlation functional (e.g., GGA-PBE). This step is REQUIRED to obtain the ground-state geometry for subsequent phonon calculations.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Γ-point Raman-active mode frequencies
- Role: scored (load-bearing)
- Action: Using the relaxed structure from step1, compute the phonon frequencies at the Brillouin-zone centre (Γ) with Phonopy (DFPT or finite-displacement via Quantum ESPRESSO). Identify the Raman-active A1g(1), A1g(2), Eg(1), and Eg(2) modes by symmetry analysis, and write their frequencies (in cm⁻¹) to the specified JSON file.
- Output file: `/app/outputs/gamma_frequencies.json`
- Format: json
- Contract: { "A1g_1": <float>, "A1g_2": <float>, "Eg_1": <float>, "Eg_2": <float> }
- Scoring: scored by hidden verifier

### Step 3: Phonon dispersion and minimum frequency
- Role: scored
- Action: Using the same relaxed structure and Phonopy, compute the full phonon band structure along high-symmetry lines that include Σ(½,0,0), Σ₁(½,0,½) and L(½,½,0). From the dispersion, extract the most negative (imaginary) phonon frequency and the corresponding q-point and its label. Write the result to the specified JSON file.
- Output file: `/app/outputs/minimum_phonon_frequency.json`
- Format: json
- Contract: { "min_frequency_cm-1": <float>, "q_point": [<float>,<float>,<float>], "q_label": "<string>" }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gamma_frequencies.json`
- `/app/outputs/minimum_phonon_frequency.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gamma_frequencies.json
- path: `/app/outputs/gamma_frequencies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed Γ-point phonon frequencies for the four Raman-active modes. The checker will compare each value to a hidden reference (the experimental Raman frequencies) within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `A1g_1`: float
    - `A1g_2`: float
    - `Eg_1`: float
    - `Eg_2`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `A1g_1`: cm⁻¹
    - `A1g_2`: cm⁻¹
    - `Eg_1`: cm⁻¹
    - `Eg_2`: cm⁻¹

### minimum_phonon_frequency.json
- path: `/app/outputs/minimum_phonon_frequency.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Most negative phonon frequency from the dispersion, indicating the presence of imaginary modes. The checker verifies that min_frequency_cm-1 ≤ −10 cm⁻¹ (threshold-or-better). q_point and q_label are validated for shape but carry negligible weight.
- schema:
  - `type`: object
  - `required`:
    - `min_frequency_cm-1`: float
    - `q_point`: array of 3 floats
    - `q_label`: string
  - `items`: object
  - `required_columns`:
  - `units`:
    - `min_frequency_cm-1`: cm⁻¹

Notes: The checker uses the hidden paper-reported experimental Raman frequencies for the Γ-point modes and a −10 cm⁻¹ threshold for the minimum phonon frequency. The exact DFT protocol (cutoff, k-mesh, pseudopotential choice) is left to the solver; the scoring tolerances account for method dependence.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gamma_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "A1g_1": "float",
          "A1g_2": "float",
          "Eg_1": "float",
          "Eg_2": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "A1g_1": "cm⁻¹",
          "A1g_2": "cm⁻¹",
          "Eg_1": "cm⁻¹",
          "Eg_2": "cm⁻¹"
        }
      },
      "description": "Computed Γ-point phonon frequencies for the four Raman-active modes. The checker will compare each value to a hidden reference (the experimental Raman frequencies) within a tolerance."
    },
    {
      "file": "minimum_phonon_frequency.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "min_frequency_cm-1": "float",
          "q_point": "array of 3 floats",
          "q_label": "string"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "min_frequency_cm-1": "cm⁻¹"
        }
      },
      "description": "Most negative phonon frequency from the dispersion, indicating the presence of imaginary modes. The checker verifies that min_frequency_cm-1 ≤ −10 cm⁻¹ (threshold-or-better). q_point and q_label are validated for shape but carry negligible weight."
    }
  ],
  "notes": "The checker uses the hidden paper-reported experimental Raman frequencies for the Γ-point modes and a −10 cm⁻¹ threshold for the minimum phonon frequency. The exact DFT protocol (cutoff, k-mesh, pseudopotential choice) is left to the solver; the scoring tolerances account for method dependence."
}
```

## How you are scored
A hidden verifier independently checks your submitted artifacts. For `gamma_frequencies.json`, it compares each of your four mode frequencies to reference values (the experimentally measured Raman frequencies) and awards credit when they fall within an acceptable tolerance. For `minimum_phonon_frequency.json`, it verifies that the reported `min_frequency_cm-1` is negative and meets a stability criterion, and that the q‑point and label are well‑formed. The two scores are combined with appropriate weights into a final reward between 0 and 1. Simply reporting expected numbers without executing the DFT workflow will not succeed, because the tolerance and the reference values are hidden from you.
