# GaN Phonon Pressure Coefficients via Buckingham Potential

## Problem background
Gallium nitride (GaN) is a wide‑bandgap semiconductor used in optoelectronics and high‑power electronics. Under ambient conditions GaN crystallises in the wurtzite structure; high‑pressure phases include rocksalt and NiAs, while zinc‑blende can be stabilised by epitaxy. Understanding the vibrational properties — phonon frequencies, their pressure dependence, and the associated Grüneisen parameters — is important for device performance and thermal management. This task asks you to simulate these properties from first principles using an empirical interatomic potential and lattice dynamics calculations.

## Approach
You will use the Buckingham pair potential for GaN as parametrised by Zapol et al. (1997), with a short‑range cut‑off of approximately 10 Å. All calculations are performed with the GULP code (General Utility Lattice Program), which handles total energy minimisation, elastic constant evaluation, phonon frequency computation, and pressure sweeps.

The workflow proceeds in five stages:
1. Set up the potential in GULP.
2. Find the equilibrium lattice parameters and total energies for the four GaN structures — wurtzite, zinc‑blende, rocksalt, and NiAs — by scanning volumes and locating the energy minimum. From these, estimate the transition pressures between the ambient and high‑pressure phases via enthalpy–pressure curves.
3. Compute structural parameters (a, c, internal parameter u) and the full tensorial elastic constants (Cij) together with the bulk modulus B for the rocksalt and NiAs phases at their equilibrium volumes.
4. Compute the Γ‑point optic phonon frequencies at zero pressure for all four structures.
5. Perform hydrostatic pressure sweeps up to the respective phase transition pressures, compute the phonon frequencies at each pressure, perform linear fits to extract the pressure coefficients dω/dP for every optic mode, and finally calculate the mode Grüneisen parameter γ = (B₀/ω₀)·(dω/dP) using the zero‑pressure frequency and the bulk modulus of each phase.

The results are written to three structured JSON files.

## Reproduction target
You must produce the following three files in `/app/outputs`:
1. **`step_01_structural_elastic.json`** — containing the equilibrium lattice parameters (a, c, u where applicable), bulk modulus B, and the independent elastic constants for the rocksalt and NiAs phases.
2. **`step_02_phonon_frequencies.json`** — containing the Γ‑point optic phonon frequencies at zero pressure for wurtzite (modes E₂(low), A₁(TO), E₁(TO), E₂(high), A₁(LO), E₁(LO)) and for zinc‑blende, rocksalt, and NiAs (TO and LO).
3. **`step_03_pressure_properties.json`** — containing the pressure coefficients dω/dP (cm⁻¹/GPa) and the mode Grüneisen parameters γ (dimensionless) for the same optic modes in all four phases, derived from your pressure‑dependent phonon calculations.

All values must be reported in the specified units and exactly follow the JSON structure shown in the workflow steps. No other files are required for scoring.

## Assets

- GULP (General Utility Lattice Program): https://gulp.curtin.edu.au/
- Buckingham potential parameters for GaN (Zapol et al. 1997): 10.1088/0953-8984/9/44/022

## Workflow steps

### Step 1: Potential model setup
- Role: process
- Action: Construct the Buckingham interatomic potential for GaN using the parameters from Zapol et al. (1997) and a short‑range cut‑off of approximately 10 Å. Create a GULP input library that can be used for all subsequent calculations.
- Evidence: `/app/outputs/potential_setup.log`

### Step 2: Energy minimisation and equilibrium structures
- Role: process
- Action: For each of the four GaN crystal structures (wurtzite, zinc‑blende, rocksalt, NiAs), perform total‑energy calculations at varying volumes using GULP with the Buckingham potential. Determine the equilibrium lattice parameters (a, c, u) for each phase. Also calculate enthalpy as a function of pressure and estimate the transition pressures from wurtzite to the high‑pressure phases.
- Evidence: `/app/outputs/equilibrium_structures.json`

### Step 3: Structural and elastic constants of high‑pressure phases
- Role: scored (load-bearing)
- Action: Using the equilibrium structures for rocksalt and NiAs, compute the equilibrium lattice parameters (a, c, u) and evaluate the full set of elastic constants (C11, C12, C13, C33, C44, C66) plus the bulk modulus B with GULP.
- Output file: `/app/outputs/step_01_structural_elastic.json`
- Format: json
- Contract: { rocksalt: { a (Å), B (GPa), C11, C12, C13, C44 (GPa) }; nias: { a (Å), c (Å), u (dimensionless), B (GPa), C11, C12, C13, C33, C44, C66 (GPa) } }
- Scoring: scored by hidden verifier

### Step 4: Phonon frequencies at ambient pressure
- Role: scored
- Action: For all four structures (wurtzite, zinc‑blende, rocksalt, NiAs), compute the Γ‑point optic phonon frequencies at zero pressure using GULP with the equilibrium structures from the energy minimisation.
- Output file: `/app/outputs/step_02_phonon_frequencies.json`
- Format: json
- Contract: { wurtzite: { E2_low, A1_TO, E1_TO, E2_high, A1_LO, E1_LO } (cm⁻¹); zinc_blende: { TO, LO } (cm⁻¹); rocksalt: { TO, LO } (cm⁻¹); nias: { TO, LO } (cm⁻¹) }
- Scoring: scored by hidden verifier

### Step 5: Pressure coefficients and Grüneisen parameters
- Role: scored (load-bearing)
- Action: Compute phonon frequencies for all four structures at several hydrostatic pressures from 0 GPa up to the respective phase transition pressure. For each optic mode, perform a linear fit to obtain the pressure coefficient dω/dP. Using the zero‑pressure frequency and the bulk modulus, calculate the mode Grüneisen parameter γ = (B₀/ω₀) (dω/dP).
- Output file: `/app/outputs/step_03_pressure_properties.json`
- Format: json
- Contract: { wurtzite: { gamma_E2_low, gamma_A1_TO, gamma_E1_TO, gamma_E2_high, gamma_A1_LO, gamma_E1_LO, domega_dP_E2_low, domega_dP_A1_TO, domega_dP_E1_TO, domega_dP_E2_high, domega_dP_A1_LO, domega_dP_E1_LO } (dimensionless, cm⁻¹/GPa); zinc_blende: { gamma_TO, gamma_LO, domega_dP_TO, domega_dP_LO }; rocksalt: same; nias: same }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_structural_elastic.json`
- `/app/outputs/step_02_phonon_frequencies.json`
- `/app/outputs/step_03_pressure_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_structural_elastic.json
- path: `/app/outputs/step_01_structural_elastic.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structural parameters and elastic constants for rocksalt and NiAs GaN.
- schema:
  - `type`: object
  - `required_keys`: `rocksalt`, `nias`
  - `properties`:
    - `rocksalt`:
      - `type`: object
      - `required_keys`: `a`, `B`, `C11`, `C12`, `C13`, `C44`
      - `units`:
        - `a`: Å
        - `B`: GPa
        - `C11`: GPa
        - `C12`: GPa
        - `C13`: GPa
        - `C44`: GPa
    - `nias`:
      - `type`: object
      - `required_keys`: `a`, `c`, `u`, `B`, `C11`, `C12`, `C13`, `C33`, `C44`, `C66`
      - `units`:
        - `a`: Å
        - `c`: Å
        - `u`: dimensionless
        - `B`: GPa
        - `C11`: GPa
        - `C12`: GPa
        - `C13`: GPa
        - `C33`: GPa
        - `C44`: GPa
        - `C66`: GPa

### step_02_phonon_frequencies.json
- path: `/app/outputs/step_02_phonon_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Zone‑centre phonon frequencies at ambient pressure.
- schema:
  - `type`: object
  - `required_keys`: `wurtzite`, `zinc_blende`, `rocksalt`, `nias`
  - `properties`:
    - `wurtzite`:
      - `type`: object
      - `required_keys`: `E2_low`, `A1_TO`, `E1_TO`, `E2_high`, `A1_LO`, `E1_LO`
      - `units`:
        - `E2_low`: cm⁻¹
        - `A1_TO`: cm⁻¹
        - `E1_TO`: cm⁻¹
        - `E2_high`: cm⁻¹
        - `A1_LO`: cm⁻¹
        - `E1_LO`: cm⁻¹
    - `zinc_blende`:
      - `type`: object
      - `required_keys`: `TO`, `LO`
      - `units`:
        - `TO`: cm⁻¹
        - `LO`: cm⁻¹
    - `rocksalt`:
      - `type`: object
      - `required_keys`: `TO`, `LO`
      - `units`:
        - `TO`: cm⁻¹
        - `LO`: cm⁻¹
    - `nias`:
      - `type`: object
      - `required_keys`: `TO`, `LO`
      - `units`:
        - `TO`: cm⁻¹
        - `LO`: cm⁻¹

### step_03_pressure_properties.json
- path: `/app/outputs/step_03_pressure_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Pressure coefficients and mode Grüneisen parameters for all four GaN phases.
- schema:
  - `type`: object
  - `required_keys`: `wurtzite`, `zinc_blende`, `rocksalt`, `nias`
  - `properties`:
    - `wurtzite`:
      - `type`: object
      - `required_keys`: `gamma_E2_low`, `gamma_A1_TO`, `gamma_E1_TO`, `gamma_E2_high`, `gamma_A1_LO`, `gamma_E1_LO`, `domega_dP_E2_low`, `domega_dP_A1_TO`, `domega_dP_E1_TO`, `domega_dP_E2_high`, `domega_dP_A1_LO`, `domega_dP_E1_LO`
      - `units`:
        - `gamma`: dimensionless
        - `domega_dP`: cm⁻¹/GPa
    - `zinc_blende`:
      - `type`: object
      - `required_keys`: `gamma_TO`, `gamma_LO`, `domega_dP_TO`, `domega_dP_LO`
      - `units`:
        - `gamma`: dimensionless
        - `domega_dP`: cm⁻¹/GPa
    - `rocksalt`:
      - `type`: object
      - `required_keys`: `gamma_TO`, `gamma_LO`, `domega_dP_TO`, `domega_dP_LO`
      - `units`:
        - `gamma`: dimensionless
        - `domega_dP`: cm⁻¹/GPa
    - `nias`:
      - `type`: object
      - `required_keys`: `gamma_TO`, `gamma_LO`, `domega_dP_TO`, `domega_dP_LO`
      - `units`:
        - `gamma`: dimensionless
        - `domega_dP`: cm⁻¹/GPa

Notes: All values are compared against the paper's reported data using hidden tolerances. The agent must run GULP with the Buckingham potential; no pre‑computed values are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_structural_elastic.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "rocksalt",
          "nias"
        ],
        "properties": {
          "rocksalt": {
            "type": "object",
            "required_keys": [
              "a",
              "B",
              "C11",
              "C12",
              "C13",
              "C44"
            ],
            "units": {
              "a": "Å",
              "B": "GPa",
              "C11": "GPa",
              "C12": "GPa",
              "C13": "GPa",
              "C44": "GPa"
            }
          },
          "nias": {
            "type": "object",
            "required_keys": [
              "a",
              "c",
              "u",
              "B",
              "C11",
              "C12",
              "C13",
              "C33",
              "C44",
              "C66"
            ],
            "units": {
              "a": "Å",
              "c": "Å",
              "u": "dimensionless",
              "B": "GPa",
              "C11": "GPa",
              "C12": "GPa",
              "C13": "GPa",
              "C33": "GPa",
              "C44": "GPa",
              "C66": "GPa"
            }
          }
        }
      },
      "description": "Structural parameters and elastic constants for rocksalt and NiAs GaN."
    },
    {
      "file": "step_02_phonon_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "wurtzite",
          "zinc_blende",
          "rocksalt",
          "nias"
        ],
        "properties": {
          "wurtzite": {
            "type": "object",
            "required_keys": [
              "E2_low",
              "A1_TO",
              "E1_TO",
              "E2_high",
              "A1_LO",
              "E1_LO"
            ],
            "units": {
              "E2_low": "cm⁻¹",
              "A1_TO": "cm⁻¹",
              "E1_TO": "cm⁻¹",
              "E2_high": "cm⁻¹",
              "A1_LO": "cm⁻¹",
              "E1_LO": "cm⁻¹"
            }
          },
          "zinc_blende": {
            "type": "object",
            "required_keys": [
              "TO",
              "LO"
            ],
            "units": {
              "TO": "cm⁻¹",
              "LO": "cm⁻¹"
            }
          },
          "rocksalt": {
            "type": "object",
            "required_keys": [
              "TO",
              "LO"
            ],
            "units": {
              "TO": "cm⁻¹",
              "LO": "cm⁻¹"
            }
          },
          "nias": {
            "type": "object",
            "required_keys": [
              "TO",
              "LO"
            ],
            "units": {
              "TO": "cm⁻¹",
              "LO": "cm⁻¹"
            }
          }
        }
      },
      "description": "Zone‑centre phonon frequencies at ambient pressure."
    },
    {
      "file": "step_03_pressure_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "wurtzite",
          "zinc_blende",
          "rocksalt",
          "nias"
        ],
        "properties": {
          "wurtzite": {
            "type": "object",
            "required_keys": [
              "gamma_E2_low",
              "gamma_A1_TO",
              "gamma_E1_TO",
              "gamma_E2_high",
              "gamma_A1_LO",
              "gamma_E1_LO",
              "domega_dP_E2_low",
              "domega_dP_A1_TO",
              "domega_dP_E1_TO",
              "domega_dP_E2_high",
              "domega_dP_A1_LO",
              "domega_dP_E1_LO"
            ],
            "units": {
              "gamma": "dimensionless",
              "domega_dP": "cm⁻¹/GPa"
            }
          },
          "zinc_blende": {
            "type": "object",
            "required_keys": [
              "gamma_TO",
              "gamma_LO",
              "domega_dP_TO",
              "domega_dP_LO"
            ],
            "units": {
              "gamma": "dimensionless",
              "domega_dP": "cm⁻¹/GPa"
            }
          },
          "rocksalt": {
            "type": "object",
            "required_keys": [
              "gamma_TO",
              "gamma_LO",
              "domega_dP_TO",
              "domega_dP_LO"
            ],
            "units": {
              "gamma": "dimensionless",
              "domega_dP": "cm⁻¹/GPa"
            }
          },
          "nias": {
            "type": "object",
            "required_keys": [
              "gamma_TO",
              "gamma_LO",
              "domega_dP_TO",
              "domega_dP_LO"
            ],
            "units": {
              "gamma": "dimensionless",
              "domega_dP": "cm⁻¹/GPa"
            }
          }
        }
      },
      "description": "Pressure coefficients and mode Grüneisen parameters for all four GaN phases."
    }
  ],
  "notes": "All values are compared against the paper's reported data using hidden tolerances. The agent must run GULP with the Buckingham potential; no pre‑computed values are provided."
}
```

## How you are scored
Your work is evaluated by a hidden automated verifier that reads the three JSON files. For every field in the structural‑elastic, phonon, and pressure‑property files, the verifier compares your calculated value against securely stored reference values derived from the published study. The comparison uses tolerances that account for the natural spread that arises when re‑running a simulation with a different code installation, operating system, or numerical settings. If your value lies within the allowed deviation, you earn full credit for that field; otherwise partial credit may be awarded based on the distance.

Additionally, the verifier may perform structural audits on the intermediate equilibrium energies to ensure that the correct phase stability ordering at zero pressure is reproduced.

Your final score (a float between 0 and 1) is a weighted sum of the scores from each file, with the main experimental claims receiving larger weight.
