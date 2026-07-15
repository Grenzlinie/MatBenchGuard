# DFT Free Energy Diagram for CO2 Reduction on Zn and ZnCu Surfaces

## Problem background
Electrochemical CO₂ reduction to CO is a promising strategy for carbon-neutral fuel production. Earth-abundant Zn-based catalysts are attractive alternatives to precious metals, but their intrinsic activity for CO generation is limited. Computational studies suggest that alloying Zn with a small amount of Cu may alter the binding of key reaction intermediates. This task requires you to compute the free energy diagram for CO₂ reduction to CO on Zn(100) and Cu-doped Zn(100) surfaces and to determine the effect of Cu on the reaction energetics, specifically whether alloying changes the energy landscape for the *COOH → *CO step.

## Approach
You will construct slab models for the Zn(100) surface and a Cu-doped Zn(100) surface (one surface Zn replaced by Cu). Using an open‑source DFT code with the GGA-PBE functional and DFT-D3 dispersion correction, you will optimize the geometries and then compute total energies of the clean slabs, adsorbed *COOH and *CO intermediates, and gas‑phase molecules (CO₂, H₂O, H₂). Zero‑point energy and entropy corrections are applied to obtain free energies. The computational hydrogen electrode model at 0 V vs. RHE is used to reference all energies to gas‑phase CO₂ and the clean slab. By comparing the free energy profiles of the two surfaces, you will assess how Cu doping influences the reaction steps.

## Reproduction target
Produce a machine‑readable JSON file containing the free energy diagram for CO₂ reduction to CO on both Zn(100) and Cu‑doped Zn(100) surfaces. For each surface, list the relative free energies (in eV) of the intermediates *COOH, *CO, and the final state CO(g) + clean surface, all referenced to gas‑phase CO₂ and the clean slab at 0 V vs. RHE. The energy for the initial CO₂(g) state is defined as 0.0 eV. The output must follow the exact schema defined in the output contract.

## Assets

- Zn hcp crystal structure (a=2.665 Å, c=4.947 Å, P63/mmc)
- Open-source DFT code (e.g., Quantum ESPRESSO, GPAW, CP2K) with GGA-PBE and DFT-D3 correction: https://www.quantum-espresso.org/
- Standard pseudopotentials (e.g., QE SSSP or PSLibrary): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Build and optimize slab models
- Role: process
- Action: Construct the Zn(100) surface slab from bulk hcp Zn (2x2 supercell, 20 atoms, 15 Å vacuum). Substitute one surface Zn atom with Cu to create the Cu-doped slab. Optimize the geometry of both slabs using DFT (GGA-PBE, D3 dispersion correction).
- Evidence: `/app/outputs/slab_optimization_evidence.json`

### Step 2: Compute DFT energies of reaction intermediates
- Role: process
- Action: For each slab (Zn and Cu-doped), compute total energies of the clean surface and of adsorbed *COOH and *CO intermediates at optimized geometries. Also compute gas-phase energies of CO2, H2O, and H2. Use the same DFT settings (PBE+D3). Apply zero-point energy (ZPE) and entropy corrections as appropriate for free energy calculations.
- Evidence: `/app/outputs/raw_energies.json`

### Step 3: Generate free energy diagram
- Role: scored (load-bearing)
- Action: From the calculated energies, compute the relative free energies of each intermediate state with respect to gas-phase CO2 and the clean slab (computational hydrogen electrode model at 0 V vs RHE). For both Zn(100) and Cu-doped Zn(100), list the free energies of *COOH, *CO, and the final CO(g) + clean surface. Write the results to free_energy_diagram.json.
- Output file: `/app/outputs/free_energy_diagram.json`
- Format: json
- Contract: An array of two objects. Each object has a 'system' key (string, one of 'Zn(100)' or 'CuZn(100)') and a 'steps' key (array of objects). Each step object has 'label' (one of 'CO2(g)', '*COOH', '*CO', 'CO(g)+*') and 'energy_eV' (float). The energy for 'CO2(g)' is defined as 0.0 eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_diagram.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_diagram.json
- path: `/app/outputs/free_energy_diagram.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Free energy diagram for CO2 reduction to CO. The checker recomputes adsorption energies and energy barriers from this data, compares them to paper reference values within tolerances, and checks that the barrier on CuZn(100) is lower than on Zn(100).
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `system`:
        - `type`: string
        - `enum`: `Zn(100)`, `CuZn(100)`
      - `steps`:
        - `type`: array
        - `items`:
          - `type`: object
          - `properties`:
            - `label`:
              - `type`: string
              - `enum`: `CO2(g)`, `*COOH`, `*CO`, `CO(g)+*`
            - `energy_eV`:
              - `type`: number
          - `required`: `label`, `energy_eV`
    - `required`: `system`, `steps`

Notes: The DFT workflow steps (slab optimization, intermediate energy calculations) must be executed before generating this file. The solver must use an open-source DFT code (e.g., Quantum ESPRESSO, GPAW, CP2K) with GGA-PBE functional and D3 dispersion correction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_diagram.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "system": {
              "type": "string",
              "enum": [
                "Zn(100)",
                "CuZn(100)"
              ]
            },
            "steps": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "label": {
                    "type": "string",
                    "enum": [
                      "CO2(g)",
                      "*COOH",
                      "*CO",
                      "CO(g)+*"
                    ]
                  },
                  "energy_eV": {
                    "type": "number"
                  }
                },
                "required": [
                  "label",
                  "energy_eV"
                ]
              }
            }
          },
          "required": [
            "system",
            "steps"
          ]
        }
      },
      "description": "Free energy diagram for CO2 reduction to CO. The checker recomputes adsorption energies and energy barriers from this data, compares them to paper reference values within tolerances, and checks that the barrier on CuZn(100) is lower than on Zn(100)."
    }
  ],
  "notes": "The DFT workflow steps (slab optimization, intermediate energy calculations) must be executed before generating this file. The solver must use an open-source DFT code (e.g., Quantum ESPRESSO, GPAW, CP2K) with GGA-PBE functional and D3 dispersion correction."
}
```

## How you are scored
A hidden verifier will read your `free_energy_diagram.json` and independently compute the adsorption energy of *COOH (energy of *COOH relative to CO₂(g)) and the energy change for *COOH → *CO from your reported numbers. It will compare these quantities for the Zn(100) and CuZn(100) surfaces against a hidden reference and will also check whether the relationship between the two surfaces (e.g., which surface shows a lower barrier) matches an expected ordering. Both the absolute energies and the trend contribute to the final reward. Simply reporting plausible numbers without correctly executing the DFT workflow will not yield a high score.
