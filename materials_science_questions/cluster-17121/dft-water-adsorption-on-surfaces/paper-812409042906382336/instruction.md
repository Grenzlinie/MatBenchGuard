# Benzene Desorption on a Metal Electrode: Molecular Dynamics Reproduction

## Problem background
Understanding how aromatic molecules adsorb on metal electrodes is important for electrochemistry and biology, as many biomolecules contain aromatic ring structures. This task uses molecular dynamics to investigate the adsorption of benzene on a model metal electrode under two electrolyte conditions: excess Na+ ions or excess Cl- ions. The goal is to determine how the ionic composition of the solution affects the adsorption behavior of benzene, focusing on the density distribution of benzene near the electrode and the electric field across the interface.

## Approach
Simulate two interfacial systems using classical molecular dynamics: System 'Na/Na' contains one benzene molecule, two Na+ ions, and 154 TIP4P water molecules; System 'Cl/Cl' replaces the two Na+ ions with two Cl- ions. Both systems are confined between a metal wall (modeled with image charges) and a 9-3 Lennard-Jones wall in a cubic box of side 1.862 nm. Intermolecular interactions are modelled with Coulomb and Lennard-Jones potentials using OPLS parameters for benzene, TIP4P for water, and published ion parameters; wall interactions are given by a 9-3 potential with specific coefficients. Run NVT simulations at 294 K with a 2 fs timestep: 200 ps equilibration then 800 ps production, treating long-range electrostatics with an image-charge-compatible method. From the production trajectories, compute the benzene centre-of-mass number density profile along the surface normal and the average electric field component in the same direction. Compare these profiles between the Na/Na and Cl/Cl systems to reveal the influence of the electrolyte on benzene adsorption.

## Reproduction target
Produce two CSV artifacts:  
(1) `benzene_density_profiles.csv` containing the binned number density of the benzene centre-of-mass along the z-axis (normal to the walls) for both systems, with columns: `system` ('NaNa' or 'ClCl'), `z_nm` (range -0.931 to +0.931 nm, bin size ~0.01 nm), `density_nm3` (number density in nm⁻³).   
(2) `electric_field_profiles.csv` with the same `system` and `z_nm` columns, and `E_V_per_nm` (electric field z-component in V/nm).  
The profiles must be computed from the full 800 ps production run. The hidden verifier will recompute integrated quantities from these tables and check that they reflect the expected adsorption characteristics when comparing the two electrolyte compositions.

## Assets

- Molecular dynamics simulation package (e.g., LAMMPS): https://github.com/lammps/lammps

## Workflow steps

### Step 1: System preparation
- Role: process
- Action: Construct initial coordinates and simulation input files (force field topology, run parameters) for two systems: System A (benzene + 2 Na+ + 154 TIP4P water) and System B (benzene + 2 Cl- + 154 TIP4P water) inside a cubic box of side 1.862 nm, with a 9-3 LJ wall at one boundary and a metal wall with image charges at the other. Use the force field parameters from Table 1 of the paper: OPLS for benzene, TIP4P for water, ion parameters (σ, ε), and wall parameters C9=17.447e-6 kJ·nm⁹·mol⁻¹, C3=76.144e-3 kJ·nm³·mol⁻¹. All interactions are Coulomb + Lennard-Jones with Lorentz-Berthelot combining rules.
- Evidence: none

### Step 2: Run MD simulations
- Role: process
- Action: For each system, perform a constant-NVT MD simulation at 294 K using a 2 fs time step. Equilibrate for 200 ps, then collect statistics over an 800 ps production run. Treat long-range electrostatics with a method that accounts for the metal wall (e.g., fast multipole method or suitable image-charge-compatible approach). Record atomic trajectories.
- Evidence: none

### Step 3: Benzene density profile
- Role: scored (load-bearing)
- Action: From the production trajectory of each system, compute the number density profile of the benzene center-of-mass along the z-axis (normal to the walls) from z=-0.931 to +0.931 nm in bins of approximately 0.01 nm. Output as CSV.
- Output file: `/app/outputs/benzene_density_profiles.csv`
- Format: csv
- Contract: CSV with columns: system (string, either 'NaNa' or 'ClCl'), z_nm (float, in range [-0.931, 0.931] in steps of ~0.01 nm), density_nm3 (float, number density in nm^{-3}).
- Scoring: scored by hidden verifier

### Step 4: Electric field profile
- Role: scored
- Action: From the production trajectory of each system, compute the average electric field component along the z-axis as a function of z (same binning as above). Output as CSV.
- Output file: `/app/outputs/electric_field_profiles.csv`
- Format: csv
- Contract: CSV with columns: system (string, either 'NaNa' or 'ClCl'), z_nm (float), E_V_per_nm (float, electric field in V/nm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/benzene_density_profiles.csv`
- `/app/outputs/electric_field_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### benzene_density_profiles.csv
- path: `/app/outputs/benzene_density_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Number density profiles of benzene center-of-mass along the surface normal for Na/Na and Cl/Cl systems. The checker will recompute integrated densities from this table to verify the desorption trend.
- schema:
  - `type`: table
  - `required_columns`: `system`, `z_nm`, `density_nm3`
  - `units`:
    - `density_nm3`: nm^{-3}

### electric_field_profiles.csv
- path: `/app/outputs/electric_field_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Average electric field z-component profile for each system. The checker will recompute the field strength at specified positions to verify the unscreened field in the Na/Na system.
- schema:
  - `type`: table
  - `required_columns`: `system`, `z_nm`, `E_V_per_nm`
  - `units`:
    - `E_V_per_nm`: V/nm

Notes: The scored artifacts are the raw profiles; no gold values or tolerances are disclosed. The hidden checker independently recomputes metrics from these profiles.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "benzene_density_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "z_nm",
          "density_nm3"
        ],
        "units": {
          "density_nm3": "nm^{-3}"
        }
      },
      "description": "Number density profiles of benzene center-of-mass along the surface normal for Na/Na and Cl/Cl systems. The checker will recompute integrated densities from this table to verify the desorption trend."
    },
    {
      "file": "electric_field_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "z_nm",
          "E_V_per_nm"
        ],
        "units": {
          "E_V_per_nm": "V/nm"
        }
      },
      "description": "Average electric field z-component profile for each system. The checker will recompute the field strength at specified positions to verify the unscreened field in the Na/Na system."
    }
  ],
  "notes": "The scored artifacts are the raw profiles; no gold values or tolerances are disclosed. The hidden checker independently recomputes metrics from these profiles."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently examines each scored artifact. For the benzene density profiles, it will integrate the density over a specific region near the metal wall for each system and compare the results; for the electric field profiles, it will extract the field strength at a designated position and compare between systems. Each artifact is scored on a 0–1 scale based on how closely the recomputed metrics match the expected behavior (without disclosing the exact reference values). The final reward is a weighted sum of these scores. Note that simply writing numbers that might correspond to the paper is not sufficient; the CSV tables must be fully consistent with the underlying simulation data, and the verifier may perform sanity checks on the data range, binning, and file format. To earn full credit, faithfully execute the simulation protocol and compute the profiles from your trajectories.
