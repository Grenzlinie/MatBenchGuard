# Continuum Elastic Modeling of Topological Defects on Curved Surfaces

## Problem background
Topological defects in nematic liquid crystal shells are influenced by both intrinsic and extrinsic curvature of the surface. This work introduces geometric curvature potentials derived from parallel-transported nematic ground states and uses a coupled shape-nematic model to predict where defects are attracted on axially symmetric closed surfaces. Here you will compute the equilibrium shapes and nematic textures, and investigate whether defect positions coincide with maxima of the computed total curvature potential for different reduced volumes and extrinsic coupling strengths.

## Approach
You will implement a mesoscopic Helfrich–Landau‑de Gennes free energy model that couples membrane curvature with a nematic tensor order parameter. The axially symmetric surface is described by a Fourier‑series representation of its profile, and the nematic configuration on the surface is found by Monte Carlo minimization. The shape and nematic order are minimized iteratively while keeping the reduced volume v constant. From each converged equilibrium, you compute intrinsic, extrinsic, and total curvature potentials; identify topological defects (points of vanishing nematic order); and assign topological charges. Finally, you classify the resulting shell shape (stomatocyte, oblate, or prolate) based on its Gaussian curvature distribution or morphology. The analysis covers a grid of reduced volumes v ∈ [0.45, 0.80] and extrinsic coupling values μ = 0 and μ = 1, producing a set of equilibrium states that span the relevant shape stability regime.

## Reproduction target
For every combination of reduced volume v (from 0.45 to 0.80) and extrinsic coupling μ (0 and 1), run the iterative minimization to obtain a self-consistent shape and nematic texture. From each equilibrium, determine the shape type ('stomatocyte', 'oblate', or 'prolate'), list all topological defects with their arc-length positions s and topological charges (±0.5), and record the total curvature potential w_t as a function of the normalized arc length s/L_s. Assemble all results into a single JSON file results.json with the structure specified in the Output Contract. The verifier will check that your shape classifications are consistent across the (v,μ) parameter space and that each reported defect position lies near a local maximum of the w_t profile (allowing for small numerical tolerance). The total topological charge over all defects in each configuration must sum to 2.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Coupled Shape-Nematic Minimization
- Role: process
- Action: For each (v, μ) configuration (v from 0.45 to 0.80, μ=0 and 1), perform iterative coupled minimization of the total dimensionless free energy. Represent the axially symmetric shape profile by a Fourier series. Compute principal curvatures. Use a Monte Carlo approach to find nematic tensor order parameter components (q0, qm) that minimize the conditional free energy for a fixed shape. Update shape by adjusting Fourier amplitudes to minimize total free energy while keeping reduced volume constant. Iterate between nematic and shape updates until self-consistency. Record equilibrium shape profiles and converged nematic fields.
- Evidence: none

### Step 2: Curvature Potential and Defect Analysis
- Role: scored (load-bearing)
- Action: For each equilibrium configuration from step 1, compute intrinsic curvature potential w_i, extrinsic curvature potential w_e_min (minimized over director angle), and total curvature potential w_t = w_i + 2μ w_e_min. Identify topological defects as points where scalar order parameter λ ≈ 0; assign topological charges (±0.5) based on director field. Determine shape type (stomatocyte, oblate, prolate) from the Gaussian curvature distribution or profile morphology. Aggregate all results into a single JSON file with the structure defined in the Output Contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with key 'simulations' (list). Each element is an object with fields: v (float), mu (float), shape_type (string), defects (list of objects with s (float) and topological_charge (float)), w_t_profile (list of objects with s (float) and w_t (float)), and L_s (float, total profile length).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Complete simulation results for all (v, mu) conditions. Must contain at least the 8 basic volumes (0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80) for both mu=0 and mu=1. The checker validates shape classification consistency with the paper's phase diagram and verifies that each reported defect position lies near a local maximum of w_t_profile.
- schema:
  - `type`: object
  - `required`:
    - `simulations`: array of simulation objects
  - `items`:
    - `simulations`:
      - `v`: float
      - `mu`: float
      - `shape_type`: string
      - `defects`: array of {s: float, topological_charge: float}
      - `w_t_profile`: array of {s: float, w_t: float}
      - `L_s`: float

Notes: No external inputs beyond the model and numerical tools are needed. The agent must implement the full minimization algorithm; a pre-computed or loaded result file would be rejected. The checker uses structural rules derived from the paper (phase boundaries, defect-w_t alignment, total charge 2, individual charges ±0.5).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "simulations": "array of simulation objects"
        },
        "items": {
          "simulations": {
            "v": "float",
            "mu": "float",
            "shape_type": "string",
            "defects": "array of {s: float, topological_charge: float}",
            "w_t_profile": "array of {s: float, w_t: float}",
            "L_s": "float"
          }
        }
      },
      "description": "Complete simulation results for all (v, mu) conditions. Must contain at least the 8 basic volumes (0.45,0.50,0.55,0.60,0.65,0.70,0.75,0.80) for both mu=0 and mu=1. The checker validates shape classification consistency with the paper's phase diagram and verifies that each reported defect position lies near a local maximum of w_t_profile."
    }
  ],
  "notes": "No external inputs beyond the model and numerical tools are needed. The agent must implement the full minimization algorithm; a pre-computed or loaded result file would be rejected. The checker uses structural rules derived from the paper (phase boundaries, defect-w_t alignment, total charge 2, individual charges ±0.5)."
}
```

## How you are scored
A hidden checker reads your results.json and scores your reproduction in two parts, with the following approximate weights:
• Shape classification (60%): For each (v,μ) entry, your shape_type is compared to the correct classification determined by the model. The overall shape‑phase diagram must be correct within a small allowed margin in v.
• Defect alignment (40%): For each configuration, the checker locates local maxima of your reported w_t(s) profile and verifies that each defect’s s‑coordinate lies within a narrow relative window of a detected maximum. Additionally, the checker confirms that the total topological charge equals 2 and that each individual defect charge is ±0.5.
You are not given the exact tolerance limits; your job is to perform the full coupled minimization faithfully and report the resulting equilibria as accurately as your numeric procedures allow.
