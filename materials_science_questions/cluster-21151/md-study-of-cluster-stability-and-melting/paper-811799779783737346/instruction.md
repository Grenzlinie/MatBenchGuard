# Silver Nanocluster Growth Morphology and Metastable Lifetime from MD

## Problem background
The growth of free silver nanoclusters from a few atoms up to sizes of about 2 nm is controlled by a subtle interplay between thermodynamic stability and kinetic trapping. At these dimensions, non-crystallographic motifs such as icosahedra (Ih) and Marks decahedra (Dh) compete with fcc structures. Experimental observations indicate that both Ih and Dh clusters can appear in gas-phase aggregation, yet the factors that select one morphology over another remain challenging to determine. This task addresses the central open question: how do growth temperature and deposition flux shape the final atomic arrangement of a silver cluster containing roughly 150 atoms? Additionally, the stability of a specific metastable decahedral structure needs to be characterized by measuring its transformation lifetime.

## Approach
The approach is molecular dynamics (MD) simulation using a classical many-body Rosato–Guillopé–Legrand (RGL) potential for silver. Growth is modeled by depositing individual atoms onto a small 7-atom pentagonal bipyramidal seed at regular time intervals, with an Andersen thermostat maintaining the chosen temperature. Simulations are run at several temperatures (350–600 K) and deposition intervals (2–21 ns) to explore a range of growth conditions. The cluster is grown until it reaches approximately 147 atoms, and the final structure is classified via common neighbor analysis (CNA) as Ih, Dh, or hybrid.

In a separate set of simulations, a perfect 146-atom (3,2,2) Marks decahedron is constructed and allowed to evolve freely at fixed temperatures. The time until this metastable structure transforms to an icosahedral configuration is recorded, providing a direct measure of its kinetic stability.

## Reproduction target
Produce two scored CSV files:

* `simulation_results.csv` – for a deposition interval of 7 ns, run independent growth simulations at 400 K, 500 K, and 600 K (one simulation per condition). Grow the cluster to about 147 atoms and use common neighbor analysis to assign the final morphology as Ih, Dh, or hybrid. Report exactly three rows, one per temperature.
* `lifetime_146_Dh.csv` – construct a perfect 146-atom Marks decahedron, perform free-evolution MD at 600 K and 550 K, and measure the time (in nanoseconds) at which it transforms to an icosahedral structure. Report one row per temperature.

The required column schemas and file paths are detailed in the Workflow steps and Output contract sections.

## Assets

- Silver RGL many-body potential parameters: 10.1103/PhysRevB.59.5881
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Common neighbour analysis implementation: ovito|pyscal

## Workflow steps

### Step 1: Structural optimisation of magic clusters
- Role: process
- Action: Perform geometry optimisation of the 55-, 75-, 100-, 101-, 146- and 147-atom magic clusters using the RGL potential to compute minimised energies and the delta quantity. This step reproduces the energetic landscape and demonstrates the energetic driving forces, but is not directly scored.
- Evidence: `/app/outputs/delta_values.csv`

### Step 2: Run atom‑by‑atom MD growth simulations
- Role: process
- Action: Starting from a 7‑atom pentagonal bipyramid seed, run MD simulations with deposition of single Ag atoms. Use a fixed interval of 7 ns between deposits, an Andersen thermostat at the target temperature, and the RGL potential. Grow the cluster until it reaches approximately 147 atoms. Perform three independent runs at 400 K, 500 K, and 600 K. Save the trajectory for subsequent analysis.
- Evidence: `/app/outputs/growth_traj.xyz`

### Step 3: Classify final cluster morphology
- Role: scored
- Action: Extract the final configuration at N≈147 from each of the three growth trajectories. Apply common neighbour analysis to assign local order and classify the overall structure as Ih, Dh, or hybrid. Record the classification in simulation_results.csv.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (int), tau_ns (int), structure (string: Ih, Dh, or hybrid). Must contain exactly three rows for conditions (400 K, 7 ns), (500 K, 7 ns), (600 K, 7 ns).
- Scoring: scored by hidden verifier

### Step 4: Run dynamical stability tests of the 146‑atom m‑Dh
- Role: process
- Action: Build a perfect 146‑atom (3,2,2) m‑Dh cluster. Run free‑evolution MD simulations at 550 K and 600 K using the same RGL potential and Andersen thermostat. Monitor and log the time at which the cluster transforms to an icosahedral structure.
- Evidence: `/app/outputs/stability_log.txt`

### Step 5: Measure metastable lifetimes
- Role: scored (load-bearing)
- Action: From the stability simulations, determine the transformation time (lifetime) for the 146‑atom m‑Dh at 550 K and 600 K. Report these values in lifetime_146_Dh.csv.
- Output file: `/app/outputs/lifetime_146_Dh.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (int), lifetime_ns (float). Must include rows for 550 K and 600 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`
- `/app/outputs/lifetime_146_Dh.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Classified final cluster morphology (Ih, Dh, or hybrid) for three growth conditions: (400 K, 7 ns), (500 K, 7 ns), (600 K, 7 ns).
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `tau_ns`, `structure`

### lifetime_146_Dh.csv
- path: `/app/outputs/lifetime_146_Dh.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Metastable lifetime in nanoseconds for the 146-atom m-Dh at 600 K and 550 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `lifetime_ns`

Notes: The exact lifetime thresholds and acceptable ranges are defined in the hidden grading spec; they are not disclosed to the agent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "tau_ns",
          "structure"
        ]
      },
      "description": "Classified final cluster morphology (Ih, Dh, or hybrid) for three growth conditions: (400 K, 7 ns), (500 K, 7 ns), (600 K, 7 ns)."
    },
    {
      "file": "lifetime_146_Dh.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "lifetime_ns"
        ]
      },
      "description": "Metastable lifetime in nanoseconds for the 146-atom m-Dh at 600 K and 550 K."
    }
  ],
  "notes": "The exact lifetime thresholds and acceptable ranges are defined in the hidden grading spec; they are not disclosed to the agent."
}
```

## How you are scored
Every scored output file (simulation_results.csv and lifetime_146_Dh.csv) is checked by a hidden verifier. The verifier compares your reported results against reference criteria using deterministic rules appropriate to each artifact (exact string comparison for structure classifications, threshold-or-better checks for lifetimes). The criteria are not disclosed in advance—you must obtain the answers from your MD simulations. The final reward is a weighted combination of the scores for the two artifacts. Ensure that your files follow the specified formats exactly; any deviation that prevents the verifier from reading the data will result in zero credit for that artifact.
