# Structural Transition of Light Metal Clusters in High-Temperature Vapor

## Problem background
This task investigates the structure of gold clusters that form in a dense vapor at high temperatures, using classical molecular dynamics (MD) simulations with a specially developed embedded atom model (EAM) potential. The study examines equilibrium cluster size distributions, cluster geometry via a structure parameter, and the temperature at which the lightest clusters undergo a solid-like to chain-like structural transition. The target result provides insight into the thermodynamics and fractal character of metal clusters, and the computed transition temperature is a key quantity to reproduce.

## Approach
A three-stage computational approach is followed. First, large-scale MD simulations of equilibrium gold vapor are performed at three temperatures (4006 K, 5005 K, 6004 K) using the provided tabulated EAM potential and an open-source MD engine (e.g., LAMMPS). The production runs are long (tens of nanoseconds) and atom coordinates are saved periodically. From these trajectories, clusters are identified with the Stillinger definition (two atoms belong to the same cluster if their separation is below 0.4057 nm), yielding cluster size distributions and, for every cluster size, the ensemble-averaged structure parameter η(k) = ρ_max/ρ_av.

Second, three model structure parameter curves are constructed for reference: η₁(k) for a linear chain (analytical), η₂(k) for a freely jointed chain (Monte Carlo), and η₃(k) for a compact solid-like sphere (Padé approximation or simulation). Third, to map the structural transition, standalone MD simulations of isolated 7-atom and 9-atom clusters are carried out at temperatures below 3000 K, giving η-vs-T data. All η values are combined to compute a reduced structure parameter v = (η − (η₂+η₃)/2) / (η₂−η₃). A second-order polynomial fit to v(T) yields the transition temperature T₀ where v = 0.

## Reproduction target
Produce the following three scored artifacts:

1. Cluster size distributions (n_k in nm⁻³) for temperatures 4006 K, 5005 K, and 6004 K, stored in size_distribution.csv with columns temperature, cluster_size, number_density.
2. Ensemble-averaged structure parameter η(k) for cluster sizes k=2 to 26 at each of the three vapor temperatures, stored in structure_parameter.json as a JSON object with keys '4006', '5005', '6004'.
3. The solid-to-chain structural transition temperature T₀ (in Kelvin), estimated from the reduced structure parameter fit, stored as a single floating-point number in transition_temperature.txt.

## Assets

- Au EAM potential (tabulated form for LAMMPS): the tabulated potential is available as a supplementary file to the publication; obtain it from the supplementary material.
- LAMMPS molecular dynamics package: https://lammps.sandia.gov
- Python with numpy, scipy, matplotlib: numpy scipy matplotlib

## Workflow steps

### Step 1: Equilibrium MD simulation of dense vapor
- Role: process
- Action: Set up LAMMPS simulations at three temperatures: 4006 K (415292 atoms, cubic box side 359 nm), 5005 K (530604 atoms, box side 201 nm), 6004 K (442368 atoms, box side 121 nm). Use the provided EAM potential. Initialize with a crystal at the desired vapor density, apply a Langevin thermostat to thermalize, then switch to NVE ensemble and run production simulations until the potential energy reaches a plateau. Save atom coordinates and velocities every 19.2 ps for cluster analysis.
- Evidence: `/app/outputs/vapor_simulations_complete.txt`

### Step 2: Cluster size distribution analysis
- Role: scored
- Action: From the saved MD trajectories, identify clusters using the Stillinger definition with a cutoff distance of 0.4057 nm. Count clusters of each size k up to at least 26. Compute the number density n_k (nm^{-3}) for each temperature and cluster size. Write the results to size_distribution.csv.
- Output file: `/app/outputs/size_distribution.csv`
- Format: csv
- Contract: Comma-separated values with columns: temperature (float, K), cluster_size (int), number_density (float, nm^{-3}). One row per (temperature, size) pair.
- Scoring: scored by hidden verifier

### Step 3: Reference structure parameter curves
- Role: process
- Action: Compute the structure parameter η₁(k) for a linear chain using the analytical formula η₁(k)=3(1-2/(k+1)). Compute η₂(k) for a freely jointed chain by Monte Carlo simulation of chains with fixed bond length and uniformly distributed bond angles for k=2 to 26. Compute η₃(k) for a solid-like sphere using the Padé approximation or simulation of a simple cubic lattice confined in a sphere, with the asymptote 35/18. Store the reference curves for later use.
- Evidence: `/app/outputs/reference_curves.txt`

### Step 4: MD structure parameter η(k)
- Role: scored
- Action: For each temperature (4006, 5005, 6004 K), using the same cluster-identification output, compute the ensemble-averaged ratio η = ρ_max / ρ_av for every cluster size k from 2 to 26. ρ_max is the maximum interatomic distance within the cluster and ρ_av is the average interatomic distance. Average over all clusters of that size in all saved frames. Output the results as structure_parameter.json.
- Output file: `/app/outputs/structure_parameter.json`
- Format: json
- Contract: JSON object with keys '4006', '5005', '6004'; each value is an array of objects with keys 'k' (int) and 'eta' (float) for k=2..26.
- Scoring: scored by hidden verifier

### Step 5: Standalone MD of individual clusters at low temperatures
- Role: process
- Action: Run additional MD simulations of isolated clusters of sizes 7 and 9 atoms using the same EAM potential. For each size, initialize a solid-like cluster at low temperature, equilibrate with a Langevin thermostat at each target temperature from ~2000 K up to 3000 K (multiple points). After equilibration, run NVE and gather configurations; stop at the first evaporation event and restart if necessary to accumulate statistics. Compute the average η for each (k, T) pair. Save the η-vs-T data for later use.
- Evidence: `/app/outputs/standalone_clusters_done.log`

### Step 6: Reduced structure parameter and transition temperature estimation
- Role: scored (load-bearing)
- Action: Combine all η values from equilibrium vapor simulations and standalone cluster simulations. For each data point at size k, compute the reduced structure parameter v = (η - η_bar) / Δη, where η_bar = (η₂(k) + η₃(k))/2 and Δη = η₂(k) - η₃(k) using the reference curves. Fit a second-order polynomial v(T) = aT² + bT + c to the v(T) data (pool all sizes). Determine the temperature T₀ where v=0 (the root of the polynomial). Output T₀ in Kelvin in transition_temperature.txt.
- Output file: `/app/outputs/transition_temperature.txt`
- Format: txt
- Contract: A single floating-point number representing T0 in Kelvin.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/size_distribution.csv`
- `/app/outputs/structure_parameter.json`
- `/app/outputs/transition_temperature.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### size_distribution.csv
- path: `/app/outputs/size_distribution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cluster size distributions n_k for three temperatures (4006, 5005, 6004 K).
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `cluster_size`, `number_density`
  - `units`:
    - `temperature`: K
    - `cluster_size`: atom count
    - `number_density`: nm^{-3}

### structure_parameter.json
- path: `/app/outputs/structure_parameter.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ensemble-averaged structure parameter η(k) from MD for cluster sizes 2..26 at each temperature.
- schema:
  - `type`: object
  - `properties`:
    - `4006`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `k`:
            - `type`: integer
          - `eta`:
            - `type`: number
    - `5005`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `k`:
            - `type`: integer
          - `eta`:
            - `type`: number
    - `6004`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `k`:
            - `type`: integer
          - `eta`:
            - `type`: number

### transition_temperature.txt
- path: `/app/outputs/transition_temperature.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Solid-to-chain structural transition temperature T0 estimated from MD reduced structure parameter fit.
- schema:
  - `type`: text
  - `content`: A single line containing a floating-point number representing T0 in Kelvin.

Notes: All outputs are compared to hidden reference values from the paper. The size distributions and structure parameters are evaluated using appropriate error metrics; the transition temperature is checked within a tolerance window.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "size_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "cluster_size",
          "number_density"
        ],
        "units": {
          "temperature": "K",
          "cluster_size": "atom count",
          "number_density": "nm^{-3}"
        }
      },
      "description": "Cluster size distributions n_k for three temperatures (4006, 5005, 6004 K)."
    },
    {
      "file": "structure_parameter.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "4006": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "k": {
                  "type": "integer"
                },
                "eta": {
                  "type": "number"
                }
              }
            }
          },
          "5005": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "k": {
                  "type": "integer"
                },
                "eta": {
                  "type": "number"
                }
              }
            }
          },
          "6004": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "k": {
                  "type": "integer"
                },
                "eta": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Ensemble-averaged structure parameter η(k) from MD for cluster sizes 2..26 at each temperature."
    },
    {
      "file": "transition_temperature.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "content": "A single line containing a floating-point number representing T0 in Kelvin."
      },
      "description": "Solid-to-chain structural transition temperature T0 estimated from MD reduced structure parameter fit."
    }
  ],
  "notes": "All outputs are compared to hidden reference values from the paper. The size distributions and structure parameters are evaluated using appropriate error metrics; the transition temperature is checked within a tolerance window."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier that independently scores each of the three output files. The size distributions and structure parameters are compared against reference values within set tolerances, and the transition temperature is checked against an expected range. The final reward is a weighted sum of the per-artifact scores (distributions and structure parameter each carry higher weight, while the transition temperature has a moderate weight). Reporting the paper's published numbers in the output files without genuinely executing the computational workflow will not satisfy the scoring criteria — the verifier assesses the consistency and correctness of the produced artifacts.

## Notes

The EAM potential used in this work is a novel contribution of the paper. Fitting this potential requires extensive DFT calculations and a stress-matching procedure that are beyond the scope of this reproduction, which focuses on the structural transition results. The agent uses the provided tabulated potential without re-fitting it.
