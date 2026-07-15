# B3LYP/B1 hydrogen abstraction barriers for cytochrome P450 Compound I model with catalytic water

## Problem background
Cytochrome P450 enzymes catalyze the hydroxylation of a wide variety of substrates via the high-valent iron-oxo species Compound I (Cpd I). In the prototypical P450cam system, previous QM/MM studies found that a single active-site water molecule (W903) lowers the hydrogen abstraction barrier. The present work generalizes this catalytic role by performing gas-phase density functional theory (DFT) calculations for nine different substrates, using a model Cpd I (iron-oxo-porphine with axial SH ligand). The aim is to compute the electronic energy barrier for hydrogen abstraction by Cpd I, both with and without the water molecule, and to determine how the barrier lowering varies among substrates, including a special interest in N,N-dimethylaniline where direct substrate–water contact may occur.

## Approach
The computational approach is a series of gas-phase DFT calculations at the B3LYP/VWN5 level of theory. The Cpd I model and each substrate (ethane, propane, phenylethane, Me‑probe, camphor, propene, toluene, iPr‑probe, N,N‑dimethylaniline) are treated as isolated molecules. For each combination, two scenarios are studied: without an additional water molecule, and with a water molecule (W903) hydrogen‑bonded to the oxo atom of Cpd I. For N,N‑dimethylaniline, an additional constrained arrangement (9c) is included, where the water oxygen is fixed trans to the aniline nitrogen to prevent direct substrate‑water interaction. All species—separated reactants (Cpd I ± W903 + substrate) and the transition state for hydrogen abstraction—are fully geometry optimized. Geometries are optimized separately for the doublet and quartet spin states. The electronic energy barrier is then computed as the energy difference between the transition state and the separated reactants. The effect of the water catalyst is quantified as the difference between the barrier without W903 and with W903.

## Reproduction target
Perform the B3LYP/B1 gas-phase calculations described above for all substrates 1–9 (including the primary/secondary/benzylic abstraction labels for propane and phenylethane, and the constrained 9c geometry) in both doublet and quartet spin states. Produce a single file containing the computed barriers and barrier differences. The results must demonstrate the general barrier lowering due to the water molecule across all substrates. For substrate 9 (N,N-dimethylaniline) the lowering must be notably larger than for any other substrate, while the constrained 9c geometry must reduce the lowering back to the typical range observed for the other substrates.

## Assets

- Turbomole or equivalent DFT code: https://www.turbomole.org

## Workflow steps

### Step 1: Prepare initial molecular geometries
- Role: process
- Action: Build realistic 3D structures of the Cpd I model (iron‑oxo‑porphyrin without side chains, axial SH ligand) and each substrate (ethane, propane, phenylethane, Me‑probe, camphor, propene, toluene, iPr‑probe, N,N‑dimethylaniline). Generate starting geometries for reactant complexes and plausible transition‑state guesses for hydrogen abstraction, both without and with a water molecule (W903) hydrogen‑bonded to the oxo atom. For N,N‑dimethylaniline, also create the constrained 9c arrangement (W903 oxygen trans to aniline nitrogen). Prepare separate inputs for doublet and quartet spin states.
- Evidence: `/app/outputs/geometry_preparation.log`

### Step 2: Perform B3LYP/B1 geometry optimizations
- Role: process
- Action: Run gas‑phase B3LYP/B1 (VWN5-LDA correlation) geometry optimizations for all species: separated reactants (Cpd I + substrate, Cpd I‑W903 + substrate) and transition states (without W903, with W903) for every substrate (1–9) and both doublet and quartet spin states. Include the constrained 9c arrangement for N,N‑dimethylaniline. Use the B1 basis (LACVP ECP on Fe, 6‑31G on all other atoms). Record the final SCF energies of the optimized geometries.
- Evidence: `/app/outputs/dft_energies.txt`

### Step 3: Compute hydrogen abstraction barriers and compile results
- Role: scored (load-bearing)
- Action: For each substrate/spin/water condition, compute the electronic energy barrier as the difference between the transition‑state total energy and the sum of the separated‑reactant total energies (Cpd I ± W903 + substrate). Calculate the barrier lowering as the difference of the barriers without and with W903. Assemble all results into a single JSON file that contains one entry per row of Table 1 (substrates 1–9 in doublet and quartet states, including labels 2n, 2i, 3n, 3b, and 9c).
- Output file: `/app/outputs/barriers_b1.json`
- Format: json
- Contract: [{"substrate": int, "label": "string", "spin": "D"|"Q", "barrier_without_W903": float, "barrier_with_W903": float, "barrier_difference": float}, ...]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barriers_b1.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers_b1.json
- path: `/app/outputs/barriers_b1.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed B3LYP/B1 hydrogen abstraction barriers and barrier lowerings for substrates 1–9 and 9c, doublet and quartet states.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `substrate`, `label`, `spin`, `barrier_without_W903`, `barrier_with_W903`, `barrier_difference`
    - `properties`:
      - `substrate`:
        - `type`: integer
        - `description`: substrate number 1–9
      - `label`:
        - `type`: string
        - `description`: e.g. '2n', '2i', '3n', '3b', '9c'
      - `spin`:
        - `type`: string
        - `enum`: `D`, `Q`
      - `barrier_without_W903`:
        - `type`: number
        - `description`: kcal/mol
      - `barrier_with_W903`:
        - `type`: number
        - `description`: kcal/mol
      - `barrier_difference`:
        - `type`: number
        - `description`: kcal/mol

Notes: No zero-point corrections; barriers are electronic energy differences. A tolerance relaxes exact agreement to account for toolchain differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers_b1.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "substrate",
            "label",
            "spin",
            "barrier_without_W903",
            "barrier_with_W903",
            "barrier_difference"
          ],
          "properties": {
            "substrate": {
              "type": "integer",
              "description": "substrate number 1–9"
            },
            "label": {
              "type": "string",
              "description": "e.g. '2n', '2i', '3n', '3b', '9c'"
            },
            "spin": {
              "type": "string",
              "enum": [
                "D",
                "Q"
              ]
            },
            "barrier_without_W903": {
              "type": "number",
              "description": "kcal/mol"
            },
            "barrier_with_W903": {
              "type": "number",
              "description": "kcal/mol"
            },
            "barrier_difference": {
              "type": "number",
              "description": "kcal/mol"
            }
          }
        }
      },
      "description": "Computed B3LYP/B1 hydrogen abstraction barriers and barrier lowerings for substrates 1–9 and 9c, doublet and quartet states."
    }
  ],
  "notes": "No zero-point corrections; barriers are electronic energy differences. A tolerance relaxes exact agreement to account for toolchain differences."
}
```

## How you are scored
A hidden verifier will read your output file and compare each reported barrier and barrier difference to reference values. It will also check that the required relative trends are satisfied: the lowering for substrate 9 must be greater than for all other substrates, and the lowering for the constrained 9c geometry must fall within the range typical of the other substrates. Partial credit is awarded for each matched entry and trend. The final score is a weighted combination of these contributions, between 0 and 1. Simply providing data that passes shape and format checks is not sufficient; the computed quantities must reflect the correct physical outcome of the DFT procedure.
