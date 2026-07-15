# Resistivity and electron distribution from analytic solution of the Boltzmann equation for a model metal with umklapp scattering

## Problem background
At low temperatures the electrical resistivity of polyvalent metals whose Fermi surface intersects the Brillouin‑zone boundary deviates from Matthiessen's rule. This task addresses the underlying physics by computing the electrical resistivity and the nonequilibrium electron distribution function from an approximate solution to the coupled electron‑phonon Boltzmann equations. The model represents a metal with a spherical Fermi surface, two Brillouin‑zone boundaries, and anisotropic umklapp electron‑phonon scattering, intended to capture the behaviour of materials like aluminium. The goal is to produce the temperature‑dependent resistivity and the distribution function as predicted by the analytic model, which demonstrate how umklapp processes dominate the deviations from classical scattering behaviour.

## Approach
We solve the steady‑state linearized Boltzmann equation for electrons scattering off phonons and impurities. The electron distribution is expanded in odd Legendre polynomials, converting the integral equation into a matrix equation. Umklapp processes are treated by expanding in powers of the phonon wave vector q relative to the Brillouin‑zone boundary, retaining lowest‑order terms while avoiding expansions that would invalidate the solution for rapidly varying distributions. The phonon spectrum is taken as a Debye model with a single Debye temperature; the electron‑ion interaction uses a 1‑OPW pseudopotential form factor. The electron‑impurity scattering is described by a relaxation time derived from a given impurity resistivity. One obtains an approximate analytic expression for the resistivity (via the first expansion coefficient a₁) and for the normalised distribution function as a function of the cosine of the angle between the electron wave vector and the electric field. The resulting formulas involve integrals over the phonon wave vector that must be evaluated numerically. The method separately includes contributions from normal scattering (which enters the diagonal term) and umklapp scattering (which couples different Legendre components) and accounts for phonon drag. The implementation therefore requires: (i) setting up the model parameters (Fermi wave number, effective mass, reciprocal‑lattice vector, Debye temperature, pseudopotential form factors), (ii) performing numerical quadrature over a two‑dimensional domain for each needed temperature and impurity condition to compute scattering rates and umklapp kernels, and (iii) assembling these into the resistivity and distribution function using the analytic formulas.

## Reproduction target
You must produce two quantitative outputs from the model:

1. **Temperature‑dependent resistivity** – Compute the electrical resistivity ρ(T) for a fixed impurity resistivity ρ₀ = 0.218×10⁻⁷ Ω cm at temperatures from 10 K to 300 K, using at least 20 evenly spaced points. The electron density n is obtained from the free‑electron Fermi wave number, and the resistivity is ρ = (m*/(n e²)) (1/a₁) where a₁ is the first Legendre coefficient from the solution.

2. **Nonequilibrium distribution function** – Compute the normalised distribution function F(y) = (X₁′ / −3A) φ(y) at a temperature of 10 K and impurity resistivity ρ₀ = 0.418×10⁻⁹ Ω cm. Evaluate it for at least 100 values of y in the interval [−1, 1], with dense coverage around y = G/(2k_F) ≈ 0.72 where a pronounced dip is expected.

## Assets

- NumPy: numpy
- SciPy: scipy
- Aluminum model parameters

## Workflow steps

### Step 1: Define aluminum model parameters
- Role: process
- Action: Gather and set all physical constants for aluminum required by the model: Fermi wave number k_F, effective mass m*, reciprocal-lattice vector magnitude G, Debye temperature Θ_D, impurity relaxation time τ_i derived from the given impurity resistivity ρ0, and pseudopotential form factors V(0) and V(G). Use standard free-electron values and the model geometry described in the paper.
- Evidence: none

### Step 2: Compute electron-phonon scattering rates and umklapp kernels
- Role: process
- Action: For the temperature and impurity conditions needed, numerically evaluate the normal scattering diagonal term X'_L and the umklapp scattering kernel functions that appear in the matrix equation, using a Debye model for the phonon spectrum (Θ_D = 428 K) and the 1-OPW pseudopotential matrix elements. Perform the required two-dimensional integrals over phonon wave vector q and angular variables with numerical quadrature. This produces the intermediate numerical inputs for the resistivity and distribution function computations.
- Evidence: `/app/outputs/scattering_terms.log`

### Step 3: Compute temperature-dependent resistivity
- Role: scored (load-bearing)
- Action: Using the precomputed scattering terms and the formula for 1/a₁ that includes impurity and phonon-drag contributions, compute the temperature-dependent part of the electrical resistivity at the impurity resistivity ρ0 = 0.218×10⁻⁷ Ω cm for temperatures from 10 K to 300 K. The electron density n = k_F³/(3π²) and resistivity ρ = (m*/(n e²)) (1/a₁). Output at least 20 evenly spaced temperature points.
- Output file: `/app/outputs/resistivity.csv`
- Format: csv
- Contract: columns: T (float, K), rho (float, Ω cm). At least 20 rows evenly spaced 10..300 K.
- Scoring: scored by hidden verifier

### Step 4: Compute nonequilibrium distribution function
- Role: scored (load-bearing)
- Action: Using the precomputed scattering terms, evaluate the normalized nonequilibrium electron distribution function F(y) = (X₁′ / −3A) φ(y) at T = 10 K and impurity resistivity ρ0 = 0.418×10⁻⁹ Ω cm. Compute the function for at least 100 points y in [-1,1], ensuring dense coverage around y = G/(2k_F) ≈ 0.72 where a dip occurs.
- Output file: `/app/outputs/distribution_function.csv`
- Format: csv
- Contract: columns: y (float, [-1,1]), phi_norm (float). At least 100 rows.
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

Notes: The two artifacts are scored independently. The checker will compare the agent's reported values to paper-reference values at selected points and against the required shape (e.g., a dip around y ≈ 0.72). Relative deviation within tolerance earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

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
  "notes": "The two artifacts are scored independently. The checker will compare the agent's reported values to paper-reference values at selected points and against the required shape (e.g., a dip around y ≈ 0.72). Relative deviation within tolerance earns full credit."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s output file.

- **resistivity.csv**: The verifier reads your reported ρ(T) at several temperatures and compares them to confidential reference values obtained from the same model. The score is based on the closeness of your values to the reference, subject to a tolerance that accounts for numerical implementation differences. Full credit is earned when your results meet or exceed an accuracy threshold.
- **distribution_function.csv**: The verifier checks that a dip appears near y ≈ 0.72 and then compares your φ_norm values at selected points around that region to reference values. Meeting the required shape and quantitative agreement within tolerance earns full credit.

The final reward is a weighted sum of the two scores. Reporting the paper’s numbers is not sufficient; you must compute them yourself by following the described method.
