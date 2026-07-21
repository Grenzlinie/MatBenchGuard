# Optical Gain Modeling and Parameter Extraction in III-Nitride Quantum Wells

## Problem background
InGaN/GaN quantum wells are the active region for blue and green laser diodes and LEDs. Strong spontaneous and piezoelectric polarization fields, along with Coulomb many-body effects, govern the optical gain and carrier dynamics. Accurate modelling of gain spectra as a function of carrier density is essential for device design. This task addresses the quantitative extraction of inhomogeneous broadening (caused by indium composition fluctuations) and the nonradiative Shockley–Read–Hall (SRH) carrier lifetime from measured gain spectra using a microscopic theory.

## Approach
The approach is a physics-based gain model that combines a six-band k·p bandstructure calculation for wurtzite InGaN/GaN quantum wells with a steady-state solution of the semiconductor Bloch equations, including carrier correlations at the second-Born Markovian level. Spontaneous and piezoelectric polarization fields are treated self-consistently (with the piezoelectric constants reduced by 50% relative to standard literature values). Homogeneous gain spectra are computed, then convolved with a Gaussian kernel to incorporate inhomogeneous broadening of variable width ΔE. The simulated spectra are matched to digitized experimental gain data (provided as a CSV resource) by adjusting the carrier density for each drive current and the global ΔE. The matched carrier-density–current pairs are used to extract the SRH lifetime via the rate equation I/(qV) = A N + B N², with given B and V. Material parameters for GaN and InN are taken from standard literature.

## Reproduction target
Compute optical gain spectra for a 2 nm In0.1Ga0.9N quantum well with 6 nm GaN barriers at 300 K, using the six-band k·p bandstructure and semiconductor Bloch equations. Match the computed gain to the provided experimental gain curves (at seven drive currents) by optimizing the global inhomogeneous broadening ΔE and mapping each current to a carrier density. Output the final gain spectra for the matched carrier densities as a CSV file (step_02_gain_spectra.csv). From the matched results, extract the inhomogeneous broadening ΔE (meV), indium composition fluctuation Δx (computed from ΔE and a bowing parameter of -1.4 eV), and the monomolecular SRH carrier lifetime τ (ns) from a fit to the rate equation using the supplied spontaneous emission coefficient B = 0.3×10⁻¹⁰ cm³/s and active volume V = 1.2×10⁻¹¹ cm³. Write these three parameters as a JSON file (step_03_extracted_parameters.json). The task is considered successful if the gain spectra satisfy structural sanity checks and the extracted parameters fall within the hidden tolerance bands of the expected physical values.

## Assets

- Digitized experimental gain spectra
- GaN and InN material parameters

## Workflow steps

### Step 1: Compute bandstructure and internal fields
- Role: process
- Action: Compute the bandstructure, subband energies, wavefunctions, and interband dipole matrix elements for a 2 nm In0.1Ga0.9N quantum well with 6 nm GaN barriers at T = 300 K, using a six-band k·p model for wurtzite structure. Include self-consistent spontaneous and piezoelectric polarization fields, with the piezoelectric constants reduced by 50% relative to standard literature values. Use material parameters from public literature (effective masses, crystal potentials, bandgap, bowing, polarization constants) for GaN and InN.
- Evidence: none

### Step 2: Gain matching and final gain spectra
- Role: scored (load-bearing)
- Action: Solve the steady-state semiconductor Bloch equations with second-Born Markovian carrier correlations to compute homogeneous gain spectra. Convolve with a Gaussian inhomogeneous broadening kernel of width ΔE (to be optimized). For the carrier densities N = [2.50, 2.60, 2.82, 2.95, 3.04, 3.15, 3.25] × 10^19 cm^{-3}, match the computed gain spectra to the provided experimental gain data by adjusting the carrier density for each drive current and the global ΔE. Output the final gain spectra (wavelength_nm, gain_cm-1, carrier_density_cm-3) for the matched densities.
- Output file: `/app/outputs/step_02_gain_spectra.csv`
- Format: csv
- Contract: CSV with columns: wavelength_nm (float), gain_cm-1 (float), carrier_density_cm-3 (float). Each row corresponds to one wavelength point; multiple carrier densities appear, each with their own wavelength sweep.
- Scoring: scored by hidden verifier

### Step 3: Extract parameters
- Role: scored
- Action: From the matched results, extract the optimal inhomogeneous broadening ΔE (meV). Compute the corresponding indium composition fluctuation Δx using the bandgap-composition relation with a bowing parameter of -1.4 eV. Fit the matched carrier density–current pairs to the rate equation I/(qV) = A N + B N^2, using the given B = 0.3 × 10^{-10} cm³/s, V = 1.2 × 10^{-11} cm³, and internal efficiency η_i = 1. Extract the monomolecular SRH carrier lifetime τ = 1/A (ns). Output the three values as JSON.
- Output file: `/app/outputs/step_03_extracted_parameters.json`
- Format: json
- Contract: JSON object with keys: {"Delta_E_meV": float, "Delta_x": float, "tau_ns": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_gain_spectra.csv`
- `/app/outputs/step_03_extracted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_gain_spectra.csv
- path: `/app/outputs/step_02_gain_spectra.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Optical gain spectra for each matched carrier density. At least 50 wavelength points per carrier density; gain values non-negative; peak gain increases with carrier density.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `gain_cm-1`, `carrier_density_cm-3`
  - `units`:
    - `wavelength_nm`: nm
    - `gain_cm-1`: 1/cm
    - `carrier_density_cm-3`: cm^-3

### step_03_extracted_parameters.json
- path: `/app/outputs/step_03_extracted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Extracted inhomogeneous broadening ΔE, indium composition fluctuation Δx, and SRH carrier lifetime τ. Compared to paper-reported values with hidden tolerances.
- schema:
  - `type`: object
  - `required`: `Delta_E_meV`, `Delta_x`, `tau_ns`
  - `items`:
    - `Delta_E_meV`: number (meV)
    - `Delta_x`: number (dimensionless)
    - `tau_ns`: number (ns)

Notes: step_02_gain_spectra.csv is audited for structural properties (non-negative gain, monotonic peak with density, sufficient resolution). step_03_extracted_parameters.json is compared to hidden paper-reported gold values (ΔE, Δx, τ) using relative tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_gain_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "gain_cm-1",
          "carrier_density_cm-3"
        ],
        "units": {
          "wavelength_nm": "nm",
          "gain_cm-1": "1/cm",
          "carrier_density_cm-3": "cm^-3"
        }
      },
      "description": "Optical gain spectra for each matched carrier density. At least 50 wavelength points per carrier density; gain values non-negative; peak gain increases with carrier density."
    },
    {
      "file": "step_03_extracted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Delta_E_meV",
          "Delta_x",
          "tau_ns"
        ],
        "items": {
          "Delta_E_meV": "number (meV)",
          "Delta_x": "number (dimensionless)",
          "tau_ns": "number (ns)"
        }
      },
      "description": "Extracted inhomogeneous broadening ΔE, indium composition fluctuation Δx, and SRH carrier lifetime τ. Compared to paper-reported values with hidden tolerances."
    }
  ],
  "notes": "step_02_gain_spectra.csv is audited for structural properties (non-negative gain, monotonic peak with density, sufficient resolution). step_03_extracted_parameters.json is compared to hidden paper-reported gold values (ΔE, Δx, τ) using relative tolerances."
}
```

## How you are scored
The grading is fully automatic and performed by a hidden verifier. It scores each scored output independently:

- `step_02_gain_spectra.csv` undergoes a structural audit: the file must contain at least 50 wavelength points per carrier density, all gain values must be non-negative, and the peak gain must increase monotonically with carrier density.
- `step_03_extracted_parameters.json` is compared to hidden reference values for ΔE, Δx, and τ using predetermined relative tolerances. The verifier does not expect exact equality, but the values must lie within a tolerance window that reflects legitimate implementation variations.

The final reward (0 to 1) is a weighted sum of the scores from these two artifacts. Copying the paper's reported numbers without performing the full computational workflow will not satisfy the structural audits, and the verifier requires both artifacts to be present and correctly formatted.
