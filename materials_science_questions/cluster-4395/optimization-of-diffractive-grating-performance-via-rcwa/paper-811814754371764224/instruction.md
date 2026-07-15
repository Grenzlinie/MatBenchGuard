# Reproduce Resonant Surface-Roughness LER Peaks in a Superlens Imaging System

## Problem background
Planar superlenses made from plasmonic materials like silver can image sub-diffraction features by amplifying evanescent near-fields. However, these imaging systems are sensitive to surface roughness at the metal-dielectric interfaces, which introduces line-edge roughness (LER) in the projected image. The roughness is characterized by its spatial frequency content, and different spatial frequencies can affect the image quality in different ways. This work investigates how the spatial frequency of sinusoidal surface roughness on the superlens interfaces influences the resulting image LER for a 100 nm half-pitch grating object. The primary quantity to compute is the LER as a function of the roughness wave vector, and from that dependence, to identify resonant features that amplify LER above a non-resonant baseline.

## Approach
The approach uses two-dimensional finite-element method (FEM) simulations to solve Maxwell's equations for a single-layer silver superlens sandwiched between dielectric spacers. The object is a grating with four slits at 100 nm half-pitch, and the image plane is located beyond the object plane. Sinusoidal surface roughness with a fixed RMS amplitude is introduced independently on both silver-dielectric interfaces, and the roughness period is swept across a wide range. For each spatial frequency (defined by the period), an ensemble of simulations is run with random phase offsets to capture statistical variation. The resulting intensity profiles along the image plane are analyzed to extract edge positions, from which line-edge roughness (LER) is computed as a multiple of the standard deviation of those edge positions. The LER vs. roughness wave vector curve is then examined to locate and characterize resonance peaks, including their center positions, widths, and relative increases over a baseline LER measured in a flat region of the curve.

## Reproduction target
Produce the LER vs. roughness wave vector k_y curve for the superlens system imaging a 100 nm half-pitch grating. From that curve, identify all distinct resonance peaks. For each peak, report its center wave vector (k_y), full width at half maximum (FWHM), and the ratio (relative increase) of the peak LER to a non-resonant baseline LER.

## Assets

- scikit-fem: scikit-fem
- numpy: numpy
- scipy: scipy
- matplotlib: matplotlib

## Workflow steps

### Step 1: Construct and validate superlens FEM model
- Role: process
- Action: Build a 2D finite-element simulation domain (~1.2 μm × 1.0 μm) with perfectly matched layers (PML) on the x-boundaries. Define the superlens geometry: a 30 nm silver layer (ε_r = -1 - 0.2j, μ_r = 1) sandwiched between two 15 nm spacer layers (ε_r = μ_r = 1). The object is a four-slit grating with 100 nm half-pitch made of a high-conductivity mask material (σ = 3.774×10⁷ S/m, ε_r = μ_r = 1). The image plane is 60 nm beyond the object plane. Use TM-polarized illumination at 365 nm. Perform mesh convergence tests to ensure numerical accuracy (target ~350,000 elements).
- Evidence: `/app/outputs/mesh_convergence.txt`

### Step 2: Run roughness ensemble FEM simulations
- Role: process
- Action: For each roughness spatial frequency k_y, corresponding to periods Λ from 10 nm to 1 μm (k_y = 2π/Λ), introduce sinusoidal surface roughness on both silver–dielectric interfaces with amplitude A = √2 nm (1 nm RMS). For each k_y value, run 15 FEM simulations with random initial phases for each interface. Record the resulting intensity profile along the image plane for every run.
- Evidence: `/app/outputs/simulation_log.json`

### Step 3: Compute LER vs k_y curve
- Role: scored
- Action: For each ensemble of 15 intensity profiles at a given k_y, extract the edge positions from the intensity profiles, compute the standard deviation σ of the edge positions, and calculate LER = 3σ. Aggregate the results to produce a table mapping k_y to the mean LER value.
- Output file: `/app/outputs/step_03_ler_vs_ky.csv`
- Format: csv
- Contract: columns: ky (float), ler (float). ky is roughness wave number in μm⁻¹; ler is line-edge roughness in nm.
- Scoring: scored by hidden verifier

### Step 4: Identify resonance peaks
- Role: scored (load-bearing)
- Action: Analyze the LER vs k_y data to locate the three resonance peaks. For each peak, determine the center k_y, the full width at half maximum (FWHM) using linear interpolation, and the relative LER increase compared to a non-resonant baseline (average LER over a flat region of the curve). Output a JSON object containing the baseline LER and an array of peak objects.
- Output file: `/app/outputs/step_04_peaks.json`
- Format: json
- Contract: {"baseline_ler": <float>, "peaks": [{"center_ky": <float>, "fwhm": <float>, "relative_increase": <float>}, ...]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_ler_vs_ky.csv`
- `/app/outputs/step_04_peaks.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_ler_vs_ky.csv
- path: `/app/outputs/step_03_ler_vs_ky.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of roughness wave number (ky) vs. calculated line-edge roughness (LER). Used to verify the presence of resonance peaks and overall curve shape.
- schema:
  - `type`: table
  - `required_columns`: `ky`, `ler`
  - `units`:
    - `ky`: μm⁻¹
    - `ler`: nm

### step_04_peaks.json
- path: `/app/outputs/step_04_peaks.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Extracted resonance peak parameters: baseline LER and, for each of the three peaks, its center wave number, FWHM, and relative LER increase over baseline.
- schema:
  - `type`: object
  - `required`:
    - `baseline_ler`: float
    - `peaks`: array
  - `items`:
    - `center_ky`: float
    - `fwhm`: float
    - `relative_increase`: float

Notes: The task reproduces the main result of the paper. The LER vs ky curve (step_03) is checked for structural consistency (plausible values, presence of peaks). The peak parameters (step_04) are compared to the paper's reported values with hidden tolerances. No gold values are revealed in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_ler_vs_ky.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "ky",
          "ler"
        ],
        "units": {
          "ky": "μm⁻¹",
          "ler": "nm"
        }
      },
      "description": "Table of roughness wave number (ky) vs. calculated line-edge roughness (LER). Used to verify the presence of resonance peaks and overall curve shape."
    },
    {
      "file": "step_04_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "baseline_ler": "float",
          "peaks": "array"
        },
        "items": {
          "center_ky": "float",
          "fwhm": "float",
          "relative_increase": "float"
        }
      },
      "description": "Extracted resonance peak parameters: baseline LER and, for each of the three peaks, its center wave number, FWHM, and relative LER increase over baseline."
    }
  ],
  "notes": "The task reproduces the main result of the paper. The LER vs ky curve (step_03) is checked for structural consistency (plausible values, presence of peaks). The peak parameters (step_04) are compared to the paper's reported values with hidden tolerances. No gold values are revealed in the public contract."
}
```

## How you are scored
Your submitted artifacts will be evaluated by a hidden verifier. The verifier first checks that the LER vs. k_y CSV file has the correct structure and contains plausible LER values with clear peaks roughly in the expected range. Then it reads the peak parameters from the JSON file and compares each reported quantity (center k_y, FWHM, relative increase) against reference values derived from the published study, using pre-defined tolerances appropriate for each parameter. The final reward is a weighted sum of these checks. You must execute the full simulation pipeline; simply reporting numbers without running the simulations will not pass.
