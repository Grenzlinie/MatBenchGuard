# First-principles DFT calculation of band gaps and conduction band composition for ALa9(GeO4)6O2 apatites

## Problem background
Oxyapatites with general formula ALa9(GeO4)6O2 are promising host materials for rare-earth activated phosphors. The optical properties of these compounds are intimately linked to their electronic structure—specifically, the magnitude of the band gap and the character of the conduction band edge. Understanding how the choice of alkali-metal (or vacancy-stabilized) A-site cation influences the band gap and the relative contributions of La 5d states from the two distinct crystallographic positions (4f and 6h) is essential for designing efficient luminescent materials. This task aims to compute those electronic-structure quantities for the full ALa9(GeO4)6O2 series.

## Approach
Use density functional theory (DFT) within the generalized gradient approximation (GGA) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional, as implemented in the open‑source SIESTA code or an equivalent plane‑wave/atom‑centered DFT package. For each compound in the series—LiLa9(GeO4)6O2, NaLa9(GeO4)6O2, KLa9(GeO4)6O2, RbLa9(GeO4)6O2, CsLa9(GeO4)6O2, and the vacancy‑stabilized La1/3La9(GeO4)6O2—perform a variable‑cell geometry relaxation starting from the experimentally reported crystal structures. Then, compute the electronic band structure along high‑symmetry paths and extract the direct band gap at the Γ point. Additionally, calculate the projected density of states (PDOS) for the La 5d orbitals on the 4f and 6h sites to determine which contribution dominates the conduction band minimum within a small energy window above the band edge.

## Reproduction target
For the six oxyapatite compounds (Li, Na, K, Rb, Cs, La1/3), produce (1) a CSV file containing the computed direct band gap at Γ (in eV) and the gap type, and (2) a JSON file mapping each compound to the dominant La 5d character at the conduction band minimum: either "La5d(6h)", "La5d(4f)", or "equal" if the two contributions are nearly identical. All results must be obtained by executing the DFT workflow described in the steps; simply transcribing reported values does not fulfill the output contract.

## Assets

- DFT code: SIESTA or equivalent GGA-PBE DFT code (https://gitlab.com/siesta-project/siesta)
- Pseudopotentials: norm-conserving Troullier–Martins pseudopotentials for La, Ge, O, Li, Na, K, Rb, Cs (can be generated with standard atomic codes or taken from public pseudopotential libraries).
- Initial crystal structures: the compounds crystallize in the hexagonal space group P6_3/m (Z=1). The atomic positions for the apatite framework are well known; they can be adopted from the structure of NaLa9(GeO4)6O2 reported by Takahashi et al., J. Solid State Chem. 139 (1998) 304–309. The starting lattice parameters for each A cation are (in Å):
  Li: a=9.892, c=7.222; Na: a=9.894, c=7.265; K: a=9.920, c=7.323; Rb: a=9.939, c=7.346; Cs: a=9.948, c=7.357; La1/3: a=9.816, c=7.302.
  For the vacancy-stabilized La1/3 composition, a 1×1×3 supercell with one La vacancy at a 4f site should be constructed from the above cell. Build a starting CIF for each compound using these lattice constants and the atomic positions from the Na compound, substituting the A cation at the 4f site as needed.

## Workflow steps

### Step 1: DFT geometry optimization of ALa9(GeO4)6O2
- Role: process
- Action: Perform variable-cell DFT geometry optimization using the GGA-PBE functional for each compound ALa9(GeO4)6O2 (A = Li, Na, K, Rb, Cs, La1/3) starting from the experimental crystal structures. Relax both atomic positions and lattice vectors until forces and stresses are converged. Preserve the relaxed structures for subsequent steps.
- Evidence: `/app/outputs/geometry_optimizations.log`

### Step 2: Extract direct band gaps at Γ
- Role: scored
- Action: From the relaxed structures, compute the electronic band structure and extract the direct band gap at the Γ point. Record the value in eV and confirm the gap type is direct.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: columns: compound (string), band_gap_direct (float, eV), band_gap_type (string, expected 'direct')
- Scoring: scored by hidden verifier

### Step 3: Determine La 5d CBM dominance
- Role: scored (load-bearing)
- Action: Compute the projected density of states (PDOS) for La 5d orbitals from the 4f and 6h sites. For each compound, identify which La 5d projection has higher intensity within the first 0.1 eV above the conduction band minimum (CBM). Assign 'La5d(6h)' or 'La5d(4f)' accordingly, or 'equal' if they are nearly identical.
- Output file: `/app/outputs/cbm_dominance.json`
- Format: json
- Contract: JSON object with keys: Li, Na, K, Rb, Cs, La1/3; values: one of 'La5d(6h)', 'La5d(4f)', 'equal'
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.csv`
- `/app/outputs/cbm_dominance.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV file with one row per compound giving the computed direct band gap and gap type.
- schema:
  - `type`: table
  - `required_columns`: `compound`, `band_gap_direct`, `band_gap_type`
  - `units`:
    - `band_gap_direct`: eV

### cbm_dominance.json
- path: `/app/outputs/cbm_dominance.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON object mapping each compound name to the dominant La 5d contribution at the conduction band minimum.
- schema:
  - `type`: object
  - `required`: object
  - `items`:
    - `value`: string, one of 'La5d(6h)', 'La5d(4f)', 'equal'

Notes: The band gaps are extracted after geometry relaxation and compared to the paper's reported direct gap values with tolerance. The CBM dominance classification is compared to the paper's assignments.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound",
          "band_gap_direct",
          "band_gap_type"
        ],
        "units": {
          "band_gap_direct": "eV"
        }
      },
      "description": "CSV file with one row per compound giving the computed direct band gap and gap type."
    },
    {
      "file": "cbm_dominance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {},
        "items": {
          "value": "string, one of 'La5d(6h)', 'La5d(4f)', 'equal'"
        }
      },
      "description": "JSON object mapping each compound name to the dominant La 5d contribution at the conduction band minimum."
    }
  ],
  "notes": "The band gaps are extracted after geometry relaxation and compared to the paper's reported direct gap values with tolerance. The CBM dominance classification is compared to the paper's assignments."
}
```

## How you are scored
A hidden verifier will independently score each of the two output artifacts (band_gaps.csv and cbm_dominance.json). The verifier compares your computed band gaps and dominance assignments against reference values derived from the work that introduced these materials. Comparisons for the band gaps use a tolerance that accounts for the typical spread between different GGA‑PBE implementations, while the dominance assignments are checked for exact agreement with the expected classification. Each artifact carries a weight, and the verifier combines the partial scores into a final reward between 0 and 1—higher consistency with the reference yields a higher reward. Reporting numbers from the literature without actually performing the DFT calculations does not satisfy the scoring criteria.
