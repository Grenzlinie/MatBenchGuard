# Chemo-Mechanical Fracture Activation Diagram and Power-Law Scaling in Battery Particles

## Problem background
Chemo-mechanical fracture during charging and discharging of Li-ion battery cathode particles can degrade performance and shorten cell lifetime. A phase-field model has been used to study crack propagation from pre-existing surface flaws in a 2D circular disk under Li extraction. The key open questions are how the critical flaw size for crack propagation depends on charging rate, and whether distinct fracture regimes exist. This task investigates the activation behavior and power-law scaling of critical flaw size with charging rate, with the goal of computing the activation diagram and the associated scaling parameters.

## Approach
The coupled chemo-mechanical phase-field model (KKL model) captures diffusion, elasticity, and brittle fracture in a unified framework. The problem is cast as a 2D circular disk of LiMn2O4 with a pre-existing radial surface crack. Given the material properties (Young's modulus, Poisson ratio, fracture energy, diffusivity, maximum concentration, and misfit strain coefficient), the dimensionless groups (β, lG, R/lG) are computed. Under galvanostatic Li extraction (constant uniform surface flux), the coupled PDEs are solved numerically using a finite-element library. A grid of initial radial flaw lengths a0/lG and dimensionless C-rates Cr is scanned, and for each (a0,Cr) pair the simulation determines whether crack propagation occurs (activation). The resulting activation map is stored as a CSV. From the activation boundary (minimum a0 that activates for each Cr), a power-law a0,min/lG = A (β Cr)^p is fitted in the intermediate regime. The fitted exponent and prefactor are reported, together with the range used for the fit and a note on any constant minimum flaw size observed for very small flaws (regime III). The workflow also implicitly verifies the three regimes: (I) large flaws not activated at moderate Cr, (II) power-law scaling, and (III) a very small flaw size where activation requires extremely high Cr.

## Reproduction target
Produce two scored artifacts:
1. `activation_diagram.csv`: activation map for a 2D circular particle with R/lG = 4.2×10^4. Columns: a0_over_lG (dimensionless initial flaw size), Cr (dimensionless C-rate), activated (0 or 1).
2. `power_law_fit.json`: fit parameters from the activation boundary in the intermediate regime (roughly a0/lG 500–5000). Keys: A (prefactor), exponent (fitted exponent p), R_squared, fitting_range_min_a0_over_lG, fitting_range_max_a0_over_lG, observed_R3_constant_a0min (float or null).
The checker will recompute the activation boundary from the CSV, perform the power-law fit, and verify the existence of the three fracture regimes.

## Assets

- Open-source finite-element library (FEniCS or deal.II): https://fenicsproject.org/
- PETSc: https://petsc.org/

## Workflow steps

### Step 1: Parameter setup
- Role: process
- Action: From LiMn2O4 material properties (E=2e11 Pa, ν=0.3, Gc=100 N/m, D0=2.2e-13 m²/s, cmax=2.37e4 mol/m³, ε0=1.09e-6 m³/mol) compute the maximum misfit strain β=cmax ε0 = 0.025, Griffith length lG=Gc/E=5e-4 μm, and set particle radius R=21 μm (so R/lG=4.2e4). Define the scan grid of initial crack lengths a0/lG (from ~200 to ~10^4) and dimensionless C-rates Cr (≈1 to ≈100).
- Evidence: none

### Step 2: 2D galvanostatic simulations
- Role: scored (load-bearing)
- Action: Implement the coupled chemo-mechanical phase-field fracture model (KKL model) for a 2D circular disk with a preexisting radial surface crack using a finite-element library. For each (a0, Cr) pair from the scan grid, run the simulation under galvanostatic Li extraction (uniform flux) and determine whether the crack propagates (activated=1) or not (activated=0). Record results in activation_diagram.csv.
- Output file: `/app/outputs/activation_diagram.csv`
- Format: csv
- Contract: CSV columns: a0_over_lG (float), Cr (float), activated (int 0 or 1).
- Scoring: scored by hidden verifier

### Step 3: Power-law fit
- Role: scored
- Action: From activation_diagram.csv, extract the activation boundary (minimum a0 that activates for each Cr, or minimum Cr for each a0). Identify the intermediate regime (roughly a0/lG between ~500 and ~5000) and fit a power-law a0_min/lG = A (β Cr)^p. Record the fitted prefactor A, exponent p, R², the fitting range, and note the constant minimum flaw size a0_min in regime III if observed. Write results to power_law_fit.json.
- Output file: `/app/outputs/power_law_fit.json`
- Format: json
- Contract: JSON keys: A (float), exponent (float), R_squared (float), fitting_range_min_a0_over_lG (float), fitting_range_max_a0_over_lG (float), observed_R3_constant_a0min (float or null).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_diagram.csv`
- `/app/outputs/power_law_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_diagram.csv
- path: `/app/outputs/activation_diagram.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw activation map for a 2D circular particle with R/l_G=4.2e4. The checker recomputes the activation threshold boundary, fits the power-law, and verifies the three fracture regimes from this CSV.
- schema:
  - `type`: table
  - `required_columns`: `a0_over_lG`, `Cr`, `activated`
  - `units`:
    - `a0_over_lG`: dimensionless
    - `Cr`: dimensionless
    - `activated`: 0 or 1

### power_law_fit.json
- path: `/app/outputs/power_law_fit.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Agent-reported power-law fit parameters. The checker compares A and exponent to paper-reported gold values within defined tolerances.
- schema:
  - `type`: object
  - `required`: `A`, `exponent`, `R_squared`, `fitting_range_min_a0_over_lG`, `fitting_range_max_a0_over_lG`, `observed_R3_constant_a0min`
  - `properties`:
    - `A`:
      - `type`: number
      - `description`: Prefactor in power-law a0_min/lG = A (β Cr)^p
      - `unit`: dimensionless
    - `exponent`:
      - `type`: number
      - `description`: Fitted exponent p
      - `unit`: dimensionless
    - `R_squared`:
      - `type`: number
      - `description`: R-squared of the fit
      - `unit`: dimensionless
    - `fitting_range_min_a0_over_lG`:
      - `type`: number
      - `description`: Minimum a0/lG used in the fit
      - `unit`: dimensionless
    - `fitting_range_max_a0_over_lG`:
      - `type`: number
      - `description`: Maximum a0/lG used in the fit
      - `unit`: dimensionless
    - `observed_R3_constant_a0min`:
      - `type`: `number`, `null`
      - `description`: If regime III observed, the constant minimum flaw size a0_min/lG; otherwise null.
      - `unit`: dimensionless

Notes: The checker recomputes the activation boundary from the raw CSV, fits the power-law, and verifies that for a0/lG > 10^4 no activation occurs for Cr < 10 (Regime I) and for a0/lG < 500 no activation occurs for any simulated Cr (Regime III). The power_law_fit.json is cross-checked for consistency with the CSV-derived fit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_diagram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "a0_over_lG",
          "Cr",
          "activated"
        ],
        "units": {
          "a0_over_lG": "dimensionless",
          "Cr": "dimensionless",
          "activated": "0 or 1"
        }
      },
      "description": "Raw activation map for a 2D circular particle with R/l_G=4.2e4. The checker recomputes the activation threshold boundary, fits the power-law, and verifies the three fracture regimes from this CSV."
    },
    {
      "file": "power_law_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "A",
          "exponent",
          "R_squared",
          "fitting_range_min_a0_over_lG",
          "fitting_range_max_a0_over_lG",
          "observed_R3_constant_a0min"
        ],
        "properties": {
          "A": {
            "type": "number",
            "description": "Prefactor in power-law a0_min/lG = A (β Cr)^p",
            "unit": "dimensionless"
          },
          "exponent": {
            "type": "number",
            "description": "Fitted exponent p",
            "unit": "dimensionless"
          },
          "R_squared": {
            "type": "number",
            "description": "R-squared of the fit",
            "unit": "dimensionless"
          },
          "fitting_range_min_a0_over_lG": {
            "type": "number",
            "description": "Minimum a0/lG used in the fit",
            "unit": "dimensionless"
          },
          "fitting_range_max_a0_over_lG": {
            "type": "number",
            "description": "Maximum a0/lG used in the fit",
            "unit": "dimensionless"
          },
          "observed_R3_constant_a0min": {
            "type": [
              "number",
              "null"
            ],
            "description": "If regime III observed, the constant minimum flaw size a0_min/lG; otherwise null.",
            "unit": "dimensionless"
          }
        }
      },
      "description": "Agent-reported power-law fit parameters. The checker compares A and exponent to paper-reported gold values within defined tolerances."
    }
  ],
  "notes": "The checker recomputes the activation boundary from the raw CSV, fits the power-law, and verifies that for a0/lG > 10^4 no activation occurs for Cr < 10 (Regime I) and for a0/lG < 500 no activation occurs for any simulated Cr (Regime III). The power_law_fit.json is cross-checked for consistency with the CSV-derived fit."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact. For `activation_diagram.csv`, it recomputes the activation boundary (minimum a0/lG that activates for each Cr), fits the power-law a0,min/lG = A (β Cr)^p, and checks that the fitted exponent is within a tolerance of the expected scaling law, and that the prefactor A matches a hidden reference. It also verifies the three regimes: (i) for large flaws (a0/lG > 10^4) no activation for Cr < 10, (ii) for very small flaws (a0/lG < 500) no activation for any simulated Cr, and (iii) a consistent power-law behavior in the intermediate range. The `power_law_fit.json` is cross-checked for consistency with the CSV-derived fit. Each stage is weighted; the final reward is the weighted sum. Reporting correct numbers is not sufficient; the raw CSV must support the conclusions.
