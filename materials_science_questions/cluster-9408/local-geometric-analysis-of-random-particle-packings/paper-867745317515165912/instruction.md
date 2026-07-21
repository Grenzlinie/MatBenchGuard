# Power-law scaling of frustrated mass in 2D random bi-chromatic bearings

## Problem background
Space-filling bearings have been proposed as simplified models for the motion of tectonic plates, where the space between plates is filled with particles that can roll on each other, reducing friction. Earlier bearing constructions required highly symmetric particle arrangements and allowed particles of arbitrarily small size. This work introduces an algorithm for generating random, bi-chromatic (two-color) space-filling packings of disks in two dimensions, which guarantees frictionless rotation. A lower cutoff on particle size (epsilon) is imposed, inevitably leaving unfilled spaces. When gravity is applied, unsupported particles move, creating frustrated contacts that dissipate energy. The key quantity of interest is how the total mass M of particles involved in these frustrated contacts scales with the cutoff epsilon; the scaling is expected to follow a power law M ~ epsilon^gamma.

## Approach
The approach consists of two main parts. First, construct a random packing of non-overlapping disks: start with disks of random sizes within a given range (lower bound epsilon) and randomly place them without overlap. Then iteratively insert the largest possible disk that fits without overlapping any existing disk, until the space is filled. To enforce the bearing (bi-chromatic) condition, each disk is assigned one of two colors so that no two disks of the same color touch. When a candidate disk would have to touch three disks that are not all the same color, its radius is reduced by a factor alpha (set to 0.5) so that it touches only the two disks that share the same color. This avoids odd loops and guarantees frictionless rotation. After constructing the packing with a given cutoff epsilon, apply a gravity semi-dynamics: any particle that does not have enough contacts to support its weight falls or rolls until a stable configuration is reached. Identify frustrated contacts (where rotation would be impossible) and compute M, the total mass of particles involved in such contacts. By repeating this procedure for at least five different values of epsilon spanning at least one order of magnitude, you obtain a set of (epsilon, M) pairs.

## Reproduction target
Implement the algorithm described above to generate random bi-chromatic 2D bearings with alpha = 0.5. For each of at least five distinct cutoff values epsilon spanning at least one order of magnitude (e.g., 0.01, 0.02, 0.04, 0.08, 0.16), run the construction, apply the gravity semi-dynamics, and compute the total frustrated mass M. Record all (epsilon, M) pairs in the output CSV file. The checker will perform a log-log linear regression on these data to extract the exponent gamma and assess the quality of the fit. Your goal is to produce data that exhibits a clear power-law scaling.

## Assets
No external datasets or pre-trained models are required. The workflow uses the standard Python scientific computing stack (NumPy, SciPy) for numerical operations and CSV writing. These are available via pip (e.g., from the default PyPI or the Tsinghua mirror).

## Workflow steps

### Step 1: Generate frustrated mass vs epsilon data
- Role: scored (load-bearing)
- Action: Implement the iterative algorithm for constructing random two-dimensional bi-chromatic space-filling packings with alpha=0.5 and a particle size cutoff epsilon. For each epsilon in a set of at least five values spanning at least one order of magnitude, generate a packing, apply the gravity semi-dynamics simulation as described (unsupported particles fall/roll until stable), identify frustrated contacts, and compute the total mass M of particles involved in frustrated contacts. Record each (epsilon, M) pair.
- Output file: `/app/outputs/frustrated_mass_vs_epsilon.csv`
- Format: csv
- Contract: columns: epsilon (float), frustrated_mass (float). At least 5 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frustrated_mass_vs_epsilon.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frustrated_mass_vs_epsilon.csv
- path: `/app/outputs/frustrated_mass_vs_epsilon.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw data of particle size cutoff epsilon versus total frustrated mass M, from which the checker will fit a power law and extract the scaling exponent gamma.
- schema:
  - `type`: table
  - `required_columns`: `epsilon`, `frustrated_mass`

Notes: The checker will perform log-log linear regression on the submitted (epsilon, M) pairs, extract the slope gamma, and compare it to a hidden reference value with a tolerance. It will also require a minimum number of data points and a fit R² threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frustrated_mass_vs_epsilon.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilon",
          "frustrated_mass"
        ]
      },
      "description": "Raw data of particle size cutoff epsilon versus total frustrated mass M, from which the checker will fit a power law and extract the scaling exponent gamma."
    }
  ],
  "notes": "The checker will perform log-log linear regression on the submitted (epsilon, M) pairs, extract the slope gamma, and compare it to a hidden reference value with a tolerance. It will also require a minimum number of data points and a fit R² threshold."
}
```

## How you are scored
A hidden verifier reads the submitted /app/outputs/frustrated_mass_vs_epsilon.csv, performs a log10(M) vs log10(epsilon) linear regression, and extracts the fitted exponent gamma and the coefficient of determination R^2. The extracted gamma is compared to a hidden reference value with an appropriate tolerance. The reward is 1.0 if gamma matches the reference within threshold AND the R^2 exceeds a required minimum (indicating a good power-law fit); otherwise the reward is 0.0. The exact tolerance and R^2 threshold are hidden.
