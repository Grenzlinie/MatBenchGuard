# Evaluation of 2D Pyramid TiO₂ Grating Antireflection for Multijunction Concentrator Cells

## Problem background
Multi-junction concentrator solar cells collect sunlight focused from a wide range of angles, which causes conventional planar double-layer anti-reflection coatings to perform poorly away from normal incidence. This angular degradation increases reflection losses and can introduce current mismatch between subcells, reducing overall device efficiency. Sub-wavelength dielectric gratings, modeled as a stack of thin films with a gradually changing effective refractive index, offer a potential solution by providing broadband, wide-angle antireflection. The goal of this work is to quantify how much the angle-averaged reflection-loss-related current loss can be reduced by replacing a double-layer ARC with an optimized 2D pyramidal grating in a concentrator system operating at a 60° aperture half-angle.

## Approach
The optical model uses an effective medium approximation (linear average of permittivity, q = 1/2) to represent each horizontal slice of a sub-wavelength grating as a homogeneous thin film with an effective refractive index that depends on the grating geometry and occupation ratio. Reflection from the multilayer structure is computed with the transfer matrix method. The two designs to be compared are:
- A double-layer planar ARC: MgF₂ (124 nm) / ZnS (70 nm) on an Al₀.₈Ga₀.₂As substrate.
- A 2D pyramidal TiO₂ grating: height 260 nm, planar-film thickness 50 nm, occupation ratio 0.7, on the same substrate.
For each design, the reflectance R(θ,λ) is calculated over the wavelength range 300–1850 nm and for incident angles from 0° to 60°. The AM1.5G photon flux is used to integrate the reflected photon flux at each angle, yielding an angle-dependent integrated photon loss. Finally, the total current loss per concentration at a given aperture half-angle is obtained by averaging the angle-dependent loss with a ring-area weighting scheme that accounts for both the change in projected area and the angular distribution of light in a concentrator, as is standard in concentrator photovoltaic characterization.

## Reproduction target
Compute and report the following three quantities:
- The total current loss (in mA/cm² per concentration) for the MgF₂/ZnS double-layer ARC (124 nm / 70 nm) at a 60° aperture half-angle.
- The total current loss (in mA/cm² per concentration) for the 2D pyramidal TiO₂ grating (h=260 nm, t=50 nm, f=0.7) at a 60° aperture half-angle.
- The improvement in current loss, defined as (double-layer loss) − (grating loss), also in mA/cm² per concentration.
All three values must be derived from the angular- and wavelength-integrated reflectance computed with the optical model and concentrator averaging described above, applied over the AM1.5G spectral range (300–1850 nm). Each number must be written as a single floating-point value in its own plain-text file.

## Assets

- AM1.5G solar spectrum: https://www.nrel.gov/grid/solar-resource/spectra-am1.5.html
- Refractive index data for MgF2, ZnS, TiO2, Al0.8Ga0.2As: https://refractiveindex.info
- numpy: numpy
- scipy: scipy
- tmm (optional): tmm

## Workflow steps

### Step 1: Implement optical simulation model
- Role: process
- Action: Implement the transfer matrix method for multilayer thin-film systems, extended with the effective medium approximation (linear average of permittivity, q = 1/2) to handle sub-wavelength grating layers. The model must accept geometry parameters (layer thicknesses, occupation ratio, shape), material refractive indices (with dispersion), and angle/wavelength to compute reflectance R(θ,λ). Validate the model with a sample configuration.
- Evidence: `/app/outputs/reflectance_check.csv`

### Step 2: Generate angle- and wavelength-resolved reflectance for both designs
- Role: process
- Action: Using the implemented model, compute the reflectance R(θ,λ) at a set of discrete incident angles (e.g., 0° to 60° in 1° steps) over the wavelength range 300–1850 nm for (a) the double-layer MgF₂/ZnS ARC (thicknesses 124 nm / 70 nm) and (b) the 2D pyramidal TiO₂ grating (height 260 nm, planar-film thickness 50 nm, occupation ratio 0.7). The incident medium is air, substrate is Al₀.₈Ga₀.₂As. Integrate the reflected photon flux separately for each angle and wavelength using the AM1.5G photon flux to obtain an angle‑dependent integrated photon loss R(θ). Save R(θ) for both designs.
- Evidence: `/app/outputs/integrated_loss_vs_angle.csv`

### Step 3: Compute total current loss for double-layer ARC
- Role: scored (load-bearing)
- Action: From the angle‑dependent integrated photon loss R(θ) for the double-layer ARC, compute the total current loss per concentration at aperture half‑angle α = 60° using the ring‑area weighting scheme (area weighting factor (tan²θ_{m+1}−tan²θ_m)/tan²α) and the AM1.5G total photon flux I₀. Output the result in mA/cm² per concentration.
- Output file: `/app/outputs/double_layer_current_loss.txt`
- Format: txt
- Contract: Single float (unit: mA/cm² per concentration).
- Scoring: scored by hidden verifier

### Step 4: Compute total current loss for 2D pyramid TiO₂ grating
- Role: scored
- Action: Perform the same concentrator averaging for the grating's R(θ) to obtain the total current loss per concentration at α = 60°.
- Output file: `/app/outputs/pyramid_current_loss.txt`
- Format: txt
- Contract: Single float (unit: mA/cm² per concentration).
- Scoring: scored by hidden verifier

### Step 5: Compute current improvement
- Role: scored
- Action: Calculate the improvement as (double-layer current loss) – (pyramid current loss) and write the result in mA/cm² per concentration.
- Output file: `/app/outputs/improvement.txt`
- Format: txt
- Contract: Single float (unit: mA/cm² per concentration).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/double_layer_current_loss.txt`
- `/app/outputs/pyramid_current_loss.txt`
- `/app/outputs/improvement.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### double_layer_current_loss.txt
- path: `/app/outputs/double_layer_current_loss.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Total current loss for the optimized double-layer MgF₂/ZnS ARC (124nm/70nm) on an air-matched 3J device at 60° aperture half-angle.
- schema:
  - `type`: text
  - `shape`: scalar
  - `unit`: mA/cm² per concentration

### pyramid_current_loss.txt
- path: `/app/outputs/pyramid_current_loss.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Total current loss for the 2D pyramidal TiO₂ grating (h=260nm, t=50nm, f=0.7) on an air-matched 3J device at 60° aperture half-angle.
- schema:
  - `type`: text
  - `shape`: scalar
  - `unit`: mA/cm² per concentration

### improvement.txt
- path: `/app/outputs/improvement.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Improvement in total current loss (double-layer loss minus pyramid loss) at 60° aperture. Higher is better.
- schema:
  - `type`: text
  - `shape`: scalar
  - `unit`: mA/cm² per concentration

Notes: The primary scored artifact is the improvement; the two individual loss files serve as consistency checks. The checker will verify that the improvement is positive, that the loss values are within plausible bounds, and that improvement = double_loss - pyramid_loss.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "double_layer_current_loss.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "shape": "scalar",
        "unit": "mA/cm² per concentration"
      },
      "description": "Total current loss for the optimized double-layer MgF₂/ZnS ARC (124nm/70nm) on an air-matched 3J device at 60° aperture half-angle."
    },
    {
      "file": "pyramid_current_loss.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text",
        "shape": "scalar",
        "unit": "mA/cm² per concentration"
      },
      "description": "Total current loss for the 2D pyramidal TiO₂ grating (h=260nm, t=50nm, f=0.7) on an air-matched 3J device at 60° aperture half-angle."
    },
    {
      "file": "improvement.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "shape": "scalar",
        "unit": "mA/cm² per concentration"
      },
      "description": "Improvement in total current loss (double-layer loss minus pyramid loss) at 60° aperture. Higher is better."
    }
  ],
  "notes": "The primary scored artifact is the improvement; the two individual loss files serve as consistency checks. The checker will verify that the improvement is positive, that the loss values are within plausible bounds, and that improvement = double_loss - pyramid_loss."
}
```

## How you are scored
A hidden verifier reads your three output files. It first ensures that the reported improvement equals (double-layer loss) − (grating loss) within numerical precision, and that the two individual current loss values lie within a physically plausible range. Then it compares your computed improvement to a hidden reference improvement derived from the original work, using a tolerance that accommodates differences arising from re‑implementation (e.g., discretization, numerical libraries). A larger improvement (greater reduction in reflection loss) is better; the score degrades as the improvement falls below the reference. The two separate loss files provide consistency checks that also contribute to the final reward. The overall score is a weighted combination of these assessments.
