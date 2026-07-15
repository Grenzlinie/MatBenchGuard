# Density functional theory study of octagonal boron nitride: structure, layering, defects, and hydrogen adsorption

## Problem background
Boron nitride is a promising two‑dimensional material beyond graphene. While the hexagonal allotrope is well known, non‑hexagonal lattices could exhibit distinct properties. This task investigates a two‑dimensional boron nitride monolayer with an octagonal lattice. Using spin‑polarized density functional theory, you will compute the binding energy per atom and the electronic band gap of the monolayer, determine how bilayer and trilayer stacks bind through van der Waals forces, measure the magnetic moment introduced by a boron vacancy, and evaluate hydrogen adsorption on pristine and defective surfaces of both hexagonal and octagonal boron nitride. The goal is to produce the full set of target quantities that characterise the stability, electronic properties, layerability, defect‑induced magnetism, and hydrogen reactivity of this material.

## Approach
You will use the open‑source GPAW package to perform spin‑polarised DFT calculations. All structures are built from known lattice parameters: hexagonal BN with a honeycomb lattice and octagonal BN derived from the octagraphene lattice. Relax the monolayer structures with the PBE exchange‑correlation functional. From the relaxed octagonal monolayer extract the binding energy per atom and the band gap. Stack the relaxed octagonal monolayer into bilayer and trilayer configurations and relax them again with two different exchange‑correlation functionals: PBE and the van der Waals density functional (vdW‑DF). For each stack and functional, compute the equilibrium interlayer distance and the binding energy. Introduce a single boron vacancy and a single nitrogen vacancy into the relaxed octagonal monolayer (and separately into the relaxed hexagonal monolayer), then relax the defective structures. From these, extract the magnetic moment on the nitrogen atom nearest to the boron vacancy. Finally, adsorb a single hydrogen atom on the eight configurations described in the target: pristine hexagonal BN with H on B and on N, pristine octagonal BN with H on B and on N, and the corresponding defect‑site adsorptions (H on the atom nearest to the vacancy in boron‑defect and nitrogen‑defect hexagonal and octagonal BN). For each adsorption case compute the adsorption energy and the H‑surface bond distance using spin‑polarised DFT. Assemble every computed value into the final JSON file described in the workflow steps.

## Reproduction target
Produce the following quantities and report them in a single JSON file at `/app/outputs/reproduction_results.json`. For the octagonal BN monolayer: the binding energy per atom (eV) and the electronic band gap (eV). For bilayer and trilayer stacks of octagonal BN, relaxed with both PBE and vdW‑DF: the interlayer distance (Å) and the binding energy (eV); for the trilayer also include the average interlayer distance (Å). For the defective octagonal BN monolayer: the magnetic moment (μB) of the nitrogen atom neighbouring a boron vacancy. For hydrogen adsorption: eight entries, one for each configuration listed in the workflow, each containing a label string, the adsorption energy (eV), and the H‑surface bond distance (Å). The exact required JSON structure is described in the output contract and the Compile reproduction results step.

## Assets

- GPAW (Grid-based Projector Augmented Wave method): https://wiki.fysik.dtu.dk/gpaw/
- Bader charge analysis code: https://theory.cm.utexas.edu/henkelman/code/bader/

## Workflow steps

### Step 1: Generate initial structures
- Role: process
- Action: Construct the unit cells for hexagonal BN and octagonal BN based on known lattice parameters (h-BN hexagonal geometry and octagraphene lattice).
- Evidence: none

### Step 2: Relax hexagonal BN monolayer
- Role: process
- Action: Perform spin-polarized DFT relaxation of the hexagonal BN monolayer using GPAW with PBE functional to obtain the equilibrium structure.
- Evidence: `/app/outputs/hbn_monolayer_relaxed.structure`

### Step 3: Relax octagonal BN monolayer and compute properties
- Role: process
- Action: Perform spin-polarized DFT relaxation of the octagonal BN monolayer using GPAW with PBE functional, and compute its binding energy per atom and band gap.
- Evidence: `/app/outputs/obn_monolayer_relaxed.structure`

### Step 4: Bilayer and trilayer physisorption calculations
- Role: process
- Action: Build bilayer and trilayer stacks from the relaxed octagonal BN monolayer. For each stack, relax the atomic positions (and interlayer spacing) using both PBE and vdW-DF exchange-correlation functionals. Compute the equilibrium interlayer distances and binding energies.
- Evidence: `/app/outputs/layering_output.log`

### Step 5: Defect calculations in octagonal BN
- Role: process
- Action: Introduce a single boron vacancy and a single nitrogen vacancy in the relaxed octagonal BN monolayer, relax the defective structures, and compute the magnetic moments on the nearest-neighbour atoms (particularly the magnetic moment on nitrogen near the boron vacancy).
- Evidence: `/app/outputs/obn_defects.traj`

### Step 6: Create defective hexagonal BN structures
- Role: process
- Action: Create a single boron vacancy and a single nitrogen vacancy in the relaxed hexagonal BN monolayer and relax the structures.
- Evidence: `/app/outputs/hbn_defects.traj`

### Step 7: Hydrogen adsorption on pristine and defective BN surfaces
- Role: process
- Action: For the eight configurations listed in Table 1 (pristine hexagonal BN H on B and N, pristine octagonal BN H on B and N, defected hexagonal BN with H at the reactive site, and defected octagonal BN), place a hydrogen atom at the designated adsorption site and perform a spin‑polarized DFT calculation to determine the adsorption energy and the H–surface bond distance.
- Evidence: `/app/outputs/hydrogen_adsorption_output.log`

### Step 8: Compile reproduction results
- Role: scored (load-bearing)
- Action: Gather all computed quantities from the previous steps and write them into a single JSON file. The file must contain: monolayer (binding_energy_per_atom in eV, band_gap in eV), layering (bilayer and trilayer with PBE and vdW-DF results: interlayer_distance in Å, binding_energy in eV; for trilayer include average_interlayer_distance), defects (B_vacancy_N_magnetic_moment in μB), and hydrogen_adsorption (a list of eight objects each with fields label, adsorption_energy in eV, bond_distance in Å).
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: JSON object with keys: monolayer (binding_energy_per_atom, band_gap), layering (bilayer and trilayer each with PBE and vdW-DF sub‑objects containing interlayer_distance and binding_energy; trilayer also includes average_interlayer_distance), defects (B_vacancy_N_magnetic_moment), hydrogen_adsorption (array of objects with label, adsorption_energy, bond_distance).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Complete set of reproduced DFT results for octagonal BN stability, layering, defects, and hydrogen reactivity.
- schema:
  - `type`: object
  - `required`:
    - `monolayer`: object with keys binding_energy_per_atom (eV) and band_gap (eV)
    - `layering`: object containing bilayer and trilayer sub-objects; each has PBE and vdW-DF sub-objects with interlayer_distance (Å) and binding_energy (eV); trilayer additionally has average_interlayer_distance (Å)
    - `defects`: object with key B_vacancy_N_magnetic_moment (μB)
    - `hydrogen_adsorption`: array of 8 objects, each with keys label (string), adsorption_energy (eV), bond_distance (Å)
  - `items`:
    - `hydrogen_adsorption_item`: object with label, adsorption_energy, bond_distance
  - `required_columns`:
  - `units`:
    - `energies`: eV
    - `distances`: Å
    - `magnetic_moment`: μB

Notes: All quantities are computed using spin-polarized DFT with GPAW; PBE and vdW-DF exchange-correlation functionals are used exactly as described. The file serves as the single scored artifact against paper-reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "monolayer": "object with keys binding_energy_per_atom (eV) and band_gap (eV)",
          "layering": "object containing bilayer and trilayer sub-objects; each has PBE and vdW-DF sub-objects with interlayer_distance (Å) and binding_energy (eV); trilayer additionally has average_interlayer_distance (Å)",
          "defects": "object with key B_vacancy_N_magnetic_moment (μB)",
          "hydrogen_adsorption": "array of 8 objects, each with keys label (string), adsorption_energy (eV), bond_distance (Å)"
        },
        "items": {
          "hydrogen_adsorption_item": "object with label, adsorption_energy, bond_distance"
        },
        "required_columns": [],
        "units": {
          "energies": "eV",
          "distances": "Å",
          "magnetic_moment": "μB"
        }
      },
      "description": "Complete set of reproduced DFT results for octagonal BN stability, layering, defects, and hydrogen reactivity."
    }
  ],
  "notes": "All quantities are computed using spin-polarized DFT with GPAW; PBE and vdW-DF exchange-correlation functionals are used exactly as described. The file serves as the single scored artifact against paper-reported values."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/reproduction_results.json` file after your run finishes. It independently checks every numeric field in that file against reference values derived from the published calculations. The verifier awards credit based on how many of the required numeric quantities are within an acceptable range. All fields are treated with equal weight, and the final reward is the fraction of checks that pass.
