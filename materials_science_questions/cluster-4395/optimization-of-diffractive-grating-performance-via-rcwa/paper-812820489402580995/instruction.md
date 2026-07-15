# Dual-layer grating coupler FDTD simulation for vertical fiber-chip coupling efficiency

## Problem background
Efficient coupling between single-mode fibers and silicon photonic integrated circuits is challenging because of the large mode-size mismatch. Grating couplers can provide out-of-plane coupling, but achieving vertical incidence, polarization diversity, and dual-wavelength operation simultaneously is difficult. This work designs a dual-layer grating coupler that uses a top grating as a beam splitter and a bottom grating to match the diffracted waves to silicon slab waveguide modes, enabling vertical fiber-chip coupling at both 1.3 μm and 1.55 μm bands for TE and TM polarizations. The performance is evaluated by 2D finite-difference time-domain (FDTD) simulations, which predict the coupling efficiency spectra and the peak efficiencies and bandwidths of the relevant modes.

## Approach
The dual-layer grating structure consists of a top grating (long period, deep etch, alternating Si3N4 and SiO2) and a bottom grating (short period, shallow etch, alternating Si and SiO2) separated by a SiO2 gap layer, all on a buried oxide (BOX) layer above a silicon substrate. A normally incident Gaussian beam with a waist of about 5 μm approximates the fiber mode. Two-dimensional FDTD simulations with a uniform grid of 10 nm and perfectly matched layer (PML) boundaries are run for TE and TM polarizations while sweeping the free-space wavelength from 1.2 μm to 1.7 μm. At each wavelength, the total optical power coupled into both silicon slab waveguide output ports is computed and normalized to the incident power, yielding coupling efficiency spectra. From these spectra, the three dominant peaks are identified and their peak wavelengths, peak efficiencies, and 3-dB bandwidths are extracted.

## Reproduction target
Run the FDTD simulations to produce two coupling efficiency spectra (CSV files) for TE and TM polarizations over the wavelength range 1.2–1.7 μm. From these spectra, identify the three main peaks: one TM0 mode near 1.32 μm, one TE0 mode near 1.56 μm, and one TM0 mode near 1.58 μm. Save a JSON file reporting for each peak its wavelength (μm), peak efficiency (as a fraction), and 3‑dB bandwidth (nm).

## Assets

- Meep: https://meep.readthedocs.io/

## Workflow steps

### Step 1: TE polarization FDTD simulation
- Role: scored
- Action: Build the dual-layer grating geometry using the provided parameters: top grating period Λt=4.1 μm, etch depth dt=1.3 μm, duty cycle 0.5 (alternating Si3N4/SiO2); bottom grating period Λc=0.63 μm, etch depth dc=0.06 μm, duty cycle 0.5 (Si/SiO2); Si slab waveguide height dSi=0.26 μm; gap layer dgap=1.75 μm; BOX layer dbox=1.75 μm. Use refractive indices n_Si3N4=2, n_SiO2=1.45, n_Si≈3.48. Run a 2D-FDTD simulation with grid size 10 nm, PML boundaries, normally incident TE-polarized Gaussian beam (waist ~5 μm). Sweep free-space wavelength from 1.2 to 1.7 μm, compute total dual-port coupling efficiency, and save the spectrum.
- Output file: `/app/outputs/coupling_spectrum_TE.csv`
- Format: csv
- Contract: wavelength_um (float), efficiency (float as fraction)
- Scoring: scored by hidden verifier

### Step 2: TM polarization FDTD simulation
- Role: scored
- Action: Using the same geometry and FDTD settings as step_01 but with TM-polarized incident field, sweep wavelength 1.2–1.7 μm, compute dual-port coupling efficiency, and save the spectrum.
- Output file: `/app/outputs/coupling_spectrum_TM.csv`
- Format: csv
- Contract: wavelength_um (float), efficiency (float as fraction)
- Scoring: scored by hidden verifier

### Step 3: Extract peak parameters
- Role: scored (load-bearing)
- Action: From coupling_spectrum_TE.csv and coupling_spectrum_TM.csv, identify the three main peaks corresponding to TM0 mode near 1.32 μm, TE0 mode near 1.56 μm, and TM0 mode near 1.58 μm. For each peak, extract the wavelength (μm), peak efficiency (fraction), and 3-dB bandwidth (nm). Save the results.
- Output file: `/app/outputs/extracted_peaks.json`
- Format: json
- Contract: [{"mode": "TE0" or "TM0", "wavelength_um": float, "efficiency": float, "bandwidth_3dB_nm": float}]
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/coupling_spectrum_TE.csv`
- `/app/outputs/coupling_spectrum_TM.csv`
- `/app/outputs/extracted_peaks.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coupling_spectrum_TE.csv
- path: `/app/outputs/coupling_spectrum_TE.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file with two numeric columns: wavelength (um) and coupling efficiency (fraction) for TE polarization.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`, `efficiency`
  - `units`:
    - `wavelength_um`: micrometer
    - `efficiency`: fraction (0 to 1)

### coupling_spectrum_TM.csv
- path: `/app/outputs/coupling_spectrum_TM.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV file with two numeric columns: wavelength (um) and coupling efficiency (fraction) for TM polarization.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_um`, `efficiency`
  - `units`:
    - `wavelength_um`: micrometer
    - `efficiency`: fraction (0 to 1)

### extracted_peaks.json
- path: `/app/outputs/extracted_peaks.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Array of peak objects containing mode identifier, peak wavelength, efficiency, and 3-dB bandwidth.
- schema:
  - `type`: array
  - `items`:
    - `mode`: string (one of 'TE0', 'TM0')
    - `wavelength_um`: number (float)
    - `efficiency`: number (float, fraction)
    - `bandwidth_3dB_nm`: number (float, nm)

Notes: The top-grating efficiency study and the Fabry-Perot thickness optimization are omitted from this reproduction; the optimized geometric and material parameters are provided directly. The simulation uses Meep, an open-source FDTD solver.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coupling_spectrum_TE.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um",
          "efficiency"
        ],
        "units": {
          "wavelength_um": "micrometer",
          "efficiency": "fraction (0 to 1)"
        }
      },
      "description": "CSV file with two numeric columns: wavelength (um) and coupling efficiency (fraction) for TE polarization."
    },
    {
      "file": "coupling_spectrum_TM.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_um",
          "efficiency"
        ],
        "units": {
          "wavelength_um": "micrometer",
          "efficiency": "fraction (0 to 1)"
        }
      },
      "description": "CSV file with two numeric columns: wavelength (um) and coupling efficiency (fraction) for TM polarization."
    },
    {
      "file": "extracted_peaks.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "mode": "string (one of 'TE0', 'TM0')",
          "wavelength_um": "number (float)",
          "efficiency": "number (float, fraction)",
          "bandwidth_3dB_nm": "number (float, nm)"
        }
      },
      "description": "Array of peak objects containing mode identifier, peak wavelength, efficiency, and 3-dB bandwidth."
    }
  ],
  "notes": "The top-grating efficiency study and the Fabry-Perot thickness optimization are omitted from this reproduction; the optimized geometric and material parameters are provided directly. The simulation uses Meep, an open-source FDTD solver."
}
```

## How you are scored
A hidden verifier will independently score your submitted artifacts. Both coupling_spectrum_TE.csv and coupling_spectrum_TM.csv must be valid CSV files with two numeric columns; a small structural validity score is awarded for their format. The main score comes from extracted_peaks.json: the verifier compares each peak’s wavelength, efficiency, and bandwidth against hidden reference values. Full credit is given when your extracted performance meets or exceeds the expected level within allowed tolerances, which are set to what a correct FDTD re‑run can achieve. Each artifact contributes a weighted portion to the final reward; simply reporting plausible numbers without having genuinely run the simulation is unlikely to pass because the tolerances are based on actual re‑run variability.
