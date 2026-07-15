# Quench-Induced Fragmentation in Colloidal Clusters

## Problem background
Colloidal particles with short-range attraction and long-range repulsion can self-assemble into stable clusters without any confining potential. When the attraction strength is suddenly reduced (quenched), these clusters break apart into fragments. The size of the original cluster and the depth of the quench determine the resulting fragment multiplicity and the distribution of fragment sizes. This work investigates the quench-induced fragmentation of two-dimensional colloidal clusters composed of N particles. By simulating clusters of different sizes and quenching to various attraction strengths, one can identify thresholds where the cluster disintegrates completely and characterize the predominant break-up patterns.

## Approach
Simulate N interacting particles in a two-dimensional open system. The particles interact via a pairwise potential that combines a long-range Coulomb repulsion and a short-range exponential attraction: U(r) = 1/r - B exp(-κ r) with κ = 1. The dynamics are overdamped Langevin equations with a small finite temperature. Begin by preparing stable clusters at a value of B slightly above the cluster stability threshold (B > B_c). Then instantaneously reduce the attraction strength to a lower value B* and continue the dynamics until the resulting fragments are stable. Record the fragment sizes from each independent run. Implement the entire simulation in Python using NumPy for numerical integration and SciPy for any required optimization. Do not use external molecular-dynamics packages.

## Reproduction target
Produce a raw dataset of quench outcomes for cluster sizes N = 5, 12, and 15. For each N, run multiple independent quenches across a range of B* values that spans from just below the cluster's stability limit down to values that cause the cluster to break into individual particles. The primary output is a JSON file containing, for every (N, B*) condition, the fragment sizes observed in each quench run. A hidden verifier will later recompute two quantities from these raw data: the complete-disintegration threshold (the B* at which the average number of fragments equals N) and the most frequent fragmentation modes (the partitioning of N into smaller clusters).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Generate stable cluster configurations
- Role: process
- Action: For N=5, 12, 15, initialize particles randomly and relax them under U(r)=1/r - B exp(-r) at zero temperature using overdamped dynamics (no thermal noise). Use B values slightly above the critical Bc (e.g., 6.5 for N=12). Save the final relaxed positions.
- Evidence: `/app/outputs/stable_configs.json`

### Step 2: Quench fragmentation simulations
- Role: scored (load-bearing)
- Action: For each N=5,12,15, select a set of quench attraction strengths B* spanning from just below Bc down to values that cause complete disintegration. For each B*, run 20 independent quenches: load the stable configuration, instantaneously change the attraction strength to B* and run Langevin dynamics at small but finite temperature until fragments stabilize. Record the sizes of the resulting clusters for each quench. Save all outcomes as quench_events.json.
- Output file: `/app/outputs/quench_events.json`
- Format: json
- Contract: Array of objects. Each object has keys: N (integer), B_star (float), outcomes (list of lists of integers; each inner list contains fragment sizes from one quench). Example element: {"N": 12, "B_star": 4.75, "outcomes": [[1,1,1,1,1,1,1,1,1,1,1,1], [1,1,1,3,3,3], ...]}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/quench_events.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### quench_events.json
- path: `/app/outputs/quench_events.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw quench events; each element contains the cluster size, the quenched attraction strength, and the fragmentation outcomes for all independent quench runs. The verifier recomputes the complete-disintegration threshold (where average multiplicity equals N) and dominant decay modes from these raw data.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `N`:
        - `type`: integer
      - `B_star`:
        - `type`: number
      - `outcomes`:
        - `type`: array
        - `items`:
          - `type`: array
          - `items`:
            - `type`: integer
    - `required`: `N`, `B_star`, `outcomes`

Notes: The agent must produce all required quench events for N=5,12,15. The verifier will recompute thresholds and modes T1-style. No gold values or tolerances are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "quench_events.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "N": {
              "type": "integer"
            },
            "B_star": {
              "type": "number"
            },
            "outcomes": {
              "type": "array",
              "items": {
                "type": "array",
                "items": {
                  "type": "integer"
                }
              }
            }
          },
          "required": [
            "N",
            "B_star",
            "outcomes"
          ]
        }
      },
      "description": "Raw quench events; each element contains the cluster size, the quenched attraction strength, and the fragmentation outcomes for all independent quench runs. The verifier recomputes the complete-disintegration threshold (where average multiplicity equals N) and dominant decay modes from these raw data."
    }
  ],
  "notes": "The agent must produce all required quench events for N=5,12,15. The verifier will recompute thresholds and modes T1-style. No gold values or tolerances are disclosed."
}
```

## How you are scored
The hidden verifier independently reads your submitted `quench_events.json` and recomputes per-(N, B*) fragment statistics. It then compares those derived quantities against the paper's findings. The verifier does not compare a single self-reported number; instead it evaluates whether the simulated data imply the correct disintegration thresholds (within physically reasonable tolerances) and the correct dominant decay modes for each cluster size, as well as whether the fragment multiplicity increases monotonically with quench depth. The final reward is a weighted combination of these checks, with the disintegration thresholds and decay-mode patterns carrying most of the weight. Simply reporting the expected numbers is not sufficient; you must produce the raw simulation events from which those numbers arise.
