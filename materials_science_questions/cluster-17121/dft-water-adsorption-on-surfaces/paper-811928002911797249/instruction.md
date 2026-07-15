# Molecular Dynamics Study of Ethanol Contamination on CO₂/Water/Calcite Interfacial Properties

## Problem background
This task investigates the effect of ethanol contamination on the interfacial properties of CO₂/water/calcite systems, relevant to geological carbon sequestration. Ethanol is a potential impurity in CO₂ streams from ethanol production facilities, and it may alter the CO₂–water interfacial tension and the wettability of calcite surfaces. The goal is to compute these interfacial properties under subsurface conditions (T=323 K, pressures 5–50 MPa) at various ethanol loadings, providing insight into how impurities could affect trapping mechanisms.

## Approach
The reproduction uses classical molecular dynamics (MD) simulations with GROMACS to model the CO₂/water interface and a water droplet on a calcite surface. The calcite substrate is described by the force field of Xiao et al.; water and CO₂ are modelled by SPC/E and flexible EPM2, respectively; ethanol uses the OPLS-AA force field. Two types of systems are built: (1) a slab geometry with a planar interface to compute CO₂–water interfacial tension (IFT) as a function of pressure and ethanol content, and (2) a cylindrical water droplet on calcite in a CO₂ atmosphere to compute the three-phase contact angle at varying ethanol concentrations. IFT is evaluated from the pressure tensor via the mechanical formula, and contact angles are extracted from 2D water density profiles using a circle-fit procedure. The effect of ethanol is assessed by comparing results across multiple ethanol loadings (0, 100, 200 molecules for IFT; 0, 500, 850, 1200 molecules for contact angle).

## Reproduction target
Produce two result files:

1.  `ift_results.csv` – CO₂–water interfacial tension for ethanol loadings 0, 100, and 200 molecules at pressures 5, 10, 20, 30, 40, and 50 MPa (T=323 K). Columns: `pressure_Mpa` (float), `ethanol_molecules` (integer 0/100/200), `ift_mN_per_m` (float).
2.  `contact_angle_results.csv` – three-phase water‑calcite‑CO₂ contact angles for systems S0 (0 ethanol), S1 (500 ethanol), S2 (850 ethanol), and S3 (1200 ethanol) at 323 K and 20 MPa. Columns: `system` (string `'S0'`/`'S1'`/`'S2'`/`'S3'`), `contact_angle_deg` (float), `std_dev_deg` (float).

Each condition should be the average over the specified replicate simulations.

## Assets

- GROMACS (version 5.1.4): https://www.gromacs.org/
- Calcite force field (Xiao et al.): 10.1021/jp205742a
- Ethanol OPLS-AA force field: 10.1021/ja9621760
- SPC/E water model: gromacs
- Flexible EPM2 CO2 model: 10.1021/jp211508p
- Calcite crystal structure [10-14]

## Workflow steps

### Step 1: System preparation
- Role: process
- Action: Build all initial simulation boxes and topologies for IFT and contact‑angle setups. Generate calcite slab with [10‑14] termination, solvate with water/CO₂/ethanol using the specified force fields (Xiao et al. for calcite, SPC/E water, EPM2 CO₂, OPLS‑AA ethanol). Prepare input files for IFT systems (box 48.57 × 50 × 100 Å³, 3000 H₂O + 2000 CO₂ + 0/100/200 ethanol) and for contact‑angle systems (box 48.57 × 270 × 120 Å³, 4000 H₂O + 14000 CO₂, with ethanol counts 0, 500, 850, 1200).
- Evidence: `/app/outputs/topology_files_list.txt`

### Step 2: IFT simulation
- Role: process
- Action: Run NPT molecular dynamics simulations for IFT systems using GROMACS at T=323 K and pressures 5, 10, 20, 30, 40, 50 MPa for ethanol loadings 0, 100, 200 molecules. Each simulation runs at least 20 ns equilibration + 4 ns production, repeated five times per condition. Use Parrinello‑Rahman barostat (Z‑direction) and Nosé‑Hoover thermostat with separate temperature control for solid and fluid when applicable.
- Evidence: `/app/outputs/ift_simulation_log.txt`

### Step 3: IFT analysis and reporting
- Role: scored (load-bearing)
- Action: Compute interfacial tension from the pressure tensor using the mechanical formula γ = ½ L_z [P_zz − ½(P_xx+P_yy)] over the last 4 ns of each trajectory. Average over replicates. Write results to ift_results.csv with columns pressure_Mpa, ethanol_molecules, ift_mN_per_m.
- Output file: `/app/outputs/ift_results.csv`
- Format: csv
- Contract: Columns: pressure_Mpa (float), ethanol_molecules (int 0/100/200), ift_mN_per_m (float). One row per condition.
- Scoring: scored by hidden verifier

### Step 4: Contact angle simulation
- Role: process
- Action: Run NPT MD simulations of a cylindrical water droplet on calcite in CO₂ atmosphere with ethanol (systems S0–S3: 0, 500, 850, 1200 ethanol) at 323 K and 20 MPa using GROMACS. Each simulation runs 40 ns (after equilibration), repeated three times. Use separate thermostats for solid and fluid.
- Evidence: `/app/outputs/ca_simulation_log.txt`

### Step 5: Contact angle analysis and reporting
- Role: scored (load-bearing)
- Action: Extract the three‑phase contact angle from 2D water oxygen density profiles using a circle‑fit procedure (de Ruijter et al.) for each replicate. Average over replicates and compute standard deviation. Write results to contact_angle_results.csv with columns system, contact_angle_deg, std_dev_deg.
- Output file: `/app/outputs/contact_angle_results.csv`
- Format: csv
- Contract: Columns: system (string 'S0'/'S1'/'S2'/'S3'), contact_angle_deg (float), std_dev_deg (float).
- Scoring: scored by hidden verifier

### Step 6: Force‑field sensitivity simulation
- Role: process
- Action: Repeat the contact angle simulation for system S3 using the calcite force field of Shen et al. (J. Phys. Chem. C 2013, 117, 6904‑6913) instead of Xiao et al. Run one NPT simulation at 323 K and 20 MPa for 40 ns and record the resulting contact angle. This is a qualitative robustness check and not scored.
- Evidence: `/app/outputs/sensitivity_angle.txt`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ift_results.csv`
- `/app/outputs/contact_angle_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ift_results.csv
- path: `/app/outputs/ift_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CO₂/water (and CO₂+ethanol/water) interfacial tension values for pressures 5‑50 MPa and ethanol loadings 0, 100, 200 at T=323 K. The checker compares reported values per condition against hidden paper‑digitized gold with tolerance gates.
- schema:
  - `type`: table
  - `required_columns`: `pressure_Mpa`, `ethanol_molecules`, `ift_mN_per_m`

### contact_angle_results.csv
- path: `/app/outputs/contact_angle_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Three‑phase water‑calcite‑CO₂ contact angles for systems S0–S3 at 323 K and 20 MPa. The checker compares the reported mean angle and standard deviation per system against hidden reference values with tolerance gates.
- schema:
  - `type`: table
  - `required_columns`: `system`, `contact_angle_deg`, `std_dev_deg`

Notes: The checker performs a result‑level comparison: IFT values are compared to digitized gold from the paper with a per‑condition tolerance; contact angle mean and std_dev are checked against paper‑reported ranges. The force‑field sensitivity evidence (sensitivity_angle.txt) is not scored. The scoring is reference_match with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ift_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_Mpa",
          "ethanol_molecules",
          "ift_mN_per_m"
        ]
      },
      "description": "CO₂/water (and CO₂+ethanol/water) interfacial tension values for pressures 5‑50 MPa and ethanol loadings 0, 100, 200 at T=323 K. The checker compares reported values per condition against hidden paper‑digitized gold with tolerance gates."
    },
    {
      "file": "contact_angle_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "contact_angle_deg",
          "std_dev_deg"
        ]
      },
      "description": "Three‑phase water‑calcite‑CO₂ contact angles for systems S0–S3 at 323 K and 20 MPa. The checker compares the reported mean angle and standard deviation per system against hidden reference values with tolerance gates."
    }
  ],
  "notes": "The checker performs a result‑level comparison: IFT values are compared to digitized gold from the paper with a per‑condition tolerance; contact angle mean and std_dev are checked against paper‑reported ranges. The force‑field sensitivity evidence (sensitivity_angle.txt) is not scored. The scoring is reference_match with appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently checks your submitted output files. For `ift_results.csv`, the verifier compares each reported interfacial tension against a hidden reference and awards partial credit proportional to the number of conditions that fall within an allowed tolerance. For `contact_angle_results.csv`, the verifier compares your reported mean contact angle and standard deviation for each system against hidden reference values, again awarding credit when your results are within tolerance. The final score is a weighted combination of these two checks. Reporting numbers that match the expected ranges only after genuinely performing the MD simulations will yield full credit; fabricated or trivial guesses will not meet the tolerance criteria.
