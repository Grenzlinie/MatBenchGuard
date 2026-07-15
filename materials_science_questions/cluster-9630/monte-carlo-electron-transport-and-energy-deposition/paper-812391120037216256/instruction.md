# Monte Carlo simulation of electron emission beyond linear response using CDW-EIS effective-atom model

## Problem background
Swift highly charged ions (H⁺, C⁶⁺, Ca²⁰⁺, Ni²⁷⁺, Mo³⁹⁺) incident on solids produce electron emission that deviates from a simple Q_P² scaling with projectile charge. Understanding the origin of these deviations is important for modeling ion-solid interactions. This task reproduces a Monte Carlo simulation of electron transport in an amorphous carbon foil that employs an effective-atom description of the primary ionization based on the Continuum Distorted Wave–Eikonal Initial State (CDW‑EIS) approximation. The goal is to compute the total backward electron yield and the electronic stopping power for five isotachic ions and to evaluate how the normalized yield and stopping-power ratios vary with projectile charge.

## Approach
The primary electron source terms for valence and 1s electrons are calculated with the CDW‑EIS effective-atom model, which treats the ion–target interaction as a two‑centre effect going beyond the first‑order Born approximation. These source terms are fed into a Monte Carlo simulation of electron transport governed by a master phase‑space equation. The transport includes elastic scattering from an effective atomic potential (phase‑shift analysis), inelastic scattering with valence electrons via a dielectric response function (Ashley energy‑loss function for amorphous carbon), and inelastic scattering with 1s core electrons using Gryzinski cross‑sections augmented by Auger electron production. From the simulation, the total backward electron yield γ_B and the electronic stopping power dE/dx are extracted for each projectile. Normalized ratios R_γ = 6²·γ_B(X) / (Q_P²·γ_B(C⁶⁺)) and R_dE/dx = 6²·dE/dx(X) / (Q_P²·dE/dx(C⁶⁺)) are then computed to isolate deviations from strict Q_P² scaling.

## Reproduction target
Compute the total backward electron yield γ_B (electrons per ion) and the electronic stopping power dE/dx (keV/nm) for projectile charges 1 (H⁺), 6 (C⁶⁺), 20 (Ca²⁰⁺), 27 (Ni²⁷⁺), and 39 (Mo³⁹⁺) at a projectile velocity v_P = 19 a.u. incident on a 200 µg/cm² amorphous carbon foil (density 2 g/cm³, internal background potential V₀ = −0.700 a.u.). Then calculate the normalized ratios R_γ and R_dE/dx relative to C⁶⁺. The required output files are absolute_values.json and normalized_ratios.csv, whose schemas are detailed in the Output contract section.

## Assets

- Clementi & Roetti atomic wavefunctions for carbon: 10.1016/S0092-640X(74)80016-1
- Ashley dielectric function for carbon

## Workflow steps

### Step 1: Compute CDW-EIS primary source terms
- Role: process
- Action: Calculate the triple-differential primary electron ejection source terms S_val_CDW(k) and S_1s_CDW(k) for projectile charges Q_P = 1, 6, 20, 27, 39 at v_P = 19 a.u. using the CDW-EIS effective-atom approximation. Apply the embedding relation k'^2/2 = k^2/2 + V_0 - U_S with V_0 = -0.700 a.u. and choose U_S in [V_0, 0] (e.g., U_S ≈ 0). Use Clementi-Roetti atomic wavefunctions for 2s, 2p and 1s orbitals. Save the momentum-dependent source terms for each projectile charge.
- Evidence: `/app/outputs/source_terms.npz`

### Step 2: Run Monte Carlo electron transport simulation
- Role: process
- Action: Execute a Monte Carlo simulation of electron transport in a 200 µg/cm² amorphous carbon foil (density 2 g/cm³, V_0 = -0.700 a.u.). Use the CDW-EIS source terms from step 01 and the electron kernels: elastic scattering (phase-shift analysis from an effective potential), inelastic with valence electrons (dielectric response using the Ashley energy-loss function), and inelastic with 1s core electrons (Gryzinski cross sections plus Auger process). Record the trajectories and energy deposits to accumulate the total backward electron yield γ_B and the electronic stopping power dE/dx for each projectile charge.
- Evidence: `/app/outputs/simulation_raw.pkl`

### Step 3: Compute absolute yields and stopping powers
- Role: scored (load-bearing)
- Action: From the Monte Carlo simulation output, extract the total backward electron yield γ_B (electrons/ion) and the electronic stopping power dE/dx (keV/nm) for each of the five ions (H⁺, C⁶⁺, Ca²⁰⁺, Ni²⁷⁺, Mo³⁹⁺). Write the results to absolute_values.json.
- Output file: `/app/outputs/absolute_values.json`
- Format: json
- Contract: JSON object with keys 'H+', 'C6+', 'Ca20+', 'Ni27+', 'Mo39+'. Each value is an object with numeric fields 'gamma_B' (electrons/ion) and 'dE_dx' (keV/nm).
- Scoring: scored by hidden verifier

### Step 4: Compute normalized ratios
- Role: scored (load-bearing)
- Action: Using the absolute values from step 03, calculate the normalized ratios R_γ = 6² · γ_B(X) / (Q_P² · γ_B(C⁶⁺)) and R_dE/dx = 6² · dE/dx(X) / (Q_P² · dE/dx(C⁶⁺)) for each ion. Write a CSV file normalized_ratios.csv with columns Q_P, R_gamma, R_dE_dx.
- Output file: `/app/outputs/normalized_ratios.csv`
- Format: csv
- Contract: CSV with columns: Q_P (integer), R_gamma (float), R_dE_dx (float). Rows for Q_P = 1, 6, 20, 27, 39.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absolute_values.json`
- `/app/outputs/normalized_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absolute_values.json
- path: `/app/outputs/absolute_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total backward electron yield and electronic stopping power for each projectile computed by the CDW-EIS model.
- schema:
  - `type`: object
  - `required`:
    - `H+`:
      - `gamma_B`: float
      - `dE_dx`: float
    - `C6+`:
      - `gamma_B`: float
      - `dE_dx`: float
    - `Ca20+`:
      - `gamma_B`: float
      - `dE_dx`: float
    - `Ni27+`:
      - `gamma_B`: float
      - `dE_dx`: float
    - `Mo39+`:
      - `gamma_B`: float
      - `dE_dx`: float
  - `units`:
    - `gamma_B`: electrons/ion
    - `dE_dx`: keV/nm

### normalized_ratios.csv
- path: `/app/outputs/normalized_ratios.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized backward yield and stopping power ratios relative to C6+; these ratios isolate deviations from strict Q_P² scaling.
- schema:
  - `type`: table
  - `required_columns`: `Q_P`, `R_gamma`, `R_dE_dx`
  - `items`:
    - `Q_P`: int
    - `R_gamma`: float
    - `R_dE_dx`: float
  - `units`:
    - `R_gamma`: dimensionless
    - `R_dE_dx`: dimensionless

Notes: The scored artifacts are compared against hidden reference data using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absolute_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "H+": {
            "gamma_B": "float",
            "dE_dx": "float"
          },
          "C6+": {
            "gamma_B": "float",
            "dE_dx": "float"
          },
          "Ca20+": {
            "gamma_B": "float",
            "dE_dx": "float"
          },
          "Ni27+": {
            "gamma_B": "float",
            "dE_dx": "float"
          },
          "Mo39+": {
            "gamma_B": "float",
            "dE_dx": "float"
          }
        },
        "units": {
          "gamma_B": "electrons/ion",
          "dE_dx": "keV/nm"
        }
      },
      "description": "Total backward electron yield and electronic stopping power for each projectile computed by the CDW-EIS model."
    },
    {
      "file": "normalized_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Q_P",
          "R_gamma",
          "R_dE_dx"
        ],
        "items": {
          "Q_P": "int",
          "R_gamma": "float",
          "R_dE_dx": "float"
        },
        "units": {
          "R_gamma": "dimensionless",
          "R_dE_dx": "dimensionless"
        }
      },
      "description": "Normalized backward yield and stopping power ratios relative to C6+; these ratios isolate deviations from strict Q_P² scaling."
    }
  ],
  "notes": "The scored artifacts are compared against hidden reference data using appropriate tolerances."
}
```

## How you are scored
A hidden verifier reads your absolute_values.json and normalized_ratios.csv files. It compares the absolute yields and stopping powers, as well as the normalized ratios, against hidden reference data. The final reward is based on how well each artifact matches the expected values. Honest execution of the full workflow is required; reporting numbers without running the simulation will not yield a passing score.
