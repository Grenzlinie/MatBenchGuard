# Thermal properties of Pd nanoclusters: heat capacity and atomic diffusion

## Problem background
Nanocrystalline palladium (Pd) samples prepared by compaction of nanoclusters have been reported to exhibit a substantial excess heat capacity compared to coarse-grained polycrystalline Pd in the temperature range 150–300 K. The origin of this excess is not fully understood; it could arise from the intrinsic finite-size effects of individual free clusters, from inter-grain boundaries and structural disorder in compacted materials, or from the presence of impurities such as hydrogen. Molecular dynamics (MD) simulations of ideal spherical Pd nanoclusters and clusters with artificially introduced vacancies can help disentangle these contributions. This task focuses on computing the heat capacity of an ideal 6 nm fcc Pd cluster and the mean square displacement of a similar cluster containing 20% vacancies, as a step toward elucidating the relation between atomic mobility, structural integrity, and measured heat capacity.

## Approach
The simulations use the Large-scale Atomic/Molecular Massively Parallel Simulator (LAMMPS) with the tight-binding second-moment approximation (TB-SMA) empirical potential for Pd. A spherical 6 nm diameter Pd cluster with the face-centred cubic (fcc) lattice is constructed. Canonical (NVT) MD runs are performed at two temperatures (150 K and 300 K) using a Nosé-Hoover thermostat; the potential energy fluctuations obtained from these runs are used to compute the isobaric heat capacity via the energy-variance formula. The computed heat capacity is compared against known bulk Pd reference values (15.6 J/(mol·K) at 150 K and 25.9 J/(mol·K) at 300 K) to obtain a percentage increase. In a separate set of runs, 20% of the atoms are randomly removed from the initial cluster to mimic a lower-density sample, and an NVT simulation at 300 K is performed. The atomic trajectory is analysed to calculate the mean square displacement (MSD), which quantifies the extent of atomic rearrangements.

## Reproduction target
The goal is to produce two scored output files: (i) heat_capacity_ideal.csv containing the percentage increase in heat capacity of the ideal 6 nm Pd cluster relative to bulk at 150 K and 300 K, and (ii) msd_vacancy_300K.txt containing the final mean square displacement (in nm²) of the Pd cluster with 20% vacancies after the MD run at 300 K. These quantities characterise the intrinsic thermal properties and atomic mobility of Pd nanoclusters.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://www.lammps.org/
- TB-SMA interatomic potential parameters for Pd (Cleri-Rosato)

## Workflow steps

### Step 1: Run MD simulation of ideal Pd cluster at 150 K and 300 K
- Role: process
- Action: Construct a spherical fcc Pd cluster of 6 nm diameter (approx. 5500-6000 atoms). Perform canonical (NVT) MD simulations using LAMMPS with the TB-SMA potential at temperatures 150 K and 300 K. Output a log file containing potential energy and temperature at each timestep.
- Evidence: `/app/outputs/ideal_md.log`

### Step 2: Compute heat capacity increase for ideal cluster
- Role: scored (load-bearing)
- Action: From the MD energy log (step1), compute the isobaric heat capacity at 150 K and 300 K using the energy fluctuation formula. Calculate the percentage increase relative to the bulk Pd heat capacity (use the provided bulk reference values: 15.6 J/(mol·K) at 150 K and 25.9 J/(mol·K) at 300 K). Write a CSV file with columns temperature_K and heat_capacity_rise_percent.
- Output file: `/app/outputs/heat_capacity_ideal.csv`
- Format: csv
- Contract: CSV with header: temperature_K,heat_capacity_rise_percent. Two data rows: 150 and 300.
- Scoring: scored by hidden verifier

### Step 3: Run MD simulation of Pd cluster with 20% vacancies at 300 K
- Role: process
- Action: Take the same 6 nm ideal fcc Pd cluster, randomly remove 20% of atoms to introduce vacancies. Perform NVT MD simulation at 300 K using the same TB-SMA potential. Output atomic trajectory (dump file) at regular intervals for MSD calculation.
- Evidence: `/app/outputs/vacancy_trajectory.lammpstrj`

### Step 4: Compute mean square displacement for vacancy cluster
- Role: scored (load-bearing)
- Action: From the atomic trajectory (step3), compute the mean square displacement (MSD) of Pd atoms over the MD run. Output the final MSD value (in nm^2) as a single floating-point number.
- Output file: `/app/outputs/msd_vacancy_300K.txt`
- Format: txt
- Contract: A plain text file containing a single floating-point number (e.g., 0.12345) representing MSD in nm^2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/heat_capacity_ideal.csv`
- `/app/outputs/msd_vacancy_300K.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### heat_capacity_ideal.csv
- path: `/app/outputs/heat_capacity_ideal.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Heat capacity increase of an ideal 6 nm Pd cluster relative to bulk Pd at 150 K and 300 K, computed from MD energy fluctuations.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `heat_capacity_rise_percent`
  - `units`:
    - `temperature_K`: kelvin
    - `heat_capacity_rise_percent`: percent

### msd_vacancy_300K.txt
- path: `/app/outputs/msd_vacancy_300K.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Mean square displacement of a 6 nm Pd cluster containing 20% vacancies after MD simulation at 300 K, quantifying atomic mobility.
- schema:
  - `type`: text
  - `units`:
    - `value`: nm^2

Notes: The bulk Pd heat capacity reference values are 15.6 J/(mol K) at 150 K and 25.9 J/(mol K) at 300 K. The agent uses these to compute the rise percent. No further gold values are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "heat_capacity_ideal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "heat_capacity_rise_percent"
        ],
        "units": {
          "temperature_K": "kelvin",
          "heat_capacity_rise_percent": "percent"
        }
      },
      "description": "Heat capacity increase of an ideal 6 nm Pd cluster relative to bulk Pd at 150 K and 300 K, computed from MD energy fluctuations."
    },
    {
      "file": "msd_vacancy_300K.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "units": {
          "value": "nm^2"
        }
      },
      "description": "Mean square displacement of a 6 nm Pd cluster containing 20% vacancies after MD simulation at 300 K, quantifying atomic mobility."
    }
  ],
  "notes": "The bulk Pd heat capacity reference values are 15.6 J/(mol K) at 150 K and 25.9 J/(mol K) at 300 K. The agent uses these to compute the rise percent. No further gold values are provided."
}
```

## How you are scored
A hidden verifier reads the two output files and scores each independently. The heat capacity increase values are compared against a hidden expected range, and the MSD value is checked against a minimum mobility threshold. The final reward is a weighted sum of these two sub-scores; reporting plausible values alone is not sufficient—the numbers must result from correctly executed MD simulations and analysis. The verifier does not access your intermediate logs, only the final scored artifacts.
