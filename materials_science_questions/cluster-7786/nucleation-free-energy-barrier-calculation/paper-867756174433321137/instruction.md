# Boiling Heat Transfer Simulation with Hybrid Lattice Boltzmann Model

## Problem background
Boiling heat transfer is a highly effective heat transfer mode essential in many industrial thermal systems, from nuclear reactors to electronics cooling. Understanding bubble nucleation, growth, departure, and the boiling curve is critical for designing such systems. Numerical simulations can provide insight into the complex multiphase physics involved, but ensuring energy conservation across liquid‑vapor interfaces is a known challenge in hybrid thermal lattice Boltzmann models. This task addresses that challenge by implementing an improved hybrid lattice Boltzmann model that uses a finite‑volume discretization of the energy equation to maintain energy balance. The model is then applied to simulate the complete pool boiling process—from onset of nucleate boiling to film boiling—and to compute the boiling curve and the critical heat flux.

## Approach
The numerical method couples a pseudopotential lattice Boltzmann solver for multiphase flow with a finite‑difference solver for the energy equation. The flow solver uses a multi‑relaxation‑time (MRT) collision operator and a non‑ideal equation of state (Peng‑Robinson) to handle phase separation and surface tension. The energy equation accounts for convection, thermal diffusion, and latent heat during phase change. A finite‑volume discretization is applied to the diffusion term, which properly treats the conjugate heat transfer across interfaces with rapid thermal‑property changes. Time integration of the energy equation uses a fourth‑order Runge‑Kutta scheme with sub‑cycling for improved stability. To validate the model, two benchmark cases are simulated first: one‑dimensional heat conduction across a static liquid‑vapor interface and film evaporation on a heated wall. Once validated, the full pool boiling simulation is conducted on a 2D domain with a heating plate, periodic side boundaries, and nucleation sites treated via surface‑wettability drops. The final output is the boiling curve (dimensionless heat flux versus Jacob number) and the identified critical heat flux.

## Reproduction target
Implement the hybrid LBM model and run three sets of simulations:

1. **Static interface test**: heat conduction across a static liquid‑vapor interface; verify energy conservation by checking that heat fluxes on the hot and cold boundaries are consistent.
2. **Film evaporation test**: evaporation of a liquid film on a heated wall for at least three thermal‑conductivity ratios; compare the steady‑state mass flux to the analytical mass flux.
3. **Pool boiling simulation**: set up a 2D domain (400×600) with a heating plate and three nucleation sites whose interaction strengths vary linearly. Run the simulation for a range of Jacob numbers Ja from about 0.05 to 0.25 (at least six distinct values). For each Ja, run to a statistically stationary state, record the time‑averaged dimensionless heat flux, and output a boiling curve (Ja vs. q*). From that curve, identify the critical heat flux (the maximum q* and its corresponding Ja).

All required CSV outputs must be written to /app/outputs.

## Assets

- Python: python
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement hybrid LBM model
- Role: process
- Action: Implement the pseudopotential lattice Boltzmann method with MRT collision operator, Peng-Robinson equation of state, interaction forces, and the energy equation using the finite-volume discretization for the diffusion term and fourth-order Runge-Kutta time integration with sub-cycling.
- Evidence: none

### Step 2: Static interface heat conduction test
- Role: scored (load-bearing)
- Action: Set up a 1D heat conduction across a static liquid-vapor interface (domain 120x20, fixed saturation temperature). Run the simulation to steady state. Compute heat fluxes at hot and cold boundaries and output a CSV.
- Output file: `/app/outputs/static_interface_test_results.csv`
- Format: csv
- Contract: columns: boundary (string: 'hot' or 'cold'), heat_flux (float)
- Scoring: scored by hidden verifier

### Step 3: Film evaporation test
- Role: scored (load-bearing)
- Action: Simulate film evaporation on a heated wall (wall thickness 20, liquid film 50, heat flux density specified) for at least three thermal conductivity ratios. Compute steady mass flux and analytical mass flux (latent heat divided by heat flux) for each case. Output a CSV.
- Output file: `/app/outputs/film_evaporation_results.csv`
- Format: csv
- Contract: columns: conductivity_ratio (int), mass_flux (float), analytical_mass_flux (float)
- Scoring: scored by hidden verifier

### Step 4: Pool boiling simulation and boiling curve
- Role: scored (load-bearing)
- Action: Set up the 2D boiling domain (400x600) with a heating plate, nucleation sites treated via surface-wettability drops, and periodic side boundaries. Run the full hybrid LB simulation for a range of Jacob numbers Ja from approximately 0.05 to 0.25 (at least six distinct values). For each Ja, run to a statistically stationary state and record the time-averaged dimensionless heat flux q* on the bottom wall. Output a CSV with columns Ja and q_star.
- Output file: `/app/outputs/boiling_curve.csv`
- Format: csv
- Contract: columns: Ja (float), q_star (float)
- Scoring: scored by hidden verifier

### Step 5: Identify critical heat flux
- Role: scored
- Action: From the boiling_curve.csv, locate the maximum q_star and its corresponding Ja. Output a CSV with the identified CHF point.
- Output file: `/app/outputs/critical_heat_flux.csv`
- Format: csv
- Contract: columns: Ja_CHF (float), q_star_CHF (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/static_interface_test_results.csv`
- `/app/outputs/film_evaporation_results.csv`
- `/app/outputs/boiling_curve.csv`
- `/app/outputs/critical_heat_flux.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### static_interface_test_results.csv
- path: `/app/outputs/static_interface_test_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV with heat fluxes at the hot and cold boundaries. The relative difference between the two fluxes must be below a hidden threshold (energy conservation check).
- schema:
  - `type`: table
  - `required_columns`: `boundary`, `heat_flux`
  - `units`:
    - `boundary`: categorical
    - `heat_flux`: dimensionless

### film_evaporation_results.csv
- path: `/app/outputs/film_evaporation_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV with simulated mass flux and analytical mass flux for each conductivity ratio. The percent error between mass_flux and analytical_mass_flux for each ratio must be below a hidden threshold.
- schema:
  - `type`: table
  - `required_columns`: `conductivity_ratio`, `mass_flux`, `analytical_mass_flux`
  - `units`:
    - `conductivity_ratio`: dimensionless
    - `mass_flux`: dimensionless
    - `analytical_mass_flux`: dimensionless

### boiling_curve.csv
- path: `/app/outputs/boiling_curve.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV with at least six (Ja, q_star) data points. The curve must exhibit a monotonic increase to a peak (CHF) followed by a decrease. The peak location (Ja, q_star) will be compared to a hidden reference within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Ja`, `q_star`
  - `units`:
    - `Ja`: dimensionless
    - `q_star`: dimensionless

### critical_heat_flux.csv
- path: `/app/outputs/critical_heat_flux.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV with the identified CHF point (Ja_CHF, q_star_CHF). The values must match the peak found in boiling_curve.csv and be within tolerance of the hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `Ja_CHF`, `q_star_CHF`
  - `units`:
    - `Ja_CHF`: dimensionless
    - `q_star_CHF`: dimensionless

Notes: All outputs are required. The static interface test and film evaporation test validate the energy conservation of the implemented model. The boiling curve and CHF point constitute the main reproduction target. The verifier will apply tolerances appropriate for re-run variability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "static_interface_test_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "boundary",
          "heat_flux"
        ],
        "units": {
          "boundary": "categorical",
          "heat_flux": "dimensionless"
        }
      },
      "description": "CSV with heat fluxes at the hot and cold boundaries. The relative difference between the two fluxes must be below a hidden threshold (energy conservation check)."
    },
    {
      "file": "film_evaporation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "conductivity_ratio",
          "mass_flux",
          "analytical_mass_flux"
        ],
        "units": {
          "conductivity_ratio": "dimensionless",
          "mass_flux": "dimensionless",
          "analytical_mass_flux": "dimensionless"
        }
      },
      "description": "CSV with simulated mass flux and analytical mass flux for each conductivity ratio. The percent error between mass_flux and analytical_mass_flux for each ratio must be below a hidden threshold."
    },
    {
      "file": "boiling_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ja",
          "q_star"
        ],
        "units": {
          "Ja": "dimensionless",
          "q_star": "dimensionless"
        }
      },
      "description": "CSV with at least six (Ja, q_star) data points. The curve must exhibit a monotonic increase to a peak (CHF) followed by a decrease. The peak location (Ja, q_star) will be compared to a hidden reference within tolerance."
    },
    {
      "file": "critical_heat_flux.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Ja_CHF",
          "q_star_CHF"
        ],
        "units": {
          "Ja_CHF": "dimensionless",
          "q_star_CHF": "dimensionless"
        }
      },
      "description": "CSV with the identified CHF point (Ja_CHF, q_star_CHF). The values must match the peak found in boiling_curve.csv and be within tolerance of the hidden reference."
    }
  ],
  "notes": "All outputs are required. The static interface test and film evaporation test validate the energy conservation of the implemented model. The boiling curve and CHF point constitute the main reproduction target. The verifier will apply tolerances appropriate for re-run variability."
}
```

## How you are scored
A hidden verifier will independently evaluate each workflow stage's output artifact. It will check the static interface test for energy conservation (relative difference between boundary heat fluxes), the film evaporation test for agreement with analytical mass flux, the boiling curve for structural properties (sufficient data points, monotonic increase to a peak then decrease), and the critical heat flux against a hidden reference. Tolerances account for normal run‑to‑run variability. Each scored stage carries a weight; the final reward is the combined score. Simply reporting numbers without running the model will not satisfy the verifier—the artifacts must be produced by executing the described workflow.
