# Reproduce axis‑permutation and Wyckoff‑site permutation tables for orthorhombic D2h and D2 space groups

## Problem background
For crystals belonging to the D2h and D2 orthorhombic point groups, the three crystallographic axes are all of order C2, so there is no unique physically defined axis. The labelling of the axes is therefore arbitrary, and different choices can lead to different factor-group analysis results for the same crystal structure. This ambiguity creates confusion when comparing published vibrational analysis results. To resolve this, one needs to determine, for every orthorhombic space group in these classes, which axis permutations leave the space-group symbol unchanged (allowed permutations), which Wyckoff site labels remain invariant under those permutations, and how the site labels permute under each allowed relabelling. This information was tabulated in a reference work, and your task is to reproduce these tables by computational means.

## Approach
Using the standard crystallographic settings from the International Tables, for each orthorhombic space group belonging to the D2h and D2 classes, you will determine the allowed axis permutations from the symmetry information (i.e., which axis relabellings keep the space-group symbol the same). You will identify whether any axes are physically defined by the symmetry operations. For each space group, you will obtain the Wyckoff positions from a public crystallographic database (e.g., spglib, the Bilbao Crystallographic Server) and analyze the algebraic forms of the equivalent-point coordinates to deduce which Wyckoff site labels are invariant under the allowed permutations and how the site names permute for each possible axis relabelling. The result will be compiled into two tables: one for D2h space groups and one for D2 space groups.

## Reproduction target
Produce two CSV files that list, for every orthorhombic space group in the D2h and D2 classes, the space group number, conventional symbol, allowed axis-permutation type, physically defined axes (if any), the set of Wyckoff sites that are invariant under allowed permutations, and the explicit Wyckoff-label permutations for each of the six possible axis relabellings: abc, bca, cab, bač (ba\bar c), čba (\bar c ba), and ačb (a\bar c b). The columns of each CSV are: space_group_number, symbol, allowed_permutations, defined_axes, invariant_sites, abc, bca, cab, bač, čba, ačb. Site lists within cells can be separated by newline or comma; empty entries are permitted where no permutation applies. The D2h table must include all 28 D2h orthorhombic space groups, and the D2 table all 9 D2 orthorhombic space groups, in order of increasing space group number.

## Assets

- spglib (space group library for Python): spglib
- Bilbao Crystallographic Server: https://www.cryst.ehu.es/

## Workflow steps

### Step 1: Compile Table 1 for orthorhombic D2h space groups
- Role: scored (load-bearing)
- Action: For every orthorhombic space group belonging to the D2h point‑group class, determine its allowed axis permutations from the standard setting (via International Tables or equivalent public database), identify physically defined axes (if any), list the Wyckoff site labels that are invariant under those permutations, and compute the explicit site‑label permutations for each possible axis relabelling (abc, bca, cab, bač, čba, ačb). Output the complete table as a CSV file.
- Output file: `/app/outputs/d2h_table.csv`
- Format: csv
- Contract: space_group_number (int), symbol (str), allowed_permutations (str), defined_axes (str), invariant_sites (str, site letters separated by newline/comma), abc (str, may be empty), bca (str, may be empty), cab (str, may be empty), bač (str, may be empty), čba (str, may be empty), ačb (str, may be empty).
- Scoring: scored by hidden verifier

### Step 2: Compile Table 2 for orthorhombic D2 space groups
- Role: scored (load-bearing)
- Action: Analogous to step_d2h_table, but for all orthorhombic space groups belonging to the D2 point‑group class. Produce the corresponding CSV file.
- Output file: `/app/outputs/d2_table.csv`
- Format: csv
- Contract: Identical to d2h_table.csv schema.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/d2h_table.csv`
- `/app/outputs/d2_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### d2h_table.csv
- path: `/app/outputs/d2h_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of allowed axis permutations, defined axes, invariant Wyckoff sites, and explicit site‑label permutations for orthorhombic D2h space groups. Compared against a hidden gold table derived from the paper’s Table 1.
- schema:
  - `type`: table
  - `required_columns`: `space_group_number`, `symbol`, `allowed_permutations`, `defined_axes`, `invariant_sites`, `abc`, `bca`, `cab`, `bač`, `čba`, `ačb`
  - `units`: object

### d2_table.csv
- path: `/app/outputs/d2_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of allowed axis permutations, defined axes, invariant Wyckoff sites, and explicit site‑label permutations for orthorhombic D2 space groups. Compared against a hidden gold table derived from the paper’s Table 2.
- schema:
  - `type`: table
  - `required_columns`: `space_group_number`, `symbol`, `allowed_permutations`, `defined_axes`, `invariant_sites`, `abc`, `bca`, `cab`, `bač`, `čba`, `ačb`
  - `units`: object

Notes: The hidden gold tables are extracted directly from the paper’s Tables 1 and 2. The checker compares each row using exact string matching for columns space_group_number, symbol, allowed_permutations, defined_axes, invariant_sites; for the site‑permutation columns (abc, bca, etc.) cell values are split by newline/comma, trimmed, and compared as sets. Empty cells must remain empty. Row order must follow increasing space_group_number.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "d2h_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "space_group_number",
          "symbol",
          "allowed_permutations",
          "defined_axes",
          "invariant_sites",
          "abc",
          "bca",
          "cab",
          "bač",
          "čba",
          "ačb"
        ],
        "units": {}
      },
      "description": "Table of allowed axis permutations, defined axes, invariant Wyckoff sites, and explicit site‑label permutations for orthorhombic D2h space groups. Compared against a hidden gold table derived from the paper’s Table 1."
    },
    {
      "file": "d2_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "space_group_number",
          "symbol",
          "allowed_permutations",
          "defined_axes",
          "invariant_sites",
          "abc",
          "bca",
          "cab",
          "bač",
          "čba",
          "ačb"
        ],
        "units": {}
      },
      "description": "Table of allowed axis permutations, defined axes, invariant Wyckoff sites, and explicit site‑label permutations for orthorhombic D2 space groups. Compared against a hidden gold table derived from the paper’s Table 2."
    }
  ],
  "notes": "The hidden gold tables are extracted directly from the paper’s Tables 1 and 2. The checker compares each row using exact string matching for columns space_group_number, symbol, allowed_permutations, defined_axes, invariant_sites; for the site‑permutation columns (abc, bca, etc.) cell values are split by newline/comma, trimmed, and compared as sets. Empty cells must remain empty. Row order must follow increasing space_group_number."
}
```

## How you are scored
A hidden verifier will compare your d2h_table.csv and d2_table.csv to hidden gold tables derived directly from the original published compilation. For columns space_group_number, symbol, allowed_permutations, defined_axes, and invariant_sites, exact string comparison is used (case-insensitive, trimmed). For each site-permutation column (abc, bca, cab, bač, čba, ačb), the cell value is split by newline or comma, trimmed, and compared as an unordered set. Empty cells are expected to be empty and are compared accordingly. All rows must be present and in the correct order; no extra rows are allowed. The final reward is the proportion of rows (across both tables) that match exactly according to these rules.
