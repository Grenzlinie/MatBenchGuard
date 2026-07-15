# Reproducing Lattice Constants and Band Gaps of Perovskite Heterostructures via Hybrid DFT

## Problem background
Ba<sub>0.5</sub>Sr<sub>0.5</sub>TiO<sub>3</sub> (BST) is a perovskite solid solution of great technological interest, particularly for memory device applications. First‑principles electronic structure calculations are essential to understand its properties, but pure end members BaTiO<sub>3</sub> and SrTiO<sub>3</sub> are themselves challenging for standard density‑functional theory (DFT) approaches, which often mis‑predict lattice constants and band gaps. The present task uses a hybrid density functional with Gaussian basis sets and effective core potentials to perform accurate periodic DFT calculations. The goal is to compute equilibrium lattice constants and optical band gaps for cubic BaTiO<sub>3</sub>, SrTiO<sub>3</sub>, and an equiatomic layered Ba<sub>0.5</sub>Sr<sub>0.5</sub>TiO<sub>3</sub> heterostructure, and to compare the computed lattice constants with experimental references to assess the method’s accuracy, as well as to determine how the band gap changes in the solid solution relative to the pure parent compounds.

## Approach
The electronic structure calculations employ the hybrid B3PW exchange‑correlation functional, which mixes a fraction of exact Hartree‑Fock exchange with a gradient‑corrected DFT functional. Small‑core Hay–Wadt effective core potentials (ECPs) replace the inner core electrons of Ti, Sr, and Ba, while oxygen is treated with an all‑electron basis. The Gaussian basis sets are contracted as O [8‑411(1d)G], Ti [411(311d)G], Sr [311(1d)G], and Ba [311(1d)G]. The primitive cubic perovskite cell is used for BaTiO<sub>3</sub> and SrTiO<sub>3</sub>. For the solid solution, a 2×2×2 supercell (40 atoms) is constructed with a layered ordering of Ba and Sr along one direction, creating an equiatomic composition. Geometry optimisations are performed for all three systems to find the equilibrium lattice parameters, followed by band‑structure calculations to extract the optical band gap (energy difference at the Γ point between the top of the valence band and the bottom of the conduction band). Additional qualitative analyses (density of states and electron density difference maps) are also carried out to examine bonding character.

## Reproduction target
Compute and report the following quantities in a single JSON file:
- Optimised lattice constants (in ångströms) for cubic BaTiO<sub>3</sub>, cubic SrTiO<sub>3</sub>, and the layered Ba<sub>0.5</sub>Sr<sub>0.5</sub>TiO<sub>3</sub> supercell.
- Optical band gaps (in electronvolts) for the same three systems.

For the pure end members, the computed lattice constants should be compared with known experimental values as a validation of the computational scheme. For the solid solution, determine whether its band gap differs from that of pure SrTiO<sub>3</sub>, and if so, by what magnitude. The final numeric results must be collected in `/app/outputs/computed_properties.json` according to the schema specified in the output contract.

## Assets

- Periodic DFT code (e.g., NWChem, PySCF) supporting B3PW hybrid functional, Gaussian basis sets, and effective core potentials: https://nwchemgit.github.io
- Gaussian basis set contractions for O, Ti, Sr, Ba (Piskunov et al. 2004): 10.1016/j.commatsci.2003.10.017
- Hay-Wadt small-core effective core potentials for Ti, Sr, Ba: https://www.basissetexchange.org

## Workflow steps

### Step 1: Optimize BaTiO3 geometry
- Role: process
- Action: Perform hybrid DFT (B3PW) geometry optimization on the cubic primitive cell of BaTiO3 to obtain the equilibrium lattice constant and ground-state wavefunction.
- Evidence: `/app/outputs/batio3_opt.out`

### Step 2: Optimize SrTiO3 geometry
- Role: process
- Action: Perform hybrid DFT geometry optimization on the cubic primitive cell of SrTiO3 to obtain the equilibrium lattice constant and ground-state wavefunction.
- Evidence: `/app/outputs/srtio3_opt.out`

### Step 3: Construct BST supercell
- Role: process
- Action: Generate a 2x2x2 supercell of the cubic ABO3 perovskite with layered Ba/Sr ordering to create the equiatomic Ba0.5Sr0.5TiO3 structure.
- Evidence: `/app/outputs/bst_supercell.inp`

### Step 4: Optimize BST supercell geometry
- Role: process
- Action: Perform hybrid DFT geometry optimization on the BST supercell to find the equilibrium lattice constant, keeping all atoms fixed at their fractional positions.
- Evidence: `/app/outputs/bst_opt.out`

### Step 5: Compute electronic band structures
- Role: process
- Action: Calculate the band structure for the optimized BaTiO3, SrTiO3, and BST supercell along high-symmetry paths and extract the optical band gap (energy difference at the Gamma point between top of valence band and bottom of conduction band).
- Evidence: `/app/outputs/band_gaps.json`

### Step 6: Generate DOS and electron density maps
- Role: process
- Action: Compute total and partial density of states for the BST supercell, and difference electron density maps (total minus ionic superposition) in the (001) and (110) planes to analyze covalency and electron localization.
- Evidence: `/app/outputs/dos_plot.png`

### Step 7: Collect results into a scored JSON file
- Role: scored (load-bearing)
- Action: Write the optimized lattice constants (in ångströms) and optical band gaps (in eV) for BaTiO3, SrTiO3, and the BST supercell into a single JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: {"BaTiO3_lattice_constant_A": float, "SrTiO3_lattice_constant_A": float, "BST_supercell_lattice_constant_A": float, "BaTiO3_band_gap_eV": float, "SrTiO3_band_gap_eV": float, "BST_band_gap_eV": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: JSON file containing the lattice constants (Å) and optical band gaps (eV) for BaTiO3, SrTiO3, and the layered Ba0.5Sr0.5TiO3 supercell, as produced by the hybrid DFT workflow.
- schema:
  - `type`: object
  - `required`:
    - `BaTiO3_lattice_constant_A`: float
    - `SrTiO3_lattice_constant_A`: float
    - `BST_supercell_lattice_constant_A`: float
    - `BaTiO3_band_gap_eV`: float
    - `SrTiO3_band_gap_eV`: float
    - `BST_band_gap_eV`: float

Notes: The qualitative DOS and electron density difference maps are produced as process evidence but are not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "BaTiO3_lattice_constant_A": "float",
          "SrTiO3_lattice_constant_A": "float",
          "BST_supercell_lattice_constant_A": "float",
          "BaTiO3_band_gap_eV": "float",
          "SrTiO3_band_gap_eV": "float",
          "BST_band_gap_eV": "float"
        }
      },
      "description": "JSON file containing the lattice constants (Å) and optical band gaps (eV) for BaTiO3, SrTiO3, and the layered Ba0.5Sr0.5TiO3 supercell, as produced by the hybrid DFT workflow."
    }
  ],
  "notes": "The qualitative DOS and electron density difference maps are produced as process evidence but are not scored."
}
```

## How you are scored
A hidden verifier independently checks the artifacts you produce at each workflow stage. For the scored step (computed_properties.json), the verifier will read your reported lattice constants and band gaps, compare them against reference values derived from the published literature, and evaluate whether the band‑gap trend between the pure SrTiO<sub>3</sub> and the BST supercell is physically meaningful. The comparison uses tolerances appropriate for independent code implementations. The exact reference values and tolerances are hidden; simply reporting numbers is not sufficient — you must execute the full DFT workflow to produce genuine results. Different stages may carry different weights in the final combined reward.
