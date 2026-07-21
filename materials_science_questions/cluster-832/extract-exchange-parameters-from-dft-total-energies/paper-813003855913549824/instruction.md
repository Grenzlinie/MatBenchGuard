# Extract magnetic exchange parameters and Cu 3d orbital populations from B3LYP total energies of pure and Mg-doped KCuF3

## Problem background
KCuF3 is a pseudocubic perovskite that exhibits quasi‑one‑dimensional antiferromagnetism, orbital ordering of the Cu 3d electrons, and a cooperative Jahn‑Teller distortion. The Cu ions (3d⁹) have one unpaired electron; strong superexchange along the crystallographic c axis gives a large antiferromagnetic coupling, while much weaker ferromagnetic coupling occurs within the ab planes. Substituting Cu with Mg (composition KCu₀.₈₇₅Mg₀.₁₂₅F₃) dilutes the magnetic lattice and modifies the local geometry around the dopant. Understanding how Mg doping affects the electronic structure, orbital populations, and the effective magnetic exchange parameters J_ab and J_c is important for disentangling spin, orbital, and lattice degrees of freedom in strongly correlated systems.

## Approach
The method uses periodic density‑functional theory (DFT) with the B3LYP hybrid functional. Two systems are studied: pure KCuF3 and a supercell of composition KCu₀.₈₇₅Mg₀.₁₂₅F₃ where one Cu is replaced by Mg. For each system the geometry of the antiferromagnetic AF1 phase is optimized. Using the optimized structures, total energies are computed for four magnetic orderings (AF1, AF2, AF3, F) within a Pmmm supercell. The energy differences are mapped onto an Ising model to extract the effective superexchange parameters J_ab (within the ab plane) and J_c (along the c axis). Mulliken population analysis of the converged wavefunctions of the AF1 phase yields the occupancies of the five Cu 3d orbitals (d_xy, d_xz, d_yz, d_z², d_x²−y²), revealing the orbital ordering pattern.

## Reproduction target
For both pure and Mg‑doped KCuF3, run the DFT workflow to produce the three scored artifacts:

- `total_energies.csv` containing the total energies (in atomic units) for the AF1, AF2, AF3, and F magnetic phases.
- `magnetic_coupling.json` giving J_ab and J_c (in Kelvin) derived from the energy differences via the Ising model.
- `mulliken_orbitals.json` listing the 3d orbital occupations for each unique Cu atom in the AF1 phase.

The goal is to complete the computational pipeline so that a verifier can independently check the energy ordering of the phases, the effect of Mg doping on the energy differences, the sign and approximate magnitude of the exchange parameters, and the orbital ordering pattern.

## Assets

- CP2K: https://www.cp2k.org
- GTH pseudopotentials and basis sets for K, Cu, F, Mg

## Workflow steps

### Step 1: Optimize geometry of pure KCuF3 AF1 phase
- Role: process
- Action: Perform geometry optimization of pure KCuF3 in the AF1 magnetic configuration using B3LYP, optimizing cell parameters a, c and the fluorine fractional coordinate x_F.
- Evidence: `/app/outputs/pure_af1_geom.log`

### Step 2: Optimize geometry of Mg-doped KCuF3 AF1 phase
- Role: process
- Action: Construct a supercell of KCuF3 with one Cu replaced by Mg (composition KCu0.875Mg0.125F3). Optimize cell parameters a', c' and the positions of the six fluorine atoms nearest to Mg, within the AF1 magnetic ordering.
- Evidence: `/app/outputs/doped_af1_geom.log`

### Step 3: Compute total energies of pure KCuF3 in four magnetic phases
- Role: process
- Action: Using the optimized pure geometry, compute total energies at the B3LYP level for the AF1, AF2, AF3, and F magnetic orderings. Extract total energy per cell (in atomic units) and the Cu magnetic moment S.
- Evidence: `/app/outputs/pure_energies.txt`

### Step 4: Compute total energies of Mg-doped KCuF3 in four magnetic phases
- Role: process
- Action: Using the optimized doped geometry, compute total energies for the AF1, AF2, AF3, and F magnetic orderings. Extract total energy per cell (a.u.) and average Cu magnetic moment S.
- Evidence: `/app/outputs/doped_energies.txt`

### Step 5: Compile total energies into CSV
- Role: scored
- Action: Compile the total energies from the pure and doped runs into a CSV file with columns: system (pure or doped), phase (AF1, AF2, AF3, F), and total_energy (atomic units).
- Output file: `/app/outputs/total_energies.csv`
- Format: csv
- Contract: system (pure/doped), phase (AF1,AF2,AF3,F), total_energy (a.u.)
- Scoring: scored by hidden verifier

### Step 6: Extract magnetic coupling parameters J_ab and J_c via Ising model mapping
- Role: scored (load-bearing)
- Action: Apply the Ising model using total energy differences and the averaged Cu magnetic moment S. Compute J_ab and J_c (in Kelvin) for both pure and doped systems and write them to magnetic_coupling.json.
- Output file: `/app/outputs/magnetic_coupling.json`
- Format: json
- Contract: {"pure": {"J_ab": float (K), "J_c": float (K)}, "doped": {"J_ab": float (K), "J_c": float (K)}}
- Scoring: scored by hidden verifier

### Step 7: Compute Cu 3d orbital populations from Mulliken analysis
- Role: scored (load-bearing)
- Action: Perform Mulliken population analysis on the converged wavefunctions of the AF1 phase for both pure and doped systems. For each unique Cu atom type, extract the occupancies of d_xy, d_xz, d_yz, d_z2, and d_x2-y2 orbitals and write them to mulliken_orbitals.json.
- Output file: `/app/outputs/mulliken_orbitals.json`
- Format: json
- Contract: {"pure": {"Cu": {"d_xy": float, "d_xz": float, "d_yz": float, "d_z2": float, "d_x2-y2": float}}, "doped": {"Cu_type1": {...}, "Cu_type2": {...}, ...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/total_energies.csv`
- `/app/outputs/magnetic_coupling.json`
- `/app/outputs/mulliken_orbitals.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### total_energies.csv
- path: `/app/outputs/total_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Compiled total energies of pure and Mg-doped KCuF3 in four magnetic orderings. The verifier checks energy ordering and the reduction of energy differences upon doping.
- schema:
  - `type`: table
  - `required`:
    - `system`: string (pure or doped)
    - `phase`: string (AF1, AF2, AF3, F)
    - `total_energy`: float
  - `items`: object
  - `required_columns`: `system`, `phase`, `total_energy`
  - `units`:
    - `total_energy`: atomic_units

### magnetic_coupling.json
- path: `/app/outputs/magnetic_coupling.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Magnetic exchange coupling parameters J_ab and J_c (in Kelvin) extracted from total energy differences. The verifier compares these to paper-reported reference values with appropriate tolerance.
- schema:
  - `type`: object
  - `required`:
    - `pure`:
      - `J_ab`: float (K)
      - `J_c`: float (K)
    - `doped`:
      - `J_ab`: float (K)
      - `J_c`: float (K)
  - `items`: object
  - `required_columns`:
  - `units`: object

### mulliken_orbitals.json
- path: `/app/outputs/mulliken_orbitals.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Mulliken d-orbital populations of copper atoms in the AF1 phase. The verifier checks that orbital populations show the expected orbital ordering pattern (filled t2g and d_z2, partially filled d_x2-y2) for both pure and doped systems.
- schema:
  - `type`: object
  - `required`:
    - `pure`:
      - `Cu`:
        - `d_xy`: float
        - `d_xz`: float
        - `d_yz`: float
        - `d_z2`: float
        - `d_x2-y2`: float
    - `doped`:
      - `Cu1`:
        - `d_xy`: float
        - `d_xz`: float
        - `d_yz`: float
        - `d_z2`: float
        - `d_x2-y2`: float
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: Scoring is structural (T3): the checker will assess energy ordering (AF1 < AF3 < AF2 ≤ F) and that Mg doping reduces the absolute energy differences. Magnetic coupling parameters are compared to paper gold with a tolerance that allows toolchain variation. Orbital populations are checked for the correct orbital ordering pattern, not exact populations. The agent is expected to use a standard B3LYP hybrid functional implementation; exact numbers depend on the code and convergence settings; relative trends and sign of J dominate scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required": {
          "system": "string (pure or doped)",
          "phase": "string (AF1, AF2, AF3, F)",
          "total_energy": "float"
        },
        "items": {},
        "required_columns": [
          "system",
          "phase",
          "total_energy"
        ],
        "units": {
          "total_energy": "atomic_units"
        }
      },
      "description": "Compiled total energies of pure and Mg-doped KCuF3 in four magnetic orderings. The verifier checks energy ordering and the reduction of energy differences upon doping."
    },
    {
      "file": "magnetic_coupling.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pure": {
            "J_ab": "float (K)",
            "J_c": "float (K)"
          },
          "doped": {
            "J_ab": "float (K)",
            "J_c": "float (K)"
          }
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Magnetic exchange coupling parameters J_ab and J_c (in Kelvin) extracted from total energy differences. The verifier compares these to paper-reported reference values with appropriate tolerance."
    },
    {
      "file": "mulliken_orbitals.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "pure": {
            "Cu": {
              "d_xy": "float",
              "d_xz": "float",
              "d_yz": "float",
              "d_z2": "float",
              "d_x2-y2": "float"
            }
          },
          "doped": {
            "Cu1": {
              "d_xy": "float",
              "d_xz": "float",
              "d_yz": "float",
              "d_z2": "float",
              "d_x2-y2": "float"
            }
          }
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "Mulliken d-orbital populations of copper atoms in the AF1 phase. The verifier checks that orbital populations show the expected orbital ordering pattern (filled t2g and d_z2, partially filled d_x2-y2) for both pure and doped systems."
    }
  ],
  "notes": "Scoring is structural (T3): the checker will assess energy ordering (AF1 < AF3 < AF2 ≤ F) and that Mg doping reduces the absolute energy differences. Magnetic coupling parameters are compared to paper gold with a tolerance that allows toolchain variation. Orbital populations are checked for the correct orbital ordering pattern, not exact populations. The agent is expected to use a standard B3LYP hybrid functional implementation; exact numbers depend on the code and convergence settings; relative trends and sign of J dominate scoring."
}
```

## How you are scored
A hidden verifier inspects each scored output file independently. It checks structural properties such as the correct ordering of total energies (AF1 < AF3 < AF2 ≤ F) and whether Mg doping reduces the absolute energy differences between phases. For the magnetic coupling parameters it verifies that J_c is large and negative and J_ab is small and positive, within generous tolerances that account for toolchain variability, and that the effective parameters in the doped system remain close to those of pure KCuF3. The orbital populations are checked for the expected orbital ordering pattern (filled t₂g and d_z² orbitals, partially filled d_x²−y²). The final reward is a weighted combination of partial scores from each stage; reporting a number without genuine computation does not satisfy the scoring criteria.
