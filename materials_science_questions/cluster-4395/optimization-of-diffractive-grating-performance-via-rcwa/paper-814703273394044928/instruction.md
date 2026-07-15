# Spectral Efficiency of Blazed Grating Emitter via FDTD Simulation

## Problem background
Solar thermophotovoltaic (STPV) systems boost solar conversion efficiency by using a selective emitter to convert broad solar radiation into narrowband thermal radiation matched to a photovoltaic cell's bandgap. The emitter's spectral selectivity is critical: it should absorb sunlight across the visible and near-infrared while maintaining high reflectance (low emittance) in the mid-infrared to suppress unusable sub-bandgap emission. Tungsten is an attractive emitter material due to its high melting point and favorable infrared reflectance. However, bare tungsten's reflectance is not optimal; surface texturing with a blazed grating creates a graded-index anti-reflection effect that can broaden visible/near-infrared absorption while preserving high infrared reflectance, promising higher spectral efficiency.

## Approach
We model the emitter using finite-difference time-domain (FDTD) simulations with an open-source solver. The structure is a blazed grating on a 1 µm tungsten substrate: period 200 nm, height 285 nm, blaze angle 55°. Bloch periodic boundary conditions are applied laterally, and perfectly matched layers (PML) vertically to absorb outgoing radiation. The optical response of tungsten is described by a Drude-plus-multiple-Lorentzian dielectric function (room-temperature constants). To approximate unpolarized light, we compute the reflectance separately for P- and S-polarized incident plane waves and average them. Two configurations are simulated: (1) the grating on the substrate alone, and (2) the same geometry with a perfect electric conductor (PEC) back reflector placed behind the substrate. For each, we record the reflectance spectrum over the wavelength range 0.3–5 µm, which covers the region relevant for solar absorption and thermal emission at STPV operating temperatures.

## Reproduction target
Produce two CSV files containing the wavelength-resolved reflectance of the described blazed tungsten grating: one without a back reflector and one with a perfect back reflector. Each file must list wavelengths in micrometers and the corresponding total reflectance (dimensionless) averaged over polarization. The wavelength range must span at least 0.3–5 µm with sufficient resolution to capture the spectral features. From these reflectance spectra, a hidden verifier will compute the spectral efficiency—the fraction of emitted thermal radiation that can be converted by a GaSb photovoltaic cell at 1750 K—by numerically integrating the emittance (1−reflectance) against the Planck blackbody spectrum, weighted by photon energy, over wavelengths up to the cell bandgap (1707 nm). Your goal is to produce reflectance data that, under this independent calculation, yields a spectral efficiency consistent with a well-designed blazed grating emitter.

## Assets

- MEEP (MIT Electromagnetic Equation Propagation): https://meep.readthedocs.io/en/latest/
- Tungsten Drude+Lorentz parameters: 10.1063/1.475695

## Workflow steps

### Step 1: Simulate blazed grating without back reflector
- Role: scored (load-bearing)
- Action: Set up FDTD simulation for a blazed grating on a 1 µm tungsten substrate (period 200 nm, height 285 nm, blaze angle 55°). Use Bloch periodic boundaries laterally, PML vertically. Model tungsten dielectric function with a Drude+Lorentzian fit. Average P- and S-polarized reflectance to approximate unpolarized light. Simulate the reflectance spectrum over the wavelength range required for the spectral efficiency integral (0.3–5 µm).
- Output file: `/app/outputs/reflectance_no_back_reflector.csv`
- Format: csv
- Contract: wavelength_um (float), reflectance (float)
- Scoring: scored by hidden verifier

### Step 2: Simulate blazed grating with perfect back reflector
- Role: scored (load-bearing)
- Action: Repeat the same FDTD simulation as Step 1 but place a perfect electric conductor (PEC) back reflector behind the 1 µm tungsten substrate. Record the reflectance spectrum over 0.3–5 µm.
- Output file: `/app/outputs/reflectance_with_back_reflector.csv`
- Format: csv
- Contract: wavelength_um (float), reflectance (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reflectance_no_back_reflector.csv`
- `/app/outputs/reflectance_with_back_reflector.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reflectance_no_back_reflector.csv
- path: `/app/outputs/reflectance_no_back_reflector.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Reflectance spectrum of the blazed grating without back reflector, used to compute spectral efficiency.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`, `reflectance`
  - `units`:
    - `wavelength_um`: micrometers
    - `reflectance`: dimensionless

### reflectance_with_back_reflector.csv
- path: `/app/outputs/reflectance_with_back_reflector.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Reflectance spectrum of the blazed grating with a perfect back reflector, used to compute spectral efficiency.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`, `reflectance`
  - `units`:
    - `wavelength_um`: micrometers
    - `reflectance`: dimensionless

Notes: The hidden checker will recompute spectral efficiency from each reflectance spectrum using Eq. (1) (Planck's law at 1750 K, GaSb bandgap 0.726 eV) and compare against threshold_or_better criteria.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reflectance_no_back_reflector.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um",
          "reflectance"
        ],
        "units": {
          "wavelength_um": "micrometers",
          "reflectance": "dimensionless"
        }
      },
      "description": "Reflectance spectrum of the blazed grating without back reflector, used to compute spectral efficiency."
    },
    {
      "file": "reflectance_with_back_reflector.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um",
          "reflectance"
        ],
        "units": {
          "wavelength_um": "micrometers",
          "reflectance": "dimensionless"
        }
      },
      "description": "Reflectance spectrum of the blazed grating with a perfect back reflector, used to compute spectral efficiency."
    }
  ],
  "notes": "The hidden checker will recompute spectral efficiency from each reflectance spectrum using Eq. (1) (Planck's law at 1750 K, GaSb bandgap 0.726 eV) and compare against threshold_or_better criteria."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier. Each of the two reflectance files is evaluated independently. For each configuration, the verifier computes the spectral efficiency from your reflectance data as described above and compares it to a reference value. If your computed efficiency meets or exceeds the reference (within a small tolerance), that stage earns full credit; if it falls short, you receive partial credit proportional to the shortfall, down to zero for very poor efficiency. The two stages are weighted equally (each contributes 0.5 to the total reward). Additionally, the verifier checks that the efficiency without a back reflector is lower than with a back reflector, as expected physically; violation of this ordering may reduce the reward. Reporting the correct numbers is not enough—you must produce physically realistic reflectance spectra that, when fed into the efficiency calculation, yield the target performance.
