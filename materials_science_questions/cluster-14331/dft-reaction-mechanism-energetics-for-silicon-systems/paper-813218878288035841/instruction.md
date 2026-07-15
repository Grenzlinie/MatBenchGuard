# DFT study of styrene adsorption and H-abstraction on OH/H-terminated Si(100)-(2×1)

## Problem background
The functionalization of semiconductor surfaces with organic molecules is important for molecular electronics and sensor devices. On the hydrogen-terminated Si(100)-(2×1) surface, terminal unsaturated molecules can undergo radical chain-reactions that form ordered molecular nanostructures. A key question is how surface hydroxyl (–OH) groups on water-saturated Si(100)-(2×1) affect these chain reactions. While H-abstraction from Si–H groups is well-known, the role of –OH groups is less clear: they might either block propagation or serve as a medium for radical transfer. This task investigates the radical chain-reaction of styrene on a water-saturated Si(100)-(2×1) surface by computing adsorption energies and energy barriers for H-atom and OH-group abstraction processes using density functional theory (DFT).

## Approach
The water-saturated Si(100)-(2×1) surface is modeled as a periodic slab using DFT with the Perdew-Burke-Ernzerhof (PBE) functional and Grimme D2 dispersion correction. The slab contains six Si layers and two dimer rows, with surface Si atoms alternately terminated by –OH and –H groups in a zigzag pattern. A surface dangling bond is introduced by removing one hydrogen atom. The radical chain-reaction is then studied in two stages: (1) barrierless adsorption of a styrene molecule onto the dangling bond, and (2) subsequent H-atom or OH-group abstraction from neighbouring surface groups by the β-carbon radical of the adsorbed styrene. Transition states for H-abstraction from –OH groups along three directions (intradimer, interdimer, and cross-dimer-row) and for direct interdimer OH-abstraction are located and their energy barriers computed. All calculations are performed using an open-source DFT package capable of periodic slab calculations, geometry optimization, and transition state search (e.g., NEB).

## Reproduction target
Using an open-source DFT code (e.g., Quantum ESPRESSO or CP2K) with the PBE functional and Grimme D2 dispersion correction, perform the following for styrene on the zigzag-patterned water-saturated Si(100)-(2×1) slab with a surface dangling bond: (a) compute the adsorption energy of styrene (positive value of released energy, in eV); (b) compute the energy barriers for H-abstraction from a surface –OH group along the intradimer (r1), interdimer (r2), and cross-dimer-row (r3) directions; (c) compute the energy barrier for direct –OH abstraction along the interdimer direction. Collect all results in a CSV file with columns `step`, `molecule`, `energy_value`, `energy_type` as specified in the output contract. The verifier will check that the relative ordering among the computed barriers is consistent with the structural relationships defined in the output contract and that the adsorption energy is positive and falls within an expected range.

## Assets

- Open-source DFT package (e.g., Quantum ESPRESSO or CP2K): https://www.quantum-espresso.org or https://www.cp2k.org
- PBE functional and Grimme D2 dispersion correction

## Workflow steps

### Step 1: Build and optimize the Si(100)-(2×1) slab with zigzag OH/H termination and a dangling bond
- Role: process
- Action: Construct a periodic 6-layer Si(100) slab with (2×1) reconstruction and two dimer rows. Terminate the surface with –OH and –H groups in a zigzag pattern. Create a surface dangling bond by removing one H atom. Relax all atomic coordinates (except fixed bottom layers) using DFT with PBE functional and Grimme D2 dispersion correction until forces converge.
- Evidence: `/app/outputs/slab_structure.xyz`

### Step 2: Compute adsorption energy and H-abstraction/OH-abstraction barriers for styrene
- Role: scored (load-bearing)
- Action: Using the optimized slab, perform DFT (PBE+D2) to: (a) relax styrene approaching the dangling bond and record the adsorption energy (positive released energy); (b) locate transition states for H-abstraction from a surface –OH group along intradimer (r1), interdimer (r2), and cross-dimer-row (r3) directions; (c) locate the transition state for direct –OH abstraction along interdimer direction. Report all energies in a CSV file.
- Output file: `/app/outputs/barriers.csv`
- Format: csv
- Contract: CSV with columns: step (text: 'adsorption', 'r1_Habstraction', 'r2_Habstraction', 'r3_Habstraction', 'r2_OHabstraction'), molecule (text: always 'styrene'), energy_value (float, in eV), energy_type (text: 'adsorption' or 'barrier').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### barriers.csv
- path: `/app/outputs/barriers.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Activation barriers and adsorption energy for styrene on water-saturated Si(100)-(2×1) zigzag surface. Contains only the five required rows: adsorption, r1_Habstraction, r2_Habstraction, r3_Habstraction, r2_OHabstraction.
- schema:
  - `type`: table
  - `required_columns`: `step`, `molecule`, `energy_value`, `energy_type`
  - `units`:
    - `energy_value`: eV

Notes: The checker verifies relative ordering: r2_Habstraction < r1_Habstraction, r2_Habstraction < r3_Habstraction, r2_Habstraction < r2_OHabstraction, and checks that the adsorption energy is positive and in the range [0.8, 1.2] eV. No O‑adatom rows or checks are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "step",
          "molecule",
          "energy_value",
          "energy_type"
        ],
        "units": {
          "energy_value": "eV"
        }
      },
      "description": "Activation barriers and adsorption energy for styrene on water-saturated Si(100)-(2×1) zigzag surface. Contains only the five required rows: adsorption, r1_Habstraction, r2_Habstraction, r3_Habstraction, r2_OHabstraction."
    }
  ],
  "notes": "The checker verifies relative ordering: r2_Habstraction < r1_Habstraction, r2_Habstraction < r3_Habstraction, r2_Habstraction < r2_OHabstraction, and checks that the adsorption energy is positive and in the range [0.8, 1.2] eV. No O‑adatom rows or checks are required."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/barriers.csv` and performs a structural audit. It checks the following inequalities: (i) the interdimer H-abstraction barrier is lower than the intradimer H-abstraction barrier, (ii) the interdimer H-abstraction barrier is lower than the cross-dimer-row H-abstraction barrier, (iii) the interdimer H-abstraction barrier is lower than the interdimer OH-abstraction barrier, and (iv) the adsorption energy is positive and lies within a pre-defined plausible interval. All checks are combined into a single reward: 1.0 if all relationships hold and the adsorption energy is in range, 0.0 otherwise. No absolute barrier values are compared against any reference; only the relative orderings and the sign of the adsorption energy matter. Reporting the paper's numbers is not sufficient—you must genuinely compute the quantities.
