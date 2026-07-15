# Optical Distortion Evaluation of Heated Window Using IFT Concept

## Problem background
Aerodynamic heating of aircraft windows creates inhomogeneous temperature and refractive index distributions, causing optical distortion. The interfacial fluid thickness (IFT) concept can be used to identify regions with high refractive index gradients that dominate the optical distortion. By applying a harmonic-mean threshold on the gradient magnitude, one can reconstruct a reduced-data refractive index field that retains only the high-gradient regions and approximates the low-gradient parts. This task aims to computationally evaluate whether the essential optical wave aberration of an aerodynamically heated zinc sulfide window can be captured after discarding a significant portion of the refractive index information.

## Approach
The workflow combines a finite element thermal-structural simulation with optical modeling. First, the temperature, deformation, and strain fields of a zinc sulfide window under a specified heat flux distribution and aerodynamic pressure are computed. From the temperature field, the thermo-optic refractive index field is derived. Its gradient magnitude field is calculated, and the harmonic mean of all non-zero gradient magnitudes defines a threshold GT. A three-step reconstruction procedure uses GT to segregate high-gradient blocks (retaining their indices and gradients) from low-gradient regions (approximated as uniform index stripes by extrapolation from the nearest high-gradient block along the beam direction). The reconstructed field is compared to the original via correlation and retained node fraction. Optical distortion is assessed with a recursive ray-tracing program: rays are traced through the hexahedral grid using node interpolation, and wave aberration is computed for both the original and reconstructed refractive index fields. A tilt-like gradient-index slab case validates the ray-tracing implementation before applying it to the window at a specified incident angle.

## Reproduction target
Produce the following results:
- The harmonic-mean refractive index gradient magnitude threshold GT (units mm⁻¹).
- The percentage of original refractive index nodes retained after reconstruction, and the correlation coefficient between the original and reconstructed refractive index fields.
- The x-coordinate of the point spread function peak from the gradient-index slab ray-tracing validation (mm).
- The RMS wave aberration (in waves) for the original and the reconstructed refractive index fields of the window at 0° azimuth / 75° elevation incidence, together with the relative error between them.
All outputs must be generated from the described finite element simulation and optical calculations, not copied from any external source.

## Assets

- Open-source finite element solver for thermal-structural analysis: http://www.calculix.de/
- Python with NumPy and SciPy: https://pypi.org/

## Workflow steps

### Step 1: Finite Element Thermal-Structural Simulation
- Role: process
- Action: Set up and solve the finite element thermal-structural model of a zinc sulfide window (80×80×8 mm) using materials properties (density 4102 kg/m³, expansion coefficient 7.0e-6 K⁻¹, heat capacity 470 J/(kg·K), Young's modulus 74e9 Pa, thermal conductivity 19 W/(m·K), Poisson ratio 0.29) and boundary conditions: heat flux distribution on the outside surface divided into nine regions with specified fluxes (2.60e4, 7.97e3, 5.03e3, 4.20e4, 1.21e5, 4.40e4, 4.70e4, 5.91e4, 7.39e4 W/m²), aerodynamic pressure 5.0e5 Pa on outside, inner air pressure 1.0e5 Pa on inside and sides, initial temperature 300 K, exposure time 15 s. Obtain temperature, sum deformation, and equivalent von Mises strain fields at 15 s.
- Evidence: none

### Step 2: Computation of Thermo-Optic Refractive Index Field
- Role: process
- Action: From the temperature field at 15 s, compute the 3D refractive index field on the same grid (80×80×8, 59,049 nodes) using the thermo-optic relation: n = n0 + dn/dT * (T - T0), with n0 = 2.20, dn/dT = 4.10e-5 K⁻¹, T0 = 300 K. Exclude elasto-optic contributions.
- Evidence: none

### Step 3: Computation of Refractive Index Gradient Magnitude Field
- Role: process
- Action: Compute the 3D refractive index gradient magnitude field from the refractive index field using finite differences on the 80×80×8 grid.
- Evidence: none

### Step 4: Harmonic-Mean Gradient Magnitude Threshold
- Role: scored
- Action: Compute the harmonic-mean refractive index gradient magnitude threshold GT using all non-zero gradient magnitudes. Write the value to threshold_GT.txt as a single float in scientific notation (units mm⁻¹).
- Output file: `/app/outputs/threshold_GT.txt`
- Format: txt
- Contract: A single floating-point number in scientific notation, e.g., '4.03e-05' (units: mm⁻¹).
- Scoring: scored by hidden verifier

### Step 5: Refractive Index Field Reconstruction and Correlation
- Role: scored (load-bearing)
- Action: Apply the three-step modeling procedure using GT: (1) identify all grid points with |∇n| > GT as high-gradient blocks, record their locations, indices and gradients; (2) for points with |∇n| ≤ GT, set the gradient to zero; (3) for each zero-gradient region, assign a uniform refractive index by extrapolating from the nearest high-gradient block along the beam propagation direction (z-axis). Compute the percentage of original refractive index nodes retained and the correlation coefficient r between original and reconstructed fields. Write both results to reconstruction_stats.json.
- Output file: `/app/outputs/reconstruction_stats.json`
- Format: json
- Contract: {"nodes_retained_percent": number, "correlation_coefficient": number}
- Scoring: scored by hidden verifier

### Step 6: Ray-Tracing Program Validation
- Role: scored
- Action: Implement a ray-tracing algorithm (recursive propagation through hexahedral grids with node interpolation) and validate it using a tilt-like gradient-index slab with parameters: c=2.20, α=0.02 mm⁻¹, thickness d=8 mm, exit pupil D=60 mm, ideal lens focal length f'=150 mm, wavelength λ=10 μm. Compute the normalized point spread function and extract the x-coordinate of the peak. Write that x-coordinate (in mm) to validation_peak.txt.
- Output file: `/app/outputs/validation_peak.txt`
- Format: txt
- Contract: A single floating-point number (mm).
- Scoring: scored by hidden verifier

### Step 7: Optical Distortion Evaluation
- Role: scored (load-bearing)
- Action: Using the validated ray-tracing program, simulate transmission through the original refractive index field and the reconstructed refractive index field for the window at 0° azimuth / 75° elevation incidence (exit pupil D=60 mm, lens f'=150 mm, λ=10 μm). For each field, compute the RMS wave aberration (in waves). Report all three values in wave_aberration_results.json as {"rms_original": number, "rms_reconstructed": number, "relative_error_percent": number}.
- Output file: `/app/outputs/wave_aberration_results.json`
- Format: json
- Contract: {"rms_original": number, "rms_reconstructed": number, "relative_error_percent": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/threshold_GT.txt`
- `/app/outputs/reconstruction_stats.json`
- `/app/outputs/validation_peak.txt`
- `/app/outputs/wave_aberration_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### threshold_GT.txt
- path: `/app/outputs/threshold_GT.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Harmonic-mean refractive index gradient magnitude threshold.
- schema:
  - `type`: text
  - `units`: mm⁻¹

### reconstruction_stats.json
- path: `/app/outputs/reconstruction_stats.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Percentage of original refractive index nodes retained and correlation coefficient between original and reconstructed fields.
- schema:
  - `type`: object
  - `required`:
    - `nodes_retained_percent`: number (percentage)
    - `correlation_coefficient`: number

### validation_peak.txt
- path: `/app/outputs/validation_peak.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: X-coordinate of the PSF peak from the gradient-index slab ray-tracing validation.
- schema:
  - `type`: text
  - `units`: mm

### wave_aberration_results.json
- path: `/app/outputs/wave_aberration_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: RMS wave aberration of original and reconstructed refractive index fields, and the relative error between them.
- schema:
  - `type`: object
  - `required`:
    - `rms_original`: number (waves)
    - `rms_reconstructed`: number (waves)
    - `relative_error_percent`: number (percent)

Notes: All output files must be placed under /app/outputs. The finite-element simulation step is not scored directly; only its downstream optical products are verified. The ray-tracing algorithm must be implemented according to the described recursive grid-based method; no external ray-tracing library is assumed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "threshold_GT.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "mm⁻¹"
      },
      "description": "Harmonic-mean refractive index gradient magnitude threshold."
    },
    {
      "file": "reconstruction_stats.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "nodes_retained_percent": "number (percentage)",
          "correlation_coefficient": "number"
        }
      },
      "description": "Percentage of original refractive index nodes retained and correlation coefficient between original and reconstructed fields."
    },
    {
      "file": "validation_peak.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "mm"
      },
      "description": "X-coordinate of the PSF peak from the gradient-index slab ray-tracing validation."
    },
    {
      "file": "wave_aberration_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "rms_original": "number (waves)",
          "rms_reconstructed": "number (waves)",
          "relative_error_percent": "number (percent)"
        }
      },
      "description": "RMS wave aberration of original and reconstructed refractive index fields, and the relative error between them."
    }
  ],
  "notes": "All output files must be placed under /app/outputs. The finite-element simulation step is not scored directly; only its downstream optical products are verified. The ray-tracing algorithm must be implemented according to the described recursive grid-based method; no external ray-tracing library is assumed."
}
```

## How you are scored
A hidden verifier independently checks the artifacts you write. Each scored workflow step contributes a weighted portion to the final reward. The verifier compares your computed values against reference thresholds and tolerances. Simply reporting numbers from a publication is not sufficient; your execution of the full computational pipeline must produce the artifacts. The verifier will not reveal the expected values, so focus on correctly implementing the described methods and writing the required output files.
