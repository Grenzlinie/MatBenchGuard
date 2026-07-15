# Pressure-Dependent Raman Frequencies from Observed Volume Data via Mode Grüneisen Parameters

## Problem background
In PbTiO3, the ferroelectric-paraelectric phase transition under pressure is studied by Raman spectroscopy. The pressure dependence of Raman mode frequencies can be related to volume changes through the mode Grüneisen parameter. This task calculates the Raman frequency shifts for several Raman modes as a function of pressure using published volume and frequency data.

## Approach
The relationship between pressure-induced volume change and Raman frequency shift is captured by the isothermal mode Grüneisen parameter γ_T(P) = d(ln v)/d(ln V). Given observed unit-cell volume and Raman mode frequencies at various pressures, both quantities are first fitted to quadratic polynomials in pressure using least squares. From these analytical expressions, γ_T(P) is computed as a function of pressure. The predicted Raman frequency v_T(P) is then obtained via the exponential Grüneisen relation v_T(P) = v0 * exp[-γ_T(P) * ln(V(P)/V0)], where v0 and V0 are the ambient (zero-pressure) frequency and volume. An empirical quadratic calibration maps these raw calculated frequencies to the observed frequencies. Finally, the calibration is applied to produce final Raman frequencies at a dense set of pressures. The entire pipeline is implemented in Python using standard numerical libraries (numpy, scipy).

## Reproduction target
Compute and save two artifacts: (1) the pressure-dependent isothermal mode Grüneisen parameter γ_T for each of the eight Raman modes (E(1TO), A1(1TO), E(2TO), A1(2TO), B1+E, E(3TO), A1(3TO), E(3LO)) at a set of pressures up to 12 GPa, and (2) the final calibrated Raman frequencies for those modes at pressures from 0 to 12 GPa in 0.5 GPa steps. The computations must be based solely on the publicly available observed volume data from Yong et al. (2008) and observed Raman frequency data from Sanjurjo et al. (1983), using the polynomial-fitting, Grüneisen, and calibration pipeline described above. No external pre-trained models or proprietary software are required.

## Assets

- PbTiO3 unit-cell volume vs pressure data from Yong et al. (2008): 10.1016/j.physb.2008.08.008
- PbTiO3 Raman frequency vs pressure data from Sanjurjo et al. (1983): 10.1103/PhysRevB.28.7260
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Acquire observed volume and Raman data
- Role: process
- Action: Obtain the observed unit-cell volume vs pressure data for PbTiO3 from Yong et al. (2008) and the observed Raman frequency vs pressure data for the eight modes (E(1TO), A1(1TO), E(2TO), A1(2TO), B1+E, E(3TO), A1(3TO), E(3LO)) from Sanjurjo et al. (1983). Digitize or extract the numerical data from the published tables/figures.
- Evidence: `/app/outputs/observed_data.csv`

### Step 2: Fit unit-cell volume to quadratic polynomial
- Role: process
- Action: Fit the observed volume data V vs P to the quadratic V(P)=a0+a1*P+a2*P^2 using least squares. Store the coefficients a0, a1, a2 and the ambient volume V0=a0.
- Evidence: `/app/outputs/volume_coefficients.json`

### Step 3: Fit Raman mode frequencies to quadratic polynomials
- Role: process
- Action: For each Raman mode, fit the observed frequency data v vs P to v(P)=b0+b1*P+b2*P^2 using least squares. Store the coefficients b0, b1, b2 and the ambient frequency v0=b0 per mode.
- Evidence: `/app/outputs/frequency_coefficients.json`

### Step 4: Compute mode Grüneisen parameter
- Role: scored
- Action: Using the fitted volume and frequency polynomials, analytically compute the isothermal mode Grüneisen parameter γ_T(P) = d(ln v)/d(ln V) for each mode as a function of pressure. Evaluate at a set of pressures from 0 to 12 GPa.
- Output file: `/app/outputs/gruneisen_parameters.csv`
- Format: csv
- Contract: mode (string), pressure_GPa (float), gamma_T (float)
- Scoring: scored by hidden verifier

### Step 5: Calculate raw predicted frequencies
- Role: process
- Action: For each mode, compute the predicted frequency v_T(P) = v0 * exp[-γ_T(P) * ln(V(P)/V0)] using the fitted volume, ambient frequency, and the computed γ_T(P) from the previous step. Produce raw predicted frequencies (v_cal) for each pressure.
- Evidence: `/app/outputs/predicted_frequencies_raw.csv`

### Step 6: Fit empirical calibration between observed and calculated frequencies
- Role: process
- Action: For each mode, fit the observed frequencies v_obs vs the raw calculated frequencies v_cal to a quadratic calibration v_obs = a + b*v_cal + c*v_cal^2 using least squares. Obtain the per-mode calibration coefficients a, b, c.
- Evidence: `/app/outputs/calibration_coefficients.json`

### Step 7: Produce final calibrated Raman frequency table
- Role: scored (load-bearing)
- Action: Using the fitted volume polynomial, the mode Grüneisen parameter functions, and the calibration coefficients, compute the predicted Raman frequency for each mode at pressures from 0 to 12 GPa in 0.5 GPa steps, apply the empirical calibration, and save the results.
- Output file: `/app/outputs/computed_raman_frequencies.csv`
- Format: csv
- Contract: mode (string), pressure_GPa (float), frequency_cm1 (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gruneisen_parameters.csv`
- `/app/outputs/computed_raman_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gruneisen_parameters.csv
- path: `/app/outputs/gruneisen_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mode Grüneisen parameter γ_T as a function of pressure for each Raman mode. The checker will compare values at a set of hidden pressure checkpoints.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `pressure_GPa`, `gamma_T`

### computed_raman_frequencies.csv
- path: `/app/outputs/computed_raman_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Calibrated Raman frequencies (energy shifts) for the eight modes at pressures from 0 to 12 GPa in 0.5 GPa steps. The checker will compare values at specific hidden pressure checkpoints and verify monotonic trends.
- schema:
  - `type`: table
  - `required_columns`: `mode`, `pressure_GPa`, `frequency_cm1`

Notes: The checker will compare the agent's γ_T and calibrated frequencies at a set of hidden pressures against reference values digitized from the paper's figures. For most modes the frequency decreases with pressure; the correct sign of the trend between successive checkpoints will be evaluated. Tolerances are set to absorb legitimate re‑implementation spread.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gruneisen_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "pressure_GPa",
          "gamma_T"
        ]
      },
      "description": "Mode Grüneisen parameter γ_T as a function of pressure for each Raman mode. The checker will compare values at a set of hidden pressure checkpoints."
    },
    {
      "file": "computed_raman_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "pressure_GPa",
          "frequency_cm1"
        ]
      },
      "description": "Calibrated Raman frequencies (energy shifts) for the eight modes at pressures from 0 to 12 GPa in 0.5 GPa steps. The checker will compare values at specific hidden pressure checkpoints and verify monotonic trends."
    }
  ],
  "notes": "The checker will compare the agent's γ_T and calibrated frequencies at a set of hidden pressures against reference values digitized from the paper's figures. For most modes the frequency decreases with pressure; the correct sign of the trend between successive checkpoints will be evaluated. Tolerances are set to absorb legitimate re‑implementation spread."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact. For the Grüneisen parameters and the final calibrated Raman frequencies, it will compare your computed values at a set of hidden pressure checkpoints against reference values digitized from the original papers, using appropriate tolerances. It will also verify that the pressure-dependent trends (e.g., monotonicity) are consistent with the expected physics. Each scored artifact contributes a weighted fraction to the final reward; the two scores are combined to give the overall result. Merely reporting numbers that match a target is not sufficient—you must execute the full pipeline from the raw observed data.
