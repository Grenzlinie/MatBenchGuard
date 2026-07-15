# Size-dependent Debye, Einstein temperatures and thermal expansion ratio computation

## Problem background
Nanocrystals exhibit size-dependent thermodynamic properties that deviate from bulk values. Understanding how the Debye temperature, Einstein temperature, and volume thermal expansion coefficient change with nanoparticle diameter and interface condition (free-standing vs. embedded in a matrix) is important for characterizing thermal vibrations and phase stability at the nanoscale. This task requires computing these size-dependent ratios for specific nanocrystal systems using a theoretical model based on a root-mean-square amplitude approach.

## Approach
The model predicts the size-dependent ratios from two dimensionless parameters: a critical diameter D0 and an interface contrast parameter α.

For nanoparticles (dimensionality d = 0), D0 = 2(3‑d)h = 6h, where h is the atomic diameter of the nanocrystal material.

For free-surface nanocrystals (α > 1), α is computed from the vibrational part of the bulk melting entropy:
  α = (2 ΔS_vib(∞) / (3R)) + 1,   with R = 8.314 J mol⁻¹ K⁻¹.
For metallic elements, ΔS_vib(∞) is obtained from the bulk melting enthalpy ΔH_m(∞) and melting temperature T_m(∞):
  ΔS_m(∞) = ΔH_m(∞) / T_m(∞)
  ΔS_pos(∞) = −R (x_A ln x_A + x_B ln x_B),   x_A = 1 / (1 + ΔV_m/V_s),   x_B = 1 − x_A
  ΔS_vib(∞) = ΔS_m(∞) − ΔS_pos(∞)
For semi‑metals (e.g. Se), the electronic contribution is not negligible; as an approximation use ΔS_vib(∞) = ΔS_m(∞).

For nanocrystals embedded in a matrix with a coherent/semi‑coherent interface (α < 1), α is given by:
  α = ½ [ (h_M / h)² (T_m(∞) / T_M(∞)) + 1 ]
where h_M and T_M(∞) are the atomic diameter and bulk melting temperature of the matrix, respectively.

The size-dependent Debye temperature ratio is:
  Θ_D(D) / Θ_D(∞) = sqrt( exp( −(α − 1) / ( (D / D0) − 1 ) ) ).

The Einstein temperature ratio follows the same expression:
  Θ_E(D) / Θ_E(∞) = sqrt( exp( −(α − 1) / ( (D / D0) − 1 ) ) ).

The volume thermal expansion coefficient ratio is:
  α_v(D) / α_v(∞) = exp( (α − 1) / ( (D / D0) − 1 ) ).

Bulk material parameters required for the calculations are given below:

| Material | Θ_D(∞) [K] | T_m(∞) [K] | ΔH_m(∞) [kJ/mol] | ΔV_m/V_s [%] | h [nm] | Notes |
|----------|-------------|-------------|-------------------|---------------|--------|-------|
| Fe       | 388.00      | 1811.00     | 13.80             | 3.4           | 0.2482 | Compute ΔS_vib(∞) via the metallic route (ΔS_pos from ΔV_m/V_s) |
| Se       | 135.90      | 494.00      | 5.40              | –             | 0.4366 | Use ΔS_vib(∞) = ΔS_m(∞) = ΔH_m(∞)/T_m(∞) |
| Pb       | –           | 600.61      | 4.77              | 3.5           | 0.3500 | Compute ΔS_vib(∞) via the metallic route |
| Ar       | 70.00       | 83.80       | –                 | –             | 0.3650 | Used in the embedded case with Al matrix |
| Al (matrix) | –        | 933.47      | –                 | –             | 0.2863 | h_M and T_M(∞) for the Ar/Al embedded calculation |

For each case, compute α and D0 using the appropriate formula and the listed parameters, then evaluate the corresponding ratio expression for a range of nanoparticle diameters D (e.g., 2–100 nm).

## Reproduction target
Compute the size-dependent ratios for the following four cases over a suitable range of nanoparticle diameters (e.g., 2–100 nm) and output the results as CSV files with the specified columns:

1. Debye temperature ratio for Fe free nanoparticles → `/app/outputs/debye_ratio_free_Fe.csv`  
   Columns: `D (nm)`, `Theta_D_ratio (dimensionless)`

2. Debye temperature ratio for Ar nanocrystals embedded in an Al matrix → `/app/outputs/debye_ratio_embedded_ArAl.csv`  
   Columns: `D (nm)`, `Theta_D_ratio (dimensionless)`

3. Einstein temperature ratio for Se free nanoparticles → `/app/outputs/einstein_ratio_Se.csv`  
   Columns: `D (nm)`, `Theta_E_ratio (dimensionless)`

4. Volume thermal expansion coefficient ratio for Se and Pb free nanoparticles → `/app/outputs/alpha_v_ratio_Se_Pb.csv`  
   Columns: `D (nm)`, `element` (either `Se` or `Pb`), `alpha_v_ratio (dimensionless)`

The ratio values are dimensionless; the diameter D is given in nm.

## Assets

- Python 3 and scientific libraries

## Workflow steps

### Step 1: Calculate model parameters α and D0
- Role: process
- Action: Compute the interface contrast parameter α and the critical size D0 for each material case (Fe free, Ar/Al embedded, Se free, Pb free) using the paper's formulas and the bulk thermodynamic parameters provided in the task instruction. This step ensures the correct starting parameters for the subsequent ratio evaluation.
- Evidence: `/app/outputs/params_summary.txt`

### Step 2: Debye temperature ratio for Fe free nanoparticles
- Role: scored (load-bearing)
- Action: Evaluate the size-dependent Debye temperature ratio Θ_D(D)/Θ_D(∞) for Fe free nanoparticles (d=0, α>1) using the paper's formula for a range of nanoparticle diameters D. Write the results to a CSV file.
- Output file: `/app/outputs/debye_ratio_free_Fe.csv`
- Format: csv
- Contract: D (nm), Theta_D_ratio (dimensionless)
- Scoring: scored by hidden verifier

### Step 3: Debye temperature ratio for Ar/Al embedded nanoparticles
- Role: scored
- Action: Evaluate the size-dependent Debye temperature ratio Θ_D(D)/Θ_D(∞) for Ar nanocrystals embedded in an Al matrix (d=0, α<1) using the paper's formula for a range of nanoparticle diameters D. Write to CSV.
- Output file: `/app/outputs/debye_ratio_embedded_ArAl.csv`
- Format: csv
- Contract: D (nm), Theta_D_ratio (dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Einstein temperature ratio for Se nanoparticles
- Role: scored
- Action: Evaluate the size-dependent Einstein temperature ratio Θ_E(D)/Θ_E(∞) for Se free nanoparticles (d=0, α>1) using the paper's formula for a range of nanoparticle diameters D. Write to CSV.
- Output file: `/app/outputs/einstein_ratio_Se.csv`
- Format: csv
- Contract: D (nm), Theta_E_ratio (dimensionless)
- Scoring: scored by hidden verifier

### Step 5: Volume thermal expansion coefficient ratio for Se and Pb nanoparticles
- Role: scored
- Action: Evaluate the size-dependent volume thermal expansion coefficient ratio α_v(D)/α_v(∞) for Se and Pb free nanoparticles (d=0, α>1) using the paper's formula for a range of nanoparticle diameters D. Write to CSV with an additional column identifying the element.
- Output file: `/app/outputs/alpha_v_ratio_Se_Pb.csv`
- Format: csv
- Contract: D (nm), element (Se or Pb), alpha_v_ratio (dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/debye_ratio_free_Fe.csv`
- `/app/outputs/debye_ratio_embedded_ArAl.csv`
- `/app/outputs/einstein_ratio_Se.csv`
- `/app/outputs/alpha_v_ratio_Se_Pb.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### debye_ratio_free_Fe.csv
- path: `/app/outputs/debye_ratio_free_Fe.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Size-dependent Debye temperature ratio for Fe free nanoparticles. The checker recomputes the expected ratio for each diameter and compares the agent's values against the recomputed values within a tolerance.
- schema:
  - `required_columns`: `D (nm)`, `Theta_D_ratio (dimensionless)`
  - `units`:
    - `D (nm)`: nm
    - `Theta_D_ratio (dimensionless)`: dimensionless

### debye_ratio_embedded_ArAl.csv
- path: `/app/outputs/debye_ratio_embedded_ArAl.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Size-dependent Debye temperature ratio for Ar nanocrystals embedded in Al matrix. The checker recomputes and compares.
- schema:
  - `required_columns`: `D (nm)`, `Theta_D_ratio (dimensionless)`
  - `units`:
    - `D (nm)`: nm
    - `Theta_D_ratio (dimensionless)`: dimensionless

### einstein_ratio_Se.csv
- path: `/app/outputs/einstein_ratio_Se.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Size-dependent Einstein temperature ratio for Se free nanoparticles. Checker recomputes and compares.
- schema:
  - `required_columns`: `D (nm)`, `Theta_E_ratio (dimensionless)`
  - `units`:
    - `D (nm)`: nm
    - `Theta_E_ratio (dimensionless)`: dimensionless

### alpha_v_ratio_Se_Pb.csv
- path: `/app/outputs/alpha_v_ratio_Se_Pb.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Size-dependent volume thermal expansion coefficient ratio for Se and Pb free nanoparticles. Checker recomputes and compares.
- schema:
  - `required_columns`: `D (nm)`, `element`, `alpha_v_ratio (dimensionless)`
  - `units`:
    - `D (nm)`: nm
    - `alpha_v_ratio (dimensionless)`: dimensionless

Notes: The agent must compute the ratios for a reasonable range of nanoparticle diameters (e.g., 2–100 nm). The checker will verify both the numerical accuracy (within a tolerance) and the correct trend (decrease with decreasing D for free nanoparticles; increase for embedded). No gold values are revealed in this contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "debye_ratio_free_Fe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "D (nm)",
          "Theta_D_ratio (dimensionless)"
        ],
        "units": {
          "D (nm)": "nm",
          "Theta_D_ratio (dimensionless)": "dimensionless"
        }
      },
      "description": "Size-dependent Debye temperature ratio for Fe free nanoparticles. The checker recomputes the expected ratio for each diameter and compares the agent's values against the recomputed values within a tolerance."
    },
    {
      "file": "debye_ratio_embedded_ArAl.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "D (nm)",
          "Theta_D_ratio (dimensionless)"
        ],
        "units": {
          "D (nm)": "nm",
          "Theta_D_ratio (dimensionless)": "dimensionless"
        }
      },
      "description": "Size-dependent Debye temperature ratio for Ar nanocrystals embedded in Al matrix. The checker recomputes and compares."
    },
    {
      "file": "einstein_ratio_Se.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "D (nm)",
          "Theta_E_ratio (dimensionless)"
        ],
        "units": {
          "D (nm)": "nm",
          "Theta_E_ratio (dimensionless)": "dimensionless"
        }
      },
      "description": "Size-dependent Einstein temperature ratio for Se free nanoparticles. Checker recomputes and compares."
    },
    {
      "file": "alpha_v_ratio_Se_Pb.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "required_columns": [
          "D (nm)",
          "element",
          "alpha_v_ratio (dimensionless)"
        ],
        "units": {
          "D (nm)": "nm",
          "alpha_v_ratio (dimensionless)": "dimensionless"
        }
      },
      "description": "Size-dependent volume thermal expansion coefficient ratio for Se and Pb free nanoparticles. Checker recomputes and compares."
    }
  ],
  "notes": "The agent must compute the ratios for a reasonable range of nanoparticle diameters (e.g., 2–100 nm). The checker will verify both the numerical accuracy (within a tolerance) and the correct trend (decrease with decreasing D for free nanoparticles; increase for embedded). No gold values are revealed in this contract."
}
```

## How you are scored
Your work will be evaluated by a hidden verifier that independently recomputes the expected ratio values for each case using the same model formulas and material parameters. The verifier will compare your CSV outputs against the recomputed values, checking both numerical accuracy and whether the size-dependent trends match the model's predictions. The final reward is a weighted combination of the scores from the four CSV files. Larger weights are assigned to the Debye temperature ratio for Fe free nanoparticles (the main scored artifact). Accurate reproduction of all files yields the highest total score.
