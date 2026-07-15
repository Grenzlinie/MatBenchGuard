# Reaction Mechanism of HCSi⁻ with CO₂

## Problem background
The reaction of the silicoacetylide anion (HCSi⁻) with CO₂ has been observed to produce the HCCO⁻ anion and SiO. Understanding the reaction mechanism at the molecular level is important for silicon chemistry and astrochemistry. Quantum chemical calculations can map the potential energy surface and determine the relative stabilities of intermediates and transition states, revealing the stepwise pathway. This task focuses on reproducing the key energetic features and a structural parameter for the CO₂ reaction path.

## Approach
Use an open‑source quantum chemistry package to perform geometry optimizations and vibrational frequency analyses at the RHF/6‑31G* level for the separated reactants (HCSi⁻ + CO₂) and the five stationary points along the reaction pathway: a four‑membered ring intermediate, the ring‑opening transition state, an open form, a chain form, and the dissociation products HCCO⁻ + SiO. Initial geometries should be constructed from the structural descriptions available in the literature. After confirming each stationary point as a minimum or transition state, compute single‑point energies at the MP2/6‑31++G** level on the optimized geometries. Apply zero‑point energy (ZPE) corrections from the RHF frequency calculations. Finally, compute the relative energy (kcal/mol) of each stationary point with respect to the sum of the optimized reactants, and extract the CSi bond length from the ring intermediate.

## Reproduction target
Produce the following quantities at the MP2/6‑31++G**//RHF/6‑31G* + ZPE level:
- Relative energies (kcal/mol) of the ring intermediate, ring‑opening transition state, open form, chain form, and products (HCCO⁻ + SiO) with respect to separated HCSi⁻ + CO₂.
- The CSi bond length (Å) in the ring intermediate.
Report these in the output file results.json, and compile the full quantum chemistry data (XYZ geometries, total energies, ZPE, and relative energies) for all stationary points in stationary_points.json.

## Assets

- Open-source quantum chemistry package: https://psicode.org/

## Workflow steps

### Step 1: Optimize reactant species and compute reference energies
- Role: process
- Action: Perform RHF/6-31G* geometry optimization and harmonic frequency analysis for HCSi⁻ (linear HC≡Si⁻) and for CO₂, confirming both are minima. Then compute MP2/6-31++G** single-point energies and zero-point energy (ZPE) corrections. Record total RHF energy, MP2 energy, and ZPE for each reactant.
- Evidence: `/app/outputs/reactants_energies.json`

### Step 2: Optimize stationary points on the HCSi⁻ + CO₂ reaction path
- Role: process
- Action: For each stationary point (the four‑membered ring intermediate, the ring‑opening transition state, the open form, the chain form, and the separated products HCCO⁻ + SiO), perform RHF/6-31G* geometry optimization and harmonic frequency analysis (confirming minimum or TS character). Then compute MP2/6-31++G** single-point energies and ZPE corrections. Use initial geometries derived from the structural descriptions in the paper's Figure 1.
- Evidence: `/app/outputs/stationary_points_raw.json`

### Step 3: Compute relative energies and key bond length
- Role: scored (load-bearing)
- Action: From the MP2/6-31++G**+ZPE total energies of reactants (step 01) and each stationary point (step 02), calculate the relative energy (kcal/mol) of the ring, ring‑opening TS, open form, chain form, and products with respect to separated HCSi⁻ + CO₂. Extract the CSi bond length (Å) from the optimized ring geometry. Write the results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Object with keys: 'ring_relative_energy' (float, kcal/mol), 'TS_relative_energy' (float, kcal/mol), 'open_relative_energy' (float, kcal/mol), 'chain_relative_energy' (float, kcal/mol), 'products_relative_energy' (float, kcal/mol), 'ring_CSi_bond_length' (float, Angstrom).
- Scoring: scored by hidden verifier

### Step 4: Compile stationary point data
- Role: scored
- Action: Collect the optimized XYZ geometries, RHF total energies, MP2 total energies, ZPE, and relative energies (computed as in step 03) for each stationary point into a structured JSON array. Write the full dataset to stationary_points.json.
- Output file: `/app/outputs/stationary_points.json`
- Format: json
- Contract: Array of objects, each with keys: 'label' (string, e.g. 'ring', 'TS', 'open', 'chain', 'products'), 'xyz' (string in XYZ format), 'RHF_energy' (float, hartrees), 'MP2_energy' (float, hartrees), 'ZPE' (float, hartrees), 'relative_energy' (float, kcal/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`
- `/app/outputs/stationary_points.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The five relative energies of the reaction pathway and the CSi bond length in the ring intermediate, all computed at MP2/6-31++G**//RHF/6-31G* with ZPE corrections. The checker compares these values against the paper's reported results.
- schema:
  - `type`: object
  - `required`:
    - `ring_relative_energy`: float (kcal/mol)
    - `TS_relative_energy`: float (kcal/mol)
    - `open_relative_energy`: float (kcal/mol)
    - `chain_relative_energy`: float (kcal/mol)
    - `products_relative_energy`: float (kcal/mol)
    - `ring_CSi_bond_length`: float (Angstrom)

### stationary_points.json
- path: `/app/outputs/stationary_points.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: All optimized stationary points with their quantum chemistry data. The checker performs a structural audit to confirm the correct species were studied.
- schema:
  - `type`: array
  - `items`:
    - `label`: string
    - `xyz`: string (XYZ format)
    - `RHF_energy`: float (hartrees)
    - `MP2_energy`: float (hartrees)
    - `ZPE`: float (hartrees)
    - `relative_energy`: float (kcal/mol)

Notes: The agent must use the RHF/6-31G* geometry level and MP2/6-31++G** energies as specified in the original study. No other basis sets or methods should be used for the geometry or energy evaluation.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "ring_relative_energy": "float (kcal/mol)",
          "TS_relative_energy": "float (kcal/mol)",
          "open_relative_energy": "float (kcal/mol)",
          "chain_relative_energy": "float (kcal/mol)",
          "products_relative_energy": "float (kcal/mol)",
          "ring_CSi_bond_length": "float (Angstrom)"
        }
      },
      "description": "The five relative energies of the reaction pathway and the CSi bond length in the ring intermediate, all computed at MP2/6-31++G**//RHF/6-31G* with ZPE corrections. The checker compares these values against the paper's reported results."
    },
    {
      "file": "stationary_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "array",
        "items": {
          "label": "string",
          "xyz": "string (XYZ format)",
          "RHF_energy": "float (hartrees)",
          "MP2_energy": "float (hartrees)",
          "ZPE": "float (hartrees)",
          "relative_energy": "float (kcal/mol)"
        }
      },
      "description": "All optimized stationary points with their quantum chemistry data. The checker performs a structural audit to confirm the correct species were studied."
    }
  ],
  "notes": "The agent must use the RHF/6-31G* geometry level and MP2/6-31++G** energies as specified in the original study. No other basis sets or methods should be used for the geometry or energy evaluation."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier. The verifier reads your results.json and stationary_points.json. It compares your reported relative energies and bond length against expected reference values, using tolerances that account for variations between computational implementations. It also performs a structural audit to confirm that all required stationary points are present and have plausible geometries and energies. The final reward is a weighted combination of these checks; simply reporting a number without performing the underlying calculations will not pass.
