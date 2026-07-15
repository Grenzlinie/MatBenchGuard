# DFT Protocol for Internal Ligand Strain Energies in Tridentate Pincer Ligands

## Problem background
Metal complexes of tridentate meridional pincer ligands, such as terpyridine and its pyrrolide-substituted analogues, experience internal ligand strain upon binding a metal ion. The 'relaxed' unbound geometry of these ligands is typically more open than the 'coordinated' geometry required to chelate a metal centre. Understanding and quantifying this strain is critical for rationalising and predicting physicochemical properties, including spin states and spin-crossover behaviour. In this task you will compute the internal ligand strain energy for a set of five parent pincer ligands and examine how it correlates with a simple geometric deformation: the relative change in the distance between the two terminal nitrogen donor atoms.

## Approach
The method uses vacuum-phase density functional theory (DFT) calculations to compute the strain energy for the five hypothetical zinc(II) complexes [Zn(L)]ᴿ⁺, where L = A (terpyridine), B⁻, C²⁻, D⁻, E²⁻ (see Figure 1 for scaffold drawings). The computational protocol works as follows:

1. **Coordinated geometry**: Perform a full geometry optimisation of each [Zn(L)]ᴿ⁺ complex at the B3LYP-GD3BJ/6-31G** level to obtain the metal-bound ligand coordinates.

2. **Frozen ligand energy** (ΔE_L(coord)): Harvest the ligand atom positions from the optimised complex, remove the Zn ion, fix all heavy-atom positions, and perform a single‑point energy calculation (B3LYP/6‑31G**) to obtain the electronic energy of the ligand frozen in its coordinated conformation.

3. **Relaxed ligand energy** (ΔE_L(relax)): Starting from the same ligand coordinates, perform a constrained geometry optimisation of the free ligand in vacuum at the B3LYP-GD3BJ/6-31G** level, while keeping the inter‑ring N–C–C–N torsion angles fixed at 0° to enforce the meridional syn,syn conformation. This yields the relaxed ligand energy and the reference geometric parameter ρ_L(relax).

4. **Strain energy and deformation**: Calculate ΔE_L(strain) = ΔE_L(coord) – ΔE_L(relax). Measure the terminal N···N donor separation ρ in both the coordinated and relaxed geometries and compute the relative deformation Δρ/ρ_L(relax) = (ρ_L(relax) – ρ_L(coord)) / ρ_L(relax).

5. **Correlation**: Perform a linear regression of ΔE_L(strain) against Δρ/ρ_L(relax) with the intercept forced through zero; the slope (units kJ mol⁻¹ per unit Δρ/ρ) is the primary quantitative result that relates strain to geometric deformation.

All calculations should be carried out with an open‑source DFT package (e.g., ORCA or PySCF) using the B3LYP exchange‑correlation functional, the 6-31G** basis set, and the GD3BJ dispersion correction. The workflow must be implemented as a series of reproducible steps, starting from manually built or SMILES‑generated initial 3D structures.

## Reproduction target
For the five ligands A, B⁻, C²⁻, D⁻, and E²⁻ in their hypothetical Zn(II) complexes, produce two scored artifacts:

- **ligand_strain_results.json**: A JSON array containing one object per ligand, each with fields `ligand` (one of `A`, `B`, `C`, `D`, `E`), `strain_energy_kJ_mol` (the computed ΔE_L(strain) in kJ mol⁻¹), and `delta_rho_over_rho_relax` (the relative terminal N···N separation change, unit‑less).

- **zero_intercept_slope.txt**: A text file containing a single floating‑point number – the slope obtained from a zero‑intercept linear regression of the five strain energy values against the five relative deformation values. The slope is expressed in kJ mol⁻¹ per unit Δρ/ρ.

These outputs represent the core quantitative results of the strain-deformation relationship for the training set of Zn(II) complexes.

## Assets

- Open-source DFT package (e.g., ORCA 5.x or PySCF): https://orcaforum.kofo.mpg.de/ (ORCA); https://pyscf.org/ (PySCF)
- 6-31G** (6-31G(d,p)) basis set: https://www.basissetexchange.org
- Molecular structure builder (e.g., RDKit, OpenBabel, or manual XYZ generation): https://www.rdkit.org or http://openbabel.org

## Workflow steps

### Step 1: Generate initial molecular geometries
- Role: process
- Action: Build initial 3D molecular structures for the five tridentate pincer ligand scaffolds (A, B⁻, C²⁻, D⁻, E²⁻) and their hypothetical Zn(II) complexes. Assign correct charge and multiplicity (closed‑shell singlet for Zn complexes).
- Evidence: none

### Step 2: DFT geometry optimizations of [Zn(L)]^{z+} complexes
- Role: process
- Action: Perform vacuum‑phase geometry optimization of each [Zn(L)]^{z+} complex using DFT (B3LYP functional, 6‑31G** basis set, GD3BJ dispersion). Verify minima via vibrational frequency analysis if possible.
- Evidence: none

### Step 3: Single‑point energy of frozen coordinated ligand (ΔE_L(coord))
- Role: process
- Action: For each ligand, harvest atomic coordinates from the optimized Zn complex, remove the Zn ion, fix all heavy‑atom positions, and perform a single‑point DFT energy calculation (B3LYP/6‑31G**) to obtain ΔE_L(coord).
- Evidence: none

### Step 4: Constrained geometry optimization of free ligand (ΔE_L(relax))
- Role: process
- Action: Starting from the same ligand coordinates, perform a constrained DFT geometry optimization (B3LYP, 6‑31G**, GD3BJ) in vacuum, fixing inter‑ring N–C–C–N torsion angles to 0° to enforce the meridional syn,syn conformation, while allowing other heavy atoms to relax. Compute the final electronic energy ΔE_L(relax).
- Evidence: none

### Step 5: Compute strain energies and deformation parameters
- Role: scored (load-bearing)
- Action: Calculate ΔE_L(strain) = ΔE_L(coord) − ΔE_L(relax) for each ligand. Measure the terminal N···N distance ρ in both coordinated and relaxed geometries and compute Δρ/ρ_L(relax) = (ρ_L(relax) − ρ_L(coord)) / ρ_L(relax). Collect results for all five ligands (A, B, C, D, E) and write to /app/outputs/ligand_strain_results.json.
- Output file: `/app/outputs/ligand_strain_results.json`
- Format: json
- Contract: [{"ligand": "A|B|C|D|E", "strain_energy_kJ_mol": float, "delta_rho_over_rho_relax": float}]
- Scoring: scored by hidden verifier

### Step 6: Zero‑intercept linear regression slope
- Role: scored (load-bearing)
- Action: Load the data from ligand_strain_results.json, perform a linear regression of strain_energy_kJ_mol vs delta_rho_over_rho_relax with the intercept forced to zero, and write the fitted slope to /app/outputs/zero_intercept_slope.txt as a single float.
- Output file: `/app/outputs/zero_intercept_slope.txt`
- Format: txt
- Contract: A single float value (units: kJ mol⁻¹ per unit Δρ/ρ).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ligand_strain_results.json`
- `/app/outputs/zero_intercept_slope.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ligand_strain_results.json
- path: `/app/outputs/ligand_strain_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Strain energies and deformation parameters for the five hypothetical Zn(II) complexes.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `ligand`, `strain_energy_kJ_mol`, `delta_rho_over_rho_relax`
    - `properties`:
      - `ligand`:
        - `type`: string
        - `enum`: `A`, `B`, `C`, `D`, `E`
      - `strain_energy_kJ_mol`:
        - `type`: number
      - `delta_rho_over_rho_relax`:
        - `type`: number

### zero_intercept_slope.txt
- path: `/app/outputs/zero_intercept_slope.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Zero‑intercept slope of ΔE_L(strain) vs Δρ/ρ_L(relax) from the training set of five ligands.
- schema:
  - `type`: text
  - `description`: A single float value (units: kJ mol⁻¹ per unit Δρ/ρ).

Notes: Values will be compared to hidden reference values derived from the paper with appropriate tolerances. Only the Zn(II) training set is required; CSD validation and Fe(II) application are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ligand_strain_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "ligand",
            "strain_energy_kJ_mol",
            "delta_rho_over_rho_relax"
          ],
          "properties": {
            "ligand": {
              "type": "string",
              "enum": [
                "A",
                "B",
                "C",
                "D",
                "E"
              ]
            },
            "strain_energy_kJ_mol": {
              "type": "number"
            },
            "delta_rho_over_rho_relax": {
              "type": "number"
            }
          }
        }
      },
      "description": "Strain energies and deformation parameters for the five hypothetical Zn(II) complexes."
    },
    {
      "file": "zero_intercept_slope.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single float value (units: kJ mol⁻¹ per unit Δρ/ρ)."
      },
      "description": "Zero‑intercept slope of ΔE_L(strain) vs Δρ/ρ_L(relax) from the training set of five ligands."
    }
  ],
  "notes": "Values will be compared to hidden reference values derived from the paper with appropriate tolerances. Only the Zn(II) training set is required; CSD validation and Fe(II) application are excluded."
}
```

## How you are scored
A hidden automated verifier will independently assess your submitted artifacts.

- **ligand_strain_results.json**: Each `strain_energy_kJ_mol` is compared to a reference value with an absolute tolerance. Partial credit may be awarded if only some values fall within the tolerance.

- **zero_intercept_slope.txt**: The reported slope is compared to a reference slope with a pre‑defined tolerance. The verifier uses your own data points to compute the slope you reported; it does not recompute the regression itself.

Both checks must pass for full credit. The reward is a weighted combination of these two components, with the strain energies and the slope each contributing substantially. No credit is given for simply producing correctly shaped files; all numerical values must be physically reasonable and obtained by genuinely executing the DFT workflow described above.
