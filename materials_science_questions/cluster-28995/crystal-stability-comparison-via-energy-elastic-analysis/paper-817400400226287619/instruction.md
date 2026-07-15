# Dynamical Stability of Two-Dimensional Metals from First Principles

## Problem background
Two-dimensional (2D) metals are atomically thin layers that can adopt several crystal structures. Their dynamical stability — whether the lattice vibrations (phonons) remain stable against distortions — is a fundamental property that determines whether a free‑standing monolayer can exist. This work investigates which elemental metals, from the alkali metals to the post‑transition metals, can form dynamically stable 2D structures in the planar hexagonal (HX), buckled honeycomb (bHC), and buckled square (bSQ) geometries, as well as thicker trilayer variants (3HX, 3SQ). The goal is to compute the equilibrium structural parameters and the phonon band structure of a representative set of elements and to classify each structure as dynamically stable or unstable based on the presence of imaginary phonon frequencies.

## Approach
We use density‑functional theory (DFT) and density‑functional perturbation theory (DFPT) to study the dynamical stability of 2D metals. The workflow consists of: (i) computing the reference energy of an isolated atom for each element; (ii) optimizing the geometry (lattice constant and buckling height) of monolayer HX, bHC, bSQ structures, and of thicker 3HX and 3SQ structures for the elements where monolayers are unstable; (iii) extracting the cohesive energy (atom energy minus monolayer energy) and the equilibrium structural parameters; (iv) calculating the phonon band structure across the first Brillouin zone for every optimized geometry; and (v) classifying each structure as dynamically stable (no imaginary phonon frequencies) or unstable. All calculations employ the GGA‑PBE exchange‑correlation functional and public pseudopotentials. Magnetic elements are treated with spin‑polarized calculations where appropriate. The final results are two tables: one with cohesive energies, lattice constants and buckling heights; the second with stability flags.

## Reproduction target
For a selected set of elements that spans groups 1 through 14 (Li, Be, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Al, Sn, plus In for a thicker structure), compute the following for each combination of element and structure (HX, bHC, bSQ, 3HX, 3SQ where applicable):
- Cohesive energy per atom (eV/atom)
- Optimized lattice constant a (Å)
- Buckling height δ (Å, zero for planar HX)
- Dynamical stability flag (True if no imaginary phonon frequencies anywhere in the Brillouin zone, False otherwise)
These quantities must be written to the CSV files `cohesive_energies.csv` and `stability_classification.csv` with the exact schemas specified in the workflow steps. The target is to obtain equilibrium properties and stability classifications that are consistent with a rigorous first‑principles phonon analysis of the selected 2D metals.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PSLibrary pseudopotentials: https://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: Atomic reference energy calculations
- Role: process
- Action: For each element in the selected set (Li, Be, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Al, Sn, as well as In), perform spin‑polarized where appropriate atom‑in‑a‑box DFT calculations to obtain the isolated‑atom total energy ε_atom. Use GGA‑PBE exchange‑correlation functional and the pslibrary pseudopotentials. Place the atom in a sufficiently large cubic simulation cell to minimise spurious interactions. Record the total energy per atom for each element.
- Evidence: `/app/outputs/atomic_energies.csv`

### Step 2: Geometry optimization of 2D structures
- Role: process
- Action: For the same set of elements, perform DFT geometry optimization for the planar hexagonal (HX), buckled honeycomb (bHC) and buckled square (bSQ) monolayers. Additionally, for the elements V, Nb, Ta optimise the 3SQ thicker structure, and for In optimise the 3HX thicker structure. Use the same DFT setup as the atomic calculations, with a k‑point grid appropriate for 2D slabs. Optimise the lattice constant a and the buckling height δ (zero for planar HX) until forces are converged below a tight threshold. Record the optimised total energy per atom, lattice constant a, and buckling height δ for each combination.
- Evidence: `/app/outputs/optimized_geometries.csv`

### Step 3: Cohesive energy extraction
- Role: scored
- Action: For each element and structure combination, compute the cohesive energy per atom E_j = ε_atom − ε_j, where ε_atom is the atomic reference energy from step_01 and ε_j is the optimised total energy per atom from step_02. Write a CSV with columns: element, structure, cohesive_energy_eV_per_atom, lattice_constant_a_A, buckling_height_delta_A (set to 0 for planar HX).
- Output file: `/app/outputs/cohesive_energies.csv`
- Format: csv
- Contract: Columns: element (string), structure (one of HX, bHC, bSQ, 3HX, 3SQ), cohesive_energy_eV_per_atom (float), lattice_constant_a_A (float), buckling_height_delta_A (float, zero for HX).
- Scoring: scored by hidden verifier

### Step 4: Phonon band structure calculations
- Role: process
- Action: For each optimised geometry from step_02, compute the phonon band structure using density‑functional perturbation theory (DFPT) with the same pseudopotentials and cutoffs. Use appropriate q‑point grids for the different structure types (finer for monolayers, possibly coarser for thicker structures). Determine the phonon energies across the first Brillouin zone without spin‑orbit coupling, applying spin‑polarisation only for the magnetic elements Cr, Mn, Fe, Co, Ni where appropriate. Record evidence of completion for every calculation.
- Evidence: `/app/outputs/phonon_completion.json`

### Step 5: Stability classification
- Role: scored (load-bearing)
- Action: For each element and structure, determine dynamical stability from the phonon calculation in step_04: a structure is stable (True) if no phonon mode has an imaginary frequency (negative squared frequency) anywhere in the Brillouin zone; otherwise it is unstable (False). Write a CSV with columns: element, structure, stable (boolean).
- Output file: `/app/outputs/stability_classification.csv`
- Format: csv
- Contract: Columns: element (string), structure (one of HX, bHC, bSQ, 3HX, 3SQ), stable (boolean, True if no imaginary phonon frequencies).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cohesive_energies.csv`
- `/app/outputs/stability_classification.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cohesive_energies.csv
- path: `/app/outputs/cohesive_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Cohesive energies (eV/atom), lattice constants (Å) and buckling heights (Å) for all computed element/structure combinations. Compared to hidden reference values from the literature with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `element`, `structure`, `cohesive_energy_eV_per_atom`, `lattice_constant_a_A`, `buckling_height_delta_A`
  - `units`:
    - `cohesive_energy_eV_per_atom`: eV/atom
    - `lattice_constant_a_A`: Å
    - `buckling_height_delta_A`: Å

### stability_classification.csv
- path: `/app/outputs/stability_classification.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Boolean stability flags for each element/structure combination. Compared to the literature's dynamical stability conclusions (True if no imaginary phonon modes).
- schema:
  - `type`: table
  - `required_columns`: `element`, `structure`, `stable`

Notes: Both scored artifacts are verified against hidden reference data extracted from the paper’s published Table I and stability map, with appropriate numerical tolerances for the cohesive energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cohesive_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "structure",
          "cohesive_energy_eV_per_atom",
          "lattice_constant_a_A",
          "buckling_height_delta_A"
        ],
        "units": {
          "cohesive_energy_eV_per_atom": "eV/atom",
          "lattice_constant_a_A": "Å",
          "buckling_height_delta_A": "Å"
        }
      },
      "description": "Cohesive energies (eV/atom), lattice constants (Å) and buckling heights (Å) for all computed element/structure combinations. Compared to hidden reference values from the literature with tolerance."
    },
    {
      "file": "stability_classification.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "structure",
          "stable"
        ]
      },
      "description": "Boolean stability flags for each element/structure combination. Compared to the literature's dynamical stability conclusions (True if no imaginary phonon modes)."
    }
  ],
  "notes": "Both scored artifacts are verified against hidden reference data extracted from the paper’s published Table I and stability map, with appropriate numerical tolerances for the cohesive energies."
}
```

## How you are scored
A hidden verifier independently evaluates the two scored artifacts (`cohesive_energies.csv` and `stability_classification.csv`). It compares the cohesive energies, lattice constants, buckling heights, and stability flags against a set of reference values (derived from a full independent computation) and computes a reward between 0 and 1. The reward is monotonic in the quality of the reproduction: closer agreement with the reference yields higher reward. The verifier does NOT simply check whether you reported a number; it verifies that the reported quantities are physically consistent with the elements and structures studied. The final score is a weighted combination of the rewards for the two artifacts.
