# Evaluation of DFT functionals for silicon and Cu-doped silicon cluster geometries

## Problem background
Density functional theory (DFT) is a workhorse for studying silicon clusters and metal‑doped silicon clusters, which are relevant to nanoelectronics. The popular hybrid functional B3LYP is widely used because of its reliability, but its computational cost motivates the search for cheaper functionals that can deliver comparable accuracy. Several exchange‑correlation functionals from different rungs of Jacob's ladder (GGA, meta‑GGA, and hybrid GGA) have been proposed, yet their performance on small Si and Cu‑doped Si clusters has not been systematically benchmarked. This task evaluates a set of such functionals by comparing the equilibrium geometries (bond lengths and bond angles) they predict for a series of selected clusters against a well‑established B3LYP/6‑311+G* reference, in order to identify candidates that may provide a cost‑effective alternative to B3LYP.

## Approach
The core idea is to perform all‑electron DFT geometry optimizations for the most stable isomers of eight cluster compositions — Si₂, CuSi, Si₃, CuSi₂, Si₄, CuSi₃, Si₅, and CuSi₄ — using six different exchange‑correlation functionals (OLYP, OPW91, OB95, VSXC, PBE0, and B3LYP) paired with the 6‑311+G* basis set, and to extract the resulting equilibrium bond lengths and bond angles. The procedure has two stages. First, the most stable isomer for each composition is identified by running B3LYP/6‑311+G* optimisations starting from plausible initial structures, testing several candidate isomers, and verifying minima via vibrational frequency analysis. Second, each obtained reference geometry is re‑optimised with every functional using the same 6‑311+G* basis set; after optimisation, a frequency calculation confirms the structure is still a minimum. From the final optimised structures, the specific interatomic distances and bond angles that define the cluster geometry are extracted and compiled into a single table, enabling a direct comparison across functionals.

## Reproduction target
Use an open‑source DFT package (ORCA is recommended) to perform full geometry optimisations and vibrational frequency checks for the eight clusters Si₂, CuSi, Si₃, CuSi₂, Si₄, CuSi₃, Si₅, and CuSi₄. Start by obtaining the most stable B3LYP/6‑311+G* geometry for each composition; then, for each cluster, run a separate geometry optimisation with each of the six functionals OLYP, OPW91, OB95, VSXC, PBE0, and B3LYP, all with the 6‑311+G* basis set. From every optimised structure, extract the relevant bond lengths (e.g., r(Si–Si), r(Cu–Si)) and bond angles (e.g., α(Si₁–Si₃–Si₂), α(Si₁–Cu–Si₂)) that characterise the cluster’s equilibrium shape. Collect all extracted parameters into a single CSV file `/app/outputs/geometries.csv` with columns: `cluster`, `functional`, `parameter`, `value`, `unit` (where `unit` is "Å" for bond lengths and "°" for angles). The CSV should contain one row per unique cluster–functional–parameter combination.

## Assets

- ORCA quantum chemistry package: https://www.orcaforum.com
- 6-311+G* basis set: standard basis set library in ORCA/Gaussian/etc.

## Workflow steps

### Step 1: Obtain reference B3LYP/6-311+G* most-stable-isomer geometries
- Role: process
- Action: Using a DFT program, perform B3LYP/6-311+G* geometry optimizations for each cluster composition (Si₂, CuSi, Si₃, CuSi₂, Si₄, CuSi₃, Si₅, CuSi₄) starting from plausible initial structures. For each composition, test several candidate isomers to identify the lowest-energy structure (most stable isomer). Confirm each structure is a true minimum by checking for absence of imaginary vibrational frequencies. Save the final Cartesian coordinates of each most-stable isomer for use in the next step.
- Evidence: none

### Step 2: Compute equilibrium geometries for six functionals and compile table
- Role: scored (load-bearing)
- Action: For each of the six exchange-correlation functionals (OLYP, OPW91, OB95, VSXC, PBE0, B3LYP), perform a full geometry optimization for every cluster using the 6-311+G* basis set, starting from the reference B3LYP geometry obtained in the previous step. After optimization, run a frequency calculation to confirm the structure is a minimum. From the optimized structure, extract the following geometric parameters using the exact parameter names given:
    - Si2: `r(Si-Si)`
    - CuSi: `r(Si-Cu)`
    - Si3: `r(Si1-Si3)`, `r(Si1-Si2)`, `α(Si1-Si3-Si2)`
    - CuSi2: `r(Si1-Cu)`, `r(Si1-Si2)`, `α(Si1-Cu-Si2)`
    - Si4: `r(Si1-Si4)`, `r(Si1-Si2)`, `α(Si1-Si3-Si2)`
    - CuSi3: `r(Si1-Cu)`, `r(Si1-Si3)`, `α(Si1-Si3-Si2)`, `α(Si1-Cu-Si2)`
    - Si5: `r(Si1-Si2)`, `r(Si1-Si3)`, `r(Si3-Si4)`
    - CuSi4: `r(Si1-Cu)`, `r(Si4-Cu)`, `r(Si1-Si2)`, `r(Si1-Si3)`, `r(Si1-Si4)`, `α(Si3-Si1-Si2-Si4)`
  Compile all extracted values into a single CSV file.
- Output file: `/app/outputs/geometries.csv`
- Format: csv
- Contract: The CSV must have exactly the following columns in any order: `cluster`, `functional`, `parameter`, `value`, `unit`. For every cluster listed above, every functional in (OLYP, OPW91, OB95, VSXC, PBE0, B3LYP), and every parameter named for that cluster, there must be one row with the `parameter` field set to the exact string defined above. Bond length values must be in Å, angle values in °, both as floating-point numbers. No extra rows may be present.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/geometries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### geometries.csv
- path: `/app/outputs/geometries.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed equilibrium bond lengths and bond angles for the most stable isomers of Si_{n+1} (n=1-4) and CuSi_n (n=1-4) clusters, covering all six functionals.
- schema:
  - `columns`: `cluster`, `functional`, `parameter`, `value`, `unit`
  - `cluster_enum`: `Si2`, `CuSi`, `Si3`, `CuSi2`, `Si4`, `CuSi3`, `Si5`, `CuSi4`
  - `functional_enum`: `OLYP`, `OPW91`, `OB95`, `VSXC`, `PBE0`, `B3LYP`
  - `parameter_map`:
    - `Si2`: `r(Si-Si)`
    - `CuSi`: `r(Si-Cu)`
    - `Si3`: `r(Si1-Si3)`, `r(Si1-Si2)`, `α(Si1-Si3-Si2)`
    - `CuSi2`: `r(Si1-Cu)`, `r(Si1-Si2)`, `α(Si1-Cu-Si2)`
    - `Si4`: `r(Si1-Si4)`, `r(Si1-Si2)`, `α(Si1-Si3-Si2)`
    - `CuSi3`: `r(Si1-Cu)`, `r(Si1-Si3)`, `α(Si1-Si3-Si2)`, `α(Si1-Cu-Si2)`
    - `Si5`: `r(Si1-Si2)`, `r(Si1-Si3)`, `r(Si3-Si4)`
    - `CuSi4`: `r(Si1-Cu)`, `r(Si4-Cu)`, `r(Si1-Si2)`, `r(Si1-Si3)`, `r(Si1-Si4)`, `α(Si3-Si1-Si2-Si4)`

Notes: Only geometric parameters are scored. The hidden verifier checks values against the paper's Table I B3LYP reference with tolerances of ±0.05 Å for bond lengths and ±2° for angles.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "columns": [
          "cluster",
          "functional",
          "parameter",
          "value",
          "unit"
        ],
        "cluster_enum": [
          "Si2",
          "CuSi",
          "Si3",
          "CuSi2",
          "Si4",
          "CuSi3",
          "Si5",
          "CuSi4"
        ],
        "functional_enum": [
          "OLYP",
          "OPW91",
          "OB95",
          "VSXC",
          "PBE0",
          "B3LYP"
        ],
        "parameter_map": {
          "Si2": [
            "r(Si-Si)"
          ],
          "CuSi": [
            "r(Si-Cu)"
          ],
          "Si3": [
            "r(Si1-Si3)",
            "r(Si1-Si2)",
            "α(Si1-Si3-Si2)"
          ],
          "CuSi2": [
            "r(Si1-Cu)",
            "r(Si1-Si2)",
            "α(Si1-Cu-Si2)"
          ],
          "Si4": [
            "r(Si1-Si4)",
            "r(Si1-Si2)",
            "α(Si1-Si3-Si2)"
          ],
          "CuSi3": [
            "r(Si1-Cu)",
            "r(Si1-Si3)",
            "α(Si1-Si3-Si2)",
            "α(Si1-Cu-Si2)"
          ],
          "Si5": [
            "r(Si1-Si2)",
            "r(Si1-Si3)",
            "r(Si3-Si4)"
          ],
          "CuSi4": [
            "r(Si1-Cu)",
            "r(Si4-Cu)",
            "r(Si1-Si2)",
            "r(Si1-Si3)",
            "r(Si1-Si4)",
            "α(Si3-Si1-Si2-Si4)"
          ]
        }
      },
      "description": "Computed equilibrium bond lengths and bond angles for the most stable isomers of Si_{n+1} (n=1-4) and CuSi_n (n=1-4) clusters, covering all six functionals."
    }
  ],
  "notes": "Only geometric parameters are scored. The hidden verifier checks values against the paper's Table I B3LYP reference with tolerances of ±0.05 Å for bond lengths and ±2° for angles."
}
```

## How you are scored
A hidden verifier reads your submitted `geometries.csv`. For each row, it extracts the reported bond length or bond angle and compares it, in the appropriate physical units, against a gold‑standard reference value derived from a benchmark B3LYP/6‑311+G* calculation (the paper’s Table I). The comparison checks whether your computed parameter falls within an acceptable margin of the reference; closer agreement yields higher credit. The verifier then combines the per‑parameter outcomes into a single reward score between 0 and 1, weighting the agreement across all required cluster–functional–parameter combinations. Merely transcribing a known table is not enough—the reward reflects how well your own DFT‑computed geometries reproduce the expected values.
