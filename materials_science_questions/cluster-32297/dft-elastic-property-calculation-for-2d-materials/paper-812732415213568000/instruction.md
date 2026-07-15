# First-principles Investigation of Stability, Cleavage Energy, and Electronic Properties of XP3 Layered Materials

## Problem background
Layered materials with the general formula XY₃, where X belongs to Group 14 (C, Si, Ge, Sn, Pb) and Y belongs to Group 15, can exhibit a metal-to-semiconductor transition when thinned from bulk to a few layers due to quantum confinement. Understanding their cleavage energies, dynamical stability, and electronic band gaps is central to assessing their exfoliability and potential for nanoelectronic devices. This task asks you to compute these properties from first principles for the phosphorus-based family, XP₃.

## Approach
Use density functional theory (DFT) with the PBE+D3 functional and a plane-wave cutoff of 500 eV. Build initial structures for bulk (space group R-3m, hexagonal), monolayer (rectangular cell with surface reconstruction), and bilayer (hexagonal) forms for each XP₃. Perform geometry relaxation, then compute phonon dispersions via the finite displacement method to classify dynamical stability. Cleavage energies are evaluated using a 5‑layer slab model with energy‑distance fitting. Finally, compute electronic band structures at the PBE level for all systems and, for those that are dynamically stable, additionally at the HSE06 hybrid‑functional level. For every (system, layer type, functional) combination determine the band gap, gap character (direct/indirect/metallic), and classify the material as metallic or semiconducting.

## Reproduction target
Reproduce the following quantities for each XP₃ system (X = C, Si, Ge, Sn, Pb) in bulk, monolayer, and bilayer forms:
- Cleavage energy (J/m²) for monolayer and bilayer exfoliation, computed from the 5‑layer slab model.
- Dynamical stability verdict (stable/unstable) from the phonon dispersion.
- Electronic band gap (eV) and gap character (direct/indirect/metallic) at the PBE level for all systems, and additionally at the HSE06 level for those that are dynamically stable.
- Classification of each (system, layer type, functional) combination as metallic or semiconducting.
The results must be written to the three CSV files under /app/outputs as detailed in the workflow steps.

## Assets

- Quantum ESPRESSO (or equivalent DFT code, e.g., VASP): https://www.quantum-espresso.org/
- Phonopy: phonopy
- SSSP precision pseudopotentials (or equivalent PBE PAW datasets): https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Geometry optimization of XP3 systems
- Role: process
- Action: Build initial crystal structures for bulk (space group R-3m, hexagonal), monolayer (rectangular unit cell with surface reconstruction), and bilayer (hexagonal) for each XP3 (X=C, Si, Ge, Sn, Pb) using published lattice parameters. Perform DFT geometry relaxation with PBE+D3 functional, plane-wave cutoff 500 eV, k-point meshes: 8x8x8 (bulk), 8x8x1 (bilayer), 8x4x1 (monolayer). Optimize lattice vectors and atomic positions until forces < 0.02 eV/Å and total energy change < 1e-4 eV. Store the relaxed structures and final energies.
- Evidence: none

### Step 2: Phonon dispersion and dynamical stability
- Role: scored
- Action: Using the relaxed structures from Step 1, compute phonon dispersions with the finite displacement method via Phonopy. Determine for each system and layer type (bulk, 1L, 2L) whether the phonon spectrum contains only real frequencies (stable) or imaginary frequencies (unstable). Write the stability verdicts to /app/outputs/phonon_stability.csv.
- Output file: `/app/outputs/phonon_stability.csv`
- Format: csv
- Contract: Columns: system (string; element, e.g., C, Si, Ge, Sn, Pb), layer_type (string: bulk/1L/2L), stable (boolean). One row per (system, layer_type).
- Scoring: scored by hidden verifier

### Step 3: Cleavage energy evaluation
- Role: scored
- Action: Construct a 5-layer (5L) slab model for each XP3 system from the relaxed bulk structure. For each X, compute the total energy of the slab at a series of separation distances between a 1L (or 2L) top layer and the remainder, following the energy-distance fitting procedure described in the paper's SI. Extract the cleavage energy for 1L and 2L exfoliation. Write the results to /app/outputs/cleavage_energies.csv.
- Output file: `/app/outputs/cleavage_energies.csv`
- Format: csv
- Contract: Columns: system (string), layer_type (string: 1L or 2L), cleavage_energy (float, J/m^2). One row per (system, layer_type).
- Scoring: scored by hidden verifier

### Step 4: Electronic band structure and band gap determination
- Role: scored (load-bearing)
- Action: Using the relaxed structures from Step 1, compute electronic band structures for each XP3 system in bulk, 1L, and 2L. Perform PBE-level calculations for all; for those dynamically stable according to Step 2, also perform HSE06 hybrid-functional calculations. For every (system, layer_type, functional) combination determine the band gap (eV), gap character (direct/indirect/metallic), and classify as metallic or semiconducting. Write the results to /app/outputs/band_gaps.csv.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: Columns: system (string), layer_type (string: bulk/1L/2L), functional (string: PBE or HSE06), band_gap (float, eV; 0.0 for metallic), gap_type (string: direct, indirect, metallic), classification (string: metallic, semiconducting). One row per (system, layer_type, functional).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_stability.csv`
- `/app/outputs/cleavage_energies.csv`
- `/app/outputs/band_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_stability.csv
- path: `/app/outputs/phonon_stability.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dynamical stability verdicts for all XP3 systems in bulk, monolayer, and bilayer.
- schema:
  - `type`: table
  - `required_columns`: `system`, `layer_type`, `stable`
  - `units`: object

### cleavage_energies.csv
- path: `/app/outputs/cleavage_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cleavage energies for 1L and 2L exfoliation of XP3 materials.
- schema:
  - `type`: table
  - `required_columns`: `system`, `layer_type`, `cleavage_energy`
  - `units`:
    - `cleavage_energy`: J/m^2

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gaps, gap type, and metal/semiconductor classification for XP3 systems at PBE and HSE06 levels.
- schema:
  - `type`: table
  - `required_columns`: `system`, `layer_type`, `functional`, `band_gap`, `gap_type`, `classification`
  - `units`:
    - `band_gap`: eV

Notes: The steps must be executed in the given order; all artifacts are written to /app/outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_stability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "layer_type",
          "stable"
        ],
        "units": {}
      },
      "description": "Dynamical stability verdicts for all XP3 systems in bulk, monolayer, and bilayer."
    },
    {
      "file": "cleavage_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "layer_type",
          "cleavage_energy"
        ],
        "units": {
          "cleavage_energy": "J/m^2"
        }
      },
      "description": "Cleavage energies for 1L and 2L exfoliation of XP3 materials."
    },
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "layer_type",
          "functional",
          "band_gap",
          "gap_type",
          "classification"
        ],
        "units": {
          "band_gap": "eV"
        }
      },
      "description": "Band gaps, gap type, and metal/semiconductor classification for XP3 systems at PBE and HSE06 levels."
    }
  ],
  "notes": "The steps must be executed in the given order; all artifacts are written to /app/outputs."
}
```

## How you are scored
A hidden verifier reads your three CSV files. It independently compares each entry against paper‑derived reference values using domain‑appropriate tolerances (for band gaps and cleavage energies) or exact boolean match (for stability flags). The final score is a weighted combination of the three tasks: band gaps and classification (60 % of total reward), cleavage energies (20 %), and dynamical stability (20 %). Reporting the paper’s numbers without executing the workflow is not sufficient; the verifier’s tolerances are chosen so that only a genuine re‑execution of the computational procedure reliably meets them.
