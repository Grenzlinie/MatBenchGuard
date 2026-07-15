# Nucleation Free-Energy Barrier: Critical Cluster Sizes and Free Energies

## Problem background
In the plasma pyrolysis of hydrocarbon gases for carbon nanofiber synthesis, carbon clusters nucleate at the interface between a catalytic metal substrate and either the gas phase or a deposited soot nanoparticle. The critical cluster size and the free-energy barrier for nucleation determine the nucleation probability and therefore the viability of the base-growth mode of nanofiber formation. The presence of a soot nanoparticle may significantly alter these quantities compared to nucleation at the bare metal–gas interface. This task concerns the computation of the critical cluster sizes and corresponding free energies for both interfaces using classical nucleation theory, under representative conditions.

## Approach
The free energy of a semispherical carbon cluster consisting of g atoms is modeled as a sum of a volume term (proportional to g k T ln S, describing the chemical potential driving force) and surface energy contributions that depend on the interface. For nucleation at the metal–gas interface, the surface energies of the carbon–metal, carbon–gas, and metal–gas interfaces all contribute. For nucleation under a soot nanoparticle, the carbon–soot surface tension is zero, simplifying the surface terms. The cluster radius r is related to the number of atoms g through the volume per carbon atom v_A (assuming a semispherical shape). The critical cluster size g* is obtained from the condition that the free energy is maximal (dΔF/dg = 0), which yields expressions for g* in terms of the supersaturation S, temperature T, surface tensions, and v_A. The critical free energy is then ΔF* = g* k T ln S / 2. This approach is applied to both scenarios using fixed representative parameters to obtain the four critical quantities.

## Reproduction target
Compute the critical cluster sizes g1* (metal–gas interface) and g2* (metal–soot interface), and the dimensionless critical free energies ΔF1*/k and ΔF2*/k, using the analytical framework described under Approach. Use the following fixed parameters: temperature T = 1000 K, supersaturation S = 10, surface tensions σ_cm = σ_cg = σ_mg = 1 J/m², volume per carbon atom v_A = 8.8 × 10⁻³⁰ m³, and Boltzmann constant k = 1.380649 × 10⁻²³ J/K. Save the four values as a JSON file named results.json with keys g1_star, g2_star, DeltaF1_star, and DeltaF2_star.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Compute critical cluster sizes and free energies
- Role: scored (load-bearing)
- Action: Implement the analytical expressions for the critical number of atoms g1* (metal-gas interface) and g2* (metal-soot interface), and the relation for critical free energy ΔF* = g* k T ln S / 2, as described in the paper. Use the specified parameters: T = 1000 K, supersaturation S = 10, surface tensions σ_cm = σ_cg = σ_mg = 1 J/m², volume per carbon atom v_A = 8.8×10⁻³⁰ m³, and Boltzmann constant k = 1.380649×10⁻²³ J/K. Compute the four values: g1*, g2*, ΔF1*/k (dimensionless), and ΔF2*/k (dimensionless). Save the results in a JSON file named results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"g1_star": "number", "g2_star": "number", "DeltaF1_star": "number", "DeltaF2_star": "number"}
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
- description: Contains the computed critical cluster sizes (g1*, g2*) and critical free energies (ΔF1*, ΔF2*) for nucleation on the metal–gas and metal–soot interfaces, expressed as defined in the paper.
- schema:
  - `type`: object
  - `required`: `g1_star`, `g2_star`, `DeltaF1_star`, `DeltaF2_star`
  - `properties`:
    - `g1_star`:
      - `type`: number
    - `g2_star`:
      - `type`: number
    - `DeltaF1_star`:
      - `type`: number
    - `DeltaF2_star`:
      - `type`: number
  - `units`:
    - `g1_star`: number of atoms
    - `g2_star`: number of atoms
    - `DeltaF1_star`: dimensionless (units of k)
    - `DeltaF2_star`: dimensionless (units of k)

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
          "g1_star",
          "g2_star",
          "DeltaF1_star",
          "DeltaF2_star"
        ],
        "properties": {
          "g1_star": {
            "type": "number"
          },
          "g2_star": {
            "type": "number"
          },
          "DeltaF1_star": {
            "type": "number"
          },
          "DeltaF2_star": {
            "type": "number"
          }
        },
        "units": {
          "g1_star": "number of atoms",
          "g2_star": "number of atoms",
          "DeltaF1_star": "dimensionless (units of k)",
          "DeltaF2_star": "dimensionless (units of k)"
        }
      },
      "description": "Contains the computed critical cluster sizes (g1*, g2*) and critical free energies (ΔF1*, ΔF2*) for nucleation on the metal–gas and metal–soot interfaces, expressed as defined in the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will evaluate your results.json by checking the computed values against expectations consistent with the given parameters. The evaluation verifies that the values satisfy the physical ordering: g2* < g1* and ΔF2* < ΔF1*, and that each quantity falls within a hidden acceptable range derived from a correct implementation of the described approach. The exact tolerance is not disclosed, but a faithful implementation of the free-energy model and critical-point derivation will pass. The reward is a single number between 0 and 1, reflecting overall fidelity.
