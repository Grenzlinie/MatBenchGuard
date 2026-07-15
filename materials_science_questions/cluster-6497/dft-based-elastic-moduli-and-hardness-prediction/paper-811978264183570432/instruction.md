# Computed isothermal bulk moduli for mixed alkaline-earth fluoride crystals using end-member formula

## Problem background
Mixed crystals, such as solid solutions of CaF2 and SrF2, exhibit elastic properties that deviate from a simple linear interpolation between the end members. Accurately predicting the isothermal bulk modulus of these mixtures is important for understanding their mechanical stability and for selecting materials with tailored stiffness. This task computes the bulk modulus values for nine different compositions across the full CaF2–SrF2 range, using a physically motivated mixing formula that accounts for the molar volume mismatch between the two fluorides.

## Approach
The isothermal bulk modulus B of a mixed crystal can be estimated from the bulk moduli and molar volumes of the two end members using a nonlinear mixing formula. According to this model, the bulk modulus of a composition with mole fraction x of SrF2 is given by an expression that involves the ratio v2/v1 of the end-member molar volumes. Because the crystals have a cubic structure, the molar volume is proportional to the cube of the nearest-neighbor distance (r0³). The provided resource `nearest_neighbor_distances.csv` supplies the r0 values for each composition; from these, the volume ratio v2/v1 for each mixture is computed. Using the fixed end-member bulk moduli (B1 = 814 kbar for CaF2, B2 = 693 kbar for SrF2), the formula is then evaluated at every composition to produce the bulk modulus in kbar. The calculation is purely analytical and does not require any external fitting or simulation.

## Reproduction target
For each of the nine compositions listed in the provided `nearest_neighbor_distances.csv` (ranging from pure CaF2 to pure SrF2, with intermediate mixed compositions), compute the isothermal bulk modulus in kbar using the mixing formula described above. Store the results in `/app/outputs/computed_bulk_moduli.csv` with two columns: `composition` (the composition identifier, as given in the CSV) and `bulk_modulus_kbar` (the computed modulus, numeric).

## Assets

- nearest_neighbor_distances.csv

## Workflow steps

### Step 1: Compute bulk moduli for mixed crystal compositions
- Role: scored (load-bearing)
- Action: Using the nearest-neighbor distances from the provided nearest_neighbor_distances.csv, compute the molar volume ratio for each composition (v ∝ distance³ for cubic crystals). Apply the mixed-crystal formula for isothermal bulk modulus of a two-end-member system: B = [1 + x*(v2/v1 - 1)] / [1 + x*(B1/B2 * v2/v1 - 1)] * B1, with end-member bulk moduli B1 = 814 kbar (CaF2) and B2 = 693 kbar (SrF2), and mole fraction x of SrF2 for each composition. Write the output to /app/outputs/computed_bulk_moduli.csv.
- Output file: `/app/outputs/computed_bulk_moduli.csv`
- Format: csv
- Contract: CSV with columns: composition (string, e.g., 'CaF2'), bulk_modulus_kbar (float). Example: composition, bulk_modulus_kbar
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_bulk_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_bulk_moduli.csv
- path: `/app/outputs/computed_bulk_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed isothermal bulk moduli for all nine mixed-crystal compositions, compared against a hidden reference (the paper's reported values) with a permissive floating-point tolerance.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `bulk_modulus_kbar`
  - `units`:
    - `bulk_modulus_kbar`: kbar

Notes: The computation uses only the bundled CSV and the given end-member moduli. No external fetching is required beyond potential Python standard library and/or pandas to read/write CSV; the formula is straightforward arithmetic.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_bulk_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "bulk_modulus_kbar"
        ],
        "units": {
          "bulk_modulus_kbar": "kbar"
        }
      },
      "description": "The computed isothermal bulk moduli for all nine mixed-crystal compositions, compared against a hidden reference (the paper's reported values) with a permissive floating-point tolerance."
    }
  ],
  "notes": "The computation uses only the bundled CSV and the given end-member moduli. No external fetching is required beyond potential Python standard library and/or pandas to read/write CSV; the formula is straightforward arithmetic."
}
```

## How you are scored
A hidden verifier will independently inspect your `/app/outputs/computed_bulk_moduli.csv`. It checks that the file follows the required format and then compares each composition's computed bulk modulus to the expected reference value (determined by the same inputs and formula). Your overall reward is the fraction of compositions whose modulus is within the verifier’s acceptable tolerance, plus any structural checks. A correct implementation that follows the approach and correctly reads the provided distances will achieve a high score. Simply reporting the paper's numbers without performing the computation will not pass the scoring.
