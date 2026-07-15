# Magnetization curves of an amorphous ferrimagnet with bond disorder

## Problem background
Amorphous rare‑earth–transition‑metal ferrimagnets are important for applications such as thermomagnetic recording. A theoretical model of an amorphous noncollinear mixed ferrimagnet considers a lattice of spin‑1/2 and spin‑1 ions interacting via nearest‑neighbour exchange, with independent transverse fields on each sublattice. Structural disorder is modelled by a random binary distribution of exchange interaction strengths, parametrised by a disorder amplitude δ. The central question is how this disorder affects the temperature dependence of the system’s total longitudinal and transverse magnetizations.

## Approach
The system is described by the Hamiltonian

$$ \mathcal{H} = - \sum_{\langle i,j \rangle} J_{ij} \mu_i^z s_j^z - \Omega_0 \sum_i \mu_i^x - \Omega_1 \sum_j s_j^x $$

where $\mu_i^\alpha$ ($s_j^\alpha$) are spin‑1/2 (spin‑1) operators, $J_{ij}$ is a random nearest‑neighbour exchange with the binary distribution

$$ P(J) = \frac12[\delta(J-J(1+\delta)) + \delta(J-J(1-\delta))], $$

and $\Omega_0,\Omega_1$ are transverse fields.  Within the effective‑field theory with correlations, the sublattice magnetizations $\sigma_z,\sigma_x$ (spin‑1/2) and $m_z,m_x$ (spin‑1) together with the quadrupolar parameter $q_z=\langle (s_j^z)^2\rangle$ satisfy the following self‑consistent equations:

$$
\begin{aligned}
\sigma_z &= \big[ q_z \langle\cosh(J D)\rangle_r - m_z \langle\sinh(J D)\rangle_r + 1 - q_z \big]^z f(x)\big|_{x=0},\\
\sigma_x &= \big[ q_z \langle\cosh(J D)\rangle_r - m_z \langle\sinh(J D)\rangle_r + 1 - q_z \big]^z g(x)\big|_{x=0},\\
m_z    &= \big[ \langle\cosh(\tfrac12 J D)\rangle_r - 2\sigma_z \langle\sinh(\tfrac12 J D)\rangle_r \big]^z F(x)\big|_{x=0},\\
m_x    &= \big[ \langle\cosh(\tfrac12 J D)\rangle_r - 2\sigma_z \langle\sinh(\tfrac12 J D)\rangle_r \big]^z G(x)\big|_{x=0},\\
q_z    &= \big[ \langle\cosh(\tfrac12 J D)\rangle_r - 2\sigma_z \langle\sinh(\tfrac12 J D)\rangle_r \big]^z H(x)\big|_{x=0},
\end{aligned}
$$

where $D = \partial/\partial x$ and $z$ is the coordination number (here $z=4$).  The random‑bond averages under the binary distribution simplify to

$$
\begin{aligned}
\langle\cosh(\gamma J D)\rangle_r &= \cosh(\gamma J\delta D)\,\cosh(\gamma J D),\\
\langle\sinh(\gamma J D)\rangle_r &= \cosh(\gamma J\delta D)\,\sinh(\gamma J D),
\end{aligned}
$$

with $\gamma=1$ for the spin‑1/2 equations and $\gamma=\tfrac12$ for the spin‑1 equations.  The operator expression is evaluated by expanding the power and using the shift property $\exp(aD)\phi(x)=\phi(x+a)$.  The auxiliary functions are

$$
\begin{aligned}
f(x) &= \frac12 \frac{x}{\sqrt{\Omega_0^2+x^2}} \tanh\!\Big(\frac{\beta}{2}\sqrt{\Omega_0^2+x^2}\Big),\\
g(x) &= \frac12 \frac{\Omega_0}{\sqrt{\Omega_0^2+x^2}} \tanh\!\Big(\frac{\beta}{2}\sqrt{\Omega_0^2+x^2}\Big),\\
F(x) &= \frac{x}{\sqrt{\Omega_1^2+x^2}} \frac{2\sinh(\beta\sqrt{\Omega_1^2+x^2})}{1+2\cosh(\beta\sqrt{\Omega_1^2+x^2})},\\
G(x) &= \frac{\Omega_1}{\sqrt{\Omega_1^2+x^2}} \frac{2\sinh(\beta\sqrt{\Omega_1^2+x^2})}{1+2\cosh(\beta\sqrt{\Omega_1^2+x^2})},\\
H(x) &= \frac{\Omega_1^2 + (\Omega_1^2+2x^2)\cosh(\beta\sqrt{\Omega_1^2+x^2})}{(\Omega_1^2+x^2)\,[1+2\cosh(\beta\sqrt{\Omega_1^2+x^2})]},
\end{aligned}
$$

where $\beta = 1/(k_B T)$.  The total longitudinal and transverse magnetizations per site are

$$
M_z = \frac{m_z + \sigma_z}{2}, \qquad M_x = \frac{m_x + \sigma_x}{2}.
$$

Solving strategy: for each fixed $T$ and $\delta$, start with an initial guess (e.g., $\sigma_z,\sigma_x,m_z,m_x,q_z$ at zero temperature), compute the right‑hand sides by expanding the binomial powers of the operator expressions, evaluate the shifted auxiliary functions, and iterate to convergence (e.g., by simple mixing).  The fixed parameters are $\Omega_0 = 0.05\,J$, $\Omega_1 = 3.65\,J$, $z = 4$, and all energies/temperatures are in units of $J$ (i.e., $k_B=1$).

## Reproduction target
Produce two CSV files:

1. `/app/outputs/magnetization_curves.csv` – for disorder strengths δ = 0.0, 0.2, 0.4, cover a dense temperature grid from near zero to above the Curie temperature. Each row gives δ, T, M_z, M_x (per‑site magnetizations).
2. `/app/outputs/magnetization_vs_delta.csv` – for fixed temperatures T = 0.1 J and 0.35 J, sweep δ from 0.0 to 0.5 in steps no larger than 0.02. Each row gives T, δ, M_z, M_x (per‑site values).

All energies and temperatures are expressed in units of J.

## Assets

- Python scientific computing stack: numpy, scipy

## Workflow steps

### Step 1: Compute magnetization curves vs temperature for three disorder strengths
- Role: scored (load-bearing)
- Action: Implement the self-consistent effective-field equations for the two sublattices (spin‑1/2 and spin‑1) with transverse fields, incorporating the random-bond average using the binary bond distribution. For the fixed parameters Ω₀=0.05 J, Ω₁=3.65 J, coordination number z=4, and disorder strengths δ=0.0, 0.2, 0.4, solve the coupled equations iteratively on a dense temperature grid from near zero to above the Curie temperature. Compute the total longitudinal M_z and transverse M_x magnetizations per site. Write the results to magnetization_curves.csv.
- Output file: `/app/outputs/magnetization_curves.csv`
- Format: csv
- Contract: CSV with header: δ, T, M_z, M_x. δ is one of 0.0, 0.2, 0.4. T is in units of J, ranging from near zero to above the Curie temperature. M_z and M_x are per‑site values (floats).
- Scoring: scored by hidden verifier

### Step 2: Compute magnetization vs disorder strength at fixed temperatures
- Role: scored
- Action: Using the same solver as step_01, fix temperatures T=0.1 J and 0.35 J and vary the disorder amplitude δ from 0.0 to 0.5 in fine steps (at most 0.02). Compute the total longitudinal M_z and transverse M_x per site for each (T,δ) pair and write the results to magnetization_vs_delta.csv.
- Output file: `/app/outputs/magnetization_vs_delta.csv`
- Format: csv
- Contract: CSV with header: T, δ, M_z, M_x. T is 0.1 or 0.35 (J). δ ranges from 0.0 to 0.5 in steps of at most 0.02. M_z and M_x are per‑site values (floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_curves.csv`
- `/app/outputs/magnetization_vs_delta.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_curves.csv
- path: `/app/outputs/magnetization_curves.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetization curves as functions of temperature for δ=0.0, 0.2, 0.4. The checker reads these curves and extracts physically meaningful features (compensation temperature, curve shape, monotonicity) to compare against paper‑derived hidden gold values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `δ`, `T`, `M_z`, `M_x`
  - `units`:
    - `δ`: dimensionless
    - `T`: energy (J)
    - `M_z`: per‑site magnetization
    - `M_x`: per‑site magnetization

### magnetization_vs_delta.csv
- path: `/app/outputs/magnetization_vs_delta.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetization vs disorder strength δ at fixed temperatures T=0.1 J and 0.35 J. The checker verifies the non‑monotonic shape and crossing features against paper‑reported reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `δ`, `M_z`, `M_x`
  - `units`:
    - `T`: energy (J)
    - `δ`: dimensionless
    - `M_z`: per‑site magnetization
    - `M_x`: per‑site magnetization

Notes: The hidden checker recomputes compensation temperatures, monotonicity, and characteristic values from the submitted CSVs and compares them against paper‑reported numbers within tolerance. The tolerance is set to absorb typical numerical differences from different solver implementations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "δ",
          "T",
          "M_z",
          "M_x"
        ],
        "units": {
          "δ": "dimensionless",
          "T": "energy (J)",
          "M_z": "per‑site magnetization",
          "M_x": "per‑site magnetization"
        }
      },
      "description": "Magnetization curves as functions of temperature for δ=0.0, 0.2, 0.4. The checker reads these curves and extracts physically meaningful features (compensation temperature, curve shape, monotonicity) to compare against paper‑derived hidden gold values with tolerance."
    },
    {
      "file": "magnetization_vs_delta.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "δ",
          "M_z",
          "M_x"
        ],
        "units": {
          "T": "energy (J)",
          "δ": "dimensionless",
          "M_z": "per‑site magnetization",
          "M_x": "per‑site magnetization"
        }
      },
      "description": "Magnetization vs disorder strength δ at fixed temperatures T=0.1 J and 0.35 J. The checker verifies the non‑monotonic shape and crossing features against paper‑reported reference values within tolerance."
    }
  ],
  "notes": "The hidden checker recomputes compensation temperatures, monotonicity, and characteristic values from the submitted CSVs and compares them against paper‑reported numbers within tolerance. The tolerance is set to absorb typical numerical differences from different solver implementations."
}
```

## How you are scored
A hidden verifier loads your two CSV files, analyzes the temperature and disorder dependencies to extract characteristic features (such as the position and existence of zero‑crossings, monotonicity of the curves, and relative behaviour under different δ conditions) and compares them against expected values within tolerance. Each scored stage contributes a weighted share to the overall reward, which ranges from 0 (failure) to 1 (perfect reproduction). The verifier does not simply compare raw numbers; it checks that the computed physical features agree with the expected behaviour. The better the agreement, the higher the reward.
