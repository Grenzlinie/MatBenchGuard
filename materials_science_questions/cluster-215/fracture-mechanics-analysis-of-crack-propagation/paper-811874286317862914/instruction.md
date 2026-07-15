# Prediction of Crack Front Twisting in Three-Point Bending Using Linear Elastic Fracture Mechanics

## Problem background
In brittle fracture, a crack front under mixed-mode loading tends to twist and kink to reach a pure mode I condition. When both in‑plane shear (mode II) and out‑of‑plane shear (mode III) are present, the front may gradually rotate around the propagation direction. This task addresses the prediction of crack front twisting in three‑point bending (3PB) specimens containing an initially inclined notch. Two competing types of criteria have been proposed: a local criterion that predicts the kink angle at each point of the front from the local stress intensity factors, and a global criterion that accounts for the collective twisting of the entire front. The goal is to compute the front‑wise kink angle distributions and the macroscopic rotation rate for several notch inclinations, and to compare the predictions of the two criteria — a quantitative comparison whose outcome determines which physical mechanism (mode II vs. mode III) dominates the observed twisting.

## Approach
The analysis proceeds in two stages. First, a three‑dimensional linear elastic finite element model of the 3PB specimen is built for the three notch inclination angles γ = 45°, 60° and 75°. The specimen geometry and material parameters (specimen length L = 260 mm, span 2Lₑ = 240 mm, thickness t = 10 mm, width W = 60 mm, crack length a = W/3; Young’s modulus E = 2 800 N/mm², Poisson’s ratio ν = 0.38) are taken from the experimental setup. A cyclic lateral force of 2.4 kN is applied. The stress intensity factors KI, KII, KIII are computed along the initial crack front using the modified virtual crack closure integral (MVCCI) method. Second, from these SIF distributions two fracture criteria are applied:

- **MTS criterion (local):** The crack is assumed to kink locally in the direction that maximises the circumferential tensile stress. This yields an implicit equation for the kink angle φ at each front point: K_I sin φ + K_II (3 cos φ − 1) = 0, which is solved for φ_MTS.

- **MVK criterion (global):** The criterion that the mean value of the mode‑I SIF after a short crack extension is maximised. It predicts a global maximum kink angle φ_m at the specimen surface. The required propagation distance (facet length) δ_c is linked to φ_m through an empirical estimate of the local facet twist angle. The resulting coupled equations are solved for φ_m and δ_c, and the front‑wise kink angle distribution follows from the geometric relation φ_MVK(x₃) = arctan( (x₃/d) · tan φ_m ), where d is the half‑length of the initial front.

Finally, the macroscopic rotation rate of the crack surface is obtained as dγ/dδ = (tan φ_m)/d.

## Reproduction target
From the finite element model, compute the SIF distributions for notch inclinations γ = 45°, 60° and 75°. Then, for each γ and for each criterion (MTS and MVK), produce the front‑wise kink angle φ(x₃) along the crack front and the macroscopic rotation rate dγ/dδ. Output these predictions in the files `/app/outputs/kink_predictions.csv` (columns: gamma, x3, phi_MTS, phi_MVK) and `/app/outputs/rotation_rate.csv` (columns: gamma, dgamma_ddelta). The predictions will be compared to hidden experimental measurements.

## Assets

- Open-source finite element solver (e.g., CalculiX, Code_Aster, Elmer): https://www.calculix.de/ or https://www.code-aster.org/ or https://www.csc.fi/web/elmer
- Mesh generation tool (e.g., Gmsh, Salome): https://gmsh.info/ or https://www.salome-platform.org/

## Workflow steps

### Step 1: Finite element computation of SIF distributions
- Role: process
- Action: Build a 3D finite element model of the three-point bending (3PB) specimen with an initial inclined crack at angles γ=45°, 60°, and 75° using the specimen geometry and material parameters specified in the experimental section. Compute the stress intensity factors KI, KII, KIII along the crack front using the modified virtual crack closure integral (MVCCI) method. Save the distributions for all three inclination angles.
- Evidence: `/app/outputs/SIF_distributions.csv`

### Step 2: Predict kink angle distributions (MTS and MVK)
- Role: scored (load-bearing)
- Action: Using the computed SIF distributions, apply the Maximum Tangential Stress (MTS) criterion to compute the local kink angle φ(x3) that annihilates mode II at each front coordinate and inclination angle. Also apply the global mean-value-of-KI (MVK) criterion to compute the maximum kink angle φ_m and then the full front-wise kink angle distribution φ(x3) via the geometric relation given in the paper. Output the predicted kink angle distributions for both criteria.
- Output file: `/app/outputs/kink_predictions.csv`
- Format: csv
- Contract: CSV with columns: gamma (degrees), x3 (mm), phi_MTS (degrees), phi_MVK (degrees). One row per (gamma, x3) sample.
- Scoring: scored by hidden verifier

### Step 3: Predict macroscopic rotation rate
- Role: scored
- Action: From the MVK criterion's maximum kink angle φ_m for each inclination angle and the half-front length d, compute the macroscopic rotation rate dγ/dδ using the geometric relation dγ/dδ = tan(φ_m)/d. Report the rotation rate for each γ.
- Output file: `/app/outputs/rotation_rate.csv`
- Format: csv
- Contract: CSV with columns: gamma (degrees), dgamma_ddelta (rad/mm).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kink_predictions.csv`
- `/app/outputs/rotation_rate.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kink_predictions.csv
- path: `/app/outputs/kink_predictions.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Kink angle distributions for each inclination angle and criterion; the checker recomputes relative error against hidden experimental data.
- schema:
  - `type`: table
  - `required_columns`: `gamma`, `x3`, `phi_MTS`, `phi_MVK`
  - `units`:
    - `gamma`: degrees
    - `x3`: mm
    - `phi_MTS`: degrees
    - `phi_MVK`: degrees

### rotation_rate.csv
- path: `/app/outputs/rotation_rate.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Rotation rate for each inclination angle; compared to hidden experimental gold with a tolerance threshold.
- schema:
  - `type`: table
  - `required_columns`: `gamma`, `dgamma_ddelta`
  - `units`:
    - `gamma`: degrees
    - `dgamma_ddelta`: rad/mm

Notes: The experimental kink angles and rotation rates are embedded in the hidden checker; the agent only needs to produce the computed predictions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kink_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "gamma",
          "x3",
          "phi_MTS",
          "phi_MVK"
        ],
        "units": {
          "gamma": "degrees",
          "x3": "mm",
          "phi_MTS": "degrees",
          "phi_MVK": "degrees"
        }
      },
      "description": "Kink angle distributions for each inclination angle and criterion; the checker recomputes relative error against hidden experimental data."
    },
    {
      "file": "rotation_rate.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "gamma",
          "dgamma_ddelta"
        ],
        "units": {
          "gamma": "degrees",
          "dgamma_ddelta": "rad/mm"
        }
      },
      "description": "Rotation rate for each inclination angle; compared to hidden experimental gold with a tolerance threshold."
    }
  ],
  "notes": "The experimental kink angles and rotation rates are embedded in the hidden checker; the agent only needs to produce the computed predictions."
}
```

## How you are scored
A hidden verifier independently scores each output file. For `kink_predictions.csv`, the verifier compares the predicted kink angle distributions to experimental gold data using a suitable relative error metric. For `rotation_rate.csv`, the verifier compares the computed rotation rates to hidden experimental reference values. The scores are combined (with the kink predictions carrying the majority of the weight) to produce a single final reward in [0,1]. Reporting numbers without genuinely executing the finite element analysis and criteria will yield scores near zero.
