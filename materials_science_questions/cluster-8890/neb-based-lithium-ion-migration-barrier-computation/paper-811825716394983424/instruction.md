# First-Principles Molecular Dynamics Simulation of Hydrogen Diffusion in Liquid Lithium-Lead

## Problem background
In fusion reactor blankets, liquid lithium-lead is a leading candidate for tritium breeding. Efficient tritium recovery requires a precise understanding of hydrogen isotope solubility and diffusion in this molten alloy. While experiments have measured macroscopic diffusion constants and solubilities, the atomic-scale chemical state of hydrogen — its charge, binding, and migration pathways — remains poorly understood. This work addresses that gap by using first-principles molecular dynamics to simulate the behavior of a single hydrogen atom in liquid Li₆Pb₃₀ at 900 K. The central open question is how the local lithium environment around the hydrogen atom couples to its charge state and how that coupling, in turn, dictates the hydrogen's mobility and residence in different atomic configurations.

## Approach
The approach is a first-principles molecular dynamics study of a 37‑atom periodic cell containing 6 Li, 30 Pb, and 1 H atom (cubic supercell side 10.93 Å). The simulation is run at 900 K using a plane‑wave density‑functional theory code with the GGA‑PBE functional and ultrasoft pseudopotentials, a 2×2×2 k‑point mesh, and a 450 eV plane‑wave cutoff. After discarding an initial equilibration period, the production trajectory provides the time evolution of all atomic positions. From this trajectory, three separate analyses are performed:

1. **Charge–distance correlation:** For snapshots taken every 10 fs, the nearest Li–H distance and the Mulliken population of the hydrogen atom are extracted. Mulliken populations are obtained by projecting the self‑consistent wavefunctions onto pseudoatomic orbitals. These paired observations allow the relationship between the hydrogen's charge state and its proximity to lithium to be examined.

2. **Local environment classification:** Each snapshot is categorized according to the number of lithium atoms within a 2.5 Å radius of the hydrogen atom: exactly one Li, exactly two Li, or no Li. The total residence time in each of these three states over the entire production run is tallied.

3. **Vibrational frequency estimation:** Time intervals during which the hydrogen is near a single lithium atom are identified. The dominant frequency of the Li–H distance oscillation within these intervals is determined, and a representative frequency (or list of frequencies if multiple independent runs were performed) is reported. This provides an estimate of the Li–H bond stiffness in the liquid.

The simulation code, pseudopotentials, and all required analysis tools (e.g., wavefunction projection) are open‑source and publicly available.

## Reproduction target
Run the first‑principles MD simulation of Li₆Pb₃₀H at 900 K as described above and produce the following three scored artifacts under `/app/outputs`:

* **`population_distance.csv`** – A CSV table with columns `timestep`, `time_fs`, `nearest_Li_H_distance_A`, and `Mulliken_population_charge`, containing one row for every 10 fs snapshot from the production phase (at least 76 rows). This file captures the paired time series of the hydrogen's nearest Li–H distance and its Mulliken population.

* **`vibrational_frequencies.txt`** – A plain text file containing the Li–H vibrational frequency estimated from distance oscillations when the hydrogen is bound to a single lithium atom. The frequency must be given in s⁻¹ and expressed in scientific notation (e.g., `2.0e13`). If you ran multiple independent production simulations with consistent methodology, you may output a space‑separated list of frequencies; otherwise, a single number is expected.

* **`residence_times.csv`** – A CSV table with columns `state` (one of `a`, `b`, `c`) and `residence_time_fs` (float), giving the total cumulative residence time for each of the three hydrogen environments defined in the approach (a: near one Li; b: near two Li; c: no Li within 2.5 Å).

No other scored outputs are required; the heavy MD simulation may be run on external compute resources, and only the final three artifacts need be placed in `/app/outputs`.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code): https://www.quantum-espresso.org/
- GGA-PBE ultrasoft pseudopotentials for Li, Pb, H: https://www.quantum-espresso.org/pseudopotentials/ or SSSP library (https://www.materialscloud.org/discover/sssp/)

## Workflow steps

### Step 1: Run first-principles MD simulation of Li6Pb30H at 900 K
- Role: process
- Action: Prepare a cubic supercell of side 10.93 Å with 6 Li, 30 Pb, and 1 H atom initially positioned near a Li atom. Using an open-source plane-wave DFT code with GGA-PBE and appropriate pseudopotentials, run NVT molecular dynamics at 900 K with a 1 fs timestep. Discard the first 250 fs for equilibration; continue production run for at least 750 fs. Save the atomic trajectory (positions, velocities) and electronic wavefunction snapshots at intervals of 10 fs (or finer) for later population analysis.
- Evidence: `/app/outputs/md_trajectory_saved.log`

### Step 2: Compute hydrogen Mulliken population and nearest Li-H distance vs time
- Role: scored (load-bearing)
- Action: From the production run trajectory (t ≥ 250 fs), every 10 fs extract the nearest Li-H distance (Å) and the Mulliken population (charge) of the hydrogen atom. Compute Mulliken populations by projecting the self-consistent wavefunction onto pseudoatomic orbitals (e.g., using projwfc.x in Quantum ESPRESSO or an equivalent post-processing step). Write the results to population_distance.csv.
- Output file: `/app/outputs/population_distance.csv`
- Format: csv
- Contract: CSV with columns: timestep (int), time_fs (float), nearest_Li_H_distance_A (float), Mulliken_population_charge (float). One row per snapshot (every 10 fs from t≥250 fs to the end of the production run), at least 76 rows.
- Scoring: scored by hidden verifier

### Step 3: Estimate Li-H vibrational frequency from distance fluctuations
- Role: scored
- Action: Identify time windows in the production run where hydrogen is bound to exactly one lithium atom (state (a)), i.e., with a nearby Li-H distance < 2.5 Å. Analyse the oscillations of the Li-H distance within those windows to determine the dominant vibration frequency. Combine the results from all state-(a) intervals (if multiple discrete windows) into a single representative frequency. Write the resulting frequency (in s⁻¹) to vibrational_frequencies.txt.
- Output file: `/app/outputs/vibrational_frequencies.txt`
- Format: txt
- Contract: Text file containing the computed Li-H vibrational frequency in s⁻¹, expressed as one number in scientific notation (e.g., 2.0e13). If the agent performed multiple independent production runs with consistent methodology, a space-separated list is acceptable.
- Scoring: scored by hidden verifier

### Step 4: Classify hydrogen states and calculate residence times
- Role: scored
- Action: Categorise each snapshot from the production run (t ≥ 250 fs) into one of three states based on the number of lithium atoms within a distance threshold of 2.5 Å: (a) exactly one Li, (b) exactly two Li, (c) zero Li. Sum the total residence time (number of snapshots × time step) for each state over the production run. Write the results to residence_times.csv.
- Output file: `/app/outputs/residence_times.csv`
- Format: csv
- Contract: CSV with columns: state (string, one of 'a','b','c'), residence_time_fs (float). One row per state. Sum of all dwell intervals for that state over the production simulation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/population_distance.csv`
- `/app/outputs/vibrational_frequencies.txt`
- `/app/outputs/residence_times.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### population_distance.csv
- path: `/app/outputs/population_distance.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time series of nearest Li-H distance and Mulliken population for hydrogen. The checker will compute a measure of association between the two columns and score based on the trend.
- schema:
  - `type`: table
  - `required_columns`: `timestep`, `time_fs`, `nearest_Li_H_distance_A`, `Mulliken_population_charge`
  - `units`:
    - `nearest_Li_H_distance_A`: angstrom
    - `Mulliken_population_charge`: e

### vibrational_frequencies.txt
- path: `/app/outputs/vibrational_frequencies.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Li-H vibrational frequency estimated from the MD trajectory. The checker will verify the frequency falls within an expected range typical for this system.
- schema:
  - `type`: text
  - `description`: A single number (or space-separated list if multiple runs) in scientific notation, e.g. '2.0e13'. Unit: s⁻¹.

### residence_times.csv
- path: `/app/outputs/residence_times.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Cumulative residence times for the three hydrogen states (a,b,c). The checker will inspect the relative ordering and magnitude of the residence times.
- schema:
  - `type`: table
  - `required_columns`: `state`, `residence_time_fs`
  - `units`:
    - `residence_time_fs`: fs

Notes: The first-principles MD simulation (step_0) is expensive; the agent may run it on external/compute resources and bring the scored artifacts back into the sandbox. The scored targets are derived from the trajectory; absolute values depend on pseudopotential choice and projection scheme, so scoring uses correlation (trend) and a frequency range rather than exact match. The residence-time structure is robust across similar simulation setups.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "population_distance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "timestep",
          "time_fs",
          "nearest_Li_H_distance_A",
          "Mulliken_population_charge"
        ],
        "units": {
          "nearest_Li_H_distance_A": "angstrom",
          "Mulliken_population_charge": "e"
        }
      },
      "description": "Time series of nearest Li-H distance and Mulliken population for hydrogen. The checker will compute a measure of association between the two columns and score based on the trend."
    },
    {
      "file": "vibrational_frequencies.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single number (or space-separated list if multiple runs) in scientific notation, e.g. '2.0e13'. Unit: s⁻¹."
      },
      "description": "Li-H vibrational frequency estimated from the MD trajectory. The checker will verify the frequency falls within an expected range typical for this system."
    },
    {
      "file": "residence_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "state",
          "residence_time_fs"
        ],
        "units": {
          "residence_time_fs": "fs"
        }
      },
      "description": "Cumulative residence times for the three hydrogen states (a,b,c). The checker will inspect the relative ordering and magnitude of the residence times."
    }
  ],
  "notes": "The first-principles MD simulation (step_0) is expensive; the agent may run it on external/compute resources and bring the scored artifacts back into the sandbox. The scored targets are derived from the trajectory; absolute values depend on pseudopotential choice and projection scheme, so scoring uses correlation (trend) and a frequency range rather than exact match. The residence-time structure is robust across similar simulation setups."
}
```

## How you are scored
After you submit the three artifacts listed above, a hidden automated verifier will evaluate them. The verifier computes derived quantities — such as a correlation coefficient from `population_distance.csv`, compares the reported vibrational frequency against a physically‑motivated interval, and inspects the ordering and magnitude of the residence times — without relying on exact numerical matches to any pre‑published value. Each artifact is assessed independently, and the final reward (a floating‑point score between 0 and 1) is a weighted combination of these assessments. You will obtain the highest score when your computed results are physically plausible and consistent with the expected behavior of hydrogen in liquid lithium‑lead, as judged by the verifier's hidden criteria.
