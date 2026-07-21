# Tricritical Points of the Diluted Transverse Spin-1 Ising Model

## Problem background
The diluted transverse spin-1 Ising model with a longitudinal crystal field exhibits finite-temperature phase transitions that can be second or first order, with tricritical points separating the two regimes. By varying the concentration of magnetic atoms, the transverse field, and the crystal field, the phase boundaries and the location of tricritical points can be mapped, revealing re‑entrant phenomena in certain parameter ranges. This work explores how dilution and external fields influence the tricritical behavior of the system on a square lattice.

## Approach
We consider a single spin‑1 ion with its nearest neighbours. The effective single‑site Hamiltonian (in units of $k_B=1$) is
$$
H_0 = -a_1 S_z - \sqrt{2}\,a_2 S_x - a_3 S_z^2,
$$
where $S_z$ and $S_x$ are the spin‑1 matrices
$$ S_z = \begin{pmatrix}1&0&0\\0&0&0\\0&0&-1\end{pmatrix},\quad
S_x = \frac{1}{\sqrt{2}}\begin{pmatrix}0&1&0\\1&0&1\\0&1&0\end{pmatrix}, $$
and the coefficients depend on the neighbour‑sum $\gamma$:
$$ a_1 = \beta J \gamma,\quad a_2 = \beta\Omega/\sqrt{2},\quad a_3 = \beta D,\quad \beta=1/(k_B T). $$

Diagonalising this $3\times3$ matrix gives eigenvalues $E_k$ and eigenstates $|\Psi_k\rangle$ ($k=1,2,3$). The single‑site thermal expectation values are
$$
F_{1z}(\gamma) = \frac{\sum_{k=1}^3 \langle\Psi_k|S_z|\Psi_k\rangle e^{-\beta E_k}}
                       {\sum_{k=1}^3 e^{-\beta E_k}},\qquad
F_{2z}(\gamma) = \frac{\sum_{k=1}^3 \langle\Psi_k|S_z^2|\Psi_k\rangle e^{-\beta E_k}}
                       {\sum_{k=1}^3 e^{-\beta E_k}}.
$$

For a diluted square lattice (coordination $N=4$) the configurational average yields the self‑consistent equation for the zero‑magnetisation quadrupolar moment $q_{0z}$:
$$
\begin{aligned}
q_{0z} = \;& 2^{-N}\!\sum_{\mu_1=0}^{N}\sum_{\mu_2=0}^{N-\mu_1}\sum_{\mu_3=0}^{N-\mu_1-\mu_3}
C_{\mu_1}^{N} C_{\mu_2}^{N-\mu_1} C_{\mu_3}^{N-\mu_1-\mu_2}
\,2^{\mu_1+\mu_3}\,(1-c)^{\mu_1}\,(c-q_{0z})^{\mu_3}\,q_{0z}^{N-\mu_1-\mu_3} \\
&\qquad\times F_{2z}\!\bigl(\beta J (N-\mu_1-2\mu_2-\mu_3)\bigr),
\end{aligned}
$$
where $C_k^l$ are binomial coefficients.

When the magnetisation $m_z$ is small, the expansion $m_z = a m_z + b m_z^3 + \cdots$ yields the Landau coefficients
$$
\begin{aligned}
a = \;& 2^{-N}\!\sum_{\mu_1=0}^{N}\sum_{\mu_2=0}^{N-\mu_1}\sum_{\mu_3=0}^{N-\mu_1-\mu_3}\sum_{i=0}^{\mu_2}\sum_{j=0}^{N-\mu_1-\mu_2-\mu_3}
2^{\mu_1+\mu_3}
C_{\mu_1}^{N} C_{\mu_2}^{N-\mu_1} C_{\mu_3}^{N-\mu_1-\mu_2}
C_{i}^{\mu_2} C_{j}^{N-\mu_1-\mu_2-\mu_3}
(-1)^i \, q_{0z}^{N-\mu_1-\mu_3-i-j} \\
&\qquad\times (1-c)^{\mu_1}\,(c-q_{0z})^{\mu_2}\,\delta_{1,i+j}
F_{1z}\!\bigl(\beta J (N-\mu_1-2\mu_2-\mu_3)\bigr), \\[6pt]
b = \;& 2^{-N}\!\sum_{\mu_1=0}^{N}\sum_{\mu_2=0}^{N-\mu_1}\sum_{\mu_3=0}^{N-\mu_1-\mu_3}\sum_{i=0}^{\mu_2}\sum_{j=0}^{N-\mu_1-\mu_2-\mu_3}
2^{\mu_1+\mu_3}
C_{\mu_1}^{N} C_{\mu_2}^{N-\mu_1} C_{\mu_3}^{N-\mu_1-\mu_2}
C_{i}^{\mu_2} C_{j}^{N-\mu_1-\mu_2-\mu_3}
(-1)^i \, q_{0z}^{N-\mu_1-\mu_3-i-j} \\
&\qquad\times (1-c)^{\mu_1}\,(c-q_{0z})^{\mu_3}\,\delta_{3,i+j}
F_{1z}\!\bigl(\beta J (N-\mu_1-2\mu_2-\mu_3)\bigr).
\end{aligned}
$$

A second‑order transition occurs when $a=1$ and $b<0$; the tricritical point is the simultaneous solution of $a=1$ and $b=0$, giving the tricritical temperature $T_t/J$ and crystal field $-D_t/J$.

## Reproduction target
Implement the effective-field theory and compute the tricritical temperature Tt/J and tricritical longitudinal crystal field –Dt/J for the square lattice (coordination number N=4) at three specific parameter pairs: (c=1.0, Ω/J=0.1), (c=0.8, Ω/J=0.1), and (c=0.8, Ω/J=0.5). Output the results as a JSON array of objects with keys c, Omega_over_J, Tt_over_J, neg_Dt_over_J in the file '/app/outputs/tricritical_points.json'.

## Assets

- Python: https://www.python.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement single-site effective-field model
- Role: process
- Action: Diagonalize the single-site Hamiltonian H0 in the spin-1 basis to obtain eigenvalues and eigenvectors, and implement the functions F1z and F2z that give the single-site thermal expectation values of S_z and S_z^2 for a given neighbor sum. These functions are used in all subsequent steps.
- Evidence: none

### Step 2: Solve zero-magnetization quadrupolar moment q0z
- Role: process
- Action: For each required parameter set (c, Omega/J) and over a grid of temperature T/J and longitudinal crystal field D/J, solve the self-consistent equation for the zero-magnetization quadrupolar moment q0z using the function F2z. Use iterative methods to converge q0z(T, D). This step provides the background needed for the Landau expansion.
- Evidence: none

### Step 3: Determine tricritical points
- Role: scored (load-bearing)
- Action: Using the q0z solutions, compute the Landau expansion coefficients a and b for each parameter set, then locate the tricritical point by solving a=1 and b=0 simultaneously to obtain Tt/J and neg_Dt_over_J for the specified (c, Omega/J) pairs: (c=1.0, Omega/J=0.1), (c=0.8, Omega/J=0.1), (c=0.8, Omega/J=0.5). Output the results in tricritical_points.json.
- Output file: `/app/outputs/tricritical_points.json`
- Format: json
- Contract: Array of objects with keys: c (float), Omega_over_J (float), Tt_over_J (float), neg_Dt_over_J (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tricritical_points.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tricritical_points.json
- path: `/app/outputs/tricritical_points.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed tricritical points; compared to hidden reference values from the paper with a tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `c`:
        - `type`: number
        - `description`: magnetic atom concentration
      - `Omega_over_J`:
        - `type`: number
        - `description`: transverse field divided by exchange coupling
      - `Tt_over_J`:
        - `type`: number
        - `description`: tricritical temperature in units of J/k_B
      - `neg_Dt_over_J`:
        - `type`: number
        - `description`: absolute value of tricritical longitudinal crystal field divided by J
    - `required`: `c`, `Omega_over_J`, `Tt_over_J`, `neg_Dt_over_J`
  - `minItems`: 3
  - `maxItems`: 3

Notes: The agent must implement the effective-field theory from the given formulas; no external datasets are needed. The hidden checker compares the reported Tt_over_J and neg_Dt_over_J to gold values with relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tricritical_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "c": {
              "type": "number",
              "description": "magnetic atom concentration"
            },
            "Omega_over_J": {
              "type": "number",
              "description": "transverse field divided by exchange coupling"
            },
            "Tt_over_J": {
              "type": "number",
              "description": "tricritical temperature in units of J/k_B"
            },
            "neg_Dt_over_J": {
              "type": "number",
              "description": "absolute value of tricritical longitudinal crystal field divided by J"
            }
          },
          "required": [
            "c",
            "Omega_over_J",
            "Tt_over_J",
            "neg_Dt_over_J"
          ]
        },
        "minItems": 3,
        "maxItems": 3
      },
      "description": "Computed tricritical points; compared to hidden reference values from the paper with a tolerance."
    }
  ],
  "notes": "The agent must implement the effective-field theory from the given formulas; no external datasets are needed. The hidden checker compares the reported Tt_over_J and neg_Dt_over_J to gold values with relative tolerance."
}
```

## How you are scored
A hidden verifier independently reads your tricritical_points.json and compares each reported coordinate (Tt_over_J and neg_Dt_over_J) against a hidden reference standard derived from the paper’s published results. Full credit is awarded when all coordinates are reproduced within the required precision; partial credit is given proportionally to the number of correctly reproduced coordinates. The verifier may also check that tricritical points are not improperly reported for parameter regions where no tricritical point exists.
