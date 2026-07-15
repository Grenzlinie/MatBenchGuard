# Finite Element Analysis of Stress Concentration in Porous Carbon Nanofibers

## Problem background
Porous carbon nanofibers (CNFs) combine structural reinforcement with high surface area, making them attractive for multifunctional composites such as structural energy storage. However, introducing porosity can compromise mechanical strength due to stress concentrations around pores and a reduction in effective load-bearing cross-section. This task investigates the mechanics of porous hollow CNFs by quantifying the stress concentration and strength reduction caused by ellipsoidal pores using finite element analysis. The goal is to compute the apparent stress concentration factor and relative strength reduction for a baseline porosity case, and to study how these quantities vary with porosity, providing insight into the trade-off between porosity and mechanical performance.

## Approach
A representative volume element (RVE) of a porous hollow CNF shell is modeled with two elongated ellipsoidal pores featuring semi-ellipsoidal caps. The geometry is defined by the pore minor axis r, major axis of the ellipsoidal cap a, and pore length l. For a given area porosity P, the RVE width and height are determined. The material is treated as isotropic linear elastic with a Poisson ratio typical of carbon fibers (ν=0.3). Symmetric and planar constraints are applied, and a small tensile strain is imposed. Linear elastic finite element analysis yields the reaction force and the maximum principal stress. From these, the apparent and true stresses, the apparent stress concentration factor K_apparent = σ_max / σ_apparent, and the relative strength reduction Δσ/σ₀ = (K_apparent - 1) / K_apparent are calculated. A parametric sweep is performed by varying porosity while keeping pore shape parameters constant, to obtain K_apparent and strength reduction over the range 5% to 25%.

## Reproduction target
Implement the FEA model and compute the apparent stress concentration factor K_apparent and the relative strength reduction Δσ/σ₀ for a baseline porous shell CNF with porosity P = 0.2 (area porosity), pore aspect ratio l/r = 20, and cap geometry parameter a/r = 3. Additionally, perform a parametric study by varying porosity from 0.05 to 0.25 while keeping l/r and a/r fixed, and output the corresponding K_apparent and strength reduction values. The results must be saved in the specified output files (base_case_results.json and parametric_porosity.csv) so that a hidden verifier can compare them to independently derived reference values and curves.

## Assets

- FEniCS (or equivalent open-source FEA library): https://fenicsproject.org/
- Python with numpy/scipy: numpy, scipy

## Workflow steps

### Step 1: Set up RVE geometry and FEA model
- Role: process
- Action: Define the RVE geometry for a porous hollow CNF with two elongated ellipsoidal pores (semi-ellipsoidal caps). Use the parameters porosity P=0.2 (area porosity), l/r=20, a/r=3. Set r to an arbitrary length scale (e.g., 1 mm). Determine RVE width w and height h such that P = πr²/(4hw). Assign isotropic linear elastic material with Poisson's ratio ν=0.3 (Young's modulus any reasonable value; stress concentration factors are independent of absolute value). Implement the FEA model in an open-source solver with symmetric boundary conditions on x=0, y=w, z=h; planar constraint on y=0; and 1% tensile strain applied on x=l.
- Evidence: `/app/outputs/fea_model.log`

### Step 2: Run FEA simulations for base case and porosity sweep
- Role: process
- Action: Run the FEA simulation for the base case (P=0.2) and for at least five additional porosity values spanning 0.05 to 0.25 (achieved by varying w while keeping r, a, l constant). For each simulation, obtain the resultant force F_d and the maximum principal stress σ_max. Save all raw simulation results as evidence.
- Evidence: `/app/outputs/simulation_results.json`

### Step 3: Compute stress concentration factors and strength reduction for base case
- Role: scored (load-bearing)
- Action: From the base case simulation (P=0.2): compute total cross-sectional area A_total = h·w, pore area A_pore = πr²/4. Compute apparent stress σ_app = F_d / A_total, true stress σ_true = F_d / (A_total - A_pore). Compute apparent stress concentration factor K_apparent = σ_max / σ_app and strength reduction Δσ/σ₀ = (K_apparent - 1)/K_apparent. Write the numeric results to base_case_results.json.
- Output file: `/app/outputs/base_case_results.json`
- Format: json
- Contract: {"porosity": 0.2, "l_over_r": 20, "a_over_r": 3, "K_apparent": <float>, "strength_reduction": <float>}
- Scoring: scored by hidden verifier

### Step 4: Generate parametric curve of strength reduction vs porosity
- Role: scored (load-bearing)
- Action: For each porosity value in the sweep (at least 0.05, 0.10, 0.15, 0.20, 0.25), compute K_apparent and strength_reduction using the same method as Step 3. Write a CSV file with columns porosity, K_apparent, strength_reduction.
- Output file: `/app/outputs/parametric_porosity.csv`
- Format: csv
- Contract: columns: porosity (float, fraction), K_apparent (float), strength_reduction (float, fraction)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/base_case_results.json`
- `/app/outputs/parametric_porosity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### base_case_results.json
- path: `/app/outputs/base_case_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Baseline FEA results: apparent stress concentration factor and relative strength reduction for porosity 0.2, l/r=20, a/r=3.
- schema:
  - `type`: object
  - `required`:
    - `porosity`: float
    - `l_over_r`: float
    - `a_over_r`: float
    - `K_apparent`: float
    - `strength_reduction`: float

### parametric_porosity.csv
- path: `/app/outputs/parametric_porosity.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Parametric sweep: K_apparent and strength_reduction vs porosity (5% to 25%). Checker recomputes MAE against a reference curve.
- schema:
  - `type`: table
  - `required_columns`: `porosity`, `K_apparent`, `strength_reduction`
  - `units`:
    - `porosity`: fraction
    - `K_apparent`: dimensionless
    - `strength_reduction`: fraction

Notes: The checker compares the baseline K_apparent and strength_reduction to hidden paper values with tolerances that account for numerical differences, ensures self-consistency (strength_reduction = (K-1)/K), and computes MAE between the agent's strength_reduction-vs-porosity curve and a reference digitized curve from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "base_case_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "porosity": "float",
          "l_over_r": "float",
          "a_over_r": "float",
          "K_apparent": "float",
          "strength_reduction": "float"
        }
      },
      "description": "Baseline FEA results: apparent stress concentration factor and relative strength reduction for porosity 0.2, l/r=20, a/r=3."
    },
    {
      "file": "parametric_porosity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "porosity",
          "K_apparent",
          "strength_reduction"
        ],
        "units": {
          "porosity": "fraction",
          "K_apparent": "dimensionless",
          "strength_reduction": "fraction"
        }
      },
      "description": "Parametric sweep: K_apparent and strength_reduction vs porosity (5% to 25%). Checker recomputes MAE against a reference curve."
    }
  ],
  "notes": "The checker compares the baseline K_apparent and strength_reduction to hidden paper values with tolerances that account for numerical differences, ensures self-consistency (strength_reduction = (K-1)/K), and computes MAE between the agent's strength_reduction-vs-porosity curve and a reference digitized curve from the paper."
}
```

## How you are scored
Your submitted artifacts are evaluated by an automated hidden verifier. Each scored output file (base_case_results.json and parametric_porosity.csv) is checked against a hidden reference. The verifier compares your reported baseline K_apparent and strength reduction to the expected values within tolerances that account for numerical implementation differences, checks self-consistency (strength_reduction = (K_apparent - 1) / K_apparent), and computes the mean absolute error between your strength reduction vs. porosity curve and a reference digitized curve from the original study. Your final reward is a weighted combination of these checks. Simply reporting numbers does not guarantee a high score; correct execution of the FEA workflow as described is necessary to achieve accurate results.
