# GCMC adsorption of ethanol and water in ZIF-1, -3, -7, -9

## Problem background
Bioethanol is a renewable fuel, but its production by fermentation yields a dilute aqueous solution that must be dehydrated to meet fuel-grade specifications. Membrane-based separation processes such as pervaporation and vapor permeation are energy-efficient alternatives to distillation, and their performance depends critically on the adsorption and diffusion properties of water and ethanol in the membrane material. Zeolitic imidazolate frameworks (ZIFs) are a subclass of metal‑organic frameworks with exceptional thermal and chemical stability, making them attractive candidates for membrane applications. This computational study investigates the adsorption behavior of pure ethanol, pure water, and ethanol‑water mixtures in four representative ZIFs (ZIF‑1, ZIF‑3, ZIF‑7, ZIF‑9) using Grand Canonical Monte Carlo simulations. The objective is to quantify the adsorption loadings and the ethanol‑over‑water selectivity under conditions relevant to membrane separation.

## Approach
The system is modeled at the atomistic level using classical force fields. The ZIF frameworks are treated as rigid and described by the Universal Force Field (UFF) for Lennard‑Jones interactions, with atomic partial charges obtained from periodic density‑functional theory (DFT) calculations using a standard functional and basis set (e.g., B3LYP/6‑31G* with ChelpG population analysis). Ethanol is represented by the united‑atom TraPPE force field, where each CHx group is a single interaction site. Water is modeled with the TIP3P three‑point potential. Grand Canonical Monte Carlo (GCMC) simulations are performed for pure ethanol, pure water, and an equimolar ethanol‑water mixture at 323 K and 373 K over a pressure range of 0–100 kPa. Simulations employ Ewald summation for electrostatics, a Lennard‑Jones cutoff with long‑range corrections, and a rigid‑framework assumption with pretabulated potential grids. From the trajectories, the average molecular loadings are collected to construct adsorption isotherms, and the ethanol‑over‑water selectivity is derived from the mixture uptake data.

## Reproduction target
Produce three tabulated data files:
1. Pure ethanol adsorption isotherms – loading (mmol/g) as a function of pressure (kPa) for each of the four ZIFs at 323 K and 373 K.
2. Pure water adsorption isotherms – loading (mmol/g) versus pressure for the same ZIFs and temperatures.
3. Ethanol/water adsorption selectivity – computed from equimolar mixture simulations at each pressure and temperature.
All data must cover the pressure range 0–100 kPa and be saved in CSV format with the columns specified in the output contract. The verifier will use these files to evaluate the structural consistency of the computed trends.

## Assets

- ZIF-1, -3, -7, -9 crystal structures: https://www.ccdc.cam.ac.uk/structures/ (Cambridge Structural Database) or http://rcsr.net
- UFF force field parameters: 10.1021/ja00051a040
- TraPPE force field for alcohols (united-atom): 10.1021/jp003882x
- TIP3P water model parameters: 10.1063/1.445869
- Open-source GCMC simulation engine (e.g., RASPA2): https://github.com/numat/RASPA2
- Open-source DFT software (ORCA, CP2K, NWChem, etc.): https://orcaforum.kofo.mpg.de/ (ORCA)

## Workflow steps

### Step 1: Obtain ZIF crystal structures
- Role: process
- Action: Retrieve CIF files for ZIF-1, ZIF-3, ZIF-7, and ZIF-9 from public crystallographic databases (e.g., Cambridge Structural Database, rcsr.net). Prepare the periodic unit cell coordinates as required by the GCMC engine.
- Evidence: none

### Step 2: Compute DFT atomic charges
- Role: process
- Action: Perform periodic DFT calculations on each ZIF framework using a standard functional and basis set (e.g., B3LYP/6-31G*) and compute atomic partial charges via ChelpG or similar population analysis. Output the charges in a format ready for force field assignment.
- Evidence: `/app/outputs/dft_charges.log`

### Step 3: Assemble force field parameter files
- Role: process
- Action: Create simulation input files by combining UFF Lennard‑Jones parameters for framework atoms, the computed DFT atomic charges, TraPPE united‑atom parameters for ethanol, and TIP3P parameters for water. Consolidate all force field terms into a format readable by the selected GCMC code.
- Evidence: `/app/outputs/force_field_params.txt`

### Step 4: GCMC simulation of pure ethanol adsorption
- Role: scored (load-bearing)
- Action: Run grand‑canonical Monte Carlo simulations for ethanol in ZIF‑1, ‑3, ‑7, ‑9 at 323 K and 373 K, pressures 0–100 kPa. Use appropriate supercells, rigid framework, LJ cutoff 12 Å with long-range corrections, Ewald summation, and a simulation length of 2×10⁷ moves with the first half for equilibration. Write the resulting adsorption loadings to the output file.
- Output file: `/app/outputs/ethanol_isotherms.csv`
- Format: csv
- Contract: ZIF (string), Temperature (K), Pressure (kPa), Loading (mmol/g)
- Scoring: scored by hidden verifier

### Step 5: GCMC simulation of pure water adsorption
- Role: scored (load-bearing)
- Action: Run GCMC simulations for pure water in the same four ZIFs, temperatures, and pressure range using the TIP3P model. Write the water loading isotherms to the output file.
- Output file: `/app/outputs/water_isotherms.csv`
- Format: csv
- Contract: ZIF (string), Temperature (K), Pressure (kPa), Loading (mmol/g)
- Scoring: scored by hidden verifier

### Step 6: GCMC simulation of ethanol–water mixture
- Role: process
- Action: Run GCMC simulations for an equimolar ethanol/water mixture in the four ZIFs at 323 K and 373 K, pressures 0–100 kPa, using the same force field and simulation parameters. Output the adsorbed amounts of each component.
- Evidence: `/app/outputs/mixture_uptakes.csv`

### Step 7: Calculate adsorption selectivity
- Role: scored (load-bearing)
- Action: From the mixture simulation results, compute the ethanol‑over‑water adsorption selectivity S = (Y_ethanol / Y_water) / (X_ethanol / X_water) with X_ethanol / X_water = 1. Write the selectivity to the output file.
- Output file: `/app/outputs/mixture_selectivity.csv`
- Format: csv
- Contract: ZIF (string), Temperature (K), Pressure (kPa), Selectivity (dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ethanol_isotherms.csv`
- `/app/outputs/water_isotherms.csv`
- `/app/outputs/mixture_selectivity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ethanol_isotherms.csv
- path: `/app/outputs/ethanol_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Absolute ethanol uptake isotherms for ZIF-1, -3, -7, -9.
- schema:
  - `type`: table
  - `required_columns`: `ZIF`, `Temperature (K)`, `Pressure (kPa)`, `Loading (mmol/g)`

### water_isotherms.csv
- path: `/app/outputs/water_isotherms.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Absolute water uptake isotherms for ZIF-1, -3, -7, -9.
- schema:
  - `type`: table
  - `required_columns`: `ZIF`, `Temperature (K)`, `Pressure (kPa)`, `Loading (mmol/g)`

### mixture_selectivity.csv
- path: `/app/outputs/mixture_selectivity.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Ethanol/water adsorption selectivity for the four ZIFs.
- schema:
  - `type`: table
  - `required_columns`: `ZIF`, `Temperature (K)`, `Pressure (kPa)`, `Selectivity`

Notes: Scoring is structural: the checker verifies that the computed isotherms and selectivities obey the paper's reported structural trends (e.g., relative ordering among ZIFs, hydrophobic character of certain ZIFs, selectivity ranking) without requiring an exact numerical match to any reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ethanol_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "ZIF",
          "Temperature (K)",
          "Pressure (kPa)",
          "Loading (mmol/g)"
        ]
      },
      "description": "Absolute ethanol uptake isotherms for ZIF-1, -3, -7, -9."
    },
    {
      "file": "water_isotherms.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "ZIF",
          "Temperature (K)",
          "Pressure (kPa)",
          "Loading (mmol/g)"
        ]
      },
      "description": "Absolute water uptake isotherms for ZIF-1, -3, -7, -9."
    },
    {
      "file": "mixture_selectivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "ZIF",
          "Temperature (K)",
          "Pressure (kPa)",
          "Selectivity"
        ]
      },
      "description": "Ethanol/water adsorption selectivity for the four ZIFs."
    }
  ],
  "notes": "Scoring is structural: the checker verifies that the computed isotherms and selectivities obey the paper's reported structural trends (e.g., relative ordering among ZIFs, hydrophobic character of certain ZIFs, selectivity ranking) without requiring an exact numerical match to any reported values."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier that reads the three scored CSV files. The verifier does not require an exact numerical match to any single value; instead, it checks that your computed results are structurally consistent with the paper's reported trends (e.g., relative ordering of ethanol uptake, hydrophobic/hydrophilic character of certain ZIFs, and selectivity ranking at low pressure). Each structural condition contributes a fixed weight to the final reward; full credit requires all conditions to be satisfied. Reporting the paper's numbers without running the actual workflow will not meet these checks. Execute the protocol faithfully and let the verifier assess the consistency of your results.
