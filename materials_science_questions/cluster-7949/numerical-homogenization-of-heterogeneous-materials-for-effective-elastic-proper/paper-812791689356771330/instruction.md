# Multiscale SAM for Contact of Inhomogeneous Materials: Accuracy Validation and Clustering Effect Trends

## Problem background
Semi-analytical models (SAMs) efficiently solve contact problems of inhomogeneous materials, but when many small particles are present, their computational cost becomes prohibitive. This paper introduces a multiscale SAM that uses two-level meshes (macroscopic and microscopic) to accelerate simulations while retaining microscopic stress details. The model homogenizes microscopic representative volume elements (RVEs) to obtain effective macroscopic eigenstrain coefficients and influence coefficients, solves the contact on the coarse mesh, and then recovers fine-scale fields. This task aims to reproduce the model's accuracy validation against a conventional single-scale SAM, and to investigate through simulation how particle clustering affects stress concentrations and contact fatigue indicators.

## Approach
The core of the multiscale method is a domain decomposition approach: a coarse macroscopic mesh captures the global contact behaviour and pressure distribution, while local microscopic meshes, each representing a small volume containing many particles, provide detailed stress/strain fields. First, the microscopic mesh is used to compute the effective mapping from macroscopic initial strain to average eigenstrain (A' matrix) and to build homogenised influence coefficients for eigenstress and surface displacement computations on the macroscopic mesh. Then an iterative contact solver (conjugate gradient with DC‑FFT/DCR‑FFT acceleration) runs on the macroscopic mesh, coupling contact pressure and eigenstrains until convergence. After the macroscopic solution, the microscopic stress fields are recovered in each RVE.

For validation, the multiscale model is compared to a conventional SAM in which all inhomogeneities are explicitly discretised. The comparison is done for a case with 512 evenly spaced stiff cuboidal particles inside a cubic cluster. Model accuracy is quantified by the relative errors of von Mises stress. The clustering study varies the cluster volume fraction Vf_U (100%, 50%, 25%) for both stiff and compliant particle materials, with 10 random cluster realisations per condition to account for statistical variability. For each configuration several stress metrics are extracted: maximum von Mises stress in the matrix and in inhomogeneities, maximum principal stress in inhomogeneities, and the stress volumetric integral over the entire calculation zone.

## Reproduction target
The objective is twofold. First, validate the multiscale SAM accuracy: for the specified validation case, compute the von Mises stress field with both the multiscale model and the conventional SAM, then output the maximum relative error and the average relative error of von Mises stress as a CSV file. Second, perform the clustering study: for each combination of Vf_U (100%, 50%, 25%) and material type (stiff and compliant), generate 10 random cluster distributions and run the multiscale model to obtain per-replicate values of maximum von Mises stress in matrix, maximum von Mises stress in inhomogeneities, maximum principal stress in inhomogeneities, and the stress volumetric integral. Store all per-replicate results in a CSV file. The verifier will subsequently assess whether the computed stress metrics exhibit the trends expected by the paper.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Develop multiscale SAM components
- Role: process
- Action: Implement the core numerical routines: generation of random particle distributions within a microscopic RVE; computing microscopic half-space influence coefficients T and G; solving the microscopic equivalent inclusion method to obtain the macroscopic equivalent-eigenstrain mapping and building macroscopic influence coefficients; implementing the iterative macroscopic contact solver using conjugate gradient and DC-FFT/DCR-FFT accelerations; implementing microscopic field recovery.
- Evidence: `/app/outputs/model_implemented.txt`

### Step 2: Conventional SAM reference simulation
- Role: process
- Action: Implement the single-scale semi-analytical model that explicitly resolves inhomogeneities. Run it for the validation case: 512 evenly spaced cuboidal inhomogeneities of size 0.02a0 inside a 0.64a0^3 cubic cluster centered at (0,0,0.48a0), with matrix/particle properties E_I/E_M=4, nu=0.3, a0=0.1mm, P0=2350MPa. Compute the full von Mises stress field and contact pressure distribution as the reference.
- Evidence: `/app/outputs/ref_validation_stress.npy`

### Step 3: Validate multiscale SAM accuracy
- Role: scored (load-bearing)
- Action: Run the new multiscale model for the same validation case, obtain the von Mises stress field, and compute the maximum relative error and average relative error of von Mises stress compared to the conventional SAM reference. Save the error metrics to a CSV file.
- Output file: `/app/outputs/validation_errors.csv`
- Format: csv
- Contract: case (str), max_error_percent (float), avg_error_percent (float)
- Scoring: scored by hidden verifier

### Step 4: Generate cluster configurations for parametric study
- Role: process
- Action: For cluster volume fractions Vf_U = 100%, 50%, 25% and both stiff (E_I/E_M=4) and compliant (E_I/E_M=0.5) cases, create 10 random distributions of particle clusters within the calculation zone as described in the method (total particle volume fraction 2%, cluster radius 0.32a0, particle size 0.01a0). Use a fixed set of seeds to ensure reproducibility. Save a summary of the generated configurations.
- Evidence: `/app/outputs/configurations_summary.json`

### Step 5: Run multiscale model for all cluster conditions
- Role: process
- Action: For each generated configuration, execute the full multiscale pipeline (homogenization, macroscopic contact simulation, microscopic field recovery) and extract: maximum von Mises stress in matrix, maximum von Mises stress in inhomogeneities, maximum principal stress in inhomogeneities, and the stress volumetric integral. Store all per-replicate raw results in a CSV file.
- Evidence: `/app/outputs/raw_cluster_results.csv`

### Step 6: Compute clustering trends and final output
- Role: scored (load-bearing)
- Action: From the raw per‑replicate results, compute the stress metrics for each cluster condition. Write the per‑replicate data (with replicate index) to a final CSV file.
- Output file: `/app/outputs/clustering_results.csv`
- Format: csv
- Contract: Vf_U (str), material (str), replicate (int), max_vM_matrix (float), max_vM_inhomo (float), max_principal_inhomo (float), stress_vol_int (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/validation_errors.csv`
- `/app/outputs/clustering_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### validation_errors.csv
- path: `/app/outputs/validation_errors.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Validation error metrics: maximum and average relative error of von Mises stress compared to the conventional SAM reference.
- schema:
  - `type`: table
  - `required_columns`: `case`, `max_error_percent`, `avg_error_percent`
  - `units`:
    - `max_error_percent`: percent
    - `avg_error_percent`: percent

### clustering_results.csv
- path: `/app/outputs/clustering_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Per‑replicate stress metrics for each cluster volume fraction and material type, used to verify monotonic trends with cluster concentration.
- schema:
  - `type`: table
  - `required_columns`: `Vf_U`, `material`, `replicate`, `max_vM_matrix`, `max_vM_inhomo`, `max_principal_inhomo`, `stress_vol_int`
  - `units`:
    - `max_vM_matrix`: MPa or normalized by P0
    - `max_vM_inhomo`: MPa or normalized by P0
    - `max_principal_inhomo`: MPa or normalized by P0
    - `stress_vol_int`: MPa*mm^3 or normalized

Notes: The clustering_results.csv must contain data for both stiff (E_I/E_M=4) and compliant (E_I/E_M=0.5) cases, with 10 replicates each at Vf_U=100%, 50%, 25%. The trends are verified by computing means from the per‑replicate data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "validation_errors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "max_error_percent",
          "avg_error_percent"
        ],
        "units": {
          "max_error_percent": "percent",
          "avg_error_percent": "percent"
        }
      },
      "description": "Validation error metrics: maximum and average relative error of von Mises stress compared to the conventional SAM reference."
    },
    {
      "file": "clustering_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Vf_U",
          "material",
          "replicate",
          "max_vM_matrix",
          "max_vM_inhomo",
          "max_principal_inhomo",
          "stress_vol_int"
        ],
        "units": {
          "max_vM_matrix": "MPa or normalized by P0",
          "max_vM_inhomo": "MPa or normalized by P0",
          "max_principal_inhomo": "MPa or normalized by P0",
          "stress_vol_int": "MPa*mm^3 or normalized"
        }
      },
      "description": "Per‑replicate stress metrics for each cluster volume fraction and material type, used to verify monotonic trends with cluster concentration."
    }
  ],
  "notes": "The clustering_results.csv must contain data for both stiff (E_I/E_M=4) and compliant (E_I/E_M=0.5) cases, with 10 replicates each at Vf_U=100%, 50%, 25%. The trends are verified by computing means from the per‑replicate data."
}
```

## How you are scored
The task is scored by a hidden verifier that independently evaluates the two scored output files. For the validation file, the verifier compares the reported max_error_percent and avg_error_percent to the paper's reference values using appropriate tolerances; a result that matches or exceeds the reference accuracy earns full credit, and credit decreases as the errors get larger. For the clustering results file, the verifier groups the data by material type and computes the mean of each stress metric per Vf_U level, then checks the required monotonic trends (e.g., whether certain metrics strictly increase or decrease as Vf_U decreases). Each trend carries equal weight within the clustering portion. The total reward is a weighted sum of the validation score (weight 0.4) and the clustering score (weight 0.6). Only honest, computationally reproduced results can satisfy these checks; reporting the paper's numbers without running the model is not sufficient.
