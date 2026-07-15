# Numerical Simulation of Electro‑Optic Metasurface Modulation Performance

## Problem background
Dynamic optical metasurfaces that enable fast, efficient control of reflected light are promising for spatial light modulators and other applications, but achieving strong modulation with electro-optic effects is challenging because the interaction length in thin metasurface layers is inherently limited. This task addresses a resonant design that circumvents this limitation by exploiting a quasi-bound state in the continuum (qBIC). The metasurface consists of a lithium niobate (LN) thin film sandwiched between an optically thick gold back-reflector and a symmetric gold nanoridge grating, where the metal ridges serve as both optical elements and control electrodes. The narrow qBIC resonance, which occurs at telecom wavelengths under normal incidence, enhances light–matter interaction and makes the reflectance very sensitive to refractive index changes induced by an applied bias via the linear electro-optic (Pockels) effect. The numerical reproduction aims to simulate the reflectance spectra of this metasurface as a function of applied voltage and to derive the resulting absolute modulation, modulation depth, phase shift, resonance shift, and figure of merit that quantify the predicted modulation performance.

## Approach
The core idea is to perform frequency-domain electromagnetic simulations of one unit cell of the symmetric grating with periodic boundary conditions, effectively modelling an infinite array. Material dielectric functions are obtained from published literature for lithium niobate, gold, and the chromium adhesion layer. First, an eigenfrequency analysis is used to identify the fundamental qBIC mode and its quality factor, confirming the narrow resonance. Then the electro-optic response is captured in two stages: a DC electrostatic simulation provides the electric field distribution inside the LN layer for applied biases of −30 V and +30 V; the Pockels coefficients are used to convert this field into a small perturbation of the LN refractive index. Optical scattering simulations at normal incidence are run for zero bias and both biased states to compute the reflectance as a continuous function of wavelength. From the resulting spectra, standard modulation metrics—absolute modulation, modulation depth, phase difference between bias states, resonance shift, and a figure of merit (Δλ/FWHM)—are extracted by post-processing. No experimental data or proprietary software is required; the same procedure can be implemented with any open-source RCWA or FEM solver.

## Reproduction target
Produce two scored artifacts: (1) a CSV file (`reflectance_spectra_symmetric.csv`) containing the simulated reflectance spectra of the symmetric gold-grating metasurface for bias states of 0 V, −30 V, and +30 V over the telecom wavelength range; (2) a JSON file (`modulation_metrics.json`) that reports the derived absolute modulation (fraction 0–1), modulation depth (fraction 0–1), maximum phase shift between the two biased states (degrees), resonance shift (nm), and figure of merit FOM = Δλ/FWHM (dimensionless). These quantities must be computed entirely from your simulation; they represent the predicted modulation performance of the infinite-period unit-cell design.

## Assets

- Lithium niobate refractive index (Zelmon et al., 1997): 10.1364/JOSAB.14.003319
- Gold complex permittivity (Rakić et al., 1998): 10.1364/AO.37.005271
- Chromium optical constants (Johnson & Christy, 1974): 10.1103/PhysRevB.9.5056
- Pockels coefficients for LN (Jazbinšek & Zgonik, 2002): 10.1007/s00340-002-0917-1
- Open‑source electromagnetic solver (e.g., S4, rcwa‑python, FEniCS): https://github.com/victorliu/S4

## Workflow steps

### Step 1: Eigenmode analysis of qBIC resonance
- Role: process
- Action: Set up the 2D unit‑cell geometry of the symmetric gold‑grating metasurface (period Λ=750 nm, ridge width w=445 nm, ridge thickness t_g=75 nm, LN film thickness 880 nm, Cr adhesion layer 10 nm, Au back‑reflector 300 nm) and assign material permittivities from the listed references. Run an eigenfrequency simulation with periodic boundary conditions to identify the fundamental quasi‑BIC mode and extract its Q‑factor.
- Evidence: `/app/outputs/eigenmode_qfactor.txt`

### Step 2: Electro‑optic reflectance simulation
- Role: scored (load-bearing)
- Action: Perform a DC electrostatic simulation for applied biases of −30 V and +30 V to obtain the electric field distribution. Compute the refractive index perturbation using the Pockels coefficients (Δn_i = −½ n_i³ r_iiz E_z). Then run frequency‑domain optical scattering simulations (normal incidence) for bias states 0 V, −30 V, and +30 V to obtain reflectance spectra. Output the reflectance values as a CSV file.
- Output file: `/app/outputs/reflectance_spectra_symmetric.csv`
- Format: csv
- Contract: CSV with columns: wavelength_nm (float), reflectance_0V (float, 0–1), reflectance_neg30V (float, 0–1), reflectance_pos30V (float, 0–1). The CSV must include a header row with these column names.
- Scoring: scored by hidden verifier

### Step 3: Modulation metric extraction
- Role: scored
- Action: From the simulated reflectance spectra CSV, compute: (i) absolute modulation |ΔR| as max|R(+30 V)−R(−30 V)|, (ii) modulation depth = 1 − min(R)/max(R) within the resonance, (iii) phase shift between the two bias states (derived from complex reflection coefficients or estimated from spectral shift), (iv) resonance shift Δλ and FWHM, and (v) figure‑of‑merit FOM = Δλ/FWHM. Write these metrics to a JSON file.
- Output file: `/app/outputs/modulation_metrics.json`
- Format: json
- Contract: JSON object with keys: absolute_modulation (float, fraction 0–1), modulation_depth (float, fraction 0–1), phase_shift_max (float, degrees), resonance_shift_nm (float, nm), FOM (float, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reflectance_spectra_symmetric.csv`
- `/app/outputs/modulation_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reflectance_spectra_symmetric.csv
- path: `/app/outputs/reflectance_spectra_symmetric.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Simulated reflectance spectra of the symmetric grating for three bias states. The hidden checker recomputes performance metrics (absolute modulation, modulation depth, resonance shift, FOM) from these raw data and compares them against the paper's reported values. The CSV includes a header row.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `reflectance_0V`, `reflectance_neg30V`, `reflectance_pos30V`
  - `units`:
    - `wavelength_nm`: nm
    - `reflectance_0V`: dimensionless (0–1)
    - `reflectance_neg30V`: dimensionless (0–1)
    - `reflectance_pos30V`: dimensionless (0–1)

### modulation_metrics.json
- path: `/app/outputs/modulation_metrics.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Agent‑computed modulation metrics derived from the reflectance spectra. The hidden checker verifies that each quantity meets or exceeds the paper's simulated performance thresholds (e.g., absolute modulation ≥ 0.50, phase shift ≥ 220°, FOM ≈ 0.47) and is internally consistent with the submitted reflectance spectra.
- schema:
  - `type`: object
  - `required`:
    - `absolute_modulation`: float (fraction 0–1)
    - `modulation_depth`: float (fraction 0–1)
    - `phase_shift_max`: float (degrees)
    - `resonance_shift_nm`: float (nm)
    - `FOM`: float (dimensionless)

Notes: This contract covers the symmetric grating design only. The infinite‑period unit‑cell simulation is assumed; geometry and material data are fully specified from the public references. The hidden checker independently recomputes the primary modulation figures from the raw reflectance CSV (T1) and supplements with a direct threshold comparison on the reported metrics (T0). The CSV must have a header row matching the required columns.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reflectance_spectra_symmetric.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "reflectance_0V",
          "reflectance_neg30V",
          "reflectance_pos30V"
        ],
        "units": {
          "wavelength_nm": "nm",
          "reflectance_0V": "dimensionless (0–1)",
          "reflectance_neg30V": "dimensionless (0–1)",
          "reflectance_pos30V": "dimensionless (0–1)"
        }
      },
      "description": "Simulated reflectance spectra of the symmetric grating for three bias states. The hidden checker recomputes performance metrics (absolute modulation, modulation depth, resonance shift, FOM) from these raw data and compares them against the paper's reported values. The CSV includes a header row."
    },
    {
      "file": "modulation_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "absolute_modulation": "float (fraction 0–1)",
          "modulation_depth": "float (fraction 0–1)",
          "phase_shift_max": "float (degrees)",
          "resonance_shift_nm": "float (nm)",
          "FOM": "float (dimensionless)"
        }
      },
      "description": "Agent‑computed modulation metrics derived from the reflectance spectra. The hidden checker verifies that each quantity meets or exceeds the paper's simulated performance thresholds (e.g., absolute modulation ≥ 0.50, phase shift ≥ 220°, FOM ≈ 0.47) and is internally consistent with the submitted reflectance spectra."
    }
  ],
  "notes": "This contract covers the symmetric grating design only. The infinite‑period unit‑cell simulation is assumed; geometry and material data are fully specified from the public references. The hidden checker independently recomputes the primary modulation figures from the raw reflectance CSV (T1) and supplements with a direct threshold comparison on the reported metrics (T0). The CSV must have a header row matching the required columns."
}
```

## How you are scored
A hidden verifier scores each workflow stage independently and combines the results into your final reward. For the reflectance spectra CSV, the verifier recomputes the absolute modulation, modulation depth, resonance shift, and figure of merit directly from your raw data and compares them against hidden reference criteria, checking both the values and their internal consistency (e.g., correct wavelength ordering, plausible reflectance range). For the modulation metrics JSON, the verifier verifies that the reported numbers fall within expected operational bounds and are consistent with the reflectance spectra you submitted. The weights are distributed so that the primary scored stage (reflectance simulation and metric recomputation) carries the largest share. Reporting numbers without a correct underlying simulation will not pass these checks.
