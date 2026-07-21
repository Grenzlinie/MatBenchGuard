# Mean-field phase diagram for a frustrated XY model under a twofold field

## Problem background
The finite-temperature crossover from a frustrated XY model to the Ising (ANNNI) model under a twofold symmetry‑breaking field is investigated. The model describes classical XY spins on a layered lattice with in‑plane nearest‑neighbour coupling $J$, competing axial interactions $J_1>0$ (nearest neighbour) and $J_2<0$ (next‑nearest neighbour), and a field $H$ that couples to $\cos 2\varphi$, favouring discrete orientations. At the ground state the XY freedom survives only for $H<0.75$; at finite temperature the system can order into a structure with spatial period $p$, and the transition temperatures $T_c$ (disordered to an Ising‑ordered phase) and $T_c'$ (appearance of the XY $\sin\varphi$ degrees of freedom) define the phase diagram. The central question is how the XY freedom is suppressed by temperature, i.e. whether $T_c'$ lies significantly below $T_c$, and how these temperatures vary with the twofold field $H$ for the period‑6 modulated phase.

## Approach
Use mean‑field theory to compute the thermodynamic potential for a structure with period $p=6$. In the limit $H=0$ the critical temperature for the disordered‑to‑modulated transition is known analytically; call this reference value $T_c^{\rm XY}$. For $H>0$ the transition temperature $T_c$ is obtained from the instability condition of the Ising sector, which involves the modified Bessel function ratio $P_1(z)=I_1(z)/I_0(z)$. The self‑consistent condition can be written as $T_c = \bigl(1 + P_1(\beta_c H)\bigr)\, T_c^{\rm XY}$ with $\beta_c = 1/(k_B T_c)$, so $T_c$ must be solved implicitly for each $H$. The lower transition $T_c'$, where the $\sin\varphi$ (XY) components become non‑zero, requires first solving the mean‑field equations for the Ising order parameters $c_i$ of the period‑6 structure at a given temperature. Knowledge of $c_i$ allows one to compute the quantity $\langle\sin^2\varphi_2\rangle$ that enters the stability condition for the $s_i$ sector. $T_c'$ is then the temperature at which this stability condition is satisfied, linking $T_c'$ to $\langle\sin^2\varphi_2\rangle$ and $T_c^{\rm XY}$. Numerically, for each $H$ one must (a) find $T_c$ by root‑finding, (b) at several trial temperatures below $T_c$ solve the self‑consistent system for $c_i$, (c) evaluate the stability criterion to locate $T_c'$.

## Reproduction target
Fix the model parameters $J_1=2$, $J_2=-1$, $J_z=0$, $k_B=1$, and consider the period‑6 modulated phase. For the twofold field $H$ ranging from $0.0$ to $2.0$ in steps of $0.1$, compute:
- the disordered‑to‑Ising‑order transition temperature $T_c$,
- the Ising‑to‑XY transition temperature $T_c'$ where the $s_i$ order parameters first appear.
Write the results to `/app/outputs/phase_diagram.csv` with columns `H`, `Tc`, `Tc_prime`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute critical temperatures Tc and Tc_prime for the period-6 phase
- Role: scored (load-bearing)
- Action: Using mean-field theory with model parameters J1=2, J2=-1, Jz=0, kB=1, for each twofold field H from 0.0 to 2.0 in steps of 0.1: (a) compute the XY reference temperature T_c^XY from the analytic expression for the H=0 limit; (b) numerically solve the implicit equation for the disordered-to-ordered transition temperature T_c involving the modified Bessel function ratio P1; (c) solve the self-consistent mean-field equations for the Ising order parameters c_i of the period-6 modulated structure and determine the lower transition temperature T_c' where XY order (sin components) appears, via the stability condition involving the average ⟨sin²φ₂⟩. Write a CSV file with columns H, Tc, Tc_prime.
- Output file: `/app/outputs/phase_diagram.csv`
- Format: csv
- Contract: CSV with header: H,Tc,Tc_prime. H: float (0.0 to 2.0, step 0.1). Tc: float (critical temperature from the disordered-to-ordered instability equation). Tc_prime: float (critical temperature for XY order onset).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram.csv
- path: `/app/outputs/phase_diagram.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed critical temperatures Tc and Tc_prime for the period-6 phase across the field H. The checker compares values to a hidden reference and verifies monotonic increase of Tc with H and that Tc_prime < Tc for H <= 0.75.
- schema:
  - `type`: table
  - `required_columns`: `H`, `Tc`, `Tc_prime`
  - `units`:
    - `H`: dimensionless (in units of |J2|, with J2=-1)
    - `Tc`: dimensionless (in units of kB, with kB=1)
    - `Tc_prime`: dimensionless (in units of kB, with kB=1)

Notes: The task reproduces the mean-field phase diagram lines for the period-6 structure as reported in the paper. Only the main transition lines are scored; no figure or probability density plots are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "H",
          "Tc",
          "Tc_prime"
        ],
        "units": {
          "H": "dimensionless (in units of |J2|, with J2=-1)",
          "Tc": "dimensionless (in units of kB, with kB=1)",
          "Tc_prime": "dimensionless (in units of kB, with kB=1)"
        }
      },
      "description": "The computed critical temperatures Tc and Tc_prime for the period-6 phase across the field H. The checker compares values to a hidden reference and verifies monotonic increase of Tc with H and that Tc_prime < Tc for H <= 0.75."
    }
  ],
  "notes": "The task reproduces the mean-field phase diagram lines for the period-6 structure as reported in the paper. Only the main transition lines are scored; no figure or probability density plots are required."
}
```

## How you are scored
A hidden verifier will independently compute the expected $T_c$ and $T_c'$ values from the same equations and parameters, then compare your submitted CSV row‑by‑row. The verifier checks that each $T_c$ and $T_c'$ falls within allowed absolute differences (which account for numerical solver choice) and verifies qualitative physical trends (e.g. the behaviour of $T_c$ as a function of $H$ and the relative ordering of $T_c$ and $T_c'$ within a certain field range). Simply reporting the correct numbers without the required computation will not satisfy the checks. Score is based on how well your produced phase diagram matches the reference within tolerance and obeys the expected trends.
