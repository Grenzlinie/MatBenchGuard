# Reproduction of fracture parameters for two parallel dielectric cracks in functionally graded piezoelectric materials

## Problem background
Functionally graded piezoelectric materials (FGPMs) combine the property gradients of functionally graded materials with the electromechanical coupling of piezoelectrics, offering improved performance and reliability in sensors, actuators and transducers. However, piezoceramics are brittle and susceptible to cracking; multiple interacting cracks that develop during manufacturing or service can critically degrade the structural integrity and electromechanical response. Analyzing the fracture behavior of parallel cracks under combined mechanical and electrical loading, while accounting for the dielectric medium (e.g. air) that fills the cracks and the deformation‑induced electric boundary conditions, is essential for safe design. This task addresses the problem of two parallel cracks in an infinite transversely isotropic FGPM with an exponential material gradient perpendicular to the crack surfaces. The objective is to quantify, through numerical computation, the effect of material gradient, crack geometry (length ratio, vertical and horizontal separation) and dielectric permittivity on fracture parameters: mode I and mode II stress intensity factors, electric displacement intensity factor, and crack opening displacement (COD) intensity factor.

## Approach
The method employs a continuous dislocation model and Fourier transform techniques. The cracked FGPM is described by the coupled electroelastic governing equations with exponentially graded material constants. By applying Fourier transforms, the governing equations are reduced to a sixth-order characteristic polynomial whose roots determine the electromechanical field in the transform domain. Each crack is represented as a distribution of generalized dislocations (displacement and electric potential jumps). The singular integral equations for two interacting cracks are derived by enforcing traction‑free and dielectric electric boundary conditions along the crack surfaces; the dielectric model couples the electric displacement to the crack opening and potential jumps via the permittivity of the filling medium. The kernel functions of these integral equations are expressed as Fourier integrals of auxiliary functions and their high‑wavenumber asymptotic behavior is extracted to regularize the singular parts.

The system is solved by expanding the dislocation density functions in Chebyshev polynomials of the first kind (with square‑root singularity weight) and satisfying the integral equations at Gauss–Chebyshev collocation points. This discretization converts the coupled singular integral equations into a linear algebraic system for the unknown Chebyshev coefficients. Once solved, the coefficients directly yield the stress and electric displacement intensity factors, and the COD intensity factor at each crack tip.

To normalize the results, single‑crack reference intensity factors are first computed for an isolated crack under the same far‑field loads and material gradient, using the same Chebyshev discretization. Then parametric sweeps are conducted by varying the crack geometry, material gradient parameter, and dielectric permittivity, each time assembling and solving the two‑crack linear system. The computed fracture parameters are normalized by the corresponding single‑crack values and written to a CSV file.

## Reproduction target
Produce a single CSV file, results.csv, containing normalized intensity factors for four parametric studies that correspond to the paper's headline results:

(1) Crack length ratio a_I/a_II for center‑aligned cracks (X = 0, a_II fixed at 1 mm, cracks at vertical distances h_I = -h_II = 0.5 a_II) with material gradient α·a_II = 0, 0.4, 1.0. Compute normalized mode I (k_I) and mode II (k_II) stress intensity factors at the right crack tips.

(2) Vertical separation h/a for equal‑length center‑aligned cracks (a_I = a_II = a) with material gradient α·a = 0, 0.4, 1.0. Compute normalized electric displacement intensity factor (k_D) and mode II (k_II) at the right crack tips.

(3) Horizontal offset X/a for equal‑length cracks with vertical separation h = a (a = 1 mm) and material gradient α·a = 0, 1.0. Compute normalized mode I (k_I) at the left and right tips of crack I.

(4) Effect of dielectric permittivity: fixed crack lengths a_I = 2 mm, a_II = 1 mm, vertical separation h = a_II, material gradient α·a_II = 0.8. Vary the horizontal offset X/a_II and the dielectric permittivity κ to sample the transition from permeable (κ → ∞) to impermeable (κ → 0) limits (use κ = κ0 (air) and large/small finite values of κ). Compute normalized electric displacement intensity factor (K_D) and COD intensity factor (K_COD) at the right tip of crack I.

For every parameter combination and crack tip, the CSV row must include: a case identifier, the swept parameter name and value, the material gradient product, the crack model (dielectric, permeable, or impermeable), which crack (I or II) and which tip (left or right), and the normalized values K_I_norm, K_II_norm, K_D_norm, K_COD_norm (set to NaN when a quantity is not computed for that sweep). All normalization uses single‑crack references computed for the appropriate crack length.

## Assets

- PZT-4 piezoelectric material constants
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define problem parameters and material constants
- Role: process
- Action: Set up the PZT-4 base material constants (c^0_ij, e^0_ij, ε^0_ij) from the known standard values. Define the exponential material gradient α, crack lengths a_I and a_II, vertical separation h, horizontal offset X (where applicable), the dielectric permittivity of the crack-filling medium κ (default air κ0=8.85×10^{-12} F/m), the applied far-field tensile stress σ^0_yy = 20 MPa, electric displacement D^0_y = 1×10^{-3} C/m², and the truncation order N for Chebyshev polynomials (e.g., N=20).
- Evidence: none

### Step 2: Compute auxiliary functions and kernel quantities
- Role: process
- Action: Implement the mathematical derivations from the paper: compute the dimensionless β_i coefficients; for each required Fourier variable s, compute the coefficients X_i(s) of the characteristic sixth-order polynomial, solve for the six roots λ_j(s) (three with positive real part, three with negative), compute the ratios a_j, b_j and the functions f_i, Δ(s), g_i(s). Evaluate the kernel integrand functions h_{ij}(s,0) and h^±_{ij}(s,y_k) and extract their high-|s| asymptotic constants h^0_{ij}.
- Evidence: none

### Step 3: Compute single-crack reference intensity factors
- Role: process
- Action: Solve the isolated single-crack problem for a crack of length a in the same exponentially graded PZT-4 material under identical far-field loads to obtain the reference mode I stress intensity factor K_I^S, electric displacement intensity factor K_D^S, and crack opening displacement intensity factor K_COD^S. This requires solving the related singular integral equation for a single crack using the same Chebyshev discretization.
- Evidence: none

### Step 4: Parametric study of normalized fracture parameters
- Role: scored (load-bearing)
- Action: Using the two-crack solver implemented from the kernel functions and the single-crack references, run the following four parameter sweeps:
  (1) crack length ratio a_I/a_II for center-aligned cracks (X=0, a_II=1 mm, h_I=-h_II=0.5 a_II) with material gradient α a_II = 0, 0.4, 1.0; compute normalized k_I and k_II at right tips.
  (2) vertical separation h/a for equal-length center-aligned cracks (a_I=a_II=a, α a = 0, 0.4, 1.0); compute normalized k_D and k_II at right tips.
  (3) horizontal offset X/a for equal-length cracks with h=a, a = 1 mm, material gradient α a = 0, 1.0; compute normalized k_I at left and right tips of crack I.
  (4) effect of dielectric permittivity: fix a_I=2 mm, a_II=1 mm, h=a_II, α a_II=0.8; vary horizontal offset X/a_II and dielectric permittivity κ to transition from permeable to impermeable limits (use κ=κ0 and large/small finite values); compute normalized K_D and K_COD at the right tip of crack I.
For every configuration, write one row to results.csv with columns: case_id, parameter_name, parameter_value, material_gradient, crack_model, crack, tip, K_I_norm, K_II_norm, K_D_norm, K_COD_norm.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: case_id (string), parameter_name (string), parameter_value (float), material_gradient (float), crack_model (string), crack (string, 'I' or 'II'), tip (string, 'left' or 'right'), K_I_norm (float), K_II_norm (float), K_D_norm (float), K_COD_norm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized stress and electric displacement intensity factors for interacting parallel cracks, compared to hidden gold values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `case_id`, `parameter_name`, `parameter_value`, `material_gradient`, `crack_model`, `crack`, `tip`, `K_I_norm`, `K_II_norm`, `K_D_norm`, `K_COD_norm`
  - `units`:
    - `parameter_value`: dimensionless
    - `material_gradient`: 1/mm or dimensionless
    - `K_I_norm`: dimensionless
    - `K_II_norm`: dimensionless
    - `K_D_norm`: dimensionless
    - `K_COD_norm`: dimensionless

Notes: The single-crack reference values are computed for the same crack length as appropriate for each normalization. The CSV includes all data points required to reproduce the paper's Figures 2–4 and 8–9.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case_id",
          "parameter_name",
          "parameter_value",
          "material_gradient",
          "crack_model",
          "crack",
          "tip",
          "K_I_norm",
          "K_II_norm",
          "K_D_norm",
          "K_COD_norm"
        ],
        "units": {
          "parameter_value": "dimensionless",
          "material_gradient": "1/mm or dimensionless",
          "K_I_norm": "dimensionless",
          "K_II_norm": "dimensionless",
          "K_D_norm": "dimensionless",
          "K_COD_norm": "dimensionless"
        }
      },
      "description": "Normalized stress and electric displacement intensity factors for interacting parallel cracks, compared to hidden gold values from the paper."
    }
  ],
  "notes": "The single-crack reference values are computed for the same crack length as appropriate for each normalization. The CSV includes all data points required to reproduce the paper's Figures 2–4 and 8–9."
}
```

## How you are scored
A hidden verifier reads your results.csv. For each parametric sweep (identified by the case_id column), it compares your reported normalized intensity factors to a hidden set of reference values derived from the paper's reported results. The comparison is made pointwise using a predefined relative tolerance. The score for a sweep is the fraction of its data points whose values fall within tolerance. Your overall reward is the average score over the four sweeps. You are not told the reference values or the tolerance; your job is to correctly implement the analytical/numerical procedure so that your computed numbers are physically accurate and within the expected numerical accuracy. The verifier does not require exact replication of any figure or table—only that your normalized fracture parameters agree with the hidden gold within the allowed tolerance.
