# DFT Barrier Lowering for CO Dimerization on Cu(100) by Hydroxide

## Problem background
Efficient electrochemical conversion of CO₂ into valuable fuels and feedstocks such as ethylene is a key step toward carbon-neutral fuel cycles. The formation of ethylene on copper catalysts involves the coupling of adsorbed CO molecules (CO dimerization), which is often reported as the rate‑determining step. Recent experimental studies have shown that operating in highly alkaline electrolytes significantly lowers the overpotential for ethylene production, and density functional theory (DFT) calculations suggest that adsorbed hydroxide ions on the Cu surface lower the activation energy barrier for CO dimerization. Understanding the magnitude of this catalytic effect is crucial for designing improved catalysts and reaction conditions. This task reproduces the DFT‑computed activation energy barrier for CO dimerization on a Cu(100) surface and quantifies the barrier lowering induced by adsorbed hydroxide.

## Approach
Periodic DFT calculations are performed using a plane‑wave code and the PBE functional. The Cu(100) surface is modeled by a 4‑layer p(2×2) slab, with the bottom two layers frozen, and an explicit water bilayer (4 H₂O molecules) is added above the surface. Two conditions are compared: a clean Cu(100) surface and a Cu(100) surface where two H₂O molecules are replaced by two OH groups, giving a coverage of 2 OH per 16 surface Cu atoms. For each surface, the activation energy barrier for the reaction 2*CO → OCCO is determined using the nudged elastic band (NEB) method. The barrier lowering is then calculated as the difference between the clean‑surface barrier and the OH‑covered‑surface barrier. The results are reported in electron‑volts and milli‑electron‑volts.

## Reproduction target
Perform DFT NEB calculations for CO dimerization (2 adsorbed CO → OCCO) on a clean Cu(100) slab and on a Cu(100) slab with 2/16 monolayer OH coverage, both in the presence of an explicit water bilayer. Extract the activation energy barriers in eV for each case, then compute the barrier lowering (clean barrier minus OH‑covered barrier) in meV. Write the results to `/app/outputs/dft_barrier_lowering.json` containing three numeric fields: `clean_barrier_eV`, `OH_barrier_eV`, and `barrier_lowering_meV`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- ONCVPSP pseudopotentials: https://www.pseudo-dojo.org
- Cu crystal structure

## Workflow steps

### Step 1: Prepare Cu(100) slab and DFT inputs
- Role: process
- Action: Generate a 4-layer p(2×2) Cu(100) slab model, fix bottom two layers, add an explicit water bilayer (4 H₂O molecules) and prepare Quantum ESPRESSO input files for NEB calculations on the clean surface and on the OH-covered surface (replace 2 H₂O with 2 OH to achieve 2/16 ML OH coverage).
- Evidence: `/app/outputs/input_preparation.log`

### Step 2: Compute CO dimerization barriers and report lowering
- Role: scored (load-bearing)
- Action: Perform DFT NEB calculations to determine the activation energy barrier for 2*CO → OCCO on (i) clean Cu(100) and (ii) Cu(100) with 2/16 ML OH coverage. Extract the clean barrier, OH‑covered barrier, and the barrier lowering (clean minus OH‑covered) in meV. Write the results to dft_barrier_lowering.json.
- Output file: `/app/outputs/dft_barrier_lowering.json`
- Format: json
- Contract: {"clean_barrier_eV": "float", "OH_barrier_eV": "float", "barrier_lowering_meV": "float"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_barrier_lowering.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_barrier_lowering.json
- path: `/app/outputs/dft_barrier_lowering.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Contains the computed activation energy barriers for CO dimerization on clean Cu(100) and on Cu(100) with 2/16 ML OH coverage, and the resulting barrier lowering in meV.
- schema:
  - `type`: object
  - `required`:
    - `clean_barrier_eV`: float
    - `OH_barrier_eV`: float
    - `barrier_lowering_meV`: float

Notes: The barrier lowering is the difference clean_barrier - OH_barrier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_barrier_lowering.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "clean_barrier_eV": "float",
          "OH_barrier_eV": "float",
          "barrier_lowering_meV": "float"
        }
      },
      "description": "Contains the computed activation energy barriers for CO dimerization on clean Cu(100) and on Cu(100) with 2/16 ML OH coverage, and the resulting barrier lowering in meV."
    }
  ],
  "notes": "The barrier lowering is the difference clean_barrier - OH_barrier."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/dft_barrier_lowering.json`. It extracts the `barrier_lowering_meV` value and compares it to a reference value derived from published computational work, with an appropriate tolerance that accounts for variations in pseudopotentials, numerical convergence, and DFT implementation details. The verifier awards a score between 0 and 1 based on how close your computed lowering is to the reference; a result within the tolerance earns full credit. No other outputs contribute to the score. Performing the full DFT NEB calculation is required—reporting a number without the calculation will not yield a correct result.
