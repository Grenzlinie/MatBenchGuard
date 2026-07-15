# Compute temperature-dependent elastic constants for MgO using Murnaghan and Tallon models

## Problem background
Understanding how the elastic constants of crystalline solids change with temperature is important for material design at elevated temperatures. For ionic solids, one approach is to relate the temperature dependence of elastic constants to volume expansion via the Anderson–Grüneisen parameter. Two alternative approximations are considered: the Murnaghan model assumes the Anderson–Grüneisen parameter is constant, while the Tallon model assumes it is directly proportional to the volume ratio. This task reproduces a computational evaluation of these models for magnesium oxide (MgO).

## Approach
The computation proceeds in two stages. First, the volume ratio V(T)/V(T_D) is obtained from the thermal expansion coefficient α using two approximation orders. The first-order (parabolic) approximation is:

V/V(T_D) = 1 + α_D (T − T_D) + (1/2) α_D² δ_T^D (T − T_D)²

The second-order (cubic) approximation adds a term:

V/V(T_D) = 1 + α_D (T − T_D) + (1/2) α_D² δ_T^D (T − T_D)² + (1/3) α_D³ (δ_T^D)² (T − T_D)³

With the volume ratio, the elastic constants C11 and C44 are then evaluated using four model variants that combine Murnaghan and Tallon relations with the two volume expansions.

Murnaghan first-order:
C_ij(T) = C_ij0 [ 1 + α_D (T − T_D) + (1/2) α_D² δ_ij (T − T_D)² ]^{−δ_ij}

Murnaghan second-order:
C_ij(T) = C_ij0 [ 1 + α_D (T − T_D) + (1/2) α_D² δ_ij (T − T_D)² + (1/3) α_D³ δ_ij² (T − T_D)³ ]^{−δ_ij}

Tallon first-order:
C_ij(T) = C_ij0 exp[ −δ_ij ( α_D (T − T_D) + (1/2) α_D² δ_ij (T − T_D)² ) ]

Tallon second-order:
C_ij(T) = C_ij0 exp[ −δ_ij ( α_D (T − T_D) + (1/2) α_D² δ_ij (T − T_D)² + (1/3) α_D³ δ_ij² (T − T_D)³ ) ]

The input parameters for MgO are:
α_D = 4.42×10⁻⁵ K⁻¹, δ_T^D = 4.86,
δ_11 = 5.38, δ_44 = 2.49,
T_D = 900 K,
C11_0 = 261.9 GPa, C44_0 = 148.1 GPa.

For C11 computations use δ_ij = δ_11 and C_ij0 = C11_0; for C44 use δ_ij = δ_44 and C_ij0 = C44_0. The temperature T is varied from 900 K to 2800 K in steps of 100 K.

Implement these expressions and write the computed elastic constants to the required CSV file.

## Reproduction target
Compute the isothermal elastic constants C11 and C44 for MgO at each integer temperature from 900 K to 2800 K in 100 K increments, using the four model variants described in the Approach. Write the results to a CSV file named `elastic_constants_mgo.csv` with the columns:

Temperature(K), C11_Mur1, C11_Mur2, C11_Tal1, C11_Tal2, C44_Mur1, C44_Mur2, C44_Tal1, C44_Tal2

All elastic constants must be given in GPa. The temperature column should contain integer values (900, 1000, ..., 2800).

## Assets

- Temperature-dependent elastic constant equations (Murnaghan & Tallon models)
- NumPy: numpy

## Workflow steps

### Step 1: Compute MgO elastic constants C11 and C44
- Role: scored (load-bearing)
- Action: For MgO, compute the elastic constants C11 and C44 at each temperature from 900 K to 2800 K (100 K steps) using the Murnaghan first-order, Murnaghan second-order, Tallon first-order, and Tallon second-order expressions. Use the input parameters: α_D=4.42e-5 K⁻¹, δ_T^D=4.86, δ_11=5.38, δ_44=2.49, T_D=900 K, C11_0=261.9 GPa, C44_0=148.1 GPa. Note that Cij0 in the equations refers to C11_0 for C11 calculations and C44_0 for C44 calculations. The temperature T in the equations is the variable. Write the results to elastic_constants_mgo.csv.
- Output file: `/app/outputs/elastic_constants_mgo.csv`
- Format: csv
- Contract: Columns: Temperature(K), C11_Mur1, C11_Mur2, C11_Tal1, C11_Tal2, C44_Mur1, C44_Mur2, C44_Tal1, C44_Tal2. All numeric values; Temperature in Kelvin (integer), elastic constants in GPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants_mgo.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants_mgo.csv
- path: `/app/outputs/elastic_constants_mgo.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV containing the computed isothermal elastic constants C11 and C44 for MgO from 900 K to 2800 K in 100 K steps, using Murnaghan (first- and second-order) and Tallon (first- and second-order) models.
- schema:
  - `type`: table
  - `required_columns`: `Temperature(K)`, `C11_Mur1`, `C11_Mur2`, `C11_Tal1`, `C11_Tal2`, `C44_Mur1`, `C44_Mur2`, `C44_Tal1`, `C44_Tal2`
  - `units`:
    - `Temperature(K)`: K
    - `C11_Mur1`: GPa
    - `C11_Mur2`: GPa
    - `C11_Tal1`: GPa
    - `C11_Tal2`: GPa
    - `C44_Mur1`: GPa
    - `C44_Mur2`: GPa
    - `C44_Tal1`: GPa
    - `C44_Tal2`: GPa

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants_mgo.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature(K)",
          "C11_Mur1",
          "C11_Mur2",
          "C11_Tal1",
          "C11_Tal2",
          "C44_Mur1",
          "C44_Mur2",
          "C44_Tal1",
          "C44_Tal2"
        ],
        "units": {
          "Temperature(K)": "K",
          "C11_Mur1": "GPa",
          "C11_Mur2": "GPa",
          "C11_Tal1": "GPa",
          "C11_Tal2": "GPa",
          "C44_Mur1": "GPa",
          "C44_Mur2": "GPa",
          "C44_Tal1": "GPa",
          "C44_Tal2": "GPa"
        }
      },
      "description": "CSV containing the computed isothermal elastic constants C11 and C44 for MgO from 900 K to 2800 K in 100 K steps, using Murnaghan (first- and second-order) and Tallon (first- and second-order) models."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted CSV will be evaluated by an automated verifier. The verifier independently recomputes the expected elastic constants using the identical mathematical expressions and input parameters described above. For each temperature and each of the eight model columns, the verifier checks whether your submitted value falls within a prescribed relative tolerance of the recomputed reference value. The overall score is the fraction of the 160 values (20 temperatures × 8 columns) that pass this tolerance check. The verifier does not award credit for simply quoting published numbers; the values must be generated by your own implementation of the described models.
