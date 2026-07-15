# MD and Metadynamics Simulation of Fluoroquinolone Adsorption on COF and CNT@COF Composites

## Problem background
Fluoroquinolone antibiotics (norfloxacin NOR, ofloxacin OFL, pefloxacin PEF) are emerging contaminants in aquatic environments, raising concerns due to their persistence and ecological impact. A promising removal strategy is adsorption onto novel porous materials. This task focuses on the adsorption of these three antibiotic molecules onto two types of substrates: a covalent organic framework (COF) and a COF‑carbon nanotube composite (CNTs@COF). Understanding the nature and strength of the molecular interactions that drive adsorption is essential for evaluating material performance.

## Approach
The work uses classical molecular dynamics (MD) and well‑tempered metadynamics simulations to study adsorption at full atomic detail. The adsorbent model is built from COF building units (condensation of 1,3,5‑triformylbenzene with 2,5‑diethoxyterephthalohydrazide) and, for the composite, carbon nanotubes embedded in the COF. Partial atomic charges are obtained from natural bond orbital (NBO) analysis at the M06-2X/6-31G** level. Force‑field topologies combine the CHARMM36 force field with those charges; antibiotic topologies are obtained via SwissParam.

Six simulation systems are prepared: PEF/COFs, OFL/COFs, NOR/COFs, PEF/CNTs@COFs, OFL/CNTs@COFs, NOR/CNTs@COFs. Each system is equilibrated and a 50 ns production MD run is performed in the NpT ensemble at 298 K. From these trajectories the average van der Waals (Lennard‑Jones) and electrostatic (Coulomb) interaction energies between the antibiotics and the adsorbent are computed, giving the total interaction energy. Separately, for the two systems expected to exhibit the strongest binding (PEF/COF and OFL/CNTs@COF), 50 ns well‑tempered metadynamics simulations are run with the distance between the antibiotic centre of mass and the adsorbent as the collective variable. The bias potential is used to reconstruct the free energy surface and locate the global free energy minimum.

## Reproduction target
Produce two comma‑separated value (CSV) files:

1. `/app/outputs/interaction_energies.csv` — For each of the six systems (PEF/COFs, OFL/COFs, NOR/COFs, PEF/CNTs@COFs, OFL/CNTs@COFs, NOR/CNTs@COFs), report the average van der Waals energy (vdW), the average electrostatic energy (Elec), and the total interaction energy (total), all in kJ/mol. Order the rows consistently.

2. `/app/outputs/free_energy_minima.csv` — For the two metadynamics systems (PEF/COFs and OFL/CNTs@COFs), report the global minimum free energy (free_energy_minimum) in kJ/mol.

The values must correspond to the simulation protocols described; no further analysis beyond these quantities is required.

## Assets

- GROMACS: https://www.gromacs.org/
- PLUMED: https://www.plumed.org/
- CHARMM36 force field: https://www.charmm.org/charmm-force-fields/
- ORCA (or alternative) for NBO charges: https://orcaforum.kofo.mpg.de/
- PubChem entries for NOR, OFL, PEF: https://pubchem.ncbi.nlm.nih.gov/
- COF crystal structure reference: 10.1038/s41467-018-05773-y
- SwissParam web server: https://www.swissparam.ch/
- Packmol: https://m3g.github.io/packmol/

## Workflow steps

### Step 1: Compute NBO partial charges
- Role: process
- Action: Perform quantum chemistry calculations at the M06-2X/6-31G** level of theory to compute Natural Bond Orbital (NBO) partial atomic charges for the COF building units and the three NOP molecules (NOR, OFL, PEF). Use any quantum chemistry package that supports NBO analysis (e.g., ORCA). The resulting charges are required for the MD force field.
- Evidence: `/app/outputs/nbo_charges.txt`

### Step 2: System preparation and force field parameterization
- Role: process
- Action: Build the six simulation systems (PEF/COFs, OFL/COFs, NOR/COFs, PEF/CNTs@COFs, OFL/CNTs@COFs, NOR/CNTs@COFs) using Packmol. Generate GROMACS topology files by combining the CHARMM36 force field with the computed NBO charges, and obtain NOP topologies via SwissParam. Prepare all input files for energy minimization and MD.
- Evidence: `/app/outputs/system_preparation.log`

### Step 3: Classical MD production simulations
- Role: process
- Action: For each of the six systems, run: (i) energy minimization, (ii) 200 ps NVT equilibration, (iii) 500 ps NpT equilibration, and (iv) a 50 ns production MD run. Use GROMACS with a 2 fs time step, 298 K, Parrinello-Rahman barostat, and Nosé-Hoover thermostat.
- Evidence: `/app/outputs/md_simulation.log`

### Step 4: Extract interaction energies from MD trajectories
- Role: scored (load-bearing)
- Action: From the production trajectories, calculate the average van der Waals (LJ) and electrostatic (Coulomb) interaction energies between all NOP molecules and the adsorbent. Compute the total interaction energy as the sum. Write the results to interaction_energies.csv.
- Output file: `/app/outputs/interaction_energies.csv`
- Format: csv
- Contract: columns: system (str), vdW (float, kJ/mol), Elec (float, kJ/mol), total (float, kJ/mol)
- Scoring: scored by hidden verifier

### Step 5: Metadynamics simulations (selected systems)
- Role: process
- Action: For the PEF/COF and OFL/CNTs@COF systems only, run 50 ns well-tempered metadynamics using GROMACS+PLUMED. Use the distance between the NOP center of mass and the adsorbent as the collective variable. Set Gaussian height 1.0 kJ/mol, width 0.25 Å, bias factor 15, and deposit Gaussians every 500 steps.
- Evidence: `/app/outputs/metadynamics.log`

### Step 6: Extract free energy minima from metadynamics
- Role: scored (load-bearing)
- Action: Reconstruct the free energy surface from the metadynamics bias potential and determine the global minimum free energy for each simulated system. Write the results to free_energy_minima.csv.
- Output file: `/app/outputs/free_energy_minima.csv`
- Format: csv
- Contract: columns: system (str), free_energy_minimum (float, kJ/mol)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_energies.csv`
- `/app/outputs/free_energy_minima.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energies.csv
- path: `/app/outputs/interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average van der Waals, electrostatic, and total interaction energies (kJ/mol) for six NOP/adsorbent systems. The hidden checker compares the reported values to hidden reference values and also checks that for every system |vdW| > |Elec|.
- schema:
  - `type`: table
  - `required_columns`: `system`, `vdW`, `Elec`, `total`
  - `units`:
    - `vdW`: kJ/mol
    - `Elec`: kJ/mol
    - `total`: kJ/mol

### free_energy_minima.csv
- path: `/app/outputs/free_energy_minima.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Global free energy minimum (kJ/mol) from metadynamics for the PEF/COF and OFL/CNTs@COF systems. The hidden checker compares to hidden reference values.
- schema:
  - `type`: table
  - `required_columns`: `system`, `free_energy_minimum`
  - `units`:
    - `free_energy_minimum`: kJ/mol

Notes: All energy quantities are in kJ/mol. The six systems for interaction energies are PEF/COFs, OFL/COFs, NOR/COFs, PEF/CNTs@COFs, OFL/CNTs@COFs, NOR/CNTs@COFs. The metadynamics systems are only PEF/COFs and OFL/CNTs@COFs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "vdW",
          "Elec",
          "total"
        ],
        "units": {
          "vdW": "kJ/mol",
          "Elec": "kJ/mol",
          "total": "kJ/mol"
        }
      },
      "description": "Average van der Waals, electrostatic, and total interaction energies (kJ/mol) for six NOP/adsorbent systems. The hidden checker compares the reported values to hidden reference values and also checks that for every system |vdW| > |Elec|."
    },
    {
      "file": "free_energy_minima.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "free_energy_minimum"
        ],
        "units": {
          "free_energy_minimum": "kJ/mol"
        }
      },
      "description": "Global free energy minimum (kJ/mol) from metadynamics for the PEF/COF and OFL/CNTs@COF systems. The hidden checker compares to hidden reference values."
    }
  ],
  "notes": "All energy quantities are in kJ/mol. The six systems for interaction energies are PEF/COFs, OFL/COFs, NOR/COFs, PEF/CNTs@COFs, OFL/CNTs@COFs, NOR/CNTs@COFs. The metadynamics systems are only PEF/COFs and OFL/CNTs@COFs."
}
```

## How you are scored
You will be evaluated by a hidden verifier that reads the two CSV files. The verifier compares your reported interaction energies and free‑energy minima to independently established reference values, allowing tolerances that account for differences in software, implementation choices, and run‑to‑run variability. In addition, the verifier checks that for every system the condition |vdW| > |Elec| holds, reflecting the dominant role of van der Waals interactions. The final score is a weighted sum of partial scores from each artifact; reporting values without having actually performed the required simulations will not satisfy the evaluation, as the tolerances are set to accept only results that are physically consistent with a correctly executed workflow.
