# DFT Reaction Energy Profile for Ethylene Insertion into Si(II)–Sn Bond

## Problem background
The migratory insertion of alkenes is a fundamental process in organometallic chemistry, typically catalyzed by transition metals. Recent experimental work has shown that a silicon(II)–tin bond in a silylene‑phosphine complex can undergo reversible, catalyst‑free insertion of unactivated alkenes such as ethylene under mild conditions. To understand the reaction mechanism and the origin of the reversibility, density functional theory (DFT) calculations were performed to map the full reaction coordinate. This task reproduces the computationally derived reaction energy profile for ethylene insertion into the Si(II)–Sn bond of the silylene‑phosphine complex 1a‑Sn, providing insight into the two‑step mechanism ([2+1] cycloaddition followed by migratory insertion).

## Approach
The computational approach employs DFT at the M06/SDD/6‑31G(d,p) level of theory. The method uses the SDD effective core potential for tin and the 6‑31G(d,p) basis set for all other atoms. Starting from publicly available crystal structures of the reactant complex 1a‑Sn and the product complex 2a‑Sn, as well as a model of ethylene, initial 3D geometries are constructed. Geometry optimizations and transition‑state searches are performed to locate the five stationary points along the ethylene insertion pathway: separated reactants, the [2+1] cycloaddition transition state (TS1), the intermediate adduct (4a‑Sn), the migratory insertion transition state (TS2), and the final product. Harmonic vibrational frequency calculations at 298 K yield Gibbs free energy corrections. Relative Gibbs free energies (kcal/mol) are derived by referencing each species to the separated reactants. Any open‑source quantum chemistry package that supports the M06 functional, SDD basis, and Pople basis sets is suitable.

## Reproduction target
The target is to compute and report the stationary points and their relative Gibbs free energies for the ethylene insertion pathway of complex 1a‑Sn. Specifically, you must produce two artifacts:

1. **stationary_point_energies.json** – A JSON file containing, for each of the five species (separated reactants, TS1, intermediate 4a‑Sn, TS2, and product 2a‑Sn), the electronic energy (Hartree), the Gibbs free energy correction at 298 K (Hartree), and the corresponding relative electronic and relative Gibbs free energies (kcal/mol) referenced to the separated reactants.

2. **optimized_geometries.xyz** – A multi‑frame XYZ file providing the optimized Cartesian coordinates of all five stationary points, in the order listed above, with each frame labelled by the structure name.

The results should be obtained at the M06/SDD/6‑31G(d,p) level of theory. The task is to produce a self‑consistent energy profile that reflects the two‑step insertion mechanism, without requiring a comparison to any pre‑specified numerical benchmark.

## Assets

- Crystal structure of 1a-Sn (CCDC 935560): https://www.ccdc.cam.ac.uk/data_request/cif?ccdc=935560
- Crystal structure of 2a-Sn (CCDC 935561): https://www.ccdc.cam.ac.uk/data_request/cif?ccdc=935561
- Open-source quantum chemistry software
- M06/SDD(Sn)/6-31G(d,p) level of theory

## Workflow steps

### Step 1: Build initial molecular models
- Role: process
- Action: Construct initial 3D structures for all species along the ethylene insertion path of 1a‑Sn. Use published X‑ray structures of 1a‑Sn and 2a‑Sn (CCDC 935560, 935561) as templates; generate reasonable transition-state guesses for the [2+1] cycloaddition and migratory insertion steps using chemical intuition and standard techniques.
- Evidence: `/app/outputs/initial_geometries.xyz`

### Step 2: DFT reaction profile computation
- Role: process
- Action: Perform geometry optimizations, transition-state searches, and harmonic vibrational frequency analyses at the M06/SDD(Sn)/6-31G(d,p) level of theory to locate the stationary points: separated reactants (1a‑Sn + C₂H₄), the [2+1] cycloaddition TS (TS1), the intermediate 4a‑Sn, the migratory insertion TS (TS2), and the final product 2a‑Sn. Obtain electronic energies and Gibbs free energy corrections at 298 K.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 3: Report relative Gibbs free energies
- Role: scored (load-bearing)
- Action: Extract electronic energies and Gibbs free energy corrections from the DFT output files, compute relative Gibbs free energies (kcal/mol) referenced to separated reactants, and write the result to the JSON file.
- Output file: `/app/outputs/stationary_point_energies.json`
- Format: json
- Contract: JSON object with keys 'separated_reactants', 'ts1_cycloaddition', 'intermediate_4a-Sn', 'ts2_insertion', 'product_2a-Sn'. Each value is an object with numeric fields 'E_elec_hartree', 'G_corr_hartree', 'rel_E_elec_kcal', 'rel_G_kcal'.
- Scoring: scored by hidden verifier

### Step 4: Report optimized geometries
- Role: scored (load-bearing)
- Action: Collect the optimized Cartesian coordinates for all five stationary points and write them as a multi-frame XYZ file in the specified order.
- Output file: `/app/outputs/optimized_geometries.xyz`
- Format: txt
- Contract: Multi-frame XYZ file. Each frame: first line = number of atoms, second line = structure label, subsequent lines = element and x y z coordinates in Å. Five frames in order: reactants, ts1_cycloaddition, intermediate (4a-Sn), ts2_insertion, product (2a-Sn).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stationary_point_energies.json`
- `/app/outputs/optimized_geometries.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stationary_point_energies.json
- path: `/app/outputs/stationary_point_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Relative Gibbs free energy profile (kcal/mol) referenced to separated reactants.
- schema:
  - `type`: object
  - `required`:
    - `separated_reactants`:
      - `E_elec_hartree`: number
      - `G_corr_hartree`: number
      - `rel_E_elec_kcal`: number
      - `rel_G_kcal`: number
    - `ts1_cycloaddition`:
      - `E_elec_hartree`: number
      - `G_corr_hartree`: number
      - `rel_E_elec_kcal`: number
      - `rel_G_kcal`: number
    - `intermediate_4a-Sn`:
      - `E_elec_hartree`: number
      - `G_corr_hartree`: number
      - `rel_E_elec_kcal`: number
      - `rel_G_kcal`: number
    - `ts2_insertion`:
      - `E_elec_hartree`: number
      - `G_corr_hartree`: number
      - `rel_E_elec_kcal`: number
      - `rel_G_kcal`: number
    - `product_2a-Sn`:
      - `E_elec_hartree`: number
      - `G_corr_hartree`: number
      - `rel_E_elec_kcal`: number
      - `rel_G_kcal`: number

### optimized_geometries.xyz
- path: `/app/outputs/optimized_geometries.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized Cartesian coordinates of all five stationary points.
- schema:
  - `type`: text
  - `description`: Multi-frame XYZ; five frames in order: reactants, ts1_cycloaddition, intermediate (4a-Sn), ts2_insertion, product (2a-Sn).

Notes: The DFT calculation is computationally intensive; the solving agent is expected to use a suitable quantum chemistry code on external HPC resources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stationary_point_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "separated_reactants": {
            "E_elec_hartree": "number",
            "G_corr_hartree": "number",
            "rel_E_elec_kcal": "number",
            "rel_G_kcal": "number"
          },
          "ts1_cycloaddition": {
            "E_elec_hartree": "number",
            "G_corr_hartree": "number",
            "rel_E_elec_kcal": "number",
            "rel_G_kcal": "number"
          },
          "intermediate_4a-Sn": {
            "E_elec_hartree": "number",
            "G_corr_hartree": "number",
            "rel_E_elec_kcal": "number",
            "rel_G_kcal": "number"
          },
          "ts2_insertion": {
            "E_elec_hartree": "number",
            "G_corr_hartree": "number",
            "rel_E_elec_kcal": "number",
            "rel_G_kcal": "number"
          },
          "product_2a-Sn": {
            "E_elec_hartree": "number",
            "G_corr_hartree": "number",
            "rel_E_elec_kcal": "number",
            "rel_G_kcal": "number"
          }
        }
      },
      "description": "Relative Gibbs free energy profile (kcal/mol) referenced to separated reactants."
    },
    {
      "file": "optimized_geometries.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "description": "Multi-frame XYZ; five frames in order: reactants, ts1_cycloaddition, intermediate (4a-Sn), ts2_insertion, product (2a-Sn)."
      },
      "description": "Optimized Cartesian coordinates of all five stationary points."
    }
  ],
  "notes": "The DFT calculation is computationally intensive; the solving agent is expected to use a suitable quantum chemistry code on external HPC resources."
}
```

## How you are scored
A hidden verifier reads your submitted artifacts and independently scores them.
- For `stationary_point_energies.json`, the verifier checks that the relative Gibbs free energies follow a physically plausible ordering (transition states higher than their flanking minima) and fall within a reasonable range consistent with the reaction being feasible at mild temperatures. The exact numerical tolerances are hidden and account for differences between quantum chemistry codes.
- For `optimized_geometries.xyz`, the verifier extracts key bond lengths of the reactant 1a‑Sn and product 2a‑Sn and compares them to published crystallographic reference values.

The two checks are combined into a single reward score between 0 and 1. There is no need to guess a target number; the verifier judges the structural and energetic consistency of your results.
