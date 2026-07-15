# Validation of DFT Convex-Hull Stability Metric for Li2MO3 Compounds

## Problem background
Lithium-rich layered oxide cathode materials of the form Li₂MO₃ (M = transition or post‑transition metal) are promising for high‑energy Li‑ion batteries. Thermodynamic stability is a prerequisite for synthesizability, and a widely used metric is the convex‑hull distance ΔHₛ: the energy difference between the compound's formation energy and the energy of the competing ground‑state phase mixture at the same composition. The paper validated whether the DFT‑based convex‑hull stability metric computed from the Open Quantum Materials Database (OQMD) correctly classifies a set of fifteen experimentally observed Li₂MO₃ compounds (C2/m layered structure). The task is to independently compute the convex‑hull distance for each of these fifteen compounds using the current OQMD and determine whether they fall within the stability envelope.

## Approach
The convex‑hull stability is assessed by constructing the Li–M–O phase diagram for each metal M from the formation energies of all known competing phases in the OQMD, then computing the hull energy at the Li₂MO₃ composition. The method involves two stages:
- Retrieve the list of compounds, compositions, and formation energies for each Li–M–O chemical system from the OQMD (the database may be queried via its REST API or by downloading bulk data).
- For each M, build the convex hull from the retrieved energies, locate the Li₂MO₃ phase (C2/m layered structure), calculate its distance to the hull, and convert the result to meV/atom.
The final artifact is a CSV table reporting the hull distance for each of the fifteen metals. This procedure tests the robustness of the stability metric against the current version of the OQMD and against an independent implementation of the convex‑hull algorithm.

## Reproduction target
Compute the convex‑hull distance (ΔHₛ) for each of the fifteen Li₂MO₃ compounds with M = Ti, V, Mn, Fe, Ni, Ge, Zr, Mo, Ru, Rh, Pd, Sn, Ir, Pt, Pb, using the C2/m layered structure and the OQMD database. Output a CSV file with two columns: 'M' and 'hull_distance_meV_per_atom'. Exactly fifteen rows are expected, one per metal. The result will be checked by a hidden verifier that confirms whether each compound lies within a predefined stability threshold, as claimed in the original work.

## Assets

- Open Quantum Materials Database (OQMD): https://oqmd.org

## Workflow steps

### Step 1: Retrieve OQMD phase data for Li–M–O systems
- Role: process
- Action: Fetch the formation energies (ΔH_f) and compositions of all stable and nearly‑stable compounds in the Li–M–O phase space for each of the 15 metals M (Ti, V, Mn, Fe, Ni, Ge, Zr, Mo, Ru, Rh, Pd, Sn, Ir, Pt, Pb) from the OQMD (API or bulk download). Save the retrieved data as a local file to be used in the next step.
- Evidence: `/app/outputs/oqmd_data.json`

### Step 2: Compute convex‑hull distances and write CSV
- Role: scored (load-bearing)
- Action: For each of the 15 M, construct the convex hull from the retrieved Li–M–O phase data, determine the hull energy at the Li₂MO₃ composition (using the formation energy of the C2/m Li₂MO₃ phase), compute the hull distance ΔH_s = ΔH_f(Li₂MO₃) – E_hull, and convert to meV/atom. Output a CSV with two columns: M (element symbol) and hull_distance_meV_per_atom (float).
- Output file: `/app/outputs/step_01_hull_distances.csv`
- Format: csv
- Contract: Header: M, hull_distance_meV_per_atom. M is the element symbol (string); hull_distance_meV_per_atom is a floating‑point number (positive for above‑hull, zero or negative for on‑hull). Exactly 15 rows, one for each of Ti, V, Mn, Fe, Ni, Ge, Zr, Mo, Ru, Rh, Pd, Sn, Ir, Pt, Pb.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_hull_distances.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_hull_distances.csv
- path: `/app/outputs/step_01_hull_distances.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Convex‑hull distance (ΔH_s) for each of the 15 experimentally known Li₂MO₃ compounds. The hidden checker verifies that every row has hull_distance_meV_per_atom ≤ 25 meV/atom and scores the fraction of rows satisfying this condition.
- schema:
  - `type`: table
  - `required_columns`: `M`, `hull_distance_meV_per_atom`
  - `units`:
    - `hull_distance_meV_per_atom`: meV/atom

Notes: The task reproduces the paper's validation claim that all 15 Li₂MO₃ compounds are stable or nearly‑stable (≤25 meV/atom) using the OQMD. The current OQMD version may differ slightly from the paper's 2017 snapshot, but the threshold‑based scoring is robust to that evolution; the conclusion that all 15 compounds satisfy the ≤25 meV/atom criterion is expected to hold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_hull_distances.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "M",
          "hull_distance_meV_per_atom"
        ],
        "units": {
          "hull_distance_meV_per_atom": "meV/atom"
        }
      },
      "description": "Convex‑hull distance (ΔH_s) for each of the 15 experimentally known Li₂MO₃ compounds. The hidden checker verifies that every row has hull_distance_meV_per_atom ≤ 25 meV/atom and scores the fraction of rows satisfying this condition."
    }
  ],
  "notes": "The task reproduces the paper's validation claim that all 15 Li₂MO₃ compounds are stable or nearly‑stable (≤25 meV/atom) using the OQMD. The current OQMD version may differ slightly from the paper's 2017 snapshot, but the threshold‑based scoring is robust to that evolution; the conclusion that all 15 compounds satisfy the ≤25 meV/atom criterion is expected to hold."
}
```

## How you are scored
A hidden verifier reads your submitted step_01_hull_distances.csv. It checks that the file contains the required fifteen rows and that each row's hull_distance_meV_per_atom is a valid finite number. The verifier then compares each computed hull distance against a pre‑determined stability criterion. The final reward is the fraction of compounds that satisfy the criterion (i.e., full credit if all fifteen pass, partial credit if only a subset pass). The criterion itself is not disclosed here, so you must genuinely perform the convex‑hull analysis to obtain a correct result.
