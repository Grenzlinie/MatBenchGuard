# Piezoelectric MEMS Energy Harvester Modeling and Optimization

## Problem background
Ambient mechanical vibrations are a widely available, untapped source of energy that can power wireless sensors and micro-systems. A MEMS piezoelectric power generator converts vibration into electricity using a silicon cantilever with a thin‑film piezoelectric layer. The device must resonate with the dominant vibration frequency (typically low, near 100 Hz) to maximize output, which is achieved by attaching a proof mass beneath the tip. To design such a harvester, it is crucial to predict the open‑circuit voltage, the optimal average output power, and the influence of geometric parameters such as the length of the piezoelectric layer. This task requires you to implement an analytical electromechanical model and use it to compute these performance metrics for a set of default dimensions and to find the piezoelectric layer length that maximizes the generated power.

## Approach
The cantilever is treated as a uniform Euler–Bernoulli beam with a lumped tip mass. First, the eigenvalue problem for the beam is solved to obtain the natural frequencies and mode shapes; the proof mass is tuned so that the fundamental frequency equals 100 Hz. Under harmonic base excitation, the forced response is obtained by modal superposition, yielding the transverse displacement and slope along the beam. The axial strain in the piezoelectric layer is derived from the second spatial derivative of the deflection, and the resulting strain‑induced charge and open‑circuit voltage are computed. The device is then described by a lumped circuit model: a sinusoidal current source in parallel with the electrode capacitance. With a resistive load connected, the average power is maximized when the load resistance satisfies a frequency‑dependent condition, giving an optimal power that depends on the open‑circuit voltage and the capacitance. Finally, a one‑dimensional sweep of the piezoelectric layer length is performed while keeping the beam length and other parameters fixed; the length that yields the highest optimal average power is recorded, together with the corresponding voltage and power.

## Reproduction target
For the default device parameters (beam length 7.1 mm, silicon thickness 17 µm, piezoelectric length 7.1 mm, piezoelectric thickness 2.0 µm, damping ratio 0.01, base excitation 10 m/s² at 100 Hz, and PZT material: Young's modulus = 86 GPa, d31 = 60.2 pC/N, relative permittivity = 504), compute and save the open‑circuit voltage amplitude V_OC (V), the optimal average power P_max (µW), and the normalized proof mass M_norm (proof mass divided by beam mass). Then, by sweeping the piezoelectric length L_P, identify the optimal length L_P_opt (mm) that maximizes P_max, and record it together with the corresponding V_OC and P_max. Save these quantities in the specified JSON files.

## Assets

- Python scientific stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Build and validate the analytical beam model
- Role: process
- Action: Implement the Euler-Bernoulli beam model with a tip mass. Solve the eigenvalue problem to obtain mode shapes and natural frequencies. Compute forced harmonic response under base excitation using modal superposition. Adjust the proof mass so that the fundamental frequency equals 100 Hz. Verify the model by checking the computed slope at the free end is physically reasonable.
- Evidence: `/app/outputs/model_validation.log`

### Step 2: Compute default device output parameters
- Role: scored (load-bearing)
- Action: Using the validated beam model, compute the open-circuit voltage amplitude V_OC (V), optimal average power P_max (µW), and normalized proof mass M_norm (dimensionless) for the default device parameters (beam length 7.1 mm, Si thickness 17 µm, PZT length 7.1 mm, PZT thickness 2.0 µm, damping 0.01, excitation 10 m/s² at 100 Hz, PZT material: Young's modulus = 86 GPa, d31 = 60.2 pC/N, relative permittivity = 504). Write the results to a JSON file.
- Output file: `/app/outputs/step_01_default_results.json`
- Format: json
- Contract: {"V_OC": float (V), "P_max": float (µW), "M_norm": float (dimensionless)}
- Scoring: scored by hidden verifier

### Step 3: Optimize piezoelectric layer length
- Role: process
- Action: Using the same beam model, sweep the PZT length L_P from a small value up to the full beam length (7.1 mm). For each L_P, compute the optimal average power P_max. Identify the L_P that yields the highest P_max.
- Evidence: `/app/outputs/optimization_trace.csv`

### Step 4: Record optimal length results
- Role: scored (load-bearing)
- Action: Write the optimal PZT length L_P_opt (mm) and the corresponding open-circuit voltage V_OC (V) and optimal average power P_max (µW) to a JSON file.
- Output file: `/app/outputs/step_02_optimal_results.json`
- Format: json
- Contract: {"L_P_opt": float (mm), "V_OC": float (V), "P_max": float (µW)}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_default_results.json`
- `/app/outputs/step_02_optimal_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_default_results.json
- path: `/app/outputs/step_01_default_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Default device performance metrics: open-circuit voltage, optimal average power, and normalized proof mass.
- schema:
  - `type`: object
  - `required`:
    - `V_OC`: float (V)
    - `P_max`: float (µW)
    - `M_norm`: float (dimensionless)

### step_02_optimal_results.json
- path: `/app/outputs/step_02_optimal_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimal PZT length and corresponding open-circuit voltage and optimal average power.
- schema:
  - `type`: object
  - `required`:
    - `L_P_opt`: float (mm)
    - `V_OC`: float (V)
    - `P_max`: float (µW)

Notes: The task reproduces the analytical electromechanical model of a piezoelectric MEMS energy harvester. Verification uses result-level comparison against paper-derived reference values within tolerances to account for legitimate numerical implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_default_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "V_OC": "float (V)",
          "P_max": "float (µW)",
          "M_norm": "float (dimensionless)"
        }
      },
      "description": "Default device performance metrics: open-circuit voltage, optimal average power, and normalized proof mass."
    },
    {
      "file": "step_02_optimal_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "L_P_opt": "float (mm)",
          "V_OC": "float (V)",
          "P_max": "float (µW)"
        }
      },
      "description": "Optimal PZT length and corresponding open-circuit voltage and optimal average power."
    }
  ],
  "notes": "The task reproduces the analytical electromechanical model of a piezoelectric MEMS energy harvester. Verification uses result-level comparison against paper-derived reference values within tolerances to account for legitimate numerical implementation differences."
}
```

## How you are scored
A hidden verifier reads your two scored artifacts (`step_01_default_results.json` and `step_02_optimal_results.json`) and compares the numerical values you report against hidden reference values obtained from the same underlying physics model. The comparison allows for the small discrepancies that naturally arise from different numerical implementations, such as choices of eigenvalue solvers, root‑finding algorithms, or discretisation. Each artifact carries a weight that contributes to your final score. To receive full credit you must implement the complete beam model and the optimization sweep; simply guessing or hard‑coding numbers will not produce values that fall within the expected numerical envelope.
