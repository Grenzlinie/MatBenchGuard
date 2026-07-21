# Temperature-Induced Short-Range Order Changes in Co67B33 Metallic Glass via Ab Initio MD

## Problem background
Metallic glasses exhibit temperature‑dependent short‑range order that affects mechanical properties. This work investigates the structural evolution of amorphous Co67B33 thin films by ab initio molecular dynamics, aiming to quantify how topological building blocks, such as B–Co–B bond angles and Frank–Kasper‑like polyhedra, change with temperature. Understanding these changes is essential for linking short‑range order to the temperature dependence of the elastic limit.

## Approach
The approach uses ab initio molecular dynamics (AIMD) simulations with the PBE exchange‑correlation functional and GTH pseudopotentials for an amorphous Co67B33 model at 300 K, 600 K, 1000 K, and 1600 K. From the resulting atomic trajectories, three types of structural analysis are carried out: (1) partial pair distribution functions (PDFs) for Co–B and B–B pairs are computed to determine the positions of key coordination shells; (2) the B–Co–B bond angle distribution is calculated to identify the fraction of angles close to 90°, which is associated with rigid second‑order structures; (3) Voronoi tessellation is performed, and the fraction of Frank–Kasper‑like polyhedra (densely packed Co‑ and B‑centered polyhedra) is obtained. The analysis is repeated at each temperature to reveal how the population of these structural motifs evolves.

## Reproduction target
Using CP2K and GTH pseudopotentials, run AIMD simulations for an amorphous Co67B33 model with at least 64 atoms and the PBE functional at 300 K, 600 K, 1000 K, and 1600 K. Equilibrate each simulation and collect a production trajectory of at least 5 ps. Then, for each temperature, compute:

• the first Co–B peak position and the first and second B–B peak positions (in Å) from the partial PDFs;

• the fraction of B–Co–B bond angles within ±5° of 90°;

• the fraction of Frank–Kasper‑like Voronoi polyhedra.

Write the results to `/app/outputs/simulation_results.json` in the format specified by the output contract.

## Assets

- CP2K: https://www.cp2k.org/
- GTH pseudopotentials for Co and B: https://www.cp2k.org/static/potentials/

## Workflow steps

### Step 1: AIMD simulations of Co67B33 at multiple temperatures
- Role: process
- Action: Run ab initio molecular dynamics simulations for an amorphous Co67B33 model at 300 K, 600 K, 1000 K, and 1600 K using CP2K and GTH pseudopotentials. Use a simulation cell with at least 64 atoms and the PBE functional. Equilibrate and run production for at least 5 ps at each temperature. Save the atomic trajectories.
- Evidence: `/app/outputs/trajectory_info.txt`

### Step 2: Compute structural properties and report results
- Role: scored (load-bearing)
- Action: From the trajectories, compute the Co–B and B–B partial pair distribution functions and extract the first Co–B peak position, and the first and second B–B peak positions at each temperature. Compute the B–Co–B bond angle distribution and report the fraction of angles within ±5° of 90° at each temperature. Perform Voronoi tessellation and compute the fraction of Frank–Kasper‑like polyhedra at each temperature. Write all results to simulation_results.json.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: {"peak_positions": {"300K": {"CoB_first": "float", "BB_first": "float", "BB_second": "float"}, "600K": {"CoB_first": "float", "BB_first": "float", "BB_second": "float"}, "1000K": {"CoB_first": "float", "BB_first": "float", "BB_second": "float"}, "1600K": {"CoB_first": "float", "BB_first": "float", "BB_second": "float"}}, "bond_angle_90deg_fraction": {"300K": "float", "600K": "float", "1000K": "float", "1600K": "float"}, "frank_kasper_fraction": {"300K": "float", "600K": "float", "1000K": "float", "1600K": "float"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported structural metrics from AIMD simulations: partial PDF peak positions (Å), fraction of B–Co–B angles near 90°, and fraction of Frank–Kasper‑like polyhedra. The hidden checker compares each reported value to the paper’s reported values within predefined tolerances and also verifies that the bond angle fraction and FK fraction decrease monotonically from 300 K to 1600 K.
- schema:
  - `type`: object
  - `required`: `peak_positions`, `bond_angle_90deg_fraction`, `frank_kasper_fraction`
  - `properties`:
    - `peak_positions`:
      - `type`: object
      - `required`: `300K`, `600K`, `1000K`, `1600K`
      - `properties`:
        - `300K`:
          - `CoB_first`: float
          - `BB_first`: float
          - `BB_second`: float
        - `600K`:
          - `CoB_first`: float
          - `BB_first`: float
          - `BB_second`: float
        - `1000K`:
          - `CoB_first`: float
          - `BB_first`: float
          - `BB_second`: float
        - `1600K`:
          - `CoB_first`: float
          - `BB_first`: float
          - `BB_second`: float
    - `bond_angle_90deg_fraction`:
      - `type`: object
      - `required`: `300K`, `600K`, `1000K`, `1600K`
      - `properties`:
        - `300K`: float
        - `600K`: float
        - `1000K`: float
        - `1600K`: float
    - `frank_kasper_fraction`:
      - `type`: object
      - `required`: `300K`, `600K`, `1000K`, `1600K`
      - `properties`:
        - `300K`: float
        - `600K`: float
        - `1000K`: float
        - `1600K`: float

Notes: The checker performs a result-level comparison (T0) because recomputing from raw trajectories inside the checker sandbox is not feasible. Tolerances and trend checks are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "peak_positions",
          "bond_angle_90deg_fraction",
          "frank_kasper_fraction"
        ],
        "properties": {
          "peak_positions": {
            "type": "object",
            "required": [
              "300K",
              "600K",
              "1000K",
              "1600K"
            ],
            "properties": {
              "300K": {
                "CoB_first": "float",
                "BB_first": "float",
                "BB_second": "float"
              },
              "600K": {
                "CoB_first": "float",
                "BB_first": "float",
                "BB_second": "float"
              },
              "1000K": {
                "CoB_first": "float",
                "BB_first": "float",
                "BB_second": "float"
              },
              "1600K": {
                "CoB_first": "float",
                "BB_first": "float",
                "BB_second": "float"
              }
            }
          },
          "bond_angle_90deg_fraction": {
            "type": "object",
            "required": [
              "300K",
              "600K",
              "1000K",
              "1600K"
            ],
            "properties": {
              "300K": "float",
              "600K": "float",
              "1000K": "float",
              "1600K": "float"
            }
          },
          "frank_kasper_fraction": {
            "type": "object",
            "required": [
              "300K",
              "600K",
              "1000K",
              "1600K"
            ],
            "properties": {
              "300K": "float",
              "600K": "float",
              "1000K": "float",
              "1600K": "float"
            }
          }
        }
      },
      "description": "Agent-reported structural metrics from AIMD simulations: partial PDF peak positions (Å), fraction of B–Co–B angles near 90°, and fraction of Frank–Kasper‑like polyhedra. The hidden checker compares each reported value to the paper’s reported values within predefined tolerances and also verifies that the bond angle fraction and FK fraction decrease monotonically from 300 K to 1600 K."
    }
  ],
  "notes": "The checker performs a result-level comparison (T0) because recomputing from raw trajectories inside the checker sandbox is not feasible. Tolerances and trend checks are hidden."
}
```

## How you are scored
The hidden verifier reads your `simulation_results.json` and compares each reported value against a set of hidden reference values derived from the published study. It also checks that the bond‑angle fraction at 90° and the Frank‑Kasper fraction follow the expected evolution with temperature (e.g., a consistent trend from 300 K to 1600 K). The reward is a weighted combination of scores from the three groups: peak positions, bond‑angle fraction, and Frank‑Kasper fraction. To achieve a high score, you must faithfully run the AIMD simulations and analysis; simply reporting fabricated numbers that do not agree with the reference will result in a low reward. The exact tolerances and reference values are hidden, so you must rely on the physics of the system and the specified procedure.
