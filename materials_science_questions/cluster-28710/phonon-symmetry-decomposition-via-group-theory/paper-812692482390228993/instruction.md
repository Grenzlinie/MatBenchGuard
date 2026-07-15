# Reproduce the superspace group and extinction rules for incommensurate NbS3-II

## Problem background
Niobium trisulfide (NbS3) crystallizes in two distinct polytypes: type I, which is commensurately modulated and whose crystal structure is known, and type II, which forms incommensurately modulated crystals whose structure has not been determined. Electron diffraction patterns from NbS3-II exhibit characteristic systematic absences for main reflections and for the incommensurate satellite reflections, together with a modulation wavevector q ≈ 0.352 c*. The known basic structure of NbS3-I (space group P2_1/m, a = 9.14 Å, b = 4.96 Å, c = 6.73 Å, γ = 97.2°) and the experimental constraints observed for NbS3-II provide the necessary input to derive a superspace-group description of the incommensurate modulation. This task asks you to determine the superspace group, the resulting extinction rules for main and first-order satellite reflections, and the corresponding modulation cell parameters that are consistent with all given constraints and with the analogy to the NbS3-I structure.

## Approach
Start from the known basic structure of NbS3-I (space group P2_1/m, a = 9.14 Å, b = 4.96 Å, c = 6.73 Å, γ = 97.2°, Z = 2). For NbS3-II, the electron-diffraction evidence indicates a basic modulation cell that is an enlargement of the NbS3-I cell, with parameters approximately a, 4b, c and a modulation wavevector q ≈ 0.352 c*. The observed indexing cells are G_M1(2a, 4b, c/0.352, γ = 97°) and G_M2(2a, 4b, 2c/0.352, γ = 97°), and the diffraction patterns require B centering with a phase shift of π between intra-layer modulation columns. Using group-theoretical tables or a standard superspace-group derivation, construct the superspace group in dualistic notation that is consistent with the P2_1/m symmetry of the basic cell, the required centering, and the phase relationships. From the symmetry operations of that group, derive the systematic extinction conditions: determine how the structure-factor contributions from the B-centring translation a/2 combine for main reflections (hkl) and for first-order satellite reflections (hkl±q). The result will give conditions on the h index. Finally, report the basic modulation cell (a, 4b, c) with lattice parameters derived from the NbS3-I cell, and the full incommensurate modulation cell with B centering, as implied by the indexing cells G_M1 and G_M2.

## Reproduction target
Given the NbS3-I basic structure (space group P2_1/m, a=9.14 Å, b=4.96 Å, c=6.73 Å, γ=97.2°, Z=2, 2e sites) and the experimental indexing cells for NbS3-II (G_B, G_M1, G_M2 with modulation wavevector q ≈ 0.352 c*), determine the dualistic superspace group that is consistent with P2_1 /m symmetry, B centering, and the required phase relationships between intra‑layer modulation columns. From that superspace group, derive the systematic extinction rules for main reflections (hkl) and first‑order satellite reflections (hkl±q). Report the basic modulation cell and the B‑centered incommensurate modulation cell implied by the superspace group enlargement. Output the superspace‑group notation, the extinction rules as a CSV file, and the modulation cell parameters as a text file, following the exact file schema described in the Workflow steps.

## Assets

- NbS3-I crystal structure reference: 10.1016/0022-4596(78)90154-8
- Group-theoretical tables (Kovalev / Bradley-Cracknell)
- Bilbao Crystallographic Server (Superspace Groups tool): https://www.cryst.ehu.es/cryst/superspace.html

## Workflow steps

### Step 1: Superspace group notation
- Role: scored (load-bearing)
- Action: From the known basic structure of NbS3-I and the indexing cells for NbS3-II (G_M1(2a,4b,c/0.352,γ=97°) and G_M2(2a,4b,2c/0.352,γ=97°)), derive the superspace group for incommensurately modulated NbS3-II in dualistic notation. The basic cell should be an appropriate enlargement of the NbS3-I cell with symmetry P2_1/m, and the modulation must be B‑centered with a π phase shift between intra‑layer modulation columns. Use the modulation wavevector q ≈ 0.352 c*.
- Output file: `/app/outputs/step_01_superspace_group.txt`
- Format: txt
- Contract: Single line string containing the superspace group in dualistic notation. Acceptable formats include the compact form (e.g., A P2_1/m (α,β)) or the full dualistic expansion with mP2_1/m and cB2/m.
- Scoring: scored by hidden verifier

### Step 2: Extinction rules
- Role: scored
- Action: From the superspace group determined in step_01, compute the systematic extinction conditions for main reflections (hkl) and first-order satellite reflections (hkl±q). Express the conditions in terms of the reflection indices (h, k, l) and the satellite order m.
- Output file: `/app/outputs/step_02_extinction_rules.csv`
- Format: csv
- Contract: Columns: reflection (string: 'main' or 'satellite'), condition (string: extinction condition expressed in terms of h,k,l indices), description (string: brief explanation).
- Scoring: scored by hidden verifier

### Step 3: Modulation cell parameters
- Role: scored
- Action: Based on the superspace group notation and the given indexing cells G_M1 and G_M2, state the basic modulation cell and the full incommensurate modulation cell for NbS3-II. The basic cell is the enlarged cell (a, 4b, c) derived from the NbS3-I cell; the incommensurate cell is the B‑centered supercell implied by G_M1.
- Output file: `/app/outputs/step_03_modulation_cell.txt`
- Format: txt
- Contract: Line 1: 'basic modulation cell: a=<value>, b=<value>, c=<value>, gamma=<degrees> degrees'. Line 2: 'incommensurate modulation cell: a=<value>, b=<value>, c=<value>, gamma=<degrees> degrees, B-centered'. Values are to be given to one decimal place where appropriate.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_superspace_group.txt`
- `/app/outputs/step_02_extinction_rules.csv`
- `/app/outputs/step_03_modulation_cell.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_superspace_group.txt
- path: `/app/outputs/step_01_superspace_group.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Superspace group notation for NbS3-II in dualistic notation. The checker normalises whitespace and special characters before exact comparison.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`: object

### step_02_extinction_rules.csv
- path: `/app/outputs/step_02_extinction_rules.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Extinction conditions for main reflections and first-order satellites. The checker compares each row's condition string to the reference derived from the paper.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `reflection`, `condition`, `description`
  - `units`: object

### step_03_modulation_cell.txt
- path: `/app/outputs/step_03_modulation_cell.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Basic and incommensurate modulation cell parameters. The checker parses the two lines, extracts numerical values for a, b, c, and gamma, and compares against the paper's values with tolerances (±0.2 Å, ±1°).
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `a`: Å
    - `b`: Å
    - `c`: Å
    - `gamma`: °

Notes: The task uses the paper-reported experimental constraints for NbS3-II as input. The superspace group is a fixed symbolic expression; extinction rules are a discrete set of conditions; cell parameters are numeric with small tolerances. All outputs are deterministic and verifiable against hidden reference values derived from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_superspace_group.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Superspace group notation for NbS3-II in dualistic notation. The checker normalises whitespace and special characters before exact comparison."
    },
    {
      "file": "step_02_extinction_rules.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "reflection",
          "condition",
          "description"
        ],
        "units": {}
      },
      "description": "Extinction conditions for main reflections and first-order satellites. The checker compares each row's condition string to the reference derived from the paper."
    },
    {
      "file": "step_03_modulation_cell.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "a": "Å",
          "b": "Å",
          "c": "Å",
          "gamma": "°"
        }
      },
      "description": "Basic and incommensurate modulation cell parameters. The checker parses the two lines, extracts numerical values for a, b, c, and gamma, and compares against the paper's values with tolerances (±0.2 Å, ±1°)."
    }
  ],
  "notes": "The task uses the paper-reported experimental constraints for NbS3-II as input. The superspace group is a fixed symbolic expression; extinction rules are a discrete set of conditions; cell parameters are numeric with small tolerances. All outputs are deterministic and verifiable against hidden reference values derived from the paper."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three scored output files. Your superspace‑group notation in `step_01_superspace_group.txt` is compared (after normalising whitespace and special characters) to the expected dualistic symbol. The extinction rules CSV is checked row‑by‑row against reference extinction conditions that the verifier recomputes from the superspace group. The modulation cell parameters in `step_03_modulation_cell.txt` are parsed; the numerical values for a, b, c, and γ are compared to the correct values with small hidden tolerances. The overall reward is a weighted combination of the scores from all three outputs. Providing numbers that happen to match the paper’s values is not sufficient — the verifier independently derives the extinction rules from your submitted superspace‑group symbol and checks internal consistency. The exact reference values and tolerances are not disclosed.
