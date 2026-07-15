# Finite-deformation thermoviscoelastic constitutive framework for fiber-reinforced SMPCs

## Problem background
Shape memory polymer composites (SMPCs) can improve the mechanical properties of shape memory polymers, but carbon fiber reinforced SMPCs are typically limited to small strains because the tensile failure strain of carbon fiber is only about 2%. This work develops a finite-deformation thermoviscoelastic constitutive model for unidirectional continuous carbon fiber reinforced SMPCs, incorporating internal state variables to describe the structural relaxation and viscous flow of the matrix, and a hyperelastic model for the composite equilibrium response. A key open question is whether, by choosing an appropriate fiber inclination angle and fiber volume fraction, the composite can undergo finite uniaxial stretch (up to 1.2) while keeping the mechanical tensile strain of the carbon fiber below its failure limit. The model is used to simulate the shape memory cycle of these composites, providing predictions for stress-strain response, shape fixity, constrained recovery stress, and free recovery behavior.

## Approach
The thermomechanical behavior is described by a finite-deformation framework that splits the deformation into mechanical and thermal parts, and the mechanical deformation into elastic and viscous components. The structural relaxation of the SMP matrix is modeled with internal state variables using a nonequilibrium thermodynamics approach, where the relaxation time depends on entropy via a modified Adam-Gibbs form. Viscous flow is governed by a stress-activated Eyring model. The equilibrium stress is captured by a hyperelastic constitutive model for transversely isotropic fiber-reinforced composites. The effective elastic constants of the composite are computed from temperature-dependent matrix properties (storage modulus and Poisson's ratio) and fiber properties using a volume-averaging micromechanical model with a transverse contact coefficient, and transformed to the loading coordinate system under plane stress. Thermal deformation is modeled with a transversely isotropic coefficient of thermal expansion derived from a two-phase homogenization. The simulations are performed for a composite lamina with a prescribed fiber volume fraction and inclination angle, undergoing uniaxial tension and a full thermomechanical shape memory cycle that includes loading, cooling, unloading, constrained recovery, and free recovery.

## Reproduction target
Implement the finite-deformation thermoviscoelastic constitutive model for a unidirectional continuous carbon fiber reinforced SMPC lamina using the given material parameters. Focus on the specific case with fiber volume fraction vf = 0.004 and fiber inclination angle φ = 45°. Compute and output the following six artifacts as CSV files:

1. Mechanical tensile strain of the carbon fiber as a function of overall uniaxial stretch at 60 °C (fiber_strain.csv).
2. Composite stress in the loading direction as a function of overall stretch at 60 °C (stress_stretch.csv).
3. Full time history of temperature, stretch, and stress during the loading–cooling–unloading phases of a shape memory cycle (stress_stretch_cycle_first3.csv).
4. Shape fixity ratio for this configuration (shape_fixity_ratio.csv).
5. Constrained recovery stress as a function of temperature during heating (constrained_recovery.csv).
6. Free recovery stretch as a function of temperature during heating (free_recovery.csv).

All outputs must follow the column schemas and units specified in the workflow steps.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Material parameters
All material parameters are taken from the paper. Use the following numeric values exactly.

### SMP matrix parameters (Table 1)
- θ_β = 22.2 °C
- θ_g = 32 °C
- θ_f = 142.5 °C
- E1' = 2552.9 MPa
- E2' = 1876.3 MPa
- E3' = 5 MPa
- m1 = 19.3
- m2 = 58.4
- m3 = 177.6
- μ_g = 0.35
- μ_r = 0.499
- θ_m = 27.5 °C
- Z = 7
- Q/s_y = 175 °C/MPa
- η_ref = 12 MPa s
- θ_ref = 25 °C
- s_ref = 6 J/kg K
- T_1ref = -5 MPa
- c_p0 = 50 J/kg K
- k_0 = 1.4×10^{-4} /°C
- d = 1.5×10^{-17} J/kg
- e = 1.5×10^{-9} J/kg K (coupling parameter)
- v_t = 1×10^{-16} m^3/kg (off-diagonal coupling)
- w_t = 5×10^{-16} m^3/kg (additional coupling)
- B = 20000 J/kg
- τ_R0 = 3×10^{-2} s
- ρ = 1050 kg/m^3

### Carbon fiber parameters (Table 2)
- E_f1 = 230 GPa
- E_f2 = 8.2 GPa
- G_f12 = 27.3 GPa
- μ_f = 0.25
- α_f1 = -8.3×10^{-7} /°C
- α_f2 = 10×10^{-6} /°C
- Transverse contact coefficient C = 0.2

## Workflow steps

### Step 1: Compute effective composite elastic constants
- Role: process
- Action: Compute the temperature-dependent effective transversely isotropic elastic constants (E_C1, E_C2, mu_C21, mu_C12, G_C12) and the transformed off-axis compliance matrix Q_bar for the composite lamina with fiber volume fraction vf=0.004 and fiber inclination angle φ=45°. Use the volume-averaging micromechanical model (series-parallel mix) with transverse contact coefficient C=0.2, and the coordinate transformation formula for plane stress. The SMP matrix Young's modulus E_m(T) is given by the Mahieux-Reifsnider storage modulus model (with parameters θ_β, θ_g, θ_f, E1', E2', E3', m1, m2, m3), and Poisson's ratio μ_m(T) by the phase-transition model (with μ_g, μ_r, θ_m, Z). Use the provided carbon fiber properties (E_f1, E_f2, G_f12, μ_f).
- Evidence: `/app/outputs/effective_constants.json`

### Step 2: Mechanical fiber strain vs stretch
- Role: scored
- Action: Simulate uniaxial tension at 60°C. For overall stretch λ_xx from 1.0 to 1.2 in increments of 0.01, compute the mechanical tensile strain ε_f^M of the carbon fiber using the geometric relation and the mechanical stretch obtained from the plane‑stress solution of the composite constitutive equations. Write the results to fiber_strain.csv.
- Output file: `/app/outputs/fiber_strain.csv`
- Format: csv
- Contract: CSV with columns: stretch_xx (float, dimensionless), fiber_mechanical_strain (float, dimensionless). Rows for stretch from 1.0 to 1.2 in increments of 0.01.
- Scoring: scored by hidden verifier

### Step 3: Composite stress vs stretch
- Role: scored
- Action: Under the same uniaxial tension at 60°C and the same stretch range, compute the Cauchy stress σ_xx of the composite. Write the results to stress_stretch.csv.
- Output file: `/app/outputs/stress_stretch.csv`
- Format: csv
- Contract: CSV with columns: stretch_xx (float, dimensionless), stress_xx (float, Pa). Rows for stretch from 1.0 to 1.2 in increments of 0.01.
- Scoring: scored by hidden verifier

### Step 4: Shape memory cycle – loading, cooling, unloading
- Role: scored (load-bearing)
- Action: Simulate the thermomechanical shape memory cycle (steps 1–3): load to λ_xx=1.2 at strain rate 0.01 s⁻¹ at 60°C, hold 10 min; cool to 10°C at −2.5°C/min while holding stretch, hold 60 min; unload at −0.01 s⁻¹ strain rate, hold 10 min. Record time (seconds), temperature (°C), stretch_xx (dimensionless) and stress_xx (Pa) throughout and write to stress_stretch_cycle_first3.csv.
- Output file: `/app/outputs/stress_stretch_cycle_first3.csv`
- Format: csv
- Contract: CSV with columns: time (float, s), temperature (float, °C), stretch_xx (float, dimensionless), stress_xx (float, Pa). Covers Steps 1 (loading+hold), 2 (cooling+hold), 3 (unloading+hold).
- Scoring: scored by hidden verifier

### Step 5: Shape fixity ratio
- Role: scored
- Action: From the stretch history recorded in the previous step, extract the stretch value at the end of the unloading hold (reserved stretch). Compute the shape fixity ratio R_fix = (reserved_stretch / 1.2) × 100%. Write a single-row CSV with vf=0.004, phi=45, and the computed fixity_ratio to shape_fixity_ratio.csv.
- Output file: `/app/outputs/shape_fixity_ratio.csv`
- Format: csv
- Contract: CSV with columns: vf (float, dimensionless), phi (float, degrees), fixity_ratio (float, %). Single row.
- Scoring: scored by hidden verifier

### Step 6: Constrained recovery
- Role: scored
- Action: Starting from the final state of the previous cycle (temperature 10°C, stretch fixed), heat to 60°C at 2.5°C/min while holding stretch fixed. Record time (s), temperature (°C), and stress_xx (Pa) and write to constrained_recovery.csv.
- Output file: `/app/outputs/constrained_recovery.csv`
- Format: csv
- Contract: CSV with columns: time (float, s), temperature (float, °C), stress_xx (float, Pa). Covers heating from 10°C to 60°C at 2.5°C/min with stretch held fixed.
- Scoring: scored by hidden verifier

### Step 7: Free recovery
- Role: scored
- Action: Starting from the same final state but under zero stress, heat to 60°C at 2.5°C/min. Record time (s), temperature (°C), and stretch_xx (dimensionless) and write to free_recovery.csv.
- Output file: `/app/outputs/free_recovery.csv`
- Format: csv
- Contract: CSV with columns: time (float, s), temperature (float, °C), stretch_xx (float, dimensionless). Covers heating from 10°C to 60°C at 2.5°C/min under zero applied stress.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fiber_strain.csv`
- `/app/outputs/stress_stretch.csv`
- `/app/outputs/stress_stretch_cycle_first3.csv`
- `/app/outputs/shape_fixity_ratio.csv`
- `/app/outputs/constrained_recovery.csv`
- `/app/outputs/free_recovery.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fiber_strain.csv
- path: `/app/outputs/fiber_strain.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Mechanical tensile strain of the carbon fiber vs overall stretch at 60°C. The verifier checks that the strain at stretch=1.2 satisfies a threshold (≤ 0.02).
- schema:
  - `type`: table
  - `required_columns`: `stretch_xx`, `fiber_mechanical_strain`
  - `units`:
    - `stretch_xx`: dimensionless
    - `fiber_mechanical_strain`: dimensionless

### stress_stretch.csv
- path: `/app/outputs/stress_stretch.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Composite stress vs stretch at 60°C. The verifier extracts the stress at stretch=1.2 and compares it to a hidden paper value with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `stretch_xx`, `stress_xx`
  - `units`:
    - `stretch_xx`: dimensionless
    - `stress_xx`: Pa

### stress_stretch_cycle_first3.csv
- path: `/app/outputs/stress_stretch_cycle_first3.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Time history of stretch and stress during the first three steps of a shape memory cycle. The verifier recomputes the shape fixity ratio from this raw curve and compares it to the hidden paper value.
- schema:
  - `type`: table
  - `required_columns`: `time`, `temperature`, `stretch_xx`, `stress_xx`
  - `units`:
    - `time`: s
    - `temperature`: °C
    - `stretch_xx`: dimensionless
    - `stress_xx`: Pa

### shape_fixity_ratio.csv
- path: `/app/outputs/shape_fixity_ratio.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Agent-reported shape fixity ratio for the specific configuration. The verifier compares this value to the paper-reported hidden value with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `vf`, `phi`, `fixity_ratio`
  - `units`:
    - `vf`: dimensionless
    - `phi`: degrees
    - `fixity_ratio`: %

### constrained_recovery.csv
- path: `/app/outputs/constrained_recovery.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Constrained recovery stress vs temperature during heating. The verifier extracts the peak stress and the temperature at which stress first becomes positive, comparing them to hidden paper values.
- schema:
  - `type`: table
  - `required_columns`: `time`, `temperature`, `stress_xx`
  - `units`:
    - `time`: s
    - `temperature`: °C
    - `stress_xx`: Pa

### free_recovery.csv
- path: `/app/outputs/free_recovery.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Free recovery stretch vs temperature during heating. The verifier finds the temperature at which stretch returns to within 1% of 1.0 and compares it to the hidden paper value.
- schema:
  - `type`: table
  - `required_columns`: `time`, `temperature`, `stretch_xx`
  - `units`:
    - `time`: s
    - `temperature`: °C
    - `stretch_xx`: dimensionless

Notes: The model parameters are given explicitly in the paper (Tables 1 and 2); the agent must implement the constitutive equations and run the four prescribed simulation cases. The verifier extracts key quantities from the raw output curves and compares them to paper-reported values with generous tolerances to absorb implementation differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fiber_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "stretch_xx",
          "fiber_mechanical_strain"
        ],
        "units": {
          "stretch_xx": "dimensionless",
          "fiber_mechanical_strain": "dimensionless"
        }
      },
      "description": "Mechanical tensile strain of the carbon fiber vs overall stretch at 60°C. The verifier checks that the strain at stretch=1.2 satisfies a threshold (≤ 0.02)."
    },
    {
      "file": "stress_stretch.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "stretch_xx",
          "stress_xx"
        ],
        "units": {
          "stretch_xx": "dimensionless",
          "stress_xx": "Pa"
        }
      },
      "description": "Composite stress vs stretch at 60°C. The verifier extracts the stress at stretch=1.2 and compares it to a hidden paper value with tolerance."
    },
    {
      "file": "stress_stretch_cycle_first3.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "temperature",
          "stretch_xx",
          "stress_xx"
        ],
        "units": {
          "time": "s",
          "temperature": "°C",
          "stretch_xx": "dimensionless",
          "stress_xx": "Pa"
        }
      },
      "description": "Time history of stretch and stress during the first three steps of a shape memory cycle. The verifier recomputes the shape fixity ratio from this raw curve and compares it to the hidden paper value."
    },
    {
      "file": "shape_fixity_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "vf",
          "phi",
          "fixity_ratio"
        ],
        "units": {
          "vf": "dimensionless",
          "phi": "degrees",
          "fixity_ratio": "%"
        }
      },
      "description": "Agent-reported shape fixity ratio for the specific configuration. The verifier compares this value to the paper-reported hidden value with a tolerance."
    },
    {
      "file": "constrained_recovery.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "temperature",
          "stress_xx"
        ],
        "units": {
          "time": "s",
          "temperature": "°C",
          "stress_xx": "Pa"
        }
      },
      "description": "Constrained recovery stress vs temperature during heating. The verifier extracts the peak stress and the temperature at which stress first becomes positive, comparing them to hidden paper values."
    },
    {
      "file": "free_recovery.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "temperature",
          "stretch_xx"
        ],
        "units": {
          "time": "s",
          "temperature": "°C",
          "stretch_xx": "dimensionless"
        }
      },
      "description": "Free recovery stretch vs temperature during heating. The verifier finds the temperature at which stretch returns to within 1% of 1.0 and compares it to the hidden paper value."
    }
  ],
  "notes": "The model parameters are given explicitly in the paper (Tables 1 and 2); the agent must implement the constitutive equations and run the four prescribed simulation cases. The verifier extracts key quantities from the raw output curves and compares them to paper-reported values with generous tolerances to absorb implementation differences."
}
```

## How you are scored
A hidden verifier reads your output artifacts and independently evaluates each scored stage. It will extract key quantities from your raw curves and compare them to hidden reference criteria: from fiber_strain.csv it checks whether the fiber mechanical strain at stretch 1.2 stays below a threshold; from stress_stretch.csv it compares the stress at a specific stretch; from stress_stretch_cycle_first3.csv it recomputes the shape fixity ratio; from shape_fixity_ratio.csv it compares the reported ratio; from constrained_recovery.csv it identifies the peak stress and the temperature at which stress first becomes positive; from free_recovery.csv it finds the temperature at which stretch returns to near 1.0. Each stage carries a weight, and the final reward is the weighted sum of the stage scores. The verifier uses tolerances that account for reasonable numerical differences between implementations, and for directional metrics meeting or exceeding the reference earns full credit.
