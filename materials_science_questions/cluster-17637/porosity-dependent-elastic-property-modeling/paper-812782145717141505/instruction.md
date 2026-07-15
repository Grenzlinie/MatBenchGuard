## Problem background

The mechanical behaviour of nano-porous and nano-cracked materials differs from their macroscopic counterparts. At the nanometre scale the surface-to-volume ratio is large, and surface/interface energy can significantly alter the effective elastic stiffness. For example, depending on the crystallographic orientation of the free surface, a nano-porous metal can become either stiffer or more compliant than the pristine matrix. Understanding and quantifying these size- and shape-dependent effects is essential for designing lightweight nanostructured materials with tailored mechanical properties.

This task concerns the computational homogenization of a two‑dimensional (plane strain) representative elementary volume (REV) containing nano-voids or nano-cracks embedded in an aluminium matrix. The goal is to calculate the effective in‑plane bulk modulus as a function of the void radius, volume fraction, void flattening, and crack multiplicity/orientation, while accounting for the surface elastic energy at the matrix‑heterogeneity interfaces via a coherent interface (Laplace–Young / Gurtin–Murdoch) model.

## Approach

The core methodology is a periodic homogenization scheme that couples the extended finite element method (XFEM) with level‑set geometry descriptions. XFEM enrichment functions (Moës‑type for inclusions, indicator for voids, Heaviside for cracks) allow interfaces to cut through the finite element mesh so that re‑meshing is unnecessary. The surface energy of each interface is introduced through a surface stiffness term that depends on the surface Lamé constants and the local tangent plane projection. The resulting discrete system (bulk stiffness + surface stiffness) is solved under periodic displacement boundary conditions to extract the effective elastic moduli.

The workflow consists of three stages:
1. Implement the solver (3‑node triangular elements, plane strain, periodic boundary conditions, level‑set geometry, and surface stiffness). Validate it against published benchmark cases for a hexagonal array of circular voids in aluminium.
2. Use the validated solver to carry out a comprehensive set of production simulations spanning hexagonal void arrays (varying radius and volume fraction), a single flattened elliptical void (varying flattening coefficient), and multiple cracks (varying number and orientation).
3. Post‑process the simulation results to obtain the normalized in‑plane bulk modulus k* = K’/K’_M. Compile the values into a CSV file that serves as the scored artifact.

The aluminium matrix is isotropic with Young’s modulus E = 70 GPa and Poisson’s ratio ν = 0.32. Three surface energy cases are considered, defined by the surface Lamé constants λ_s and μ_s:
- K_s’ < 0: λ_s = 3.48912 N/m, μ_s = –6.2178 N/m
- K_s’ > 0: λ_s = 6.842 N/m, μ_s = –0.375 N/m
- K_s’ = 0: λ_s = 0 N/m, μ_s = 0 N/m
where K_s’ = λ_s + 2μ_s is the surface bulk modulus.

## Reproduction target

Your objective is to produce a CSV file `effective_moduli.csv` that contains the normalized in‑plane bulk modulus k* for every configuration listed in the Workflow steps. The solver must be validated against the benchmark cases before running the full production suite. The computed values should faithfully reflect the size‑dependent physics: a critical void radius below which the porous medium becomes stiffer than the matrix, the convergence of the modulus of a flattened void to that of a crack, and the influence of crack orientation and number. The hidden verifier will compare each row of your CSV to reference data (not provided) and score the agreement.

## Assets

- **Python scientific computing packages**: numpy, scipy, matplotlib. Install at runtime.

All other required data (material constants, surface Lamé constants, geometry parameters) are specified below.

## Workflow steps

### Step 1: Implement and validate XFEM‑level‑set homogenization solver
- Role: process
- Action: Implement a 2D plane‑strain periodic homogenization code using 3‑node triangular elements and XFEM with level‑set functions. Include the coherent interface (Laplace–Young) surface energy model: compute the surface stiffness matrix and implement enrichment functions (Moës‑type continuous enrichment for inclusions, indicator enrichment for voids). Validate the solver by computing the in‑plane bulk modulus of a hexagonal array of circular voids (radius R = 1 nm, volume fraction f = 0.2) in aluminium for the three surface energy cases (K_s’ < 0, K_s’ > 0, K_s’ = 0). Compare your computed moduli with the reference values from Yvonnet et al. (2008) and Quang & He (2009); the values should agree within ±10 %. Record the validation check and the obtained moduli in a file.
- Evidence: `/app/outputs/validation_log.txt`

### Step 2: Run all production simulations
- Role: process
- Action: Using the validated solver, run simulations for every configuration listed below. For each case compute the effective in‑plane bulk modulus K’ and the matrix bulk modulus K’_M (derived from E=70 GPa, ν=0.32 under plane strain). Calculate the normalized modulus k* = K’/K’_M. Keep the raw simulation outputs under a directory (e.g., `/app/outputs/simulations/`).

Configurations:
**(A) Hexagonal array of cylindrical voids**
- Fixed volume fraction f = 0.2; void radius R (nm): 0.1, 0.5, 1, 2, 3, 4, 5. For each R, run all three surface cases.
- Fixed radius R = 1 nm; void volume fraction f: 0.1, 0.2, 0.3, 0.4, 0.5, 0.6. For each f, run all three surface cases.

**(B) Single flattened elliptical void**
- Surface fraction index f’ = a/w = 0.4 (w = REV side). Flattening coefficient c = a/b: 1, 2, 5, 10, 20, 30, 40. For each c, compute k* for the three surface cases.

**(C) Multiple cracks (zero surface energy only, λ_s = μ_s = 0)**
- Square REV; total crack length L such that the surface fraction f’ = 0.4. Place n cracks of equal length L/n, where n = 1, 2, 5, 10, 20. For each n, compute k* for three orientation scenarios:
  * all cracks horizontal (0°)
  * all cracks vertical (90°)
  * randomly oriented (average over 5 random realizations)

- Evidence: none

### Step 3: Compile normalized bulk moduli CSV (scored, load-bearing)
- Role: scored (load-bearing)
- Action: From the simulation results, extract the normalized in‑plane bulk modulus k* for every simulation point and write a CSV file. The file must contain one row per configuration, with columns:
  - `case`: a descriptive string (e.g., "hexagonal_R", "hexagonal_f", "flattened_c", "cracks_horizontal", "cracks_vertical", "cracks_random")
  - `K_s_type`: one of `pos`, `neg`, `zero`
  - `parameter_value`: the varying parameter (R in nm, f (dimensionless), c (dimensionless), or n (number of cracks))
  - `normalized_bulk_modulus`: the computed k* (float, dimensionless)
  Ensure consistent spelling and that every configuration run appears.
- Output file: `/app/outputs/effective_moduli.csv`
- Format: csv
- Contract: CSV with the four columns above. All numeric columns must be valid floats.
- Scoring: The hidden verifier compares each row's `normalized_bulk_modulus` to a reference gold value.

## Output files
- `/app/outputs/validation_log.txt` (process evidence)
- `/app/outputs/effective_moduli.csv` (scored artifact)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### effective_moduli.csv
- path: `/app/outputs/effective_moduli.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized in-plane bulk modulus k* = K'/K'_M for all simulated configurations. The verifier compares each row's normalized_bulk_modulus to a hidden gold value within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `case`, `K_s_type`, `parameter_value`, `normalized_bulk_modulus`
  - `units`:
    - `parameter_value`: nm (radius) or dimensionless (f, c, n)
    - `normalized_bulk_modulus`: dimensionless

Notes: Only the numeric value in normalized_bulk_modulus is compared for scoring; the other columns must correctly identify the configuration. The verifier applies a predefined relative tolerance (e.g., 5%) to each value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "effective_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "K_s_type",
          "parameter_value",
          "normalized_bulk_modulus"
        ],
        "units": {
          "parameter_value": "nm (radius) or dimensionless (f, c, n)",
          "normalized_bulk_modulus": "dimensionless"
        }
      },
      "description": "Normalized in-plane bulk modulus k* = K'/K'_M for all simulated configurations. The verifier compares each row's normalized_bulk_modulus to a hidden gold value within a relative tolerance."
    }
  ],
  "notes": "Only the numeric value in normalized_bulk_modulus is compared for scoring; the other columns must correctly identify the configuration. The verifier applies a predefined relative tolerance (e.g., 5%) to each value."
}
```

## How you are scored
The hidden verifier reads `/app/outputs/effective_moduli.csv` and for each row checks whether the `normalized_bulk_modulus` matches the expected value within a predefined relative tolerance. Your total score is the fraction of rows that pass this check. Environmental setup and evidence files do not directly contribute to the reward. Only the numerical accuracy of the reported moduli matters.
