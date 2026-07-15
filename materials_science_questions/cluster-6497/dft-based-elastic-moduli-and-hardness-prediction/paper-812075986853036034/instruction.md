# Fitting nanoring condition and predicting nanohelix thicknesses in ZnO nanostructures

## Problem background
ZnO nanorings and nanohelices have been observed experimentally. To understand their formation, a theoretical model is constructed that considers the competition between elastic energy, spontaneous polarization-induced surface energy, volume energy, and defect-induced energy. This model yields necessary conditions for the existence of these nanostructures, relating their geometric parameters (radius, thickness, pitch). The key question is whether a single set of parameters can simultaneously fit the experimental data for nanorings and predict the thicknesses of nanohelices, thereby demonstrating the consistency and explanatory power of the model. This task reproduces the computational fitting and prediction steps to test that hypothesis.

## Approach
The shape formation energy of ZnO nanobelts is expressed in terms of the central-line curvature and torsion. For nanorings (constant radius, zero torsion), the energy minimization leads to a relation linking the ring thickness t and radius R: (t/R)^3 = ξ (t/R) + η / R, where ξ, η are combinations of material/energy parameters. We will fit this equation to a set of experimental nanoring (R, t) measurements using linear regression (treating (t/R) and 1/R as independent variables) to obtain ξ and η. Another parameter, χ, is defined as the supremum of t/R among the nanoring data. For nanohelices (constant radius r0 and pitch p), the condition from energy minimization involves the pitch angle φ = arctan(p/(2π r0)), the fitted parameters, and the thickness t. Using an effective Young's modulus of 50 GPa and Poisson ratio ν=0.3 (giving β = 2/(1+ν)), the nanohelix condition is solved numerically to find the possible thickness values. The normalized shape energy is also computed as a consistency check. The analysis uses two datasets: nanoring sizes (R, t) and nanohelix dimensions (r0, p), both provided as CSV files.

## Reproduction target
Using the provided experimental nanoring data (radius and thickness), fit the equation (t/R)^3 = ξ (t/R) + η / R to obtain the dimensionless parameter ξ and the length parameter η. Determine χ as the maximum t/R among all nanoring data points. Then, for each nanohelix (given its radius r0 and pitch p), use the fitted ξ, η, χ and the nanohelix condition to solve for its thickness t (identify the physically relevant range, if multiple solutions exist) and compute the normalized shape energy. The final deliverables are two JSON files: fitted_parameters.json (ξ, η, χ) and predicted_thicknesses.json (for each helix: helix_id, r0, p, the minimum and maximum viable thickness, and the normalized shape energy).

## Assets

- ZnO nanoring experimental data (R, t)
- ZnO nanohelix experimental data (r0, p)
- NumPy: https://pypi.tuna.tsinghua.edu.cn/simple
- SciPy: https://pypi.tuna.tsinghua.edu.cn/simple
- Pandas: https://pypi.tuna.tsinghua.edu.cn/simple

## Workflow steps

### Step 1: Fit nanoring condition and determine χ
- Role: scored
- Action: Load nanoring data (radius R, thickness t) from nanoring_data.csv. Fit the equation (t/R)^3 = ξ (t/R) + η / R using linear regression (treat (t/R) and 1/R as independent variables) to obtain ξ and η. Determine χ as the maximum value of t/R among all data points. Write the fitted parameters to fitted_parameters.json.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {"xi": float, "eta": float, "chi": float}
- Scoring: scored by hidden verifier

### Step 2: Estimate nanohelix thicknesses and shape energies
- Role: scored
- Action: Load nanohelix data (r0, p) from nanohelix_data.csv. For each helix, compute pitch angle φ = arctan(p/(2π r0)). Using the fitted parameters ξ, η, χ from step_01, β = 2/(1+ν) with ν=0.3, solve the nanohelix condition equation cos^4 φ + (3β-2) sin^2 φ cos^2 φ + (2χ r0/t) sin^2 φ = r0^2 (η + ξ t)/t^3 to find the root(s) t (identify the physically relevant range). Compute the normalized shape energy F_norm = cos^4 φ + (2β-1)/4 sin^2 2φ - (χ r0/t) cos 2φ. Write results to predicted_thicknesses.json, including for each helix: helix_id (1,2,3 corresponding to the rows in the data), r0, p, t_min, t_max, and F_norm.
- Output file: `/app/outputs/predicted_thicknesses.json`
- Format: json
- Contract: [{"helix_id": int, "r0": float, "p": float, "t_min": float, "t_max": float, "F_norm": float}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/predicted_thicknesses.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted parameters from the nanoring condition equation (ξ, η) and the maximum t/R value (χ).
- schema:
  - `type`: object
  - `required`:
    - `xi`: float (dimensionless)
    - `eta`: float (nm)
    - `chi`: float (dimensionless)

### predicted_thicknesses.json
- path: `/app/outputs/predicted_thicknesses.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Predicted thickness ranges and normalized shape energies for the three nanohelices reported in the literature.
- schema:
  - `type`: array
  - `items`:
    - `helix_id`: int
    - `r0`: float (nm)
    - `p`: float (nm)
    - `t_min`: float (nm)
    - `t_max`: float (nm)
    - `F_norm`: float (dimensionless)

Notes: The predicted_thicknesses artifact must be a plain JSON array, not an object with a 'helices' key.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "xi": "float (dimensionless)",
          "eta": "float (nm)",
          "chi": "float (dimensionless)"
        }
      },
      "description": "Fitted parameters from the nanoring condition equation (ξ, η) and the maximum t/R value (χ)."
    },
    {
      "file": "predicted_thicknesses.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "helix_id": "int",
          "r0": "float (nm)",
          "p": "float (nm)",
          "t_min": "float (nm)",
          "t_max": "float (nm)",
          "F_norm": "float (dimensionless)"
        }
      },
      "description": "Predicted thickness ranges and normalized shape energies for the three nanohelices reported in the literature."
    }
  ],
  "notes": "The predicted_thicknesses artifact must be a plain JSON array, not an object with a 'helices' key."
}
```

## How you are scored
A hidden verifier will independently evaluate your submitted artifacts. For fitted_parameters.json, it will compare your ξ, η, and χ values to reference values derived from the paper's analysis, with tolerances that account for numerical differences. For predicted_thicknesses.json, it will check that your predicted thickness ranges and shape energies are consistent with the paper's results. Each scored artifact contributes a weighted share to the final reward; simply reporting numbers without correctly performing the fitting and solving steps will not suffice.
