# GCMC Binary CO2/H2O Adsorption Isotherms on UiO-66 with Defects

## Problem background
Metal-organic frameworks (MOFs) are promising for gas separations, but understanding how structural defects and co-adsorbed water affect CO2 uptake remains a challenge. This task focuses on the binary adsorption of CO2 and water in UiO-66, a water-stable zirconium-based MOF. Using Grand Canonical Monte Carlo (GCMC) simulations, the effect of two different missing-linker defects on CO2 adsorption is examined under dry conditions and at two levels of water preloading. The goal is to reproduce the simulated CO2 adsorption isotherms for the ideal UiO-66 structure and two defect-containing variants across a low-pressure range (0.2–5 kPa), revealing the interplay between defect chemistry and water co-adsorption on CO2 capacity.

## Approach
The computational approach employs GCMC simulations with the RASPA molecular simulation code. The simulations rely on force fields: UFF for zirconium, DREIDING for other framework atoms, the TIP4P model for water, and TraPPE for CO2. The workflow proceeds in two main stages. First, pure water GCMC simulations are run on the two defect structures (defect‑1 and defect‑2) to achieve prescribed water loadings: a low loading (~1 mol/kg) and an intermediate loading (~4 mol/kg); the ideal UiO-66 structure does not take up water under these conditions and remains dry. These water‑preloaded MOF configurations, together with the dry structures (no water), then serve as fixed hosts for binary CO2 adsorption simulations. For each host, CO2 adsorption isotherms are computed by performing GCMC at 25 °C for a series of CO2 partial pressures from 0.2 to 5 kPa, with the water molecules held fixed. The resulting CO2 loading (mol/kg) as a function of CO2 partial pressure is saved to CSV files, producing seven distinct isotherms that cover all combinations of structure type and water loading.

## Reproduction target
Produce seven CSV isotherm files corresponding to the following conditions (all at 25 °C, CO2 partial pressure 0.2–5 kPa):

- ideal UiO‑66 dry
- defect‑1 dry
- defect‑1 with low water loading (approx. 1.37 mol/kg)
- defect‑1 with intermediate water loading (approx. 4.07 mol/kg)
- defect‑2 dry
- defect‑2 with low water loading (approx. 1.08 mol/kg)
- defect‑2 with intermediate water loading (approx. 4.05 mol/kg)

Each CSV must contain two columns: CO2_pressure_kPa (float) and CO2_loading_mol_kg (float). The required target is to correctly reproduce these isotherms by running the GCMC pipeline as described, without relying on pre-computed data.

## Assets

- RASPA molecular simulation software (version 2): https://github.com/numat/RASPA2
- UiO-66 ideal, defect-1, and defect-2 CIF files with DFT partial charges: 10.1039/C4CC04945D
- UFF force field parameters: RASPA
- DREIDING force field parameters: RASPA
- TIP4P water model parameters: RASPA
- TraPPE CO2 model parameters: RASPA

## Workflow steps

### Step 1: Prepare MOF structures and force field parameters
- Role: process
- Action: Obtain the CIF files for ideal UiO-66, defect-1, and defect-2 with DFT partial charges from Ghosh et al. (DOI:10.1039/C4CC04945D). Assemble all required force field parameters (UFF for Zr, DREIDING for other framework atoms, TIP4P for water, TraPPE for CO2) and prepare simulation input files with appropriate unit‑cell replication.
- Evidence: `/app/outputs/simulation_inputs_ready.txt`

### Step 2: Compute BET surface areas via N2 GCMC
- Role: process
- Action: Perform GCMC simulations of N2 adsorption at 77 K on the three MOF structures using the TraPPE force field. Calculate BET surface areas from the simulated isotherms. This step documents that the structures were correctly simulated and is not part of the scored target.
- Evidence: `/app/outputs/bet_surface_areas.json`

### Step 3: Simulate pure water adsorption to obtain water‑loaded configurations
- Role: process
- Action: Run GCMC simulations of pure water adsorption on defect‑1 and defect‑2 UiO‑66 at 25 °C and pressures that achieve water loadings of approximately 1.37 mol/kg and 4.07 mol/kg for defect‑1, and 1.08 mol/kg and 4.05 mol/kg for defect‑2. Save the MOF‑plus‑water configurations at each target loading. For ideal UiO‑66 no water loading is needed (always dry).
- Evidence: `/app/outputs/water_loading_configurations_saved.txt`

### Step 4: Simulate CO2 on ideal dry UiO‑66
- Role: scored
- Action: Run GCMC simulation of CO2 adsorption on the ideal UiO‑66 structure at 25 °C, dry (no water preloading), with CO2 partial pressures in the range 0.2–5 kPa. Save the resulting isotherm (CO2 loading vs. pressure) as a CSV.
- Output file: `/app/outputs/ideal_dry_isotherm.csv`
- Format: csv
- Contract: table with columns: CO2_pressure_kPa (float), CO2_loading_mol_kg (float)
- Scoring: scored by hidden verifier

### Step 5: Simulate CO2 on defect‑1 dry
- Role: scored
- Action: Run GCMC simulation of CO2 adsorption on the defect‑1 UiO‑66 structure at 25 °C, dry (no water). Save the isotherm as a CSV.
- Output file: `/app/outputs/defect1_dry_isotherm.csv`
- Format: csv
- Contract: table with columns: CO2_pressure_kPa (float), CO2_loading_mol_kg (float)
- Scoring: scored by hidden verifier

### Step 6: Simulate CO2 on defect‑1 low water loading
- Role: scored (load-bearing)
- Action: Run GCMC simulation of CO2 adsorption on defect‑1 preloaded with ~1.37 mol/kg water. Fix water molecules, simulate CO2 at 25 °C, 0.2–5 kPa. Save isotherm CSV.
- Output file: `/app/outputs/defect1_low_water_isotherm.csv`
- Format: csv
- Contract: table with columns: CO2_pressure_kPa (float), CO2_loading_mol_kg (float)
- Scoring: scored by hidden verifier

### Step 7: Simulate CO2 on defect‑1 intermediate water loading
- Role: scored (load-bearing)
- Action: Run GCMC simulation of CO2 adsorption on defect‑1 preloaded with ~4.07 mol/kg water. Fix water, simulate CO2 0.2–5 kPa. Save isotherm CSV.
- Output file: `/app/outputs/defect1_intermediate_water_isotherm.csv`
- Format: csv
- Contract: table with columns: CO2_pressure_kPa (float), CO2_loading_mol_kg (float)
- Scoring: scored by hidden verifier

### Step 8: Simulate CO2 on defect‑2 dry
- Role: scored
- Action: Run GCMC simulation of CO2 adsorption on the defect‑2 UiO‑66 structure at 25 °C, dry. Save isotherm CSV.
- Output file: `/app/outputs/defect2_dry_isotherm.csv`
- Format: csv
- Contract: table with columns: CO2_pressure_kPa (float), CO2_loading_mol_kg (float)
- Scoring: scored by hidden verifier

### Step 9: Simulate CO2 on defect‑2 low water loading
- Role: scored (load-bearing)
- Action: Run GCMC simulation of CO2 adsorption on defect‑2 preloaded with ~1.08 mol/kg water. Fix water, simulate CO2 0.2–5 kPa. Save isotherm CSV.
- Output file: `/app/outputs/defect2_low_water_isotherm.csv`
- Format: csv
- Contract: table with columns: CO2_pressure_kPa (float), CO2_loading_mol_kg (float)
- Scoring: scored by hidden verifier

### Step 10: Simulate CO2 on defect‑2 intermediate water loading
- Role: scored (load-bearing)
- Action: Run GCMC simulation of CO2 adsorption on defect‑2 preloaded with ~4.05 mol/kg water. Fix water, simulate CO2 0.2–5 kPa. Save isotherm CSV.
- Output file: `/app/outputs/defect2_intermediate_water_isotherm.csv`
- Format: csv
- Contract: table with columns: CO2_pressure_kPa (float), CO2_loading_mol_kg (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ideal_dry_isotherm.csv`
- `/app/outputs/defect1_dry_isotherm.csv`
- `/app/outputs/defect1_low_water_isotherm.csv`
- `/app/outputs/defect1_intermediate_water_isotherm.csv`
- `/app/outputs/defect2_dry_isotherm.csv`
- `/app/outputs/defect2_low_water_isotherm.csv`
- `/app/outputs/defect2_intermediate_water_isotherm.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ideal_dry_isotherm.csv
- path: `/app/outputs/ideal_dry_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CO2 adsorption isotherm for ideal UiO‑66 without water.
- schema:
  - `type`: table
  - `required_columns`: `CO2_pressure_kPa`, `CO2_loading_mol_kg`
  - `units`:
    - `CO2_pressure_kPa`: kPa
    - `CO2_loading_mol_kg`: mol/kg

### defect1_dry_isotherm.csv
- path: `/app/outputs/defect1_dry_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Dry defect‑1 CO2 isotherm.
- schema:
  - `type`: table
  - `required_columns`: `CO2_pressure_kPa`, `CO2_loading_mol_kg`
  - `units`:
    - `CO2_pressure_kPa`: kPa
    - `CO2_loading_mol_kg`: mol/kg

### defect1_low_water_isotherm.csv
- path: `/app/outputs/defect1_low_water_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Defect‑1 CO2 isotherm at low water loading (~1.37 mol/kg).
- schema:
  - `type`: table
  - `required_columns`: `CO2_pressure_kPa`, `CO2_loading_mol_kg`
  - `units`:
    - `CO2_pressure_kPa`: kPa
    - `CO2_loading_mol_kg`: mol/kg

### defect1_intermediate_water_isotherm.csv
- path: `/app/outputs/defect1_intermediate_water_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Defect‑1 CO2 isotherm at intermediate water loading (~4.07 mol/kg).
- schema:
  - `type`: table
  - `required_columns`: `CO2_pressure_kPa`, `CO2_loading_mol_kg`
  - `units`:
    - `CO2_pressure_kPa`: kPa
    - `CO2_loading_mol_kg`: mol/kg

### defect2_dry_isotherm.csv
- path: `/app/outputs/defect2_dry_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Dry defect‑2 CO2 isotherm.
- schema:
  - `type`: table
  - `required_columns`: `CO2_pressure_kPa`, `CO2_loading_mol_kg`
  - `units`:
    - `CO2_pressure_kPa`: kPa
    - `CO2_loading_mol_kg`: mol/kg

### defect2_low_water_isotherm.csv
- path: `/app/outputs/defect2_low_water_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Defect‑2 CO2 isotherm at low water loading (~1.08 mol/kg).
- schema:
  - `type`: table
  - `required_columns`: `CO2_pressure_kPa`, `CO2_loading_mol_kg`
  - `units`:
    - `CO2_pressure_kPa`: kPa
    - `CO2_loading_mol_kg`: mol/kg

### defect2_intermediate_water_isotherm.csv
- path: `/app/outputs/defect2_intermediate_water_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Defect‑2 CO2 isotherm at intermediate water loading (~4.05 mol/kg).
- schema:
  - `type`: table
  - `required_columns`: `CO2_pressure_kPa`, `CO2_loading_mol_kg`
  - `units`:
    - `CO2_pressure_kPa`: kPa
    - `CO2_loading_mol_kg`: mol/kg

Notes: Only the GCMC simulation part is reproduced. Experimental adsorption measurements and IAST predictions are excluded. The water preloading step is computationally intensive but feasible. The verifier checks internal consistency; the specific criteria are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ideal_dry_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "CO2_pressure_kPa",
          "CO2_loading_mol_kg"
        ],
        "units": {
          "CO2_pressure_kPa": "kPa",
          "CO2_loading_mol_kg": "mol/kg"
        }
      },
      "description": "CO2 adsorption isotherm for ideal UiO‑66 without water."
    },
    {
      "file": "defect1_dry_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "CO2_pressure_kPa",
          "CO2_loading_mol_kg"
        ],
        "units": {
          "CO2_pressure_kPa": "kPa",
          "CO2_loading_mol_kg": "mol/kg"
        }
      },
      "description": "Dry defect‑1 CO2 isotherm."
    },
    {
      "file": "defect1_low_water_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "CO2_pressure_kPa",
          "CO2_loading_mol_kg"
        ],
        "units": {
          "CO2_pressure_kPa": "kPa",
          "CO2_loading_mol_kg": "mol/kg"
        }
      },
      "description": "Defect‑1 CO2 isotherm at low water loading (~1.37 mol/kg)."
    },
    {
      "file": "defect1_intermediate_water_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "CO2_pressure_kPa",
          "CO2_loading_mol_kg"
        ],
        "units": {
          "CO2_pressure_kPa": "kPa",
          "CO2_loading_mol_kg": "mol/kg"
        }
      },
      "description": "Defect‑1 CO2 isotherm at intermediate water loading (~4.07 mol/kg)."
    },
    {
      "file": "defect2_dry_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "CO2_pressure_kPa",
          "CO2_loading_mol_kg"
        ],
        "units": {
          "CO2_pressure_kPa": "kPa",
          "CO2_loading_mol_kg": "mol/kg"
        }
      },
      "description": "Dry defect‑2 CO2 isotherm."
    },
    {
      "file": "defect2_low_water_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "CO2_pressure_kPa",
          "CO2_loading_mol_kg"
        ],
        "units": {
          "CO2_pressure_kPa": "kPa",
          "CO2_loading_mol_kg": "mol/kg"
        }
      },
      "description": "Defect‑2 CO2 isotherm at low water loading (~1.08 mol/kg)."
    },
    {
      "file": "defect2_intermediate_water_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "CO2_pressure_kPa",
          "CO2_loading_mol_kg"
        ],
        "units": {
          "CO2_pressure_kPa": "kPa",
          "CO2_loading_mol_kg": "mol/kg"
        }
      },
      "description": "Defect‑2 CO2 isotherm at intermediate water loading (~4.05 mol/kg)."
    }
  ],
  "notes": "Only the GCMC simulation part is reproduced. Experimental adsorption measurements and IAST predictions are excluded. The water preloading step is computationally intensive but feasible. The verifier checks internal consistency; the specific criteria are hidden."
}
```

## How you are scored
The submitted isotherm CSVs are evaluated by a hidden verifier. For each isotherm, the verifier reads the (pressure, loading) pairs, interpolates to a common set of CO2 partial pressures, and computes a quantitative error metric between the submitted loadings and the expected values. The verifier also checks for internal consistency among the isotherms. The final reward is based on the quantitative error metric and consistency checks, with a strong emphasis on reproducing the isotherm data correctly. Reporting a plausible number without actually running the GCMC pipeline will not satisfy the verification because the hidden checks include both metric comparison and trend requirements that require self-consistent, physically realistic outputs.
