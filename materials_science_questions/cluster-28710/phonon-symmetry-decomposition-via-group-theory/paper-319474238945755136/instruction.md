# Phonon symmetry decomposition via group theory

## Problem background
In solid-state physics, optical and scattering processes (infrared absorption, Raman scattering, carrier relaxation) are controlled by selection rules derived from the full space-group symmetry of the crystal. These rules are obtained by decomposing direct products of irreducible representations of the space group. For the non-symmorphic hexagonal group C6v4 (the space group of wurtzite-type lattices such as ZnO, BeO, CdS), a complete set of numerical selection rules and the associated Clebsch–Gordan coefficients (CGC) are required for quantitative interpretation, yet they had not been systematically computed. This task computes, using group-theoretical methods, both the full set of selection rules (star product and irreducible representation direct product decompositions) and a specific Clebsch–Gordan coefficient table for the space group C6v4.

## Approach
The computation follows the loaded-representation formalism. First, obtain the irreducible representation matrices for C6v4 – either from published tables (e.g., Kovalev 1961) or from a group-theory system such as GAP. Then, using wavevector conservation and character tables, compute the star product decompositions and the direct product decompositions of irreducible representations for all pairs of the high-symmetry stars (k0, k3, k4, k9, k10, k11). Finally, for the direct product U4 × U4, compute the Clebsch–Gordan coefficients by evaluating the standard formula that contracts the representation matrices. The results are expressed in the paper's notation for stars and irreducible representations.

## Reproduction target
Produce two JSON artifacts:
1. `selection_rules.json` – a complete set of selection rules containing star product decompositions and irreducible representation direct product decompositions, using the notation of the paper (e.g., k3, F1, U4) for all stars and irreps.
2. `cgc_table.json` – a Clebsch–Gordan coefficient table for the case U4 × U4. The table must list, for every pair of wavevector indices (i, j) from the star, the coefficients for each resulting representation, expressed as symbolic strings using `eta`, `phi`, `omega`, and `sqrt`. The row ordering must follow the standard presentation for this group.

## Assets

- GAP system: https://www.gap-system.org/
- Irreducible representations of space group C6v4 from Kovalev (1961)

## Workflow steps

### Step 1: Compute selection rules
- Role: scored (load-bearing)
- Action: Apply the loaded representation formulas from Saulevich et al. (1970) to the irreducible representation data of space group C6v4 to compute the direct product decompositions for all pairs of stars and irreducible representations. Save the complete set of selection rules.
- Output file: `/app/outputs/selection_rules.json`
- Format: json
- Contract: JSON object with 'star_products' (array of {star1, star2, decomposition: [{star, multiplicity}]}) and 'ir_products' (array of {ir1, ir2, decomposition: [{ir, multiplicity}]}) using paper notation (k0, k3, F1, etc.)
- Scoring: scored by hidden verifier

### Step 2: Compute Clebsch-Gordan coefficients for U4×U4
- Role: scored (load-bearing)
- Action: Using the same irreducible representation matrices, compute the Clebsch-Gordan coefficients for the direct product U4 × U4 → U1 + U4 + Δ1 + Δ5 via the formula from Saulevich et al. (1970). Produce a table matching the ordering of the wavevector index combinations (k1/k2/k3) as presented in the paper.
- Output file: `/app/outputs/cgc_table.json`
- Format: json
- Contract: JSON array of rows, each row with fields: i (string: k1/k2/k3), j (string: k1/k2/k3), U1_k1, U1_k2, U1_k3, U4_k1, U4_k2, U4_k3, Delta1_k1pp, Delta5_k1pp_1, Delta5_k1pp_2. Entries are strings representing complex numbers or symbolic expressions (e.g., '1/sqrt(2)', 'eta/sqrt(2)')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/selection_rules.json`
- `/app/outputs/cgc_table.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### selection_rules.json
- path: `/app/outputs/selection_rules.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Complete set of selection rules for space group C6v4: star product decompositions and irreducible representation direct product decompositions, to be compared against the paper's reported hidden gold equations.
- schema:
  - `type`: object
  - `required`:
    - `star_products`: array
    - `ir_products`: array
  - `items`:
    - `star_products`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `star1`: string
          - `star2`: string
          - `decomposition`:
            - `type`: array
            - `items`:
              - `type`: object
              - `properties`:
                - `star`: string
                - `multiplicity`: integer
    - `ir_products`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `ir1`: string
          - `ir2`: string
          - `decomposition`:
            - `type`: array
            - `items`:
              - `type`: object
              - `properties`:
                - `ir`: string
                - `multiplicity`: integer

### cgc_table.json
- path: `/app/outputs/cgc_table.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Clebsch-Gordan coefficient table for U4×U4 with rows ordered by wavevector index pairs, each entry a symbolic expression to be compared against the paper's hidden table.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `i`: string
      - `j`: string
      - `U1_k1`: string
      - `U1_k2`: string
      - `U1_k3`: string
      - `U4_k1`: string
      - `U4_k2`: string
      - `U4_k3`: string
      - `Delta1_k1pp`: string
      - `Delta5_k1pp_1`: string
      - `Delta5_k1pp_2`: string
    - `required`: `i`, `j`, `U1_k1`, `U1_k2`, `U1_k3`, `U4_k1`, `U4_k2`, `U4_k3`, `Delta1_k1pp`, `Delta5_k1pp_1`, `Delta5_k1pp_2`

Notes: All representations use paper notation (k0, k3, k4, k9, k10, k11, A1, F1, F2, B1, B2, U1, U2, U3, U4, P1, P2, P3, Δ1, Δ2, Δ3, Δ4, Δ5, Δ6). The checker normalizes ordering and symbolic expressions for comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "selection_rules.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "star_products": "array",
          "ir_products": "array"
        },
        "items": {
          "star_products": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "star1": "string",
                "star2": "string",
                "decomposition": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "star": "string",
                      "multiplicity": "integer"
                    }
                  }
                }
              }
            }
          },
          "ir_products": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "ir1": "string",
                "ir2": "string",
                "decomposition": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "ir": "string",
                      "multiplicity": "integer"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "Complete set of selection rules for space group C6v4: star product decompositions and irreducible representation direct product decompositions, to be compared against the paper's reported hidden gold equations."
    },
    {
      "file": "cgc_table.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "i": "string",
            "j": "string",
            "U1_k1": "string",
            "U1_k2": "string",
            "U1_k3": "string",
            "U4_k1": "string",
            "U4_k2": "string",
            "U4_k3": "string",
            "Delta1_k1pp": "string",
            "Delta5_k1pp_1": "string",
            "Delta5_k1pp_2": "string"
          },
          "required": [
            "i",
            "j",
            "U1_k1",
            "U1_k2",
            "U1_k3",
            "U4_k1",
            "U4_k2",
            "U4_k3",
            "Delta1_k1pp",
            "Delta5_k1pp_1",
            "Delta5_k1pp_2"
          ]
        }
      },
      "description": "Clebsch-Gordan coefficient table for U4×U4 with rows ordered by wavevector index pairs, each entry a symbolic expression to be compared against the paper's hidden table."
    }
  ],
  "notes": "All representations use paper notation (k0, k3, k4, k9, k10, k11, A1, F1, F2, B1, B2, U1, U2, U3, U4, P1, P2, P3, Δ1, Δ2, Δ3, Δ4, Δ5, Δ6). The checker normalizes ordering and symbolic expressions for comparison."
}
```

## How you are scored
A hidden verifier evaluates your two output files independently. For `selection_rules.json`, it compares your set of decomposition equations (after normalizing the ordering of terms) against an expected reference. For `cgc_table.json`, each symbolic entry is compared after normalization (e.g., expression simplification) against the expected coefficients. Both tests are weighted and combined into a final score; reporting the paper's numbers without genuine computation is not sufficient. You must produce correct symbolic expressions; numerical floating-point approximations are not accepted unless the expression is inherently numeric.
