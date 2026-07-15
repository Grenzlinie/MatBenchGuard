# MD Simulation of Nanocrystalline Fe-Cr-Ni Alloys: Influence of Grain Size and Temperature on Mechanical Properties

## Problem background
Nanocrystalline austenitic stainless steels exhibit a strong dependence of mechanical properties on grain size. Understanding how yield strength, tensile strength, and Young's modulus change as grains shrink from tens of nanometers down to a few nanometers is critical for designing high-strength materials. A central open question is the transition from conventional Hall–Petch strengthening (strength increases with decreasing grain size) to inverse Hall–Petch softening (strength decreases with decreasing grain size) and the location of the critical grain size separating these two regimes. Additionally, the role of temperature in modifying these properties and the underlying deformation mechanisms (grain boundary sliding, dislocation activity, twinning) remains an active area of investigation. The goal is to compute these mechanical properties for nanocrystalline Fe-17Cr-12Ni (wt.%) under uniaxial tension across a range of grain sizes and temperatures, and to determine how yield strength scales with grain size and temperature.

## Approach
The study uses classical molecular dynamics (MD) simulations to model the mechanical response of nanocrystalline Fe-Cr-Ni (316L composition) polycrystals. Polycrystalline atomic configurations are generated via a Voronoi construction that fills a cubic simulation box with randomly oriented grains of a specified average size. The interatomic interactions are described by an embedded-atom method (EAM) potential for the Fe-Ni-Cr system. The workflow consists of three phases: (i) building samples with six different average grain sizes; (ii) energy minimization followed by isobaric-isothermal (NPT) equilibration at the target temperature and near-zero pressure; and (iii) uniaxial tensile deformation along one axis at a high constant strain rate while recording stress and strain. The grain-size study is performed at a single reference temperature, and the temperature dependence is probed for the smallest grain size by repeating the relaxation and deformation at several temperatures. From the resulting stress–strain curves, the Young's modulus (initial elastic slope), yield strength (0.2% offset), and ultimate tensile strength (maximum stress) are extracted.

## Reproduction target
Produce a single CSV file containing the computed mechanical properties. For the six average grain sizes (2.5, 3.6, 4.1, 7.7, 9.9, 11.5 nm), compute the yield strength, ultimate tensile strength, and Young's modulus at 300 K. Additionally, for the 2.5 nm sample, repeat the calculation at temperatures of 10 K, 100 K, 600 K, and 900 K. Compile all results into exactly 10 rows with these columns: grain size (in nm), temperature (in K), yield strength (in GPa), tensile strength (in GPa), and Young's modulus (in GPa). The output must be written to `/app/outputs/step_01_mechanical_properties.csv`.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org/download.html
- Atomsk polycrystal generation tool: https://atomsk.univ-lille.fr/download.html
- Zhou et al. Fe-Ni-Cr EAM potential: 10.1002/jcc.25043
- OVITO visualization software: https://www.ovito.org/download

## Workflow steps

### Step 1: Build polycrystalline samples
- Role: process
- Action: Using Atomsk and the Voronoi construction method, generate LAMMPS data files for nanocrystalline Fe-17Cr-12Ni (wt.%) with average grain sizes 2.5, 3.6, 4.1, 7.7, 9.9, 11.5 nm. Each sample is a cubic box of side 200 Å. The Zhou EAM potential is used to assign atomic species.
- Evidence: `/app/outputs/generated_data_files.log`

### Step 2: Energy minimization and NPT relaxation
- Role: process
- Action: For each configuration, run LAMMPS: first a conjugate‑gradient energy minimization, then an NPT relaxation at 0 bar and the target temperature for 200 ps with a 2 fs timestep, using the Zhou EAM potential. For the grain-size study set temperature 300 K; for the 2.5 nm sample also relax at 10, 100, 600, 900 K. Save the relaxed atomic configurations.
- Evidence: none

### Step 3: Uniaxial tensile deformation simulations
- Role: process
- Action: Starting from each relaxed state, perform uniaxial tensile deformation along the x‑axis at a constant strain rate of 1.0×10^10 s⁻¹. Record the stress tensor components and strain (thermo output). For the 2.5 nm sample, run at all five temperatures (10, 100, 300, 600, 900 K); for other grain sizes run at 300 K.
- Evidence: none

### Step 4: Extract mechanical properties into CSV
- Role: scored (load-bearing)
- Action: From the stress‑strain data of each simulation, compute the Young's modulus (slope of the initial linear elastic region), the yield strength using the 0.2% offset method, and the ultimate tensile strength (maximum stress). Compile all results into a single CSV file with columns: grain_size_nm, temperature_K, yield_strength_GPa, tensile_strength_GPa, youngs_modulus_GPa. The file must contain 10 rows: one for each of the six grain sizes at 300 K, and for the 2.5 nm sample at 10, 100, 600, and 900 K (the 300 K row for 2.5 nm is already covered).
- Output file: `/app/outputs/step_01_mechanical_properties.csv`
- Format: csv
- Contract: Columns: grain_size_nm (float), temperature_K (int), yield_strength_GPa (float), tensile_strength_GPa (float), youngs_modulus_GPa (float). Exactly 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mechanical_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mechanical_properties.csv
- path: `/app/outputs/step_01_mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed mechanical properties. Each cell will be compared to the paper-reported values with tolerances (threshold or better for directional metrics), and the critical grain size trend (yield strength maximum at 7.7 nm, monotonic on both sides) will be verified.
- schema:
  - `type`: table
  - `required_columns`: `grain_size_nm`, `temperature_K`, `yield_strength_GPa`, `tensile_strength_GPa`, `youngs_modulus_GPa`
  - `units`:
    - `grain_size_nm`: nm
    - `temperature_K`: K
    - `yield_strength_GPa`: GPa
    - `tensile_strength_GPa`: GPa
    - `youngs_modulus_GPa`: GPa

Notes: The output table summarizes yield strength, tensile strength, and Young's modulus for six grain sizes at 300 K and temperature-dependent data for the 2.5 nm sample. The hidden checker compares these values to paper-reported references with tolerances, and additionally checks the Hall–Petch / inverse Hall–Petch trend (peak at 7.7 nm, monotonic decrease on both sides) and the monotonic decrease of yield strength and Young's modulus with temperature for the 2.5 nm sample.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "grain_size_nm",
          "temperature_K",
          "yield_strength_GPa",
          "tensile_strength_GPa",
          "youngs_modulus_GPa"
        ],
        "units": {
          "grain_size_nm": "nm",
          "temperature_K": "K",
          "yield_strength_GPa": "GPa",
          "tensile_strength_GPa": "GPa",
          "youngs_modulus_GPa": "GPa"
        }
      },
      "description": "Computed mechanical properties. Each cell will be compared to the paper-reported values with tolerances (threshold or better for directional metrics), and the critical grain size trend (yield strength maximum at 7.7 nm, monotonic on both sides) will be verified."
    }
  ],
  "notes": "The output table summarizes yield strength, tensile strength, and Young's modulus for six grain sizes at 300 K and temperature-dependent data for the 2.5 nm sample. The hidden checker compares these values to paper-reported references with tolerances, and additionally checks the Hall–Petch / inverse Hall–Petch trend (peak at 7.7 nm, monotonic decrease on both sides) and the monotonic decrease of yield strength and Young's modulus with temperature for the 2.5 nm sample."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that examines the produced CSV file. The verifier checks each reported mechanical property value against independently derived expected numbers for the same grain size and temperature conditions. It uses tolerances appropriate for the expected run-to-run spread of classical MD simulations with different implementations. Correctness is assessed per value: meeting or exceeding the threshold earns full credit, and reward decreases as the value deviates further from the expectation. Additionally, the verifier inspects structural trends: the yield strength at 300 K must exhibit a maximum at a particular grain size (the Hall–Petch to inverse Hall–Petch transition), with monotonic behavior on either side, and for the 2.5 nm sample the verifier inspects the temperature dependence of the yield strength and Young's modulus. Each correct value and correctly reproduced trend contributes to a total reward between 0 and 1. The verifier does not disclose its internal gold values or tolerances; your task is to faithfully execute the MD pipeline and extract the properties as specified.
