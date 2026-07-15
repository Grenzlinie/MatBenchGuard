# First-principles calculation of shear‑energy landscape and superconductivity in compressed atomic hydrogen

## Problem background
Under extreme pressures, solid hydrogen is predicted to adopt an atomic metallic phase with the tetragonal I4₁/amd (Cs‑IV) structure. External shear distortions of this structure, parameterized by an angle θ, are expected to produce unusual flat energy landscapes and to influence the superconducting properties through phonon softening. This task investigates these effects using first‑principles density‑functional theory (DFT): compute the total energy of the Cs‑IV structure as a function of the shear angle θ at a fixed cell volume corresponding to approximately 400 GPa, and determine the superconducting transition temperature Tc of the same structure at a pressure of approximately 1150 GPa.

## Approach
You will use the plane‑wave DFT code Quantum ESPRESSO with the Perdew–Burke–Ernzerhof (PBE) exchange–correlation functional and the Rappe–Rabe–Kaxiras–Joannopoulos ultrasoft pseudopotential for hydrogen. The general workflow is: (1) Relax the Cs‑IV cell at the two target pressures (400 GPa and 1150 GPa) to obtain equilibrium geometries. (2) For the shear‑energy landscape, at the volume obtained at 400 GPa, perform a series of static total‑energy calculations at fixed cell while varying the shear angle θ from 80° to 100°. (3) For the superconducting state, starting from the 1150 GPa geometry, compute the phonon spectrum and electron‑phonon coupling using density‑functional perturbation theory (DFPT); from these obtain the electron‑phonon coupling constant λ and the logarithmic‑averaged phonon frequency ω_log. Finally, calculate the superconducting transition temperature Tc using the Allen–Dynes formula with a Coulomb pseudopotential μ* = 0.089.

## Reproduction target
Produce two scored artifacts:

- **`energy_curve.csv`** – a table with columns `theta_deg` (numeric) and `total_energy_Ry` (numeric) that lists the total electronic energy (in Rydberg per primitive cell of 4 H atoms) of the Cs‑IV structure at the fixed volume corresponding to 400 GPa, for a range of shear angles θ covering at least 80°–100° in steps not larger than 2°.

- **`superconductivity.json`** – a JSON object with keys `pressure_GPa` (number), `lambda` (number), `omega_log_K` (number) and `Tc_K` (number). These are the pressure, electron‑phonon coupling constant, logarithmic‑averaged phonon frequency (in K), and the Allen–Dynes superconducting transition temperature (in K), all for the Cs‑IV structure at approximately 1150 GPa.

The values you compute will be compared against hidden reference results for this system.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Rappe‑Rabe‑Kaxiras‑Joannopoulos ultrasoft pseudopotential for H (PBE): https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Structural optimization of Cs‑IV at 400 GPa
- Role: process
- Action: Perform a variable‑cell relaxation of the Cs‑IV structure (space group I4₁/amd, primitive cell of 4 H atoms) at an external pressure of 400 GPa, or equivalently at a fixed volume of 7.14 a.u.³/proton, using DFT. Obtain the equilibrium lattice parameters and atomic positions.
- Evidence: `/app/outputs/optimization_400.log`

### Step 2: Static total‑energy curve vs shear angle θ
- Role: scored (load-bearing)
- Action: Take the optimized cell from step opt_400. Holding the volume fixed, construct a series of structures with shear angle θ varying from 80° to 100° (step size ≤2°). For each θ, perform a static DFT total‑energy calculation (fixed cell, no relaxation). Output a CSV file containing θ (degrees) and the total electronic energy (in Rydberg per primitive cell of 4 atoms).
- Output file: `/app/outputs/energy_curve.csv`
- Format: csv
- Contract: CSV with header: theta_deg (numeric), total_energy_Ry (numeric).
- Scoring: scored by hidden verifier

### Step 3: Structural optimization of Cs‑IV at 1150 GPa
- Role: process
- Action: Perform a variable‑cell relaxation of the Cs‑IV structure at a pressure of approximately 1150 GPa (using the same functional and pseudopotential). Obtain the equilibrium lattice parameters and atomic positions.
- Evidence: `/app/outputs/optimization_1150.log`

### Step 4: Superconducting Tc of Cs‑IV at 1150 GPa
- Role: scored (load-bearing)
- Action: Starting from the optimized structure from step opt_1150, compute the phonon dispersion and electron‑phonon coupling using density functional perturbation theory (DFPT). Calculate the electron‑phonon coupling constant λ, the logarithmic‑averaged phonon frequency ω_log, and the superconducting transition temperature Tc via the Allen‑Dynes formula with effective Coulomb repulsion μ* = 0.089. Output these values in a JSON file.
- Output file: `/app/outputs/superconductivity.json`
- Format: json
- Contract: JSON object with keys: pressure_GPa (number), lambda (number), omega_log_K (number), Tc_K (number).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_curve.csv`
- `/app/outputs/superconductivity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_curve.csv
- path: `/app/outputs/energy_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of shear angle θ (degrees) and the corresponding total electronic energy (Rydberg) for the Cs‑IV structure at a fixed volume of 7.14 a.u.³/proton. Theta should range from 80° to 100° inclusive.
- schema:
  - `type`: table
  - `required_columns`: `theta_deg`, `total_energy_Ry`
  - `units`:
    - `theta_deg`: degrees
    - `total_energy_Ry`: Rydberg per primitive cell (4 atoms)

### superconductivity.json
- path: `/app/outputs/superconductivity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Superconductivity parameters for the Cs‑IV structure at 1150 GPa: the electron‑phonon coupling constant λ, logarithmic‑averaged phonon frequency ω_log, and the Allen‑Dynes superconducting transition temperature Tc.
- schema:
  - `type`: object
  - `required`:
    - `pressure_GPa`: number
    - `lambda`: number
    - `omega_log_K`: number
    - `Tc_K`: number
  - `units`:
    - `pressure_GPa`: GPa
    - `omega_log_K`: K
    - `Tc_K`: K

Notes: The energy curve must be computed for a sufficient number of θ points covering the range 80°–100° to faithfully capture the energy landscape. The superconductivity JSON must include the four listed keys; the units are as declared.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta_deg",
          "total_energy_Ry"
        ],
        "units": {
          "theta_deg": "degrees",
          "total_energy_Ry": "Rydberg per primitive cell (4 atoms)"
        }
      },
      "description": "Table of shear angle θ (degrees) and the corresponding total electronic energy (Rydberg) for the Cs‑IV structure at a fixed volume of 7.14 a.u.³/proton. Theta should range from 80° to 100° inclusive."
    },
    {
      "file": "superconductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "pressure_GPa": "number",
          "lambda": "number",
          "omega_log_K": "number",
          "Tc_K": "number"
        },
        "units": {
          "pressure_GPa": "GPa",
          "omega_log_K": "K",
          "Tc_K": "K"
        }
      },
      "description": "Superconductivity parameters for the Cs‑IV structure at 1150 GPa: the electron‑phonon coupling constant λ, logarithmic‑averaged phonon frequency ω_log, and the Allen‑Dynes superconducting transition temperature Tc."
    }
  ],
  "notes": "The energy curve must be computed for a sufficient number of θ points covering the range 80°–100° to faithfully capture the energy landscape. The superconductivity JSON must include the four listed keys; the units are as declared."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that evaluates each artifact independently.

- **`energy_curve.csv`**: The verifier evaluates your total‑energy‑vs‑angle curve using hidden criteria. It will assess the curve's shape and values against reference information; your reward depends on how well your computed curve matches the expected physical properties.

- **`superconductivity.json`**: The verifier compares your λ, ω_log and Tc to hidden reference values within generous tolerances. In addition, it recomputes Tc from your submitted λ and ω_log using the Allen‑Dynes formula with μ* = 0.089 and checks that the recomputed Tc matches the Tc you reported; internally inconsistent entries receive reduced or no credit.

The final reward is a weighted combination of these checks, with the energy curve and the superconductivity parameters carrying similar weight.
