# Grain boundary energy and coordination-deficient site density in cubic zirconia

## Problem background
Grain boundary properties in ceramics are often determined by the local atomistic structure. In yttria-stabilized cubic zirconia, experimental bicrystal studies have linked grain boundary excess energy and solute segregation to the density of coordination-deficient cation sites at the grain boundary core. This task recreates the lattice statics calculations for three representative high‑angle symmetric tilt grain boundaries to compute their excess energies and the areal densities of such sites, and to test whether a monotonic relationship holds across these boundaries.

## Approach
Use the Lewis–Catlow empirical pair potentials for pure cubic ZrO₂ to perform static energy minimizations. Build periodic supercells for the Σ3{111}, Σ11{113}, and Σ9{221} symmetric tilt grain boundaries with a [110] rotation axis. For each boundary, systematically sample relative grain translations and expansions to locate the lowest‑energy configuration using LAMMPS. Also compute the bulk reference energy from a perfect‑crystal supercell. From the relaxed structures, extract the grain boundary excess energy as (E_boundary − E_perfect) / (2 × boundary area). Determine the density of coordination‑deficient cation sites by counting Zr sites whose oxygen coordination number falls below 8 (using a bond‑length cutoff). Compare the ordering of the computed excess energies and site densities across the three boundaries to discern any systematic trend.

## Reproduction target
Compute the grain boundary excess energies (J/m²) and the areal density of coordination‑deficient cation sites (sites per nm²) for the three high‑angle symmetric tilt grain boundaries Σ3{111}, Σ11{113}, and Σ9{221} in cubic zirconia. Write the results to the specified output files.

## Assets

- Lewis-Catlow potential parameters for ZrO2: 10.1088/0022-3719/18/6/009
- Cubic fluorite ZrO2 crystal structure
- LAMMPS molecular dynamics code: https://www.lammps.org

## Workflow steps

### Step 1: Lattice statics simulations
- Role: process
- Action: Build simulation cells for Σ=3{111} (misorientation 70.6°), Σ=11{113} (misorientation 129.6°), and Σ=9{221} (misorientation 39.0°) symmetric tilt grain boundaries with [110] rotation axis, using the cubic fluorite structure (a=5.14 Å). Perform energy minimization with LAMMPS using the Lewis-Catlow potential, systematically varying relative translations and expansions to find the minimum-energy configuration. Also run a perfect crystal supercell to obtain the bulk energy. Save the relaxed total energies and final configurations.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute grain boundary excess energies
- Role: scored (load-bearing)
- Action: Calculate the grain boundary excess energy for each boundary as (E_boundary − E_perfect) / (2 × area) and write the results to grain_boundary_energies.csv.
- Output file: `/app/outputs/grain_boundary_energies.csv`
- Format: csv
- Contract: Columns: Boundary (string), Energy_J_m2 (float). Units: J/m^2.
- Scoring: scored by hidden verifier

### Step 3: Compute coordination-deficient cation site densities
- Role: scored (load-bearing)
- Action: From the relaxed grain boundary structures, identify cation sites with oxygen coordination number less than 8 (using a bond-length cutoff of 25% beyond the bulk nearest-neighbor O-O distance). Compute their areal density per unit boundary area and write the results to coordination_deficient_site_densities.csv.
- Output file: `/app/outputs/coordination_deficient_site_densities.csv`
- Format: csv
- Contract: Columns: Boundary (string), Density_per_nm2 (float). Units: sites per nm^2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/grain_boundary_energies.csv`
- `/app/outputs/coordination_deficient_site_densities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### grain_boundary_energies.csv
- path: `/app/outputs/grain_boundary_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed grain boundary excess energies for Σ=3{111}, Σ=11{113}, and Σ=9{221}.
- schema:
  - `type`: table
  - `required_columns`: `Boundary`, `Energy_J_m2`
  - `units`:
    - `Energy_J_m2`: J/m^2

### coordination_deficient_site_densities.csv
- path: `/app/outputs/coordination_deficient_site_densities.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed areal densities of coordination-deficient cation sites for the three grain boundaries.
- schema:
  - `type`: table
  - `required_columns`: `Boundary`, `Density_per_nm2`
  - `units`:
    - `Density_per_nm2`: sites per nm^2

Notes: The checker inspects the computed grain boundary excess energies and the coordination-deficient cation site densities and verifies that a specific structural relationship holds across the boundaries. No absolute numerical comparison to paper-reported values is performed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "grain_boundary_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Boundary",
          "Energy_J_m2"
        ],
        "units": {
          "Energy_J_m2": "J/m^2"
        }
      },
      "description": "Computed grain boundary excess energies for Σ=3{111}, Σ=11{113}, and Σ=9{221}."
    },
    {
      "file": "coordination_deficient_site_densities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Boundary",
          "Density_per_nm2"
        ],
        "units": {
          "Density_per_nm2": "sites per nm^2"
        }
      },
      "description": "Computed areal densities of coordination-deficient cation sites for the three grain boundaries."
    }
  ],
  "notes": "The checker inspects the computed grain boundary excess energies and the coordination-deficient cation site densities and verifies that a specific structural relationship holds across the boundaries. No absolute numerical comparison to paper-reported values is performed."
}
```

## How you are scored
A hidden verifier inspects your two CSV output files. It assesses whether the computed grain boundary excess energies and coordination‑deficient site densities satisfy specific structural relationships derived from the paper's findings. Each correctly satisfied constraint contributes a weighted share to the final score. Simply reporting fabricated numbers without performing the required simulations will not pass the verifier's checks.
