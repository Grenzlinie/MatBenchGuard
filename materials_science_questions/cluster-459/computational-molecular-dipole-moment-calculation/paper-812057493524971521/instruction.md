# Computational Evidence of Physical Achirality in Hydrazine and Boranylborane Rotamers

## Problem background
Axially chiral molecules that lack improper rotations are geometrically chiral, yet their chiroptical response may still vanish at certain dihedral angles due to the physical inability of the electron cloud to sustain induced toroidal or helical currents. This phenomenon, termed physical achirality, is studied here for three small H–X–X–H systems: hydrazine (N₂H₄), boranylborane (B₂H₄), and ethane (C₂H₆). The diagonal components of the static anapole magnetizability tensor (a⍺⍺, with isotropic average ˉa) and the frequency-dependent mixed electric-dipole–magnetic-dipole polarisability (κ'⍺⍺, with isotropic average ˉκ') are computed as functions of the H–X–X–H dihedral angle φ. The goal is to discover whether these components exhibit accidental zeros—or remain non-zero—for geometrically chiral rotamers, and under which conditions such behavior occurs.

## Approach
Use first-principles quantum chemistry to compute the required tensor components. For each molecule, optimize the equilibrium geometry at the B3LYP level with a triple-zeta quality basis set. Generate rigid conformers by scanning the dihedral angle φ while keeping all other internal coordinates fixed: for hydrazine and boranylborane, scan φ from 0° to 180° in steps ≤15°; for ethane, scan φ from 0° to 60° in steps ≤10°. At each φ, perform linear-response calculations (HF or B3LYP) with a basis of at least triple-zeta quality to obtain the static anapole magnetizability (a_xx, a_yy, a_zz, a_bar) and the frequency-dependent MEMDP at two optical wavelengths: 589.60 nm (ω=0.077278 a.u., Na D line) and 355.00 nm (ω=0.128347 a.u.). The results for each molecule are collected in a CSV file with columns: phi_deg, a_xx, a_yy, a_zz, a_bar, kappa_xx_Na, kappa_yy_Na, kappa_zz_Na, kappa_bar_Na, kappa_xx_355, kappa_yy_355, kappa_zz_355, kappa_bar_355 (all values in atomic units). Ethane serves as a structural control; its tensor components are expected to behave differently from those of hydrazine and boranylborane.

## Reproduction target
Produce three scored CSV artifacts under /app/outputs:

- `hydrazine_tensors.csv` – diagonal components and isotropic averages of anapole magnetizability and MEMDP for hydrazine at dihedral angles 0°–180° (step ≤15°).
- `boranylborane_tensors.csv` – same quantities for boranylborane over the same φ range.
- `ethane_tensors.csv` – same quantities for ethane over the range 0°–60° (step ≤10°).

Each CSV must contain exactly the columns: phi_deg, a_xx, a_yy, a_zz, a_bar, kappa_xx_Na, kappa_yy_Na, kappa_zz_Na, kappa_bar_Na, kappa_xx_355, kappa_yy_355, kappa_zz_355, kappa_bar_355. The reported values, recorded in atomic units, will be used to evaluate whether accidental zeros or near-zero behavior appear in the diagonal tensor components at specific dihedral angles for each molecule.

## Assets

- Quantum chemistry package (PySCF, Psi4, or equivalent) capable of HF, B3LYP, and linear-response magnetizability/polarizability calculations: https://pyscf.org
- Uncontracted (13s10p5d2f/11s7p4d) basis set or a comparable triple-zeta quality basis for anapole/mixed polarizability: https://www.basissetexchange.org
- Initial molecular coordinates for N2H4, B2H4, C2H6

## Workflow steps

### Step 1: Geometry optimization of N2H4, B2H4, and C2H6
- Role: process
- Action: Optimize the equilibrium geometries of hydrazine (N2H4), boranylborane (B2H4), and ethane (C2H6) at the B3LYP level using a triple-zeta quality basis set. Save the optimized Cartesian coordinates.
- Evidence: `/app/outputs/geom_opt.log`

### Step 2: Dihedral scan generation
- Role: process
- Action: From the optimized geometries, generate rigid conformers for each molecule by varying the H-X-X-H dihedral angle φ. For N2H4 and B2H4 generate φ from 0° to 180° in steps ≤15°. For C2H6 generate φ from 0° to 60° in steps ≤10°. Keep all other internal coordinates fixed. Save each conformer in a usable quantum chemistry input format (e.g., XYZ).
- Evidence: `/app/outputs/scan_coords.txt`

### Step 3: Hydrazine response tensors
- Role: scored (load-bearing)
- Action: For every dihedral angle φ of N2H4, compute the static anapole magnetizability diagonal components (a_xx, a_yy, a_zz, isotropic average a_bar) and the frequency-dependent MEMDP diagonal components (κ'_xx, κ'_yy, κ'_zz, isotropic average) at two wavelengths: 589.60 nm (ω=0.077278 a.u.) and 355.00 nm (ω=0.128347 a.u.). Use HF or B3LYP with a basis set of at least triple-zeta quality. Collect results and write hydrazine_tensors.csv.
- Output file: `/app/outputs/hydrazine_tensors.csv`
- Format: csv
- Contract: phi_deg (float, degrees), a_xx (float, a.u.), a_yy (float), a_zz (float), a_bar (float), kappa_xx_Na (float), kappa_yy_Na (float), kappa_zz_Na (float), kappa_bar_Na (float), kappa_xx_355 (float), kappa_yy_355 (float), kappa_zz_355 (float), kappa_bar_355 (float)
- Scoring: scored by hidden verifier

### Step 4: Boranylborane response tensors
- Role: scored (load-bearing)
- Action: For every dihedral angle φ of B2H4, compute the same set of tensor components and frequencies as for hydrazine. Write boranylborane_tensors.csv.
- Output file: `/app/outputs/boranylborane_tensors.csv`
- Format: csv
- Contract: Same columns as hydrazine_tensors.csv
- Scoring: scored by hidden verifier

### Step 5: Ethane response tensors
- Role: scored
- Action: For every dihedral angle φ of C2H6, compute the same set of tensor components and frequencies. Write ethane_tensors.csv.
- Output file: `/app/outputs/ethane_tensors.csv`
- Format: csv
- Contract: Same columns as hydrazine_tensors.csv
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hydrazine_tensors.csv`
- `/app/outputs/boranylborane_tensors.csv`
- `/app/outputs/ethane_tensors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hydrazine_tensors.csv
- path: `/app/outputs/hydrazine_tensors.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Diagonal components and isotropic averages of static anapole magnetizability and frequency-dependent MEMDP for hydrazine as a function of dihedral angle φ. The checker recomputes a metric (e.g., max absolute deviation from zero at φ=90°) from these raw values and scores against a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `phi_deg`, `a_xx`, `a_yy`, `a_zz`, `a_bar`, `kappa_xx_Na`, `kappa_yy_Na`, `kappa_zz_Na`, `kappa_bar_Na`, `kappa_xx_355`, `kappa_yy_355`, `kappa_zz_355`, `kappa_bar_355`
  - `units`:
    - `phi_deg`: degrees
    - `a_xx`: atomic units
    - `a_yy`: atomic units
    - `a_zz`: atomic units
    - `a_bar`: atomic units
    - `kappa_xx_Na`: atomic units
    - `kappa_yy_Na`: atomic units
    - `kappa_zz_Na`: atomic units
    - `kappa_bar_Na`: atomic units
    - `kappa_xx_355`: atomic units
    - `kappa_yy_355`: atomic units
    - `kappa_zz_355`: atomic units
    - `kappa_bar_355`: atomic units

### boranylborane_tensors.csv
- path: `/app/outputs/boranylborane_tensors.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Same structure as hydrazine_tensors.csv. The checker verifies that a_yy is near zero over the chiral range (e.g., 10°–170°) and that κ' diagonal components vanish at φ=90°.
- schema:
  - `type`: table
  - `required_columns`: `phi_deg`, `a_xx`, `a_yy`, `a_zz`, `a_bar`, `kappa_xx_Na`, `kappa_yy_Na`, `kappa_zz_Na`, `kappa_bar_Na`, `kappa_xx_355`, `kappa_yy_355`, `kappa_zz_355`, `kappa_bar_355`
  - `units`:
    - `phi_deg`: degrees
    - `a_xx`: atomic units
    - `a_yy`: atomic units
    - `a_zz`: atomic units
    - `a_bar`: atomic units
    - `kappa_xx_Na`: atomic units
    - `kappa_yy_Na`: atomic units
    - `kappa_zz_Na`: atomic units
    - `kappa_bar_Na`: atomic units
    - `kappa_xx_355`: atomic units
    - `kappa_yy_355`: atomic units
    - `kappa_zz_355`: atomic units
    - `kappa_bar_355`: atomic units

### ethane_tensors.csv
- path: `/app/outputs/ethane_tensors.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Negative control CSV. The checker ensures that the isotropic average κ'_bar_Na is non-zero at φ=30° and that no accidental zeros appear at chiral angles.
- schema:
  - `type`: table
  - `required_columns`: `phi_deg`, `a_xx`, `a_yy`, `a_zz`, `a_bar`, `kappa_xx_Na`, `kappa_yy_Na`, `kappa_zz_Na`, `kappa_bar_Na`, `kappa_xx_355`, `kappa_yy_355`, `kappa_zz_355`, `kappa_bar_355`
  - `units`:
    - `phi_deg`: degrees
    - `a_xx`: atomic units
    - `a_yy`: atomic units
    - `a_zz`: atomic units
    - `a_bar`: atomic units
    - `kappa_xx_Na`: atomic units
    - `kappa_yy_Na`: atomic units
    - `kappa_zz_Na`: atomic units
    - `kappa_bar_Na`: atomic units
    - `kappa_xx_355`: atomic units
    - `kappa_yy_355`: atomic units
    - `kappa_zz_355`: atomic units
    - `kappa_bar_355`: atomic units

Notes: All values are in atomic units. The checker recomputes metrics (e.g., maximum absolute deviation from zero at specified dihedral angles) from these raw CSVs and scores against hidden tolerances. No gold values or tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hydrazine_tensors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_deg",
          "a_xx",
          "a_yy",
          "a_zz",
          "a_bar",
          "kappa_xx_Na",
          "kappa_yy_Na",
          "kappa_zz_Na",
          "kappa_bar_Na",
          "kappa_xx_355",
          "kappa_yy_355",
          "kappa_zz_355",
          "kappa_bar_355"
        ],
        "units": {
          "phi_deg": "degrees",
          "a_xx": "atomic units",
          "a_yy": "atomic units",
          "a_zz": "atomic units",
          "a_bar": "atomic units",
          "kappa_xx_Na": "atomic units",
          "kappa_yy_Na": "atomic units",
          "kappa_zz_Na": "atomic units",
          "kappa_bar_Na": "atomic units",
          "kappa_xx_355": "atomic units",
          "kappa_yy_355": "atomic units",
          "kappa_zz_355": "atomic units",
          "kappa_bar_355": "atomic units"
        }
      },
      "description": "Diagonal components and isotropic averages of static anapole magnetizability and frequency-dependent MEMDP for hydrazine as a function of dihedral angle φ. The checker recomputes a metric (e.g., max absolute deviation from zero at φ=90°) from these raw values and scores against a hidden tolerance."
    },
    {
      "file": "boranylborane_tensors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_deg",
          "a_xx",
          "a_yy",
          "a_zz",
          "a_bar",
          "kappa_xx_Na",
          "kappa_yy_Na",
          "kappa_zz_Na",
          "kappa_bar_Na",
          "kappa_xx_355",
          "kappa_yy_355",
          "kappa_zz_355",
          "kappa_bar_355"
        ],
        "units": {
          "phi_deg": "degrees",
          "a_xx": "atomic units",
          "a_yy": "atomic units",
          "a_zz": "atomic units",
          "a_bar": "atomic units",
          "kappa_xx_Na": "atomic units",
          "kappa_yy_Na": "atomic units",
          "kappa_zz_Na": "atomic units",
          "kappa_bar_Na": "atomic units",
          "kappa_xx_355": "atomic units",
          "kappa_yy_355": "atomic units",
          "kappa_zz_355": "atomic units",
          "kappa_bar_355": "atomic units"
        }
      },
      "description": "Same structure as hydrazine_tensors.csv. The checker verifies that a_yy is near zero over the chiral range (e.g., 10°–170°) and that κ' diagonal components vanish at φ=90°."
    },
    {
      "file": "ethane_tensors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_deg",
          "a_xx",
          "a_yy",
          "a_zz",
          "a_bar",
          "kappa_xx_Na",
          "kappa_yy_Na",
          "kappa_zz_Na",
          "kappa_bar_Na",
          "kappa_xx_355",
          "kappa_yy_355",
          "kappa_zz_355",
          "kappa_bar_355"
        ],
        "units": {
          "phi_deg": "degrees",
          "a_xx": "atomic units",
          "a_yy": "atomic units",
          "a_zz": "atomic units",
          "a_bar": "atomic units",
          "kappa_xx_Na": "atomic units",
          "kappa_yy_Na": "atomic units",
          "kappa_zz_Na": "atomic units",
          "kappa_bar_Na": "atomic units",
          "kappa_xx_355": "atomic units",
          "kappa_yy_355": "atomic units",
          "kappa_zz_355": "atomic units",
          "kappa_bar_355": "atomic units"
        }
      },
      "description": "Negative control CSV. The checker ensures that the isotropic average κ'_bar_Na is non-zero at φ=30° and that no accidental zeros appear at chiral angles."
    }
  ],
  "notes": "All values are in atomic units. The checker recomputes metrics (e.g., maximum absolute deviation from zero at specified dihedral angles) from these raw CSVs and scores against hidden tolerances. No gold values or tolerances are revealed here."
}
```

## How you are scored
Each scored CSV artifact is evaluated independently by a hidden verifier. The verifier reads your computed diagonal components and isotropic averages and compares them against a set of predetermined physical conditions (e.g., expected magnitudes at certain dihedral angles, non-zero thresholds at others). These conditions encode the structural signatures of physical achirality; they are not revealed. The verifier computes per-artifact scores based on how well your submitted values satisfy the required conditions within acceptable tolerances. The overall reward is the weighted average of the three per-artifact scores: hydrazine (40%), boranylborane (40%), ethane (20%). A correct physical reproduction of the tensor components will earn full credit; systematic deviations reduce the score proportionally.
