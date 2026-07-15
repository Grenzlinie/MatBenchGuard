# Electric field-induced oxygen vacancy formation in YBa2Cu3O7 slab from DFT

## Problem background
Understanding the response of oxygen vacancies in YBa2Cu3O7 to external electric fields is crucial for explaining the superconductor-to-insulator transition observed in electrolyte gating experiments. This task investigates the formation energy of a single oxygen vacancy at the surface CuO chain under applied electric fields and the resulting structural relaxation, using first-principles density functional theory (DFT) calculations. The objective is to determine whether massive external fields can drive vacancy formation and to quantify the associated structural changes.

## Approach
The calculations are performed using density functional theory (DFT) with the PBE functional and ultrasoft pseudopotentials. A CuO chain-terminated YBa2Cu3O7 slab is constructed with a fixed in-plane lattice constant and vacuum. External electric fields are applied via a sawtooth potential, and a dipole correction is employed. The oxygen chemical potential is derived from a separate O2 molecule calculation. The vacancy formation energy is computed for a single oxygen vacancy at the surface CuO chain (configuration (a)) at several field strengths (0, 4, 6, 10, and 30 V/nm) using the formula ΔE_vac = (E_vac – E_stoi + μ_O)/n, where E_vac and E_stoi are the total energies of the defective and stoichiometric slabs, and μ_O is half the total energy of an isolated O2 molecule. Additionally, the relaxed atomic structure at the highest field is analyzed to extract the Cu–O_surface bond length and the O_plane–O_surface distance, providing a measure of the outward relaxation of the remaining surface oxygen.

## Reproduction target
The goal is to compute, for a single oxygen vacancy at the surface CuO chain of YBa2Cu3O7, the vacancy formation energy per vacancy (ΔE_vac) at applied electric fields of 0, 4, 6, 10, and 30 V/nm, and to report the relaxed Cu–O_surface bond length and O_plane–O_surface distance at 30 V/nm. The formation energies must be written to vacancy_formation_energies.csv with columns Field (V/nm) and Delta_E_vac (eV), containing exactly five rows. The structural distances must be written to structural_relaxation_30Vnm.json with keys Cu_O_surface_bond_length_A and O_plane_O_surface_distance_A as floating-point numbers. These artifacts will be evaluated by a hidden verifier.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- pslibrary (Rappe-Rabe-Kaxiras-Joannopoulos ultrasoft pseudopotentials): https://www.quantum-espresso.org/pseudopotentials/pslibrary

## Workflow steps

### Step 1: Slab model construction
- Role: process
- Action: Build the CuO chain-terminated YBa2Cu3O7 slab model: 2×2 in-plane supercell, 2 unit cells along z, fixed in-plane lattice constant 3.9419 Å, with vacuum layer and dipole correction. Write the input file(s) for the stoichiometric slab.
- Evidence: `/app/outputs/slab_input.pwi`

### Step 2: O2 molecule reference calculation
- Role: process
- Action: Perform a DFT calculation on an isolated O2 molecule using the same functional, pseudopotentials, and cutoffs to obtain total energy E_O2, from which the oxygen chemical potential μ_O = 0.5*E_O2 is derived.
- Evidence: `/app/outputs/o2_energy.txt`

### Step 3: Stoichiometric slab optimization at zero field
- Role: process
- Action: Perform geometry optimization of the stoichiometric YBCO slab (from step01) without electric field to obtain relaxed atomic positions and total energy E_stoi.
- Evidence: `/app/outputs/stoichiometric_opt.out`

### Step 4: Defective slab calculations under electric fields
- Role: process
- Action: Create a slab with a single oxygen vacancy at the surface CuO chain (configuration (a)). Perform geometry optimizations under applied electric fields of 0, 4, 6, 10, and 30 V/nm using a sawtooth potential and the same slab setup. Collect total energies E_vac and optimized geometries for each field.
- Evidence: `/app/outputs/vacancy_calculations.log`

### Step 5: Formation energy computation and reporting
- Role: scored (load-bearing)
- Action: For each applied electric field (0, 4, 6, 10, 30 V/nm), compute the vacancy formation energy per vacancy ΔE_vac = (E_vac – E_stoi + μ_O)/n using the energies from steps 02-04. Write the results to the output file.
- Output file: `/app/outputs/vacancy_formation_energies.csv`
- Format: csv
- Contract: CSV with columns: Field (V/nm), Delta_E_vac (eV).
- Scoring: scored by hidden verifier

### Step 6: Structural relaxation at 30 V/nm
- Role: scored (load-bearing)
- Action: From the 30 V/nm optimized geometry of step04, extract the Cu–O_surface bond length (distance between the surface Cu and the remaining chain oxygen) and the O_plane–O_surface distance (distance between the oxygen in the CuO2 plane and the surface oxygen). Write the values to a JSON file.
- Output file: `/app/outputs/structural_relaxation_30Vnm.json`
- Format: json
- Contract: JSON object with keys: "Cu_O_surface_bond_length_A", "O_plane_O_surface_distance_A". Values as floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/vacancy_formation_energies.csv`
- `/app/outputs/structural_relaxation_30Vnm.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### vacancy_formation_energies.csv
- path: `/app/outputs/vacancy_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Vacancy formation energy per vacancy for the surface CuO chain oxygen vacancy (configuration (a)) at applied electric fields of 0, 4, 6, 10, and 30 V/nm. Exactly 5 rows.
- schema:
  - `type`: table
  - `required_columns`: `Field (V/nm)`, `Delta_E_vac (eV)`
  - `items`: object
  - `units`:
    - `Field (V/nm)`: V/nm
    - `Delta_E_vac (eV)`: eV

### structural_relaxation_30Vnm.json
- path: `/app/outputs/structural_relaxation_30Vnm.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relaxed Cu–O_surface bond length and O_plane–O_surface distance at 30 V/nm, extracted from the optimized defective slab geometry.
- schema:
  - `type`: object
  - `required`:
    - `Cu_O_surface_bond_length_A`: float
    - `O_plane_O_surface_distance_A`: float
  - `items`: object
  - `units`:
    - `Cu_O_surface_bond_length_A`: Angstrom
    - `O_plane_O_surface_distance_A`: Angstrom

Notes: The task is a minimal reproduction of the spontaneous surface vacancy formation claim. Only configuration (a) is required. The checker will compare the reported formation energies and bond lengths to hidden paper reference values using absolute tolerances (e.g., 0.05 eV for energies, 0.05 Å for distances). The 30 V/nm formation energy must be negative.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "vacancy_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Field (V/nm)",
          "Delta_E_vac (eV)"
        ],
        "items": {},
        "units": {
          "Field (V/nm)": "V/nm",
          "Delta_E_vac (eV)": "eV"
        }
      },
      "description": "Vacancy formation energy per vacancy for the surface CuO chain oxygen vacancy (configuration (a)) at applied electric fields of 0, 4, 6, 10, and 30 V/nm. Exactly 5 rows."
    },
    {
      "file": "structural_relaxation_30Vnm.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Cu_O_surface_bond_length_A": "float",
          "O_plane_O_surface_distance_A": "float"
        },
        "items": {},
        "units": {
          "Cu_O_surface_bond_length_A": "Angstrom",
          "O_plane_O_surface_distance_A": "Angstrom"
        }
      },
      "description": "Relaxed Cu–O_surface bond length and O_plane–O_surface distance at 30 V/nm, extracted from the optimized defective slab geometry."
    }
  ],
  "notes": "The task is a minimal reproduction of the spontaneous surface vacancy formation claim. Only configuration (a) is required. The checker will compare the reported formation energies and bond lengths to hidden paper reference values using absolute tolerances (e.g., 0.05 eV for energies, 0.05 Å for distances). The 30 V/nm formation energy must be negative."
}
```

## How you are scored
Each scored output (vacancy_formation_energies.csv and structural_relaxation_30Vnm.json) is checked independently by a hidden verifier. The verifier compares your reported numbers to reference values using appropriate tolerances. For the formation energies, scoring is directional: meeting or exceeding the expected accuracy yields full credit, with progressively lower credit for larger deviations. For the structural distances, accuracy within tolerance is required. Additionally, the verifier validates that the output files exist, are correctly formatted, and contain all required rows and columns/keys. The final reward is a weighted combination of these checks.
