# Atomistic Simulation of Al Interdiffusion in U-Mo Surfaces

## Problem background
In U-Mo/Al dispersion nuclear fuels, low-Mo alloy particles exhibit extensive aluminum interdiffusion and swelling during irradiation, while high-Mo particles show little dimensional change. Understanding the atomic-scale energetics of aluminum on uranium-molybdenum surfaces is essential to explain this difference in behavior. This task uses atomistic simulations to compute the relative energies of Al adatoms on U-Mo slabs with varying Mo placement and concentration, providing thermodynamic insight into whether Mo-rich configurations present energetic barriers to Al penetration.

## Approach
The Bozzolo-Ferrante-Smith (BFS) method for alloys computes the total energy of an atomic configuration as a sum over atoms of strain and chemical contributions linked by a coupling function. The single-element ECT parameters (p, α, l, λ) and the BFS perturbation matrix Δ_ij for Al, U, and Mo are taken from first-principles LAPW results. The following tables give the needed parameters:

| Element | Lattice param. (Å) | Cohesive energy (eV) | Bulk modulus (GPa) | p | α (Å⁻¹) | l (Å) | λ (Å) |
|---------|-------------------|---------------------|---------------------|---|---|---|---|---|
| Al      | 3.2381           | 3.44                | 69.14               | 4 | 1.7639 | 0.3641 | 1.0232 |
| Mo      | 3.1616           | 6.67                | 260.61              | 8 | 3.4773 | 0.2641 | 0.7422 |
| U       | 3.4501           | 5.55                | 141.40              |12 | 4.8689 | 0.3132 | 0.8801 |

Δ_ij (Å⁻¹) matrix:

| i\j | Al       | Mo       | U        |
|-----|----------|----------|----------|
| Al  | –        | -0.03351 | 0.15351  |
| Mo  | 0.10065  | –        | -0.06189 |
| U   | -0.03909 | 0.09261  | –        |

The BFS energy of atom i is ε_i = ε_i^S + g_i (ε_i^C − ε_i^{C0}), where ε_i^S is the ECT strain energy, ε_i^C is the chemical energy using the Δ parameters, ε_i^{C0} is a reference chemical energy, and g_i is a coupling function that depends on the local environment. Implement this method to compute the total energy of an atomic configuration for Al, U, and Mo atoms.

Two sets of configurations are studied:
1. Single-Mo configurations (Fig. 4 in the source): Al adatom on U(100) and U(110) slabs with one Mo atom placed at surface (S), first subsurface (1b), or second subsurface (2b) sites, with Al either close to or far from Mo. The relative energy of each configuration is computed with respect to the lowest-energy state for that face and Mo location.
2. Mo-patch configurations (Fig. 5 in the source): A U(100) slab containing a surface patch of four Mo atoms. An Al atom is placed in overlayer (O), surface (S), or first subsurface (1b) positions, with 0 to 4 direct Al–Mo nearest neighbors. The reference is the configuration where Al is far from the Mo patch in the overlayer. The relative energies of all 15 configurations are computed.

## Reproduction target
Compute the relative energies (in eV) for the ternary Al-U-Mo configurations described above and write them to CSV files:

- `fig4_relative_energies.csv`: For each face (U100, U110) and Mo location (S, 1b, 2b), include configurations with Al close and far from Mo. The relative energy of each configuration is the total energy difference from the lowest-energy configuration for that face and Mo location (set the lowest to 0.0 eV). Columns: face, mo_location, al_proximity, configuration, relative_energy_eV.

- `fig5_relative_energies.csv`: For the 15 configurations with the Mo surface patch, compute relative energies with respect to the overlayer configuration where Al is far from the patch (that configuration must have 0.0 eV). Each row corresponds to a row in the figure panel (row numbers 1 to 5, top to bottom), with column labels O, S, or 1b, and includes coordination (0–4). Columns: row_number, column_label, coordination, configuration_label, relative_energy_eV.

## Assets
The only required external asset is the Python package `numpy` (available via pip). No external datasets, models, or other tools are needed.

## Workflow steps

### Step 1: Implement BFS energy calculation for Al-U-Mo system
- Role: process
- Action: Implement the Bozzolo-Ferrante-Smith (BFS) method for the Al-U-Mo system using the single-element parameters (p, alpha, l, lambda) and the perturbation matrix Delta_ij given in the problem statement. The energy is computed as a sum over atoms of strain and chemical energy contributions with a coupling function. Write a Python module bfs_module.py that accepts atomic positions and returns the total energy.
- Evidence: `/app/outputs/bfs_module.py`

### Step 2: Compute relative energies for single-Mo ternary configurations (Fig. 4)
- Role: scored (load-bearing)
- Action: For U(100) and U(110) slabs with one Al adatom and one Mo atom placed at surface (S), first subsurface (1b), or second subsurface (2b) sites, and for Al close to or far from Mo, compute the total energy of each configuration using the BFS implementation. For each face and Mo location, determine the lowest-energy configuration and report the energy of every configuration relative to it (lowest = 0.0 eV). Output a CSV file with the relative energies.
- Output file: `/app/outputs/fig4_relative_energies.csv`
- Format: csv
- Contract: Columns: face (U100 or U110), mo_location (S, 1b, 2b), al_proximity (close, far), configuration (string label), relative_energy_eV (float).
- Scoring: scored by hidden verifier

### Step 3: Compute relative energies for Mo-patch configurations (Fig. 5)
- Role: scored (load-bearing)
- Action: For a U(100) slab with a surface patch of 4 Mo atoms, construct 15 configurations of an Al atom in overlayer (O), surface (S), or first subsurface (1b) positions with 0 to 4 direct Al-Mo nearest neighbors. Compute the total energy of each configuration using the BFS implementation. Use the configuration where Al is far from the Mo patch in the overlayer as the reference (relative energy = 0.0 eV). Output a CSV file with the relative energies of all 15 configurations.
- Output file: `/app/outputs/fig5_relative_energies.csv`
- Format: csv
- Contract: Columns: row_number (1 to 5), column_label (O, S, 1b), coordination (integer 0-4 Al-Mo nearest neighbors), configuration_label (string), relative_energy_eV (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fig4_relative_energies.csv`
- `/app/outputs/fig5_relative_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fig4_relative_energies.csv
- path: `/app/outputs/fig4_relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative energies (in eV) for single-Mo ternary configurations (Fig. 4). Each row is one configuration; the lowest-energy configuration per face and mo_location must be exactly 0.0 eV.
- schema:
  - `type`: table
  - `required_columns`: `face`, `mo_location`, `al_proximity`, `configuration`, `relative_energy_eV`
  - `units`:
    - `relative_energy_eV`: eV

### fig5_relative_energies.csv
- path: `/app/outputs/fig5_relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative energies (in eV) for the 15 Mo‑patch configurations (Fig. 5). The reference configuration (row 1, column O) must be exactly 0.0 eV.
- schema:
  - `type`: table
  - `required_columns`: `row_number`, `column_label`, `coordination`, `configuration_label`, `relative_energy_eV`
  - `units`:
    - `relative_energy_eV`: eV

Notes: The checker compares relative energies to published reference values and verifies ordering within each sub-case (e.g., energy barrier of ~0.0571 eV for the specific U(100) Mo(1b) close configuration, and the trend that higher Al-Mo coordination increases subsurface incorporation energy). No absolute tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fig4_relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "face",
          "mo_location",
          "al_proximity",
          "configuration",
          "relative_energy_eV"
        ],
        "units": {
          "relative_energy_eV": "eV"
        }
      },
      "description": "Relative energies (in eV) for single-Mo ternary configurations (Fig. 4). Each row is one configuration; the lowest-energy configuration per face and mo_location must be exactly 0.0 eV."
    },
    {
      "file": "fig5_relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "row_number",
          "column_label",
          "coordination",
          "configuration_label",
          "relative_energy_eV"
        ],
        "units": {
          "relative_energy_eV": "eV"
        }
      },
      "description": "Relative energies (in eV) for the 15 Mo‑patch configurations (Fig. 5). The reference configuration (row 1, column O) must be exactly 0.0 eV."
    }
  ],
  "notes": "The checker compares relative energies to published reference values and verifies ordering within each sub-case (e.g., energy barrier of ~0.0571 eV for the specific U(100) Mo(1b) close configuration, and the trend that higher Al-Mo coordination increases subsurface incorporation energy). No absolute tolerances are disclosed here."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently reads your two CSV output files and compares the relative energies to expected reference values. The verifier checks that: (a) the lowest-energy state is correctly identified as 0.0 eV within each group; (b) the ordering and trends of the relative energies across configurations are correct; and (c) specific energy values match the expected results. The final reward is a weighted combination of the scores from `fig4_relative_energies.csv` and `fig5_relative_energies.csv`. Simply reporting correct-looking numbers without implementing the BFS method will not produce valid outputs that pass the hidden checks.
