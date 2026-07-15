# DFT band gap narrowing in layered oxide semiconductors upon nitrogen doping

## Problem background
Layered oxide semiconductors such as CsTaWO6, CsCa2Ta3O10, and Ba4Ta4O15 are candidate photocatalysts for solar water splitting, but their wide band gaps limit absorption to the ultraviolet region. Nitrogen doping is a strategy to modify the electronic structure and potentially enhance visible-light absorption. Density functional theory (DFT) calculations can assess how nitrogen incorporation affects the valence band edge and the fundamental band gap. The goal is to compute the electronic band gaps for these three parent oxides and their nitrogen-doped analogs from first principles.

## Approach
The computational approach employs spin-polarized density functional theory with the Perdew-Burke-Ernzerhof (PBE) generalized gradient approximation, as implemented in Quantum ESPRESSO. Starting from the published crystal structures, supercell models are constructed for each undoped material. A nitrogen-doped variant is built by substituting one oxygen atom with nitrogen. Geometry optimization is performed, followed by a self-consistent field (SCF) calculation, and a final calculation to obtain the total density of states (DOS). The fundamental band gap is extracted from the DOS as the energy separation between the valence band maximum and the conduction band minimum. This procedure is carried out for all six systems.

## Reproduction target
Compute the band gaps for undoped and nitrogen-doped CsTaWO6, CsCa2Ta3O10, and Ba4Ta4O15 from the DFT total DOS, and write the six values to the file /app/outputs/band_gaps.json. The JSON object must contain the keys CsTaWO6_undoped, CsTaWO6_doped, CsCa2Ta3O10_undoped, CsCa2Ta3O10_doped, Ba4Ta4O15_undoped, Ba4Ta4O15_doped, each with a numerical value in eV.

## Assets

- Crystal structures of CsTaWO6, CsCa2Ta3O10, Ba4Ta4O15
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials (SSSP efficiency set): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Prepare structures
- Role: process
- Action: Obtain the crystal structures of CsTaWO6, CsCa2Ta3O10, and Ba4Ta4O15 from public crystallographic databases. Build supercell models to avoid spurious periodic image interactions. For each parent oxide, create a nitrogen-doped model by substituting one oxygen atom with nitrogen in a representative site. Generate Quantum ESPRESSO input files for geometry optimization and self-consistent field (SCF) calculations for all six systems.
- Evidence: `/app/outputs/structures_used.txt`

### Step 2: Run DFT calculations
- Role: process
- Action: For each of the six systems, perform spin-polarized DFT calculations using Quantum ESPRESSO with the GGA-PBE functional. Run geometry optimization (relax atomic positions and cell parameters if needed) to convergence. Then run a self-consistent field (SCF) calculation on the relaxed structure. Finally, compute the total density of states (DOS) on a fine k‑point mesh. Extract the fundamental band gap from the DOS as the energy difference between the valence band maximum and conduction band minimum.
- Evidence: `/app/outputs/dft_runs_summary.txt`

### Step 3: Compile band gaps
- Role: scored (load-bearing)
- Action: Collect the computed band gaps for all six materials and write them to a JSON file.
- Output file: `/app/outputs/band_gaps.json`
- Format: json
- Contract: {"CsTaWO6_undoped": "number (eV)", "CsTaWO6_doped": "number (eV)", "CsCa2Ta3O10_undoped": "number (eV)", "CsCa2Ta3O10_doped": "number (eV)", "Ba4Ta4O15_undoped": "number (eV)", "Ba4Ta4O15_doped": "number (eV)"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gaps.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gaps.json
- path: `/app/outputs/band_gaps.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Band gaps computed from DFT total DOS for undoped and nitrogen-doped CsTaWO6, CsCa2Ta3O10, and Ba4Ta4O15. The checker compares four of the gaps against paper-reported DFT values with an absolute tolerance, and verifies that the doped Ba4Ta4O15 gap is strictly smaller than its undoped counterpart.
- schema:
  - `type`: object
  - `properties`:
    - `CsTaWO6_undoped`:
      - `type`: number
      - `unit`: eV
    - `CsTaWO6_doped`:
      - `type`: number
      - `unit`: eV
    - `CsCa2Ta3O10_undoped`:
      - `type`: number
      - `unit`: eV
    - `CsCa2Ta3O10_doped`:
      - `type`: number
      - `unit`: eV
    - `Ba4Ta4O15_undoped`:
      - `type`: number
      - `unit`: eV
    - `Ba4Ta4O15_doped`:
      - `type`: number
      - `unit`: eV
  - `required`: `CsTaWO6_undoped`, `CsTaWO6_doped`, `CsCa2Ta3O10_undoped`, `CsCa2Ta3O10_doped`, `Ba4Ta4O15_undoped`, `Ba4Ta4O15_doped`

Notes: The hidden checker uses paper-reported DFT band gaps for CsTaWO6 and CsCa2Ta3O10 (undoped and doped) as reference, applying a tolerance to allow for basis-set and pseudopotential differences. For Ba4Ta4O15, where the paper did not report explicit DFT values, the checker enforces the qualitative trend that doping reduces the band gap.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gaps.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "CsTaWO6_undoped": {
            "type": "number",
            "unit": "eV"
          },
          "CsTaWO6_doped": {
            "type": "number",
            "unit": "eV"
          },
          "CsCa2Ta3O10_undoped": {
            "type": "number",
            "unit": "eV"
          },
          "CsCa2Ta3O10_doped": {
            "type": "number",
            "unit": "eV"
          },
          "Ba4Ta4O15_undoped": {
            "type": "number",
            "unit": "eV"
          },
          "Ba4Ta4O15_doped": {
            "type": "number",
            "unit": "eV"
          }
        },
        "required": [
          "CsTaWO6_undoped",
          "CsTaWO6_doped",
          "CsCa2Ta3O10_undoped",
          "CsCa2Ta3O10_doped",
          "Ba4Ta4O15_undoped",
          "Ba4Ta4O15_doped"
        ]
      },
      "description": "Band gaps computed from DFT total DOS for undoped and nitrogen-doped CsTaWO6, CsCa2Ta3O10, and Ba4Ta4O15. The checker compares four of the gaps against paper-reported DFT values with an absolute tolerance, and verifies that the doped Ba4Ta4O15 gap is strictly smaller than its undoped counterpart."
    }
  ],
  "notes": "The hidden checker uses paper-reported DFT band gaps for CsTaWO6 and CsCa2Ta3O10 (undoped and doped) as reference, applying a tolerance to allow for basis-set and pseudopotential differences. For Ba4Ta4O15, where the paper did not report explicit DFT values, the checker enforces the qualitative trend that doping reduces the band gap."
}
```

## How you are scored
A hidden verifier will read your band_gaps.json. For CsTaWO6 and CsCa2Ta3O10, it will compare your computed undoped and doped band gaps to reference values within a predefined tolerance. For Ba4Ta4O15, it will verify that the doped band gap is strictly smaller than the undoped band gap. Your final score is a weighted combination of these comparisons. Only the contents of band_gaps.json are scored; the other evidence files are for documentation only and do not contribute to the score.
