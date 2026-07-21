# Simulation of Rayleigh Wave Fields with Multi-Gaussian Beam Model

## Problem background
Angle beam ultrasonic transducers are widely used to generate Rayleigh waves for near‑surface flaw detection and material characterization. Accurately modelling the radiated beam fields is essential for quantitative nondestructive evaluation. A three‑dimensional point source model (PSM) based on high‑frequency asymptotics can compute these fields but requires significant numerical integration and is computationally demanding. A multi‑Gaussian beam (MGB) model has been proposed as an alternative that may yield similar accuracy while being much faster. This task requires implementing both models and comparing the predicted velocity profiles and computational cost for a standard angle‑beam transducer setup.

## Approach
The PSM computes the velocity field at any point by numerically integrating a pressure integral over the transducer surface, using a high‑frequency Rayleigh‑wave Green function and a stationary‑phase approximation to obtain the pressure under the wedge. The MGB model replaces the surface integration with an analytic expression: the pressure under the wedge is expanded as a sum of 10 Gaussian beams, and the Rayleigh‑wave Green function is approximated to yield a closed‑form spatial integral. Both models use the same transducer and material parameters – a circular transducer of specified radius and frequency on a Lucite wedge, incident at the Rayleigh angle, radiating into an aluminium specimen. The agent must evaluate both models on a fine 200×200 grid to measure computational time, and also compute one‑dimensional velocity profiles (on‑axis, off‑axis, and depth) to enable a direct comparison of the predicted field magnitudes.

## Reproduction target
Implement the point source model and the multi‑Gaussian beam model for the given transducer parameters: Lucite wedge P‑wave speed 2.7 mm/µs, incident angle 71.63°, Rayleigh speed in aluminium 2.845 mm/µs, transducer radius 6 mm, frequency 5 MHz, and typical values for density and S‑wave speed in aluminium. Compute the velocity components v1, v2, v3 on the specimen surface (x3 = 0) on two lines: on‑axis (x2 = 0, x1 from 0 to 100 mm, ~1 mm step) and off‑axis (x1 = 50 mm, x2 from −20 to 20 mm, ~0.5 mm step), and a depth profile at x1 = 50 mm, x2 = 0 for x3 from 0 to 5 mm. Also time both models on a 200×200 evaluation grid. Collect the one‑dimensional velocity magnitude data into `velocity_profiles.json` and the recorded PSM and MGB wall‑clock times into `computational_time.json`.

## Assets

- 10-term multi-Gaussian beam coefficients (A_r, B_r)
- Python scientific packages: numpy scipy matplotlib

## Workflow steps

### Step 1: Compute PSM velocity fields and timing
- Role: process
- Action: Implement the point source model (PSM) using the specified transducer/material parameters: Lucite wedge P-wave speed 2.7 mm/µs, incident angle 71.63°, Rayleigh speed in aluminum 2.845 mm/µs, transducer radius 6 mm, frequency 5 MHz. Use necessary additional parameters (density, S-wave speed in aluminum, etc.) with typical values. Compute velocity components v1, v2, v3 on the specimen surface (x3=0) for on-axis grid (x2=0, x1 from 0 to 100 mm, step ~1 mm) and off-axis grid (x1=50 mm, x2 from -20 to 20 mm, step ~0.5 mm), and depth profile at x1=50 mm, x2=0 for x3 from 0 to 5 mm. Record the computational time for a 200×200 point evaluation grid.
- Evidence: `/app/outputs/psm_timing_log.txt`

### Step 2: Compute MGB velocity fields and timing
- Role: process
- Action: Implement the multi-Gaussian beam model (MGB) using the standard 10-term coefficients A_r, B_r (from resource res_coeff) and the same transducer/material parameters as step_psm. Compute velocity components at the identical grid points (on-axis, off-axis, depth) and record the computational time for the same 200×200 grid.
- Evidence: `/app/outputs/mgb_timing_log.txt`

### Step 3: Assemble velocity profiles
- Role: scored (load-bearing)
- Action: Combine the PSM and MGB velocity component magnitudes into a single JSON file, velocity_profiles.json, for the three measurement geometries (on-axis, off-axis, depth).
- Output file: `/app/outputs/velocity_profiles.json`
- Format: json
- Contract: JSON object with keys 'on_axis', 'off_axis', 'depth'. Each value is a list of objects. For 'on_axis', each object has keys 'x1' (float), 'v1_psm' (float), 'v2_psm' (float), 'v3_psm' (float), 'v1_mgb' (float), 'v2_mgb' (float), 'v3_mgb' (float). For 'off_axis', each object has 'x2' (float) and same velocity fields at x1=50mm. For 'depth', each object has 'x3' (float) and same velocity fields at x1=50mm, x2=0.
- Scoring: scored by hidden verifier

### Step 4: Record computational times
- Role: scored
- Action: Write computational_time.json containing the recorded PSM_time_sec and MGB_time_sec for the 200×200 grid evaluation.
- Output file: `/app/outputs/computational_time.json`
- Format: json
- Contract: JSON object with keys 'PSM_time_sec' (float) and 'MGB_time_sec' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/velocity_profiles.json`
- `/app/outputs/computational_time.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### velocity_profiles.json
- path: `/app/outputs/velocity_profiles.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Velocity magnitude profiles from the point source and multi‑Gaussian beam models at three measurement geometries, used to verify agreement between the two models.
- schema:
  - `type`: object
  - `required`: `on_axis`, `off_axis`, `depth`
  - `properties`:
    - `on_axis`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `x1`, `v1_psm`, `v2_psm`, `v3_psm`, `v1_mgb`, `v2_mgb`, `v3_mgb`
        - `additionalProperties`: False
    - `off_axis`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `x2`, `v1_psm`, `v2_psm`, `v3_psm`, `v1_mgb`, `v2_mgb`, `v3_mgb`
        - `additionalProperties`: False
    - `depth`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `x3`, `v1_psm`, `v2_psm`, `v3_psm`, `v1_mgb`, `v2_mgb`, `v3_mgb`
        - `additionalProperties`: False

### computational_time.json
- path: `/app/outputs/computational_time.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Recorded computational times for a 200×200 point evaluation using the two models, used to verify the speedup factor.
- schema:
  - `type`: object
  - `required`: `PSM_time_sec`, `MGB_time_sec`
  - `additionalProperties`: False

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "velocity_profiles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "on_axis",
          "off_axis",
          "depth"
        ],
        "properties": {
          "on_axis": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "x1",
                "v1_psm",
                "v2_psm",
                "v3_psm",
                "v1_mgb",
                "v2_mgb",
                "v3_mgb"
              ],
              "additionalProperties": false
            }
          },
          "off_axis": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "x2",
                "v1_psm",
                "v2_psm",
                "v3_psm",
                "v1_mgb",
                "v2_mgb",
                "v3_mgb"
              ],
              "additionalProperties": false
            }
          },
          "depth": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "x3",
                "v1_psm",
                "v2_psm",
                "v3_psm",
                "v1_mgb",
                "v2_mgb",
                "v3_mgb"
              ],
              "additionalProperties": false
            }
          }
        }
      },
      "description": "Velocity magnitude profiles from the point source and multi‑Gaussian beam models at three measurement geometries, used to verify agreement between the two models."
    },
    {
      "file": "computational_time.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "PSM_time_sec",
          "MGB_time_sec"
        ],
        "additionalProperties": false
      },
      "description": "Recorded computational times for a 200×200 point evaluation using the two models, used to verify the speedup factor."
    }
  ],
  "notes": ""
}
```

## How you are scored
Each scored artifact (`velocity_profiles.json` and `computational_time.json`) is independently assessed by a hidden verifier and contributes a weighted fraction to your final reward (0‑1). For `velocity_profiles.json`, the verifier computes the normalized root‑mean‑square error between the PSM and MGB on‑axis v1 and v3 profiles and checks that the error lies below a confidential tolerance. For `computational_time.json`, the verifier computes the speedup ratio PSM_time_sec / MGB_time_sec and checks that it exceeds a confidential threshold. Reporting a plausible value is not enough – your implementation must actually produce the data so that the verifier’s recomputation yields a passing result. Both checks are directional: lower RMSE and higher speedup are better; meeting or surpassing the hidden thresholds earns full credit for that component.
