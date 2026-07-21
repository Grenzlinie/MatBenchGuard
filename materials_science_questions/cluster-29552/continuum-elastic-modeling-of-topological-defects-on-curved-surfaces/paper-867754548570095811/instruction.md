# Analytic Drag Coefficients and Defect Velocities in 2D Nematic Liquid Crystals

## Problem background
Nematic liquid crystals contain topological defects—singular points around which the director field rotates. Understanding how these defects move is essential for modeling coarsening dynamics in passive nematics and spontaneous flows in active nematics. In a minimal hydrodynamic description, the fluid flow (backflow) couples to the director field, making the drag force depend on the topological charge. A moving defect dissipates energy, and the translational drag coefficients for +1/2 and −1/2 defects differ. This task computes the analytic translational drag coefficients and the resulting defect velocities in two geometries: a planar channel and a free active +1/2 defect.

## Approach
We use a perturbation analysis within the minimal nematic hydrodynamic model: equal Frank constant K for elasticity, a single isotropic flow viscosity α4, and a rotational viscosity γ1. The equations of motion are derived from a Rayleigh dissipation function. In the limit of small defect velocity u, the stream function for the flow is expanded in a perturbation series, yielding a quartic characteristic equation whose roots determine the flow profile. Integrating the dissipation rate over an annulus from a core cutoff r_core to a system-size cutoff r_max gives analytic expressions for the translational drag coefficients D1 (for +1/2 defect) and D1′ (for −1/2 defect). From these, force balance in a channel (where the defect is driven by an elastic force from boundary anchoring) yields defect velocities as functions of the channel width d and viscosity α4. For active nematics, an extra active term in the dissipation function provides a driving force; balancing it against passive drag gives the free-propulsion velocity of a +1/2 defect.

## Input
All parameter values are provided in a JSON file `/app/inputs/parameters.json`. Load this file at the start of your computation. The file contains the following keys with numeric values:

- `K`: Frank elastic constant (single float)
- `gamma1`: rotational viscosity (single float)
- `alpha4`: isotropic flow viscosity used as the base value (single float)
- `r_core`: core cutoff radius (single float)
- `r_max`: system-size cutoff radius (single float)
- `d`: planar channel width (single float)
- `zeta`: activity coefficient (single float)
- `channel_alphas`: an array of float values representing different isotropic flow viscosities α4 for the channel velocity computation.

Units are consistent within the parameter set; you do not need to convert them.

## Reproduction target
Your task is to implement the analytic formulas described above, using the parameters loaded from `/app/inputs/parameters.json`. Specifically:

1. Given the parameters K, gamma1, alpha4 (base α4), r_core, r_max, compute the translational drag coefficients D1 (for k=+1/2) and D1′ (for k=−1/2) and save them as a JSON object with keys "D1" and "D1_prime" to /app/outputs/analytic_drag_coefficients.json.

2. For the planar channel of width d (using r_max = d/2), and for each α4 value in the array `channel_alphas`, compute the steady-state defect velocities u_{+1/2} and u_{−1/2} using the same K, gamma1, r_core. Output a CSV file at /app/outputs/channel_velocities.csv with columns alpha4, u_plus_half, u_minus_half.

3. Using the activity coefficient ζ and the parameters alpha4 (base α4), gamma1, r_max, r_core, compute the active driving coefficient D5 and then the free motion velocity u_free = −D5 / D1 for a +1/2 defect, using the D1 value computed from the same base parameters. Save the result as {"u_free": <float>} to /app/outputs/active_free_velocity.json.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute analytic drag coefficients D1 and D1′
- Role: scored
- Action: From the parameters K, gamma1, alpha4, r_core, r_max loaded from /app/inputs/parameters.json, and topological charges k=+1/2 and k=−1/2, evaluate the explicit translational drag coefficient formulas from the minimal model. The formulas require solving the quartic characteristic equation for exponents p1,p2 using the viscosity ratio g=gamma1/alpha4. Compute D1 for k=+1/2 and D1′ for k=−1/2 and write them to a JSON file.
- Output file: `/app/outputs/analytic_drag_coefficients.json`
- Format: json
- Contract: {"D1": <float>, "D1_prime": <float>}
- Scoring: scored by hidden verifier

### Step 2: Compute defect velocities in a planar channel
- Role: scored
- Action: For a planar channel of width d (from /app/inputs/parameters.json) and each value of alpha4 in the array channel_alphas (also from /app/inputs/parameters.json), compute the defect velocities u_{+1/2} and u_{−1/2} using the same K, gamma1, r_core. Output a CSV file with columns alpha4, u_plus_half, u_minus_half.
- Output file: `/app/outputs/channel_velocities.csv`
- Format: csv
- Contract: columns: alpha4 (float), u_plus_half (float), u_minus_half (float)
- Scoring: scored by hidden verifier

### Step 3: Compute active +1/2 defect free-propulsion velocity
- Role: scored
- Action: Using the activity coefficient zeta (from /app/inputs/parameters.json) and the same parameters (alpha4 base value, gamma1, r_max, r_core), compute the active driving coefficient D5 from the analytic expression, then compute the free motion velocity u_free = −D5 / D1 (D2=0 in the minimal model) using the D1 value from the same parameter set. Write the result to a JSON file.
- Output file: `/app/outputs/active_free_velocity.json`
- Format: json
- Contract: {"u_free": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/analytic_drag_coefficients.json`
- `/app/outputs/channel_velocities.csv`
- `/app/outputs/active_free_velocity.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### analytic_drag_coefficients.json
- path: `/app/outputs/analytic_drag_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The translational drag coefficients D1 (for +1/2 defect) and D1′ (for −1/2 defect) computed from the minimal model. Numeric values; units are consistent with the input parameters (K, γ1, α4, r_core, r_max).
- schema:
  - `type`: object
  - `required`:
    - `D1`: number
    - `D1_prime`: number

### channel_velocities.csv
- path: `/app/outputs/channel_velocities.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV table of defect velocities in a planar channel for different values of the isotropic flow viscosity α4. Columns are alpha4 (float), u_plus_half (velocity of +1/2 defect), u_minus_half (velocity of −1/2 defect).
- schema:
  - `type`: table
  - `required_columns`: `alpha4`, `u_plus_half`, `u_minus_half`
  - `units`:
    - `alpha4`: input units (viscosity)
    - `u_plus_half`: velocity units (distance/time)
    - `u_minus_half`: velocity units (distance/time)

### active_free_velocity.json
- path: `/app/outputs/active_free_velocity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: The steady-state free-propulsion velocity of an active +1/2 defect, computed from the analytic model. Numeric value; units consistent with inputs.
- schema:
  - `type`: object
  - `required`:
    - `u_free`: number

Notes: All three scored artifacts are obtained by evaluating explicit analytic formulas from the minimal model. The checker will independently recompute the expected values using the same formulas and parameters from /app/inputs/parameters.json, and compare with the agent's submitted numbers within appropriate numeric tolerances. The load-bearing requirement is not strictly enforced because there are no mandatory process steps; the agent must implement the formulas correctly to pass.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "analytic_drag_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "D1": "number",
          "D1_prime": "number"
        }
      },
      "description": "The translational drag coefficients D1 (for +1/2 defect) and D1′ (for −1/2 defect) computed from the minimal model. Numeric values; units are consistent with the input parameters (K, γ1, α4, r_core, r_max)."
    },
    {
      "file": "channel_velocities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha4",
          "u_plus_half",
          "u_minus_half"
        ],
        "units": {
          "alpha4": "input units (viscosity)",
          "u_plus_half": "velocity units (distance/time)",
          "u_minus_half": "velocity units (distance/time)"
        }
      },
      "description": "CSV table of defect velocities in a planar channel for different values of the isotropic flow viscosity α4. Columns are alpha4 (float), u_plus_half (velocity of +1/2 defect), u_minus_half (velocity of −1/2 defect)."
    },
    {
      "file": "active_free_velocity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "u_free": "number"
        }
      },
      "description": "The steady-state free-propulsion velocity of an active +1/2 defect, computed from the analytic model. Numeric value; units consistent with inputs."
    }
  ],
  "notes": "All three scored artifacts are obtained by evaluating explicit analytic formulas from the minimal model. The checker will independently recompute the expected values using the same formulas and parameters from /app/inputs/parameters.json, and compare with the agent's submitted numbers within appropriate numeric tolerances. The load-bearing requirement is not strictly enforced because there are no mandatory process steps; the agent must implement the formulas correctly to pass."
}
```

## How you are scored
After your code finishes, a hidden verifier independently recomputes the expected values for each scored artifact using the same analytic expressions and the same hidden parameters. For analytic_drag_coefficients.json, it compares your D1 and D1′ to its recomputed values within a small absolute tolerance. For channel_velocities.csv, it checks that for every row u_plus_half > u_minus_half (a required physical trend) and compares the numerical velocities to the expected ones. For active_free_velocity.json, it compares your u_free to the recomputed value. The final reward is a weighted combination of these three checks; reporting numbers that are not obtained from a correct implementation of the formulas will not pass. The exact tolerances and gold values are hidden.
