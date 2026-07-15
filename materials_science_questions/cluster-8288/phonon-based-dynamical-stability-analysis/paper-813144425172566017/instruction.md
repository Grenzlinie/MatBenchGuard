# DFT study of elastic constants, phonon stability, and anisotropy of MSiP2 chalcopyrites (M=Be, Mg, Cd, Zn, Hg)

## Problem background
Ternary pnictide chalcopyrite MSiP2 (M=Be, Mg, Cd, Zn, Hg) compounds are candidate materials for photovoltaic and nonlinear optical applications. Accurate first-principles prediction of their structural stability, elastic behavior, dynamical stability, elastic anisotropy, and pressure-induced phase transitions under static conditions is essential for understanding their mechanical and thermodynamic properties.

## Approach
This reproduction relies on open-source density functional theory (DFT) with plane-wave basis sets and projector augmented wave (PAW) pseudopotentials within the PBE functional. The workflow consists of: (1) full geometry relaxation of the tetragonal I-42d chalcopyrite phase for each compound; (2) elastic constant calculation by applying small finite strains and fitting the resulting stress tensor to obtain the stiffness matrix; (3) phonon dispersion calculation using density functional perturbation theory (DFPT) with a supercell to check for imaginary modes (dynamical stability); (4) Voigt–Reuss–Hill averaging to derive polycrystalline bulk, shear, Young's moduli and Poisson's ratio; (5) construction of the elastic compliance tensor and computation of directional Young's modulus and linear compressibility surfaces to extract global extrema; (6) total energy vs. volume scans for the chalcopyrite, orthorhombic Pna21, and cubic Fm-3m phases, followed by enthalpy–pressure intersection to locate the static phase transition pressures. The computational pipeline uses Quantum ESPRESSO for DFT, PHONOPY for phonon processing, and standard Python libraries for post-processing.

## Reproduction target
Execute the sequential workflow defined in the steps below to generate five scored output files: elastic constants, phonon stability verdict and minimum squared frequency, polycrystalline moduli by VRH averaging, elastic anisotropy extremes (min/max Young's modulus and linear compressibility), and static phase transition pressures (I-42d → Pna21 and I-42d → Fm-3m). All five compounds (BeSiP2, MgSiP2, CdSiP2, ZnSiP2, HgSiP2) must be included in each output artifact. Write the files to /app/outputs exactly as specified.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- SSSP pseudopotentials (PAW, PBE): https://www.materialscloud.org/discover/sssp/table/precision
- Python scientific stack: numpy scipy pandas

## Workflow steps

### Step 1: Geometry optimization of chalcopyrite structures
- Role: process
- Action: Perform DFT geometry relaxation for the tetragonal I-42d chalcopyrite phase of BeSiP₂, MgSiP₂, CdSiP₂, ZnSiP₂, and HgSiP₂ to obtain equilibrium lattice parameters and atomic positions.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 2: Single-crystal elastic constants
- Role: scored
- Action: Calculate the elastic stiffness tensor C_ij for the chalcopyrite phase of each compound by applying small finite strains to the relaxed structure, computing stress, and fitting Hooke's law.
- Output file: `/app/outputs/step_01_elastic_constants.json`
- Format: json
- Contract: Array of objects: {compound: string, C11: number, C12: number, C13: number, C33: number, C44: number, C66: number}
- Scoring: scored by hidden verifier

### Step 3: Phonon dynamical stability
- Role: scored
- Action: Compute phonon dispersion for the relaxed chalcopyrite phase using DFPT with a supercell via PHONOPY. Assess dynamical stability by checking for imaginary modes (negative squared frequency).
- Output file: `/app/outputs/step_02_phonon_stability.json`
- Format: json
- Contract: Object: {stable: boolean, min_squared_frequency: number} (unit THz²)
- Scoring: scored by hidden verifier

### Step 4: Polycrystalline moduli (VRH averages)
- Role: scored
- Action: From the single-crystal elastic constants, compute polycrystalline bulk modulus B_VRH, shear modulus G_VRH, Young's modulus Y_VRH, and Poisson's ratio ν_VRH using Voigt–Reuss–Hill averaging.
- Output file: `/app/outputs/step_03_polycrystalline_moduli.json`
- Format: json
- Contract: Array of objects: {compound: string, B_VRH: number, G_VRH: number, Y_VRH: number, Poisson_VRH: number}
- Scoring: scored by hidden verifier

### Step 5: Elastic anisotropy extremes
- Role: scored
- Action: Calculate the elastic compliance tensor S, then compute directional Young's modulus and linear compressibility as functions of direction (θ,φ) and extract the minimum and maximum values for each compound.
- Output file: `/app/outputs/step_05_anisotropy_summary.json`
- Format: json
- Contract: Array of objects: {compound: string, Y_min: number, Y_max: number, beta_min: number, beta_max: number}
- Scoring: scored by hidden verifier

### Step 6: Total energy vs volume curves for all phases
- Role: process
- Action: Perform a series of DFT total energy calculations at multiple fixed volumes for the chalcopyrite (I-42d), orthorhombic (Pna2₁), and cubic (Fm-3m) phases of each compound, relaxing internal coordinates at each volume. Obtain E(V) data for subsequent phase transition analysis.
- Evidence: `/app/outputs/ev_data.json`

### Step 7: Phase transition pressures
- Role: scored (load-bearing)
- Action: From the E(V) data, compute enthalpies H = E + pV and determine the crossing pressures for the I-42d → Pna2₁ and I-42d → Fm-3m transitions for each compound.
- Output file: `/app/outputs/step_04_transition_pressures.json`
- Format: json
- Contract: Array of objects: {compound: string, Pt_I42d_Pna21: number, Pt_I42d_Fm3m: number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_elastic_constants.json`
- `/app/outputs/step_02_phonon_stability.json`
- `/app/outputs/step_03_polycrystalline_moduli.json`
- `/app/outputs/step_04_transition_pressures.json`
- `/app/outputs/step_05_anisotropy_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_elastic_constants.json
- path: `/app/outputs/step_01_elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Single-crystal elastic stiffness constants (Voigt notation) for the chalcopyrite phase of each compound.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `compound`:
        - `type`: string
      - `C11`:
        - `type`: number
        - `unit`: GPa
      - `C12`:
        - `type`: number
        - `unit`: GPa
      - `C13`:
        - `type`: number
        - `unit`: GPa
      - `C33`:
        - `type`: number
        - `unit`: GPa
      - `C44`:
        - `type`: number
        - `unit`: GPa
      - `C66`:
        - `type`: number
        - `unit`: GPa
    - `required`: `compound`, `C11`, `C12`, `C13`, `C33`, `C44`, `C66`

### step_02_phonon_stability.json
- path: `/app/outputs/step_02_phonon_stability.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Phonon dynamical stability assessment for the chalcopyrite phase: stability verdict and minimum squared frequency (must be non-negative for stability).
- schema:
  - `type`: object
  - `properties`:
    - `stable`:
      - `type`: boolean
    - `min_squared_frequency`:
      - `type`: number
      - `unit`: THz²
  - `required`: `stable`, `min_squared_frequency`

### step_03_polycrystalline_moduli.json
- path: `/app/outputs/step_03_polycrystalline_moduli.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Voigt–Reuss–Hill polycrystalline averages of bulk, shear, Young's moduli and Poisson's ratio for each compound.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `compound`:
        - `type`: string
      - `B_VRH`:
        - `type`: number
        - `unit`: GPa
      - `G_VRH`:
        - `type`: number
        - `unit`: GPa
      - `Y_VRH`:
        - `type`: number
        - `unit`: GPa
      - `Poisson_VRH`:
        - `type`: number
        - `unit`: dimensionless
    - `required`: `compound`, `B_VRH`, `G_VRH`, `Y_VRH`, `Poisson_VRH`

### step_04_transition_pressures.json
- path: `/app/outputs/step_04_transition_pressures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Pressure-induced phase transition pressures from chalcopyrite (I-42d) to orthorhombic (Pna2_1) and to cubic (Fm-3m) for each compound, determined from enthalpy–pressure crossing.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `compound`:
        - `type`: string
      - `Pt_I42d_Pna21`:
        - `type`: number
        - `unit`: GPa
      - `Pt_I42d_Fm3m`:
        - `type`: number
        - `unit`: GPa
    - `required`: `compound`, `Pt_I42d_Pna21`, `Pt_I42d_Fm3m`

### step_05_anisotropy_summary.json
- path: `/app/outputs/step_05_anisotropy_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Directional elastic anisotropy extremes: minimum and maximum Young's modulus and linear compressibility for the chalcopyrite phase of each compound.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `compound`:
        - `type`: string
      - `Y_min`:
        - `type`: number
        - `unit`: GPa
      - `Y_max`:
        - `type`: number
        - `unit`: GPa
      - `beta_min`:
        - `type`: number
        - `unit`: TPa⁻¹
      - `beta_max`:
        - `type`: number
        - `unit`: TPa⁻¹
    - `required`: `compound`, `Y_min`, `Y_max`, `beta_min`, `beta_max`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "compound": {
              "type": "string"
            },
            "C11": {
              "type": "number",
              "unit": "GPa"
            },
            "C12": {
              "type": "number",
              "unit": "GPa"
            },
            "C13": {
              "type": "number",
              "unit": "GPa"
            },
            "C33": {
              "type": "number",
              "unit": "GPa"
            },
            "C44": {
              "type": "number",
              "unit": "GPa"
            },
            "C66": {
              "type": "number",
              "unit": "GPa"
            }
          },
          "required": [
            "compound",
            "C11",
            "C12",
            "C13",
            "C33",
            "C44",
            "C66"
          ]
        }
      },
      "description": "Single-crystal elastic stiffness constants (Voigt notation) for the chalcopyrite phase of each compound."
    },
    {
      "file": "step_02_phonon_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "stable": {
            "type": "boolean"
          },
          "min_squared_frequency": {
            "type": "number",
            "unit": "THz²"
          }
        },
        "required": [
          "stable",
          "min_squared_frequency"
        ]
      },
      "description": "Phonon dynamical stability assessment for the chalcopyrite phase: stability verdict and minimum squared frequency (must be non-negative for stability)."
    },
    {
      "file": "step_03_polycrystalline_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "compound": {
              "type": "string"
            },
            "B_VRH": {
              "type": "number",
              "unit": "GPa"
            },
            "G_VRH": {
              "type": "number",
              "unit": "GPa"
            },
            "Y_VRH": {
              "type": "number",
              "unit": "GPa"
            },
            "Poisson_VRH": {
              "type": "number",
              "unit": "dimensionless"
            }
          },
          "required": [
            "compound",
            "B_VRH",
            "G_VRH",
            "Y_VRH",
            "Poisson_VRH"
          ]
        }
      },
      "description": "Voigt–Reuss–Hill polycrystalline averages of bulk, shear, Young's moduli and Poisson's ratio for each compound."
    },
    {
      "file": "step_04_transition_pressures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "compound": {
              "type": "string"
            },
            "Pt_I42d_Pna21": {
              "type": "number",
              "unit": "GPa"
            },
            "Pt_I42d_Fm3m": {
              "type": "number",
              "unit": "GPa"
            }
          },
          "required": [
            "compound",
            "Pt_I42d_Pna21",
            "Pt_I42d_Fm3m"
          ]
        }
      },
      "description": "Pressure-induced phase transition pressures from chalcopyrite (I-42d) to orthorhombic (Pna2_1) and to cubic (Fm-3m) for each compound, determined from enthalpy–pressure crossing."
    },
    {
      "file": "step_05_anisotropy_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "compound": {
              "type": "string"
            },
            "Y_min": {
              "type": "number",
              "unit": "GPa"
            },
            "Y_max": {
              "type": "number",
              "unit": "GPa"
            },
            "beta_min": {
              "type": "number",
              "unit": "TPa⁻¹"
            },
            "beta_max": {
              "type": "number",
              "unit": "TPa⁻¹"
            }
          },
          "required": [
            "compound",
            "Y_min",
            "Y_max",
            "beta_min",
            "beta_max"
          ]
        }
      },
      "description": "Directional elastic anisotropy extremes: minimum and maximum Young's modulus and linear compressibility for the chalcopyrite phase of each compound."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier examines each scored output file independently. For each quantity, the verifier compares your submitted value against a reference (the paper-reported result) using appropriate tolerances and (for directional metrics) a threshold-or-better policy: meeting or exceeding the expected benchmark earns full credit, and the score diminishes only as the result gets worse. The verifier also checks that structures and key fields are present and correctly formatted. The per-stage scores are combined with weights to form the final reward in [0,1]. Note that reporting numbers that match the reference is not sufficient; the verifier expects each value to be derived from the computational pipeline, and staged outputs will be checked for internal consistency where possible.
