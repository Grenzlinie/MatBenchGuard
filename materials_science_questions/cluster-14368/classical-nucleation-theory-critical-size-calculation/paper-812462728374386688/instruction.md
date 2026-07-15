# Free Energy Change of Droplet Formation using Fisher's Model

## Problem background
In hot nuclear matter expanding through the metastable region at subnuclear densities, density inhomogeneities can grow, leading to the formation of liquid droplets in a supersaturated vapor. Understanding the free-energy barrier that governs this droplet nucleation is important for interpreting fragmentation in heavy-ion collisions and astrophysical scenarios. Classical nucleation theory extended with Fisher's droplet model provides an expression for the free-energy change ΔG as a function of droplet radius r, incorporating surface tension, bulk free-energy gain, and a logarithmic surface-entropy correction. This task computes ΔG(r) curves for a nucleonic vapor at fixed temperature and several supersaturation ratios, from which the critical droplet radius can be determined.

## Approach
Implement the Fisher droplet model free-energy function: ΔG(r) = 4π r² σ – (4/3)π r³ n T ln S + 3 T τ ln(r/r₀). The physical parameters are fixed: temperature T = 10 MeV, number density of the hot liquid n = 0.15 fm⁻³, surface tension σ = 1 MeV·fm⁻², and the critical exponent τ = 2.2. The small-distance cutoff r₀ is derived from the density via r₀ = (3/(4π n))^(1/3). Evaluate ΔG(r) for three supersaturation ratios: S = 2, 3, and 4. Compute the curves on a fine grid of radii spanning the region where the maximum is expected, then write the results to a CSV file. The submitted curve data will be used to locate the critical radius r*, defined as the radius that maximizes ΔG for each S.

## Reproduction target
Produce a single CSV file `free_energy_curves.csv` containing the free-energy change ΔG(r) for each supersaturation ratio S = 2, 3, 4. The file must have columns S (integer), r (float, radius in fm), and DeltaG (float, free energy in MeV). One row per (S, r) point; the r grid must be fine enough to capture the maximum. The hidden verifier will load this file, group by S, and extract the critical radius that maximizes DeltaG.

## Assets

- Python with scientific libraries (numpy, scipy, pandas): numpy scipy pandas

## Workflow steps

### Step 1: Compute ΔG(r) curves and output CSV
- Role: scored
- Action: Implement the free energy change function ΔG(r) = 4π r² σ – (4/3)π r³ n T ln S + 3 T τ ln(r/r₀) with parameters T=10 MeV, n=0.15 fm⁻³, σ=1 MeV·fm⁻², τ=2.2, and supersaturation ratios S = 2, 3, 4. Derive r₀ from n via r₀ = (3/(4π n))^(1/3). Compute ΔG(r) on a fine grid of radii (covering the critical region, e.g., 0.1–10 fm with sufficient resolution to locate the maximum) and write the results as a CSV file with columns: S, r, DeltaG.
- Output file: `/app/outputs/free_energy_curves.csv`
- Format: csv
- Contract: CSV with columns: S (integer, supersaturation ratio), r (float, radius in fm), DeltaG (float, free energy change in MeV). One row per (S, r) point. Must include a header line.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_curves.csv
- path: `/app/outputs/free_energy_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Free energy change ΔG(r) computed for S=2,3,4. The checker will group by S, find the r that maximizes DeltaG, and compare the resulting critical radii to hidden reference values with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `S`, `r`, `DeltaG`
  - `columns`:
    - `S`: integer (supersaturation ratio)
    - `r`: float (droplet radius, fm)
    - `DeltaG`: float (free energy change, MeV)

Notes: The agent must derive r₀ from the given number density n. The hidden checker recomputes critical radii directly from the submitted curve; it does not trust any agent-reported numbers. No network access is needed for scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "S",
          "r",
          "DeltaG"
        ],
        "columns": {
          "S": "integer (supersaturation ratio)",
          "r": "float (droplet radius, fm)",
          "DeltaG": "float (free energy change, MeV)"
        }
      },
      "description": "Free energy change ΔG(r) computed for S=2,3,4. The checker will group by S, find the r that maximizes DeltaG, and compare the resulting critical radii to hidden reference values with an absolute tolerance."
    }
  ],
  "notes": "The agent must derive r₀ from the given number density n. The hidden checker recomputes critical radii directly from the submitted curve; it does not trust any agent-reported numbers. No network access is needed for scoring."
}
```

## How you are scored
The hidden verifier has expected critical radii for each S. It will read your submitted CSV, isolate the curve for each S, find the radius that yields the maximum DeltaG, and compare the extracted r* values to the expected ones with predetermined tolerances. The reward is a combined score between 0 and 1 that reflects the fraction of S values whose derived critical radius is sufficiently accurate. The verifier's scoring logic, tolerances, and reference values are hidden; submitting the curve with a well-resolved maximum that matches the physics of the problem will earn the highest reward.
