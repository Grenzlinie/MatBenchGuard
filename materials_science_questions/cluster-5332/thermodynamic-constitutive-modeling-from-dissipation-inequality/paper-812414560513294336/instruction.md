# Unconditionally Stable Staggered Thermoplasticity Simulation

## Problem background
Nonlinear coupled thermoplasticity at finite strains involves widely separated time scales.  Conventional staggered (operator-split) algorithms partition the problem into a mechanical phase (usually isothermal) followed by a heat conduction phase.  Although attractive computationally, this isothermal split is known to be only conditionally stable – a crucial limitation for strongly coupled problems.  The work presented here introduces an alternative `adiabatic split' in which the mechanical phase preserves the total entropy, followed by a heat conduction phase at fixed configuration.  The central claim is that this new split inherits an a priori energy estimate of the continuum problem and therefore yields an unconditionally stable staggered scheme.  The present task reproduces the numerical simulations of a thick‑walled thermoplastic cylinder to evaluate the performance and stability of both the adiabatic and the isothermal split under different loading conditions.

## Approach
Implement the J₂‑flow thermoplasticity model at finite strains with a logarithmic stored energy function, isotropic saturation hardening, and linear thermal softening (as summarised in Box 1 of the source material).  The material model includes both elastic and plastic contributions to the entropy.  Build two staggered time‑stepping schemes: (1) the adiabatic split – an isentropic mechanical phase followed by a heat conduction phase at fixed configuration, and (2) the conventional isothermal split – a mechanical phase at constant temperature followed by a heat conduction phase at fixed configuration.  Discretise the spatial domain with axisymmetric plane‑strain finite elements (enhanced‑strain formulation).  Use the material parameters from Table 1 of the source material and the boundary conditions shown in Fig. 1: a thick‑walled cylinder with inner radius 100 mm, outer radius 200 mm, insulated thermal boundaries, and an inner face displacement ramp that expands the cylinder until the inner radius reaches 3.1 times its initial value.  Perform simulations for two separate objectives: (a) a convergence study with the adiabatic split at two nominal strain rates (1e − 2 s⁻¹ and 1 s⁻¹), and (b) a strongly coupled comparison where the thermal expansion coefficient is artificially raised (α = 1.4 × 10⁻⁴ K⁻¹) at a strain rate of 1e − 2 s⁻¹ – for this case run both the adiabatic split and the isothermal split on the same time grid.  Record the temperature at the inner face during each simulation.

## Reproduction target
Produce two comma‑separated (CSV) files containing the temperature time series at the inner face of the cylinder.

- `thick_cylinder_convergence.csv`: For the two nominal strain rates (1e − 2 s⁻¹ and 1 s⁻¹), record every time step’s temperature (in Kelvin).  Columns: `strain_rate` (string), `step` (integer index), `temperature_inner_K` (float).
- `thick_cylinder_strong_coupling.csv`: For the enhanced coupling case (α = 1.4 × 10⁻⁴ K⁻¹, strain rate 1e − 2 s⁻¹), record the temperature obtained with the adiabatic split and with the isothermal split on the same time grid.  Columns: `time_s` (float), `T_adiabatic_K` (float), `T_isothermal_K` (float).
The final steady‑state temperatures and the qualitative behaviour of the curves (e.g., presence or absence of oscillations) constitute the target quantities; no explicit numeric targets are given.  The implemented code must be able to produce these files by running the prescribed simulations.

## Assets

- Open-source finite element library (e.g. FEniCS, deal.II) with Python interface: https://fenicsproject.org

## Workflow steps

### Step 1: Implement thermoplasticity model and adiabatic split
- Role: process
- Action: Implement the J2-flow plasticity model with logarithmic free energy, linear thermal softening, and the adiabatic (isentropic) split algorithm (mechanical phase + heat conduction phase) as given in the paper's Appendix. Use an axisymmetric plane-strain finite-element discretization with enhanced strain elements. The code must be able to simulate the expansion of a thick-walled cylinder under given strain rates and thermal boundary conditions.
- Evidence: `/app/outputs/implementation_summary.txt`

### Step 2: Run cylinder expansion for two strain rates (adiabatic split)
- Role: scored (load-bearing)
- Action: Using the implemented adiabatic split, simulate the expansion of a thick-walled cylinder with inner radius 100 mm, outer radius 200 mm, material properties from the paper's Table 1, plane-strain axisymmetric conditions, insulated thermal boundaries, and imposed inner displacement up to final radius 3.1·a₀. Run at nominal strain rates 1e-2 s⁻¹ and 1e0 s⁻¹. Record the temperature at the inner face at each time step.
- Output file: `/app/outputs/thick_cylinder_convergence.csv`
- Format: csv
- Contract: Columns: strain_rate (string, '1e-2' or '1e0'), step (integer, time step index), temperature_inner_K (float, temperature in Kelvin). All rows for a given strain_rate belong to one complete run.
- Scoring: scored by hidden verifier

### Step 3: Simulate strongly coupled case with adiabatic and isothermal splits
- Role: scored (load-bearing)
- Action: Run the same cylinder expansion but with an enhanced thermal expansion coefficient α = 1.4e-4 K⁻¹ and strain rate 1e-2 s⁻¹. Run two separate simulations: one using the adiabatic split and one using the conventional isothermal split (mechanical phase at constant temperature, thermal phase at fixed configuration). Record the temperature at the inner face at each time step for both splits, using the same time grid.
- Output file: `/app/outputs/thick_cylinder_strong_coupling.csv`
- Format: csv
- Contract: Columns: time_s (float, simulation time in seconds), T_adiabatic_K (float, temperature in Kelvin), T_isothermal_K (float, temperature in Kelvin). Each row corresponds to a time instant; both temperatures are recorded on the same temporal grid.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thick_cylinder_convergence.csv`
- `/app/outputs/thick_cylinder_strong_coupling.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thick_cylinder_convergence.csv
- path: `/app/outputs/thick_cylinder_convergence.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Temperature at the inner face of the thick-walled cylinder for two strain rates, each run's complete time history. The final time-step temperature is compared to a hidden reference value from the paper.
- schema:
  - `type`: table
  - `required_columns`: `strain_rate`, `step`, `temperature_inner_K`
  - `units`:
    - `temperature_inner_K`: Kelvin

### thick_cylinder_strong_coupling.csv
- path: `/app/outputs/thick_cylinder_strong_coupling.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature evolution at inner face for strongly coupled case, comparing adiabatic and isothermal splits. Checker verifies monotonic adiabatic curve and oscillatory isothermal curve.
- schema:
  - `type`: table
  - `required_columns`: `time_s`, `T_adiabatic_K`, `T_isothermal_K`
  - `units`:
    - `time_s`: seconds
    - `T_adiabatic_K`: Kelvin
    - `T_isothermal_K`: Kelvin

Notes: The checker extracts the final temperature from the first CSV for each strain rate and compares to a hidden digitised value from the paper's Fig. 2 (±5% tolerance). For the second CSV, it verifies that the adiabatic temperature is monotonic (no oscillation amplitude >1 K) while the isothermal temperature shows a standard deviation >3 K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thick_cylinder_convergence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain_rate",
          "step",
          "temperature_inner_K"
        ],
        "units": {
          "temperature_inner_K": "Kelvin"
        }
      },
      "description": "Temperature at the inner face of the thick-walled cylinder for two strain rates, each run's complete time history. The final time-step temperature is compared to a hidden reference value from the paper."
    },
    {
      "file": "thick_cylinder_strong_coupling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_s",
          "T_adiabatic_K",
          "T_isothermal_K"
        ],
        "units": {
          "time_s": "seconds",
          "T_adiabatic_K": "Kelvin",
          "T_isothermal_K": "Kelvin"
        }
      },
      "description": "Temperature evolution at inner face for strongly coupled case, comparing adiabatic and isothermal splits. Checker verifies monotonic adiabatic curve and oscillatory isothermal curve."
    }
  ],
  "notes": "The checker extracts the final temperature from the first CSV for each strain rate and compares to a hidden digitised value from the paper's Fig. 2 (±5% tolerance). For the second CSV, it verifies that the adiabatic temperature is monotonic (no oscillation amplitude >1 K) while the isothermal temperature shows a standard deviation >3 K."
}
```

## How you are scored
A hidden verifier will independently evaluate your submitted CSV files.  It does not merely check that the files exist; it extracts the relevant numerical quantities and structural features from the temperature curves.  For the convergence study it compares the final steady‑state temperature for each strain rate against hidden reference values derived from the original publication, applying a tolerance that accounts for legitimate discretisation and implementation differences.  For the strong coupling case it checks that the temperature curves exhibit the characteristic patterns expected for a stable algorithm (e.g., monotonicity) and for an unstable algorithm (e.g., presence of oscillations), using hidden amplitude and statistical thresholds.  The two scored artifacts carry unequal weights that sum to 1.0; the final reward is the weighted average of the per‑artifact scores.  No partial credit is given for approximating the correct answer without actually running the simulations; the verifier relies on the data you write to the specified output files.
