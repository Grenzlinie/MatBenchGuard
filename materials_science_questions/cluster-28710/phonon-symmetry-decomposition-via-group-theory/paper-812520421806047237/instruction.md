# Group-theoretical mode classification and DFT phonon calculation for Y2Mo4O15

## Problem background
Y2Mo4O15 is a molybdate crystal being investigated for Raman laser applications. Its Raman activity is determined by its lattice vibrational properties, which can be analyzed through group-theoretical mode classification and first-principles phonon calculations. This task reproduces the computational workflow that predicts the crystal's zone-center vibrational mode symmetry counts and the highest optical phonon frequency, both of which are critical for understanding its Raman scattering performance.

## Approach
The workflow proceeds in two stages. First, perform a group-theoretical decomposition of the lattice vibrations at the Γ point. Using the published crystal structure (space group P2_1/c, point group C2h), determine the irreducible representations (irreps) of all 72 vibrational degrees of freedom. Count the number of infrared-active (A_u, B_u) and Raman-active (A_g, B_g) modes, and identify the acoustic mode irreps. Second, run a density-functional perturbation theory (DFPT) or frozen-phonon calculation with an open-source DFT code and Phonopy to obtain the Γ‑point phonon frequencies and eigenvectors. From these results, extract the frequency spectrum and classify the symmetry of each mode, then identify the irreducible representation of the mode with the highest frequency.

## Reproduction target
Compute from the Y2Mo4O15 crystal structure (CCDC 2027158): (a) the integer counts of infrared-active A_u and B_u modes, and of Raman-active A_g and B_g modes; (b) the array of Γ‑point phonon frequencies (in cm⁻¹) and the symmetry label of the mode with the highest frequency. The group‑theory counts are an exact consequence of the structure; the phonon frequencies reflect the DFT calculation at the Γ point.

## Assets

- Y2Mo4O15 crystal structure CIF: 10.1039/d0ra08609f
- DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: Group-theoretical mode decomposition
- Role: scored
- Action: Using the crystal structure from CCDC 2027158 (space group P2_1/c, point group C2h), perform a group-theoretical analysis to classify the Γ-point vibrational modes. Determine the irreducible representation decomposition: count IR-active (A_u, B_u), Raman-active (A_g, B_g), and acoustic modes. Write the integer counts to a JSON file.
- Output file: `/app/outputs/step_01_group_theory.json`
- Format: json
- Contract: JSON object with keys: 'ir_counts' (object containing 'IR_active' and 'Raman_active', each with integer counts for specific irreps), 'total_modes' (int), 'acoustic_modes' (string).
- Scoring: scored by hidden verifier

### Step 2: DFT phonon calculation at Gamma point
- Role: process
- Action: Set up and run a DFT phonon calculation for Y2Mo4O15 at the Γ-point using an open-source DFT code and PHONOPY. A 2×2×1 supercell is suggested; choose appropriate convergence parameters. This step generates phonon frequencies and eigenvectors needed for the next scored step.
- Evidence: `/app/outputs/phonon_calculation.log`

### Step 3: Extract phonon frequencies and identify highest mode
- Role: scored (load-bearing)
- Action: Parse the DFT phonon output to obtain the Γ-point phonon frequencies (in cm⁻¹). Determine the irreducible representation of each mode, or at least identify the symmetry of the mode with the highest frequency. Write the frequencies, the maximum frequency, and its symmetry label to a JSON file.
- Output file: `/app/outputs/step_02_phonon_gamma.json`
- Format: json
- Contract: JSON object with keys: 'gamma_point_frequencies' (array of floats, cm⁻¹), 'max_frequency' (float), 'max_frequency_mode' (string, e.g., "B_g").
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_group_theory.json`
- `/app/outputs/step_02_phonon_gamma.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_group_theory.json
- path: `/app/outputs/step_01_group_theory.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Counts of vibrational irreducible representations from group theory.
- schema:
  - `type`: object
  - `required`:
    - `ir_counts`: object
    - `total_modes`: int
    - `acoustic_modes`: string
  - `items`:
    - `ir_counts.IR_active.A_u`: int
    - `ir_counts.IR_active.B_u`: int
    - `ir_counts.Raman_active.A_g`: int
    - `ir_counts.Raman_active.B_g`: int

### step_02_phonon_gamma.json
- path: `/app/outputs/step_02_phonon_gamma.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Γ-point phonon frequencies, maximum frequency, and its irreducible representation label.
- schema:
  - `type`: object
  - `required`:
    - `gamma_point_frequencies`: array of floats
    - `max_frequency`: float
    - `max_frequency_mode`: string

Notes: The group-theory counts are deterministic from the crystal structure and must match exactly. The phonon frequencies depend on the DFT functional and computational settings; a tolerance is applied to the maximum frequency, and the symmetry label is checked exactly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_group_theory.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "ir_counts": "object",
          "total_modes": "int",
          "acoustic_modes": "string"
        },
        "items": {
          "ir_counts.IR_active.A_u": "int",
          "ir_counts.IR_active.B_u": "int",
          "ir_counts.Raman_active.A_g": "int",
          "ir_counts.Raman_active.B_g": "int"
        }
      },
      "description": "Counts of vibrational irreducible representations from group theory."
    },
    {
      "file": "step_02_phonon_gamma.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "gamma_point_frequencies": "array of floats",
          "max_frequency": "float",
          "max_frequency_mode": "string"
        }
      },
      "description": "Γ-point phonon frequencies, maximum frequency, and its irreducible representation label."
    }
  ],
  "notes": "The group-theory counts are deterministic from the crystal structure and must match exactly. The phonon frequencies depend on the DFT functional and computational settings; a tolerance is applied to the maximum frequency, and the symmetry label is checked exactly."
}
```

## How you are scored
Each scored artifact is verified by a hidden checker. For step_01_group_theory.json, the irreducible representation counts are compared to a hidden reference derived from the crystal structure; exact match is expected. For step_02_phonon_gamma.json, the list of frequencies and the highest-frequency mode symmetry are compared to a hidden reference with a tolerance that accounts for normal DFT method variations. The final reward is a weighted combination of the two scores.
