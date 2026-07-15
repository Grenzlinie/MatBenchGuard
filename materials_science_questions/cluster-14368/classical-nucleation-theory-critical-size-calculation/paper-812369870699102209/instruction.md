# Heterogeneous Nucleation Probability and Contact Parameter Limits in Classical Nucleation Theory

## Problem background
Polar stratospheric clouds (PSCs) influence ozone chemistry through heterogeneous reactions. One proposed formation mechanism is the heterogeneous nucleation of nitric acid trihydrate (NAT) or supercooled binary HNO₃–H₂O solution (SBS) onto pre-existing solid sulfuric acid tetrahydrate (SAT) particles. Classical nucleation theory provides the framework to compute the contact parameter m required for a nucleating phase to appear on a substrate and to estimate upper bounds on m from surface energies. The problem is to determine whether such nucleation is efficient under typical stratospheric conditions. This requires computing, at 192 K for pressures of 100 mbar and 50 mbar, the threshold contact parameter m for which the nucleation probability of NAT and SBS approaches unity within one hour, and to estimate the maximum possible values of m for the NAT–SAT and SBS–SAT interfaces based on surface energy considerations. By comparing these required thresholds with the estimated upper limits, one can assess the feasibility of heterogeneous nucleation as a pathway for PSC formation.

## Approach
The computational approach is rooted in classical heterogeneous nucleation theory (Fletcher, 1958). First, solid-vapor surface energies for NAT, SBS, and SAT are derived by combining liquid-vapor surface tensions from published correlations (Sabinina & Terpugov for H₂SO₄–H₂O, Granzhan & Laktionova for HNO₃–H₂O) with solid-liquid surface energies obtained from the empirical Turnbull correlation (b = 0.32), and using Antonoff‘s rule. These surface energies, together with standard expressions for critical cluster free energy and nucleation rate, are then used to compute the heterogeneous nucleation probability P as a function of the contact parameter m. The probability is evaluated for a given particle radius, ambient vapor mixing ratios of HNO₃ and H₂O, temperature, nucleation time, and two total pressures. From the resulting probability curves, the threshold m where P reaches unity can be extracted.

In parallel, upper limits for the contact parameters between SAT and NAT, and between SAT and SBS, are obtained from Young’s equation. A conservative estimate adopts temperature-independent solid-vapor surface energies (the primed values) and assumes that the solid-solid surface energy is at least as large as the solid-liquid surface energy between SBS and NAT. The computed thresholds and upper limits together provide a basis for evaluating whether nucleation can proceed efficiently.

## Reproduction target
The concrete deliverable is three scored output files:

*   `m_upper_limits.json`: a JSON file containing the estimated upper limits `m_NAT_SAT` and `m_SBS_SAT` (dimensionless floats).
*   `nucleation_probability_NAT.csv`: a CSV table with columns `m`, `P_100mbar`, `P_50mbar`, providing the nucleation probability of NAT for `m` from 0 to 1 in steps of 0.01.
*   `nucleation_probability_SBS.csv`: the analogous table for SBS.

The hidden verifier will extract from the CSVs the minimum `m` at which the nucleation probability reaches or exceeds 0.9999, separately for each substance and pressure, and will compare these four threshold values to reference thresholds. It will also compare the two upper limits from the JSON file to reference limits. Finally, it will perform a structural check that each extracted threshold exceeds its corresponding upper limit.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute surface energies
- Role: process
- Action: Calculate solid-vapor surface energies for NAT, SBS, and SAT, and the solid-liquid surface energy between SBS and NAT, using the Turnbull empirical correlation (b=0.32), Antonoff's rule, and published liquid-vapor surface tension formulas for H2SO4-H2O (Sabinina and Terpugov 1935) and HNO3-H2O (Granzhan and Laktionova 1975). Use required enthalpies of fusion and molar volumes at 192 K. Compute also the primed (sensitivity) surface energies. Write the complete set of computed values to a structured evidence file for downstream use.
- Evidence: `/app/outputs/surface_energies.json`

### Step 2: Estimate contact parameter upper limits
- Role: scored (load-bearing)
- Action: Using the surface energies computed in the previous step and Young's equation, derive upper limits for the contact parameters m_SAT,NAT and m_SAT,SBS at 192 K. Assume that the solid-solid surface energy is at least as high as the solid-liquid surface energy between SBS and NAT. Adopt the primed (sensitivity) surface energy values as the conservative upper bounds. Write the resulting limits to m_upper_limits.json.
- Output file: `/app/outputs/m_upper_limits.json`
- Format: json
- Contract: JSON object with keys: m_NAT_SAT (float), m_SBS_SAT (float).
- Scoring: scored by hidden verifier

### Step 3: Compute NAT heterogeneous nucleation probability
- Role: scored (load-bearing)
- Action: For NAT (solid phase), compute the nucleation probability P as a function of the contact parameter m (from 0 to 1 in steps of 0.01) at temperature 192 K, HNO3 mixing ratio 10 ppbv, H2O mixing ratio 4.5 ppmv, particle radius 0.5 μm, nucleation time 1 hour, and pressures 100 mbar and 50 mbar. Use the classical heterogeneous nucleation theory formulas with the surface energies from step_01. Write the probability curve to a CSV file with columns m, P_100mbar, P_50mbar.
- Output file: `/app/outputs/nucleation_probability_NAT.csv`
- Format: csv
- Contract: CSV with columns: m (float), P_100mbar (float), P_50mbar (float). Row for each m value 0 to 1 step 0.01.
- Scoring: scored by hidden verifier

### Step 4: Compute SBS heterogeneous nucleation probability
- Role: scored (load-bearing)
- Action: For SBS (liquid phase), compute the nucleation probability P as a function of the contact parameter m (from 0 to 1 in steps of 0.01) under the same conditions as step_03: temperature 192 K, HNO3 10 ppbv, H2O 4.5 ppmv, particle radius 0.5 μm, time 1 hour, at 100 mbar and 50 mbar. Use the classical heterogeneous binary nucleation formulas with surface energies from step_01. Write the probability curve to a CSV file with columns m, P_100mbar, P_50mbar.
- Output file: `/app/outputs/nucleation_probability_SBS.csv`
- Format: csv
- Contract: CSV with columns: m (float), P_100mbar (float), P_50mbar (float). Row for each m value 0 to 1 step 0.01.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/m_upper_limits.json`
- `/app/outputs/nucleation_probability_NAT.csv`
- `/app/outputs/nucleation_probability_SBS.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### m_upper_limits.json
- path: `/app/outputs/m_upper_limits.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Estimated upper limits for the contact parameters between SAT and NAT, and between SAT and SBS at 192 K.
- schema:
  - `type`: object
  - `required`:
    - `m_NAT_SAT`: float
    - `m_SBS_SAT`: float

### nucleation_probability_NAT.csv
- path: `/app/outputs/nucleation_probability_NAT.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Calculated nucleation probability for NAT as a function of contact parameter m at 100 mbar and 50 mbar.
- schema:
  - `type`: table
  - `required_columns`: `m`, `P_100mbar`, `P_50mbar`
  - `units`:
    - `m`: dimensionless
    - `P_100mbar`: dimensionless probability
    - `P_50mbar`: dimensionless probability

### nucleation_probability_SBS.csv
- path: `/app/outputs/nucleation_probability_SBS.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Calculated nucleation probability for SBS as a function of contact parameter m at 100 mbar and 50 mbar.
- schema:
  - `type`: table
  - `required_columns`: `m`, `P_100mbar`, `P_50mbar`
  - `units`:
    - `m`: dimensionless
    - `P_100mbar`: dimensionless probability
    - `P_50mbar`: dimensionless probability

Notes: All scored outputs are compared against hidden gold values from the reference publication. The CSV files are used to recompute the threshold m where probability first reaches 1; that recomputed threshold is then checked against the reported gold thresholds. The upper limits JSON is checked for proximity to the reported limits. No solver or paper-specific identification is included.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "m_upper_limits.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "m_NAT_SAT": "float",
          "m_SBS_SAT": "float"
        }
      },
      "description": "Estimated upper limits for the contact parameters between SAT and NAT, and between SAT and SBS at 192 K."
    },
    {
      "file": "nucleation_probability_NAT.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "P_100mbar",
          "P_50mbar"
        ],
        "units": {
          "m": "dimensionless",
          "P_100mbar": "dimensionless probability",
          "P_50mbar": "dimensionless probability"
        }
      },
      "description": "Calculated nucleation probability for NAT as a function of contact parameter m at 100 mbar and 50 mbar."
    },
    {
      "file": "nucleation_probability_SBS.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "P_100mbar",
          "P_50mbar"
        ],
        "units": {
          "m": "dimensionless",
          "P_100mbar": "dimensionless probability",
          "P_50mbar": "dimensionless probability"
        }
      },
      "description": "Calculated nucleation probability for SBS as a function of contact parameter m at 100 mbar and 50 mbar."
    }
  ],
  "notes": "All scored outputs are compared against hidden gold values from the reference publication. The CSV files are used to recompute the threshold m where probability first reaches 1; that recomputed threshold is then checked against the reported gold thresholds. The upper limits JSON is checked for proximity to the reported limits. No solver or paper-specific identification is included."
}
```

## How you are scored
A hidden verifier reads your submitted output files. From the two CSV files, it computes the minimum `m` where `P` ≥ 0.9999 for each substance–pressure combination; these extracted thresholds are compared to hidden reference thresholds, with credit awarded according to accuracy. The values in `m_upper_limits.json` are compared to reference upper limits under a similar accuracy criterion. In addition, the structural condition that each threshold exceeds its corresponding upper limit is verified. The overall reward is a weighted sum of these components. Simply reporting plausible numbers without correct underlying curves will not yield a high score, because the thresholds are recomputed from the submitted probability data.
