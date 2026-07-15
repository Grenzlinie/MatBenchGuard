# Lithium-ion migration energy barriers from Bond Valence Site Energy calculations on argyrodite crystal structures

## Problem background
Solid-state lithium-ion conductors based on the argyrodite structure can achieve superionic conductivity when Li⁺ site disorder flattens the potential energy landscape and activates concerted ion migration. The Bond Valence Site Energy (BVSE) method uses the crystal structure to map the energy landscape for mobile ions, enabling the prediction of migration pathways and activation barriers without resorting to expensive first-principles simulations. In this task, BVSE is applied to two argyrodite compositions with different Li⁺ content to see how the migration barrier changes.

## Approach
Use the open-source SoftBV tool (or an equivalent BVSE implementation) to perform BVSE calculations on the neutron-derived crystal structures of Li₆SbS₅I (parent) and Li₆.₆Si₀.₆Sb₀.₄S₅I (Si-substituted). For each structure, map the Li⁺ energy landscape, identify the minimum-energy migration path, and extract the activation energy barrier (eV) for long-range Li⁺ diffusion. The results are written to a CSV file with columns composition and barrier_eV. The difference in barriers reflects the effect of Li⁺ concentration and site disorder on the energy landscape.

## Reproduction target
Compute the BVSE migration barriers for the parent composition Li₆SbS₅I and the Si-substituted composition Li₆.₆Si₀.₆Sb₀.₄S₅I (or the closest refined compositions) using the provided CIF files. Output a CSV file with two rows, one for each composition, containing the composition name and the computed barrier in eV. The goal is to obtain activation barriers for both compositions; the hidden verifier will assess if the Si-substituted composition exhibits a lower barrier than the parent and if its absolute value meets the expected low-activation-energy characteristic of this material.

## Assets

- Crystallographic data (CIFs) for Li6+xSixSb1-xS5I series: https://pubs.acs.org/doi/suppl/10.1021/jacs.9b08357
- SoftBV (Bond Valence Site Energy) software: https://github.com/eladn/softbv
- Python 3 environment with pymatgen, numpy, pandas: https://pypi.org/

## Workflow steps

### Step 1: Compute BVSE migration barriers
- Role: scored
- Action: Using the SoftBV tool (or an equivalent Bond Valence Site Energy implementation), perform BVSE calculations on the neutron-derived crystal structures of Li₆SbS₅I (x=0) and Li₆.₆Si₀.₆Sb₀.₄S₅I (x=0.6) from the provided CIF files. Map the Li⁺ energy landscape, identify the minimum-energy migration path, and extract the activation energy barrier (eV) for long-range Li⁺ diffusion. Write the extracted barriers to a CSV file.
- Output file: `/app/outputs/migration_barriers.csv`
- Format: csv
- Contract: CSV with columns: composition (string), barrier_eV (float). Exactly two rows corresponding to the parent and Si-substituted compositions.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_barriers.csv
- path: `/app/outputs/migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: BVSE migration barriers for two argyrodite compositions. The checker verifies that the Si-substituted barrier is lower than the parent barrier and meets a prescribed low value with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "BVSE migration barriers for two argyrodite compositions. The checker verifies that the Si-substituted barrier is lower than the parent barrier and meets a prescribed low value with tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by a hidden verifier that independently checks the CSV you produce. It verifies that the Si-substituted composition has a barrier lower than the parent by a meaningful margin and that the absolute barrier value for the Si-substituted composition falls within an acceptable tolerance around a known low value. The combined check yields a reward between 0 and 1; a trivial or fabricated output that does not satisfy both conditions receives low or zero credit.
