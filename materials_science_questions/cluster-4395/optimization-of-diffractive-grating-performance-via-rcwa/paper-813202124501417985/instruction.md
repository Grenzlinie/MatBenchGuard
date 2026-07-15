# RCWA Simulation of Ultrathin Metal Grating Absorbers for Wide-Angle Absorption

## Problem background
Thin-film solar cells must absorb sufficient sunlight to generate a high current, yet thinner active layers reduce carrier collection distances. A structure consisting of a thin amorphous silicon (a-Si) film sandwiched between a top metal grating and a back metal reflector aims to overcome this trade-off by coupling incident light into leaky modes with flat dispersion, potentially enabling broadband, polarization-insensitive absorption even at very high incidence angles. This task asks you to numerically investigate the optical absorption properties of such a structure and quantify its performance as a solar absorber.

## Approach
You will use rigorous coupled-wave analysis (RCWA) to simulate the optical response of planar and grating-based absorbers. First, you will study a planar reference structure (Ag/a-Si/Ag) to identify the resonant leaky mode and its dispersion character. Then you will extend to 1D silver grating configurations with fixed period and fill factor, testing both a thick grating and an ultrathin grating. For each grating structure, you will separate the absorption into a-Si and metal contributions by integrating the time-averaged power density. Finally, you will weight the a-Si absorption with the AM1.5G solar spectrum to extract net absorption efficiency and short-circuit current density (Jsc), and you will sweep the angle of incidence to characterize angle-invariant behavior.

## Reproduction target
Determine the net absorption efficiency (a-Si only) and short-circuit current density (Jsc) for TM and TE polarizations in both an ultrathin (d_Grat=0.01 μm) and a thick (d_Grat=0.1 μm) top grating structure, using RCWA simulations with the AM1.5G solar spectrum. Also, find the resonant absorption peak wavelength and bandwidth of the planar absorber (top Ag 0.01 μm, a-Si 0.03 μm), and examine the angle dependence of the ultrathin grating up to 80° incidence to assess absorption magnitude and peak wavelength stability.

## Assets

- Optical constants of Ag and a-Si (Palik): https://refractiveindex.info/?shelf=main&book=Ag&page=Johnson
- RCWA simulation tool (e.g., S4 or Python rcwa): https://github.com/ilyakava/s4-python
- AM1.5G solar spectrum (ASTM G173-03): https://www.nrel.gov/grid/solar-resource/spectra-astm-e490.html

## Workflow steps

### Step 1: Simulate planar absorber absorption at normal incidence
- Role: scored
- Action: Run RCWA simulation for an Ag/a-Si/Ag planar stack (top Ag thickness 0.01 μm, a-Si thickness 0.03 μm, semi-infinite bottom Ag) at normal incidence for TM and TE polarizations, wavelength range 0.3–0.9 μm. Compute absorption efficiency as (1 - reflection). Identify the main absorption peak wavelength and its full-width at half-maximum (FWHM).
- Output file: `/app/outputs/flat_film_peak.json`
- Format: json
- Contract: peak_wavelength_nm: number, fwhm_nm: number
- Scoring: scored by hidden verifier

### Step 2: Simulate grating structures at normal incidence and partition absorption
- Role: process
- Action: Run RCWA for grating structures with period P=0.4 μm, fill factor F=0.5, a-Si thickness 0.03 μm, for top grating thicknesses d_Grat=0.01 μm (ultrathin) and d_Grat=0.1 μm (thick) at normal incidence, TM and TE polarizations, wavelength 0.3–0.9 μm. From the full electromagnetic field, compute the power absorbed in a-Si and metal regions separately using time-average power density integration. Save the a-Si and metal absorption spectra per configuration.
- Evidence: `/app/outputs/grating_absorption_spectra.csv`

### Step 3: Compute net absorption efficiency and short-circuit current density
- Role: scored (load-bearing)
- Action: Using the a-Si absorption spectra from Step 2 and the AM1.5G standard solar spectrum, compute net absorption efficiency (integrated weighted absorption) and short-circuit current density Jsc = e * ∫ (λ/(h c)) S(λ) a(λ) dλ, for each grating configuration (thick/ultrathin) and polarization (TM/TE). Output the values in a CSV file.
- Output file: `/app/outputs/net_absorption_Jsc.csv`
- Format: csv
- Contract: columns: configuration (string: thick_grating, ultrathin_grating), polarization (string: TM, TE), net_absorption_total (float), net_absorption_Ag (float), net_absorption_aSi (float), Jsc_mA_cm2 (float)
- Scoring: scored by hidden verifier

### Step 4: Simulate ultrathin grating angle-dependent absorption
- Role: scored
- Action: Run RCWA for the ultrathin grating structure (d_Grat=0.01 μm) for incident angles from 0° to 80° in steps of e.g., 10°, TM and TE polarizations, wavelength 0.3–0.9 μm. For each angle and polarization, compute the total absorption spectrum and extract the peak wavelength and the maximum absorption value. Record these in a JSON file.
- Output file: `/app/outputs/angle_dependence.json`
- Format: json
- Contract: ultrathin_TM: array of {angle_deg, peak_wavelength_nm, max_absorption}; ultrathin_TE: similar
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/flat_film_peak.json`
- `/app/outputs/net_absorption_Jsc.csv`
- `/app/outputs/angle_dependence.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### flat_film_peak.json
- path: `/app/outputs/flat_film_peak.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Resonant absorption peak wavelength and bandwidth of the planar absorber.
- schema:
  - `required`: `peak_wavelength_nm`, `fwhm_nm`
  - `properties`:
    - `peak_wavelength_nm`:
      - `type`: number
      - `unit`: nm
    - `fwhm_nm`:
      - `type`: number
      - `unit`: nm

### net_absorption_Jsc.csv
- path: `/app/outputs/net_absorption_Jsc.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Net absorption efficiencies and short-circuit current density for thick and ultrathin grating configurations at normal incidence.
- schema:
  - `required_columns`: `configuration`, `polarization`, `net_absorption_total`, `net_absorption_Ag`, `net_absorption_aSi`, `Jsc_mA_cm2`
  - `column_types`:
    - `configuration`: string
    - `polarization`: string
    - `net_absorption_total`: float
    - `net_absorption_Ag`: float
    - `net_absorption_aSi`: float
    - `Jsc_mA_cm2`: float
  - `units`:
    - `net_absorption_total`: dimensionless
    - `net_absorption_Ag`: dimensionless
    - `net_absorption_aSi`: dimensionless
    - `Jsc_mA_cm2`: mA/cm^2

### angle_dependence.json
- path: `/app/outputs/angle_dependence.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Angle-dependent peak positions and maximum absorption for the ultrathin grating, used to verify peak wavelength invariance and TM threshold.
- schema:
  - `required_keys`: `ultrathin_TM`, `ultrathin_TE`
  - `array_schema`:
    - `type`: array
    - `items`:
      - `required`: `angle_deg`, `peak_wavelength_nm`, `max_absorption`
      - `properties`:
        - `angle_deg`:
          - `type`: number
          - `unit`: deg
        - `peak_wavelength_nm`:
          - `type`: number
          - `unit`: nm
        - `max_absorption`:
          - `type`: number
          - `unit`: dimensionless

Notes: All outputs are derived from RCWA simulations using public optical constants and the AM1.5G spectrum. The flat film peak is checked against a fixed target; net absorption/Jsc use threshold-or-better policy; the angle dependence checks structural invariance and absorption threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "flat_film_peak.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "required": [
          "peak_wavelength_nm",
          "fwhm_nm"
        ],
        "properties": {
          "peak_wavelength_nm": {
            "type": "number",
            "unit": "nm"
          },
          "fwhm_nm": {
            "type": "number",
            "unit": "nm"
          }
        }
      },
      "description": "Resonant absorption peak wavelength and bandwidth of the planar absorber."
    },
    {
      "file": "net_absorption_Jsc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "required_columns": [
          "configuration",
          "polarization",
          "net_absorption_total",
          "net_absorption_Ag",
          "net_absorption_aSi",
          "Jsc_mA_cm2"
        ],
        "column_types": {
          "configuration": "string",
          "polarization": "string",
          "net_absorption_total": "float",
          "net_absorption_Ag": "float",
          "net_absorption_aSi": "float",
          "Jsc_mA_cm2": "float"
        },
        "units": {
          "net_absorption_total": "dimensionless",
          "net_absorption_Ag": "dimensionless",
          "net_absorption_aSi": "dimensionless",
          "Jsc_mA_cm2": "mA/cm^2"
        }
      },
      "description": "Net absorption efficiencies and short-circuit current density for thick and ultrathin grating configurations at normal incidence."
    },
    {
      "file": "angle_dependence.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "required_keys": [
          "ultrathin_TM",
          "ultrathin_TE"
        ],
        "array_schema": {
          "type": "array",
          "items": {
            "required": [
              "angle_deg",
              "peak_wavelength_nm",
              "max_absorption"
            ],
            "properties": {
              "angle_deg": {
                "type": "number",
                "unit": "deg"
              },
              "peak_wavelength_nm": {
                "type": "number",
                "unit": "nm"
              },
              "max_absorption": {
                "type": "number",
                "unit": "dimensionless"
              }
            }
          }
        }
      },
      "description": "Angle-dependent peak positions and maximum absorption for the ultrathin grating, used to verify peak wavelength invariance and TM threshold."
    }
  ],
  "notes": "All outputs are derived from RCWA simulations using public optical constants and the AM1.5G spectrum. The flat film peak is checked against a fixed target; net absorption/Jsc use threshold-or-better policy; the angle dependence checks structural invariance and absorption threshold."
}
```

## How you are scored
Each scored artifact (flat film peak, net absorption/Jsc table, angle dependence) is independently evaluated by a hidden verifier. The verifier compares your computed quantities to reference values (or checks structural trends such as peak invariance) with appropriate tolerances. The scores are weighted and combined into a single reward between 0 and 1. Simply printing expected numbers without running the required simulations will not pass the scoring checks.
