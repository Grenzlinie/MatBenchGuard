# Hysteresis Impact on Plate-PZT Vibration Control

## Problem background
Vibration control of thin plates using bonded piezoelectric (PZT) wafers can be achieved through passive resonant shunts or hybrid active-passive schemes. When the PZT transducer is driven at moderate to high levels, its dielectric hysteresis may alter the effective electroelastic coupling, potentially reducing the attenuation that an optimized shunt can provide. This task examines a simply-supported plate with a surface-bonded PZT wafer, modeled with the Ishlinskii hysteresis (IM) model. The goal is to determine the steady-state transverse displacement amplitude at a measurement point under harmonic point force excitation at the first natural frequency, for different shunt configurations and force amplitudes, so that the influence of hysteresis on vibration attenuation can be assessed.

## Approach
The workflow is as follows. First, the optimal inductance L* and resistance R* for the passive LR shunt, and the optimal active control voltage Vc* for the hybrid case, are computed from the linearized coupled electroelastic equations using the plate and PZT physical parameters (geometry, material properties, first mode), ignoring hysteresis. Then, a single-mode model of the coupled plate–PZT system is implemented, incorporating the five-element Ishlinskii hysteresis model with the provided elastic coefficients and slide constants. The system is simulated under harmonic point-force excitation at the first mode frequency for three shunt configurations: open circuit (no shunt, no active voltage), passive optimized LR shunt (L*, R*, Vc=0), and hybrid (L*, R*, Vc*). The force amplitude is set to a low value (1 N) and a high value (5 N). For each case the steady-state transverse displacement amplitude at the measurement point (x=279.4 mm, y=133.3 mm on the plate) is recorded. By comparing the attenuation achieved at low and high excitation levels, the effect of hysteresis on vibration control can be evaluated.

## Reproduction target
The primary scored output is a CSV file `/app/outputs/plate_displacement_results.csv` containing the computed displacement amplitudes for all six scenarios (2 forces × 3 shunt cases). The checker will read this file and evaluate whether the displacement ratios (passive/open and hybrid/open) exhibit a physically consistent trend with respect to the force amplitude, as expected from a system with hysteresis. There is no absolute target displacement value; your simulation must faithfully implement the described model, and the checker will verify that the resulting trends match the established qualitative behavior.

## Assets

- Python runtime with numpy, scipy: numpy, scipy
## Physical system parameters

**Plate (steel):** density ρ_pl = 7800 kg/m³, ν_pl = 0.3, E_pl = 2×10¹¹ N/m², L_pl = 560 mm, b_pl = 270 mm, h_pl = 1.5 mm.

**PZT wafer (PZT-5H):** density ρ_pz = 7800 kg/m³, ν_pz = 0.4, E_pz = 1×10¹¹ N/m²,
g₃₁ = –10.1×10⁻³ V·m/N, h₃₁ = –1.35×10⁹ V/m,
L_pz = b_pz = 72.4 mm, h_pz = 0.267 mm.
Position: x₁ = 27.3 mm, x₂ = 99.7 mm, y₁ = 10 mm, y₂ = 82.4 mm.
Forcing: (x=250 mm, y=50 mm). Measurement: (x_m=279.4 mm, y_m=133.3 mm).

**First mode (1,1):** natural frequency ω₁₁/(2π) = 61.04 Hz, damping ratio ζ = 0.0061.

**Ishlinskii model coefficients (IM, n=5):**
Elastic coefficients β_T^(i)  [units: N/m²] :
[3.0868e6, 2.3188e6, 1.8356e6, 1.418e6, 16.7796e6]
Slide constants e_rc^(i)  [units: N/m²] :
[0.8996, 1.3515, 1.6048, 1.6529, ∞]   (the last element is a pure reversible spring, no sliding).


### Step 1: Compute optimal shunt and control parameters
- Role: process
- Action: Compute the optimal shunt inductance L* and resistance R* for the first mode (1,1) using the linearized coupled equations that ignore hysteresis:

  A = (x₂ – x₁) × (y₂ – y₁)                                  (PZT patch area)
  J₂ = 0.5 × [ (h_pl/2 + h_pz)² – (h_pl/2)² ]                 (plate‑PZT coupling moment arm)
  ω₁₁ = 2π × 61.04 rad/s

  L* = h_pz × (β₃₃ᵀ + 2·h₃₁·g₃₁) / ( ω₁₁² × A )

  I_shape = ∫_{y₁}^{y₂} [ (∂Φ/∂x)(x₂,y) – (∂Φ/∂x)(x₁,y) ] dy  +  ∫_{x₁}^{x₂} [ (∂Φ/∂y)(x,y₂) – (∂Φ/∂y)(x,y₁) ] dx
  where Φ(x,y) = sin(π x / L_pl) sin(π y / b_pl).

  R* = (1/ω₁₁) × sqrt(  h_pz × (β₃₃ᵀ + 2·h₃₁·g₃₁ ) × J₂ × ( h₃₁ + g₃₁·E_pz/(1–ν_pz) ) × I_shape  /  ( 2 × A² )  )

  Compute the optimal active control voltage amplitude per unit force, Vc_over_F, as a complex number:
  Vc_over_F = [ –L*·ω₁₁²  +  j·ω₁₁·R*  +  h_pz·(β₃₃ᵀ + 2·h₃₁·g₃₁)/A ]  /  [ J₂·( h₃₁ + g₃₁·E_pz/(1–ν_pz) ) · I_shape / (2·A) ]

  Save L* (scalar, H), R* (scalar, Ω) and Vc_over_F (complex, V/N) as a JSON object to `/app/outputs/optimal_params.json`.
- Evidence: `/app/outputs/optimal_params.json`

### Step 2: Simulate vibration response with hysteresis
- Role: scored (load-bearing)
- Action: Implement the Ishlinskii hysteresis model (IM, n=5) using the provided elastic coefficients and slide constants. Implement the single-mode coupled electromechanical equations for the simply-supported plate with bonded PZT wafer. Using the optimal L*, R*, Vc* from step_0, compute the steady-state transverse displacement amplitude at the measurement point (x_m=279.4 mm, y_m=133.3 mm) for harmonic point-force excitation at the first natural frequency. Perform the simulation for force amplitudes F = 1 N and F = 5 N, and for three shunt configurations: open circuit (no shunt), optimized LR shunt (passive), and hybrid (LR shunt + active voltage Vc*). Write the results to a CSV file with columns: force_amplitude, shunt_case, displacement_amplitude.
- Output file: `/app/outputs/plate_displacement_results.csv`
- Format: csv
- Contract: CSV with columns: force_amplitude (float, N), shunt_case (string: one of 'open', 'passive', 'hybrid'), displacement_amplitude (float, m). There must be six rows (2 forces × 3 cases).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/plate_displacement_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### plate_displacement_results.csv
- path: `/app/outputs/plate_displacement_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Transverse displacement amplitude at the measurement point for two force amplitudes and three control configurations. The structural checker verifies that the displacement amplitudes exhibit a physically consistent trend consistent with hysteresis degradation, without specifying the exact direction.
- schema:
  - `type`: table
  - `required_columns`: `force_amplitude`, `shunt_case`, `displacement_amplitude`
  - `units`:
    - `force_amplitude`: N
    - `displacement_amplitude`: m

Notes: All parameters are public and taken directly from the paper's Table 1. The simulation requires no external dataset.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "plate_displacement_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "force_amplitude",
          "shunt_case",
          "displacement_amplitude"
        ],
        "units": {
          "force_amplitude": "N",
          "displacement_amplitude": "m"
        }
      },
      "description": "Transverse displacement amplitude at the measurement point for two force amplitudes and three control configurations. The structural checker verifies that the displacement amplitudes exhibit a physically consistent trend consistent with hysteresis degradation, without specifying the exact direction."
    }
  ],
  "notes": "All parameters are public and taken directly from the paper's Table 1. The simulation requires no external dataset."
}
```

## How you are scored
The hidden verifier independently scores each workflow stage’s artifact. For Step 1, it checks that `optimal_params.json` exists and contains numeric L*, R*, and Vc*. For Step 2 (the scored step), the verifier reads `plate_displacement_results.csv`, validates its schema (six rows, correct columns, numeric displacements), and then computes the attenuation ratios `displacement_passive / displacement_open` and `displacement_hybrid / displacement_open` for both force amplitudes. It compares these ratios to a hidden structural condition derived from the physics of the hysteresis model. The reward is computed from the agreement with that condition; a correct simulation that reflects the actual behavior of the hysteretic system earns full credit. Reporting a preset number without performing the simulation is not sufficient.
