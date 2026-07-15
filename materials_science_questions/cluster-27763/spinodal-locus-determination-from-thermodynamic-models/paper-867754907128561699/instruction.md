# Two-Phase Fluid Model with Korteweg Stresses: Validation and Spinodal Decomposition

## Problem background
This task investigates a two-phase single-species fluid model in which interfacial tension is modelled as a volumetric (Korteweg) stress derived from a van der Waals–Cahn–Hilliard free energy. The model captures the spontaneous emergence and evolution of liquid-vapour interfaces and allows the study of phase separation without prescribing interface locations. Simulating the model at a fixed temperature permits quantitative tests of thermodynamic coexistence, surface tension, and the coarsening dynamics of phase-separated domains. The goal is to numerically reproduce the three central quantitative validations that establish the model's predictive ability: equilibrium densities of the coexisting phases at a given reduced temperature, the linear relationship between pressure difference and curvature (Laplace's law), and the late-stage domain growth exponent during spinodal decomposition.

## Approach
Implement the two-phase fluid model on a two-dimensional Cartesian grid. The governing equations are the isothermal compressible Navier–Stokes equations augmented with Korteweg interfacial stresses: the stress tensor includes a van der Waals equation of state (which provides mechanical instability and phase separation) together with density-gradient terms that produce surface tension. The numerical method is an explicit two-step MacCormack predictor-corrector scheme. First, simulate a flat liquid–gas interface at a prescribed reduced temperature (θ′=0.85) and fixed Reynolds and Weber numbers to obtain the equilibrium density profile and compute the surface tension coefficient α from the squared density gradient across the interface. Extract the bulk liquid and gas densities from this profile. Next, simulate equilibrium liquid drops of several radii suspended in gas using the same parameters and the previously found α; for each drop measure the pressure difference between the interior and exterior. Verify that the pressure difference is proportional to α/radius (Laplace's law). Finally, simulate isothermal spinodal decomposition on a larger grid: initialise a uniform near-critical density field with small random perturbations, quench the temperature to θ′=0.85, and evolve until late-stage coarsening. From the density snapshots, compute the circularly-averaged two-point correlation function and determine the average domain size D(t) as its first zero crossing. Fit a power law D ∝ tⁿ to the late-stage domain sizes (those between 20 and 128 grid cells) and report the exponent n.

## Reproduction target
Produce the following four scored artifacts:
1. **equilibrium_densities.csv** – the liquid and gas densities obtained from the flat interface simulation at reduced temperature θ′=0.85.
2. **laplace_verification.csv** – a table of drop radii and the corresponding inside/outside pressures, together with the surface tension coefficient, from drops of several radii (e.g., 8, 16, 32, 64 grid cells) simulated with the model parameters Re=2.0, We=1.0. The data should be sufficient to assess the linear relationship Δp ∝ α/R.
3. **domain_growth.csv** – the average domain size (in grid cells) at a sequence of times (including t=25, 50, 250, 500) extracted from the spinodal decomposition run after a quench to θ′=0.85.
4. **growth_exponent.txt** – a single floating-point number: the exponent n from a power-law fit D = A tⁿ performed on the domain sizes that lie between 20 and 128 grid cells.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Simulate flat interface and compute surface tension
- Role: process
- Action: Implement the two-phase fluid model with van der Waals equation of state and Korteweg interfacial stresses using a MacCormack predictor-corrector numerical scheme on a 64×64 grid. Set Reynolds number 2.0, Weber number 1.0, and reduced temperature θ′=0.85. Initialize a planar liquid–gas interface and run until the density profile reaches equilibrium. Save the final equilibrium density profile as flat_density_profile.npy. Compute the surface tension coefficient α using the formula α = λ ∫ (dρ/dy)² dy from the density profile, and write it to surface_tension_coefficient.csv.
- Evidence: `/app/outputs/flat_density_profile.npy, surface_tension_coefficient.csv`

### Step 2: Extract equilibrium liquid and gas densities
- Role: scored
- Action: From the flat_density_profile.npy, identify the liquid and gas phase densities (e.g., average density in the two bulk regions). Write a single row to equilibrium_densities.csv with columns: reduced_temperature, liquid_density, gas_density.
- Output file: `/app/outputs/equilibrium_densities.csv`
- Format: csv
- Contract: CSV with columns: reduced_temperature, liquid_density, gas_density. One row for θ′=0.85.
- Scoring: scored by hidden verifier

### Step 3: Verify Laplace's law
- Role: scored (load-bearing)
- Action: Using the surface_tension_coefficient.csv value, simulate equilibrium drops of several radii (e.g., 8, 16, 32, 64 grid cells) on a 256×256 grid with Re=2.0, We=1.0. Measure inside and outside pressures, compute Δp = inside - outside, and α/R. Write results to laplace_verification.csv with columns: drop_radius, inside_pressure, outside_pressure, surface_tension_coefficient.
- Output file: `/app/outputs/laplace_verification.csv`
- Format: csv
- Contract: CSV with columns: drop_radius, inside_pressure, outside_pressure, surface_tension_coefficient. One row per drop.
- Scoring: scored by hidden verifier

### Step 4: Run spinodal decomposition simulation
- Role: process
- Action: Initialize a 512×512 grid with average density 1.06344ρc plus random noise of amplitude 0.2ρc (fixed random seed). Quench to θ′=0.85. Run isothermal simulation with periodic boundaries for at least 500 dimensionless time units. Save density fields at times 25, 50, 250, 500 as density_t0025.npy, density_t0050.npy, density_t0250.npy, density_t0500.npy.
- Evidence: `/app/outputs/density_t0025.npy, density_t0050.npy, density_t0250.npy, density_t0500.npy`

### Step 5: Compute domain sizes from spinodal snapshots
- Role: scored (load-bearing)
- Action: For each snapshot, compute the circularly-averaged two-point correlation function, find the first zero crossing as average domain size D(t) in grid cells. Write domain_growth.csv with columns: time, domain_size. Include times 25, 50, 250, 500 and any additional saved times.
- Output file: `/app/outputs/domain_growth.csv`
- Format: csv
- Contract: CSV with columns: time, domain_size. Domain size in grid cells.
- Scoring: scored by hidden verifier

### Step 6: Fit power law and extract exponent
- Role: scored
- Action: From domain_growth.csv, select points where domain_size between 20 and 128 grid cells. Fit D = A t^n, output the exponent n as a single floating-point number to growth_exponent.txt.
- Output file: `/app/outputs/growth_exponent.txt`
- Format: txt
- Contract: A single floating-point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_densities.csv`
- `/app/outputs/laplace_verification.csv`
- `/app/outputs/domain_growth.csv`
- `/app/outputs/growth_exponent.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_densities.csv
- path: `/app/outputs/equilibrium_densities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium co-existing densities at reduced temperature 0.85.
- schema:
  - `type`: table
  - `required_columns`: `reduced_temperature`, `liquid_density`, `gas_density`

### laplace_verification.csv
- path: `/app/outputs/laplace_verification.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Pressure difference vs α/R for drops of various radii.
- schema:
  - `type`: table
  - `required_columns`: `drop_radius`, `inside_pressure`, `outside_pressure`, `surface_tension_coefficient`

### domain_growth.csv
- path: `/app/outputs/domain_growth.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Domain size over time from spinodal snapshots.
- schema:
  - `type`: table
  - `required_columns`: `time`, `domain_size`

### growth_exponent.txt
- path: `/app/outputs/growth_exponent.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Fitted growth exponent n from power law.
- schema:
  - `type`: text

Notes: All scored artifacts are re-derived by the checker against hidden gold values from the paper. No gold values or tolerances are revealed. The checker recomputes metrics from raw artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_densities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reduced_temperature",
          "liquid_density",
          "gas_density"
        ]
      },
      "description": "Equilibrium co-existing densities at reduced temperature 0.85."
    },
    {
      "file": "laplace_verification.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "drop_radius",
          "inside_pressure",
          "outside_pressure",
          "surface_tension_coefficient"
        ]
      },
      "description": "Pressure difference vs α/R for drops of various radii."
    },
    {
      "file": "domain_growth.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "domain_size"
        ]
      },
      "description": "Domain size over time from spinodal snapshots."
    },
    {
      "file": "growth_exponent.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text"
      },
      "description": "Fitted growth exponent n from power law."
    }
  ],
  "notes": "All scored artifacts are re-derived by the checker against hidden gold values from the paper. No gold values or tolerances are revealed. The checker recomputes metrics from raw artifacts."
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently processes your raw artifacts. The verifier re-derives the required quantities from your files, not from a single self-reported number. For equilibrium densities, it checks that the liquid and gas densities are consistent with the expected thermodynamic coexistence at the given temperature. For Laplace verification, it recomputes the pressure–curvature relationship from your tabulated drop data and evaluates agreement with Laplace's law. For domain growth, it fits a power law to the reported domain sizes and compares the resulting exponent against a hidden reference. The final growth exponent file is also compared directly. Each scored artifact carries a fractional weight; the reward is the weighted sum of stage scores. Reporting the expected final values without correctly generating the underlying simulation data will not yield a passing score.
