# DFT Calculation of Activation Energies for Siloxane Cross-Linking with Hydrolyzed Alumatrane

## Problem background
Polymer-derived ceramics based on silicon oxycarbide compositions exhibit excellent thermomechanical stability, but their final properties depend critically on the cross‑linking mechanisms during the sol‑gel process. Commercial polysiloxanes contain only a limited number of reactive hydroxy and alkoxy groups, yet gelation with alumatrane has been observed to proceed only when traces of water are present. This suggests that hydrolysis of alumatrane generates Al–OH groups that can react not only with terminal functional groups on the polysiloxane but also potentially with the Si–O–Si backbone. A quantitative understanding of the activation energy barriers for these condensation pathways is essential to rationalize the catalytic role of water and to guide the design of precursor formulations. This task aims to determine these barriers by computing the relative energies of key stationary points along the reaction paths for model systems that represent the different functional groups found in polysiloxanes.

## Approach
Density functional theory (DFT) is used to map the potential energy surface of three model condensation reactions between a hydrolyzed alumatrane cluster, Al2(OH)6, and a siloxane model cluster, (HO)H2SiR, where the substituent R = OH, OCH3, and OSiH3 represents hydroxy, methoxy, and siloxy functional groups, respectively. For each reaction, the following stationary points are located: separated reactants, reactant complex, transition state, product complex, and separated products.

First, geometry optimizations and transition state searches are performed at the B3LYP/6‑31G(d) level of theory. Each transition state is verified by following the intrinsic reaction coordinate (IRC) to the adjacent minima. Then the energies are refined by carrying out single‑point calculations on the optimized geometries at the BH&HLYP/6‑311+G(3df,2p) level. Finally, the relative energy (in kJ/mol) of each stationary point is calculated with respect to the separated reactants for every substituent R. This pipeline yields the reaction energy profiles and allows the activation barriers and reaction thermodynamics to be compared across the three substituent types.

## Reproduction target
Compute the relative energies (kJ/mol) of the reactant complex, transition state, product complex, and separate products with respect to the separated reactants for each of the three model reactions (R = OH, OCH3, OSiH3). Write the 12 values to the file `/app/outputs/step_01_relative_energies.json` according to the JSON schema specified in the output contract below.

## Assets

- ORCA quantum chemistry package (or equivalent open-source DFT code): https://orcaforum.kofo.mpg.de

## Workflow steps

### Step 1: Geometry optimization and transition state search
- Role: process
- Action: Construct initial molecular geometries for the Al2(OH)6 cluster and (HO)H2SiR clusters (R = OH, OCH3, OSiH3). Perform DFT geometry optimizations of all reactive species (separated reactants, reactant complexes, transition states, product complexes, separated products) at the B3LYP/6-31G(d) level of theory. For each reaction, locate the transition state using analytical Hessians and verify it by following the intrinsic reaction coordinate (IRC) path.
- Evidence: `/app/outputs/step_01_geom_opt.log`

### Step 2: Single-point energy refinement
- Role: process
- Action: Using the optimized geometries from Step 1, run single-point energy calculations at the BH&HLYP/6-311+G(3df,2p) level of theory for all stationary points.
- Evidence: `/app/outputs/step_02_sp_energy.log`

### Step 3: Compute relative energies and activation energies
- Role: scored (load-bearing)
- Action: From the single-point energies of Step 2, compute the relative energy (in kJ/mol) of the reactant complex, transition state, product complex, and separate products with respect to the separated reactants for each of the three model reactions (R = OH, OCH3, OSiH3). Write the 12 values into a JSON file.
- Output file: `/app/outputs/step_01_relative_energies.json`
- Format: json
- Contract: JSON object with keys 'R=OH', 'R=OCH3', 'R=OSiH3'. Each value is an object with keys 'reactant_complex', 'transition_state', 'product_complex', 'separate_products'. All values are floats in kJ/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_relative_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_relative_energies.json
- path: `/app/outputs/step_01_relative_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative energies of stationary points for the three model reactions, compared against hidden reference values with absolute tolerances and ordering check.
- schema:
  - `type`: object
  - `required`: `R=OH`, `R=OCH3`, `R=OSiH3`
  - `items`:
    - `reactant_complex`: number
    - `transition_state`: number
    - `product_complex`: number
    - `separate_products`: number
  - `units`:
    - `reactant_complex`: kJ/mol
    - `transition_state`: kJ/mol
    - `product_complex`: kJ/mol
    - `separate_products`: kJ/mol

Notes: The hidden checker compares each of the 12 numeric values to reference values with an absolute tolerance and also verifies the ordering of transition state energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_relative_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "R=OH",
          "R=OCH3",
          "R=OSiH3"
        ],
        "items": {
          "reactant_complex": "number",
          "transition_state": "number",
          "product_complex": "number",
          "separate_products": "number"
        },
        "units": {
          "reactant_complex": "kJ/mol",
          "transition_state": "kJ/mol",
          "product_complex": "kJ/mol",
          "separate_products": "kJ/mol"
        }
      },
      "description": "Relative energies of stationary points for the three model reactions, compared against hidden reference values with absolute tolerances and ordering check."
    }
  ],
  "notes": "The hidden checker compares each of the 12 numeric values to reference values with an absolute tolerance and also verifies the ordering of transition state energies."
}
```

## How you are scored
A hidden verifier reads your JSON output and compares each of the 12 relative energy values (kJ/mol) to a set of hidden reference values, using a tolerance that accounts for expected differences between quantum chemistry implementations. In addition, it examines the ordering of the three transition state energies across the R substituents. The final reward (a float between 0 and 1) is a weighted combination: the numeric energy comparisons contribute equally to a majority share of the score, while the ordering check accounts for the remainder. A reproduction that faithfully follows the specified theoretical methods and obtains energy profiles close to the reference will earn a high score; reporting numbers that merely appear plausible will not.
