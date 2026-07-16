# Ultrasonic transducer lens design optimization via Gauss-Hermite beam model

## Problem background
In immersion ultrasonic inspection of steel bar stock, the sound beam must enter through a cylindrical surface. This curved entry acts as a lens and defocuses the beam in the rotational direction, broadening the images of embedded inclusions. A practical way to compensate for this effect is to attach a bi‑cylindrical lens to the transducer so that the resulting beam profile within the steel mimics that of a standard spherically focused probe inspecting through a flat surface. This task uses a Gauss‑Hermite beam model to numerically optimize such a lens for a 15‑MHz, 0.5‑inch‑diameter circular transducer inspecting 3‑inch‑diameter cylindrical steel bar stock. The optimized lens design — its geometric focal lengths in the x‑z and y‑z planes, plus the water path — is the quantity to be computed.

## Approach
The core of the reproduction is a Gauss‑Hermite beam propagation model that computes the ultrasonic pressure field in water and steel. The workflow consists of two stages. First, a reference on‑axis |pressure|² vs. depth profile is computed for the existing, commercially available spherically focused transducer (effective element diameter and geometrical focal length in water are known fixed values) under a flat entry surface and a prescribed water path. This profile becomes the target curve that the lens design must replicate. Second, the beam model is run for a normal‑incidence inspection through the cylindrical surface of the 3‑inch bar, now assuming a bi‑cylindrical lens attached to the same transducer element. The lens’s two geometric focal lengths (Fx in the x‑z plane, Fy in the y‑z plane) and the water path are adjusted iteratively to minimize the difference between the computed curved‑surface amplitude‑vs‑depth curve and the flat‑entry reference curve. All computations use fixed, published sound speeds for water and steel.

## Reproduction target
Compute and report in a JSON file the geometric focal lengths Fx and Fy (in inches) and the associated inspection water path (in inches) of a bi‑cylindrical lens that best reproduces, for the 3‑inch‑diameter cylindrical bar, the on‑axis |pressure|² vs. depth profile produced through a flat entry surface by the same transducer element. The output file, `/app/outputs/optimized_lens_parameters.json`, must contain the three numeric fields `Fx_in`, `Fy_in`, and `waterpath_in`. The instructions and given transducer parameters fully specify the required input conditions; no external data sets are needed.

## Assets

- Python 3 scientific computing environment: python3

## Workflow steps

### Step 1: Compute reference flat-entry amplitude-vs-depth profile
- Role: process
- Action: Implement a Gauss-Hermite beam model for ultrasonic pressure field propagation in water and steel. Using the transducer parameters: effective element diameter 0.51 in, geometrical focal length in water 2.93 in, frequency 15 MHz, sound speed in water 0.149 cm/μs, sound speed in steel 0.590 cm/μs, and inspection waterpath 1.97 in (through a flat entry surface), compute the on-axis |pressure|² vs depth profile in steel. Save the computed profile as reference_profile.json (an array of depth–value pairs).
- Evidence: `/app/outputs/reference_profile.json`

### Step 2: Optimize bi-cylindrical lens focal parameters
- Role: scored (load-bearing)
- Action: Using the same Gauss-Hermite beam model, compute the on-axis |pressure|² vs depth profile for a normal-incidence inspection through a cylindrical surface of a 3-inch diameter steel bar, with a bi-cylindrical lens attached to the same transducer. Vary the geometric focal lengths Fx (in the x-z plane) and Fy (in the y-z plane), and the waterpath, to minimize the discrepancy between the resulting curved-surface profile and the flat-entry reference profile from the previous step. Use the same sound speeds. Save the optimized parameters to optimized_lens_parameters.json.
- Output file: `/app/outputs/optimized_lens_parameters.json`
- Format: json
- Contract: {"Fx_in": float, "Fy_in": float, "waterpath_in": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimized_lens_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimized_lens_parameters.json
- path: `/app/outputs/optimized_lens_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized geometric focal lengths and inspection waterpath for the bi‑cylindrical lens, computed by fitting the curved‑surface amplitude‑vs‑depth profile to the flat‑entry reference profile.
- schema:
  - `type`: object
  - `required`: `Fx_in`, `Fy_in`, `waterpath_in`
  - `properties`:
    - `Fx_in`:
      - `type`: number
      - `units`: inches
    - `Fy_in`:
      - `type`: number
      - `units`: inches
    - `waterpath_in`:
      - `type`: number
      - `units`: inches

Notes: The hidden checker compares the reported Fx_in, Fy_in, waterpath_in against the paper’s published values using per‑parameter absolute tolerances. The reference flat‑entry profile is not scored but must be computed to perform the optimization.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimized_lens_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "Fx_in",
          "Fy_in",
          "waterpath_in"
        ],
        "properties": {
          "Fx_in": {
            "type": "number",
            "units": "inches"
          },
          "Fy_in": {
            "type": "number",
            "units": "inches"
          },
          "waterpath_in": {
            "type": "number",
            "units": "inches"
          }
        }
      },
      "description": "Optimized geometric focal lengths and inspection waterpath for the bi‑cylindrical lens, computed by fitting the curved‑surface amplitude‑vs‑depth profile to the flat‑entry reference profile."
    }
  ],
  "notes": "The hidden checker compares the reported Fx_in, Fy_in, waterpath_in against the paper’s published values using per‑parameter absolute tolerances. The reference flat‑entry profile is not scored but must be computed to perform the optimization."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/optimized_lens_parameters.json` and compares the reported Fx, Fy, and water path to independently determined gold values. Each parameter is checked against a per‑parameter tolerance (the tolerances themselves are not disclosed). Full credit is awarded if all three values fall within their respective tolerances; partial credit is given proportional to the number of values that satisfy the tolerance. The intermediate flat‑entry reference profile file is required for the optimization but is not scored directly. The final reward is a single floating‑point number between 0 and 1 that reflects the quality of your lens design parameters.
