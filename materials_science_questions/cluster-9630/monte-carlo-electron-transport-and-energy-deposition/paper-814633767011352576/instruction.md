# Monte Carlo electron transmission in silver: cross-section model validation

## Problem background
Predicting how medium-energy electrons travel through thin solid films is important for electron microscopy, surface chemical analysis, and materials characterisation. A key quantity is the transmission probability — the fraction of electrons that pass fully through the film. This task requires you to compute transmission probabilities for electrons on a silver foil using a Monte Carlo transport simulation, comparing predictions from three different models for the elastic scattering cross section against experimental measurements.

## Approach
Implement a single-scattering Monte Carlo simulation of electron transport in silver. Each electron is tracked as it undergoes successive elastic and inelastic collisions until it exits the film or its kinetic energy drops below a 50 eV cutoff. The elastic scattering rates (macroscopic total cross sections) are obtained from three alternative models: (i) a screened Rutherford formula using the Nigam screening parameter (k=5.43), (ii) tabulated total cross sections from the Mayol & Salvat database, and (iii) tabulated total cross sections from the NIST electron elastic-scattering cross-section database. For the Mayol & Salvat and NIST data, fit the cross-section values with a five-parameter log-log polynomial to allow fast interpolation. The inelastic scattering and energy loss are treated via the Liljequist model for the inelastic mean free path and stopping power, combined with the Gryzinski semi-empirical energy-loss expression. Run the simulation for the key condition: 336 keV electrons normally incident on a silver film of mass thickness 55 mg/cm². For each elastic model, compute the transmission probability and write the results to the output CSV.

## Reproduction target
Simulate 10,000 electron trajectories for the condition: 336 keV primary energy, 55 mg/cm² silver film. Perform three separate Monte Carlo runs, each using one of the three elastic scattering cross-section models (Rutherford with Nigam screening, Mayol & Salvat fitted, NIST fitted). For each run, compute the transmission probability (fraction of transmitted electrons). The final required artifact is a CSV file with columns: material (Ag), thickness_mg_cm2 (55.0), energy_keV (336.0), model (Rutherford_Nigam, Mayol_Salvat, or NIST), transmission_probability (float). The file must contain exactly one row per model. The values you report will be compared against a hidden experimental reference measurement for the same silver film and beam energy.

## Assets

- Mayol & Salvat total elastic scattering cross sections: 10.1006/adnd.1997.0745
- NIST Electron Elastic-Scattering Cross-Section Database: https://www.nist.gov/srd/refdata/elasticscattering

## Workflow steps

### Step 1: Prepare cross-section models
- Role: process
- Action: Prepare the macroscopic total elastic scattering cross sections for silver (Ag) as functions of electron kinetic energy from 50 eV to 0.50 MeV. For the Mayol & Salvat and NIST data, fit the five-parameter polynomial (log-log expansion) to represent the cross sections. Implement the screened Rutherford total elastic cross section with Nigam screening parameter k=5.43. Also implement the inelastic scattering cross sections using the Liljequist model for mean free path and stopping power, and the Gryzinski energy-loss expression. Produce internal data structures ready for the Monte Carlo simulation.
- Evidence: `/app/outputs/cross_section_preparation.log`

### Step 2: Simulate electron transmission for key condition
- Role: scored (load-bearing)
- Action: Run a Monte Carlo simulation of 10,000 electrons with kinetic energy 336 keV normally incident on a silver film of mass thickness 55 mg/cm². Use a single-scattering model with three elastic cross-section variants: (i) Rutherford with Nigam screening (k=5.43), (ii) Mayol & Salvat fitted cross section, and (iii) NIST fitted cross section. Track each electron until it is transmitted or its energy falls below 50 eV. For each model, compute the transmission probability (fraction of transmitted electrons). Write the results to a CSV file.
- Output file: `/app/outputs/transmission_probabilities.csv`
- Format: csv
- Contract: CSV with columns: material (string: Ag), thickness_mg_cm2 (float: 55.0), energy_keV (float: 336.0), model (string: Rutherford_Nigam, Mayol_Salvat, NIST), transmission_probability (float). Must contain exactly three rows, one for each model.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transmission_probabilities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transmission_probabilities.csv
- path: `/app/outputs/transmission_probabilities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Agent-supplied transmission probabilities. The hidden checker compares these against a hidden experimental reference value for the same condition using predefined tolerances.
- schema:
  - `type`: table
  - `required_columns`: `material`, `thickness_mg_cm2`, `energy_keV`, `model`, `transmission_probability`
  - `units`:
    - `thickness_mg_cm2`: mg/cm^2
    - `energy_keV`: keV
    - `transmission_probability`: dimensionless probability (0-1)

Notes: Only the single condition (Ag 55 mg/cm², 336 keV) is scored. The agent must compute and report all three model values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transmission_probabilities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "thickness_mg_cm2",
          "energy_keV",
          "model",
          "transmission_probability"
        ],
        "units": {
          "thickness_mg_cm2": "mg/cm^2",
          "energy_keV": "keV",
          "transmission_probability": "dimensionless probability (0-1)"
        }
      },
      "description": "Agent-supplied transmission probabilities. The hidden checker compares these against a hidden experimental reference value for the same condition using predefined tolerances."
    }
  ],
  "notes": "Only the single condition (Ag 55 mg/cm², 336 keV) is scored. The agent must compute and report all three model values."
}
```

## How you are scored
A hidden verifier will examine every workflow artifact and combine the scores into a final reward (0 to 1). The main credit comes from the transmission simulation step. The verifier checks that `transmission_probabilities.csv` is correctly formatted and contains the required rows. It then compares your reported transmission probabilities for each model against a hidden experimental reference value. The comparison allows for the natural run-to-run spread of stochastic Monte Carlo simulations as well as minor implementation differences; no special seed or hyperparameters are enforced. To earn full credit you must genuinely execute the Monte Carlo simulation using the described physical models — simply writing down a known result will not satisfy the output contract.
