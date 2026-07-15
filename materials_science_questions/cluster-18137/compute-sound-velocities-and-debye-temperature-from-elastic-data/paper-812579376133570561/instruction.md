# Compute Sound Velocities and Debye Temperature from Elastic Data

## Problem background
Gadolinium zirconate (Gd2Zr2O7) pyrochlore is a candidate material for nuclear waste immobilization and thermal barrier coatings. Under irradiation, point defects such as vacancies, interstitials, and antisites can alter its mechanical and thermal stability. This task investigates how isolated point defects affect the elastic moduli, ductility, and Debye temperature of Gd2Zr2O7 by computing these properties from first principles.

## Approach
Use density functional theory with a Hubbard U correction (DFT+U) to model pristine Gd2Zr2O7 and five defective configurations containing a single point defect. For each configuration, perform geometry optimization followed by an elastic constant calculation via the strain–stress method. From the three independent elastic constants of the cubic crystal (C11, C12, C44), derive the Voigt–Reuss–Hill average bulk modulus, shear modulus, Young's modulus, Poisson's ratio, average sound velocity, and Debye temperature. Also verify that the mechanical stability criteria for cubic symmetry are satisfied. The baseline is the pristine structure; the defective configurations are compared against it to assess how each defect modifies the mechanical and thermal properties.

## Reproduction target
Compute and report the three independent elastic constants (C11, C12, C44), the Voigt–Reuss–Hill moduli (B_VRH, G_VRH, E), Poisson's ratio, average sound velocity, and Debye temperature for pristine Gd2Zr2O7 and for five defective configurations: V_O48f (O vacancy at the 48f site), Zr_Gd (Zr antisite on a Gd site), Gd_int2 (Gd interstitial at the int2 site), Zr_8a (Zr interstitial at the 8a site), and O_8a (O interstitial at the 8a site). Also report whether each configuration satisfies the cubic mechanical stability conditions (C11+2C12 > 0, C44 > 0, C11 - C12 > 0).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (v1.3.0 Efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python packages: numpy scipy ase
- Crystal structure of ideal Gd2Zr2O7 pyrochlore

## Workflow steps

### Step 1: DFT+U geometry optimization of pristine and defective structures
- Role: process
- Action: Perform DFT+U geometry relaxation of the pristine Gd2Zr2O7 supercell and five defective supercells (V_O48f, Zr_Gd, Gd_int2, Zr_8a, O_8a) using an open-source DFT code. Employ the PBE functional with Hubbard U correction on Gd 4f electrons, SSSP pseudopotentials for Gd, Zr, O, a kinetic energy cutoff of 600 eV, and a 2×2×2 Monkhorst–Pack k-mesh. Build each supercell from the ideal pyrochlore structure (Fd-3m, a0≈10.666 Å) and introduce the specified defect. Save the relaxed atomic positions and cell parameters.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Compute elastic constants, moduli, sound velocities, and Debye temperature
- Role: scored (load-bearing)
- Action: Using the relaxed structures from the previous step, compute the three independent elastic constants C11, C12, C44 for each configuration via the strain–stress method. From these constants, derive the Voigt–Reuss–Hill average bulk modulus B_VRH, shear modulus G_VRH, Young's modulus E, and Poisson's ratio. Compute mass density from the DFT lattice constant and molar mass. Calculate longitudinal sound velocity v_l, transverse sound velocity v_s, average sound velocity v_m, and Debye temperature θ_D using standard formulas. Also determine whether each configuration satisfies the cubic mechanical stability conditions (C11+2C12>0, C44>0, C11-C12>0). Output the results as a CSV file with one row per configuration.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: Columns: configuration (pristine, V_O48f, Zr_Gd, Gd_int2, Zr_8a, O_8a), C11 (GPa), C12 (GPa), C44 (GPa), B_VRH (GPa), G_VRH (GPa), E (GPa), Poisson_ratio (dimensionless), v_m (m/s), Debye_T (K), stable_C1p2 (bool), stable_C4 (bool), stable_C11mC12 (bool).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file containing the computed elastic constants, moduli, average sound velocity, Debye temperature, and stability indicators for the pristine and five defective Gd2Zr2O7 configurations. The checker compares each value against hidden reference values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `configuration`, `C11`, `C12`, `C44`, `B_VRH`, `G_VRH`, `E`, `Poisson_ratio`, `v_m`, `Debye_T`, `stable_C1p2`, `stable_C4`, `stable_C11mC12`
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa
    - `B_VRH`: GPa
    - `G_VRH`: GPa
    - `E`: GPa
    - `Poisson_ratio`: dimensionless
    - `v_m`: m/s
    - `Debye_T`: K
    - `stable_C1p2`: boolean
    - `stable_C4`: boolean
    - `stable_C11mC12`: boolean

Notes: The public instruction will describe the task as computing elastic properties and thermal quantities from first principles for a pyrochlore material, without naming the specific reference values. The agent must perform all DFT calculations; no pre-computed structures or constants are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "configuration",
          "C11",
          "C12",
          "C44",
          "B_VRH",
          "G_VRH",
          "E",
          "Poisson_ratio",
          "v_m",
          "Debye_T",
          "stable_C1p2",
          "stable_C4",
          "stable_C11mC12"
        ],
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa",
          "B_VRH": "GPa",
          "G_VRH": "GPa",
          "E": "GPa",
          "Poisson_ratio": "dimensionless",
          "v_m": "m/s",
          "Debye_T": "K",
          "stable_C1p2": "boolean",
          "stable_C4": "boolean",
          "stable_C11mC12": "boolean"
        }
      },
      "description": "CSV file containing the computed elastic constants, moduli, average sound velocity, Debye temperature, and stability indicators for the pristine and five defective Gd2Zr2O7 configurations. The checker compares each value against hidden reference values with appropriate tolerances."
    }
  ],
  "notes": "The public instruction will describe the task as computing elastic properties and thermal quantities from first principles for a pyrochlore material, without naming the specific reference values. The agent must perform all DFT calculations; no pre-computed structures or constants are provided."
}
```

## How you are scored
A hidden verifier independently examines the output of each scored workflow step and combines them into a final reward between 0 and 1. You are scored on the accuracy of your computed elastic constants, moduli, sound velocities, Debye temperatures, and mechanical stability assessments relative to reference values derived from the published study. Reporting a value is not sufficient; the underlying calculations must be performed as described in the workflow steps, and the submitted artifacts must conform to the required formats and contracts.
