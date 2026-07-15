# Compute Spinodal Temperatures and UCST Critical Minimum for a Polymer Solution Model

## Problem background
Liquid–liquid phase separation in polymer solutions is strongly influenced by pressure and the polymer’s molecular weight distribution. For systems that exhibit both an upper critical solution temperature (UCST) and a lower critical solution temperature (LCST), the interplay of temperature and pressure can cause the two immiscibility regions to merge, producing hourglass-shaped phase diagrams. Predicting the pressure‑dependent demixing temperatures for a polydisperse polymer solution requires a thermodynamic model that captures the combined effects of entropy, excess Gibbs energy, and polydispersity. This task targets the quantitative prediction of spinodal temperatures and the minimum of the UCST critical curve for a specific polydisperse system using a continuous‑thermodynamics framework.

## Approach
The computation uses a continuous‑thermodynamics description that treats the polymer as a continuous distribution of chain lengths. The segment‑molar Gibbs energy of mixing combines the Flory–Huggins entropy of mixing for a polydisperse polymer in a solvent with an excess Gibbs energy term of the form

  G^E / (RT) = X (1 – X) (1 – d X) χ(T, P)

where X is the segment mole fraction of polymer, d is a constant, and χ(T,P) depends on temperature and pressure.

The temperature‑and‑pressure‑dependent interaction function χ(T,P) is given by

  χ(T, P) = a₁ + a₂ / T + a₃ ln(T / [K])

with each coefficient aᵢ expressed as a quadratic polynomial in pressure:

  aᵢ (P) = a_{i,1} + a_{i,2} P + a_{i,3} P²   (P in bar).

The model parameters are taken from the published set that includes quadratic pressure dependence (a_{i,3} ≠ 0 for all i). The numerical values used throughout the task are:

  d = 0.27
  a₁₁ = –26.455,              a₁₂ = 0.0073 bar⁻¹,       a₁₃ = 0.00133 bar⁻²
  a₂₁ = 1542.995 K,           a₂₂ = 0.8049 K bar⁻¹,     a₂₃ = –0.08363 K bar⁻²
  a₃₁ = 3.875,                a₃₂ = –0.00172 bar⁻¹,     a₃₃ = –1.851 × 10⁻⁴ bar⁻².

The polymer molecular weight distribution is described by the Schulz–Flory distribution,

  W(r) = (k^(k+1) / (r_N Γ(k+1))) (r / r_N)^k exp(–k r / r_N),

with number‑average segment number r_N = 1456 and shape parameter k = 0.5457. From these, the mass‑average segment number is r_W = 4124, and the z‑average follows from r_z = r_W (k+2)/(k+1). The solvent is treated as a single segment (r_A = 1).

The spinodal condition is obtained by setting the second derivative of G^E/(RT) with respect to X to zero, leading to an equation that involves r_W and X. The critical condition adds the vanishing of the third derivative, which brings in r_z. To find spinodal temperatures, one solves the spinodal equation for temperature T at a fixed segment mole fraction X = 0.048 and prescribed pressures. The UCST critical branch is located by solving the spinodal and critical conditions simultaneously for X and T at a series of pressures, after which the temperature minimum of that branch gives the critical temperature and pressure at the minimum.

## Reproduction target
Compute the following four quantities using the continuous‑thermodynamics model and the parameter values stated in the Approach.

1. Spinodal temperature at segment mole fraction X = 0.048 and pressure P = 20 bar (in K).
2. Spinodal temperature at X = 0.048 and P = 100 bar (in K).
3. Temperature at the minimum of the UCST critical curve (in K).
4. Pressure at that minimum (in bar).

Write these numbers as a JSON object with the keys "spinodal_T_20bar", "spinodal_T_100bar", "UCST_critical_T_min", and "UCST_critical_P_min" into the output file `/app/outputs/step_01_results.json`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute spinodal temperatures and UCST critical minimum
- Role: scored (load-bearing)
- Action: Implement the continuous thermodynamics framework for a polydisperse polymer solution: define the segment-molar Gibbs energy of mixing including the athermal Flory‑Huggins entropy and a concentration‑ and pressure‑dependent excess Gibbs energy term of the form G^E/RT = X(1-X)(1-dX) χ(T,P), where χ(T,P) has a three‑term temperature function with each coefficient expanded as a polynomial in pressure. Use the Schulz‑Flory distribution to describe the polymer molecular weight distribution with given number‑average segment number r_N and shape parameter k, and set the solvent segment number to 1. Derive the spinodal condition (vanishing second derivative with respect to polymer segment mole fraction X) and the critical condition (spinodal plus third‑derivative zero) in terms of the mass‑average and z‑average segment numbers and the derivatives of G^E/RT. Solve the spinodal condition for temperature T at a fixed segment mole fraction X=0.048 and pressures P=20 bar and P=100 bar using the published parameter set that includes quadratic pressure dependence (d and all a_i,j coefficients with a_i,3 nonzero). Locate the UCST critical branch by solving the spinodal and critical conditions simultaneously for X and T as functions of P, then find the temperature minimum of that branch, recording the corresponding critical temperature T_min and pressure P_min. Write the four computed values into the output file.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: JSON object with fields: "spinodal_T_20bar" (float, unit K), "spinodal_T_100bar" (float, unit K), "UCST_critical_T_min" (float, unit K), "UCST_critical_P_min" (float, unit bar).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent's computed spinodal and critical values compared to a hidden reference recomputation using the same model equations and parameters.
- schema:
  - `type`: object
  - `required`:
    - `spinodal_T_20bar`: float (K)
    - `spinodal_T_100bar`: float (K)
    - `UCST_critical_T_min`: float (K)
    - `UCST_critical_P_min`: float (bar)

Notes: The agent must use the publicly provided model parameters and polymer distribution parameters to compute the four output quantities. No parameter fitting is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "spinodal_T_20bar": "float (K)",
          "spinodal_T_100bar": "float (K)",
          "UCST_critical_T_min": "float (K)",
          "UCST_critical_P_min": "float (bar)"
        }
      },
      "description": "Agent's computed spinodal and critical values compared to a hidden reference recomputation using the same model equations and parameters."
    }
  ],
  "notes": "The agent must use the publicly provided model parameters and polymer distribution parameters to compute the four output quantities. No parameter fitting is required."
}
```

## How you are scored
Your submission is scored by an independent verifier that re‑implements the same continuous‑thermodynamics model (Schulz–Flory distribution, the G^E/RT expression, and the same numerical parameters) and solves the spinodal and critical conditions numerically. It compares your reported spinodal temperatures and UCST minimum coordinates against its own recomputed values. The reward depends on how closely your results match the verifier’s reference; all four fields must agree within the verifier’s hidden tolerances to receive full credit. The verifier does not inspect your code—it only checks the numerical results in the output file.
