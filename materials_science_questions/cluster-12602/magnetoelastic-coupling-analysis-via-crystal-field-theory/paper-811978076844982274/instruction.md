# Magnetoelastic Metamagnetism Simulation via Molecular Field Approximation

## Problem background
The magnetization of two‑sublattice axial magnets is described by a magnetoelastic Hamiltonian that includes Ising exchange, exchange-strain coupling, and strain-coupled single-ion anisotropy. Within the mean-field approximation (MFA) this leads to coupled self-consistency equations for the sublattice magnetizations, quadrupole moments, and the equilibrium strain. For certain choices of the dimensionless material parameters, the system can undergo a temperature-induced phase transition from an antiferromagnetic (A) phase to a ferromagnetic (F) phase. This task investigates whether such a transition occurs for a specific parameter set.

## Approach
The MFA provides exact self-consistency equations for the sublattice magnetization σ and the equilibrium strain ε in two magnetic phases.  
**Fixed dimensionless parameters** (identical to Fig. 5 of the paper):
- \(k = -1.1\)
- \(c = 1.0\)
- \(l = 1.0\)
- \(m = 2.0\)

The reduced temperature is \(t = k_{\mathrm B}T/(z_1 I)\) (all energies are measured in units of \(z_1 I\)).

---

### 1. Self-consistency equations for the antiferromagnetic (A) phase
In the A phase the sublattice magnetizations satisfy \(\sigma_1 = -\sigma_2 = \sigma\). The two coupled equations are

\[
\sigma \;=\; \frac{2\,e^{\,l\varepsilon/t}\;\sinh\!\bigl(\sigma\,(m-(1+k\varepsilon))/t\bigr)}
{2\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m-(1+k\varepsilon))/t\bigr) \;+\; 1} ,
\tag{1}
\]

\[
\varepsilon \;=\; \frac{1}{2c}\,
\left[\;
\frac{4l\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m-(1+k\varepsilon))/t\bigr)}
{2\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m-(1+k\varepsilon))/t\bigr) \;+\; 1}
\;-\; \sigma^2 k
\right].
\tag{2}
\]

After solving these equations the quadrupole moments are given by

\[
Q_1 = Q_2 = Q = 
\frac{2\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m-(1+k\varepsilon))/t\bigr)}
{2\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m-(1+k\varepsilon))/t\bigr) \;+\; 1}.
\tag{3}
\]

---

### 2. Self-consistency equations for the ferromagnetic (F) phase
In the F phase \(\sigma_1 = \sigma_2 = \sigma\). The equations become

\[
\sigma \;=\; \frac{2\,e^{\,l\varepsilon/t}\;\sinh\!\bigl(\sigma\,(m+1+k\varepsilon)/t\bigr)}
{2\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m+1+k\varepsilon)/t\bigr) \;+\; 1},
\tag{4}
\]

\[
\varepsilon \;=\; \frac{1}{2c}\,
\left[\;
\frac{4l\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m+1+k\varepsilon)/t\bigr)}
{2\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m+1+k\varepsilon)/t\bigr) \;+\; 1}
\;+\; \sigma^2 k
\right],
\tag{5}
\]

and the quadrupole moments are again

\[
Q_1 = Q_2 = Q = 
\frac{2\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m+1+k\varepsilon)/t\bigr)}
{2\,e^{\,l\varepsilon/t}\;\cosh\!\bigl(\sigma\,(m+1+k\varepsilon)/t\bigr) \;+\; 1}.
\tag{6}
\]

---

### 3. Free energy density \(f\)
The dimensionless free energy density (per two sublattice sites) is given by

\[
\begin{aligned}
f &= -t\,\Bigl[\,\ln\!\bigl(2\,e^{y_2/t}\cosh(y_1/t)+1\bigr)
          + \ln\!\bigl(2\,e^{y_4/t}\cosh(y_3/t)+1\bigr)\Bigr] \\
  &\quad - \sigma_1\sigma_2\,(1+k\varepsilon)
    - l\,\varepsilon\,(Q_1+Q_2)
    - \tfrac12\,m\,(\sigma_1^2+\sigma_2^2) \\
  &\quad + y_1\sigma_1 + y_3\sigma_2
    + y_2 Q_1 + y_4 Q_2
    + c\,\varepsilon^2 ,
\end{aligned}
\tag{7}
\]

where the auxiliary fields are

\[
\begin{aligned}
y_1 &= \sigma_2\,(1+k\varepsilon) + \sigma_1\,m, \\
y_2 &= y_4 = l\varepsilon, \\
y_3 &= \sigma_1\,(1+k\varepsilon) + \sigma_2\,m .
\end{aligned}
\tag{8}
\]

- For the **A phase** use \(\sigma_1 = -\sigma\), \(\sigma_2 = \sigma\), \(Q_1=Q_2=Q\) from (3).
- For the **F phase** use \(\sigma_1 = \sigma\), \(\sigma_2 = \sigma\), \(Q_1=Q_2=Q\) from (6).

---

### 4. Special treatment at \(t = 0\)
Equations (1)–(2) and (4)–(5) are singular at \(t=0\). The exact analytic limits are:

- **A phase** (antiferromagnetic):
  \[
  \sigma_{\mathrm A} = 1,\qquad
  \varepsilon_{\mathrm A} = \frac{2l - k}{2c},\qquad
  f_{\mathrm A} = 1 - m - \frac{(2l-k)^2}{4c}.
  \tag{9}
  \]

- **F phase** (ferromagnetic):
  \[
  \sigma_{\mathrm F} = 1,\qquad
  \varepsilon_{\mathrm F} = \frac{2l + k}{2c},\qquad
  f_{\mathrm F} = -1 - m - \frac{(2l+k)^2}{4c}.
  \tag{10}
  \]

When solving the equations, use these closed-form values at \(t = 0\) and begin the numerical iteration from these values for \(t>0\).

---

### 5. Numerical solution
For a dense temperature grid (\(t\) from 0 to 2, at least 100 equally spaced points) you must:
1. At \(t=0\) record the analytic values (9)–(10).
2. For \(t>0\) solve the coupled equations (1)–(2) for A phase and (4)–(5) for F phase simultaneously. Use a robust root‑finder (e.g., `scipy.optimize.fsolve`) with initial guesses taken from the previous temperature step or from the \(t=0\) solution.
3. After obtaining \(\sigma\) and \(\varepsilon\) for each phase, compute \(Q\) via (3) or (6) and then the free energy \(f\) via (7) using the appropriate signs for \(\sigma_1,\sigma_2\).
4. Write all results to a CSV file.

The key scientific question is whether \(f_{\mathrm F}\) becomes lower than \(f_{\mathrm A}\) at some finite temperature, signalling an A→F transition.

## Reproduction target
For the parameter set \(k = -1.1, c = 1, l = 1, m = 2\), solve the MFA self-consistency equations for the antiferromagnetic (A) and ferromagnetic (F) phases on a grid of reduced temperature \(t\) spanning at least 100 evenly spaced points from 0 to 2. For each \(t\) and each phase, compute the sublattice magnetization σ, the equilibrium strain ε, and the free energy density f. Write all results to `/app/outputs/magnetoelastic_results.csv` with columns: `t`, `sigma_A`, `sigma_F`, `epsilon_A`, `epsilon_F`, `f_A`, `f_F` (all floating-point numbers). Your numerical solution should reveal whether an A→F transition exists for this parameter set and, if so, approximately where it occurs.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Magnetoelastic simulation for A and F phases
- Role: scored (load-bearing)
- Action: Implement the molecular-field (MFA) self-consistency equations for the antiferromagnetic (A) and ferromagnetic (F) phases as detailed in the Approach section. Solve the coupled transcendental equations numerically for a grid of reduced temperature \(t\) from 0 to 2 (at least 100 evenly spaced points). For each phase, compute the sublattice magnetization σ, equilibrium strain ε, and free energy density f. Output all results to a CSV file.
- Output file: `/app/outputs/magnetoelastic_results.csv`
- Format: csv
- Contract: columns: `t` (float), `sigma_A` (float), `sigma_F` (float), `epsilon_A` (float), `epsilon_F` (float), `f_A` (float), `f_F` (float); header required; at least 100 evenly spaced t points in [0.0, 2.0]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetoelastic_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetoelastic_results.csv
- path: `/app/outputs/magnetoelastic_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Table of reduced temperature t, sublattice magnetizations sigma_A/F, equilibrium strains epsilon_A/F, and free energy densities f_A/F for the antiferromagnetic and ferromagnetic phases. The checker will recompute the free energy RMSE against hidden gold values and verify the A→F phase transition crossing.
- schema:
  - `type`: table
  - `required_columns`: `t`, `sigma_A`, `sigma_F`, `epsilon_A`, `epsilon_F`, `f_A`, `f_F`
  - `units`: object

Notes: The task reproduces the main numerical result (Fig. 5) of the paper. The earlier critical‑temperature parameter scan is not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetoelastic_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "sigma_A",
          "sigma_F",
          "epsilon_A",
          "epsilon_F",
          "f_A",
          "f_F"
        ],
        "units": {}
      },
      "description": "Table of reduced temperature t, sublattice magnetizations sigma_A/F, equilibrium strains epsilon_A/F, and free energy densities f_A/F for the antiferromagnetic and ferromagnetic phases. The checker will recompute the free energy RMSE against hidden gold values and verify the A→F phase transition crossing."
    }
  ],
  "notes": "The task reproduces the main numerical result (Fig. 5) of the paper. The earlier critical‑temperature parameter scan is not required."
}
```

## How you are scored
Your submission will be evaluated by a hidden autograder. For the scored output file `magnetoelastic_results.csv`, the grader independently recomputes the free energy density f_A and f_F at several probe temperatures using the same model parameters and equations. It computes the relative root-mean-square error (RMSE) between your free energy values and the recomputed ”gold” values; this RMSE determines a performance score. In addition, the grader checks whether your data shows a temperature at which f_A and f_F cross (i.e., the F phase becomes more stable than the A phase) within a physically plausible range. The final reward is a weighted combination of these checks, with the primary weight on the free-energy RMSE. There is no need to match the paper’s exact numerical method; as long as your solutions are correct to within the accuracy of floating-point computation, you will receive full credit.