# Two-State Piezoelectric Model for Outer Hair Cell Electromechanical Coupling

## Problem background
Outer hair cells (OHCs) in the mammalian cochlea exhibit fast, voltage-dependent length changes essential for hearing sensitivity and frequency selectivity. The underlying mechanism is thought to involve membrane-bound motor proteins that undergo conformational transitions, coupling charge movement across the membrane with changes in the motor’s cross-sectional area. This electromechanical coupling is analogous to piezoelectricity, but the motor’s two-state nature introduces non-linearity and, when many motors are embedded in the cylindrical cell membrane, a self-consistency effect that reduces the motor’s voltage sensitivity.

The goal is to compute, from a well-characterised set of model parameters, the piezoelectric coefficients of the whole cell, the coupling coefficient that quantifies energy conversion efficiency, the cooperativity factor that captures the self-consistency, and the voltage dependence of the motor’s state probability. This determines how effective the hair cell is as a piezoelectric transducer and how its response differs from that of an isolated motor unit.

## Approach
The model is a two-state “area motor” model. A motor unit can occupy either a compact or an extended state; the free energy difference between the states depends linearly on membrane potential and on the anisotropic membrane tension in the cell’s cylindrical geometry. The motor’s conformational equilibrium leads to a voltage- and force-dependent probability Pℓ that the motor is in the extended state.

When many motors are incorporated into the lateral membrane of a cylindrical cell, the motor-induced changes in membrane area feed back onto membrane tension, creating a self-consistency condition. This yields a transcendental equation for Pℓ that must be solved numerically. From the solution, one obtains the small-signal piezoelectric coefficients c11 (membrane capacitance beyond a constant linear part), c12 (piezoelectric coupling), and c22 (axial compliance), as well as the coupling coefficient k and a cooperativity factor α that describes how the cell embedding dampens the voltage sensitivity. An isolated motor is also analysed for comparison.

The computation proceeds in three stages: (1) assemble all model constants from the literature and apply a self-consistency correction; (2) solve the self-consistent equation for Pℓ as a function of membrane potential, and compute the small-signal coefficients and α; (3) evaluate these quantities at half-activation (Pℓ=0.5) to obtain peak values, and produce a full table of voltage-dependent coefficients for a 50‑μm‑long cell.

## Reproduction target
Implement the two-state area motor model for a 50‑μm‑long outer hair cell using the parameter set given in the problem description. Solve the motor’s self-consistent equation for Pℓ over the membrane potential range −150 to +50 mV (1 mV steps) under zero external axial force. From this solution, compute: (1) the peak values of the piezoelectric coefficients (c11 excluding the linear capacitance contribution, c12, c22), the coupling coefficient k, the cooperativity factor α, and the load-free relative amplitude b1·n at the half‑activation point Pℓ=0.5, and write these to step_01_coefficients.json; (2) the full voltage dependence of Pℓ, its voltage derivative dPℓ/dV, α, c11, c12, c22, and k, and write these to step_02_voltage_dependence.csv.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Determine model parameters and constants
- Role: process
- Action: Set the elastic moduli, motor area changes, motor charge and density from literature values, apply the self-consistency correction to obtain true motor parameters, and compute constants b1, b2, b3, and g.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Compute isolated motor coupling coefficient
- Role: process
- Action: Using the motor parameters and estimated motor membrane area and specific capacitance, compute the piezoelectric coefficient a12 and coupling coefficient k of a single motor unit in an isotropic membrane.
- Evidence: `/app/outputs/isolated_motor.json`

### Step 3: Solve self-consistent equation for P_ℓ
- Role: process
- Action: For zero axial force and membrane potential Vm from −150 to +50 mV in 1 mV steps, solve the self-consistent equation relating Vm, P_ℓ, and the constants b2, b3 to obtain the motor state probability P_ℓ. Save the raw P_ℓ vs Vm results for use in downstream steps.
- Evidence: `/app/outputs/pell_vs_Vm.csv`

### Step 4: Compute peak piezoelectric coefficients
- Role: scored (load-bearing)
- Action: From the solved P_ℓ, identify the voltage where P_ℓ=0.5. At that point compute the maximum values of the membrane capacitance contribution c11 (excluding linear capacitance), the piezoelectric coefficient c12, the axial compliance c22, the coupling coefficient k, the cooperativity factor α, and the load-free relative amplitude b1·n. Save these peak values to step_01_coefficients.json.
- Output file: `/app/outputs/step_01_coefficients.json`
- Format: json
- Contract: Keys: c11_max (float, F), c12_max (float, m/V), c22_max (float, m/N), k_max (float), alpha_at_half (float), b2 (float), b1_n (float).
- Scoring: scored by hidden verifier

### Step 5: Voltage dependence of motor state and coefficients
- Role: scored
- Action: For each Vm, compute the derivative dP_ℓ/dV (using finite differences), the cooperativity factor α, and the small-signal coefficients c11, c12, c22 and coupling coefficient k. Save as a CSV with columns: V_m, P_ell, dP_dV, alpha, c11, c12, c22, k.
- Output file: `/app/outputs/step_02_voltage_dependence.csv`
- Format: csv
- Contract: Columns: V_m (mV), P_ell (dimensionless), dP_dV (1/V), alpha (dimensionless), c11 (F), c12 (m/V), c22 (m/N), k (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_coefficients.json`
- `/app/outputs/step_02_voltage_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_coefficients.json
- path: `/app/outputs/step_01_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Peak values of the piezoelectric and mechanical coefficients at half-activation of the motor.
- schema:
  - `type`: object
  - `required`:
    - `c11_max`: float, in Farads (F)
    - `c12_max`: float, in meters per Volt (m/V) or equivalently C/N
    - `c22_max`: float, in meters per Newton (m/N)
    - `k_max`: float, dimensionless
    - `alpha_at_half`: float, dimensionless
    - `b2`: float, dimensionless
    - `b1_n`: float, dimensionless

### step_02_voltage_dependence.csv
- path: `/app/outputs/step_02_voltage_dependence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Voltage dependence of motor state, derivative, cooperativity factor, and whole-cell piezoelectric/mechanical coefficients.
- schema:
  - `type`: table
  - `required_columns`: `V_m`, `P_ell`, `dP_dV`, `alpha`, `c11`, `c12`, `c22`, `k`
  - `units`:
    - `V_m`: mV
    - `P_ell`: dimensionless
    - `dP_dV`: 1/V
    - `alpha`: dimensionless
    - `c11`: F
    - `c12`: m/V
    - `c22`: m/N
    - `k`: dimensionless

Notes: All parameters are constants from the model description; the agent must re-implement the equations and solve numerically. The task is purely computational and requires no external datasets.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c11_max": "float, in Farads (F)",
          "c12_max": "float, in meters per Volt (m/V) or equivalently C/N",
          "c22_max": "float, in meters per Newton (m/N)",
          "k_max": "float, dimensionless",
          "alpha_at_half": "float, dimensionless",
          "b2": "float, dimensionless",
          "b1_n": "float, dimensionless"
        }
      },
      "description": "Peak values of the piezoelectric and mechanical coefficients at half-activation of the motor."
    },
    {
      "file": "step_02_voltage_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "V_m",
          "P_ell",
          "dP_dV",
          "alpha",
          "c11",
          "c12",
          "c22",
          "k"
        ],
        "units": {
          "V_m": "mV",
          "P_ell": "dimensionless",
          "dP_dV": "1/V",
          "alpha": "dimensionless",
          "c11": "F",
          "c12": "m/V",
          "c22": "m/N",
          "k": "dimensionless"
        }
      },
      "description": "Voltage dependence of motor state, derivative, cooperativity factor, and whole-cell piezoelectric/mechanical coefficients."
    }
  ],
  "notes": "All parameters are constants from the model description; the agent must re-implement the equations and solve numerically. The task is purely computational and requires no external datasets."
}
```

## How you are scored
A hidden verifier independently inspects your submitted artifacts. It checks that the files contain the required keys and columns, that the voltage dependence of Pℓ and its derivative have the correct functional form (e.g., a bell-shaped derivative that peaks where Pℓ≈0.5), and that the coefficients are internally consistent (the coupling coefficient k must match the value computed from c11, c12, and c22). The verifier also compares the peak values to reference targets with appropriate tolerances. Each stage’s score is weighted and combined into a final reward; reporting a plausible‑looking number without actually implementing the model is not sufficient.
