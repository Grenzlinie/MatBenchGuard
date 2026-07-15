# DFT-Based Free-Energy Analysis of CO2 Electroreduction on Copper-Based Catalyst Models

## Problem background
Electrochemical CO₂ reduction to hydrocarbons on copper‐based catalysts is a promising route for carbon utilization. Tailoring the interaction between copper species and nitrogen‐containing carbon supports (CₓNᵧ) can dramatically alter product selectivity toward C₂H₄ or CH₄. Density functional theory (DFT) calculations are employed to predict the free‐energy barriers for elementary mechanistic steps on different catalyst surface models, helping to rationalize how the support chemistry and copper state influence reaction pathways.

## Approach
Four idealized catalyst surface models are constructed: Cu₃N(100), a Cu₁₄ cluster supported on a tri‑s‑triazine g‑C₃N₄ sheet, a Cu(111) single‑crystal slab, and a Cu cluster on pristine graphene. For each model, spin‑polarized DFT calculations are performed with a PBE exchange‑correlation functional, Grimme DFT‑D3 dispersion correction, and an implicit water solvation model. After geometry optimization, total energies of adsorbed *CO, *CHO, and *CHOCO intermediates, together with gas‑phase reference molecules (H₂, CO, H₂O), are computed. Finally, the computational hydrogen electrode (CHE) model is applied to derive Gibbs free energy changes (ΔG) for *CO hydrogenation to *CHO on all four surfaces and for *CHO coupling with *CO to *CHOCO on three of the surfaces (the Cu–C model is excluded from the coupling step). The relative barriers across the surfaces provide insight into the selectivity‑determining steps.

## Reproduction target
Construct the four surface models (Cu₃N(100), g‑C₃N₄‑supported Cu cluster, Cu(111), and Cu on graphene) and execute the DFT + CHE free‑energy workflow. Report the Gibbs free energy changes (in eV) for:
- *CO hydrogenation to *CHO on Cu‑C₃N₄, Cu‑C, Cu(111), and Cu₃N(100).
- *CHO coupling with *CO to *CHOCO on Cu‑C₃N₄, Cu(111), and Cu₃N(100).
Write the results to `/app/outputs/free_energies.json` following the specified schema.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, GPAW): https://www.quantum-espresso.org
- Cu3N primitive cell (Materials Project): https://materialsproject.org/
- Tri-s-triazine g-C3N4 unit cell
- Cu(111) surface lattice parameter

## Workflow steps

### Step 1: Model construction and geometry optimization
- Role: process
- Action: Build four atomic models: (1) Cu3N(100) 3×3 supercell from the Cu3N primitive cell, (2) tri-s-triazine g-C3N4 unit cell with a Cu14 cluster anchored at the central cavity, (3) Cu(111) 3×3 surface slab, and (4) Cu cluster on graphene (Cu-C). Perform spin-polarized DFT geometry optimization using PBE functional, DFT-D3 dispersion correction, and an implicit water solvation model.
- Evidence: none

### Step 2: DFT total energy calculation of reaction intermediates
- Role: process
- Action: For each optimized surface model, compute spin-polarized DFT total energies of adsorbed *CO, *CHO, and *CHOCO intermediates, as well as gas-phase reference molecules H2, CO, and H2O.
- Evidence: none

### Step 3: Gibbs free energy evaluation
- Role: scored (load-bearing)
- Action: Apply the computational hydrogen electrode (CHE) model to compute Gibbs free energy changes (ΔG) in eV for: (a) *CO hydrogenation to *CHO on Cu-C3N4, Cu-C, Cu(111), and Cu3N(100); (b) *CHO coupling with *CO to *CHOCO on Cu-C3N4, Cu(111), and Cu3N(100). Include zero-point energy and entropy corrections. Write the results to free_energies.json.
- Output file: `/app/outputs/free_energies.json`
- Format: json
- Contract: {"Cu-C3N4":{"CO_to_CHO":<float>,"CHO_CO_coupling":<float>},"Cu3N(100)":{"CO_to_CHO":<float>,"CHO_CO_coupling":<float>},"Cu(111)":{"CO_to_CHO":<float>,"CHO_CO_coupling":<float>},"Cu-C":{"CO_to_CHO":<float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energies.json
- path: `/app/outputs/free_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gibbs free energy barriers for key elementary steps: *CO hydrogenation on four surfaces, and *CHO-*CO coupling on three surfaces (Cu-C omitted for coupling). Compares against hidden reference values from the paper's free-energy diagrams, with tolerance for DFT toolchain differences.
- schema:
  - `type`: object
  - `properties`:
    - `Cu-C3N4`:
      - `type`: object
      - `properties`:
        - `CO_to_CHO`:
          - `type`: number
          - `units`: eV
        - `CHO_CO_coupling`:
          - `type`: number
          - `units`: eV
      - `required`: `CO_to_CHO`, `CHO_CO_coupling`
    - `Cu3N(100)`:
      - `type`: object
      - `properties`:
        - `CO_to_CHO`:
          - `type`: number
          - `units`: eV
        - `CHO_CO_coupling`:
          - `type`: number
          - `units`: eV
      - `required`: `CO_to_CHO`, `CHO_CO_coupling`
    - `Cu(111)`:
      - `type`: object
      - `properties`:
        - `CO_to_CHO`:
          - `type`: number
          - `units`: eV
        - `CHO_CO_coupling`:
          - `type`: number
          - `units`: eV
      - `required`: `CO_to_CHO`, `CHO_CO_coupling`
    - `Cu-C`:
      - `type`: object
      - `properties`:
        - `CO_to_CHO`:
          - `type`: number
          - `units`: eV
      - `required`: `CO_to_CHO`
  - `required`: `Cu-C3N4`, `Cu3N(100)`, `Cu(111)`, `Cu-C`

Notes: The four surface models and the intermediates are exactly those described in the paper's computational details. The checker compares each reported free-energy value to a hidden gold tolerance and also verifies that the relative trend ordering among the surfaces (lowest CO-to-CHO barrier on Cu-C3N4, most exergonic C-C coupling on Cu3N(100)) is reproduced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "Cu-C3N4": {
            "type": "object",
            "properties": {
              "CO_to_CHO": {
                "type": "number",
                "units": "eV"
              },
              "CHO_CO_coupling": {
                "type": "number",
                "units": "eV"
              }
            },
            "required": [
              "CO_to_CHO",
              "CHO_CO_coupling"
            ]
          },
          "Cu3N(100)": {
            "type": "object",
            "properties": {
              "CO_to_CHO": {
                "type": "number",
                "units": "eV"
              },
              "CHO_CO_coupling": {
                "type": "number",
                "units": "eV"
              }
            },
            "required": [
              "CO_to_CHO",
              "CHO_CO_coupling"
            ]
          },
          "Cu(111)": {
            "type": "object",
            "properties": {
              "CO_to_CHO": {
                "type": "number",
                "units": "eV"
              },
              "CHO_CO_coupling": {
                "type": "number",
                "units": "eV"
              }
            },
            "required": [
              "CO_to_CHO",
              "CHO_CO_coupling"
            ]
          },
          "Cu-C": {
            "type": "object",
            "properties": {
              "CO_to_CHO": {
                "type": "number",
                "units": "eV"
              }
            },
            "required": [
              "CO_to_CHO"
            ]
          }
        },
        "required": [
          "Cu-C3N4",
          "Cu3N(100)",
          "Cu(111)",
          "Cu-C"
        ]
      },
      "description": "Gibbs free energy barriers for key elementary steps: *CO hydrogenation on four surfaces, and *CHO-*CO coupling on three surfaces (Cu-C omitted for coupling). Compares against hidden reference values from the paper's free-energy diagrams, with tolerance for DFT toolchain differences."
    }
  ],
  "notes": "The four surface models and the intermediates are exactly those described in the paper's computational details. The checker compares each reported free-energy value to a hidden gold tolerance and also verifies that the relative trend ordering among the surfaces (lowest CO-to-CHO barrier on Cu-C3N4, most exergonic C-C coupling on Cu3N(100)) is reproduced."
}
```

## How you are scored
A hidden verifier independently inspects your `/app/outputs/free_energies.json`. Each reported free‑energy value is compared to a reference value derived from the original study, with an appropriate tolerance that accounts for differences in DFT toolchains and computational settings. Additionally, the verifier checks that the computed barriers reproduce the relative reactivity trends among the surfaces (e.g., which surface is most favorable for *CO hydrogenation and which is most exergonic for C–C coupling). No partial credit is given for merely reporting values; the entire workflow must be executed and must yield consistent, physically meaningful numbers. The final reward is a weighted combination of the value‑level comparisons and the trend‑ordering checks.
