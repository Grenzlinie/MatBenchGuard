# Investigation of quenching at a Cu high-angle grain boundary

## Problem background
Grain boundaries (GBs) play a central role in the mechanical and thermal behaviour of polycrystalline materials. High-angle boundaries can exhibit interface melting at temperatures well below the bulk melting point. When a melted GB is subsequently quenched, the rapid temperature drop may lead to a regrown GB structure that differs from the one obtained by simply heating to the same temperature. Understanding whether and how quenching alters the atomic-scale structure of a high-angle GB is important for materials processing and performance. This task investigates the structural changes at a Cu Σ5(310)/[001] symmetric tilt grain boundary using molecular dynamics simulations. The goal is to determine how the atom density profiles compare between a heating-only pathway and a quench following interface melting.

## Approach
The investigation proceeds in two main phases. First, a bicrystal simulation cell with the Σ5(310)/[001] tilt GB is constructed using the lattice constant of Cu from a published embedded-atom method (EAM) potential. The cell is heated in a series of temperature steps, and at each step the static structure factor and internal energy per atom in the GB region are computed to detect the onset of interface melting. Second, starting from the melted configuration, the system is quenched through a sequence of decreasing temperatures down to 300 K. From both the heating and quenching runs, the time-averaged atom density profile along the direction normal to the GB is extracted. The key comparison is made at 300 K: the density profile from the heating series is contrasted with that from the quenching series, focussing on the central density peak at the grain boundary. All simulations use the same EAM potential and an open-source molecular dynamics engine.

## Reproduction target
Your task is to reproduce the molecular dynamics simulations and compute the following artifacts:
- A table confirming the interface melting transition (melting confirmation CSV).
- The atom density profile along Y at 300 K obtained from the heating series (heating 300K CSV).
- The same profile at 300 K obtained from the quenching series (quenching 300K CSV).
- A quantitative comparison of the central GB density peaks extracted from the two profiles (comparison metrics JSON).

The objective is to establish whether the quenched 300 K GB structure differs from the one produced by heating alone, as reflected in the atom density profiles.

## Assets

- Cu EAM potential (Mei et al. 1991): https://www.ctcms.nist.gov/potentials/Download/1991--Mei-J-Davenport-J-W-Fernando-G-W--Cu/1/eam.alloy_Cu_mei
- LAMMPS molecular dynamics package: https://www.lammps.org

## Workflow steps

### Step 1: Build Σ5(310)/[001] Cu bicrystal cell
- Role: process
- Action: Construct a bicrystalline simulation cell containing 33,480 Cu atoms representing a Σ5(310)/[001] symmetric tilt grain boundary. Use the EAM lattice constant (3.615 Å), dimensions 12 CSL units along X, 44 a0 along Y, 10 a0 along Z, and fixed boundary slabs of ~3 a0 thickness. Export the atomic configuration.
- Evidence: `/app/outputs/cell_data.dump`

### Step 2: Run MD heating series from 300 K to 1200 K
- Role: process
- Action: Using the constructed cell and the Cu EAM potential, perform MD simulations with a time step of 1.6e-15 s, velocity rescaling every 50 steps. From 300 K to 1200 K in 100 K increments, run 100,000 steps for equilibration followed by 20,000 steps for production at each temperature. Save the trajectories.
- Evidence: `/app/outputs/heating_traj.log`

### Step 3: Compute melting confirmation diagnostics
- Role: scored
- Action: From the heating trajectories, divide the cell into layers along Y. Compute the average static structure factor S in the bicrystal centre using k=(0,0,4π/a0) and the internal energy per atom in the GB region at each temperature. Output a table with temperature, S_centre, and energy_per_atom.
- Output file: `/app/outputs/melting_confirmation.csv`
- Format: csv
- Contract: columns: temperature (K), S_centre (dimensionless), energy_per_atom (eV/atom); rows for temperatures 300,400,...,1200 K.
- Scoring: scored by hidden verifier

### Step 4: Run MD quenching from the melted GB at 1100 K
- Role: process
- Action: Starting from the configuration at 1100 K, perform quenching MD with the temperature sequence: 1090 K (100,000 steps), 1000 K (75,000 steps), 900 K (55,000 steps), 800 K (55,000 steps), 700 K (55,000 steps), 600 K (55,000 steps), 500 K (55,000 steps), 400 K (55,000 steps), 300 K (55,000 steps). Save the trajectories.
- Evidence: `/app/outputs/quenching_traj.log`

### Step 5: Compute atom density profile for heating at 300 K
- Role: scored
- Action: From the production trajectory of the heating series at 300 K, compute the time-averaged atom density ρ along the Y axis (layer bins). Output a CSV with Y position (in units of a0) and density (in atoms/a0^3).
- Output file: `/app/outputs/density_profile_heating_300K.csv`
- Format: csv
- Contract: columns: Y_position (units of a0), density (atoms/a0^3); rows for each layer.
- Scoring: scored by hidden verifier

### Step 6: Compute atom density profile for quenching at 300 K
- Role: scored
- Action: From the trajectory at the end of the quenching run at 300 K, compute the time-averaged atom density ρ along Y. Output a CSV with Y position (in units of a0) and density (in atoms/a0^3).
- Output file: `/app/outputs/density_profile_quenching_300K.csv`
- Format: csv
- Contract: columns: Y_position (units of a0), density (atoms/a0^3); rows for each layer.
- Scoring: scored by hidden verifier

### Step 7: Compare heating vs quenching density at 300 K
- Role: scored (load-bearing)
- Action: From the two density profile CSVs, extract the peak density in the central GB region. Compute the peak heights and their difference. Output a JSON with heating_peak_density, quenching_peak_density, and peak_density_difference (all in atoms/a0^3).
- Output file: `/app/outputs/comparison_metrics.json`
- Format: json
- Contract: {"heating_peak_density": <float in atoms/a0^3>, "quenching_peak_density": <float in atoms/a0^3>, "peak_density_difference": <float in atoms/a0^3>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/melting_confirmation.csv`
- `/app/outputs/density_profile_heating_300K.csv`
- `/app/outputs/density_profile_quenching_300K.csv`
- `/app/outputs/comparison_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### melting_confirmation.csv
- path: `/app/outputs/melting_confirmation.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Table of centre static structure factor and internal energy per atom in the GB region versus temperature, used to confirm the interface melting transition.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `S_centre`, `energy_per_atom`
  - `units`:
    - `temperature`: K
    - `S_centre`: dimensionless
    - `energy_per_atom`: eV/atom

### density_profile_heating_300K.csv
- path: `/app/outputs/density_profile_heating_300K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Atom density profile along Y from the heating simulation at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `Y_position`, `density`
  - `units`:
    - `Y_position`: a0
    - `density`: atoms/a0^3

### density_profile_quenching_300K.csv
- path: `/app/outputs/density_profile_quenching_300K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Atom density profile along Y from the quenching simulation at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `Y_position`, `density`
  - `units`:
    - `Y_position`: a0
    - `density`: atoms/a0^3

### comparison_metrics.json
- path: `/app/outputs/comparison_metrics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Key metrics comparing the central GB density peaks between heating and quenching at 300 K.
- schema:
  - `type`: object
  - `required`:
    - `heating_peak_density`: float (atoms/a0^3)
    - `quenching_peak_density`: float (atoms/a0^3)
    - `peak_density_difference`: float (atoms/a0^3)

Notes: The checker will validate that the structure factor drops near zero and the internal energy jumps near 1088 K from the melting_confirmation.csv, and that the quenching peak density is lower than the heating peak at 300 K. The comparison_metrics.json values must be consistent with the corresponding density CSVs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "melting_confirmation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "S_centre",
          "energy_per_atom"
        ],
        "units": {
          "temperature": "K",
          "S_centre": "dimensionless",
          "energy_per_atom": "eV/atom"
        }
      },
      "description": "Table of centre static structure factor and internal energy per atom in the GB region versus temperature, used to confirm the interface melting transition."
    },
    {
      "file": "density_profile_heating_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Y_position",
          "density"
        ],
        "units": {
          "Y_position": "a0",
          "density": "atoms/a0^3"
        }
      },
      "description": "Atom density profile along Y from the heating simulation at 300 K."
    },
    {
      "file": "density_profile_quenching_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Y_position",
          "density"
        ],
        "units": {
          "Y_position": "a0",
          "density": "atoms/a0^3"
        }
      },
      "description": "Atom density profile along Y from the quenching simulation at 300 K."
    },
    {
      "file": "comparison_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "heating_peak_density": "float (atoms/a0^3)",
          "quenching_peak_density": "float (atoms/a0^3)",
          "peak_density_difference": "float (atoms/a0^3)"
        }
      },
      "description": "Key metrics comparing the central GB density peaks between heating and quenching at 300 K."
    }
  ],
  "notes": "The checker will validate that the structure factor drops near zero and the internal energy jumps near 1088 K from the melting_confirmation.csv, and that the quenching peak density is lower than the heating peak at 300 K. The comparison_metrics.json values must be consistent with the corresponding density CSVs."
}
```

## How you are scored
A hidden verifier will evaluate your submitted files. For the melting confirmation CSV, it checks that the static structure factor in the GB centre drops near zero and that the internal energy shows a clear jump at the melting temperature, indicating the transition. The density profile CSVs are inspected for expected physical features (e.g., oscillations with period consistent with the lattice constant, distinct bulk and GB regions). The verifier extracts the central peak densities and verifies that the quenching peak is measurably different from the heating peak. Finally, the comparison metrics JSON is cross‑checked against the CSVs for internal consistency. Each scored artifact contributes a portion to the final reward, and the total score is a weighted sum of these contributions.
