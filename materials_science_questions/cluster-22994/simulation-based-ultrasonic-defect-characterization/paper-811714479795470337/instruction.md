# Ultrasonic Lamb Wave Lateral Crack Quantification via Coefficient Surface Intersection

## Problem background
Ultrasonic guided waves, such as Lamb waves, enable rapid, long-distance inspection of thin plate-like structures. When a Lamb wave encounters a lateral crack (a notch whose opening is perpendicular to the propagation direction), part of the wave is reflected and part is transmitted. The reflection coefficient |R| and transmission coefficient |T| depend on the crack's width and depth, as well as on the incident wave mode and frequency. Quantifying crack dimensions from these coefficients is an inverse problem of great practical importance for structural integrity management. A fixed-frequency approach is attractive because practical inspections often operate at a preselected frequency, but extracting both width and depth from the two scalar coefficients is challenging.

## Approach
This work uses a two-stage procedure. First, a 2D frequency-domain hybrid boundary element method (BEM) simulates Lamb wave scattering at lateral cracks in a thin steel plate. For a chosen incident pure mode and fixed frequency-thickness product, the simulation is run over a grid of crack widths and depths to build four coefficient surfaces: |R|(w,d) and |T|(w,d) for both rectangular and triangular cross-section notches. These surfaces capture the forward mapping from crack geometry to the measurable coefficients.

Second, a fixed-frequency inverse algorithm uses the precomputed surfaces to quantify an unknown crack. Given measured |R| and |T| for a defect, constant-coefficient planes are drawn through the corresponding surfaces. The intersection curves between each plane and its surface are projected onto the (w,d) plane, and their intersection point provides the quantified width and depth. The algorithm assumes that both coefficients are available and that the coefficient-vs-depth relationship is sufficiently monotonic over the working range.

## Reproduction target
Implement the BEM forward simulation for a 1 mm thick isotropic steel plate (density 7800 kg/m³, shear wave speed 3200 m/s, longitudinal wave speed 5940 m/s) with an incident S0 Lamb wave mode at fd = 1000 Hz·m. For rectangular and triangular cross‑section notches, sample widths from 0.1 mm to 0.7 mm in steps of 0.05 mm and depths from 20% to 60% of plate thickness in steps of 5%. Compute |R| and |T| for the same mode as the incident wave at every (w,d) pair and save the resulting four coefficient surfaces.

Using the simulated surfaces, apply the inverse algorithm to ten test defects: five rectangular notches with true (width, depth) pairs (0.26 mm, 40%), (0.45 mm, 23%), (0.15 mm, 55%), (0.56 mm, 22%), (0.67 mm, 46%) and five triangular notches with the same (width, depth) pairs. For each defect, obtain its “measured” |R| and |T| by interpolation on the appropriate surface, then execute the fixed‑frequency inversion: construct constant‑|R| and constant‑|T| planes, intersect with the coefficient surfaces, project onto the (w,d) plane, and locate the intersection point to obtain quantified width (mm) and depth (%). Produce a CSV file with header defect_shape,true_width_mm,true_depth_percent,quantified_width_mm,quantified_depth_percent containing all ten rows. The true dimensions are inputs to the inversion; the output is the quantified dimensions produced by the algorithm.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Generate coefficient surfaces via BEM simulation
- Role: process
- Action: Implement a 2D frequency-domain hybrid boundary element method simulation for Lamb wave scattering at lateral cracks in a 1 mm steel plate (density 7800 kg/m^3, C_T=3200 m/s, C_L=5940 m/s) with incident S0 mode at fd=1000 Hz·m. For both rectangular and triangular cross-section notches, sample widths from 0.1 mm to 0.7 mm in steps of 0.05 mm and depths from 20% to 60% of plate thickness in 5% steps. Compute the reflection coefficient |R| and transmission coefficient |T| for each (w,d) pair and save the resulting coefficient surfaces.
- Evidence: `/app/outputs/coeff_surfaces_rect_R.npy, coeff_surfaces_rect_T.npy, coeff_surfaces_tri_R.npy, coeff_surfaces_tri_T.npy`

### Step 2: Apply inverse quantification algorithm and report results
- Role: scored (load-bearing)
- Action: Load the precomputed coefficient surfaces. For each of the 10 test defects (rectangular: (0.26 mm,40%), (0.45 mm,23%), (0.15 mm,55%), (0.56 mm,22%), (0.67 mm,46%); triangular: same width-depth pairs), estimate the reflection and transmission coefficients from the corresponding surface by interpolation to serve as measured inputs. Execute the fixed-frequency inverse algorithm: for each defect, construct constant-|R| and constant-|T| planes, intersect with the coefficient surfaces, project the intersection curves onto the (w,d) plane, locate their intersection point(s) to obtain quantified width (mm) and depth (%). Write a CSV file with header defect_shape,true_width_mm,true_depth_percent,quantified_width_mm,quantified_depth_percent containing all 10 rows.
- Output file: `/app/outputs/quantification_results.csv`
- Format: csv
- Contract: CSV with columns: defect_shape (rectangular|triangular), true_width_mm (float), true_depth_percent (float), quantified_width_mm (float), quantified_depth_percent (float). 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/quantification_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### quantification_results.csv
- path: `/app/outputs/quantification_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Quantification results for 10 test defects: column defect_shape is 'rectangular' or 'triangular'; true_width_mm and true_depth_percent are the known input dimensions; quantified_width_mm and quantified_depth_percent are the algorithm's output.
- schema:
  - `type`: table
  - `required_columns`: `defect_shape`, `true_width_mm`, `true_depth_percent`, `quantified_width_mm`, `quantified_depth_percent`

Notes: The true dimensions are provided as inputs to the inverse algorithm; they are not the gold. The gold for scoring is the paper's reported quantified values, compared against the agent's quantified_width_mm and quantified_depth_percent.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "quantification_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_shape",
          "true_width_mm",
          "true_depth_percent",
          "quantified_width_mm",
          "quantified_depth_percent"
        ]
      },
      "description": "Quantification results for 10 test defects: column defect_shape is 'rectangular' or 'triangular'; true_width_mm and true_depth_percent are the known input dimensions; quantified_width_mm and quantified_depth_percent are the algorithm's output."
    }
  ],
  "notes": "The true dimensions are provided as inputs to the inverse algorithm; they are not the gold. The gold for scoring is the paper's reported quantified values, compared against the agent's quantified_width_mm and quantified_depth_percent."
}
```

## How you are scored
A hidden verifier reads your quantification_results.csv. It compares each row’s quantified_width_mm and quantified_depth_percent against the paper’s reported quantified values for the same defect. The comparison uses absolute error tolerances on width and depth. All ten defects must fall within the tolerances to earn full credit; the reward decreases if some defects exceed the bounds. Simply reporting numbers is not enough — the verifier checks the values you produce, not their format.
