# Monte Carlo charged particle transport simulations in GaN and CdSe thin film

## Problem background
When charged particle beams—such as electrons or helium ions—interact with a semiconductor or thin-film structure, they deposit energy in a volume that depends strongly on the particle mass and energy. In imaging and spectroscopy applications, the size and shape of this interaction volume influence the emitted signal and the damage introduced by the beam. A key comparison is between the interaction volumes of 20 keV electrons and 30 keV helium ions in gallium nitride (GaN), and the depth distribution of lattice vacancies created when 30 keV helium ions impinge on a thin cadmium selenide (CdSe) layer on an aluminium substrate. Computing these quantities with Monte Carlo particle-transport simulations provides insight into why some materials luminesce differently under electron and ion excitation.

## Approach
The task uses two open-source Monte Carlo simulation codes: CASINO for electron trajectories and SRIM for ion trajectories. For GaN, run CASINO to simulate 20 keV electrons and SRIM to simulate 30 keV He⁺ ions, both on bulk material. From the stopping positions or energy-deposition data, estimate an interaction volume (e.g., the volume containing 90% of the stopped particles) for each beam, then compute the ratio of the electron volume to the ion volume. Separately, run SRIM for 30 keV He⁺ ions incident on a target comprising a 5.2 nm CdSe layer on an aluminium substrate, simulating 50,000 ions, and extract the depth‑resolved total lattice vacancies and the number of implanted helium ions that come to rest in each depth bin. The entire workflow is implemented as a series of ordered steps: simulate, then process the raw output to produce the two final scored artifacts.

## Reproduction target
The goal is to produce two scored artifacts in the output directory:

- interaction_volume_ratio.json: a JSON file containing a single number, the ratio of the interaction volume of 20 keV electrons in GaN to that of 30 keV He⁺ ions in GaN.
- depth_vacancy_profile.csv: a CSV file with columns depth_nm (nanometres), total_vacancies (integer), he_ions_remaining (integer), giving the depth distribution of radiation damage and implanted ions in a 5.2 nm CdSe layer on an aluminium substrate under 30 keV He⁺ irradiation.

The output must conform to the contracts described in the 'Output contract' section.

## Assets

- SRIM (Stopping and Range of Ions in Matter): http://www.srim.org/
- CASINO (monte CArlo SImulation of electroN trajectory in sOlids): https://www.gel.usherbrooke.ca/casino/

## Workflow steps

### Step 1: Simulate 20 keV electrons in GaN with CASINO
- Role: process
- Action: Use CASINO (or an equivalent Monte Carlo electron‑trajectory code) to simulate 20 keV electrons incident on bulk GaN. Record electron stopping positions or energy deposition data that can be used to estimate the interaction volume. Save the raw output as casino_gan_tracks.txt.
- Evidence: `/app/outputs/casino_gan_tracks.txt`

### Step 2: Simulate 30 keV He ions in GaN with SRIM
- Role: process
- Action: Run SRIM for 30 keV helium ions incident on bulk GaN. Obtain ion stopping positions or energy‑loss profiles to compute the interaction volume. Save the raw output as srim_gan_ions.txt.
- Evidence: `/app/outputs/srim_gan_ions.txt`

### Step 3: Compute electron‑to‑ion interaction volume ratio in GaN
- Role: scored (load-bearing)
- Action: From the CASINO and SRIM outputs for GaN, define a consistent metric of interaction volume (e.g., the volume enclosing 90% of the stopped particles, or a bounding box that contains 90% of the trajectories). Compute the ratio (electron volume / ion volume). Write a JSON file with the ratio.
- Output file: `/app/outputs/interaction_volume_ratio.json`
- Format: json
- Contract: {"ratio": "float", "unit": "dimensionless"}
- Scoring: scored by hidden verifier

### Step 4: Simulate 30 keV He ions in CdSe layer on Al with SRIM
- Role: process
- Action: Run SRIM for 30 keV helium ions incident on a target consisting of a 5.2 nm thick CdSe layer on an aluminum substrate. Simulate 50,000 ions. Save the raw vacancy and ion distribution output as srim_cdse_al_raw.txt.
- Evidence: `/app/outputs/srim_cdse_al_raw.txt`

### Step 5: Generate depth‑dependent vacancy profile for CdSe/Al
- Role: scored (load-bearing)
- Action: From the SRIM output for the CdSe/Al target, extract depth‑resolved total vacancies and remaining helium ions per depth bin. Create a CSV file with columns: depth_nm (depth in nanometers), total_vacancies (total number of lattice vacancies created by all simulated ions in that bin), he_ions_remaining (number of implanted helium ions that come to rest in that bin).
- Output file: `/app/outputs/depth_vacancy_profile.csv`
- Format: csv
- Contract: {"columns": ["depth_nm", "total_vacancies", "he_ions_remaining"], "depth_nm": "float (nm)", "total_vacancies": "int", "he_ions_remaining": "int"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_volume_ratio.json`
- `/app/outputs/depth_vacancy_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_volume_ratio.json
- path: `/app/outputs/interaction_volume_ratio.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Ratio of the interaction volume of 20 keV electrons in GaN to that of 30 keV He+ ions in GaN.
- schema:
  - `ratio`: float
  - `unit`: dimensionless

### depth_vacancy_profile.csv
- path: `/app/outputs/depth_vacancy_profile.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Depth distribution of radiation damage and implanted helium ions in a 5.2 nm CdSe layer on Al under 30 keV He+ irradiation.
- schema:
  - `columns`: `depth_nm`, `total_vacancies`, `he_ions_remaining`
  - `depth_nm`:
    - `type`: float
    - `unit`: nm
  - `total_vacancies`:
    - `type`: int
    - `description`: total lattice vacancies created by simulated ions in that depth bin
  - `he_ions_remaining`:
    - `type`: int
    - `description`: number of implanted helium ions that stop in that depth bin

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_volume_ratio.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "ratio": "float",
        "unit": "dimensionless"
      },
      "description": "Ratio of the interaction volume of 20 keV electrons in GaN to that of 30 keV He+ ions in GaN."
    },
    {
      "file": "depth_vacancy_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "columns": [
          "depth_nm",
          "total_vacancies",
          "he_ions_remaining"
        ],
        "depth_nm": {
          "type": "float",
          "unit": "nm"
        },
        "total_vacancies": {
          "type": "int",
          "description": "total lattice vacancies created by simulated ions in that depth bin"
        },
        "he_ions_remaining": {
          "type": "int",
          "description": "number of implanted helium ions that stop in that depth bin"
        }
      },
      "description": "Depth distribution of radiation damage and implanted helium ions in a 5.2 nm CdSe layer on Al under 30 keV He+ irradiation."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the two scored artifacts and checks them against independently computed reference criteria. The overall score is a weighted combination: the interaction volume ratio is evaluated by determining whether the computed value falls inside an acceptable range derived from the physical expectation; the vacancy profile is checked by several structural audits—including whether the peak of the total vacancy distribution lies in the expected subsurface region and whether the fractions of vacancies and stopped helium ions inside the thin CdSe layer are below expected thresholds. The verifier does not reveal the exact reference numbers or tolerances. Reproducing the correct physics via the simulation steps is essential; simply guessing or hard-coding an answer will not pass the hidden checks.
