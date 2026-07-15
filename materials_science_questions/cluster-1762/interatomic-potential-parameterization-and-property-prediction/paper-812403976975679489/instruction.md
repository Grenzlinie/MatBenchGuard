# Elastic Moduli and Pressure Derivatives of Rare Gas Solids

## Problem background
Rare gas solids (Ne, Ar, Kr, Xe) are ideal model systems for studying van der Waals interactions and anharmonic lattice dynamics. Knowledge of their elastic moduli and how those moduli change under pressure is central for testing interatomic potential models and for constructing accurate equations of state. The present task addresses the determination of the isothermal bulk modulus, two shear moduli, and their first and second pressure derivatives for these four solids using a three-body interaction model.

## Approach
The reproduction adopts a two-stage workload. First, fit the parameters of a potential energy model that includes a modified van der Waals attraction (with three-body overlap corrections from variable induced dipoles), a short-range Born–Mayer repulsion, and a zero-point vibrational term. The fitting uses published low-temperature experimental data — lattice constant, second-order elastic constants (C11, C12, C44), Debye temperature, and Grüneisen parameter — by solving the zero-pressure equilibrium conditions that couple these quantities. Second, evaluate the analytic expressions derived from this potential for the isothermal bulk modulus K_T, the shear moduli C_S and C_44, and their first- and second-order pressure derivatives at zero pressure. All computations are for the four rare gas solids Ne, Ar, Kr, Xe.

## Reproduction target
Compute, for Ne, Ar, Kr, and Xe at zero pressure, the following quantities from the fitted potential model: isothermal bulk modulus K_T (GPa), shear moduli C_S and C_44 (GPa), first pressure derivatives dK_T/dP, dC_S/dP, dC44'/dP (dimensionless), and second pressure derivatives d²K_T/dP², d²C_S/dP², d²C44'/dP² (GPa⁻¹). Collect the results in a structured JSON file (`rgs_properties.json`).

## Assets

- Experimental data for rare gas solids (Bell & Zucker, 1976)
- Python scientific stack

## Workflow steps

### Step 1: Fit interatomic potential parameters
- Role: process
- Action: Using the experimental data for Ne, Ar, Kr, Xe (lattice constant, elastic constants C11, C12, C44, Debye temperature, Grüneisen parameter) from Bell & Zucker (1976), solve the zero-pressure equilibrium relations to determine the short-range force constants A, B, the modified van der Waals parameter α'/a^8, and the three-body overlap terms. From the exponential forms compute the higher-order constants C, D and all required derivatives. Save the full set of model parameters to fitted_parameters.json.
- Evidence: `/app/outputs/fitted_parameters.json`

### Step 2: Compute elastic properties and pressure derivatives
- Role: scored (load-bearing)
- Action: Using the fitted parameters, evaluate the analytic formulas for the isothermal bulk modulus K_T, shear moduli C_S and C_44, and their first and second pressure derivatives (dK_T/dP, dC_S/dP, dC_44'/dP, d^2K_T/dP^2, d^2C_S/dP^2, d^2C_44'/dP^2) at zero pressure for Ne, Ar, Kr, and Xe. Assemble all results into a single JSON file.
- Output file: `/app/outputs/rgs_properties.json`
- Format: json
- Contract: Object with top-level keys Ne, Ar, Kr, Xe. Each value is an object with numeric fields: K_T, C_S, C_44, dK_T_dP, dC_S_dP, dC44_prime_dP, d2K_T_dP2, d2C_S_dP2, d2C44_prime_dP2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rgs_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rgs_properties.json
- path: `/app/outputs/rgs_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Final elastic moduli and pressure derivatives at P=0 for Ne, Ar, Kr, Xe computed from the fitted potential.
- schema:
  - `type`: object
  - `required`:
    - `Ne`: object
    - `Ar`: object
    - `Kr`: object
    - `Xe`: object
  - `items`:
    - `K_T`: number (GPa)
    - `C_S`: number (GPa)
    - `C_44`: number (GPa)
    - `dK_T_dP`: number (dimensionless)
    - `dC_S_dP`: number (dimensionless)
    - `dC44_prime_dP`: number (dimensionless)
    - `d2K_T_dP2`: number (GPa^-1)
    - `d2C_S_dP2`: number (GPa^-1)
    - `d2C44_prime_dP2`: number (GPa^-1)

Notes: All quantities computed from analytic expressions with fitted parameters. Units: moduli in GPa, first-order derivatives dimensionless, second-order derivatives in GPa^-1. The hidden checker compares each value to the paper's reported values using a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rgs_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Ne": "object",
          "Ar": "object",
          "Kr": "object",
          "Xe": "object"
        },
        "items": {
          "K_T": "number (GPa)",
          "C_S": "number (GPa)",
          "C_44": "number (GPa)",
          "dK_T_dP": "number (dimensionless)",
          "dC_S_dP": "number (dimensionless)",
          "dC44_prime_dP": "number (dimensionless)",
          "d2K_T_dP2": "number (GPa^-1)",
          "d2C_S_dP2": "number (GPa^-1)",
          "d2C44_prime_dP2": "number (GPa^-1)"
        }
      },
      "description": "Final elastic moduli and pressure derivatives at P=0 for Ne, Ar, Kr, Xe computed from the fitted potential."
    }
  ],
  "notes": "All quantities computed from analytic expressions with fitted parameters. Units: moduli in GPa, first-order derivatives dimensionless, second-order derivatives in GPa^-1. The hidden checker compares each value to the paper's reported values using a relative tolerance."
}
```

## How you are scored
A hidden verifier will read your `rgs_properties.json` and compare each reported quantity for each element to reference values obtained from a correct implementation of the model. The comparison uses a relative tolerance; if all quantities fall within the tolerance, you receive full credit. As deviations grow larger, the score decreases proportionally, down to zero for large errors. The final reward is a single number between 0 and 1.
