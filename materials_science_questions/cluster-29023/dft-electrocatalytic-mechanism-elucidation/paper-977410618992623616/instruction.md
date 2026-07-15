# DFT Elucidation of CO2RR Electrocatalytic Mechanism for 2D MOF Candidates

## Problem background
Electrocatalytic CO₂ reduction is a promising route to produce valuable chemicals while mitigating greenhouse gas emissions, but achieving high selectivity toward a single product at low overpotential is challenging because of the competing hydrogen evolution reaction (HER) and the stability of the CO₂ molecule. Two‑dimensional π‑conjugated metal‑organic frameworks (2D c‑MOFs) with well‑defined TM‑X₄ active sites offer a tunable platform where both the metal center and the organic linker can modulate the reaction pathway and product distribution. This study computationally screens 2D MOFs built from 3d transition metals and different ligand topologies to predict which combinations yield highly selective CO₂ reduction electrocatalysts with distinct single‑carbon products.

## Approach
Using spin‑polarized density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) functional, periodic slab models of 2D MOFs are built from the experimental crystal structures. The aqueous electrolyte is treated with an implicit solvation model (continuum dielectric, ε = 78.54) and van der Waals interactions are included via the DFT‑D3 correction. For each MOF, the clean surface and all adsorbed CO₂ reduction intermediates along the possible proton‑coupled electron transfer (PCET) pathways up to the final C₁ product are computed. The computational hydrogen electrode (CHE) model converts total energies to Gibbs free‑energy changes (ΔG) at zero applied potential (pH 0, 298 K), including zero‑point energy and entropy corrections from vibrational frequencies. The first hydrogenation step (CO₂ → *HCOO or *COOH) is compared with HER to ensure CO₂ activation is kinetically preferred. The most favorable reaction pathway is identified by choosing, at each branching point, the step with the lowest ΔG, and the rate‑limiting step is the elementary step with the largest positive ΔG. The limiting potential is calculated as U_L = −max(ΔG_step) (in V). The final product identity follows from the sequence that leads to the weakest bound product.

## Reproduction target
For the five 2D MOFs Cu₃(HIB)₂, Cu₃(HITP)₂, Ni₃HHB, Co₃HIB, and Cr₃HTB, compute the complete Gibbs free‑energy profile for the CO₂RR pathway and the competing HER. Determine the most favorable reaction path, identify the rate‑limiting step (largest positive ΔG), and calculate the limiting potential U_L = −max(ΔG). Confirm that the first CO₂ hydrogenation is thermodynamically more favorable than HER (ΔG(first hydrogenation) < ΔG(HER)). Report the final product (one of HCOOH, CH₂O, or CH₄) and all computed ΔG values for the most favorable pathway in a JSON file exactly following the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Atomic Simulation Environment (ASE): ase
- PBE pseudopotentials (SSSP or GBRV): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Construct and optimize MOF structures
- Role: process
- Action: Build periodic slab models for the five specified 2D MOFs (Cu3(HIB)2, Cu3(HITP)2, Ni3HHB, Co3HIB, Cr3HTB) using the provided lattice parameters and atomic coordinates, with a vacuum spacing of at least 15 Å. Perform full geometry optimization (atomic positions and cell) at the PBE level with plane-wave basis, appropriate k‑point sampling, DFT‑D3 van der Waals correction, and an implicit solvation model (e.g., VASPsol‑type continuum, dielectric constant 78.54) to represent aqueous electrolyte. Converge forces to <0.02 eV/Å.
- Evidence: `/app/outputs/geometry_optimization.log`

### Step 2: Compute Gibbs free‑energy changes for all elementary steps
- Role: process
- Action: For each optimized MOF, calculate DFT total energies of the clean slab and of all adsorbed CO2RR intermediates along every plausible PCET pathway up to the final single‑carbon product (HCOOH, CH2O, or CH4), including the competing HER intermediate H*. Use the computational hydrogen electrode (CHE) model to convert total energies to Gibbs free‑energy changes ΔG at zero applied potential (pH 0, 298 K), applying zero‑point energy and entropy corrections from vibrational frequency calculations. Record every ΔG value (in eV) for each elementary step in a JSON file.
- Evidence: `/app/outputs/intermediate_energies.json`

### Step 3: Determine pathway, rate‑limiting step, limiting potential, and output results
- Role: scored (load-bearing)
- Action: From the computed ΔG values, for each MOF identify the most favorable CO2RR pathway (the sequence of PCET steps with the lowest free‑energy change at each hydrogenation branch, considering *HCOO vs *COOH, subsequent hydrogenation to HCOOH or CO, and further reductions to CH2O or CH4). Confirm that the first CO2 hydrogenation is thermodynamically more favorable than HER (ΔG(first hydrogenation) < ΔG(HER)). Determine the rate‑limiting step (the elementary step with the largest positive ΔG) and compute the limiting potential U_L = −max(ΔG_step) (in V). Write all results to /app/outputs/results.json exactly as specified in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "Cu3HIB2": {
    "product": "string",
    "limiting_potential": "number (V)",
    "rate_limiting_step": "string description",
    "delta_G_steps": [{"step": "string label", "DG": "number (eV)"}, ...]
  },
  "Cu3HITP2": { ... },
  "Ni3HHB": { ... },
  "Co3HIB": { ... },
  "Cr3HTB": { ... },
  "summary": [
    {"MOF": "string", "product": "string", "U_L": "number (V)"},
    ... for all five MOFs
  ]
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
- target_policy: threshold_or_better
- description: Computed limiting potentials, product identities, rate‑limiting steps, and raw free‑energy profiles for the five MOF catalysts.
- schema:
  - `type`: object
  - `required`: `Cu3HIB2`, `Cu3HITP2`, `Ni3HHB`, `Co3HIB`, `Cr3HTB`, `summary`
  - `properties`:
    - `Cu3HIB2`:
      - `type`: object
      - `required`: `product`, `limiting_potential`, `rate_limiting_step`, `delta_G_steps`
      - `properties`:
        - `product`:
          - `type`: string
        - `limiting_potential`:
          - `type`: number
        - `rate_limiting_step`:
          - `type`: string
        - `delta_G_steps`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `step`, `DG`
            - `properties`:
              - `step`:
                - `type`: string
              - `DG`:
                - `type`: number
    - `Cu3HITP2`:
      - `$ref`: #/properties/Cu3HIB2
    - `Ni3HHB`:
      - `$ref`: #/properties/Cu3HIB2
    - `Co3HIB`:
      - `$ref`: #/properties/Cu3HIB2
    - `Cr3HTB`:
      - `$ref`: #/properties/Cu3HIB2
    - `summary`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `MOF`, `product`, `U_L`
        - `properties`:
          - `MOF`:
            - `type`: string
          - `product`:
            - `type`: string
          - `U_L`:
            - `type`: number

Notes: The checker recomputes the limiting potential from the delta_G_steps array and compares product identities. The 'threshold_or_better' policy applies to U_L (less negative is better). All required fields must be present.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "Cu3HIB2",
          "Cu3HITP2",
          "Ni3HHB",
          "Co3HIB",
          "Cr3HTB",
          "summary"
        ],
        "properties": {
          "Cu3HIB2": {
            "type": "object",
            "required": [
              "product",
              "limiting_potential",
              "rate_limiting_step",
              "delta_G_steps"
            ],
            "properties": {
              "product": {
                "type": "string"
              },
              "limiting_potential": {
                "type": "number"
              },
              "rate_limiting_step": {
                "type": "string"
              },
              "delta_G_steps": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "step",
                    "DG"
                  ],
                  "properties": {
                    "step": {
                      "type": "string"
                    },
                    "DG": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "Cu3HITP2": {
            "$ref": "#/properties/Cu3HIB2"
          },
          "Ni3HHB": {
            "$ref": "#/properties/Cu3HIB2"
          },
          "Co3HIB": {
            "$ref": "#/properties/Cu3HIB2"
          },
          "Cr3HTB": {
            "$ref": "#/properties/Cu3HIB2"
          },
          "summary": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "MOF",
                "product",
                "U_L"
              ],
              "properties": {
                "MOF": {
                  "type": "string"
                },
                "product": {
                  "type": "string"
                },
                "U_L": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Computed limiting potentials, product identities, rate‑limiting steps, and raw free‑energy profiles for the five MOF catalysts."
    }
  ],
  "notes": "The checker recomputes the limiting potential from the delta_G_steps array and compares product identities. The 'threshold_or_better' policy applies to U_L (less negative is better). All required fields must be present."
}
```

## How you are scored
Your submission will be scored by a hidden verifier that reads /app/outputs/results.json. For each MOF, the verifier extracts the array of ΔG values (delta_G_steps) and recomputes the limiting potential as U_L = −max(ΔG). The recomputed U_L is compared to the paper’s reported value with a threshold‑or‑better policy: meeting or exceeding (more positive) the reference earns full credit. The verifier also checks that the reported product matches the expected product for that MOF. Additionally, it verifies that the ΔG of the first CO₂ hydrogenation step in your reported pathway is lower than the ΔG of the HER step, confirming that CO₂ reduction is favored over hydrogen evolution. A weighted combination of these checks determines your score; simply writing the expected numbers without performing the DFT workflow will result in inconsistent or missing raw ΔG data and will not pass the recompute checks.
