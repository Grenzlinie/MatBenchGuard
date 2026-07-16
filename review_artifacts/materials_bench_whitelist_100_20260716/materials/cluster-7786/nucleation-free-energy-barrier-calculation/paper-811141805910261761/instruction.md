# Homogeneous Ice Nucleation Rate Calculation

## Problem background
Liquid water can persist in a supercooled state to below 238 K in Earth's atmosphere, where homogeneous ice nucleation becomes increasingly probable. However, the rate of homogeneous ice nucleation in supercooled water is poorly constrained. Accurate parameterizations of the nucleation rate are essential for cloud and climate models, yet existing formulations diverge significantly. This work develops a physically constrained classical nucleation theory (CNT) parameterization for the homogeneous nucleation rate of ice in supercooled water. The key terms – the diffusion activation energy and the ice–liquid interfacial energy – are constrained by physically consistent descriptions: a power-law fit to water's translational self-diffusion coefficient and a Turnbull correlation to relate the interfacial energy to the enthalpy of melting of stacking-disordered ice.

## Approach
You will implement a classical nucleation theory (CNT) model to compute the homogeneous ice nucleation rate J(T). The CNT expression (Eq. 1) consists of a kinetic prefactor and an exponential term involving the diffusion activation free energy ΔG_diff(T) and the critical cluster formation free energy ΔG_crit(T). The saturation ratio S(T) required for ΔG_crit is obtained from published vapor pressure parameterizations for supercooled water and for stacking-disordered ice (with a stacking‑fault enthalpy correction). The diffusion coefficient D(T) is described by a power‑law function of temperature; from it the diffusion activation energy is derived via the temperature derivative. The interfacial energy σ_sd,l(T) is estimated using the Turnbull correlation: its temperature dependence is scaled to the enthalpy of melting of stacking‑disordered ice ΔH_m,sd(T), which itself is computed from polynomial fits to calorimetric data with a constant offset for stacking disorder. The only fitted parameter is the interfacial energy at a single reference temperature; the task provides that value. Finally, the number density of water molecules n_l is evaluated from a fixed liquid‑water density, and J(T) is computed from the CNT equations over a range of temperatures.

## Reproduction target
Compute the homogeneous ice nucleation rate J(T) (cm⁻³ s⁻¹) and the intermediate quantities D(T) (cm² s⁻¹), ΔG_diff(T) (J), and σ_sd,l(T) (mJ m⁻²) over the temperature range 225–250 K, using classical nucleation theory with the power‑law diffusion model and the Turnbull‑correlated interfacial energy for stacking‑disordered ice. Output these quantities as a CSV file at 1 K intervals, and ensure the file includes rows for the temperatures T = 230 K, 240 K, and 250 K. The file must be written to `/app/outputs/step_01_CNT_results.csv`.

## Assets
No external datasets or proprietary models are required. The following constants and parameterizations are provided for the computation.

### Physical constants
- Boltzmann constant k = 1.380648e-23 J K⁻¹
- Planck constant h = 6.626070e-34 J s
- Avogadro constant N_A = 6.02214e23 mol⁻¹
- Molar mass of water M(H₂O) = 18.0148 g mol⁻¹
- Melting temperature of hexagonal ice T_m = 273.15 K
- Enthalpy difference stacking-disordered vs hexagonal ice ΔH_sd,h = 0.155 kJ mol⁻¹
- Reference temperature for interfacial energy T_r = 236.0 K
- Liquid water density ρ_l = 0.965 g cm⁻³ (assumed constant)
- Gas constant R = 8.314e-3 kJ mol⁻¹ K⁻¹

### Ice density
ρ_i(T) in g cm⁻³:
ρ_i(T) = -1.3103×10⁻⁹ T³ + 3.8109×10⁻⁷ T² - 9.2592×10⁻⁵ T + 0.94040
where T is in K.

### Vapor pressures and saturation ratio
ln(P_l / Pa) = 54.842763 − 6763.22 / T − 4.210 ln(T) + 0.000367 T
                + tanh[0.0415 (T − 218.8)] × (53.878 − 1331.22 / T − 9.44523 ln(T) + 0.014025 T)

ln(P_h / Pa) = 9.550426 − 5723.265 / T + 3.53068 ln(T) − 0.00728332 T

S(T) = P_l / [P_h exp(ΔH_sd,h / (R T))]

### Diffusion coefficient (power‑law fit)
D(T) = D* T^{0.5} (T / T_s − 1)^{γ}
with D* = 8.3175×10⁻⁶ cm² s⁻¹ K⁻⁰.⁵, T_s = 215.45 K, γ = 1.9188

ΔG_diff,PL(T) = (k T) / 2 + (γ k T²) / (T − T_s)

### Enthalpy of melting of hexagonal ice
ΔH_m,h(T) / (kJ mol⁻¹) = Σ_{i=0}^{6} k_i (T − T_m)^i

Coefficients k_i (best estimate):
k_0 = 6.008
k_1 = 0.03616
k_2 = −3.9479×10⁻⁴
k_3 = −1.6248×10⁻⁵
k_4 = −3.2563×10⁻⁷
k_5 = 0
k_6 = 0

### Enthalpy of melting and interfacial energy for stacking‑disordered ice
ΔH_m,sd(T) = ΔH_m,h(T) − ΔH_sd,h  (ΔH_sd,h = 0.155 kJ mol⁻¹)

σ_sd,l(T) = ΔH_m,sd(T) × σ_sd,l(T_r) / ΔH_m,sd(T_r)
with T_r = 236.0 K, σ_sd,l(T_r) = 18.505 mJ m⁻².

### Number density of water molecules
n_l = (ρ_l N_A) / M(H₂O)   (units: cm⁻³)

The computation can be carried out with a standard scientific Python environment. We recommend installing numpy, scipy, and pandas from the PyPI mirror:

```bash
python3 -m pip install -q --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple numpy scipy pandas
```

## Workflow steps

### Step 1: Compute CNT nucleation rate and intermediate quantities
- Role: scored (load-bearing)
- Action: Implement the classical nucleation theory model: (1) compute saturation ratio S(T) using vapor pressure parameterizations for supercooled water and stacking-disordered ice; (2) compute self-diffusion coefficient D(T) using the power-law fit D(T) = D* * T^0.5 * (T/T_s - 1)^gamma with D* = 8.3175e-6 cm^2 s^-1 K^-0.5, T_s = 215.45 K, gamma = 1.9188; (3) derive the diffusion activation free energy via the derivative of the power law; (4) compute the enthalpy of melting for stacking-disordered ice ΔH_m,sd(T) using polynomial coefficients (Table III) and a constant offset, then the ice–liquid interfacial energy σ_sd,l(T) via the Turnbull correlation with reference value σ_sd,l(236 K) = 18.505 mJ m^-2; (5) compute the number density of water molecules n_l; (6) compute the homogeneous nucleation rate J(T) from the CNT equations. Output a CSV file with columns T, D, Delta_G_diff, sigma_sd_l, J for temperatures 225–250 K at 1 K intervals, ensuring rows for T = 230, 240, and 250 K.
- Output file: `/app/outputs/step_01_CNT_results.csv`
- Format: csv
- Contract: CSV with columns: T (float, units K), D (float, units cm^2/s), Delta_G_diff (float, units J), sigma_sd_l (float, units mJ/m^2), J (float, units cm^-3 s^-1). Must include rows for T = 230, 240, 250 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_CNT_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_CNT_results.csv
- path: `/app/outputs/step_01_CNT_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Table of computed CNT quantities over temperature range 225–250 K, including the homogeneous nucleation rate. The hidden checker recomputes D, ΔG_diff, σ_sd_l, and J at T = 230, 240, 250 K using the same formulas and compares against the submitted values with tolerances (5% relative for J, 2% relative for others).
- schema:
  - `type`: table
  - `required_columns`: `T`, `D`, `Delta_G_diff`, `sigma_sd_l`, `J`
  - `units`:
    - `T`: K
    - `D`: cm^2/s
    - `Delta_G_diff`: J
    - `sigma_sd_l`: mJ/m^2
    - `J`: cm^-3 s^-1

Notes: The agent must implement the CNT model using the provided parameterizations; no refitting or external data download is required. The output must be well-formed CSV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_CNT_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "D",
          "Delta_G_diff",
          "sigma_sd_l",
          "J"
        ],
        "units": {
          "T": "K",
          "D": "cm^2/s",
          "Delta_G_diff": "J",
          "sigma_sd_l": "mJ/m^2",
          "J": "cm^-3 s^-1"
        }
      },
      "description": "Table of computed CNT quantities over temperature range 225–250 K, including the homogeneous nucleation rate. The hidden checker recomputes D, ΔG_diff, σ_sd_l, and J at T = 230, 240, 250 K using the same formulas and compares against the submitted values with tolerances (5% relative for J, 2% relative for others)."
    }
  ],
  "notes": "The agent must implement the CNT model using the provided parameterizations; no refitting or external data download is required. The output must be well-formed CSV."
}
```

## How you are scored
A hidden verifier will independently recompute the quantities D, ΔG_diff, σ_sd,l, and J from your submitted CSV at selected temperatures. The verifier compares your values against independently calculated hidden reference values using appropriate tolerances. The closeness of match determines the score for this step, which carries the full weight of the task. Reporting the paper's numbers without performing the correct computation will not yield a high score, as the verifier recomputes the quantities from the governing equations and does not rely on the reported values alone.
