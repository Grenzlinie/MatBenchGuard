# RCWA Simulation of Concentric Circular Grating Filters

## Problem background
Concentric circular grating filters (CCGFs) are a variant of guided-mode resonance (GMR) filters that offer polarization-insensitive operation under normal incidence due to their rotational symmetry. Unlike traditional 1‑D linear grating filters, which usually produce a single resonance per polarization, CCGFs feature a couple of resonant peaks because each local point on the grating simultaneously receives azimuthal and radial electric field components, each coupling to a different guided mode. The CCGFs investigated here are built on an HfO₂‑on‑silicon platform and are simulated indirectly via a 1‑D linear grating analog, avoiding the need for expensive three‑dimensional computations.

## Approach
The CCGF reflection spectrum is approximated by the equal‑weight average of the TE and TM zeroth‑order reflectivities of a 1‑D linear grating that shares identical layer structure and material parameters. For each CCGF design, construct the linear grating with the specified period Λ, filling factor η, grating thickness Tg, waveguide thickness Tw, and HfO₂ refractive index (1.95), surrounded by air (n=1). Using an open‑source rigorous coupled‑wave analysis (RCWA) solver, compute the reflectivity for TE polarization (electric field parallel to the grating bars; simulates the azimuthal component) and TM polarization (electric field perpendicular; simulates the radial component) over the wavelength range 550‑800 nm at normal incidence. Average the two spectra pointwise to obtain the CCGF reflection spectrum. From the averaged spectrum, identify the resonant peaks (local maxima) and extract each peak’s central wavelength, peak reflectivity, and full‑width at half‑maximum (FWHM). The procedure is carried out for two different grating designs (CCGF‑I and CCGF‑II) that differ in filling factor and period.

## Reproduction target
Produce the zeroth‑order reflection spectra for CCGF‑I and CCGF‑II over the wavelength range 550‑800 nm by performing RCWA on the 1‑D linear analog and averaging the TE and TM contributions. Output the combined spectra as CSV files (cggf1_spectrum.csv and cggf2_spectrum.csv). From each spectrum, identify the two dominant reflection peaks and create a peak_summary.json file containing, for each peak, its label (A, B for CCGF‑I; C, D for CCGF‑II, in order of increasing wavelength), central wavelength, peak reflectivity, and FWHM.

## Assets

- RCWA solver (open-source)

## Workflow steps

### Step 1: RCWA simulation for TE polarization (azimuthal component)
- Role: process
- Action: Perform rigorous coupled-wave analysis (RCWA) on the 1-D linear grating analog under TE polarization for both CCGF-I and CCGF-II. Use the measured structure parameters: for CCGF-I, period Λ ≈ 448 nm, filling factor η ≈ 0.49, grating thickness Tg ≈ 70 nm, waveguide thickness Tw ≈ 130 nm; for CCGF-II, Λ ≈ 461 nm, η ≈ 0.71, Tg ≈ 70 nm, Tw ≈ 130 nm. The grating material is HfO₂ with refractive index 1.95, surrounded by air (n=1). Normal incidence. Scan wavelengths from 550 nm to 800 nm with fine resolution. Compute zeroth-order reflectivity spectra and store internally for later combination.
- Evidence: none

### Step 2: RCWA simulation for TM polarization (radial component)
- Role: process
- Action: Perform RCWA on the 1-D linear grating analog under TM polarization for both CCGF-I and CCGF-II, using the same structure parameters as in step_01. Normal incidence, wavelength range 550–800 nm. Compute zeroth-order reflectivity spectra and store internally.
- Evidence: none

### Step 3: Combine TE/TM spectra for CCGF-I and save reflection curve
- Role: scored
- Action: Average the TE and TM reflectivities for CCGF-I at each wavelength (equal weight, representing the 50/50 split of azimuthal and radial components). Write the resulting wavelength–reflectivity pairs to a CSV file sorted by ascending wavelength.
- Output file: `/app/outputs/cggf1_spectrum.csv`
- Format: csv
- Contract: Columns: wavelength_nm (float), reflectivity (float, 0-1). Rows sorted by ascending wavelength.
- Scoring: scored by hidden verifier

### Step 4: Combine TE/TM spectra for CCGF-II and save reflection curve
- Role: scored
- Action: Average the TE and TM reflectivities for CCGF-II at each wavelength (equal weight). Write the resulting wavelength–reflectivity pairs to a CSV file sorted by ascending wavelength.
- Output file: `/app/outputs/cggf2_spectrum.csv`
- Format: csv
- Contract: Columns: wavelength_nm (float), reflectivity (float, 0-1). Rows sorted by ascending wavelength.
- Scoring: scored by hidden verifier

### Step 5: Extract resonant peak parameters
- Role: scored (load-bearing)
- Action: From the combined spectra of step_03 and step_04, identify the two resonant reflection peaks for each CCGF design. For CCGF-I, label the peak at shorter wavelength 'A' and the one at longer wavelength 'B'. For CCGF-II, label them 'C' and 'D'. Determine the central wavelength (wavelength of maximum reflectivity), peak reflectivity, and full-width at half-maximum (FWHM) for each peak. Save the results in peak_summary.json.
- Output file: `/app/outputs/peak_summary.json`
- Format: json
- Contract: JSON object with keys 'ccgf1_peaks' and 'ccgf2_peaks'. Each key maps to an array of two peak objects. Each object has keys: peak_label (string), central_wavelength_nm (float), peak_reflectivity (float), FWHM_nm (float). Arrays sorted by increasing central_wavelength.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cggf1_spectrum.csv`
- `/app/outputs/cggf2_spectrum.csv`
- `/app/outputs/peak_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cggf1_spectrum.csv
- path: `/app/outputs/cggf1_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CCGF-I combined reflection spectrum (TE/TM average). Used for structural audit: wavelength monotonicity, two-peak shape, reflectivity in [0,1].
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `reflectivity`
  - `units`:
    - `wavelength_nm`: nm
    - `reflectivity`: dimensionless (0–1)

### cggf2_spectrum.csv
- path: `/app/outputs/cggf2_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CCGF-II combined reflection spectrum (TE/TM average). Used for structural audit.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `reflectivity`
  - `units`:
    - `wavelength_nm`: nm
    - `reflectivity`: dimensionless (0–1)

### peak_summary.json
- path: `/app/outputs/peak_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Peak parameters for both CCGFs. Checked against paper-reported simulated values (hidden reference) with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `ccgf1_peaks`: array of two peak objects
    - `ccgf2_peaks`: array of two peak objects
  - `items`:
    - `peak_label`: string (A, B for ccgf1; C, D for ccgf2)
    - `central_wavelength_nm`: float, nm
    - `peak_reflectivity`: float
    - `FWHM_nm`: float, nm

Notes: The RCWA simulations are process steps; their intermediate arrays are not scored. The peak_summary.json is the main reproduction target. The combined spectra are also scored for structural validity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cggf1_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "reflectivity"
        ],
        "units": {
          "wavelength_nm": "nm",
          "reflectivity": "dimensionless (0–1)"
        }
      },
      "description": "CCGF-I combined reflection spectrum (TE/TM average). Used for structural audit: wavelength monotonicity, two-peak shape, reflectivity in [0,1]."
    },
    {
      "file": "cggf2_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "reflectivity"
        ],
        "units": {
          "wavelength_nm": "nm",
          "reflectivity": "dimensionless (0–1)"
        }
      },
      "description": "CCGF-II combined reflection spectrum (TE/TM average). Used for structural audit."
    },
    {
      "file": "peak_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "ccgf1_peaks": "array of two peak objects",
          "ccgf2_peaks": "array of two peak objects"
        },
        "items": {
          "peak_label": "string (A, B for ccgf1; C, D for ccgf2)",
          "central_wavelength_nm": "float, nm",
          "peak_reflectivity": "float",
          "FWHM_nm": "float, nm"
        }
      },
      "description": "Peak parameters for both CCGFs. Checked against paper-reported simulated values (hidden reference) with tolerances."
    }
  ],
  "notes": "The RCWA simulations are process steps; their intermediate arrays are not scored. The peak_summary.json is the main reproduction target. The combined spectra are also scored for structural validity."
}
```

## How you are scored
A hidden verifier will independently evaluate your three output files and combine the per‑component scores into a final reward value between 0 and 1. The scoring first checks the structural validity of each reflection spectrum (e.g., wavelength axis is monotonic, reflectivity values are in [0,1], two identifiable peaks appear). More heavily weighted is the accuracy of the extracted peak parameters (central wavelength, peak reflectivity, FWHM) for each of the four peaks. The verifier compares your reported parameters against reference results using pre‑established tolerances. Simply printing a number is not sufficient; the verifier reads your submitted files and scores what you have actually computed.
