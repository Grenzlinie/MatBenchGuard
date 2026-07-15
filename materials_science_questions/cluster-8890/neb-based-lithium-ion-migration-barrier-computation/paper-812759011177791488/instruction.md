# AIMD Study of Li Self-Diffusion in Amorphous LiSi and Li2Si Alloys

## Problem background
Lithium-ion transport is critical for the rate capability of electrode materials in Li-ion batteries. Silicon (Si) anodes suffer from massive structural changes during charge/discharge, which affect Li-ion diffusion. This task investigates how the internal microstructure of Si atoms in amorphous Li-Si alloys relates to Li self-diffusion. Using first-principles molecular dynamics (AIMD), the Li self-diffusion coefficients are computed for different amorphous configurations, and structural descriptors are extracted: for Li-deficient LiSi, the projected low-Si channel area fraction; for Li-rich Li2Si, the total number of Si microstructures (isolated atoms, dumbbells, boomerangs, stars, chains). The goal is to compute these quantities for multiple independently generated structures and determine the nature of the correlation between the structural descriptor and the Li diffusion coefficient.

## Approach
Amorphous LiSi and Li2Si configurations are generated via a melt-quench simulated annealing protocol within orthorhombic supercells (LiSi: 64 Li + 64 Si, ~18.706×9.353×11.486 Å; Li2Si: 96 Li + 48 Si, ~15.40×13.23×12.01 Å). For each configuration, ab initio molecular dynamics (NVT ensemble, 800 K, Nosé–Hoover thermostat, Verlet integrator, 1.5 fs time step, 15 ps total, Γ‑point sampling) is run to obtain atomic trajectories. From these trajectories, the Li mean-square displacement (MSD) is computed, and the Li self-diffusion coefficient D_Li is extracted from the long-time linear slope MSD/(6t). For LiSi, snapshots from the first 1000 steps (every 10th step) are used to project Si positions onto the yz plane, construct a Si density map, and calculate the fraction of the projected area that is low in Si density (the diffusion channel area). For Li2Si, snapshots are sampled similarly, and the total number of Si microstructures (isolated atoms, dumbbells, boomerangs, stars, chains) is counted using a 2.5 Å Si–Si cutoff. The scripted workflow outputs the (structure_id, D_Li, channel_area_fraction) pairs for LiSi and (structure_id, D_Li, total_microstructures) pairs for Li2Si as CSV files.

## Reproduction target
For at least 5 independently generated amorphous LiSi configurations, produce a CSV file containing each configuration's identifier, the AIMD-computed Li self-diffusion coefficient (cm²/s), and the projected low-Si channel area fraction (dimensionless). For at least 5 independently generated amorphous Li2Si configurations, produce a CSV file containing each configuration's identifier, the AIMD-computed Li self-diffusion coefficient (cm²/s), and the total number of Si microstructures counted over 1000 sampled snapshots. The hidden verifier will use these files to examine the relationship between the structural descriptors and the diffusion coefficients.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Generate amorphous LiSi and Li2Si structures
- Role: process
- Action: Generate at least 5 independent amorphous LiSi configurations (64 Li + 64 Si, supercell ~18.706×9.353×11.486 Å) and at least 5 independent amorphous Li2Si configurations (96 Li + 48 Si, supercell ~15.40×13.23×12.01 Å) using a melt-quench simulated annealing protocol.
- Evidence: none

### Step 2: Run AIMD simulations
- Role: process
- Action: Perform ab initio molecular dynamics (NVT, 800 K, Nosé–Hoover thermostat, Verlet integrator, 1.5 fs time step, 15 ps total, Γ-point sampling) for each generated structure to obtain atomic trajectories.
- Evidence: none

### Step 3: Compute Li self-diffusion coefficients from MSD
- Role: process
- Action: From each AIMD trajectory, compute the Li mean-square displacement (MSD), identify the long-time linear region, and extract the Li self-diffusion coefficient D_Li = MSD/(6t) in cm²/s.
- Evidence: none

### Step 4: Compute channel area for LiSi and output correlation data
- Role: scored
- Action: For each LiSi configuration, using snapshots from the first 1000 AIMD steps (sampled every 10 steps), project Si atomic positions onto the yz plane, compute a Si density map, identify low-Si density regions as the diffusion channel, calculate the fraction of the projected plane area that is low-Si, and combine with the corresponding D_Li into a CSV.
- Output file: `/app/outputs/lisi_correlation.csv`
- Format: csv
- Contract: Columns: structure_id (string), D_Li (float, cm2/s), channel_area_fraction (float, dimensionless). At least 5 rows.
- Scoring: scored by hidden verifier

### Step 5: Count Si microstructures for Li2Si and output correlation data
- Role: scored
- Action: For each Li2Si configuration, sample structures every 10 steps over 1000 snapshots from the AIMD trajectory. Count the total number of Si microstructures (isolated atoms, dumbbells, boomerangs, stars, chains) using a 2.5 Å Si–Si cutoff. Sum over all snapshots to obtain total_microstructures. Combine with the corresponding D_Li into a CSV.
- Output file: `/app/outputs/li2si_correlation.csv`
- Format: csv
- Contract: Columns: structure_id (string), D_Li (float, cm2/s), total_microstructures (int). At least 5 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lisi_correlation.csv`
- `/app/outputs/li2si_correlation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lisi_correlation.csv
- path: `/app/outputs/lisi_correlation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Each row corresponds to one LiSi amorphous configuration. The checker will compute Spearman rank correlation between D_Li and channel_area_fraction and require rho >= 0.7.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `D_Li`, `channel_area_fraction`
  - `units`:
    - `D_Li`: cm^2/s
    - `channel_area_fraction`: dimensionless

### li2si_correlation.csv
- path: `/app/outputs/li2si_correlation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Each row corresponds to one Li2Si amorphous configuration. The checker will compute Spearman rank correlation between D_Li and total_microstructures and require rho <= -0.7.
- schema:
  - `type`: table
  - `required_columns`: `structure_id`, `D_Li`, `total_microstructures`
  - `units`:
    - `D_Li`: cm^2/s
    - `total_microstructures`: count

Notes: The task omits manual structural modifications, ring-size breakdown for LiSi, and Li15Si4 phase per the agreed scope. The agent must generate its own amorphous configurations; no specific structures from the paper are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lisi_correlation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "D_Li",
          "channel_area_fraction"
        ],
        "units": {
          "D_Li": "cm^2/s",
          "channel_area_fraction": "dimensionless"
        }
      },
      "description": "Each row corresponds to one LiSi amorphous configuration. The checker will compute Spearman rank correlation between D_Li and channel_area_fraction and require rho >= 0.7."
    },
    {
      "file": "li2si_correlation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_id",
          "D_Li",
          "total_microstructures"
        ],
        "units": {
          "D_Li": "cm^2/s",
          "total_microstructures": "count"
        }
      },
      "description": "Each row corresponds to one Li2Si amorphous configuration. The checker will compute Spearman rank correlation between D_Li and total_microstructures and require rho <= -0.7."
    }
  ],
  "notes": "The task omits manual structural modifications, ring-size breakdown for LiSi, and Li15Si4 phase per the agreed scope. The agent must generate its own amorphous configurations; no specific structures from the paper are required."
}
```

## How you are scored
Each scored workflow stage (the LiSi channel area step and the Li2Si microstructure counting step) is evaluated independently by a hidden verifier. The verifier checks the required output files for correct format and the presence of at least the minimum number of configurations, then computes a statistical measure of the relationship between the reported D_Li values and the respective structural descriptor. The final reward is a weighted combination of the scores from the two stages. Simply reporting numerical values without actually performing the AIMD simulations and analysis will not satisfy the verifier; the pipeline must be executed to produce the specified CSV files.
