# Compressibility of pyrochlore-type MgZrSi2O7 from equation-of-state and linear compressibility fitting

## Problem background
Pyrochlore-type MgZrSi₂O₇ is a silicate with the cubic pyrochlore structure (space group Fd-3m) that can be synthesized at high pressure and temperature. Understanding its mechanical response under hydrostatic compression is of interest for comparing it with other pyrochlore materials. The compressibility of a crystalline solid is commonly characterized by the parameters of an equation of state (EOS): the zero-pressure unit-cell volume V₀, the isothermal bulk modulus K_T, and its first pressure derivative K_T′. Additionally, the pressure dependence of the lattice parameter a can be described by a quadratic polynomial that yields linear compressibility coefficients k_a and k_a′, from which the volume compressibility k_V = 3 k_a is obtained. This task reproduces the determination of these quantities from experimental pressure–volume–lattice data collected up to approximately 24 GPa.

## Approach
The bundled pressure–volume data set (see Assets) provides, at each applied pressure P (in GPa), the unit-cell volume V (in Å³) and the cubic lattice parameter a (in Å). Two independent regression analyses are performed.

1. **Linear compressibility**: The a-vs-P data are fitted by a quadratic polynomial
   \( a(P) = a_0 - k_a a_0 P + k_a' a_0 P^2 \).
   From the fitted coefficients the linear compressibility \( k_a \) and its pressure derivative \( k_a' \) are obtained; the volume compressibility is \( k_V = 3 k_a \).

2. **Equation of state**: The P–V data are fitted to the third-order Birch–Murnaghan equation of state,
   \( P = 3 K_T f_E (1+2 f_E)^{5/2} \left[1 + \frac{3}{2}(K_T' - 4) f_E\right] \),
   where \( f_E = \frac{1}{2}\left[(V_0/V)^{2/3} - 1\right] \) is the Eulerian finite strain.
   The fit yields \( V_0 \), \( K_T \), and \( K_T' \). A second fit with \( K_T' \) held fixed at 4 gives another estimate of \( K_T \).

All fits use nonlinear least-squares minimization; in addition to the best-fit parameters, the standard errors (uncertainties) from the fits are reported. The computations can be performed with any reliable nonlinear least-squares implementation (e.g., SciPy’s `curve_fit`).

## Reproduction target
Using the supplied pressure–volume data (pressure, volume, lattice parameter), perform both the quadratic fit of the lattice parameter and the third-order Birch–Murnaghan EOS fit as described, and produce a single JSON file `/app/outputs/eos_fit_results.json` that contains the following numeric quantities:

- `V0` (Å³) and `V0_error`
- `KT` (GPa) and `KT_error`
- `KT_prime` and `KT_prime_error`
- `KT_fixed4` (GPa) and `KT_fixed4_error` (KT obtained with K_T′ = 4)
- `ka` (GPa⁻¹) and `ka_error`
- `ka_prime` (GPa⁻²) and `ka_prime_error`
- `k_V` (GPa⁻¹)

All values must be floats. The JSON keys must exactly match the names listed above.

## Assets

- Pressure-volume measurement data (Table 2)
- SciPy (nonlinear least-squares fitting): scipy

## Workflow steps

### Step 1: Perform quadratic fit of lattice parameter vs pressure and third-order Birch-Murnaghan EOS fitting
- Role: scored (load-bearing)
- Action: Load pressure-volume data from data/pv_data.csv. Perform a quadratic polynomial fit of lattice parameter a versus pressure to obtain linear compressibility coefficients k_a, k_a' and volume compressibility k_V = 3*k_a. Then fit the pressure-volume data to the third-order Birch-Murnaghan equation of state using nonlinear least squares (SciPy's curve_fit) to extract zero-pressure volume V0, isothermal bulk modulus KT, its first pressure derivative KT', and their standard errors. Also compute KT with KT' fixed at 4 and its error. Write all parameters and their uncertainties into a single JSON file.
- Output file: `/app/outputs/eos_fit_results.json`
- Format: json
- Contract: JSON object with keys: V0 (Å³), V0_error, KT (GPa), KT_error, KT_prime, KT_prime_error, KT_fixed4 (GPa), KT_fixed4_error, ka (GPa^-1), ka_error, ka_prime (GPa^-2), ka_prime_error, k_V (GPa^-1). All values are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eos_fit_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eos_fit_results.json
- path: `/app/outputs/eos_fit_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the fitted zero-pressure volume, isothermal bulk modulus, its first pressure derivative, the bulk modulus with fixed K_T'=4, the linear compressibility coefficients from the quadratic fit of lattice parameter, and all associated standard errors.
- schema:
  - `type`: object
  - `required`:
    - `V0`: float (Å^3)
    - `V0_error`: float (Å^3)
    - `KT`: float (GPa)
    - `KT_error`: float (GPa)
    - `KT_prime`: float
    - `KT_prime_error`: float
    - `KT_fixed4`: float (GPa)
    - `KT_fixed4_error`: float (GPa)
    - `ka`: float (GPa^-1)
    - `ka_error`: float (GPa^-1)
    - `ka_prime`: float (GPa^-2)
    - `ka_prime_error`: float (GPa^-2)
    - `k_V`: float (GPa^-1)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The bundled data file provides pressure (GPa), lattice parameter a (Å), and volume V (Å³) from Table 2 of the paper. The agent must perform both regression tasks and output a single JSON with all parameters and their uncertainties. The exact fitting library (e.g., SciPy) is not mandated; any equivalent nonlinear least-squares implementation is acceptable. The output is compared to the paper-reported numbers within hidden tolerances that accommodate numerical and implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eos_fit_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "V0": "float (Å^3)",
          "V0_error": "float (Å^3)",
          "KT": "float (GPa)",
          "KT_error": "float (GPa)",
          "KT_prime": "float",
          "KT_prime_error": "float",
          "KT_fixed4": "float (GPa)",
          "KT_fixed4_error": "float (GPa)",
          "ka": "float (GPa^-1)",
          "ka_error": "float (GPa^-1)",
          "ka_prime": "float (GPa^-2)",
          "ka_prime_error": "float (GPa^-2)",
          "k_V": "float (GPa^-1)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Contains the fitted zero-pressure volume, isothermal bulk modulus, its first pressure derivative, the bulk modulus with fixed K_T'=4, the linear compressibility coefficients from the quadratic fit of lattice parameter, and all associated standard errors."
    }
  ],
  "notes": "The bundled data file provides pressure (GPa), lattice parameter a (Å), and volume V (Å³) from Table 2 of the paper. The agent must perform both regression tasks and output a single JSON with all parameters and their uncertainties. The exact fitting library (e.g., SciPy) is not mandated; any equivalent nonlinear least-squares implementation is acceptable. The output is compared to the paper-reported numbers within hidden tolerances that accommodate numerical and implementation differences."
}
```

## How you are scored
A hidden verifier reads the agent’s submitted `eos_fit_results.json`. The verifier compares the reported values of the fitted parameters — `V0`, `KT`, `KT_prime`, `KT_fixed4`, `ka`, `ka_prime`, `k_V` — to hidden reference values that correspond to the correct result from the same data. For each parameter, the verifier checks whether the reported value lies within a predefined tolerance that accounts for legitimate differences in fitting implementation details. The final reward is proportional to the number of these parameters that fall within their tolerance window; a submission that fails to include the required fields or contains structurally invalid data receives zero credit. Performing the actual fits is essential; simply guessing or copying known numbers is unlikely to succeed because the tolerance windows are not disclosed.
