# ZT Simulation of Zinc Phosphate Glass/Graphite Composites via GEMT

## Problem background
In thermoelectric composites, the dimensionless figure of merit ZT combines electrical conductivity σ, Seebeck coefficient S, and thermal conductivity κ to quantify energy conversion efficiency. Zinc phosphate glass (ZPG) is a promising matrix due to its high Seebeck coefficient, but it suffers from very low electrical conductivity. Adding conductive graphite fillers can dramatically improve electrical transport, but the interplay between percolation thresholds for different transport properties may lead to a non-monotonic dependence of ZT on filler volume fraction. This task addresses the computational prediction of ZT in ZPG/graphite composites as a function of graphite loading, testing whether a shift between the electrical percolation threshold and the κ/S percolation threshold can give rise to a ZT peak.

## Approach
The effective transport properties of the composite are calculated using the generalized effective medium theory (GEMT). The electrical conductivity follows the McLachlan equation with a percolation threshold φ_σ and critical exponent t_σ. Thermal conductivity is described by a Landauer-type equation without percolation. A third GEMT equation models the ratio κ/S (thermal conductivity divided by Seebeck coefficient) with its own percolation threshold φ_κ/S. The matrix and filler properties (conductivities, κ/S ratios) and the critical exponents are fixed to values obtained from the paper's experimental fits. For a range of filler volume fractions from 0% to 12%, the three implicit equations are solved to obtain effective σ_e, κ_e, and (κ/S)_e. The effective Seebeck coefficient is then derived as S_e = κ_e/(κ/S)_e, and ZT is computed as ZT = (σ_e · S_e² · T)/κ_e with T = 300 K. Two configurations are explored: (1) the shifted-threshold case with φ_σ = 0.035 and φ_κ/S = 0.06, and (2) a baseline no-shift case where both thresholds are set to 0.06. The comparison reveals how the offset between percolation thresholds influences ZT.

## Reproduction target
Produce two comma-separated value tables (step_01_zt_vs_filler.csv and step_02_zt_noshift.csv) containing the computed σ_e, κ_e, κ/S_e, S_e, and ZT for every 0.5 vol.% increment from 0% to 12% graphite loading for each threshold scenario. Additionally, generate a summary text file (step_03_summary.txt) reporting the maximum ZT and its filler fraction for both cases. The objective is to quantify the ZT maximum that emerges from the shifted percolation thresholds and to confirm that no comparable maximum arises when the thresholds coincide.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute ZT with shifted percolation thresholds
- Role: scored (load-bearing)
- Action: Implement the GEMT models for effective electrical conductivity (McLachlan equation), effective thermal conductivity (Landauer equation), and effective κ/S ratio (Sonntag equation). Use the following parameters explicitly reported in the paper: electrical percolation threshold φ_σ = 0.035, critical exponent t_σ = 2.1, matrix electrical conductivity σ_m = 1.34×10⁻⁵ S/m, filler electrical conductivity σ_f = 500.07 S/m; thermal conductivity (no percolation) with t_κ = 1, A_κ = 2, matrix thermal conductivity κ_m = 0.63 W/m/K, filler thermal conductivity κ_f = 31.2 W/m/K; κ/S percolation threshold φ_κ/S = 0.06, critical exponent t_κ/S = 1, matrix ratio κ_m/S_m = 1.15×10⁻⁴ W/m/μV, filler ratio κ_f/S_f = 1.2 W/m/μV. For graphite volume fractions from 0% to 12% in steps of 0.5%, solve each implicit GEMT equation for the effective composite values (σ_e, κ_e, κ/S_e), derive the effective Seebeck coefficient S_e = κ_e / (κ/S)_e, and compute the dimensionless figure of merit ZT = (σ_e × S_e² × T) / κ_e at T = 300 K. Write the resulting table to the output CSV.
- Output file: `/app/outputs/step_01_zt_vs_filler.csv`
- Format: csv
- Contract: filler_vol_percent: float (0 to 12, step 0.5)
sigma_e: float (S/m)
kappa_e: float (W/m/K)
kappa_S_e: float (W/m/μV)
Seebeck_e: float (μV/K)
ZT: float (dimensionless)
- Scoring: scored by hidden verifier

### Step 2: Compute ZT without percolation-threshold shift
- Role: scored
- Action: Using the identical GEMT models and all other parameters unchanged, set both percolation thresholds equal: φ_σ = φ_κ/S = 0.06. Solve the equations for effective σ_e, κ_e, κ/S_e at the same filler volume fraction grid (0–12 vol.%, step 0.5%). Derive S_e and compute ZT at T=300 K. Write the results to the output CSV.
- Output file: `/app/outputs/step_02_zt_noshift.csv`
- Format: csv
- Contract: filler_vol_percent: float (0 to 12, step 0.5)
sigma_e: float (S/m)
kappa_e: float (W/m/K)
kappa_S_e: float (W/m/μV)
Seebeck_e: float (μV/K)
ZT: float (dimensionless)
- Scoring: scored by hidden verifier

### Step 3: Summarize peak ZT values
- Role: scored
- Action: From the computed ZT data in step_01 and step_02, extract the maximum ZT value and the filler volume percent at which it occurs. Write a two-line text file: the first line reports the peak ZT and its filler content for the shifted case, the second line for the no-shift case. If no clear peak exists, report the maximum ZT and its location anyway.
- Output file: `/app/outputs/step_03_summary.txt`
- Format: txt
- Contract: Two lines, each formatted as 'Peak ZT (<case>): <value> at <filler_vol_percent>'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_zt_vs_filler.csv`
- `/app/outputs/step_02_zt_noshift.csv`
- `/app/outputs/step_03_summary.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_zt_vs_filler.csv
- path: `/app/outputs/step_01_zt_vs_filler.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of ZT and intermediate effective transport properties as a function of filler content for the shifted-threshold scenario. The hidden checker will extract the peak ZT, verify it falls at 5 ± 0.5 vol.% and is within tolerance of the paper-reported 2.64×10⁻⁴, and confirm the curve exhibits a clear maximum.
- schema:
  - `type`: table
  - `required_columns`: `filler_vol_percent`, `sigma_e`, `kappa_e`, `kappa_S_e`, `Seebeck_e`, `ZT`
  - `units`:
    - `filler_vol_percent`: % (by volume)
    - `sigma_e`: S/m
    - `kappa_e`: W/m/K
    - `kappa_S_e`: W/m/μV
    - `Seebeck_e`: μV/K
    - `ZT`: dimensionless

### step_02_zt_noshift.csv
- path: `/app/outputs/step_02_zt_noshift.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of ZT and intermediate effective transport properties as a function of filler content for the coincident-threshold scenario. The hidden checker will verify that no peak comparable to the shifted case appears (ZT should be monotonic or exhibit a much lower maximum).
- schema:
  - `type`: table
  - `required_columns`: `filler_vol_percent`, `sigma_e`, `kappa_e`, `kappa_S_e`, `Seebeck_e`, `ZT`
  - `units`:
    - `filler_vol_percent`: % (by volume)
    - `sigma_e`: S/m
    - `kappa_e`: W/m/K
    - `kappa_S_e`: W/m/μV
    - `Seebeck_e`: μV/K
    - `ZT`: dimensionless

### step_03_summary.txt
- path: `/app/outputs/step_03_summary.txt`
- format: txt
- purpose: scored
- target_policy: structural_audit
- description: Plain-text summary of the peak ZT values and their locations extracted from the two simulation scenarios. The hidden checker will verify consistency with the corresponding CSV files (i.e., the reported peak values and filler percentages match the data in step_01_zt_vs_filler.csv and step_02_zt_noshift.csv).
- schema:
  - `type`: text

Notes: All three output files are scored; the main load-bearing artifact is step_01_zt_vs_filler.csv. The fitted GEMT parameters are taken as given from the paper (publicly reported) and are not produced by an upstream step. The scoring tolerances and specific reference values are hidden and are based on the paper’s reported peak ZT (2.64×10⁻⁴ at 5 vol.%) and the expected qualitative difference between the two threshold scenarios.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_zt_vs_filler.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "filler_vol_percent",
          "sigma_e",
          "kappa_e",
          "kappa_S_e",
          "Seebeck_e",
          "ZT"
        ],
        "units": {
          "filler_vol_percent": "% (by volume)",
          "sigma_e": "S/m",
          "kappa_e": "W/m/K",
          "kappa_S_e": "W/m/μV",
          "Seebeck_e": "μV/K",
          "ZT": "dimensionless"
        }
      },
      "description": "Table of ZT and intermediate effective transport properties as a function of filler content for the shifted-threshold scenario. The hidden checker will extract the peak ZT, verify it falls at 5 ± 0.5 vol.% and is within tolerance of the paper-reported 2.64×10⁻⁴, and confirm the curve exhibits a clear maximum."
    },
    {
      "file": "step_02_zt_noshift.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "filler_vol_percent",
          "sigma_e",
          "kappa_e",
          "kappa_S_e",
          "Seebeck_e",
          "ZT"
        ],
        "units": {
          "filler_vol_percent": "% (by volume)",
          "sigma_e": "S/m",
          "kappa_e": "W/m/K",
          "kappa_S_e": "W/m/μV",
          "Seebeck_e": "μV/K",
          "ZT": "dimensionless"
        }
      },
      "description": "Table of ZT and intermediate effective transport properties as a function of filler content for the coincident-threshold scenario. The hidden checker will verify that no peak comparable to the shifted case appears (ZT should be monotonic or exhibit a much lower maximum)."
    },
    {
      "file": "step_03_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "text"
      },
      "description": "Plain-text summary of the peak ZT values and their locations extracted from the two simulation scenarios. The hidden checker will verify consistency with the corresponding CSV files (i.e., the reported peak values and filler percentages match the data in step_01_zt_vs_filler.csv and step_02_zt_noshift.csv)."
    }
  ],
  "notes": "All three output files are scored; the main load-bearing artifact is step_01_zt_vs_filler.csv. The fitted GEMT parameters are taken as given from the paper (publicly reported) and are not produced by an upstream step. The scoring tolerances and specific reference values are hidden and are based on the paper’s reported peak ZT (2.64×10⁻⁴ at 5 vol.%) and the expected qualitative difference between the two threshold scenarios."
}
```

## How you are scored
Each output artifact is evaluated by a hidden verifier. The CSV for the shifted-threshold scenario is checked for the presence of a well-defined ZT maximum; its location (filler volume percent) and magnitude are compared against a reference using tolerance thresholds. The CSV for the no-shift scenario is checked to ensure that it lacks a peak of comparable magnitude. The summary text file is verified for consistency with the CSV data. The final score is a weighted sum of these individual checks. The verifier does not accept a simple restatement of numbers; it validates that the artifacts result from a correct implementation of the GEMT equations.
