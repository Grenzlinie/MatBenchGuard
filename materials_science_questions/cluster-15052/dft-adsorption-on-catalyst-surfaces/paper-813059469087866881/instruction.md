# Conformational and Frontier Orbital Analysis of Substituted Diphenyldisulfides

## Problem background
Sulfided NiMo catalysts selectively hydrogenolyze the sulfur–sulfur bond in para-substituted diphenyldisulfides (X‑DPDS) to produce the corresponding thiols, yet one particular substituent dramatically changes the reaction pathway, suppressing S–S cleavage in favor of attacking the substituent itself. Understanding why requires a molecular‑level picture of how the disulfide adsorbs on the catalyst surface. The adsorption mode — whether the molecule binds through its disulfide bridge or through some other functional group — determines which bonds are activated. Computational modeling of the free molecule can predict the preferred binding site by examining two factors: the accessibility of the S–S bond (governed by the molecular conformation) and the availability of low‑energy empty orbitals that can accept electron density from the metal surface. This task reproduces that computational analysis: first, determine the most stable conformation of each X‑DPDS to evaluate if the S–S bond is sterically exposed; second, compute the frontier molecular orbitals to identify which part of the molecule is most likely to interact with the catalyst.

## Approach
First, build reasonable starting geometries for six para‑substituted diphenyldisulfides (X = H, CH₃, Cl, OH, NH₂, NO₂) and find the lowest‑energy conformation of each using a molecular mechanics (force‑field) optimization. For the optimized structures, calculate the dihedral angle around the disulfide C–S–S–C unit; a common value across substituents would indicate that the S–S bond is consistently accessible. Second, take the optimized geometries of the unsubstituted (H‑DPDS) and nitro‑substituted (NO₂‑DPDS) molecules and perform extended Hückel molecular orbital calculations using the supplied atomic parameters (orbital energies and Slater exponents). From the resulting molecular orbital energies and atom‑wise compositions, identify the highest occupied molecular orbital (HOMO) and the lowest unoccupied molecular orbital (LUMO) for each molecule. The central question is whether the frontier orbitals of the two molecules differ in a way that shifts the preferred adsorption site from the disulfide bridge to the substituent. No experimental data are needed beyond the molecular structures and the parameter table; the computation itself generates the quantities of interest.

## Reproduction target
Produce two output files:
1. A multi‑molecule XYZ file (`geometry_optimized.xyz`) containing the Cartesian coordinates of the lowest‑energy conformer for each of the six X‑DPDS molecules.
2. A JSON file (`orbital_energies.json`) that contains, for H‑DPDS and NO₂‑DPDS, the HOMO energy, the LUMO energy, and the atom‑resolved composition (fractional contribution) of the HOMO and LUMO.
The verifier will compute the C–S–S–C dihedral angle from your optimized geometries and check whether it falls within the expected range for an exposed disulfide bond. It will then inspect the orbital energies and compositions to assess whether the electronic structure of NO₂‑DPDS plausibly favors adsorption through the nitro group rather than through the S–S bond, and whether the HOMO of H‑DPDS is dominated by sulfur lone pairs, consistent with the disulfide being the primary binding site.

## Assets

- RDKit (cheminformatics toolkit with molecular mechanics support): pip install rdkit-pypi -i https://pypi.tuna.tsinghua.edu.cn/simple
- Extended Hückel implementation (e.g., pyaehmop): https://github.com/qsnakes/pyaehmop
- Extended Hückel parameters (Table 2) for H, C, N, O, S, Cl

## Workflow steps

### Step 1: Molecular mechanics conformational optimization
- Role: scored (load-bearing)
- Action: For each para-substituted diphenyldisulfide (X = H, CH3, Cl, OH, NH2, NO2), perform molecular mechanics optimization to find the lowest-energy conformation. Write the optimized Cartesian coordinates of all six molecules to geometry_optimized.xyz.
- Output file: `/app/outputs/geometry_optimized.xyz`
- Format: txt
- Contract: Standard multi-molecule XYZ format: comment line per molecule (can include substructure name), followed by atom lines with element symbol and x, y, z coordinates.
- Scoring: scored by hidden verifier

### Step 2: Extended Hückel molecular orbital calculation
- Role: scored (load-bearing)
- Action: Using the optimized geometry from step_geometry and the provided extended Hückel parameters, compute the molecular orbitals for H-DPDS and NO2-DPDS. Output the HOMO and LUMO energies (in eV) and per-atom orbital compositions in a JSON file.
- Output file: `/app/outputs/orbital_energies.json`
- Format: json
- Contract: Keys: H_DPDS, NO2_DPDS. Each object has HOMO_energy (float, eV), LUMO_energy (float, eV), HOMO_composition (dict of string->float), LUMO_composition (dict). Compositions must sum to 1.0 within 0.01.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometry_optimized.xyz`
- `/app/outputs/orbital_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometry_optimized.xyz
- path: `/app/outputs/geometry_optimized.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized atomic coordinates for all six molecules. The checker recomputes the CSSC dihedral angle for each and verifies it is within 5° of 90°, scoring the structural property.
- schema:
  - `type`: text
  - `format_description`: Standard multi-molecule XYZ format: comment line per molecule (can include substructure name), followed by atom lines with element symbol and x, y, z coordinates.

### orbital_energies.json
- path: `/app/outputs/orbital_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: HOMO and LUMO energies (eV) and atom-wise compositions for H-DPDS and NO2-DPDS. The checker compares the LUMO energy of NO2-DPDS to the paper value (±0.5 eV tolerance), verifies that the HOMO of H-DPDS is dominated by sulfur lone pairs (S contribution > 50%), and checks the overall composition thresholds.
- schema:
  - `type`: object
  - `required_keys`: `H_DPDS`, `NO2_DPDS`
  - `structure`: Each key maps to an object with 'HOMO_energy' (float, eV), 'LUMO_energy' (float, eV), 'HOMO_composition' (dict mapping atom label to float), and 'LUMO_composition' (dict). Compositions should sum to 1.0 within tolerance.

Notes: Only the dry-lab computational sub-result is included; wet-lab catalytic experiments are excluded. The agent must perform geometry optimization and EH calculation using public tools or a self-implemented EH solver. The key output dihedral angle and frontier orbital energies/compositions are checked against the paper's reported values with appropriate tolerances. The task is compute-driven with no external data fetching beyond the bundled parameter file.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometry_optimized.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "format_description": "Standard multi-molecule XYZ format: comment line per molecule (can include substructure name), followed by atom lines with element symbol and x, y, z coordinates."
      },
      "description": "Optimized atomic coordinates for all six molecules. The checker recomputes the CSSC dihedral angle for each and verifies it is within 5° of 90°, scoring the structural property."
    },
    {
      "file": "orbital_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "H_DPDS",
          "NO2_DPDS"
        ],
        "structure": "Each key maps to an object with 'HOMO_energy' (float, eV), 'LUMO_energy' (float, eV), 'HOMO_composition' (dict mapping atom label to float), and 'LUMO_composition' (dict). Compositions should sum to 1.0 within tolerance."
      },
      "description": "HOMO and LUMO energies (eV) and atom-wise compositions for H-DPDS and NO2-DPDS. The checker compares the LUMO energy of NO2-DPDS to the paper value (±0.5 eV tolerance), verifies that the HOMO of H-DPDS is dominated by sulfur lone pairs (S contribution > 50%), and checks the overall composition thresholds."
    }
  ],
  "notes": "Only the dry-lab computational sub-result is included; wet-lab catalytic experiments are excluded. The agent must perform geometry optimization and EH calculation using public tools or a self-implemented EH solver. The key output dihedral angle and frontier orbital energies/compositions are checked against the paper's reported values with appropriate tolerances. The task is compute-driven with no external data fetching beyond the bundled parameter file."
}
```

## How you are scored
A hidden verifier will independently examine each of your submitted files. For `geometry_optimized.xyz`, it will compute the CSSC dihedral angle for every molecule and verify that the angle is compatible with an unobstructed disulfide bridge. For `orbital_energies.json`, it will extract the frontier orbital energies and compositions and compare them to expected qualitative trends and quantitative thresholds; for example, it will check whether the LUMO of NO₂‑DPDS falls within a specific energy window that would make it an effective electron acceptor, and whether the HOMO of H‑DPDS is primarily localized on the sulfur atoms. Both artifacts carry a weighted portion of the total reward; reporting numbers that appear plausible is not sufficient — the verifier reads the raw geometric and electronic data from your files and scores them against hidden criteria. Tolerances are applied to accommodate differences in implementation details, but the results must be physically meaningful and consistent with the adsorption model described in the approach.
