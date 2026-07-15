# Temperature Dependence of Phase-Matching Angle from SHG Intensity Data

## Problem background
NYAB (Nd:YAl3(BO3)4) is a self-frequency-doubling crystal used in compact diode-pumped green lasers. The temperature dependence of the phase-matching angle affects laser alignment and efficiency. Measuring the rate of change of the phase-matching angle with temperature (dθm/dT) and the corresponding acceptance widths is essential for thermal management and cavity design.

## Approach
The second-harmonic intensity follows a sinc^2 function of the wave-vector mismatch. Near the phase-matching condition, the mismatch is approximately linear in both the propagation angle and the temperature. By recording SHG intensity versus angle at several fixed temperatures (and versus temperature at a fixed angle), one can fit each trace to a sinc^2 model to extract the phase-matching angle and the angular/temperature sensitivity parameters. A linear regression of the extracted phase-matching angles against temperature yields dθm/dT. Independently, the ratio of the angular acceptance width to the temperature acceptance width (Δθ/ΔT) can be derived from the fitted sensitivity parameters and should theoretically agree with the directly measured dθm/dT.

## Reproduction target
Given the digitized SHG intensity vs. angle data at five temperatures (bundled as a CSV file) and SHG intensity vs. temperature data at a fixed propagation angle (bundled as a separate CSV file), your goal is to: (1) extract the phase-matching angles at each temperature by fitting a sinc^2 function; (2) perform linear regression of the phase-matching angle against temperature to obtain the slope dθm/dT and its uncertainty; (3) fit the temperature scan to a sinc^2 function to obtain the temperature sensitivity parameter; (4) compute the angular and temperature acceptance width–length products (Δθ·L and ΔT·L) and their ratio Δθ/ΔT; (5) compare the independently determined dθm/dT and Δθ/ΔT to assess the agreement predicted by the theoretical relation between them.

## Assets

- angle_scan_data.csv
- temperature_scan_data.csv
- scipy: scipy
- numpy: numpy

## Workflow steps

### Step 1: Fit sinc² to angle scans
- Role: process
- Action: Load angle_scan_data.csv, separate the five temperature scans, and fit each to a model of the form y = A + B·sinc²[C(x−D)] using least‑squares curve fitting. Extract the fitted parameters D (phase‑matching angle) and C for each temperature.
- Evidence: none

### Step 2: Output fitted angles
- Role: scored
- Action: Write the extracted phase‑matching angles (D) for each temperature to fitted_angles.json.
- Output file: `/app/outputs/fitted_angles.json`
- Format: json
- Contract: {"T_C": [float], "D_rad": [float]}
- Scoring: scored by hidden verifier

### Step 3: Linear regression of θm vs T
- Role: scored (load-bearing)
- Action: Perform linear least‑squares regression on the (T, D) pairs from the angle fits. Output the slope (dθm/dT), intercept, and rms residual.
- Output file: `/app/outputs/linear_regression_slope.json`
- Format: json
- Contract: {"slope_rad_per_C": float, "intercept_rad": float, "rms_residual_rad": float}
- Scoring: scored by hidden verifier

### Step 4: Fit sinc² to temperature scan
- Role: process
- Action: Load temperature_scan_data.csv and fit to y = A + B·sinc²[C_temp·(T−T0)] using least‑squares curve fitting to obtain C_temp and T0.
- Evidence: none

### Step 5: Compute acceptance widths and ratio
- Role: process
- Action: Using the average C from the five angle fits (|C_avg|) and |C_temp| from the temperature fit, compute the acceptance width‑length products: ΔθL = 2.782 * L / |C_avg| (L = 0.4 cm) in mrad·cm, and ΔTL = 2.782 * L / |C_temp| in °C·cm. Then compute the ratio Δθ/ΔT.
- Evidence: none

### Step 6: Output acceptance ratio
- Role: scored (load-bearing)
- Action: Write ΔθL (in mrad·cm), ΔTL (in °C·cm), and the ratio (rad/°C) to acceptance_ratio.json.
- Output file: `/app/outputs/acceptance_ratio.json`
- Format: json
- Contract: {"Delta_theta_L_mrad_cm": float, "Delta_T_L_C_cm": float, "ratio_rad_per_C": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_angles.json`
- `/app/outputs/linear_regression_slope.json`
- `/app/outputs/acceptance_ratio.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_angles.json
- path: `/app/outputs/fitted_angles.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The five fitted phase‑matching angles (D_rad, in rad) and the corresponding temperatures (T_C, in °C) from the angle scan fits.
- schema:
  - `type`: object
  - `properties`:
    - `T_C`:
      - `type`: array
      - `items`:
        - `type`: number
    - `D_rad`:
      - `type`: array
      - `items`:
        - `type`: number
  - `required`: `T_C`, `D_rad`

### linear_regression_slope.json
- path: `/app/outputs/linear_regression_slope.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Result of the linear regression of phase‑matching angle vs temperature: slope, intercept, and RMS residual.
- schema:
  - `type`: object
  - `properties`:
    - `slope_rad_per_C`:
      - `type`: number
    - `intercept_rad`:
      - `type`: number
    - `rms_residual_rad`:
      - `type`: number
  - `required`: `slope_rad_per_C`, `intercept_rad`, `rms_residual_rad`

### acceptance_ratio.json
- path: `/app/outputs/acceptance_ratio.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed acceptance width products and their ratio.
- schema:
  - `type`: object
  - `properties`:
    - `Delta_theta_L_mrad_cm`:
      - `type`: number
    - `Delta_T_L_C_cm`:
      - `type`: number
    - `ratio_rad_per_C`:
      - `type`: number
  - `required`: `Delta_theta_L_mrad_cm`, `Delta_T_L_C_cm`, `ratio_rad_per_C`

Notes: The fitted_angles.json must contain the five temperatures in the same order as the scans. The acceptance ratio is the quotient Δθ/ΔT derived from the fitted C parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_angles.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "T_C": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "D_rad": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        },
        "required": [
          "T_C",
          "D_rad"
        ]
      },
      "description": "The five fitted phase‑matching angles (D_rad, in rad) and the corresponding temperatures (T_C, in °C) from the angle scan fits."
    },
    {
      "file": "linear_regression_slope.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "slope_rad_per_C": {
            "type": "number"
          },
          "intercept_rad": {
            "type": "number"
          },
          "rms_residual_rad": {
            "type": "number"
          }
        },
        "required": [
          "slope_rad_per_C",
          "intercept_rad",
          "rms_residual_rad"
        ]
      },
      "description": "Result of the linear regression of phase‑matching angle vs temperature: slope, intercept, and RMS residual."
    },
    {
      "file": "acceptance_ratio.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "properties": {
          "Delta_theta_L_mrad_cm": {
            "type": "number"
          },
          "Delta_T_L_C_cm": {
            "type": "number"
          },
          "ratio_rad_per_C": {
            "type": "number"
          }
        },
        "required": [
          "Delta_theta_L_mrad_cm",
          "Delta_T_L_C_cm",
          "ratio_rad_per_C"
        ]
      },
      "description": "Computed acceptance width products and their ratio."
    }
  ],
  "notes": "The fitted_angles.json must contain the five temperatures in the same order as the scans. The acceptance ratio is the quotient Δθ/ΔT derived from the fitted C parameters."
}
```

## How you are scored
After you complete the workflow, a hidden verifier (which has access to the paper’s reported results) will independently score each required output file. Your submitted `fitted_angles.json`, `linear_regression_slope.json`, and `acceptance_ratio.json` will be compared to reference values within tolerance. The verifier checks that the extracted angles, the regression slope, and the acceptance ratio are sufficiently close to the expected results. A combined reward between 0 and 1 is awarded based on accuracy; merely reporting a plausible number is not enough – the outputs must be self-consistent and derive from the actual fitting and regression steps.
