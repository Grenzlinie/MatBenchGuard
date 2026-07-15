# Construct a 4D Vibrational Bush Displacement Pattern from Symmetry Basis Vectors

## Problem background
Group-theoretical analysis of nonlinear vibrations in solids reveals exact solutions beyond the harmonic approximation: bushes of nonlinear normal modes (NNMs). In monolayer graphene (space group P6mm), the theory predicts a finite set of such low-dimensional vibrational bushes, each corresponding to a symmetry-determined atomic displacement pattern that is an exact solution to the nonlinear equations of motion. The present task focuses on constructing one of these patterns — the four-dimensional bush with symmetry group Cmm2 — from the irreducible representations (irreps) of the parent space group. This is a purely symbolic computation: given the explicit basis vectors of the relevant irreps, the displacement pattern follows deterministically from linear combinations and a reparameterization.

## Approach
The construction follows the group-theoretical procedure: each vibrational mode belongs to an irrep of the parent space group P6mm. For a chosen subgroup (here Cmm2), the displacement pattern is obtained by selecting invariant vectors for each contributing irrep. The provided Table 1 contains the 16-dimensional basis vectors for the three active irreps — Γ12-2, Γ12-1, and Γ16-6 — expressed as sequential (x,y) displacements of atoms 1…8 in a 2×2 supercell. First, build the root-mode displacement from Γ12-2 using its invariant vector (a,a,0): δ = a φ₁ + a φ₂. Then add the secondary contributions from Γ12-1 with invariant vector (a,-a,b): δ = a ψ₁ − a ψ₂ + b ψ₃, and from Γ16-6 with invariant vector (a,−√3/2 a): δ = a χ₁ − (√3/2)a χ₂. The parameters a,b are independent for each irrep. Sum the three parts to obtain a 16-component intermediate pattern. Finally, reparameterize the result into four independent parameters A,B,C,D and simplify to obtain a concise symbolic expression for the displacement pattern of the Cmm2 bush.

## Reproduction target
Your goal is to compute the exact symbolic displacement pattern for the four-dimensional vibrational bush B[Cmm2] and write it to displacement_pattern.txt as a single-line text string. The string must consist of an opening parenthesis, eight pipe-separated groups (one per atom in the supercell), each containing two symbolic expressions (x and y displacements) using the parameters A,B,C,D, separated by a comma, and a closing parenthesis. Example format: (expr1_x,expr1_y|expr2_x,expr2_y|…|expr8_x,expr8_y). The expressions must be the correct result of the linear combination and reparameterization described in the workflow.

## Assets

- Basis vectors of irreps Γ12-2, Γ12-1, Γ16-6

## Workflow steps

### Step 1: Construct the B[Cmm2] displacement pattern
- Role: scored (load-bearing)
- Action: Load the provided basis vectors for irreducible representations Γ12-2, Γ12-1, and Γ16-6 from the bundled resource (Table 1 basis vectors). Construct the root-mode displacement using the invariant vector (a,a,0) for Γ12-2: δ[Γ12-2,(a,a,0)] = a φ1 + a φ2. Construct the secondary-mode contributions: δ[Γ12-1,(a,-a,b)] = a ψ1 − a ψ2 + b ψ3, and δ[Γ16-6,(a,−√3/2 a)] = a χ1 − (√3/2)a χ2. Sum the root and secondary contributions, treating the parameters a and b as independent for each irrep. Reparameterize the combined 16-component vector into four arbitrary parameters A,B,C,D and simplify to obtain the final parameterized displacement pattern for the 2×2 supercell (atoms 1..8, each with x,y displacements). Write the resulting pattern as a single-line text string to the output file.
- Output file: `/app/outputs/displacement_pattern.txt`
- Format: txt
- Contract: A single line of text containing an opening parenthesis, followed by eight groups separated by vertical bars, each group being two symbolic expressions (using parameters A,B,C,D) separated by a comma, and a closing parenthesis. Example format: (expr1_x,expr1_y|expr2_x,expr2_y|...|expr8_x,expr8_y).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/displacement_pattern.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### displacement_pattern.txt
- path: `/app/outputs/displacement_pattern.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The full displacement pattern string for the four-dimensional bush B[Cmm2]; scored by exact match against the paper's reported pattern after whitespace normalization.
- schema:
  - `type`: text
  - `description`: Single-line text representing the displacement pattern of the Cmm2 bush with four parameters A,B,C,D. The pattern must be in the form (A,B|2C,-C|2D,-D|-A,A+B|A,-A-B|-2D,D|-2C,C|-A,-B).

Notes: The hidden checker normalises whitespace and compares the agent's output character-by-character to the gold pattern. No tolerance band is used because the target is a fixed deterministic symbolic expression.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "displacement_pattern.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single-line text representing the displacement pattern of the Cmm2 bush with four parameters A,B,C,D. The pattern must be in the form (A,B|2C,-C|2D,-D|-A,A+B|A,-A-B|-2D,D|-2C,C|-A,-B)."
      },
      "description": "The full displacement pattern string for the four-dimensional bush B[Cmm2]; scored by exact match against the paper's reported pattern after whitespace normalization."
    }
  ],
  "notes": "The hidden checker normalises whitespace and compares the agent's output character-by-character to the gold pattern. No tolerance band is used because the target is a fixed deterministic symbolic expression."
}
```

## How you are scored
Your output file displacement_pattern.txt is scored by a hidden verifier. The verifier normalises whitespace in your file and compares it character-by-character to the correct pattern derived from the paper's group-theoretical construction. Because the pattern is completely determined by the provided inputs, an exact match is required. You will receive a reward of 1.0 for an exact match (modulo whitespace) and 0.0 otherwise. The verifier does not use tolerance bands; the target is a fixed deterministic symbolic expression.
