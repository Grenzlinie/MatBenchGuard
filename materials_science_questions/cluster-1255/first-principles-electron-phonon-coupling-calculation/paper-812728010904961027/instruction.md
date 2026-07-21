# Resistivity and electron distribution from analytic solution of the Boltzmann equation for a model metal with umklapp scattering

## Problem background
At low temperatures the electrical resistivity of polyvalent metals whose Fermi surface intersects the Brillouin‑zone boundary deviates from Matthiessen's rule. This task addresses the underlying physics by computing the electrical resistivity and the nonequilibrium electron distribution function from an approximate solution to the coupled electron‑phonon Boltzmann equations. The model represents a metal with a spherical Fermi surface, two Brillouin‑zone boundaries, and anisotropic umklapp electron‑phonon scattering, intended to capture the behaviour of materials like aluminium. The goal is to produce the temperature‑dependent resistivity and the distribution function as predicted by the analytic model, which demonstrate how umklapp processes dominate the deviations from classical scattering behaviour.

## Model parameters (Aluminum)
All physical constants must be set to the values below.  These follow the free‑electron model for aluminium and the 1‑OPW pseudopotential scheme described in the paper.

| Symbol         | Value                              | Description                                                               |
|----------------|------------------------------------|---------------------------------------------------------------------------|
| `k_F`          | 1.75 × 10¹⁰ m⁻¹                     | Fermi wave number (1.75 Å⁻¹)                                              |
| `m_star`       | 9.11 × 10⁻³¹ kg (free electron mass) | Effective electron mass                                                   |
| `G`            | 2.69 × 10¹⁰ m⁻¹                     | Magnitude of the reciprocal‑lattice vector that defines the zone boundary |
| `Theta_D`      | 428 K                              | Debye temperature                                                        |
| `V_0`          | −0.220 Ry                          | Pseudopotential form factor at q = 0 (1 Ry ≈ 13.6057 eV)                 |
| `V_G`          |  0.018 Ry                          | Pseudopotential form factor at q = G                                      |
| `v_s`          | 3.0 × 10³ m s⁻¹                    | Average sound speed                                                      |
| `c`            | 4.04 Å                             | Lattice constant (used to build `G = 2π√3 / c`)                           |

## Mathematical formulation (summary of the paper)

### Boltzmann equation and Legendre expansion
The steady‑state linearised electron Boltzmann equation is solved on a spherical Fermi surface.  The electron distribution is expanded in odd Legendre polynomials,

\[
\varphi_{\vec{k}} = \varphi(\hat{k}\cdot\hat{E}) = \sum_{M=1,3,5,\dots} a_M P_M(\hat{k}\cdot\hat{E}) .
\]

Only the first coefficient \(a_1\) is retained in the analytic approximation because umklapp coupling to higher coefficients is shown to be small for the temperature and impurity ranges considered.  The resulting equation for \(a_1\) is

\[
\bigl( X'_L + C_{\text{umk}} \bigr) a_1 = -\frac{e E v_F}{3}.
\]

Here \(v_F = \hbar k_F / m^*\) is the Fermi velocity and \(e\) is the elementary charge.

### Scattering terms
- **Normal (diagonal) term \(X'_L\)**:  describes electron‑phonon scattering without umklapp and is given by the phase‑space integral

\[
X'_L = \frac{3\pi m^*}{ k_B \Theta_D } \,
\frac{1}{k_F^2} \,
\int_0^{2k_F} q^3 \, |V(q)|^2 \,
S\!\left(\frac{\hbar \omega_q}{k_B T}\right) \, dq ,
\]

where \(V(q)\) is the Ashcroft‑type pseudopotential (with \(V(0)=V_0\) and \(V(G)=V_G\); the form factor is assumed to vary slowly and can be taken as \(V(q) = V_0\) for \(q < G/2\) and \(V(q) = V_G\) for \(q \ge G/2\)), \(\hbar\omega_q = \hbar v_s q\) is the Debye‑phonon energy, and

\[
S(x) = \frac{x^2 e^x}{(e^x-1)^2}
\]

is the phonon statistical factor.  Do **not** expand \(S(x)\) at low temperature; evaluate it directly.

- **Umklapp correction \(C_{\text{umk}}\)**:  represents scattering across the Brillouin‑zone boundary.  For the two‑boundary model it is

\[
C_{\text{umk}} = \frac{3\pi m^*}{ k_B \Theta_D } \,
\frac{2}{k_F} \,
\int_{0}^{2k_F} q \, dq \,
\int_{0}^{2\pi} d\phi_q \,
\frac{q^2}{ (2\pi)^3 } \,
|V(q-G)|^2 \,
F_{\text{umk}}(q,\phi_q,T) .
\]

The kernel \(F_{\text{umk}}\) contains the same phonon factor \(S\) evaluated at a shifted wave‑vector magnitude \(|\vec{q}-\vec{G}|\) and a geometric factor that restricts the integral to the “neck” region of the Fermi surface where umklapp is kinematically allowed.  Because the angular integration is non‑trivial you should perform the two‑dimensional integral numerically using Gaussian quadrature or an equivalent method (scipy.integrate.nquad or nested quad).

- **Impurity scattering**:  enters through the impurity relaxation time \(\tau_i\), which is obtained from the given low‑temperature resistivity \(\rho_0\) by

\[
\tau_i = \frac{m^*}{n e^2 \rho_0}, \qquad
n = \frac{k_F^3}{3\pi^2} .
\]

The effective scattering rate that appears in the final expression for \(a_1\) is \((X'_L + C_{\text{umk}} + 1/\tau_i)\).

### Resistivity and distribution function

1. **Resistivity**  
   \[
   \rho(T) = \frac{m^*}{n e^2} \cdot \frac{1}{a_1}
           = \frac{m^*}{n e^2} \bigl( X'_L + C_{\text{umk}} + 1/\tau_i \bigr) \bigg/ \left(-\frac{e E v_F}{3}\right) .
   \]
   Because the right‑hand side is proportional to \(E\) and only the temperature‑dependent part is physically meaningful, the final working formula is
   \[
   \rho(T) = \rho_0 + \frac{m^*}{n e^2} \,
   \frac{ X'_L(T) + C_{\text{umk}}(T) }{ (-e E v_F/3) } .
   \]
   In practice you compute the *deviation* \(\delta\rho(T) = \rho(T) - \rho_0\) directly by evaluating \(X'_L\) and \(C_{\text{umk}}\) at each temperature.

2. **Normalised distribution function**  
   Define \(y = \hat{k}\cdot\hat{E} = \cos\theta\).  The normalised nonequilibrium distribution is
   \[
   \Phi(y) = \frac{ X'_L }{ -3A } \, \varphi(y)
   \]
   where \(A\) is a constant chosen such that \(\Phi(y) \approx y\) far from the zone boundary.  The function \(\varphi(y)\) is obtained by solving the integral equation for the full angular dependence (keeping the first few Legendre coefficients if necessary).  For the purpose of this task you can use the analytic form derived in the paper:

   \[
   \Phi(y) = y - \text{dip}(y) ,
   \]
   where the “dip” contribution is a localised reduction near \(y_0 = G/(2k_F)\).  The shape of the dip is determined by the umklapp kernel integrated over the Fermi‑surface neck.  You must evaluate it numerically from the integral equation, but the paper’s result shows a smooth dip whose centre is at \(y_0\) and whose width is controlled by the temperature and impurity parameters.

## Approach
You will implement the above formulas in a numerical Python script.  The main computational work is evaluating the integrals for \(X'_L\) and \(C_{\text{umk}}\) at the required temperatures and impurity values.  The integrals are well‑behaved and can be handled with standard quadrature.  Once the scattering terms are known the resistivity and distribution function follow from the analytic expressions.

## Reproduction target
You must produce two quantitative outputs from the model:

1. **Temperature‑dependent resistivity** – Compute the electrical resistivity \(\rho(T)\) for a fixed impurity resistivity \(\rho_0 = 0.218\times 10^{-7}\ \Omega\,\text{cm}\) at temperatures from 10 K to 300 K, using at least **20 evenly spaced points**. The electron density \(n = k_F^3/(3\pi^2)\) and the resistivity is obtained from the formula above.

2. **Nonequilibrium distribution function** – Compute the normalised distribution function \(\Phi(y)\) at a temperature of 10 K and impurity resistivity \(\rho_0 = 0.418\times 10^{-9}\ \Omega\,\text{cm}\). Evaluate it for at least **100 values of \(y\)** in the interval \([-1, 1]\), with **dense coverage** (at least 10 extra points) in the neighbourhood of the dip position \(y_0 = G/(2k_F)\) so that the shape of the dip is well resolved.

## Assets

- NumPy: numpy
- SciPy: scipy
- Aluminum model parameters (detailed in the table above)

## Workflow steps

### Step 1: Define aluminum model parameters
- Role: process
- Action: Set all physical constants to the values listed in the **Model parameters** table.  The impurity relaxation time \(\tau_i\) must be computed from the supplied \(\rho_0\) as described in the **Mathematical formulation** section.  All subsequent numerical work uses these values.
- Evidence: none

### Step 2: Compute electron‑phonon scattering rates and umklapp kernels
- Role: process
- Action: For the temperature and impurity conditions needed, numerically evaluate the normal scattering diagonal term \(X'_L\) and the umklapp scattering kernel \(C_{\text{umk}}\) using the integrals given in the **Mathematical formulation** section.  Use a Debye model for the phonon spectrum (\(\Theta_D = 428\) K) and the 1‑OPW pseudopotential matrix elements.  Perform the required one‑dimensional (\(X'_L\)) and two‑dimensional (\(C_{\text{umk}}\)) integrals with numerical quadrature (e.g. `scipy.integrate.quad`).  This produces the intermediate numerical inputs for the resistivity and distribution function computations.  Log intermediate results to a file if desired, but it is not required for scoring.
- Evidence: none

### Step 3: Compute temperature‑dependent resistivity
- Role: scored (load-bearing)
- Action: Using the precomputed scattering terms and the formula for \(\rho(T)\) that includes impurity and phonon‑drag contributions, compute the temperature‑dependent part of the electrical resistivity at the impurity resistivity \(\rho_0 = 0.218\times 10^{-7}\ \Omega\,\text{cm}\) for temperatures from 10 K to 300 K.  Output **at least 20 evenly spaced temperature points** (the scoring verifier expects a grid from 10 K to 300 K with uniform spacing).
- Output file: `/app/outputs/resistivity.csv`
- Format: csv
- Contract: columns: `T` (float, K), `rho` (float, Ω cm).  At least 20 rows, uniformly spaced between 10 K and 300 K inclusive.
- Scoring: scored by hidden verifier

### Step 4: Compute nonequilibrium distribution function
- Role: scored (load-bearing)
- Action: Using the precomputed scattering terms, evaluate the normalized nonequilibrium electron distribution function \(\Phi(y)\) at \(T = 10\) K and impurity resistivity \(\rho_0 = 0.418\times 10^{-9}\ \Omega\,\text{cm}\).  Compute the function for **at least 100 points \(y\) in \([-1, 1]\)**, and **include at least 10 additional points** clustered within \(\pm 0.04\) of the dip centre \(y_0 = G/(2k_F)\) so that the narrow feature is adequately sampled.
- Output file: `/app/outputs/distribution_function.csv`
- Format: csv
- Contract: columns: `y` (float, \([-1,1]\)), `phi_norm` (float).  At least 100 rows in total, with at least 10 in the window \([y_0 - 0.04,\; y_0 + 0.04]\).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/resistivity.csv`
- `/app/outputs/distribution_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### resistivity.csv
- path: `/app/outputs/resistivity.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Temperature-dependent resistivity computed from the model.
- schema:
  - `type`: table
  - `required_columns`: `T`, `rho`
  - `units`:
    - `T`: K
    - `rho`: Ω cm

### distribution_function.csv
- path: `/app/outputs/distribution_function.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized nonequilibrium electron distribution function.
- schema:
  - `type`: table
  - `required_columns`: `y`, `phi_norm`
  - `units`:
    - `y`: none
    - `phi_norm`: none

Notes: The two artifacts are scored independently. The checker will compare the agent's reported values to paper‑reference values at selected points and against the required shape (a sharp dip near \(y_0\)). Relative deviation within tolerance earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "resistivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "rho"
        ],
        "units": {
          "T": "K",
          "rho": "Ω cm"
        }
      },
      "description": "Temperature-dependent resistivity computed from the model."
    },
    {
      "file": "distribution_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "y",
          "phi_norm"
        ],
        "units": {
          "y": "none",
          "phi_norm": "none"
        }
      },
      "description": "Normalized nonequilibrium electron distribution function."
    }
  ],
  "notes": "The two artifacts are scored independently. The checker will compare the agent's reported values to paper-reference values at selected points and against the required shape (a sharp dip near y0). Relative deviation within tolerance earns full credit."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s output file.

- **resistivity.csv**: The verifier reads your reported \(\rho(T)\) at several temperatures and compares them to confidential reference values obtained from the same model. The score is based on the closeness of your values to the reference, subject to a tolerance that accounts for numerical implementation differences. Full credit is earned when your results meet or exceed an accuracy threshold.  The verifier also checks that at least 20 uniform temperature points are provided.
- **distribution_function.csv**: The verifier checks that a dip appears near \(y_0 = G/(2k_F)\) and then compares your \(\phi_{norm}\) values at selected points around that region to reference values.  Meeting the required shape and quantitative agreement within tolerance earns full credit.  The verifier also checks that at least 100 points are present and that the dip region is sufficiently sampled.

The final reward is a weighted sum of the two scores. Reporting the paper’s numbers is not sufficient; you must compute them yourself by following the described method.