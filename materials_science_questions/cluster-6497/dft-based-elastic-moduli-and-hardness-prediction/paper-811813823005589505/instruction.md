# Lattice Thermal Conductivity and Bulk Modulus Prediction for Zinc Blende Semiconductors

## Problem background
Zinc blende (cubic) binary semiconductors of the A<sup>II</sup>B<sup>VI</sup> and A<sup>III</sup>B<sup>V</sup> families are widely used in optoelectronics and high-power electronics. Understanding their lattice thermal conductivity (K) and bulk modulus (B) is important for thermal management and mechanical design. This task examines an empirical approach that relates K and B to simple structural parameters — the nearest-neighbour distance d (Å) and the product of the formal ionic charges Z₁Z₂. The target is to compute K and B for a comprehensive set of zinc blende compounds and to evaluate how well the empirical predictions align with reference measurements.

## Approach
The empirical relations are:
- Lattice thermal conductivity (K, in W/K·cm): K = 2·(Z₁·Z₂)^1.5 / d^5, where d is the nearest-neighbour distance in Å and the ionic charge product is Z₁Z₂ = 4 for A<sup>II</sup>B<sup>VI</sup> compounds and Z₁Z₂ = 9 for A<sup>III</sup>B<sup>V</sup> compounds.
- Bulk modulus (B, in GPa): B = C·K^0.75, with the proportionality constant C = 110 for A<sup>III</sup>B<sup>V</sup> semiconductors and C = 235 for A<sup>II</sup>B<sup>VI</sup> semiconductors.

The only input needed per compound is its nearest-neighbour distance d. These d values must be obtained from a published crystallographic source (the asset "Nearest neighbor distances for zinc blende semiconductors (Verma 2009)" listed below) or an equivalent reliable source. Using these inputs, K and B are computed for all compounds that appear in the referenced compilation.

## Reproduction target
Produce a CSV file `computed_properties.csv` with one row per zinc blende compound (covering both A<sup>II</sup>B<sup>VI</sup> and A<sup>III</sup>B<sup>V</sup> families) and columns: compound (string), d (float, Å), K_computed (float, W/K·cm), B_computed (float, GPa). The computations must follow the empirical formulas described in the Approach section. A hidden verifier will compare your computed K and B values against a hidden reference set to assess agreement.

## Assets

- Nearest neighbor distances for zinc blende semiconductors (Verma 2009): 10.1088/0031-8949/79/04/045703

## Workflow steps

### Step 1: Compile nearest neighbor distances
- Role: process
- Action: Obtain the nearest neighbor distance d (Å) for each zinc blende compound (A^IIB^VI and A^IIIB^V) from the reference (Verma, Phys. Scr. 79, 2009) or a reliable crystallographic source. Prepare a list mapping compound names to d values and save it as /app/outputs/d_values_compilation.txt.
- Evidence: `/app/outputs/d_values_compilation.txt`

### Step 2: Compute K and B and output CSV
- Role: scored (load-bearing)
- Action: For each compound, compute lattice thermal conductivity K (W/K·cm) using the empirical relation that combines ionic charge product and nearest neighbor distance, and compute bulk modulus B (GPa) from K using a power-law with compound-family-specific constants. Write the results to computed_properties.csv with columns: compound, d, K_computed, B_computed.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: CSV with columns: compound (string), d (float, Å), K_computed (float, W/K·cm), B_computed (float, GPa). One row per compound covering all zinc blende semiconductors listed in the paper.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV with computed lattice thermal conductivity and bulk modulus for each zinc blende compound. The checker will recompute MAPE against hidden experimental values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `d`, `K_computed`, `B_computed`
  - `units`:
    - `d`: Å
    - `K_computed`: W/K·cm
    - `B_computed`: GPa

Notes: The CSV must contain at least the compounds for which hidden experimental values exist. The checker computes mean absolute percentage error (MAPE) separately for K and B, and passes the task if both are below a hidden tolerance, with partial credit for larger errors.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "d",
          "K_computed",
          "B_computed"
        ],
        "units": {
          "d": "Å",
          "K_computed": "W/K·cm",
          "B_computed": "GPa"
        }
      },
      "description": "CSV with computed lattice thermal conductivity and bulk modulus for each zinc blende compound. The checker will recompute MAPE against hidden experimental values from the paper."
    }
  ],
  "notes": "The CSV must contain at least the compounds for which hidden experimental values exist. The checker computes mean absolute percentage error (MAPE) separately for K and B, and passes the task if both are below a hidden tolerance, with partial credit for larger errors."
}
```

## How you are scored
Your submission will be scored by a hidden verifier.
- The primary scored artifact is `computed_properties.csv`. The verifier extracts your computed K and B values for the compounds where hidden reference values exist and calculates an error metric (e.g., mean absolute percentage error) separately for K and for B.
- The score is monotonic in quality: lower error yields a higher score; there is no penalty for producing values that are more accurate than the reference.
- The workflow is sequential: Step 1 (compiling distances) is a required process step; its evidence file documents that you assembled the inputs. Step 2 (computing K and B and writing the CSV) is the scored step. Both steps must be executed; skipping the data-gathering step will prevent a successful computation.
- The final reward is a combination of scores from the scored artifacts, with the CSV carrying the dominant weight. Reporting numbers without executing the described procedure is not sufficient.
