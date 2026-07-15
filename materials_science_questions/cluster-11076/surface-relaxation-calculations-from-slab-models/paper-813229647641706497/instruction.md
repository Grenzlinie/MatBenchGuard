# DFT step-edge displacement calculations for MgO(100) surface

## Problem background
MgO is a model oxide surface widely used as a substrate and catalyst, but the atomic-scale structure of steps on its (100) surface has been challenging to measure experimentally. Steps introduce under-coordinated atoms that can relax significantly, affecting surface reactivity and thin-film growth. Understanding these displacements quantitatively is important for catalytic and deposition applications. This task aims to compute the relaxation-driven changes in bond lengths, bond angles, atomic rumpling, and step formation energies at monoatomic steps on MgO(100) using density functional theory.

## Approach
The computational approach uses density functional theory (DFT) with the PBE exchange-correlation functional to relax slab models of the MgO surface. Bulk MgO is first computed to obtain the equilibrium lattice parameter. Then a flat 7-layer MgO(001) slab with vacuum is relaxed to determine the flat surface energy and to serve as a reference. The stepped surface is modeled by a (107) slab containing monoatomic steps: 7 atomic layers, step spacing of 7 interatomic distances along [100], and ~10 Å vacuum. Both an unrelaxed single-point calculation and a full ionic relaxation are performed on this stepped slab. From the relaxed stepped structure, the positions of Mg and O atoms at the low-coordination step-edge sites are used to compute projected bond lengths and bond angles between specific atom pairs/triplets, as well as in-plane and out-of-plane rumpling for each site. Finally, step formation energies (relaxed and unrelaxed) are derived from the total energies of the flat and stepped slabs.

## Reproduction target
Using the DFT-relaxed stepped MgO(107) slab, compute the following quantities and write them to CSV files:

1. **Step-edge bond lengths and angles**: For the atom pairs and triplets at the step-edge positions (1–8) as labeled in the method, compute the projected bond lengths (in Å) for: Mg8–O1, O8–Mg1, Mg1–O2, O1–Mg2, Mg2–O3, O2–Mg3; and the bond angles (in degrees) for: Mg8–O1–Mg2, O8–Mg1–O2, Mg1–O2–Mg3, O1–Mg2–O3. Write a CSV with columns parameter, value, unit.

2. **In-plane and out-of-plane rumpling**: For each step-site position (1–8), compute out-of-plane rumpling = (z_O – z_Mg) / d_b and in-plane rumpling = (y_Mg – y_O) / d_b, where d_b is the bulk {200} interlayer spacing (a_DFT/2). Write a CSV with columns position, out_of_plane_rumpling (Å), in_plane_rumpling (Å).

3. **Step formation energies**: From the total energies E_bulk (per formula unit), E_flat, E_stepped_relaxed, and E_stepped_unrelaxed, compute the relaxed and unrelaxed step formation energies per unit step length γ = (E_stepped – E_flat) / l, where l is the total step length in the supercell (2 steps of length a_0 along [010], with a_0 the bulk lattice constant). Express γ in meV/Å. Write a CSV with columns energy_type (either 'relaxed' or 'unrelaxed') and gamma.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE (Atomic Simulation Environment): ase

## Workflow steps

### Step 1: Bulk MgO DFT calculation
- Role: process
- Action: Perform a DFT calculation on bulk MgO (rock-salt) using PBE exchange-correlation, obtaining the equilibrium lattice parameter a_DFT and total energy per formula unit E_bulk. Save the lattice parameter and total energy to a text file.
- Evidence: `/app/outputs/bulk_results.txt`

### Step 2: Flat MgO(001) slab relaxation
- Role: process
- Action: Construct a symmetric 7-layer MgO(001) slab using the DFT equilibrium lattice parameter, with at least 10 Å vacuum. Perform ionic relaxation (cell fixed) with the same functional, cutoff and an ~11x11x1 k-point mesh. Save the relaxed total energy E_flat and the relaxed atomic structure (e.g., CIF format).
- Evidence: `/app/outputs/flat_slab_energy.txt, flat_slab_structure.cif`

### Step 3: Unrelaxed stepped slab total energy
- Role: process
- Action: Build a MgO(107) slab with monoatomic steps: 7 atomic layers, step spacing of 7 interatomic distances along [100], vacuum ~10 Å. Without ionic relaxation, compute the total energy E_stepped_unrelaxed using the same DFT parameters. Save this total energy.
- Evidence: `/app/outputs/step_slab_unrelaxed_energy.txt`

### Step 4: Relaxed stepped MgO(107) slab relaxation
- Role: process
- Action: Using the same stepped slab model, relax all ionic positions (cell fixed). Save the relaxed total energy E_stepped_relaxed and the relaxed atomic structure (e.g., CIF).
- Evidence: `/app/outputs/step_slab_relaxed_energy.txt, step_slab_structure.cif`

### Step 5: Compute step-edge bond lengths and angles
- Role: scored (load-bearing)
- Action: From the relaxed stepped slab structure, identify Mg and O atoms at low-coordination step-edge sites (positions 1–8). Compute projected bond lengths and angles for the specific pairs and triplets described in the paper: Mg8–O1, O8–Mg1, Mg1–O2, O1–Mg2, Mg2–O3, O2–Mg3 (bond lengths) and Mg8–O1–Mg2, O8–Mg1–O2, Mg1–O2–Mg3, O1–Mg2–O3 (bond angles). Write results as a CSV file.
- Output file: `/app/outputs/bond_lengths_angles.csv`
- Format: csv
- Contract: columns: parameter (string), value (float), unit (string)
- Scoring: scored by hidden verifier

### Step 6: Compute in-plane and out-of-plane rumpling
- Role: scored (load-bearing)
- Action: Using the relaxed stepped slab structure, for each step-site position 1–8 compute out-of-plane rumpling = (z_O - z_Mg)/d_b and in-plane rumpling = (y_Mg - y_O)/d_b, where d_b is the bulk {200} interlayer spacing (a_DFT/2). Output results as a CSV file with rumpling in Å.
- Output file: `/app/outputs/rumpling.csv`
- Format: csv
- Contract: columns: position (int), out_of_plane_rumpling (float, Å), in_plane_rumpling (float, Å)
- Scoring: scored by hidden verifier

### Step 7: Compute step formation energies
- Role: scored (load-bearing)
- Action: From the total energies E_bulk (per formula unit), E_flat, E_stepped_relaxed, and E_stepped_unrelaxed, compute relaxed and unrelaxed step formation energies per unit step length γ = (E_stepped - E_flat) / l, where l is the total step length in the supercell (2 steps of length a_0 along [010]). Convert to meV/Å. Write a CSV with energy_type and gamma.
- Output file: `/app/outputs/step_energies.csv`
- Format: csv
- Contract: columns: energy_type (string, 'relaxed' or 'unrelaxed'), gamma (float, meV/Å)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bond_lengths_angles.csv`
- `/app/outputs/rumpling.csv`
- `/app/outputs/step_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bond_lengths_angles.csv
- path: `/app/outputs/bond_lengths_angles.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed bond lengths (in Å) and bond angles (in degrees) for the specified step-edge atom pairs and triplets. Values will be compared to hidden reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `parameter`, `value`, `unit`

### rumpling.csv
- path: `/app/outputs/rumpling.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Out-of-plane and in-plane rumpling (in Å) for each step-site position 1–8. Values will be compared to hidden reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `position`, `out_of_plane_rumpling`, `in_plane_rumpling`

### step_energies.csv
- path: `/app/outputs/step_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Relaxed and unrelaxed step formation energies (meV/Å). Values will be compared to hidden paper-reported values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `energy_type`, `gamma`

Notes: All scored outputs are re-derivable from the agent's DFT artifacts. The checker will read these CSV files and verify values against hidden gold within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bond_lengths_angles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter",
          "value",
          "unit"
        ]
      },
      "description": "Computed bond lengths (in Å) and bond angles (in degrees) for the specified step-edge atom pairs and triplets. Values will be compared to hidden reference values within tolerance."
    },
    {
      "file": "rumpling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "position",
          "out_of_plane_rumpling",
          "in_plane_rumpling"
        ]
      },
      "description": "Out-of-plane and in-plane rumpling (in Å) for each step-site position 1–8. Values will be compared to hidden reference values within tolerance."
    },
    {
      "file": "step_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_type",
          "gamma"
        ]
      },
      "description": "Relaxed and unrelaxed step formation energies (meV/Å). Values will be compared to hidden paper-reported values within tolerance."
    }
  ],
  "notes": "All scored outputs are re-derivable from the agent's DFT artifacts. The checker will read these CSV files and verify values against hidden gold within appropriate tolerances."
}
```

## How you are scored
After you submit your output files, a hidden verifier will read each CSV and compare every numerical value to the expected result (computed from a reference DFT calculation). Each value is assigned a tolerance: if your value lies within the tolerance of the expected value, you earn full credit for that entry; if it deviates beyond tolerance, the credit decreases linearly with the absolute deviation (exact_match scoring). The total score is a weighted sum over all entries across the three files. To achieve a high score, your DFT calculations must fully relax the stepped slab and accurately extract the geometric and energetic quantities; merely reporting the correct numbers without genuine computation will result in a low score because the verifier checks multiple quantities that are interdependent and cannot be guessed without the actual relaxed structure.
