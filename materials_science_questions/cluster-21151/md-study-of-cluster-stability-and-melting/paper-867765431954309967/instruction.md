# Cooperative Atom Attachment in Supercooled Ni via MD Simulation

## Problem background
Classical theories of crystal nucleation and growth from a liquid assume that atoms individually attach to and detach from the growing interface via diffusion-based jumps. However, recent molecular dynamics (MD) simulations suggest that this picture may be incomplete for metallic liquids. The simulations indicate that atoms might instead join the interface by small adjustments in their local order, and that multiple atoms may coordinate their attachment. This task reproduces the core MD simulation protocol for supercooled nickel (Ni) to examine how atoms incorporate into a growing crystal from the liquid. The goal is to re-run the seeded-growth simulation pipeline and compute measures that quantify whether nearby atoms coordinate their crystallisation and how that coordination depends on temperature.

## Approach
The reproduction uses classical MD with the Mendelev embedded-atom method (EAM) potential for Ni. A liquid of 32,000 atoms is prepared and equilibrated at high temperature, then cooled to supercooled target temperatures. A small crystalline seed is inserted and the system is annealed to allow growth. From the MD trajectories, a local bond-orientational order parameter is computed per atom to construct an index of crystallinity (IC) that distinguishes crystalline from liquid-like atoms. An attachment event is identified where a liquid-like atom near the interface transitions to a crystal-like IC. Persistent nearest neighbours (atoms staying within the first neighbour shell) are tracked, and the IC time series of the target atom and its neighbours are compared to quantify the degree of cooperative attachment. The procedure is repeated at multiple supercooled temperatures to determine how the size of the cooperating group changes.

## Reproduction target
Produce two scored artifacts under /app/outputs:

1. **ic_traces.csv** – IC time series for a target atom and at least five of its persistent nearest neighbours during a cooperative attachment event. The target atom’s IC must rise from below 40 to above 100. The traces must be highly overlapped, indicating coordinated crystallisation.

2. **coherence_lengths.csv** – A table of average coherence length (number of cooperatively attaching atoms) for at least two temperatures. The coherence length must be strictly larger at the lower temperature.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- Mendelev Ni EAM potential (2012): https://www.ctcms.nist.gov/potentials/Ni/Ni.eam.alloy

## Workflow steps

### Step 1: Prepare Ni supercooled liquid
- Role: process
- Action: Using LAMMPS and the Ni EAM potential, create a Ni liquid of 32,000 atoms at 1800 K, equilibrate for 2 ns in NPT, then cool to target temperatures (e.g., 1400 K and 1300 K) at a rate of 10 K/ps, and equilibrate for 1 ns at each temperature.
- Evidence: `/app/outputs/system_prep.log`

### Step 2: Seeded growth MD simulations
- Role: process
- Action: For each target temperature, insert a spherical crystalline Ni seed of radius ~2 nm into the equilibrated liquid. Run a short 5 ps equilibration to heal the interface, then anneal for 1 ns in NPT. Save atomic trajectories every 1 ps for analysis.
- Evidence: `/app/outputs/seed_growth.log`

### Step 3: Compute index of crystallinity (IC)
- Role: process
- Action: From the MD trajectories, compute the local bond-orientational order parameter q6, normalize components, and calculate dot products between neighboring atoms to assign an IC value per atom per timestep. Distinguish crystalline and liquid-like atoms.
- Evidence: none

### Step 4: Extract cooperative attachment IC traces
- Role: scored (load-bearing)
- Action: Identify an attachment event where a liquid atom near the interface transitions to crystalline (IC rises from <40 to >100). For that target atom, find its persistent nearest neighbors (atoms that stay within 3.5 Å for ≥80% of the observation window). Export the IC time series for the target atom and up to 6 nearest neighbors as ic_traces.csv, covering at least 200 ps around the rise.
- Output file: `/app/outputs/ic_traces.csv`
- Format: csv
- Contract: Columns: time (ps), target_IC, neighbor_1_IC, ..., neighbor_N_IC (floats). N >= 5. Time values in ascending order.
- Scoring: scored by hidden verifier

### Step 5: Compute coherence length across events
- Role: process
- Action: For each simulation temperature, identify all attachment and detachment events, compute per-event coherence length as the number of persistent nearest neighbors whose IC traces are highly correlated (Pearson r > 0.8) with the target atom during the attachment window. Average over events to obtain the mean coherence length per temperature.
- Evidence: `/app/outputs/coherence_analysis.log`

### Step 6: Coherence length vs temperature
- Role: scored (load-bearing)
- Action: Export a CSV file coherence_lengths.csv with columns temperature (in Kelvin) and coherence_length (average number of cooperative atoms). Include at least two rows (e.g., T=1400 K and 1300 K). The coherence length must be larger at the lower temperature.
- Output file: `/app/outputs/coherence_lengths.csv`
- Format: csv
- Contract: Columns: temperature (float, K), coherence_length (float). At least two rows with strictly decreasing temperature and strictly increasing coherence_length.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ic_traces.csv`
- `/app/outputs/coherence_lengths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ic_traces.csv
- path: `/app/outputs/ic_traces.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: IC time series of a target atom and its persistent nearest neighbours during a cooperative attachment event. The checker will recompute pairwise Pearson correlations between target_IC and each neighbour_IC over the rise window and verify the average correlation exceeds a hidden threshold.
- schema:
  - `type`: table
  - `required_columns`: `time`, `target_IC`, `neighbor_1_IC`, `neighbor_2_IC`, `neighbor_3_IC`, `neighbor_4_IC`, `neighbor_5_IC`
  - `units`:
    - `time`: ps
    - `target_IC`: dimensionless
    - `neighbor_1_IC`: dimensionless
    - `neighbor_2_IC`: dimensionless
    - `neighbor_3_IC`: dimensionless
    - `neighbor_4_IC`: dimensionless
    - `neighbor_5_IC`: dimensionless

### coherence_lengths.csv
- path: `/app/outputs/coherence_lengths.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Average number of cooperatively attaching atoms at each temperature. The checker verifies that coherence_length strictly increases with decreasing temperature and compares the values to a hidden reference (within tolerance).
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `coherence_length`
  - `units`:
    - `temperature`: K
    - `coherence_length`: number of atoms

Notes: The ic_traces.csv is the primary load-bearing artifact that forces the full MD–IC pipeline to be executed. The coherence_lengths.csv corroborates the temperature trend. No gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ic_traces.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "target_IC",
          "neighbor_1_IC",
          "neighbor_2_IC",
          "neighbor_3_IC",
          "neighbor_4_IC",
          "neighbor_5_IC"
        ],
        "units": {
          "time": "ps",
          "target_IC": "dimensionless",
          "neighbor_1_IC": "dimensionless",
          "neighbor_2_IC": "dimensionless",
          "neighbor_3_IC": "dimensionless",
          "neighbor_4_IC": "dimensionless",
          "neighbor_5_IC": "dimensionless"
        }
      },
      "description": "IC time series of a target atom and its persistent nearest neighbours during a cooperative attachment event. The checker will recompute pairwise Pearson correlations between target_IC and each neighbour_IC over the rise window and verify the average correlation exceeds a hidden threshold."
    },
    {
      "file": "coherence_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "coherence_length"
        ],
        "units": {
          "temperature": "K",
          "coherence_length": "number of atoms"
        }
      },
      "description": "Average number of cooperatively attaching atoms at each temperature. The checker verifies that coherence_length strictly increases with decreasing temperature and compares the values to a hidden reference (within tolerance)."
    }
  ],
  "notes": "The ic_traces.csv is the primary load-bearing artifact that forces the full MD–IC pipeline to be executed. The coherence_lengths.csv corroborates the temperature trend. No gold values are disclosed here."
}
```

## How you are scored
A hidden verifier independently scores each scored workflow stage’s artifact and combines them into a final reward. For ic_traces.csv, the verifier recomputes pairwise Pearson correlations between the target IC trace and each neighbour trace over the attachment window; it verifies that the average correlation exceeds a hidden threshold. For coherence_lengths.csv, the verifier checks that the coherence length strictly increases with decreasing temperature and compares the values to hidden reference numbers (with tolerance) extracted from the original study. Simply reporting the paper’s published numbers is not enough — the artifacts must be generated by executing the full MD–IC pipeline described in the workflow steps.
