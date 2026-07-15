# DFT Formation Energies and Band Gaps of Doped Anatase TiO2

## Problem background
Anatase titanium dioxide (TiO2) is a wide-bandgap semiconductor widely studied as a photocatalyst but is only active under ultraviolet light. Doping with impurity atoms, such as nitrogen (N) and tungsten (W), can narrow the band gap and extend absorption into the visible region. This task investigates the effects of single doping with N or W and codoping with both on the electronic structure and formation thermodynamics of anatase TiO2. The goal is to understand how codoping modifies the stability and band gap compared to the individual dopants, and whether it leads to enhanced visible-light activity.

## Approach
The approach uses spin-polarized density functional theory (DFT) with the generalized gradient approximation (PBE functional). Bulk anatase is first optimized to obtain the equilibrium lattice constants. A (2×2×1) supercell (48 atoms) is then constructed. Three substitutionally doped systems are modeled: (a) one O replaced by N (N-doped), (b) one Ti replaced by W (W-doped), and (c) an adjacent O–Ti pair replaced by N and W (N/W-codoped). For each supercell — pure and doped — a full geometry relaxation (cell fixed) is performed, followed by a static electronic-structure calculation to obtain total energies and Kohn-Sham eigenvalues. Reference total energies of O2 molecule, N2 molecule, bulk Ti metal, and bulk W metal are computed using the same DFT settings. From these, the formation energy of each doped system is evaluated under both Ti-rich and O-rich chemical potential conditions using standard formation energy expressions. The fundamental band gap (the difference between the valence band maximum and conduction band minimum) is extracted from the Kohn-Sham eigenvalues of each relaxed system.

## Reproduction target
Produce two JSON files: (1) `formation_energies.json` containing the six formation energies (in eV) for N-doped, W-doped, and N/W-codoped anatase under Ti-rich and O-rich conditions, with keys `N_Tirich`, `N_Orich`, `W_Tirich`, `W_Orich`, `NW_Tirich`, `NW_Orich`. (2) `band_gaps.json` containing the fundamental band gaps (in eV) of the pure, N-doped, W-doped, and N/W-doped systems, with keys `pure`, `N`, `W`, `NW`. The hidden verifier will check that the computed values match reference targets within tolerances and that the relative ordering of formation energies and band gaps across doping conditions follows physically expected trends.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Anatase TiO2 crystal structure: https://www.crystallography.net/cod/9011340.html
- PBE pseudopotentials (Ti, O, N, W): https://www.quantum-espresso.org/pseudopotentials
- Reference species structures (O2, N2, bulk Ti, bulk W)

## Workflow steps

### Step 1: Bulk Anatase Optimization
- Role: process
- Action: Perform DFT geometry optimization of bulk anatase TiO2 to obtain equilibrium lattice parameters a and c. Use PBE exchange-correlation functional.
- Evidence: `/app/outputs/bulk_optimization.log`

### Step 2: Compute Reference Total Energies
- Role: process
- Action: Compute total energies of O2 molecule, N2 molecule, bulk Ti metal, and bulk W metal using the same DFT settings. These energies will be used as chemical potentials.
- Evidence: `/app/outputs/reference_energies.json`

### Step 3: Construct Pure and Doped Supercells
- Role: process
- Action: Using the optimized lattice parameters, build a (2x2x1) supercell of anatase (48 atoms). Then create substitutionally doped supercells: N-doped (O replaced by N), W-doped (Ti replaced by W), and N/W-codoped (adjacent O and Ti replaced by N and W).
- Evidence: `/app/outputs/supercell_structures.log`

### Step 4: DFT Simulations of All Supercells
- Role: process
- Action: For each supercell (pure, N-doped, W-doped, N/W-codoped), perform spin-polarized DFT calculations: relax atomic positions (cell fixed) using PBE, then run a static electronic-structure calculation to obtain total energy and Kohn-Sham eigenvalues. Save the relaxed total energies and final structures, as well as eigenvalues.
- Evidence: `/app/outputs/supercell_total_energies.json`

### Step 5: Calculate Formation Energies
- Role: scored (load-bearing)
- Action: Using the total energies of the doped supercells, the pure supercell, and the reference energies, compute the formation energy for each doped system under Ti-rich and O-rich conditions according to the standard formation energy formula. Use the appropriate chemical potential definitions: for O-rich, mu_O = 1/2 E(O2), mu_Ti from equilibrium condition; for Ti-rich, mu_Ti = E(bulk Ti)/atom, mu_O from equilibrium condition. mu_N = 1/2 E(N2), mu_W = E(bulk W)/atom. Output all six values in eV.
- Output file: `/app/outputs/formation_energies.json`
- Format: json
- Contract: {"type": "object", "properties": {"N_Tirich": {"type": "number"}, "N_Orich": {"type": "number"}, "W_Tirich": {"type": "number"}, "W_Orich": {"type": "number"}, "NW_Tirich": {"type": "number"}, "NW_Orich": {"type": "number"}}}
- Scoring: scored by hidden verifier

### Step 6: Determine Band Gaps
- Role: scored
- Action: From the Kohn-Sham eigenvalues of each supercell calculation, extract the fundamental band gap (energy difference between VBM and CBM) for the pure, N-doped, W-doped, and N/W-doped systems. Record the gaps in eV.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"type": "object", "properties": {"pure": {"type": "number"}, "N": {"type": "number"}, "W": {"type": "number"}, "NW": {"type": "number"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/formation_energies.json`
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### formation_energies.json
- path: `/app/outputs/formation_energies.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Formation energies (eV) for N-, W-, and N/W-doped anatase under Ti-rich and O-rich conditions. Checker compares each reported value to hidden reference tolerances and verifies that the formation energies satisfy specific trend inequalities (e.g., N/W-codoping has lower formation energy than single W-doping under Ti-rich conditions).
- schema:
  - `type`: object
  - `properties`:
    - `N_Tirich`:
      - `type`: number
    - `N_Orich`:
      - `type`: number
    - `W_Tirich`:
      - `type`: number
    - `W_Orich`:
      - `type`: number
    - `NW_Tirich`:
      - `type`: number
    - `NW_Orich`:
      - `type`: number

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fundamental band gaps (eV) of pure anatase, N-doped, W-doped, and N/W-doped systems. Checker compares directly to paper-reported values with tolerances.
- schema:
  - `type`: object
  - `properties`:
    - `pure`:
      - `type`: number
    - `N`:
      - `type`: number
    - `W`:
      - `type`: number
    - `NW`:
      - `type`: number

Notes: The formation energies and band gaps are compared to hidden paper-reported values with tolerances; structural trend inequalities are also verified. No recomputation from raw artifacts is performed. All scored values are derived from DFT runs using publicly available inputs and open-source software.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "properties": {
          "N_Tirich": {
            "type": "number"
          },
          "N_Orich": {
            "type": "number"
          },
          "W_Tirich": {
            "type": "number"
          },
          "W_Orich": {
            "type": "number"
          },
          "NW_Tirich": {
            "type": "number"
          },
          "NW_Orich": {
            "type": "number"
          }
        }
      },
      "description": "Formation energies (eV) for N-, W-, and N/W-doped anatase under Ti-rich and O-rich conditions. Checker compares each reported value to hidden reference tolerances and verifies that the formation energies satisfy specific trend inequalities (e.g., N/W-codoping has lower formation energy than single W-doping under Ti-rich conditions)."
    },
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "pure": {
            "type": "number"
          },
          "N": {
            "type": "number"
          },
          "W": {
            "type": "number"
          },
          "NW": {
            "type": "number"
          }
        }
      },
      "description": "Fundamental band gaps (eV) of pure anatase, N-doped, W-doped, and N/W-doped systems. Checker compares directly to paper-reported values with tolerances."
    }
  ],
  "notes": "The formation energies and band gaps are compared to hidden paper-reported values with tolerances; structural trend inequalities are also verified. No recomputation from raw artifacts is performed. All scored values are derived from DFT runs using publicly available inputs and open-source software."
}
```

## How you are scored
A hidden verifier independently scores the two output artifacts. It reads your `formation_energies.json` and `band_gaps.json` and compares each numeric value to a hidden reference (target value) with predefined tolerances. In addition, the verifier checks that the formation energies and band gaps satisfy expected structural trends (e.g., certain inequalities between different doping conditions). Your final score is a weighted combination of these sub-scores, where the formation energies and band gaps together determine the majority of the reward. To receive credit, the values must come from a properly executed DFT pipeline; the verifier also inspects the accompanying evidence (log files and intermediate energy files) to ensure the simulation steps were completed.
