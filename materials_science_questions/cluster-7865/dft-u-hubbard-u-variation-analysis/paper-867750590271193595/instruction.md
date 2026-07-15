# Magnetic Exchange Couplings and Critical Temperatures of Europium Superhydrides from DFT+U and Monte Carlo

## Problem background
Europium superhydrides synthesized at high pressure exhibit magnetic ordering. Three phases have been identified: a cubic phase, a hexagonal phase, and a clathrate phase. Their magnetic exchange couplings and critical temperatures are of interest. In this task, you will computationally determine the magnetic exchange coupling constants and the corresponding critical temperatures for all three phases.

## Approach
The magnetic properties are obtained through a three-stage computational workflow. First, DFT+U total-energy calculations are performed for several collinear magnetic configurations of each phase (ferromagnetic and selected antiferromagnetic configurations). These calculations use Quantum ESPRESSO with Hubbard U parameters derived from linear response. Second, the total energies are used to build an Ising Hamiltonian for each phase, from which the nearest-neighbor and (where applicable) next-nearest-neighbor exchange coupling constants (J1, J2, J3) are extracted by solving the resulting set of equations. Third, the derived coupling constants are fed into atomistic Monte Carlo simulations (VAMPIRE) on representative simulation boxes to obtain the temperature dependence of the magnetization; the critical temperature (Néel or Curie) is identified as the temperature where the normalized mean magnetization drops below 0.25.

## Reproduction target
Produce a file `results.json` containing an array of three objects, one for each europium superhydride phase. Each object must have the fields: `phase` (a string identifier), `magnetic_order` (either "AFM" or "FM"), `J1` and `J2` (coupling constants in Joules per Eu–Eu link, as floats), `J3` (optional coupling constant, float or null), and `Tc` (critical temperature in Kelvin, float).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- VAMPIRE: https://vampire.york.ac.uk/

## Provided crystal structures and Hubbard U parameters

### Cubic EuH9 (F-43m) at 130 GPa
Space group: F-43m (No. 216)
Lattice constant: a = 4.9475 Å
Atomic positions (fractional):
- Eu: 0.25 0.25 0.25
- H1: -0.13655 -0.13655 -0.13
- H2: -0.38097 -0.38 -0.38907
- H3: 0.0 0.0 0.0
Hubbard U-J: 4.46 eV
Magnetic configurations required for extracting exchange couplings (spin orientations along z):
- FM: all four Eu spins up ( + + + + )
- AFM2: up up up down ( + + + - )
- AFM5: up down up up ( + - + + )

### Hexagonal EuH9 (P6_3/mmc) at 130 GPa
Space group: P6_3/mmc (No. 194)
Lattice parameters: a = 3.5911 Å, c = 5.5094 Å
Atomic positions (fractional):
- Eu1: 1/3 2/3 3/4
- H1: 0.0 0.0 0.25
- H2: 1/3 2/3 0.33627
- H3: 0.152 0.30401 0.04717
Hubbard U-J: 4.74 eV
Magnetic configurations:
- FM: all Eu spins up ( + + + + )
- AFM1: up down up down ( + - + - )
- AFM3: up down down up ( + - - + )

### Clathrate Eu8H46 (Pm-3n) at 130 GPa
Space group: Pm-3n (No. 223)
Lattice constant: a = 5.8582 Å
Atomic positions (fractional):
- Eu1: 0.0 0.0 0.0
- Eu2: 0.25 0.0 0.5
- H1: 0.0 0.11963 0.30584
- H2: 0.25 0.5 0.0
Hubbard U-J: 5.01 eV
Magnetic configurations:
- FM: all eight Eu spins up
- AFM1: spins on Eu1–Eu4 up, Eu5–Eu8 down
- AFM5: alternating up/down pattern: Eu1 up, Eu2 down, Eu3 up, Eu4 down, Eu5 up, Eu6 down, Eu7 up, Eu8 down
- AFM8: spins on Eu1, Eu2, Eu5, Eu6 up; Eu3, Eu4, Eu7, Eu8 down

For the Ising model, only the relative spin signs matter. The solver should set up the initial spin configurations accordingly before relaxation.

## Workflow steps

### Step 1: DFT+U total-energy calculations for magnetic configurations
- Role: process
- Action: For each of the three europium superhydride phases (cubic EuH9, hexagonal EuH9, clathrate Eu8H46), set up the crystal structures from the provided coordinates and perform DFT+U calculations using Quantum ESPRESSO with the Hubbard U-J values given in the instruction. Compute total energies for the specified collinear magnetic configurations: for cubic EuH9, FM, AFM2, AFM5; for hexagonal EuH9, FM, AFM1, AFM3; for Eu8H46, FM, AFM1, AFM5, AFM8. Relax each configuration (without spin-orbit coupling) and record the final total energy per formula unit. Save all computed energies as a JSON file for documentation.
- Evidence: `/app/outputs/dft_energies.json`

### Step 2: Ising model mapping and Monte Carlo determination of critical temperatures
- Role: scored (load-bearing)
- Action: From the DFT total energies obtained in the previous step, derive the magnetic exchange coupling constants J1, J2 (and J3 for Eu8H46) by solving the Ising Hamiltonian equations for each phase. Then use the VAMPIRE code to perform Monte Carlo simulations with the derived couplings and the specified simulation box dimensions (8×8×2 nm for EuH9 phases, 10×10×2 nm for Eu8H46). Determine the critical temperature (Néel or Curie) as the temperature at which the normalized mean magnetization falls below 0.25. Output a JSON file containing the coupling constants, magnetic ordering type, and critical temperature for each phase.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of objects, each with string field 'phase', string field 'magnetic_order' (either 'AFM' or 'FM'), float fields 'J1' and 'J2' (units: Joules per Eu-Eu link), optional float field 'J3' (for Eu8H46 only, null for other phases), and float field 'Tc' (unit: Kelvin).
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
- description: This file contains the magnetic exchange coupling constants and critical temperatures for the three europium superhydride phases, as derived from DFT+U calculations and Monte Carlo simulations. The checker compares the reported values to hidden paper-reported reference values with tolerances (exact_match policy) to score the reproduction.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `phase`:
        - `type`: string
        - `description`: Phase name, e.g., 'cubic-EuH9', 'hexagonal-EuH9', 'Eu8H46'
      - `magnetic_order`:
        - `type`: string
        - `enum`: `AFM`, `FM`
        - `description`: Magnetic ordering type
      - `J1`:
        - `type`: number
        - `unit`: Joules per Eu-Eu link
        - `description`: First nearest neighbour exchange coupling constant
      - `J2`:
        - `type`: number
        - `unit`: Joules per Eu-Eu link
        - `description`: Second nearest neighbour exchange coupling constant
      - `J3`:
        - `type`: `number`, `null`
        - `unit`: Joules per Eu-Eu link
        - `description`: Third nearest neighbour exchange coupling constant (present for Eu8H46, null for EuH9 phases)
      - `Tc`:
        - `type`: number
        - `unit`: Kelvin
        - `description`: Critical temperature (Néel or Curie)
    - `required`: `phase`, `magnetic_order`, `J1`, `J2`, `Tc`
  - `minItems`: 3
  - `maxItems`: 3
  - `description`: Array of results for the three europium superhydride phases.

Notes: The results.json is the only scored artifact. The process step's evidence file (dft_energies.json) is not scored; it documents that the DFT calculations were performed but the checker does not rely on it. The task is designed around a result-level comparison of the published deterministic quantities, using exact_match with appropriate tolerances that absorb legitimate toolchain spread (Quantum ESPRESSO vs. VASP). All hidden gold values are taken from the paper's Supporting Information Table S14.

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
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "phase": {
              "type": "string",
              "description": "Phase name, e.g., 'cubic-EuH9', 'hexagonal-EuH9', 'Eu8H46'"
            },
            "magnetic_order": {
              "type": "string",
              "enum": [
                "AFM",
                "FM"
              ],
              "description": "Magnetic ordering type"
            },
            "J1": {
              "type": "number",
              "unit": "Joules per Eu-Eu link",
              "description": "First nearest neighbour exchange coupling constant"
            },
            "J2": {
              "type": "number",
              "unit": "Joules per Eu-Eu link",
              "description": "Second nearest neighbour exchange coupling constant"
            },
            "J3": {
              "type": [
                "number",
                "null"
              ],
              "unit": "Joules per Eu-Eu link",
              "description": "Third nearest neighbour exchange coupling constant (present for Eu8H46, null for EuH9 phases)"
            },
            "Tc": {
              "type": "number",
              "unit": "Kelvin",
              "description": "Critical temperature (Néel or Curie)"
            }
          },
          "required": [
            "phase",
            "magnetic_order",
            "J1",
            "J2",
            "Tc"
          ]
        },
        "minItems": 3,
        "maxItems": 3,
        "description": "Array of results for the three europium superhydride phases."
      },
      "description": "This file contains the magnetic exchange coupling constants and critical temperatures for the three europium superhydride phases, as derived from DFT+U calculations and Monte Carlo simulations. The checker compares the reported values to hidden paper-reported reference values with tolerances (exact_match policy) to score the reproduction."
    }
  ],
  "notes": "The results.json is the only scored artifact. The process step's evidence file (dft_energies.json) is not scored; it documents that the DFT calculations were performed but the checker does not rely on it. The task is designed around a result-level comparison of the published deterministic quantities, using exact_match with appropriate tolerances that absorb legitimate toolchain spread (Quantum ESPRESSO vs. VASP). All hidden gold values are taken from the paper's Supporting Information Table S14."
}
```

## How you are scored
Your solution is scored by a hidden verifier. The verifier reads your `results.json` and compares the submitted coupling constants, magnetic ordering labels, and critical temperatures against the expected reference values obtained by this procedure. Each phase contributes equally to the total reward; the final score is the weighted sum of phase-level comparisons. The verifier expects results consistent with the specified DFT+U and Monte Carlo workflow — simply copying numbers from any source will not receive full credit.
