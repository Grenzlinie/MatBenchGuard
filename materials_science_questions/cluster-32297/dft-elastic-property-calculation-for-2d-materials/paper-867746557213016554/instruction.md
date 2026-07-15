# Strain-tuned nanoporous CN membrane for He separation: DFT energy barriers and selectivity

## Problem background
Helium is a critical resource in scientific and industrial applications, but its low natural abundance and tendency to escape into the atmosphere make efficient purification methods essential. Membrane-based separation using ultrathin two‑dimensional materials offers a promising route. The key challenge is designing a membrane with pore sizes that discriminate between helium (He) and larger noble gases like neon (Ne) and argon (Ar). A porous graphitic carbon nitride (CN) monolayer, when subjected to a biaxial compressive strain of -6%, has been proposed as a candidate for highly selective He filtration. The problem is to verify whether this strain-tuned pore indeed yields low permeation barriers for He and high barriers for Ne and Ar, thereby enabling exceptional He selectivity.

## Approach
This reproduction employs density functional theory (DFT) with the climbing-image nudged elastic band (CI-NEB) method to compute the energy barrier for each noble gas atom (He, Ne, Ar) moving through a CN monolayer under -6% biaxial compressive strain. The CN monolayer is modeled as a 2×2 supercell with a lattice parameter of 7.12 Å, and the compressive strain of -6% is applied uniformly in both lateral directions. For each gas, initial (adsorbed) and final (pore-center) configurations are used to define the minimum-energy path, and CI-NEB determines the transition state and the associated energy barrier. From the computed barriers, the selectivity for He over Ne and He over Ar at 300 K is calculated using the Arrhenius equation with a diffusion prefactor of 10¹¹ s⁻¹. The workflow produces a single scored artifact containing the three energy barriers and the two selectivities.

## Reproduction target
Compute the energy barriers (in eV) for He, Ne, and Ar atoms permeating through a CN monolayer under -6% biaxial compressive strain using DFT CI-NEB. Then, using the obtained barriers, calculate the selectivities S(He/Ne) and S(He/Ar) at 300 K via the Arrhenius equation S = exp[-(E_He − E_gas)/(k_B T)] (with equal prefactors for all gases), where k_B is Boltzmann's constant. Produce a single JSON file, results.json, containing the three barriers and the two selectivities. All numerical parameters necessary for the calculation (lattice parameter, atomic positions, strain magnitude, temperature, prefactor) are specified in the workflow steps.

## Assets

- Open-source DFT code with CI-NEB support (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Build strained CN monolayer and prepare NEB input
- Role: process
- Action: Construct the CN monolayer 2×2 supercell (lattice parameter 7.12 Å, C–C 1.51 Å, C–N 1.34 Å) and apply a biaxial compressive strain of -6%. Define initial (adsorbed) and final (pore-centre) configurations for He, Ne and Ar permeation. Create all necessary DFT input files for CI-NEB calculations.
- Evidence: `/app/outputs/cn_strained_neb_inputs.xyz`

### Step 2: DFT energy barriers and He selectivity
- Role: scored (load-bearing)
- Action: Perform DFT CI-NEB transition-state search for He, Ne, and Ar permeation through the strained CN membrane to obtain the energy barrier Eb (eV) for each gas. Using the computed barriers, calculate the He/Ne and He/Ar selectivities at 300 K with the Arrhenius equation S = (A_He/A_gas) exp[-(E_He – E_gas)/(k_B T)], where the diffusion prefactor A = 10^11 s⁻¹. Write the three barriers and two selectivities to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "energy_barriers": {
    "He": <barrier_in_eV>,
    "Ne": <barrier_in_eV>,
    "Ar": <barrier_in_eV>
  },
  "selectivities": {
    "He_Ne": <value>,
    "He_Ar": <value>
  }
}
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
- description: Contains the DFT-computed energy barriers and derived selectivities; the hidden checker compares barrier values to paper-reported references with absolute tolerance, compares selectivities with logarithmic tolerance, and verifies that selectivities are consistent with the submitted barriers via the Arrhenius equation.
- schema:
  - `type`: object
  - `required`: `energy_barriers`, `selectivities`
  - `properties`:
    - `energy_barriers`:
      - `type`: object
      - `required`: `He`, `Ne`, `Ar`
      - `additionalProperties`: False
      - `properties`:
        - `He`:
          - `type`: number
          - `description`: Energy barrier for He permeation (eV)
        - `Ne`:
          - `type`: number
          - `description`: Energy barrier for Ne permeation (eV)
        - `Ar`:
          - `type`: number
          - `description`: Energy barrier for Ar permeation (eV)
    - `selectivities`:
      - `type`: object
      - `required`: `He_Ne`, `He_Ar`
      - `additionalProperties`: False
      - `properties`:
        - `He_Ne`:
          - `type`: number
          - `description`: Selectivity for He over Ne at 300 K
        - `He_Ar`:
          - `type`: number
          - `description`: Selectivity for He over Ar at 300 K
  - `additionalProperties`: False

Notes: The MD permeance part is omitted because it depends on the proprietary COMPASS force field. Only the DFT barriers and selectivities are scored. The agent must install an open-source DFT code (e.g., Quantum ESPRESSO) and appropriate pseudopotentials.

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
          "energy_barriers",
          "selectivities"
        ],
        "properties": {
          "energy_barriers": {
            "type": "object",
            "required": [
              "He",
              "Ne",
              "Ar"
            ],
            "additionalProperties": false,
            "properties": {
              "He": {
                "type": "number",
                "description": "Energy barrier for He permeation (eV)"
              },
              "Ne": {
                "type": "number",
                "description": "Energy barrier for Ne permeation (eV)"
              },
              "Ar": {
                "type": "number",
                "description": "Energy barrier for Ar permeation (eV)"
              }
            }
          },
          "selectivities": {
            "type": "object",
            "required": [
              "He_Ne",
              "He_Ar"
            ],
            "additionalProperties": false,
            "properties": {
              "He_Ne": {
                "type": "number",
                "description": "Selectivity for He over Ne at 300 K"
              },
              "He_Ar": {
                "type": "number",
                "description": "Selectivity for He over Ar at 300 K"
              }
            }
          }
        },
        "additionalProperties": false
      },
      "description": "Contains the DFT-computed energy barriers and derived selectivities; the hidden checker compares barrier values to paper-reported references with absolute tolerance, compares selectivities with logarithmic tolerance, and verifies that selectivities are consistent with the submitted barriers via the Arrhenius equation."
    }
  ],
  "notes": "The MD permeance part is omitted because it depends on the proprietary COMPASS force field. Only the DFT barriers and selectivities are scored. The agent must install an open-source DFT code (e.g., Quantum ESPRESSO) and appropriate pseudopotentials."
}
```

## How you are scored
A hidden verifier independently evaluates your submitted results.json. It compares your computed energy barriers and selectivities against reference values derived from the original study's DFT calculations, using appropriate tolerances that account for differences in implementation details while still requiring meaningful reproduction of the key results. It also checks that your reported selectivities are internally consistent with the barriers you report by recalculating them via the Arrhenius equation. Simply quoting values from the original paper will not satisfy the scoring criteria; the scores require that the numbers in results.json be the output of your own DFT-based workflow.
