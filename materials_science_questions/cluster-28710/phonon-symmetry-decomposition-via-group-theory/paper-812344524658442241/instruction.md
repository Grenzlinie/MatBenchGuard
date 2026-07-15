# Polyethylene chain vibrational block decomposition using line group representations

## Problem background
Determining the vibrational normal modes of a long polymer chain, such as polyethylene, requires solving a large secular determinant whose size grows with the number of repeat units. Group theory, specifically the theory of one-dimensional space groups (line groups), can exploit the translational and point symmetry of the chain to factor this determinant into small diagonal blocks labelled by a reciprocal-space vector k and by irreducible representation species. This factoring dramatically reduces the computational effort for a normal-coordinate analysis. The key quantity to compute is the block decomposition — the sizes of the symmetry-adapted blocks and their multiplicities — for each relevant k regime, using the line-group irreducible representations of the polymer's space group.

## Approach
This reproduction follows the Seitz formalism for space groups. The line group Vh (isomorphous to the point group D2h) describes the symmetry of the polyethylene chain with six atoms per unit cell. Using the character table and multiplication table of the factor group Vh, explicit irreducible representation matrices are constructed for all coset representatives — pure translations T, σ_v, σ_h, C2, C2', inversion i, glide reflection \bar{σ}_h, and screw rotation \bar{C}_2 — as functions of the reciprocal-space vector k and the half-translation vector o = d/2. When k is not at a zone center or boundary, the translational matrices are two-dimensional, mixing k and -k; at k=0 and k=b/2 the representations reduce appropriately. With these representations in hand, character projection is applied to the 18 Cartesian displacement coordinates of the polyethylene unit cell. This yields the symmetry-adapted block structure of the secular determinant for three distinct k categories: the factor-group regime (k=0), the general non-zone-boundary regime (k ≠ 0, b/2), and the zone-boundary regime (k = b/2).

## Reproduction target
Produce a JSON file containing the block sizes (positive integers) and the number of blocks of each size for each of the three k regimes. Specifically, compute the decomposition of the 18×18 secular submatrix for a polyethylene chain with six atoms per unit cell into symmetry blocks. Output the result for the factor group (k=0), for a general non-zone-boundary point (k ≠ 0, b/2), and for the zone boundary (k = b/2). The output must be a JSON object with keys 'k0', 'k_non_zone', and 'k_zone_boundary', each holding a list of [block_size, count] pairs.

## Assets

- numpy: numpy
- sympy: sympy

## Workflow steps

### Step 1: Construct Vh line group irreducible representations for polyethylene
- Role: process
- Action: Build explicit irreducible representation matrices for the Vh line group (isomorphous to D2h) as functions of the reciprocal-space vector k and translation parameters. Use the character tables and multiplication table of the point group Vh, together with the Seitz formalism for space groups, to obtain the two- and one-dimensional matrices for all coset representatives (T, σ_v, σ_h, C2, C2', i, σ̄_h, C̄2). The result should be a set of representation matrices parameterised by k and the half-translation vector o = d/2.
- Evidence: `/app/outputs/vh_representations.json`

### Step 2: Factor secular equation for polyethylene
- Role: scored (load-bearing)
- Action: Using the Vh representations from the previous step, apply character projection to the 3n=18 Cartesian coordinates of the polyethylene unit cell. Determine the block structure of the secular matrix for three k categories: k=0 (factor group), k≠0,b/2 (general non-zone-boundary points), and k=b/2 (zone boundary). For each category, report the block sizes and the number of blocks of each size.
- Output file: `/app/outputs/block_decomposition.json`
- Format: json
- Contract: {"k0": [[block_size_int, count_int], ...], "k_non_zone": [[block_size_int, count_int], ...], "k_zone_boundary": [[block_size_int, count_int], ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/block_decomposition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### block_decomposition.json
- path: `/app/outputs/block_decomposition.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Block decomposition of the secular determinant for polyethylene chain: list of [block_size, count] pairs for each of the three k regimes (k=0, general non-zone-boundary k, and zone-boundary k=b/2).
- schema:
  - `type`: object
  - `required`:
    - `k0`: list of [int, int]
    - `k_non_zone`: list of [int, int]
    - `k_zone_boundary`: list of [int, int]

Notes: The block sizes and counts are fixed deterministic group-theoretical integers. The checker compares against the paper-reported exact decomposition.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "block_decomposition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "k0": "list of [int, int]",
          "k_non_zone": "list of [int, int]",
          "k_zone_boundary": "list of [int, int]"
        }
      },
      "description": "Block decomposition of the secular determinant for polyethylene chain: list of [block_size, count] pairs for each of the three k regimes (k=0, general non-zone-boundary k, and zone-boundary k=b/2)."
    }
  ],
  "notes": "The block sizes and counts are fixed deterministic group-theoretical integers. The checker compares against the paper-reported exact decomposition."
}
```

## How you are scored
A hidden verifier will compare your submitted block_decomposition.json against the correct decomposition obtained from the group-theoretical procedure (the hidden gold). The comparison is exact; the block sizes and multiplicities are deterministic integers that follow uniquely from the symmetry. The final reward is a weighted sum of the correctness of this output and any supporting evidence, with the scored decomposition being the primary metric. To earn full credit you must compute the decomposition through a correct implementation of the line-group representations and character projection; merely reporting the expected numbers without performing the computation will not pass.
