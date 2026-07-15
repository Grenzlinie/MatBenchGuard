# Thermoelastic equation-of-state fitting for sodium majorite garnet

## Problem background
Sodium-bearing majoritic garnet (Na-majorite) is a key phase in the Earth's transition zone. Its thermoelastic properties – isothermal bulk modulus, pressure and temperature derivatives, thermal expansion coefficients, and the Grüneisen parameter – are essential for geobarometry and for modelling the composition and dynamics of the deep mantle. This task is based on *in situ* synchrotron X-ray diffraction experiments that measured pressure-volume-temperature (P‑V‑T) data for synthetic Na-majorite up to ~21 GPa and ~1673 K. The dataset is provided; the goal is to determine the equation-of-state parameters that best describe the pressure and temperature response of the mineral.

## Approach
The thermoelastic parameters are derived by a series of non‑linear least‑squares fits to three established equations of state, using only the provided P‑V‑T dataset and standard numerical libraries (numpy, scipy).

1.  **Room‑temperature Birch‑Murnaghan (BM) fit** – all data measured at 300 K are fitted to a third‑order Birch‑Murnaghan equation of state to obtain the ambient unit‑cell volume V₀, the isothermal bulk modulus K₀ at 300 K, and its pressure derivative K′₀.
2.  **High‑temperature Birch‑Murnaghan (HTBM) fit** – the complete P‑V‑T dataset is fitted to an extended Birch‑Murnaghan formulation in which the bulk modulus depends linearly on temperature and the thermal expansion coefficient α = a + bT. The ambient volume V₀ is fixed to the value obtained in step 1, while K₀, K′₀, the temperature derivative (∂K/∂T)_P, and the expansion parameters a and b are adjusted simultaneously.
3.  **Mie–Grüneisen–Debye (MGD) fit** – the dataset is further fitted to a MGD equation of state that expresses total pressure as the sum of a static (room‑temperature) pressure and a thermal pressure. The Debye temperature is fixed at 890 K and the volume‑dependence parameter q is fixed at 1. Using the V₀, K₀, and K′₀ obtained from the HTBM fit as fixed values, the fit determines the Grüneisen parameter γ₀.

All fits follow the forms of the equations as described in the geophysical literature; the agent must implement these forms accurately and apply a standard non‑linear least‑squares method (e.g., scipy.optimize.curve_fit).

## Reproduction target
From the provided P‑V‑T dataset (Table 1, supplied inline as CSV), perform the three fits described above and collect the resulting parameters into a single JSON file, `/app/outputs/fitted_parameters.json`. The file must contain the following nine floating‑point values:
- `V0` (ambient volume, Å³)
- `BM300_K0` (isothermal bulk modulus from the room‑temperature BM fit, GPa)
- `BM300_Kp` (pressure derivative from the room‑temperature BM fit, dimensionless)
- `HTBM_K0` (bulk modulus from the HTBM fit, GPa)
- `HTBM_Kp` (pressure derivative from the HTBM fit, dimensionless)
- `HTBM_dKdT` (temperature derivative of bulk modulus, GPa/K)
- `HTBM_a` (linear thermal‑expansion coefficient, /K)
- `HTBM_b` (quadratic thermal‑expansion coefficient, /K²)
- `MGD_gamma0` (Grüneisen parameter, dimensionless).

All values must be computed solely from the given dataset and the fitting procedures; no external parameter values or pre‑fitted results are allowed.

## Assets

- Na-majorite P-V-T data (Table 1)
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare P-V-T dataset
- Role: process
- Action: Parse the provided P-V-T data (inline CSV), extract the room-temperature subset (T = 300 K) and the full dataset for subsequent fits. Validate that the required columns (pressure, temperature, volume) are present.
- Evidence: `/app/outputs/data_prep.log`

### Step 2: Fit equations of state and output parameters
- Role: scored
- Action: Using the room-temperature subset, least-squares fit the third-order Birch-Murnaghan equation to obtain ambient volume V0, isothermal bulk modulus K0,300, and its pressure derivative K'0,300. Then, using the full P-V-T dataset and fixing V0 to the value just obtained, fit the high-temperature Birch-Murnaghan equations (temperature-dependent bulk modulus and thermal expansion) to obtain K0,300, K'0,300, temperature derivative (∂K/∂T)_P, and thermal expansion coefficients a, b. Finally, fit the Mie-Grüneisen-Debye equation with Debye temperature θ0 = 890 K and q = 1 fixed, and using V0, K0,300, K'0,300 from the HTBM fit as fixed parameters, to obtain the Grüneisen parameter γ0. Write all results into fitted_parameters.json.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: JSON object with keys: V0 (float, Å^3), BM300_K0 (float, GPa), BM300_Kp (float, dimensionless), HTBM_K0 (float, GPa), HTBM_Kp (float, dimensionless), HTBM_dKdT (float, GPa/K), HTBM_a (float, 1/K), HTBM_b (float, 1/K^2), MGD_gamma0 (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted parameters from room-temperature Birch-Murnaghan, high-temperature Birch-Murnaghan, and Mie-Grüneisen-Debye equation-of-state fits. All values are floats. The checker compares each parameter to the paper-reported reference value within an appropriate tolerance window; the tolerance windows are hidden.
- schema:
  - `type`: object
  - `required`:
    - `V0`: float (Å^3)
    - `BM300_K0`: float (GPa)
    - `BM300_Kp`: float (dimensionless)
    - `HTBM_K0`: float (GPa)
    - `HTBM_Kp`: float (dimensionless)
    - `HTBM_dKdT`: float (GPa/K)
    - `HTBM_a`: float (1/K)
    - `HTBM_b`: float (1/K^2)
    - `MGD_gamma0`: float (dimensionless)

Notes: Only the fitted_parameters.json file is scored. The data_prep.log evidence from the process step is not scored and exists only to document that the data preparation step was executed.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "V0": "float (Å^3)",
          "BM300_K0": "float (GPa)",
          "BM300_Kp": "float (dimensionless)",
          "HTBM_K0": "float (GPa)",
          "HTBM_Kp": "float (dimensionless)",
          "HTBM_dKdT": "float (GPa/K)",
          "HTBM_a": "float (1/K)",
          "HTBM_b": "float (1/K^2)",
          "MGD_gamma0": "float (dimensionless)"
        }
      },
      "description": "Fitted parameters from room-temperature Birch-Murnaghan, high-temperature Birch-Murnaghan, and Mie-Grüneisen-Debye equation-of-state fits. All values are floats. The checker compares each parameter to the paper-reported reference value within an appropriate tolerance window; the tolerance windows are hidden."
    }
  ],
  "notes": "Only the fitted_parameters.json file is scored. The data_prep.log evidence from the process step is not scored and exists only to document that the data preparation step was executed."
}
```

## How you are scored
A hidden verifier will load your `fitted_parameters.json` and compare each of the nine parameters to a hidden reference value. The comparison uses a tolerance window appropriate for the numerical spread expected across different fitting implementations. You receive partial credit for each parameter that falls within its tolerance. The total reward is the fraction of parameters that pass, weighted more heavily toward the primary HTBM and MGD parameters. Reporting values that simply copy numbers from the paper without actually running the fits is not sufficient: the verifier expects values that could realistically be obtained by an honest, independent least‑squares re‑implementation.
