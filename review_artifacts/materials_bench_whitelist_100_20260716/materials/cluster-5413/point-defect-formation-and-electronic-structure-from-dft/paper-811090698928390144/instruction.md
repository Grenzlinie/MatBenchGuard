# Ferroelectric polarization induced by native defects in SrTiO3 (DFT)

## Problem background
Intrinsic point defects in the perovskite oxide SrTiO3, such as titanium-strontium (Ti_Sr) and strontium-titanium (Sr_Ti) antisite defects, can induce local ferroelectric polarization within the material. The addition of oxygen vacancies can further alter this polarization behavior. This task aims to quantify the spontaneous polarization and the energy barriers for polarization switching that arise from individual antisite defects and from a Ti_Sr antisite bound to an oxygen vacancy, using density functional theory (DFT).

## Approach
The calculations are performed with DFT using the PBEsol exchange-correlation functional augmented by a Hubbard U correction (U_eff = 4.36 eV) on the Ti 3d states. The workflow begins by optimizing the bulk SrTiO3 lattice constant and constructing a 3×3×3 supercell (135 atoms). For each defect system (Ti_Sr antisite, Sr_Ti antisite, and Ti_Sr+V_O complex), the most stable off-centered geometry is determined by ionic relaxation from multiple initial displacement directions. Once the most stable structure is found, the following quantities are computed: the off-centering displacement (magnitude and direction), the Born effective charge of the off-centered cation using a finite-difference approach, the spontaneous polarization of the supercell using the Berry phase method, and the lowest-energy polarization switching barrier using the climbing image nudged elastic band (CI-NEB) method. All DFT calculations use the open-source Quantum ESPRESSO package with PBEsol pseudopotentials.

## Reproduction target
Using Quantum ESPRESSO with the PBEsol+U functional (U_eff = 4.36 eV on Ti 3d) and appropriate PBEsol pseudopotentials, perform DFT calculations on a 3×3×3 SrTiO3 supercell at the optimized lattice constant. For the Ti_Sr antisite defect, the Sr_Ti antisite defect, and the Ti_Sr antisite bound with a doubly charged oxygen vacancy (V_O••) complex, compute: (1) the off-centering displacement (magnitude in Å and crystallographic direction), (2) the Born effective charge of the off-centered cation, (3) the spontaneous polarization (in μC/cm²) of the supercell, and (4) the lowest-energy polarization switching barrier (in eV). Write the collected results to the file defect_polarization_results.csv in the required format.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBEsol pseudopotentials for Sr, Ti, O: https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Optimize bulk SrTiO3 lattice constant
- Role: process
- Action: Perform a variable-cell DFT relaxation of the cubic SrTiO3 unit cell using PBEsol+U (U_eff=4.36 eV) to obtain the equilibrium lattice constant. Fix the lattice constant to this optimized value for all subsequent defect supercell calculations.
- Evidence: none

### Step 2: Generate 3×3×3 SrTiO3 supercell
- Role: process
- Action: Construct a 3×3×3 supercell (135 atoms) of SrTiO3 from the optimized bulk structure. This supercell will be used for all defect calculations.
- Evidence: none

### Step 3: Relax Ti_Sr antisite defect
- Role: process
- Action: In the supercell, replace one Sr atom with Ti to create the Ti_Sr antisite defect. Create initial structures with the antisite Ti displaced along [100], [110], [111] and the non-shifted configuration. Perform ionic relaxation (fixed cell) for each configuration to identify the most stable off-centered geometry and record its displacement.
- Evidence: none

### Step 4: Relax Sr_Ti antisite defect
- Role: process
- Action: In the supercell, replace one Ti atom with Sr to create the Sr_Ti antisite defect. Create initial structures with the antisite Sr displaced along [110] and [100]. Perform ionic relaxation to find the most stable off-centered geometry.
- Evidence: none

### Step 5: Relax Ti_Sr + V_O•• defect complex
- Role: process
- Action: In the supercell containing the Ti_Sr antisite, introduce a doubly charged oxygen vacancy (V_O••) at several nearest-neighbor sites. For each, create configurations with the antisite Ti displaced towards and away from the vacancy. Perform non-spin-polarised ionic relaxations to identify the most stable complex (lowest energy) and its off-centering.
- Evidence: none

### Step 6: Compute defect properties and output results
- Role: scored (load-bearing)
- Action: Using the relaxed geometries from steps 03-05, compute for each defect: the off-centering displacement (magnitude and direction), Born effective charge of the off-centered cation (via finite-difference polarization), spontaneous polarization of the supercell (Berry phase), and the lowest-energy polarization switching barrier (using CI-NEB). Write the collected results to defect_polarization_results.csv.
- Output file: `/app/outputs/defect_polarization_results.csv`
- Format: csv
- Contract: Columns: defect (string), displacement_A (float, Å), displacement_dir (string), born_charge (float), polarization_uCcm2 (float, μC/cm²), barrier_eV (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_polarization_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_polarization_results.csv
- path: `/app/outputs/defect_polarization_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed defect properties (off-centering, Born charge, polarization, switching barrier) for Ti_Sr, Sr_Ti, and Ti_Sr_V_O defects.
- schema:
  - `type`: table
  - `required_columns`: `defect`, `displacement_A`, `displacement_dir`, `born_charge`, `polarization_uCcm2`, `barrier_eV`
  - `units`:
    - `displacement_A`: Angstrom
    - `born_charge`: 
    - `polarization_uCcm2`: μC/cm²
    - `barrier_eV`: eV

Notes: The checker compares each numeric value to hidden gold values from the paper within appropriate tolerances and verifies relative trends (polarization order, barrier order).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_polarization_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "displacement_A",
          "displacement_dir",
          "born_charge",
          "polarization_uCcm2",
          "barrier_eV"
        ],
        "units": {
          "displacement_A": "Angstrom",
          "born_charge": "",
          "polarization_uCcm2": "μC/cm²",
          "barrier_eV": "eV"
        }
      },
      "description": "Computed defect properties (off-centering, Born charge, polarization, switching barrier) for Ti_Sr, Sr_Ti, and Ti_Sr_V_O defects."
    }
  ],
  "notes": "The checker compares each numeric value to hidden gold values from the paper within appropriate tolerances and verifies relative trends (polarization order, barrier order)."
}
```

## How you are scored
A hidden verifier independently examines the final defect_polarization_results.csv file. It checks each computed numeric value (displacement, Born charge, polarization, barrier) against reference values within defined tolerances and also verifies relative trends across the three defect systems (e.g., the ordering of spontaneous polarization and the ordering of switching barriers). The intermediate process steps are required to produce the final artifact, but only the values and trends in the CSV are scored. The final reward is a weighted combination of these checks; reporting numbers alone without executing the full workflow will not produce a passing score.
