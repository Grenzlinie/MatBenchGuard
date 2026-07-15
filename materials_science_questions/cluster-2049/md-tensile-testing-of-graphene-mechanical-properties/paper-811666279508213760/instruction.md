# Size-dependent elastic properties of single-walled ZnO nanotubes from first principles

## Problem background
Single-walled ZnO nanotubes (SWZONTs) are predicted to form as rolled-up graphitic sheets analogous to carbon nanotubes. Their mechanical and electronic properties are expected to depend on both diameter and chirality. This task investigates how the binding energy, Young's modulus, Zn–O bond length, and charge transfer vary with tube diameter for armchair and zigzag SWZONTs, and how these properties compare to the flat ZnO graphitic sheet limit. Understanding these size-dependent trends is important for applications of ZnO nanotubes in nanoelectromechanical systems.

## Approach
The analysis proceeds by constructing atomic models of armchair (n,n) and zigzag (n,0) SWZONTs for a range of diameters by rolling a ZnO graphitic sheet. First-principles density functional theory (DFT) calculations using the PW91 functional are performed to relax all structures and obtain total energies. Uniaxial strain simulations are then applied along the tube axis to extract the strain-energy relation, from which Young's modulus is derived via the second derivative of energy with respect to strain at the equilibrium state. Bader charge analysis quantifies the amount of charge transferred from Zn to O atoms. The computed properties are compared across tube diameters and chiralities, and against the planar sheet to probe the approach to the infinite-diameter limit.

## Reproduction target
Construct and compute, using an open-source DFT package (e.g., Quantum ESPRESSO), the binding energy per ZnO unit, Young's modulus, average Zn–O bond length, and Bader charge transfer for armchair (n,n) and zigzag (n,0) single-walled ZnO nanotubes with n = 3 to 10, and for a ZnO graphitic sheet. Report all results in a CSV file at `/app/outputs/swzont_computed_properties.csv` with the columns specified in the workflow steps and output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Bader charge analysis code (Henkelman group): http://theory.cm.utexas.edu/henkelman/code/bader/
- Atomic Simulation Environment (ASE): ase
- PW91 pseudopotentials for Zn and O: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Generate SWZONT structures and graphitic sheet
- Role: process
- Action: Construct armchair (n,n) and zigzag (n,0) single-walled ZnO nanotubes for n=3 to 10 by rolling a ZnO graphitic sheet using appropriate literature lattice constants. Also create a ZnO graphitic sheet supercell.
- Evidence: `/app/outputs/structure_generation.log`

### Step 2: DFT geometry optimization of all structures
- Role: process
- Action: Perform DFT geometry optimization on all tube structures (n=3..10, both chiralities) and the sheet using Quantum ESPRESSO with the PW91-GGA functional, relaxing until forces and energies are converged to standard criteria. Record optimized atomic positions and total energies.
- Evidence: `/app/outputs/relaxation_summary.txt`

### Step 3: Uniaxial strain simulations
- Role: process
- Action: For each relaxed tube and the sheet, apply a series of uniaxial strains along the tube axis, covering a range from compressive to tensile (e.g., -2% to +2%) in small increments. At each strain step, relax the structure (keeping the strained cell) and record the total energy, obtaining energy versus strain curves.
- Evidence: `/app/outputs/strain_energy_curves.txt`

### Step 4: Compute all properties and write scored CSV
- Role: scored (load-bearing)
- Action: From the optimized geometries and strain-energy data, compute the following for each tube and the sheet: (i) diameter d as the average of the Zn and O cylindrical surface diameters; (ii) binding energy per ZnO unit from the relaxed total energy; (iii) Young's modulus by fitting a parabola to the energy vs. strain data at zero strain and dividing the curvature by the equilibrium volume; (iv) average Zn-O bond length from the relaxed coordinates; (v) charge transfer amount from Zn to O using Bader analysis on the charge density of the optimized structure. Write a CSV file with columns: chirality (armchair/zigzag/sheet), n (tube index, 0 for sheet), diameter (Å), binding_energy_eV_per_ZnO (eV), youngs_modulus_GPa (GPa), avg_bond_length_ang (Å), charge_transfer_e (e). For the sheet, set diameter to a large representative value (e.g., 999) or 'inf'.
- Output file: `/app/outputs/swzont_computed_properties.csv`
- Format: csv
- Contract: chirality (str), n (int, 0 for sheet), diameter (float, Å), binding_energy_eV_per_ZnO (float, eV), youngs_modulus_GPa (float, GPa), avg_bond_length_ang (float, Å), charge_transfer_e (float, e)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/swzont_computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### swzont_computed_properties.csv
- path: `/app/outputs/swzont_computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file containing the computed diameter, binding energy per ZnO unit, Young's modulus, average Zn-O bond length, and Bader charge transfer for armchair (n,n) and zigzag (n,0) SWZONTs (n=3..10) and the ZnO graphitic sheet.
- schema:
  - `type`: table
  - `required_columns`: `chirality`, `n`, `diameter`, `binding_energy_eV_per_ZnO`, `youngs_modulus_GPa`, `avg_bond_length_ang`, `charge_transfer_e`
  - `units`:
    - `diameter`: Å
    - `binding_energy_eV_per_ZnO`: eV
    - `youngs_modulus_GPa`: GPa
    - `avg_bond_length_ang`: Å
    - `charge_transfer_e`: e

Notes: The checker verifies that the computed properties exhibit the expected physical trends (monotonic changes with diameter, chirality differences, and convergence to the graphitic sheet limit) without disclosing the specific direction of each trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "swzont_computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "chirality",
          "n",
          "diameter",
          "binding_energy_eV_per_ZnO",
          "youngs_modulus_GPa",
          "avg_bond_length_ang",
          "charge_transfer_e"
        ],
        "units": {
          "diameter": "Å",
          "binding_energy_eV_per_ZnO": "eV",
          "youngs_modulus_GPa": "GPa",
          "avg_bond_length_ang": "Å",
          "charge_transfer_e": "e"
        }
      },
      "description": "CSV file containing the computed diameter, binding energy per ZnO unit, Young's modulus, average Zn-O bond length, and Bader charge transfer for armchair (n,n) and zigzag (n,0) SWZONTs (n=3..10) and the ZnO graphitic sheet."
    }
  ],
  "notes": "The checker verifies that the computed properties exhibit the expected physical trends (monotonic changes with diameter, chirality differences, and convergence to the graphitic sheet limit) without disclosing the specific direction of each trend."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that inspects the scored CSV file and checks whether your computed properties exhibit the correct structural relationships: required monotonic trends with tube diameter, correct relative ordering between armchair and zigzag nanotubes, and consistency with the graphitic sheet limit. The verifier does not require exact numerical agreement with any published values; scoring is based on the fraction of satisfied trend checks. Process evidence files are also inspected for completeness but carry low weight. The final reward is a combined score across all stages, with the main property CSV carrying the largest share.
