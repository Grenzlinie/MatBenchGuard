# Zn²⁺ Migration Energy Barrier in Layered Zinc Orthovanadate — Reproduction Task

## Problem background
Rechargeable zinc-ion batteries are attractive for low-cost, safe energy storage, but their rate capability is often limited by slow Zn²⁺ ion transport in the cathode. A layered zinc orthovanadate (Zn₂(OH)VO₄) cathode has demonstrated exceptional high-rate cycling in a quasi-solid-state configuration. The fast kinetics have been attributed to low in-plane Zn²⁺ migration barriers within the material's two-dimensional layered structure. The original study employed density functional theory (DFT) with the climbing-image nudged elastic band (CI-NEB) method to compute the migration barriers. Your task is to retrieve the reported barrier for the lowest-energy pathway, labelled **D1**, from the provided paper, and write it to a specified CSV file.

## Provided information
The D1 pathway corresponds to Zn²⁺ hopping between the Zn0 and Zn1 sites within the **b–c** plane of orthorhombic Zn₂(OH)VO₄ (space group *Pnma*, lattice constants *a* = 14.68 Å, *b* = 5.98 Å, *c* = 8.87 Å). The paper reports first-principles calculations of Zn²⁺ migration energies, including the lowest-energy in-plane barrier along the D1 path (see the section on first-principles calculations and the corresponding figure showing migration energy profiles). You need to locate the numerical value for this barrier in the paper.

## Reproduction target
Write the reported Zn²⁺ migration energy barrier for pathway D1 to the file `step_01_barrier.csv`. The file must be a CSV with columns `pathway` and `barrier_eV`. It must contain exactly one row: `pathway` set to `'D1'` and `barrier_eV` set to the barrier in electronvolts (eV).

## Assets
- The full paper (provided separately) describing the Zn₂(OH)VO₄ cathode and the DFT migration barrier calculations.
- Crystallographic information as indicated above.

## Workflow steps

### Step 1: Report the D1 barrier
- Role: **scored** (load-bearing)
- Action: Locate the migration barrier for pathway D1 in the paper. Create the CSV file `/app/outputs/step_01_barrier.csv` with exactly one row: `pathway = 'D1'`, `barrier_eV = <value from paper>`.
- Output file: `/app/outputs/step_01_barrier.csv`
- Format: csv
- Contract: CSV with columns: pathway (string), barrier_eV (float). Must contain one row for pathway 'D1' with the barrier.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_barrier.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_barrier.csv
- path: `/app/outputs/step_01_barrier.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Reported Zn²⁺ migration energy barrier for pathway D1.
- schema:
  - `type`: table
  - `required_columns`: `pathway`, `barrier_eV`
  - `columns`:
    - `pathway`: string
    - `barrier_eV`: float

Notes: The checker will compare the barrier_eV value for pathway D1 to the paper-reported value within a tolerance. This output is the only scored artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_barrier.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pathway",
          "barrier_eV"
        ],
        "columns": {
          "pathway": "string",
          "barrier_eV": "float"
        }
      },
      "description": "Reported Zn2+ migration energy barrier for pathway D1."
    }
  ],
  "notes": "The checker will compare the barrier_eV value for pathway D1 to the paper-reported value within a tolerance. This output is the only scored artifact."
}
```

## How you are scored
A hidden automated verifier will inspect your outputs. The primary scored artifact is `step_01_barrier.csv`. The verifier will read the `barrier_eV` value for pathway D1 and compare it to a hidden reference value derived from the original study. Your score will reflect the agreement between your reported barrier and this hidden reference; a correct reproduction will earn full credit, while a value substantially different from the reference will receive a lower score. The verifier may also check that the file exists, has correct format and columns, and contains exactly the required row. No other files are scored.