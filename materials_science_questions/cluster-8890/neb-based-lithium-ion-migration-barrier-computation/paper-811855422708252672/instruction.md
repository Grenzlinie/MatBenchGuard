# DFT Energy Profiles for Li Ion Migration in LLTO with Vacancies

## Problem background
Solid-state lithium ionic conductors La_{4/3-y}Li_{3y}Ti_2O_6 (LLTO) exhibit high ionic conductivity useful for batteries. The A-site sublattice contains La, Li, and vacancies, and the distribution of vacancies influences Li ion migration. This task investigates, through electronic structure calculations, how the presence and arrangement of A-site vacancies affect the static energy landscape for Li ion movement. By computing the total electronic energy as a Li ion is displaced along a crystallographic direction across different vacancy configurations, one can infer the stable positions and the energy barriers that control ionic transport.

## Approach
The approach uses first-principles total-energy calculations (density functional theory) on three periodic structural models that represent distinct vacancy patterns at composition y≈0.21. All models adopt the tetragonal space group P4/mmm. Model A (LaLiTi₂O₆) has La at the 1a site and Li at the 1b site, with no vacancy; Model B (LiTi₂O₆) introduces vacancies at the 1a site; Model C (La₂LiTi₄O₁₂) places vacancies at the 1b site and requires a doubled unit cell for periodicity. For each model, a single Li ion is fixed at successive positions along the crystallographic a-axis on the ab plane at z=1/2, spanning the range from the 1b site (x=0) to the mid-point (x=0.5 in units of lattice parameter a). At each position, a static total electronic energy calculation is performed while keeping all other atoms fixed. The resulting energy profiles (energy vs. x) for the three models reveal how the energy landscape, stable sites, and bottlenecks depend on the vacancy configuration. The open-source DFT code used should support fixed-atom single-point calculations; the agent chooses a suitable code and convergence setup.

## Reproduction target
The primary deliverable is the file `energy_profiles.csv`, which contains the computed total electronic energy (in eV) for each model at each sampled Li position x. From these raw profiles, the quantities of interest are the x-coordinate of the energy minimum and the energy barrier (difference between the energy at x=0.5 and the minimum) for each model. These features are extracted automatically by the verifier and compared against hidden reference data derived from the physical results of the study. The goal is to produce energy profiles that accurately capture the stable Li positions and the relative barrier heights across the three model vacancy configurations, thus reproducing the main finding that vacancies influence the stable site and activation barrier.

## Assets

- Open-source DFT software package: https://www.quantum-espresso.org/
- Crystallographic data for LLTO (y=0.21) from Zou & Inoue (2005): 10.1007/s11581-005-0033-8

## Workflow steps

### Step 1: Construct periodic structural models
- Role: process
- Action: Prepare the three periodic structural models (Model A: LaLiTi2O6, Model B: LiTi2O6, Model C: La2LiTi4O12) using the crystallographic data from the literature for composition y=0.21 in tetragonal space group P4/mmm. Model A has La at the 1a site and Li at the 1b site. Model B has vacancies at the 1a site and Li at the 1b site. Model C has vacancies at the 1b site and requires a doubled unit cell to be periodic. Write a text file documenting the final cell parameters and atomic coordinates for each model.
- Evidence: `/app/outputs/models_info.txt`

### Step 2: Compute total electronic energy vs Li displacement profiles
- Role: scored (load-bearing)
- Action: For each model (A, B, C), use an open-source DFT code to compute the total electronic energy with a single Li ion fixed at successive positions along the crystallographic a-axis on the ab plane at z=1/2. Sample the Li in-plane coordinate x (in units of the lattice parameter a, with x=0 at the 1b site and x=0.5 at half the cell length) at sufficient intervals to resolve the energy minimum and the barrier at x=0.5. Keep all other atoms fixed at their refined crystallographic positions. Output the computed total energy (in eV) for each (model, x) pair in a CSV file.
- Output file: `/app/outputs/energy_profiles.csv`
- Format: csv
- Contract: columns: model (string: A, B, or C), x (float, dimensionless fraction of lattice parameter a), total_energy (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_profiles.csv
- path: `/app/outputs/energy_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw total electronic energy profiles for the three models. The checker will extract for each model the x position of the energy minimum and the energy barrier (E(x=0.5) - E(min)) and compare to hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `model`, `x`, `total_energy`
  - `units`:
    - `x`: dimensionless, fraction of lattice parameter a
    - `total_energy`: eV

Notes: The agent must not report the extracted minima or barriers as separate artifacts; the checker recomputes them directly from this CSV. The absolute energy zero may be arbitrary but must be consistent within each model.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "x",
          "total_energy"
        ],
        "units": {
          "x": "dimensionless, fraction of lattice parameter a",
          "total_energy": "eV"
        }
      },
      "description": "Raw total electronic energy profiles for the three models. The checker will extract for each model the x position of the energy minimum and the energy barrier (E(x=0.5) - E(min)) and compare to hidden reference values."
    }
  ],
  "notes": "The agent must not report the extracted minima or barriers as separate artifacts; the checker recomputes them directly from this CSV. The absolute energy zero may be arbitrary but must be consistent within each model."
}
```

## How you are scored
The hidden verifier reads `energy_profiles.csv`, identifies for each model (A, B, C) the Li displacement x that yields the lowest total energy and computes the energy barrier as the difference between the total energy at x=0.5 and that minimum. It then compares these extracted values to predetermined reference values with allowances for legitimate numerical spread arising from different DFT implementations and convergence choices. The absolute energy zero is irrelevant; only the relative energy differences and the position of the minima matter. The reward is a number between 0 and 1, computed from the deviations across all three models, with full credit awarded when the minima positions and barriers are within acceptable tolerance of the references. Larger deviations lead to lower scores. The reward is monotonic: more accurate reproduction yields a higher score.
