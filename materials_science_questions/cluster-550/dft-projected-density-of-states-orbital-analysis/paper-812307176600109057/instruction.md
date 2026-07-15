# DFT Structure and Polarization of PbFe0.5Nb0.5O3 Supercell

## Problem background
Lead iron niobate (PbFe0.5Nb0.5O3) is a complex perovskite ferroelectric in which iron and niobium share the B‑site of the ABO3 structure. Its room‑temperature ferroelectricity has been known for decades, but the microscopic origin and the relative role of the two B‑site cations in driving the ferroelectric phase have not been fully resolved by first‑principles computations. This work targets the key density‑functional‑theory (DFT) calculation that determines the equilibrium crystal structure and the spontaneous polarization of the ordered supercell, providing the quantities needed to assess the individual contributions of the PbFeO₃ and PbNbO₃ subcells.

## Approach
The computational approach uses DFT within the generalized gradient approximation (GGA) with the Perdew–Burke–Ernzerhof (PBE) functional. A periodic supercell is built by stacking two perovskite unit cells along the [001] direction, creating alternating layers of PbFeO₃ and PbNbO₃. The ground‑state structure is obtained by relaxing both the cell parameters and the atomic positions in a variable‑cell optimization. From the relaxed structure, the spontaneous polarization of each subcell is computed using the Berry‑phase method. All calculations are performed with an open‑source plane‑wave pseudopotential code (Quantum ESPRESSO), which replaces the original full‑potential linearized augmented‑plane‑wave (FLAPW) implementation; the methodology and workflow are therefore fully reproducible with publicly available tools.

## Reproduction target
Produce two results:
1) The equilibrium pseudocubic lattice parameter and the fractional coordinates of all atoms in the relaxed supercell, written to `optimized_structure.csv`.
2) The Berry‑phase spontaneous polarization (in μC/cm²) of the PbFeO₃ and PbNbO₃ subcells, written to `polarization_values.csv`.
All quantities must be computed from the supercell model and the DFT‑relaxation and Berry‑phase procedure defined in the workflow steps, not taken from pre‑existing tables.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Build ordered supercell model
- Role: process
- Action: Construct a periodic supercell of PbFe0.5Nb0.5O3 by stacking two perovskite unit cells along [001] such that one layer is PbFeO3 and the other is PbNbO3. Create an initial input file for DFT calculation (e.g., Quantum ESPRESSO pw.x input).
- Evidence: none

### Step 2: DFT structure relaxation (vc-relax)
- Role: process
- Action: Run Quantum ESPRESSO pw.x in vc-relax mode with GGA-PBE functional. Relax both cell parameters and atomic positions to obtain the equilibrium structure.
- Evidence: none

### Step 3: Extract optimized structure
- Role: scored (load-bearing)
- Action: Parse the QE output (or final structure file) to obtain the pseudocubic lattice parameter a (in Å) and the fractional coordinates of all atoms. Write to optimized_structure.csv in the same order as Table 1 of the paper: O, O, O, O, O, O, Fe, Nb, Pb, Pb.
- Output file: `/app/outputs/optimized_structure.csv`
- Format: csv
- Contract: Columns: lattice_parameter_a_angstrom (float), element (string), x_frac (float), y_frac (float), z_frac (float). First row: element='lattice', lattice_parameter_a_angstrom=<value>, x_frac=y_frac=z_frac=0. Subsequent rows: each atom in the order of Table 1 (O, O, O, O, O, O, Fe, Nb, Pb, Pb).
- Scoring: scored by hidden verifier

### Step 4: Berry-phase polarization of PbFeO3 and PbNbO3 subcells
- Role: process
- Action: Using the relaxed structure, perform nscf and Berry-phase polarization calculations with Quantum ESPRESSO to compute the spontaneous polarization of the PbFeO3 and PbNbO3 subcells.
- Evidence: none

### Step 5: Extract subcell polarization values
- Role: scored
- Action: Extract the spontaneous polarization values (in μC/cm²) for PbFeO3 and PbNbO3 subcells from the Berry-phase outputs and write to polarization_values.csv.
- Output file: `/app/outputs/polarization_values.csv`
- Format: csv
- Contract: Columns: subcell (string), polarization_muC_per_cm2 (float). Two rows: 'PbFeO3' and 'PbNbO3'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_structure.csv`
- `/app/outputs/polarization_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_structure.csv
- path: `/app/outputs/optimized_structure.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Equilibrium pseudocubic lattice parameter and fractional coordinates of the relaxed supercell.
- schema:
  - `type`: table
  - `required_columns`: `lattice_parameter_a_angstrom`, `element`, `x_frac`, `y_frac`, `z_frac`
  - `units`:
    - `lattice_parameter_a_angstrom`: angstrom

### polarization_values.csv
- path: `/app/outputs/polarization_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spontaneous polarization of PbFeO3 and PbNbO3 subcells.
- schema:
  - `type`: table
  - `required_columns`: `subcell`, `polarization_muC_per_cm2`
  - `units`:
    - `polarization_muC_per_cm2`: microC/cm^2

Notes: The checker compares the lattice parameter and fractional coordinates to the paper's reported values within tolerances. For polarization, it verifies that the polarization of PbNbO3 is larger than that of PbFeO3, and checks absolute values against the paper's reference within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_structure.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice_parameter_a_angstrom",
          "element",
          "x_frac",
          "y_frac",
          "z_frac"
        ],
        "units": {
          "lattice_parameter_a_angstrom": "angstrom"
        }
      },
      "description": "Equilibrium pseudocubic lattice parameter and fractional coordinates of the relaxed supercell."
    },
    {
      "file": "polarization_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "subcell",
          "polarization_muC_per_cm2"
        ],
        "units": {
          "polarization_muC_per_cm2": "microC/cm^2"
        }
      },
      "description": "Spontaneous polarization of PbFeO3 and PbNbO3 subcells."
    }
  ],
  "notes": "The checker compares the lattice parameter and fractional coordinates to the paper's reported values within tolerances. For polarization, it verifies that the polarization of PbNbO3 is larger than that of PbFeO3, and checks absolute values against the paper's reference within a tolerance."
}
```

## How you are scored
A hidden verifier examines the two CSV files you write under `/app/outputs`. It compares the reported lattice parameter, atomic coordinates, and sub‑cell polarizations to reference results obtained from the same DFT protocol. Tolerances are used to absorb the expected differences between a plane‑wave pseudopotential calculation and the all‑electron FLAPW results that served as the original reference. Both artifacts are scored independently, and the two scores are combined into an overall reward between 0.0 and 1.0. Simply reporting textbook values without actually executing the DFT workflow will not yield a high reward.
