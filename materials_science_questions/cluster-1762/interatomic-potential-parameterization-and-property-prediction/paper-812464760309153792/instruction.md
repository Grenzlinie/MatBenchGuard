# Raman-active phonon modes of La4BaCu5O13 from shell-model lattice dynamics

## Problem background
La₄BaCu₅O₁₃ is a perovskite-like layered copper oxide with tetragonal P4/m symmetry. Its structure comprises corner-sharing CuO₅ pyramids and CuO₆ octahedra, with La and Ba atoms occupying ordered sites. The Raman-active phonon modes of this compound—10 A_g, 10 B_g, and 5 E_g modes—provide information about the vibrational properties and the atomic contributions to each mode. The goal here is to compute the Γ‑point phonon frequencies and identify the dominant atoms for all 25 Raman‑active modes using a shell-model lattice dynamical calculation.

## Approach
The shell model describes ions as cores coupled to charged shells to account for polarizability. Interatomic interactions are treated with long-range Coulomb potentials (evaluated via Ewald summation) and short-range Born–Mayer–Buckingham repulsive potentials. The model parameters—ion charges, shell charges, anisotropic polarizabilities, and the Born–Mayer–Buckingham a, b, c constants for each ion pair—are provided explicitly in the task assets. The crystal structure (space group P4/m, lattice constants a = 8.6475 Å, c = 3.8594 Å, and atomic positions reported by Michel et al., 1987) is also supplied.

Using these inputs, implement the shell model and compute the complete Γ‑point phonon spectrum. From the eigenvectors determine the three most dominant atoms (by displacement amplitude) for each of the 10 A_g, 10 B_g, and 5 E_g modes. The final output is a JSON file containing the computed frequencies (in cm⁻¹) and the dominant atoms for all 25 modes, ordered by decreasing frequency within each symmetry block.

## Reproduction target
Produce the file `/app/outputs/computed_phonon_modes.json`. This file must contain exactly 25 objects—one for each Raman‑active mode—with the following structure per mode: `symmetry` (one of `"Ag"`, `"Bg"`, `"Eg"`), `computed_frequency` (the Γ‑point phonon frequency in cm⁻¹), and `dominant_atoms` (a list of up to three atom labels, e.g., `["O5"]`, indicating the atoms that contribute most to the eigenvector of that mode). The modes must be grouped by symmetry and ordered by decreasing computed frequency within each group (A_g first, then B_g, then E_g).

## Assets

- Crystal structure of La4BaCu5O13 (Michel et al. 1987): 10.1016/0022-4596(87)90105-5
- Shell model parameters (Table 3 of the paper)
- Lattice dynamics code/library

## Workflow steps

### Step 1: Compute Raman-active phonon frequencies and eigenvectors
- Role: scored (load-bearing)
- Action: Implement the shell model for La4BaCu5O13 using the given crystal structure and the Born-Mayer-Buckingham parameters (Table 3) together with core-shell charges and anisotropic polarizabilities. Compute Γ-point phonon eigenfrequencies and eigenvectors. From the eigenvectors, for each of the 10 A_g, 10 B_g, and 5 E_g Raman-active modes, identify the three most dominant atoms by eigenvector amplitude. Output the frequencies and dominant atoms in the JSON file.
- Output file: `/app/outputs/computed_phonon_modes.json`
- Format: json
- Contract: A JSON array of exactly 25 objects, ordered by decreasing computed_frequency within each symmetry block (Ag first, then Bg, then Eg). Each object has keys: 'symmetry' (one of 'Ag','Bg','Eg'), 'computed_frequency' (float in cm⁻¹), 'dominant_atoms' (list of strings, up to 3 atoms, e.g. ['O5']).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_phonon_modes.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_phonon_modes.json
- path: `/app/outputs/computed_phonon_modes.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed phonon frequencies and dominant atomic contributors for all Raman-active modes. The checker will compare the computed frequencies against hidden experimental reference frequencies (Table 2) via mean absolute error, and verify that the dominant atoms match the paper's explicit assignments for 12 key modes.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `symmetry`, `computed_frequency`, `dominant_atoms`
    - `properties`:
      - `symmetry`:
        - `type`: string
        - `enum`: `Ag`, `Bg`, `Eg`
      - `computed_frequency`:
        - `type`: number
        - `unit`: cm^-1
      - `dominant_atoms`:
        - `type`: array
        - `items`:
          - `type`: string
        - `maxItems`: 3
  - `minItems`: 25
  - `maxItems`: 25

Notes: The experimental Raman frequencies and exact assignment mapping are hidden and used solely by the checker. The agent must not access the paper's Table 2 or the reference values during the task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_phonon_modes.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "symmetry",
            "computed_frequency",
            "dominant_atoms"
          ],
          "properties": {
            "symmetry": {
              "type": "string",
              "enum": [
                "Ag",
                "Bg",
                "Eg"
              ]
            },
            "computed_frequency": {
              "type": "number",
              "unit": "cm^-1"
            },
            "dominant_atoms": {
              "type": "array",
              "items": {
                "type": "string"
              },
              "maxItems": 3
            }
          }
        },
        "minItems": 25,
        "maxItems": 25
      },
      "description": "Computed phonon frequencies and dominant atomic contributors for all Raman-active modes. The checker will compare the computed frequencies against hidden experimental reference frequencies (Table 2) via mean absolute error, and verify that the dominant atoms match the paper's explicit assignments for 12 key modes."
    }
  ],
  "notes": "The experimental Raman frequencies and exact assignment mapping are hidden and used solely by the checker. The agent must not access the paper's Table 2 or the reference values during the task."
}
```

## How you are scored
Your output is evaluated by a hidden verifier that compares your computed results to a set of reference values.

- **Frequency accuracy**: The verifier computes the mean absolute error (MAE) between your `computed_frequency` values and the hidden reference frequencies. Full credit is earned when the MAE is at or below a hidden tolerance; credit decreases as the error increases beyond that threshold.
- **Assignment accuracy**: For a subset of modes whose dominant atomic displacements are well established, the verifier compares your `dominant_atoms` list against a hidden set of expected matches. A higher number of correct matches yields more credit.

The two components are combined into a single final reward between 0 and 1. Only the verifier has access to the reference frequencies and expected assignments—do not attempt to retrieve them from any external source.
