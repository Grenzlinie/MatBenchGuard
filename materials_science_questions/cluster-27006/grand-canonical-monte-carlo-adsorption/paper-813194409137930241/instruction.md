# Grand Canonical Monte Carlo Simulation of CO2 Adsorption in a Porous Copper(II) Bis-imidazolate Framework

## Problem background
Efficient capture of carbon dioxide from flue gas or air requires adsorbents that combine high uptake with moderate, reversible binding energy. Porous coordination polymers (PCPs) with open metal sites (OMSs) can provide strong CO₂ binding, but the concentration of OMSs is often limited. A flexible copper(II) bis-imidazolate framework that features planar Cu₂(μ-OH)₂ clusters offers an exceptionally high concentration of Cu(II)-based open metal sites. Grand-canonical Monte Carlo (GCMC) simulations are used to investigate the host–guest interactions, identify the primary adsorption site, and predict the CO₂ adsorption properties of the guest-free (expanded) phase of the framework. This task targets the headline quantities from those simulations: the zero-coverage isosteric heat of adsorption and the CO₂ uptake at ambient pressure.

## Approach
The framework is treated as rigid during the simulation. The crystal structure of the guest-free expanded phase (denoted 1′) is obtained from published supplementary information. The framework atoms are modelled with a standard universal force field (e.g., UFF), and CO₂ is described by a transferable potential (e.g., TraPPE). Grand-canonical Monte Carlo (GCMC) simulations are run at 298 K for a range of pressures up to 1 atm. Each pressure yields an equilibrium uptake, producing a simulated adsorption isotherm. The zero-coverage isosteric heat of adsorption (Q_st) is extracted either by Widom insertion at infinite dilution or from the slope of the Henry’s law region of the isotherm. The CO₂ uptake at exactly 1 atm is read from the simulated isotherm (or interpolated if an exact 1 atm point is not present). The two resulting numbers are reported in simple text files.

## Reproduction target
Reproduce the GCMC simulation results for CO₂ adsorption in the expanded phase (1′) of the copper(II) bis-imidazolate framework at 298 K. Compute (1) the zero-coverage isosteric heat of adsorption (Q_st) in kJ/mol, and (2) the CO₂ uptake at 1 atm in cm³ (STP) per gram of framework. Report each quantity as a single floating-point number in the files specified below.

## Assets

- Crystal structure of the expanded phase 1' (guest-free MAF-35): CCDC 963854 (to be confirmed)
- RASPA (or equivalent GCMC simulation package): https://github.com/numat/RASPA
- Standard force field parameters (e.g., UFF for framework, TraPPE for CO2): RASPA

## Workflow steps

### Step 1: Run GCMC simulation of CO2 in 1'
- Role: process
- Action: Using the crystal structure of the guest-free framework 1' and standard force field parameters (e.g., UFF for framework atoms, TraPPE or similar for CO2), perform grand-canonical Monte Carlo (GCMC) simulations of CO2 adsorption at 298 K for pressures up to 1 atm. Record the simulated uptake at each pressure to produce an isotherm. Save the isotherm data as a CSV file.
- Evidence: `/app/outputs/gcmc_isotherm.csv`

### Step 2: Extract zero-coverage isosteric heat
- Role: scored (load-bearing)
- Action: From the GCMC simulation output, obtain the zero-coverage isosteric heat of adsorption (Q_st) in kJ/mol. This can be computed via Widom insertion or from the slope of the Henry's law region of the isotherm. Write the single numeric value to /app/outputs/zero_coverage_qst.txt.
- Output file: `/app/outputs/zero_coverage_qst.txt`
- Format: txt
- Contract: A single floating-point number.
- Scoring: scored by hidden verifier

### Step 3: Extract CO2 uptake at 1 atm
- Role: scored (load-bearing)
- Action: From the simulated isotherm, determine the CO2 uptake at 298 K and a pressure of 1 atm, expressed in cm³ (STP) per gram of framework. If the simulation did not exactly include 1 atm, interpolate or use the closest data point. Write the single numeric value to /app/outputs/uptake_at_1atm.txt.
- Output file: `/app/outputs/uptake_at_1atm.txt`
- Format: txt
- Contract: A single floating-point number.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zero_coverage_qst.txt`
- `/app/outputs/uptake_at_1atm.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zero_coverage_qst.txt
- path: `/app/outputs/zero_coverage_qst.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Zero-coverage isosteric heat of adsorption of CO2 in the expanded framework 1' at 298 K.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing zero-coverage isosteric heat of adsorption (Q_st) in kJ/mol.

### uptake_at_1atm.txt
- path: `/app/outputs/uptake_at_1atm.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: CO2 uptake from GCMC simulation at 298 K and 1 atm.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing CO2 uptake in cm³ (STP) per gram of framework at 298 K and 1 atm.

Notes: The task reproduces the two headline GCMC simulation results: zero-coverage Q_st and uptake at 1 atm. Both outputs are compared to hidden reference values from the paper with appropriate tolerances. All inputs (crystal structure, force fields, GCMC code) are public.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zero_coverage_qst.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing zero-coverage isosteric heat of adsorption (Q_st) in kJ/mol."
      },
      "description": "Zero-coverage isosteric heat of adsorption of CO2 in the expanded framework 1' at 298 K."
    },
    {
      "file": "uptake_at_1atm.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing CO2 uptake in cm³ (STP) per gram of framework at 298 K and 1 atm."
      },
      "description": "CO2 uptake from GCMC simulation at 298 K and 1 atm."
    }
  ],
  "notes": "The task reproduces the two headline GCMC simulation results: zero-coverage Q_st and uptake at 1 atm. Both outputs are compared to hidden reference values from the paper with appropriate tolerances. All inputs (crystal structure, force fields, GCMC code) are public."
}
```

## How you are scored
After you finish, a hidden verifier reads your output files `/app/outputs/zero_coverage_qst.txt` and `/app/outputs/uptake_at_1atm.txt`. It compares each value to the reference result obtained from the paper’s own GCMC simulation, using prescribed numeric tolerances. Reward is assigned as follows: full credit (1.0) if both values fall within tolerance; partial credit (proportional) if only one is within tolerance; zero credit if neither is within tolerance. The intermediate isotherm (gcmc_isotherm.csv) is required to be produced but is not scored directly; it serves as evidence that the simulation was performed.
