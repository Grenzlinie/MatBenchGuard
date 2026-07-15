# MD tensile testing of graphene-covered silicon nanofilms to extract Young's modulus and ultimate tensile strength

## Problem background
Graphene-covered silicon nanofilms are being explored for nanoscale devices and MEMS/NEMS because they combine the outstanding mechanical stability of graphene with the mature silicon manufacturing base. A key reliability question is how the film's thickness and operating temperature influence its mechanical response under tensile loading. This reproduction task aims to quantify, through molecular dynamics simulations, the effective Young's modulus and ultimate tensile strength of such composite films. The target is to determine whether these properties exhibit a size effect at nanometer thicknesses and how they degrade as temperature rises, thereby mapping the regime where the graphene coating provides the greatest mechanical benefit.

## Approach
We simulate the uniaxial tensile deformation of a graphene monolayer covalently bonded to a Si(100) substrate using classical molecular dynamics. The interatomic forces are described by three complementary potentials: AIREBO for carbon–carbon interactions, an Erhart‑Albe potential for the C–Si interface and the adjacent silicon layer, and the Stillinger‑Weber potential for the remaining silicon atoms. The simulation protocol consists of an equilibration phase in the isothermal‑isobaric ensemble to relax the structure at the target temperature, followed by tensile loading at a constant engineering strain rate in the NVE ensemble with a Nosé‑Hoover thermostat. The tensile stress is computed from the virial expression and averaged over all atoms. From the resulting stress–strain curves we extract Young's modulus (initial elastic slope) and the ultimate tensile strength (maximum stress). The simulation campaign spans a range of silicon film thicknesses and temperatures to capture both the size and thermal effects on the mechanical performance.

## Reproduction target
Construct atomistic models of graphene-covered Si(100) nanofilms with the required interface geometry and inter‑layer covalent bonds. Using LAMMPS and the three interatomic potentials above, run the full tensile simulation protocol for the following conditions: (i) silicon thicknesses of 1, 2, 3, 4, 5, and 6 nm at a fixed temperature of 300 K; (ii) a silicon thickness of 1 nm at temperatures of 200, 300, 500, 700, and 900 K. For every simulation, compute the engineering stress–strain data. Aggregate all raw data points into a single CSV file (`stress_strain_data.csv`). From that file, calculate Young's modulus (linear fit to strain ≤ 0.02) and ultimate tensile strength (global stress maximum) for each condition and store them in `properties_summary.csv`. The hidden verifier will assess whether the produced data exhibit the physically expected dependences on thickness and temperature.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.org/

## Workflow steps

### Step 1: Build atomistic models and LAMMPS input scripts
- Role: process
- Action: Construct atomistic models of graphene-covered Si(100) nanofilms with interface lattice mismatch 5.76% and interfacial covalent bonds C2-Si2, for thicknesses 1–6 nm and temperatures 200–1000 K as per the simulation campaign. Generate corresponding LAMMPS data and input scripts.
- Evidence: `/app/outputs/model_manifest.txt`

### Step 2: Run MD tensile simulations
- Role: process
- Action: For each condition, run LAMMPS: equilibrate for 10 ps in NPT at target temperature, then apply uniaxial tensile loading at strain rate 2e9 s⁻¹ in NVE ensemble with Nose-Hoover thermostat and time step 0.001 ps until failure. Use AIREBO for C-C, Erhart-Albe for C-Si and Si2-Si2, and Stillinger-Weber for Si1-Si1/Si1-Si2 interactions. Output per-atom stress and strain data to dump files.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Generate stress-strain curves
- Role: scored (load-bearing)
- Action: From the LAMMPS dump files, compute the average tensile (virial) stress and engineering strain for each simulation, and aggregate all stress-strain pairs into a single CSV file.
- Output file: `/app/outputs/stress_strain_data.csv`
- Format: csv
- Contract: CSV with columns: thickness_nm (float), temperature_K (float), strain (float), stress_GPa (float). One row per strain value for each simulation condition.
- Scoring: scored by hidden verifier

### Step 4: Extract mechanical properties
- Role: scored
- Action: From stress_strain_data.csv, for each condition compute Young's modulus by linear fit to the initial elastic region (strain < 0.02) and ultimate tensile strength as the maximum stress. Save the extracted values to CSV.
- Output file: `/app/outputs/properties_summary.csv`
- Format: csv
- Contract: CSV with columns: thickness_nm (float), temperature_K (float), young_modulus_GPa (float), ultimate_tensile_strength_GPa (float). One row per condition.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain_data.csv`
- `/app/outputs/properties_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain_data.csv
- path: `/app/outputs/stress_strain_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain data points for all simulated conditions; the checker recomputes Young's modulus and ultimate tensile strength from these and verifies thickness/temperature/shape trends.
- schema:
  - `type`: table
  - `required_columns`: `thickness_nm`, `temperature_K`, `strain`, `stress_GPa`
  - `units`:
    - `thickness_nm`: nm
    - `temperature_K`: K
    - `strain`: dimensionless
    - `stress_GPa`: GPa

### properties_summary.csv
- path: `/app/outputs/properties_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Agent-extracted mechanical properties; the checker compares against its own recomputed values for consistency.
- schema:
  - `type`: table
  - `required_columns`: `thickness_nm`, `temperature_K`, `young_modulus_GPa`, `ultimate_tensile_strength_GPa`
  - `units`:
    - `thickness_nm`: nm
    - `temperature_K`: K
    - `young_modulus_GPa`: GPa
    - `ultimate_tensile_strength_GPa`: GPa

Notes: Only graphene-covered nanofilm simulations under uniaxial tension are reproduced; pristine silicon films and VMD visualization are excluded per task scope. The required simulation conditions are: thicknesses 1,2,3,4,5,6 nm at 300 K, and 1 nm at temperatures 200,300,500,700,900 K.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_nm",
          "temperature_K",
          "strain",
          "stress_GPa"
        ],
        "units": {
          "thickness_nm": "nm",
          "temperature_K": "K",
          "strain": "dimensionless",
          "stress_GPa": "GPa"
        }
      },
      "description": "Stress-strain data points for all simulated conditions; the checker recomputes Young's modulus and ultimate tensile strength from these and verifies thickness/temperature/shape trends."
    },
    {
      "file": "properties_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_nm",
          "temperature_K",
          "young_modulus_GPa",
          "ultimate_tensile_strength_GPa"
        ],
        "units": {
          "thickness_nm": "nm",
          "temperature_K": "K",
          "young_modulus_GPa": "GPa",
          "ultimate_tensile_strength_GPa": "GPa"
        }
      },
      "description": "Agent-extracted mechanical properties; the checker compares against its own recomputed values for consistency."
    }
  ],
  "notes": "Only graphene-covered nanofilm simulations under uniaxial tension are reproduced; pristine silicon films and VMD visualization are excluded per task scope. The required simulation conditions are: thicknesses 1,2,3,4,5,6 nm at 300 K, and 1 nm at temperatures 200,300,500,700,900 K."
}
```

## How you are scored
Your submission is evaluated by an automated hidden checker. The checker first reads `stress_strain_data.csv` and independently recomputes Young's modulus and ultimate tensile strength; it compares these recomputed values to those you report in `properties_summary.csv` for self-consistency. It then evaluates the stress–strain curves and the derived mechanical properties against a set of hidden criteria (e.g., monotonicity, relative magnitudes, curve shape) that reflect the physically meaningful trends of the study. Each scored artifact contributes to the final reward with a pre-defined weight, resulting in a single score between 0 and 1. Achieving a high score requires that your simulation outputs capture the genuine thickness and temperature dependences, not merely that you report specific numerical targets.
