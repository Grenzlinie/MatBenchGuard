# DFT calculation of elastic and thermodynamic properties of Mg3Rh

## Problem background
Mg3Rh is a magnesium-based intermetallic compound of the Cu3P type. Its elastic and mechanical properties have not been studied experimentally or theoretically, so first-principles predictions can provide a basis for future experimental validation and alloy design. This work computes the single-crystal elastic constants, polycrystalline moduli, sound velocities, and Debye temperature of Mg3Rh using density functional theory.

## Approach
Use first-principles density functional theory (DFT) with the plane-wave pseudopotential method. Two exchange-correlation functionals are employed: LDA (Perdew–Zunger parameterization) and GGA-WC (Wu–Cohen functional). The computational engine should be an open-source plane-wave DFT code such as Quantum ESPRESSO. Starting from the experimental crystal structure, first optimize the unit cell parameters. Then compute the single-crystal elastic stiffness constants via the stress–strain method: apply finite homogeneous strains, extract the resulting stresses using Hooke’s law, and obtain C11, C12, C13, C33, C44, and C66. From these constants, calculate isotropic polycrystalline moduli—bulk modulus (B), shear modulus (G), Young’s modulus (E), Poisson’s ratio (σ), Zener anisotropy factor (A), B/G ratio, and hardness parameter (H)—using Voigt–Reuss–Hill averaging. Finally, use the Hill-averaged moduli and the optimized cell volume to compute the mass density, longitudinal (v_l), transverse (v_t), and average (v_m) sound velocities, and the Debye temperature (Θ_D). All quantities are determined for both LDA and GGA-WC functionals.

## Reproduction target
For the intermetallic compound Mg3Rh (space group P6₃cm, Cu3P structure), perform the following computational protocol using an open-source plane-wave DFT code: (1) compute the single-crystal elastic constants C11, C12, C13, C33, C44, C66 (in GPa) for both LDA and GGA-WC functionals; (2) derive the polycrystalline elastic moduli (B, G, E, σ, anisotropy factor A, B/G ratio, and hardness parameter H) via Voigt–Reuss–Hill averaging; (3) calculate the mass density, longitudinal, transverse, and average sound velocities, and Debye temperature. The objective is to obtain internally consistent predictions for these properties by re-running the described first-principles workflow.

## Assets

- Quantum ESPRESSO (open-source DFT code): https://www.quantum-espresso.org/download
- SSSP pseudopotential library: https://www.materialscloud.org/discover/sssp/table/precision
- Mg3Rh experimental crystal structure

## Workflow steps

### Step 1: DFT structural optimization of Mg3Rh
- Role: process
- Action: Perform DFT geometry optimization for the Mg3Rh unit cell (Cu3P type, space group P6₃cm) starting from experimental lattice parameters a=7.905 Å, c=8.256 Å, using both LDA and GGA-WC functionals. Record the optimized cell parameters and volume.
- Evidence: `/app/outputs/optimized_cell_info.json`

### Step 2: Single-crystal elastic constants Cij
- Role: scored (load-bearing)
- Action: Using the relaxed structures from Step 1, compute the elastic stiffness constants C11, C12, C13, C33, C44, C66 by applying finite homogeneous strains and extracting the resulting stresses (Hooke's law). Use the same functional, cutoff, and k-point mesh as in Step 1. Output the elastic constants in GPa for both LDA and GGA-WC.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"LDA": {"C11": "number", "C12": "number", "C13": "number", "C33": "number", "C44": "number", "C66": "number"}, "GGA-WC": {"C11": "number", "C12": "number", "C13": "number", "C33": "number", "C44": "number", "C66": "number"}}
- Scoring: scored by hidden verifier

### Step 3: Polycrystalline elastic moduli and mechanical properties
- Role: scored
- Action: From the elastic constants in elastic_constants.json, compute the Voigt and Reuss bounds for bulk and shear moduli of a hexagonal crystal, then Hill averages B and G. Derive Young's modulus E, Poisson's ratio σ, Zener anisotropy factor A, B/G ratio, and hardness parameter H using standard formulas. Produce all quantities for both LDA and GGA-WC.
- Output file: `/app/outputs/polycrystalline_properties.json`
- Format: json
- Contract: {"LDA": {"B": "number", "G": "number", "E": "number", "sigma": "number", "A": "number", "B_over_G": "number", "H": "number"}, "GGA-WC": {"B": "number", "G": "number", "E": "number", "sigma": "number", "A": "number", "B_over_G": "number", "H": "number"}}
- Scoring: scored by hidden verifier

### Step 4: Sound velocities and Debye temperature
- Role: scored
- Action: Using the Hill-averaged bulk modulus B and shear modulus G from Step 3, and the optimized cell volume from Step 1 (to compute mass density ρ and atomic volume V_a), calculate longitudinal sound velocity v_l, transverse sound velocity v_t, average sound velocity v_m, and Debye temperature θ_D via standard formulas. Report all values for both LDA and GGA-WC.
- Output file: `/app/outputs/thermodynamic_properties.json`
- Format: json
- Contract: {"LDA": {"rho": "number", "v_l": "number", "v_t": "number", "v_m": "number", "Theta_D": "number"}, "GGA-WC": {"rho": "number", "v_l": "number", "v_t": "number", "v_m": "number", "Theta_D": "number"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/polycrystalline_properties.json`
- `/app/outputs/thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single-crystal elastic stiffness constants computed from DFT stress-strain calculations.
- schema:
  - `type`: object
  - `required`:
    - `LDA`:
      - `C11`: number (GPa)
      - `C12`: number (GPa)
      - `C13`: number (GPa)
      - `C33`: number (GPa)
      - `C44`: number (GPa)
      - `C66`: number (GPa)
    - `GGA-WC`:
      - `C11`: number (GPa)
      - `C12`: number (GPa)
      - `C13`: number (GPa)
      - `C33`: number (GPa)
      - `C44`: number (GPa)
      - `C66`: number (GPa)

### polycrystalline_properties.json
- path: `/app/outputs/polycrystalline_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Polycrystalline elastic moduli and mechanical parameters derived from single-crystal elastic constants via Voigt–Reuss–Hill averaging.
- schema:
  - `type`: object
  - `required`:
    - `LDA`:
      - `B`: number (GPa)
      - `G`: number (GPa)
      - `E`: number (GPa)
      - `sigma`: number (dimensionless)
      - `A`: number (dimensionless)
      - `B_over_G`: number (dimensionless)
      - `H`: number (GPa)
    - `GGA-WC`:
      - `B`: number (GPa)
      - `G`: number (GPa)
      - `E`: number (GPa)
      - `sigma`: number (dimensionless)
      - `A`: number (dimensionless)
      - `B_over_G`: number (dimensionless)
      - `H`: number (GPa)

### thermodynamic_properties.json
- path: `/app/outputs/thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Density, sound velocities, and Debye temperature computed from elastic moduli and cell volume.
- schema:
  - `type`: object
  - `required`:
    - `LDA`:
      - `rho`: number (g/cm³)
      - `v_l`: number (m/s)
      - `v_t`: number (m/s)
      - `v_m`: number (m/s)
      - `Theta_D`: number (K)
    - `GGA-WC`:
      - `rho`: number (g/cm³)
      - `v_l`: number (m/s)
      - `v_t`: number (m/s)
      - `v_m`: number (m/s)
      - `Theta_D`: number (K)

Notes: All three artifacts are compared against the paper-reported values with appropriate tolerances. Internal consistency (the relationships between elastic constants, polycrystalline moduli, density, and sound velocities) is also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA": {
            "C11": "number (GPa)",
            "C12": "number (GPa)",
            "C13": "number (GPa)",
            "C33": "number (GPa)",
            "C44": "number (GPa)",
            "C66": "number (GPa)"
          },
          "GGA-WC": {
            "C11": "number (GPa)",
            "C12": "number (GPa)",
            "C13": "number (GPa)",
            "C33": "number (GPa)",
            "C44": "number (GPa)",
            "C66": "number (GPa)"
          }
        }
      },
      "description": "Single-crystal elastic stiffness constants computed from DFT stress-strain calculations."
    },
    {
      "file": "polycrystalline_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA": {
            "B": "number (GPa)",
            "G": "number (GPa)",
            "E": "number (GPa)",
            "sigma": "number (dimensionless)",
            "A": "number (dimensionless)",
            "B_over_G": "number (dimensionless)",
            "H": "number (GPa)"
          },
          "GGA-WC": {
            "B": "number (GPa)",
            "G": "number (GPa)",
            "E": "number (GPa)",
            "sigma": "number (dimensionless)",
            "A": "number (dimensionless)",
            "B_over_G": "number (dimensionless)",
            "H": "number (GPa)"
          }
        }
      },
      "description": "Polycrystalline elastic moduli and mechanical parameters derived from single-crystal elastic constants via Voigt–Reuss–Hill averaging."
    },
    {
      "file": "thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "LDA": {
            "rho": "number (g/cm³)",
            "v_l": "number (m/s)",
            "v_t": "number (m/s)",
            "v_m": "number (m/s)",
            "Theta_D": "number (K)"
          },
          "GGA-WC": {
            "rho": "number (g/cm³)",
            "v_l": "number (m/s)",
            "v_t": "number (m/s)",
            "v_m": "number (m/s)",
            "Theta_D": "number (K)"
          }
        }
      },
      "description": "Density, sound velocities, and Debye temperature computed from elastic moduli and cell volume."
    }
  ],
  "notes": "All three artifacts are compared against the paper-reported values with appropriate tolerances. Internal consistency (the relationships between elastic constants, polycrystalline moduli, density, and sound velocities) is also verified."
}
```

## How you are scored
A hidden verifier checks each scored workflow stage’s output file independently against a hidden reference. The verifier compares the submitted elastic constants, polycrystalline quantities, and thermodynamic properties to expected values, and also verifies internal consistency (e.g., the relationships among elastic constants, polycrystalline moduli, density, and sound velocities). Each stage contributes to the final reward (0.0–1.0) according to a weighted rubric. Simply reporting numbers is not sufficient; your artifacts must be the result of executing the computational steps described in the workflow.
