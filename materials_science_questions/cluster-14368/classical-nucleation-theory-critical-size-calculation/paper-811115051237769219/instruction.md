# Growth Rate and Critical Supersaturation of Elongated Nanostructures via Kinetic Monte Carlo

## Problem background
Elongated nanostructures, such as quantum wires or interconnecting lines, are grown from the gas phase onto a masked substrate where material can only deposit on the exposed stripe. The finite width of the stripe creates size-dependent behavior: the growth rate and thermal stability are expected to vary with the stripe width. This modeling task addresses the central question of how the width of an elongated nanostructure influences its growth rate and the critical vapor pressure required for growth versus etching. Using kinetic Monte Carlo simulations, you will compute the time-average growth rate as a function of stripe width at a fixed supersaturation, and determine the critical supersaturation (equilibrium vapor pressure relative to an infinite surface) as a function of width.

## Approach
The growth is modeled with a continuous-time kinetic Monte Carlo method under the solid-on-solid approximation on a simple cubic lattice. The simulation cell is 80 lattice sites long in the stripe direction (periodic boundary condition) and w sites wide (free boundaries). At each site, adsorption and desorption events compete. Adsorption is driven by the relative supersaturation σ∞ (with respect to an infinite surface), and the desorption rate of an atom depends on its number of first-nearest neighbors via the interaction energy ε = 0.23 eV at temperature T = 1000 K. The total event rate determines the time advancement. By running independent realizations for each stripe width, you obtain the height of the deposited film as a function of time. The average growth rate is extracted as the slope of the linear regime. To find the critical supersaturation for growth, the supersaturation is varied near the zero-growth point, and the net growth/etch rate is interpolated to zero.

## Reproduction target
Produce two scored comma-separated values (CSV) files under /app/outputs. First, growth_rates.csv must contain the time-average growth rate (dimensionless) for each specified stripe width w/a0 at a fixed relative supersaturation σ∞ = 0.6. The list of widths is: 6, 8, 10, 15, 20, 40, 160. Second, critical_supersaturation.csv must report the critical supersaturation σ_c (dimensionless) at which the net growth rate becomes zero for at least the widths w/a0 = 8 and 15. The growth rates are derived from averaging over at least 10 independent KMC simulations per width; the critical supersaturations are obtained by interpolating growth/etch rates from simulations spanning a range of σ∞. Both CSV files have columns: width (in units of a0) and either growth_rate or critical_supersaturation.

## Assets

- Python 3 with numpy/scipy: numpy scipy

## Workflow steps

### Step 1: Run KMC growth simulations at fixed supersaturation
- Role: process
- Action: Implement the continuous-time Monte Carlo model: adsorption/desorption probabilities based on first-nearest-neighbor interactions, solid-on-solid approximation, simple cubic lattice of size 80×w with periodic boundary along the long direction and free boundaries at edges. For stripe widths w/a0 = 6, 8, 10, 15, 20, 40, 160 at relative supersaturation σ∞=0.6, run at least 10 independent simulations and record the number of deposited layers vs. time.
- Evidence: `/app/outputs/growth_simulations.log`

### Step 2: Compute growth rates vs. width
- Role: scored
- Action: From the height-time trajectories obtained in step_01, compute the time-average growth rate as the slope of height vs. time for each stripe width. Write the results to growth_rates.csv.
- Output file: `/app/outputs/growth_rates.csv`
- Format: csv
- Contract: CSV with two columns: width (float, in units of a0) and growth_rate (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 3: Run KMC simulations for varying supersaturations
- Role: process
- Action: For selected stripe widths (at least w/a0 = 8 and 15), perform KMC simulations over a range of relative supersaturations σ∞ near the expected zero-growth point. For each condition, record the net growth or etching rate.
- Evidence: `/app/outputs/supersaturation_simulations.log`

### Step 4: Determine critical supersaturations
- Role: scored (load-bearing)
- Action: For each width, interpolate the growth/etch rates as a function of supersaturation to find the critical supersaturation σ_c at which the net growth rate is zero. Write the results to critical_supersaturation.csv.
- Output file: `/app/outputs/critical_supersaturation.csv`
- Format: csv
- Contract: CSV with two columns: width (float, in units of a0) and critical_supersaturation (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/growth_rates.csv`
- `/app/outputs/critical_supersaturation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### growth_rates.csv
- path: `/app/outputs/growth_rates.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time-average growth rate of the elongated nanostructure as a function of stripe width at a fixed relative supersaturation of 0.6. The checker compares the submitted values to the paper's reported values within a tolerance and verifies that the growth rate increases with width.
- schema:
  - `type`: table
  - `required_columns`: `width`, `growth_rate`
  - `units`:
    - `width`: a0
    - `growth_rate`: dimensionless

### critical_supersaturation.csv
- path: `/app/outputs/critical_supersaturation.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical relative supersaturation as a function of stripe width. The checker compares the submitted values to the paper's reported values within a tolerance and verifies that the critical supersaturation decreases with increasing width.
- schema:
  - `type`: table
  - `required_columns`: `width`, `critical_supersaturation`
  - `units`:
    - `width`: a0
    - `critical_supersaturation`: dimensionless

Notes: No hidden gold or tolerances revealed; all scoring is based on comparison to paper-reported values via hidden tests.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "growth_rates.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "width",
          "growth_rate"
        ],
        "units": {
          "width": "a0",
          "growth_rate": "dimensionless"
        }
      },
      "description": "Time-average growth rate of the elongated nanostructure as a function of stripe width at a fixed relative supersaturation of 0.6. The checker compares the submitted values to the paper's reported values within a tolerance and verifies that the growth rate increases with width."
    },
    {
      "file": "critical_supersaturation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "width",
          "critical_supersaturation"
        ],
        "units": {
          "width": "a0",
          "critical_supersaturation": "dimensionless"
        }
      },
      "description": "Critical relative supersaturation as a function of stripe width. The checker compares the submitted values to the paper's reported values within a tolerance and verifies that the critical supersaturation decreases with increasing width."
    }
  ],
  "notes": "No hidden gold or tolerances revealed; all scoring is based on comparison to paper-reported values via hidden tests."
}
```

## How you are scored
Your submission is scored by an automated hidden verifier. It reads the submitted growth_rates.csv and critical_supersaturation.csv and compares each entry against expected reference values, with tolerances that accommodate legitimate simulation-to-simulation variability. The verifier also checks that the reported growth rates increase with stripe width and that the critical supersaturations decrease with width. The final reward is a weighted combination of these checks; the exact reference values, tolerances, and weights are hidden. The task is not satisfied by simply reporting the paper's numbers — you must execute the Monte Carlo pipeline described in the workflow steps and compute the quantities from your own simulation runs.
