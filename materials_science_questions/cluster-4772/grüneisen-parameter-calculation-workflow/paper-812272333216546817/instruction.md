# Linear Correlation of Specific Heat and Raman Frequency Shifts in Solid Ammonia I

## Problem background
In the spectroscopic modification of the first Pippard relation, the isobaric specific heat \(C_p\) of a solid near a phase transition is predicted to vary linearly with the Raman frequency shift variable \(X \equiv (1/\nu)(\partial \nu/\partial T)_p\) for a given vibrational mode. This relation is tested for the rotatory (librational) mode (~280 cm⁻¹) in ammonia solid I close to the melting point at three fixed pressures: 0, 1.93, and 3.07 kbar. Verifying the linear correlation and extracting the resulting slope \(\mathrm{d}P_m/\mathrm{d}T\) and intercept \((\mathrm{d}S/\mathrm{d}T)_m\) provides a quantitative check of the spectroscopic Pippard relation and serves as the computational target of this reproduction.

## Approach
The method computes the specific heat \(C_p\) and the frequency-shift variable \(X\) for the librational mode at each pressure from published thermodynamic empirical relations and a volume‑dependent Raman frequency model, then performs a linear regression of \(C_p\) vs \(X\) to obtain the slope and intercept.

**Thermodynamic inputs**
- Melting pressure slope: \(\mathrm{d}P_m/\mathrm{d}T(T) = 1.967 \times 10^{-8}\, T^{2.96}\) (bar/K).
- Melting temperatures \(T_m\): 192.5 K at 0 kbar, 210 K at 1.93 kbar, 217.34 K at 3.07 kbar.
- Constant amplitude \(k = 0.0137\) and critical exponent \(\gamma = 0.49\) (from the divergence of isothermal compressibility).
- Critical volume \(V_c(T) = 27.79 - 0.0316\,T\) (cm³/mol).

**Thermodynamic quantities at a given pressure** (computed for a set of temperatures approaching \(T_m\)):
1. Solid volume: \(V_s(T) = V_c(T)\,\exp\!\big[-k(1-\gamma)^{-1}\,(\mathrm{d}P_m/\mathrm{d}T)^{1-\gamma}\,(T_m - T)^{1-\gamma}\big]\).
2. Thermal expansivity: \(\alpha_p(T) = k\,(\mathrm{d}P_m/\mathrm{d}T)^{1-\gamma}\,(T_m - T)^{-\gamma} + V_c'(T)/V_c(T)\), where \(V_c'(T) = -0.0316\).
3. Isothermal compressibility: \(\kappa_T(T) = k\,(\mathrm{d}P_m/\mathrm{d}T)^{-\gamma}\,(T_m - T)^{-\gamma}\).
4. Isobaric specific heat: \(C_p(T) = T\,V_s(T)\,\alpha_p(T)^2 / \kappa_T(T)\).

**Raman frequency of the librational mode**
- Model: \(\nu_p(T) = \Delta_p + A(P) + \nu_m\,\exp\!\big[-\gamma_p\,\ln(V_p(T)/V_m)\big]\) with \(V_p(T) = V_s(T)\).
- Parameters: \(\gamma_p = 0.8\), \(\nu_m = 276.31\) cm⁻¹, \(V_m = 21.61\) cm³/mol.
- The constant term \(\Delta_p + A(P)\) is expressed as \(\Delta_p + a_0 + a_1 P + a_2 P^2\) with \(\Delta_p + a_0 = -10.47\) cm⁻¹, \(a_1 = -0.858\) cm⁻¹ K⁻¹, \(a_2 = 0.344\) cm⁻¹ K⁻².

**Frequency‑shift variable**
Compute \(X(T) = (1/\nu_p)\,(\partial\nu_p/\partial T)_p\) by numerically differentiating \(\nu_p(T)\).

**Linear regression**
For each pressure, fit \(C_p\) as a linear function of \(X\): \(C_p = (\mathrm{d}P_m/\mathrm{d}T)\,(-T V_s/\gamma_p)\,X + T\,(\mathrm{d}S/\mathrm{d}T)_m\). The slope and intercept from the fit directly give \(\mathrm{d}P_m/\mathrm{d}T\) (bar/K) and \((\mathrm{d}S/\mathrm{d}T)_m\) (J/(mol·K²)).

## Reproduction target
Compute the arrays of isobaric specific heat \(C_p\) and frequency‑shift variable \(X\) for the librational mode at the three fixed pressures (0, 1.93, 3.07 kbar) over a set of temperatures approaching the respective melting temperatures. For each pressure, perform a linear regression of \(C_p\) vs \(X\) to obtain the slope \(\mathrm{d}P_m/\mathrm{d}T\) (bar/K) and the intercept \((\mathrm{d}S/\mathrm{d}T)_m\) (J/(mol·K²)). Write the temperature arrays, \(C_p\) arrays, \(X\) arrays, and the fitted parameters for all three pressures into \texttt{/app/outputs/results.json} following the exact schema given in the output contract.

## Assets

- Python 3 interpreter
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute thermodynamic and spectroscopic quantities
- Role: process
- Action: Implement the thermodynamic relations and the empirical frequency model from the paper. Compute the solid volume V_s(T), thermal expansivity α_p(T), isothermal compressibility κ_T(T), and isobaric specific heat C_p(T) for the librational mode at the three fixed pressures (0, 1.93, 3.07 kbar) using the published constants k=0.0137, γ=0.49, the melting curve slope dP_m/dT from Eq. (3.2), critical volume V_c(T) from Eq. (3.4), and related formulas. Compute the librational Raman frequency ν_p(T) from Eq. (2.5) with the coefficients given in Table 2 (γ_p=0.8, ν_m=276.31 cm⁻¹, Δ_p+a0=-10.47 cm⁻¹, a1=-0.858, a2=0.344) and the solid volume V_p(T) (same as V_s). Numerically differentiate to obtain X=(1/ν)(∂ν/∂T)_p. Store the resulting C_p and X arrays for each pressure for use in the next step.
- Evidence: none

### Step 2: Linear regression and scored output
- Role: scored (load-bearing)
- Action: For each pressure, perform a linear regression of C_p versus X using the data computed in the previous step. Write a JSON file containing the temperatures, C_p array, X array, the fitted slope dPm_dT (bar/K), and the fitted intercept dS_dT_m (J/(mol·K²)) for each pressure.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Top-level keys: '0kbar', '1.93kbar', '3.07kbar'. Each value is an object with keys: 'temperatures' (list of floats, K), 'C_p' (list of floats, J/(mol·K)), 'X' (list of floats, K⁻¹), 'dPm_dT' (float, bar/K), 'dS_dT_m' (float, J/(mol·K²)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Computed (C_p, X) data and the linear-fit parameters (slope dPm_dT and intercept dS_dT_m) for each of the three pressures.
- schema:
  - `type`: object
  - `required`: `0kbar`, `1.93kbar`, `3.07kbar`
  - `properties`:
    - `0kbar`:
      - `type`: object
      - `required`: `C_p`, `X`, `dPm_dT`, `dS_dT_m`
      - `properties`:
        - `temperatures`:
          - `type`: array
          - `items`: number
          - `unit`: K
        - `C_p`:
          - `type`: array
          - `items`: number
          - `unit`: J/(mol·K)
        - `X`:
          - `type`: array
          - `items`: number
          - `unit`: K⁻¹
        - `dPm_dT`:
          - `type`: number
          - `unit`: bar/K
        - `dS_dT_m`:
          - `type`: number
          - `unit`: J/(mol·K²)
    - `1.93kbar`:
      - `type`: object
      - `required`: `C_p`, `X`, `dPm_dT`, `dS_dT_m`
      - `properties`:
        - `temperatures`:
          - `type`: array
          - `items`: number
          - `unit`: K
        - `C_p`:
          - `type`: array
          - `items`: number
          - `unit`: J/(mol·K)
        - `X`:
          - `type`: array
          - `items`: number
          - `unit`: K⁻¹
        - `dPm_dT`:
          - `type`: number
          - `unit`: bar/K
        - `dS_dT_m`:
          - `type`: number
          - `unit`: J/(mol·K²)
    - `3.07kbar`:
      - `type`: object
      - `required`: `C_p`, `X`, `dPm_dT`, `dS_dT_m`
      - `properties`:
        - `temperatures`:
          - `type`: array
          - `items`: number
          - `unit`: K
        - `C_p`:
          - `type`: array
          - `items`: number
          - `unit`: J/(mol·K)
        - `X`:
          - `type`: array
          - `items`: number
          - `unit`: K⁻¹
        - `dPm_dT`:
          - `type`: number
          - `unit`: bar/K
        - `dS_dT_m`:
          - `type`: number
          - `unit`: J/(mol·K²)

Notes: All constants and functional forms are stated in the paper appendix supplied with the task. The checker will recompute the linear regression from the provided C_p and X arrays and compare the resulting slopes to hidden reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "0kbar",
          "1.93kbar",
          "3.07kbar"
        ],
        "properties": {
          "0kbar": {
            "type": "object",
            "required": [
              "C_p",
              "X",
              "dPm_dT",
              "dS_dT_m"
            ],
            "properties": {
              "temperatures": {
                "type": "array",
                "items": "number",
                "unit": "K"
              },
              "C_p": {
                "type": "array",
                "items": "number",
                "unit": "J/(mol·K)"
              },
              "X": {
                "type": "array",
                "items": "number",
                "unit": "K⁻¹"
              },
              "dPm_dT": {
                "type": "number",
                "unit": "bar/K"
              },
              "dS_dT_m": {
                "type": "number",
                "unit": "J/(mol·K²)"
              }
            }
          },
          "1.93kbar": {
            "type": "object",
            "required": [
              "C_p",
              "X",
              "dPm_dT",
              "dS_dT_m"
            ],
            "properties": {
              "temperatures": {
                "type": "array",
                "items": "number",
                "unit": "K"
              },
              "C_p": {
                "type": "array",
                "items": "number",
                "unit": "J/(mol·K)"
              },
              "X": {
                "type": "array",
                "items": "number",
                "unit": "K⁻¹"
              },
              "dPm_dT": {
                "type": "number",
                "unit": "bar/K"
              },
              "dS_dT_m": {
                "type": "number",
                "unit": "J/(mol·K²)"
              }
            }
          },
          "3.07kbar": {
            "type": "object",
            "required": [
              "C_p",
              "X",
              "dPm_dT",
              "dS_dT_m"
            ],
            "properties": {
              "temperatures": {
                "type": "array",
                "items": "number",
                "unit": "K"
              },
              "C_p": {
                "type": "array",
                "items": "number",
                "unit": "J/(mol·K)"
              },
              "X": {
                "type": "array",
                "items": "number",
                "unit": "K⁻¹"
              },
              "dPm_dT": {
                "type": "number",
                "unit": "bar/K"
              },
              "dS_dT_m": {
                "type": "number",
                "unit": "J/(mol·K²)"
              }
            }
          }
        }
      },
      "description": "Computed (C_p, X) data and the linear-fit parameters (slope dPm_dT and intercept dS_dT_m) for each of the three pressures."
    }
  ],
  "notes": "All constants and functional forms are stated in the paper appendix supplied with the task. The checker will recompute the linear regression from the provided C_p and X arrays and compare the resulting slopes to hidden reference values."
}
```

## How you are scored
A hidden verifier reads \texttt{results.json}. For each pressure it independently recomputes a linear regression on the \(C_p\) and \(X\) arrays you provided to obtain a slope and intercept. These recomputed values are then compared to hidden reference values (derived from the original study) with an appropriate tolerance. Full credit is awarded if the recomputed slopes and intercepts lie within the tolerance; otherwise partial credit may be given based on the deviation. The verifier also checks that the linear fits are consistent with the reported data. The overall reward is a weighted combination of the scores across the three pressures, with the slopes carrying the largest weight.
