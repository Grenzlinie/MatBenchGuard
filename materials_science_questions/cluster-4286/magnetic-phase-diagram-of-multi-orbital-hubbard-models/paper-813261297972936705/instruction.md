# Phase Transition and Hysteresis Reduction in a Bosonic t-J Model via Double CP¹ Slave-Particle Monte Carlo

## Problem background
Hard-core bosons with two internal species appear in models of correlated systems and optical lattices. When strong on-site repulsion forbids double occupancy, the low-energy physics is described by a bosonic t‑J model, which couples hopping and spin‑exchange terms. Studying this model is challenging because the hard-core constraint must be enforced exactly at every site, and Monte Carlo simulations often encounter severe hysteresis near first‑order phase transitions. This task addresses the development of a slave‑particle representation that resolves the constraint and an improved Monte Carlo algorithm designed to reduce hysteresis, allowing precise determination of the location and nature of the phase transition.

## Approach
The hard-core boson operators are expressed as composites of two sets of CP¹ slave particles: a Schwinger boson (spinon) and a second CP¹ field (holon), forming a double CP¹ representation that automatically enforces the no‑double‑occupancy condition. The finite‑temperature partition function is cast as a path integral over the spinon, holon, and a U(1) gauge field on a three‑dimensional cubic lattice, giving an effective action with parameters c₁ (spin‑exchange strength), c₃ (hopping strength), and a chemical potential μc that controls the hole density. Monte Carlo simulations will be run sweeping c₁ across a range that contains a first‑order transition, using two update strategies: (a) standard Metropolis updates of the local densities and (b) an improved algorithm that proposes a symmetric density configuration, `ρ_new = (ρ₁+ρ₂) − ρ_old`, to jump between metastable states. For each algorithm and c₁ value the internal energy and average hole density are recorded. From these measurements the critical coupling is identified as the location of the sharpest feature in the energy data, and at selected c₁ values the magnetic order is diagnosed via the spin structure factor (staggered versus uniform).

## Reproduction target
- Implement the double CP¹ path integral for Model I of the bosonic t‑J model (the formulation that includes the hole‑projector factors) on a 3D cubic lattice of size L=12 with periodic boundary conditions, setting μc=16 and c₃=24.
- Sweep c₁ from 6.0 to 10.0 in steps of about 0.25. For each c₁ value, equilibrate and measure (i) the internal energy per site U and (ii) the average hole density ρ, using both standard Metropolis updates and the improved algorithm (density‑symmetry proposal). Write the full scan to a CSV file with columns c₁, U_metropolis, U_improved, rho_metropolis, rho_improved.
- From the improved‑algorithm data, locate the critical coupling c₁c where the energy or density changes most steeply, and record the range (e.g., the two c₁ values bracketing the midpoint of the jump).
- Run dedicated simulations at c₁ = 6.0 and c₁ = 10.0 (same lattice, μc, c₃). Compute the spin structure factor (or staggered magnetization) and, from its behaviour, classify the low‑c₁ phase as antiferromagnetic (AF) or ferromagnetic+superfluid (FM+SF), and similarly for the high‑c₁ phase. Package the phase labels and the critical c₁ range into a JSON object with keys low_c1_phase, high_c1_phase, and critical_c1_range (a list of two floats).

## Assets

- Python scientific stack

## Workflow steps

### Step 1: Monte Carlo scan over c1
- Role: scored (load-bearing)
- Action: Implement the double CP¹ slave-particle path integral for Model I of the bosonic t-J model (the double CP¹ path integral with hole-projector factors) on a 3D cubic lattice of size L=12 with periodic boundary conditions. Set mu_c=16, c3=24. For each c1 in a fine grid from 6.0 to 10.0 (step about 0.25), run Monte Carlo simulations using both standard Metropolis updates and the improved algorithm that symmetrically proposes density configurations. After equilibration, measure the internal energy per site U and the average hole density rho for each algorithm. Write the results to a CSV.
- Output file: `/app/outputs/step_01_scan_results.csv`
- Format: csv
- Contract: columns: c1 (float), U_metropolis (float), U_improved (float), rho_metropolis (float), rho_improved (float). One row per c1 value.
- Scoring: scored by hidden verifier

### Step 2: Phase identification and critical coupling
- Role: scored
- Action: Using the same simulation code, run additional simulations at c1=6.0 and c1=10.0 (with c3=24, mu_c=16, L=12). Compute the spin structure factor (or staggered magnetization) to determine whether the phase is antiferromagnetic (AF) or ferromagnetic + superfluid (FM+SF). Also, from the scan data in step_01, estimate the critical coupling c1c as the midpoint of the sharpest jump in U_improved vs c1. Package the phase labels and the critical c1 range into a JSON.
- Output file: `/app/outputs/step_02_phase_analysis.json`
- Format: json
- Contract: Keys: 'low_c1_phase' (string, e.g., 'AF'), 'high_c1_phase' (string, e.g., 'FM+SF'), 'critical_c1_range' (list of two floats, e.g., [8.25, 8.30]).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_scan_results.csv`
- `/app/outputs/step_02_phase_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_scan_results.csv
- path: `/app/outputs/step_01_scan_results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Energy and density scan data; the checker recomputes the derivative of U_improved to locate the first-order transition and compare to the paper-reported critical range.
- schema:
  - `type`: table
  - `required_columns`: `c1`, `U_metropolis`, `U_improved`, `rho_metropolis`, `rho_improved`
  - `units`: object

### step_02_phase_analysis.json
- path: `/app/outputs/step_02_phase_analysis.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Phase classification results and the estimated critical coupling range; the checker compares the phase labels and the range against the paper-reported gold values.
- schema:
  - `type`: object
  - `required`:
    - `low_c1_phase`: string
    - `high_c1_phase`: string
    - `critical_c1_range`: array of two floats

Notes: The checker performs T1 recompute on the CSV (derivative analysis) and T0 result-level comparison on the JSON.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_scan_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "c1",
          "U_metropolis",
          "U_improved",
          "rho_metropolis",
          "rho_improved"
        ],
        "units": {}
      },
      "description": "Energy and density scan data; the checker recomputes the derivative of U_improved to locate the first-order transition and compare to the paper-reported critical range."
    },
    {
      "file": "step_02_phase_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "low_c1_phase": "string",
          "high_c1_phase": "string",
          "critical_c1_range": "array of two floats"
        }
      },
      "description": "Phase classification results and the estimated critical coupling range; the checker compares the phase labels and the range against the paper-reported gold values."
    }
  ],
  "notes": "The checker performs T1 recompute on the CSV (derivative analysis) and T0 result-level comparison on the JSON."
}
```

## How you are scored
A hidden verifier independently scores each output artifact and combines them by weight into a final 0‑1 reward.
- **CSV scan (step_01_scan_results.csv)**: The verifier recomputes a numerical derivative of U_improved versus c₁ to locate the sharpest jump, then compares the resulting critical coupling range to the paper‑reported gold range (with a tolerance that accepts a correct re‑implementation despite statistical noise). It also checks that the improved algorithm reduces hysteresis compared to standard Metropolis. This is a recompute‑and‑compare step; simply reporting a plausible number is not sufficient—the raw scan data must support it.
- **Phase analysis JSON (step_02_phase_analysis.json)**: The verifier compares the reported phase labels and critical c₁ range to the hidden gold values, rewarding correct assignment and penalising misclassifications.
Your reward degrades as the computed critical range deviates from the true one or if a phase is misidentified, and is highest when the scan correctly reveals a sharp transition near the true coupling and both side phases are correctly labelled.
