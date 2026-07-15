# DFT-based elastic constants and mechanical properties of bcc W-Re-Os alloys

## Problem background
Neutron transmutation in tungsten plasma-facing components of fusion reactors produces rhenium (Re) and osmium (Os) as the dominant transmutation products, modifying the mechanical properties of the alloy. Understanding how the concentration of these solutes affects the elastic and plastic behavior of body-centered cubic (bcc) tungsten-rich alloys is essential for predicting the lifetime and performance of first-wall materials. This task quantifies the single-crystal and polycrystalline elastic moduli, ductility indicators, and solid-solution hardening trends as functions of Re and Os content using first-principles calculations.

## Approach
Use density functional theory (DFT) within the generalized gradient approximation (Perdew–Burke–Ernzerhof, PBE) to compute total energies of bcc W-Re-Os random alloys. For selected compositions (pure W, binary W-Re and W-Os alloys with up to 6 at.% solute, and one ternary composition), obtain equilibrium lattice constants and bulk moduli from equation-of-state fits. Extract the single-crystal elastic constants C11, C12, C44, and the tetragonal shear modulus C' from volume-conserving orthorhombic and monoclinic distortions by fitting strain-energy relations. From these, derive polycrystalline shear and Young's moduli (Hill average), Poisson's ratio, the bulk-to-shear modulus ratio (B/G), Cauchy pressure, Zener anisotropy, and Debye temperature. Optionally estimate solid‑solution hardening (SSH) parameters for binary alloys using the Labusch–Nabarro model, compute the fcc–bcc structural energy difference, and approximate the ideal tensile strength in the [001] direction. Perform all calculations with an open-source plane-wave DFT code (Quantum ESPRESSO) and standard SSSP PBE pseudopotentials.

## Reproduction target
Produce two scored JSON artifacts. The file single_crystal_elastic_constants.json must contain the lattice constant, bulk modulus, and single-crystal elastic constants (C11, C12, C44, C') for at least the following compositions: pure W, W₀.₉₇Re₀.₀₃, W₀.₉₄Re₀.₀₆, W₀.₉₇Os₀.₀₃, W₀.₉₄Os₀.₀₆, and W₀.₉₄Re₀.₀₃Os₀.₀₃. The file derived_properties.json must contain, for the same set of compositions, the polycrystalline shear modulus (Hill average), Young's modulus, Poisson's ratio, B/G ratio, Cauchy pressure, Debye temperature, and Zener anisotropy. Additional compositions and optional fields (cleavage ratio, solid‑solution hardening misfit parameters and SSH factor for binary compositions, fcc–bcc structural energy difference, and ideal tensile strength in [001]) may be included; report null for any parameter that is not computed or not applicable.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials for W, Re, Os: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT total energy calculations for W-Re-Os alloys
- Role: process
- Action: Run Quantum ESPRESSO (or equivalent plane-wave DFT code) to compute total energies for the bcc equilibrium structures and for volume-conserving orthorhombic and monoclinic distorted structures of pure W, W1-xRex (x=0.03,0.06), W1-yOsy (y=0.03,0.06), and one ternary composition (e.g., W0.94Re0.03Os0.03). Use SSSP PBE pseudopotentials, a sufficiently dense k-point mesh, and an appropriate energy cutoff. Output total energies for each composition, distortion type, and strain value.
- Evidence: `/app/outputs/dft_energies.csv`

### Step 2: Single-crystal elastic constants
- Role: scored (load-bearing)
- Action: From the DFT total energies, fit an equation of state to obtain equilibrium lattice constant and bulk modulus for each composition. Fit the orthorhombic strain energies to the energy change ΔE(δ0) = 2V C′ δ0² to extract the tetragonal shear modulus C′, and the monoclinic strain energies to the relation ΔE(δm) = 2V C44 δm² to extract the cubic shear modulus C44. Compute C11 = B + 4C′/3 and C12 = B − 2C′/3. Write results to single_crystal_elastic_constants.json.
- Output file: `/app/outputs/single_crystal_elastic_constants.json`
- Format: json
- Contract: [ {"Re": float, "Os": float, "lattice_constant_Angstrom": float, "bulk_modulus_GPa": float, "C11_GPa": float, "C12_GPa": float, "C44_GPa": float, "Cprime_GPa": float} ]
- Scoring: scored by hidden verifier

### Step 3: Derived polycrystalline and mechanical properties
- Role: scored
- Action: Using the computed elastic constants and lattice constants, compute polycrystalline shear modulus (Hill average), Young's modulus, Poisson ratio, B/G ratio, Cauchy pressure, Zener anisotropy A_Z, and Debye temperature. Optionally compute cleavage ratio χ_{110} (requires slab DFT for {110} surface energies), solid-solution hardening misfit parameters and SSH factor (for binary compositions), fcc-bcc structural energy difference, and estimated ideal tensile strength in [001]. Write all results to derived_properties.json.
- Output file: `/app/outputs/derived_properties.json`
- Format: json
- Contract: [ {"Re": float, "Os": float, "shear_modulus_Hill_GPa": float, "youngs_modulus_GPa": float, "poisson_ratio": float, "B_over_G": float, "cauchy_pressure_GPa": float, "debye_temperature_K": float, "Zener_anisotropy_AZ": float, "cleavage_ratio_110": float|null, "solid_solution_hardening_misfit_epsilon_L": float|null, "solid_solution_hardening_factor": float|null, "fcc_bcc_SED_J_per_atom": float|null, "estimated_ideal_tensile_strength_001_GPa": float|null} ]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/single_crystal_elastic_constants.json`
- `/app/outputs/derived_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### single_crystal_elastic_constants.json
- path: `/app/outputs/single_crystal_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single-crystal elastic constants, lattice parameter, and bulk modulus for selected W-Re-Os alloy compositions. All values are from DFT calculations.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `Re`, `Os`, `lattice_constant_Angstrom`, `bulk_modulus_GPa`, `C11_GPa`, `C12_GPa`, `C44_GPa`, `Cprime_GPa`
    - `properties`:
      - `Re`:
        - `type`: number
      - `Os`:
        - `type`: number
      - `lattice_constant_Angstrom`:
        - `type`: number
      - `bulk_modulus_GPa`:
        - `type`: number
      - `C11_GPa`:
        - `type`: number
      - `C12_GPa`:
        - `type`: number
      - `C44_GPa`:
        - `type`: number
      - `Cprime_GPa`:
        - `type`: number

### derived_properties.json
- path: `/app/outputs/derived_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Polycrystalline moduli, ductility indicators, Debye temperature, elastic anisotropy, and optional cleavage ratio, solid-solution hardening parameters, and ideal tensile strength derived from the single-crystal elastic constants.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `Re`, `Os`, `shear_modulus_Hill_GPa`, `youngs_modulus_GPa`, `poisson_ratio`, `B_over_G`, `cauchy_pressure_GPa`, `debye_temperature_K`, `Zener_anisotropy_AZ`
    - `optional`: `cleavage_ratio_110`, `solid_solution_hardening_misfit_epsilon_L`, `solid_solution_hardening_factor`, `fcc_bcc_SED_J_per_atom`, `estimated_ideal_tensile_strength_001_GPa`
    - `properties`:
      - `Re`:
        - `type`: number
      - `Os`:
        - `type`: number
      - `shear_modulus_Hill_GPa`:
        - `type`: number
      - `youngs_modulus_GPa`:
        - `type`: number
      - `poisson_ratio`:
        - `type`: number
      - `B_over_G`:
        - `type`: number
      - `cauchy_pressure_GPa`:
        - `type`: number
      - `debye_temperature_K`:
        - `type`: number
      - `Zener_anisotropy_AZ`:
        - `type`: number
      - `cleavage_ratio_110`:
        - `type`: `number`, `null`
      - `solid_solution_hardening_misfit_epsilon_L`:
        - `type`: `number`, `null`
      - `solid_solution_hardening_factor`:
        - `type`: `number`, `null`
      - `fcc_bcc_SED_J_per_atom`:
        - `type`: `number`, `null`
      - `estimated_ideal_tensile_strength_001_GPa`:
        - `type`: `number`, `null`

Notes: The target is the paper-reported elastic constants, lattice parameter, bulk modulus, and derived polycrystalline properties. Internal consistency (C11+2C12)/3 = B and C' = (C11-C12)/2 is checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "single_crystal_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "Re",
            "Os",
            "lattice_constant_Angstrom",
            "bulk_modulus_GPa",
            "C11_GPa",
            "C12_GPa",
            "C44_GPa",
            "Cprime_GPa"
          ],
          "properties": {
            "Re": {
              "type": "number"
            },
            "Os": {
              "type": "number"
            },
            "lattice_constant_Angstrom": {
              "type": "number"
            },
            "bulk_modulus_GPa": {
              "type": "number"
            },
            "C11_GPa": {
              "type": "number"
            },
            "C12_GPa": {
              "type": "number"
            },
            "C44_GPa": {
              "type": "number"
            },
            "Cprime_GPa": {
              "type": "number"
            }
          }
        }
      },
      "description": "Single-crystal elastic constants, lattice parameter, and bulk modulus for selected W-Re-Os alloy compositions. All values are from DFT calculations."
    },
    {
      "file": "derived_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "Re",
            "Os",
            "shear_modulus_Hill_GPa",
            "youngs_modulus_GPa",
            "poisson_ratio",
            "B_over_G",
            "cauchy_pressure_GPa",
            "debye_temperature_K",
            "Zener_anisotropy_AZ"
          ],
          "optional": [
            "cleavage_ratio_110",
            "solid_solution_hardening_misfit_epsilon_L",
            "solid_solution_hardening_factor",
            "fcc_bcc_SED_J_per_atom",
            "estimated_ideal_tensile_strength_001_GPa"
          ],
          "properties": {
            "Re": {
              "type": "number"
            },
            "Os": {
              "type": "number"
            },
            "shear_modulus_Hill_GPa": {
              "type": "number"
            },
            "youngs_modulus_GPa": {
              "type": "number"
            },
            "poisson_ratio": {
              "type": "number"
            },
            "B_over_G": {
              "type": "number"
            },
            "cauchy_pressure_GPa": {
              "type": "number"
            },
            "debye_temperature_K": {
              "type": "number"
            },
            "Zener_anisotropy_AZ": {
              "type": "number"
            },
            "cleavage_ratio_110": {
              "type": [
                "number",
                "null"
              ]
            },
            "solid_solution_hardening_misfit_epsilon_L": {
              "type": [
                "number",
                "null"
              ]
            },
            "solid_solution_hardening_factor": {
              "type": [
                "number",
                "null"
              ]
            },
            "fcc_bcc_SED_J_per_atom": {
              "type": [
                "number",
                "null"
              ]
            },
            "estimated_ideal_tensile_strength_001_GPa": {
              "type": [
                "number",
                "null"
              ]
            }
          }
        }
      },
      "description": "Polycrystalline moduli, ductility indicators, Debye temperature, elastic anisotropy, and optional cleavage ratio, solid-solution hardening parameters, and ideal tensile strength derived from the single-crystal elastic constants."
    }
  ],
  "notes": "The target is the paper-reported elastic constants, lattice parameter, bulk modulus, and derived polycrystalline properties. Internal consistency (C11+2C12)/3 = B and C' = (C11-C12)/2 is checked."
}
```

## How you are scored
A hidden verifier reads your submitted JSON files and compares each computed quantity (lattice constants, elastic constants, moduli, ductility parameters, etc.) against reference data, checks internal consistency (e.g., the relationship between C11, C12, and bulk modulus, and that C′ equals (C11−C12)/2), and verifies that the trends of certain quantities across compositions are physically plausible. The reward is a weighted average over all scored items; higher agreement and consistency yield higher rewards. Supplying numerically plausible values is necessary but not sufficient—the values must be internally self-consistent and must follow the expected monotonic behavior across the composition series.
