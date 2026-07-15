# Molecular Dynamics Simulation of Biomolecule Adsorption on Metal Surfaces

## Problem background
Understanding how histidine and histidine-containing peptides interact with gold surfaces is critical for designing biosensors, biocompatible coatings, and gold-binding polypeptides. This task investigates the adsorption of histidine (His) and three derived peptides (Gly-His, Gly-His-Gly, Gly-Gly-His) from aqueous solution onto a Au(111) surface. The goal is to compute, through all-atom molecular dynamics simulations, the interaction energies, self-diffusion coefficients, and distance changes between the imidazole's imino nitrogen and the carboxylate group upon adsorption, and to determine whether the amino acid sequence influences these properties.

## Approach
The work uses all-atom molecular dynamics simulations in explicit water. For each of the four molecules, a solution model is built, equilibrated, and simulated to obtain the pre-adsorption conformational ensemble. Then each system is placed against a two-layer Au(111) slab and a longer NVT simulation is performed. From the resulting trajectories, several properties are extracted: (1) the total, van der Waals, and electrostatic interaction energies between the biomolecule and the gold surface, computed from energy-minimized configurations; (2) the self-diffusion coefficients in the plane of the surface (D_xy) and perpendicular to it (D_z), derived from mean-square displacements using the Einstein relation; (3) the average distance between the imino nitrogen of the imidazole ring and the carboxylate oxygen atoms, measured both in pure solution and after adsorption, to quantify adsorption-induced conformational changes. All simulations can be carried out with open-source software (GROMACS) and a public force field (CHARMM36) with gold Lennard-Jones parameters from the literature.

## Reproduction target
Produce the following three scored artifacts for the four systems (His, Gly-His, Gly-His-Gly, Gly-Gly-His): interaction_energies.csv (total, vdW, electrostatic energies in kcal/mol), diffusion_coefficients.csv (D_z and D_xy in 10^-6 cm^2/s), and distance_shift_summary.csv (average imino N–COO distances in solution and adsorbed states, and their difference, in Å). The results are expected to reflect the differences in molecular size and sequence among the four peptides/amino acids.

## Assets

- GROMACS: https://www.gromacs.org
- CHARMM36 force field: https://www.charmm.org/charmm/
- Gold Lennard-Jones parameters (Heinz et al. 2008): https://doi.org/10.1021/jp7119518
- Python analysis libraries: numpy pandas MDAnalysis

## Workflow steps

### Step 1: Build and equilibrate solution models
- Role: process
- Action: For each of the four amino acids/peptides (His, Gly-His, Gly-His-Gly, Gly-Gly-His), generate a topology and build a solution box of explicit water. Energy-minimize and equilibrate to prepare the solution-phase systems.
- Evidence: `/app/outputs/solution_equilibrated.gro`

### Step 2: Run solution-phase MD
- Role: process
- Action: Run solution-phase molecular dynamics for each solution model to generate the baseline conformational ensemble. Save coordinates for later distance analysis.
- Evidence: `/app/outputs/solution_trajectory.xtc`

### Step 3: Build solid-liquid adsorption systems
- Role: process
- Action: Place each equilibrated solution box against a two-layer Au(111) slab with a vacuum layer above. Energy-minimize the combined systems with fixed gold atoms.
- Evidence: `/app/outputs/adsorption_system.gro`

### Step 4: Run adsorption MD
- Role: process
- Action: Run NVT molecular dynamics for each adsorption system. Verify equilibration by monitoring temperature and energy fluctuations. Save coordinates for analysis.
- Evidence: `/app/outputs/adsorption_trajectory.xtc`

### Step 5: Compute interaction energies
- Role: scored
- Action: From equilibrated configurations extracted from the adsorption trajectories, compute the total, van der Waals, and electrostatic interaction energies per amino acid with the Au surface. Write the results to interaction_energies.csv.
- Output file: `/app/outputs/interaction_energies.csv`
- Format: csv
- Contract: Columns: System, TotalEnergy_kcal_mol, vdW_Energy_kcal_mol, Elec_Energy_kcal_mol. One row per system.
- Scoring: scored by hidden verifier

### Step 6: Compute diffusion coefficients
- Role: scored
- Action: From the adsorption trajectories, calculate mean square displacements and extract the self-diffusion coefficients D_z (normal) and D_xy (in-plane) using the Einstein relation. Write the values to diffusion_coefficients.csv.
- Output file: `/app/outputs/diffusion_coefficients.csv`
- Format: csv
- Contract: Columns: System, D_z_cm2_s, D_xy_cm2_s. One row per system.
- Scoring: scored by hidden verifier

### Step 7: Compute imino N–COO distance shift
- Role: scored (load-bearing)
- Action: From the solution and adsorption trajectories, compute the distance between the imino nitrogen of the imidazole ring and the carboxylate oxygen atoms. Extract the average distance in solution, average distance after adsorption, and the shift for each system. Write to distance_shift_summary.csv.
- Output file: `/app/outputs/distance_shift_summary.csv`
- Format: csv
- Contract: Columns: System, AvgDist_Solution_Ang, AvgDist_Adsorbed_Ang, Shift_Ang. One row per system.
- Scoring: scored by hidden verifier

### Step 8: Generate density profiles and snapshots
- Role: process
- Action: From the adsorption trajectories, compute number density profiles along the surface normal for water O, carboxylate O, and imino N, and extract final adsorption snapshots for structural validation.
- Evidence: `/app/outputs/density_profiles.csv and adsorption_snapshots.pdb`

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_energies.csv`
- `/app/outputs/diffusion_coefficients.csv`
- `/app/outputs/distance_shift_summary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energies.csv
- path: `/app/outputs/interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Interaction energies (total, van der Waals, electrostatic) between each amino acid/peptide and the Au(111) surface.
- schema:
  - `type`: table
  - `required_columns`: `System`, `TotalEnergy_kcal_mol`, `vdW_Energy_kcal_mol`, `Elec_Energy_kcal_mol`

### diffusion_coefficients.csv
- path: `/app/outputs/diffusion_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Self-diffusion coefficients in the plane (Dxy) and normal to it (Dz) in 10^-6 cm²/s.
- schema:
  - `type`: table
  - `required_columns`: `System`, `D_z_cm2_s`, `D_xy_cm2_s`

### distance_shift_summary.csv
- path: `/app/outputs/distance_shift_summary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average imino N–COO distances in solution and after adsorption, and the shortening shift, for each sequence.
- schema:
  - `type`: table
  - `required_columns`: `System`, `AvgDist_Solution_Ang`, `AvgDist_Adsorbed_Ang`, `Shift_Ang`

Notes: All CSV files should contain one row per system (His, Gly-His, Gly-His-Gly, Gly-Gly-His). The 'System' column must use these exact names. The shift in distance_shift_summary.csv is defined as AvgDist_Adsorbed - AvgDist_Solution (negative values indicate shortening).

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
          "System",
          "TotalEnergy_kcal_mol",
          "vdW_Energy_kcal_mol",
          "Elec_Energy_kcal_mol"
        ]
      },
      "description": "Interaction energies (total, van der Waals, electrostatic) between each amino acid/peptide and the Au(111) surface."
    },
    {
      "file": "diffusion_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "D_z_cm2_s",
          "D_xy_cm2_s"
        ]
      },
      "description": "Self-diffusion coefficients in the plane (Dxy) and normal to it (Dz) in 10^-6 cm²/s."
    },
    {
      "file": "distance_shift_summary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "System",
          "AvgDist_Solution_Ang",
          "AvgDist_Adsorbed_Ang",
          "Shift_Ang"
        ]
      },
      "description": "Average imino N–COO distances in solution and after adsorption, and the shortening shift, for each sequence."
    }
  ],
  "notes": "All CSV files should contain one row per system (His, Gly-His, Gly-His-Gly, Gly-Gly-His). The 'System' column must use these exact names. The shift in distance_shift_summary.csv is defined as AvgDist_Adsorbed - AvgDist_Solution (negative values indicate shortening)."
}
```

## How you are scored
Your submission will be judged by a hidden verifier. For each scored CSV file, the verifier compares the values you provide to expected reference values (obtained from the original study) and evaluates whether they lie within physically reasonable tolerances. It also checks that the relative ordering of the four systems for each property follows physically consistent trends. The final score is a weighted average of the scores of all three scored artifacts; no partial credit is given for merely running the simulations without producing the required numeric results.
