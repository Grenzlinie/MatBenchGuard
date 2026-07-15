# Mean-Field Model of Static Recrystallization with Orientation Spread

## Problem background
Static recrystallization in crystalline materials involves the competitive growth of subgrains, ultimately giving rise to new, strain-free grains. Predicting recrystallization kinetics and the resulting crystallographic orientations is challenging because it depends on a large number of evolving microstructural features, including the distribution of boundary disorientation angles. This work develops a compute-driven mean-field model that tracks the moments of orientation spreads to simultaneously predict how fast recrystallization occurs and which orientations become dominant. The central open quantity to compute is whether this mean-field approach can reproduce the kinetics and orientation selection observed in more detailed full-field simulations, using only statistical information about the initial orientation spread and boundary properties.

## Approach
The core idea is a cellular mean-field model where each subgrain is represented by its equivalent radius and its reference disorientation vector. Instead of tracking every boundary explicitly, the model estimates the mean boundary energy and mobility for each cell and for the average medium from the statistical moments of the boundary disorientation angle distribution. This is done in two steps: first, the reference disorientation spread (characterised by a covariance matrix) is used to compute the moments of the boundary disorientation distribution under the assumption of no spatial correlation between orientations. Second, the Read–Shockley energy and Huang–Humphreys mobility laws are expanded around the mean disorientation angle to second order, yielding mean boundary properties that account for the variance of the distribution. Growth rates are then calculated from a classic capillary growth law, and the radii are updated by Euler integration. Small cells are removed to conserve total area, and cells larger than eight times the mean initial radius are identified as recrystallized grains. The model runs without any external data beyond an initial Voronoi-based microstructure that is relaxed to a steady-state size distribution and assigned an isotropic orientation spread. The simulation outputs the time evolution of recrystallized fraction, grain density, mean recrystallized grain size, boundary disorientation moments, and the area-weighted orientation distribution of all grains and of recrystallized grains.

## Reproduction target
Implement the complete mean-field model for static recrystallization with the following specification:

- Generate an initial two-dimensional subgrain microstructure by Voronoi tessellation with periodic boundaries, relax the network to approximate the normal grain-growth steady state (Rayleigh radius distribution with mean radius R0), and assign each cell an isotropic reference disorientation vector drawn from a trivariate normal distribution with isotropic standard deviation σ = 3.5°.
- Run the mean-field simulation under the no-spatial-correlation limit (α → ∞), using the Read–Shockley boundary energy and the Huang–Humphreys mobility law with the parameters γ_c, μ_c, θ_c = 15°, B = 5, η = 4. Integrate cell radii with Euler's method, remove the smallest and negative-radius cells to preserve total area, and identify cells with radius ≥ 8 R0 as recrystallized grains.
- From the simulation, produce the following scored artifacts:
  1. initial_microstructure.csv: cell radii (normalised by R0) and the three components of the reference disorientation vector.
  2. recrystallization_kinetics.csv: time series of recrystallized fraction X, recrystallized grain density (normalised by initial density), and mean recrystallized grain radius (normalised by 8 R0) at discrete normalised time steps.
  3. orientation_distribution.json: area-weighted histograms of reference disorientation angles ω for all grains and for recrystallized grains only, taken at the time step when the recrystallized fraction is closest to 0.5, using 1° bins.
  4. boundary_moments.csv: time series of the mean boundary disorientation angle ⟨θ⟩ and √⟨θ²⟩ for the whole microstructure.

All artifacts must strictly follow the format and schema described in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Generate initial relaxed microstructure and orientations
- Role: scored
- Action: Create a 2D Voronoi tessellation with periodic boundaries, relax the cell network to approximate the normal grain‑growth steady state (Rayleigh radius distribution), then assign each cell an isotropic reference disorientation vector drawn from a trivariate normal distribution with isotropic spread σ=3.5°. Save the cell radii (normalised by mean radius) and the three components of the reference disorientation vector to a CSV.
- Output file: `/app/outputs/initial_microstructure.csv`
- Format: csv
- Contract: Columns: cell_id (int), radius (float), r1 (float), r2 (float), r3 (float). Radius is in units of the mean radius R0, disorientation vector components are in quaternion vector part representation (unitless).
- Scoring: scored by hidden verifier

### Step 2: Execute mean-field recrystallization simulation
- Role: process
- Action: Implement and run the complete mean-field model for static recrystallization, using the initial microstructure as input. At every time step: (i) compute the covariance matrix of reference disorientation vectors (second moment) and the isotropic spread σ^{ref}; (ii) compute the boundary disorientation vector second moments per cell and for the whole microstructure under the no‑spatial‑correlation limit (α→∞); (iii) derive the first two moments of the boundary disorientation angle distribution using the non‑central χ statistics (Laguerre function); (iv) compute mean boundary mobility and energy per cell and the medium mean energy via second‑order Taylor expansions of the Read–Shockley energy law and Huang–Humphreys mobility law; (v) update cell radii using the growth‑rate equation with Euler integration and remove smallest/negative‑radius cells to conserve total area; (vi) identify cells with radius ≥ 8R₀ as recrystallized grains. Accumulate the full history of recrystallized fraction X, recrystallized grain density ρ_rx, mean recrystallized radius ⟨R⟩_rx, boundary disorientation angle moments ⟨θ⟩ and √⟨θ²⟩, and the orientation distribution of recrystallized grains (reference disorientation angles ω).
- Evidence: `/app/outputs/none`

### Step 3: Output recrystallization kinetics
- Role: scored (load-bearing)
- Action: From the simulation history, extract and save the time series of recrystallized fraction X, recrystallized grain density ρ_rx (normalised by initial subgrain density), and mean recrystallized grain radius ⟨R⟩_rx (normalised by the critical radius R_rx = 8R₀). All quantities are sampled at discrete simulation time points (normalised time t in units of 1/(μ_c γ_c ρ₀)).
- Output file: `/app/outputs/recrystallization_kinetics.csv`
- Format: csv
- Contract: Columns: t (float, normalised time), X (float, recrystallized fraction), rho_rx (float, grain density / initial subgrain density), mean_R_rx (float, mean radius / R_rx). All dimensionless.
- Scoring: scored by hidden verifier

### Step 4: Output recrystallized grain orientation distribution
- Role: scored
- Action: At the simulation time step when the recrystallized fraction X is closest to 0.5, compute the area‑weighted histogram of reference disorientation angles ω for all grains (the whole population) and for recrystallized grains only, using bins of 1° width. Save the bin edges and the area fraction arrays as a JSON object.
- Output file: `/app/outputs/orientation_distribution.json`
- Format: json
- Contract: Keys: 'bin_edges' (array of float, bin boundaries in degrees, length = number of bins + 1), 'all_grains_area_fraction' (array of float, area fraction per bin for all grains), 'recrystallized_area_fraction' (array of float, area fraction per bin for recrystallized grains).
- Scoring: scored by hidden verifier

### Step 5: Output boundary disorientation moments time series
- Role: scored
- Action: From the simulation history, extract and save the time evolution of the first moment of the boundary disorientation angle distribution ⟨θ⟩ (mean) and the square root of the second moment √⟨θ²⟩. Both are taken over the whole microstructure and reported in degrees, sampled at the same normalised time points as the kinetics.
- Output file: `/app/outputs/boundary_moments.csv`
- Format: csv
- Contract: Columns: t (float, normalised time), mean_theta (float, ⟨θ⟩ in degrees), sqrt_second_moment (float, √⟨θ²⟩ in degrees).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/initial_microstructure.csv`
- `/app/outputs/recrystallization_kinetics.csv`
- `/app/outputs/orientation_distribution.json`
- `/app/outputs/boundary_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### initial_microstructure.csv
- path: `/app/outputs/initial_microstructure.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Initial subgrain microstructure: cell radii and reference disorientation vectors.
- schema:
  - `type`: table
  - `required_columns`: `cell_id`, `radius`, `r1`, `r2`, `r3`
  - `units`:
    - `radius`: normalised by mean radius R0
    - `r1`: component of δr^{ref} (unitless)
    - `r2`: component of δr^{ref} (unitless)
    - `r3`: component of δr^{ref} (unitless)

### recrystallization_kinetics.csv
- path: `/app/outputs/recrystallization_kinetics.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Recrystallization kinetics: fraction, grain density, and mean recrystallized radius versus time.
- schema:
  - `type`: table
  - `required_columns`: `t`, `X`, `rho_rx`, `mean_R_rx`
  - `units`:
    - `t`: normalised time (1/(μ_c γ_c ρ₀))
    - `X`: dimensionless
    - `rho_rx`: normalised by initial subgrain density ρ₀
    - `mean_R_rx`: normalised by critical radius R_rx = 8R₀

### orientation_distribution.json
- path: `/app/outputs/orientation_distribution.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Area‑weighted histograms of reference disorientation angles ω at ~50% recrystallized fraction.
- schema:
  - `type`: object
  - `required`:
    - `bin_edges`: array of float (degrees)
    - `all_grains_area_fraction`: array of float
    - `recrystallized_area_fraction`: array of float

### boundary_moments.csv
- path: `/app/outputs/boundary_moments.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Time evolution of the first two moments of the boundary disorientation angle distribution (whole microstructure).
- schema:
  - `type`: table
  - `required_columns`: `t`, `mean_theta`, `sqrt_second_moment`
  - `units`:
    - `t`: normalised time (1/(μ_c γ_c ρ₀))
    - `mean_theta`: degrees
    - `sqrt_second_moment`: degrees

Notes: The agent must use the model parameters as given in the paper: γ_c, μ_c, θ_c=15°, B=5, η=4, and the no‑spatial‑correlation limit α→∞. The threshold recrystallized grain radius is 8 times the mean initial radius. The simulation must include at least 5000 subgrains. All outputs are scored against hidden references derived from the paper's figures.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "initial_microstructure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "cell_id",
          "radius",
          "r1",
          "r2",
          "r3"
        ],
        "units": {
          "radius": "normalised by mean radius R0",
          "r1": "component of δr^{ref} (unitless)",
          "r2": "component of δr^{ref} (unitless)",
          "r3": "component of δr^{ref} (unitless)"
        }
      },
      "description": "Initial subgrain microstructure: cell radii and reference disorientation vectors."
    },
    {
      "file": "recrystallization_kinetics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "X",
          "rho_rx",
          "mean_R_rx"
        ],
        "units": {
          "t": "normalised time (1/(μ_c γ_c ρ₀))",
          "X": "dimensionless",
          "rho_rx": "normalised by initial subgrain density ρ₀",
          "mean_R_rx": "normalised by critical radius R_rx = 8R₀"
        }
      },
      "description": "Recrystallization kinetics: fraction, grain density, and mean recrystallized radius versus time."
    },
    {
      "file": "orientation_distribution.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "bin_edges": "array of float (degrees)",
          "all_grains_area_fraction": "array of float",
          "recrystallized_area_fraction": "array of float"
        }
      },
      "description": "Area‑weighted histograms of reference disorientation angles ω at ~50% recrystallized fraction."
    },
    {
      "file": "boundary_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "t",
          "mean_theta",
          "sqrt_second_moment"
        ],
        "units": {
          "t": "normalised time (1/(μ_c γ_c ρ₀))",
          "mean_theta": "degrees",
          "sqrt_second_moment": "degrees"
        }
      },
      "description": "Time evolution of the first two moments of the boundary disorientation angle distribution (whole microstructure)."
    }
  ],
  "notes": "The agent must use the model parameters as given in the paper: γ_c, μ_c, θ_c=15°, B=5, η=4, and the no‑spatial‑correlation limit α→∞. The threshold recrystallized grain radius is 8 times the mean initial radius. The simulation must include at least 5000 subgrains. All outputs are scored against hidden references derived from the paper's figures."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads each of the four scored output files. For each artifact, the verifier recomputes or extracts key derived quantities: for the initial microstructure, it checks that the mean radius and orientation spread are statistically consistent with the target values. For the kinetics, it computes metrics such as the time to 50% recrystallization, the recrystallized grain density at a specific early time, and the mean recrystallized radius at that time. For the orientation distribution, it quantifies the agreement between your recrystallized-area histogram and a hidden reference using the Wasserstein distance. For the boundary moments, it compares your ⟨θ⟩ and √⟨θ²⟩ at selected times against hidden gold values. Each check is directional where appropriate (e.g., meeting or beating a threshold earns full credit; larger errors earn less), and all scores are combined with a weighting that reflects the importance of each artifact. The final reward is a number between 0 and 1. Simply reporting the expected numbers without running the simulation will not pass these checks, because the verifier examines the full time series and distributions, not just a single self-reported value.
