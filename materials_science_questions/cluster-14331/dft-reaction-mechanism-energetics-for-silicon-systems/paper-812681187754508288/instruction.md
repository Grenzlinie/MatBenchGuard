# DFT Bond Dissociation Energies for Anisole and Phenol at B3LYP/6-311+G(d,p)

## Problem background
The preparation of high-quality organic monolayers on hydrogen-terminated silicon surfaces from dilute solutions of 1-alkenes is sensitive to the choice of solvent. Certain solvents, such as anisole, yield disordered monolayers while others produce well-ordered layers. A proposed explanation is that anisole participates in radical side reactions that disrupt the monolayer formation process, involving cleavage of the O–CH3 bond and subsequent radical chemistry at the silicon surface. To assess the feasibility of this mechanism, we need to compute the bond dissociation energies (BDEs) of relevant bonds: the O–CH3 bond in anisole, the O–H bond in phenol (a product of hydrogen abstraction by the phenoxy radical), and a representative primary C–H bond in an alkylbenzene (e.g., the methyl C–H bond in toluene). These BDEs quantify the energy required for homolytic bond cleavage and help determine whether such reactions are thermally accessible under the experimental conditions.

## Approach
We employ density functional theory (DFT) with the hybrid B3LYP functional and the 6-311+G(d,p) basis set to optimize geometries and compute harmonic vibrational frequencies for the parent molecules and for the radical fragments arising from homolytic bond cleavage. The bond dissociation energy (BDE) is defined as the difference in zero-point-corrected total energies between the sum of the radical fragments and the parent molecule:
BDE = [E(rad1) + ZPE(rad1)] + [E(rad2) + ZPE(rad2)] − [E(parent) + ZPE(parent)].
For the closed-shell parent molecules we use restricted Kohn-Sham (RB3LYP), while unrestricted (UB3LYP) calculations are employed for the open-shell radicals. The three targeted bonds are the O–CH3 in anisole, the O–H in phenol, and the methyl C–H in toluene. The calculations are performed using any quantum chemistry code that supports these methods, such as ORCA or Psi4.

## Reproduction target
The task is to reproduce the three bond dissociation energies (in kcal/mol) at the B3LYP/6-311+G(d,p) level of theory. Specifically, compute:
- the O–CH3 BDE in anisole,
- the O–H BDE in phenol,
- the methyl C–H BDE in toluene.
All calculations must include zero-point energy corrections. The resulting values must be stored in a JSON file at /app/outputs/bde_results.json with keys anisole_OCH3_BDE, phenol_OH_BDE, and alkyl_CH_BDE.

## Assets

- Quantum chemistry software supporting B3LYP/6-311+G(d,p): https://orcaforum.kofo.mpg.de/ (ORCA) or https://psicode.org/ (Psi4)

## Workflow steps

### Step 1: Calculate Bond Dissociation Energies
- Role: scored
- Action: For anisole, phenol, and toluene (as the representative alkylbenzene), perform geometry optimizations and harmonic frequency calculations at the B3LYP/6-311+G(d,p) level of theory for the parent molecules and for the corresponding radical fragments from homolytic bond cleavage (use unrestricted UB3LYP for radicals).
Compute the bond dissociation energy (BDE) with zero-point energy corrections as: BDE = (E+ZPE)(radical1) + (E+ZPE)(radical2) - (E+ZPE)(parent).
Compute the O-CH3 BDE in anisole, the O-H BDE in phenol, and the primary C-H BDE in toluene (methyl C-H bond). Report all values in kcal/mol. Write the results to a JSON file with the specified keys.
- Output file: `/app/outputs/bde_results.json`
- Format: json
- Contract: object with keys anisole_OCH3_BDE, phenol_OH_BDE, alkyl_CH_BDE (all numbers in kcal/mol)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bde_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bde_results.json
- path: `/app/outputs/bde_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed bond dissociation energies (BDEs) for anisole O-CH3, phenol O-H, and toluene methyl C-H bonds at the B3LYP/6-311+G(d,p) level including zero-point energy corrections.
- schema:
  - `type`: object
  - `required`:
    - `anisole_OCH3_BDE`: number (kcal/mol)
    - `phenol_OH_BDE`: number (kcal/mol)
    - `alkyl_CH_BDE`: number (kcal/mol)

Notes: The molecular free-volume calculations using Cerius2 are omitted because they rely on proprietary software and are not part of the main mechanistic claim scoped for reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bde_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "anisole_OCH3_BDE": "number (kcal/mol)",
          "phenol_OH_BDE": "number (kcal/mol)",
          "alkyl_CH_BDE": "number (kcal/mol)"
        }
      },
      "description": "Computed bond dissociation energies (BDEs) for anisole O-CH3, phenol O-H, and toluene methyl C-H bonds at the B3LYP/6-311+G(d,p) level including zero-point energy corrections."
    }
  ],
  "notes": "The molecular free-volume calculations using Cerius2 are omitted because they rely on proprietary software and are not part of the main mechanistic claim scoped for reproduction."
}
```

## How you are scored
Your submitted bde_results.json will be scored by an automated verifier. The verifier compares each of the three BDE values you report to the reference values (computed at the same level of theory) using a tolerance for acceptable deviation. The final score is proportional to the number of bonds whose BDE falls within the tolerance. Full credit requires all three bonds to be within tolerance; partial credit is assigned if some bonds are within tolerance and others are not.
