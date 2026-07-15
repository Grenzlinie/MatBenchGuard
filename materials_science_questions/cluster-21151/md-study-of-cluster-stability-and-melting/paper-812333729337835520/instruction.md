# Power Spectra of Atomic Potential-Energy Fluctuations in Rare-Gas Clusters

## Problem background
Small rare-gas clusters exhibit a solid-to-liquid transition with increasing temperature. In the liquid-like state, the dynamics may become complex, potentially giving rise to long-range temporal correlations. This task investigates the power spectra of individual atomic potential-energy fluctuations in 55-atom Lennard-Jones clusters—pure Xe55 and impurity-doped ArXe54—via molecular dynamics simulations. The goal is to determine the spectral shape in the liquid state and how the presence of a confined impurity atom modifies the frequency dependence.

## Approach
The approach uses classical molecular dynamics (MD) with Lennard-Jones interatomic potentials. Two systems are studied: a pure Xe55 cluster and a mixed ArXe54 cluster where one central Xe atom is replaced by an Ar impurity. Icosahedral starting structures are built, and NVE dynamics are used to equilibrate each cluster near its liquid-like temperature (≈69.6 K for Xe55, ≈68 K for ArXe54). Production trajectories of sufficient length are generated. From the trajectories, the time series of the total potential energy of individual atoms is extracted, and power spectra are computed via fast Fourier transform. For Xe atoms the spectra are averaged over all atoms. The three output spectra capture: (1) the averaged Xe spectrum in pure Xe55, (2) the spectrum of the single Ar impurity in ArXe54, and (3) the averaged Xe spectrum in ArXe54. Comparing these three cases reveals how atomic mobility and confinement influence the frequency content of the potential-energy fluctuations.

## Reproduction target
Produce three CSV files containing power spectra for the systems described above:

- `/app/outputs/step_01_power_spectrum_xe55.csv` : averaged Xe spectrum in Xe55 at T≈69.6 K
- `/app/outputs/step_02_power_spectrum_ar_arxexe.csv` : Ar impurity spectrum in ArXe54 at T=68 K
- `/app/outputs/step_03_power_spectrum_xe_arxexe.csv` : averaged Xe spectrum in ArXe54 at T=68 K

Each file must contain two columns, `frequency` (positive, increasing, in reduced units) and `power` (arbitrary units). The verifier will compute the log-log slope of each spectrum over a low-frequency interval and check whether the Xe and Ar spectra exhibit distinctly different slopes, consistent with the liquid-state dynamics described in the approach.

## Assets

- Lennard-Jones potential parameters for Ar-Ar, Ar-Xe, Xe-Xe

## Workflow steps

### Step 1: Build initial atomic structures and define force field
- Role: process
- Action: Construct icosahedral coordinates for a 55-atom Xe cluster. For the mixed ArXe54 cluster, replace one Xe atom (the central one) by Ar. Define the Lennard-Jones potential parameters as given in resource lj_params.
- Evidence: none

### Step 2: Molecular dynamics simulation of pure Xe55 cluster
- Role: process
- Action: Equilibrate the Xe55 cluster at temperature ~69.6 K using NVE dynamics with the defined LJ potentials, then run a production trajectory of sufficient length (at least 10^5 MD steps after equilibration) to resolve low-frequency spectral features, storing atomic positions and velocities.
- Evidence: none

### Step 3: Molecular dynamics simulation of impurity-doped ArXe54 cluster
- Role: process
- Action: Equilibrate the ArXe54 cluster at temperature ~68 K using NVE dynamics, then run a production trajectory of similar length, saving atomic positions and velocities.
- Evidence: none

### Step 4: Power spectrum of Xe in Xe55
- Role: scored (load-bearing)
- Action: From the Xe55 production trajectory, compute the potential energy V_i(t) for every Xe atom. Compute the power spectrum via FFT for each atom, average over all atoms, and output the averaged spectrum.
- Output file: `/app/outputs/step_01_power_spectrum_xe55.csv`
- Format: csv
- Contract: Two columns: 'frequency' (float) and 'power' (float). No header row needed but recommended. Frequency values must be positive and in increasing order over a range that resolves the 1/f region.
- Scoring: scored by hidden verifier

### Step 5: Power spectrum of Ar impurity in ArXe54
- Role: scored
- Action: From the ArXe54 production trajectory, compute the potential energy V_Ar(t) for the single Ar atom. Compute its power spectrum via FFT and output.
- Output file: `/app/outputs/step_02_power_spectrum_ar_arxexe.csv`
- Format: csv
- Contract: Two columns: 'frequency' (float) and 'power' (float). No header row needed but recommended.
- Scoring: scored by hidden verifier

### Step 6: Power spectrum of Xe in ArXe54
- Role: scored
- Action: From the ArXe54 production trajectory, compute the potential energy V_i(t) for all Xe atoms. Compute the power spectrum for each, average over all Xe atoms, and output the averaged spectrum.
- Output file: `/app/outputs/step_03_power_spectrum_xe_arxexe.csv`
- Format: csv
- Contract: Two columns: 'frequency' (float) and 'power' (float). No header row needed but recommended.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_power_spectrum_xe55.csv`
- `/app/outputs/step_02_power_spectrum_ar_arxexe.csv`
- `/app/outputs/step_03_power_spectrum_xe_arxexe.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_power_spectrum_xe55.csv
- path: `/app/outputs/step_01_power_spectrum_xe55.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Averaged power spectrum of individual Xe atom potential-energy fluctuations in the pure Xe55 cluster at T~69.6 K. Contains frequency (positive, increasing) and corresponding power.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `power`
  - `units`:
    - `frequency`: reduced units
    - `power`: arbitrary units
  - `items`: object

### step_02_power_spectrum_ar_arxexe.csv
- path: `/app/outputs/step_02_power_spectrum_ar_arxexe.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Power spectrum of the Ar impurity atom's potential-energy fluctuations in the ArXe54 cluster at T=68 K.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `power`
  - `units`:
    - `frequency`: reduced units
    - `power`: arbitrary units
  - `items`: object

### step_03_power_spectrum_xe_arxexe.csv
- path: `/app/outputs/step_03_power_spectrum_xe_arxexe.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Averaged power spectrum of Xe atom potential-energy fluctuations in the ArXe54 cluster at T=68 K.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `power`
  - `units`:
    - `frequency`: reduced units
    - `power`: arbitrary units
  - `items`: object

Notes: Only the power spectra are scored; radial distributions and multi-Gaussian fits are not required. The submitted CSV files must contain two columns (frequency and power) and allow the checker to perform a log-log linear fit to extract the spectral slope. No header is required but it is recommended for clarity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_power_spectrum_xe55.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "power"
        ],
        "units": {
          "frequency": "reduced units",
          "power": "arbitrary units"
        },
        "items": {}
      },
      "description": "Averaged power spectrum of individual Xe atom potential-energy fluctuations in the pure Xe55 cluster at T~69.6 K. Contains frequency (positive, increasing) and corresponding power."
    },
    {
      "file": "step_02_power_spectrum_ar_arxexe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "power"
        ],
        "units": {
          "frequency": "reduced units",
          "power": "arbitrary units"
        },
        "items": {}
      },
      "description": "Power spectrum of the Ar impurity atom's potential-energy fluctuations in the ArXe54 cluster at T=68 K."
    },
    {
      "file": "step_03_power_spectrum_xe_arxexe.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "power"
        ],
        "units": {
          "frequency": "reduced units",
          "power": "arbitrary units"
        },
        "items": {}
      },
      "description": "Averaged power spectrum of Xe atom potential-energy fluctuations in the ArXe54 cluster at T=68 K."
    }
  ],
  "notes": "Only the power spectra are scored; radial distributions and multi-Gaussian fits are not required. The submitted CSV files must contain two columns (frequency and power) and allow the checker to perform a log-log linear fit to extract the spectral slope. No header is required but it is recommended for clarity."
}
```

## How you are scored
Your submission is scored by a hidden verifier that processes only the three CSV output files. For each scored spectrum, the verifier fits a straight line to the log-log plot of power versus frequency over a predetermined frequency interval (excluding the very lowest and highest frequencies). The slope obtained from the fit is compared to the expected behavior, and a partial reward is assigned for each file. The final reward is a weighted sum of the three partial rewards. The verifier does not inspect intermediate trajectory data or simulation code; only the CSV outputs determine the score. Reporting a number from the literature without actually running the required MD simulations will not pass the verifier, because the slopes are recomputed from the submitted data and must satisfy specific structural criteria.
