# Diffusion Activation Energies and Coefficients via CI-NEB Calculations

## Problem background
Ionic diffusion in lead sulfide (PbS) and silver sulfide (Ag₂S) is relevant for solid-state batteries, electrodes, and catalysts. This work computationally studies the diffusion of Ag⁺, Li⁺, and H⁺ ions in these sulfides using first-principles electronic structure methods. The goal is to determine the activation energies for diffusion and the corresponding diffusion coefficients for several impurity-lattice combinations, providing atomic-scale insight into the diffusion mechanisms.

## Approach
The approach combines density functional theory (DFT) geometry optimizations with the climbing-image nudged elastic band (CI-NEB) method to find minimum energy paths for ion migration. You will build supercells for PbS (face‑centered cubic) and Ag₂S (monoclinic) and introduce point defects—vacancies, substitutional impurities, and interstitials—to create initial and final states for each diffusion pathway. For every system, CI-NEB calculations are run with the endpoints fixed to extract the activation barrier. The diffusion coefficient is then estimated from the activation energy using a transition‑state‑theory Arrhenius expression:  D = l * sqrt(2Eₐ/m) * exp(−Eₐ/(k_B T)), where l is the jump distance, m is the mass of the diffusing ion, and T is the temperature. All DFT computations use the PBE functional, a plane‑wave basis, and ultrasoft pseudopotentials.

## Reproduction target
Produce a single CSV file (diffusion_results.csv) containing the activation energy (eV) and diffusion coefficient (cm²/s) for each of the following seven impurity‑lattice combinations:

- Ag in PbS
- Li in PbS
- H in PbS
- Ag in Pb-doped Ag₂S
- Ag in pure (undoped) Ag₂S
- Li in Ag₂S
- H in Ag₂S

The file must have exactly these columns: impurity, lattice, activation_energy_eV, diffusion_coefficient_cm2_s1, with one row per combination.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Vanderbilt ultrasoft pseudopotentials (PBE): https://www.quantum-espresso.org/pseudopotentials
- Initial crystal structures of PbS (FCC) and Ag₂S (monoclinic)

## Workflow steps

### Step 1: Bulk Unit Cell DFT Optimization
- Role: process
- Action: Perform DFT geometry optimization of the PbS (FCC) and Ag₂S (monoclinic) unit cells using PBE functional, plane-wave basis set with a 30 Ry cutoff, ultrasoft pseudopotentials, and Monkhorst-Pack k-point mesh. Obtain relaxed lattice parameters for both structures.
- Evidence: `/app/outputs/bulk_opt_results.json`

### Step 2: Defect Structure Generation and Relaxation
- Role: process
- Action: Build 2×2×2 supercells from optimized unit cells. For each of the seven diffusion systems (Ag in PbS, Li in PbS, H in PbS, Ag in Pb-doped Ag₂S, Ag in pure Ag₂S, Li in Ag₂S, H in Ag₂S), create the required defects (one Pb vacancy and two Ag/Li/H atoms for PbS; Ag vacancies + Pb dopant for Pb-doped Ag₂S; Frenkel Ag interstitial for pure Ag₂S, substituted for Li/H as needed). Relax the initial and final structures via DFT with the same PBE functional, 30 Ry cutoff, ultrasoft pseudopotentials, and appropriate k-point meshes.
- Evidence: `/app/outputs/defect_structures.json`

### Step 3: CI-NEB and Diffusion Coefficient Computation
- Role: scored (load-bearing)
- Action: For each diffusion system, run a climbing-image nudged elastic band (CI-NEB) calculation keeping the first and last images fixed. Extract the activation energy from the barrier height. Compute the diffusion coefficient using the transition-state-theory Arrhenius expression D = l sqrt(2E_a/m) exp(-E_a/k_B T), where l is the diffusion distance, m is the mass of the diffusing atom, and T is temperature. Write all results to diffusion_results.csv.
- Output file: `/app/outputs/diffusion_results.csv`
- Format: csv
- Contract: impurity, lattice, activation_energy_eV, diffusion_coefficient_cm2_s1
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/diffusion_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### diffusion_results.csv
- path: `/app/outputs/diffusion_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Activation energies and diffusion coefficients for Ag+, Li+, and H+ diffusion in PbS and Ag2S lattices (seven rows).
- schema:
  - `type`: table
  - `required_columns`: `impurity`, `lattice`, `activation_energy_eV`, `diffusion_coefficient_cm2_s1`
  - `units`:
    - `activation_energy_eV`: eV
    - `diffusion_coefficient_cm2_s1`: cm^2/s

Notes: The agent must compute E_a and D via CI-NEB. The hidden checker compares each value against the paper-reported reference within tolerances (activation energy ±0.05 eV, diffusion coefficient within a factor of 2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "diffusion_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "impurity",
          "lattice",
          "activation_energy_eV",
          "diffusion_coefficient_cm2_s1"
        ],
        "units": {
          "activation_energy_eV": "eV",
          "diffusion_coefficient_cm2_s1": "cm^2/s"
        }
      },
      "description": "Activation energies and diffusion coefficients for Ag+, Li+, and H+ diffusion in PbS and Ag2S lattices (seven rows)."
    }
  ],
  "notes": "The agent must compute E_a and D via CI-NEB. The hidden checker compares each value against the paper-reported reference within tolerances (activation energy ±0.05 eV, diffusion coefficient within a factor of 2)."
}
```

## How you are scored
An automated verifier reads your diffusion_results.csv and compares each reported activation energy and diffusion coefficient to expected values that follow from the computational protocol. You receive credit for every impurity‑lattice system that satisfies the required accuracy; partial credit is proportional to the number of correct systems. It is not enough that the file merely exists or is correctly formatted—the numeric results must be obtained by genuinely executing the described workflow. The verifier combines these comparisons into a single reward in [0, 1].
