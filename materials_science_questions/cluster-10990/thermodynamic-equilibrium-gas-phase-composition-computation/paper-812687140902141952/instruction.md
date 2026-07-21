# Phase Diagram and Hydrogen Coverage for Carbon in Vapor–Solid Equilibrium

## Problem background
The equilibrium between carbon solid phases (like diamond vs. graphite) and vapor in a hydrogen atmosphere is critical for understanding diamond film growth. This work models the system as classical ideal atomic gases (carbon and hydrogen) in contact with a crystalline solid treated as a d‑dimensional Einstein oscillator and a surface with monohydride adsorption. By equating chemical potentials, closed‑form expressions for total vapor pressure and hydrogen covering ratio are derived. Reproducing these expressions and the resulting curves quantifies the phase boundaries and surface coverage under controlled conditions.

## Approach
The method uses classical statistical mechanics:
- Vapor-phase chemical potentials for atomic carbon and hydrogen from the ideal gas translational partition function.
- Solid carbon as a d‑dimensional Einstein oscillator with a partition function that depends on the Debye temperature and cohesive energy.
- Surface adsorption centers as monohydride sites with a partition function that includes stretching and bending vibrational modes and an adsorption energy.

Equating the chemical potentials of the two phases yields closed-form expressions for the total vapor pressure P (MPa) and the hydrogen covering ratio θ (dimensionless). The explicit formulas derived in the paper are given below; you should use them directly for computation.

## Model equations and constants
The following closed-form expressions from the paper must be used exactly as written. All energies are in electronvolts per atom, wavenumbers in cm⁻¹, temperature in kelvin, and pressure in MPa.

**Vapor pressure P (Eq. 10):**

\[
P = 0.108 \,\frac{T^{5/2}}{f}\;
     \left[2\,\sinh\!\left(\frac{\theta_D}{2T}\right)\right]^{d}\;
     \exp\!\left(-\frac{11600\,\epsilon_c}{T}\right)
\]

where:
- \(d\) = dimensionality of the solid (3 for 3D, 2 for 2D),
- \(\epsilon_c\) = cohesive energy (eV/atom),
- \(\theta_D\) = Debye temperature (K),
- \(f\) = carbon fraction in the vapor,
- The constants 0.108 and 11600 are unit-conversion factors.

**Hydrogen covering ratio θ (Eqs. 14 and 15):**

Define

\[
X = 41.1 \;\frac{1-f}{f}\;\frac{Z_1}{q_1}
\]

then

\[
\theta = \frac{X}{1+X}
\qquad\text{(equivalent to } 1-\theta = \frac{1}{1+X}\text{)}
\]

where \(\frac{Z_1}{q_1}\) is given by

\[
\frac{Z_1}{q_1}=
2\,
\exp\!\left(-\frac{11600\,(\epsilon_c-\epsilon_a)}{T}\right)\;
\left[2\,\sinh\!\left(\frac{\theta_D}{2T}\right)\right]^{d}\;
\left[2\,\sinh\!\left(\frac{0.719\,k_\perp}{T}\right)\right]^{-1}\;
\left[2\,\sinh\!\left(\frac{0.719\,k_\parallel}{T}\right)\right]^{-2}
\]

- \(\epsilon_a\) = adsorption energy (eV/atom),
- \(k_\perp\) = C–H stretching wavenumber (cm⁻¹),
- \(k_\parallel\) = C–H bending wavenumber (cm⁻¹),
- The constants 41.1 and 0.719 are unit-conversion factors.

**Fixed parameter values (from the paper):**

| Parameter                 | Symbol      | Value    | Unit   |
|---------------------------|-------------|----------|--------|
| Debye temperature         | \(\theta_D\)| 1860     | K      |
| Cohesive energy (3D)      | \(\epsilon_c\) | 7.0  | eV     |
| Cohesive energy (2D)      | \(\epsilon_c\) | 5.0  | eV     |
| Adsorption energy         | \(\epsilon_a\) | 4.0  | eV     |
| C–H stretching wavenumber | \(k_\perp\) | 3107     | cm⁻¹   |
| C–H bending wavenumber    | \(k_\parallel\)| 1405  | cm⁻¹   |

These parameters are the only ones allowed; they must be used exactly as specified.

## Reproduction target
Compute the equilibrium vapor pressure P (MPa) as a function of temperature T (K) for a 3D solid (d=3, cohesive energy 7 eV) and a 2D solid (d=2, cohesive energy 5 eV) at carbon fractions f = 1×10⁻³ and f = 1×10⁻⁴. Compute the hydrogen covering ratio θ (dimensionless) as a function of T for the same solids at f = 0.01 and f = 0.005. Produce two CSV files:
- step_01_phase_boundary.csv: columns T, P_d3_f1e-3, P_d3_f1e-4, P_d2_f1e-3, P_d2_f1e-4. Temperature range 1000–2500 K, step ≤10 K.
- step_02_covering_ratio.csv: columns T, theta_d3_f0.01, theta_d3_f0.005, theta_d2_f0.01, theta_d2_f0.005. Temperature range 1000–2000 K, step ≤10 K.

The columns must be computed using the explicit formulas shown in “Model equations and constants” together with the fixed parameter table above. No other parameter values are allowed.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Implement the computational model
- Role: process
- Action: Write Python code that implements the formulas for P and θ given in “Model equations and constants”. Use the parameter values from the table (θ_D = 1860 K, ε_c = 7 eV for 3D / 5 eV for 2D, ε_a = 4 eV, k_⊥ = 3107 cm⁻¹, k_∥ = 1405 cm⁻¹). The code must be reusable for the subsequent computation steps.
- Evidence: none

### Step 2: Compute vapor pressure P (phase boundary)
- Role: scored (load-bearing)
- Action: Using the implemented formulas, compute equilibrium vapor pressure P (MPa) as a function of temperature T (K) for four cases: 3D solid (d=3, ε_c=7 eV) with carbon fraction f=1e-3 and f=1e-4, and 2D solid (d=2, ε_c=5 eV) with f=1e-3 and f=1e-4. Evaluate T from 1000 K to 2500 K in steps no larger than 10 K. Produce a CSV with columns: T, P_d3_f1e-3, P_d3_f1e-4, P_d2_f1e-3, P_d2_f1e-4.
- Output file: `/app/outputs/step_01_phase_boundary.csv`
- Format: csv
- Contract: Columns: T (numeric, Kelvin), P_d3_f1e-3 (numeric, MPa), P_d3_f1e-4 (numeric, MPa), P_d2_f1e-3 (numeric, MPa), P_d2_f1e-4 (numeric, MPa).
- Scoring: scored by hidden verifier

### Step 3: Compute hydrogen covering ratio θ
- Role: scored (load-bearing)
- Action: Using the same formulas, compute hydrogen covering ratio θ (dimensionless) as a function of temperature T (K) for four cases: 3D solid with f=0.01 and f=0.005, and 2D solid with f=0.01 and f=0.005. Evaluate T from 1000 K to 2000 K in steps no larger than 10 K. Produce a CSV with columns: T, theta_d3_f0.01, theta_d3_f0.005, theta_d2_f0.01, theta_d2_f0.005.
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