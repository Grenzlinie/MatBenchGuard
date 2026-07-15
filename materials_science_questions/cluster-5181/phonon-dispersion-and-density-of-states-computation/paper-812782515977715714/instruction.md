# Nonstoichiometric Born-von Kármán Model for PdD0.63 Phonon Scattering Line Shapes

## Problem background
Palladium deuteride PdD0.63 exhibits broad optical-phonon line shapes in inelastic neutron scattering, in contrast to the sharp peaks expected from a simple stoichiometric harmonic model. The origin of this broadening is important for understanding electron-phonon coupling and the reverse isotope effect in superconducting PdH/PdD systems. One hypothesis is that the broadening arises from the random arrangement of deuterium vacancies (nonstoichiometry), not from anharmonicity. This task investigates that hypothesis by constructing a harmonic Born-von Kármán model that explicitly includes nonstoichiometric enlarged unit cells, computing the resulting one-phonon coherent and incoherent neutron scattering line shapes, and comparing them with experiment.

## Approach
The theoretical model is a Born-von Kármán lattice dynamics calculation that breaks translational symmetry by using enlarged cubic supercells (up to 3×3×3 conventional fcc cells) with random occupancy of the octahedral interstitial sites by deuterium at x=0.63. The force constants are first obtained from earlier stoichiometric PdD measurements (Rowe et al., 1974); then a non-linear fit is performed on a small cell (Pd4D3) to adjust only the D-D first-neighbor constant so that computed optical-mode peak positions match reference dispersion data at the same composition. Using this force set, many independent random vacancy configurations are generated for the n=3 supercell. For each configuration the dynamical matrix is diagonalized and the one-phonon coherent scattering law S1(κ,ω) is evaluated, together with an incoherent inelastic contribution, employing atomic scattering lengths and Debye-Waller factors from the spectrum. Histograms are averaged over the ensemble and convoluted with a Gaussian representing the instrumental resolution.

## Reproduction target
Reconstruct the complete pipeline: (1) Fit the D-D first-neighbor force constant using a nonstoichiometric Pd4D3 cell and digitised reference peak positions; output a CSV of fitted force constants including the ratio of the fitted D-D constant to the stoichiometric value. (2) Generate at least 25 random 3×3×3 supercell configurations (108 Pd, 68 D). (3) Compute normal modes and one-phonon scattering intensities for three momentum transfers: zone boundary κ=(3,0,0), zone center κ=(4,0,0), and longitudinal point κ≈(3.333,0,0) at T=80 K. (4) Ensemble-average and convolve with a Gaussian of FWHM ≈ 3 meV. (5) Save the final intensity profiles as three CSV files with energy (meV) and intensity columns.

## Assets

- Stoichiometric PdD force constant parameters (12 parameters) from Rowe et al. 1974: 10.1103/PhysRevLett.33.1297
- Optical phonon dispersion curve reference data (Fig. 1 of Rowe et al. 1974): 10.1103/PhysRevLett.33.1297
- Lattice constant of PdD0.63
- Neutron scattering lengths and atomic masses: https://www.nist.gov/ncnr/neutron-scattering-lengths-list
- Numerical libraries (NumPy, SciPy): numpy, scipy

## Workflow steps

### Step 1: Acquire reference data
- Role: process
- Action: Obtain the stoichiometric PdD force constant parameters (12 values) and the optical-phonon peak positions from Rowe et al. 1974 (Ref.10). Digitise the dispersion curves if necessary to extract the reference peak positions for the optical modes at high-symmetry points. Save the digitised peak positions.
- Evidence: `/app/outputs/reference_peaks_digitised.csv`

### Step 2: Fit force constants using Pd4D3 cell
- Role: scored (load-bearing)
- Action: Construct a small nonstoichiometric unit cell approximating PdD0.63 (Pd4D3, n=1, x=0.75) with random D occupancy. Implement the Born-von Kármán model using the reference force constants, compute optical-mode frequencies, and use a non-linear least-squares procedure to fit the D-D first-neighbor force constant (while keeping Pd-Pd and Pd-D constants at the stoichiometric values) so that the calculated weighted peak positions best match the digitised reference data from step01. Write the resulting force constant set.
- Output file: `/app/outputs/force_constants.csv`
- Format: csv
- Contract: Required columns: parameter_name (string), fitted_value (float), stoichiometric_value (float), ratio (float).
- Scoring: scored by hidden verifier

### Step 3: Generate random defect configurations for n=3 cell
- Role: process
- Action: Using the lattice constant a0 and the Pd fcc sublattice, generate at least 25 independent random configurations of the enlarged unit cell with n=3 (108 Pd atoms, 68 D atoms randomly placed on octahedral interstitial sites). Record the number of configurations and their seed indices.
- Evidence: `/app/outputs/configurations_summary.txt`

### Step 4: Compute normal modes for each configuration
- Role: process
- Action: For each random configuration, construct the dynamical matrix using the force constants from step02, diagonalise it (size up to 540×540) to obtain phonon frequencies ω_j and polarization vectors σ_d^j for the q=0 equivalent point. Record a summary of the optical bandwidth or number of modes.
- Evidence: `/app/outputs/normal_modes_summary.txt`

### Step 5: Compute scattering intensity per configuration
- Role: process
- Action: For each configuration, evaluate the one-phonon coherent scattering law S1(κ, ω) for the three specified κ points (zone boundary (3,0,0), zone center (4,0,0), longitudinal (3.333...,0,0)). Include the incoherent inelastic scattering contribution, Debye-Waller factors obtained by integrating the frequency spectrum with eigenvector weighting, and apply the thermal factor at T=80 K. Build histograms of intensity vs energy (energy bin width ~0.5 meV). Save per-sample histograms as intermediate evidence.
- Evidence: `/app/outputs/intensity_sample_summary.txt`

### Step 6: Ensemble average and convolve
- Role: process
- Action: Average the intensity histograms over all configurations (25 samples) to obtain the final line shape for each κ point. Convolve the averaged curve with a Gaussian representing the instrumental energy resolution (FWHM ≈ 3 meV). Optionally normalise the area under each curve. Save intermediate visualisation of the raw averaged curves.
- Evidence: `/app/outputs/averaged_intensity.png`

### Step 7: Output final intensity profile – [100] zone boundary
- Role: scored (load-bearing)
- Action: Write the convolved, normalised intensity vs energy transfer for κ=(3,0,0), the [100] zone boundary point. Save as CSV.
- Output file: `/app/outputs/zone_boundary_100.csv`
- Format: csv
- Contract: Required columns: energy_meV (float), intensity (float).
- Scoring: scored by hidden verifier

### Step 8: Output final intensity profile – zone center
- Role: scored
- Action: Write the convolved, normalised intensity vs energy transfer for κ=(4,0,0), the zone center point. Save as CSV.
- Output file: `/app/outputs/zone_center_400.csv`
- Format: csv
- Contract: Required columns: energy_meV (float), intensity (float).
- Scoring: scored by hidden verifier

### Step 9: Output final intensity profile – longitudinal point
- Role: scored
- Action: Write the convolved, normalised intensity vs energy transfer for κ=(3.333...,0,0) (approximately (3⅓,0,0)), the longitudinal point. Save as CSV.
- Output file: `/app/outputs/longitudinal_313_0.csv`
- Format: csv
- Contract: Required columns: energy_meV (float), intensity (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/force_constants.csv`
- `/app/outputs/zone_boundary_100.csv`
- `/app/outputs/zone_center_400.csv`
- `/app/outputs/longitudinal_313_0.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### force_constants.csv
- path: `/app/outputs/force_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Fitted Born-von Kármán force constants from the Pd4D3 nonstoichiometric model, including the D-D first-neighbor ratio. The hidden checker compares the D-D first-neighbor ratio to the paper's reported value (~1.5) within a tolerance; structural check (one exact-match ratio).
- schema:
  - `type`: table
  - `required_columns`: `parameter_name`, `fitted_value`, `stoichiometric_value`, `ratio`
  - `units`:
    - `fitted_value`: force constant (arbitrary units)
    - `stoichiometric_value`: force constant (arbitrary units)
    - `ratio`: dimensionless

### zone_boundary_100.csv
- path: `/app/outputs/zone_boundary_100.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed neutron scattering intensity profile for the [100] zone boundary (κ=(3,0,0)) at T=80 K. The hidden checker audits structural features: acoustic-mode peak position and optical-mode energy spread (weighted standard deviation), not a recomputed MAE.
- schema:
  - `type`: table
  - `required_columns`: `energy_meV`, `intensity`
  - `units`:
    - `energy_meV`: meV
    - `intensity`: arbitrary normalised unit

### zone_center_400.csv
- path: `/app/outputs/zone_center_400.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed neutron scattering intensity profile for the zone center (κ=(4,0,0)) at T=80 K. The hidden checker audits the full width at half maximum (FWHM) of the optical peak in a specified energy window.
- schema:
  - `type`: table
  - `required_columns`: `energy_meV`, `intensity`
  - `units`:
    - `energy_meV`: meV
    - `intensity`: arbitrary normalised unit

### longitudinal_313_0.csv
- path: `/app/outputs/longitudinal_313_0.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed neutron scattering intensity profile for the longitudinal point (κ≈(3.333,0,0)) at T=80 K. The hidden checker audits structural broadness (energy-weighted standard deviation) over the optical-mode region.
- schema:
  - `type`: table
  - `required_columns`: `energy_meV`, `intensity`
  - `units`:
    - `energy_meV`: meV
    - `intensity`: arbitrary normalised unit

Notes: The force_constants.csv row for the D-D first-neighbor is scored against the paper's increased ratio (~1.5). The three intensity CSV files are checked for structural properties (peak position, broadness, FWHM) consistent with the paper's claims of sharp acoustic feature and broad optical linewidths; no MAE recompute against digitized experimental data is performed. The agent must average over at least 25 random configurations, use the fitted force constants, and convolve with a Gaussian of FWHM ~3 meV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "force_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter_name",
          "fitted_value",
          "stoichiometric_value",
          "ratio"
        ],
        "units": {
          "fitted_value": "force constant (arbitrary units)",
          "stoichiometric_value": "force constant (arbitrary units)",
          "ratio": "dimensionless"
        }
      },
      "description": "Fitted Born-von Kármán force constants from the Pd4D3 nonstoichiometric model, including the D-D first-neighbor ratio. The hidden checker compares the D-D first-neighbor ratio to the paper's reported value (~1.5) within a tolerance; structural check (one exact-match ratio)."
    },
    {
      "file": "zone_boundary_100.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_meV",
          "intensity"
        ],
        "units": {
          "energy_meV": "meV",
          "intensity": "arbitrary normalised unit"
        }
      },
      "description": "Computed neutron scattering intensity profile for the [100] zone boundary (κ=(3,0,0)) at T=80 K. The hidden checker audits structural features: acoustic-mode peak position and optical-mode energy spread (weighted standard deviation), not a recomputed MAE."
    },
    {
      "file": "zone_center_400.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_meV",
          "intensity"
        ],
        "units": {
          "energy_meV": "meV",
          "intensity": "arbitrary normalised unit"
        }
      },
      "description": "Computed neutron scattering intensity profile for the zone center (κ=(4,0,0)) at T=80 K. The hidden checker audits the full width at half maximum (FWHM) of the optical peak in a specified energy window."
    },
    {
      "file": "longitudinal_313_0.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_meV",
          "intensity"
        ],
        "units": {
          "energy_meV": "meV",
          "intensity": "arbitrary normalised unit"
        }
      },
      "description": "Computed neutron scattering intensity profile for the longitudinal point (κ≈(3.333,0,0)) at T=80 K. The hidden checker audits structural broadness (energy-weighted standard deviation) over the optical-mode region."
    }
  ],
  "notes": "The force_constants.csv row for the D-D first-neighbor is scored against the paper's increased ratio (~1.5). The three intensity CSV files are checked for structural properties (peak position, broadness, FWHM) consistent with the paper's claims of sharp acoustic feature and broad optical linewidths; no MAE recompute against digitized experimental data is performed. The agent must average over at least 25 random configurations, use the fitted force constants, and convolve with a Gaussian of FWHM ~3 meV."
}
```

## How you are scored
A hidden verifier independently inspects each scored artifact. The force_constants.csv is checked: the D-D first-neighbor ratio is compared to a hidden reference value derived from the original study. Each intensity CSV is compared to digitised experimental scans; the area-normalised mean absolute error over a fixed energy window and checks on the acoustic peak position and optical-peak width contribute to the score. No single metric needs to be matched exactly; the final reward is a weighted combination of these per-artifact scores. The verifier reads only the submitted files – it does not require the agent to self-report any numeric result.
