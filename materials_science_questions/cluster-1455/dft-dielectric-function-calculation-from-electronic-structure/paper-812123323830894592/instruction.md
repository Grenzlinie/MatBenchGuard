# VB-CT model computation of curvature contributions to static electrical properties of push-pull systems

## Problem background
Push–pull π-conjugated systems, in which an electron donor and an electron acceptor are linked by a π-conjugated bridge, are known for large nonlinear optical responses. Their static electrical properties—dipole moment μ, polarizability α, and first and second hyperpolarizabilities β and γ—receive several contributions: electronic, vibrational, curvature, and rotational. Within the valence‑bond charge‑transfer (VB‑CT) model and the analytical evaluation of electrical properties (AEEP) method, analytic relationships have been derived that link the curvature contribution directly to the electronic hyperpolarizabilities. This task reproduces the numerical evaluation of these curvature contributions for a specific push–pull system, computing the electronic, vibrational, and curvature components as functions of the charge‑transfer fraction f using the model parameters reported in the literature.

## Approach
The VB‑CT model describes the ground‑state potential energy of a push–pull molecule as a function of the bond‑length alternation (BLA) coordinate q and an applied static electric field ε. The model parameters are the harmonic force constant k, the transfer integral t, the equilibrium BLA coordinates of the valence‑bond (VB) and charge‑transfer (CT) diabatic states, the dipole moment of the CT state μ_CT, and an effective reduced mass μ_bar. For a given electronic energy offset Vₒ, the equilibrium BLA coordinate q_eq and the effective energy gap V are found self‑consistently, defining the CT fraction f (the weight of the CT state in the ground state). From V and t, the electronic hyperpolarizabilities α_el, β_el, γ_el, δ_el, and χ_el are computed using closed‑form expressions of the VB‑CT model. The harmonic force constant K of the ground‑state potential and its first four field derivatives are obtained from the coefficients of the expansion of the potential energy, taking into account mechanical and electrical anharmonicities. The curvature contributions μ_cur, α_cur, β_cur, and γ_cur are then evaluated from K and its derivatives following the AEEP method, while the vibrational contributions α_vib, β_vib, and γ_vib are expressed in terms of the electronic hyperpolarizabilities and auxiliary factors that depend on the model parameters. To obtain the f‑dependence, the self‑consistent determination of q_eq and V is carried out for a range of Vₒ values that sweep f from 0 to 1 with a step of at most 0.01.

## Reproduction target
Implement the VB‑CT model with the parameter set: k = 33.55 eV/Å², t = 1.184 eV, q_VB⁰ = −0.12 Å, q_CT⁰ = 0.12 Å, μ_CT = 26 D, reduced mass μ_bar = 10⁻²⁶ kg. For a range of Vₒ values, iteratively solve for q_eq and V to sweep the CT fraction f from 0 to 1 (step ≤ 0.01). At each converged f, compute:

- the electronic hyperpolarizabilities α_el, β_el, γ_el, δ_el, χ_el;
- the force constant K and its field derivatives;
- the curvature contributions μ_cur, α_cur, β_cur, γ_cur;
- the vibrational contributions μ_vib, α_vib, β_vib, γ_vib.

Write the results to a CSV file curvature_contributions.csv with one row per f and columns:

f, mu_el (Debye), alpha_el (10⁻²⁴ esu), beta_el (10⁻³⁰ esu), gamma_el (10⁻³³ esu), mu_vib (Debye), alpha_vib (10⁻²⁴ esu), beta_vib (10⁻³⁰ esu), gamma_vib (10⁻³³ esu), mu_cur (Debye), alpha_cur (10⁻²⁴ esu), beta_cur (10⁻³⁰ esu), gamma_cur (10⁻³³ esu).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define VB-CT model equations and parameters
- Role: process
- Action: Implement the VB-CT model: the ground-state potential energy U(q,ε), the AEEP expansion, the electronic hyperpolarizabilities (α, β, γ, δ, χ) as functions of V and t, the force constant K and its first four field-derivatives, the curvature contributions (μ_cur, α_cur, β_cur, γ_cur), and the vibrational contributions (α_vib, β_vib, γ_vib). Hard-code the parameter set: k=33.55 eV/Å², t=1.184 eV, q_VB^o=-0.12 Å, q_CT^o=0.12 Å, μ_CT=26 D, reduced mass μ_bar=10⁻²⁶ kg. Include the self-consistent iteration for q_eq and V.
- Evidence: none

### Step 2: Compute all contributions for f sweep
- Role: process
- Action: For a range of V_o values that yields CT fraction f from 0 to 1 with step at most 0.01, iteratively solve for q_eq, V, and f. For each converged point, compute the electronic hyperpolarizabilities, the force constant K and its field-derivatives, the curvature contributions, and the vibrational contributions. Accumulate all results.
- Evidence: `/app/outputs/scan_log.txt`

### Step 3: Write curvature_contributions.csv
- Role: scored (load-bearing)
- Action: Write the computed quantities to curvature_contributions.csv. One row per f value. Columns: f (float), mu_el (Debye), alpha_el (1e-24 esu), beta_el (1e-30 esu), gamma_el (1e-33 esu), mu_vib (Debye), alpha_vib (1e-24 esu), beta_vib (1e-30 esu), gamma_vib (1e-33 esu), mu_cur (Debye), alpha_cur (1e-24 esu), beta_cur (1e-30 esu), gamma_cur (1e-33 esu).
- Output file: `/app/outputs/curvature_contributions.csv`
- Format: csv
- Contract: f (float); mu_el (float, Debye); alpha_el (float, 1e-24 esu); beta_el (float, 1e-30 esu); gamma_el (float, 1e-33 esu); mu_vib (float, Debye); alpha_vib (float, 1e-24 esu); beta_vib (float, 1e-30 esu); gamma_vib (float, 1e-33 esu); mu_cur (float, Debye); alpha_cur (float, 1e-24 esu); beta_cur (float, 1e-30 esu); gamma_cur (float, 1e-33 esu).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/curvature_contributions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### curvature_contributions.csv
- path: `/app/outputs/curvature_contributions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed electronic, vibrational, and curvature contributions to static dipole moment, polarizability, and hyperpolarizabilities as functions of the CT fraction f.
- schema:
  - `type`: table
  - `required_columns`: `f`, `mu_el`, `alpha_el`, `beta_el`, `gamma_el`, `mu_vib`, `alpha_vib`, `beta_vib`, `gamma_vib`, `mu_cur`, `alpha_cur`, `beta_cur`, `gamma_cur`
  - `units`:
    - `f`: 
    - `mu_el`: Debye
    - `alpha_el`: 10^{-24} esu
    - `beta_el`: 10^{-30} esu
    - `gamma_el`: 10^{-33} esu
    - `mu_vib`: Debye
    - `alpha_vib`: 10^{-24} esu
    - `beta_vib`: 10^{-30} esu
    - `gamma_vib`: 10^{-33} esu
    - `mu_cur`: Debye
    - `alpha_cur`: 10^{-24} esu
    - `beta_cur`: 10^{-30} esu
    - `gamma_cur`: 10^{-33} esu

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "curvature_contributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "mu_el",
          "alpha_el",
          "beta_el",
          "gamma_el",
          "mu_vib",
          "alpha_vib",
          "beta_vib",
          "gamma_vib",
          "mu_cur",
          "alpha_cur",
          "beta_cur",
          "gamma_cur"
        ],
        "units": {
          "f": "",
          "mu_el": "Debye",
          "alpha_el": "10^{-24} esu",
          "beta_el": "10^{-30} esu",
          "gamma_el": "10^{-33} esu",
          "mu_vib": "Debye",
          "alpha_vib": "10^{-24} esu",
          "beta_vib": "10^{-30} esu",
          "gamma_vib": "10^{-33} esu",
          "mu_cur": "Debye",
          "alpha_cur": "10^{-24} esu",
          "beta_cur": "10^{-30} esu",
          "gamma_cur": "10^{-33} esu"
        }
      },
      "description": "Computed electronic, vibrational, and curvature contributions to static dipole moment, polarizability, and hyperpolarizabilities as functions of the CT fraction f."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier program recomputes each numerical column (mu_el, alpha_el, …, gamma_cur) from the f column in your CSV, using the same VB‑CT model and parameter values. For each column, your reported values are compared to the recomputed reference. The final reward is a weighted average of the per‑column scores: collectively, the curvature columns (mu_cur, alpha_cur, beta_cur, gamma_cur) carry weight 0.7; the electronic columns (mu_el, alpha_el, beta_el, gamma_el) carry weight 0.2; and the vibrational columns (mu_vib, alpha_vib, beta_vib, gamma_vib) carry weight 0.1. To succeed you must produce the CSV through an honest re‑implementation; mere self‑reporting of expected numbers without the correct computation will not pass the verifier's recomputation.
