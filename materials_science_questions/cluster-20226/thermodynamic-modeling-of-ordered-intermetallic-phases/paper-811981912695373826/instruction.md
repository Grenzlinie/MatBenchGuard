# Analytical computation of tracer diffusivities and correlation factors in non-stoichiometric B2 intermetallics

## Problem background
Tracer diffusion in highly ordered non-stoichiometric B2 intermetallic compounds is governed by the six-jump-cycle (6JC) mechanism, where vacancies move along low-energy-penalty trajectories. At off-stoichiometric compositions, antistructural atoms modify the diffusion behaviour. This task computes the tracer diffusivities and correlation factors for both atomic species (A and B) using an analytical model that extends the 6JC concept to non-stoichiometry. The model combines the Ising alloy picture with the Bragg–Williams approximation and an analogue of the five-frequency model for impurity diffusion, yielding closed-form expressions that depend on composition, interaction asymmetry, and temperature.

## Approach
The Ising alloy is defined by pair interaction energies \(E_{AA}\), \(E_{BB}\), \(E_{AB}\). The ordering energy is \(E = E_{AA} + E_{BB} - 2E_{AB}\) and the asymmetry parameter is \(U = (E_{AA}-E_{BB})/E\). Set \(E_{AB}=0\), which implies \(E_{AA} = (1+U)E/2\), \(E_{BB} = (1-U)E/2\). The migration energies are taken as symmetric, so the migration asymmetry \(\Delta = U_B - U_A = 0\). With Bragg–Williams statistics for B-rich compositions (composition deviation \(\delta\), such that \(c_A = 0.5 - \delta\)), the central quantities are: \(\Delta_A = E_{AA}\) and \(\Delta_B = E_{BB}\).

Define the normalized inverse temperature \(\theta = E/kT\). All frequencies are expressed in units of the attempt frequency \(\nu\); the vacancy concentration factor \(c_v^\alpha \, a^2 \, \nu \, \exp(7E_{AB}\beta)\) is set to unity, so the diffusivities \(D_A^*\), \(D_B^*\) are reported as dimensionless multiples.

The basic isolated \(\alpha\)-6JC frequency is
\[w_0 = \exp\!\big[\theta\, \big(\!-6 + \delta(19 - 7U)\big)\big].\]
The four rotational jump frequencies around an antistructural B atom are
\[
\begin{aligned}
w_1^{(1)} &= \exp\!\big[\theta\, \big(\!-5.5 - 0.5U + 18\delta - 6\delta U\big)\big], \\
w_1^{(2)} &= \exp\!\big[\theta\, \big(\!-5 + \delta(17 - 7U)\big)\big], \\
w_1^{(3)} &= \exp\!\big[\theta\, \big(\!-4.5 - 0.5U + 16\delta - 6\delta U\big)\big], \\
w_1^{(4)} &= w_0.
\end{aligned}
\]

The B-atom tracer correlation factor is
\[f_{\rm B} = 2\delta\big[14w_1^{(3)} + 25\big(w_1^{(1)}+w_1^{(2)}\big)\big] + 8(1-15\delta)w_0 + \frac{2(1-15\delta)w_0}{\delta}\,\exp\!\big[\!-4\theta(1-U)(1-2\delta)\big].\]
The B tracer diffusivity (in the chosen units) is
\[D_{\rm B}^* = \frac{4\delta\big[14w_1^{(3)} + 25\big(w_1^{(1)}+w_1^{(2)}\big)\big] + 16(1-15\delta)w_0 + \displaystyle\frac{4(1-15\delta)w_0}{\delta}\,\exp\!\big[\!-4\theta(1-U)(1-2\delta)\big]}{1+2\delta}.\]

The A-atom tracer correlation factor is
\[
\begin{aligned}
f_{\rm A} = &\; \frac{24.1\,\delta^2}{1-2\delta}\big[w_1^{(3)}+1.5\big(w_1^{(1)}+w_1^{(2)}\big)\big]\,\exp\!\big[\theta(1-U)(4-7\delta)\big] \\
&+ \frac{8(1-15\delta)w_0}{1-2\delta}\,\Big[\delta\exp\!\big[\theta(1-U)(4-7\delta)\big] + \exp\!\big[\theta\delta(1-U)\big]\Big].
\end{aligned}
\]
The A tracer diffusivity is
\[
D_{\rm A}^* = \frac{24.1\,\delta^2\big[w_1^{(3)}+1.5\big(w_1^{(1)}+w_1^{(2)}\big)\big] + 8(1-15\delta)w_0 + \displaystyle\frac{8(1-15\delta)w_0}{\delta}\,\exp\!\big[\!-4\theta(1-U)(1-2\delta)\big]}{1-2\delta}.
\]

Evaluate these expressions for each required parameter set (\(\delta\), \(U\), \(\theta\)) as described in the reproduction target. The output columns directly correspond to \(f_{\rm A}\), \(f_{\rm B}\), \(D_{\rm A}^*\), \(D_{\rm B}^*\).

## Reproduction target
Compute the tracer correlation factors \(f_{\rm A}\), \(f_{\rm B}\) and tracer diffusivities \(D_{\rm A}^*\), \(D_{\rm B}^*\) (in units of \(a^2\,c_{\rm v}^\alpha\,\nu\,\exp(7E_{AB}\beta)\)) for the following parameter combinations:

- Composition deviations \(\delta\): 0.02, 0.04.
- Asymmetry parameters \(U\): 0.0, 0.125, -0.125.
- Normalized inverse temperatures \(\theta = E/kT\): a grid from 0.5 to 2.0 in steps of 0.1 (inclusive).

For every combination of \((\delta, U, \theta)\), calculate the four quantities according to the analytical expressions given in the Approach and write one row to `/app/outputs/tracer_diffusion_results.csv`. The CSV must contain the columns `delta`, `U_param`, `E_over_kT`, `f_A`, `f_B`, `D_A_star`, `D_B_star` in that order, with floating-point values. The order of rows does not matter, but every combination must be present exactly once.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute tracer diffusivities and correlation factors
- Role: scored (load-bearing)
- Action: Implement the analytical model: define the Ising-alloy pair interactions, compute effective 6JC jump frequencies via the Bragg–Williams and bond-breaking formalism, then compute B‑atom and A‑atom tracer correlation factors and total tracer diffusivities using the five‑frequency‑model analogue for antistructural‑atom‑assisted 6JCs. Evaluate the derived expressions for each required parameter set (composition δ, asymmetry parameter U, and normalized temperature E/kT) and write the results to tracer_diffusion_results.csv.
- Output file: `/app/outputs/tracer_diffusion_results.csv`
- Format: csv
- Contract: Columns: delta (float), U_param (float), E_over_kT (float), f_A (float), f_B (float), D_A_star (float), D_B_star (float). Each row corresponds to one parameter set.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tracer_diffusion_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tracer_diffusion_results.csv
- path: `/app/outputs/tracer_diffusion_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed tracer correlation factors and diffusivities for each input parameter combination. The checker recomputes the same formulas and compares the values with a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `delta`, `U_param`, `E_over_kT`, `f_A`, `f_B`, `D_A_star`, `D_B_star`
  - `units`:
    - `delta`: dimensionless (deviation from stoichiometry 0.5)
    - `U_param`: dimensionless asymmetry parameter (E_AA - E_BB)/E
    - `E_over_kT`: dimensionless (normalized inverse temperature)
    - `f_A`: dimensionless (A tracer correlation factor)
    - `f_B`: dimensionless (B tracer correlation factor)
    - `D_A_star`: units of a^2 * c_v^alpha * nu * exp(7*E_AB*beta)
    - `D_B_star`: units of a^2 * c_v^alpha * nu * exp(7*E_AB*beta)

Notes: Monte Carlo simulations are not required; only the analytical computation is scored. The instruction will define the parameter grids used in the paper's validation without revealing the expected numeric values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tracer_diffusion_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta",
          "U_param",
          "E_over_kT",
          "f_A",
          "f_B",
          "D_A_star",
          "D_B_star"
        ],
        "units": {
          "delta": "dimensionless (deviation from stoichiometry 0.5)",
          "U_param": "dimensionless asymmetry parameter (E_AA - E_BB)/E",
          "E_over_kT": "dimensionless (normalized inverse temperature)",
          "f_A": "dimensionless (A tracer correlation factor)",
          "f_B": "dimensionless (B tracer correlation factor)",
          "D_A_star": "units of a^2 * c_v^alpha * nu * exp(7*E_AB*beta)",
          "D_B_star": "units of a^2 * c_v^alpha * nu * exp(7*E_AB*beta)"
        }
      },
      "description": "Computed tracer correlation factors and diffusivities for each input parameter combination. The checker recomputes the same formulas and compares the values with a relative tolerance."
    }
  ],
  "notes": "Monte Carlo simulations are not required; only the analytical computation is scored. The instruction will define the parameter grids used in the paper's validation without revealing the expected numeric values."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted CSV. It re-computes the same analytical formulas for each row using the input parameters (`delta`, `U_param`, `E_over_kT`) and compares the obtained `f_A`, `f_B`, `D_A_star`, `D_B_star` with your values. The comparison uses a relative tolerance; any row where all four quantities match within the tolerance is considered correct. The final reward is the fraction of correct rows. The verifier does not have access to the original paper; it uses only the published expressions.
