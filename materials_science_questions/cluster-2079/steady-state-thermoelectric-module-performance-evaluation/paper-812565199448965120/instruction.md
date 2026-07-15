# Solar irradiance sensitivity of a solar-thermionic-thermoelectric hybrid system

## Problem background
Concentrated solar power (CSP) systems, particularly parabolic dish collectors, can provide high-temperature heat for direct thermal-to-electric conversion devices such as thermionic generators. By cascading a thermoelectric device to recover waste heat, a hybrid system can produce additional electricity and cooling. Understanding how the total power output of such a system varies with the incident solar irradiance is essential for optimizing operating conditions and sizing. This task explores a solar‑driven hybrid system that couples a parabolic dish collector, a thermionic generator, and a thermoelectric device, and aims to characterize its power output as a function of solar irradiance.

## Approach
The hybrid system consists of a parabolic dish collector (PDC) that concentrates sunlight and delivers thermal energy to the cathode of a thermionic generator (TIG). The TIG converts a portion of this heat directly into electricity via thermionic emission. The anode of the TIG releases waste heat to the hot side of a thermoelectric device (combining a thermoelectric generator and cooler), which generates additional electrical power and, optionally, a cooling load. The coupled energy balances among the collector, TIG cathode, TIG anode, and thermoelectric cold end form a nonlinear system that must be solved iteratively to obtain the cathode temperature, anode temperature, and cold-end temperature. Once the temperature solution is found, the power outputs of the TIG and thermoelectric device can be computed. By sweeping the incident solar irradiance density \( I_0 \) while keeping all other design parameters (collector geometry, cathode work function, TIG voltage, thermal conductivities, resistance ratio) at their baseline values, the dependence of the total hybrid power on irradiance can be determined.

**Note:** The paper also reports a second scenario analysing the PDC optical/thermal performance in five Asian cities (Yazd, Istanbul, Beijing, Inchon, Riyadh) using real climatic data. That second scenario is not scored in this task; reproducing it would require retrieving hourly site-specific climatic data and performing a separate full-day optical/thermal analysis, which is beyond the scope of the main irradiance-sweep claim that is the focus here. Only the irradiance sweep (scenario 1) is required.

## Reproduction target
Implement the energy‑balance model and an iterative solver for the coupled system using the baseline parameters (collector aperture area 12.5 m², concentration ratio 1800, cavity wall temperature 827 °C, ambient temperature 25 °C, optical efficiency 0.95, cathode work function 1 eV, TIG voltage 0.2 V, TIG plate area 1.6×10⁻² m², thermoelectric module conductivity 61.3 W/K, inter‑device conductivity 60 W/K, ratio of resistances R₂/R = 1). Retrieve the thermoelectric device coefficients (Seebeck coefficient, figure of merit, internal resistance) from the public reference Marefati et al. (2019, DOI 10.1016/j.seta.2019.100550). Sweep \( I_0 \) from 0 to 3×10⁶ W/m² with sufficient resolution (at least 50 points). For each irradiance, compute the thermionic generator power \( P_{\text{TIG}} \), thermoelectric device power \( P_{\text{TD}} \), and total power \( P_{\text{total}} = P_{\text{TIG}} + P_{\text{TD}} \), and write them to `power_vs_irradiance.csv`. The hidden verifier will locate the irradiance that maximizes total power, verify the shape of the power curve, and check the thermoelectric device’s contribution.

## Assets

- NumPy: numpy
- SciPy: scipy
- Reference for thermoelectric device parameters (Marefati et al., Sustain. Energy Technol. Assess. 36, 2019, 100550): 10.1016/j.seta.2019.100550

## Workflow steps

### Step 1: Implement hybrid system model and iterative solver
- Role: process
- Action: Implement the following mathematical model for the hybrid system, then solve it iteratively for the unknown temperatures Tc (TIG cathode), Ta (TIG anode), and T2 (TEG cold end) at each irradiance.

  **Solar collector (PDC)**
  - Solar power incident on the dish aperture: Q_s = I0 * A_p (A_p = 12.5 m²).
  - Energy absorbed by the receiver: Q_r = η_opt * Q_s (η_opt = 0.95).
  - Cavity wall temperature Tw = 827 °C (1100 K) and ambient temperature Tamb = 25 °C (298 K). Convection and radiation losses are computed using the PDC thermal model: convection loss Q_conv = h_c * A_w * (Tw - Tamb) where h_c = Nu * K / L_s and Nu = 0.0196 * Ra_L^{0.41} * Pr^{0.13}, with L_s, Ra_L, Pr computed from geometry (cavity wall area A_w = 0.0645 m², receiver area A_c = 0.0069 m²); radiation loss Q_rad = A_c * ε_eff * σ * (Tw^4 - Tamb^4) with ε_eff = 1 / (1 + (1/ε_c - 1) * A_c/A_w), ε_c ≈ 0.9, σ = 5.67e-8 W/m²K⁴. Conduction loss is neglected. The net useful thermal energy delivered to the cathode is Q_{PDC} = Q_r - (Q_conv + Q_rad).

  **Thermionic generator (TIG)**
  - Constants: Richardson-Dushman constant A0 = 1.2e6 A/m²K², elementary charge q = 1.602e-19 C, Boltzmann constant k_B = 1.381e-23 J/K, anode work function φ_a = 1 eV = 1.602e-19 J, TIG voltage V = 0.2 V, cathode area A_c = 1.6e-2 m², emissivity ε_L (assumed 0.9).
  - Current densities: J_c = A0 * T_c² * exp(-(φ_a + q V) / (k_B T_c)), J_a = A0 * T_a² * exp(-φ_a / (k_B T_a)).
  - Energy balance at cathode (Q_{PDC} = heat absorbed by cathode): 
    Q_{PDC} = A_c * J_c * (V + (φ_a + 2 k_B T_c)/q) - A_c * J_a * (V + (φ_a + 2 k_B T_a)/q) + A_c * ε_L * σ * (T_c^4 - T_a^4).
  - Energy balance at anode (heat released by anode = Q_H, which is the heat absorbed by the TEG hot side):
    Q_H = A_c * J_c * ((φ_a + 2 k_B T_c)/q) - A_c * J_a * ((φ_a + 2 k_B T_a)/q) + A_c * ε_L * σ * (T_c^4 - T_a^4).

  **Thermoelectric device (TD)**
  - The TD consists of a TEG and TEC. The hot junction of the TEG is at temperature T_a, cold junction at T_2.
  - Seebeck coefficient α, figure of merit Z, total internal resistance R are obtained from the reference DOI 10.1016/j.seta.2019.100550 (Marefati et al., 2019). Use those values: α, Z, R.
  - Thermal conductivity of the TD module: K = 61.3 W/K.
  - Ratio of external load to internal resistances: R2/R = 1.
  - The heat absorbed by the TEG hot side: Q_H = α T_a I + K (T_a - T_2) - (I² R)/2, with current I = α (T_a - T_2) / (R + R2). Substituting gives:
    Q_H = [α² T_a (T_a - T_2) / (R + R2)] + K (T_a - T_2) - [α² (T_a - T_2)² / (2 (R + R2))].
  - The power produced by the TD: P_TD = I² R2 = α² R2 (T_a - T_2)² / (R + R2)². Using Z = α² / (K R), this can be rewritten as P_TD = Z K (T_a - T_2)² / (1 + R2/R)² * (R2/R).
  - Energy balance at the cold end of TEG (T_2): the heat conducted away from the cold side to a sink at temperature T_L (ambient 25 °C) through a thermal conductance K_L = 60 W/K:
    K_L (T_2 - T_L) = α² T_2 (T_a - T_2) / (R + R2) + K (T_a - T_2) + α² (T_a - T_2)² / (2 (R + R2)).

  **Iterative solution**
  For a given I0, guess initial temperatures (e.g., Tc = 1100 K, Ta = 800 K, T2 = 500 K). Compute Q_PDC from the PDC model, then iteratively adjust Tc, Ta, T2 to satisfy the three nonlinear energy balances (cathode, anode, cold-end) to within a tolerance of 1e-6 relative change. Use a numerical solver (e.g., scipy.optimize.fsolve) or a fixed-point iteration. After convergence, compute P_TIG = A_c * A0 * V * [ T_c² exp(-(φ_a + q V)/(k_B T_c)) - T_a² exp(-φ_a/(k_B T_a)) ] and P_TD as above, and total P_total = P_TIG + P_TD. Write a convergence log to convergence_log.txt (optional).
- Evidence: `/app/outputs/convergence_log.txt`

### Step 2: Solar irradiance sweep and output power curves
- Role: scored (load-bearing)
- Action: Using the model and solver from step 1, sweep the incident solar irradiance density I0 over the range from 0 to 3×10^6 W/m² (use at least 50 points to resolve the peak). For each I0, compute the three power quantities: thermionic generator power P_TIG (W), thermoelectric device power P_TD (W), and total hybrid power P_total = P_TIG + P_TD (W). Save the results to power_vs_irradiance.csv.
- Output file: `/app/outputs/power_vs_irradiance.csv`
- Format: csv
- Contract: CSV with header: I0,P_TIG,P_TD,P_total. I0: float, solar irradiance in W/m². P_TIG, P_TD, P_total: float, power in W.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/power_vs_irradiance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### power_vs_irradiance.csv
- path: `/app/outputs/power_vs_irradiance.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The hidden checker will locate the solar irradiance I0 that maximises P_total and compare it to the paper-reported critical irradiance; it will also verify that P_total increases before the peak and decreases after it, and that the thermoelectric device contributes more than 37% of total power at some irradiance.
- schema:
  - `type`: table
  - `required_columns`: `I0`, `P_TIG`, `P_TD`, `P_total`
  - `units`:
    - `I0`: W/m^2
    - `P_TIG`: W
    - `P_TD`: W
    - `P_total`: W

Notes: The checker uses the CSV to compute the peak irradiance and verify structural trends. No gold values or tolerances are exposed publicly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "power_vs_irradiance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "I0",
          "P_TIG",
          "P_TD",
          "P_total"
        ],
        "units": {
          "I0": "W/m^2",
          "P_TIG": "W",
          "P_TD": "W",
          "P_total": "W"
        }
      },
      "description": "The hidden checker will locate the solar irradiance I0 that maximises P_total and compare it to the paper-reported critical irradiance; it will also verify that P_total increases before the peak and decreases after it, and that the thermoelectric device contributes more than 37% of total power at some irradiance."
    }
  ],
  "notes": "The checker uses the CSV to compute the peak irradiance and verify structural trends. No gold values or tolerances are exposed publicly."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads `power_vs_irradiance.csv`. The verifier will (a) identify the solar irradiance that gives the maximum total power and compare it against a reference value (with tolerance), (b) confirm that the total power increases for irradiances below the peak and decreases above it, and (c) verify that the ratio \( P_{\text{TD}} / P_{\text{total}} \) exceeds a required threshold at some operating point. Each of these checks contributes to an overall reward between 0 and 1; the exact tolerances and threshold are hidden. Only a submission that correctly computes the power curve and satisfies the structural and threshold checks will achieve a high score.
