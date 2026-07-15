# DFT Defect Formation Energy and Level Pressure Coefficients in Cubic Boron Nitride

## Problem background
Cubic boron nitride (c-BN) is a wide-band-gap semiconductor used in high-power and high-temperature electronics. During synthesis, carbon atoms often substitute for boron or nitrogen sites, creating unintentional dopants that can strongly alter the electronic properties. Hydrostatic pressure can change both the thermodynamic stability of these substitutional defects and the positions of their electronic energy levels. Understanding how the formation enthalpy and defect level positions of carbon-on-boron (C_B) and carbon-on-nitrogen (C_N) defects evolve under pressure is essential for designing high-pressure c-BN devices. This task asks you to compute these quantities using first-principles density-functional theory (DFT) and extract their pressure dependence.

## Approach
The approach follows a plane-wave DFT supercell method with projector augmented-wave (PAW) pseudopotentials and the local density approximation (LDA). All calculations are performed with the open-source Quantum ESPRESSO code.

First, accurate atomic chemical potentials are obtained from the total energies of elemental reference crystals: α-B, α-N₂, and diamond. The bulk c-BN equation of state is then computed via variable-cell relaxation to map hydrostatic pressure to cell volume at 0, 20, 40, and 60 GPa. A pristine 128‑atom (4×4×4) c-BN supercell is built and its enthalpy is computed at each target pressure to serve as the host reference.

Next, for every combination of defect type (C_B, C_N), charge state (−1, 0, +1), and pressure, a single carbon atom replaces a B or N site in the supercell. Atomic positions are relaxed until forces drop below 0.005 eV/Å, and the total enthalpy of the defective supercell is recorded.

Formation enthalpies are calculated using the standard defect formation energy expression, which includes the total enthalpies of the defective and pristine supercells, the number of atoms exchanged, the appropriate atomic chemical potentials, the electron chemical potential referenced to the valence-band maximum (VBM), and a screened Madelung correction (α = 1.63806, ε = 3.86). For C_B defects, B‑rich chemical potential conditions are used; for C_N, N‑rich conditions.

Defect energy levels are extracted from the projected density of states (PDOS) of each relaxed defective supercell. For each charge state, the centre of gravity of the impurity band relative to the VBM is computed. A linear fit of these level energies against pressure yields the average pressure coefficient in meV/GPa.

The overall workflow is structured as a series of compute steps leading to two deliverable artifacts.

## Reproduction target
Using Quantum ESPRESSO with SSSP PAW (LDA) pseudopotentials:

1. Compute the formation enthalpy H_f (in eV) for substitutional carbon defects C_B and C_N in charge states −1, 0, +1 at hydrostatic pressures of 0, 20, 40, and 60 GPa under B‑rich conditions (for C_B) and N‑rich conditions (for C_N).
2. For each defect/charge state, extract the defect-induced energy level position (centre of gravity of the impurity DOS) relative to the VBM at each pressure, and then derive the average pressure coefficient (in meV/GPa) from a linear fit across the four pressures.

The results must be saved as two output files:
- `/app/outputs/step_01_formation_enthalpies.csv` (columns: pressure_GPa, defect, charge, H_f_eV)
- `/app/outputs/step_02_defect_level_pressure_coefficients.json` (keys like C_B^+1 with fields pressure_coefficient_meV_GPa and level_energies_eV array of length 4).

## Assets

- Quantum ESPRESSO DFT code: https://www.quantum-espresso.org/
- SSSP PAW pseudopotentials for B, N, C: https://www.materialscloud.org/discover/sssp/table/efficiency
- Crystal structures of c-BN, α-B, α-N2, diamond: Known standard structures; can be taken from the Materials Project (mp-1562, mp-1692, mp-942, mp-66)

## Workflow steps

### Step 1: Elemental reference total energy calculations
- Role: process
- Action: Compute DFT total energies per atom for α-B, α-N2, and diamond using the same pseudopotential/functional setup. Record total energies needed for chemical potentials μ_B^0, μ_N^0, μ_C^0.
- Evidence: `/app/outputs/elemental_energies.json`

### Step 2: Bulk c-BN equation of state and pressure-volume relation
- Role: process
- Action: Relax the c-BN primitive cell to find equilibrium lattice constant a0 and bulk modulus B. Compute the energy-volume curve and determine the cell volumes corresponding to hydrostatic pressures 0, 20, 40, 60 GPa.
- Evidence: `/app/outputs/cBN_eos.json`

### Step 3: Perfect supercell enthalpy at target pressures
- Role: process
- Action: Construct a 128-atom c-BN supercell (4x4x4). Compute its total enthalpy at each hydrostatic pressure (0,20,40,60 GPa) using the volumes from the equation of state.
- Evidence: `/app/outputs/host_enthalpies.json`

### Step 4: Defect supercell geometry relaxation and enthalpy calculation
- Role: process
- Action: For each combination of defect type (C_B, C_N), charge state (-1,0,+1), and pressure (0,20,40,60 GPa): create a supercell with one substitutional carbon, relax atomic positions, and record the total enthalpy of the defective supercell.
- Evidence: `/app/outputs/defect_enthalpies.json`

### Step 5: Formation enthalpy table
- Role: scored (load-bearing)
- Action: Using enthalpies from previous steps and chemical potentials, compute formation enthalpies H_f via the standard defect formation energy formula, including VBM alignment and screened Madelung correction (α=1.63806, ε=3.86). Use B-rich conditions for C_B and N-rich for C_N. Output a CSV of H_f values.
- Output file: `/app/outputs/step_01_formation_enthalpies.csv`
- Format: csv
- Contract: Columns: pressure_GPa (float), defect (string: C_B or C_N), charge (int: -1,0,1), H_f_eV (float).
- Scoring: scored by hidden verifier

### Step 6: Defect level pressure coefficients
- Role: scored (load-bearing)
- Action: For each defective supercell, compute projected DOS and extract defect-induced energy level positions (center of gravity of impurity band) relative to VBM. Fit level energies vs. pressure linearly to obtain pressure coefficients in meV/GPa. Output a JSON file with the coefficients.
- Output file: `/app/outputs/step_02_defect_level_pressure_coefficients.json`
- Format: json
- Contract: Object with keys like C_B^+1 mapping to {pressure_coefficient_meV_GPa: float, level_energies_eV: [4 floats] for pressures 0,20,40,60}. Keys: C_B^+1, C_B^0, C_B^-1, C_N^+1, C_N^0, C_N^-1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_enthalpies.csv`
- `/app/outputs/step_02_defect_level_pressure_coefficients.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_enthalpies.csv
- path: `/app/outputs/step_01_formation_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed formation enthalpies for C_B and C_N defects under hydrostatic pressure.
- schema:
  - `type`: table
  - `required_columns`: `pressure_GPa`, `defect`, `charge`, `H_f_eV`
  - `units`:
    - `pressure_GPa`: GPa
    - `H_f_eV`: eV

### step_02_defect_level_pressure_coefficients.json
- path: `/app/outputs/step_02_defect_level_pressure_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Pressure coefficients of defect energy levels derived from projected DOS.
- schema:
  - `type`: object
  - `required`:
    - `C_B^+1`: object
    - `C_B^0`: object
    - `C_B^-1`: object
    - `C_N^+1`: object
    - `C_N^0`: object
    - `C_N^-1`: object
  - `items`:
    - `pressure_coefficient_meV_GPa`: float
    - `level_energies_eV`: array of 4 floats
  - `units`:
    - `pressure_coefficient_meV_GPa`: meV/GPa
    - `level_energies_eV`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_GPa",
          "defect",
          "charge",
          "H_f_eV"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "H_f_eV": "eV"
        }
      },
      "description": "Computed formation enthalpies for C_B and C_N defects under hydrostatic pressure."
    },
    {
      "file": "step_02_defect_level_pressure_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C_B^+1": "object",
          "C_B^0": "object",
          "C_B^-1": "object",
          "C_N^+1": "object",
          "C_N^0": "object",
          "C_N^-1": "object"
        },
        "items": {
          "pressure_coefficient_meV_GPa": "float",
          "level_energies_eV": "array of 4 floats"
        },
        "units": {
          "pressure_coefficient_meV_GPa": "meV/GPa",
          "level_energies_eV": "eV"
        }
      },
      "description": "Pressure coefficients of defect energy levels derived from projected DOS."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden automated verifier independently examines the two output files you produce. For the formation enthalpy table, it compares your computed H_f values (for each defect, charge, and pressure combination) to reference values and checks any required quantitative behaviour across pressures. For the defect level pressure coefficients, it compares your reported coefficients and level energies to reference results. The verifier does not see your intermediate calculations or log files; it only reads the final scored artifacts. Each scored artifact carries an equal share of the total reward (0.5 each). The reward is a float between 0 and 1 based on how well your outputs match the hidden reference; simply printing a number without running the described DFT workflow will not earn a high score. Exact numeric tolerances are not disclosed.
