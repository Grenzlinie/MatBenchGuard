# DFT Activation Barriers for Methane-to-Methanol on Pd‑CeO₂ and Pd‑iC‑CeO₂ Catalysts

## Problem background
Direct conversion of methane to methanol in the liquid phase is hindered by overoxidation to CO₂ and other byproducts. This catalytic reaction typically involves the activation of both methane and hydrogen peroxide over metal/oxide interfaces. The present work explores a Pd‑CeO₂ catalyst with an interfacial carbon (iC) layer and uses density functional theory to investigate the reaction mechanism. The computational question is the size of the activation barriers for methane activation and for methanol formation via a solvated Eley–Rideal‑like pathway on the two types of catalyst surfaces: the plain Pd‑CeO₂ interface and the carbon‑modified Pd‑iC‑CeO₂ interface. The calculated barriers are expected to reveal which elementary steps control the kinetics and how the iC layer modifies the energy landscape.

## Approach
Density functional theory calculations are performed using slab models of a rhombohedral Pd₄ cluster adsorbed on a CeO₂(111) surface, with and without four interfacial C–H species inserted between the metal and the oxide (representing the iC layer). The functional is PBE+U (U=4.5 eV on Ce 4f) with D3 dispersion corrections. Transition states are located with the climbing‑image nudged elastic band method. The workflow consists of: building and optimizing both surface models; computing the activation energy for the first C–H bond cleavage in adsorbed CH₄ on each surface; adsorbing H₂O₂ and decomposing it to adsorbed OH groups; and finally, setting up the Eley–Rideal initial states where CH₃*, H*, and OH* are co‑adsorbed, with an explicit 8H₂O·2OH(aq) complex to represent solvated peroxide, and then finding the transition states for the formation of CH₂OH and CH₃OH on both Pd‑CeO₂ and Pd‑iC‑CeO₂. All calculations are to be carried out with an open‑source DFT code such as CP2K or Quantum ESPRESSO, using consistent computational parameters.

## Reproduction target
Your task: use an open‑source DFT code to execute the workflow described in the steps above, and write the results to the following scored output files in the /app/outputs directory:
- `ch4_barriers.json`: activation energies (eV) for CH₄ dissociation on Pd‑CeO₂ and on Pd‑iC‑CeO₂.
- `er_barriers.json`: activation barriers (eV) for CH₂OH formation and CH₃OH formation on both catalysts, following the Eley–Rideal pathway with the solvated peroxide complex.

Each file must conform to the JSON schema specified in the Output contract. No other file is scored, but intermediate evidence files (`model_energies.json`, `oh_structures.xyz`) may be required by the workflow and should also be placed in `/app/outputs`.

## Assets

- CP2K (open‑source DFT code, recommended): https://www.cp2k.org/
- Quantum ESPRESSO (alternative open‑source DFT code): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Build and optimize surface models
- Role: process
- Action: Construct the two slab models: Pd‑CeO₂ (rhombohedral Pd₄ cluster on CeO₂(111)) and Pd‑iC‑CeO₂ (four C–H species inserted at the interface). Optimize geometries with DFT (PBE+U, D3 dispersion) until forces converge. Ensure the correct Ce³⁺ reduction pattern (one Ce³⁺ in Pd‑CeO₂, five Ce³⁺ in Pd‑iC‑CeO₂).
- Evidence: `/app/outputs/model_energies.json`

### Step 2: CH₄ activation barrier calculation
- Role: scored (load-bearing)
- Action: Adsorb CH₄ on both optimized surfaces, then locate the transition state for the first C–H bond breaking (CH₄* → CH₃* + H*) using the climbing‑image nudged elastic band (CI‑NEB) method. Compute the activation energy E_act = E(TS) − E(initial state).
- Output file: `/app/outputs/ch4_barriers.json`
- Format: json
- Contract: [ {"system": "Pd-CeO2"|"Pd-iC-CeO2", "step": "CH4_activation", "activation_energy_eV": <float> } ]
- Scoring: scored by hidden verifier

### Step 3: H₂O₂ adsorption and decomposition to OH*
- Role: process
- Action: Adsorb H₂O₂ on both surfaces and decompose it to 2OH* species. Record the relaxed co‑adsorbed OH structures for use in the Eley–Rideal mechanism.
- Evidence: `/app/outputs/oh_structures.xyz`

### Step 4: Eley–Rideal‑like pathway barriers for methanol formation
- Role: scored (load-bearing)
- Action: Set up the initial states with co‑adsorbed CH₃*, H*, and OH* species on each catalyst. Introduce an explicit 8H₂O·2OH(aq) complex to model solvated H₂O₂. Use CI‑NEB to determine the reaction paths for (i) formation of CH₂OH* and (ii) formation of CH₃OH(aq) on Pd‑CeO₂ and Pd‑iC‑CeO₂. Report the activation barriers.
- Output file: `/app/outputs/er_barriers.json`
- Format: json
- Contract: [ {"system": "Pd-CeO2"|"Pd-iC-CeO2", "step": "CH2OH_formation"|"CH3OH_formation", "activation_energy_eV": <float> } ]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ch4_barriers.json`
- `/app/outputs/er_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ch4_barriers.json
- path: `/app/outputs/ch4_barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Activation energies for the first C–H bond breaking in CH₄ on Pd‑CeO₂ and Pd‑iC‑CeO₂, computed by CI‑NEB.
- schema:
  - `type`: array
  - `items`:
    - `system`: string
    - `step`: string (value: 'CH4_activation')
    - `activation_energy_eV`: float
  - `required`: `system`, `step`, `activation_energy_eV`

### er_barriers.json
- path: `/app/outputs/er_barriers.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Activation barriers for CH₂OH and CH₃OH formation via the Eley–Rideal‑like pathway with an explicit 8H₂O·2OH(aq) complex, on both catalysts.
- schema:
  - `type`: array
  - `items`:
    - `system`: string (values: 'Pd-CeO2' or 'Pd-iC-CeO2')
    - `step`: string (values: 'CH2OH_formation' or 'CH3OH_formation')
    - `activation_energy_eV`: float
  - `required`: `system`, `step`, `activation_energy_eV`

Notes: The target_policy 'threshold_or_better' means the checker compares each reported activation_energy_eV to a hidden reference value; meeting or beating the reference (lower barrier) earns full credit, subject to tolerances. Additionally the relative ordering of barriers between the two catalysts is enforced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ch4_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "system": "string",
          "step": "string (value: 'CH4_activation')",
          "activation_energy_eV": "float"
        },
        "required": [
          "system",
          "step",
          "activation_energy_eV"
        ]
      },
      "description": "Activation energies for the first C–H bond breaking in CH₄ on Pd‑CeO₂ and Pd‑iC‑CeO₂, computed by CI‑NEB."
    },
    {
      "file": "er_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "array",
        "items": {
          "system": "string (values: 'Pd-CeO2' or 'Pd-iC-CeO2')",
          "step": "string (values: 'CH2OH_formation' or 'CH3OH_formation')",
          "activation_energy_eV": "float"
        },
        "required": [
          "system",
          "step",
          "activation_energy_eV"
        ]
      },
      "description": "Activation barriers for CH₂OH and CH₃OH formation via the Eley–Rideal‑like pathway with an explicit 8H₂O·2OH(aq) complex, on both catalysts."
    }
  ],
  "notes": "The target_policy 'threshold_or_better' means the checker compares each reported activation_energy_eV to a hidden reference value; meeting or beating the reference (lower barrier) earns full credit, subject to tolerances. Additionally the relative ordering of barriers between the two catalysts is enforced."
}
```

## How you are scored
A hidden verifier will score each of the two scored artifacts independently. For each activation energy you report, the verifier compares the value against a reference set (derived from the paper’s own DFT calculations) using an undisclosed tolerance. The verifier also checks whether the relative ordering of the barriers between the two catalysts follows a prescribed trend. The individual checks are combined into a weighted final score between 0 (no credit) and 1 (full credit). Providing numbers without genuinely performing the DFT workflow will not match the hidden reference and will yield a low score. The specific reference values and tolerances are not revealed in the task instructions.
