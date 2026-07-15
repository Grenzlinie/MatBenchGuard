# Classical MD Simulation of CNT-Epoxy Resin Wetting and Filling

## Problem background
Carbon nanotubes are promising reinforcements for polymer composites, but poor wetting and weak interfacial bonding limit performance. Understanding the molecular interactions between nanotubes and epoxy resin is essential for processing optimization. Molecular dynamics simulations at the nanoscale can predict the wetting, filling, and wrapping behavior at a given temperature, providing guidance for nanocomposite fabrication. This task investigates the interaction of a single-walled carbon nanotube with an epoxy resin oligomer using classical MD simulations, focusing on the time evolution of the interaction energy and the final molecular dispositions.

## Approach
The study employs classical molecular dynamics simulations with the PCFF force field to investigate the interactions between a single-walled carbon nanotube and an epoxy resin oligomer. Two separate NVT simulations at 300 K are performed: one where the resin is placed near the nanotube opening to study possible entry (filling), and another where the resin is placed near the side to study possible surface wetting (wrapping). From the trajectories, the interaction energy (van der Waals plus electrostatic) between nanotube and resin is extracted as a function of time, and the final atomic configurations are examined to determine the resulting disposition of the resin relative to the nanotube.

## Reproduction target
Produce three outputs: (1) a CSV file of the interaction energy between the whole SWNT and the resin molecule as a function of time for the filling simulation; (2) a CSV file of the interaction energy for the wrapping simulation; (3) a two-frame XYZ file showing the final atomic configurations of both simulations. The verifier will evaluate the interaction energy profiles and the final molecular arrangements from these outputs against hidden criteria.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- Epon 862 resin oligomer chemical structure: https://pubchem.ncbi.nlm.nih.gov/compound/111126
- PCFF force field parameters: lammps-potentials

## Workflow steps

### Step 1: Build SWNT and resin molecular models
- Role: process
- Action: Construct a hydrogen-capped (10,10) armchair single-walled carbon nanotube (SWNT) with 400 carbon atoms, 40 hydrogen atoms, length 9.7 nm, diameter 1.38 nm, C–C bond length 1.42 Å, C–H bond length 1.10 Å. Hydrogen atoms carry charge +0.1268 e, bonded carbon atoms carry –0.1268 e to make the tube neutral. Construct the Epon 862 resin molecule from its SMILES (bisphenol-F diglycidyl ether) and energy-minimise using molecular mechanics to obtain a low-potential-energy conformation approximating 23×9×6 Å. Prepare coordinate files suitable for LAMMPS data inputs.
- Evidence: `/app/outputs/models_data.tar.gz`

### Step 2: Run filling MD simulation (40 ps NVT)
- Role: process
- Action: Set up a LAMMPS simulation with the SWNT and the resin molecule. Place the resin molecule near the open end of the nanotube, oriented along the tube axis. Use the PCFF force field, NVT ensemble at 300 K, timestep 2 fs, total duration 40 ps. Record the total potential energy, per-atom energies (to enable later interaction energy extraction), and the atomic trajectory.
- Evidence: `/app/outputs/filling_trajectory.lammpstrj`

### Step 3: Run wrapping MD simulation (100 ps NVT)
- Role: process
- Action: Set up a LAMMPS simulation with the SWNT and the resin molecule placed near the side of the nanotube (one end close to the wall, the other away). Use the same settings: PCFF force field, NVT at 300 K, 2 fs timestep, total duration 100 ps. Record energy components and save the trajectory.
- Evidence: `/app/outputs/wrapping_trajectory.lammpstrj`

### Step 4: Interaction energy curve – filling
- Role: scored
- Action: From the filling simulation outputs, compute the interaction energy (van der Waals + electrostatic) between the SWNT and the resin molecule at each saved timestep and write a CSV file.
- Output file: `/app/outputs/interaction_energy_filling.csv`
- Format: csv
- Contract: Time series of the interaction energy between the whole SWNT and the resin molecule during the 40 ps filling run. Energy in kcal/mol.
- Scoring: scored by hidden verifier

### Step 5: Interaction energy curve – wrapping
- Role: scored
- Action: From the wrapping simulation outputs, compute the interaction energy (van der Waals + electrostatic) between the SWNT and the resin molecule at each saved timestep and write a CSV file.
- Output file: `/app/outputs/interaction_energy_wrapping.csv`
- Format: csv
- Contract: Time series of the interaction energy between the whole SWNT and the resin molecule during the 100 ps wrapping run. Energy in kcal/mol.
- Scoring: scored by hidden verifier

### Step 6: Final atomic configurations (both simulations)
- Role: scored (load-bearing)
- Action: Extract the last frame from the filling trajectory and the last frame from the wrapping trajectory, and combine them into a single multi-frame XYZ file.
- Output file: `/app/outputs/final_configurations.xyz`
- Format: txt
- Contract: Two-frame XYZ file: first frame shows the final configuration of the filling simulation, second frame the final configuration of the wrapping simulation. All atomic coordinates in Angstroms.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_energy_filling.csv`
- `/app/outputs/interaction_energy_wrapping.csv`
- `/app/outputs/final_configurations.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energy_filling.csv
- path: `/app/outputs/interaction_energy_filling.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Interaction energy (vdW+electrostatic) between the SWNT and resin molecule as a function of time for the filling simulation.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `interaction_energy_kcal_per_mol`
  - `units`:
    - `time_ps`: picosecond
    - `interaction_energy_kcal_per_mol`: kcal/mol

### interaction_energy_wrapping.csv
- path: `/app/outputs/interaction_energy_wrapping.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Interaction energy (vdW+electrostatic) between the SWNT and resin molecule as a function of time for the wrapping simulation.
- schema:
  - `type`: table
  - `required_columns`: `time_ps`, `interaction_energy_kcal_per_mol`
  - `units`:
    - `time_ps`: picosecond
    - `interaction_energy_kcal_per_mol`: kcal/mol

### final_configurations.xyz
- path: `/app/outputs/final_configurations.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Final atomic configurations of both simulations showing the resin inside the nanotube (filling) and wrapped around it (wrapping).
- schema:
  - `type`: text
  - `description`: Two-frame extended XYZ file; first frame: filling final configuration, second frame: wrapping final configuration. Atom symbols and coordinates in angstroms, with optional extra columns ignored.

Notes: The checker will read the two CSV files and compute the decrease in interaction energy (average of initial 2 ps minus average of last 2 ps) and verify the decrease meets a required threshold. The XYZ file will be checked for structural evidence: in the filling frame the resin centre of mass must be inside the nanotube cylinder; in the wrapping frame the resin must be close to the nanotube surface with evidence of wrapping.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_energy_filling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "interaction_energy_kcal_per_mol"
        ],
        "units": {
          "time_ps": "picosecond",
          "interaction_energy_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Interaction energy (vdW+electrostatic) between the SWNT and resin molecule as a function of time for the filling simulation."
    },
    {
      "file": "interaction_energy_wrapping.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_ps",
          "interaction_energy_kcal_per_mol"
        ],
        "units": {
          "time_ps": "picosecond",
          "interaction_energy_kcal_per_mol": "kcal/mol"
        }
      },
      "description": "Interaction energy (vdW+electrostatic) between the SWNT and resin molecule as a function of time for the wrapping simulation."
    },
    {
      "file": "final_configurations.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Two-frame extended XYZ file; first frame: filling final configuration, second frame: wrapping final configuration. Atom symbols and coordinates in angstroms, with optional extra columns ignored."
      },
      "description": "Final atomic configurations of both simulations showing the resin inside the nanotube (filling) and wrapped around it (wrapping)."
    }
  ],
  "notes": "The checker will read the two CSV files and compute the decrease in interaction energy (average of initial 2 ps minus average of last 2 ps) and verify the decrease meets a required threshold. The XYZ file will be checked for structural evidence: in the filling frame the resin centre of mass must be inside the nanotube cylinder; in the wrapping frame the resin must be close to the nanotube surface with evidence of wrapping."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that checks the uploaded CSV files and the XYZ file. For the energy CSV files, it will compute the decrease in interaction energy over the simulation and compare it to required quantitative criteria. For the XYZ file, it will examine the atomic positions to verify that the resin molecule is located inside the nanotube in the filling configuration and wrapped around it in the wrapping configuration. Each output contributes a weighted portion to your final score; scores are awarded for meeting or exceeding the criteria on both energy and structure. Note that simply reporting the paper's numbers without correct simulation trajectories will not yield a passing score.
