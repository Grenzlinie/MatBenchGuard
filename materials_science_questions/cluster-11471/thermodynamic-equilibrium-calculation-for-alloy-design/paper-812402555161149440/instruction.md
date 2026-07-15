# Homogenization distance calculation for C-Mn steels

## Problem background
In the welding of C-Mn steels, the heat-affected zone (HAZ) near the fusion line experiences a rapid thermal cycle that causes carbon to migrate from pearlite into ferrite. Incomplete carbon homogenization can leave regions with elevated carbon content, increasing local hardenability and the susceptibility to hydrogen-assisted cracking (HAC). The extent of homogenization depends on the initial microstructural geometry, which differs between normalized and hot-rolled plate. The key unknown is the characteristic diffusion distance √(Dt) required to reach a nearly uniform carbon distribution in each microstructure.

## Approach
Two idealized diffusion models capture the essential physics:
- **Normalized steel** is approximated as a sphere of ferrite (radius ~10 µm) surrounded by a thin shell of pearlite. Carbon diffuses from the pearlite reservoir into the ferrite sphere. The applicable solution is that of diffusion into a sphere from a well‑stirred volume of limited capacity. The result is expressed as a series expansion that gives the fractional approach to equilibrium as a function of dimensionless time τ = Dt/a². We are interested in the τ at which this fraction reaches 0.95, from which √(Dt) = √(τ)·a is obtained.
- **Hot‑rolled steel** exhibits a banded structure: alternating layers of ferrite (~60 µm) and pearlite (~20 µm). The diffusion problem reduces to a one‑dimensional finite slab with a solute‑rich region at one end. The concentration profile is built from error‑function solutions, modified by reflection at the boundaries. The agent must solve the finite‑slab problem with reflections to find the √(Dt) at which the distribution is essentially uniform.

## Reproduction target
Implement the two diffusion models described above and compute the homogenization distances:
1. For the normalized microstructure, find the √(Dt) (in micrometres) at which 95% homogenization is achieved.
2. For the hot‑rolled microstructure, find the √(Dt) (in micrometres) at which the carbon distribution is essentially uniform.
Write both values to a single JSON file at `/app/outputs/homogenization_distances.json` using the keys `normalized_steel_95pct_sqrtDt_micrometers` and `hot_rolled_steel_sqrtDt_essentially_complete_micrometers`.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Microstructural geometry parameterization
- Role: process
- Action: Determine the characteristic dimensions for the two microstructures from the paper's description: normalized steel – ferrite sphere radius a = 10 µm, compute the pearlite shell volume factor K; hot-rolled steel – ferrite band width = 60 µm, pearlite band width = 20 µm. Write these parameters to a JSON file.
- Evidence: `/app/outputs/microstructure_parameters.json`

### Step 2: Compute homogenization distances
- Role: scored (load-bearing)
- Action: Implement the analytical diffusion models for the two microstructures:
- Normalized case: spherical diffusion from a well-stirred reservoir of limited volume. Solve the series expansion to find the dimensionless time τ at which the fractional approach to equilibrium is 0.95, then compute √(Dt) = √(τ) × a.
- Hot-rolled case: finite one-dimensional slab with reflections. Using the band geometry, compute the concentration profile via error‑function superposition and reflections and determine the √(Dt) at which the distribution is essentially uniform.
Report both √(Dt) values in micrometers within a single JSON file.
- Output file: `/app/outputs/homogenization_distances.json`
- Format: json
- Contract: JSON object with keys 'normalized_steel_95pct_sqrtDt_micrometers' (float) and 'hot_rolled_steel_sqrtDt_essentially_complete_micrometers' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homogenization_distances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homogenization_distances.json
- path: `/app/outputs/homogenization_distances.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed √(Dt) homogenization distances for the normalized and hot-rolled steel microstructures. The checked values are compared to hidden reference values with an appropriate tolerance.
- schema:
  - `type`: object
  - `required`:
    - `normalized_steel_95pct_sqrtDt_micrometers`: float (micrometers)
    - `hot_rolled_steel_sqrtDt_essentially_complete_micrometers`: float (micrometers)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The task reproduces the two headline homogenization distances reported in the paper. The first step parameterizes the microstructural dimensions; the second step computes the distances. Only the computed distances are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homogenization_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "normalized_steel_95pct_sqrtDt_micrometers": "float (micrometers)",
          "hot_rolled_steel_sqrtDt_essentially_complete_micrometers": "float (micrometers)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Computed √(Dt) homogenization distances for the normalized and hot-rolled steel microstructures. The checked values are compared to hidden reference values with an appropriate tolerance."
    }
  ],
  "notes": "The task reproduces the two headline homogenization distances reported in the paper. The first step parameterizes the microstructural dimensions; the second step computes the distances. Only the computed distances are scored."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/homogenization_distances.json` and compare the two numeric values against predetermined reference results. Each distance is checked independently; the final reward is proportional to the number of values that fall within an accepted tolerance band around the reference. Simply reporting a number without running the required diffusion calculations will not succeed. Ensure your output file follows the required JSON format exactly.
