# DFT-based prediction of iron pernitride FeN₂ structure and high-pressure synthesis

## Problem background
Iron nitrides are a class of materials studied for their structural and magnetic properties, but no binary iron–nitrogen compound with a nitrogen content exceeding 50 at.% has been experimentally confirmed. Predictions of nitrogen‑rich iron phases are of fundamental interest because pernitride motifs (N₂²⁻ or N₂⁴⁻) can give rise to unusual hardness and magnetism. The present task addresses the first‑principles prediction of a candidate FeN₂ phase and its synthesis conditions. The goal is to computationally identify the most stable crystal structure of FeN₂ at ambient pressure, determine its physical properties (elastic, magnetic, bonding), and estimate the pressure needed to synthesise it at high temperature.

## Approach
The computational strategy is based on spin‑polarised density‑functional theory (DFT) using the generalised‑gradient approximation (PBE functional). An open‑source plane‑wave code (e.g., Quantum ESPRESSO) is used to perform full structural relaxations of multiple candidate FeN₂ arrangements. Starting from several well‑known AB₂ prototype structures (e.g., ThC₂, CaC₂, TiO₂), cells are built that contain either pernitride (N₂⁴⁻ / N₂²⁻) units or isolated N³⁻ ions. All structures are relaxed with respect to volume, shape, and atomic positions to obtain their total energies. The lowest‑energy configuration is selected, and energy–volume data are collected around its equilibrium to fit an equation of state, yielding the bulk modulus and its pressure derivative. The magnetic moment is extracted from the spin‑polarised calculation, and the N–N bond length is measured. To evaluate thermodynamic stability, the total energies of reference phases FeN (zincblende) and α‑N₂ are computed with the same DFT settings, and the formation enthalpy at 0 K is calculated as ΔH = E(FeN₂) – [E(FeN) + 0.5 E(N₂)]. The temperature‑dependent stability is then assessed by combining density‑functional perturbation theory (DFPT) phonon calculations with a classical estimate of the Gibbs free energy of N₂, yielding the relative Gibbs free energy ΔG(P) at 1000 K over a pressure range from 0 to 25 GPa. The pressure where ΔG(P) changes sign is the predicted synthesis pressure.

## Reproduction target
Given the problem setup, your objective is to perform the DFT‑based structure search and property calculations described in “Approach”. You must produce three scored artifacts:

1. The fully relaxed, lowest‑energy FeN₂ crystal structure as a CIF file.
2. A JSON file containing the computed bulk modulus, bulk modulus pressure derivative, magnetic moment, N–N bond length, formation enthalpy at 0 K, lattice parameters a and c, Wyckoff positions, and the N internal z‑parameter.
3. A CSV file containing the relative Gibbs free energy ΔG(P) at 1000 K for pressures from 0 to at least 25 GPa.

The target is not a specific paper figure or table, but the predicted ground‑state FeN₂ phase and its properties obtained from a PBE‑DFT workflow. Your results will be compared against the expected reference values that correspond to a correct re‑execution of the outlined protocol.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- PBE PAW pseudopotentials (SSSP efficiency): https://www.materialscloud.org/discover/sssp
- FeN zincblende reference structure
- α-N2 crystal structure

## Workflow steps

### Step 1: Generate FeN2 candidate structures
- Role: process
- Action: Construct at least 10 candidate FeN2 structures derived from known AB2 prototypes (e.g., ThC2, CaC2, TiO2) with both pernitride (N2²⁻/N2⁴⁻) and dinitride (2×N³⁻) motifs.
- Evidence: `/app/outputs/candidate_structures.txt`

### Step 2: DFT relax and select lowest-energy FeN2
- Role: process
- Action: Perform spin-polarized DFT relaxations (PBE functional, with sufficient cutoff energy and k-point sampling) for all candidate FeN2 cells. For the lowest-energy structure, compute additional energies at volumes around equilibrium to obtain energy–volume points.
- Evidence: `/app/outputs/lowest_energy_relaxation.out`

### Step 3: Compute reference total energies
- Role: process
- Action: Calculate the total energy of FeN (zincblende) and solid α-N2 using the same DFT parameters.
- Evidence: `/app/outputs/reference_energies.json`

### Step 4: Write equilibrium FeN2 CIF
- Role: scored
- Action: Extract the fully relaxed lowest-energy FeN2 structure from the DFT relaxation and save it as a CIF file containing lattice parameters, space group, and fractional coordinates.
- Output file: `/app/outputs/relaxed_structure.cif`
- Format: other
- Contract: CIF with _cell_length_a, _cell_length_b, _cell_length_c, _cell_angle_alpha, _cell_angle_beta, _cell_angle_gamma, _symmetry_space_group_name_H-M, and loop of _atom_site_* fields.
- Scoring: scored by hidden verifier

### Step 5: Compute FeN2 properties
- Role: scored (load-bearing)
- Action: From the data of steps 02 and 03: (a) fit a Murnaghan equation of state to the energy–volume points to obtain bulk modulus and its derivative; (b) extract the magnetic moment from the spin-polarized calculation; (c) compute the N–N bond length; (d) calculate the formation enthalpy at 0 K relative to FeN + 0.5 N2; (e) record lattice parameters a, c, Wyckoff sites, and N z-parameter. Write all results into a JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: {"bulk_modulus_GPa": <number>, "bulk_modulus_derivative": <number>, "magnetic_moment_muB": <number>, "N_N_bond_length_A": <number>, "formation_enthalpy_0K_kJ_mol": <number>, "lattice_a_A": <number>, "lattice_c_A": <number>, "Fe_Wyckoff": "3a", "N_Wyckoff": "6c", "N_z_parameter": <number>}
- Scoring: scored by hidden verifier

### Step 6: Phonon calculations for thermal effects
- Role: process
- Action: Perform density-functional perturbation theory (DFPT) phonon calculations for the lowest-energy FeN2 and for FeN to obtain the vibrational free energies at T=1000 K within the quasi-harmonic approximation.
- Evidence: `/app/outputs/phonon_dos_FeN2.json`

### Step 7: Compute transition pressure at 1000 K
- Role: scored
- Action: Combine the DFT-computed Gibbs free energies of FeN2 and FeN at 1000 K with a classical estimate of the N2 Gibbs free energy to compute ΔG(P) for a set of pressures from 0 to 25 GPa. Write a CSV with columns pressure_GPa and deltaG_kJ_mol. Identify the pressure where ΔG changes sign as the predicted synthesis pressure.
- Output file: `/app/outputs/transition_pressure_1000K.csv`
- Format: csv
- Contract: pressure_GPa (float), deltaG_kJ_mol (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxed_structure.cif`
- `/app/outputs/computed_properties.json`
- `/app/outputs/transition_pressure_1000K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxed_structure.cif
- path: `/app/outputs/relaxed_structure.cif`
- format: other
- purpose: scored
- target_policy: exact_match
- description: CIF file of the DFT-optimized lowest-energy FeN2 crystal structure.
- schema:
  - `type`: text
  - `description`: CIF file; the checker will parse lattice parameters, space group, and fractional coordinates and compare them to hidden reference values within tolerances.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Derived physical properties of FeN2; the checker compares each numeric field to hidden reference values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `bulk_modulus_GPa`: number
    - `bulk_modulus_derivative`: number
    - `magnetic_moment_muB`: number
    - `N_N_bond_length_A`: number
    - `formation_enthalpy_0K_kJ_mol`: number
    - `lattice_a_A`: number
    - `lattice_c_A`: number
    - `Fe_Wyckoff`: string
    - `N_Wyckoff`: string
    - `N_z_parameter`: number
  - `units`:
    - `bulk_modulus_GPa`: GPa
    - `magnetic_moment_muB`: μB
    - `N_N_bond_length_A`: Å
    - `formation_enthalpy_0K_kJ_mol`: kJ/mol
    - `lattice_a_A`: Å
    - `lattice_c_A`: Å

### transition_pressure_1000K.csv
- path: `/app/outputs/transition_pressure_1000K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of pressure (GPa) and relative Gibbs free energy (kJ/mol). The checker interpolates the zero-crossing and compares it to the hidden reference synthesis pressure within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `deltaG_kJ_mol`
  - `units`:
    - `pressure_GPa`: GPa
    - `deltaG_kJ_mol`: kJ/mol

Notes: The hidden checker extracts structural parameters from the CIF and compares the numeric quantities in the JSON and CSV against the paper-reported values using pre-set tolerances. The task requires re-running the entire DFT procedure; no result values are disclosed in the public instructions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxed_structure.cif",
      "format": "other",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "CIF file; the checker will parse lattice parameters, space group, and fractional coordinates and compare them to hidden reference values within tolerances."
      },
      "description": "CIF file of the DFT-optimized lowest-energy FeN2 crystal structure."
    },
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "bulk_modulus_GPa": "number",
          "bulk_modulus_derivative": "number",
          "magnetic_moment_muB": "number",
          "N_N_bond_length_A": "number",
          "formation_enthalpy_0K_kJ_mol": "number",
          "lattice_a_A": "number",
          "lattice_c_A": "number",
          "Fe_Wyckoff": "string",
          "N_Wyckoff": "string",
          "N_z_parameter": "number"
        },
        "units": {
          "bulk_modulus_GPa": "GPa",
          "magnetic_moment_muB": "μB",
          "N_N_bond_length_A": "Å",
          "formation_enthalpy_0K_kJ_mol": "kJ/mol",
          "lattice_a_A": "Å",
          "lattice_c_A": "Å"
        }
      },
      "description": "Derived physical properties of FeN2; the checker compares each numeric field to hidden reference values within tolerances."
    },
    {
      "file": "transition_pressure_1000K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "deltaG_kJ_mol"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "deltaG_kJ_mol": "kJ/mol"
        }
      },
      "description": "Table of pressure (GPa) and relative Gibbs free energy (kJ/mol). The checker interpolates the zero-crossing and compares it to the hidden reference synthesis pressure within a tolerance."
    }
  ],
  "notes": "The hidden checker extracts structural parameters from the CIF and compares the numeric quantities in the JSON and CSV against the paper-reported values using pre-set tolerances. The task requires re-running the entire DFT procedure; no result values are disclosed in the public instructions."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier. For each scored output, the verifier extracts the relevant quantities and compares them to reference values using pre‑set tolerances.

- The CIF file is parsed to obtain lattice constants, space group, atom coordinates, and the shortest N–N distance. Structural parameters are compared individually.
- The computed_properties.json fields are compared to reference numbers for bulk modulus (GPa), magnetic moment (μB), N–N bond length (Å), formation enthalpy (kJ mol⁻¹), and lattice parameters (Å).
- The transition_pressure_1000K.csv is read, and the pressure where the relative Gibbs free energy crosses zero (i.e., becomes favourable) is determined by interpolation. This crossover pressure is compared to the reference synthesis pressure.

Each stage contributes a defined weight to the final reward (0 to 1). You must genuinely run the DFT workflow and produce meaningful output; reporting numbers without executing the pipeline will not succeed because the tolerances are tied to a correct calculation. No paper identity, gold values, or error margins are disclosed.
