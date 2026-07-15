# Spectral Reflectance Simulation of Gaussian-Apodized Bragg Grating

## Problem background
Dense wavelength division multiplexing (DWDM) optical communication systems require narrow-band filters with high diffraction efficiency and strong suppression of spectral side lobes. Edge-illuminated holographic polymer Bragg gratings offer a planar geometry that enables long interaction lengths and facilitates apodization of the refractive index profile. A Gaussian apodization can dramatically reduce side-lobe levels, but it also shortens the effective grating length, so physically longer gratings are needed to achieve both narrow bandwidth and high reflectivity. Simulating the spectral response of such apodized gratings is essential for designing filters that meet the stringent DWDM specifications.

## Approach
The core simulation method is Rouard’s method, a transfer-matrix approach for stratified media. The grating is divided into many thin uniform layers, each with its own refractive index given by the apodized profile. For TE-polarized light at normal incidence, a 2×2 transfer matrix is constructed for each layer by computing the layer’s optical path length at the current wavelength. Multiplying the layer matrices yields the total transfer matrix of the grating, from which the reflectance at that wavelength is extracted. This computation is repeated over a fine wavelength grid covering the expected reflection band.

The required grating parameters are: physical length L = 14.0 mm, grating pitch Λ = 517 nm, average refractive index n_avg = 1.5, peak index modulation Δn_max = 1.5×10⁻⁴, and Gaussian apodization parameter ε = 9.0. The spatial dependence of the index modulation follows a Gaussian envelope: Δn(x) = Δn_max · exp[-ε (x/L)²], where x is the coordinate along the grating length from -L/2 to L/2. The background refractive index is constant n_avg, so the local refractive index is n(x) = n_avg + Δn(x) · cos(2πx/Λ). No material absorption is considered, and the simulation is for normal incidence, TE polarization.

## Reproduction target
Your task is to implement the Rouard’s method simulation described above and compute the spectral reflectance of the Gaussian-apodized Bragg grating over a wavelength range of 1549–1551 nm with a step size no larger than 0.001 nm. From the resulting reflectance spectrum (reflectance in linear scale, 0–1), you must extract three filter performance metrics:
1. peak_reflectance – the maximum reflectance value in the spectrum.
2. fwhm_nm – the full width at half-maximum (in nm) of the main reflection peak.
3. max_side_lobe_dB – the maximum reflectance (converted to dB) found outside a window of ±0.5 nm centred on the wavelength of peak reflectance.
Output the full (wavelength, reflectance) pairs into a CSV file named spectral_response.csv, and the three metrics into a JSON file named summary_metrics.json. Both files must be placed under /app/outputs.

## Assets

- Python scientific stack: numpy scipy

## Workflow steps

### Step 1: Simulate grating reflectance spectrum
- Role: scored (load-bearing)
- Action: Implement Rouard’s method (transfer-matrix approach for stratified media) to compute the reflectance spectrum of a Gaussian-apodized Bragg grating with parameters L=14.0 mm, Λ=517 nm, n_avg=1.5, Δn_max=1.5×10⁻⁴, ε=9.0. Use TE polarization at normal incidence over a wavelength range of 1549–1551 nm with a step of ≤0.001 nm. Write the resulting (wavelength_nm, reflectance) pairs to spectral_response.csv.
- Output file: `/app/outputs/spectral_response.csv`
- Format: csv
- Contract: CSV with columns: wavelength_nm (float), reflectance (float, linear scale 0-1).
- Scoring: scored by hidden verifier

### Step 2: Extract filter metrics
- Role: scored
- Action: Read spectral_response.csv and compute: (a) peak_reflectance as the maximum reflectance value; (b) fwhm_nm as the full width at half-maximum of the main reflection peak; (c) max_side_lobe_dB as the maximum reflectance (in dB) outside a ±0.5 nm window centered on the wavelength of peak reflectance. Write these three values as a JSON object to summary_metrics.json.
- Output file: `/app/outputs/summary_metrics.json`
- Format: json
- Contract: JSON object with keys: peak_reflectance (float, linear), fwhm_nm (float), max_side_lobe_dB (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spectral_response.csv`
- `/app/outputs/summary_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spectral_response.csv
- path: `/app/outputs/spectral_response.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed reflectance spectrum used by the checker to recompute peak reflectance, FWHM, and side-lobe suppression.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `reflectance`
  - `units`:
    - `wavelength_nm`: nm
    - `reflectance`: linear (0-1)

### summary_metrics.json
- path: `/app/outputs/summary_metrics.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent-reported metrics extracted from the spectrum; checker cross-validates consistency with values recomputed from spectral_response.csv.
- schema:
  - `type`: object
  - `required`:
    - `peak_reflectance`: float
    - `fwhm_nm`: float
    - `max_side_lobe_dB`: float

Notes: The checker recomputes the three filter metrics from spectral_response.csv and compares them to hidden gold values with appropriate tolerances. The summary_metrics.json is also checked for self-consistency against those recomputed numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spectral_response.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "reflectance"
        ],
        "units": {
          "wavelength_nm": "nm",
          "reflectance": "linear (0-1)"
        }
      },
      "description": "Computed reflectance spectrum used by the checker to recompute peak reflectance, FWHM, and side-lobe suppression."
    },
    {
      "file": "summary_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "peak_reflectance": "float",
          "fwhm_nm": "float",
          "max_side_lobe_dB": "float"
        }
      },
      "description": "Agent-reported metrics extracted from the spectrum; checker cross-validates consistency with values recomputed from spectral_response.csv."
    }
  ],
  "notes": "The checker recomputes the three filter metrics from spectral_response.csv and compares them to hidden gold values with appropriate tolerances. The summary_metrics.json is also checked for self-consistency against those recomputed numbers."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently recomputes the three metrics from your spectral_response.csv file using the same definitions (peak reflectance, FWHM, max side-lobe level). These recomputed values are compared against reference values derived from the original study. Your summary_metrics.json is also checked for consistency with the recomputed values. A combined score (between 0 and 1) is assigned based on how closely each metric matches the reference, with partial credit possible. To earn full credit, your simulation must faithfully implement Rouard’s method with the specified grating parameters and fine wavelength sampling, producing metrics that agree with the reference within acceptable tolerances. Providing both CSV and JSON files in the correct format is required; missing or malformed files will result in a low score.
