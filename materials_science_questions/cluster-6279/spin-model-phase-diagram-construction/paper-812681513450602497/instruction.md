# Multiple Phase Transitions in Decorated Ising Square Lattice

## Problem background
The decorated square lattice Ising model is an exactly solvable frustrated spin system in which decorating spins are placed between the nodal sites of a square lattice and interact via exchange couplings. Decoration-iteration transformations map the model onto the ordinary square-lattice Ising model, yielding a closed-form partition function. Depending on the signs and strengths of the interactions and the decoration numbers, the system can display complex thermodynamic phenomena—frustration, partial orderings, and multiple phase transitions—that are reflected in the temperature dependence of its heat capacity and entropy. This task requires you to compute those thermodynamic functions numerically from the exact analytic expressions and to explore the behaviour for two specific parameter regimes.

## Approach
The thermodynamic behaviour follows from the partition function \(\lambda\) per unit cell of the decorated lattice. For the general model with coupling parameters \(J_{xd}, J_{yd}, J_x, J_y\) and decoration numbers \(d_x, d_y\), the logarithm of \(\lambda\) is given by a double integral over two angles \(\phi, \theta\):

\[
N_0 \ln(\lambda/2) = \frac{1}{8\pi^2}\int_0^{2\pi}\!\int_0^{2\pi} \ln\bigl[ C_1 C_2 - S_1 D_2 \cos\phi - S_2 D_1 \cos\theta \bigr] \, d\phi\, d\theta ,
\]

where \(K_{i} = J_i / T\), \(K_{id} = J_{id} / T\) and the auxiliary functions are

\[
\begin{aligned}
D_i &= \cosh^{2d_i+2} K_{id} - \sinh^{2d_i+2} K_{id},\\
C_i &= \tfrac12 e^{2K_i} (\cosh^{d_i+1} K_{id} + \sinh^{d_i+1} K_{id})^2 + \tfrac12 e^{-2K_i} (\cosh^{d_i+1} K_{id} - \sinh^{d_i+1} K_{id})^2,\\
S_i &= \tfrac12 e^{2K_i} (\cosh^{d_i+1} K_{id} + \sinh^{d_i+1} K_{id})^2 - \tfrac12 e^{-2K_i} (\cosh^{d_i+1} K_{id} - \sinh^{d_i+1} K_{id})^2,
\end{aligned}
\]

with \(i = x, y\). The energy and entropy follow from derivatives of \(\ln\lambda\); the heat capacity is \(C = T \, dS/dT\). You can obtain the required curves by numerically evaluating the double integral for many temperatures and differentiating.

For the isotropic singly decorated lattice (\(J_x=J_y=0\), \(d_x=d_y=1\), equal coupling \(J_{xd}=J_{yd}=J_d\)) the partition function simplifies. Let \(K_d = J_d/T\) and define

\[
m = \frac{2\sinh 2K_d \sinh 4K_d}{(\cosh^2 2K_d + 1)^2}.
\]

Then the logarithm of the partition function contains a term that can be expressed through the complete elliptic integrals of the first and second kind, \(K(m)\) and \(E(m)\). The heat capacity has the explicit analytic form

\[
C = \frac{4K_d^2}{3\pi} \Bigl[ \pi(3+\cosh 4K_d)\,\mathrm{csch}^2 4K_d + \frac{1}{4m^2}\bigl(2(m')^2 - m\, m''\bigr) K(m) - (\coth 4K_d + 3\,\mathrm{csch}\,4K_d)^2 E(m) \Bigr],
\]

where \(m' = dm/dK_d\) and \(m'' = d^2m/dK_d^2\). This expression can be evaluated directly at each temperature to produce the heat capacity curve. The scheme does not require any external data; only standard numerical libraries (NumPy for array operations and SciPy for integration and special functions) are needed.

## Reproduction target
You must produce computable evidence for two distinct parameter regimes of the decorated square lattice Ising model.

1. **Multiple-transition regime.** Use \(J_{xd} = J_{yd} = -1\), \(J_x = -0.8\), \(J_y = -3\), and \(d_x = d_y = 1\). Compute the temperature-dependent heat capacity and entropy over a temperature range that spans at least from 0.1 to 10 (in units where \(k_B=1\)), with sufficient resolution to resolve any sharp features (two distinct peaks in the heat capacity are expected for this parameter set). Output a CSV file with columns `temperature`, `heat_capacity`, `entropy`.

2. **Isotropic singly decorated regime.** Use \(J_x = J_y = 0\), \(d_x = d_y = 1\), and set the decorating couplings equal to each other, e.g. \(J_{xd}=J_{yd}=1\) (temperature in units of the coupling). Compute the heat capacity as a function of temperature over the range 0.1 to 5.0 and output a CSV with columns `temperature`, `heat_capacity`. From this heat capacity curve, locate the temperature at which the singular peak (logarithmic divergence) occurs and output that single floating-point number as a plain text file.

## Assets

- NumPy: https://pypi.org/project/numpy
- SciPy: https://pypi.org/project/scipy

## Workflow steps

### Step 1: Multiple-transition heat capacity and entropy
- Role: scored (load-bearing)
- Action: Implement the general partition function of the decorated square lattice Ising model as a double integral over two angles (the Onsager-like integral expression), compute the heat capacity and entropy as functions of temperature by numerical evaluation and differentiation, for the parameter set J_xd = J_yd = -1, J_x = -0.8, J_y = -3, d_x = d_y = 1. Write a CSV file with columns temperature, heat_capacity, entropy over the temperature range 0.1 to 10 with sufficient resolution to resolve two distinct heat capacity peaks.
- Output file: `/app/outputs/step_01_hc_entropy_multiple.csv`
- Format: csv
- Contract: temperature (float), heat_capacity (float), entropy (float)
- Scoring: scored by hidden verifier

### Step 2: Isotropic singly decorated heat capacity
- Role: scored
- Action: For the isotropic singly decorated lattice (J_x = J_y = 0, d_x = d_y = 1, equal coupling J_xd = J_yd), compute the heat capacity using the simplified analytic expression involving the complete elliptic integrals K(m) and E(m) and the parameter m defined in terms of the coupling. Write a CSV with columns temperature and heat_capacity over a range from 0.1 to 5.0 (in units of the coupling).
- Output file: `/app/outputs/step_02_hc_isotropic_equal.csv`
- Format: csv
- Contract: temperature (float), heat_capacity (float)
- Scoring: scored by hidden verifier

### Step 3: Isotropic critical temperature
- Role: scored
- Action: Determine the phase transition temperature for the isotropic case by locating the singular peak (divergence) in the heat capacity computed in the previous step, and output that temperature as a single number.
- Output file: `/app/outputs/step_03_Tc_isotropic.txt`
- Format: txt
- Contract: A single floating-point number
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_hc_entropy_multiple.csv`
- `/app/outputs/step_02_hc_isotropic_equal.csv`
- `/app/outputs/step_03_Tc_isotropic.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_hc_entropy_multiple.csv
- path: `/app/outputs/step_01_hc_entropy_multiple.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent heat capacity and entropy for the multiple-transition parameter set. The checker will recompute these values at hidden temperature points and compare with the submitted CSV within a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `heat_capacity`, `entropy`

### step_02_hc_isotropic_equal.csv
- path: `/app/outputs/step_02_hc_isotropic_equal.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Heat capacity curve for the isotropic singly decorated lattice. The checker will recompute at hidden temperature points and compare.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `heat_capacity`

### step_03_Tc_isotropic.txt
- path: `/app/outputs/step_03_Tc_isotropic.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Critical temperature of the isotropic decorated lattice. A single floating-point number; the checker will compare it to the exact theoretical value within an absolute tolerance.
- schema:
  - `type`: text

Notes: All formulas are fully described in the method-level instruction (no paper equation numbers). The checker uses hidden gold values derived from the analytic expressions and the theoretical Tc.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_hc_entropy_multiple.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "heat_capacity",
          "entropy"
        ]
      },
      "description": "Temperature-dependent heat capacity and entropy for the multiple-transition parameter set. The checker will recompute these values at hidden temperature points and compare with the submitted CSV within a relative tolerance."
    },
    {
      "file": "step_02_hc_isotropic_equal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "heat_capacity"
        ]
      },
      "description": "Heat capacity curve for the isotropic singly decorated lattice. The checker will recompute at hidden temperature points and compare."
    },
    {
      "file": "step_03_Tc_isotropic.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text"
      },
      "description": "Critical temperature of the isotropic decorated lattice. A single floating-point number; the checker will compare it to the exact theoretical value within an absolute tolerance."
    }
  ],
  "notes": "All formulas are fully described in the method-level instruction (no paper equation numbers). The checker uses hidden gold values derived from the analytic expressions and the theoretical Tc."
}
```

## How you are scored
A hidden verifier will independently implement the analytic thermodynamic expressions described above. For the CSV outputs (steps 1 and 2), the verifier recomputes the heat capacity and entropy at a hidden set of temperature points (including points that probe the phase‑transition peaks) and compares your submitted numbers to its recomputed values using relative tolerances. For the critical temperature (step 3), the verifier compares your reported value to the exact theoretical value for the isotropic case using an absolute tolerance. The final score is a weighted combination of the per‑artifact scores, with the multiple‑transition CSV (step 1) carrying the largest weight. You do not need to match any particular “paper” number—the assessment is based on agreement with the verifier’s own correct computation of the same analytic quantities.
