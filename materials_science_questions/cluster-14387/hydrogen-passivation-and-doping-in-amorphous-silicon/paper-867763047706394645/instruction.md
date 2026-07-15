# Number Series of Atoms, Bonds and Interface Bonds for Zinc-Blende Nanocrystals

## Problem background
Zinc-blende nanocrystals exhibit size- and shape-dependent stress and interface effects that influence their structural, electronic, and optical properties. A universal gauge for evaluating such effects requires knowledge of the number of nanocrystal atoms ($N_{\text{NC}}$), the number of bonds between those atoms ($N_{\text{bnd}}$), and the number of interface bonds connecting the nanocrystal to its environment ($N_{\text{IF}}$). Analytical number series for these quantities as functions of a size index $i$ provide a rigorous, repeatable tool for interpreting solid-state spectroscopy data. The present task computes these number series for seven high-symmetry zinc-blende nanocrystal shapes: cube, octahedron, dodecahedron (with odd and even size classes), pyramid, tetrahedron, {111}-dominant quatrodecahedron, and {001}-dominant quatrodecahedron.

## Approach
Implement the explicit analytical formulas that give $N_{\text{NC}}$, $N_{\text{bnd}}$, and $N_{\text{IF}}$ as functions of the integer size index $i$. The formulas for each shape are provided below. For shapes where the index can start at $i=0$ (octahedron, pyramid, tetrahedron), evaluate only $i = 1, 2, \dots, 7$ in this task; for all others the formulas are defined for $i \ge 1$. Dodecahedral nanocrystals have two alternating classes, odd and even, each described by its own set of formulas. The computed quantities are all integers; use integer arithmetic.

**Cubic {001}**  
$N_{\text{NC}}^{\text{cube}}[i] = 8i^3$  
$N_{\text{bnd}}^{\text{cube}}[i] = i\left[(4i-2)(4i-1)+1\right]$  
$N_{\text{IF}}^{\text{cube}}[i] = 6\left[(2i-1)^2+3i-1\right]$  

**Octahedral {111}**  
$N_{\text{NC}}^{\text{octa}}[i] = \frac{1}{3}(i+1)\left[4(i+1)^2-1\right]$  
$N_{\text{bnd}}^{\text{octa}}[i] = 2i(i+1)+\frac{4}{3}i(i+1)(2i+1)$  
$N_{\text{IF}}^{\text{octa}}[i] = 4(i+1)^2$  

**Dodecahedral {110} (odd class)**  
$N_{\text{NC},\text{odd}}^{\text{dod}}[i] = 16i\left[(i+1)(24i+9)-8(i+1)(2i+1)\right] + 10(4i+1)$  
$N_{\text{bnd},\text{odd}}^{\text{dod}}[i] = 16i\left[3(16i+5)(i+1)-16(i+1)(2i+1)\right] + 4(23i+3)$  
$N_{\text{IF},\text{odd}}^{\text{dod}}[i] = 128i(i+1)-184i+112$  

**Dodecahedral {110} (even class)**  
$N_{\text{NC},\text{even}}^{\text{dod}}[i] = 16i\left[(24i+21)(i+1)-8(i+1)(2i+1)\right] + 88(i+1)$  
$N_{\text{bnd},\text{even}}^{\text{dod}}[i] = 16i\left[3(16i+13)(i+1)-16(i+1)(2i+1)\right] + 140(i+1)$  
$N_{\text{IF},\text{even}}^{\text{dod}}[i] = 128i(i+1)-56i+136$  

**Pyramidal {001} base, {111} sides**  
$N_{\text{NC}}^{\text{pyra}}[i] = \frac{1}{6}i(i+1)\left[2(2i+1)+9\right] + i+1$  
$N_{\text{bnd}}^{\text{pyra}}[i] = \frac{2}{3}i(i+1)(2i+1) + i(i+1)$  
$N_{\text{IF}}^{\text{pyra}}[i] = 4(i+1)^2$  

**Tetrahedral {111}**  
$N_{\text{NC}}^{\text{tetra}}[i] = \frac{1}{6}i(i+1)(2i+1) + (i+1)^2$  
$N_{\text{bnd}}^{\text{tetra}}[i] = \frac{1}{3}i(i+1)(2i+1) + i(i+1)$  
$N_{\text{IF}}^{\text{tetra}}[i] = 2(i+1)(i+2)$  

**Quatrodecahedral {111}-dominant**  
$N_{\text{NC}}^{\text{q111}}[i] = 9i(2i+1)^2 + (2i+1) - i(4i+5)(i+1)$  
$N_{\text{bnd}}^{\text{q111}}[i] = 2i(3i+1)(12i+5) - \left[4i(i+1)(2i+1) + 6i(i+1)\right]$  
$N_{\text{IF}}^{\text{q111}}[i] = (6i+2)^2$  

**Quatrodecahedral {001}-dominant**  
$N_{\text{NC}}^{\text{q001}}[i] = (2i+7)\left[(i+4)^2 + \frac{2}{3}(i+3)\left(i+\frac{5}{2}\right)\right] + 2(i+3)\left[(i+4)^2 + i\right] + \frac{4}{3}(i+1)(i+2)(i+3)$  
$N_{\text{bnd}}^{\text{q001}}[i] = 4\left[6(i+3)^2 + (i+1)\left(i\left(\frac{10}{3}i + \frac{11}{3}\right) + \frac{9}{2}i + 5\right) + 7(2i+3)(i+2)\right]$  
$N_{\text{IF}}^{\text{q001}}[i] = 4(2i+7)^2$

## Reproduction target
Compute $N_{\text{NC}}$, $N_{\text{bnd}}$, and $N_{\text{IF}}$ for each of the seven nanocrystal shapes (cube, octahedron, dodecahedron, pyramid, tetrahedron, quatro_111, quatro_001) and for each applicable subclass (odd/even for dodecahedron) over the index range $i = 1, 2, \dots, 7$. Write a single CSV file `nc_formulas_values.csv` under `/app/outputs/`. The CSV must contain one row per (shape, subclass, i) combination with the exact integer values, using the following columns:
- `shape`: one of the string labels `cube`, `octahedron`, `dodecahedron`, `pyramid`, `tetrahedron`, `quatro_111`, `quatro_001`.
- `subclass`: empty string for all shapes except dodecahedron, where it must be `odd` or `even`.
- `i`: integer from 1 to 7.
- `N_NC`: integer number of nanocrystal atoms.
- `N_bnd`: integer number of bonds between nanocrystal atoms.
- `N_IF`: integer number of interface bonds.

## Assets
No external datasets, models, or pre-trained assets are required. All needed formulas are provided in the Approach section above. The workflow only needs standard Python libraries (e.g., `csv`, `math`). Install them if necessary from the default PyPI mirror.

## Workflow steps

### Step 1: Compute nanocrystal number series
- Role: scored (load-bearing)
- Action: Implement the explicit formulas (given in the paper) for each of the seven zinc-blende nanocrystal shapes: cubic, octahedral, dodecahedral (odd and even classes), pyramidal, tetrahedral, {111}-dominant quatrodecahedral, {001}-dominant quatrodecahedral. Evaluate N_NC (number of NC atoms), N_bnd (number of bonds between NC atoms), and N_IF (number of interface bonds) for size index i from 1 to 7. Write the results to nc_formulas_values.csv.
- Output file: `/app/outputs/nc_formulas_values.csv`
- Format: csv
- Contract: shape (string, one of: cube, octahedron, dodecahedron, pyramid, tetrahedron, quatro_111, quatro_001), subclass (string, empty for most shapes, 'odd' or 'even' for dodecahedron), i (int), N_NC (int), N_bnd (int), N_IF (int)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nc_formulas_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nc_formulas_values.csv
- path: `/app/outputs/nc_formulas_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV containing the computed integer counts of atoms, bonds, and interface bonds for each zinc-blende nanocrystal shape, subclass, and size index i=1..7.
- schema:
  - `type`: table
  - `required_columns`: `shape`, `subclass`, `i`, `N_NC`, `N_bnd`, `N_IF`
  - `units`:
    - `N_NC`: integer
    - `N_bnd`: integer
    - `N_IF`: integer

Notes: The hidden checker reimplements the explicit formulas from the paper and compares each row's integer values exactly. All rows must match exactly for full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nc_formulas_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "shape",
          "subclass",
          "i",
          "N_NC",
          "N_bnd",
          "N_IF"
        ],
        "units": {
          "N_NC": "integer",
          "N_bnd": "integer",
          "N_IF": "integer"
        }
      },
      "description": "CSV containing the computed integer counts of atoms, bonds, and interface bonds for each zinc-blende nanocrystal shape, subclass, and size index i=1..7."
    }
  ],
  "notes": "The hidden checker reimplements the explicit formulas from the paper and compares each row's integer values exactly. All rows must match exactly for full credit."
}
```

## How you are scored
A hidden verifier independently reimplements the same analytical formulas for each shape and subclass, producing an exact integer reference table for all i = 1..7. It reads your `nc_formulas_values.csv` and compares every row's `N_NC`, `N_bnd`, `N_IF` against the reference. The comparison uses integer exact match (tolerance = 0). All rows must match exactly to earn full credit; any discrepancy reduces the score proportionally. The final reward is a weighted average across all rows, with the scored artifact weighted as 1.0 for this task.
