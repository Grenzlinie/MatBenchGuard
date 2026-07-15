# First-principles prediction of structural, electronic, optical, elastic, and thermal properties of B2 CuZr intermetallic

## Problem background
The intermetallic compound CuZr, with the B2 (CsCl) crystal structure, is of interest for aerospace and nuclear applications because it is ductile, has low density, and a high melting point. A systematic first-principles account of its electronic, optical, elastic, and thermal properties is needed to understand its behaviour. Density functional theory (DFT) can predict structural stability, density of states, optical dielectric function, elastic constants, polycrystalline mechanical moduli, and Debye temperature. This task addresses whether a modern DFT calculation with a standard exchange-correlation functional can reliably provide these quantities and determine whether the material satisfies established ductility criteria (Pugh and Frantsevich rules).

## Approach
The approach uses density functional theory with the Perdew-Burke-Ernzerhof generalized gradient approximation (PBE-GGA) to treat exchange and correlation. Total energy as a function of unit cell volume is computed for three candidate crystal structures—B1 (NaCl), B2 (CsCl), and B3 (ZnS). The most stable phase is identified by fitting the energy-volume data to the Birch-Murnaghan equation of state; this yields the equilibrium lattice constant, bulk modulus, and its pressure derivative. Self-consistent field calculations for the stable B2 phase are then used to obtain the electronic density of states (DOS) at the Fermi level and, from momentum matrix elements followed by a Kramers-Kronig transformation, the zero-frequency limit of the real dielectric function (the static dielectric constant). The three independent second-order elastic constants for the cubic lattice are determined by applying finite distortions and computing stress. From the elastic constants and the density, polycrystalline shear, Young's, and Poisson's moduli are derived via Voigt-Reuss-Hill averaging, together with the Pugh ratio. Finally, sound velocities (longitudinal, transverse, average) and the Debye temperature are obtained from the elastic moduli and mass density.

## Reproduction target
Using a DFT code that implements PBE-GGA, compute and report the following properties of B2 CuZr:
- Stable phase and its equilibrium lattice constant a0 (Å), bulk modulus B (GPa), and pressure derivative B'.
- Density of states at the Fermi level N(EF) (states/eV per formula unit).
- Static dielectric constant ε₁(0).
- Single-crystal elastic constants C11, C12, C44 (all in GPa).
- Polycrystalline Hill shear modulus GH (GPa), Young's modulus E (GPa), Poisson's ratio σ, and Pugh ratio B/GH.
- Longitudinal, transverse, and average sound velocities (m/s), and Debye temperature θD (K).
Additionally, assess whether the computed Pugh ratio and Poisson ratio satisfy the ductility thresholds B/GH > 1.75 and σ > 1/3.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, Elk, or exciting) with PBE-GGA functional: https://www.quantum-espresso.org/download (or https://elk.sourceforge.io / https://exciting-code.org)
- PBE pseudopotentials for Cu and Zr: https://www.quantum-espresso.org/pseudopotentials (e.g., SSSP or GBRV libraries)

## Workflow steps

### Step 1: Ground-state structural properties and phase stability
- Role: scored
- Action: Perform DFT total energy calculations for B1 (NaCl), B2 (CsCl), and B3 (ZnS) crystal structures of CuZr over a range of unit cell volumes. Fit the energy-volume data to the Birch-Murnaghan equation of state to determine the most stable phase (B2). Obtain its equilibrium lattice constant a0, bulk modulus B, and pressure derivative B'.
- Output file: `/app/outputs/structural_output.json`
- Format: json
- Contract: {"a0": "float (Angstrom)", "B": "float (GPa)", "B_prime": "float (dimensionless)"}
- Scoring: scored by hidden verifier

### Step 2: Electronic density of states at the Fermi level
- Role: scored
- Action: Run a self-consistent DFT calculation for the equilibrium B2 CuZr structure. Compute the electronic density of states (DOS) and extract the value at the Fermi level N(EF) in states/eV per formula unit. Confirm the metallic character (no band gap).
- Output file: `/app/outputs/electronic_output.json`
- Format: json
- Contract: {"N_EF": "float (states/eV per f.u.)"}
- Scoring: scored by hidden verifier

### Step 3: Optical dielectric function and static dielectric constant
- Role: scored
- Action: Using the self-consistent electronic structure, compute the imaginary part of the dielectric function ε₂(ω) from momentum matrix elements, and obtain the real part ε₁(ω) via Kramers-Kronig transformation. Report the zero-frequency limit ε₁(0) (the static dielectric constant).
- Output file: `/app/outputs/optical_output.json`
- Format: json
- Contract: {"epsilon1_0": "float (dimensionless)"}
- Scoring: scored by hidden verifier

### Step 4: Single-crystal elastic constants
- Role: scored
- Action: Compute the three independent second-order elastic constants C11, C12, C44 for the cubic B2 CuZr structure using a finite-strain method with DFT. Verify that the elastic constants satisfy the mechanical stability criteria for a cubic crystal.
- Output file: `/app/outputs/elastic_output.json`
- Format: json
- Contract: {"C11": "float (GPa)", "C12": "float (GPa)", "C44": "float (GPa)"}
- Scoring: scored by hidden verifier

### Step 5: Polycrystalline mechanical moduli, ductility, sound velocities, and Debye temperature
- Role: scored (load-bearing)
- Action: From C11, C12, C44 and bulk modulus B, compute the Hill shear modulus GH via Voigt-Reuss-Hill averaging. Then derive Young's modulus E, Poisson's ratio σ, and the Pugh ratio B/GH. Verify that B/GH > 1.75 and σ > 1/3 (Pugh and Frantsevich ductility criteria). Using the elastic constants and the mass density, calculate longitudinal, transverse, and average sound velocities, and the Debye temperature θD.
- Output file: `/app/outputs/mechanical_thermal_output.json`
- Format: json
- Contract: {"GH": "float (GPa)", "E": "float (GPa)", "sigma": "float", "B_over_GH": "float", "v_l": "float (m/s)", "v_t": "float (m/s)", "v_avg": "float (m/s)", "theta_D": "float (K)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_output.json`
- `/app/outputs/electronic_output.json`
- `/app/outputs/optical_output.json`
- `/app/outputs/elastic_output.json`
- `/app/outputs/mechanical_thermal_output.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_output.json
- path: `/app/outputs/structural_output.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Equilibrium lattice constant, bulk modulus, and pressure derivative of B2 CuZr.
- schema:
  - `type`: object
  - `required`:
    - `a0`: float
    - `B`: float
    - `B_prime`: float
  - `units`:
    - `a0`: Angstrom
    - `B`: GPa
    - `B_prime`: dimensionless

### electronic_output.json
- path: `/app/outputs/electronic_output.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Density of states at the Fermi level.
- schema:
  - `type`: object
  - `required`:
    - `N_EF`: float
  - `units`:
    - `N_EF`: states/eV per formula unit

### optical_output.json
- path: `/app/outputs/optical_output.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Static dielectric constant ε₁(0).
- schema:
  - `type`: object
  - `required`:
    - `epsilon1_0`: float
  - `units`:
    - `epsilon1_0`: dimensionless

### elastic_output.json
- path: `/app/outputs/elastic_output.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Single-crystal elastic constants for cubic B2 CuZr.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float
    - `C12`: float
    - `C44`: float
  - `units`:
    - `C11`: GPa
    - `C12`: GPa
    - `C44`: GPa

### mechanical_thermal_output.json
- path: `/app/outputs/mechanical_thermal_output.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Hill shear modulus, Young's modulus, Poisson's ratio, Pugh ratio, sound velocities, and Debye temperature.
- schema:
  - `type`: object
  - `required`:
    - `GH`: float
    - `E`: float
    - `sigma`: float
    - `B_over_GH`: float
    - `v_l`: float
    - `v_t`: float
    - `v_avg`: float
    - `theta_D`: float
  - `units`:
    - `GH`: GPa
    - `E`: GPa
    - `sigma`: dimensionless
    - `B_over_GH`: dimensionless
    - `v_l`: m/s
    - `v_t`: m/s
    - `v_avg`: m/s
    - `theta_D`: K

Notes: All values are computed using DFT with PBE-GGA. The checker compares against paper-reported reference values with appropriate tolerances (tight for structural/elastic constants, wider for derived mechanical/thermal properties and DOS/dielectric constant). Ductility criteria (B/GH > 1.75 and σ > 1/3) are also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a0": "float",
          "B": "float",
          "B_prime": "float"
        },
        "units": {
          "a0": "Angstrom",
          "B": "GPa",
          "B_prime": "dimensionless"
        }
      },
      "description": "Equilibrium lattice constant, bulk modulus, and pressure derivative of B2 CuZr."
    },
    {
      "file": "electronic_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "N_EF": "float"
        },
        "units": {
          "N_EF": "states/eV per formula unit"
        }
      },
      "description": "Density of states at the Fermi level."
    },
    {
      "file": "optical_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon1_0": "float"
        },
        "units": {
          "epsilon1_0": "dimensionless"
        }
      },
      "description": "Static dielectric constant ε₁(0)."
    },
    {
      "file": "elastic_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float",
          "C12": "float",
          "C44": "float"
        },
        "units": {
          "C11": "GPa",
          "C12": "GPa",
          "C44": "GPa"
        }
      },
      "description": "Single-crystal elastic constants for cubic B2 CuZr."
    },
    {
      "file": "mechanical_thermal_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "GH": "float",
          "E": "float",
          "sigma": "float",
          "B_over_GH": "float",
          "v_l": "float",
          "v_t": "float",
          "v_avg": "float",
          "theta_D": "float"
        },
        "units": {
          "GH": "GPa",
          "E": "GPa",
          "sigma": "dimensionless",
          "B_over_GH": "dimensionless",
          "v_l": "m/s",
          "v_t": "m/s",
          "v_avg": "m/s",
          "theta_D": "K"
        }
      },
      "description": "Hill shear modulus, Young's modulus, Poisson's ratio, Pugh ratio, sound velocities, and Debye temperature."
    }
  ],
  "notes": "All values are computed using DFT with PBE-GGA. The checker compares against paper-reported reference values with appropriate tolerances (tight for structural/elastic constants, wider for derived mechanical/thermal properties and DOS/dielectric constant). Ductility criteria (B/GH > 1.75 and σ > 1/3) are also verified."
}
```

## How you are scored
A hidden verifier evaluates each of the five output JSON files separately. It first validates the JSON schema and then compares every required numeric field against a reference value obtained from the original study. The comparison uses a relative tolerance (tight for structural and elastic constants, wider for derived mechanical, thermal, electronic, and optical quantities). For each field, the credit is proportional to how close the computed value is to the reference: full credit when within tolerance, partial credit for moderate deviations, and zero for large deviations. The final score is a weighted sum over all scored artifacts, with the structural, elastic, and mechanical/thermal outputs receiving the largest share. Output files that are missing, malformed, or structurally wrong receive zero credit. Reporting a number without actually performing the computation will not suffice because the verifier expects values that are consistent with a bona fide DFT re-execution and mechanical post-processing.
