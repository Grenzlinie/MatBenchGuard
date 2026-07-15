# Zn²⁺ Migration Energy Barrier Calculation in Layered Zinc Orthovanadate

## Problem background
Rechargeable zinc-ion batteries are attractive for low-cost, safe energy storage, but their rate capability is often limited by slow Zn²⁺ ion transport in the cathode. A layered zinc orthovanadate (Zn₂(OH)VO₄) cathode has demonstrated exceptional high-rate cycling in a quasi-solid-state configuration. The fast kinetics have been attributed to low in-plane Zn²⁺ migration barriers within the material's two-dimensional layered structure. Independently verifying these computed barriers is essential to establishing the mechanistic foundation for the cathode's performance. This task reproduces the first-principles calculation of the lowest Zn²⁺ migration energy barrier along a specific pathway in the Zn₂(OH)VO₄ lattice.

## Approach
The approach employs density functional theory (DFT) with the GGA-PBE exchange-correlation functional and the climbing-image nudged elastic band (CI-NEB) method. The system is the layered Zn₂(OH)VO₄ cathode material. The migration pathway of interest, labelled D1, connects the Zn0 site to a neighbouring Zn1 site within the b–c plane. The end-point structures for the NEB calculation are the fully relaxed Zn₂(OH)VO₄ unit cell and the Zn₃(OH)VO₄ cell with an inserted Zn ion. The energy barrier is taken as the energy difference between the highest-energy image along the converged NEB path and the initial state. The calculations can be carried out with any open-source DFT code that supports CI-NEB, such as Quantum ESPRESSO, using standard GGA-PBE pseudopotentials for Zn, O, V, and H.

## Reproduction target
Compute the minimum Zn²⁺ migration energy barrier along pathway D1 in Zn₂(OH)VO₄ using DFT+NEB and write the result to the file `step_01_barrier.csv`. The file must be a CSV with columns `pathway` and `barrier_eV`. It must contain exactly one row: `pathway` set to `'D1'` and `barrier_eV` set to the computed barrier in electronvolts (eV).

## Assets

- ZOV crystal structure (Zn2(OH)VO4)
- DFT software with NEB capability: https://www.quantum-espresso.org/
- GGA-PBE pseudopotentials (Zn, O, V, H)

## Workflow steps

### Step 1: Geometry Optimization of ZOV Structures
- Role: process
- Action: Perform DFT geometry optimization of the Zn2(OH)VO4 and Zn3(OH)VO4 unit cells using GGA-PBE to obtain relaxed atomic positions for the subsequent CI-NEB calculation.
- Evidence: `/app/outputs/geo_opt.log`

### Step 2: NEB Barrier Calculation for D1 Pathway
- Role: scored (load-bearing)
- Action: Using the optimized structures, run a climbing-image nudged elastic band (CI-NEB) calculation for Zn2+ migration between Zn0 and Zn1 sites along pathway D1. Extract the minimum energy barrier in eV and write the result to step_01_barrier.csv.
- Output file: `/app/outputs/step_01_barrier.csv`
- Format: csv
- Contract: CSV with columns: pathway (string), barrier_eV (float). Must contain one row for pathway 'D1' with the computed barrier.
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
- description: Computed Zn2+ migration energy barrier for pathway D1.
- schema:
  - `type`: table
  - `required_columns`: `pathway`, `barrier_eV`
  - `columns`:
    - `pathway`: string
    - `barrier_eV`: float

Notes: The checker will compare the barrier_eV value for pathway D1 to the paper-reported value within a tolerance. This output is the only scored artifact; the geometry optimization log is a supporting process artifact.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

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
      "description": "Computed Zn2+ migration energy barrier for pathway D1."
    }
  ],
  "notes": "The checker will compare the barrier_eV value for pathway D1 to the paper-reported value within a tolerance. This output is the only scored artifact; the geometry optimization log is a supporting process artifact."
}
```

## How you are scored
A hidden automated verifier will inspect your outputs. The primary scored artifact is `step_01_barrier.csv`. The verifier will read the `barrier_eV` value for pathway D1 and compare it to a hidden reference value derived from the original study. Your score will reflect the agreement between your computed barrier and this hidden reference; a correct reproduction will earn full credit, while a value substantially different from the reference will receive a lower score. The verifier may also check that the file exists, has correct format and columns, and contains exactly the required row. No other files are scored.
