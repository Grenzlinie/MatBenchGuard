# Identification of carrier-trapping surface defects in MAPbI3 under I-rich conditions via first-principles DFT

## Problem background
Perovskite solar cells (PSCs) exhibit high power conversion efficiencies, but carrier trapping at surface defects remains a major performance bottleneck, causing nonradiative recombination and current–voltage hysteresis. On the (001) surface of tetragonal methylammonium lead iodide (MAPbI3), several surface terminations and defect types are possible, yet which specific defects act as carrier traps under iodide-rich fabrication conditions is not well established. This task addresses that question by performing first-principles density functional theory (DFT) calculations to determine the formation energies and electronic defect levels of candidate surface defects, allowing a comparison of their thermodynamic stability and propensity to introduce deep mid-gap states.

## Approach
The approach models the MAPbI3(001) surface using periodic slab supercells with three distinct terminations: MAI, flat, and vacant. Point defects—cation/anion vacancies and interstitials—are introduced on each termination. Structural relaxations are performed with the GGA-PBE exchange-correlation functional, and defect formation energies are then calculated under I-rich chemical potentials. For a subset of defects of particular interest (interstitial iodine on flat and vacant surfaces), the single-particle defect levels are obtained from HSE06 hybrid functional calculations including spin–orbit coupling, referenced to the valence band maximum (VBM) of each slab. The computed formation energies and defect levels allow identification of which defects are both thermodynamically favorable and introduce levels deep within the band gap, thereby acting as carrier traps under I-rich conditions.

## Reproduction target
Produce two CSV files:

- **Formation energies:** for the defects V_MA on MAI termination, and I_i, V_I, Pb_i, V_Pb on both flat and vacant terminations, evaluated under I-rich chemical potentials.
- **Defect levels:** for interstitial iodine (I_i) on the flat and vacant terminations, including the VBM and CBM positions, obtained from HSE06+SOC calculations.

The target is to accurately compute these quantities through DFT simulations, not to retrieve them from any external source.

## Assets

- Tetragonal MAPbI3 crystal structure: 10.1143/JPSJ.71.1694
- DFT code (GGA-PBE + HSE+SOC): Quantum ESPRESSO, GPAW, CP2K, or VASP
- PAW pseudopotentials for H, Pb, C, I, N: PSlibrary, GBRV, or VASP recommended sets

## Workflow steps

### Step 1: Construct surface slab models
- Role: process
- Action: Build 2x2 surface slab models of tetragonal MAPbI3(001) for MAI, flat, and vacant terminations using the experimental lattice constants a=b=17.602 A. Introduce the defect types: V_MA on MAI; I_i, V_I, Pb_i, V_Pb on both flat and vacant terminations. Add a vacuum layer >= 15 A. Orient MA cations to alternate so the slab has no net electric dipole moment.
- Evidence: none

### Step 2: Perform DFT structural relaxations
- Role: process
- Action: Relax atomic positions of all pristine and defected slab models using DFT with the GGA-PBE functional, a plane-wave cutoff of 500 eV, Gamma-point only Brillouin zone sampling, and PAW pseudopotentials. Converge forces to <0.02 eV/A. Spin-orbit coupling is not included during relaxations.
- Evidence: none

### Step 3: Calculate defect formation energies under I-rich conditions
- Role: scored (load-bearing)
- Action: Using the relaxed structures, run total-energy calculations with GGA-PBE, a 500 eV plane-wave cutoff, and a 2x2x1 Gamma-centered k-point mesh. Compute defect formation energies for all defects using the I-rich chemical potentials (mu_I=0 eV, mu_Pb=-2.44 eV, mu_MA=-3.15 eV relative to elemental phases).
- Output file: `/app/outputs/step_01_formation_energies.csv`
- Format: csv
- Contract: defect_name (string), termination (string, one of MAI, flat, vacant), formation_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 4: Calculate HSE+SOC defect levels for I_i defect
- Role: scored (load-bearing)
- Action: For the I_i defect on flat and vacant terminations and the corresponding pristine slabs, perform single-point HSE06 (alpha=0.43) calculations with spin-orbit coupling using a 400 eV plane-wave cutoff and Gamma-point sampling, on the relaxed structures. Identify the VBM, CBM, and defect-state energies from the Kohn-Sham orbital eigenvalues, referencing all levels to the VBM of each system.
- Output file: `/app/outputs/step_02_defect_levels.csv`
- Format: csv
- Contract: termination (string), defect (string), level_eV (float), VBM_eV (float), CBM_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_formation_energies.csv`
- `/app/outputs/step_02_defect_levels.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_formation_energies.csv
- path: `/app/outputs/step_01_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Defect formation energies under I-rich conditions. The checker compares each value to the paper-reported formation energies with an appropriate tolerance.
- schema:
  - `type`: table
  - `required_columns`: `defect_name`, `termination`, `formation_energy_eV`
  - `units`:
    - `formation_energy_eV`: eV

### step_02_defect_levels.csv
- path: `/app/outputs/step_02_defect_levels.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Defect level positions for I_i on flat and vacant terminations, with VBM and CBM references. The checker compares these values to the paper-reported defect levels and band edges with an appropriate tolerance.
- schema:
  - `type`: table
  - `required_columns`: `termination`, `defect`, `level_eV`, `VBM_eV`, `CBM_eV`
  - `units`:
    - `level_eV`: eV
    - `VBM_eV`: eV
    - `CBM_eV`: eV

Notes: The task focuses only on the I-rich chemical condition, as that supports the main claim of I_i being the dominant carrier-trapping defect. Charge density visualizations and other chemical conditions are omitted per scope. The formation energies from Table 1 and defect levels from Figure 2 of the source paper serve as hidden targets; the agent must re-compute them from first principles.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_name",
          "termination",
          "formation_energy_eV"
        ],
        "units": {
          "formation_energy_eV": "eV"
        }
      },
      "description": "Defect formation energies under I-rich conditions. The checker compares each value to the paper-reported formation energies with an appropriate tolerance."
    },
    {
      "file": "step_02_defect_levels.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "termination",
          "defect",
          "level_eV",
          "VBM_eV",
          "CBM_eV"
        ],
        "units": {
          "level_eV": "eV",
          "VBM_eV": "eV",
          "CBM_eV": "eV"
        }
      },
      "description": "Defect level positions for I_i on flat and vacant terminations, with VBM and CBM references. The checker compares these values to the paper-reported defect levels and band edges with an appropriate tolerance."
    }
  ],
  "notes": "The task focuses only on the I-rich chemical condition, as that supports the main claim of I_i being the dominant carrier-trapping defect. Charge density visualizations and other chemical conditions are omitted per scope. The formation energies from Table 1 and defect levels from Figure 2 of the source paper serve as hidden targets; the agent must re-compute them from first principles."
}
```

## How you are scored
Each CSV output is evaluated by a hidden verifier that compares your reported formation energies and defect levels to independently determined reference values. The verifier uses predefined tolerances to award fractional credit for each entry; only values produced by a correct DFT workflow will match. The overall reward is a weighted average of scores from the two artifacts. Reproducing the original study's numerical values without actually performing the computations will not suffice—the checker expects values that are consistent with an independent re-execution of the described protocol within the acceptable numerical margins of the DFT approach.
