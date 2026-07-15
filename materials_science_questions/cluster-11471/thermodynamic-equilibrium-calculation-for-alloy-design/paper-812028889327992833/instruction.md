# Determination of the effective diffusion coefficient controlling pearlite dissolution under rapid heating

## Problem background
Surface hardening of steels by rapid heating involves fast austenitization followed by quenching. The kinetics of austenite formation from a starting microstructure of pearlite and proeutectoid ferrite are critical for predicting case depth and optimizing processing parameters. In the first stage of austenitization, lamellar pearlite dissolves to form austenite. An analytic expression has been derived from diffusion theory that relates the volume fraction of pearlite transformed to austenite ($f_{p\to\gamma}$) to the maximum temperature of the thermal cycle ($T_\text{max}$), the dwell time above the critical temperature ($\tau$), the cementite lamella thickness ($s_\text{cem}$), and an effective carbon diffusion coefficient ($D$): $f_{p\to\gamma} = (T_\text{max}/A_{\text{e1}} - 1) \cdot \sqrt{D \cdot \tau} / s_\text{cem}$, where $A_{\text{e1}}$ is the equilibrium austenite start temperature (727 °C). However, it is unclear which physical diffusion coefficient—carbon diffusion in austenite, in ferrite, or some combination—controls the transformation under different peak temperature conditions. This task investigates that question by computing the predicted transformation curves for five candidate diffusion coefficients and comparing them to reference simulation data.

## Approach
We use the analytic expression $f_{p\to\gamma} = (T_\text{max}/A_{\text{e1}} - 1) \cdot \sqrt{D \cdot \tau} / s_\text{cem}$ with $A_{\text{e1}} = 1000.15\,\text{K}$ and $s_\text{cem} = 25\,\text{nm}$ to compute the volume fraction of pearlite transformed to austenite as a function of dwell time. Five candidate effective diffusion coefficients are considered, all derived from published Arrhenius parameters for carbon diffusion in austenite ($D_0 = 2.3\times10^{-5}\,\text{m}^2\!/\text{s}$, $Q = 137700\,\text{J/mol}$) and in ferrite ($D_0 = 1.1\times10^{-6}\,\text{m}^2\!/\text{s}$, $Q = 87500\,\text{J/mol}$): the average austenite diffusion coefficient $\bar{D}_\gamma$ (integrated over $[A_{\text{e1}}, T_\text{max}]$), the austenite coefficient evaluated at the peak temperature $D_\gamma^{T_\text{max}}$, the corresponding ferrite quantities $\bar{D}_\alpha$ and $D_\alpha^{T_\text{max}}$, and the mixed average $(\bar{D}_\gamma + \bar{D}_\alpha)/2$. Curves are generated for four maximum temperatures (750, 800, 850, 900 °C) over a logarithmically spaced range of dwell times from approximately $1\times10^{-5}\,\text{s}$ to $0.5\,\text{s}$. The resulting data set will be compared to reference points to infer which diffusion coefficient best describes the transformation at each temperature, revealing whether the controlling mechanism shifts with peak temperature.

## Reproduction target
Produce a CSV file containing the computed $f_{p\to\gamma}$ values for every combination of the four maximum temperatures (750, 800, 850, 900 °C) and the five candidate diffusion coefficient labels (`Dγ_avg`, `Dγ_Tmax`, `Dα_avg`, `Dα_Tmax`, `D_mixed`) over a dense set of dwell times. This file serves as the input to a hidden evaluation that determines, for each $T_\text{max}$, which candidate coefficient yields predictions closest to reference simulation data, thereby identifying the apparent controlling diffusion mechanism at each temperature regime.

## Assets

- Python scientific computing stack (NumPy, SciPy, Matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Compute f_p→γ curves from analytic expression
- Role: scored (load-bearing)
- Action: For each maximum temperature (750, 800, 850, 900 °C) and each candidate diffusion coefficient label (Dγ_avg, Dγ_Tmax, Dα_avg, Dα_Tmax, D_mixed), compute the volume fraction of pearlite transformed to austenite f_p→γ as a function of dwell time τ using the analytic expression f_p→γ = (T_max/A_e1 - 1) * sqrt(D·τ) / s_cem. Use A_e1 = 727 °C (1000.15 K), s_cem = 25 nm. Compute the average austenite and ferrite diffusion coefficients (D̅_γ, D̅_α) by numerically integrating the Arrhenius law D(T) = D0 exp(-Q/(R T)) over the interval [A_e1, T_max] using the austenite parameters D0=2.3e-5 m²/s, Q=137700 J/mol and the ferrite parameters D0=1.1e-6 m²/s, Q=87500 J/mol. Compute peak-temperature coefficients D_γ^Tmax and D_α^Tmax by evaluating D(T) directly at T_max. Compute the mixed average D_mixed = (D̅_γ + D̅_α)/2. Generate a dense, logarithmically spaced set of τ values from approximately 1×10⁻⁵ s to 0.5 s, and write one row per (T_max_C, D_candidate, tau_s, f_p_gamma) to /app/outputs/computed_curves.csv.
- Output file: `/app/outputs/computed_curves.csv`
- Format: csv
- Contract: Columns: T_max_C (float, temperature in °C), D_candidate (string, one of: Dγ_avg, Dγ_Tmax, Dα_avg, Dα_Tmax, D_mixed), tau_s (float, time in seconds), f_p_gamma (float, dimensionless volume fraction).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_curves.csv
- path: `/app/outputs/computed_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Analytically computed pearlite transformation curves for five candidate diffusion coefficients at four maximum temperatures. The checker recomputes the RMSE against hidden reference points and determines which candidate has the minimum RMSE at each temperature to validate the claimed temperature-dependent shift in controlling diffusion mechanism.
- schema:
  - `type`: table
  - `required_columns`: `T_max_C`, `D_candidate`, `tau_s`, `f_p_gamma`

Notes: The scored outcome is the identity of the best-fit candidate diffusion coefficient per T_max, not the absolute f_p→γ values. The hidden checker bundles digitized reference points from the paper's Figure 8 and does not access external data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_max_C",
          "D_candidate",
          "tau_s",
          "f_p_gamma"
        ]
      },
      "description": "Analytically computed pearlite transformation curves for five candidate diffusion coefficients at four maximum temperatures. The checker recomputes the RMSE against hidden reference points and determines which candidate has the minimum RMSE at each temperature to validate the claimed temperature-dependent shift in controlling diffusion mechanism."
    }
  ],
  "notes": "The scored outcome is the identity of the best-fit candidate diffusion coefficient per T_max, not the absolute f_p→γ values. The hidden checker bundles digitized reference points from the paper's Figure 8 and does not access external data."
}
```

## How you are scored
A hidden verifier will read your computed_curves.csv and, for each $T_\text{max}$, interpolate your $f_{p\to\gamma}$ curves at a set of reference dwell times (not disclosed to you). It will compute the root‑mean‑square error (RMSE) between your curve and the reference points for each of the five candidate diffusion coefficients, then determine which candidate has the lowest RMSE at each temperature. The overall reward is based on how well the pattern of best‑fit candidates you implicitly produce matches the physical behavior established by detailed moving‑boundary simulations. Correctly identifying the dominant diffusion coefficient at each temperature (i.e., which candidate yields the lowest RMSE) earns full credit; partial credit is awarded for partially correct patterns or correct ordering of RMSE values. Your absolute $f_{p\to\gamma}$ values are not scored directly—only the resulting ranking of candidate coefficients matters.
