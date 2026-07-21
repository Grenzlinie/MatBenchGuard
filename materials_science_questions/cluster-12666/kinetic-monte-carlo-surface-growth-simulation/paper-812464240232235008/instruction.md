# Kinetic Monte Carlo Surface Growth with and without Incorporation

## Problem background
During epitaxial growth of thin films, mound formation and surface roughening are strongly influenced by the Ehrlich-Schwoebel (ES) barrier, which hinders adatoms from descending step edges. Continuum models suggest that an additional incorporation mechanism—where freshly deposited adatoms can immediately relax downwards within a finite range—changes the coarsening behaviour and may lead to slope selection. This task uses kinetic Monte Carlo (KMC) simulations of a solid-on-solid (SOS) model to test this idea: does the presence of an incorporation rule change the surface width evolution from random‑deposition‑like behaviour to coarsening with a distinct growth exponent? You will produce two time series of surface width that allow a verifier to extract the long‑time power‑law exponent.

## Model specification
Your KMC simulation must follow the definitions below exactly.

### Lattice and boundaries
- 2D square lattice of 300 × 300 sites with periodic boundary conditions.
- The surface is represented by a height array `h[x][y]` (integers, in lattice units). Only positive overhangs are forbidden (solid‑on‑solid condition).

### Standard events and rates
The simulation evolves via two kinds of events: deposition and diffusion hops. All rates are given in s⁻¹.

#### 1. Deposition
Particles are deposited onto the surface at a constant global rate of `F * N_sites`, where
- `F = 1 ML s⁻¹` (monolayer per second)
- `N_sites = 90000`

Each deposition event selects a lattice site `(x, y)` uniformly at random and increments `h[x][y]` by one, i.e., places an atom on top of the existing column.

#### 2. Diffusion hops
Every surface atom can hop to a vacant neighbouring site. A hop from site `i` to a nearest‑neighbour site `j` is allowed only if `h[j] ≤ h[i]` (downwards or lateral) and the final height difference after the hop would be one lattice constant (SOS constraint). The attempt frequency is `ν0 = 10¹² s⁻¹`.

The activation energy for a hop is
```
E_act = E_B + n * E_N + (E_S if the hop is downward and not suppressed else 0)
```
with
- substrate diffusion barrier `E_B = 0.9 eV`
- nearest‑neighbour bond energy `E_N = 0.25 eV`
- Ehrlich‑Schwoebel (ES) barrier `E_S = 0.1 eV`
- `n` = number of in‑plane nearest neighbours of the jumping atom **before** the jump (neighbours in the same layer).

A hop is **downward** if the height of the origin site is strictly greater than the height of the target site before the jump, i.e. `h[origin] > h[target]`.

The rate of a specific hop is
```
r = ν0 * exp( - E_act / (k_B T) )
```
where `k_B` is the Boltzmann constant and the temperature is `T = 560 K`.

#### 3. Suppression of the ES barrier for narrow bottom terraces
When the jumping atom resides on a **bottom terrace whose width is exactly one lattice constant**, the ES barrier is not added, i.e. `E_S = 0` for that hop even if it is downward.

*How to detect a bottom terrace of width 1*: For the jumping atom at `(x, y)`, examine the local height field. A bottom terrace of width 1 is a local minimum that is only one lattice constant wide in at least one direction. A practical definition that reproduces the papers findings is: if `h[x][y]` has two opposite neighbours `(x-1,y)` and `(x+1,y)` both with heights `h >= h[x][y]+1`, or similarly for the y‑direction, the atom sits on a narrow bottom terrace and the ES barrier is suppressed. If you implement a different but physically equivalent detection you must ensure it reproduces the suppression for terraces that are exactly one lattice constant wide.

### Incorporation mechanism (used only in the “with incorporation” variant)
After **each deposition event**, the newly placed particle is allowed to relax immediately:
- Look at the four nearest neighbours of the deposition site.
- If any neighbour has a height strictly lower than the current height after deposition (`h[dep_site] > h[neighbour]`), move the particle **once** to a lower neighbour. If several lower neighbours exist, pick one arbitrarily (e.g. the first found).
- The relaxed atom ends one layer lower; no further relaxation is performed.
- This rule implements an incorporation radius `R_inc = 1a` (one lattice constant), as checked only nearest neighbours.

The **without incorporation** variant never applies this relaxation step.

### KMC algorithm
Use the standard rejection‑free kinetic Monte Carlo method (e.g. Bortz‑Kalos‑Lebowitz / Gillespie):
1. Build a list of all possible events (deposition + diffusion hops for all surface atoms) and compute their rates as defined above using the provided physical constants.
2. Choose an event with probability proportional to its rate and advance the physical time by `Δt = -ln(U)/R_total`, where `U` is a uniform random number in (0,1] and `R_total` is the sum of all rates.
3. Execute the chosen event (update heights). For the “with incorporation” variant apply the incorporation rule immediately after any deposition event.
4. Repeat until the total deposited amount reaches 1000 ML.

### Recording surface configurations
Every **10 ML** of deposited material, save the full height array `h[x][y]` to an intermediate file (internal, not scored) to be used later for the width computation. The time (ML) of each snapshot must be recorded.

## Workflow steps

### Step 1: Run KMC simulations with and without incorporation
- Role: process
- Action: Implement the KMC model **exactly** as specified above. Run **two independent simulations** (with and without incorporation) on a 300×300 periodic lattice at T = 560 K. Use the given physical constants. Deposit a total of 1000 ML. Save the full height configuration every 10 ML for each variant. These intermediate files are not directly scored but are required for the next steps.
- Evidence: (internal, not scored)

### Step 2: Compute surface width without incorporation
- Role: scored (load‑bearing)
- Action: From the recorded height data of the simulation **without incorporation**, at every recorded time (every 10 ML) compute the root‑mean‑square surface width
  ```
  w(t) = sqrt( ⟨ (h_i - ⟨h⟩)² ⟩ )
  ```
  where the average is over all 90 000 lattice sites.
  Write a CSV file with columns `time` (in ML) and `surface_width` (in lattice units). Times must be strictly increasing.
- Output file: `/app/outputs/surface_width_without_incorporation.csv`
- Format: csv
- Contract: Two columns: `time` (float, units ML), `surface_width` (float, units lattice constants). Times are strictly increasing.
- Scoring: scored by hidden verifier

### Step 3: Compute surface width with incorporation
- Role: scored (load‑bearing)
- Action: From the recorded height data of the simulation **with incorporation**, compute the surface width at each recorded time and write a CSV file in the same format as the without‑incorporation file.
- Output file: `/app/outputs/surface_width_with_incorporation.csv`
- Format: csv
- Contract: Two columns: `time` (float, units ML), `surface_width` (float, units lattice constants). Times are strictly increasing.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_width_without_incorporation.csv`
- `/app/outputs/surface_width_with_incorporation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_width_without_incorporation.csv
- path: `/app/outputs/surface_width_without_incorporation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of RMS surface width for the simulation without incorporation. The checker will fit the growth exponent beta from the late‑time data and verify it against the expected behaviour.
- schema:
  - `type`: table
  - `required_columns`: `time`, `surface_width`
  - `units`:
    - `time`: ML
    - `surface_width`: lattice units

### surface_width_with_incorporation.csv
- path: `/app/outputs/surface_width_with_incorporation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of RMS surface width for the simulation with incorporation. The checker will fit the growth exponent beta and verify coarsening behaviour (decreasing time derivative).
- schema:
  - `type`: table
  - `required_columns`: `time`, `surface_width`
  - `units`:
    - `time`: ML
    - `surface_width`: lattice units

Notes: The checker recomputes the growth exponent beta from the provided time‑series data and compares against hidden gold values; no exact tolerances are disclosed. The full KMC simulation on a 300×300 lattice for 1000 ML is computationally intensive but required.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, CSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_width_without_incorporation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [ "time", "surface_width" ],
        "units": { "time": "ML", "surface_width": "lattice units" }
      },
      "description": "Time series of RMS surface width for the simulation without incorporation. The checker will fit the growth exponent beta from the late‑time data and verify it against the expected behaviour."
    },
    {
      "file": "surface_width_with_incorporation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [ "time", "surface_width" ],
        "units": { "time": "ML", "surface_width": "lattice units" }
      },
      "description": "Time series of RMS surface width for the simulation with incorporation. The checker will fit the growth exponent beta and verify coarsening behaviour (decreasing time derivative)."
    }
  ],
  "notes": "The checker recomputes the growth exponent beta from the provided time‑series data and compares against hidden gold values; no exact tolerances are disclosed. The full KMC simulation on a 300×300 lattice for 1000 ML is computationally intensive but required."
}
```

## How you are scored
A hidden verifier program reads each submitted CSV file. It performs a linear regression of `log(surface_width)` versus `log(time)` using data from the later deposition stages to extract the growth exponent beta. The verifier checks that surface width increases monotonically over time. For the with‑incorporation run, it also verifies that coarsening occurs (the local slope decreases). Each scored output contributes a weighted portion to your total reward. The verifier judges the quantitative accuracy and trends of your results; simply reporting a number without the underlying reproducible time series is not enough.