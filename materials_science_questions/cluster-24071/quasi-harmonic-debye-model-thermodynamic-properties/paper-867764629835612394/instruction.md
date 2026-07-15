# DFT-based thermophysical and superconducting properties of orthorhombic MgVH6 under pressure (100–200 GPa)

## Problem background
Metal hydrides under high pressure are promising candidates for high-temperature superconductivity. In particular, Mg-based ternary hydrides can stabilize hydrogen-rich structures where strong electron–phonon coupling leads to elevated superconducting transition temperatures. This task investigates the orthorhombic (space group Pmn2_1) phase of the ternary hydride MgVH6 under hydrostatic pressures in the range 100–200 GPa. Understanding how pressure modifies the structural, elastic, thermophysical, and superconducting properties of this compound is the central challenge. The quantitative goal is to compute key physical quantities—including the superconducting transition temperature—and to capture their systematic pressure dependence.

## Approach
The reproduction uses first-principles density functional theory (DFT) with the generalized gradient approximation (GGA-PBE) for exchange-correlation. The workflow consists of three core DFT stages followed by a post-processing stage. First, variable-cell geometry optimization of the orthorhombic unit cell is performed at each target pressure to obtain relaxed lattice parameters. Second, the nine independent single-crystal elastic constants are computed from the optimized structures via the stress–strain or energy–strain approach. Third, a self-consistent field calculation and density-of-states (DOS) calculation are carried out to extract the electronic density of states at the Fermi level. Finally, all derived quantities are obtained by post-processing: polycrystalline elastic moduli and sound velocities are computed via Voigt–Reuss–Hill averaging; the Debye temperature is evaluated with the Anderson method; the Grüneisen parameter is obtained from Poisson’s ratio; melting temperature, thermal expansion coefficient, minimum thermal conductivity, and hardness (using several established models) are derived from the elastic constants; the Coulomb pseudopotential is estimated from the Fermi-level DOS; the electron–phonon coupling constant is scaled from a reference value at 150 GPa; and the superconducting transition temperature is predicted with the McMillan formula. The entire pipeline is implemented using an open-source DFT code (e.g., Quantum ESPRESSO) and standard Python post-processing libraries.

## Reproduction target
For the orthorhombic Pmn2_1 phase of MgVH6 at five pressures (100, 125, 150, 175, and 200 GPa), compute the following quantities and assemble them into a single structured JSON file named `reproduced_properties.json`. For each pressure include: lattice parameters (a, b, c in Å); the nine independent elastic constants C11, C22, C33, C44, C55, C66, C12, C13, C23 (in GPa); polycrystalline moduli (bulk modulus B, shear modulus G, Young’s modulus Y, Poisson’s ratio ν, and Pugh’s ratio G/B); sound velocities (transverse vt, longitudinal vl, average vm in km/s); Debye temperature (K); Grüneisen parameter; melting temperature (K); thermal expansion coefficient (10⁻⁵ K⁻¹); minimum thermal conductivity (W·m⁻¹·K⁻¹); hardness values according to the Teter, Tian, Chen, and micro-hardness models (GPa); electronic density of states at the Fermi level N(EF) (states/eV); Coulomb pseudopotential μ*; electron–phonon coupling constant λ; and the superconducting transition temperature Tc (K). The output JSON must follow the schema described in the output contract. These results constitute the complete reproduction target.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials (SSSP library): https://www.materialscloud.org/discover/sssp/table/efficiency
- Python scientific packages (numpy, scipy, json): numpy, scipy, json
- Crystal structure of orthorhombic MgVH6 (Pmn2_1): 10.1021/acs.jpcc.0c10475

## Workflow steps

### Step 1: DFT geometry optimization
- Role: process
- Action: Perform variable-cell geometry optimization of orthorhombic MgVH6 (Pmn2_1) at each target pressure (100, 125, 150, 175, 200 GPa) using an open-source DFT code with GGA-PBE functional and appropriate pseudopotentials. Extract optimized lattice parameters and total energy.
- Evidence: `/app/outputs/geometry_convergence.log`

### Step 2: DFT elastic constants calculation
- Role: process
- Action: Using the optimized structures from step 1, compute the nine independent single-crystal elastic constants C11, C22, C33, C44, C55, C66, C12, C13, C23 for each pressure via a stress-strain or energy-strain method implemented in the DFT code.
- Evidence: `/app/outputs/elastic_constants.csv`

### Step 3: DFT electronic density of states
- Role: process
- Action: Perform a self-consistent field calculation and density-of-states (DOS) calculation for each pressure using the optimized structures. Extract the electronic density of states at the Fermi level, N(EF), in states/eV per formula unit.
- Evidence: `/app/outputs/dos_data.csv`

### Step 4: Post-process and compute all derived properties
- Role: scored (load-bearing)
- Action: From the lattice parameters, elastic constants, and N(EF) obtained in the previous steps, compute the following quantities for each pressure using standard formulas: polycrystalline moduli (B, G, Y, ν, G/B) via Voigt-Reuss-Hill averaging; sound velocities (vt, vl, vm); Debye temperature θD (Anderson method); Grüneisen parameter γ from Poisson's ratio; minimum thermal conductivity κmin; melting temperature Tm (from C11 and C33); thermal expansion coefficient α (from G); hardness H_Teter, H_Tian, H_Chen, H_micro; Coulomb pseudopotential μ* = 0.26 N(EF)/(1+N(EF)); electron–phonon coupling constant λ scaled from a reference λ=1.43 at 150 GPa; and Tc from the McMillan formula. Write all results to reproduced_properties.json.
- Output file: `/app/outputs/reproduced_properties.json`
- Format: json
- Contract: {"100_GPa": {"lattice_a": float, "lattice_b": float, "lattice_c": float, "elastic_constants": {"C11": float, "C22": float, "C33": float, "C44": float, "C55": float, "C66": float, "C12": float, "C13": float, "C23": float}, "bulk_modulus_B": float, "shear_modulus_G": float, "Youngs_modulus_Y": float, "Poisson_ratio_v": float, "Pugh_ratio_GB": float, "sound_velocity_t": float, "sound_velocity_l": float, "sound_velocity_m": float, "debye_temperature": float, "gruneisen_parameter": float, "melting_temperature": float, "thermal_expansion_coefficient": float, "min_thermal_conductivity": float, "hardness_Teter": float, "hardness_Tian": float, "hardness_Chen": float, "hardness_micro": float, "N_EF": float, "mu_star": float, "lambda": float, "T_c": float}, "125_GPa": {...}, ...}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduced_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduced_properties.json
- path: `/app/outputs/reproduced_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The single scored artifact that aggregates all reproduced physical properties for the orthorhombic phase at the five target pressures. The hidden checker will compare the provided values to reference data using appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `100_GPa`, `125_GPa`, `150_GPa`, `175_GPa`, `200_GPa`
  - `properties`:
    - `100_GPa`:
      - `type`: object
      - `required`: `lattice_a`, `lattice_b`, `lattice_c`, `elastic_constants`, `bulk_modulus_B`, `shear_modulus_G`, `Youngs_modulus_Y`, `Poisson_ratio_v`, `Pugh_ratio_GB`, `sound_velocity_t`, `sound_velocity_l`, `sound_velocity_m`, `debye_temperature`, `gruneisen_parameter`, `melting_temperature`, `thermal_expansion_coefficient`, `min_thermal_conductivity`, `hardness_Teter`, `hardness_Tian`, `hardness_Chen`, `hardness_micro`, `N_EF`, `mu_star`, `lambda`, `T_c`
      - `properties`:
        - `elastic_constants`:
          - `type`: object
          - `required`: `C11`, `C22`, `C33`, `C44`, `C55`, `C66`, `C12`, `C13`, `C23`
  - `description`: Top-level keys are the pressures. Each pressure value is an object containing lattice parameters (Å), elastic constants (GPa), polycrystalline moduli (GPa), ratios, sound velocities (km/s), Debye temperature (K), Grüneisen parameter, melting temperature (K), thermal expansion coefficient (1e-5/K), minimum thermal conductivity (W/m·K), hardness values (GPa), N(EF) (states/eV), μ*, λ, and Tc (K).

Notes: Only the orthorhombic Pmn2_1 phase is scored. The optical properties stage and monoclinic phase are omitted because they are not part of the primary superconducting/thermal claims.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduced_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "100_GPa",
          "125_GPa",
          "150_GPa",
          "175_GPa",
          "200_GPa"
        ],
        "properties": {
          "100_GPa": {
            "type": "object",
            "required": [
              "lattice_a",
              "lattice_b",
              "lattice_c",
              "elastic_constants",
              "bulk_modulus_B",
              "shear_modulus_G",
              "Youngs_modulus_Y",
              "Poisson_ratio_v",
              "Pugh_ratio_GB",
              "sound_velocity_t",
              "sound_velocity_l",
              "sound_velocity_m",
              "debye_temperature",
              "gruneisen_parameter",
              "melting_temperature",
              "thermal_expansion_coefficient",
              "min_thermal_conductivity",
              "hardness_Teter",
              "hardness_Tian",
              "hardness_Chen",
              "hardness_micro",
              "N_EF",
              "mu_star",
              "lambda",
              "T_c"
            ],
            "properties": {
              "elastic_constants": {
                "type": "object",
                "required": [
                  "C11",
                  "C22",
                  "C33",
                  "C44",
                  "C55",
                  "C66",
                  "C12",
                  "C13",
                  "C23"
                ]
              }
            }
          }
        },
        "description": "Top-level keys are the pressures. Each pressure value is an object containing lattice parameters (Å), elastic constants (GPa), polycrystalline moduli (GPa), ratios, sound velocities (km/s), Debye temperature (K), Grüneisen parameter, melting temperature (K), thermal expansion coefficient (1e-5/K), minimum thermal conductivity (W/m·K), hardness values (GPa), N(EF) (states/eV), μ*, λ, and Tc (K)."
      },
      "description": "The single scored artifact that aggregates all reproduced physical properties for the orthorhombic phase at the five target pressures. The hidden checker will compare the provided values to reference data using appropriate tolerances."
    }
  ],
  "notes": "Only the orthorhombic Pmn2_1 phase is scored. The optical properties stage and monoclinic phase are omitted because they are not part of the primary superconducting/thermal claims."
}
```

## How you are scored
A hidden verifier evaluates the contents of your `reproduced_properties.json`. Each reported value is compared against a hidden reference with pressure-dependent tolerances that absorb legitimate differences arising from the choice of DFT code, pseudopotentials, and numerical settings. In addition to point-by-point comparisons, the verifier checks that physically expected trends are correctly reproduced—for example, the monotonic variation of certain quantities with pressure. Failure to produce a result within the acceptable range for a given property reduces the score for that component. The final reward (a float between 0 and 1) is a weighted sum over all scored quantities, with the superconducting transition temperature and its trends carrying the largest share. Reporting the correct numbers is necessary but not sufficient; they must emerge from a faithful execution of the workflow described in the steps (the verifier does not inspect intermediate process evidence but scores only the final JSON).
