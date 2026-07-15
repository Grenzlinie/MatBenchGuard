# Molecular Statics and MD Simulation of Vacancy Diffusion Mechanisms in B2 NiAl

## Problem background
Diffusion in ordered B2 intermetallic compounds like NiAl is more complex than in pure metals because a simple nearest-neighbor (NN) vacancy jump would create anti-site defects and destroy the long-range order. Various cyclic mechanisms that restore order after a series of NN jumps have been hypothesized, including the classic six-jump cycle, but also possible longer cycles. Alternatively, a next-nearest-neighbor (NNN) jump mechanism could maintain order at all times. This investigation aims to determine, through atomistic simulations, which diffusion mechanisms actually operate at high temperature, to compute the activation energies associated with the important jumps, and to obtain the statistical occurrence frequencies of each type of diffusion event.

## Approach
The approach combines molecular statics energy calculations and molecular dynamics (MD) simulations. First, static energy minimizations are used to compute the Ni vacancy formation energy, the migration barrier for a next-nearest-neighbor (NNN) jump, and the highest barrier along a {110} six-jump cycle path for both Ni and Al vacancies. These values provide a basis for comparing the energetic feasibility of NNN jumps versus six-jump cycles. Then, constant-temperature NVT MD simulations are performed on a B2 NiAl supercell containing a single vacancy, using the Farkas embedded-atom method interatomic potential. Separate runs are carried out for a Ni vacancy at 1150 K and 1200 K, and for an Al vacancy at 1100 K and 1150 K, accumulating enough simulation time to obtain sufficient diffusion events for meaningful statistics. The atomic trajectories are recorded and analyzed to identify and classify every completed diffusion event: various types of six-jump cycles (uninterrupted, interrupted, different geometric subtypes), ten-jump cycles, fourteen-jump cycles, failed attempts (where the system returns to its original configuration), and any other events. The percentage occurrence of each event type is computed for each vacancy/temperature condition. The analysis also allows characterizing the detailed sequential coordination of jumps within a cycle and identifying any new cyclic mechanisms that may appear.

## Reproduction target
The reproduction task is to compute, using the Farkas EAM potential and the LAMMPS package, (a) three activation energies from molecular statics: the Ni vacancy formation energy, the Ni vacancy NNN migration energy, and the highest migration barrier of the {110} six-jump cycle for both Ni and Al vacancies; and (b) the statistical frequencies of diffusion events (six-jump cycles, ten-jump cycles, fourteen-jump cycles, failed attempts, and other) for each of the four MD conditions (Ni vacancy at 1150 K and 1200 K; Al vacancy at 1100 K and 1150 K), expressed as percentages of total events. The MD results must also report whether NNN jumps were observed or not. The required outputs are two CSV files: `activation_energies.csv` and `md_event_statistics.csv`, formatted exactly as specified in the workflow steps.

## Assets

- Farkas NiAl EAM interatomic potential: https://www.ctcms.nist.gov/potentials/
- LAMMPS: https://lammps.sandia.gov/

## Workflow steps

### Step 1: Molecular statics activation energy calculations
- Role: scored
- Action: Set up B2 NiAl supercells using the Farkas EAM potential. Perform energy minimizations to compute: Ni vacancy formation energy, migration energy for a NNN jump of a Ni vacancy, and the highest migration barrier for the {110} six-jump cycle for both Ni and Al vacancies. Output the results to activation_energies.csv.
- Output file: `/app/outputs/activation_energies.csv`
- Format: csv
- Contract: CSV with columns: quantity, value_eV. Rows: Ni_vacancy_formation_energy, Ni_vacancy_NNN_migration_energy, six_jump_cycle_peak_barrier_Ni, six_jump_cycle_peak_barrier_Al.
- Scoring: scored by hidden verifier

### Step 2: Molecular dynamics simulations of vacancy diffusion
- Role: process
- Action: Run constant-temperature (NVT) MD simulations using LAMMPS with the Farkas EAM potential for a B2 NiAl block containing a single vacancy. Perform separate runs for a Ni vacancy at 1150 K and 1200 K, and for an Al vacancy at 1100 K and 1150 K. Accumulate total simulation time sufficient to obtain substantial statistics of diffusion events (tens of nanoseconds total). Save atomic trajectories for subsequent analysis.
- Evidence: none

### Step 3: Event classification and statistics
- Role: scored (load-bearing)
- Action: Analyze the saved MD trajectories to identify and classify all diffusion events: six-jump cycles (uninterrupted, interrupted, {110}/{100} subtypes), ten-jump cycles, fourteen-jump cycles, failed attempts, and other. Compute the percentage occurrence of each event type for each vacancy/temperature combination. Also record that NNN jumps were not observed (0%). Output the statistical frequencies to md_event_statistics.csv.
- Output file: `/app/outputs/md_event_statistics.csv`
- Format: csv
- Contract: CSV with columns: vacancy_type, temperature_K, event_specification, percentage, total_percentage. Example: Ni,1150,6-jump_cycles_uninterrupted,42.3,42.3. Include rows for NNN jumps observed (0%).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.csv`
- `/app/outputs/md_event_statistics.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.csv
- path: `/app/outputs/activation_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed activation energies: Ni vacancy formation energy, Ni vacancy NNN migration energy, and the highest migration barriers of the {110} six-jump cycle for Ni and Al vacancies.
- schema:
  - `type`: table
  - `required_columns`: `quantity`, `value_eV`
  - `units`:
    - `value_eV`: eV

### md_event_statistics.csv
- path: `/app/outputs/md_event_statistics.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Statistical occurrence percentages of the various diffusion events observed in the MD simulations for each vacancy type and temperature.
- schema:
  - `type`: table
  - `required_columns`: `vacancy_type`, `temperature_K`, `event_specification`, `percentage`, `total_percentage`
  - `units`:
    - `percentage`: percent
    - `total_percentage`: percent

Notes: The activation energies and event percentages are compared to the paper's reported values with hidden tolerances. The expected unit for energies is eV, and percentages are between 0 and 100.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "quantity",
          "value_eV"
        ],
        "units": {
          "value_eV": "eV"
        }
      },
      "description": "Computed activation energies: Ni vacancy formation energy, Ni vacancy NNN migration energy, and the highest migration barriers of the {110} six-jump cycle for Ni and Al vacancies."
    },
    {
      "file": "md_event_statistics.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "vacancy_type",
          "temperature_K",
          "event_specification",
          "percentage",
          "total_percentage"
        ],
        "units": {
          "percentage": "percent",
          "total_percentage": "percent"
        }
      },
      "description": "Statistical occurrence percentages of the various diffusion events observed in the MD simulations for each vacancy type and temperature."
    }
  ],
  "notes": "The activation energies and event percentages are compared to the paper's reported values with hidden tolerances. The expected unit for energies is eV, and percentages are between 0 and 100."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the two CSV files. For `activation_energies.csv`, the three reported values are each compared to a hidden reference using an absolute tolerance, and a score is computed from how many fall within tolerance. For `md_event_statistics.csv`, the verifier parses all rows, groups by vacancy type and temperature, and compares each event percentage against a hidden reference percentage using an absolute tolerance; it also checks that the NNN jump observation is explicitly reported as 0% (or absent). The final reward is a weighted combination of the scores from the two stages, with the MD statistics stage carrying the larger weight because it depends on the full MD simulation pipeline. Simply copying numbers from the literature without executing the required simulations and analysis will not pass, as the internal consistency and tolerance checks would be violated.
