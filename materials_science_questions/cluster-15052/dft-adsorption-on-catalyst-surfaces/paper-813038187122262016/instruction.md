# CO Oxidation First-Step Eley-Rideal Barriers on Ni-Embedded BNNTs via DFT

## Problem background
Carbon monoxide (CO) is a toxic pollutant and a poison for hydrogen fuel cell electrodes. Catalytic oxidation to CO2 is an effective removal method. Single-atom catalysts (SACs) based on transition metals embedded in two-dimensional materials are promising, and boron nitride nanotubes (BNNTs) offer a well-defined hollow interior that could confine the active metal atom. However, the impact of confinement inside BNNTs on the catalytic reaction barrier for CO oxidation has not been fully quantified. In particular, the first Eley-Rideal (ER) step, CO(gas) + O2(ads) → CO2 + O(ads), is believed to be rate-determining, but the energy barriers for Ni atoms embedded in interior N-vacancies of BNNTs of different diameters remain an open question. This task aims to compute these barriers via first-principles calculations.

## Approach
The calculations employ spin-polarized density functional theory (DFT) using the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional and the Grimme D3 dispersion correction. An open-source plane-wave DFT code (e.g., Quantum ESPRESSO) is used. Three armchair BNNTs — (5,5), (6,6), and (7,7) — are constructed in large supercells to avoid inter-tube interactions. A single nitrogen atom is removed from the inner wall to create an N-vacancy, and a Ni atom is placed at the vacancy site. The catalyst structures are fully relaxed. Then, an O2 molecule is pre-adsorbed on Ni in the most stable side-on configuration and the geometry is optimized to obtain the initial state (IS) of the ER step. The final state (FS) consists of a CO2 molecule and a remaining O atom adsorbed on Ni; this structure is also optimized. Using the optimized IS and FS, the climbing-image nudged elastic band (CI-NEB) method locates the transition state (TS). The energy barrier for each tube is calculated as the total energy difference between the TS and IS. These computed barriers, one for each chirality, constitute the main result.

## Reproduction target
Compute the first-step Eley-Rideal energy barriers (in eV) for the reaction CO(gas) + O2(ads) → CO2 + O(ads) on a single Ni atom embedded in an N-vacancy on the interior wall of BNNT(5,5), BNNT(6,6), and BNNT(7,7). Write the three barriers to a JSON file at /app/outputs/barriers.json with exactly the keys "BNNT(5,5)_N-Vacancy-in", "BNNT(6,6)_N-Vacancy-in", and "BNNT(7,7)_N-Vacancy-in", each mapped to a floating-point number in eV.

## Assets

- Quantum ESPRESSO (or equivalent open-source DFT code): https://www.quantum-espresso.org/
- Standard pseudopotential library: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Build and optimize Ni-embedded BNNT structures
- Role: process
- Action: Construct armchair BNNT(5,5), (6,6), (7,7) unit cells, create a single N-vacancy on the inner wall, embed a Ni atom at the vacancy, and perform spin-polarized DFT geometry optimization using PBE+D3 to obtain the stable catalyst models. Save the relaxed coordinates and energies for each tube.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: Pre-adsorb O2 and prepare initial/final states for the first ER step
- Role: process
- Action: For each tube, adsorb O2 on Ni in the most stable side-on configuration and relax the geometry to obtain the initial state (IS) for the Eley-Rideal step. Also set up the final state (FS) with a CO2 molecule and a remaining O atom adsorbed on Ni, and optimize it. Save the IS and FS energies and coordinates.
- Evidence: `/app/outputs/initial_final_states.json`

### Step 3: Compute first-step ER barriers via CI-NEB
- Role: scored (load-bearing)
- Action: Using the optimized IS and FS from the previous step, run the climbing-image nudged elastic band (CI-NEB) method with several images to locate the transition state for the reaction CO(gas) + O2(ads) -> CO2 + O(ads). Extract the total energy of the transition state (TS) and compute the energy barrier as the difference between TS energy and IS energy for each tube (BNNT(5,5), BNNT(6,6), BNNT(7,7) with interior N-vacancy). Report the three barriers in a JSON file.
- Output file: `/app/outputs/barriers.json`
- Format: json
- Contract: {"BNNT(5,5)_N-Vacancy-in": <float>, "BNNT(6,6)_N-Vacancy-in": <float>, "BNNT(7,7)_N-Vacancy-in": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers.json
- path: `/app/outputs/barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Computed first-step Eley-Rideal energy barriers for CO oxidation on interior Ni-BNNTs with N-vacancy. The value represents the energy difference between the transition state and the initial state for the reaction CO(gas) + O2(ads) -> CO2 + O(ads).
- schema:
  - `type`: object
  - `required`:
    - `BNNT(5,5)_N-Vacancy-in`: number (eV)
    - `BNNT(6,6)_N-Vacancy-in`: number (eV)
    - `BNNT(7,7)_N-Vacancy-in`: number (eV)
  - `units`:
    - `BNNT(5,5)_N-Vacancy-in`: eV
    - `BNNT(6,6)_N-Vacancy-in`: eV
    - `BNNT(7,7)_N-Vacancy-in`: eV

Notes: Only the first ER step barriers are scored; second-step barriers and exterior-surface cases are omitted as they are not required for the main claim.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "BNNT(5,5)_N-Vacancy-in": "number (eV)",
          "BNNT(6,6)_N-Vacancy-in": "number (eV)",
          "BNNT(7,7)_N-Vacancy-in": "number (eV)"
        },
        "units": {
          "BNNT(5,5)_N-Vacancy-in": "eV",
          "BNNT(6,6)_N-Vacancy-in": "eV",
          "BNNT(7,7)_N-Vacancy-in": "eV"
        }
      },
      "description": "Computed first-step Eley-Rideal energy barriers for CO oxidation on interior Ni-BNNTs with N-vacancy. The value represents the energy difference between the transition state and the initial state for the reaction CO(gas) + O2(ads) -> CO2 + O(ads)."
    }
  ],
  "notes": "Only the first ER step barriers are scored; second-step barriers and exterior-surface cases are omitted as they are not required for the main claim."
}
```

## How you are scored
A hidden verifier will evaluate your submitted barriers.json. It compares each of your three computed barriers to reference values using an absolute tolerance; full credit is awarded when a barrier falls within a close margin, and partial credit decays linearly for larger deviations up to a maximum allowed discrepancy. In addition, the verifier checks the relative ordering of the three barriers (expected trend: 5,5 > 7,7 > 6,6). The final score is a weighted combination of the per-barrier accuracy and the trend check. Simply reporting a known reference value without performing the DFT and CI-NEB steps will yield a low score if your computed barriers differ from the expected results.
