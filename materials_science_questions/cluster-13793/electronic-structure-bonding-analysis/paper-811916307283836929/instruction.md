# First-principles Structural Stability of TaN Polymorphs

## Problem background
Transition metal nitrides, particularly TaN, are technologically important as hard coatings, diffusion barriers, and gate electrodes in microelectronics. Determining the ground-state crystal structure and its equilibrium mechanical properties is crucial for understanding phase stability and guiding synthesis. Among several candidate crystal structures, the one with the lowest cohesive energy is identified as the ground state.

## Approach
Density functional theory (DFT) calculations are performed using the plane-wave pseudopotential method with the generalized gradient approximation of Perdew, Burke, and Ernzerhof (GGA-PBE), as implemented in Quantum ESPRESSO. Ultrast Vanderbilt pseudopotentials from the PSLibrary are used for Ta and N. For five candidate TaN crystal structures—CoSn (hexagonal, space group P6 2 m), WC (hexagonal), NaCl (cubic), ZnS-B3 (cubic), and CsCl (cubic)—total energies are computed for a series of unit cell volumes around the expected equilibrium. The energy–volume data for each structure is fitted to the third-order Birch-Murnaghan equation of state to extract the equilibrium volume (V0), cohesive energy (E0), bulk modulus (K0), and its first pressure derivative (K0′). The lattice constants are derived from the equilibrium volume. By comparing cohesive energies, the ground-state structure (lowest E0) is identified.

## Reproduction target
Produce a CSV table (`step_01_equilibrium_properties.csv`) listing for each of the five TaN structures the equilibrium lattice constants (a and, for hexagonal phases, c), cohesive energy E0 (in eV per TaN formula unit), equilibrium volume V0 (in Å³ per formula unit), bulk modulus K0 (in GPa), and pressure derivative K0′. Additionally, write a single-line text file (`step_02_ground_state.txt`) containing the name of the structure with the lowest cohesive energy—the calculated ground state.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotential library (PSL): http://pseudopotentials.quantum-espresso.org/

## Workflow steps

### Step 1: Prepare input structures and volume sweeps
- Role: process
- Action: Generate Quantum ESPRESSO input files for the five TaN phases (CoSn, WC, NaCl, ZnS-B3, CsCl) using their known crystal structures (space groups, Wyckoff positions). For each structure, create a series of unit cells with scaled volumes to sample the energy-volume curve.
- Evidence: `/app/outputs/step_01_structures_generated.txt`

### Step 2: Run DFT total energy calculations
- Role: process
- Action: Perform SCF calculations for each structure at each volume using Quantum ESPRESSO pw.x with the GGA-PBE functional and appropriate plane-wave kinetic energy cutoff and Monkhorst-Pack k-point meshes. Collect total energies per formula unit.
- Evidence: `/app/outputs/energy_volume_data.json`

### Step 3: Fit Birch-Murnaghan equation of state
- Role: process
- Action: Fit the energy-volume data for each structure to the third-order Birch-Murnaghan equation of state to extract the equilibrium volume, cohesive energy, bulk modulus, and its pressure derivative.
- Evidence: none

### Step 4: Save equilibrium structural properties
- Role: scored (load-bearing)
- Action: Write the fitted equilibrium properties for all five structures to a CSV file.
- Output file: `/app/outputs/step_01_equilibrium_properties.csv`
- Format: csv
- Contract: columns: structure (str), a (Å), c (Å, blank if cubic), E0 (eV per TaN formula unit), V0 (Å³ per formula unit), K0 (GPa), K0_prime (dimensionless)
- Scoring: scored by hidden verifier

### Step 5: Identify ground-state structure
- Role: scored
- Action: Compare cohesive energies and write the structure name with the lowest cohesive energy to a text file.
- Output file: `/app/outputs/step_02_ground_state.txt`
- Format: txt
- Contract: single line string
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_equilibrium_properties.csv`
- `/app/outputs/step_02_ground_state.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_equilibrium_properties.csv
- path: `/app/outputs/step_01_equilibrium_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium structural parameters for the five TaN phases extracted from Birch-Murnaghan equation of state fitting.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `a`, `c`, `E0`, `V0`, `K0`, `K0_prime`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `E0`: eV per TaN formula unit
    - `V0`: Å³ per formula unit
    - `K0`: GPa
    - `K0_prime`: dimensionless

### step_02_ground_state.txt
- path: `/app/outputs/step_02_ground_state.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Name of the ground-state TaN structure (lowest cohesive energy).
- schema:
  - `type`: text
  - `notes`: single line string, e.g. 'CoSn'

Notes: The checker compares the CoSn row properties to hidden reference values with tolerances and verifies that CoSn has the lowest cohesive energy among all five structures. The ground-state text file must match the exact expected string.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_equilibrium_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "a",
          "c",
          "E0",
          "V0",
          "K0",
          "K0_prime"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "E0": "eV per TaN formula unit",
          "V0": "Å³ per formula unit",
          "K0": "GPa",
          "K0_prime": "dimensionless"
        }
      },
      "description": "Equilibrium structural parameters for the five TaN phases extracted from Birch-Murnaghan equation of state fitting."
    },
    {
      "file": "step_02_ground_state.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "notes": "single line string, e.g. 'CoSn'"
      },
      "description": "Name of the ground-state TaN structure (lowest cohesive energy)."
    }
  ],
  "notes": "The checker compares the CoSn row properties to hidden reference values with tolerances and verifies that CoSn has the lowest cohesive energy among all five structures. The ground-state text file must match the exact expected string."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that knows the expected ground-state structure and reference equilibrium properties. The verifier reads your CSV (`step_01_equilibrium_properties.csv`) and checks: (i) the row corresponding to the ground-state structure has lattice constants, cohesive energy, bulk modulus, and pressure derivative that deviate from the reference values by no more than a set tolerance; (ii) the cohesive energy of that row is the lowest among all rows. It also reads your ground-state text file (`step_02_ground_state.txt`) and checks that it contains exactly the expected structure name. Full reward (1.0) is given only if all checks pass; otherwise a lower score proportional to the number of passing checks may be assigned.
