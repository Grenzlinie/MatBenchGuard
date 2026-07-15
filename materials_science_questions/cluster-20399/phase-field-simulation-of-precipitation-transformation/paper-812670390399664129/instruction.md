# Phase-field analysis of U-Nb alloy local equilibria and energy barrier

## Problem background
Discontinuous precipitation (DP) in U-Nb alloys involves the decomposition of the supersaturated bcc γ matrix into orthorhombic α and a metastable bcc γ' phase, which can eventually transform to the stable γ₂ phase. The thermodynamic origin that stabilizes the intermediate γ' product against immediate decomposition is unclear. This work uses phase-field simulations with a finite-interface-dissipation model and CALPHAD free energies to find local equilibria (LE) between the α and γ phases and to quantify any energy barriers that may trap the system in an intermediate state. The target is to compute the γ-phase compositions at local equilibrium and the energy barrier from 1D diffusion-couple simulations across several temperatures.

## Approach
The finite-interface-dissipation phase-field model is used, where the chemical free energy density is taken from the CALPHAD Gibbs energies of the α (orthorhombic) and γ (bcc) phases. A 1D diffusion couple is set up with an initial α region and an initial γ region. The evolution equations for phase fractions and phase compositions are solved numerically until the Kirkendall interface stops, the chemical driving force vanishes, and the bulk compositions become homogeneous – at which point a local equilibrium (LE) is reached. The search is performed at 450°C, 550°C, and 605°C. At a temperature where a single LE is reached initially, a small external driving force may be applied to overcome a region of negative driving force; the peak energy required to cross this barrier is recorded, and the simulation then proceeds to a second LE. The overall approach is to run the 1D phase-field diffusion-couple simulations and extract the LE compositions and the energy barrier.

## Reproduction target
Produce, from the 1D phase-field simulations, the following quantities:
- At 450°C: the γ-phase composition (at.% Nb) at the local equilibrium found by the simulation.
- At 550°C: the γ-phase composition (at.% Nb) at the local equilibrium found by the simulation.
- At 605°C: the γ-phase compositions (at.% Nb) at the two local equilibria found, denoted LE1 and LE2 (in the order discovered by the simulation).
- At 605°C: the peak energy barrier (in J/mol) that must be overcome to transition from the first LE to the second LE.
All results are to be written to JSON files as specified in the workflow steps.

## Assets

- CALPHAD thermodynamic assessment for U-Nb (Duong et al. 2016): https://doi.org/10.1016/j.calphad.2016.08.003

## Workflow steps

### Step 1: Run 1D phase-field diffusion-couple simulations
- Role: process
- Action: Implement the finite-interface-dissipation phase-field model (chemical free energy density using the CALPHAD Gibbs energies, phase-field evolution equations for phase fractions and compositions with interface permeability, chemical driving force calculation) using the parameters provided in the paper (interface width 6 nm, grid spacing 2 nm, diffusivities, atomic mobilities, interfacial energies, molar volume 12.27 cm³/mol). Set up a 1D diffusion couple of α (0.1 μm, 1 at.% Nb) and γ (0.9 μm, 13 at.% Nb) with 500 grid points (Δx=2 nm). Perform simulations at 450°C, 550°C, and 605°C until the Kirkendall interface stops moving, the chemical driving force vanishes, and bulk compositions become homogeneous. At 605°C, after reaching the first LE, apply a small external driving force to overcome the negative driving force region; record the peak energy barrier. Continue until the second LE is reached. Save all necessary intermediate data (time evolution, interface position, driving force, compositions) for later extraction of the target quantities.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Extract local equilibrium compositions
- Role: scored (load-bearing)
- Action: From the simulation output of step 1, extract the homogeneous γ-phase compositions (in at.% Nb) at the found local equilibria for each temperature and write them to the output file.
- Output file: `/app/outputs/step_04_local_equilibria.json`
- Format: json
- Contract: {"T450_c_gamma_at_pct": float, "T550_c_gamma_at_pct": float, "T605_c_gamma_LE1_at_pct": float, "T605_c_gamma_LE2_at_pct": float}
- Scoring: scored by hidden verifier

### Step 3: Extract energy barrier
- Role: scored (load-bearing)
- Action: From the 605°C simulation output of step 1, extract the peak energy barrier (J/mol) that was overcome during the forced transition from the intermediate LE to the stable LE, and write it to the output file.
- Output file: `/app/outputs/step_05_energy_barrier.json`
- Format: json
- Contract: {"barrier_J_per_mol": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_local_equilibria.json`
- `/app/outputs/step_05_energy_barrier.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_local_equilibria.json
- path: `/app/outputs/step_04_local_equilibria.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Local equilibrium γ-phase compositions at 450°C, 550°C, and the two LEs at 605°C.
- schema:
  - `type`: object
  - `required`:
    - `T450_c_gamma_at_pct`: float (at.% Nb)
    - `T550_c_gamma_at_pct`: float (at.% Nb)
    - `T605_c_gamma_LE1_at_pct`: float (at.% Nb)
    - `T605_c_gamma_LE2_at_pct`: float (at.% Nb)

### step_05_energy_barrier.json
- path: `/app/outputs/step_05_energy_barrier.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Peak energy barrier overcome during the forced transition from intermediate LE to stable LE at 605°C.
- schema:
  - `type`: object
  - `required`:
    - `barrier_J_per_mol`: float (J/mol)

Notes: The checker reads each JSON file and compares the reported numerical values against the paper’s hidden gold values using absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_local_equilibria.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "T450_c_gamma_at_pct": "float (at.% Nb)",
          "T550_c_gamma_at_pct": "float (at.% Nb)",
          "T605_c_gamma_LE1_at_pct": "float (at.% Nb)",
          "T605_c_gamma_LE2_at_pct": "float (at.% Nb)"
        }
      },
      "description": "Local equilibrium γ-phase compositions at 450°C, 550°C, and the two LEs at 605°C."
    },
    {
      "file": "step_05_energy_barrier.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "barrier_J_per_mol": "float (J/mol)"
        }
      },
      "description": "Peak energy barrier overcome during the forced transition from intermediate LE to stable LE at 605°C."
    }
  ],
  "notes": "The checker reads each JSON file and compares the reported numerical values against the paper’s hidden gold values using absolute tolerances."
}
```

## How you are scored
Each scored output artifact is independently evaluated by a hidden verifier. The verifier checks the reported numerical values against expected values using appropriate tolerances. The final reward (a number between 0 and 1) is a weighted combination of the scores from the two scored steps (step_02_local_equilibria and step_03_energy_barrier). Partial credit is given for correct partial results. Reporting the paper’s numbers directly without actually executing the simulation will not pass the verifier’s checks.
