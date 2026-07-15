# DFT Calculation of Oxygen Vacancy Defect Levels in GeO₂

## Problem background
Germanium dioxide (GeO₂) is a promising passivation layer for germanium metal-oxide-semiconductor field-effect transistors (MOSFETs). Oxygen vacancies (V_O) in the oxide can introduce defect states that act as fixed positive charges or carrier traps, degrading device performance. Understanding the formation energies and charge-state transition levels of these vacancies is essential to predict their electronic role in the dielectric. First-principles density-functional-theory (DFT) calculations can determine these quantities, providing insight into whether the vacancy introduces fixed charge or serves as a trap center.

## Approach
We use a plane-wave DFT approach with a hybrid functional (PBE0) to study the oxygen vacancy in GeO₂. The structure is modelled by a 72-atom supercell of α-quartz GeO₂, rescaled to match the density of amorphous GeO₂ (3.6 g/cm³). The workflow proceeds by:

- Building the rescaled supercell.
- Performing a full geometry relaxation of the perfect supercell.
- Creating an oxygen vacancy and relaxing the defective supercell in charge states 0, +1, and +2.
- Carrying out a reference calculation on an isolated O₂ molecule to obtain the oxygen chemical potential.
- From the total energies, computing formation energies as a function of the Fermi level using the standard defect formation energy formula (involving the oxygen chemical potential and the valence-band maximum of the neutral defect cell).
- Determining the thermodynamic (+2/0) transition level and aligning the GeO₂ energy scale to Ge using literature valence-band offsets (VBOs in the range 3.6–4.5 eV) to decide whether this transition lies above the Ge conduction band minimum.
- Computing the (+1/0) charge-state switching level from a single-point calculation of the +1 charge state using the relaxed neutral (q=0) atomic geometry.

All DFT calculations use the open-source Quantum ESPRESSO package. The final results are collected in a JSON file.

## Reproduction target
Produce a JSON file, `/app/outputs/results.json`, containing:

- `total_energies`: an object with four floating-point energies (in eV) for the perfect supercell and for the vacancy in charge states 0, +1, and +2, labelled `perfect`, `V0`, `V+1`, `V+2`.
- `thermodynamic_transition_+2_0_above_Ge_CBM`: a boolean indicating whether, after energy alignment with the given VBO range, the thermodynamic (+2/0) transition level lies above the Ge conduction band minimum.
- `charge_switching_level_+1_0`: a floating-point number (in eV) representing the (+1/0) charge-state switching level referenced to the GeO₂ valence-band maximum.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ge and O pseudopotentials: https://www.quantum-espresso.org/pseudopotentials
- pymatgen: pymatgen

## Workflow steps

### Step 1: Build rescaled α-quartz GeO₂ supercell
- Role: process
- Action: Construct a 72-atom supercell of α-quartz GeO₂ with lattice parameters rescaled to match the density of amorphous GeO₂ (3.6 g/cm³).
- Evidence: `/app/outputs/supercell.cif`

### Step 2: DFT relaxation of perfect supercell
- Role: process
- Action: Perform DFT geometry optimization on the perfect 72-atom GeO₂ supercell using a hybrid functional (PBE0), relaxing all atomic positions. Record the total energy and the valence-band maximum (VBM).
- Evidence: `/app/outputs/perfect_relax.log`

### Step 3: Oxygen vacancy defect relaxations
- Role: process
- Action: Remove one oxygen atom from the relaxed perfect supercell to create an oxygen vacancy. Perform DFT relaxations for charge states q = 0, +1, +2, recording total energies. Additionally, perform a single-point DFT calculation for the +1 charge state using the relaxed neutral (q=0) atomic geometry.
- Evidence: `/app/outputs/defect_relax.log`

### Step 4: O₂ molecule reference calculation
- Role: process
- Action: Compute the total energy of an isolated O₂ molecule using the same DFT parameters to obtain the oxygen chemical potential μ_O = 0.5 E_tot(O₂).
- Evidence: `/app/outputs/o2_calc.log`

### Step 5: Compute defect formation energies, transition levels, and alignment
- Role: scored (load-bearing)
- Action: Using the total energies from the previous steps and the VBM from the neutral defect cell, compute formation energies for each charge state as a function of the Fermi level using the standard formation-energy formula. Determine the thermodynamic (+2/0) transition level and whether it lies above the Ge conduction band minimum after aligning the GeO₂ energy scale to Ge using literature valence-band offsets (VBO 3.6–4.5 eV). Compute the (+1/0) charge-state switching level (eV above GeO₂ VBM) using the fixed neutral geometry. Write all results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: total_energies (object with keys perfect, V0, V+1, V+2 each float eV), thermodynamic_transition_+2_0_above_Ge_CBM (boolean), charge_switching_level_+1_0 (float eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Consolidated DFT results: total energies of perfect and defective supercells, the (+2/0) thermodynamic transition verdict relative to Ge CBM, and the (+1/0) charge-state switching level referenced to the GeO₂ VBM.
- schema:
  - `type`: object
  - `required`: `total_energies`, `thermodynamic_transition_+2_0_above_Ge_CBM`, `charge_switching_level_+1_0`
  - `properties`:
    - `total_energies`:
      - `type`: object
      - `required`: `perfect`, `V0`, `V+1`, `V+2`
      - `properties`:
        - `perfect`:
          - `type`: number
          - `unit`: eV
        - `V0`:
          - `type`: number
          - `unit`: eV
        - `V+1`:
          - `type`: number
          - `unit`: eV
        - `V+2`:
          - `type`: number
          - `unit`: eV
    - `thermodynamic_transition_+2_0_above_Ge_CBM`:
      - `type`: boolean
    - `charge_switching_level_+1_0`:
      - `type`: number
      - `unit`: eV

Notes: The agent must use an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and available pseudopotentials. The alignment to Ge bands relies on literature VBO values; the agent may choose an appropriate value within the 3.6–4.5 eV range.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "total_energies",
          "thermodynamic_transition_+2_0_above_Ge_CBM",
          "charge_switching_level_+1_0"
        ],
        "properties": {
          "total_energies": {
            "type": "object",
            "required": [
              "perfect",
              "V0",
              "V+1",
              "V+2"
            ],
            "properties": {
              "perfect": {
                "type": "number",
                "unit": "eV"
              },
              "V0": {
                "type": "number",
                "unit": "eV"
              },
              "V+1": {
                "type": "number",
                "unit": "eV"
              },
              "V+2": {
                "type": "number",
                "unit": "eV"
              }
            }
          },
          "thermodynamic_transition_+2_0_above_Ge_CBM": {
            "type": "boolean"
          },
          "charge_switching_level_+1_0": {
            "type": "number",
            "unit": "eV"
          }
        }
      },
      "description": "Consolidated DFT results: total energies of perfect and defective supercells, the (+2/0) thermodynamic transition verdict relative to Ge CBM, and the (+1/0) charge-state switching level referenced to the GeO₂ VBM."
    }
  ],
  "notes": "The agent must use an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) and available pseudopotentials. The alignment to Ge bands relies on literature VBO values; the agent may choose an appropriate value within the 3.6–4.5 eV range."
}
```

## How you are scored
Your submission is scored by a hidden verifier. It reads `/app/outputs/results.json` and evaluates:

- The `charge_switching_level_+1_0` value is compared to the expected target (with an appropriate tolerance).
- The `thermodynamic_transition_+2_0_above_Ge_CBM` boolean is checked for correctness (it must be consistent with the actual computed transition relative to the Ge CBM).
- The `total_energies` are subjected to a basic sanity check (e.g., negativity and physically reasonable ordering by charge state).

Each of these components contributes to a final weighted score between 0 and 1. A correct reproduction of the key material property (the switching level and the transition conclusion) earns full credit; only reporting the paper’s numbers without actually performing the calculation will not suffice.
