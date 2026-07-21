# Compute LiF adsorption energies on CaF2(111) surface and step using classical pair potentials

## Problem background
The adsorption of lithium fluoride molecules on the (111) surface of calcium fluoride is central to understanding epitaxial growth and surface chemistry of ionic crystals. LiF vapor consists mainly of monomers and dimers; when deposited onto CaF2(111) they interact strongly with surface steps, where dissociation and incorporation occur. This task investigates the equilibrium adsorption of the LiF monomer, the rhombic Li2F2 dimer, and the metastable linear Li2F2 dimer on the flat (111) terrace and at a [10-1] monomolecular step of type I. The goal is to compute the total adsorption energies, which characterize the molecule–surface binding strength and help explain step-mediated dimer dissociation.

## Approach
The computational model treats all ions as point charges with classical pair potentials. Short-range interactions use Catlow-type potentials: Born-Mayer repulsion for Li+–F– and Ca2+–F–, and van der Waals attraction between fluorine ions; interactions between cations are purely Coulombic. A slab of four F––Ca2+–F– triple layers represents the CaF2(111) substrate. Long-range Coulomb sums for the slab are handled by a 2D Ewald method; for the step region, direct summation over many ion rows is used alongside Ewald for the deeper bulk. First, the clean surface and step geometries are relaxed: the outermost triple layer ions and the ion rows at the [10-1] type I step are allowed to move perpendicular to the surface and within the step plane, respectively. Then, for each admolecule (monomer, rhombic dimer, linear dimer), energy minimizations are performed on the relaxed terrace and at the relaxed step, allowing a cluster of nearby crystal ions (10–16 ions) to relax as well. The total adsorption energy is computed as the sum of three contributions: the relaxation energy of the adregion crystal ions relative to the clean relaxed surface, the change in intramolecular energy of the admolecule compared to its free state, and the interaction energy between the admolecule and the crystal plus adregion. The free-molecule reference energies are obtained by optimizing the isolated monomer, rhombic dimer, and linear dimer with the same potentials.

## Reproduction target
Compute, using the described workflow, the total adsorption energies (in eV) for the LiF monomer, the rhombic Li2F2 dimer, and the linear Li2F2 dimer at two sites: the relaxed (111) terrace and the relaxed [10-1] type I step on CaF2. Report the six energies in a JSON file `/app/outputs/adsorption_energies.json` with keys `terrace_monomer`, `terrace_rhombic_dimer`, `terrace_linear_dimer`, `step_monomer`, `step_rhombic_dimer`, and `step_linear_dimer`.

## Assets

- Catlow-type pair potentials for LiF and CaF2: 10.1088/0022-3719/10/8/018
- CaF2 bulk lattice constant a0

## Workflow steps

### Step 1: Reference free LiF molecule calculations
- Role: process
- Action: Using the Catlow-type pair potentials, compute equilibrium geometries and binding energies of the free LiF monomer, the rhombic Li2F2 dimer, and the metastable linear Li2F2 dimer. These energies are needed to define the molecular relaxation term in the adsorption energy decomposition.
- Evidence: `/app/outputs/free_mol_energies.json`

### Step 2: Relaxation of CaF2(111) surface and [10-1] step
- Role: process
- Action: Construct a slab of four F-–Ca2+–F- triple layers of CaF2(111). Implement 2D Ewald summation for long-range Coulomb energy of the slab and direct real-space summation for near-step regions. Using the Catlow potentials, relax the ion positions of the outermost triple layer and of the ion rows at a [10-1] type I step to obtain the equilibrium substrate geometry.
- Evidence: `/app/outputs/relaxed_surface_step.json`

### Step 3: Adsorption energy minimizations on terrace and step
- Role: scored (load-bearing)
- Action: For each of the three admolecules (LiF monomer, rhombic Li2F2 dimer, linear Li2F2 dimer), perform energy minimizations on both the relaxed terrace and at the relaxed [10-1] step. Include relaxation of adregion ions (10–16 crystal ions). Compute the total adsorption energy E_ad as E_reg_rel + E_mol_rel + E_int. Output the six final energies in a JSON file.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: JSON object with keys: terrace_monomer, terrace_rhombic_dimer, terrace_linear_dimer, step_monomer, step_rhombic_dimer, step_linear_dimer; each value a float in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Six adsorption energies (in eV) for LiF monomer, rhombic dimer, linear dimer on terrace and at [10-1] step.
- schema:
  - `type`: object
  - `required`:
    - `terrace_monomer`: number
    - `terrace_rhombic_dimer`: number
    - `terrace_linear_dimer`: number
    - `step_monomer`: number
    - `step_rhombic_dimer`: number
    - `step_linear_dimer`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "terrace_monomer": "number",
          "terrace_rhombic_dimer": "number",
          "terrace_linear_dimer": "number",
          "step_monomer": "number",
          "step_rhombic_dimer": "number",
          "step_linear_dimer": "number"
        }
      },
      "description": "Six adsorption energies (in eV) for LiF monomer, rhombic dimer, linear dimer on terrace and at [10-1] step."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will score each required artifact. The main scored artifact is `/app/outputs/adsorption_energies.json`. The verifier compares each reported adsorption energy against a hidden reference value using a tolerance that allows for the normal spread of independent re-implementations but excludes unreasonable guesses. It also checks that the submitted energies satisfy internal consistency and expected physical trends (such as the relative ordering of binding strengths at different sites). The preceding process steps (`free_mol_energies.json` and `relaxed_surface_step.json`) are not individually scored, but their evidence files must be present to confirm that the pipeline was executed. The final reward is a weighted combination of the scores for all scored artifacts.
