# Simulating Free and Sticking Coverage in Random Particle Deposition

## Problem background
In industrial sorting processes (e.g., sensor-based sorting of plastic flakes or crushed minerals), objects must be fed non-overlapping onto a plane so that individual recognition can be performed. The simplest feeding method is uniform random deposition, but the fraction of free (non-overlapping) particles and particles that stick to the bottom layer under this protocol is poorly understood. If these fractions can be predicted from the shape of the particles, dense monolayer feeding can be designed more efficiently. This task investigates the problem for identical convex particles (rectangles with aspect ratio 1:2): determine the free coverage fraction (area of particles that end up non-overlapped by any other) and the sticking coverage fraction (area of particles that were free at the instant they landed and form the bottom layer) as functions of the deposition ratio, where the deposition ratio is the ratio of the total area of all deposited particles to the plane area.

## Approach
The approach has two parts. First, derive analytical curves from a general overlap-probability model for convex particles. For identical particles, the free and sticking coverage fractions depend only on the deposition ratio ω and the shape factor s = P/√(4πA), where P is the perimeter and A the area of one particle. The formulas are computed for rectangular particles of dimensions 40×80 units (aspect ratio 1:2), which corresponds to a shape factor s ≈ 1.2. The free coverage fraction is given by ρ_free(ω) = ω exp(−2ω (1 + s²)), and the sticking coverage fraction is ρ_stick(ω) = (1 − exp(−2 (1 + s²) ω)) / (2 (1 + s²)). Second, verify these predictions by Monte Carlo simulation. Rectangles of the same dimensions are deposited uniformly at random onto a large plane (linear dimensions at least 100 times larger than the longer side) with random positions and orientations, one by one, until the cumulative deposited area equals ω·A_plane. For each ω in a range from 0 to 1, independent realizations are run. From each realization we record the free particles (those that do not overlap any earlier particle and are not overlapped by any later particle) and the sticking particles (those that at the instant of deposition do not overlap any earlier particle). The average free and sticking coverage fractions (area of such particles divided by plane area) are computed across realizations and compared to the theoretical curves.

## Reproduction target
Produce the following artifacts for identical rectangular particles (40×80 units, shape factor s≈1.2): theoretical curves of free and sticking coverage fractions as functions of the deposition ratio ω over the interval [0,1] (step ≤0.01), Monte Carlo simulation curves for the same quantities on a coarser ω grid (step ≤0.05) with at least 10 independent realizations per ω, and a summary JSON containing four headline numbers – the maximum free coverage fraction from the theoretical curve, the maximum free coverage fraction from the simulation curve, and the sticking coverage fraction at deposition ratio ω=0.5 from both the theoretical and simulation curves (interpolating if necessary).

## Assets

- Python packages numpy, matplotlib: numpy matplotlib

## Workflow steps

### Step 1: Compute theoretical free coverage fraction curve
- Role: scored
- Action: Implement ρ_free(ω) = ω exp(−2ω (1 + s²)) with s≈1.2. For deposition ratio ω from 0 to 1 (inclusive) with step ≤0.01, compute ρ_free(ω). Save the pairs (ω, ρ_free) to /app/outputs/free_theoretical.csv.
- Output file: `/app/outputs/free_theoretical.csv`
- Format: csv
- Contract: CSV with header 'omega,coverage_fraction'. Each row gives a numeric ω and the corresponding ρ_free.
- Scoring: scored by hidden verifier

### Step 2: Compute theoretical sticking coverage fraction curve
- Role: scored
- Action: Implement ρ_stick(ω) = (1 − exp(−2 (1 + s²) ω)) / (2 (1 + s²)) with s≈1.2. For the same ω grid as the free curve (0 to 1, step ≤0.01), compute ρ_stick(ω). Save to /app/outputs/sticking_theoretical.csv.
- Output file: `/app/outputs/sticking_theoretical.csv`
- Format: csv
- Contract: CSV with header 'omega,coverage_fraction'. Each row gives a numeric ω and the corresponding ρ_stick.
- Scoring: scored by hidden verifier

### Step 3: Monte Carlo simulation of free coverage fraction
- Role: scored
- Action: Simulate uniform random deposition of identical rectangular particles (dimensions 40×80 arbitrary units, aspect ratio 1:2) onto a large plane whose linear dimensions are at least 100 times larger than the longer side. For deposition ratio ω from 0 to 1 (step ≤0.05), run at least 10 independent realizations. In each realization, randomly place particles with uniformly random centre coordinates and uniformly random orientation until the cumulative deposited area equals ω·A_plane. Record which particles are free (never overlap any other particle). Compute the average free coverage fraction (area of free particles divided by plane area) across realizations for each ω. Save as /app/outputs/free_simulation.csv. A free particle is one that does not overlap with any earlier particle and is not overlapped by any later particle.
- Output file: `/app/outputs/free_simulation.csv`
- Format: csv
- Contract: CSV with header 'omega,coverage_fraction'. ω values are the simulation grid points; coverage_fraction is the average over realizations.
- Scoring: scored by hidden verifier

### Step 4: Monte Carlo simulation of sticking coverage fraction
- Role: scored
- Action: Using the same simulation realizations (or equivalent independent set with the same ω grid and number of runs), compute the average sticking coverage fraction. A particle contributes to the sticking fraction if, at the moment it is deposited, it does not overlap any previously placed particle. Compute the sticking coverage fraction (area of such particles divided by plane area) averaged over realizations for each ω. Save as /app/outputs/sticking_simulation.csv.
- Output file: `/app/outputs/sticking_simulation.csv`
- Format: csv
- Contract: CSV with header 'omega,coverage_fraction', same ω grid as free simulation.
- Scoring: scored by hidden verifier

### Step 5: Extract headline summary metrics
- Role: scored
- Action: From the generated theoretical and simulation CSVs, determine: (a) the maximum free coverage fraction from the theoretical curve (free_max_theoretical) and the maximum from the simulation curve (free_max_simulation); (b) the sticking coverage fraction at deposition ratio ω=0.5 from the theoretical curve (stick_at_0.5_theoretical) and from the simulation curve (stick_at_0.5_simulation, linearly interpolating if ω=0.5 is not an exact grid point). Write these four numbers to /app/outputs/results_summary.json as a JSON object with those keys.
- Output file: `/app/outputs/results_summary.json`
- Format: json
- Contract: JSON object with keys: free_max_theoretical, free_max_simulation, stick_at_0.5_theoretical, stick_at_0.5_simulation. Each value is a float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_theoretical.csv`
- `/app/outputs/sticking_theoretical.csv`
- `/app/outputs/free_simulation.csv`
- `/app/outputs/sticking_simulation.csv`
- `/app/outputs/results_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_theoretical.csv
- path: `/app/outputs/free_theoretical.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Theoretical free coverage fraction curve for identical rectangular particles (s≈1.2). The checker recomputes the curve and compares pointwise with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `coverage_fraction`

### sticking_theoretical.csv
- path: `/app/outputs/sticking_theoretical.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Theoretical sticking coverage fraction curve for identical rectangular particles (s≈1.2). The checker recomputes the curve and compares pointwise with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `coverage_fraction`

### free_simulation.csv
- path: `/app/outputs/free_simulation.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulated free coverage fraction from Monte Carlo runs. The checker verifies that the curve shape follows the theoretical trend within a specified tolerance at selected ω points and exhibits a maximum near a expected ω value.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `coverage_fraction`

### sticking_simulation.csv
- path: `/app/outputs/sticking_simulation.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulated sticking coverage fraction from Monte Carlo runs. The checker verifies that the curve shape follows the theoretical trend within a specified tolerance at selected ω points.
- schema:
  - `type`: table
  - `required_columns`: `omega`, `coverage_fraction`

### results_summary.json
- path: `/app/outputs/results_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Headline summary metrics: maximum free coverage fraction (theoretical and simulation) and sticking coverage fraction at ω=0.5 (theoretical and simulation). Checker compares to paper‑reported values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `free_max_theoretical`: float
    - `free_max_simulation`: float
    - `stick_at_0.5_theoretical`: float
    - `stick_at_0.5_simulation`: float

Notes: Theoretical steps use the analytical formulas from the paper with shape factor s≈1.2. The simulation uses rectangular particles 40×80 units on a canvas 100×100 times larger than the particle's longer side. The checker independently recomputes the theoretical curves and performs structural checks on simulation curves. Summary values are compared to paper‑reported target values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_theoretical.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "coverage_fraction"
        ]
      },
      "description": "Theoretical free coverage fraction curve for identical rectangular particles (s≈1.2). The checker recomputes the curve and compares pointwise with an absolute tolerance."
    },
    {
      "file": "sticking_theoretical.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "coverage_fraction"
        ]
      },
      "description": "Theoretical sticking coverage fraction curve for identical rectangular particles (s≈1.2). The checker recomputes the curve and compares pointwise with an absolute tolerance."
    },
    {
      "file": "free_simulation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "coverage_fraction"
        ]
      },
      "description": "Simulated free coverage fraction from Monte Carlo runs. The checker verifies that the curve shape follows the theoretical trend within a specified tolerance at selected ω points and exhibits a maximum near a expected ω value."
    },
    {
      "file": "sticking_simulation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega",
          "coverage_fraction"
        ]
      },
      "description": "Simulated sticking coverage fraction from Monte Carlo runs. The checker verifies that the curve shape follows the theoretical trend within a specified tolerance at selected ω points."
    },
    {
      "file": "results_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "free_max_theoretical": "float",
          "free_max_simulation": "float",
          "stick_at_0.5_theoretical": "float",
          "stick_at_0.5_simulation": "float"
        }
      },
      "description": "Headline summary metrics: maximum free coverage fraction (theoretical and simulation) and sticking coverage fraction at ω=0.5 (theoretical and simulation). Checker compares to paper‑reported values within tolerances."
    }
  ],
  "notes": "Theoretical steps use the analytical formulas from the paper with shape factor s≈1.2. The simulation uses rectangular particles 40×80 units on a canvas 100×100 times larger than the particle's longer side. The checker independently recomputes the theoretical curves and performs structural checks on simulation curves. Summary values are compared to paper‑reported target values."
}
```

## How you are scored
A hidden verifier independently scores each workflow artifact. The theoretical curves are recomputed from first principles and compared pointwise; the simulation curves are checked for agreement with the theoretical trends and for structural features (e.g., peak location and shape); the summary numbers are compared to independently determined reference values. Each artifact contributes a weighted share to a final reward between 0 and 1. Simply reporting a number is not sufficient – all artifacts must be generated from your computations and must pass the verifier's checks.
