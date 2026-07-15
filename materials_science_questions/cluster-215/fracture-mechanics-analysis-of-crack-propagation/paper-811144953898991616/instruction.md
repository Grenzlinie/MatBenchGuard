# Analytical Mixed-Mode Crack Propagation Simulation

## Problem background
Predicting the three-dimensional propagation path of an internally pressurized circular crack under remote compressive stresses is important for hydraulic fracturing design. The crack, embedded in an infinite brittle rock, may kink and reorient as it grows due to mixed-mode loading. This task models the stepwise evolution of such a crack using linear elastic fracture mechanics: you will compute the stress intensity factors along the initial crack front and then simulate the crack front propagation over multiple steps, producing the final crack surface.

## Approach
The method uses the maximum tangential stress (MTS) criterion and a fictitious planar elliptical crack approximation to make the problem analytic. Given the crack orientation (dip direction and dip angle), the far-field principal stresses, and the internal pressure, the effective normal and shear stresses on the crack plane are computed. For the initial circular crack the stress intensity factors KI, KII, KIII come from closed‑form circular‑crack expressions; after the first propagation step the front is approximated by an ellipse, and the stress intensity factors are evaluated from standard elliptical‑crack formulas. At each propagation step the MTS criterion determines the critical kink angle at every point around the front. A constant increment is applied at the two points where |KII| is maximum, and the resulting front is fitted to a new planar ellipse whose orientation is updated. The process repeats for the specified number of steps, treating the crack as a fictitious planar crack at each iteration.

## Reproduction target
Work with the following set of parameters: dip angle = 45°, dip direction = 0°, initial circular crack radius a = 0.1 m, effective principal stresses σ'_x = σ'_y = 92 MPa, σ'_z = 63 MPa, internal fluid pressure P = 80 MPa, Poisson's ratio ν = 0.25.

(1) Compute the stress intensity factors KI, KII, KIII for the initial circular crack at 36 equally spaced apparent angles φ from 0° to 350° in 10° increments using the analytical circular‑crack expressions. Write the results to `/app/outputs/sifs_initial_crack.csv`.

(2) Run 20 propagation steps with a constant increment inc = 0.01 m. At each step: compute effective stresses on the current crack plane; obtain SIFs using circular formulas (first step) or elliptical formulas (subsequent steps); determine critical kink angles via the MTS criterion; update the crack front geometry by fitting a planar ellipse and re‑computing the crack plane orientation. After 20 steps, output the global (x, y, z) coordinates of the final fitted elliptical crack front at the same 36 φ angles to `/app/outputs/final_crack_front.csv`.

The two CSV files will be independently verified against a reference implementation of the same algorithm.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute initial circular-crack SIFs
- Role: scored
- Action: Using the parameters of Case 3 (dip angle 45°, dip direction 0°, radius a=0.1 m, σ'_x=σ'_y=92 MPa, σ'_z=63 MPa, internal pressure P=80 MPa, Poisson's ratio ν=0.25), compute the effective normal stress σ_n(eff), effective shear stress τ_eff, and shear angle ω on the initial crack plane. Evaluate the stress intensity factors K_I, K_II, K_III from the analytical expressions for a circular crack at 36 equally spaced apparent angles φ from 0° to 350° in 10° increments. Write the results to sifs_initial_crack.csv.
- Output file: `/app/outputs/sifs_initial_crack.csv`
- Format: csv
- Contract: CSV with header: phi_deg, KI, KII, KIII. phi_deg from 0 to 350 in 10 deg increments. KI, KII, KIII in Pa√m.
- Scoring: scored by hidden verifier

### Step 2: Run 20‑step propagation and output final crack front
- Role: scored (load-bearing)
- Action: Implement the full stepwise propagation algorithm from the initial circular crack for Case 3. For 20 propagation steps: (a) compute effective normal and shear stresses on the current fictitious crack plane; (b) compute SIFs using the circular crack formulas (first step) or elliptical crack formulas (subsequent steps); (c) determine critical propagation angles θ_c(φ) via the maximum tangential stress criterion; (d) update the crack front geometry using a fictitious planar elliptical crack approximation (compute radial lengths, fit an ellipse, update the crack plane orientation). Use a constant increment inc=0.01 m applied at the two reference points where |K_II| is maximum. After 20 steps, write the global (x,y,z) coordinates of the final fitted elliptical crack front at 36 apparent angles φ from 0° to 350° in 10° increments to final_crack_front.csv.
- Output file: `/app/outputs/final_crack_front.csv`
- Format: csv
- Contract: CSV with header: phi_deg, x, y, z. phi_deg from 0 to 350 in 10 deg increments (apparent angle). Coordinates in meters in the global coordinate system.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sifs_initial_crack.csv`
- `/app/outputs/final_crack_front.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sifs_initial_crack.csv
- path: `/app/outputs/sifs_initial_crack.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Stress intensity factors for the initial pressurized circular crack (Case 3) at 36 angles.
- schema:
  - `type`: table
  - `required_columns`: `phi_deg`, `KI`, `KII`, `KIII`
  - `units`:
    - `phi_deg`: degree
    - `KI`: Pa*sqrt(m)
    - `KII`: Pa*sqrt(m)
    - `KIII`: Pa*sqrt(m)

### final_crack_front.csv
- path: `/app/outputs/final_crack_front.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Global coordinates of the final fitted elliptical crack front after 20 propagation steps for Case 3.
- schema:
  - `type`: table
  - `required_columns`: `phi_deg`, `x`, `y`, `z`
  - `units`:
    - `phi_deg`: degree
    - `x`: m
    - `y`: m
    - `z`: m

Notes: The initial SIFs are computed from the closed-form expressions for a circular crack; the final front is obtained by iterating the fictitious planar elliptical crack propagation method. The checker will recompute the same quantities independently from the same parameters and formulas, comparing element-wise absolute differences (for SIFs) and RMSE (for the crack front) against fixed tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sifs_initial_crack.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_deg",
          "KI",
          "KII",
          "KIII"
        ],
        "units": {
          "phi_deg": "degree",
          "KI": "Pa*sqrt(m)",
          "KII": "Pa*sqrt(m)",
          "KIII": "Pa*sqrt(m)"
        }
      },
      "description": "Stress intensity factors for the initial pressurized circular crack (Case 3) at 36 angles."
    },
    {
      "file": "final_crack_front.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "phi_deg",
          "x",
          "y",
          "z"
        ],
        "units": {
          "phi_deg": "degree",
          "x": "m",
          "y": "m",
          "z": "m"
        }
      },
      "description": "Global coordinates of the final fitted elliptical crack front after 20 propagation steps for Case 3."
    }
  ],
  "notes": "The initial SIFs are computed from the closed-form expressions for a circular crack; the final front is obtained by iterating the fictitious planar elliptical crack propagation method. The checker will recompute the same quantities independently from the same parameters and formulas, comparing element-wise absolute differences (for SIFs) and RMSE (for the crack front) against fixed tolerances."
}
```

## How you are scored
Each scored artifact is verified independently by the hidden checker. For the initial SIFs, the checker recomputes the exact SIFs from the same parameters and formulas, then compares your submitted values element‑wise via absolute difference; all differences must be within a fixed tolerance. For the final crack front, the checker runs its own reference implementation of the 20‑step propagation and computes the root‑mean‑square error (RMSE) between your submitted coordinates and the reference; the RMSE must be below a predetermined threshold. Each stage carries a weight, and the final reward is the weighted sum of the stage scores. Success requires that both outputs meet their respective tolerances.
