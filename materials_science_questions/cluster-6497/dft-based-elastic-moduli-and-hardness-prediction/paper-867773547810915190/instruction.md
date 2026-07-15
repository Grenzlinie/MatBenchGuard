# Configurational energy spectrum of L-site vacancy ordering in maghemite

## Problem background
Maghemite (γ-Fe₂O₃) is a ferrimagnetic iron oxide with a spinel crystal structure. The unit cell contains cation vacancies that reside solely on octahedral sites. The ordering of these iron vacancies influences the electrostatic energy of the crystal and can alter its symmetry. In the commonly cited cubic structure (space group P4₃32) the vacancies partially occupy special Wyckoff positions; fully ordered distributions give rise to a tetragonal superstructure. This task investigates the configurational energy landscape of vacancy ordering by computing the relative lattice energies of all symmetrically inequivalent ways to arrange 4 Fe cations on 12 specific octahedral vacancy sites (the “L sites”) in a 1×1×3 supercell of γ-Fe₂O₃. The objective is to determine which vacancy arrangement is the most stable and to rank all possible ordered configurations by their computed energies.

## Approach
The calculations are based on the Born model of ionic solids, where ions interact via long‑range Coulomb forces and short‑range repulsion and dispersion, described by a Buckingham potential. Electronic polarisability of the oxygen ions is included through the Dick–Overhauser shell model. The interatomic potential parameters for Fe–O and O–O interactions are taken from Lewis & Catlow (1985). A 1×1×3 supercell of cubic γ‑Fe₂O₃ (space group P4₃32) is constructed, providing 12 L octahedral sites. All 495 distinct arrangements of 4 Fe cations on these 12 sites are enumerated. Equivalent configurations under the symmetry operations of the parent structure are grouped using symmetry analysis, yielding a reduced set of symmetrically inequivalent configurations. For each inequivalent configuration a complete supercell containing Fe, vacancies, and O is built and its lattice energy is minimised with an interatomic‑potential code (e.g., GULP or LAMMPS) using the Lewis–Catlow potential. The relaxed total energies are then referenced to the lowest energy configuration, and the configurations are ordered by increasing relative energy, recording their degeneracies and space‑group symmetries.

## Reproduction target
Produce a CSV file (`configurational_energies.csv`) that lists every symmetrically inequivalent configuration, ordered by increasing relative energy. Each row must contain: a configuration identifier, the iron positions as comma‑separated L‑site labels (e.g., 'L1,L4,L7,L10'), the degeneracy (an integer), the space group (a string), and the relative lattice energy in kJ/mol (with the lowest energy set to 0.0). The file must contain exactly the full set of symmetrically inequivalent configurations (29 rows). The most stable configuration must be unambiguously identifiable from its iron positions and space group, and its energy must be the global minimum among all computed configurations.

## Assets

- Lewis and Catlow (1985) interatomic potential parameters: 10.1088/0022-3719/18/6/010
- Simulation code (GULP or LAMMPS): https://gulp.curtin.edu.au/
- Symmetry analysis library (spglib/pymatgen): spglib

## Workflow steps

### Step 1: Generate L-site coordinates in the 1×1×3 supercell
- Role: process
- Action: Construct the 1×1×3 supercell of cubic maghemite (space group P4₃32) and record the fractional coordinates of the 12 L (octahedral vacancy) sites as listed in the problem setup. These coordinates are the basis for cation-vacancy enumeration.
- Evidence: none

### Step 2: Enumerate and reduce to symmetrically inequivalent configurations
- Role: process
- Action: Enumerate all 495 arrangements of 4 Fe cations on the 12 L sites. Reduce this full set to the 29 symmetrically inequivalent configurations using symmetry analysis (e.g., spglib or pymatgen), and record each configuration's degeneracy and space group.
- Evidence: none

### Step 3: Compute relaxed lattice energies with interatomic potentials
- Role: process
- Action: For each of the 29 inequivalent configurations, build the complete supercell stoichiometry (Fe, vacancies, O) and compute the relaxed lattice energy. Use an interatomic potential model with Born/Buckingham short-range potentials and shell-model oxygen polarizability, employing parameters from Lewis & Catlow (1985). Perform energy minimisation with a suitable code (e.g., GULP or LAMMPS).
- Evidence: `/app/outputs/energy_minimisation.log`

### Step 4: Compile configurational energy results
- Role: scored (load-bearing)
- Action: Compile a CSV file with one row per symmetrically inequivalent configuration. Columns: configuration_id, iron_positions (comma-separated L-site labels, e.g. 'L1,L4,L7,L10'), degeneracy (int), space_group (string), and relative_energy_kJ_per_mol (float, normalized to the lowest-energy configuration as 0.0). Order rows by increasing relative energy.
- Output file: `/app/outputs/configurational_energies.csv`
- Format: csv
- Contract: Columns: configuration_id (int), iron_positions (str), degeneracy (int), space_group (str), relative_energy_kJ_per_mol (float). 29 rows, sorted by relative_energy_kJ_per_mol ascending.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/configurational_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### configurational_energies.csv
- path: `/app/outputs/configurational_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV listing all 29 symmetrically inequivalent vacancy configurations, their degeneracies, space groups, and relative lattice energies (kJ/mol) referenced to the lowest-energy configuration.
- schema:
  - `type`: table
  - `required_columns`: `configuration_id`, `iron_positions`, `degeneracy`, `space_group`, `relative_energy_kJ_per_mol`
  - `units`:
    - `relative_energy_kJ_per_mol`: kJ/mol

Notes: The checker compares the reported relative energies to the paper's Table 2 reference values within a tolerance, and also verifies the lowest-energy configuration is P4₁2₁2 with Fe at L1,L4,L7,L10. The agent must compute energies using the specified interatomic potential model; the result is compared to the paper's published spectrum.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "configurational_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration_id",
          "iron_positions",
          "degeneracy",
          "space_group",
          "relative_energy_kJ_per_mol"
        ],
        "units": {
          "relative_energy_kJ_per_mol": "kJ/mol"
        }
      },
      "description": "CSV listing all 29 symmetrically inequivalent vacancy configurations, their degeneracies, space groups, and relative lattice energies (kJ/mol) referenced to the lowest-energy configuration."
    }
  ],
  "notes": "The checker compares the reported relative energies to the paper's Table 2 reference values within a tolerance, and also verifies the lowest-energy configuration is P4₁2₁2 with Fe at L1,L4,L7,L10. The agent must compute energies using the specified interatomic potential model; the result is compared to the paper's published spectrum."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects `configurational_energies.csv`. The verifier checks structural integrity (correct number of rows, required columns present) and compares your computed relative energies and the energy ordering to a reference set of energies. It confirms that the configuration identified as the most stable has the expected iron positions and space group. Your score reflects the fraction of configurations whose relative energy lies within an acceptable tolerance of the reference, as well as the correctness of the ranking and the identification of the most stable arrangement. The verifier does not demand an exact numerical match to the reference; it accounts for the typical spread that arises from different simulation codes or numerical settings, provided the physical trends and the energy ordering are correctly reproduced.
