# Analytic tight-binding model for Si dangling bond pinning at interfacial vacancies

## Problem background
When a transition metal is deposited on Si, a Schottky barrier forms whose height is remarkably insensitive to the metal species—a phenomenon known as Fermi-level pinning. One proposed explanation is that Si dangling bonds at interfacial vacancies are sheltered by the transition-metal atoms, causing the defect level to be pinned near the Si hybrid energy. The paper develops an analytic four-atom sp³ tight-binding model of such a defect, using one Si hybrid orbital and three transition-metal hybrid orbitals oriented toward the vacancy. The model predicts that the A₁-symmetric state yields a defect level in the Si band gap. To test this idea, the task is to implement this model for three metals (Ni, Pd, Pt), compute the energy of the A₁-derived level (E₋) relative to the Si valence band maximum, and examine whether these levels lie within the Si band gap (0–1.1 eV) and whether they exhibit a chemical trend.

## Approach
The theory treats the defect as a molecule with four sp³ hybrid orbitals: one on the Si atom that dangles into the vacancy, and three on the neighboring transition-metal atoms. Because the metal atoms are very electropositive relative to Si, their on-site energies are much higher (large positive defect potentials). The A₁ symmetric combination of the three metal orbitals couples to the Si orbital through a nearest-neighbor hopping parameter β. An effective two-state Hamiltonian can be constructed in this A₁ subspace; diagonalizing it gives two eigenvalues, where the lower one corresponds to the Si dangling bond level in the band gap. The on-site hybrid energies (ε_Si, ε_Ni, ε_Pd, ε_Pt) are obtained from Harrison's atomic orbital energies, and the hopping β is taken as -0.39 eV as reported in the paper. By solving the A₁ eigenproblem numerically, one obtains E₋ for each metal.

## Reproduction target
Produce a CSV file `step_01_defect_levels.csv` with columns `metal` and `defect_level_eV` containing the computed energies of the A₁-derived level E₋ (in eV) for Ni, Pd, and Pt, measured from the Si valence band maximum. The hidden verifier will independently recompute the same model and check (i) that all three defect levels satisfy 0 ≤ defect_level_eV ≤ 1.1 (the Si band gap), and (ii) that the ordering of the three metals follows the expected chemical trend (the exact ordering is not disclosed here).

## Assets
None. All required parameters (the on-site hybrid energies and hopping β) are provided directly in the step action.

## Workflow steps

### Step 1: Compute defect level energies
- Role: scored (load-bearing)
- Action: Implement the four-atom sp³ tight-binding model for an interfacial vacancy where three tetrahedral sites are occupied by transition-metal atoms (Ni, Pd, Pt) and one by Si. Use the on-site hybrid energies ε_Si=0.24 eV, ε_Ni=5.39 eV, ε_Pd=5.35 eV, ε_Pt=5.08 eV (derived from Harrison's atomic orbital energies) and hopping parameter β=-0.39 eV. Derive and solve the A₁-symmetric eigenproblem to obtain the energy of the a₁-derived level E₋. Report the defect level energy for each metal in eV relative to the Si valence band maximum.
- Output file: `/app/outputs/step_01_defect_levels.csv`
- Format: csv
- Contract: CSV with header: metal,defect_level_eV. Rows: Ni,<float>; Pd,<float>; Pt,<float>. defect_level_eV is the energy of the A₁-derived level relative to the Si valence band maximum, in eV.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_defect_levels.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_defect_levels.csv
- path: `/app/outputs/step_01_defect_levels.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Defect level energies computed via analytic four-atom sp³ tight-binding model for Ni, Pd, Pt.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `defect_level_eV`
  - `units`:
    - `defect_level_eV`: eV

Notes: The energies are measured from the valence band maximum. The checker will recompute the defect level energy for each metal independently and compare within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_defect_levels.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "defect_level_eV"
        ],
        "units": {
          "defect_level_eV": "eV"
        }
      },
      "description": "Defect level energies computed via analytic four-atom sp³ tight-binding model for Ni, Pd, Pt."
    }
  ],
  "notes": "The energies are measured from the valence band maximum. The checker will recompute the defect level energy for each metal independently and compare within a tolerance."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently re-implements the same four-atom sp³ tight-binding model using the same input parameters. The verifier computes its own reference defect level energies for each metal and compares them to your reported values within a tolerance appropriate for implementation differences. In addition, the verifier checks the ordering of the three defect levels against a hidden reference trend. The final score is a weighted combination of these checks; it is not sufficient to simply report numbers—the verifier's recomputation ensures that honest executable implementation is rewarded.
