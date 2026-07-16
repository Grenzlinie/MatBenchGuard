# Simulation of Bottom-Side-Coupled Apodized Grating Coupler Efficiency on Low-Index-Contrast Platform

## Problem background
Grating couplers are a critical interface for fiber-to-chip coupling in integrated photonic circuits. On the aluminum-nitride (AlN) on sapphire platform, the relatively low refractive-index contrast between AlN (n≈2.1) and sapphire (n≈1.74) historically limits the achievable transmission efficiency. This work introduces a bottom-side coupling scheme that places a metal reflector on the top side of the chip, directing the majority of the scattered light downward toward a fiber array attached under the sapphire substrate. The task is to computationally reproduce the key numerical predictions that validate this design: the downward scattering power ratio as a function of wavelength, the resulting per-coupler transmission efficiency for both TM and TE polarizations, and the fundamental coupling-efficiency upper bound imposed by the mode overlap between a Gaussian fiber mode and an exponential scattered field profile. All geometry and material parameters are fully specified, and the reproduction uses an open-source FDTD solver, allowing the entire simulation pipeline to be executed and verified.

## Approach
The grating coupler is built from a 1 µm AlN film, etched to a depth of 400 nm, on a 430 µm thick double-side polished sapphire substrate. A 2.7 µm SiO2 cladding covers the grating, and a 100 nm Nb metal reflector is placed on top. Light from an on‑chip waveguide is scattered by the apodized grating and directed downward through the sapphire substrate. A fiber mode (Gaussian beam with 5.2 µm waist) propagates through the substrate and an air gap to the grating plane, where its spot diameter expands significantly.
Two‑dimensional FDTD simulations are performed for TM polarization, launching the TM0 waveguide mode. A monitor plane is placed 3 µm below the AlN film. Simulations are run both without and with the metal reflector, recording the fraction of total power that reaches the monitor plane as a function of wavelength, yielding the downward scattering power ratio.
To design the apodized grating, the grating period and fill factor are varied spatially to focus the scattered field onto the fiber mode. The fill factor tapers linearly from 0.85 at the beginning of the grating to 0.70 over 30 µm and stays constant afterward. The grating periods are adjusted using a phase‑compensation method to imprint a focusing phase profile centered at an optimized position, based on the effective indices of the waveguide and the diffraction angle (12°).
After the FDTD simulation, the scattered field amplitude distribution at the monitor plane is extracted. The per‑coupler transmission efficiency is then computed from the overlap integral between this scattered field and the propagated Gaussian fiber mode, evaluated for both TM and TE polarizations. The peak efficiency and the corresponding wavelength are reported.
Finally, an analytic mode‑overlap integral is evaluated between a pure Gaussian profile (representing the fiber mode) and an exponential profile (representing the typical scattered field shape from a low‑index‑contrast grating). This yields a theoretical upper bound on the coupling efficiency that cannot be exceeded without modifying the field profile itself.

## Reproduction target
Produce three standalone artifacts:
1. A CSV file (`downward_power_ratio.csv`) containing the downward scattering power ratio (a dimensionless fraction between 0 and 1) as a function of wavelength (nm). The file must have columns: `wavelength_nm`, `power_ratio_without_reflector`, `power_ratio_with_reflector`. Data should cover wavelengths around the telecom C‑band (~1550 nm) and must reflect the TM0 waveguide mode simulation with and without the metal reflector.
2. A JSON file (`coupling_efficiency.json`) with two keys, `TM` and `TE`. Each key contains an object with `peak_efficiency` (float, 0–1) and `peak_wavelength_nm` (float). These values are obtained from the overlap integral between the scattered field at the monitor plane and the propagated Gaussian fiber mode (waist 5.2 µm, effective propagation path ~567 µm).
3. A plain text file (`mode_overlap_upper_bound.txt`) containing a single decimal number (float between 0 and 1) that is the analytic upper bound of coupling efficiency computed from the Gaussian–exponential mode overlap.

## Assets

- Meep FDTD solver: https://github.com/NanoComp/meep
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Prepare grating geometry and fiber mode model
- Role: process
- Action: Compile the layer structure and material indices; compute the fiber Gaussian mode expansion through the sapphire substrate and air gap to obtain the spot diameter at the grating plane; design the apodized grating periods and fill factors using the equations provided in the paper (target diffraction angle 12°, fill factor taper 0.85→0.70, optimized phase center xc=43 µm).
- Evidence: `/app/outputs/grating_design.json`

### Step 2: Simulate downward scattering power ratio
- Role: scored
- Action: Run 2D FDTD simulations of the grating coupler for TM polarization, first without and then with the top metal reflector, launching the TM0 waveguide mode. Monitor the power flow through the monitor plane placed 3 µm below the AlN film and record the fraction of power directed downward as a function of wavelength. Save the scattered field amplitude distribution at the monitor plane for subsequent overlap analysis.
- Output file: `/app/outputs/downward_power_ratio.csv`
- Format: csv
- Contract: wavelength_nm (float), power_ratio_without_reflector (float), power_ratio_with_reflector (float)
- Scoring: scored by hidden verifier

### Step 3: Compute coupling efficiency for TM and TE
- Role: scored (load-bearing)
- Action: Using the scattered field amplitude at the monitor plane obtained from the FDTD simulations, compute the overlap integral between the scattered field and the propagated Gaussian fiber mode (waist ω0=5.2 µm, effective propagation path ~567 µm) for both TM and TE polarizations. Determine the peak coupling efficiency and the corresponding wavelength for each polarization, and report them.
- Output file: `/app/outputs/coupling_efficiency.json`
- Format: json
- Contract: { "TM": { "peak_efficiency": <float>, "peak_wavelength_nm": <float> }, "TE": { "peak_efficiency": <float>, "peak_wavelength_nm": <float> } }
- Scoring: scored by hidden verifier

### Step 4: Compute theoretical coupling efficiency upper bound
- Role: scored
- Action: Analytically evaluate the mode-overlap integral between a Gaussian profile (fiber mode) and an exponential profile (scattered field shape from a low-index-contrast grating) to obtain the fundamental maximum achievable coupling efficiency.
- Output file: `/app/outputs/mode_overlap_upper_bound.txt`
- Format: txt
- Contract: Single float value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/downward_power_ratio.csv`
- `/app/outputs/coupling_efficiency.json`
- `/app/outputs/mode_overlap_upper_bound.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### downward_power_ratio.csv
- path: `/app/outputs/downward_power_ratio.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Simulated downward power ratio vs wavelength; the checker will extract the maximum ratio with reflector and without reflector and compare to expected thresholds.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `power_ratio_without_reflector`, `power_ratio_with_reflector`
  - `units`:
    - `wavelength_nm`: nm
    - `power_ratio_without_reflector`: dimensionless fraction
    - `power_ratio_with_reflector`: dimensionless fraction

### coupling_efficiency.json
- path: `/app/outputs/coupling_efficiency.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Peak coupling efficiency (from overlap integral) for TM and TE polarizations, together with the 3 dB misalignment tolerance width derived from the same scattered-field overlap. The checker verifies these values meet or exceed the reference within tolerances.
- schema:
  - `type`: object
  - `required`: `TM`, `TE`, `tolerance_3dB_um`
  - `items`:
    - `TM`:
      - `peak_efficiency`: float (0-1)
      - `peak_wavelength_nm`: float
    - `TE`:
      - `peak_efficiency`: float (0-1)
      - `peak_wavelength_nm`: float
    - `tolerance_3dB_um`: float (µm)

### mode_overlap_upper_bound.txt
- path: `/app/outputs/mode_overlap_upper_bound.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Analytic theoretical upper bound on coupling efficiency; the checker compares this value to the known bound (~0.80) within a tolerance.
- schema:
  - `type`: text
  - `description`: A single decimal number (float) representing the computed Gaussian–exponential overlap efficiency bound.

Notes: The downward power ratio CSV must contain data for wavelengths near 1550 nm. The coupling efficiency JSON now also includes the misalignment tolerance 3 dB width, computed from the same overlap integral, so a separate file is not needed. The overlap bound must be computed analytically, not copied from a pre-known constant.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "downward_power_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "power_ratio_without_reflector",
          "power_ratio_with_reflector"
        ],
        "units": {
          "wavelength_nm": "nm",
          "power_ratio_without_reflector": "dimensionless fraction",
          "power_ratio_with_reflector": "dimensionless fraction"
        }
      },
      "description": "Simulated downward power ratio vs wavelength; the checker will extract the maximum ratio with reflector and without reflector and compare to expected thresholds."
    },
    {
      "file": "coupling_efficiency.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "TM",
          "TE",
          "tolerance_3dB_um"
        ],
        "items": {
          "TM": {
            "peak_efficiency": "float (0-1)",
            "peak_wavelength_nm": "float"
          },
          "TE": {
            "peak_efficiency": "float (0-1)",
            "peak_wavelength_nm": "float"
          },
          "tolerance_3dB_um": "float (µm)"
        }
      },
      "description": "Peak coupling efficiency (from overlap integral) for TM and TE polarizations, together with the 3 dB misalignment tolerance width derived from the same scattered-field overlap. The checker verifies these values meet or exceed the reference within tolerances."
    },
    {
      "file": "mode_overlap_upper_bound.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single decimal number (float) representing the computed Gaussian–exponential overlap efficiency bound."
      },
      "description": "Analytic theoretical upper bound on coupling efficiency; the checker compares this value to the known bound (~0.80) within a tolerance."
    }
  ],
  "notes": "The downward power ratio CSV must contain data for wavelengths near 1550 nm. The coupling efficiency JSON now also includes the misalignment tolerance 3 dB width, computed from the same overlap integral, so a separate file is not needed. The overlap bound must be computed analytically, not copied from a pre-known constant."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier that independently examines each output file. For every scored stage, the verifier reads your file, checks its structure, and compares the extracted numerical values against reference criteria using predefined thresholds. A result that meets or exceeds the expected threshold earns full credit for that stage; results that fall short receive proportionally lower credit. The stages are combined with weights that together sum to 1.0, and the final reward is a single floating‑point number between 0 and 1. To succeed, you must faithfully implement the described methodology, but you are not required to hit any specific published number exactly. The verifier’s reference values and tolerances are designed to account for the expected variability between different open‑source and commercial FDTD implementations.
