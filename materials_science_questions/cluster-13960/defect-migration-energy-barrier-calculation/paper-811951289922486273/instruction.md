# Approximate transition states via iterative flooding on a periodic energy grid

## Problem background
In computational studies of ionic diffusion in crystalline materials, identifying transition states—the least-stable configurations through which a diffusing ion passes—is essential for determining migration barriers. These saddle points are local maxima along the minimum-energy path on the potential energy hypersurface. For many systems, especially interstitial diffusion, the approximate transition state location is not obvious, so it is necessary to map the potential energy as a function of the diffusing ion's position over a periodic grid and then automatically locate candidate saddle points. The Bubble algorithm is an iterative flooding method that addresses this: starting from the global minimum, it gradually raises an energy threshold and tracks the expanding connected region of accessible states, recording the highest points encountered when the region first connects the global minimum to its periodic images.

## Approach
The Bubble algorithm treats the discretised energy grid as a landscape. It begins by locating the global minimum in the central unit cell. All other grid points are initially marked as dry. Iteratively, a water level (energy threshold) is raised, and any dry grid point that is a nearest neighbour of a wet point and has energy below the current level becomes wet, expanding the connected region. Simultaneously, grid points that lie above the previous water level but have at least one dry neighbour below that level are flagged as candidate saddle points. When the wet region first reaches a periodic image of the global minimum, the highest wet grid point along the connecting ridge is recorded as an approximate transition state for that periodic direction. The process continues until all distinct periodic directions have been found. The resulting set of transition states provides approximate locations and energies that can later be refined by saddle-point search methods.

## Reproduction target
Implement the Bubble iterative flooding algorithm for the 3D periodic synthetic potential f(x,y,z) = -cos(2πx/Lx) - cos(2πy/Ly) - cos(2πz/Lz), where Lx=5 Å, Ly=10 Å, Lz=5 Å. Evaluate the potential on a uniform grid over the central unit cell, enforce periodic boundary conditions in all three directions, locate the global minimum, and run the flooding search to discover all distinct approximate transition states that connect the global minimum to its periodic images. For each discovered transition state, record its index, energy (in eV), and Cartesian coordinates (in Å). Write these results as a JSON file.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Run Bubble flooding algorithm
- Role: scored (load-bearing)
- Action: Implement the Bubble iterative flooding search on the synthetic periodic potential provided in the instruction. The algorithm must: (1) evaluate the given analytic potential on a uniform 20×40×20 grid with 0.25 Å spacing over the central unit cell, enforcing periodic boundary conditions; (2) locate the global minimum grid point; (3) iteratively raise a water level (energy threshold), expanding a connected wet region by nearest‑neighbour connectivity and recording candidate saddle points (grid points with energy above the previous threshold and a neighbour dry point below that threshold); (4) when the wet region first reaches a periodic image of the global minimum, identify the highest wet point along that connection as the approximate transition state; (5) continue flooding to discover transition states in all distinct periodic directions; (6) write the resulting transition states to the output file.
- Output file: `/app/outputs/transition_states.json`
- Format: json
- Contract: A JSON array of objects. Each object has keys: "index" (integer), "energy" (float, in eV), and "coordinates" (array of three floats, Cartesian coordinates in Å). The order of objects in the array is arbitrary.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_states.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_states.json
- path: `/app/outputs/transition_states.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: List of distinct approximate transition states found by the Bubble flooding algorithm on the synthetic periodic potential. The checker matches each reported state to a precomputed set of true saddle points within coordinate and energy tolerances.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `index`, `energy`, `coordinates`
    - `properties`:
      - `index`:
        - `type`: integer
      - `energy`:
        - `type`: number
        - `units`: eV
      - `coordinates`:
        - `type`: array
        - `items`:
          - `type`: number
          - `units`: Å
        - `minItems`: 3
        - `maxItems`: 3

Notes: The synthetic analytic potential function is supplied in the instruction. The Bubble algorithm must be implemented by the agent; no external Bubble code or precomputed grid is provided. The output must contain all distinct diffusion directions (at least three for a 3D unit cell).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_states.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "index",
            "energy",
            "coordinates"
          ],
          "properties": {
            "index": {
              "type": "integer"
            },
            "energy": {
              "type": "number",
              "units": "eV"
            },
            "coordinates": {
              "type": "array",
              "items": {
                "type": "number",
                "units": "Å"
              },
              "minItems": 3,
              "maxItems": 3
            }
          }
        }
      },
      "description": "List of distinct approximate transition states found by the Bubble flooding algorithm on the synthetic periodic potential. The checker matches each reported state to a precomputed set of true saddle points within coordinate and energy tolerances."
    }
  ],
  "notes": "The synthetic analytic potential function is supplied in the instruction. The Bubble algorithm must be implemented by the agent; no external Bubble code or precomputed grid is provided. The output must contain all distinct diffusion directions (at least three for a 3D unit cell)."
}
```

## How you are scored
A hidden verifier will independently score your output artifact. The verifier compares each transition state you report against a reference set of true saddle points for the synthetic potential. Matching is performed using coordinate and energy tolerances (the verifier finds the nearest reported state for each reference saddle). Your reward is proportional to the fraction of reference states correctly identified. Simply writing a known value from the literature is not sufficient; you must run the flooding algorithm to produce the output file. The verifier does not require a specific ordering of the transition states in the JSON file.
