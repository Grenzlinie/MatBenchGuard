# Li Adsorption and Diffusion Barriers on NiO(111) via DFT-NEB

## Problem background
Transition metal oxides such as NiO are widely studied as electrode materials for supercapacitors, but the atomic-level charge storage mechanism—whether it is dominated by surface adsorption or bulk insertion—remains debated. First-principles calculations can provide atomistic insight by computing the adsorption energies of Li atoms on different surface sites, the energy barriers for Li diffusion on the surface and into the bulk, and the resulting theoretical capacity and voltage. Reproducing these quantities is a crucial step toward understanding the intrinsic energy storage behavior.

## Approach
Density functional theory (DFT) calculations with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional, projector‑augmented‑wave (PAW) pseudopotentials, and a van der Waals correction (DFT‑D3) are used to study Li on the NiO(111) surface. A slab model of the NiO(111) surface is constructed, and the adsorption energy of a single Li atom is computed at the four high‑symmetry sites: top (T), bridge (B), fcc (H1), and hcp (H2). The climbing‑image nudged elastic band (CI‑NEB) method is then employed to find the minimum‑energy paths and barriers for Li diffusion on the surface and from the surface into the bulk. Finally, sequential Li adsorption on the surface is performed to determine the maximum Li content before metallic Li precipitation, from which the theoretical surface capacity and the average intercalation voltage are derived.

## Reproduction target
Produce three output files under `/app/outputs`:

1. `adsorption_energies.csv` — Single‑Li adsorption energies (eV) at the T, B, H1, and H2 sites on the NiO(111) surface.
2. `diffusion_barriers.csv` — Energy barriers (eV) for Li diffusion: two surface paths (surface_path1, surface_path2) and one path from the surface into the bulk through three atomic layers.
3. `theoretical_capacity.txt` — Two comma‑separated values: the theoretical maximum surface capacity (mAh/g) and the average intercalation voltage (V), derived from sequential Li adsorption up to the point where the adsorption energy remains below the cohesive energy of bcc Li.

## Assets

- NiO crystal structure (rock-salt, a=4.177 Å)
- Quantum ESPRESSO (spin‑polarized DFT, CI‑NEB, PAW support): https://www.quantum-espresso.org/
- PAW pseudopotentials for Ni and O: https://www.materialscloud.org/discover/sssp
- ASE (Atomic Simulation Environment): ase

## Workflow steps

### Step 1: Build and relax NiO(111) slab model
- Role: process
- Action: Construct a 6‑layer 3×3×1 supercell of the NiO(111) surface with a 15 Å vacuum layer, using the experimental lattice constant (a = 4.177 Å). Relax the top two layers while keeping the bottom four layers fixed, employing spin‑polarized DFT with PBE, PAW pseudopotentials, DFT‑D3 van der Waals correction, a plane‑wave cutoff of 450 eV and a 2×2×1 k‑point mesh for optimisation.
- Evidence: `/app/outputs/slab_relaxation.log`

### Step 2: Compute single‑Li adsorption energies on NiO(111)
- Role: scored
- Action: For the optimized slab, place a Li atom at the top (T), bridge (B), fcc (H1), and hcp (H2) sites, relax each geometry, and calculate the adsorption energy via E_ads = E_slab+Li - E_slab - E_Li_bulk, where E_Li_bulk is the total energy per atom of bcc Li. Output the results to adsorption_energies.csv.
- Output file: `/app/outputs/adsorption_energies.csv`
- Format: csv
- Contract: Columns: site (string: T, B, H1, H2), adsorption_energy_eV (float). One row per site.
- Scoring: scored by hidden verifier

### Step 3: Compute Li diffusion barriers (surface and surface‑to‑bulk)
- Role: scored (load-bearing)
- Action: Using the climbing‑image nudged elastic band (CI‑NEB) method, compute the minimum energy path and barrier for Li diffusion between two adjacent fcc sites on the NiO(111) surface along two symmetric paths (path‑1 and path‑2). Then construct a path from a surface fcc site into the first subsurface layer and through three atomic layers (surface‑to‑bulk path) and compute the corresponding barrier. Write the three barriers to diffusion_barriers.csv.
- Output file: `/app/outputs/diffusion_barriers.csv`
- Format: csv
- Contract: Columns: path (string: surface_path1, surface_path2, surface_to_bulk), barrier_eV (float). Three rows.
- Scoring: scored by hidden verifier

### Step 4: Compute theoretical surface capacity and average intercalation voltage
- Role: scored
- Action: Place Li atoms sequentially on the fcc sites of the NiO(111) slab, relaxing structures for Li concentrations x = 0.037, 0.074, …, 0.333 (Li_xNiO). For each concentration, compute the sequential adsorption energy. Determine the maximum x for which the adsorption energy remains lower than the cohesive energy of bcc Li (−1.63 eV/atom). From that maximum stoichiometry, calculate the theoretical capacity C = xF / M_NiO (F = 96485 C/mol, M_NiO = 74.69 g/mol) and the average intercalation voltage V = −(E_Li_xNiO − E_NiO − x·E_Li_bulk) / (x·e) for the final concentration, taking the absolute value. Output the capacity (mAh/g) and average voltage (V) to theoretical_capacity.txt.
- Output file: `/app/outputs/theoretical_capacity.txt`
- Format: txt
- Contract: Single line with two comma‑separated values: theoretical_capacity_mAh_per_g (float), average_voltage_V (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.csv`
- `/app/outputs/diffusion_barriers.csv`
- `/app/outputs/theoretical_capacity.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.csv
- path: `/app/outputs/adsorption_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Single‑Li adsorption energies on NiO(111) at T, B, H1, H2 sites.
- schema:
  - `type`: table
  - `required_columns`: `site`, `adsorption_energy_eV`
  - `units`:
    - `adsorption_energy_eV`: eV

### diffusion_barriers.csv
- path: `/app/outputs/diffusion_barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CI‑NEB barriers for surface diffusion (path‑1, path‑2) and surface‑to‑bulk migration.
- schema:
  - `type`: table
  - `required_columns`: `path`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

### theoretical_capacity.txt
- path: `/app/outputs/theoretical_capacity.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Theoretical surface capacity and average voltage from sequential Li adsorption.
- schema:
  - `type`: text
  - `description`: Comma‑separated pair: theoretical capacity (mAh/g), average intercalation voltage (V).

Notes: All scored values are compared to the paper‑reported reference numbers with domain‑appropriate tolerances (e.g., ±0.15 eV for adsorption energies, ±0.05 eV for barriers, ±10% for capacity and voltage). The checker uses a hidden gold derived from the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "site",
          "adsorption_energy_eV"
        ],
        "units": {
          "adsorption_energy_eV": "eV"
        }
      },
      "description": "Single‑Li adsorption energies on NiO(111) at T, B, H1, H2 sites."
    },
    {
      "file": "diffusion_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "path",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "CI‑NEB barriers for surface diffusion (path‑1, path‑2) and surface‑to‑bulk migration."
    },
    {
      "file": "theoretical_capacity.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Comma‑separated pair: theoretical capacity (mAh/g), average intercalation voltage (V)."
      },
      "description": "Theoretical surface capacity and average voltage from sequential Li adsorption."
    }
  ],
  "notes": "All scored values are compared to the paper‑reported reference numbers with domain‑appropriate tolerances (e.g., ±0.15 eV for adsorption energies, ±0.05 eV for barriers, ±10% for capacity and voltage). The checker uses a hidden gold derived from the paper."
}
```

## How you are scored
A hidden verifier independently scores each of your three output files by comparing your computed numbers to reference values obtained from first‑principles calculations. The comparison uses domain‑appropriate tolerances that account for differences in DFT implementation, pseudopotentials, and numerical settings. The three stages carry different weights: adsorption energies, diffusion barriers, and capacity+voltage. The total reward is a weighted combination of the stage scores, with the diffusion barriers and the capacity‑voltage pair contributing more heavily than the individual site adsorption energies.
