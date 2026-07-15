# Angle-Resolved Reflectance and Optical Impedance Matching of Plasmonic Perfect Absorbers

## Problem background
Plasmonic perfect absorbers consist of a resonant metallic nanostructure placed above a dielectric spacer and a metallic mirror, enabling near-unity absorbance at a designed wavelength. For practical applications, the angular independence of the absorptive performance is essential, but the physical reasons for angular dispersion in such structures have not been fully quantified. This task investigates the role of optical impedance matching in determining the angular behavior of plasmonic perfect absorbers. The key question is: does a perfect absorber that exhibits zero reflectance at normal incidence also maintain low reflectance over a broad angular range, and if not, which impedance parameters control the angular dispersion? The task addresses this by computing the complex optical impedance and angle-resolved reflectance for several absorber designs covering both visible and near-infrared wavelengths.

## Approach
The method combines rigorous coupled-wave analysis (RCWA) simulations of periodic array-based absorbers and a finite-difference time-domain (FDTD) simulation of a single absorber element. For each periodic design, the scattering matrix coefficient S11 at normal incidence is extracted, and the reflectance at p‑polarization is computed at incident angles of 0°, 20°, and 36°. The single-element simulation yields the local impedance of an isolated absorber, free from array grating effects. From S11, the complex optical impedance Z = Z' + iZ'' is calculated assuming zero transmission through the mirror. The impedance components are then compared to the vacuum values (Z' = 1, Z'' = 0) to assess the degree of impedance matching. The procedure is applied to four specific designs: (1) an Au nanodisk array absorber operating around 1480 nm, (2) a Pd wire absorber with large periodicity (450 nm) around 720 nm, (3) a Pd wire absorber with small periodicity (300 nm) around 690 nm, and (4) a disordered Au nanodisk absorber with single‑element properties. By correlating the computed impedance values with the angular reflectance traces, the approach tests whether matching both the real and the imaginary parts of the impedance is required for angle‑independent absorption.

## Reproduction target
The target is to produce a single CSV file, `impedance_and_reflectance.csv`, containing the following columns for each of the four designs: design_name, resonance_wavelength_nm, S11_amplitude, S11_phase_deg, Z_real, Z_imag, reflectance_0deg, reflectance_20deg, reflectance_36deg. For the disordered single‑element design, only the Z_real and Z_imag columns are required; the reflectance columns may be left empty. The CSV file provides the quantitative foundation for evaluating the impedance matching model.

## Assets

- S4 (Stanford Stratified Structure Solver): https://web.stanford.edu/group/fan/S4/
- MEEP: https://github.com/NanoComp/meep
- Optical constants of gold (Johnson and Christy, 1972): https://refractiveindex.info/?shelf=main&book=Au&page=Johnson
- Optical constants of palladium (Vargas et al., 2006): https://refractiveindex.info/?shelf=main&book=Pd&page=Vargas
- Refractive index of MgF2: https://refractiveindex.info/?shelf=main&book=MgF2&page=Dodge
- Refractive index of Al2O3: https://refractiveindex.info/?shelf=main&book=Al2O3&page=Malitson

## Workflow steps

### Step 1: RCWA simulation of Au nanodisk array perfect absorber
- Role: process
- Action: Using an open-source RCWA solver (e.g., S4), simulate the reflectance of the Au nanodisk/MgF₂/mirror structure (disk diameter 330 nm, period 600 nm, disk height 20 nm, spacer height 30 nm, mirror height 200 nm) for p-polarization at incident angles θ = 0°, 20°, 36°. Extract the scattering matrix coefficient S11(λ) at normal incidence and record the reflectance at the resonance wavelength (around 1480 nm).
- Evidence: `/app/outputs/au_absorber_reflectance_angles.json`

### Step 2: RCWA simulation of Pd wire absorber (period 450 nm)
- Role: process
- Action: Simulate the reflectance of the Pd wire/MgF₂/Au mirror structure (wire width 125 nm, period 450 nm, wire height 20 nm, MgF₂ spacer 50 nm, Au mirror 200 nm) for p-polarization at θ = 0°, 20°, 36°. Extract S11(λ) at normal incidence and the reflectance at the resonance wavelength (around 720 nm).
- Evidence: `/app/outputs/pd_large_reflectance_angles.json`

### Step 3: RCWA simulation of Pd wire absorber (period 300 nm)
- Role: process
- Action: Simulate the reflectance of the Pd wire/Al₂O₃/Au mirror structure (wire width 85 nm, period 300 nm, wire height 30 nm, Al₂O₃ spacer 35 nm, Au mirror 200 nm) for p-polarization at θ = 0°, 20°, 36°. Extract S11(λ) at normal incidence and the reflectance at the resonance wavelength (around 690 nm).
- Evidence: `/app/outputs/pd_small_reflectance_angles.json`

### Step 4: FDTD simulation of a single Au nanodisk absorber element
- Role: process
- Action: Use an open-source FDTD solver (MEEP) to model a single Au nanodisk (diameter 160 nm, height 20 nm) on a 40 nm MgF₂ spacer and a 120 nm Au mirror, with a cubic source enclosing the element. Extract the backward-scattered field amplitude and phase at normal incidence, correct for propagation phase, and compute S11. Then calculate the complex impedance Z from S11 (assuming S21=0).
- Evidence: `/app/outputs/single_au_impedance.json`

### Step 5: Compile impedance and reflectance results
- Role: scored (load-bearing)
- Action: Using the simulation outputs from the previous steps, extract the resonance wavelength, S11 amplitude and phase at that wavelength, compute Z using Z = sqrt(((1+S11)^2)/((1-S11)^2)), and record the reflectance values at 0°, 20°, and 36° at the resonance wavelength. Write all results into a single CSV file.
- Output file: `/app/outputs/impedance_and_reflectance.csv`
- Format: csv
- Contract: CSV with columns: design_name, resonance_wavelength_nm, S11_amplitude, S11_phase_deg, Z_real, Z_imag, reflectance_0deg, reflectance_20deg, reflectance_36deg. For the disordered design, only Z_real and Z_imag are required; reflectance angles may be left empty.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/impedance_and_reflectance.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### impedance_and_reflectance.csv
- path: `/app/outputs/impedance_and_reflectance.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV file containing the resonance wavelength, complex impedance, and angle-resolved reflectance for the four absorber designs. The checker recomputes impedance from S11 internally and verifies that the values meet the physical thresholds consistent with angle-independent or angle-dependent behavior.
- schema:
  - `type`: table
  - `required_columns`: `design_name`, `resonance_wavelength_nm`, `S11_amplitude`, `S11_phase_deg`, `Z_real`, `Z_imag`, `reflectance_0deg`, `reflectance_20deg`, `reflectance_36deg`
  - `columns`:
    - `design_name`:
      - `type`: string
    - `resonance_wavelength_nm`:
      - `type`: float
      - `unit`: nanometers
    - `S11_amplitude`:
      - `type`: float
      - `unit`: dimensionless
    - `S11_phase_deg`:
      - `type`: float
      - `unit`: degrees
    - `Z_real`:
      - `type`: float
      - `unit`: dimensionless
    - `Z_imag`:
      - `type`: float
      - `unit`: dimensionless
    - `reflectance_0deg`:
      - `type`: float
      - `unit`: dimensionless (0 to 1)
    - `reflectance_20deg`:
      - `type`: float
      - `unit`: dimensionless (0 to 1)
    - `reflectance_36deg`:
      - `type`: float
      - `unit`: dimensionless (0 to 1)

Notes: The disordered single-element design (compiled from the FDTD simulation) may leave reflectance angles empty; only Z_real and Z_imag are required for that row. The solving agent should use the provided geometries and public material data to run RCWA and FDTD simulations, then extract the quantities. The checker will confirm internal consistency of impedance and apply hidden threshold-based scoring.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "impedance_and_reflectance.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "design_name",
          "resonance_wavelength_nm",
          "S11_amplitude",
          "S11_phase_deg",
          "Z_real",
          "Z_imag",
          "reflectance_0deg",
          "reflectance_20deg",
          "reflectance_36deg"
        ],
        "columns": {
          "design_name": {
            "type": "string"
          },
          "resonance_wavelength_nm": {
            "type": "float",
            "unit": "nanometers"
          },
          "S11_amplitude": {
            "type": "float",
            "unit": "dimensionless"
          },
          "S11_phase_deg": {
            "type": "float",
            "unit": "degrees"
          },
          "Z_real": {
            "type": "float",
            "unit": "dimensionless"
          },
          "Z_imag": {
            "type": "float",
            "unit": "dimensionless"
          },
          "reflectance_0deg": {
            "type": "float",
            "unit": "dimensionless (0 to 1)"
          },
          "reflectance_20deg": {
            "type": "float",
            "unit": "dimensionless (0 to 1)"
          },
          "reflectance_36deg": {
            "type": "float",
            "unit": "dimensionless (0 to 1)"
          }
        }
      },
      "description": "CSV file containing the resonance wavelength, complex impedance, and angle-resolved reflectance for the four absorber designs. The checker recomputes impedance from S11 internally and verifies that the values meet the physical thresholds consistent with angle-independent or angle-dependent behavior."
    }
  ],
  "notes": "The disordered single-element design (compiled from the FDTD simulation) may leave reflectance angles empty; only Z_real and Z_imag are required for that row. The solving agent should use the provided geometries and public material data to run RCWA and FDTD simulations, then extract the quantities. The checker will confirm internal consistency of impedance and apply hidden threshold-based scoring."
}
```

## How you are scored
A hidden verifier parses your submitted CSV. It recomputes the impedance from the reported S11 amplitude and phase to confirm internal consistency. It then compares the real and imaginary parts of the impedance and the angle‑resolved reflectances against hidden reference values that represent the correct computational results. The scoring is design‑specific and checks whether the impedance components and reflectance levels satisfy threshold criteria consistent with the physical behavior of angle‑independent versus angle‑dependent absorbers. Your final reward is a weighted sum of scores from all scored stages. You are not given the reference values or tolerances; the task is to run the specified simulations and extract the quantities accurately from your own computed results.
