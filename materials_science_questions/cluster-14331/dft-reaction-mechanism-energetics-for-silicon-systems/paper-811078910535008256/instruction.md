# DFT Formation Energy and Barriers of Silicon Hydride Ions

## Problem background
Silicon hydride anions (SiH5−, SiH3−) are central to understanding the stability of five-coordinate silicon species and the role of electron correlation in closed-shell reactions. This task investigates the geometric and energetic properties of these ions by computing formation energies, pseudorotation barriers, and inversion barriers from first-principles electronic structure calculations. The results will illuminate how correlation effects modify reaction energetics compared to Hartree–Fock theory.

## Approach
The computational approach employs ab initio Hartree–Fock (HF) and correlated electronic structure methods (MP2 or CCSD) to obtain total energies for the relevant molecular species: SiH5− (D3h and C4v configurations), SiH4, SiH3− (C3v and D3h), H2, H−, and a supermolecule SiH4 + H− at 200 a.u. separation. The calculations use the basis sets specified in the instructions: for Si, an (11s,7p)/[7,4] set with two d functions and one f function; for H, a 5s/[3,1,1] plus a p set; and for H−, additional diffuse s and p functions. The total energies are then used to derive four key quantities: (a) the formation energy of SiH5− from SiH4 + H−, (b) the pseudorotation barrier of SiH5−, (c) the inversion barrier of SiH3−, and (d) the reaction energy for SiH5− → SiH3− + H2. Comparing HF and correlated results reveals the influence of electron correlation on these energy differences.

## Reproduction target
Compute total energies at the HF and a correlated level (MP2 or CCSD) for all species listed above, using the supplied geometries and basis set definitions. From these energies, derive: (1) formation energy of SiH4 + H− → SiH5−, (2) pseudorotation barrier ΔEB = E(SiH5− C4v) − E(SiH5− D3h), (3) inversion barrier ΔEi = E(SiH3− D3h) − E(SiH3− C3v), and (4) reaction energy of SiH5− → SiH3− (C3v) + H2. Report all total energies in atomic units (hartree) and all derived quantities in kcal/mol in a single JSON file, `results.json`, conforming to the output contract schema.

## Assets

- Open-source quantum chemistry package (Psi4 or PySCF): psi4 or pyscf

## Workflow steps

### Step 1: Compute total energies and reaction quantities
- Role: scored (load-bearing)
- Action: Using the molecular geometries given in the instruction and the basis set specifications, perform single-point energy calculations at the Hartree–Fock and a correlated wavefunction level (MP2 or CCSD) for the following species: H−, H2, SiH3− (C3v and D3h), SiH4, SiH5− (D3h and C4v), and the supermolecule SiH4 + H− at 200 a.u. separation. Compute the derived quantities: (a) formation energy of SiH4 + H− → SiH5−, (b) pseudorotation barrier ΔEB = E(SiH5− C4v) − E(SiH5− D3h), (c) inversion barrier ΔEi = E(SiH3− D3h) − E(SiH3− C3v), (d) reaction energy of SiH5− → SiH3− (C3v) + H2. Write all total energies (atomic units) and all derived energies (kcal/mol) into results.json according to the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with two top-level keys: 'total_energies' (mapping species codes to {hf, correlated} in au) and 'reaction_energies' (keys reaction1_hf, reaction1_correlated, pseudorotation_hf, pseudorotation_correlated, inversion_hf, inversion_correlated, reaction3_hf, reaction3_correlated in kcal/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Total energies for all species (HF and correlated) and derived reaction energies/barriers. The checker recomputes the four headline quantities from 'total_energies' and compares each to a paper-reported reference within a hidden tolerance.
- schema:
  - `type`: object
  - `required`:
    - `total_energies`: object
    - `reaction_energies`: object
  - `items`:
    - `total_energies.<species>.hf`: number (au)
    - `total_energies.<species>.correlated`: number (au)
    - `reaction_energies.<key>`: number (kcal/mol)
  - `required_columns`:
  - `units`: object

Notes: The agent should use the basis set and geometries provided in the instruction. The correlated method can be MP2 or CCSD; scoring tolerances account for the method difference from the original PNO-CI/CEPA calculations.

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
          "total_energies": "object",
          "reaction_energies": "object"
        },
        "items": {
          "total_energies.<species>.hf": "number (au)",
          "total_energies.<species>.correlated": "number (au)",
          "reaction_energies.<key>": "number (kcal/mol)"
        },
        "required_columns": [],
        "units": {}
      },
      "description": "Total energies for all species (HF and correlated) and derived reaction energies/barriers. The checker recomputes the four headline quantities from 'total_energies' and compares each to a paper-reported reference within a hidden tolerance."
    }
  ],
  "notes": "The agent should use the basis set and geometries provided in the instruction. The correlated method can be MP2 or CCSD; scoring tolerances account for the method difference from the original PNO-CI/CEPA calculations."
}
```

## How you are scored
A hidden verifier independently recomputes the four derived quantities from your submitted total energies and compares each against reference results. The comparison uses tolerances that account for legitimate differences between quantum chemistry implementations (e.g., basis set handling, convergence thresholds). Additionally, a structural consistency check verifies that the correlated formation energy is lower than the HF formation energy, as expected when correlation stabilizes the product. The final reward is a weighted combination of the scores across all derived quantities and the consistency check.
