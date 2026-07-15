# MD Simulation of Organic Solvent Sorption on Crystalline Syndiotactic Polystyrene

## Problem background
Syndiotactic polystyrene (s-PS) can crystallize into a δe form containing an ordered network of molecular cavities. These cavities can selectively host small solvent molecules, making the material a candidate for high-performance separation membranes. For membrane design it is essential to understand how solvent molecules are absorbed from a liquid phase into the crystal, and whether this sorption depends on the crystal face exposed. The present task uses molecular dynamics (MD) simulations to investigate the interface between organic liquids (benzene and chloroform) and the δe crystal of s-PS. The simulation needs to provide the density and lattice constants of the relaxed single crystal, and to determine on which crystal faces solvent molecules enter the cavities and whether the solvent type affects the level of absorption.

## Approach
The reproduction follows a classical all‑atom MD workflow applied to a polymer crystal/liquid interface. First, build a single‑crystal model of the δe form from the published X‑ray fractional coordinates (space group P2₁/a, main chain TTGG conformation), replicate the unit cell with factors 3×4×6, and apply periodic boundary conditions. Use the AMBER force field for bonded and non‑bonded interactions of s‑PS, and obtain compatible parameters for benzene and chloroform from the open literature. Equilibrate the crystal at 300 K and ambient pressure with SHAKE constraints on bonds, a 14 Å non‑bonded cutoff, a Nosé thermostat, and a Parrinello–Rahman barostat. From the production trajectory compute the time‑averaged density and lattice parameters. Next, create four two‑phase interface models by elongating the crystal cell along either the a‑axis (giving the (100) interface) or the b‑axis (giving the (010) interface) and filling the void with 576 randomly oriented solvent molecules (benzene or chloroform). Run NPT molecular dynamics for each interface model at 300 K, keeping cell angles fixed to the average values obtained for the single crystal. Analyze the production trajectories of the four interface models by counting the number of solvent molecules that penetrate the first‑layer cavities of the crystal. The comparison of interest is between the two crystal faces ((100) vs. (010)) and between the two solvents (benzene vs. chloroform).

## Reproduction target
1. Single‑crystal validation: After the equilibration and production run of the δe crystal, report the time‑averaged mass density (g/cm³), the edge lengths a, b, c (Å), and the cell angles α, β, γ (degrees) in a JSON file.   
2. Solvent‑sorption assessment: For each of the four interface models — (100)–benzene, (100)–chloroform, (010)–benzene, (010)–chloroform — count how many solvent molecules have entered the crystal cavities during the production run. Write the results as a CSV table with columns `interface`, `solvent`, and `count`. From these counts it must be possible to infer (a) whether absorption occurs on the (100) face, (b) whether absorption occurs on the (010) face, and (c) whether chloroform is absorbed more readily than benzene on the (100) face.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- AMBER force field parameters for s-PS, benzene, and chloroform
- Experimental crystal structure of δe s-PS: 10.1021/ma9617763

## Workflow steps

### Step 1: Assemble force field parameters
- Role: process
- Action: Gather bonded and non-bonded force field parameters for syndiotactic polystyrene, benzene, and chloroform from public literature (AMBER force field). Obtain parameters for s-PS from reference [11], and for solvents from references [19,22,21] of the paper. The required parameters include atomic charges, Lennard-Jones σ and ε, bond lengths, angles, torsions, and improper torsions. Assemble into a LAMMPS-compatible format.
- Evidence: `/app/outputs/forcefield_parameters.lammps`

### Step 2: Construct single crystal model
- Role: process
- Action: Build the initial atomic configuration of the δe form crystal of s-PS using the experimental fractional coordinates from de Rosa et al. (Macromolecules 1997), space group P2₁/a, main chain TTGG conformation. Replicate the unit cell by factors 3 × 4 × 6 to form an MD unit cell and apply three-dimensional periodic boundary conditions.
- Evidence: `/app/outputs/initial_crystal.data`

### Step 3: Single crystal MD simulation
- Role: process
- Action: Run NPT molecular dynamics on the single crystal model using the assembled force field. Set temperature 300 K and ambient pressure. Use SHAKE constraints on bonds, 14 Å cutoff for non-bonded interactions, Nosé thermostat, and Parrinello–Rahman barostat. Perform 50 ps equilibration followed by a 200 ps production run. Save the trajectory and final configuration.
- Evidence: `/app/outputs/crystal_trajectory.dump`

### Step 4: Compute crystal density and lattice constants
- Role: scored (load-bearing)
- Action: Analyze the production trajectory of the single crystal MD simulation to compute the time-averaged mass density (g/cm³) and lattice constants a, b, c (Å) and cell angles α, β, γ (degrees). Write the results to single_crystal_properties.json.
- Output file: `/app/outputs/single_crystal_properties.json`
- Format: json
- Contract: {"density": float, "a": float, "b": float, "c": float, "alpha": float, "beta": float, "gamma": float}
- Scoring: scored by hidden verifier

### Step 5: Construct interface models
- Role: process
- Action: From the equilibrated single crystal configuration, create four two-phase interface models: (100)-benzene, (100)-chloroform, (010)-benzene, (010)-chloroform. For each, elongate the appropriate crystal axis (a for (100), b for (010)) and insert 576 randomly oriented solvent molecules into the vacuum space, avoiding severe overlaps. Output the initial configurations.
- Evidence: `/app/outputs/interface_models.tar.gz`

### Step 6: Interface MD simulations
- Role: process
- Action: For each of the four interface models, run NPT molecular dynamics at 300 K with constrained cell angles. Use the same force field, thermostat, barostat, and SHAKE as for the single crystal, with adjusted virtual masses as described in the paper. Equilibrate for a total of 300 ps then perform a 5 ns production run. Save trajectories.
- Evidence: `/app/outputs/interface_trajectories.zip`

### Step 7: Analyze sorption behavior
- Role: scored (load-bearing)
- Action: Analyze the production trajectories of the four interface models. Count the number of solvent molecules that have entered the crystal cavities (first-layer absorption) during the simulation. Record the counts in absorption_counts.csv with columns: interface (string, (100) or (010)), solvent (string, benzene or chloroform), count (integer).
- Output file: `/app/outputs/absorption_counts.csv`
- Format: csv
- Contract: interface (string, values (100) or (010)), solvent (string, values benzene or chloroform), count (integer)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/single_crystal_properties.json`
- `/app/outputs/absorption_counts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### single_crystal_properties.json
- path: `/app/outputs/single_crystal_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Time-averaged density and lattice constants of the δe crystal from the NPT simulation.
- schema:
  - `type`: object
  - `required`:
    - `density`: float (g/cm³)
    - `a`: float (Å)
    - `b`: float (Å)
    - `c`: float (Å)
    - `alpha`: float (degrees)
    - `beta`: float (degrees)
    - `gamma`: float (degrees)

### absorption_counts.csv
- path: `/app/outputs/absorption_counts.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Number of absorbed solvent molecules per interface and solvent. The qualitative trend (presence/absence per face and relative ordering) is scored, not absolute numbers.
- schema:
  - `type`: table
  - `required_columns`: `interface`, `solvent`, `count`
  - `units`:
    - `count`: integer

Notes: The absolute number of absorbed molecules is stochastic; the checker evaluates only whether absorption occurs on the (100) face, does not occur on the (010) face, and that chloroform count exceeds benzene count on the (100) face. The crystal properties are compared to paper-reported values with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "single_crystal_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "density": "float (g/cm³)",
          "a": "float (Å)",
          "b": "float (Å)",
          "c": "float (Å)",
          "alpha": "float (degrees)",
          "beta": "float (degrees)",
          "gamma": "float (degrees)"
        }
      },
      "description": "Time-averaged density and lattice constants of the δe crystal from the NPT simulation."
    },
    {
      "file": "absorption_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "interface",
          "solvent",
          "count"
        ],
        "units": {
          "count": "integer"
        }
      },
      "description": "Number of absorbed solvent molecules per interface and solvent. The qualitative trend (presence/absence per face and relative ordering) is scored, not absolute numbers."
    }
  ],
  "notes": "The absolute number of absorbed molecules is stochastic; the checker evaluates only whether absorption occurs on the (100) face, does not occur on the (010) face, and that chloroform count exceeds benzene count on the (100) face. The crystal properties are compared to paper-reported values with tolerances."
}
```

## How you are scored
A hidden verifier independently checks the two required artifacts.   
- The crystal‑property file (`single_crystal_properties.json`) is compared to reference simulation values using acceptable tolerances on density and on each lattice constant and angle.   
- The absorption‑count file (`absorption_counts.csv`) is checked for the qualitative pattern: presence or absence of absorption on each face, and the relative ordering of the counts for the two solvents on the (100) face.   
Both artifacts contribute to the final reward, which is a number between 0 and 1. Reporting the correct numbers from the literature is not enough; the verifier expects them to be obtained from the specified MD workflow.
