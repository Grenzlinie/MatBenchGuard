# Magnetostrictive energy-minimization model for epitaxial Dy films

## Problem background
Bulk hexagonal dysprosium exhibits a helical antiferromagnetic order below TN=176 K and a helical-to-ferromagnetic transition at a Curie temperature TC=89 K, driven by magnetostrictive effects. Epitaxial growth of Dy films on substrates with different lattice parameters introduces a c‑axis strain ε33 that can shift the Curie temperature. The goal is to compute the Curie temperature of an epitaxial dysprosium film as a function of the c‑axis strain ε33, using a magnetostrictive total‑energy model.

## Approach
Consider a symmetric X/Dy/X sandwich where X is Y or Er. The total energy includes three contributions: (i) elastic energy in the Dy layer and in the clamping X layers, using literature elastic constants; (ii) magnetoelastic energy in Dy that couples the magnetic order to three symmetry‑adapted strains (εα1, εα2, εγ); (iii) exchange energy in Dy, treated with the classical three‑planes model. For a fixed c‑axis strain ε33, the total energy is minimised with respect to the free symmetry strains at several temperatures, for both the helical and ferromagnetic states. The Curie temperature is identified as the temperature at which the ferromagnetic total energy becomes lower than the helical one. The magnetostriction constants are first calibrated by requiring that the model reproduces the known bulk Dy Curie temperature at zero epitaxial strain. The calibrated model is then evaluated for a set of ε33 values covering a range of negative and positive strains.

## Reproduction target
Compute a list of (ε33, TC) pairs for c‑axis strain values that span at least the interval from −0.5 % to +0.5 %. For each strain, determine TC via total‑energy minimisation as described above. Save the results in `/app/outputs/tc_vs_strain.json` as an array of objects, each having field `epsilon33` (dimensionless strain) and `Tc` (Kelvin). The output must contain enough points to reveal the dependence of TC on ε33.

## Assets

- Elastic constants of hcp dysprosium: 10.1103/PhysRev.109.1544
- Magnetostriction constants of dysprosium: 10.1103/PhysRev.139.A455
- Exchange integrals for three-planes model: 10.1063/1.1736156
- Elastic constants of Y and Er: 10.1103/PhysRev.109.1544

## Workflow steps

### Step 1: Compute exchange barrier
- Role: process
- Action: Implement the classical three-planes model using literature exchange integrals for dysprosium to compute the exchange energy difference between helical and ferromagnetic states as a function of temperature (the exchange barrier).
- Evidence: `/app/outputs/exchange_barrier.txt`

### Step 2: Calibrate magnetostriction constants
- Role: process
- Action: Using the exchange barrier from step 01 and literature elastic constants for Dy and clamping layers, perform total energy minimisation at zero epitaxial strain and adjust the magnetostriction constants (within literature ranges) so that the model predicts a Curie temperature of 89 K. Save the calibrated constants.
- Evidence: `/app/outputs/calibrated_constants.json`

### Step 3: Compute Tc vs epitaxial strain
- Role: scored (load-bearing)
- Action: With the calibrated magnetostriction constants and the exchange barrier, for a set of c-axis epitaxial strain values covering at least -0.5% to +0.5%, perform total energy minimisation with respect to the free symmetry strains (εα1, εα2, εγ) for both helical and ferromagnetic states at various temperatures. For each strain, determine the Curie temperature as the temperature where the total energy of the ferromagnetic state becomes lower than that of the helical state. Output the list of (ε33, Tc) pairs.
- Output file: `/app/outputs/tc_vs_strain.json`
- Format: json
- Contract: [{"epsilon33": number, "Tc": number}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tc_vs_strain.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tc_vs_strain.json
- path: `/app/outputs/tc_vs_strain.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Computed Tc vs ε33 data; verified by monotonic increase and zero-strain Tc near 89 K.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `epsilon33`, `Tc`
    - `properties`:
      - `epsilon33`:
        - `type`: number
        - `description`: c-axis epitaxial strain (dimensionless, e.g. -0.005 to +0.005)
      - `Tc`:
        - `type`: number
        - `units`: K
        - `description`: Calculated Curie temperature

Notes: The model may be run for either Y or Er clamping layers; the trend is independent of the choice. The checker validates structural properties (monotonicity, zero-strain Tc match).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tc_vs_strain.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "epsilon33",
            "Tc"
          ],
          "properties": {
            "epsilon33": {
              "type": "number",
              "description": "c-axis epitaxial strain (dimensionless, e.g. -0.005 to +0.005)"
            },
            "Tc": {
              "type": "number",
              "units": "K",
              "description": "Calculated Curie temperature"
            }
          }
        }
      },
      "description": "Computed Tc vs ε33 data; verified by monotonic increase and zero-strain Tc near 89 K."
    }
  ],
  "notes": "The model may be run for either Y or Er clamping layers; the trend is independent of the choice. The checker validates structural properties (monotonicity, zero-strain Tc match)."
}
```

## How you are scored
A hidden verifier inspects each workflow stage’s output: the exchange barrier text file, the calibrated constants JSON, and the final Tc‑vs‑strain JSON. The overall reward is a weighted sum, with the main scored artifact (`tc_vs_strain.json`) receiving the largest weight. The verifier checks the structure of the Tc‑vs‑strain list (minimum number of points, strain range covered, data types) and examines the trend of Tc with ε33 as well as the Tc value at zero strain. The exact comparison thresholds and scoring function are not disclosed.
