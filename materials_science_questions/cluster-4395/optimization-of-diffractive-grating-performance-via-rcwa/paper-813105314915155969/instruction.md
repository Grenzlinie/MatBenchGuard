# Thermal Emission Angular Dispersion Reduction via Graphene-Bundle Grating Design

## Problem background
Thermal radiation from a hot SiC surface grating is inherently angularly dispersive—each wavelength emits at a different angle—because of two factors: the rapid material dispersion of the surface phonon polaritons (SPhPs) on SiC, and the misalignment of the grating's diffraction dispersion curve relative to the light line. As a result, practical thermal emitters based on polar materials either exhibit wideband-dispersive emission (broad overall angular spread) or narrowband-directive emission (only one wavelength well collimated). Reducing the angular dispersion would enable wideband-directive sources useful for spectroscopy, thermophotovoltaics, and mid-infrared imaging. The problem studied here is whether inserting a bundled graphene layer between the SiC substrate and a surface diffraction grating can compensate the SPhP material dispersion and, together with a carefully chosen grating period, bring the emission dispersion curve into alignment, thereby drastically narrowing the angular spread of thermal radiation in the 11–12 μm wavelength range.

## Approach
The reproduction implements a modified rigorous coupled wave analysis (RCWA) for transverse magnetic (TM) polarization to treat graphene sheets as zero-thickness conducting boundaries. The composite structure consists of a SiC substrate modeled by a Lorentz permittivity (phonon resonances), a bundle of 30 graphene sheets separated by 10‑nm dielectric spacer layers (ε = 2.25), and a top Si diffraction grating (ε = 12.1, period Λ = 37.51 µm, height 235 nm, duty cycle 39%). Within each homogeneous or grating layer, RCWA eigenmodes are computed; graphene interfaces are incorporated via boundary conditions that introduce a Toeplitz matrix of the surface conductivity (Kubo model, Fermi level 0.7 eV, scattering time 200 fs, temperature 315 K). The emissivity for each wavelength (11–12 µm, step ~0.01 µm) and each emission angle (covering at least the directional peak, e.g. −90° to 90° with ~0.5° step) is obtained as 1 minus the total reflected power summed over all propagating diffraction orders. No external dataset is required—the procedure is the experiment: all material models and geometry parameters are public, and the simulation produces the required angle‑ and frequency‑resolved emissivity directly from first principles.

## Reproduction target
Simulate the SiC/graphene‑bundle/Si‑grating composite structure using the described modified RCWA method and produce two artifacts under `/app/outputs`:
1. `emissivity_data.csv` — a matrix giving the TM‑polarized emissivity (values in [0,1]) on a uniform grid of wavelengths (11.0–12.0 µm in steps of ~0.01 µm) and emission angles (covering at least the directional peak, e.g. −90° to 90° in steps of ~0.5°). The first column must be `wavelength_um`, and subsequent columns should be named `angle_{deg}` for each angle.
2. `angular_dispersion.txt` — a single floating‑point number representing the angular dispersion Δθ (in degrees), computed from the emissivity matrix as the maximum full width at half maximum (FWHM) of the emissivity angular profile over the wavelength range 11–12 µm. The FWHM is defined as the angular span where emissivity ≥ half of the peak emissivity at that wavelength.
The target is to produce a physically plausible emissivity matrix that, when processed by the same FWHM protocol, yields a Δθ consistent with the paper's narrow‑dispersion claim. No gold value is provided here; the verifier independently recomputes Δθ from the raw emissivity data and compares it against a hidden reference.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Material parameter generation
- Role: process
- Action: Compute wavelength-dependent material properties for 11–12 μm: SiC complex permittivity from Lorentz model (high-frequency permittivity, TO/LO phonon frequencies, damping), graphene surface conductivity from Kubo formula (Fermi level 0.7 eV, scattering time 200 fs, temperature 315 K), and spacer permittivity (ε=2.25). Save to material_properties.csv.
- Evidence: `/app/outputs/material_properties.csv`

### Step 2: RCWA simulation of composite structure
- Role: scored (load-bearing)
- Action: Implement the modified RCWA for TM-polarized light: treat graphene as zero-thickness conducting interfaces via Toeplitz matrices of surface conductivity. Stack: SiC substrate, 30 graphene sheets with 10 nm dielectric spacers (ε=2.25) forming a 300 nm bundle, Si grating (ε=12.1, period Λ=37.51 μm, height 235 nm, duty cycle 39%). Compute emissivity (1 − total reflected power) over wavelengths 11–12 μm (step ~0.01 μm) and emission angles from -90° to 90° (step ~0.5°). Write the emissivity matrix to emissivity_data.csv.
- Output file: `/app/outputs/emissivity_data.csv`
- Format: csv
- Contract: CSV. First column: wavelength_um (float). Subsequent columns: angle_{deg} (e.g., angle_-90, angle_-89.5, ...), values emissivity (float in [0,1]). One row per wavelength. Grid uniform.
- Scoring: scored by hidden verifier

### Step 3: Angular dispersion analysis
- Role: scored
- Action: From emissivity_data.csv, for each wavelength locate the angle of peak emissivity, determine the angular span where emissivity ≥ half of that peak (FWHM), then compute the maximum FWHM across wavelengths as the angular dispersion Δθ. Write Δθ (in degrees) to angular_dispersion.txt.
- Output file: `/app/outputs/angular_dispersion.txt`
- Format: txt
- Contract: A single float value representing Δθ in degrees.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/emissivity_data.csv`
- `/app/outputs/angular_dispersion.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### emissivity_data.csv
- path: `/app/outputs/emissivity_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw angle- and frequency-resolved emissivity matrix. The checker recomputes angular dispersion Δθ from this data and compares to the paper's reference value.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`
  - `description`: Columns: wavelength_um (float); one column per angle from -90 to 90 deg in 0.5 deg steps, named angle_{deg} (e.g., angle_-90, angle_-89.5, ...), values float emissivity in [0,1]. One row per wavelength.
  - `units`:
    - `wavelength_um`: micron
    - `emissivity`: dimensionless

### angular_dispersion.txt
- path: `/app/outputs/angular_dispersion.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: The agent's computed angular dispersion Δθ; checked against a hidden golden threshold.
- schema:
  - `type`: text
  - `description`: A single float value (in degrees) representing the maximum full-width half-maximum of the emissivity peak over 11–12 µm.

Notes: The checker will primarily recompute Δθ from emissivity_data.csv. angular_dispersion.txt provides a quick consistency check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "emissivity_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um"
        ],
        "description": "Columns: wavelength_um (float); one column per angle from -90 to 90 deg in 0.5 deg steps, named angle_{deg} (e.g., angle_-90, angle_-89.5, ...), values float emissivity in [0,1]. One row per wavelength.",
        "units": {
          "wavelength_um": "micron",
          "emissivity": "dimensionless"
        }
      },
      "description": "Raw angle- and frequency-resolved emissivity matrix. The checker recomputes angular dispersion Δθ from this data and compares to the paper's reference value."
    },
    {
      "file": "angular_dispersion.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "description": "A single float value (in degrees) representing the maximum full-width half-maximum of the emissivity peak over 11–12 µm."
      },
      "description": "The agent's computed angular dispersion Δθ; checked against a hidden golden threshold."
    }
  ],
  "notes": "The checker will primarily recompute Δθ from emissivity_data.csv. angular_dispersion.txt provides a quick consistency check."
}
```

## How you are scored
A hidden verifier reads your two output files and scores them as follows:
- **emissivity_data.csv (primary weight):** The verifier validates that the file is a complete grid with all required columns/rows, that all emissivity values are in [0,1], and that there are no missing entries. It then recomputes the angular dispersion Δθ from your raw data using the same peak‑finding and FWHM procedure described in Step 3. The recomputed Δθ is compared against a hidden reference dispersion value derived from the paper. Scoring uses a monotonic scheme: meeting or beating the reference dispersion earns full credit, and the score decreases as the dispersion gets worse (larger Δθ).
- **angular_dispersion.txt (secondary weight):** The verifier reads your reported Δθ and scores it as threshold‑or‑better against a hidden threshold. A reported Δθ at or below the threshold gives full credit; higher values receive progressively lower credit. This provides a quick consistency check but the main score comes from the recomputed metric.
The final reward is a weighted combination of these scores. Simply reporting a number is not sufficient—the raw emissivity matrix must be present, correctly structured, and must demonstrate the narrow angular dispersion when analyzed by the verifier.
