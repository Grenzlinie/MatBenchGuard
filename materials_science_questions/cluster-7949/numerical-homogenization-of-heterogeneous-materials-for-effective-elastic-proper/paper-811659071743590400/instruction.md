# Three-Level Adaptive Finite Element Simulation for SENT Specimen Stress Intensity Factors

## Problem background
Predicting crack paths and the onset of unstable growth in brittle materials requires accurate computation of stress intensity factors (SIFs) and T‑stresses near the crack tip. Conventional finite element models become extremely expensive when they must simultaneously resolve the singular crack‑tip field and material heterogeneities such as voids or inclusions. This task focuses on a three‑level adaptive finite element scheme designed to balance accuracy and computational cost. The scheme’s performance was originally validated on a homogeneous single‑edge‑notched tension (SENT) specimen by comparing the computed mode I stress intensity factor and T‑stress against reference solutions, thereby demonstrating its ability to capture the crack‑tip field efficiently.

## Approach
The computational domain is divided into three non‑overlapping nested regions. Far from the crack a coarse mesh is used, where the overall homogenised elastic constants suffice. Closer to the crack tip, an intermediate mesh resolves geometrical features without yet capturing the singular field. A fine mesh is built immediately around the crack tip; its innermost elements are quarter‑point singular elements that reproduce the inverse square‑root stress singularity, surrounded by standard quadratic elements. Different mesh levels are connected seamlessly by variable‑node elements that allow an arbitrary number of nodes on each edge while preserving compatibility and linear or quadratic completeness. The stress intensity factor K_I and the T‑stress are extracted from the finite element solution by evaluating a domain form of the two‑state conservation integral (interaction integral) over a path that excludes any inhomogeneities. For this validation task, only the homogeneous case is required: a rectangular SENT specimen of width w and height 2h (h/w = 1) with an edge crack of length a is loaded by uniform uniaxial tension σ on the top and bottom faces. The analysis is repeated for six crack‑length ratios a/w = 0.2, 0.3, 0.4, 0.5, 0.6, 0.7 under plane‑strain conditions.

## Reproduction target
Implement a two‑dimensional plane‑strain finite element code that constructs the three‑level adaptive mesh for the SENT geometry, applies the uniform tension loading, and for each of the six crack‑length ratios performs a static linear elastic analysis. From the computed displacement and stress fields, use the two‑state conservation integral to obtain the mode I stress intensity factor K_I and the T‑stress. Normalise the results as K_I/(σ√(πa)) and T√(πa)/K_I. Write the six resulting rows to `/app/outputs/sent_results.csv` with the columns `a_over_w`, `K_I_norm`, `T_norm`. The submitted values should be in agreement with established reference data (the exact tolerances are not disclosed).

## Assets

- Variable-node finite element formulation (Lim et al. 2007), Int. J. Numer. Methods Eng. 72:835-857: 10.1002/nme.1919
- Two-state conservation integral method for stress intensity factors and T-stress (Im & Kim 2000; Jeon & Im 2001): 10.1016/S0022-5096(99)00003-0
- Quarter-point singular element technique (Barsoum 1974, Int. J. Numer. Methods Eng. 10:25-37): 10.1002/nme.1620100103

## Workflow steps

### Step 1: Run three-level finite element simulation for SENT specimen
- Role: process
- Action: Implement a plane-strain finite element solver. For each crack length ratio a/w = 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, construct the three-level adaptive mesh for the SENT geometry: coarse mesh of reasonable density, intermediate region within radius R from crack tip (each coarse element subdivided into 80x80 quadrilateral elements), fine region with circumferential refinement until θe<22.5°, innermost ring of quarter-point singular elements, quadratic rings, and outer ring of linear–quadratic transition elements. Apply uniform uniaxial tension boundary conditions (h/w=1) and perform static linear elastic analysis. Store the resulting displacement and stress fields.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute and output normalized K_I and T-stress
- Role: scored (load-bearing)
- Action: For each a/w, apply the two-state conservation integral (domain form) on the finite element solution to extract mode I stress intensity factor K_I and T-stress. Normalize K_I as K_I/(σ√(πa)) and T-stress as T√(πa)/K_I. Write the results to /app/outputs/sent_results.csv with columns a_over_w, K_I_norm, T_norm (one row per a/w).
- Output file: `/app/outputs/sent_results.csv`
- Format: csv
- Contract: CSV file with header: a_over_w, K_I_norm, T_norm. Six rows for a/w = 0.2, 0.3, 0.4, 0.5, 0.6, 0.7.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sent_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sent_results.csv
- path: `/app/outputs/sent_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized mode I stress intensity factor and T-stress for SENT specimen at six crack length ratios.
- schema:
  - `columns`: `a_over_w`, `K_I_norm`, `T_norm`

Notes: Verifier compares the computed values against reference tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/sent_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "columns": [
          "a_over_w",
          "K_I_norm",
          "T_norm"
        ]
      },
      "description": "Normalized mode I stress intensity factor and T-stress for SENT specimen at six crack length ratios."
    }
  ],
  "notes": "Verifier compares the computed values against reference tolerances."
}
```

## How you are scored
A hidden automated verifier reads your `/app/outputs/sent_results.csv` and compares each `K_I_norm` and `T_norm` value against a set of hidden gold reference values. Scoring uses a threshold‑or‑better rule: if your relative error is within the allowed tolerance you earn full credit for that entry; if the error exceeds the tolerance the credit decreases linearly to zero. A result that is better (smaller error) than the reference does not reduce your score. The overall reward is the average of the scores over all six crack‑length ratios. Simply reporting numbers that match the paper’s tables without actually running the finite‑element simulation will not satisfy the scoring process.
