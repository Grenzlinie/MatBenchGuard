# Dislocation shear stress and equilibrium spacing in elastic half-cylinders

## Problem background
When two crystals with slightly mismatched lattices are joined, an array of interfacial dislocations forms to accommodate the misfit. In a finite deposit on a substrate, the shear stress that drives dislocations inward is modified by the free lateral boundary. This task computes the relaxed shear stress distribution along the interface and the resulting equilibrium spacing of misfit dislocations for a model of two elastic half-cylinders with a free cylindrical boundary.

## Approach
The task is based on a continuum elasticity model of two misfitting half-cylinders. The derivation proceeds as follows: First, the unrelaxed shear stress along the interface is computed for the case where the cylindrical boundary is constrained, using a line of infinitesimal dislocations. Then the unrelaxed stresses on the free cylindrical boundary are expressed as Fourier series. A corrective stress function is constructed to cancel these boundary tractions while remaining regular inside the cylinder. Solving the resulting linear equations yields closed-form coefficients for the corrective field. Adding the corrective stress to the embedded solution gives the relaxed shear stress along the interface, expressed as a series in (x/R). Finally, the equilibrium spacing of a pair of misfit dislocations is obtained from the force balance between the dislocation interaction and the calculated shear stress.

## Reproduction target
Compute the dimensionless relaxed shear stress p_rθ/F along the interface as a function of x/R for the model, and compute the equilibrium spacing X of two misfit dislocations for the parameters b=1.0, R=1.0, ε=0.01, μ=1.0, ν=0.3.

## Assets

- Python 3 with numpy and math: python>=3.8, numpy

## Workflow steps

### Step 1: Embedded shear stress
- Role: process
- Action: Implement the unrelaxed embedded shear stress along the interface: p_rθ_embedded(x) = F * ln((R + x)/(R - x)), where F = εμ/(2π(1-ν)). This function will be used later to compare with the relaxed result.
- Evidence: none

### Step 2: Boundary traction Fourier series
- Role: process
- Action: Express the unrelaxed stresses on the cylindrical boundary r=R as Fourier series in θ. The series for the shear stress σ_rθ at r=R is: (b/(εD)) p_rθ = (1/3)cosθ + (π/2) sgn(y) sin2θ + sum_{t=1}^∞ [1/(2t-1) + 1/(2t+3)] cos(2t+1)θ. The normal stress has a similar sine series. Use these series to identify the coefficients that the corrective stress must cancel.
- Evidence: none

### Step 3: Corrective stress coefficients
- Role: process
- Action: Set up the linear equations ensuring that the corrective stresses cancel the boundary tractions when r=R and remain regular inside the cylinder. Solve to obtain the coefficients a_t = -(2t-3)/((2t-1) 2t (2t+3)) and b_t = 1/((2t+2)(2t+3)).
- Evidence: none

### Step 4: Relaxed interface shear stress
- Role: scored (load-bearing)
- Action: Combine the embedded shear stress and the corrective stress contribution to obtain the relaxed shear stress p_rθ(x) along the interface. The dimensionless expression is: (b/(εD)) p_rθ(x) = 16/15 (x/R) + sum_{t=1}^∞ [(2t+2)/((2t+1)(2t+3)(2t+5))] (x/R)^{2t+1}. Truncate the series when additional terms contribute less than 1e-8. Compute p_rθ/F = (b/(εD)) p_rθ (since F = εD/b). Output a CSV with two columns: x_over_R (values from 0.0 to 1.0 in steps of 0.1) and p_rθ_over_F.
- Output file: `/app/outputs/relaxed_shear_stress.csv`
- Format: csv
- Contract: Two columns: x_over_R (float), p_rθ_over_F (float). Comma-separated, header row included.
- Scoring: scored by hidden verifier

### Step 5: Equilibrium spacing
- Role: scored
- Action: Using the derived shear stress behavior and the force balance, compute the equilibrium spacing X = sqrt(15 b R / (32 ε)) for the parameters b=1.0, R=1.0, ε=0.01, μ=1.0, ν=0.3. Write the result to a text file as 'X = <value>'.
- Output file: `/app/outputs/equilibrium_spacing.txt`
- Format: txt
- Contract: A single line containing 'X = <value>', where value is a floating-point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_shear_stress.csv`
- `/app/outputs/equilibrium_spacing.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_shear_stress.csv
- path: `/app/outputs/relaxed_shear_stress.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed shear stress along the interface as a function of x/R
- schema:
  - `type`: table
  - `required_columns`: `x_over_R`, `p_rθ_over_F`

### equilibrium_spacing.txt
- path: `/app/outputs/equilibrium_spacing.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Equilibrium spacing of two misfit dislocations
- schema:
  - `type`: text
  - `content_pattern`: X = <float>

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_shear_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_over_R",
          "p_rθ_over_F"
        ]
      },
      "description": "Relaxed shear stress along the interface as a function of x/R"
    },
    {
      "file": "equilibrium_spacing.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "content_pattern": "X = <float>"
      },
      "description": "Equilibrium spacing of two misfit dislocations"
    }
  ],
  "notes": ""
}
```

## How you are scored
Each scored workflow step produces an artifact (CSV or text file). A hidden checker will independently recompute the expected results using the same mathematical model but with a much larger series truncation and analytical expressions. The checker compares your submitted values to these recomputed benchmarks. For the shear stress CSV, it checks that the values at multiple x/R positions (including the edge) are within acceptable tolerances. For the equilibrium spacing, it verifies the computed X against the analytic formula with the given parameters. Your final score is a weighted sum of the per-step scores. Correctness and accuracy of the numerical results is essential; you must execute the computations faithfully. Providing the correct file format and structure is a prerequisite, but scoring is based on the numerical values.
