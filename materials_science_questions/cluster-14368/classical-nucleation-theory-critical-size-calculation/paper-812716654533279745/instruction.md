# Cloud Base Supersaturation Maximum and Droplet Concentration Calculation via Iterative Algorithm

## Problem background
Standard cloud microphysics parameterizations often assume that all droplets at cloud base form from dry CCN. However, in many situations liquid water is already present at the cloud base, either inside haze particles or as pre-existing drops, which can significantly alter the supersaturation evolution and the number of activated droplets. This task targets a more general computational method that accounts for an initial liquid water mixing ratio q2 and the liquid water contained in haze particles. The method calculates the maximum supersaturation S_max reached in an ascending parcel and the resulting droplet concentration N, for given aerosol size distributions, thermodynamic conditions, and vertical velocity. Such a calculation is important for accurately predicting cloud droplet number in models.

## Approach
The method relies on a universal non-dimensional supersaturation profile that depends on a single parameter Q0, the normalized initial liquid water mixing ratio. The maximum of the normalized supersaturation, S_max*, is a function of Q0, known from solving the non-dimensional equation and tabulated below. The iterative algorithm computes a self-consistent S_max and droplet concentration N by cycling through the following conceptual steps:

1. Start from an initial guess of supersaturation maximum S_max.
2. Compute the critical dry aerosol radius from S_max using the Köhler equation.
3. Calculate the droplet concentration N by integrating the aerosol size distribution above the critical radius (for a trimodal lognormal distribution, analytical formulas based on the error function are available).
4. Compute a dimensionless parameter R that depends on N, vertical velocity w, and thermodynamic coefficients.
5. Evaluate the mean radius of wet aerosol particles at cloud base (the radius of haze particles at zero supersaturation) from the aerosol size distribution.
6. Calculate Q0 from the mean haze radius, the liquid water mixing ratio of pre-existing drops q2, the parameter R, and thermodynamic constants. Q0 has two contributions: one from the liquid water inside haze and one from any initial drops present at cloud base.
7. Look up the corresponding S_max* for this Q0 from the table below (interpolate as needed).
8. Update S_max using the relation S_max = R^{-3/4} S_max*.
9. Repeat from step 2 until convergence.

Thermodynamic coefficients are evaluated at a temperature T = 6 °C using standard formulas for water vapor saturation pressure, latent heat, diffusion coefficient, thermal conductivity, and other constants. The required expressions for A1, A2, F, A, B are provided in the appendix of the original derivation but can be derived from standard atmospheric thermodynamics.

The non-dimensional supersaturation maximum S_max* as a function of Q0 is:

| Q0    | S_max* | z_max* |
|-------|--------|--------|
| 0.0   | 1.0540 | 1.9080 |
| 0.1   | 0.9589 | 1.9930 |
| 0.2   | 0.9147 | 2.0210 |
| 0.3   | 0.8821 | 2.0390 |
| 0.4   | 0.8557 | 2.0520 |
| 0.5   | 0.8333 | 2.0610 |
| 0.6   | 0.8139 | 2.0690 |
| 0.7   | 0.7967 | 2.0760 |
| 0.8   | 0.7812 | 2.0820 |
| 0.9   | 0.7672 | 2.0870 |
| 1.0   | 0.7543 | 2.0900 |
| 1.1   | 0.7425 | 2.0930 |
| 1.2   | 0.7315 | 2.0950 |
| 1.3   | 0.7214 | 2.0960 |
| 1.4   | 0.7120 | 2.0960 |
| 1.5   | 0.7032 | 2.0960 |
| 1.6   | 0.6931 | 2.0960 |
| 1.7   | 0.6850 | 2.0970 |
| 1.8   | 0.6772 | 2.0970 |
| 1.9   | 0.6698 | 2.0970 |
| 2.0   | 0.6628 | 2.0970 |
| 2.1   | 0.6561 | 2.0970 |
| 2.2   | 0.6497 | 2.0970 |

If Q0 falls outside this range, use the nearest endpoint value (the function is nearly constant beyond 2.2).

The aerosol size distribution is a trimodal lognormal distribution. The parameters for each aerosol type are given in the table below. The radii R_i are in micrometers, the standard deviations σ_i are dimensionless, and the modal concentrations N_i are in cm⁻³. Convert concentrations to m⁻³ before use in equations.

| Aerosol type       | Mode | R (µm) | σ   | N (cm⁻³) |
|--------------------|------|--------|------|----------|
| marine             | 1    | 0.005  | 1.6  | 340      |
|                    | 2    | 0.035  | 2.0  | 60       |
|                    | 3    | 0.31   | 2.7  | 3.1      |
| clean_continental  | 1    | 0.008  | 1.6  | 1000     |
|                    | 2    | 0.034  | 2.1  | 800      |
|                    | 3    | 0.46   | 2.2  | 0.72     |
| background         | 1    | 0.008  | 1.7  | 6400     |
|                    | 2    | 0.038  | 2.0  | 2300     |
|                    | 3    | 0.51   | 2.16 | 3.2      |
| urban              | 1    | 0.007  | 1.8  | 106000   |
|                    | 2    | 0.027  | 2.16 | 32000    |
|                    | 3    | 0.43   | 2.21 | 5.4      |

The analytical formulas for droplet concentration and mean haze radius using the error function are given by:

N = Σ_i (N_i/2) [1 - erf( ln(r_n_cr / R_i) / sqrt(2 (ln σ_i)^2) )]

and

r_0 = (1/N) Σ_i (N_i/2) * R_i^* exp(α_i^2 / 2) [1 + erf( (ln R_i^* + α_i^2 - ln r^*) / (sqrt(2) α_i) )]

where α_i = (3/2) ln σ_i, R_i^* = sqrt( B R_i^3 / A ), r^* = sqrt(B/A) r_n_cr^{3/2}, and r_n_cr is the critical dry radius given by r_n_cr = (A/3) (4/(B S_max^2))^{1/3}. The coefficients A and B are the Köhler equation parameters.

Implement these steps in Python using numpy. Use linear interpolation on the S_max* table. The iteration should continue until the relative change in S_max falls below 1e-6. Use the given thermodynamic constants and aerosol parameters to compute all required coefficients.

## Reproduction target
Implement the iterative algorithm described in the approach section for the four aerosol types provided (marine, clean_continental, background, urban). For each type, run the algorithm for each vertical velocity w in the list [0.1, 0.5, 1.0, 2.0, 5.0, 10.0] m/s, with initial liquid water mixing ratio q2 = 0. In addition, for the marine and clean_continental types only, also run for q2 = 1e-5 and q2 = 1e-4 kg/kg. For every combination, record the aerosol type, w, q2, the converged S_max, and the final N in a CSV file. The full set of rows to compute is:

- marine: w in {0.1,0.5,1.0,2.0,5.0,10.0} with q2 = 0, 1e-5, 1e-4 → 18 rows
- clean_continental: w in {0.1,0.5,1.0,2.0,5.0,10.0} with q2 = 0, 1e-5, 1e-4 → 18 rows
- background: w in {0.1,0.5,1.0,2.0,5.0,10.0} with q2 = 0 → 6 rows
- urban: w in {0.1,0.5,1.0,2.0,5.0,10.0} with q2 = 0 → 6 rows

Total rows: 48 rows. Write them all to /app/outputs/results.csv with columns: aerosol_type, w, q2, S_max, N (units as specified in the output contract). S_max should be dimensionless and N in m⁻³. Use a convergence tolerance of 1e-6 relative change in S_max.

## Assets

- Python scientific stack: numpy scipy

## Workflow steps

### Step 1: Compute supersaturation maximum and droplet concentration
- Role: scored (load-bearing)
- Action: Implement the iterative algorithm (Section 4 of the source paper) to compute supersaturation maximum S_max and droplet concentration N for each prescribed condition (aerosol_type, w, q2) using the given thermodynamic coefficient formulas, aerosol trimodal lognormal distribution parameters, and the normalized supersaturation maximum lookup table. Conditions: aerosol_type in {marine, clean_continental, background, urban}; w (m/s) in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0] with q2 = 0 for all types; additionally for marine and clean_continental, include q2 in [1e-5, 1e-4] kg/kg. Write results to /app/outputs/results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: aerosol_type (string), w (float, m/s), q2 (float, kg/kg), S_max (float, dimensionless), N (float, m^{-3})
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Supersaturation maximum and droplet concentration for each aerosol type, vertical velocity, and initial liquid water mixing ratio condition.
- schema:
  - `type`: table
  - `required_columns`: `aerosol_type`, `w`, `q2`, `S_max`, `N`
  - `units`:
    - `w`: m/s
    - `q2`: kg/kg
    - `S_max`: dimensionless
    - `N`: m^{-3}

Notes: The hidden checker recomputes S_max and N for each row using the same algorithm and compares the agent's values within a relative tolerance. The columns aerosol_type is a lowercase string identifier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "aerosol_type",
          "w",
          "q2",
          "S_max",
          "N"
        ],
        "units": {
          "w": "m/s",
          "q2": "kg/kg",
          "S_max": "dimensionless",
          "N": "m^{-3}"
        }
      },
      "description": "Supersaturation maximum and droplet concentration for each aerosol type, vertical velocity, and initial liquid water mixing ratio condition."
    }
  ],
  "notes": "The hidden checker recomputes S_max and N for each row using the same algorithm and compares the agent's values within a relative tolerance. The columns aerosol_type is a lowercase string identifier."
}
```

## How you are scored
After you submit your solution, a hidden verifier will read your results.csv. For each row, it will independently recompute the expected S_max and N using the same iterative algorithm, the same thermodynamic coefficients, and the same lookup table and aerosol parameters that were provided in the approach section. It will compare your S_max and N to the recomputed reference values row by row. Your score will be based on the fraction of rows where both S_max and N are within an undisclosed relative tolerance of the reference. The tolerance is chosen to account for minor numerical differences due to implementation choices, but it is strict enough that a correct implementation will pass. Simply copying numbers from a publication without actually running the algorithm will not pass the verifier. There is only one scored artifact, so your total reward is the fraction of compliant rows.
