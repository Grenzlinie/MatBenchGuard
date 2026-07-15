# Extracting topological invariants from boundary charges in Chern insulators

## Problem background
Crystalline Chern insulators can host fractional boundary and corner charge responses governed by many-body topological invariants: the discrete shift \(\delta_o\) and electric polarization \(\vec{\mathcal{P}}_o\). These invariants are defined even in the presence of gapless edge states and non-zero Chern number. This task aims to extract \(\delta_o\) and \(\vec{\mathcal{P}}_o\) from numerical tight-binding simulations of two model systems: the square-lattice Hofstadter model (C = −2) and the quadrupole insulator model (C = 0).

## Approach
We implement tight-binding Hamiltonians for the Hofstadter model (flux \(\phi = \pi\) per plaquette, staggered potential to open a gap) and the quadrupole insulator model (\(t_1/t_2 = 0.5\)) on cylinder and ribbon geometries. Using exact diagonalization, we obtain ground-state charge distributions and compute the weighted total charge \(Q_W\) inside a chosen subregion \(W\) that encloses one boundary (cylinder) or a corner (ribbon). By regularizing \(Q_W\) with filling \(\nu\) and excess flux contributions, we isolate the pure polarization and discrete shift contributions. For cylinder geometries, the regularized charge versus system length \(L_y\) yields the polarization \(\vec{\mathcal{P}}_o\); for ribbon geometries with a single corner of angle \(-\pi/2\), the regularized charge directly gives the discrete shift \(\delta_o\).

## Reproduction target
Produce a CSV of regularized charges and geometric measures for multiple cylinder sizes and ribbon configurations. Extract the electric polarization \(\vec{\mathcal{P}}_o\) and discrete shift \(\delta_o\) for both the Hofstadter and quadrupole insulator models at the two maximal Wyckoff positions \(\alpha\) and \(\beta\). Confirm that the discrete shift \(\delta_o\) and Chern number \(C\) obey the predicted modular relation, and that the regularized ribbon charge is consistent with \(\delta_o\) via the corner angle contribution.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Model Simulation and Charge Computation
- Role: process
- Action: Construct tight‑binding Hamiltonians for the square‑lattice Hofstadter model (C=−2, flux φ=π per plaquette, staggered potential to open a gap) and the quadrupole insulator model (C=0, t1/t2=0.5) on cylinder and ribbon geometries. Perform exact diagonalization to obtain ground states. Compute site‑resolved charge expectation values and evaluate the weighted total charge Q_W for regions following the angle‑subtended weighting rule. Compute the geometric measures (Γ, L_o, n_W,o, excess flux δΦ_W,o) for each configuration as defined in the paper.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Write Charge Data
- Role: scored
- Action: Compile the computed total charges and geometric measures for multiple system sizes (L_y values) and geometries (cylinder, ribbon) into a CSV file.
- Output file: `/app/outputs/charge_data.csv`
- Format: csv
- Contract: Columns: model (string: 'hofstadter' or 'quadrupole'), geometry (string: 'cylinder' or 'ribbon'), origin (string: 'alpha' or 'beta'), L_y (integer, present only for cylinder), Q_W (float), n_W (float), delta_Phi_W (float), regularized_Q (float).
- Scoring: scored by hidden verifier

### Step 3: Extract Invariants
- Role: scored (load-bearing)
- Action: From charge_data.csv, compute regularized charge Q_mod = Q_W − ν·n_W − C·δΦ_W/(2π) mod 1. For cylinder entries, fit Q_mod vs L_y to extract polarization P_o (slope). For ribbon entries with corner angle Ω_cor = −π/2, extract discrete shift δ_o using Q_mod = δ_o · Ω_cor/(2π) mod 1. Output the extracted invariants.
- Output file: `/app/outputs/extracted_invariants.json`
- Format: json
- Contract: JSON object with top‑level keys 'hofstadter' and 'quadrupole', each containing: P_o_alpha (float), P_o_beta (float), delta_o_alpha (float), delta_o_beta (float), C (int), nu (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/charge_data.csv`
- `/app/outputs/extracted_invariants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### charge_data.csv
- path: `/app/outputs/charge_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw charge and geometric data; the checker recomputes the invariants from this file and compares the derived values to hidden gold.
- schema:
  - `type`: table
  - `required_columns`: `model`, `geometry`, `origin`, `L_y`, `Q_W`, `n_W`, `delta_Phi_W`, `regularized_Q`
  - `items`: object

### extracted_invariants.json
- path: `/app/outputs/extracted_invariants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Headline invariants; the checker compares the extracted values to paper‑reported gold with a tolerance, and also checks consistency against a recomputation from charge_data.csv.
- schema:
  - `type`: object
  - `required`:
    - `hofstadter`: object
    - `quadrupole`: object
  - `items`:
    - `P_o_alpha`: float
    - `P_o_beta`: float
    - `delta_o_alpha`: float
    - `delta_o_beta`: float
    - `C`: int
    - `nu`: float

Notes: The checker will recompute P_o and δ_o from charge_data.csv and compare the obtained values to hidden paper‑reported references. The extracted_invariants.json must match the recomputed values within a tolerance. This verifies that the simulation and invariant extraction were done correctly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "charge_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "geometry",
          "origin",
          "L_y",
          "Q_W",
          "n_W",
          "delta_Phi_W",
          "regularized_Q"
        ],
        "items": {}
      },
      "description": "Raw charge and geometric data; the checker recomputes the invariants from this file and compares the derived values to hidden gold."
    },
    {
      "file": "extracted_invariants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "hofstadter": "object",
          "quadrupole": "object"
        },
        "items": {
          "P_o_alpha": "float",
          "P_o_beta": "float",
          "delta_o_alpha": "float",
          "delta_o_beta": "float",
          "C": "int",
          "nu": "float"
        }
      },
      "description": "Headline invariants; the checker compares the extracted values to paper‑reported gold with a tolerance, and also checks consistency against a recomputation from charge_data.csv."
    }
  ],
  "notes": "The checker will recompute P_o and δ_o from charge_data.csv and compare the obtained values to hidden paper‑reported references. The extracted_invariants.json must match the recomputed values within a tolerance. This verifies that the simulation and invariant extraction were done correctly."
}
```

## How you are scored
A hidden verifier independently reads your `charge_data.csv` and `extracted_invariants.json`. It recomputes the regularized charges and invariant extraction, then compares the obtained \(\vec{\mathcal{P}}_o\) and \(\delta_o\) to reference values derived from the paper. It also checks that the self-consistency relations (e.g., \(\delta_o \bmod 1 = C/2 \bmod 1\)) hold within a small tolerance. The final reward is a weighted combination of scores from both artifacts.
