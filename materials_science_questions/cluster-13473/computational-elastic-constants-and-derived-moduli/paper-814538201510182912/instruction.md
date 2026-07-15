# Monte Carlo Auxeticity in Yukawa Crystals with Nanochannels

## Problem background
Auxetic materials, which possess a negative Poisson's ratio (they expand laterally when stretched), have attracted interest for advanced applications such as sensors and composites. A promising strategy to engineer auxeticity is to modify the internal crystal structure at the nanoscale. This task investigates a system of face-centered cubic (fcc) crystals of particles interacting via a hard-core repulsive Yukawa potential (HCRYP), into which very narrow cylindrical channels (nanochannels) are introduced along the [001] crystallographic direction. The goal is to determine how the concentration of particles filling these nanochannels affects the Poisson's ratio in the [110][1-10] direction, and whether the effect can be adequately captured using a simulation cell that contains only a single channel. By reproducing these elastic property calculations via Monte Carlo simulations, you will quantify the auxeticity amplification and validate the simulation cell size.

## Approach
The core methodology is Monte Carlo simulation in the isothermal-isobaric (NpT) ensemble with variable box shape, following the Parrinello–Rahman method. The elastic compliance tensor is obtained from strain fluctuations, and the Poisson's ratio for any pair of orthogonal directions is then derived. Host particles interact via the HCRYP potential; the particles that occupy the nanochannel positions are treated as hard spheres. The system is set up with type‑A nanochannels: each channel consists of a single chain of particles along [001]. You will construct initial configurations for a unit cell containing N=500 particles with a single channel, at several concentrations c (percentage of channel particles): c=0% (perfect crystal without channels), c=5%, and c=14%. Additionally, you will construct a larger cell of N=2000 particles with four channels, at the same c=5%. For the simulations, you will use dimensionless parameters: inverse screening length κσ=10, inverse temperature βε=20, reduced pressure Pσ³β=100, and a potential cutoff of 2.5σ. Each run must include 10⁶ equilibration cycles and 10⁷ production cycles, with periodic boundary conditions. The primary analyses are: (i) for the size-effect validation, compute the Poisson's ratio in the [110][1-10] direction as a function of the transverse angle α (0–180°, step ≤5°) for both the N=500 and N=2000 systems at c=5%; (ii) for the concentration study, compute the Poisson's ratio at α=0 for the three concentrations (c=0%,5%,14%) using the N=500 cell. The results are required as CSV files with specified columns.

## Reproduction target
Your task is to produce two scored CSV artifacts. 

First, for a fixed channel concentration of 5%, you must compute the Poisson's ratio ν in the [110][1-10] direction as a function of the transverse angle α (from 0° to 180° in steps of 5° or smaller) for two system sizes: a cell of N=500 particles (single channel) and a cell of N=2000 particles (four channels). The resulting curves should be essentially indistinguishable, confirming that the single-channel cell is representative. 

Second, using the single-channel N=500 cell, you must compute ν at α=0 for channel concentrations c=0%, c=5%, and c=14%. The data must be stored in two CSV files: `size_effect_curves.csv` and `concentration_effect.csv`, with the exact schema described in the workflow steps and output contract. The hidden verifier will score each file independently based on how well your computed Poisson's ratios match the expected physical trend and overlap criteria, without requiring prior knowledge of the exact numerical outcomes.

## Assets

- Python 3 with numpy, scipy, matplotlib: numpy scipy matplotlib

## Workflow steps

### Step 1: Build initial configurations
- Role: process
- Action: Construct initial particle coordinates and simulation box matrices for fcc Yukawa crystals with type-A nanochannels. Prepare systems: (i) N=500, single channel at concentrations c=0%, 5%, 14%; (ii) N=2000, four channels at c=5%. Use fcc lattice with lattice constant a derived from pressure Pσ^3β=100 via known equation of state or approximate density. Place channel particles as hard spheres along [001] chains and assign particle types. Save initial configurations in a structured file (e.g., .npz).
- Evidence: `/app/outputs/initial_configs.npz`

### Step 2: Size-effect validation
- Role: scored (load-bearing)
- Action: Using initial configurations from step1, implement Monte Carlo NpT ensemble with variable box shape (Parrinello–Rahman method) and the hard-core repulsive Yukawa potential (HCRYP) for host particles (κσ=10, βε=20, cut-off 2.5σ) and hard-sphere potential for channel particles. Set pressure Pσ^3β=100, acceptance ratio ~30%, periodic boundary conditions. Run 10^6 equilibration and 10^7 production MC cycles. For systems N=500 (single channel, c=5%) and N=2000 (four channels, c=5%), compute the elastic compliance tensor from strain fluctuations and derive the Poisson's ratio in the [110][1-10] direction as a function of the transverse angle α (0–180°, step ≤5°). Write results to size_effect_curves.csv.
- Output file: `/app/outputs/size_effect_curves.csv`
- Format: csv
- Contract: columns: system_size (int), angle_alpha (float, degrees), poisson_ratio (float)
- Scoring: scored by hidden verifier

### Step 3: Concentration dependence
- Role: scored (load-bearing)
- Action: Using the same MC implementation, simulate N=500 single channel at concentrations c=0%, 5%, 14% (using initial configs from step1). For each concentration, compute the Poisson's ratio in the [110][1-10] direction at transverse angle α=0. Write the results to concentration_effect.csv.
- Output file: `/app/outputs/concentration_effect.csv`
- Format: csv
- Contract: columns: concentration (float, percent), poisson_ratio (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/size_effect_curves.csv`
- `/app/outputs/concentration_effect.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### size_effect_curves.csv
- path: `/app/outputs/size_effect_curves.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Poisson's ratio vs α for two system sizes; the checker computes the max absolute difference between the two curves to confirm overlap.
- schema:
  - `type`: table
  - `required_columns`: `system_size`, `angle_alpha`, `poisson_ratio`
  - `units`:
    - `angle_alpha`: degrees
    - `poisson_ratio`: dimensionless

### concentration_effect.csv
- path: `/app/outputs/concentration_effect.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Poisson's ratio at α=0 for concentrations c=0%,5%,14%; values are compared to hidden gold tolerances and checked for monotonic decrease.
- schema:
  - `type`: table
  - `required_columns`: `concentration`, `poisson_ratio`
  - `units`:
    - `concentration`: percent
    - `poisson_ratio`: dimensionless

Notes: The accuracy of the simulations depends on implementation details and stochastic variation; the checker tolerates reasonable spreads while rejecting obviously wrong results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "size_effect_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "system_size",
          "angle_alpha",
          "poisson_ratio"
        ],
        "units": {
          "angle_alpha": "degrees",
          "poisson_ratio": "dimensionless"
        }
      },
      "description": "Poisson's ratio vs α for two system sizes; the checker computes the max absolute difference between the two curves to confirm overlap."
    },
    {
      "file": "concentration_effect.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "concentration",
          "poisson_ratio"
        ],
        "units": {
          "concentration": "percent",
          "poisson_ratio": "dimensionless"
        }
      },
      "description": "Poisson's ratio at α=0 for concentrations c=0%,5%,14%; values are compared to hidden gold tolerances and checked for monotonic decrease."
    }
  ],
  "notes": "The accuracy of the simulations depends on implementation details and stochastic variation; the checker tolerates reasonable spreads while rejecting obviously wrong results."
}
```

## How you are scored
Your submission will be evaluated by an automatic verifier that runs in a separate environment. It will load your CSV files and compute two independent scores that are combined into a final reward. 

- For `size_effect_curves.csv`, the verifier will compute the maximum absolute difference between the Poisson's ratio curve for N=500 and the curve for N=2000 across all angles; a small difference (compared to a hidden tolerance) indicates the curves overlap and earns full credit for that part. 
- For `concentration_effect.csv`, the verifier will check that the reported Poisson's ratio values follow the correct monotonic trend (becoming more negative with increasing concentration) and that the values are consistent with hidden reference numbers. 

Providing only the expected final numbers without executing the required Monte Carlo simulations will not satisfy the structural checks: the verifier examines the internal consistency of the curves and the physical validity of the trend. Overly small effort (e.g., submitting exactly the reference values without realistic statistical noise) may also be penalised.
