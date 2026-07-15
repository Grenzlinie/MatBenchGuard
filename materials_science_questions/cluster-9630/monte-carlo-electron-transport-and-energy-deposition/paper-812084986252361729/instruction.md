# Monte Carlo Electron Energy Deposition in a Thin Carbon Target

## Problem background
CVD diamond has been investigated as a thermoluminescent (TL) dosimeter for electrons. Experimentally, samples were irradiated with electron beams at clinical energies (6 MeV and 21 MeV) and the TL glow curve peak area at ~540 K was measured as a function of fluence. Surprisingly, the TL response showed no significant dependence on the electron energy. To understand this observation, detailed calculations of the energy deposited by electrons in the thin diamond sample are needed. The present task reproduces the Monte Carlo simulation part of that study: a 260 μm thick carbon slab (density 3.52 g/cm³) is bombarded with electrons of various incident energies, and the mean energy deposited per primary electron is computed. This deposited energy governs the number of electron-hole pairs generated and therefore the TL response. Your goal is to simulate this process and determine how the deposited energy changes with incident energy, and whether it can explain the observed energy independence.

## Approach
The core of the task is a Geant4 application that transports electrons through a carbon slab. You will implement the following conceptual workflow:
1. Define the target geometry: a 260 μm thick carbon slab (density 3.52 g/cm³) with lateral dimensions large enough to contain the primary beam.
2. Choose a standard electromagnetic physics list (e.g., G4EmStandardPhysics) to model electron interactions and energy deposition.
3. For each incident electron energy in the set 0.1, 0.2, 0.3, 0.5, 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 30, 50, 70, 100 MeV, fire a beam of at least 10⁵ primary electrons normally incident on the slab surface and record the total energy deposited in the slab for each primary.
4. From the per-event deposited energies, compute the mean deposited energy per primary at each incident energy.
5. Compare the mean deposited energies at 6 MeV and 21 MeV by computing the percent difference. This comparison addresses the experimental observation directly.
The simulation output yields a curve of mean deposited energy versus incident energy and a single number—the percent difference at the two clinical energies. All choices of physics list and secondary production cuts are yours; use settings that yield physically reasonable results.

## Reproduction target
Produce two scored artifacts:
- `simulation_results.csv`: a CSV file with columns `incident_energy_MeV` (float) and `mean_deposited_energy_MeV` (float) containing the results for every energy listed above.
- `summary.json`: a JSON file with keys `deposited_energy_6MeV` (float), `deposited_energy_21MeV` (float), and `percent_difference` (float), where `percent_difference = 100 * |E_6 - E_21| / ((E_6 + E_21)/2)`.
The hidden verifier will compare your computed deposited energies and the percent difference against a reference (derived from the original study) and will also inspect the overall shape of the deposited energy curve. Your task is to produce these values by actually running the simulation; the verifier expects the results to be consistent with a correct Geant4 simulation of this system.

## Assets

- Geant4 Monte Carlo Toolkit: https://geant4.org/download.html

## Workflow steps

### Step 1: Set up Geant4 simulation application
- Role: process
- Action: Implement a Geant4 application defining the target geometry (a 260 μm thick carbon slab, density 3.52 g/cm³, lateral dimensions large enough to contain the primary beam), the physics list for electromagnetic processes, and a primary particle generator that fires monoenergetic electrons normally incident on the slab surface. Instrument the sensitive volume to collect the total energy deposited per primary event.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Run Monte Carlo simulation for all incident energies
- Role: process
- Action: Execute the Geant4 simulation for each incident electron energy in the set: 0.1, 0.2, 0.3, 0.5, 1, 2, 3, 4, 5, 6, 7, 10, 15, 20, 30, 50, 70, 100 MeV. Use at least 10^5 primary electrons per energy. Store per-event deposited energies in a temporary checkpoint (e.g., a directory or file) for subsequent analysis.
- Evidence: `/app/outputs/per_event_energies`

### Step 3: Compute mean deposited energies
- Role: scored (load-bearing)
- Action: For each incident energy, compute the mean deposited energy per primary from the stored per-event data. Output a CSV file with columns incident_energy_MeV and mean_deposited_energy_MeV.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: incident_energy_MeV (float), mean_deposited_energy_MeV (float)
- Scoring: scored by hidden verifier

### Step 4: Compute percent difference at 6 and 21 MeV
- Role: scored
- Action: From the mean deposited energies at 6 MeV and 21 MeV (extracted from simulation_results.csv), compute the percent difference as 100 * |E_6 - E_21| / ((E_6 + E_21)/2). Output a JSON file with keys deposited_energy_6MeV, deposited_energy_21MeV, and percent_difference.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: {"deposited_energy_6MeV": float, "deposited_energy_21MeV": float, "percent_difference": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with incident electron energies and the corresponding mean energy deposited per primary electron. The checker compares the values and the overall curve shape to hidden gold values and structural expectations (maximum near 0.35 MeV, gradual increase after 2 MeV).
- schema:
  - `type`: table
  - `required_columns`: `incident_energy_MeV`, `mean_deposited_energy_MeV`
  - `units`:
    - `incident_energy_MeV`: MeV
    - `mean_deposited_energy_MeV`: MeV

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: JSON file containing the mean deposited energies at 6 MeV and 21 MeV and the computed percent difference. The checker will compare the percent_difference against a hidden threshold; a physically plausible result consistent with a correct simulation is expected.
- schema:
  - `type`: object
  - `required`:
    - `deposited_energy_6MeV`: float (MeV)
    - `deposited_energy_21MeV`: float (MeV)
    - `percent_difference`: float (percent)

Notes: The hidden checker performs a reference match on the simulation_results.csv values with tolerances that absorb toolchain differences, and a threshold check on the percent_difference in summary.json. Additionally, the curve shape is audited for a maximum near 0.35 MeV and a slight increase after 2 MeV, but the primary scoring uses the numeric targets.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "incident_energy_MeV",
          "mean_deposited_energy_MeV"
        ],
        "units": {
          "incident_energy_MeV": "MeV",
          "mean_deposited_energy_MeV": "MeV"
        }
      },
      "description": "CSV file with incident electron energies and the corresponding mean energy deposited per primary electron. The checker compares the values and the overall curve shape to hidden gold values and structural expectations (maximum near 0.35 MeV, gradual increase after 2 MeV)."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "deposited_energy_6MeV": "float (MeV)",
          "deposited_energy_21MeV": "float (MeV)",
          "percent_difference": "float (percent)"
        }
      },
      "description": "JSON file containing the mean deposited energies at 6 MeV and 21 MeV and the computed percent difference. The checker will compare the percent_difference against a hidden threshold; a physically plausible result consistent with a correct simulation is expected."
    }
  ],
  "notes": "The hidden checker performs a reference match on the simulation_results.csv values with tolerances that absorb toolchain differences, and a threshold check on the percent_difference in summary.json. Additionally, the curve shape is audited for a maximum near 0.35 MeV and a slight increase after 2 MeV, but the primary scoring uses the numeric targets."
}
```

## How you are scored
Each scored artifact is evaluated independently by a hidden checker, and the total reward is a weighted combination. The checker compares your `simulation_results.csv` entries and the `summary.json` values to reference numbers (hidden) and also verifies that the curve shape is physically plausible. A submission that merely writes the paper's published numbers without actually running the simulation will not score well because the checker requires consistency across all energies and the correct physical trends. The reward ranges from 0 (no resemblance) to 1 (reproduction matches the reference within tolerances).
