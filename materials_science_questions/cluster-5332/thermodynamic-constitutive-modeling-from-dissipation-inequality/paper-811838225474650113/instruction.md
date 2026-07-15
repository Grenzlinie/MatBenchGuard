# Uniaxial Viscoelastic Polymer Response Simulation

## Problem background
Polymers subjected to cyclic loading dissipate mechanical energy as heat, which can limit component life. A thermodynamically consistent constitutive model for rate‑type viscoelastic solids has been developed to predict the mechanical response of polyamide 6. The model describes the uniaxial force–time behaviour during stress‑relaxation and displacement‑controlled cyclic loading experiments. This task requires implementing the model and computing the axial force as a function of time under the same loading protocols used in the experiments. The hidden verifier will compare the computed force–time curves against the actual experimental measurements.

## Approach
The model postulates a Helmholtz free energy depending on two left Cauchy–Green stretch tensors: one from the reference configuration and one from an evolving natural configuration. By enforcing the second law of thermodynamics and incompressibility, explicit expressions for the Cauchy stress and an evolution equation for an internal scalar variable B(t) are obtained. For a uniaxial, homogeneous extension the model reduces to a scalar ordinary differential equation for B(t) and an algebraic expression for the axial force f_z(t) that depends on the applied stretch λ(t) and the current value of B(t). The model uses four material constants (two shear moduli, a viscosity parameter, and a power‑law exponent). The constants are supplied in Step 1. Given a prescribed stretch history λ(t) (a ramp‑and‑hold profile for stress relaxation or a cyclic ramp waveform for cyclic loading), the ODE is solved numerically with initial condition B(0)=1, and the force f_z(t) is computed. The workflow produces two CSV files containing the simulated force–time series.

## Reproduction target
Compute the axial force f_z(t) for the following four test conditions:

- Stress relaxation: three uniaxial tests where the specimen is stretched at a constant rate to a peak strain and then the displacement is held constant.
  * Condition 1: strain = 0.07, stretch rate = 0.0325 s⁻¹
  * Condition 2: strain = 0.07, stretch rate = 0.0176 s⁻¹
  * Condition 3: strain = 0.08, stretch rate = 0.0008 s⁻¹
  The force–time traces for all three conditions must be written together to `stress_relaxation_force.csv` (columns: test_id, time_s, force_N).

- Cyclic loading: a displacement‑controlled cyclic stretch with peak strain = 0.06, strain ratio = 0.1 (minimum strain divided by peak strain), and frequency = 0.4 Hz. The waveform is a linear ramp (sawtooth) with 20 full cycles. The force–time data are written to `cyclic_loading_force.csv` (columns: time_s, force_N).

In every case use the material parameters listed in Step 1 and the initial condition B(0)=1. The hidden checker will compare the submitted force–time series against the experimental measurements; the agent does not need to post‑process or report any aggregate metric itself.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement viscoelastic model functions
- Role: process
- Action: Implement Python functions that compute the right‑hand side of the scalar ODE for B(t), the axial Cauchy stress T_ZZ, and the axial force f_z, using the published material parameters (μ₁=129.1267 MPa, μ₂=70.3011 MPa, ν=12.4878 MPa·s, β=0.5666) and given stretch history λ(t) and its time derivative. The equations are (with a₀ = 24 mm²):

  ODE d B/dt (Eq. 35):
  dB/dt = 2 * (μ₁/(2ν))^(1/(2β−1)) * [ (2 + B^(3/2))/B^(1/2) − 9 B/(2 B^(3/2) + 1) ]^( (1−β)/(2β−1) ) * [ 3 B/(2 B^(3/2) + 1) − B ] + 2 B * (dλ/dt)/λ

  Axial Cauchy stress T_ZZ (Eq. 32): T_ZZ = μ₁ (B − 1/√B) + μ₂ (λ² − 1/λ)

  Axial force f_z (Eq. 34): f_z = a₀ T_ZZ / λ   (units of a₀ are mm², so force in N)

  Initial condition: B(0) = 1.
- Evidence: none

### Step 2: Simulate stress‑relaxation experiments
- Role: scored (load-bearing)
- Action: For the three stress‑relaxation conditions (0.07 strain at 0.0325 s⁻¹, 0.07 strain at 0.0176 s⁻¹, and 0.08 strain at 0.0008 s⁻¹), reconstruct the stretch history λ(t) based on the reported stretch rates and hold periods, solve the ODE for B(t) with B(0)=1, and compute the axial force f_z(t). The test_id values in the CSV must be exactly: '0.07_0.0325', '0.07_0.0176', '0.08_0.0008'. Write the combined force–time series to stress_relaxation_force.csv.
- Output file: `/app/outputs/stress_relaxation_force.csv`
- Format: csv
- Contract: Columns: test_id, time_s, force_N
- Scoring: scored by hidden verifier

### Step 3: Simulate cyclic loading experiment
- Role: scored (load-bearing)
- Action: Construct the cyclic stretch history λ(t) for 20 cycles at 0.4 Hz, peak strain 0.06, strain ratio 0.1, solve the ODE for B(t) with B(0)=1, and compute the axial force f_z(t). Write the force–time series to cyclic_loading_force.csv.
- Output file: `/app/outputs/cyclic_loading_force.csv`
- Format: csv
- Contract: Columns: time_s, force_N
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_relaxation_force.csv`
- `/app/outputs/cyclic_loading_force.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_relaxation_force.csv
- path: `/app/outputs/stress_relaxation_force.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Force–time curves for the three stress‑relaxation experiments: 0.07 strain at 0.0325 s⁻¹, 0.07 strain at 0.0176 s⁻¹, 0.08 strain at 0.0008 s⁻¹.
- schema:
  - `type`: table
  - `required_columns`: `test_id`, `time_s`, `force_N`
  - `units`:
    - `time_s`: s
    - `force_N`: N

### cyclic_loading_force.csv
- path: `/app/outputs/cyclic_loading_force.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Force–time curve for cyclic loading: 20 cycles at 0.4 Hz, peak strain 0.06, strain ratio 0.1.
- schema:
  - `type`: table
  - `required_columns`: `time_s`, `force_N`
  - `units`:
    - `time_s`: s
    - `force_N`: N

Notes: The agent uses the published material parameters from Table 2 of the paper; parameter fitting is not required. The checker will recompute a relative error metric against digitized gold curves and score based on tolerance thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_relaxation_force.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "test_id",
          "time_s",
          "force_N"
        ],
        "units": {
          "time_s": "s",
          "force_N": "N"
        }
      },
      "description": "Force–time curves for the three stress‑relaxation experiments: 0.07 strain at 0.0325 s⁻¹, 0.07 strain at 0.0176 s⁻¹, 0.08 strain at 0.0008 s⁻¹."
    },
    {
      "file": "cyclic_loading_force.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time_s",
          "force_N"
        ],
        "units": {
          "time_s": "s",
          "force_N": "N"
        }
      },
      "description": "Force–time curve for cyclic loading: 20 cycles at 0.4 Hz, peak strain 0.06, strain ratio 0.1."
    }
  ],
  "notes": "The agent uses the published material parameters from Table 2 of the paper; parameter fitting is not required. The checker will recompute a relative error metric against digitized gold curves and score based on tolerance thresholds."
}
```

## How you are scored
A hidden verification program reads your two output CSV files. For each test condition it compares your computed force values point‑wise against reference (gold) force–time curves obtained from the experiments. The comparison uses a relative error metric that measures how well your simulated curves follow the experimental behaviour. Each file receives a sub‑score, and the final reward is a weighted combination of the sub‑scores; the stress‑relaxation and cyclic‑loading targets carry meaningful weight. The reward is monotonic in solution quality: a force curve that is closer to the experimental data yields a higher score. Only the content of the CSV files is scored; you are not required to report any aggregate metric in prose.
