# Phase-field grain boundary segregation: GB energy vs composition for Models I and II

## Problem background
Grain boundary (GB) segregation of solute atoms can dramatically alter material properties, including GB energy and thermodynamic stability. Phase-field models have been developed to capture the thermodynamic and kinetic effects of GB segregation. This study investigates two phase-field models that differ in the thermodynamic closure condition at a point in the GB region: Model I (equal composition) and Model II (equal diffusion potential). Both are diffuse-interface versions of the classical two-phase model of GB segregation. The key question is how the GB energy depends on the matrix composition for each model. The problem is to compute and compare these compositional dependencies for a set of prescribed physical parameters.

## Approach
The approach consists of implementing the free energy densities for the matrix (dilute regular solution with a linear interaction term and ideal mixing entropy) and the GB phase (ideal solution), using the given pure-solvent GB energy, GB width, temperature, molar volume, and the dimensionless parameter α that controls segregation strength. For each α value (2, 3, 4), the common equilibrium GB composition as a function of matrix composition is obtained via the parallel-tangent (equal diffusion potential) construction. Model I GB energy is computed by solving for the equilibrium concentration profile under the equal composition condition and numerically integrating the resulting effective double-well potential. Model II GB energy is computed analytically from the closed-form square-root relationship derived from the equal diffusion potential condition, using the same equilibrium compositions. The classical two-phase model GB energy serves as a reference, computed with a linear relation assuming constant GB width. All results are tabulated and compared across the three models.

## Reproduction target
Produce tabulated GB energy as a function of matrix composition for Model I, Model II, and the classical two-phase model, using α = 2, 3, 4. The parameters are: σₐ = 1 J/m², 2ξₐ = 1 nm, T = 1273 K, vₘ = 1.06 × 10⁻⁵ m³/mol, and βωₐ = 1.0. Also output the common equilibrium GB composition relation u_g^e(u_m^e) shared by all models, and provide selected analytic constants (gradient energy coefficient, pure-solvent GB energy, and a sample evaluation) for Model II. All outputs are written to CSV and JSON files under /app/outputs.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define physical parameters and free energy functions
- Role: process
- Action: Set the numerical values for pure-solvent GB energy σ_A=1 J/m², GB width 2ξ_A=1 nm, temperature T=1273 K, molar volume v_m=1.06e-5 m³/mol (so β = v_m/(RT) and ω_A = σ_A/(2ξ_A) with βω_A=1.0). Define the matrix free energy density f^m(u) as a dilute regular solution (linear regular solution term L^m plus ideal mixing entropy) and the GB free energy f^g(u) as an ideal solution. Use the α values 2, 3, 4 (α defined from free energy differences and L^m). These functions and parameters are the basis for all later computations.
- Evidence: none

### Step 2: Compute common equilibrium GB composition
- Role: scored
- Action: For each α=2,3,4, use the parallel-tangent condition (equal diffusion potential) to compute the equilibrium GB composition u_g^e as a function of the matrix composition u_m^e. Sample u_m^e from 0.001 to 0.15 with step 0.005, and also determine the upper bound (common tangent) compositions u_m^ct, u_g^ct for Model I. Write the results to /app/outputs/common_gb_composition.csv.
- Output file: `/app/outputs/common_gb_composition.csv`
- Format: csv
- Contract: CSV with columns: alpha (int), u_m_e (float), u_g_e (float). Rows for each α and u_m_e step, as well as the critical compositions for Model I.
- Scoring: scored by hidden verifier

### Step 3: Compute Model I GB energy
- Role: scored (load-bearing)
- Action: For each α=2,3,4, compute the GB energy σ for Model I (equal composition) as a function of u_m^e. For u_m^e increasing from 0.001 up to the upper bound u_m^ct, determine the equilibrium concentration profile u(φ) via the equal composition condition, then numerically integrate the effective double‑well potential Ω₁(φ) to obtain σ. Record the bound compositions u_m^ct and u_g^ct (same for all rows of that α) in the output. Write to /app/outputs/modelI_gb_energy.csv.
- Output file: `/app/outputs/modelI_gb_energy.csv`
- Format: csv
- Contract: CSV with columns: alpha (int), u_m_e (float), sigma (float, J/m²), u_m_ct (float, same per alpha), u_g_ct (float, same per alpha). For each α, rows for increasing u_m_e up to the bound.
- Scoring: scored by hidden verifier

### Step 4: Compute Model II GB energy
- Role: scored
- Action: For each α=2,3,4, compute the GB energy σ for Model II (equal diffusion potential) using the closed‑form expression σ = σ_A √(ω^e / ω_A). ω^e is derived from u_m^e and the common equilibrium GB composition u_g^e as ω^e = ω_A + (1/β) ln((1 - u_g^e)/(1 - u_m^e)) (essentially the parallel‑tangent construction). Use the same u_m^e grid as for Model II (from 0.001 up to the common tangent composition where σ→0). Write to /app/outputs/modelII_gb_energy.csv.
- Output file: `/app/outputs/modelII_gb_energy.csv`
- Format: csv
- Contract: CSV with columns: alpha (int), u_m_e (float), sigma (float, J/m²). Rows for u_m_e from 0.001 to the common tangent composition.
- Scoring: scored by hidden verifier

### Step 5: Compute classical two‑phase model GB energy
- Role: scored
- Action: For each α=2,3,4, compute the GB energy σ of the classical two‑phase model using σ = σ_A (ω^e / ω_A) with the same common equilibrium compositions as Model II. Use the same u_m_e grid. Write to /app/outputs/classical_two_phase_gb_energy.csv.
- Output file: `/app/outputs/classical_two_phase_gb_energy.csv`
- Format: csv
- Contract: CSV with columns: alpha (int), u_m_e (float), sigma (float, J/m²). Same grid as modelII.
- Scoring: scored by hidden verifier

### Step 6: Output analytic constants for Model II
- Role: scored
- Action: Compute the gradient energy coefficient ε from ε = (4/π) √(ξ_A σ_A), the pure‑solvent GB energy σ_A and half‑width ξ_A, and the parameter ω_A = σ_A/(2ξ_A). Evaluate the analytic GB energy for the condition u_m^e = 0.09, α = 3 using the closed‑form Model II expression. Also compute the ratios σ/σ_A (using the closed-form expression) and σ/(2ξ ω^e) (which should equal 1 for Model II). Write to /app/outputs/modelII_analytic_results.json.
- Output file: `/app/outputs/modelII_analytic_results.json`
- Format: json
- Contract: JSON object with keys: sigma_A (float, J/m²), xi_A (float, m), epsilon (float), omega_A (float, J/m³), sigma (float, J/m², at u_m^e=0.09, α=3), sigma_over_sigma_A (float), sigma_over_xi_omega (float, expected value 1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/common_gb_composition.csv`
- `/app/outputs/modelI_gb_energy.csv`
- `/app/outputs/modelII_gb_energy.csv`
- `/app/outputs/classical_two_phase_gb_energy.csv`
- `/app/outputs/modelII_analytic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### common_gb_composition.csv
- path: `/app/outputs/common_gb_composition.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium GB composition u_g^e vs matrix composition u_m^e from the parallel-tangent construction, for α=2,3,4. The agent must also include the critical compositions (u_m^ct, u_g^ct) for Model I in this file.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `u_m_e`, `u_g_e`
  - `units`:
    - `alpha`: dimensionless
    - `u_m_e`: mole fraction
    - `u_g_e`: mole fraction

### modelI_gb_energy.csv
- path: `/app/outputs/modelI_gb_energy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Model I GB energy σ vs matrix composition u_m^e, for α=2,3,4. The columns u_m_ct and u_g_ct give the upper bound compositions for each α.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `u_m_e`, `sigma`, `u_m_ct`, `u_g_ct`
  - `units`:
    - `alpha`: dimensionless
    - `u_m_e`: mole fraction
    - `sigma`: J/m²
    - `u_m_ct`: mole fraction
    - `u_g_ct`: mole fraction

### modelII_gb_energy.csv
- path: `/app/outputs/modelII_gb_energy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Model II GB energy σ vs matrix composition u_m^e, for α=2,3,4.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `u_m_e`, `sigma`
  - `units`:
    - `alpha`: dimensionless
    - `u_m_e`: mole fraction
    - `sigma`: J/m²

### classical_two_phase_gb_energy.csv
- path: `/app/outputs/classical_two_phase_gb_energy.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Classical two-phase model GB energy σ vs matrix composition u_m^e, for α=2,3,4.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `u_m_e`, `sigma`
  - `units`:
    - `alpha`: dimensionless
    - `u_m_e`: mole fraction
    - `sigma`: J/m²

### modelII_analytic_results.json
- path: `/app/outputs/modelII_analytic_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Analytic constants: σ_A, ξ_A (half-width), ε (gradient energy coefficient), ω_A, and Model II GB energy σ at u_m^e=0.09, α=3, plus the ratios σ/σ_A and σ/(2ξ ω^e).
- schema:
  - `type`: object
  - `required`: `sigma_A`, `xi_A`, `epsilon`, `omega_A`, `sigma`, `sigma_over_sigma_A`, `sigma_over_xi_omega`
  - `units`:
    - `sigma_A`: J/m²
    - `xi_A`: m
    - `epsilon`: dimensionless (or consistent units)
    - `omega_A`: J/m³
    - `sigma`: J/m²
    - `sigma_over_sigma_A`: dimensionless
    - `sigma_over_xi_omega`: dimensionless

Notes: All CSV files must be written with a header. The JSON file must contain the specified keys. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "common_gb_composition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "u_m_e",
          "u_g_e"
        ],
        "units": {
          "alpha": "dimensionless",
          "u_m_e": "mole fraction",
          "u_g_e": "mole fraction"
        }
      },
      "description": "Equilibrium GB composition u_g^e vs matrix composition u_m^e from the parallel-tangent construction, for α=2,3,4. The agent must also include the critical compositions (u_m^ct, u_g^ct) for Model I in this file."
    },
    {
      "file": "modelI_gb_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "u_m_e",
          "sigma",
          "u_m_ct",
          "u_g_ct"
        ],
        "units": {
          "alpha": "dimensionless",
          "u_m_e": "mole fraction",
          "sigma": "J/m²",
          "u_m_ct": "mole fraction",
          "u_g_ct": "mole fraction"
        }
      },
      "description": "Model I GB energy σ vs matrix composition u_m^e, for α=2,3,4. The columns u_m_ct and u_g_ct give the upper bound compositions for each α."
    },
    {
      "file": "modelII_gb_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "u_m_e",
          "sigma"
        ],
        "units": {
          "alpha": "dimensionless",
          "u_m_e": "mole fraction",
          "sigma": "J/m²"
        }
      },
      "description": "Model II GB energy σ vs matrix composition u_m^e, for α=2,3,4."
    },
    {
      "file": "classical_two_phase_gb_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "u_m_e",
          "sigma"
        ],
        "units": {
          "alpha": "dimensionless",
          "u_m_e": "mole fraction",
          "sigma": "J/m²"
        }
      },
      "description": "Classical two-phase model GB energy σ vs matrix composition u_m^e, for α=2,3,4."
    },
    {
      "file": "modelII_analytic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "sigma_A",
          "xi_A",
          "epsilon",
          "omega_A",
          "sigma",
          "sigma_over_sigma_A",
          "sigma_over_xi_omega"
        ],
        "units": {
          "sigma_A": "J/m²",
          "xi_A": "m",
          "epsilon": "dimensionless (or consistent units)",
          "omega_A": "J/m³",
          "sigma": "J/m²",
          "sigma_over_sigma_A": "dimensionless",
          "sigma_over_xi_omega": "dimensionless"
        }
      },
      "description": "Analytic constants: σ_A, ξ_A (half-width), ε (gradient energy coefficient), ω_A, and Model II GB energy σ at u_m^e=0.09, α=3, plus the ratios σ/σ_A and σ/(2ξ ω^e)."
    }
  ],
  "notes": "All CSV files must be written with a header. The JSON file must contain the specified keys. No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage's artifact. For each scored file, the verifier recomputes the quantities (e.g., GB compositions, GB energies) from the same public parameters and free energy functions, or checks structural properties such as positivity and bounds. The final reward is a weighted combination of the scores across all artifacts. Reporting the paper's numbers is not enough; you must execute the computation and produce the correct results, which the verifier will compare against its own hidden reference implementation.
