# Compute 3d Electron Configurations and Magnetic Moments for Transition Metals

## Problem background
In the crystalline state, the electron configurations of transition metal atoms differ from their free‑atom configurations, largely because the spatial extent of the 3d charge density changes and inter‑electronic overlap between neighbours becomes important. A theoretical framework has been proposed that connects the effective radius of the 3d electrons, the effective nuclear charge acting on them, and the degree of overlap to the total number of 3d electrons per atom and to the fractional magnetic moment. This task implements that framework to compute, for a set of 3d metals in face‑centred cubic (f.c.c.) and simple cubic (s.c.) structures, the effective radius, effective nuclear charge, overlap parameters, fractional magnetic moment, total 3d electron count (via two different formulas), and the resulting electron configurations.

## Approach
The model characterises a metal atom by an effective radius $R$ (in atomic units) that depends on the total number of valence electrons $C$ (3d + 4s) and on an indicator $K$ ($K=0$ if $C\le 8$, $K=1$ if $C>8$):

$$
R = 0.065 \left[ \left(\frac{C}{2}\right)^2 - (4.75+K)(C-8) + 5 \right] .
$$

From $R$ one obtains the effective nuclear charge for the 3d electrons:

$$
Z(3d) = \frac{9}{R} .
$$

Overlap parameters that quantify the interaction between the 3d electrons of an atom and those of its neighbours are defined as

$$
b_1 = 0.6780\, n_1 \, (r_1 - R), \qquad
b_2 = 0.6780\, n_2 \, (r_2 - R),
$$

where $n_1$ is the number of nearest neighbours, $r_1$ the nearest‑neighbour distance, $n_2$ the number of next‑nearest neighbours, and $r_2$ the next‑nearest‑neighbour distance. All distances are in atomic units.

The fractional magnetic moment $\Delta m$ (in $\mu_{\mathrm{B}}$) is computed with a formula that differs between the two subgroups considered here:

- **Ni subgroup (f.c.c. ferromagnetic metals: Cu, Ni, Co, Fe, Mn, Cr)**
  $$
  \Delta m = \frac{3 Z(3d) - K b_1 - C_{\max}}{2},
  \qquad C_{\max}=10.
  $$

- **V subgroup (s.c.‑in‑f.c.c. metals: Sc, Ti, V, Cr)**
  $$
  \Delta m = \frac{Z(3d) - C_{\max}}{2} + b_2,
  \qquad C_{\max}=6.
  $$

Two prescriptions are used to estimate the total number of 3d electrons per atom, $N_{\mathrm{tot}}$.

**Method (8):**

$$
N_{\mathrm{tot}}^{(8)} = 8 + b_1 - \left( \frac{3 Z(3d) - K b_1}{2} - 5 \right) \cdot 0.1 .
$$

**Method (9):**

$$
N_{\mathrm{tot}}^{(9)} = N_{\mathrm{tot}}^{\mathrm{free}}(3d) + \Delta m ,
$$

where $N_{\mathrm{tot}}^{\mathrm{free}}(3d)$ is the total number of 3d electrons in the normal free atom (the number obtained from the free‑atom electron configuration).

Electron configurations are written as $3d^{N_{\mathrm{tot}}}\,4s^{C-N_{\mathrm{tot}}}$, retaining the computed fractional numbers to one or two decimal places.

The input parameters for each element/structure combination are listed in the table below.

| element | structure       | $a$     | $C$ | $N_{\mathrm{free}}(3d)$ | $r_1$   | $r_2$   | $n_1$ | $n_2$ | $C_{\max}$ | $K$ |
|---------|-----------------|---------|-----|--------------------------|---------|---------|-------|-------|--------------|-----|
| Cu      | f.c.c.          | 6.8309  | 11  | 9                        | 2.4151  | 3.4154  | 12    | 6     | 10           | 1   |
| Ni      | f.c.c.          | 6.6590  | 10  | 8                        | 2.3543  | 3.3295  | 12    | 6     | 10           | 1   |
| Co      | f.c.c.          | 6.6975  | 9   | 7                        | 2.3679  | 3.3487  | 12    | 6     | 10           | 1   |
| Fe      | f.c.c.          | 6.8922  | 8   | 6                        | 2.4368  | 3.4461  | 12    | 6     | 10           | 0   |
| Mn      | f.c.c.          | 7.1266  | 7   | 5                        | 2.440   | 2.5227  | 12    | 6     | 10           | 0   |
| Cr      | f.c.c.          | 5.1361  | 6   | 5                        | 2.5605  | 2.5680  | 12    | 6     | 10           | 0   |
| Sc      | s.c. in f.c.c.  | 6.9855  | 3   | 1                        | 3.062   | 4.3302  | 6     | 6     | 6            | 0   |
| Ti      | s.c. in f.c.c.  | 6.2949  | 4   | 2                        | 2.754   | 3.8941  | 6     | 6     | 6            | 0   |
| V       | s.c. in f.c.c.  | 5.7225  | 5   | 3                        | 2.478   | 3.5036  | 6     | 6     | 6            | 0   |
| Cr      | s.c. in f.c.c.  | 5.1361  | 6   | 5                        | 1.816   | 2.5680  | 6     | 6     | 6            | 0   |

For the Ni‑subgroup f.c.c. entries the nearest‑ and next‑nearest‑neighbour distances $r_1$, $r_2$ are taken directly from the published crystallographic data. For the V‑subgroup s.c.‑in‑f.c.c. entries the nearest‑neighbour distance $r_1$ is computed from the given $r_2$ via the simple‑cubic relation $r_1 = r_2 / \sqrt{2}$, and $n_1 = n_2 = 6$ as appropriate for the considered sub‑lattice.

## Reproduction target
Compute the quantities defined above for the ten element/structure combinations listed in the input table. Write the results to `/app/outputs/computed_properties.csv`, a CSV file with exactly one header row and the following columns in this order:

`element, structure, R, Z3d, b1, b2, Delta_m, Ntot_8, Ntot_9, EC_8, EC_9`

- `element` : chemical symbol (string)
- `structure` : structural label, exactly one of "f.c.c." or "s.c. in f.c.c."
- Numerical columns `R`, `Z3d`, `b1`, `b2`, `Delta_m`, `Ntot_8`, `Ntot_9` : computed values given to at least three significant figures; do not append units (units are atomic units for lengths and dimensionless otherwise, $\mu_B$ for $\Delta m$).
- `EC_8` and `EC_9` : electron configuration strings formatted as `3d^X 4s^Y`, where $X$ is the value from the corresponding $N_{\mathrm{tot}}$ column (retain one decimal place) and $Y = C - X$ (also one decimal place).

All ten rows must be present. The order of the rows is not prescribed, but every combination shown in the input table must appear exactly once.

## Assets

- Reference atomic and crystallographic data

## Workflow steps

### Step 1: Compile input parameters
- Role: process
- Action: Collect the required input constants for each element/structure from the provided tables: lattice constant a, free-atom total valence electron count C, free-atom total 3d electron count N_tot_free(3d), nearest-neighbor distance r1, next-nearest-neighbor distance r2, numbers of neighbors n1 and n2, subgroup parameters C_max (10 for Ni, 6 for Cr in V sub-group) and K indicator (0 if C≤8 else 1).
- Evidence: none

### Step 2: Compute effective radius, nuclear charge, and overlap parameters
- Role: process
- Action: For each element/structure, compute the effective radius R using the author's formula that relates R to C and K; compute effective nuclear charge Z(3d) = 9/R; compute overlap parameters b1 = 0.6780 * n1 * (r1 - R) and b2 = 0.6780 * n2 * (r2 - R).
- Evidence: `/app/outputs/intermediate_values.csv`

### Step 3: Compute fractional magnetic moments, total 3d electron numbers, and electron configurations
- Role: scored (load-bearing)
- Action: For each target element/structure (Ni sub-group f.c.c.: Cu, Ni, Co, Fe, Mn, Cr; V sub-group s.c. in f.c.c.: Sc, Ti, V, Cr), using the computed intermediate values (R, Z(3d), b1, b2), compute the fractional magnetic moment contribution Δm using the appropriate subgroup formula (ferromagnetic f.c.c. or V sub-group s.c. in f.c.c.). Compute total 3d electron count via method 8 and method 9 as described by the author. Derive the electron configurations (3d^x 4s^y) for both methods. Output all computed quantities in CSV format.
- Output file: `/app/outputs/computed_properties.csv`
- Format: csv
- Contract: element,structure,R,Z3d,b1,b2,Delta_m,Ntot_8,Ntot_9,EC_8,EC_9
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.csv
- path: `/app/outputs/computed_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The main reproduction artifact: a table of computed atomic properties for selected 3d metals in f.c.c. and s.c. in f.c.c. structures, reproducing the key quantities from the paper’s Table 2.
- schema:
  - `type`: table
  - `required_columns`: `element`, `structure`, `R`, `Z3d`, `b1`, `b2`, `Delta_m`, `Ntot_8`, `Ntot_9`, `EC_8`, `EC_9`
  - `units`:
    - `R`: atomic units (Bohr)
    - `Z3d`: dimensionless
    - `b1`: dimensionless
    - `b2`: dimensionless
    - `Delta_m`: μB
    - `Ntot_8`: electrons
    - `Ntot_9`: electrons
    - `EC_8`: configuration string (e.g., 3d^X 4s^Y)
    - `EC_9`: configuration string

Notes: The checker compares each numerical column against hidden reference values (the paper’s reported numbers) with a tolerance, and verifies electron configuration format consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "structure",
          "R",
          "Z3d",
          "b1",
          "b2",
          "Delta_m",
          "Ntot_8",
          "Ntot_9",
          "EC_8",
          "EC_9"
        ],
        "units": {
          "R": "atomic units (Bohr)",
          "Z3d": "dimensionless",
          "b1": "dimensionless",
          "b2": "dimensionless",
          "Delta_m": "μB",
          "Ntot_8": "electrons",
          "Ntot_9": "electrons",
          "EC_8": "configuration string (e.g., 3d^X 4s^Y)",
          "EC_9": "configuration string"
        }
      },
      "description": "The main reproduction artifact: a table of computed atomic properties for selected 3d metals in f.c.c. and s.c. in f.c.c. structures, reproducing the key quantities from the paper’s Table 2."
    }
  ],
  "notes": "The checker compares each numerical column against hidden reference values (the paper’s reported numbers) with a tolerance, and verifies electron configuration format consistency."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your `computed_properties.csv` file. For each numerical cell (`R`, `Z3d`, `b1`, `b2`, `Delta_m`, `Ntot_8`, `Ntot_9`) the verifier compares your value against a reference value derived from the analytical model described above. Cells that fall within an undisclosed tolerance of the reference earn full credit for that cell; cells that deviate more receive partial credit that decreases continuously with the size of the deviation. Electron configuration strings are checked for correct format and for consistency with the corresponding $N_{\mathrm{tot}}$ and total valence electron count $C$. The final score is a weighted average over all scored cells and structural checks, with the highest weight placed on the magnetic moment $\Delta m$ and the total 3d‑electron counts. The verifier does not require perfect agreement with any published table; it rewards honest computation according to the prescribed formulas and input data.
