# Thermodynamic Equilibrium Phase Diagram of Hydrogen-Adsorbed Carbon

## Problem background
The equilibrium between carbon solid phases (like diamond vs. graphite) and vapor in a hydrogen atmosphere is critical for understanding diamond film growth. This work models the system as classical ideal atomic gases (carbon and hydrogen) in contact with a crystalline solid treated as a d‑dimensional Einstein oscillator and a surface with monohydride adsorption. By equating chemical potentials, closed‑form expressions for total vapor pressure and hydrogen covering ratio are derived. Reproducing these expressions and the resulting curves quantifies the phase boundaries and surface coverage under controlled conditions.

## Approach
The method uses classical statistical mechanics:
- Vapor-phase chemical potentials for atomic carbon and hydrogen from the ideal gas translational partition function.
- Solid carbon as a d-dimensional Einstein oscillator with a partition function that depends on the Debye temperature and cohesive energy.
- Surface adsorption centers as monohydride sites with a partition function that includes stretching and bending vibrational modes and an adsorption energy.

Equating the chemical potentials of the two phases yields formulas for the total vapor pressure P (MPa) and the hydrogen covering ratio θ (dimensionless) in terms of temperature, the carbon fraction f, and fixed material parameters (cohesive energy, Debye temperature, adsorption energy, C–H stretching and bending wavenumbers).

## Reproduction target
Compute the equilibrium vapor pressure P (MPa) as a function of temperature T (K) for a 3D solid (d=3, cohesive energy 7 eV) and a 2D solid (d=2, cohesive energy 5 eV) at carbon fractions f = 1×10⁻³ and f = 1×10⁻⁴. Compute the hydrogen covering ratio θ (dimensionless) as a function of T for the same solids at f = 0.01 and f = 0.005. Produce two CSV files:
- step_01_phase_boundary.csv: columns T, P_d3_f1e-3, P_d3_f1e-4, P_d2_f1e-3, P_d2_f1e-4. Temperature range 1000–2500 K, step ≤10 K.
- step_02_covering_ratio.csv: columns T, theta_d3_f0.01, theta_d3_f0.005, theta_d2_f0.01, theta_d2_f0.005. Temperature range 1000–2000 K, step ≤10 K.

Use the published parameter values: Debye temperature θ_D = 1860 K, adsorption energy ε_a = 4 eV, C–H stretching ν⟂ = 3107 cm⁻¹, bending ν∥ = 1405 cm⁻¹.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Implement the thermodynamic model
- Role: process
- Action: Write Python code that implements the chemical potentials and partition functions from the model (classical ideal atomic gases, d-dimensional Einstein solid, monohydride adsorption) and derives the closed-form expressions for total vapor pressure P (in MPa) and hydrogen covering ratio θ (dimensionless). Use the parameter values: cohesive energy ε_c = 7 eV for 3D solid and 5 eV for 2D solid, Debye temperature θ_D = 1860 K, adsorption energy ε_a = 4 eV, C–H stretching wavenumber k⟂ = 3107 cm⁻¹, bending wavenumber k∥ = 1405 cm⁻¹. The implementation must be reusable for subsequent computation steps.
- Evidence: none

### Step 2: Compute vapor pressure P (phase boundary)
- Role: scored (load-bearing)
- Action: Using the implemented model, compute equilibrium vapor pressure P (MPa) as a function of temperature T (K) for four cases: 3D solid (d=3, ε_c=7 eV) with carbon fraction f=1e-3 and f=1e-4, and 2D solid (d=2, ε_c=5 eV) with f=1e-3 and f=1e-4. Evaluate T from 1000 K to 2500 K in steps no larger than 10 K. Produce a CSV with columns: T, P_d3_f1e-3, P_d3_f1e-4, P_d2_f1e-3, P_d2_f1e-4.
- Output file: `/app/outputs/step_01_phase_boundary.csv`
- Format: csv
- Contract: Columns: T (numeric, Kelvin), P_d3_f1e-3 (numeric, MPa), P_d3_f1e-4 (numeric, MPa), P_d2_f1e-3 (numeric, MPa), P_d2_f1e-4 (numeric, MPa).
- Scoring: scored by hidden verifier

### Step 3: Compute hydrogen covering ratio θ
- Role: scored (load-bearing)
- Action: Using the same model, compute hydrogen covering ratio θ (dimensionless) as a function of temperature T (K) for four cases: 3D solid with f=0.01 and f=0.005, and 2D solid with f=0.01 and f=0.005. Evaluate T from 1000 K to 2000 K in steps no larger than 10 K. Produce a CSV with columns: T, theta_d3_f0.01, theta_d3_f0.005, theta_d2_f0.01, theta_d2_f0.005.
- Output file: `/app/outputs/step_02_covering_ratio.csv`
- Format: csv
- Contract: Columns: T (numeric, Kelvin), theta_d3_f0.01 (numeric, dimensionless), theta_d3_f0.005 (numeric, dimensionless), theta_d2_f0.01 (numeric, dimensionless), theta_d2_f0.005 (numeric, dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_phase_boundary.csv`
- `/app/outputs/step_02_covering_ratio.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_phase_boundary.csv
- path: `/app/outputs/step_01_phase_boundary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed equilibrium vapor pressure P as function of temperature T for four combinations of solid dimensionality (3D/2D) and carbon fraction f.
- schema:
  - `type`: table
  - `required_columns`: `T`, `P_d3_f1e-3`, `P_d3_f1e-4`, `P_d2_f1e-3`, `P_d2_f1e-4`
  - `units`:
    - `T`: K
    - `P_d3_f1e-3`: MPa
    - `P_d3_f1e-4`: MPa
    - `P_d2_f1e-3`: MPa
    - `P_d2_f1e-4`: MPa

### step_02_covering_ratio.csv
- path: `/app/outputs/step_02_covering_ratio.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed hydrogen covering ratio θ as function of temperature T for four combinations of solid dimensionality (3D/2D) and carbon fraction f.
- schema:
  - `type`: table
  - `required_columns`: `T`, `theta_d3_f0.01`, `theta_d3_f0.005`, `theta_d2_f0.01`, `theta_d2_f0.005`
  - `units`:
    - `T`: K
    - `theta_d3_f0.01`: 
    - `theta_d3_f0.005`: 
    - `theta_d2_f0.01`: 
    - `theta_d2_f0.005`:

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_phase_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "P_d3_f1e-3",
          "P_d3_f1e-4",
          "P_d2_f1e-3",
          "P_d2_f1e-4"
        ],
        "units": {
          "T": "K",
          "P_d3_f1e-3": "MPa",
          "P_d3_f1e-4": "MPa",
          "P_d2_f1e-3": "MPa",
          "P_d2_f1e-4": "MPa"
        }
      },
      "description": "Computed equilibrium vapor pressure P as function of temperature T for four combinations of solid dimensionality (3D/2D) and carbon fraction f."
    },
    {
      "file": "step_02_covering_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "theta_d3_f0.01",
          "theta_d3_f0.005",
          "theta_d2_f0.01",
          "theta_d2_f0.005"
        ],
        "units": {
          "T": "K",
          "theta_d3_f0.01": "",
          "theta_d3_f0.005": "",
          "theta_d2_f0.01": "",
          "theta_d2_f0.005": ""
        }
      },
      "description": "Computed hydrogen covering ratio θ as function of temperature T for four combinations of solid dimensionality (3D/2D) and carbon fraction f."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently implements the same thermodynamic model and recomputes the expected P and θ values for exactly the same T, f conditions. It reads your CSV files and compares each column against its recomputed reference using relative error tolerances. For each scored step, the reward is the fraction of rows (T points) for which all required columns are within the acceptable tolerance. The final reward is a weighted combination of the two step scores (phase boundary and covering ratio each carry a significant share). Reporting someone else’s numbers without correct computation will not pass; you must produce physically correct outputs from the model.
