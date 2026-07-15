# DFT Energy Profile for NHC-Catalyzed CO2 Hydrosilylation

## Problem background
The reaction of CO2 with hydrosilanes catalyzed by N-heterocyclic carbenes (NHCs) is a promising metal-free CO2 reduction route. Understanding the mechanism and energy landscape is critical. This task concentrates on the DFT-computed energy profile for the reaction of the imidazolium carboxylate Imes-CO2 with diphenylsilane (Ph2SiH2). The mechanism involves a three-step cascade: (1) hydrosilylation to a formoxysilane-NHC adduct, (2) further hydrosilylation to a bis(silylacetal)-NHC adduct, (3) rearrangement and hydride transfer to yield silyl methoxide and free NHC. The goal is to compute the relative energies of all stationary points along this pathway and to determine the activation barriers and overall reaction energy.

## Approach
Use density functional theory (DFT) with the B3LYP functional and the 6-31G basis set in the gas phase. Construct initial molecular structures for the reactants (Imes-CO2 and Ph2SiH2), the transition states (TS1, TS2, TS3), the formoxysilane-NHC adduct (Int1), the bis(silylacetal)-NHC adduct (Int2), and the final product (silyl methoxide and free NHC). Perform geometry optimizations and transition state searches (with IRC calculations if needed) to locate stationary points. Compute the total electronic energy (in Hartree) for each optimized structure. Then calculate relative energies (kcal/mol) with respect to the reactants. An open-source DFT code such as NWChem, ORCA, or PySCF should be used. RDKit (optional) can assist in building initial geometries.

## Reproduction target
Write a JSON file `/app/outputs/energy_profile.json` containing the relative energies (kcal/mol) for each key: `reactants` (set to 0.0), `TS1`, `Int1`, `TS2`, `Int2`, `TS3`, `product`. The numbers must be computed from the DFT total energies.

## Assets

- NWChem: https://github.com/nwchemgit/nwchem
- RDKit: https://pypi.org/project/rdkit/

## Workflow steps

### Step 1: DFT calculation of reaction pathway
- Role: process
- Action: Construct the molecular structures for all species (Imes, CO2, Imes-CO2, Ph2SiH2, the formoxysilane-NHC adduct, bis(silylacetal)-NHC adduct, free NHC, silyl methoxide, and the transition states TS1, TS2, TS3). Run gas-phase DFT geometry optimizations and intrinsic reaction coordinate calculations to locate stationary points using the B3LYP functional and the 6-31G basis set with an open-source code (NWChem, ORCA, or PySCF). Compute the total electronic energy (Hartree) for each optimized structure.
- Evidence: `/app/outputs/dft_energies.csv`

### Step 2: Extract relative energy profile
- Role: scored (load-bearing)
- Action: Read the computed total energies from the DFT output. Compute the relative energies (kcal/mol) with respect to the reactants (Imes-CO2 + Ph2SiH2). Write a JSON file with the keys reactants, TS1, Int1, TS2, Int2, TS3, product.
- Output file: `/app/outputs/energy_profile.json`
- Format: json
- Contract: Object with keys: reactants (float, must be 0.0), TS1, Int1, TS2, Int2, TS3, product. All values are relative energies in kcal/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_profile.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_profile.json
- path: `/app/outputs/energy_profile.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The agent's computed relative energies. The checker will derive activation barriers and overall reaction energy, compare against hidden gold values with tolerances, and verify the monotonic energy ordering (Int1 < reactants, Int2 < Int1, product < Int2).
- schema:
  - `type`: object
  - `required`: `reactants`, `TS1`, `Int1`, `TS2`, `Int2`, `TS3`, `product`
  - `description`: Each value is a relative energy in kcal/mol. reactants must be 0.0.

Notes: The DFT procedure uses gas-phase B3LYP/6-31G. Any open-source DFT code is acceptable. The checker tests both the numerical values and the required downward trend.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_profile.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "reactants",
          "TS1",
          "Int1",
          "TS2",
          "Int2",
          "TS3",
          "product"
        ],
        "description": "Each value is a relative energy in kcal/mol. reactants must be 0.0."
      },
      "description": "The agent's computed relative energies. The checker will derive activation barriers and overall reaction energy, compare against hidden gold values with tolerances, and verify the monotonic energy ordering (Int1 < reactants, Int2 < Int1, product < Int2)."
    }
  ],
  "notes": "The DFT procedure uses gas-phase B3LYP/6-31G. Any open-source DFT code is acceptable. The checker tests both the numerical values and the required downward trend."
}
```

## How you are scored
A hidden verifier reads your `energy_profile.json`. It derives the activation barriers (TS1, TS2, TS3) and the overall reaction energy (product − reactants). These derived quantities are compared against hidden reference values with appropriate tolerances. Additionally, the verifier checks the energetic trend: Int1 lower than reactants, Int2 lower than Int1, and product lower than Int2. The reward is a weighted combination of the barrier/overall energy accuracy and the trend check. The verifier's criteria and tolerances are not revealed; your task is to compute the best DFT energies you can using the specified level of theory.
