# DFT Relative Stability of Peroxo and Ferryl Intermediates in Diiron Complex

## Problem background
Methane monooxygenase (MMO) mimics containing a diiron active site catalyze O2 activation. The mechanism proceeds through a peroxo intermediate (P) before forming a bis-ferryl intermediate (Q). Understanding whether P or Q is thermodynamically favored is critical for describing the oxygen cleavage step. This computational work uses density functional theory to determine the relative stability and structural parameters of these two intermediates in a model complex based on the heptapodate ligand HPTM.

## Approach
The method uses DFT at the B3LYP level with an effective core potential basis set (e.g., LANL2DZ augmented with polarization functions) to perform full geometry optimizations on both the peroxo P and bis‑ferryl Q intermediates. An implicit solvation model (water) is applied to mimic the aqueous environment. From the optimized structures, the total electronic energies are extracted to compute the relative energy ΔE = E(P) − E(Q), and key bond distances (Fe–Fe, O–O in P; the two terminal Fe=O distances in Q) are measured. The comparison of these quantities determines the thermodynamic preference between the two intermediates.

## Reproduction target
Compute the relative electronic energy ΔE (kcal/mol) and the specified bond distances (Å) for the model complex [Fe₂(HPTM)(μ‑OH)]⁺ at the B3LYP/ECP level of theory (using an open‑source quantum chemistry package). Report these values in the output JSON file as specified. The objective is to determine whether the peroxo or bis‑ferryl form is more stable and to characterize their geometries, not to match a predetermined numeric target.

## Assets

- Open-source quantum chemistry package (ORCA, NWChem, or PySCF): https://orcaforum.kofo.mpg.de/ (free for academic use); https://www.nwchem-sw.org/; https://pyscf.org/
- Molecular structure builder (Avogadro, OpenBabel, or RDKit): https://avogadro.cc/; https://openbabel.org/; https://www.rdkit.org/

## Workflow steps

### Step 1: Build initial molecular models
- Role: process
- Action: Construct 3D molecular models for the peroxo intermediate P (Fe2(HPTM)(μ‑OH)(μ‑η1:η1‑O2) with two Fe(III)) and the bis‑ferryl intermediate Q (Fe2(HPTM)(μ‑OH)(O)2 with two Fe(IV)). Generate initial Cartesian coordinates in XYZ format as starting points for DFT optimization.
- Evidence: none

### Step 2: Perform DFT geometry optimization
- Role: process
- Action: Perform full geometry optimization at the B3LYP level with an effective core potential basis set (e.g., LANL2DZ augmented with polarization functions) on both intermediates P and Q. Use an implicit solvation model (water) to mimic the aqueous environment. Set the charge and spin multiplicity appropriate for high‑spin Fe(III) coupling in P and high‑spin Fe(IV) in Q. Converge the optimizations to standard thresholds.
- Evidence: none

### Step 3: Extract relative energy and key distances
- Role: scored (load-bearing)
- Action: From the final DFT total energies of P and Q, compute ΔE = E(P) − E(Q) in kcal/mol. Extract the Fe–Fe distance (Å) from the P geometry, the O–O distance (Å) of the peroxo group in P, and the two Fe=O bond distances (Å) from the Q geometry. Output these quantities in a JSON file.
- Output file: `/app/outputs/relative_energy_and_geometry.json`
- Format: json
- Contract: {
  "delta_E_kcal_per_mol": float,   // ΔE = E(P) − E(Q)
  "Fe_Fe_distance_P_Angstrom": float,
  "O_O_distance_P_Angstrom": float,
  "Fe_O_distance_Q_Angstrom": [float, float]   // two Fe=O bond lengths, order does not matter
}
- Scoring: scored by hidden verifier

### Step 4: Save optimized geometry of P in XYZ format
- Role: scored
- Action: Write the final optimized Cartesian coordinates of the peroxo intermediate P to an XYZ file, including atomic symbols and coordinates.
- Output file: `/app/outputs/optimized_geometry_P.xyz`
- Format: txt
- Contract: Standard XYZ format: first line atom count, second line comment, then element symbol and x y z per atom.
- Scoring: scored by hidden verifier

### Step 5: Save optimized geometry of Q in XYZ format
- Role: scored
- Action: Write the final optimized Cartesian coordinates of the bis‑ferryl intermediate Q to an XYZ file, including atomic symbols and coordinates.
- Output file: `/app/outputs/optimized_geometry_Q.xyz`
- Format: txt
- Contract: Standard XYZ format: first line atom count, second line comment, then element symbol and x y z per atom.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energy_and_geometry.json`
- `/app/outputs/optimized_geometry_P.xyz`
- `/app/outputs/optimized_geometry_Q.xyz`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energy_and_geometry.json
- path: `/app/outputs/relative_energy_and_geometry.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed relative electronic energy ΔE = E(P) − E(Q) and key bond distances from the DFT-optimized geometries.
- schema:
  - `type`: object
  - `required`:
    - `delta_E_kcal_per_mol`: float (kcal/mol)
    - `Fe_Fe_distance_P_Angstrom`: float
    - `O_O_distance_P_Angstrom`: float
    - `Fe_O_distance_Q_Angstrom`: array of two floats

### optimized_geometry_P.xyz
- path: `/app/outputs/optimized_geometry_P.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized Cartesian coordinates for peroxo intermediate P in XYZ format.
- schema:
  - `type`: other
  - `required`: Standard XYZ format: line 1 = number of atoms, line 2 = comment, remaining lines = element symbol x y z.

### optimized_geometry_Q.xyz
- path: `/app/outputs/optimized_geometry_Q.xyz`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Optimized Cartesian coordinates for bis‑ferryl intermediate Q in XYZ format.
- schema:
  - `type`: other
  - `required`: Standard XYZ format: line 1 = number of atoms, line 2 = comment, remaining lines = element symbol x y z.

Notes: The relative energy is the primary target; bond lengths are secondary. The XYZ files provide an internal consistency check: the checker recomputes the relevant distances from the coordinates and compares them to the JSON values (tight tolerance 0.01 Å). The agent may use any of the listed open-source DFT packages.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energy_and_geometry.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "delta_E_kcal_per_mol": "float (kcal/mol)",
          "Fe_Fe_distance_P_Angstrom": "float",
          "O_O_distance_P_Angstrom": "float",
          "Fe_O_distance_Q_Angstrom": "array of two floats"
        }
      },
      "description": "Computed relative electronic energy ΔE = E(P) − E(Q) and key bond distances from the DFT-optimized geometries."
    },
    {
      "file": "optimized_geometry_P.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "required": "Standard XYZ format: line 1 = number of atoms, line 2 = comment, remaining lines = element symbol x y z."
      },
      "description": "Optimized Cartesian coordinates for peroxo intermediate P in XYZ format."
    },
    {
      "file": "optimized_geometry_Q.xyz",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "other",
        "required": "Standard XYZ format: line 1 = number of atoms, line 2 = comment, remaining lines = element symbol x y z."
      },
      "description": "Optimized Cartesian coordinates for bis‑ferryl intermediate Q in XYZ format."
    }
  ],
  "notes": "The relative energy is the primary target; bond lengths are secondary. The XYZ files provide an internal consistency check: the checker recomputes the relevant distances from the coordinates and compares them to the JSON values (tight tolerance 0.01 Å). The agent may use any of the listed open-source DFT packages."
}
```

## How you are scored
A hidden verifier independently checks each scored artifact you submit. The relative energy reported in relative_energy_and_geometry.json is compared against a hidden reference value derived from the original study; the three bond distances are similarly compared. The verifier also performs a structural audit on the two XYZ files to ensure they are internally consistent with the distances you reported. Each component contributes a weight to the final reward between 0 and 1. Simply reporting paper-derived numbers without genuine computation will not pass the full check. You are scored on producing the correct result through your DFT workflow.
