# Lattice Energy Calculations of CoO Polymorphs with Born-Shell Model

## Problem background
Cobalt monoxide (CoO) can crystallise in rock salt, zinc blende, and wurtzite structures. Understanding the relative stability of these polymorphs is essential for predicting which phase forms under given synthesis conditions. This reproduction task uses atomistic lattice energy calculations to investigate the relative stability of the three polymorphs. By applying a Born ionic model with a Dick-Overhauser shell description of polarizability, Buckingham short-range potentials, and an octahedral site preference energy (OSPE) correction, the calculations yield ionic cohesive energies, total lattice energies (including crystal-field effects), equilibrium lattice parameters, and dielectric constants. These computed properties will be used to infer the stability ordering of the polymorphs.

## Approach
The lattice energy simulations are carried out with the open-source General Utility Lattice Program (GULP). The computational setup models CoO as an ionic crystal with formal charges (O²⁻ and Co²⁺). Ionic polarizability is described by the Dick-Overhauser shell model: a massless shell is attached to each ion by a harmonic spring, allowing the shells to displace relative to the cores. Short-range interactions between ions are parameterised with a Buckingham potential. The required potential parameters and shell model constants are taken from Catlow et al. (1977).<br/><br/>The workflow proceeds as follows. Crystal structures for the three target polymorphs — rock salt (Fm-3m), zinc blende (F-43m), and wurtzite (P6₃mc) — are constructed using approximate experimental lattice parameters as initial guesses. GULP is then used to perform geometry optimisation (relaxation of atomic positions and unit cell dimensions) and to compute the resulting ionic cohesive energy, optimised lattice parameters, and dielectric constants. For the tetrahedrally coordinated polymorphs (zinc blende and wurtzite), the octahedral site preference energy (OSPE) of 0.32 eV (Dunitz and Orgel, 1957) is added to the ionic cohesive energy to obtain the total lattice energy; for rock salt (octahedral coordination) the total lattice energy is simply the ionic cohesive energy. The final quantities are parsed from the GULP output files and assembled into a single scored CSV table.

## Reproduction target
Run atomistic lattice energy calculations for the rock salt, zinc blende, and wurtzite CoO polymorphs using GULP with the shell model and Buckingham potentials. Compute the ionic cohesive energy, total lattice energy (ionic + OSPE for tetrahedral structures), equilibrium lattice parameters a and c, and the static and high-frequency dielectric constants. Collect the results in a CSV file, `/app/outputs/computed_properties.csv`, with one row per polymorph and columns: structure, ionic_cohesive_energy_eV, total_lattice_energy_eV, lattice_parameter_a_nm, lattice_parameter_c_nm, dielectric_eps0, dielectric_epsinf, eps0_11, eps0_33, epinf_11, epinf_33. The computed numbers must be derived from your own GULP simulations; do not simply copy-paste values from any pre‑existing source.

## Assets

- GULP (General Utility Lattice Program): https://github.com/ProjectGULP/gulp
- Buckingham potential parameters for CoO from Catlow et al. (1977): 10.1080/14786437708232964
- OSPE value for Co2+ from Dunitz and Orgel (1957): 10.1016/0022-3697(57)90001-X

## Workflow steps

### Step 1: Prepare GULP input files
- Role: process
- Action: Create GULP input files (.gin) for rock salt (Fm-3m), zinc blende (F-43m), and wurtzite (P6_3mc) CoO. Incorporate initial lattice parameters from known experimental values (a=0.4267 nm rock salt, a=0.455 nm zinc blende, a=0.321 nm c=0.524 nm wurtzite), shell model charges, and Buckingham short-range parameters from Catlow et al. (1977). Set up geometry optimization and property calculation keywords.
- Evidence: `/app/outputs/gulp_input_files.txt`

### Step 2: Run GULP simulations
- Role: process
- Action: Execute GULP with each input file to optimize geometry and compute energies, lattice parameters, and dielectric constants. Save the standard output/log files for post-processing.
- Evidence: none

### Step 3: Compile computed properties into CSV
- Role: scored (load-bearing)
- Action: Parse the GULP output log files to extract the final ionic cohesive energy, equilibrium lattice constants a (and c for wurtzite), and static/high-frequency dielectric constants. For zinc blende and wurtzite, add the octahedral site preference energy (OSPE, 0.32 eV) to the ionic cohesive energy to obtain total lattice energy. For rock salt, total lattice energy equals ionic cohesive energy. Write a single CSV file computed_properties.csv with one row per polymorph.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: structure (string), ionic_cohesive_energy_eV (float), total_lattice_energy_eV (float), lattice_parameter_a_nm (float), lattice_parameter_c_nm (float or 'NA'), dielectric_eps0 (float or 'NA'), dielectric_epsinf (float or 'NA'), eps0_11 (float or 'NA'), eps0_33 (float or 'NA'), epinf_11 (float or 'NA'), epinf_33 (float or 'NA')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The checker compares lattice parameters to experimental references (within 1%), ionic and total lattice energies to paper-calculated references (within 0.1 eV), dielectric constants to experimental/paper-calculated references (within 10%), and verifies the stability ordering of total lattice energies.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `ionic_cohesive_energy_eV`, `total_lattice_energy_eV`, `lattice_parameter_a_nm`, `lattice_parameter_c_nm`, `dielectric_eps0`, `dielectric_epsinf`, `eps0_11`, `eps0_33`, `epinf_11`, `epinf_33`
  - `units`:
    - `ionic_cohesive_energy_eV`: eV
    - `total_lattice_energy_eV`: eV
    - `lattice_parameter_a_nm`: nm
    - `lattice_parameter_c_nm`: nm
    - `dielectric_eps0`: dimensionless
    - `dielectric_epsinf`: dimensionless
    - `eps0_11`: dimensionless
    - `eps0_33`: dimensionless
    - `epinf_11`: dimensionless
    - `epinf_33`: dimensionless

Notes: The solver must extract potential parameters from the Catlow et al. (1977) paper and apply the OSPE addition correctly. The checker uses hidden gold values derived from Table I and experimental references; no network fetch is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "ionic_cohesive_energy_eV",
          "total_lattice_energy_eV",
          "lattice_parameter_a_nm",
          "lattice_parameter_c_nm",
          "dielectric_eps0",
          "dielectric_epsinf",
          "eps0_11",
          "eps0_33",
          "epinf_11",
          "epinf_33"
        ],
        "units": {
          "ionic_cohesive_energy_eV": "eV",
          "total_lattice_energy_eV": "eV",
          "lattice_parameter_a_nm": "nm",
          "lattice_parameter_c_nm": "nm",
          "dielectric_eps0": "dimensionless",
          "dielectric_epsinf": "dimensionless",
          "eps0_11": "dimensionless",
          "eps0_33": "dimensionless",
          "epinf_11": "dimensionless",
          "epinf_33": "dimensionless"
        }
      },
      "description": "The checker compares lattice parameters to experimental references (within 1%), ionic and total lattice energies to paper-calculated references (within 0.1 eV), dielectric constants to experimental/paper-calculated references (within 10%), and verifies the stability ordering of total lattice energies."
    }
  ],
  "notes": "The solver must extract potential parameters from the Catlow et al. (1977) paper and apply the OSPE addition correctly. The checker uses hidden gold values derived from Table I and experimental references; no network fetch is required."
}
```

## How you are scored
A hidden verifier inspects your `/app/outputs/computed_properties.csv`. The verifier compares your computed numeric values against independent reference values (experimental measurements and published calculations) within hidden tolerances. Specifically, it checks that your optimised lattice parameters agree with experiment, that your ionic and total lattice energies match reference values, and that your dielectric constants are consistent with reference data. It also verifies that you correctly applied the OSPE addition rule (total_lattice_energy = ionic_cohesive_energy + 0.32 eV for tetrahedral structures, no addition for rock salt) and that the stability ordering implied by your total lattice energies follows the expected trend. Full credit is awarded when your values are correct within the prescribed tolerances; partial credit is given when some values deviate. The verifier does not reward manual copying of numbers from any source — you must produce the CSV as the genuine output of your GULP simulations.
