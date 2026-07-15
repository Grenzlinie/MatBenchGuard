# Explicit finite-difference model for interstitial oxygen diffusion and precipitation in silicon

## Problem background
Czochralski silicon wafers contain dissolved interstitial oxygen that can precipitate during high-temperature processing. Understanding how these precipitates nucleate, grow, and interact is critical for controlling defect formation and engineering denuded zones near the wafer surface, a technique known as intrinsic gettering. A predictive model that captures the interplay between oxygen diffusion, precipitate growth/dissolution, and the resulting spatial distribution of precipitates is needed to guide process design. This task asks you to implement and exercise such a model, computing quantities that characterize precipitation kinetics and the development of denuded zones under well-defined thermal conditions.

## Approach
The modeling approach is a discrete numerical scheme that evolves interstitial oxygen concentration on a two‑dimensional spatial grid via an explicit finite‑difference diffusion solver. Each grid cell may contain a spherical oxide precipitate. At each time step, oxygen diffuses between neighboring cells, while within each cell the precipitate grows or dissolves depending on the local oxygen supersaturation relative to a critical radius. The critical radius is derived from the solid solubility of oxygen, which is a function of temperature. The mass exchange between precipitate and interstitial oxygen follows distinct laws for growth and dissolution: growth incorporates a sticking coefficient that modulates the attachment rate, while dissolution is driven by the local under-saturation. The simulation evolves over many time steps, conserving total oxygen, and tracks the amount of precipitated oxygen per precipitate as well as the radius of each precipitate. Two distinct physical scenarios are studied: a small periodic domain at 1000 °C with a fixed number of precipitates to examine competition among them, and a larger domain at 1200 °C with outdiffusion at the surface to examine denuded‑zone formation. In the latter, the dependence on the sticking coefficient is explored by repeating the simulation for different values of that parameter.

## Reproduction target
Implement the explicit finite‑difference diffusion‑precipitation model and run it in the two scenarios described in the workflow steps below. The primary targets are two CSV files:

1. `step01_precipitation_kinetics.csv` — the time evolution of the average number of precipitated oxygen atoms per precipitate for a 20‑precipitate configuration at 1000 °C over 12 hours.

2. `step02_parameter_sweep.csv` — for a fixed precipitate density at 1200 °C and a 13‑hour anneal, compute, for each sticking coefficient α = 1.0, 0.1, and 0.01: (a) the denuded‑zone depth (distance from the wafer surface to the first depth where the average precipitate radius exceeds 0.05 µm) and (b) the final average precipitate radius over all precipitates.

Your implementation must respect the domain sizes, cell sizes, initial conditions, boundary conditions, and physical parameters detailed in the workflow steps. The goal is to obtain physically reasonable numerical results that arise from the model dynamics, not to match any particular published figure or table.

## Assets

- Interstitial oxygen diffusion coefficient D: 10.1063/1.331757

## Workflow steps

### Step 1: 1000°C precipitation kinetics
- Role: scored (load-bearing)
- Action: Implement the explicit finite‑difference nearest‑neighbor oxygen diffusion scheme on a 2D grid (20.2×20.2 µm, cell 0.2 µm) with periodic boundary conditions. Initialize 20 precipitates with radius 8 Å and interstitial oxygen concentration 8.4×10¹⁷ cm⁻³. Use the diffusion coefficient D at 1000 °C, the critical‑radius expression, the solid‑solubility relation, and the growth/dissolution laws with sticking coefficient α=1. Run the simulation for 12 hours, recording the number of precipitated oxygen atoms per precipitate at regular intervals. Output the result as `step01_precipitation_kinetics.csv`.
- Output file: `/app/outputs/step01_precipitation_kinetics.csv`
- Format: csv
- Contract: CSV with columns: time_hr (float), precipitated_oxygen_atoms_per_precipitate (float). Headers required.
- Scoring: scored by hidden verifier

### Step 2: 1200°C parameter sweep (sticking coefficient)
- Role: scored
- Action: Extend the same diffusion‑precipitation model to a 101×250 µm domain (cell 1 µm) at 1200 °C. Use reflecting boundary at y=250 µm (wafer centre) and outdiffusion surface condition (Oi forced towards the equilibrium value) at y=0. Initial interstitial oxygen 9.0×10¹⁷ cm⁻³, initial precipitate radius 18 Å, precipitate density 5.78×10⁹ cm⁻³. Run the simulation for 13 hours for each sticking coefficient α = 1.0, 0.1, 0.01. After each run, compute (a) the denuded‑zone depth (distance from y=0 to the first y‑coordinate where the average precipitate radius exceeds 0.05 µm) and (b) the final average precipitate radius over all precipitates. Output the results as `step02_parameter_sweep.csv`.
- Output file: `/app/outputs/step02_parameter_sweep.csv`
- Format: csv
- Contract: CSV with columns: sticking_coefficient (float), denuded_zone_depth_um (float), final_precipitate_radius_um (float). Three rows for α = 1.0, 0.1, 0.01.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step01_precipitation_kinetics.csv`
- `/app/outputs/step02_parameter_sweep.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step01_precipitation_kinetics.csv
- path: `/app/outputs/step01_precipitation_kinetics.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time evolution of the average number of precipitated oxygen atoms per precipitate for the 20‑precipitate case at 1000 °C. Compared to digitized values from the paper with relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `time_hr`, `precipitated_oxygen_atoms_per_precipitate`
  - `units`:
    - `time_hr`: hours
    - `precipitated_oxygen_atoms_per_precipitate`: atoms

### step02_parameter_sweep.csv
- path: `/app/outputs/step02_parameter_sweep.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Denuded‑zone depth and final average precipitate radius for sticking coefficients 1.0, 0.1, and 0.01 at 1200 °C. Compared to digitized values from the paper with relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `sticking_coefficient`, `denuded_zone_depth_um`, `final_precipitate_radius_um`
  - `units`:
    - `sticking_coefficient`: dimensionless
    - `denuded_zone_depth_um`: micrometers
    - `final_precipitate_radius_um`: micrometers

Notes: The denuded‑zone depth is defined as the distance from the surface (y=0) to the first depth where the average precipitate radius exceeds 0.05 µm. Both outputs are scored by comparing the agent's computed values to digitized data from the paper's figures using a relative tolerance on both axes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step01_precipitation_kinetics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_hr",
          "precipitated_oxygen_atoms_per_precipitate"
        ],
        "units": {
          "time_hr": "hours",
          "precipitated_oxygen_atoms_per_precipitate": "atoms"
        }
      },
      "description": "Time evolution of the average number of precipitated oxygen atoms per precipitate for the 20‑precipitate case at 1000 °C. Compared to digitized values from the paper with relative tolerance."
    },
    {
      "file": "step02_parameter_sweep.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sticking_coefficient",
          "denuded_zone_depth_um",
          "final_precipitate_radius_um"
        ],
        "units": {
          "sticking_coefficient": "dimensionless",
          "denuded_zone_depth_um": "micrometers",
          "final_precipitate_radius_um": "micrometers"
        }
      },
      "description": "Denuded‑zone depth and final average precipitate radius for sticking coefficients 1.0, 0.1, and 0.01 at 1200 °C. Compared to digitized values from the paper with relative tolerance."
    }
  ],
  "notes": "The denuded‑zone depth is defined as the distance from the surface (y=0) to the first depth where the average precipitate radius exceeds 0.05 µm. Both outputs are scored by comparing the agent's computed values to digitized data from the paper's figures using a relative tolerance on both axes."
}
```

## How you are scored
A hidden verifier will read your output files and independently score each of the two workflow artifacts. For each artifact, the computed values are compared against reference data using appropriate tolerances that allow for legitimate differences arising from implementation choices (e.g., discretization, time‑stepping), while still demanding that the model captures the essential physical trends. The two scores are combined with pre‑defined weights into a single overall reward between 0 and 1. It is therefore essential that you actually implement and run the model as specified; simply copying or fabricating numbers will not pass the hidden verification. The verifier does not assess your code style, documentation, or intermediate outputs beyond the two CSV files.
