# Compute Thermodynamic State Functions of an Elongated Polymer Chain

## Problem background
Understanding the thermodynamics of polymer deformation is essential for designing materials that sustain large elastic strains. When a polymer specimen is uniaxially stretched, the applied force does both internal energy and entropy changes. This task computes the separate energetic and entropic contributions to the elastic force as well as the changes in internal energy and entropy for a polymer chain model that incorporates a temperature‑dependent maximum elongation. The goal is to verify that these state functions satisfy fundamental thermodynamic relations and reveal when the deformation is predominantly entropic or energetic.

## Approach
The polymer is modeled as a freely jointed chain of segments. The chain’s elastic extension is described by the Langevin function, with the maximum elongation assumed to vary exponentially with temperature between the glass‑transition and melting temperatures. From this model, analytic expressions for the internal energy change U_f, entropy change S_f, entropic force f_S, and energetic force f_U are derived as functions of temperature T and applied force f. The task implements these expressions numerically using standard Python libraries and evaluates them over a grid of (T, f) values. The sum f_S + f_U is then compared to f, and the limiting behavior at zero force is checked, providing a self‑contained validation of the thermodynamic decomposition.

## Reproduction target
Compute U_f, S_f, f_S, and f_U for a grid of temperatures from 300 K to 373 K and forces from 0 N to 5×10⁻¹¹ N (approximately 10–20 points per axis) using the following fixed polymer parameters: fully‑extended chain segment length l₀* = 1×10⁻⁹ m, maximum elongation prefactor Δ₀l = 1×10⁻⁸ m, glass‑transition temperature Tg = 300 K, melting temperature Tm = 373 K, reference temperature T₀ = (Tm+Tg)/2, temperature‑width parameter α = 4/(Tm−Tg), and Boltzmann constant k = 1.380649×10⁻²³ J/K. For each (T,f) point, calculate the Langevin parameter a = l₀* f / (k T), the corresponding Langevin function, the actual elongation, and then the four thermodynamic quantities. Write all results to a CSV file with columns temperature_T, force_f, a, U_f, S_f, f_S, f_U.

## Assets

- numpy: numpy

## Model equations

The thermodynamic quantities are evaluated from the following analytic expressions, derived in the paper for a freely jointed chain model with temperature‑dependent maximum elongation.

- **Langevin function:** \(\mathrm{La}(a)=\coth a-\frac{1}{a}\)
- **Argument:** \(a = \frac{l_0^* f}{k T}\)
- **Temperature‑dependent maximum elongation:** \(\Delta l = \Delta_0 l \,\exp\!\bigl[\alpha(T-T_0)\bigr]\)
- **Sample length:** \(l = l_0 + \Delta l\,\mathrm{La}(a)\).  (The initial length \(l_0\) cancels in the expressions below; only the difference \(l-l_0=\Delta l\,\mathrm{La}(a)\) matters.)
- **Internal energy change:** \(U_f = \alpha\,\Delta l\,\frac{k T^2}{l_0^*}\,\ln\!\Bigl(\frac{e^{a}-e^{-a}}{2a}\Bigr)\)
- **Entropy change:** \(S_f = -\frac{l-l_0}{\kappa T}\Bigl[a\,\mathrm{La}(a)-\ln\!\Bigl(\frac{e^{a}-e^{-a}}{2a}\Bigr)\Bigr] + \alpha\,\Delta l\,\frac{k T}{l_0^*}\,\ln\!\Bigl(\frac{e^{a}-e^{-a}}{2a}\Bigr)\), where \(\kappa = l_0^*/(k T)\).
     (Note that \(l-l_0 = \Delta l\,\mathrm{La}(a)\).)
- **Entropic force:** \(f_S = \Bigl(1 - \frac{\alpha T\,\mathrm{La}(a)}{a\,(\partial\mathrm{La}/\partial a)}\Bigr) f\)
- **Energetic force:** \(f_U = \frac{\alpha T\,\mathrm{La}(a)}{a\,(\partial\mathrm{La}/\partial a)}\,f\), with \(\partial\mathrm{La}/\partial a = \frac{1}{a^2} - \frac{1}{\sinh^2 a}\).

## Workflow steps

### Step 1: Compute thermodynamic quantities for a polymer chain
- Role: scored (load-bearing)
- Action: Implement the Langevin function La(a) = coth(a) - 1/a, with a = l0* f / (k T).  Use the temperature‑dependent maximum elongation Δl = Δ0 l exp[α(T - T0)] and the sample length l = l0 + Δl La(a).  Compute the internal energy change U_f, entropy change S_f, entropic force f_S, and energetic force f_U using the explicit formulas provided in the **Model equations** section above.  Use the constants: l0* = 1e-9 m, Δ0 l = 1e-8 m, T_g = 300 K, T_m = 373 K, T0 = (T_m+T_g)/2, α = 4/(T_m-T_g), k = 1.380649e-23 J/K.  Generate a grid of forces from 0 N to 5e-11 N and temperatures from 300 K to 373 K (approximately 10–20 points per axis).  For each (T,f) point compute a, Δl, La(a), ∂La/∂a, and the thermodynamic quantities.  Write all results to computed_quantities.csv.
- Output file: `/app/outputs/computed_quantities.csv`
- Format: csv
- Contract: CSV with columns: temperature_T, force_f, a, U_f, S_f, f_S, f_U. All fields are floating-point numbers in scientific notation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_quantities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_quantities.csv
- path: `/app/outputs/computed_quantities.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed thermodynamic state functions (internal energy, entropy, entropic and energetic force components) for a grid of temperature and applied force values.
- schema:
  - `type`: table
  - `required_columns`: `temperature_T`, `force_f`, `a`, `U_f`, `S_f`, `f_S`, `f_U`
  - `units`:
    - `temperature_T`: K
    - `force_f`: N
    - `a`: dimensionless
    - `U_f`: J
    - `S_f`: J/K
    - `f_S`: N
    - `f_U`: N

Notes: The checker independently recomputes the quantities from the formulas using hidden grid and parameter values, then compares each column with relative tolerance. It also verifies f_S + f_U ≈ f and that U_f and S_f vanish within tolerance at f=0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_quantities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_T",
          "force_f",
          "a",
          "U_f",
          "S_f",
          "f_S",
          "f_U"
        ],
        "units": {
          "temperature_T": "K",
          "force_f": "N",
          "a": "dimensionless",
          "U_f": "J",
          "S_f": "J/K",
          "f_S": "N",
          "f_U": "N"
        }
      },
      "description": "Computed thermodynamic state functions (internal energy, entropy, entropic and energetic force components) for a grid of temperature and applied force values."
    }
  ],
  "notes": "The checker independently recomputes the quantities from the formulas using hidden grid and parameter values, then compares each column with relative tolerance. It also verifies f_S + f_U ≈ f and that U_f and S_f vanish within tolerance at f=0."
}
```

## How you are scored
A hidden verifier independently recomputes the same quantities using the identical formulas and hidden parameter values. It reads your CSV and compares each column to pre‑computed gold values with a column‑wise relative tolerance (the exact tolerance is hidden). It also checks two self‑consistency conditions for every row: f_S + f_U ≈ f (within a small absolute tolerance) and, for rows where f = 0, U_f and S_f must be zero within tolerance. The verifier then combines the numerical accuracy and self‑consistency checks into a single reward score between 0 and 1. Submitting a CSV of the correct shape is required, but only an honest computation that matches the expected values closely will earn a high reward.
