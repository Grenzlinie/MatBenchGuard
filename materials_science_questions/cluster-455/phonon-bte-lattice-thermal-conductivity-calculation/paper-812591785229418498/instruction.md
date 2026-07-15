# Phonon BTE lattice thermal conductivity and thermoelectric figure of merit calculation

## Problem background
Half-Heusler compounds are attractive for thermoelectric energy conversion because of their favorable electronic properties. However, most known members of this family suffer from high lattice thermal conductivity, which limits their thermoelectric figure of merit. Recent theoretical work has identified BiBaK as a candidate half-Heusler that may exhibit intrinsically low lattice thermal conductivity. The mechanism proposed is a rattling of the light K atom inside a cage formed by the heavy Bi and Ba atoms, leading to strong phonon scattering and suppressed heat transport. If this mechanism proves effective, it offers a design route toward high thermoelectric performance. Reproducing the full phonon and electronic transport properties of BiBaK is therefore an important validation step, and this task challenges you to compute the key quantities that determine its performance.

## Approach
The task uses first-principles calculations and Boltzmann transport theory to evaluate both the lattice and electronic transport contributions. The overall strategy is:

1. **Structure and phonons** – Optimize the cubic BiBaK crystal structure with density functional theory (DFT), compute harmonic and anharmonic interatomic force constants via the finite-displacement method, and then solve the phonon Boltzmann transport equation to obtain the lattice thermal conductivity, phonon group velocities, and relaxation times.
2. **Electronic structure** – Compute the electronic band structure of BiBaK using a hybrid functional with spin-orbit coupling to obtain an accurate band gap. From the band structure, extract deformation potential constants and density-of-states effective masses to estimate carrier relaxation times via deformation potential theory.
3. **Electronic transport and ZT** – Feed the electronic band structure and relaxation times into semiclassical Boltzmann transport theory to calculate the Seebeck coefficient, electrical conductivity, and electronic thermal conductivity as functions of carrier concentration and temperature. Combine the electronic contributions with the previously obtained lattice thermal conductivity to evaluate the thermoelectric figure of merit ZT.

All calculations can be performed with open-source tools: a suitable DFT code (e.g., Quantum ESPRESSO), phonopy for force constants, ShengBTE for the phonon transport, and BoltzTraP2 for electronic transport. The pipeline is fully defined; the agent must execute it and extract the requested quantities.

## Reproduction target
The goal is to compute and report the following three results for BiBaK:

1. **Lattice thermal conductivity** at 300 K and 900 K, in W m⁻¹ K⁻¹.
2. **Mean phonon group velocities** for the transverse acoustic (TA) and longitudinal acoustic (LA) branches, in m s⁻¹.
3. **Maximum n-type thermoelectric figure of merit ZT** at 900 K, together with the corresponding optimum carrier concentration (cm⁻³).

Each of these quantities must be saved in a dedicated JSON file as specified in the workflow steps. The task is considered successfully reproduced if all three artifacts fall within acceptable agreement with independent reference values. There is no need to reproduce the qualitative plots or p-type branches beyond their role in arriving at the scored values.

## Assets

- DFT code (e.g., Quantum ESPRESSO with pseudopotentials for Bi, Ba, K): https://www.quantum-espresso.org/
- PHONOPY: https://phonopy.github.io/phonopy/
- ShengBTE: https://www.shengbte.org/
- BoltzTraP2: https://gitlab.com/sousaw/BoltzTraP2
- Pseudopotential library (e.g., SSSP or PSlibrary): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Structural optimization and configuration selection
- Role: process
- Action: Optimize the crystal structure of BiBaK in the cubic phase (space group F-43m) with the three atoms at Wyckoff positions 4c (Bi), 4b (Ba), 4a (K), using DFT, to obtain the relaxed lattice constant and structure.
- Evidence: `/app/outputs/relaxed_structure.cif`

### Step 2: Harmonic force constant calculation
- Role: process
- Action: Compute second-order interatomic force constants using the finite-displacement method on a supercell of the relaxed structure, employing phonopy.
- Evidence: `/app/outputs/FORCE_CONSTANTS`

### Step 3: Anharmonic force constant calculation
- Role: process
- Action: Compute third-order interatomic force constants using a larger supercell and a cutoff radius, employing phonopy.
- Evidence: `/app/outputs/FORCE_CONSTANTS_3RD`

### Step 4: Phonon transport BTE solution
- Role: process
- Action: Solve the linearized phonon Boltzmann transport equation using ShengBTE with the harmonic and anharmonic force constants, on a dense q-mesh, to obtain phonon transport properties (lattice thermal conductivity, group velocities, relaxation times).
- Evidence: `/app/outputs/BTE.out`

### Step 5: Report lattice thermal conductivity at target temperatures
- Role: scored
- Action: From the ShengBTE output, extract the lattice thermal conductivity at 300 K and 900 K and write a JSON file.
- Output file: `/app/outputs/thermal_conductivity.json`
- Format: json
- Contract: {
  "type": "object",
  "properties": {
    "temperature_K": {"type": "array", "items": {"type": "number"}},
    "kappa_l_W_mK": {"type": "array", "items": {"type": "number"}}
  }
}
- Scoring: scored by hidden verifier

### Step 6: Report mean phonon group velocities
- Role: scored (load-bearing)
- Action: From the ShengBTE output, compute the mean group velocities for the transverse acoustic (TA) and longitudinal acoustic (LA) branches and write a JSON file.
- Output file: `/app/outputs/phonon_group_velocities.json`
- Format: json
- Contract: {
  "type": "object",
  "properties": {
    "TA_mean_m_s": {"type": "number"},
    "LA_mean_m_s": {"type": "number"}
  }
}
- Scoring: scored by hidden verifier

### Step 7: Electronic structure and deformation potential calculation
- Role: process
- Action: Compute the electronic band structure of BiBaK using a hybrid functional (HSE) with spin-orbit coupling, and calculate the elastic constant, DOS effective masses, and deformation potential constants for electrons and holes.
- Evidence: `/app/outputs/band_results.h5`

### Step 8: Electronic transport coefficients calculation
- Role: process
- Action: Using the band structure and deformation potential constants, compute the Seebeck coefficient, electrical conductivity, and electronic thermal conductivity as functions of carrier concentration and temperature using the semi-classical Boltzmann transport theory.
- Evidence: `/app/outputs/transport_no_path`

### Step 9: Report maximum n-type ZT at 900 K
- Role: scored (load-bearing)
- Action: Combine the lattice thermal conductivity from step_04 with the electronic transport coefficients to compute ZT as a function of carrier concentration at 900 K. Extract the maximum ZT value for n-type doping and the corresponding carrier concentration, and write a JSON file.
- Output file: `/app/outputs/ZT_n_type.json`
- Format: json
- Contract: {
  "type": "object",
  "properties": {
    "ZT_max": {"type": "number"},
    "carrier_concentration_cm-3": {"type": "number"},
    "temperature_K": {"type": "number", "const": 900}
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity.json`
- `/app/outputs/phonon_group_velocities.json`
- `/app/outputs/ZT_n_type.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity.json
- path: `/app/outputs/thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lattice thermal conductivity at 300 K and 900 K for BiBaK.
- schema:
  - `type`: object
  - `properties`:
    - `temperature_K`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Temperatures in Kelvin
    - `kappa_l_W_mK`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Lattice thermal conductivity in W/mK
  - `required`: `temperature_K`, `kappa_l_W_mK`

### phonon_group_velocities.json
- path: `/app/outputs/phonon_group_velocities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mean phonon group velocities for the TA and LA branches.
- schema:
  - `type`: object
  - `properties`:
    - `TA_mean_m_s`:
      - `type`: number
      - `description`: Mean group velocity of transverse acoustic branch in m/s
    - `LA_mean_m_s`:
      - `type`: number
      - `description`: Mean group velocity of longitudinal acoustic branch in m/s
  - `required`: `TA_mean_m_s`, `LA_mean_m_s`

### ZT_n_type.json
- path: `/app/outputs/ZT_n_type.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum n-type ZT and optimum carrier concentration at 900 K.
- schema:
  - `type`: object
  - `properties`:
    - `ZT_max`:
      - `type`: number
      - `description`: Maximum n-type ZT at 900 K
    - `carrier_concentration_cm-3`:
      - `type`: number
      - `description`: Optimum carrier concentration in cm^{-3} at which ZT_max is achieved
    - `temperature_K`:
      - `type`: number
      - `description`: Temperature in Kelvin (must be 900)
  - `required`: `ZT_max`, `carrier_concentration_cm-3`, `temperature_K`

Notes: All scored artifacts are produced from DFT and Boltzmann transport calculations. The checker compares the reported values to reference values with appropriate tolerances; for ZT, higher values are accepted as better performance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "temperature_K": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Temperatures in Kelvin"
          },
          "kappa_l_W_mK": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Lattice thermal conductivity in W/mK"
          }
        },
        "required": [
          "temperature_K",
          "kappa_l_W_mK"
        ]
      },
      "description": "Lattice thermal conductivity at 300 K and 900 K for BiBaK."
    },
    {
      "file": "phonon_group_velocities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "TA_mean_m_s": {
            "type": "number",
            "description": "Mean group velocity of transverse acoustic branch in m/s"
          },
          "LA_mean_m_s": {
            "type": "number",
            "description": "Mean group velocity of longitudinal acoustic branch in m/s"
          }
        },
        "required": [
          "TA_mean_m_s",
          "LA_mean_m_s"
        ]
      },
      "description": "Mean phonon group velocities for the TA and LA branches."
    },
    {
      "file": "ZT_n_type.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "properties": {
          "ZT_max": {
            "type": "number",
            "description": "Maximum n-type ZT at 900 K"
          },
          "carrier_concentration_cm-3": {
            "type": "number",
            "description": "Optimum carrier concentration in cm^{-3} at which ZT_max is achieved"
          },
          "temperature_K": {
            "type": "number",
            "description": "Temperature in Kelvin (must be 900)"
          }
        },
        "required": [
          "ZT_max",
          "carrier_concentration_cm-3",
          "temperature_K"
        ]
      },
      "description": "Maximum n-type ZT and optimum carrier concentration at 900 K."
    }
  ],
  "notes": "All scored artifacts are produced from DFT and Boltzmann transport calculations. The checker compares the reported values to reference values with appropriate tolerances; for ZT, higher values are accepted as better performance."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the three scored output files. Each artifact is checked independently against reference criteria that account for the expected spread of numerical results from different toolchains and implementations. The checks include:

- For the lattice thermal conductivity, verifying that the reported values are within a tolerance of the reference and that they decrease with temperature as expected.
- For the phonon group velocities, comparing the TA and LA branch averages to reference values with an appropriate tolerance.
- For the n-type ZT at 900 K, comparing the reported maximum ZT to a reference threshold and confirming that the corresponding carrier concentration lies in a physically reasonable range.

The final reward is a weighted combination of the scores from each artifact. It is not enough to write a plausible-looking number; the pipeline must be executed honestly, and the verifier may also perform basic structural checks on the submitted files. Do not attempt to back‑out the reference values from this description—focus on running the full computational protocol correctly.
