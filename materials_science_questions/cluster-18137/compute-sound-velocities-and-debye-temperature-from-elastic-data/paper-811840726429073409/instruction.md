# Compute Temperature-Dependent Elastic Constants for MgO using Murnaghan and Tallon Models

## Problem background
The temperature variation of elastic constants in ionic solids is critical for understanding their mechanical and thermal behavior at high temperatures. For the rock-salt oxide MgO, the elastic constants C11 and C44 govern wave propagation and lattice stability. This task involves computing how C11 and C44 change with temperature using established closed‑form models (Murnaghan and Tallon) that connect the elastic constants to the thermal expansion of the crystal. The computed values provide a theoretical prediction of MgO’s high‑temperature elasticity, which is valuable for geophysics and materials science.

## Approach
The thermal variation of the elastic constants is derived from the Anderson–Grüneisen formalism. First, the temperature‑dependent volume ratio V(T)/V(T_D) is obtained from the volume thermal expansion coefficient α(T) using a first‑order (parabolic) and second‑order (cubic) expansion in (T – T_D). Given input parameters for MgO (T_D = 900 K, α_D = 4.42×10⁻⁵ K⁻¹, and the Anderson–Grüneisen parameters δ_11 = 5.38 and δ_44 = 2.49), the volume ratio is computed. Then, the elastic constants are calculated via two model families: the Murnaghan model (assumes δ_ij constant, resulting in a power‑law scaling of C_ij with volume) and the Tallon model (assumes δ_ij ∝ volume, giving an exponential relation). For each model, both the first‑order (using the parabolic volume expansion) and second‑order (using the cubic volume expansion) approximations are applied. Thus, four estimates of each elastic constant are obtained at every temperature, enabling a comparison of the different approximations. The computation is performed for temperatures from 900 K to 2800 K in steps of 100 K.

## Reproduction target
Produce a CSV file `elastic_constants_MgO.csv` containing 20 rows (temperatures from 900 K to 2800 K, inclusive, in steps of 100 K). The columns are: `T` (temperature in K); `C11_M1`, `C11_M2`, `C11_T1`, `C11_T2` (C11 in GPa for Murnaghan first‑order, Murnaghan second‑order, Tallon first‑order, Tallon second‑order); and `C44_M1`, `C44_M2`, `C44_T1`, `C44_T2` (C44 in GPa for the same four approximations). All numeric values must be given with at most one decimal place. The elastic constants are expected to decrease monotonically as temperature increases, and the different approximations should yield similar but not identical values.

## Assets

- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Compute temperature-dependent elastic constants for MgO
- Role: scored (load-bearing)
- Action: Compute C11(T) and C44(T) for MgO at temperatures T = 900, 1000, ..., 2800 K (step 100 K) using the Murnaghan (first-order and second-order) and Tallon (first-order and second-order) models. Input parameters: T_D = 900 K, C11_0 = 261.9 GPa, C44_0 = 148.1 GPa, α_D = 4.42e-5 K⁻¹, δ_11 = 5.38, δ_44 = 2.49. First compute the volume ratio V(T)/V(T_D) using the first-order (parabolic) and second-order (cubic) expansions derived from the Anderson–Grüneisen relation, then evaluate the elastic constants via the power-law (Murnaghan) and exponential (Tallon) formulas that connect C_ij to volume ratio. Write the results as a CSV file.
- Output file: `/app/outputs/elastic_constants_MgO.csv`
- Format: csv
- Contract: CSV with header: T (int, K), C11_M1 (float, GPa), C11_M2 (float, GPa), C11_T1 (float, GPa), C11_T2 (float, GPa), C44_M1 (float, GPa), C44_M2 (float, GPa), C44_T1 (float, GPa), C44_T2 (float, GPa). Temperatures from 900 to 2800 in steps of 100 K (20 rows). All values given with at most one decimal place.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants_MgO.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants_MgO.csv
- path: `/app/outputs/elastic_constants_MgO.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed elastic constants for MgO across a temperature range using four model approximations. Each entry is compared to a hidden gold value (paper’s Table 2) with an appropriate tolerance. The CSV must contain exactly 20 rows for T = 900..2800 K in steps of 100 K.
- schema:
  - `type`: table
  - `required_columns`: `T`, `C11_M1`, `C11_M2`, `C11_T1`, `C11_T2`, `C44_M1`, `C44_M2`, `C44_T1`, `C44_T2`
  - `units`:
    - `T`: K
    - `C11_M1`: GPa
    - `C11_M2`: GPa
    - `C11_T1`: GPa
    - `C11_T2`: GPa
    - `C44_M1`: GPa
    - `C44_M2`: GPa
    - `C44_T1`: GPa
    - `C44_T2`: GPa

Notes: Gold values and tolerances are hidden. The numeric comparison is based on the paper’s own computed values for MgO in Table 2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants_MgO.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "C11_M1",
          "C11_M2",
          "C11_T1",
          "C11_T2",
          "C44_M1",
          "C44_M2",
          "C44_T1",
          "C44_T2"
        ],
        "units": {
          "T": "K",
          "C11_M1": "GPa",
          "C11_M2": "GPa",
          "C11_T1": "GPa",
          "C11_T2": "GPa",
          "C44_M1": "GPa",
          "C44_M2": "GPa",
          "C44_T1": "GPa",
          "C44_T2": "GPa"
        }
      },
      "description": "Computed elastic constants for MgO across a temperature range using four model approximations. Each entry is compared to a hidden gold value (paper’s Table 2) with an appropriate tolerance. The CSV must contain exactly 20 rows for T = 900..2800 K in steps of 100 K."
    }
  ],
  "notes": "Gold values and tolerances are hidden. The numeric comparison is based on the paper’s own computed values for MgO in Table 2."
}
```

## How you are scored
Your submitted CSV will be evaluated by a hidden verifier. For each temperature and each model variant, the computed elastic constant is compared to a hidden gold value (derived from the paper’s reported calculations for MgO) with an appropriate tolerance. The score is based on the fraction of entries that fall within the tolerance; more accurate entries yield a higher reward. A small structural consistency check verifies that each elastic constant series decreases monotonically with temperature. A perfect score requires correctly implementing all four model variants across the full temperature range. No gold values are disclosed; the task is solved by faithfully coding the physical models with the given parameters.
