# Energetics of place exchange and impurity interactions on Au(100) surface

## Problem background
When a 3d transition-metal adatom is deposited on an Au(100) surface, place exchange with a surface Au atom can create a surface alloy. Understanding the energetic driving forces—specifically, whether site exchange is thermodynamically favorable and whether the impurities tend to cluster or disperse—is essential for predicting the morphology and growth of magnetic nanostructures. Ab initio total-energy calculations can determine the sign and magnitude of the exchange energy difference (ΔE) and the interaction energies between impurities. This task requires computing these quantities for each 3d impurity on Au(100) using spin-polarized density-functional theory.

## Approach
The study uses spin-polarized density-functional theory within the local density approximation (LDA). The Au(100) surface is modeled by a periodic slab with a vacuum layer. For each 3d impurity (Sc through Zn), two configurations are compared: (A) impurity as an adatom on the surface, and (B) impurity substituted into the first surface layer with the displaced Au atom placed at the adatom site (site-exchanged configuration). Total energies E_A and E_B are computed without relaxing atomic positions. The exchange energy difference is ΔE = E_B − E_A. To examine impurity clustering, total energies of nearest-neighbor impurity pairs are calculated for two geometries: both atoms on adatom sites, and both atoms in the first surface layer. Interaction energies are obtained as E_pair − 2 × E_single. Additionally, for Co, the single-impurity calculation is repeated without spin polarization (paramagnetic Co) to assess the effect of magnetism. All DFT calculations are performed with an open-source plane-wave code (Quantum ESPRESSO), and the slab structures are built with the Atomic Simulation Environment (ASE).

## Reproduction target
The goal is to produce two CSV files containing the derived energy differences.

- `exchange_energies.csv` must list ΔE (in eV) for each 3d element (Sc through Zn) and for paramagnetic Co.
- `interaction_energies.csv` must list the interaction energy (in eV) for each impurity, for both adatom-pair and layer-pair arrangements.

The computed numbers will be checked against reference values by an automated verifier; no additional output is required.

## Assets

- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase
- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP efficiency LDA pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build Au(100) slab model
- Role: process
- Action: Construct an unreconstructed fcc Au(100) slab with 5 atomic layers and ~15 Å vacuum using the experimental (or LDA‑optimized) lattice constant. Save the slab structure for later use.
- Evidence: `/app/outputs/slab_structure.xyz`

### Step 2: DFT total energies for single impurity configurations
- Role: process
- Action: For each 3d impurity (Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn), create adatom (A) and site‑exchanged (B) configurations on the slab. Perform spin‑polarized LDA total‑energy calculations using Quantum ESPRESSO, without lattice relaxation. Record E_A and E_B. For Co also run a non‑spin‑polarized calculation for both configurations (paramagnetic Co). Save all raw total energies to a file for the next step.
- Evidence: `/app/outputs/single_impurity_energies.json`

### Step 3: DFT total energies for impurity pairs
- Role: process
- Action: Using a suitable supercell (e.g., 2×2) create configurations with two identical impurities at nearest‑neighbour positions: (i) both on surface adatom sites; (ii) both in first‑layer terrace sites. Perform spin‑polarized LDA total‑energy calculations for each ferromagnetic pair. Save E_pair_surface and E_pair_layer to a file.
- Evidence: `/app/outputs/pair_impurity_energies.json`

### Step 4: Compute exchange energy differences
- Role: scored (load-bearing)
- Action: From the single‑impurity DFT energies compute ΔE = E_B – E_A for each magnetic 3d impurity and for paramagnetic Co. Write a CSV file with columns element (string) and delta_E_eV (float).
- Output file: `/app/outputs/exchange_energies.csv`
- Format: csv
- Contract: element: string, delta_E_eV: float
- Scoring: scored by hidden verifier

### Step 5: Compute impurity interaction energies
- Role: scored (load-bearing)
- Action: For each impurity compute the surface interaction energy E_int_surface = E_pair_surface – 2×E_A, and the layer interaction energy E_int_layer = E_pair_layer – 2×E_B. Write a CSV file with columns element (string), position (one of 'surface_adatom' or 'surface_layer'), and interaction_energy_eV (float).
- Output file: `/app/outputs/interaction_energies.csv`
- Format: csv
- Contract: element: string, position: string, interaction_energy_eV: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/exchange_energies.csv`
- `/app/outputs/interaction_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### exchange_energies.csv
- path: `/app/outputs/exchange_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Exchange energy differences (ΔE) for 3d impurities on Au(100). Values are compared to hidden paper‑derived references with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `element`, `delta_E_eV`
  - `units`:
    - `delta_E_eV`: eV

### interaction_energies.csv
- path: `/app/outputs/interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nearest‑neighbour impurity interaction energies for 3d impurities on Au(100), both on adatom sites and in the surface layer. Values are compared to hidden paper‑derived references with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `element`, `position`, `interaction_energy_eV`
  - `units`:
    - `interaction_energy_eV`: eV

Notes: All values must be computed using spin‑polarized LDA‑DFT without lattice relaxation. The checker compares the submitted energy values to the paper’s digitized results; tolerances account for code‑dependent spread. The sign check for ΔE is implicitly handled within the tolerance‑based reference match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "exchange_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "delta_E_eV"
        ],
        "units": {
          "delta_E_eV": "eV"
        }
      },
      "description": "Exchange energy differences (ΔE) for 3d impurities on Au(100). Values are compared to hidden paper‑derived references with tolerances."
    },
    {
      "file": "interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "position",
          "interaction_energy_eV"
        ],
        "units": {
          "interaction_energy_eV": "eV"
        }
      },
      "description": "Nearest‑neighbour impurity interaction energies for 3d impurities on Au(100), both on adatom sites and in the surface layer. Values are compared to hidden paper‑derived references with tolerances."
    }
  ],
  "notes": "All values must be computed using spin‑polarized LDA‑DFT without lattice relaxation. The checker compares the submitted energy values to the paper’s digitized results; tolerances account for code‑dependent spread. The sign check for ΔE is implicitly handled within the tolerance‑based reference match."
}
```

## How you are scored
A hidden verification program reads your `exchange_energies.csv` and `interaction_energies.csv` and compares each numerical value against a set of reference answers using tolerances appropriate for DFT re-runs carried out with a different code. The exchange energy differences are given the highest weight, the impurity interaction energies a moderate weight, and the paramagnetic Co exchange energy the lowest weight. The final score is a weighted average (0.0–1.0). Only submissions that result from faithfully executing the required DFT workflow are expected to pass the tolerance checks.
