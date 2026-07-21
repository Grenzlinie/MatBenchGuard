# Off-lattice Grand Canonical Monte Carlo simulations of diamond (111) surface reconstructions

## Problem background
The clean diamond (111) surface can adopt several competing reconstructions, with the (2×1) Pandey chain reconstruction long proposed as the ground state. However, fully threefold coordinated graphite‑like structures at the surface are also energetically competitive for carbon, and a definitive understanding of which structures are stable or meta‑stable, and under what conditions, remains incomplete. This question is important because surface reconstructions influence the electronic properties and the interpretation of experimental probes such as X‑ray diffraction and ion scattering. The aim is to investigate the stability and atomic geometry of possible surface phases using off‑lattice Grand Canonical Monte Carlo simulations.

## Approach
The approach is a computational exploration of the potential energy surface of the diamond (111) slab using the Brenner empirical many‑body potential (parametrization I). The simulation employs off‑lattice Grand Canonical Monte Carlo (GCMC) with tabulated potential terms and an umbrella correction to facilitate atom creation/destruction. A slab of four bilayers is constructed from the bulk diamond lattice, with the bottom layers fixed. The configuration space is explored by annealing in different thermodynamic ensembles (VNT, PNT, PμT) at low and high temperatures. The lowest‑energy configurations are selected and locally minimized. The resulting structures are then compared by their energy gains relative to the bulk‑terminated surface, and the atomic coordinates of the Pandey reconstruction are recorded.

## Reproduction target
Produce a JSON file containing the relative energy ΔE per 1×1 unit cell (in eV) for the Pandey (2×1) reconstruction, the dimerized (2×1) reconstruction, the dimerized (4×1) reconstruction, and the vacancy (√3×√3)R30° reconstruction, as well as the relaxed atomic coordinates (atom labels and x, y, z positions in Å) of the top three bilayers (12 atoms) of the Pandey reconstruction. The slab is initialized from the bulk diamond lattice and the simulations must follow the GCMC annealing protocol described in the workflow steps.

## Assets

- Brenner potential parametrization I: 10.1103/PhysRevB.42.9458

## Workflow steps

### Step 1: Construct initial diamond(111) slab
- Role: process
- Action: Build an initial slab model of the diamond(111) surface with four bilayers (128 atoms per bilayer) using the bulk diamond lattice constant. Fix the bottom layers at their ideal bulk positions.
- Evidence: `/app/outputs/slab_initial.xyz`

### Step 2: Run off-lattice GCMC simulation with Brenner potential
- Role: process
- Action: Implement and execute off-lattice Grand Canonical Monte Carlo (GCMC) simulations using the Brenner potential (parametrization I). Include neighbor lists, tabulated one-dimensional potential terms (VA, VR, fc) as functions of squared interatomic distance with linear interpolation, and the three-dimensional bond-order function F on a fine grid with linear interpolation. Apply an umbrella-energy correction (~2 eV) for atom creation/destruction moves. Perform annealing cycles in VNT, PNT, and PμT ensembles at temperatures around 750 K and 2350 K to allow spontaneous reconstruction and identification of low-energy structures.
- Evidence: `/app/outputs/trajectory_frames.xyz`

### Step 3: Extract relaxed energies and Pandey coordinates
- Role: scored (load-bearing)
- Action: From the simulation runs, select the lowest-energy configurations corresponding to the Pandey (2×1), dimerized (2×1), dimerized (4×1), and vacancy (√3×√3)R30° reconstructions. Perform local energy minimization to obtain fully relaxed coordinates. Compute the relative energy ΔE per 1×1 unit cell for each structure and the relaxed atomic coordinates (x,y,z) of the top three bilayers of the Pandey reconstruction.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: 'pandey_energy_eV' (float, unit eV per 1×1 cell), 'dimer_2x1_energy_eV' (float, eV per 1×1 cell), 'dimer_4x1_energy_eV' (float, eV per 1×1 cell), 'vacancy_sqrt3_energy_eV' (float, eV per 1×1 cell), and 'pandey_coordinates': a list of 12 objects, each with keys 'atom_label' (string), 'x' (float, Å), 'y' (float, Å), 'z' (float, Å).
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
- target_policy: metric_recompute
- description: Energetic and structural result of the GCMC exploration. The energies are the gains ΔE per 1×1 cell relative to the bulk-terminated surface. The coordinates list contains the relaxed positions of the top three bilayers (12 atoms) of the Pandey reconstruction.
- schema:
  - `type`: object
  - `required`:
    - `pandey_energy_eV`: float (eV per 1×1 cell)
    - `dimer_2x1_energy_eV`: float (eV per 1×1 cell)
    - `dimer_4x1_energy_eV`: float (eV per 1×1 cell)
    - `vacancy_sqrt3_energy_eV`: float (eV per 1×1 cell)
    - `pandey_coordinates`: array of objects, each with 'atom_label' (string), 'x' (float, Å), 'y' (float, Å), 'z' (float, Å)

Notes: The checker will recompute energy deviations against the paper's reference values and the root-mean-square deviation (RMSD) of the submitted coordinates against the hidden gold Pandey coordinates from Table I of the paper. Both components contribute to the final reward.

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
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "pandey_energy_eV": "float (eV per 1×1 cell)",
          "dimer_2x1_energy_eV": "float (eV per 1×1 cell)",
          "dimer_4x1_energy_eV": "float (eV per 1×1 cell)",
          "vacancy_sqrt3_energy_eV": "float (eV per 1×1 cell)",
          "pandey_coordinates": "array of objects, each with 'atom_label' (string), 'x' (float, Å), 'y' (float, Å), 'z' (float, Å)"
        }
      },
      "description": "Energetic and structural result of the GCMC exploration. The energies are the gains ΔE per 1×1 cell relative to the bulk-terminated surface. The coordinates list contains the relaxed positions of the top three bilayers (12 atoms) of the Pandey reconstruction."
    }
  ],
  "notes": "The checker will recompute energy deviations against the paper's reference values and the root-mean-square deviation (RMSD) of the submitted coordinates against the hidden gold Pandey coordinates from Table I of the paper. Both components contribute to the final reward."
}
```

## How you are scored
A hidden verifier reads your `results.json` and independently checks each quantity. The energy values are compared to reference energy gains using a tolerance‑based criterion; the Pandey coordinates are evaluated via root‑mean‑square deviation against a reference set of atomic positions. Each component contributes a predefined weight to the final score, which is a single number between 0 (no match) and 1 (perfect reproduction of the target quantities). The verifier does not disclose the reference values or the tolerances. You do not need to match any particular implementation detail — only that the reported energies and coordinates fall within the acceptable agreement with the expected results for a correct simulation.
