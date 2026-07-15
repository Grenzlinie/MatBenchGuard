# First-principles calculation of relaxed structure and IR-active phonon modes of Bi2Ti2O6O'

## Problem background
Bi2Ti2O6O' is a bismuth pyrochlore whose structure is known to deviate from the ideal cubic Fd-3m symmetry, leading to a large dielectric response. Density‑functional theory (DFT) can be used to predict the relaxed ground‑state crystal structure and to compute the vibrational spectrum, providing insight into the origin of the material's enhanced permittivity. The central computational task is to perform a full structural relaxation starting from the ideal pyrochlore configuration, identify the resulting space group, and compute the infrared‑active phonon modes together with their contributions to the dielectric constant.

## Approach
Use first‑principles DFT with a generalised‑gradient approximation (GGA) functional. Begin with the ideal cubic pyrochlore structure (space group Fd‑3m, 88‑atom conventional cell) and relax all atomic positions without symmetry constraints (P1 symmetry). Analyse the relaxed low‑symmetry configuration to detect the approximate space group, then construct the primitive cell of that space group and perform a further relaxation with symmetry constraints. After obtaining the final relaxed structure, carry out a frozen‑phonon calculation at the Γ point to obtain phonon frequencies and eigenvectors. Compute Born effective charges and derive from them the phonon contribution to the dielectric function. Finally, extract the IR‑active modes (A1, B1, B2) and report their frequencies, relative intensities, and dielectric contributions along the respective polarisation axes. An open‑source DFT code (e.g., Quantum ESPRESSO) can be used in place of the proprietary code employed in the original work.

## Reproduction target
Produce the following two artifacts:
1. A CSV file containing the relaxed fractional coordinates of all unique ions in the low‑symmetry primitive cell (labelled Bi(1), Bi(2), Ti(1), Ti(2), O(1)–O(6), O'), ordered as in the published structure listing.
2. A JSON array of all IR‑active phonon modes whose relative intensity I/Imax exceeds 0.10. For each mode, report the irreducible representation (A1, B1, or B2), the frequency in cm⁻¹, the normalised intensity I_Imax (float between 0 and 1), and the contribution ε_p to the diagonal dielectric constant along the mode's polarisation axis.
These results must be obtained by executing the full computational workflow described in the steps; simply quoting published values will not satisfy the task.

## Assets

- Open-source periodic DFT code (e.g., Quantum ESPRESSO, CP2K, ABINIT): quantum-espresso
- Pseudopotentials and basis sets for Bi, Ti, O
- Ideal Fd-3m pyrochlore structure for Bi2Ti2O6O'
- Symmetry analysis tool (e.g., spglib, findsym): https://pypi.org/project/spglib/

## Workflow steps

### Step 1: Unconstrained DFT relaxation of the 88-ion Fd-3m cell
- Role: process
- Action: Starting from the ideal cubic pyrochlore structure (Fd-3m, 88 atoms), perform DFT total-energy minimization without any symmetry constraints using a GGA functional. Allow all atomic positions to relax until forces are converged.
- Evidence: `/app/outputs/p1_relaxation.log`

### Step 2: Symmetry analysis to obtain Pna2_1 primitive cell
- Role: process
- Action: Analyze the relaxed P1 atomic coordinates to identify the space group (should be approximately Pna2_1). Reduce the 88-atom cell to a 44-atom primitive cell with Pna2_1 symmetry. Output the approximate fractional coordinates and lattice vectors for this cell to serve as input for the next step.
- Evidence: `/app/outputs/pna21_primitive_input.txt`

### Step 3: Constrained DFT relaxation of the Pna2_1 structure
- Role: process
- Action: Using the approximate Pna2_1 atomic coordinates from step 2, perform a DFT geometry optimization with Pna2_1 symmetry constraints. Allow both atomic positions and the lattice parameters to relax until forces and stresses are converged.
- Evidence: `/app/outputs/pna21_relaxation.log`

### Step 4: Extract relaxed fractional coordinates
- Role: scored
- Action: From the final relaxed Pna2_1 structure, write the unique fractional coordinates of all atoms (Bi(1), Bi(2), Ti(1), Ti(2), O(1)–O(6), O') to a CSV file. The order and labeling must follow the published unique-ion list. Report coordinates in fractional units relative to the Pna2_1 cell axes (a, b, c).
- Output file: `/app/outputs/Pna2_1_fractional_coordinates.csv`
- Format: csv
- Contract: Columns: atom (string, e.g. 'Bi(1)'), x (float, fractional coordinate), y (float), z (float). The CSV shall contain 11 rows (Bi(1), Bi(2), Ti(1), Ti(2), O(1) through O(6), O').
- Scoring: scored by hidden verifier

### Step 5: Frozen-phonon and dielectric function calculation
- Role: process
- Action: For the relaxed Pna2_1 structure, perform a frozen-phonon calculation at the Γ point to obtain phonon frequencies and eigenvectors. Compute Born effective charges and then the phonon contribution to the dielectric function. From these results, determine for each IR-active mode (A1, B1, B2): its frequency, its normalized intensity I/Imax, and its dielectric contribution ε_p.
- Evidence: `/app/outputs/phonon_dielectric.log`

### Step 6: Output IR-active modes with I/Imax > 0.10
- Role: scored (load-bearing)
- Action: Filter the computed phonon data: select all IR-active modes whose relative intensity I/Imax is greater than 0.10. For each selected mode, record the representation (A1, B1, or B2), the frequency in cm⁻¹, I/Imax, and ε_p. Write the list as a JSON array to the output file. Modes can appear in any order, but the JSON must be parseable as an array of objects.
- Output file: `/app/outputs/IR_active_modes_Pna2_1.json`
- Format: json
- Contract: JSON array, each element: { "representation": string ("A1"/"B1"/"B2"), "frequency": float (cm⁻¹), "I_Imax": float (0‑1), "epsilon_p": float }. The number of entries should correspond to modes with I/Imax > 0.10.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Pna2_1_fractional_coordinates.csv`
- `/app/outputs/IR_active_modes_Pna2_1.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Pna2_1_fractional_coordinates.csv
- path: `/app/outputs/Pna2_1_fractional_coordinates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing the relaxed fractional coordinates of all unique ions in the Pna2_1 structure. The hidden checker will compare each coordinate to the published reference values with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `atom`, `x`, `y`, `z`
  - `units`:
    - `x`: fractional
    - `y`: fractional
    - `z`: fractional
  - `description`: One row per unique ion in the Pna2_1 primitive cell, with atom label and fractional coordinates.

### IR_active_modes_Pna2_1.json
- path: `/app/outputs/IR_active_modes_Pna2_1.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON array listing all IR-active phonon modes whose relative intensity is at least 10% of the most intense mode. The hidden checker will compare each mode's frequency, I_Imax, and epsilon_p to the published reference values with tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `representation`, `frequency`, `I_Imax`, `epsilon_p`
    - `properties`:
      - `representation`:
        - `type`: string
        - `enum`: `A1`, `B1`, `B2`
      - `frequency`:
        - `type`: number
        - `unit`: cm⁻¹
      - `I_Imax`:
        - `type`: number
        - `minimum`: 0.0
        - `maximum`: 1.0
      - `epsilon_p`:
        - `type`: number
  - `description`: Array of IR-active modes with I/Imax ≥ 0.10.

Notes: Only the two scored artifacts are required. The hidden checker uses the paper's Table II and Table V as references (not disclosed to the agent). Tolerances are chosen to absorb differences between DFT implementations while still discriminating random guesses.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Pna2_1_fractional_coordinates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "atom",
          "x",
          "y",
          "z"
        ],
        "units": {
          "x": "fractional",
          "y": "fractional",
          "z": "fractional"
        },
        "description": "One row per unique ion in the Pna2_1 primitive cell, with atom label and fractional coordinates."
      },
      "description": "CSV file containing the relaxed fractional coordinates of all unique ions in the Pna2_1 structure. The hidden checker will compare each coordinate to the published reference values with a tolerance."
    },
    {
      "file": "IR_active_modes_Pna2_1.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "representation",
            "frequency",
            "I_Imax",
            "epsilon_p"
          ],
          "properties": {
            "representation": {
              "type": "string",
              "enum": [
                "A1",
                "B1",
                "B2"
              ]
            },
            "frequency": {
              "type": "number",
              "unit": "cm⁻¹"
            },
            "I_Imax": {
              "type": "number",
              "minimum": 0.0,
              "maximum": 1.0
            },
            "epsilon_p": {
              "type": "number"
            }
          }
        },
        "description": "Array of IR-active modes with I/Imax ≥ 0.10."
      },
      "description": "JSON array listing all IR-active phonon modes whose relative intensity is at least 10% of the most intense mode. The hidden checker will compare each mode's frequency, I_Imax, and epsilon_p to the published reference values with tolerances."
    }
  ],
  "notes": "Only the two scored artifacts are required. The hidden checker uses the paper's Table II and Table V as references (not disclosed to the agent). Tolerances are chosen to absorb differences between DFT implementations while still discriminating random guesses."
}
```

## How you are scored
A hidden verifier independently evaluates your two submitted artifacts. For the fractional coordinates, each coordinate is compared to a reference set of values with a tolerance appropriate for a re‑implementation of the DFT calculations using a different (open‑source) code. For the IR modes, the verifier checks each mode's frequency, I_Imax, and ε_p against reference data, again with tolerances that account for the expected spread between independent DFT toolchains. The two artifacts are scored separately, and the final reward is a weighted sum of these scores. Reporting the original paper's numbers without actually executing the simulation will result in a low score, because the verifier can detect unrealistic submissions that do not derive from the described protocol.
