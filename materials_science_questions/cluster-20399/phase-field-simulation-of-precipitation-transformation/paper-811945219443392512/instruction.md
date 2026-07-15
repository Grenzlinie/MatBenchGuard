# Compute theoretical parabolic growth-rate constants for ferrite growth in an Fe-C-Mn alloy

## Problem background
In steel metallurgy, the growth kinetics of ferrite from austenite determine microstructure and final properties. When carbon diffusion controls the transformation, the growth of ferrite particles is often modeled as shape-preserving diffusion-controlled growth, with the particle shape idealized as a sphere or ellipsoid. This study examined intragranular ferrite idiomorphs (roughly equiaxed particles nucleated at inclusions) and grain-boundary ferrite allotriomorphs (nucleated at prior austenite grain boundaries) in an Fe-0.09C-1.48Mn alloy. The authors measured three-dimensional particle sizes by serial sectioning and extracted experimental parabolic growth-rate constants (k) at several temperatures. A central question is whether the measured growth kinetics can be accounted for by paraequilibrium carbon diffusion-controlled models. To investigate this, theoretical growth-rate constants can be computed from the provided paraequilibrium supersaturation and carbon diffusivity using the ellipsoidal growth integral. Your task is to compute these theoretical constants.

## Approach
The theoretical growth constants are obtained by solving the shape-preserving diffusion-controlled growth equation for ellipsoidal particles. For a given supersaturation S and particle geometry, the parabolic rate parameter λ (which relates the particle half-dimension to √t) satisfies the integral

  S = 2 λ² exp(λ²) √[(1−rₐ²)(1−r_b²)] ∫₁^∞ exp(−λ² u²) / √[(u²−rₐ²)(u²−r_b²)] du

The geometry parameters rₐ, r_b and the aspect ratio v depend on the morphology:
- Intragranular idiomorphs are treated as spheres: v = 1, rₐ = r_b = 0.
- Face-nucleated grain-boundary allotriomorphs are treated as oblate ellipsoids with aspect ratio v = 1/3: rₐ = 0, r_b = √(1 − v²).
- Edge-nucleated grain-boundary allotriomorphs are treated as prolate ellipsoids with aspect ratio v = 1/3: rₐ = r_b = √(1 − v²).

For each temperature in the supplied supersaturation.csv, you will numerically solve this integral to obtain λ for each morphology, using the corresponding supersaturation S and geometry parameters. Then compute the theoretical parabolic growth-rate constant k = 2 √D v λ, where D is the carbon diffusivity at that temperature taken from carbon_diffusivity.csv. Finally, write the results to the specified CSV file.

## Reproduction target
Produce a CSV file named step_01_theoretical_k.csv under /app/outputs. The file must contain one row for every combination of temperature (present in supersaturation.csv) and morphology: idiomorph, face_allotriomorph, edge_allotriomorph. For each row compute the theoretical_k in cm/s^{1/2} as described in the Approach and write the value. The exact column names and format must follow the Output contract.

## Assets

- Supersaturation values
- Carbon diffusivity in austenite

## Workflow steps

### Step 1: Compute theoretical parabolic growth-rate constants
- Role: scored (load-bearing)
- Action: Load supersaturation.csv and carbon_diffusivity.csv. For each temperature, compute the theoretical parabolic growth-rate constant k for three morphologies: idiomorph (spherical, aspect ratio v=1, r_a=r_b=0), face-nucleated grain-boundary allotriomorph (oblate ellipsoid, v=1/3, r_a=0, r_b=sqrt(1-v^2)), and edge-nucleated grain-boundary allotriomorph (prolate ellipsoid, v=1/3, r_a=r_b=sqrt(1-v^2)). Numerically solve the ellipsoidal shape-preserving diffusion-controlled growth integral that relates supersaturation S to the parabolic rate parameter lambda, using the S for that temperature and the appropriate r_a, r_b. Obtain lambda, then compute k = 2 * sqrt(D) * v * lambda, where D is the carbon diffusivity at that temperature. Write a CSV with columns: temperature (float, in Celsius), morphology_type (string: idiomorph, face_allotriomorph, edge_allotriomorph), theoretical_k (float, in cm/s^{1/2}).
- Output file: `/app/outputs/step_01_theoretical_k.csv`
- Format: csv
- Contract: temperature (float, Celsius), morphology_type (string, one of idiomorph, face_allotriomorph, edge_allotriomorph), theoretical_k (float, cm/s^{1/2})
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_theoretical_k.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_theoretical_k.csv
- path: `/app/outputs/step_01_theoretical_k.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Theoretical parabolic growth-rate constants for three morphologies per temperature, computed using the ellipsoidal diffusion-controlled growth model. The checker will compare each theoretical_k against a hidden experimental k and verify that theoretical_k > experimental_k for all entries.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `morphology_type`, `theoretical_k`
  - `units`:
    - `temperature`: C
    - `morphology_type`: string
    - `theoretical_k`: cm/s^{1/2}

Notes: The hidden experimental k values are those reported in the paper's Table 2. The task only requires computing the theoretical constants; the directional inequality (theoretical > experimental) is verified by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_theoretical_k.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "morphology_type",
          "theoretical_k"
        ],
        "units": {
          "temperature": "C",
          "morphology_type": "string",
          "theoretical_k": "cm/s^{1/2}"
        }
      },
      "description": "Theoretical parabolic growth-rate constants for three morphologies per temperature, computed using the ellipsoidal diffusion-controlled growth model. The checker will compare each theoretical_k against a hidden experimental k and verify that theoretical_k > experimental_k for all entries."
    }
  ],
  "notes": "The hidden experimental k values are those reported in the paper's Table 2. The task only requires computing the theoretical constants; the directional inequality (theoretical > experimental) is verified by the checker."
}
```

## How you are scored
A hidden automatic verifier will score your submission. The verifier reads your step_01_theoretical_k.csv and, for each row, compares your computed theoretical_k to a hidden experimental growth-rate constant reported in the original study for the same temperature and morphology. A threshold_or_better policy is applied: an entry receives credit only if your constant meets the (undisclosed) directional threshold. The final reward is the fraction of entries that satisfy the threshold. Compute the theoretical constants as accurately as possible; you do not need to guess the direction of comparison.
