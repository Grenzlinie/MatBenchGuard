# Generalized Maxwell Scheme for Effective Elastic Properties of Porous Media

## Problem background
Predicting the effective elastic properties of porous materials, such as the effective Young's modulus as a function of porosity, is a central problem in micromechanics. The Maxwell homogenization scheme, which equates the far elastic field produced by a set of inhomogeneities to that produced by an equivalent homogeneous fictitious domain, provides a closed-form prediction when reformulated in terms of compliance contribution tensors. This reformulation allows explicit evaluation of the effective compliance for composites containing pores of various shapes.

## Approach
Use the generalized Maxwell scheme in terms of compliance contribution tensors for identical randomly oriented spheroidal pores. First, compute the compliance contribution tensor of a single spheroidal pore (aspect ratio 0.7) from the Eshelby solution, expressed via standard shape functions. Then, obtain the isotropic average to find two scalars B and C that represent the pore contributions to the bulk and shear compliance. Together with the shape factors of a spherical representative volume element, the Maxwell equations yield the effective bulk and shear moduli as rational functions of porosity. The normalized effective Young's modulus is derived from these effective moduli using standard isotropic elasticity relations.

## Reproduction target
Compute the normalized Young's modulus (E_eff / E_0) as a function of porosity for a material containing randomly oriented spheroidal pores of aspect ratio 0.7. Use matrix elastic constants E0 = 70 GPa and Poisson's ratio ν0 = 0.33. Evaluate the effective modulus at least 20 evenly spaced porosity values from 0 to 0.8 inclusive, and write a CSV file with columns 'porosity' and 'E_eff_over_E0'.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute normalized Young's modulus vs. porosity
- Role: scored (load-bearing)
- Action: Implement the Maxwell homogenization scheme for a material containing identical randomly oriented spheroidal pores, using the compliance contribution tensor formulation. Compute the normalized effective Young's modulus (E_eff/E_0) as a function of porosity. Use matrix elastic constants E0=70 GPa, nu0=0.33, and pore aspect ratio 0.7. Compute for a range of porosity values from 0 to 0.8 (at least 20 evenly spaced points). Output a CSV file with columns 'porosity' and 'E_eff_over_E0'.
- Output file: `/app/outputs/step_01_E_eff_normalized.csv`
- Format: csv
- Contract: Two columns: 'porosity' (float, range 0 to 0.8 inclusive, at least 20 evenly spaced points) and 'E_eff_over_E0' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_E_eff_normalized.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_E_eff_normalized.csv
- path: `/app/outputs/step_01_E_eff_normalized.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Normalized effective Young's modulus (E_eff/E_0) as a function of porosity for spheroidal pores of aspect ratio 0.7, computed via the generalized Maxwell homogenization scheme.
- schema:
  - `type`: table
  - `required_columns`: `porosity`, `E_eff_over_E0`
  - `units`:
    - `porosity`: dimensionless (ratio)
    - `E_eff_over_E0`: dimensionless (ratio)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_E_eff_normalized.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "porosity",
          "E_eff_over_E0"
        ],
        "units": {
          "porosity": "dimensionless (ratio)",
          "E_eff_over_E0": "dimensionless (ratio)"
        }
      },
      "description": "Normalized effective Young's modulus (E_eff/E_0) as a function of porosity for spheroidal pores of aspect ratio 0.7, computed via the generalized Maxwell homogenization scheme."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submitted CSV will be scored by a hidden verifier. The verifier independently recomputes the normalized Young's modulus from the same analytical model at several secret porosity points. It reads your curve, interpolates the E_eff/E_0 values at those points, and compares them to the recomputed reference values. The reward is proportional to the number of hidden points that agree within the verifier's predetermined relative tolerance.
