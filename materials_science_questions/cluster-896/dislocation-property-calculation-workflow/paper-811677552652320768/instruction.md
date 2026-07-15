# Dislocation Property Calculation in Silicon and Germanium

## Problem background
Dislocations in semiconductors strongly influence electronic and mechanical properties, making their atomic-scale structure and energetics critical for understanding device behavior. This work investigates three dislocation types in bulk silicon and germanium: the 60° shuffle dislocation, the 60° glide dislocation, and the 90° glide partial. Computing their core and total energies, as well as derived properties from the energy versus radial distance behavior, provides insight into which configurations are stable and how they compare across materials.

## Approach
The central idea is atomistic simulation using an empirical interatomic potential. Dislocations are modeled by constructing a periodic computational cell of approximately 1250 atoms arranged in two (220) planes along the [110] direction. An isotropic elastic displacement field corresponding to the Burgers vector is applied to generate initial atomic positions, and the system is relaxed via energy minimization with the Stillinger-Weber potential. The potential parameters differ for Si and Ge, and each dislocation type requires a separate simulation. Once relaxed, the dislocation energy per unit length is computed within concentric cylinders of varying radius R. The analysis extracts the core energy at R = 5 Å and the total energy at R = 28 Å for each case. For selected configurations, the linear region of E vs ln(R) is identified to determine its slope, and the core radius is estimated from the deviation from linearity. The workflow is entirely computational, using public potential parameters and an open-source minimization code such as LAMMPS.

## Reproduction target
Produce a single JSON file, `dislocation_results.json`, containing the following quantities computed from the atomistic simulations. All energies and slopes are in eV/Å; the core radius is in Å.

- Core energy (R=5 Å) and total energy (R=28 Å) for the 60° shuffle dislocation in Si (`core_energy_Si_shuffle`, `total_energy_Si_shuffle`).
- Core energy (R=5 Å) and total energy (R=28 Å) for the 60° shuffle dislocation in Ge (`core_energy_Ge_shuffle`, `total_energy_Ge_shuffle`).
- Core energy (R=5 Å) and total energy (R=28 Å) for the 60° glide dislocation in Ge (`core_energy_Ge_glide`, `total_energy_Ge_glide`).
- Core energy (R=5 Å) and total energy (R=28 Å) for the 90° glide partial in Si (`core_energy_Si_90partial`, `total_energy_Si_90partial`).
- Core energy (R=5 Å) and total energy (R=28 Å) for the 90° glide partial in Ge (`core_energy_Ge_90partial`, `total_energy_Ge_90partial`).
- Slope of the linear region of E vs ln(R) for the 60° shuffle dislocation in Ge (`slope_Ge_shuffle`).
- Slope of the linear region of E vs ln(R) for the 90° glide partial in Ge (`slope_Ge_90partial`).
- Core radius (deviation from linearity) for the 60° shuffle dislocation in Ge (`core_radius_Ge_shuffle`).

## Assets

- Stillinger-Weber potential parameters for Si: 10.1103/PhysRevB.31.5262
- Stillinger-Weber potential parameters for Ge: 10.1103/PhysRevB.34.6987
- LAMMPS: https://lammps.sandia.gov

## Workflow steps

### Step 1: Build initial dislocation configurations
- Role: process
- Action: For each dislocation type (60° shuffle Si, 60° shuffle Ge, 60° glide Ge, 90° glide partial Si, 90° glide partial Ge), create a computational cell of approximately 1250 atoms arranged in two consecutive (220) planes, periodic along [110] with repeat distance a/√2. Apply the isotropic elastic displacement field for the corresponding Burgers vector to generate initial atomic coordinates.
- Evidence: `/app/outputs/initial_positions.log`

### Step 2: Relax dislocation structures
- Role: process
- Action: For each initial configuration, fix the outer layers of atoms and minimize the total energy using the Stillinger-Weber potential (Si parameters for Si cases, Ge parameters for Ge cases). Output relaxed atomic coordinates and energies.
- Evidence: `/app/outputs/relaxed_structures.log`

### Step 3: Compute dislocation energies, slopes, and core radius
- Role: scored (load-bearing)
- Action: From the relaxed atomic configurations, compute the dislocation energy per unit length within a cylinder of radius R at multiple radii. Extract the core energy at R = 5 Å and the total energy at R = 28 Å for each configuration. For the 60° shuffle Ge and 90° glide partial Ge configurations, analyse the linear region of E vs ln(R) to determine its slope, and identify the core radius where linearity deviates. Write all numeric results to dislocation_results.json.
- Output file: `/app/outputs/dislocation_results.json`
- Format: json
- Contract: JSON object with keys: core_energy_Si_shuffle (float, eV/Å), total_energy_Si_shuffle (float, eV/Å), core_energy_Ge_shuffle (float, eV/Å), total_energy_Ge_shuffle (float, eV/Å), core_energy_Ge_glide (float, eV/Å), total_energy_Ge_glide (float, eV/Å), core_energy_Si_90partial (float, eV/Å), total_energy_Si_90partial (float, eV/Å), core_energy_Ge_90partial (float, eV/Å), total_energy_Ge_90partial (float, eV/Å), slope_Ge_shuffle (float, eV/Å), slope_Ge_90partial (float, eV/Å), core_radius_Ge_shuffle (float, Å).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dislocation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dislocation_results.json
- path: `/app/outputs/dislocation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single JSON file containing all required dislocation energies, slopes, and core radius computed from the atomistic simulations.
- schema:
  - `type`: object
  - `required`:
    - `core_energy_Si_shuffle`: float
    - `total_energy_Si_shuffle`: float
    - `core_energy_Ge_shuffle`: float
    - `total_energy_Ge_shuffle`: float
    - `core_energy_Ge_glide`: float
    - `total_energy_Ge_glide`: float
    - `core_energy_Si_90partial`: float
    - `total_energy_Si_90partial`: float
    - `core_energy_Ge_90partial`: float
    - `total_energy_Ge_90partial`: float
    - `slope_Ge_shuffle`: float
    - `slope_Ge_90partial`: float
    - `core_radius_Ge_shuffle`: float
  - `units`:
    - `all_energies`: eV/Å
    - `all_slopes`: eV/Å
    - `core_radius_Ge_shuffle`: Å

Notes: All energy and slope fields are in eV/Å; core radius in Å. The output contains only public structural information with no gold values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dislocation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "core_energy_Si_shuffle": "float",
          "total_energy_Si_shuffle": "float",
          "core_energy_Ge_shuffle": "float",
          "total_energy_Ge_shuffle": "float",
          "core_energy_Ge_glide": "float",
          "total_energy_Ge_glide": "float",
          "core_energy_Si_90partial": "float",
          "total_energy_Si_90partial": "float",
          "core_energy_Ge_90partial": "float",
          "total_energy_Ge_90partial": "float",
          "slope_Ge_shuffle": "float",
          "slope_Ge_90partial": "float",
          "core_radius_Ge_shuffle": "float"
        },
        "units": {
          "all_energies": "eV/Å",
          "all_slopes": "eV/Å",
          "core_radius_Ge_shuffle": "Å"
        }
      },
      "description": "Single JSON file containing all required dislocation energies, slopes, and core radius computed from the atomistic simulations."
    }
  ],
  "notes": "All energy and slope fields are in eV/Å; core radius in Å. The output contains only public structural information with no gold values."
}
```

## How you are scored
A hidden verifier checks your submitted `dislocation_results.json`. Each numeric field is compared against independently computed reference values using pre-defined tolerances. The overall score is a weighted combination of the energy fields, slope fields, and the core radius field. The intermediate process steps (building initial configurations and relaxing structures) must be executed and evidenced by the requested log files, but they are not directly scored; only the final JSON output determines your reward.
