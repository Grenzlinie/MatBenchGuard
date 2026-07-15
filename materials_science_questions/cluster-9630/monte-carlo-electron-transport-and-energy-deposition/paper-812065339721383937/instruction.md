# Muffin-tin vs isolated-atom DCS and elastic-backscattering probability for silicon

## Problem background
Computer simulations of electron transport in solids require accurate differential elastic-scattering cross sections (DCS). In practice, DCSs calculated for isolated neutral atoms are used, but interactions inside a solid are different. The muffin-tin potential provides a model for the solid-state environment. This task investigates the influence of the interaction potential on elastic-backscattering probabilities. For silicon at primary energies of 200, 500 and 1000 eV, the percentage deviation between DCSs from isolated-atom (Dirac–Hartree–Fock) and muffin-tin potentials is computed, and the resulting elastic-backscattering probabilities are obtained via Monte Carlo simulation. The computed probabilities are then compared to hidden experimental elastic-peak intensities to quantify the effect of the DCS model on the accuracy of the Monte Carlo predictions.

## Approach
The approach uses the ELSEPA program package to compute DCSs for silicon under two potentials: (i) an isolated neutral atom using the Dirac–Hartree–Fock (DHF) potential, and (ii) a muffin-tin potential with radius equal to half the silicon interatomic distance (2.351 Å). The Furness–McCarthy local exchange and a Fermi nuclear charge distribution are employed. From these, the percentage deviation ΔDCS = 100 × (DCSₙₐ − DCSₘₜ) / DCSₘₜ is evaluated across scattering angles.

Separate conventional forward Monte Carlo simulations of electron trajectories in amorphous silicon are then performed using each DCS set. Normal incidence of the primary beam is assumed, with an acceptance half-angle of 4.1° and 2 × 10⁷ trajectories per run. Inelastic mean free paths are taken from the TPP-2M formula or the NIST IMFP database. The elastic-backscattering probability η is recorded as a function of emission angle (0°–80°) at the three primary energies. The resulting η curves are to be compared, by the hidden verifier, to experimental elastic-peak intensities for silicon (provided as a hidden reference at the measured emission angles) by fitting a scaling factor that minimizes the sum of squared residuals and computing mean percentage deviations, as defined in the relevant literature.

## Reproduction target
Produce for silicon at primary kinetic energies 200 eV, 500 eV, and 1000 eV:

1. `dcs_delta_si.csv` – the percentage deviation ΔDCS between neutral-atom and muffin-tin DCS as a function of scattering angle.
2. `eta_na_si.csv` – the elastic-backscattering probability η vs. emission angle (0°–80°, fine resolution) using the neutral-atom DCS.
3. `eta_mt_si.csv` – the elastic-backscattering probability η vs. emission angle (0°–80°) using the muffin-tin DCS.

The hidden verifier will compare your ΔDCS values at selected scattering angles to digitized reference curves within a tolerance, and will use your η tables together with hidden experimental elastic-peak intensities for Si to fit scaling constants and compute mean percentage deviations. Your outputs must allow the verifier to perform these comparisons.

## Assets

- ELSEPA program package: Source code available from CPC Program Library (Salvat et al., Comput. Phys. Commun. 165, 2005) or as part of the NIST Electron Elastic-Scattering Cross-Section Database (SRD 64).
- Interatomic distance for silicon: From Pearson's Handbook of Lattice Spacing and Structures of Metals and Alloys; silicon (diamond structure) interatomic distance is 2.351 Å, used to set muffin-tin radius.
- Inelastic mean free path values: Use TPP-2M predictive formula (Tanuma et al., Surf. Interf. Anal. 21, 1994) or NIST Electron Inelastic-Mean-Free-Path Database (SRD 71).

## Workflow steps

### Step 1: Calculate differential elastic-scattering cross sections for silicon
- Role: process
- Action: Using the ELSEPA program package, compute differential elastic-scattering cross sections dσ/dΩ for silicon at primary electron kinetic energies 200 eV, 500 eV, and 1000 eV. Compute for two potentials: (i) isolated neutral atom using the Dirac–Hartree–Fock (DHF) potential, and (ii) muffin-tin potential with radius equal to half the interatomic distance (2.351 Å for Si). Use the Furness–McCarthy local exchange and a Fermi nuclear charge distribution. Save the resulting DCS tables as intermediate files.
- Evidence: `/app/outputs/dcs_na_si.csv, dcs_mt_si.csv`

### Step 2: Compute percentage deviation ΔDCS between muffin-tin and neutral-atom DCS
- Role: scored
- Action: From the DCS tables produced in step_01, compute the percentage deviation defined as ΔDCS = 100 * (DCS_na – DCS_mt) / DCS_mt at each computed scattering angle for energies 200, 500, 1000 eV. Output the results as a single CSV file.
- Output file: `/app/outputs/dcs_delta_si.csv`
- Format: csv
- Contract: energy (eV), scattering_angle (deg), delta_DCS (percent)
- Scoring: scored by hidden verifier

### Step 3: Monte Carlo simulation of elastic-backscattering probability using neutral-atom DCS
- Role: scored (load-bearing)
- Action: Implement a conventional forward Monte Carlo simulation for electron trajectories in amorphous silicon using the neutral-atom DCS from step_01. Assume normal incidence, acceptance half-angle 4.1°, and generate 2×10⁷ trajectories. Use inelastic mean free paths from TPP-2M or NIST IMFP database. Compute the elastic-backscattering probability η as a function of emission angle (0°–80° with fine resolution, e.g., 1° bins) for energies 200, 500, and 1000 eV. Save the results.
- Output file: `/app/outputs/eta_na_si.csv`
- Format: csv
- Contract: energy (eV), emission_angle (deg), eta (dimensionless)
- Scoring: scored by hidden verifier

### Step 4: Monte Carlo simulation of elastic-backscattering probability using muffin-tin DCS
- Role: scored (load-bearing)
- Action: Repeat the Monte Carlo simulation of step_03, but using the muffin-tin DCS from step_01. All other parameters (normal incidence, half-angle 4.1°, 2×10⁷ trajectories, IMFP values) remain identical. Compute and save η at the same emission angle grid.
- Output file: `/app/outputs/eta_mt_si.csv`
- Format: csv
- Contract: energy (eV), emission_angle (deg), eta (dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dcs_delta_si.csv`
- `/app/outputs/eta_na_si.csv`
- `/app/outputs/eta_mt_si.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dcs_delta_si.csv
- path: `/app/outputs/dcs_delta_si.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Percentage difference ΔDCS between neutral-atom and muffin-tin DCS at 200, 500, 1000 eV over scattering angles. Checker compares at selected angles to reference values within ±10% relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `scattering_angle`, `delta_DCS`
  - `units`:
    - `energy`: eV
    - `scattering_angle`: degrees
    - `delta_DCS`: percent

### eta_na_si.csv
- path: `/app/outputs/eta_na_si.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Elastic-backscattering probability η for neutral-atom DCS as a function of emission angle. The checker interpolates at hidden experimental emission angles, fits a scaling factor C_na, and computes the mean percentage deviation R_na.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `emission_angle`, `eta`
  - `units`:
    - `energy`: eV
    - `emission_angle`: degrees
    - `eta`: dimensionless

### eta_mt_si.csv
- path: `/app/outputs/eta_mt_si.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Elastic-backscattering probability η for muffin-tin DCS. Checker similarly derives R_mt and compares both R_na and R_mt to the paper's reported values within ±1 percentage point.
- schema:
  - `type`: table
  - `required_columns`: `energy`, `emission_angle`, `eta`
  - `units`:
    - `energy`: eV
    - `emission_angle`: degrees
    - `eta`: dimensionless

Notes: The hidden checker possesses digitized experimental elastic-peak intensities for silicon at the three energies. It uses these intensities, together with the submitted eta curves, to fit scaling constants and compute R_na,R_mt per the paper's Eqs. (4a,b) and (5a,b). The agent does not need to output the experimental angles or the scaling factors.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dcs_delta_si.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "scattering_angle",
          "delta_DCS"
        ],
        "units": {
          "energy": "eV",
          "scattering_angle": "degrees",
          "delta_DCS": "percent"
        }
      },
      "description": "Percentage difference ΔDCS between neutral-atom and muffin-tin DCS at 200, 500, 1000 eV over scattering angles. Checker compares at selected angles to reference values within ±10% relative tolerance."
    },
    {
      "file": "eta_na_si.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "emission_angle",
          "eta"
        ],
        "units": {
          "energy": "eV",
          "emission_angle": "degrees",
          "eta": "dimensionless"
        }
      },
      "description": "Elastic-backscattering probability η for neutral-atom DCS as a function of emission angle. The checker interpolates at hidden experimental emission angles, fits a scaling factor C_na, and computes the mean percentage deviation R_na."
    },
    {
      "file": "eta_mt_si.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy",
          "emission_angle",
          "eta"
        ],
        "units": {
          "energy": "eV",
          "emission_angle": "degrees",
          "eta": "dimensionless"
        }
      },
      "description": "Elastic-backscattering probability η for muffin-tin DCS. Checker similarly derives R_mt and compares both R_na and R_mt to the paper's reported values within ±1 percentage point."
    }
  ],
  "notes": "The hidden checker possesses digitized experimental elastic-peak intensities for silicon at the three energies. It uses these intensities, together with the submitted eta curves, to fit scaling constants and compute R_na,R_mt per the paper's Eqs. (4a,b) and (5a,b). The agent does not need to output the experimental angles or the scaling factors."
}
```

## How you are scored
A hidden verifier scores each of your three output artifacts independently:

- For `dcs_delta_si.csv`, the verifier compares your ΔDCS at chosen scattering angles against reference data from the published work; a relative tolerance is applied.
- For `eta_na_si.csv` and `eta_mt_si.csv`, the verifier loads hidden experimental elastic-peak intensities (silicon, three energies, measured emission angles), interpolates your η values at those angles, fits a single scaling factor per model by minimizing the sum of squared residuals, and computes the mean absolute percentage deviation Rₙₐ and Rₘₜ.

Your final reward is a weighted combination of these scores. Reporting numbers that merely match the paper without genuine computation will not pass—the verifier cross-checks consistency and compares against reference quantities that are not disclosed to you.
