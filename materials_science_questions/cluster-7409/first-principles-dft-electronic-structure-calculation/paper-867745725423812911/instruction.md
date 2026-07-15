# DFT+GW Prediction of a 2D Carbon Allotrope (Octite SC)

## Problem background
Graphene, a single layer of carbon atoms arranged in a honeycomb lattice, possesses exceptional mechanical strength and extremely high electron mobility, but it is a semi-metal with no intrinsic band gap, which limits its use in logic circuits. To enable carbon-based electronics, it is desirable to open a band gap in a planar all-carbon material without relying on external substrates, chemical functionalisation, or confinement boundaries. One promising route is the introduction of periodic patterns of lattice defects that break the sublattice symmetry and create a gap. A recently predicted planar, single-layer carbon allotrope named Octite SC is built from an arrangement of divacancy and Stone–Thrower–Wales defects, resulting in a square primitive cell with 28 atoms. Computational first-principles simulations indicate that Octite SC is a semiconductor. The task is to reproduce the key structural and electronic properties of Octite SC using density functional theory and many-body perturbation theory, thereby validating the concept of defect-engineered semiconducting graphene allotropes.

## Approach
The central idea is to construct the atomic geometry of Octite SC from its symmetry and bonding pattern, then use plane-wave density functional theory (DFT) to relax the structure, and finally apply the GW approximation to obtain a more accurate electronic band gap. The reference system for energetics is pristine graphene, relaxed with the same DFT settings. Specifically, you will:
- Build the 28-atom primitive cell with p4/MMM symmetry, where carbon atoms form rings of pentagons, hexagons and octagons, with each central octagon completely surrounded by hexagons.
- Perform a DFT structural relaxation with the Perdew–Burke–Ernzerhof (PBE) functional; this yields the equilibrium lattice constant, planar atomic density, and total energy.
- Relax a graphene unit cell under the same conditions to obtain a reference energy per carbon atom.
- Compute the Kohn–Sham band structure on a dense k‑point grid to extract the direct band gap at the Γ point.
- Carry out a G₀W₀ (or GW₀) quasiparticle calculation using the DFT wavefunctions as a starting point to determine the Γ‑point direct band gap including many‑body effects.
All calculations can be performed with the open‑source codes Quantum ESPRESSO (pw.x) and Yambo, together with standard PBE pseudopotentials for carbon. The complete workflow is detailed in the numbered steps below. The outputs of these calculations are then post‑processed to produce the five headline quantities listed in the reproduction target.

## Reproduction target
Produce a single JSON file named `results.json` containing the following five numeric quantities computed for Octite SC:
- `lattice_constant_A`: the relaxed lattice constant in angstroms.
- `planar_density_atoms_per_A2`: the planar atomic density in atoms per square angstrom, calculated as the number of atoms in the unit cell divided by the cell area.
- `energy_relative_to_graphene_meV_per_atom`: the energy per atom of Octite SC minus the energy per atom of pristine graphene, expressed in millielectronvolts per atom.
- `dft_band_gap_eV`: the direct band gap at the Γ point obtained from the DFT band structure, in electronvolts.
- `gw_band_gap_eV`: the direct band gap at the Γ point obtained from the GW quasiparticle correction, in electronvolts.
All intermediate steps (structure generation, DFT relaxations, band structure calculation, and GW correction) must be executed in sequence, using the open‑source tools and pseudopotentials listed in the Assets section. The final values must be written into `results.json` following the exact JSON schema shown in Step 6.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Yambo: https://www.yambo-code.eu/
- PBE pseudopotentials for carbon: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build initial Octite SC structure
- Role: process
- Action: Construct the 28-atom primitive cell of Octite SC with square p4/MMM symmetry, containing rings of pentagons, hexagons and octagons, with the central octagon completely surrounded by hexagons. Save the initial structure in a suitable input format (e.g., POSCAR or xyz).
- Evidence: `/app/outputs/initial_octite_structure.xyz`

### Step 2: DFT relaxation of Octite SC
- Role: process
- Action: Perform a plane-wave DFT structural relaxation on the Octite SC structure using the PBE functional until forces converge. Save the fully relaxed structure, total energy, and cell vectors.
- Evidence: `/app/outputs/octite_relaxed.out`

### Step 3: DFT relaxation of pristine graphene
- Role: process
- Action: Relax a pristine graphene unit cell using the same plane-wave DFT settings as step_02 to obtain the reference total energy per atom. Save the graphene total energy.
- Evidence: `/app/outputs/graphene_relaxed.out`

### Step 4: DFT band structure calculation
- Role: process
- Action: Using the relaxed Octite SC structure, perform a non-self-consistent band structure calculation with a dense Γ-centered k-point grid to obtain the Kohn-Sham eigenvalues and extract the direct band gap at the Γ point. Save the band energies.
- Evidence: `/app/outputs/octite_bands.dat`

### Step 5: GW quasiparticle correction
- Role: process
- Action: Using the DFT wavefunctions and eigenvalues from step_04, run a G0W0 (or GW0) calculation with Yambo to obtain the quasiparticle band structure. Extract the direct band gap at the Γ point.
- Evidence: `/app/outputs/gw_bandgap.log`

### Step 6: Compile scored summary
- Role: scored (load-bearing)
- Action: From the outputs of steps 02–05, compute the five target quantities: (1) relaxed lattice constant (Å), (2) planar atomic density (atoms/Å²), (3) energy per atom relative to graphene (meV/atom), (4) DFT direct band gap at Γ (eV), and (5) GW direct band gap at Γ (eV). Write these values to results.json with the exact keys specified.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "lattice_constant_A": <numeric>,
  "planar_density_atoms_per_A2": <numeric>,
  "energy_relative_to_graphene_meV_per_atom": <numeric>,
  "dft_band_gap_eV": <numeric>,
  "gw_band_gap_eV": <numeric>
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing the seven computed structural and electronic properties of Octite SC and the embedded ribbon.
- schema:
  - `type`: object
  - `required`:
    - `lattice_constant_A`: number
    - `planar_density_atoms_per_A2`: number
    - `energy_relative_to_graphene_meV_per_atom`: number
    - `dft_band_gap_eV`: number
    - `gw_band_gap_eV`: number
    - `max_z_deviation_A`: number
    - `ribbon_dft_band_gap_eV`: number

Notes: No gold values or tolerances disclosed. The ribbon planarity deviation and band gap are scored with a threshold to verify planarity and semiconducting character.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "lattice_constant_A": "number",
          "planar_density_atoms_per_A2": "number",
          "energy_relative_to_graphene_meV_per_atom": "number",
          "dft_band_gap_eV": "number",
          "gw_band_gap_eV": "number",
          "max_z_deviation_A": "number",
          "ribbon_dft_band_gap_eV": "number"
        }
      },
      "description": "JSON file containing the seven computed structural and electronic properties of Octite SC and the embedded ribbon."
    }
  ],
  "notes": "No gold values or tolerances disclosed. The ribbon planarity deviation and band gap are scored with a threshold to verify planarity and semiconducting character."
}
```

## How you are scored
A hidden verifier reads your `results.json` and compares each of the five fields to a set of reference values. The reward for the task ranges from 0 to 1, with credit distributed equally among the five quantities. For each field, you receive partial credit proportional to how close your computed value is to the reference, up to a per‑field tolerance that accounts for the typical numerical differences arising from the use of different DFT and GW implementations. No single field dominates the score, and obtaining the correct numbers for all five properties yields the maximum reward. Simply reporting plausible values is not enough; the values must result from the full workflow described in the steps above. The verifier does not inspect intermediate files directly; the score is determined solely from the contents of `results.json`.
