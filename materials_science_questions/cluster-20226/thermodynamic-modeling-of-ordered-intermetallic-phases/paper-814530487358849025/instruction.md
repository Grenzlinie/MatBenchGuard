# Thermodynamic properties of phase-field models for grain boundary segregation

## Problem background
Grain boundary (GB) segregation dramatically changes the physical and chemical properties of GBs. Phase-field models provide a unified framework for the thermodynamics and kinetics of GB segregation. This work develops diffuse‑interface two‑phase models—Model I (equal composition condition) and Model II (equal diffusion potential condition)—and compares their thermodynamic properties with the classical two‑phase model. The key question is how GB energy depends on matrix composition in each model; computing these curves provides insight into the fundamental differences between the modelling choices.

## Approach
The system is treated as a mixture of a matrix phase and a GB phase, connected by an interpolation function that gives the GB phase fraction. Two thermodynamic conditions are considered: equal composition (Model I) and equal diffusion potential (Model II). The free energy of the matrix phase is described by a regular‑solution form valid for dilute alloys, while the GB phase is taken as an ideal solution. The equilibrium compositions are determined from the parallel‑tangent condition applied to the free energy curves. For Model I the effective potential Ω₁(φ) is computed, and the GB energy is obtained by numerical integration; for Model II the GB energy follows from an analytic expression, and the classical two‑phase model assumes a constant GB width. The computation uses the parameters σ_A = 1 J m⁻², 2ξ_A = 1 nm, β = 1.0×10⁻⁹ J m⁻³, ω_A = 1.0×10⁹ J m⁻³, and three values of the enrichment parameter α = 2, 3, 4. The workflow first solves for equilibrium compositions and constructs the effective potential, then evaluates the GB energy over a range of matrix compositions for each model.

## Reproduction target
Compute the GB energy σ (J m⁻²) as a function of the matrix composition u_m for Model I, Model II, and the classical two‑phase model at α = 2, 3, 4. Produce a CSV file named `gb_energy_data.csv` with columns alpha, model, u_m, sigma that covers a sufficiently dense set of u_m values to define the curves. The verifier will independently recompute σ at hidden u_m points and check structural properties (lower bound in Model I, monotonicity, and relative ordering between models) to assess correctness.

## Assets

- Python 3: https://www.python.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute equilibrium compositions and effective potential
- Role: process
- Action: From the free-energy functions (regular solution for matrix phase, ideal solution for GB phase) and given parameters, compute the equilibrium GB composition from a matrix composition using the parallel‑tangent condition, and compute the effective potential Ω₁(ϕ) as a function of ϕ for Model I, covering the range of u_m values to be used later.
- Evidence: `/app/outputs/equilibrium_data.npz`

### Step 2: Evaluate GB energy for all models
- Role: scored (load-bearing)
- Action: For each α in {2,3,4}, iterate over a wide range of matrix composition u_m. For each u_m, compute the GB energy σ for Model I (numerical integration of the effective potential; record NaN where integration is impossible), Model II (analytic formula), and the classical two‑phase model (analytic formula). Write all results to gb_energy_data.csv.
- Output file: `/app/outputs/gb_energy_data.csv`
- Format: csv
- Contract: CSV with columns: alpha (integer), model (string: 'modelI','modelII','classical'), u_m (float, matrix composition), sigma (float, GB energy in J/m²). One row per combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gb_energy_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gb_energy_data.csv
- path: `/app/outputs/gb_energy_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Tabulated GB energy values for verification of the paper's main thermodynamic curves. The checker recomputes σ at hidden u_m points and checks structural properties (lower bound, monotonicity, ordering).
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `model`, `u_m`, `sigma`
  - `units`:
    - `sigma`: J/m²

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gb_energy_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "model",
          "u_m",
          "sigma"
        ],
        "units": {
          "sigma": "J/m²"
        }
      },
      "description": "Tabulated GB energy values for verification of the paper's main thermodynamic curves. The checker recomputes σ at hidden u_m points and checks structural properties (lower bound, monotonicity, ordering)."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier scores each workflow stage's artifact and combines them into a final reward. The main load‑bearing artifact `gb_energy_data.csv` is validated by recomputing the GB energy at hidden u_m values using the same free‑energy formulas and equilibrium conditions, and by verifying that the data respect required structural trends (such as a positive lower bound and monotonic decrease for Model I, and the relative ordering between models). The reward is proportional to how well the submitted curves agree with the reference, with the majority of weight on the `gb_energy_data.csv` artifact. Reporting the paper's numbers is not sufficient; the verifier independently checks the computed results.
