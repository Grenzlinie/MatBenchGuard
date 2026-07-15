# Lithium Migration Barrier in LiTi2(PO4)3 via Molecular Mechanics

## Problem background
Lithium titanium phosphate (LTP, LiTi2(PO4)3) is a solid electrolyte candidate for all-solid-state lithium batteries. Understanding the Li+ diffusion pathway and the activation barrier is crucial for optimizing ionic conductivity. Experiments can measure bulk and grain-boundary conductivities, but theoretical modeling is needed to identify the diffusion path and the energy landscape for lithium hopping. The crystal structure consists of a three-dimensional network of PO4 tetrahedra and TiO6 octahedra, with lithium occupying interstitial sites. The main diffusion channel has been proposed to run along Li(1)–Li(2)–Li(1) sites, by analogy with NASICON-type materials. The goal of this task is to compute the migration barrier (activation energy) for a single Li+ ion moving along this path using molecular mechanics.

## Approach
The simulation uses classical molecular mechanics with a modified Universal Force Field (UFF), which models bonded (bonds, angles) and non-bonded (van der Waals, Coulomb) interactions. Partial charges are assigned via the charge equilibration (QEq) method. The force-field parameters (natural bond lengths and angles) for Al–O, P–O, Ti–O, and the O–X–O and X–O–P angles are taken from the literature on NASICON compounds. Periodic boundary conditions are applied to a single unit cell containing 6 formula units (108 atoms), and long-range electrostatics are handled by Ewald summation. The experimental unit-cell parameters are fixed, while atomic positions are relaxed by energy minimization. First, the ground-state configuration with all Li ions at the crystallographic Li(1) sites is optimized. Then, a single Li+ is moved to an interstitial Li(2) site (coordinates deduced from NASICON analogues), the migrating lithium and all titanium atoms are constrained, and the remaining atoms are relaxed to obtain the transition-state energy. The migration barrier is the energy difference between the transition-state and ground-state configurations.

## Reproduction target
Using the described molecular mechanics setup, compute the lithium migration barrier for the Li(1)→Li(2)→Li(1) diffusion path in crystalline LiTi2(PO4)3. Produce a JSON file containing the ground-state total energy (kJ/mol per unit cell), the transition-state total energy (kJ/mol per unit cell), the barrier in kJ/mol, and the barrier in eV. Ensure that the barrier is positive and corresponds to the difference between the transition-state and ground-state energies.

## Assets

- LiTi2(PO4)3 crystal structure (CIF file): https://www.crystallography.net/cod/2002926.html
- Molecular mechanics engine with UFF and QEq support: lammps

## Workflow steps

### Step 1: Build LiTi2(PO4)3 unit cell
- Role: process
- Action: Obtain the crystal structure (space group R-3c, atomic coordinates) from a public crystallographic database and construct a simulation box containing one unit cell (108 atoms, 6 formula units). All Li ions are initially placed at the crystallographic Li(1) sites.
- Evidence: none

### Step 2: Set up modified UFF force field and simulation parameters
- Role: process
- Action: Implement the modified Universal Force Field with parameters: natural bond lengths Al–O 1.885 Å, P–O 1.520 Å, Ti–O 1.955 Å; natural bond angles O–Al–O 90°, O–Ti–O 90°, O–P–O 109.4712°, Ti–O–P 145.50°, Al–O–P 145.50°. Apply periodic boundary conditions, use Ewald summation for long-range electrostatics, and assign partial charges via charge equilibration (QEq).
- Evidence: none

### Step 3: Ground state energy minimization
- Role: process
- Action: Perform a geometry optimization (energy minimization) of the unit cell with all Li ions on Li(1) sites, keeping the experimental unit cell parameters fixed; only atomic positions are relaxed. Record the minimum total energy of the ground-state configuration.
- Evidence: none

### Step 4: Transition state energy minimization and migration barrier
- Role: scored (load-bearing)
- Action: Construct the transition state by moving one Li+ ion from its Li(1) site to an interstitial Li(2) position (coordinates deduced from NASICON analogues). Fix the migrating Li ion and all Ti atoms; relax the remaining atoms while keeping unit cell dimensions fixed. Minimize the energy and compute the energy difference ΔE = E_transition − E_ground. Report both energies and the barrier in kJ/mol and eV.
- Output file: `/app/outputs/migration_barrier.json`
- Format: json
- Contract: A JSON object with numeric fields: ground_state_energy (kJ/mol per unit cell), transition_state_energy (kJ/mol per unit cell), barrier_kJmol (kJ/mol), barrier_eV (eV). All values must be present.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_barrier.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_barrier.json
- path: `/app/outputs/migration_barrier.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The migration barrier and the component energies after MM optimization.
- schema:
  - `type`: object
  - `required`:
    - `ground_state_energy`: number (kJ/mol per unit cell)
    - `transition_state_energy`: number (kJ/mol per unit cell)
    - `barrier_kJmol`: number (kJ/mol)
    - `barrier_eV`: number (eV)

Notes: The verifier will recompute barrier_eV from the reported energies and compare the result to the expected value with a tolerance. The MM engine must support the UFF force field and charge equilibration.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ground_state_energy": "number (kJ/mol per unit cell)",
          "transition_state_energy": "number (kJ/mol per unit cell)",
          "barrier_kJmol": "number (kJ/mol)",
          "barrier_eV": "number (eV)"
        }
      },
      "description": "The migration barrier and the component energies after MM optimization."
    }
  ],
  "notes": "The verifier will recompute barrier_eV from the reported energies and compare the result to the expected value with a tolerance. The MM engine must support the UFF force field and charge equilibration."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/migration_barrier.json`. It will recompute the barrier as `transition_state_energy − ground_state_energy` and compare the resulting value (in eV) against a hidden reference value within an appropriate tolerance. It will also verify that the reported energies are internally consistent and lie within physically plausible ranges. Partial credit may be awarded if the result is close to the expected value but not exact. The reward is a single float between 0 and 1 based on the agreement.
