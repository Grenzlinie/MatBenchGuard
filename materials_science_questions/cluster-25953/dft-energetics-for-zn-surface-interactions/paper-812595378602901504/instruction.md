# Single water molecule adsorption on ZnO surface via DFT

## Problem background
Zinc oxide (ZnO) is widely used in humidity sensors, where the adsorption of water molecules on the ZnO surface alters its electrical response. Understanding the fundamental interaction of a single water molecule with the surface—its binding strength, geometry, and charge redistribution—is essential to assess whether the adsorption is physical or chemical, which in turn governs sensor reversibility and sensitivity. This task uses first-principles density functional theory (DFT) to quantify the adsorption behavior of a lone H2O molecule on the ZnO(0001) surface.

## Approach
The computational approach employs spin-polarized DFT with the Perdew-Burke-Ernzerhof (PBE) generalized-gradient approximation, an open-source plane-wave/pseudopotential code (e.g., Quantum ESPRESSO), and pseudopotentials for Zn and O. Start from the wurtzite ZnO crystal structure to build a two-layer slab in a supercell with a vacuum region normal to the surface. Freeze the bottom layer and relax the top layer to obtain the clean surface. Then place one water molecule near a surface Zn site and relax the combined system, keeping the bottom layer fixed. The key outputs are the binding energy (computed from total energy differences), the shortest O(water)–Zn(surface) and H(water)–O(surface) distances, and the net charge transfer (Mulliken or Bader analysis). Two stages carry out this workflow: (1) relaxation of the pristine slab, and (2) adsorption and property evaluation for the single water molecule.

## Reproduction target
Using the above slab model and DFT methodology, compute the following four quantities for a single H2O molecule adsorbed on ZnO(0001):
1. Binding energy (eV)
2. Shortest distance between the water oxygen and a surface zinc atom (Å)
3. Shortest distance between a water hydrogen and a surface oxygen atom (Å)
4. Net charge transfer between the water molecule and the surface (elementary charge)
Write these values to the JSON file `single_water_adsorption_results.json` according to the output contract.

## Assets

- ZnO wurtzite crystal structure: https://materialsproject.org/materials/mp-2133/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials for Zn and O (SSSP): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare and relax clean ZnO slab
- Role: process
- Action: Build a two-layer ZnO slab in a [5×3] supercell using the wurtzite crystal structure. Add a 10 Å vacuum region normal to the surface. Fix the bottom ZnO layer and relax the top layer using spin-polarized DFT with PBE functional, kinetic energy cutoff and k-point mesh chosen for convergence. Relax until forces on movable atoms are below 0.002 Ha/Å and energy change < 1e-6 Ha.
- Evidence: `/app/outputs/relaxed_slab.xyz`

### Step 2: Single H2O molecule adsorption
- Role: scored (load-bearing)
- Action: Place a single H2O molecule on the relaxed ZnO slab, near a surface Zn site. Relax the combined system (bottom ZnO layer fixed, top layer and water molecule free) using the same DFT settings. Compute the total energy of the slab+H2O system, the isolated H2O molecule, and the clean slab. Calculate the binding energy as E_bind = E_slab_H2O - E_slab - E_H2O_isolated. Extract the shortest O(water)–Zn(surface) distance and H(water)–O(surface) distance from the optimized geometry. Compute the net charge transfer (via Mulliken or Bader analysis) between the molecule and the surface. Write all four quantities to the output JSON file.
- Output file: `/app/outputs/single_water_adsorption_results.json`
- Format: json
- Contract: {"binding_energy_eV": float, "zn_o_distance_A": float, "h_o_distance_A": float, "charge_transfer_e": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/single_water_adsorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### single_water_adsorption_results.json
- path: `/app/outputs/single_water_adsorption_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Results of single water molecule adsorption on ZnO: binding energy, nearest Zn-O distance, H-O distance, and net charge transfer. All fields must be present and within tolerances compared to the hidden reference.
- schema:
  - `type`: object
  - `required`:
    - `binding_energy_eV`: number (eV)
    - `zn_o_distance_A`: number (Å)
    - `h_o_distance_A`: number (Å)
    - `charge_transfer_e`: number (elementary charge)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "single_water_adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "binding_energy_eV": "number (eV)",
          "zn_o_distance_A": "number (Å)",
          "h_o_distance_A": "number (Å)",
          "charge_transfer_e": "number (elementary charge)"
        }
      },
      "description": "Results of single water molecule adsorption on ZnO: binding energy, nearest Zn-O distance, H-O distance, and net charge transfer. All fields must be present and within tolerances compared to the hidden reference."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `single_water_adsorption_results.json` and compares the four reported quantities against independently established reference values. Each field must be present and within pre-defined absolute tolerances to earn full credit; missing fields or values outside tolerance reduce the score. The verifier also checks that required evidence artifacts (e.g., `relaxed_slab.xyz`) exist, but only the adsorption JSON contributes substantively to the final reward.
