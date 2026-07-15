# DFT Solvation and Binding Energy Analysis of Hexa-Aqua Iron Complexes

## Problem background
Pyrite (FeS₂) scale formation in oil and gas wells impedes fluid flow and causes formation damage. A new green borax-based formulation has been proposed for pyrite removal. The mechanism involves oxidation of Fe²⁺ to Fe³⁺, which is hypothesized to enhance water binding and solubility. Density functional theory (DFT) calculations on hexa-aqua iron complexes provide an atomic-level test of this hypothesis by probing how the iron oxidation state affects Fe–O bond distances, binding energy stability, and solvation free energy. This task reproduces those computational experiments, so we can independently assess the relationship between oxidation and solvation.

## Approach
We study the octahedral [Fe(H₂O)₆]²⁺ (quintet spin) and [Fe(H₂O)₆]³⁺ (sextet spin) complexes, along with isolated Fe²⁺/Fe³⁺ ions and a water hexamer cluster, using DFT at the B3LYP/def2-TZVP level. Geometries are fully optimized in vacuum and in implicit water solvent (PCM). Vibrational frequency analysis confirms true minima. From the solvent-phase optimized structures we extract the six Fe–O bond distances; compute the binding energy ΔE_binding = E(complex) – [E(Fe ion) + E(water hexamer)]; and obtain the solvation free energy ΔG_solv = E(solvent‑optimized) – E(vacuum‑optimized). All energy values are converted to kcal/mol. The results are collected in a single JSON file.

## Reproduction target
Produce a JSON file at `/app/outputs/dft_results.json` containing, for both Fe²⁺(H₂O)₆ and Fe³⁺(H₂O)₆, the six Fe–O bond lengths (in Å, labelled Fe‑O2, Fe‑O5, Fe‑O8, Fe‑O11, Fe‑O14, Fe‑O17), the binding energy (in kcal/mol), and the solvation free energy (in kcal/mol). The file must conform to the schema described in the Output Contract. The verifier will compare each value to reference standards and check internal consistency (e.g., that the bond lengths and energies are physically consistent between the two oxidation states).

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/
- def2-TZVP basis set

## Workflow steps

### Step 1: Build initial molecular structures
- Role: process
- Action: Construct initial coordinates for the octahedral hexa-aqua iron complexes [Fe(H2O)6]2+ (quintet spin) and [Fe(H2O)6]3+ (sextet spin), the isolated Fe2+/Fe3+ ions, and a water hexamer cluster (H2O)6. Use standard bond lengths and angles; exact initial geometry is not critical as optimization will relax it.
- Evidence: `/app/outputs/initial_structures.xyz`

### Step 2: DFT geometry optimization and energy calculations
- Role: process
- Action: For each species (Fe2+(H2O)6, Fe3+(H2O)6, Fe2+, Fe3+, and (H2O)6) perform geometry optimization and vibrational frequency analysis in vacuum and with PCM implicit water solvent using B3LYP/def2-TZVP. Confirm that all optimized structures are true minima (no imaginary frequencies). Retain total electronic energies and the final optimized coordinates.
- Evidence: `/app/outputs/dft_output_logs.txt`

### Step 3: Compute bond lengths, binding energies, and solvation free energies
- Role: scored (load-bearing)
- Action: From the solvent-phase optimized geometries, extract the six Fe-O bond distances (O2, O5, O8, O11, O14, O17 as per the paper's labeling). Compute the binding energy for each complex using ΔE_binding = E(complex) - (E(Fe ion) + E(water hexamer)), where all energies are the solvent-phase optimized total electronic energies. Compute the solvation free energy as ΔG_solv = E(optimized in solvent) - E(optimized in vacuum). Write all values to dft_results.json.
- Output file: `/app/outputs/dft_results.json`
- Format: json
- Contract: {"type": "object", "required": ["Fe2+", "Fe3+"], "properties": {"Fe2+": {"type": "object", "required": ["bond_lengths", "binding_energy_kcal_mol", "solvation_energy_kcal_mol"], "properties": {"bond_lengths": {"type": "object", "required": ["Fe-O2", "Fe-O5", "Fe-O8", "Fe-O11", "Fe-O14", "Fe-O17"], "properties": {"Fe-O2": {"type": "number"}, "Fe-O5": {"type": "number"}, "Fe-O8": {"type": "number"}, "Fe-O11": {"type": "number"}, "Fe-O14": {"type": "number"}, "Fe-O17": {"type": "number"}}}, "binding_energy_kcal_mol": {"type": "number"}, "solvation_energy_kcal_mol": {"type": "number"}}}, "Fe3+": {"type": "object", "required": ["bond_lengths", "binding_energy_kcal_mol", "solvation_energy_kcal_mol"], "properties": {"bond_lengths": {"type": "object", "required": ["Fe-O2", "Fe-O5", "Fe-O8", "Fe-O11", "Fe-O14", "Fe-O17"], "properties": {"Fe-O2": {"type": "number"}, "Fe-O5": {"type": "number"}, "Fe-O8": {"type": "number"}, "Fe-O11": {"type": "number"}, "Fe-O14": {"type": "number"}, "Fe-O17": {"type": "number"}}}, "binding_energy_kcal_mol": {"type": "number"}, "solvation_energy_kcal_mol": {"type": "number"}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dft_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dft_results.json
- path: `/app/outputs/dft_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: DFT-computed bond lengths (in Å) and energies (in kcal/mol) for Fe2+(H2O)6 and Fe3+(H2O)6. The hidden checker compares the reported numbers to the paper's reference values with tolerances and verifies the directional trends: Fe3+ must have systematically shorter bond lengths, more negative binding energy, and more negative solvation energy than Fe2+.
- schema:
  - `type`: object
  - `required`:
    - `Fe2+`:
      - `type`: object
      - `required`:
        - `bond_lengths`:
          - `type`: object
          - `required`:
            - `Fe-O2`: number
            - `Fe-O5`: number
            - `Fe-O8`: number
            - `Fe-O11`: number
            - `Fe-O14`: number
            - `Fe-O17`: number
        - `binding_energy_kcal_mol`: number
        - `solvation_energy_kcal_mol`: number
    - `Fe3+`:
      - `type`: object
      - `required`:
        - `bond_lengths`:
          - `type`: object
          - `required`:
            - `Fe-O2`: number
            - `Fe-O5`: number
            - `Fe-O8`: number
            - `Fe-O11`: number
            - `Fe-O14`: number
            - `Fe-O17`: number
        - `binding_energy_kcal_mol`: number
        - `solvation_energy_kcal_mol`: number

Notes: The task reproduces the computational DFT analysis only; experimental dissolution kinetics and corrosion tests are omitted. The workflow is compute-heavy due to multiple geometry optimizations at the B3LYP/def2-TZVP level.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dft_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Fe2+": {
            "type": "object",
            "required": {
              "bond_lengths": {
                "type": "object",
                "required": {
                  "Fe-O2": "number",
                  "Fe-O5": "number",
                  "Fe-O8": "number",
                  "Fe-O11": "number",
                  "Fe-O14": "number",
                  "Fe-O17": "number"
                }
              },
              "binding_energy_kcal_mol": "number",
              "solvation_energy_kcal_mol": "number"
            }
          },
          "Fe3+": {
            "type": "object",
            "required": {
              "bond_lengths": {
                "type": "object",
                "required": {
                  "Fe-O2": "number",
                  "Fe-O5": "number",
                  "Fe-O8": "number",
                  "Fe-O11": "number",
                  "Fe-O14": "number",
                  "Fe-O17": "number"
                }
              },
              "binding_energy_kcal_mol": "number",
              "solvation_energy_kcal_mol": "number"
            }
          }
        }
      },
      "description": "DFT-computed bond lengths (in Å) and energies (in kcal/mol) for Fe2+(H2O)6 and Fe3+(H2O)6. The hidden checker compares the reported numbers to the paper's reference values with tolerances and verifies the directional trends: Fe3+ must have systematically shorter bond lengths, more negative binding energy, and more negative solvation energy than Fe2+."
    }
  ],
  "notes": "The task reproduces the computational DFT analysis only; experimental dissolution kinetics and corrosion tests are omitted. The workflow is compute-heavy due to multiple geometry optimizations at the B3LYP/def2-TZVP level."
}
```

## How you are scored
A hidden verifier reads `dft_results.json` and independently compares each reported value against a set of reference values and structural expectations. Reward is monotonic in accuracy: full credit if all comparisons satisfy the required agreements; partial credit is awarded for individual metrics that meet the thresholds. Simply reporting a number is not sufficient—the values must be the result of a genuine DFT calculation at the specified level of theory. The verifier's tolerances are generous enough to absorb routine toolchain variability, but the workflow must be executed to obtain realistic numbers.
