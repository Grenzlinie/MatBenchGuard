# Surface Energy Calculation of α-Fe₂O₃ Low-Index Surfaces via DFT Slab Models

## Problem background
The stability of different crystallographic surfaces of α‑Fe₂O₃ (hematite) governs its morphology, growth habits, and catalytic properties. First‑principles surface energy calculations provide a quantitative ranking of the relative stabilities of low‑index facets, which is essential for understanding why certain facets dominate in natural and synthetic crystals. This task addresses the computation of relaxed surface energies for a set of low‑index stoichiometric surfaces, thereby determining their stability ordering.

## Approach
Periodic plane‑wave DFT with a hybrid functional (e.g., PBE0) is used to model bulk hematite and symmetric slab models of seven low‑index surfaces ({0001}, {01‾12}, {11‾20}, {10‾10}, {10‾11}, {10‾12}, {11‾26}). Slab models are built with specific layer counts and terminations that minimize the dipole moment, and all atomic positions are relaxed while preserving two‑dimensional symmetry. The total energy of the bulk unit cell is converted to an energy per repeating unit layer (E_bulk). For each relaxed slab, the surface energy is then computed via the standard slab formula E_S = (E_slab − n · E_bulk) / (2A), where n is the number of layers in the slab and A is the primitive surface unit cell area. The computed surface energies are used to rank the surfaces from most to least stable.

## Reproduction target
Construct the bulk unit cell and the seven slab models as described in the workflow steps. Perform a bulk reference DFT calculation to obtain E_bulk. Run geometry optimizations for each slab model to obtain relaxed total energies and surface cell areas. Compute the relaxed surface energy for each surface and rank them by stability. Write the results to `/app/outputs/surface_energies_relaxed.csv` as a CSV file with the columns: surface, slab_total_energy, n_layers, bulk_energy_per_layer, surface_cell_area, computed_surface_energy, and relaxed_order_rank. The surface energies must be reported in J/m², derived from the submitted raw energies and areas using the formula above. The ordering from most stable (rank 1) to least stable (rank 7) must be inferred from the computed surface energies.

## Assets

- Crystal structure of α-Fe₂O₃ (hematite): https://www.crystallography.net/cod/1000038.cif
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (Fe and O): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Construct bulk and slab models
- Role: process
- Action: From the hematite crystal structure, build the bulk unit cell and symmetric slab models for the seven low-index surfaces ({0001}, {01‾12}, {11‾20}, {10‾10}, {10‾11}, {10‾12}, {11‾26}) with the layer counts and terminations that minimize the dipole moment: 21 layers for {0001}, 25 layers for {01‾12}, 30 layers for {11‾20} and {10‾10}, 35 layers for {10‾12}, 36 layers for {11‾26}, 40 layers for {10‾11}. Prepare DFT input files (e.g., Quantum ESPRESSO pw.x inputs) for each model.
- Evidence: `/app/outputs/slab_input_files.log`

### Step 2: Bulk reference calculation
- Role: process
- Action: Run a self‑consistent DFT calculation on the bulk hematite unit cell using a hybrid functional (e.g., PBE0) to obtain the total energy per formula unit. Convert this to the energy per repeating unit layer (E_bulk) as required by the surface energy formula.
- Evidence: `/app/outputs/bulk_energy.out`

### Step 3: Slab geometry optimizations
- Role: process
- Action: For each of the seven slab models, perform DFT geometry optimization (relaxation) with the same hybrid functional, preserving the two‑dimensional periodicity and symmetry. Record the relaxed total energies and the primitive surface unit cell areas.
- Evidence: `/app/outputs/slab_energies.log`

### Step 4: Compute surface energies and stability order
- Role: scored (load-bearing)
- Action: Apply the surface energy formula E_S = (E_slab − n · E_bulk) / (2A) to each surface's relaxed total energy, layer count, bulk energy per layer, and primitive surface unit cell area. Compute the relaxed surface energy (J/m²) and rank the surfaces from most stable (1) to least stable (7). Write the results to surface_energies_relaxed.csv.
- Output file: `/app/outputs/surface_energies_relaxed.csv`
- Format: csv
- Contract: Columns: surface (string, Miller-Bravais, e.g. '01‾12'), slab_total_energy (float, eV or Hartree), n_layers (int), bulk_energy_per_layer (float, same units as slab_total_energy), surface_cell_area (float, Å²), computed_surface_energy (float, J/m²), relaxed_order_rank (int, 1‑7).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_energies_relaxed.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_energies_relaxed.csv
- path: `/app/outputs/surface_energies_relaxed.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Relaxed surface energies and stability ranking computed from DFT slab and bulk calculations.
- schema:
  - `type`: table
  - `required_columns`: `surface`, `slab_total_energy`, `n_layers`, `bulk_energy_per_layer`, `surface_cell_area`, `computed_surface_energy`, `relaxed_order_rank`
  - `units`:
    - `slab_total_energy`: eV or Hartree (consistent)
    - `bulk_energy_per_layer`: same as slab_total_energy
    - `surface_cell_area`: Å²
    - `computed_surface_energy`: J/m²

Notes: The checker recomputes the surface energy from the submitted raw numbers, verifies self‑consistency, and then scores the stability ordering (Kendall tau against a hidden reference) and absolute energy tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_energies_relaxed.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "surface",
          "slab_total_energy",
          "n_layers",
          "bulk_energy_per_layer",
          "surface_cell_area",
          "computed_surface_energy",
          "relaxed_order_rank"
        ],
        "units": {
          "slab_total_energy": "eV or Hartree (consistent)",
          "bulk_energy_per_layer": "same as slab_total_energy",
          "surface_cell_area": "Å²",
          "computed_surface_energy": "J/m²"
        }
      },
      "description": "Relaxed surface energies and stability ranking computed from DFT slab and bulk calculations."
    }
  ],
  "notes": "The checker recomputes the surface energy from the submitted raw numbers, verifies self‑consistency, and then scores the stability ordering (Kendall tau against a hidden reference) and absolute energy tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads `surface_energies_relaxed.csv`. First, the verifier recomputes each surface energy from the raw numbers you provide (slab_total_energy, n_layers, bulk_energy_per_layer, surface_cell_area) and checks that they are internally consistent within 1%. It then derives the stability ordering (1=lowest energy, 7=highest). The main portion of your score (80%) is based on how well your ordering matches a hidden reference stability ordering (measured by Kendall tau rank correlation). A secondary portion (20%) checks that each computed surface energy falls within a tolerance band around reference values. Surface energies must also be positive and lie in a physically reasonable range. Structural checks (correct column names, all seven surfaces present) carry near-zero weight but must pass to begin scoring. The exact tolerance thresholds and the hidden reference values are not disclosed, but the exercise expects that a careful re‑implementation with a hybrid functional will yield an ordering that aligns well with the reference.
