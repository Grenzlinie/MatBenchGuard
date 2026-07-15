# First-principles elastic constants and Debye temperature of BaS and BaSe

## Problem background
Barium chalcogenides BaS and BaSe are wide-gap ionic insulators that crystallize in the NaCl (B1) structure. They have potential applications in microelectronics, light-emitting diodes, and laser diodes. Accurate knowledge of their structural, elastic, and thermal properties—including elastic stiffness coefficients, bulk modulus, sound velocities, and Debye temperature—is essential for materials design and for understanding their mechanical and thermal behavior. First-principles density functional theory (DFT) can predict these quantities from the crystal structure and the constituent atoms, providing a route to characterize materials where experimental data may be scarce or difficult to obtain.

## Approach
The workflow follows a standard first-principles computational scheme:

- Use plane-wave pseudopotential DFT with the generalized gradient approximation (GGA) in the Perdew–Burke–Ernzerhof (PBE) form, as implemented in an open-source DFT code such as Quantum ESPRESSO. Pseudopotentials for Ba, S, and Se are taken from a public library (SSSP efficiency set).
- Determine the equilibrium lattice constant and bulk modulus by computing total energies at a series of lattice parameters and fitting the resulting energy‑volume data to the Vinet equation of state.
- Compute the three independent elastic constants of the cubic lattice (C₁₁, C₁₂, C₄₄) by applying small volume‑conserving tetragonal and orthorhombic strains to the equilibrium cell. For each strain pattern and magnitude, perform a self-consistent calculation with internal relaxations; fit the energy‑strain curves to extract the stiffness coefficients.
- From the elastic constants and equilibrium lattice constant, derive the isotropic shear moduli using Voigt and Reuss averaging, the elastic anisotropy ratio, Poisson’s ratio, and the density. Then compute the transverse, longitudinal, and mean sound velocities, and finally the Debye temperature.

All calculations are carried out for both BaS and BaSe.

## Reproduction target
Produce a single JSON file at `/app/outputs/step_01_results.json`. The file must contain an array of two objects, one for BaS and one for BaSe, each with the following keys and appropriate numeric values (units indicated):

- `compound` (string: 'BaS' or 'BaSe')
- `lattice_constant_A` (float, Å)
- `bulk_modulus_GPa` (float, GPa)
- `bulk_modulus_derivative` (float, dimensionless)
- `C11_GPa`, `C12_GPa`, `C44_GPa` (float, GPa)
- `shear_modulus_Voigt_GPa`, `shear_modulus_Reuss_GPa`, `shear_modulus_isotropic_GPa` (float, GPa)
- `anisotropy_ratio` (float, dimensionless)
- `poisson_ratio` (float, dimensionless)
- `transverse_velocity_kms`, `longitudinal_velocity_kms`, `mean_velocity_kms` (float, km/s)
- `debye_temperature_K` (float, K)

The values must be obtained from a self‑consistent DFT calculation with the GGA‑PBE functional using an open‑source plane‑wave pseudopotential code, as described in the workflow steps.

## Assets

- Quantum ESPRESSO (open-source DFT package): https://www.quantum-espresso.org/
- SSSP GGA-PBE pseudopotentials for Ba, S, Se: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT total energy vs volume calculations
- Role: process
- Action: For both BaS and BaSe in NaCl-type structure, run multiple DFT self-consistent field (SCF) calculations at different lattice parameters spanning at least ±10% of equilibrium to produce energy-volume data points. Use GGA-PBE functional, SSSP pseudopotentials, and converged k-point grid and plane-wave cutoff. Perform fixed-volume relaxations to minimize forces at each volume.
- Evidence: none

### Step 2: Vinet equation of state fitting
- Role: process
- Action: Fit the energy-volume data to the Vinet equation of state to obtain equilibrium lattice constant a0, bulk modulus B, and pressure derivative B' for each compound. Use a robust fitting procedure on the E(V) data.
- Evidence: none

### Step 3: Elastic constants from volume-conserving strains
- Role: process
- Action: Compute the three independent cubic elastic constants C11, C12, C44 for each compound. Apply tetragonal and orthorhombic volume-conserving strain patterns. For each strain pattern and magnitude, perform fully relaxed DFT calculations at fixed cell shape and compute total energies. Fit energy vs strain to extract the stiffness coefficients.
- Evidence: none

### Step 4: Derived isotropic and thermal quantities and final report
- Role: scored (load-bearing)
- Action: From the computed lattice constants, bulk moduli, elastic constants, and atomic masses: compute Voigt and Reuss shear moduli (via standard cubic formulas), isotropic shear modulus (average), elastic anisotropy ratio A = 2*C44/(C11-C12), Poisson's ratio using bulk modulus and isotropic shear modulus, density from lattice constant, and transverse, longitudinal, and mean sound velocities; then compute Debye temperature from mean velocity and density. Assemble all quantities into a JSON file with one entry per compound.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: Array of two JSON objects. Required keys: compound (string, 'BaS' or 'BaSe'), lattice_constant_A (float), bulk_modulus_GPa (float), bulk_modulus_derivative (float), C11_GPa (float), C12_GPa (float), C44_GPa (float), shear_modulus_Voigt_GPa (float), shear_modulus_Reuss_GPa (float), shear_modulus_isotropic_GPa (float), anisotropy_ratio (float), poisson_ratio (float), transverse_velocity_kms (float), longitudinal_velocity_kms (float), mean_velocity_kms (float), debye_temperature_K (float). All values in the stated units.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final material properties for BaS and BaSe computed from DFT and elastic derivations.
- schema:
  - `type`: array
  - `required`:
    - `compound`: string
    - `lattice_constant_A`: float
    - `bulk_modulus_GPa`: float
    - `bulk_modulus_derivative`: float
    - `C11_GPa`: float
    - `C12_GPa`: float
    - `C44_GPa`: float
    - `shear_modulus_Voigt_GPa`: float
    - `shear_modulus_Reuss_GPa`: float
    - `shear_modulus_isotropic_GPa`: float
    - `anisotropy_ratio`: float
    - `poisson_ratio`: float
    - `transverse_velocity_kms`: float
    - `longitudinal_velocity_kms`: float
    - `mean_velocity_kms`: float
    - `debye_temperature_K`: float
  - `items`:
    - `compound`: string
    - `lattice_constant_A`: float (Angstrom)
    - `bulk_modulus_GPa`: float (GPa)
    - `bulk_modulus_derivative`: float (dimensionless)
    - `C11_GPa`: float (GPa)
    - `C12_GPa`: float (GPa)
    - `C44_GPa`: float (GPa)
    - `shear_modulus_Voigt_GPa`: float (GPa)
    - `shear_modulus_Reuss_GPa`: float (GPa)
    - `shear_modulus_isotropic_GPa`: float (GPa)
    - `anisotropy_ratio`: float (dimensionless)
    - `poisson_ratio`: float (dimensionless)
    - `transverse_velocity_kms`: float (km/s)
    - `longitudinal_velocity_kms`: float (km/s)
    - `mean_velocity_kms`: float (km/s)
    - `debye_temperature_K`: float (K)
  - `units`:
    - `lattice_constant_A`: Angstrom
    - `bulk_modulus_GPa`: GPa
    - `bulk_modulus_derivative`: dimensionless
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C44_GPa`: GPa
    - `shear_modulus_Voigt_GPa`: GPa
    - `shear_modulus_Reuss_GPa`: GPa
    - `shear_modulus_isotropic_GPa`: GPa
    - `anisotropy_ratio`: dimensionless
    - `poisson_ratio`: dimensionless
    - `transverse_velocity_kms`: km/s
    - `longitudinal_velocity_kms`: km/s
    - `mean_velocity_kms`: km/s
    - `debye_temperature_K`: K

Notes: Values will be compared to hidden reference (paper‑reported) data using tolerances that account for typical toolchain and pseudopotential variability. Internal self‑consistency (bulk modulus from elastic constants vs from EOS) may also be checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": {
          "compound": "string",
          "lattice_constant_A": "float",
          "bulk_modulus_GPa": "float",
          "bulk_modulus_derivative": "float",
          "C11_GPa": "float",
          "C12_GPa": "float",
          "C44_GPa": "float",
          "shear_modulus_Voigt_GPa": "float",
          "shear_modulus_Reuss_GPa": "float",
          "shear_modulus_isotropic_GPa": "float",
          "anisotropy_ratio": "float",
          "poisson_ratio": "float",
          "transverse_velocity_kms": "float",
          "longitudinal_velocity_kms": "float",
          "mean_velocity_kms": "float",
          "debye_temperature_K": "float"
        },
        "items": {
          "compound": "string",
          "lattice_constant_A": "float (Angstrom)",
          "bulk_modulus_GPa": "float (GPa)",
          "bulk_modulus_derivative": "float (dimensionless)",
          "C11_GPa": "float (GPa)",
          "C12_GPa": "float (GPa)",
          "C44_GPa": "float (GPa)",
          "shear_modulus_Voigt_GPa": "float (GPa)",
          "shear_modulus_Reuss_GPa": "float (GPa)",
          "shear_modulus_isotropic_GPa": "float (GPa)",
          "anisotropy_ratio": "float (dimensionless)",
          "poisson_ratio": "float (dimensionless)",
          "transverse_velocity_kms": "float (km/s)",
          "longitudinal_velocity_kms": "float (km/s)",
          "mean_velocity_kms": "float (km/s)",
          "debye_temperature_K": "float (K)"
        },
        "units": {
          "lattice_constant_A": "Angstrom",
          "bulk_modulus_GPa": "GPa",
          "bulk_modulus_derivative": "dimensionless",
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C44_GPa": "GPa",
          "shear_modulus_Voigt_GPa": "GPa",
          "shear_modulus_Reuss_GPa": "GPa",
          "shear_modulus_isotropic_GPa": "GPa",
          "anisotropy_ratio": "dimensionless",
          "poisson_ratio": "dimensionless",
          "transverse_velocity_kms": "km/s",
          "longitudinal_velocity_kms": "km/s",
          "mean_velocity_kms": "km/s",
          "debye_temperature_K": "K"
        }
      },
      "description": "Final material properties for BaS and BaSe computed from DFT and elastic derivations."
    }
  ],
  "notes": "Values will be compared to hidden reference (paper‑reported) data using tolerances that account for typical toolchain and pseudopotential variability. Internal self‑consistency (bulk modulus from elastic constants vs from EOS) may also be checked."
}
```

## How you are scored
A hidden verifier independently checks each workflow stage's artifact and combines them by weight into the final reward. Your submission will be compared to a set of reference values (hidden gold) using relative tolerances appropriate for the methods and pseudopotentials employed. In addition, the verifier checks internal consistency: for each compound, the bulk modulus computed from the elastic constants via \(B = (C_{11} + 2C_{12})/3\) must agree with the submitted `bulk_modulus_GPa` within a reasonable margin. The final reward is a weighted average over all quantities, with larger weight on the headline elastic constants and bulk modulus. Credit decreases only when your results deviate from the reference beyond the expected reproducibility margin; results that agree within tolerance receive full credit. You do not need to match any particular code or pseudopotential exactly, but your workflow must follow the described protocol.
