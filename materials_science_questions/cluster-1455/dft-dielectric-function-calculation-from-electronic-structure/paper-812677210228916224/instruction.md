# DFT calculation of mechanical, electronic, and optical properties of α-RDX under pressure

## Problem background
α‑RDX is one of the most widely used secondary explosives. Its behaviour under hydrostatic pressure is of great interest because pressure can significantly alter structural, elastic, electronic and optical properties, which in turn affect performance and sensitivity. This task focuses on computing key quantities that characterise the pressure‑dependent response of α‑RDX over the range 0–40 GPa using first‑principles density functional theory. The quantities to be determined are (a) polycrystalline mechanical ductility indicators — bulk modulus, shear modulus, the B/G ratio, Poisson’s ratio, and the C₁₂–C₄₄ indicator — derived from elastic constants; (b) the electronic band gap; and (c) the static refractive index at zero pressure for the three independent polarisation directions. Understanding how these properties evolve with pressure is important for predicting the material’s behaviour under extreme conditions.

## Approach
The reproduction follows a standard first‑principles workflow using plane‑wave density functional theory (DFT). The exchange‑correlation treatment uses the Perdew–Burke–Ernzerhof (PBE) generalised gradient approximation, supplemented with Grimme’s D2 dispersion correction to better capture van der Waals interactions in this molecular crystal. Starting from the known orthorhombic crystal structure of α‑RDX (space group Pbca, 168 atoms per unit cell), geometry optimisations are performed with variable‑cell relaxation at a sequence of hydrostatic pressures. For each relaxed structure, the elastic constants are obtained by the stress–strain finite‑difference method: small deformations are applied, and the resulting stress tensor is computed from static DFT runs; the nine independent elastic constants Cᵢⱼ for the orthorhombic system are extracted by linear‑response or stress‑strain fitting. Following the elastic constants, polycrystalline mechanical properties (bulk modulus, shear modulus, B/G ratio, Poisson’s ratio, and the C₁₂–C₄₄ indicator) are calculated using Voigt‑Reuss‑Hill averaging of the Voigt and Reuss bounds. The electronic band structure is obtained from a self‑consistent field calculation followed by a non‑self‑consistent band‑structure run; the band gap is determined as the energy difference between the valence‑band maximum and the conduction‑band minimum. The static refractive index at zero pressure is obtained from the optical dielectric function: the imaginary part is computed via dipole matrix elements, the real part is obtained by Kramers‑Kronig transformation, and the zero‑frequency limit gives n(0). The overall workflow is implemented with an open‑source DFT package (e.g., Quantum ESPRESSO) using norm‑conserving pseudopotentials.

## Reproduction target
Produce three CSV files as specified in the workflow steps:
1. `step_01_mechanical_properties.csv` – for each pressure 0, 5, 10, 15, 20, 25, 30, 35, 40 GPa, report the bulk modulus B_H (GPa), shear modulus G_H (GPa), the ratio B_H/G_H (dimensionless), Poisson’s ratio v (dimensionless), and the C₁₂–C₄₄ indicator (GPa).
2. `step_02_band_gap.csv` – for each of the same nine pressures, report the electronic band gap (eV).
3. `step_03_static_refractive_index.csv` – at 0 GPa, report the static refractive index n(0) for the three independent polarisation directions: (100), (010), and (001).
All quantities must be the result of the DFT calculations described in the workflow; the files must follow the exact column formats given in the output contract.

## Assets

- Quantum ESPRESSO (or ABINIT): https://www.quantum-espresso.org/
- Norm-conserving pseudopotentials for C, N, O, H (e.g., PseudoDojo ONCV or GBRV): http://www.pseudo-dojo.org/
- α-RDX crystal structure CIF (Pbca, 168 atoms): 10.1107/S1600536808012580
- Atomic Simulation Environment (ASE): ase

## Workflow steps

### Step 1: Geometry optimization under hydrostatic pressure
- Role: process
- Action: Using the α-RDX CIF as initial structure, perform DFT geometry optimization (variable-cell relaxation) at pressures 0, 5, 10, 15, 20, 25, 30, 35, 40 GPa with GGA-PBE exchange-correlation functional and a dispersion correction (e.g., Grimme D2). Save the optimized lattice parameters and atomic positions for each pressure.
- Evidence: `/app/outputs/geo_opt.log`

### Step 2: Elastic constants calculation via finite differences
- Role: process
- Action: For each optimized structure, apply a set of small deformations and compute the resulting stress tensor from static DFT calculations. Extract the nine independent elastic constants C_ij for the orthorhombic cell and write them to a CSV file (elastic_constants.csv).
- Evidence: `/app/outputs/elastic_constants.csv`

### Step 3: Mechanical properties and ductility indicators
- Role: scored (load-bearing)
- Action: Read the elastic constants from elastic_constants.csv, compute bulk modulus B_H, shear modulus G_H, B_H/G_H ratio, Poisson's ratio v, and C12-C44 using Voigt-Reuss-Hill averaging, following the formulas given in the paper. Write a CSV file with columns: pressure (GPa), B_H (GPa), G_H (GPa), B_H_G_H, v, C12_C44 (GPa) for pressures 0,5,10,15,20,25,30,35,40 GPa.
- Output file: `/app/outputs/step_01_mechanical_properties.csv`
- Format: csv
- Contract: CSV with header: pressure (int), B_H (float), G_H (float), B_H_G_H (float), v (float), C12_C44 (float).
- Scoring: scored by hidden verifier

### Step 4: Electronic band gap calculation
- Role: scored
- Action: Using the electronic structure from DFT, determine the band gap (energy difference between valence-band maximum and conduction-band minimum) at each pressure. Write a CSV with columns: pressure (GPa), band_gap (eV).
- Output file: `/app/outputs/step_02_band_gap.csv`
- Format: csv
- Contract: CSV with header: pressure (int), band_gap (float).
- Scoring: scored by hidden verifier

### Step 5: Static refractive index from optical dielectric function
- Role: scored
- Action: Using the electronic structure (wavefunctions and eigenvalues) from the DFT calculation at 0 GPa, compute the imaginary part of the dielectric function via momentum matrix elements, obtain the real part by Kramers-Kronig transformation, and extract the static refractive index n(0) for the three independent polarization directions (100), (010), (001). Write a CSV with columns: direction, static_refractive_index_n0.
- Output file: `/app/outputs/step_03_static_refractive_index.csv`
- Format: csv
- Contract: CSV with header: direction (string: 100, 010, 001), static_refractive_index_n0 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mechanical_properties.csv`
- `/app/outputs/step_02_band_gap.csv`
- `/app/outputs/step_03_static_refractive_index.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mechanical_properties.csv
- path: `/app/outputs/step_01_mechanical_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pressure-dependent mechanical properties computed from DFT elastic constants. Contains 9 rows (0,5,...,40 GPa).
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `B_H`, `G_H`, `B_H_G_H`, `v`, `C12_C44`
  - `units`:
    - `pressure`: GPa
    - `B_H`: GPa
    - `G_H`: GPa
    - `B_H_G_H`: dimensionless
    - `v`: dimensionless
    - `C12_C44`: GPa

### step_02_band_gap.csv
- path: `/app/outputs/step_02_band_gap.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electronic band gap at pressures from 0 to 40 GPa. Contains 9 rows.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `band_gap`
  - `units`:
    - `pressure`: GPa
    - `band_gap`: eV

### step_03_static_refractive_index.csv
- path: `/app/outputs/step_03_static_refractive_index.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Static refractive index at 0 GPa for three polarization directions (100), (010), (001). Contains 3 rows.
- schema:
  - `type`: table
  - `required_columns`: `direction`, `static_refractive_index_n0`
  - `units`:
    - `direction`: string (100, 010, 001)
    - `static_refractive_index_n0`: dimensionless

Notes: The checker compares the agent's reported values to hidden paper gold results with tolerances appropriate for DFT toolchain spread. Mechanical properties carry the highest weight (60%), band gap and refractive index 20% each. A structural sanity check on elastic constants is performed as a low-weight audit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mechanical_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "B_H",
          "G_H",
          "B_H_G_H",
          "v",
          "C12_C44"
        ],
        "units": {
          "pressure": "GPa",
          "B_H": "GPa",
          "G_H": "GPa",
          "B_H_G_H": "dimensionless",
          "v": "dimensionless",
          "C12_C44": "GPa"
        }
      },
      "description": "Pressure-dependent mechanical properties computed from DFT elastic constants. Contains 9 rows (0,5,...,40 GPa)."
    },
    {
      "file": "step_02_band_gap.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "band_gap"
        ],
        "units": {
          "pressure": "GPa",
          "band_gap": "eV"
        }
      },
      "description": "Electronic band gap at pressures from 0 to 40 GPa. Contains 9 rows."
    },
    {
      "file": "step_03_static_refractive_index.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "direction",
          "static_refractive_index_n0"
        ],
        "units": {
          "direction": "string (100, 010, 001)",
          "static_refractive_index_n0": "dimensionless"
        }
      },
      "description": "Static refractive index at 0 GPa for three polarization directions (100), (010), (001). Contains 3 rows."
    }
  ],
  "notes": "The checker compares the agent's reported values to hidden paper gold results with tolerances appropriate for DFT toolchain spread. Mechanical properties carry the highest weight (60%), band gap and refractive index 20% each. A structural sanity check on elastic constants is performed as a low-weight audit."
}
```

## How you are scored
Your submission will be evaluated automatically by a hidden verifier. For each scored artifact, the verifier compares your reported values against reference values (derived from the original study) using pre‑defined tolerances that account for differences in DFT implementations and computational details. Each artifact contributes a weight to the final score. A secondary, low‑weight structural audit may check that the elastic constants satisfy mechanical stability criteria under pressure and that physically expected trends (e.g., moduli generally increase with compression) are present. Simply copying the paper’s reported numbers without performing the actual computations will not satisfy the hidden comparison and will result in a low or zero score.
