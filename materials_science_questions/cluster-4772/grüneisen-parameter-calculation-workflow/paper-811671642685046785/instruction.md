# Grüneisen Parameter and Equation of State for Diamond from Ab Initio Phonon Theory

## Problem background
Accurate equations of state (EOS) for materials at high pressures and finite temperatures are needed for hydrodynamic simulations of warm condensed matter. While first-principles methods based on density functional theory (DFT) can provide low-temperature properties, extending them to finite temperature requires knowledge of ion and electron thermal contributions. A promising approach is to combine static-lattice DFT energies with vibrational free energies obtained from ab initio phonon calculations. In this task, the method is applied to diamond: a wide-bandgap insulator whose thermal behaviour is dominated by ion vibrations. The goal is to compute the room-temperature isotherm, the principal shock Hugoniot, and the Grüneisen parameter from first principles using an effective Einstein oscillator model derived from linear-response phonons.

## Approach
The free energy is decomposed as F(T,V) = F0(V) + F_ion(T,V) + F_el(T,V). F0(V) is the zero-temperature cold curve, obtained from static-lattice DFT-LDA total-energy calculations using plane-wave pseudopotentials. Linear-response phonon calculations at several volumes yield phonon frequencies; a small set of these frequencies is averaged to define a volume-dependent effective Einstein frequency ω_E(V). The ion vibrational free energy and pressure are then computed within the harmonic Einstein model. The Grüneisen parameter is defined as γ(V) = -d ln ω_E / d ln V, and the ion thermal pressure is P_ion = 3RT γ(V) / V. For diamond, the electronic contribution is negligible due to the large band gap, so the total pressure is the sum of the cold pressure and P_ion. The principal Hugoniot is obtained by solving the Rankine-Hugoniot relation E - E0 = (1/2)(P + P0)(V0 - V), using the computed internal energy and pressure. Agents should implement this workflow with an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and an LDA pseudopotential for carbon.

## Reproduction target
Your objective is to compute and save three data files: 1) Room-temperature isotherm: pressure vs. compression (V/V0) at T = 300 K. Compression range approximately 0.7 to 1.02. 2) Principal shock Hugoniot: pressure vs. compression. Compression range approximately 0.5 to 1.0. 3) Grüneisen parameter γ as a function of compression (dimensionless γ, same compression range as the isotherm). Each file must be a two-column CSV with the specified columns (see Output contract). The computed curves should reflect the underlying physics of diamond as obtained from the ab initio phonon model.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- LDA pseudopotential for carbon (diamond): https://pseudopotentials.quantum-espresso.org/upf_files/C.pz-rrkjus.UPF

## Workflow steps

### Step 1: DFT cold curve and effective Einstein frequency
- Role: process
- Action: Perform plane-wave DFT calculations on diamond using an LDA pseudopotential to obtain static lattice energy F0(V) (cold curve). Run linear-response phonon calculations at several volumes to compute phonon mode frequencies. Average a small set of phonon frequencies to derive a density-dependent effective Einstein frequency omega_E(V).
- Evidence: `/app/outputs/cold_curve_and_phonon_results.json`

### Step 2: Room-temperature isotherm
- Role: scored
- Action: Using the static lattice energy F0(V) and the vibrational free energy computed with the harmonic Einstein model from omega_E(V), calculate pressure as a function of compression at temperature 300 K and output the room-temperature isotherm.
- Output file: `/app/outputs/step_02_room_temp_isotherm.csv`
- Format: csv
- Contract: Two-column CSV: 'compression' (V/V0, dimensionless), 'pressure' (GPa). Compression range approximately 0.7 to 1.02.
- Scoring: scored by hidden verifier

### Step 3: Principal shock Hugoniot
- Role: scored
- Action: From the total free energy (cold curve + vibrational contribution) compute internal energy and pressure, then solve the Rankine-Hugoniot relation for the principal Hugoniot. Output pressure vs. compression.
- Output file: `/app/outputs/step_03_shock_hugoniot.csv`
- Format: csv
- Contract: Two-column CSV: 'compression' (V/V0, dimensionless), 'pressure' (GPa). Compression range approximately 0.5 to 1.0.
- Scoring: scored by hidden verifier

### Step 4: Grüneisen parameter
- Role: scored (load-bearing)
- Action: Calculate the Grüneisen parameter gamma = - d(ln omega_E) / d(ln V) from the effective Einstein frequency omega_E(V). Output gamma as a function of compression.
- Output file: `/app/outputs/step_04_gruneisen_gamma.csv`
- Format: csv
- Contract: Two-column CSV: 'compression' (V/V0, dimensionless), 'gamma' (dimensionless). Compression range similar to isotherm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_room_temp_isotherm.csv`
- `/app/outputs/step_03_shock_hugoniot.csv`
- `/app/outputs/step_04_gruneisen_gamma.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_room_temp_isotherm.csv
- path: `/app/outputs/step_02_room_temp_isotherm.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed room-temperature isotherm for diamond: pressure vs. compression at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `compression`, `pressure`
  - `units`:
    - `compression`: dimensionless (V/V0)
    - `pressure`: GPa

### step_03_shock_hugoniot.csv
- path: `/app/outputs/step_03_shock_hugoniot.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed principal shock Hugoniot for diamond: pressure vs. compression.
- schema:
  - `type`: table
  - `required_columns`: `compression`, `pressure`
  - `units`:
    - `compression`: dimensionless (V/V0)
    - `pressure`: GPa

### step_04_gruneisen_gamma.csv
- path: `/app/outputs/step_04_gruneisen_gamma.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Grüneisen parameter for diamond as a function of compression.
- schema:
  - `type`: table
  - `required_columns`: `compression`, `gamma`
  - `units`:
    - `compression`: dimensionless (V/V0)
    - `gamma`: dimensionless

Notes: All quantities are derived from the same DFT+phonon results (cold curve and effective Einstein frequency). The checker will compare submitted curves against digitized reference curves from the paper using pointwise tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_room_temp_isotherm.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compression",
          "pressure"
        ],
        "units": {
          "compression": "dimensionless (V/V0)",
          "pressure": "GPa"
        }
      },
      "description": "Computed room-temperature isotherm for diamond: pressure vs. compression at 300 K."
    },
    {
      "file": "step_03_shock_hugoniot.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compression",
          "pressure"
        ],
        "units": {
          "compression": "dimensionless (V/V0)",
          "pressure": "GPa"
        }
      },
      "description": "Computed principal shock Hugoniot for diamond: pressure vs. compression."
    },
    {
      "file": "step_04_gruneisen_gamma.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compression",
          "gamma"
        ],
        "units": {
          "compression": "dimensionless (V/V0)",
          "gamma": "dimensionless"
        }
      },
      "description": "Computed Grüneisen parameter for diamond as a function of compression."
    }
  ],
  "notes": "All quantities are derived from the same DFT+phonon results (cold curve and effective Einstein frequency). The checker will compare submitted curves against digitized reference curves from the paper using pointwise tolerances."
}
```

## How you are scored
A hidden verifier independently scores each of the three scored workflow stages. For each stage, the verifier reads your CSV file and compares the computed curves against reference data for diamond. The comparison uses pointwise tolerances and checks the overall trend consistency. The final score is a weighted sum of the per-stage scores. A correct execution of the described method will yield a high score, while simply reporting expected numbers without performing the computations will not.
