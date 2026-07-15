# DFT Calculated C-H Activation Barriers of n-Hexane on Copper Step Edges

## Problem background
Direct selective activation of sp³ C–H bonds in linear alkanes is challenging due to strong C–H bonds and poor selectivity. This work demonstrates that the step edges of copper surfaces act as heterogeneous catalysts for the terminal methyl C–H cleavage, enabling linear alkane coupling under mild conditions. Density functional theory (DFT) calculations with dispersion corrections provide insight into the mechanism, revealing the activation barriers for C–H dissociation on Cu(100) and Cu(111) step edges and the corresponding adsorption energies. Reproducing these DFT-calculated quantities is crucial to validate the mechanistic explanation, and the target of this task is to compute these energies from first principles.

## Approach
The computational approach employs periodic DFT with the Perdew-Burke-Ernzerhof (PBE) functional and the D3 dispersion correction to account for van der Waals interactions. Slab models of Cu(100) and Cu(111) are constructed, each with a monatomic step edge. An n-hexane molecule is placed at the upper step edge, and geometry optimizations are performed with the bottom two Cu layers fixed. From the optimized geometries, adsorption energies are computed as the difference between the total energy of the adsorbed system, the clean slab, and the gas-phase n-hexane molecule. Transition state searches (climbing-image NEB or dimer method) are then carried out for the cleavage of specific hydrogen atoms: terminal methyl (H1), penultimate methylene (H2), and optionally the next methylene (H3). The activation barrier for each H detachment is the energy difference between the transition state and the reactant state. This procedure is repeated for both Cu(100) and Cu(111) step edges to evaluate the facet-dependence and the relative reactivity of different C–H bonds.

## Reproduction target
Compute, using DFT with the PBE-D3 method, the adsorption energy of n-hexane and the activation barriers for C–H bond cleavage of selected hydrogen atoms on Cu(100) and Cu(111) step edges. Build the slab models, perform geometry relaxations, locate transition states, and report all energies in electronvolts (eV) in the structured JSON file `results.json`. The output must contain, for each surface, the adsorption energy and the barriers for at least H1 and H2 (H3 is optional).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotential library (efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- ASE (Atomic Simulation Environment): ase

## Workflow steps

### Step 1: Build Cu(100) step-edge model with n-hexane
- Role: process
- Action: Construct a periodic slab model of Cu(100) exposing a monatomic step edge along the [001] direction. Place an n-hexane molecule in an initial adsorption position at the upper step edge, with the terminal methyl group near the low-coordinated step atoms.
- Evidence: `/app/outputs/cu100_initial_structure.xyz`

### Step 2: Geometry optimization of n-hexane on Cu(100) step edge
- Role: process
- Action: Perform DFT-D (PBE-D3) geometry relaxation of the n-hexane + Cu(100) step-edge system. Allow all atoms to relax except the bottom two Cu layers. After convergence, compute the adsorption energy as E_ads = E_system - E_slab - E_nhexane_gas.
- Evidence: `/app/outputs/cu100_optimized.xyz`

### Step 3: Transition state searches for C-H dissociation on Cu(100) step edge
- Role: process
- Action: Using the optimized geometry, perform climbing-image NEB or dimer method calculations to locate transition states for the detachment of H(1) (terminal methyl), H(2) (penultimate methylene), and optionally H(3) of the adsorbed n-hexane. Compute the activation barrier as the energy difference between the transition state and the reactant state.
- Evidence: `/app/outputs/cu100_barriers.log`

### Step 4: Build Cu(111) step-edge model with n-hexane
- Role: process
- Action: Construct a periodic slab model of Cu(111) with a monatomic step edge along the [1-10] direction. Place an n-hexane molecule at the upper step edge, ensuring the geometry reflects interactions with both upper and lower terrace atoms as implied by the paper.
- Evidence: `/app/outputs/cu111_initial_structure.xyz`

### Step 5: Geometry optimization of n-hexane on Cu(111) step edge
- Role: process
- Action: Perform DFT-D (PBE-D3) geometry relaxation of the n-hexane + Cu(111) step-edge system. Relaxation constraints similar to Cu(100). Compute the adsorption energy as E_ads = E_system - E_slab - E_nhexane_gas.
- Evidence: `/app/outputs/cu111_optimized.xyz`

### Step 6: Transition state searches for C-H dissociation on Cu(111) step edge
- Role: process
- Action: Perform transition state searches (NEB/dimer) for the detachment of H(1), H(2), and optionally H(3) on the Cu(111) step edge using the optimized geometry. Compute activation barriers.
- Evidence: `/app/outputs/cu111_barriers.log`

### Step 7: Compile and report DFT energies
- Role: scored (load-bearing)
- Action: Collect the computed adsorption energies and activation barriers from the preceding DFT calculations into a single JSON file named results.json. All energies must be in electronvolts (eV).
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"cu100":{"adsorption_energy":"number","barriers":{"H1":"number","H2":"number","H3":"number (optional)"}},"cu111":{"adsorption_energy":"number","barriers":{"H1":"number","H2":"number"}}}
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
- description: JSON file containing DFT-computed adsorption energies (eV) and activation barriers (eV) for H(1), H(2) (and optionally H(3)) on Cu(100) and Cu(111) step edges.
- schema:
  - `type`: object
  - `required`: `cu100`, `cu111`
  - `properties`:
    - `cu100`:
      - `type`: object
      - `required`: `adsorption_energy`, `barriers`
      - `properties`:
        - `adsorption_energy`:
          - `type`: number
          - `units`: eV
        - `barriers`:
          - `type`: object
          - `required`: `H1`, `H2`
          - `properties`:
            - `H1`:
              - `type`: number
              - `units`: eV
            - `H2`:
              - `type`: number
              - `units`: eV
            - `H3`:
              - `type`: number
              - `units`: eV
    - `cu111`:
      - `type`: object
      - `required`: `adsorption_energy`, `barriers`
      - `properties`:
        - `adsorption_energy`:
          - `type`: number
          - `units`: eV
        - `barriers`:
          - `type`: object
          - `required`: `H1`, `H2`
          - `properties`:
            - `H1`:
              - `type`: number
              - `units`: eV
            - `H2`:
              - `type`: number
              - `units`: eV

Notes: All energies are in electronvolts (eV). H3 on Cu(100) is optional; if not computed, omit the field. The required keys are cu100.adsorption_energy, cu100.barriers.H1, cu100.barriers.H2, cu111.adsorption_energy, cu111.barriers.H1, cu111.barriers.H2.

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
          "cu100",
          "cu111"
        ],
        "properties": {
          "cu100": {
            "type": "object",
            "required": [
              "adsorption_energy",
              "barriers"
            ],
            "properties": {
              "adsorption_energy": {
                "type": "number",
                "units": "eV"
              },
              "barriers": {
                "type": "object",
                "required": [
                  "H1",
                  "H2"
                ],
                "properties": {
                  "H1": {
                    "type": "number",
                    "units": "eV"
                  },
                  "H2": {
                    "type": "number",
                    "units": "eV"
                  },
                  "H3": {
                    "type": "number",
                    "units": "eV"
                  }
                }
              }
            }
          },
          "cu111": {
            "type": "object",
            "required": [
              "adsorption_energy",
              "barriers"
            ],
            "properties": {
              "adsorption_energy": {
                "type": "number",
                "units": "eV"
              },
              "barriers": {
                "type": "object",
                "required": [
                  "H1",
                  "H2"
                ],
                "properties": {
                  "H1": {
                    "type": "number",
                    "units": "eV"
                  },
                  "H2": {
                    "type": "number",
                    "units": "eV"
                  }
                }
              }
            }
          }
        }
      },
      "description": "JSON file containing DFT-computed adsorption energies (eV) and activation barriers (eV) for H(1), H(2) (and optionally H(3)) on Cu(100) and Cu(111) step edges."
    }
  ],
  "notes": "All energies are in electronvolts (eV). H3 on Cu(100) is optional; if not computed, omit the field. The required keys are cu100.adsorption_energy, cu100.barriers.H1, cu100.barriers.H2, cu111.adsorption_energy, cu111.barriers.H1, cu111.barriers.H2."
}
```

## How you are scored
A hidden verifier compares the contents of your `results.json` against reference values and trends derived from the published study. Your reported adsorption energies and activation barriers are each evaluated for accuracy; the relative ordering of barriers across different hydrogen positions and copper facets is also checked. The final reward is a weighted combination of these checks, so obtaining the correct quantitative values and the correct qualitative trends is essential. Simply reporting known numbers is not sufficient; the verifier expects the energies to arise from a genuine computational workflow.
