# Thermoelectric Transport Modeling of NaxCoO2 and ZnRh2O4

## Problem background
Thermoelectric materials convert waste heat into electricity, and their efficiency is governed by the figure of merit ZT = σS²T/κ, where S is the thermopower (Seebeck coefficient). Improving ZT requires large S, which is often associated with low carrier concentrations and narrow band gaps. However, layered sodium cobaltate Na_xCoO_2 exhibits unusually high thermopower even at metallic carrier densities, making it a benchmark oxide thermoelectric. The origin of this large S is debated: some propose that strong electron correlation effects are essential, while others argue that standard band theory with narrow t_2g bands can account for it. This task investigates this by computing the Seebeck coefficient S(T) for Na_xCoO_2 under hole doping and for the related cubic spinel ZnRh_2O_4 under p-type doping, using first-principles electronic structure and Boltzmann transport theory. The goal is to reproduce the predicted thermopower values as a function of temperature and doping level and to understand whether narrow-band effects alone can explain the observed high thermopower.

## Approach
The approach is based on density functional theory (DFT) in the local density approximation (LDA), combined with semiclassical Boltzmann transport in the constant relaxation time approximation. The electronic band structure is computed for two compounds: (1) Na_xCoO_2 with a virtual crystal approximation to model the partially occupied Na sites at composition x = 0.67, and (2) ZnRh_2O_4 in its cubic spinel structure. Eigenvalues are obtained on a dense k‑point mesh that converges the transport integrals. Then, using the BoltzTrap code (or an equivalent implementation), the Seebeck tensor is calculated from the band structure. A rigid-band model is applied to simulate different carrier concentrations: for Na_xCoO_2, hole doping levels h = 0.5, 0.6, 0.7, 0.8 per Co are considered and the in‑plane (ab‑plane) component of S is evaluated; for ZnRh_2O_4, isotropic p‑type doping levels p = 0.5, 1.0, 2.0 per formula unit are evaluated. The calculations are performed at temperatures T = 100, 200, 300, and 400 K. The constant scattering time approximation eliminates the unknown scattering time, making the resulting S(T) a parameter‑free prediction from the band structure.

## Reproduction target
Produce a single CSV file, `Seebeck_vs_T.csv`, that contains the computed Seebeck coefficient (in μV/K) for every combination of compound, doping level, and temperature. Specifically, the file must include: for compound 'Na_xCoO2', doping levels h=0.5, h=0.6, h=0.7, h=0.8; for compound 'ZnRh2O4', doping levels p=0.5, p=1.0, p=2.0; at temperatures 100 K, 200 K, 300 K, and 400 K. The CSV must have the columns: `compound`, `doping_level`, `temperature_K`, `Seebeck_uV_K`. Each row corresponds to one (compound, doping, temperature) combination, and the Seebeck value is the calculated in‑plane component (for Na_xCoO2) or isotropic average (for ZnRh2O4). This file is the sole scored artifact.

## Assets

- Crystal structure of Na_xCoO2 (hexagonal, P63/mmc): https://materialsproject.org/materials/mp-19076
- Crystal structure of ZnRh2O4 (cubic spinel, Fd-3m): https://materialsproject.org/materials/mp-19075
- DFT-LDA code (e.g., Quantum ESPRESSO, WIEN2k): https://www.quantum-espresso.org
- BoltzTrap transport code: https://bitbucket.org/sousaw/boltztrap

## Workflow steps

### Step 1: DFT-LDA band structure of Na0.67CoO2 (virtual crystal)
- Role: process
- Action: Compute the electronic band structure of Na_xCoO2 using density functional theory with the local density approximation and a virtual crystal approximation (x = 0.67). Obtain eigenvalues on a dense k‑point mesh suitable for transport calculations.
- Evidence: `/app/outputs/naco_dft_done.log`

### Step 2: DFT-LDA band structure of ZnRh2O4
- Role: process
- Action: Compute the electronic band structure of cubic spinel ZnRh2O4 using density functional theory with the local density approximation. Obtain eigenvalues on a dense k‑point mesh suitable for transport calculations.
- Evidence: `/app/outputs/znrh_dft_done.log`

### Step 3: Boltzmann transport and Seebeck coefficient computation
- Role: scored (load-bearing)
- Action: Using the eigenvalues from steps 1 and 2, run Boltzmann transport theory with the constant relaxation time approximation and a rigid-band model to compute the Seebeck coefficient (thermopower). For Na_xCoO2 evaluate in‑plane transport at hole doping levels h = 0.5, 0.6, 0.7, 0.8 per Co, and for ZnRh2O4 evaluate isotropic transport at p‑type doping levels p = 0.5, 1.0, 2.0 per formula unit. Evaluate at temperatures 100, 200, 300, 400 K. Write all results to a single CSV.
- Output file: `/app/outputs/Seebeck_vs_T.csv`
- Format: csv
- Contract: compound (str), doping_level (str, e.g. h=0.5), temperature_K (float), Seebeck_uV_K (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Seebeck_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Seebeck_vs_T.csv
- path: `/app/outputs/Seebeck_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Seebeck coefficient values for specified compounds, doping levels, and temperatures.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `doping_level`, `temperature_K`, `Seebeck_uV_K`
  - `units`:
    - `temperature_K`: K
    - `Seebeck_uV_K`: μV/K

Notes: The hidden checker digitizes the paper's S(T) curves and compares the agent's values against those reference values with a relative tolerance. A separate monotonicity check ensures the Seebeck coefficient decreases with increasing doping for a given compound and temperature.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Seebeck_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "doping_level",
          "temperature_K",
          "Seebeck_uV_K"
        ],
        "units": {
          "temperature_K": "K",
          "Seebeck_uV_K": "μV/K"
        }
      },
      "description": "Computed Seebeck coefficient values for specified compounds, doping levels, and temperatures."
    }
  ],
  "notes": "The hidden checker digitizes the paper's S(T) curves and compares the agent's values against those reference values with a relative tolerance. A separate monotonicity check ensures the Seebeck coefficient decreases with increasing doping for a given compound and temperature."
}
```

## How you are scored
A hidden verifier compares your `Seebeck_vs_T.csv` to a set of reference Seebeck values derived from the original study (not accessible to you). The comparison allows for reasonable numerical differences that stem from using a different DFT code, implementation details, or convergence choices—you do not need to match the reference values exactly, but they should be close. Additionally, the verifier checks a structural property: for each compound at a fixed temperature, the Seebeck coefficient must decrease monotonically as the doping level increases. The final reward is a weighted combination of the individual value agreements and the monotonicity check. Reporting the paper’s numbers without actually performing the computations will not pass these checks.
