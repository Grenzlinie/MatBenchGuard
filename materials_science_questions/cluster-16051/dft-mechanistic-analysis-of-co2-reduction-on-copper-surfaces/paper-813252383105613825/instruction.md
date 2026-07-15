# DFT Kinetic Analysis of CO2 Reduction Selectivity on Copper Surfaces

## Problem background
Electrochemical CO2 reduction on copper electrodes can produce methane, ethylene, and methanol, but the mechanism that controls selectivity among these products is not fully understood. While earlier DFT free-energy studies suggested a pathway through a CHO intermediate, recent experiments indicate that formaldehyde reduction yields methanol rather than methane, and that methane and ethylene may share a common potential-limiting step on Cu(111). This task investigates the kinetic branching at the key reduction steps—reduction of CO and reduction of the methoxy (CH3O) intermediate—by computing activation barriers under operational electrochemical conditions. The goal is to determine, from first-principles kinetics, which reaction path dominates and to quantify the resulting selectivity toward methanol or methane.

## Approach
Construct a Cu(111) surface slab model with two explicit water molecules to capture solvation effects. Place the relevant adsorbates (CO, CH3O, and the corresponding transition states) for four elementary steps: CH3O → CH3OH, CH3O → CH4, CO → CHO, and CO → COH. Perform plane-wave DFT calculations using an open-source code. For O–H bond forming steps, use a water-assisted proton-shuttling model; for C–H bond forming steps, use direct surface hydrogenation. Compute activation barriers via climbing-image nudged elastic band (NEB) calculations. Apply a potential-dependent barrier correction to obtain effective barriers at U = -1.15 V (RHE). The correction uses the linear free energy relationship ΔG‡(U) = ΔE‡_barrier + β * ΔG_rxn(U), where ΔG_rxn(U) is the reaction free energy at potential U computed with the computational hydrogen electrode (CHE) model and β is the symmetry factor (commonly 0.5). ΔE‡_barrier is the DFT-computed activation energy from the NEB calculation at zero potential. Finally, derive methanol/methane selectivity and the kinetic preference for COH vs. CHO formation using Arrhenius expressions at 300 K.

## Reproduction target
Using an open-source plane-wave DFT code, construct a Cu(111) slab with two explicit water molecules and the necessary adsorbates. Optimize all structures, then compute activation barriers via climbing-image NEB for the four elementary steps at U = -1.15 V (RHE). Write the four barrier energies (in eV) to `/app/outputs/step_01_barriers.json`. From these barriers, compute the rate constant ratio for methanol vs. methane formation via the CHO path and the kinetic preference for COH over CHO formation, and write the results to `/app/outputs/step_02_selectivity.json`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/download
- Pseudopotential library (e.g., SSSP): https://github.com/materialsproject/pymatgen/wiki/Pseudopotential-sets
- Atomic Simulation Environment (ASE): ase
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Build and optimize initial structures
- Role: process
- Action: Construct Cu(111) surface slab with two explicit water molecules and place adsorbates (reactants/products) for the four elementary steps: CH3O to CH3OH, CH3O to CH4, CO to CHO, CO to COH. Perform DFT geometry optimizations with Quantum ESPRESSO to obtain stable structures.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: Compute activation barriers at U = -1.15 V (RHE)
- Role: scored (load-bearing)
- Action: For the four elementary steps, set up climbing-image NEB calculations using the optimized structures. Apply the water-assisted H-shuttling model for O-H bond forming steps (CH3O to CH3OH, CO to COH) and direct surface hydrogenation model for C-H bond forming steps (CH3O to CH4, CO to CHO). Apply the electrode-potential-dependent barrier correction scheme to obtain effective activation barriers at U = -1.15 V (RHE). Write the four barrier values to /app/outputs/step_01_barriers.json.
- Output file: `/app/outputs/step_01_barriers.json`
- Format: json
- Contract: {"CH3O_to_CH3OH": <float (eV)>, "CH3O_to_CH4": <float (eV)>, "CO_to_CHO": <float (eV)>, "CO_to_COH": <float (eV)>}
- Scoring: scored by hidden verifier

### Step 3: Calculate selectivity ratios
- Role: scored
- Action: Read the barriers from step_01_barriers.json. Compute the methanol/methane selectivity ratio for path I using the Arrhenius expression at 300 K: exp((E_barrier_CH4 - E_barrier_CH3OH) / (k_B * 300 K)). Compute the kinetic preference for COH over CHO formation similarly using the barrier difference. Write step_02_selectivity.json with the barrier differences and the derived selectivity factors.
- Output file: `/app/outputs/step_02_selectivity.json`
- Format: json
- Contract: {"selectivity_ratio_pathI": <float>, "barrier_difference_pathI": <float (eV)>, "selectivity_pathII_over_I": <float>, "barrier_difference_CO_reduction": <float (eV)>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_barriers.json`
- `/app/outputs/step_02_selectivity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_barriers.json
- path: `/app/outputs/step_01_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Activation barriers (eV) at U = -1.15 V (RHE) for the four selectivity-determining elementary steps plus the ethylene C2H4 formation barrier from CH2 dimerization.
- schema:
  - `type`: object
  - `required`: `CH3O_to_CH3OH`, `CH3O_to_CH4`, `CO_to_CHO`, `CO_to_COH`, `CH2_dimer_ethylene`
  - `properties`:
    - `CH3O_to_CH3OH`:
      - `type`: number
      - `unit`: eV
    - `CH3O_to_CH4`:
      - `type`: number
      - `unit`: eV
    - `CO_to_CHO`:
      - `type`: number
      - `unit`: eV
    - `CO_to_COH`:
      - `type`: number
      - `unit`: eV
    - `CH2_dimer_ethylene`:
      - `type`: number
      - `unit`: eV

### step_02_selectivity.json
- path: `/app/outputs/step_02_selectivity.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Selectivity ratios and barrier differences derived from activation barriers.
- schema:
  - `type`: object
  - `required`: `selectivity_ratio_pathI`, `barrier_difference_pathI`, `selectivity_pathII_over_I`, `barrier_difference_CO_reduction`
  - `properties`:
    - `selectivity_ratio_pathI`:
      - `type`: number
      - `unit`: 
    - `barrier_difference_pathI`:
      - `type`: number
      - `unit`: eV
    - `selectivity_pathII_over_I`:
      - `type`: number
      - `unit`: 
    - `barrier_difference_CO_reduction`:
      - `type`: number
      - `unit`: eV

Notes: All activation barriers are at U = -1.15 V (RHE). Selectivity ratios are computed at 300 K using the Arrhenius expression. The DFT code to use is Quantum ESPRESSO, but other open-source plane-wave DFT codes with equivalent accuracy are acceptable as long as the barrier values are within the hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "CH3O_to_CH3OH",
          "CH3O_to_CH4",
          "CO_to_CHO",
          "CO_to_COH",
          "CH2_dimer_ethylene"
        ],
        "properties": {
          "CH3O_to_CH3OH": {
            "type": "number",
            "unit": "eV"
          },
          "CH3O_to_CH4": {
            "type": "number",
            "unit": "eV"
          },
          "CO_to_CHO": {
            "type": "number",
            "unit": "eV"
          },
          "CO_to_COH": {
            "type": "number",
            "unit": "eV"
          },
          "CH2_dimer_ethylene": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Activation barriers (eV) at U = -1.15 V (RHE) for the four selectivity-determining elementary steps plus the ethylene C2H4 formation barrier from CH2 dimerization."
    },
    {
      "file": "step_02_selectivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "selectivity_ratio_pathI",
          "barrier_difference_pathI",
          "selectivity_pathII_over_I",
          "barrier_difference_CO_reduction"
        ],
        "properties": {
          "selectivity_ratio_pathI": {
            "type": "number",
            "unit": ""
          },
          "barrier_difference_pathI": {
            "type": "number",
            "unit": "eV"
          },
          "selectivity_pathII_over_I": {
            "type": "number",
            "unit": ""
          },
          "barrier_difference_CO_reduction": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Selectivity ratios and barrier differences derived from activation barriers."
    }
  ],
  "notes": "All activation barriers are at U = -1.15 V (RHE). Selectivity ratios are computed at 300 K using the Arrhenius expression. The DFT code to use is Quantum ESPRESSO, but other open-source plane-wave DFT codes with equivalent accuracy are acceptable as long as the barrier values are within the hidden tolerance."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file. For `step_01_barriers.json`, it checks the four activation barriers against reference values derived from the original study and verifies that the correct ordering between specific pairs is observed. For `step_02_selectivity.json`, it recomputes the selectivity ratios from the barriers you reported and compares them to expected values. Each scored stage carries a weight; the final reward is a weighted combination. Simply quoting literature values without performing the computational workflow will result in a low score.
