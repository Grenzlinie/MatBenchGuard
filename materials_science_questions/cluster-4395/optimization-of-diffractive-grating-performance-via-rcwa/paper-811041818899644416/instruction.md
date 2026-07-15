# FDTD Simulation of a Subwavelength Metal Grating Multiband Waveplate

## Problem background
Controlling polarization of light is critical in many optical applications. A waveplate transforms the polarization state, typically converting between linear and circular polarization (quarter-waveplate) or rotating linear polarization (half-waveplate). Recent work has explored reflective metallic subwavelength gratings as compact, flexible, and all-metal waveplates that avoid dielectric materials. The performance of such a reflective waveplate is determined by the phase difference and amplitude ratio between the two orthogonal reflected electric field components (TE and TM) and the overall reflectance. In this task, you will simulate an aluminum (Al) nano-grating on a nickel (Ni) substrate to evaluate its multiband waveplate functionality.

## Approach
The core principle is that a subwavelength metallic grating exhibits form birefringence. When a linearly polarized plane wave with polarization orientation θ is incident normally onto the grating, the TE component (electric field parallel to the grating grooves) reflects mainly from the top surface, while the TM component (perpendicular) penetrates into the grooves and reflects from the bottom, accumulating a phase delay. By controlling the grating depth, ridge width, and period, one can engineer a desired phase difference Δφ between the reflected components. The amplitude ratio β = |E_y|/|E_x| can be tuned by adjusting the incident polarization orientation θ. The total reflectance R of the device must remain high for efficient operation. To reproduce the results, you will use an open-source finite-difference time-domain (FDTD) solver such as MEEP. You will define the grating geometry (period 0.25 μm, ridge width 0.13 μm, grating depth 0.13 μm) with an Al thickness >0.18 μm over a Ni substrate. Optical constants for Al and Ni are taken from Palik's handbook (available via refractiveindex.info). You will run a broadband simulation (0.4–1.2 μm) with θ=45° to extract the spectral variation of Δφ, β, and R. You will also perform fine θ sweeps around 40–45° at three design wavelengths (near 465 nm, 656 nm, and 921 nm) to locate the angle that gives β=1. The required outputs are two CSV files summarizing the computed quantities.

## Reproduction target
Produce two scored artifacts in `/app/outputs`:
- `spectral_data.csv`: columns `wavelength_um`, `phase_difference_rad`, `amplitude_ratio`, `reflectance` for the θ=45° simulation over 0.4–1.2 μm.
- `beta_one_theta.csv`: columns `wavelength_um`, `theta_deg` with one row for each of the three design wavelengths (near 465 nm, 656 nm, and 921 nm) giving the polarization orientation θ that yields amplitude ratio β=1.
Your FDTD simulation must compute the reflected complex electric field components; from these you derive Δφ as the phase difference between the reflected TE and TM components, β as |E_y|/|E_x|, and the total reflectance R.

## Assets

- MEEP FDTD solver: https://meep.readthedocs.io/
- Optical constants of Al and Ni: https://refractiveindex.info/

## Workflow steps

### Step 1: Run FDTD simulation of the nano‑grating
- Role: process
- Action: Using the open‑source FDTD solver MEEP, simulate the reflective Al/Ni nano‑grating. Set geometry: period 0.25 μm, ridge width 0.13 μm, grating depth 0.13 μm, with Al film thickness >0.18 μm on a Ni substrate. Use optical constants for Al and Ni obtained from a public database (Palik). Run a spectral sweep over 0.4–1.2 μm with normally incident linearly polarized plane wave at polarization orientation θ=45° and record the reflected complex electric field components Ex and Ey as functions of wavelength. Additionally, for the three design wavelengths (near 465 nm, 656 nm, and 921 nm), run a fine θ sweep between 40° and 45° to capture the angle that gives amplitude ratio β=1. Save all raw complex reflection data for later extraction.
- Evidence: none

### Step 2: Extract spectral performance data (θ=45°)
- Role: scored (load-bearing)
- Action: From the θ=45° simulation, compute the phase difference Δφ between the reflected TE and TM components, the amplitude ratio β = |Ey|/|Ex|, and the total reflectance R as functions of wavelength. Output the results as spectral_data.csv.
- Output file: `/app/outputs/spectral_data.csv`
- Format: csv
- Contract: wavelength_um (float), phase_difference_rad (float), amplitude_ratio (float), reflectance (float)
- Scoring: scored by hidden verifier

### Step 3: Determine polarization orientation for amplitude balance
- Role: scored
- Action: From the θ‑sweep simulations at the three design wavelengths (near 465 nm, 656 nm, and 921 nm), find the polarization orientation θ (in degrees) that yields amplitude ratio β = 1. Output the results as beta_one_theta.csv.
- Output file: `/app/outputs/beta_one_theta.csv`
- Format: csv
- Contract: wavelength_um (float), theta_deg (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/spectral_data.csv`
- `/app/outputs/beta_one_theta.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### spectral_data.csv
- path: `/app/outputs/spectral_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spectral performance of the nano‑grating waveplate at incident polarization θ=45°, containing wavelength, phase difference, amplitude ratio, and reflectance. The checker compares the phase difference and reflectance at specific hidden wavelengths to reference design values.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`, `phase_difference_rad`, `amplitude_ratio`, `reflectance`
  - `units`:
    - `wavelength_um`: μm
    - `phase_difference_rad`: rad
    - `amplitude_ratio`: dimensionless
    - `reflectance`: dimensionless

### beta_one_theta.csv
- path: `/app/outputs/beta_one_theta.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Polarization orientation θ at which the amplitude ratio β=1 is achieved for the three design wavelengths. The checker verifies that the reported angles fall within the expected interval for the respective wavelengths.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`, `theta_deg`
  - `units`:
    - `wavelength_um`: μm
    - `theta_deg`: deg

Notes: Both outputs are re‑derivable from the FDTD simulation. The checker performs a result‑level comparison (T0) against hidden paper‑reported gold values with appropriate tolerances; exact match is not required, but the submitted numbers must be consistent with honest re‑computation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "spectral_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um",
          "phase_difference_rad",
          "amplitude_ratio",
          "reflectance"
        ],
        "units": {
          "wavelength_um": "μm",
          "phase_difference_rad": "rad",
          "amplitude_ratio": "dimensionless",
          "reflectance": "dimensionless"
        }
      },
      "description": "Spectral performance of the nano‑grating waveplate at incident polarization θ=45°, containing wavelength, phase difference, amplitude ratio, and reflectance. The checker compares the phase difference and reflectance at specific hidden wavelengths to reference design values."
    },
    {
      "file": "beta_one_theta.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um",
          "theta_deg"
        ],
        "units": {
          "wavelength_um": "μm",
          "theta_deg": "deg"
        }
      },
      "description": "Polarization orientation θ at which the amplitude ratio β=1 is achieved for the three design wavelengths. The checker verifies that the reported angles fall within the expected interval for the respective wavelengths."
    }
  ],
  "notes": "Both outputs are re‑derivable from the FDTD simulation. The checker performs a result‑level comparison (T0) against hidden paper‑reported gold values with appropriate tolerances; exact match is not required, but the submitted numbers must be consistent with honest re‑computation."
}
```

## How you are scored
A hidden verifier will independently check your output artifacts. For `spectral_data.csv`, it compares your reported phase difference, amplitude ratio, and reflectance against hidden reference values derived from rigorous FDTD calculations at a set of verification wavelengths. It also verifies that the phase difference follows the expected trend and that reflectance stays above a required threshold. For `beta_one_theta.csv`, it checks that the reported θ values lie within the physically plausible range for each design wavelength and that they yield β≈1 in a self-consistency check. The verifier combines these checks into a final reward in [0,1]. Fabricating numbers without running the simulation will not pass, because many verification points are at conditions where only a correct simulation can produce consistent results. To succeed, you must carry out the simulation as described and output the computed quantities faithfully.
