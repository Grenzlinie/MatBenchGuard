# Predicting Mode I Delamination Toughness of Stitched CFRPs via Micromechanics Model

## Problem background
The interlaminar fracture toughness of traditional carbon‑fibre reinforced polymer laminates is low, making them susceptible to delamination when subjected to interlaminar stresses. Stitching the laminate through‑the‑thickness with high‑strength yarns can substantially increase the mode I delamination toughness by introducing crack‑closure forces. The mechanisms involve debonding of the thread/matrix interface, elastic stretching of the threads, thread rupture, and subsequent pull‑out. This task implements a micromechanics‑based model that predicts the steady‑state mode I delamination toughness (often referred to as G_IRs) from measured material and geometric parameters. The model captures the quantitative influence of stitch density, thread diameter, and thread type on interlaminar toughness.

## Approach
The model treats the double‑cantilever beam specimen using Euler–Bernoulli beam theory. The crack‑opening displacement is governed by a differential equation that includes the closure traction from the bridging stitches. The closure traction depends on the stitch density, the thread‑matrix interfacial frictional shear stress, the thread tensile strength and stiffness, and the available embedded length. Step functions model the transitions among frictional slip, elastic stretching, thread rupture at the embedded end, and pull‑out. By solving the beam equation and integrating the resulting traction along the crack‑bridging zone, the crack‑growth resistance expressed as a stress intensity factor is computed. This is then converted to the energy release rate G_IR(Δa). The steady‑state value G_IRs is extracted as the plateau of the R‑curve. The model is applied to several stitch configurations that differ in thread type (Kevlar or carbon), ply count, and stitch density, using experimentally measured input parameters (thread properties after stitching, interfacial shear stress, flexural moduli, stitch geometry, and specimen dimensions).

## Reproduction target
Implement the micromechanics model and use the provided material and geometric parameters. For every stitch configuration listed in Table 6 of the source paper (2‑ply Kevlar at 4, 8, and 12 stitches cm⁻²; 3‑ply Kevlar at 4 stitches cm⁻²; 4‑ply Kevlar at 4 and 8 stitches cm⁻²; T900 carbon at 4 and 8 stitches cm⁻²), compute the G_IR(Δa) curve and extract the steady‑state value G_IRs. Output a CSV file with one row per configuration containing the thread type, the stitch density (stitches per cm²), and the predicted G_IRs (in kJ m⁻²). The computed values should reflect the expected physics: within each thread family, higher stitch density or larger thread diameter should lead to a higher predicted steady‑state toughness.

## Assets

- NumPy: numpy
- SciPy: scipy

## Model input parameters

The following material, geometric, and stitch parameters are required for the micromechanics model. They are taken from Tables 1, 2, 3, and 6 of the source publication and are provided here for self‑contained reproducibility.

### Thread and interfacial properties

| Thread type | 2-ply Kevlar | 3-ply Kevlar | 4-ply Kevlar | T900 carbon |
|-------------|--------------|--------------|--------------|-------------|
| Loop tensile strength σ_fu (GPa) | 1.79 | 1.89 | 1.87 | 2.21 |
| Thread Young's modulus E_f (GPa) | 62.5 | 56.8 | 49.3 | 217.9 |
| Thread diameter d_f (mm) | 0.16 | 0.200 | 0.234 | 0.164 |
| Interfacial pull‑out shear stress τ (MPa) | 18.2 | 21.4 | 24.7 | 37.6 |

### Laminate geometry and stiffness

| Parameter | Value | Notes |
|-----------|-------|-------|
| Laminate half‑thickness h_c (mm) | 1.5 | Specimen half‑thickness |
| Initial crack length a₀ (mm) | 25 |  |
| Stitch pitch L_p (mm) | 3.33 | For all configurations (Table 6) |
| Orthotropic modulus E_0 (GPa) | 11.37 |  |
| Intrinsic fracture toughness K_Ic (MPa·√m) | 2.24 | Unstitched steady‑state value |

### Configuration‑specific parameters

| Configuration | Stitch density (st/cm²) | E_c (GPa) | S_L (mm) |
|---------------|------------------------|-----------|----------|
| 2-ply Kevlar 4 st/cm² | 4 | 95.5 | 7.5 |
| 2-ply Kevlar 8 st/cm² | 8 | 88.9 | 3.75 |
| 2-ply Kevlar 12 st/cm² | 12 | 87.5 | 2.5 |
| 3-ply Kevlar 4 st/cm² | 4 | 90.7 | 7.5 |
| 4-ply Kevlar 4 st/cm² | 4 | 89.5 | 7.5 |
| 4-ply Kevlar 8 st/cm² | 8 | 85.6 | 3.75 |
| T900 carbon 4 st/cm² | 4 | 88.0 | 7.5 |
| T900 carbon 8 st/cm² | 8 | 87.4 | 3.75 |

## Workflow steps

### Step 1: Compile model input parameters
- Role: process
- Action: Compile the model input parameters from the specification above into a JSON file `/app/outputs/parameters.json`. The file should contain an array of configuration objects, each including fields: `thread_type` (string), `stitch_density` (float, st/cm²), `E_c` (GPa), `tau` (MPa), `d_f` (mm), `sigma_fu` (GPa), `E_f` (GPa), `L_p` (mm), `S_L` (mm), `h_c` (mm), `a_0` (mm), `K_Ic` (MPa·√m), and `E_0` (GPa). Use the values from the tables above.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Predict steady-state delamination toughness
- Role: scored (load-bearing)
- Action: Implement the micromechanics model using the parameters from the previous step. For each stitch configuration listed in the paper (2-ply Kevlar at 4, 8, 12 stitches/cm², 3-ply Kevlar at 4, 4-ply Kevlar at 4, 8, T900 carbon at 4, 8), compute the crack closure traction, solve the beam equation, calculate the crack growth resistance K_IR(Δa) and energy release rate G_IR(Δa), extract the steady-state value G_IRs, and output the predictions.
- Output file: `/app/outputs/predicted_G_IRs.csv`
- Format: csv
- Contract: thread_type: string, stitch_density: float (stitches per cm²), G_IRs_predicted: float (kJ/m²)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_G_IRs.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_G_IRs.csv
- path: `/app/outputs/predicted_G_IRs.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Predicted steady-state mode I delamination toughness values for stitched laminate configurations listed in the paper's Table 6. The values are compared to experimental measurements (hidden) with a tolerance on relative error for Kevlar threads, and a directional check for carbon threads. Monotonic trends with stitch density and thread diameter are also verified.
- schema:
  - `type`: table
  - `required_columns`: `thread_type`, `stitch_density`, `G_IRs_predicted`
  - `columns`:
    - `thread_type`:
      - `type`: string
    - `stitch_density`:
      - `type`: float
      - `unit`: stitches per cm²
    - `G_IRs_predicted`:
      - `type`: float
      - `unit`: kJ/m²
  - `units`:
    - `stitch_density`: stitches per cm²
    - `G_IRs_predicted`: kJ/m²

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_G_IRs.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "thread_type",
          "stitch_density",
          "G_IRs_predicted"
        ],
        "columns": {
          "thread_type": {
            "type": "string"
          },
          "stitch_density": {
            "type": "float",
            "unit": "stitches per cm²"
          },
          "G_IRs_predicted": {
            "type": "float",
            "unit": "kJ/m²"
          }
        },
        "units": {
          "stitch_density": "stitches per cm²",
          "G_IRs_predicted": "kJ/m²"
        }
      },
      "description": "Predicted steady-state mode I delamination toughness values for stitched laminate configurations listed in the paper's Table 6. The values are compared to experimental measurements (hidden) with a tolerance on relative error for Kevlar threads, and a directional check for carbon threads. Monotonic trends with stitch density and thread diameter are also verified."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will independently evaluate your predicted_G_IRs.csv by comparing your predicted steady‑state toughness values to the experimental measurements reported in the literature (not provided). For Kevlar‑thread configurations, the verifier will check that your predicted values fall within a specified tolerance of the hidden experimental values; predictions that are closer to the measurements receive higher credit, while larger deviations receive lower credit. The verifier will also verify that your predictions exhibit the correct monotonic trends: with a given thread type, increasing stitch density or larger thread diameter should lead to higher predicted G_IRs. For the T900 carbon configurations, the verifier will check that your predicted values are lower than the corresponding experimental measurements (the model is expected to underpredict for this thread type). The overall reward is a weighted combination of these checks. Note that merely reporting the paper's published numbers is insufficient; the verifier will examine the detailed numerical output to confirm that the model has been genuinely implemented and solved.
