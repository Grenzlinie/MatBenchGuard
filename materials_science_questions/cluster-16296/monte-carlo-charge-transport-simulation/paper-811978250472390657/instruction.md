# Hot Carrier Photogradient EMF Simulation in n-Ge

## Problem background
In n-type germanium at room temperature, experimental measurements of the photogradient electromotive force (e.m.f.) of hot carriers under a high microwave electric field show a departure from simple heating models at field strengths above about 5 kV/cm. It is hypothesised that this departure arises because electrons in the populated <111> valleys can undergo non‑equivalent intervalley scattering into the higher‑energy <100> minima, increasing the energy‑loss rate. This task requires you to compute the microwave‑cycle‑averaged photogradient e.m.f. ⟨U_fg⟩_T as a function of electric field, both with and without the additional non‑equivalent intervalley scattering term, in order to assess its effect on the field dependence.

## Approach
The electron temperature T_n is obtained by solving the steady‑state energy balance equation e μ E^2 + ⟨dε/dt⟩ = 0, where ⟨dε/dt⟩ is the total average energy‑loss rate of electrons. The loss rate sums contributions from intravalley scattering by acoustic and optical phonons, equivalent intervalley scattering, and, optionally, non‑equivalent intervalley (n‑i) scattering. Intravalley and equivalent intervalley rates are computed using standard semiconductor formulas with the material parameters listed below. The n‑i loss rate is taken from the derivation reported in the literature; its explicit expression is:

$$\left\langle\frac{d \varepsilon}{dt}\right\rangle_{\mathrm{ni}} = \frac{\sqrt{2} N D_{\mathrm{ni}}^2 m_{\|}^{1/2} m_{\perp} (k_0 T_n)^{1/2}}{\pi^{3/2} \hbar^2 \rho \left[\exp\left(\frac{\hbar \omega_{\mathrm{ni}}}{k_0 T_0}\right)-1\right] \exp\left(\frac{\Delta \varepsilon - \hbar \omega_{\mathrm{ni}}}{2 k_0 T_n}\right)}\times\\
\times \left[ \frac{\Delta \varepsilon - \hbar \omega_{\mathrm{ni}}}{2 k_0 T_n} K_1\!\left(\frac{\Delta \varepsilon - \hbar \omega_{\mathrm{ni}}}{2 k_0 T_n}\right) - \frac{\Delta \varepsilon + \hbar \omega_{\mathrm{ni}}}{2 k_0 T_n} K_1\!\left(\frac{\Delta \varepsilon + \hbar \omega_{\mathrm{ni}}}{2 k_0 T_n}\right) \exp\!\left(\frac{\hbar \omega_{\mathrm{ni}}}{k_0 T_0} - \frac{\hbar \omega_{\mathrm{ni}}}{k_0 T_n}\right) \right],$$ 

where $N$ is the number of equivalent $\langle 100\rangle$ minima, $D_{\mathrm{ni}}$ is the coupling constant, $m_{\|}$ and $m_{\perp}$ are the electron effective masses in the $\langle 111\rangle$ valleys, $\hbar \omega_{\mathrm{ni}}$ is the n‑i phonon energy, $\Delta \varepsilon$ is the energy separation between the $\langle 111\rangle$ and $\langle 100\rangle$ minima, $T_n$ is the electron temperature, $T_0=300$ K is the lattice temperature, $\rho$ is the mass density of germanium, and $K_1$ is the modified Bessel function of the second kind.

The required numerical parameters for n‑Ge are:

- Electron effective masses in $\langle 111\rangle$ valleys: $m_{\|}=1.58 \, m_0$, $m_{\perp}=0.082 \, m_0$
- Intravalley optical phonon energy: $k_0 \theta_0 = k_0 \times 430$ K
- Intravalley optical deformation potential: $D_0 = 5 \times 10^8$ eV/cm
- Equivalent intervalley phonon energy: $k_0 \theta_i = k_0 \times 320$ K
- Equivalent intervalley deformation potential: $D_i = 1.4 \times 10^8$ eV/cm
- Acoustic deformation potential: $E_1 = 11$ eV
- Density of germanium: $\rho = 5.32$ g/cm³ (convert to kg/m³ as needed)
- Non‑equivalent intervalley parameters: $m_{\|[100]}=0.9 \, m_0$, $m_{\perp[100]}=0.19 \, m_0$, $\hbar \omega_{\mathrm{ni}} = k_0 \times 320$ K, $D_{\mathrm{ni}} = 1 \times 10^8$ eV/cm, $\Delta \varepsilon = 0.18$ eV, $N=4$
- Mobility (low‑field): $\mu_n \approx 3.8 \times 10^3$ cm²/(V·s), $\mu_p \approx 1.9 \times 10^3$ cm²/(V·s); for high‑field mobility you may adopt a constant or a standard model.
- Electron concentration: $n_0 = 5 \times 10^{14}$ cm⁻³; hole population negligible (n‑type). Excess carrier ratios: $\Delta n'/n_0 = 1$, $\Delta p'/p_0 = 1$.

The photogradient e.m.f. is evaluated using the temperature‑approximation expression:

$$\begin{aligned}
U_{\mathrm{fg}} = \frac{k_0}{e} \Bigg\{ & \big(n_0 \Delta p' - p_0 \Delta n'\big) \int_0^E \frac{\mu_n(E)\,\mu_p(E)\,\big[(1-s_n)\partial T_n/\partial E + (1-s_p)\partial T_p/\partial E\big]}{\big[n_0\mu_n(E)+p_0\mu_p(E)\big]\big[(n_0+\Delta n')\mu_n(E)+(p_0+\Delta p')\mu_p(E)\big]} \, dE \\
&+ \frac{\mu_n(E) T_n \Delta n - \mu_p(E) T_p \Delta p}{\mu_n(E) \Delta n + \mu_p(E) \Delta p} 
\ln\!\left[1 + \frac{\mu_n(E)\Delta n' + \mu_p(E)\Delta p'}{n_0\mu_n(E)+p_0\mu_p(E)}\right] \\
&- \frac{\mu_n(0) \Delta n - \mu_p(0) \Delta p}{\mu_n(0) \Delta n + \mu_p(0) \Delta p} \, T_0 \, \ln\!\left[1 + \frac{\mu_n(0)\Delta n' + \mu_p(0)\Delta p'}{n_0\mu_n(0)+p_0\mu_p(0)}\right] \Bigg\}, 
\end{aligned}$$

where $s_n$ and $s_p$ set the momentum‑relaxation‑time exponent ($\tau \propto \varepsilon^{-s}$; use $s_n = 1/2$ for acoustic‑phonon scattering and $s_p = 1/2$). The hole temperature $T_p$ may be assumed equal to the lattice temperature $T_0$ or computed from the hole energy balance; the difference is small for the present conditions.

Finally, the microwave‑cycle‑averaged e.m.f. $\langle U_{\mathrm{fg}}\rangle_T$ is obtained by integrating $U_{\mathrm{fg}}(E)$ over one cycle of the microwave field (e.g., using the root‑mean‑square amplitude or appropriate averaging). Two separate curves are generated:
- Baseline: intravalley + equivalent intervalley only (n‑i term omitted).
- With n‑i: the additional non‑equivalent intervalley loss term included in the energy balance.

The computed $\langle U_{\mathrm{fg}}\rangle_T$ vs. $E$ tables allow the effect of n‑i scattering to be investigated.

## Reproduction target
Produce a CSV file containing the microwave‑cycle‑averaged photogradient e.m.f. $\langle U_{\mathrm{fg}}\rangle_T$ (in mV) for n‑Ge at $T_0 = 300$ K as a function of the electric field amplitude $E$ (in kV/cm). The field must cover the range 0–16 kV/cm in steps of 1 kV/cm. The table must have three columns: `E` (int, kV/cm), `Ufg_no_ni` (float, mV), and `Ufg_with_ni` (float, mV). The `Ufg_no_ni` column is computed using only intravalley and equivalent intervalley scattering; the `Ufg_with_ni` column includes the additional non‑equivalent intervalley scattering term described in the approach. The concentrations, mobilities, and other parameters listed above must be used. The CSV must be written to `/app/outputs/step_01_ufg_vs_E.csv`.

## Assets

- numpy: pip install numpy
- scipy: pip install scipy

## Workflow steps

### Step 1: Implement energy‑loss rate functions for n-Ge
- Role: process
- Action: Implement analytic functions for: (i) intravalley and equivalent intervalley electron energy‑loss rates using standard semiconductor‑physics formulas with the material parameters listed in the instructions; (ii) the non‑equivalent intervalley energy‑loss rate from the paper’s derived expression (given as a formula in the instructions). The functions must compute the total average energy‑loss rate ⟨dε/dt⟩ as a function of electron temperature T_n and lattice temperature T_0.
- Evidence: `/app/outputs/energy_loss_functions.py`

### Step 2: Solve electron energy balance for T_n(E)
- Role: process
- Action: Using the rate functions from the previous step, numerically solve the steady‑state energy balance equation e μ E² + ⟨dε/dt⟩(T_n) = 0 over the electric field range 0–16 kV/cm in steps of 1 kV/cm. Perform the solution for two cases: (a) with only intravalley and equivalent intervalley losses, and (b) with the additional non‑equivalent intervalley loss term. Store the resulting electron temperature profiles T_n_a(E) and T_n_b(E) for later use.
- Evidence: `/app/outputs/Tn_profiles.npz`

### Step 3: Compute ⟨U_fg⟩_T vs E and write CSV
- Role: scored (load-bearing)
- Action: For each electric field value (0–16 kV/cm) and for both T_n profiles obtained above, evaluate the temperature‑approximation expression for the photogradient e.m.f. U_fg and perform the microwave‑cycle averaging to obtain the microwave‑averaged e.m.f. ⟨U_fg⟩_T. Use the fixed carrier concentrations, mobilities, and other parameters specified in the instructions. Output a CSV file with columns: E (kV/cm), Ufg_no_ni (mV), Ufg_with_ni (mV).
- Output file: `/app/outputs/step_01_ufg_vs_E.csv`
- Format: csv
- Contract: Columns: 'E' (int, kV/cm), 'Ufg_no_ni' (float, mV), 'Ufg_with_ni' (float, mV). Rows for E from 0 to 16 in steps of 1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_ufg_vs_E.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_ufg_vs_E.csv
- path: `/app/outputs/step_01_ufg_vs_E.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed microwave‑averaged photogradient e.m.f. as a function of electric field for n‑Ge without and with non‑equivalent intervalley scattering.
- schema:
  - `type`: table
  - `required_columns`: `E`, `Ufg_no_ni`, `Ufg_with_ni`
  - `units`:
    - `E`: kV/cm
    - `Ufg_no_ni`: mV
    - `Ufg_with_ni`: mV

Notes: The CSV provides the full computed ⟨U_fg⟩_T curve. The checker will compare these values to digitised gold curves, recompute the mean absolute error, and verify the slope reduction for E > 5 kV/cm in the with‑ni case.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_ufg_vs_E.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "E",
          "Ufg_no_ni",
          "Ufg_with_ni"
        ],
        "units": {
          "E": "kV/cm",
          "Ufg_no_ni": "mV",
          "Ufg_with_ni": "mV"
        }
      },
      "description": "Computed microwave‑averaged photogradient e.m.f. as a function of electric field for n‑Ge without and with non‑equivalent intervalley scattering."
    }
  ],
  "notes": "The CSV provides the full computed ⟨U_fg⟩_T curve. The checker will compare these values to digitised gold curves, recompute the mean absolute error, and verify the slope reduction for E > 5 kV/cm in the with‑ni case."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your `/app/outputs/step_01_ufg_vs_E.csv`. The verifier compares your computed `Ufg_no_ni` values to reference digitised data for the baseline (no n‑i scattering) and your `Ufg_with_ni` values to reference data that include n‑i scattering. It computes error metrics (e.g., mean absolute error) for each curve and also checks that the high‑field slope of `Ufg_with_ni` for $E > 5$ kV/cm is smaller than that of `Ufg_no_ni` — reflecting the expected role of non‑equivalent intervalley scattering. The final score is a weighted combination: 50% of the score comes from the accuracy of the no‑ni curve, 50% from the accuracy of the with‑ni curve, and a small bonus is added for passing the slope‑trend check. Reporting correct tabulated values is essential; the verifier does not receive any other artifacts from you.
