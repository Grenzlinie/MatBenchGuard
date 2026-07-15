# Bloch Mode Calculation of Effective Thermo-Optic Coefficient for Subwavelength Grating Waveguides

## Problem background
Silicon photonic waveguides are a key building block of integrated photonics, but they suffer from a large thermo-optic (TO) coefficient — their effective refractive index changes significantly with temperature. This temperature sensitivity degrades the performance of interferometers, resonators, and wavelength-selective devices, and typically requires active thermal stabilization. A subwavelength grating (SWG) waveguide replaces a continuous silicon core with a periodic pattern of silicon segments separated by narrow gaps filled with a polymer that possesses a negative TO coefficient. Through spatial index averaging, the composite core can reduce, and potentially cancel, the overall temperature dependence. This task aims to compute the effective thermo-optic coefficient of such SWG waveguides as a function of the grating duty ratio and polarization, and to determine the conditions under which near-athermal operation may occur.

## Approach
The effective thermo-optic coefficient dn_eff/dT quantifies the change of the waveguide Bloch mode effective index with temperature. We compute it by running electromagnetic Bloch mode simulations with the open-source tool MIT Photonic Bands (MPB) at two temperatures — room temperature and a +20 K increase — and taking the finite difference. The waveguide cross-section is fixed: silicon core thickness 0.26 µm, buried oxide 2 µm, waveguide width 470 nm, grating period (pitch) 250 nm, overcladding of SU‑8 polymer. The material refractive indices at room temperature are n_Si = 3.476, n_SU8 = 1.58, n_SiO2 = 1.444. The temperature-dependent indices are shifted according to the material TO coefficients: d n_Si / dT = +1.8×10⁻⁴ K⁻¹, d n_SU8 / dT = −1.1×10⁻⁴ K⁻¹, and the oxide index is assumed temperature-independent. Simulations are performed at a wavelength of 1550 nm for a set of SWG duty ratios covering 46%, 56%, 64%, 66%, 80%, and the photonic wire (100%) for both TE and TM polarization. In addition, for the 66% duty TE waveguide, the effective index is calculated over a wavelength range from 1525 nm to 1575 nm at both temperatures. The raw effective indices are then post-processed: dn_eff/dT is obtained for each case at 1550 nm, and for the 66% TE sweep a linear least‑squares fit f(λ)=aλ+b is performed, from which the zero‑crossing wavelength (athermal point) is extracted.

## Reproduction target
1. For each of the following SWG duty ratios — 46%, 56%, 64%, 66%, 80%, and 100% — compute the effective thermo-optic coefficient dn_eff/dT at λ = 1550 nm for both TE and TM polarizations. Output the results as a CSV file with columns `duty_ratio` (integer, percent), `polarization` (string, `TE` or `TM`), and `dn_eff_dT` (float, units K⁻¹).

2. For the 66% duty TE polarization waveguide, compute dn_eff/dT at multiple wavelengths evenly covering the range 1525–1575 nm. Perform a linear least‑squares fit of the form f(λ)=a·λ + b, where λ is in nm and f(λ) is dn_eff/dT in K⁻¹. Find the athermal (zero‑crossing) wavelength λ₀ such that f(λ₀)=0. Output the fit result as a JSON file containing keys `a` (float, nm⁻¹ K⁻¹), `b` (float, K⁻¹), and `zero_crossing_nm` (float, nm).

## Assets

- MIT Photonic Bands (MPB): https://ab-initio.mit.edu/wiki/index.php/MIT_Photonic_Bands
- Python with numpy/scipy: https://pypi.org

## Workflow steps

### Step 1: Run Bloch mode simulations for all duty ratios and polarizations
- Role: process
- Action: Set up MIT Photonic Bands to compute Bloch mode effective indices for the SWG waveguide with given geometry (Si thickness 0.26 µm, width 470 nm, pitch 250 nm, SU-8 cladding) for each duty ratio (46%, 56%, 64%, 66%, 80%, 100%) and for TE/TM polarizations at two temperatures (room temperature and +20 K). Additionally, for the TE 66% duty waveguide, compute effective indices over a wavelength range of 1525–1575 nm at both temperatures. Record all raw effective indices for later analysis.
- Evidence: `/app/outputs/mpb_output.log`

### Step 2: Compute dn_eff/dT vs duty ratio from simulation data
- Role: scored (load-bearing)
- Action: From the MPB simulation results, compute dn_eff/dT = (n_eff_hot - n_eff_room) / 20 K for each duty ratio and polarization at λ=1550 nm. Output a CSV file with columns: duty_ratio (integer, percent), polarization (TE or TM), dn_eff_dT (float, K⁻¹). Include duty ratios 46, 56, 64, 66, 80, 100 for both polarizations.
- Output file: `/app/outputs/dn_eff_dT_vs_duty.csv`
- Format: csv
- Contract: CSV with columns: duty_ratio (integer), polarization (string), dn_eff_dT (float)
- Scoring: scored by hidden verifier

### Step 3: Linear fit for TE 66% duty dn_eff/dT vs wavelength
- Role: scored (load-bearing)
- Action: Using the MPB wavelength-sweep data for the TE, 66% duty waveguide, compute dn_eff/dT for each wavelength in the 1525–1575 nm range. Perform a linear least-squares fit f(λ)=a*λ+b. Find the zero-crossing wavelength where f(λ)=0. Write a JSON file with keys: a (float, nm⁻¹ K⁻¹), b (float, K⁻¹), zero_crossing_nm (float).
- Output file: `/app/outputs/te_66_duty_fit.json`
- Format: json
- Contract: JSON object with keys: a (float), b (float), zero_crossing_nm (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dn_eff_dT_vs_duty.csv`
- `/app/outputs/te_66_duty_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dn_eff_dT_vs_duty.csv
- path: `/app/outputs/dn_eff_dT_vs_duty.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Effective thermo-optic coefficient dn_eff/dT (K⁻¹) from Bloch mode simulations for given duty ratios and polarizations at λ=1550 nm.
- schema:
  - `type`: table
  - `required_columns`: `duty_ratio`, `polarization`, `dn_eff_dT`
  - `units`:
    - `duty_ratio`: percent
    - `polarization`: string
    - `dn_eff_dT`: K⁻¹

### te_66_duty_fit.json
- path: `/app/outputs/te_66_duty_fit.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Linear-fit parameters a, b of dn_eff/dT vs wavelength for TE 66% duty waveguide and the athermal zero-crossing wavelength.
- schema:
  - `type`: object
  - `required`:
    - `a`: float (nm⁻¹ K⁻¹)
    - `b`: float (K⁻¹)
    - `zero_crossing_nm`: float (nm)

Notes: Only the numerical Bloch mode calculation stage is scored; experimental MZI data extraction is excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dn_eff_dT_vs_duty.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "duty_ratio",
          "polarization",
          "dn_eff_dT"
        ],
        "units": {
          "duty_ratio": "percent",
          "polarization": "string",
          "dn_eff_dT": "K⁻¹"
        }
      },
      "description": "Effective thermo-optic coefficient dn_eff/dT (K⁻¹) from Bloch mode simulations for given duty ratios and polarizations at λ=1550 nm."
    },
    {
      "file": "te_66_duty_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "float (nm⁻¹ K⁻¹)",
          "b": "float (K⁻¹)",
          "zero_crossing_nm": "float (nm)"
        }
      },
      "description": "Linear-fit parameters a, b of dn_eff/dT vs wavelength for TE 66% duty waveguide and the athermal zero-crossing wavelength."
    }
  ],
  "notes": "Only the numerical Bloch mode calculation stage is scored; experimental MZI data extraction is excluded."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file. For `dn_eff_dT_vs_duty.csv`, the computed dn_eff/dT values for each duty ratio and polarization are compared against reference values derived from the correct Bloch mode simulation. For `te_66_duty_fit.json`, the fit parameters a, b and the zero‑crossing wavelength are compared against the corresponding reference quantities. Each output contributes a weighted share to the final reward, and the scores are combined. Simply reporting the paper’s published numbers without running the simulation is not sufficient — the verifier expects results that match the values obtained by correctly setting up and executing the MPB workflow described in this instruction.
