# Coupled thermo-electromechanical simulation of a composite axisymmetric resonator

## Problem background
Ultrasonic power transducers used in applications such as plastic welding generate internal heat due to mechanical vibratory loss in the elastic materials and dielectric loss in the ferroelectric elements. The resulting temperature rise alters material properties, causes thermal expansion, and changes the resonant frequency and electrical capacitance, potentially limiting the operational envelope. Understanding and predicting the steady-state temperature distribution and its effect on transducer characteristics is therefore essential for design.

This task focuses on a bolt-clamped Langevin-type transducer (BLT) — a composite resonator consisting of multiple materials clamped together. The transducer operates in its fundamental longitudinal mode and is cooled by natural convection. You will use the finite element method to simulate the coupled electromechanical vibration and the resulting heat generation and diffusion to predict the transducer's behavior under operating conditions.

The BLT is composed of the following parts (from tip to back): a titanium front plate that is 100 mm long with an outer diameter of 30 mm at the tip, stepping to 50 mm at a flange located 50 mm from the tip; four PZT (MT-18) ceramic disks, each 5 mm thick, with outer diameter 38 mm and inner diameter 18 mm, polarized in the thickness direction and arranged with alternating polarity; beryllium-copper electrode foils (0.2 mm thick) inserted between the ceramic disks and at the outer faces; an aluminum back plate, 30 mm long and 38 mm in diameter; and an iron bolt (M8) passing through the center of all components, clamped with an iron nut at the back. The outer electrode of the first and third PZT disks from the tip are grounded, while the second and fourth are driven with an AC voltage of 1 kV rms. The transducer is cooled by natural convection with a heat-transfer coefficient of 9 J/(m²·s·°C) and thermal radiation (emissivity 0.9, radiation shape factor 0.9) at all exposed surfaces. ### Material properties

| Property | PZT (MT-18) | Titanium | Aluminum | Iron | Be-Cu |
|---|---|---|---|---|---|
| Density (kg/m³) | 7600 | 4510 | 2690 | 7840 | 8250 |
| Young's modulus (N/m²) | — | 9.93×10¹⁰ | 7.03×10¹⁰ | 19.86×10¹⁰ | 11.2×10¹⁰ |
| Temp. coeff. of Young's modulus (/°C) | — | −6.5×10⁻⁴ | −5.5×10⁻⁴ | −5.1×10⁻⁴ | −3.87×10⁻⁴ |
| Poisson's ratio | 0.31 | 0.3 | 0.34 | 0.29 | 0.3 |
| Damping coefficient | 5.5×10⁻⁴ | 4.5×10⁻⁴ | 2.21×10⁻⁴ | 1.09×10⁻⁴ | 2.2×10⁻⁴ |
| Coefficient of thermal expansion (1/°C) | 12×10⁻⁶ | 8.6×10⁻⁶ | 30.2×10⁻⁶ | 11.8×10⁻⁶ | 11.5×10⁻⁶ |
| Specific heat (J/(kg·°C)) | 491 | 472 | 877 | 640 | 380 |
| Thermal conductivity (W/(m·°C)) | 1.5 | 10.0 | 236 | 83.5 | 403 |
| Dielectric loss factor tan δ | 0.003 | — | — | — | — |
| Relative permittivity ε₁₁^s/ε₀ | 1300 | — | — | — | — |
| Relative permittivity ε₃₃^s/ε₀ | 1400 | — | — | — | — |
| Temp. coeff. of permittivity (/°C) | 3.2×10⁻³ | — | — | — | — |
| Elastic stiffness matrix Cᴱ (N/m², Voigt) | [[14.6,9.9,9.9,0],[9.9,17.5,10.1,0],[9.9,10.1,17.5,0],[0,0,0,2.85]] ×10¹⁰ | — | — | — | — |
| Temp. coeff. of stiffness (/°C) | −2×10⁻⁴ | — | — | — | — |
| Piezoelectric constant matrix e (C/m²) | [[19.5,−1.13,−1.13,0],[0,0,0,7.25]] | — | — | — | — |
| Temp. coeff. of piezoelectric constants (/°C) | 1×10⁻⁴ | — | — | — | — |

For non-piezoelectric materials the elastic constitutive law uses Young's modulus and Poisson's ratio; for PZT use the full stiffness matrix and piezoelectric coupling. Temperature dependence of elastic constants, permittivity and piezoelectric constants is implemented via the coefficients above: updated value = reference value × (1 + coeff × (T − 20 °C)).

## Approach
The simulation treats the transducer as an axisymmetric body and discretizes the equations of motion and electrostatics with the finite element method, yielding a coupled linear system for nodal displacements and electric potentials. From the steady-state vibration solution, the strain distribution in the elastic solids and the electric field distribution in the piezoelectric ceramics are obtained.

Mechanical vibratory loss per unit volume is modeled as proportional to the square of the vibrational strain, while dielectric loss is proportional to the square of the electric field intensity. These element-wise heat sources drive a steady-state heat diffusion equation. Thermal boundary conditions include natural convection (specified heat-transfer coefficient) and thermal radiation at exposed surfaces.

The temperature solution modifies material stiffness, capacitance, and coupling matrices through their temperature coefficients, and also alters the mesh geometry via thermal expansion. Because the changed geometry and properties shift the resonance, the procedure iterates: after each thermal update, the electromechanical equations are re-solved, and the new resonant frequency is compared to the previous iteration; the loop continues until the relative change in resonant frequency falls below a preset convergence tolerance.

Finally, from the converged solution, the transducer's steady-state characteristics—resonant frequency, displacement amplitude at the tip, capacitance at a low frequency, and surface temperature profile—are extracted.

## Reproduction target
Build the simulation as described for the bolt-clamped Langevin-type transducer under natural convection. From the converged solution, extract these four quantities:
- resonant frequency of the fundamental longitudinal mode (Hz),
- maximum displacement amplitude at the tip (µm),
- capacitance at a driving frequency of 1 kHz (pF), estimated from the input admittance,
- steady-state temperature at five points along the outer surface of the titanium front plate, measured from the tip: z = 0, 25, 50, 75, and 100 mm (in °C).

Write these outputs into the file `/app/outputs/results.json` following the schema specified in the Output contract. The values you report are what the verifier will compare against a hidden reference derived from experimental measurements.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Build FE model for BLT
- Role: process
- Action: Generate an axisymmetric finite element mesh of the bolt-clamped Langevin-type transducer using the geometry from the problem description. Assemble the stiffness matrix K, mass matrix M, damping matrices R and R', electromechanical coupling matrix P, and capacitance matrix G using the provided material constants (Young's modulus, Poisson's ratio, density, piezoelectric tensors, dielectric constants, damping coefficients, etc.).
- Evidence: none

### Step 2: Initial electromechanical simulation
- Role: process
- Action: Solve the coupled frequency-domain equations without thermal effects to compute displacement distribution, strain distribution, electric potential distribution, resonant frequency, and capacitance at 1 kHz. This serves as the baseline for the iterative thermal loop.
- Evidence: none

### Step 3: Iterative coupled thermo-electromechanical solution
- Role: process
- Action: Iterate the coupled thermal-electromechanical loop until relative change in resonant frequency falls below a convergence tolerance: (a) compute elementwise heat sources from mechanical vibratory loss and dielectric loss using the latest strain and electric field; (b) solve the steady-state heat diffusion equation with natural convection (heat-transfer coefficient τ = 9 J/(m²·s·°C), emissivity 0.9, radiation shape factor 0.9) and thermal radiation; (c) compute thermal expansion and update nodal coordinates; (d) update temperature-dependent material matrices (stiffness, capacitance, coupling) using the temperature coefficients; (e) re-solve the electromechanical equations to obtain updated vibration fields and resonant frequency.
- Evidence: `/app/outputs/convergence_log.txt`

### Step 4: Output final transducer characteristics
- Role: scored (load-bearing)
- Action: From the converged simulation extract: (i) resonant frequency of the fundamental longitudinal mode (Hz), (ii) maximum displacement at the tip (µm), (iii) capacitance at 1 kHz (pF) via input admittance, and (iv) steady-state temperature at outer surface points z = 0, 25, 50, 75, 100 mm from the tip (°C). Write results to results.json.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {"resonant_frequency_hz": float, "maximum_displacement_um": float, "capacitance_pF": float, "temperature_profile": [{"z_mm": float, "temperature_C": float}]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Final computed characteristics of the bolt-clamped Langevin-type transducer under natural convection. The checker compares these reported values to the paper's experimental measurements using absolute difference within hidden tolerances.
- schema:
  - `type`: object
  - `required`:
    - `resonant_frequency_hz`: number
    - `maximum_displacement_um`: number
    - `capacitance_pF`: number
    - `temperature_profile`:
      - `z_mm`: number
      - `temperature_C`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `resonant_frequency_hz`: Hz
    - `maximum_displacement_um`: µm
    - `capacitance_pF`: pF
    - `temperature_profile.z_mm`: mm
    - `temperature_profile.temperature_C`: °C

Notes: The geometry and full material constants are described in the instruction. Only natural convection is required; forced convection is omitted. Thermal stress distribution is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "resonant_frequency_hz": "number",
          "maximum_displacement_um": "number",
          "capacitance_pF": "number",
          "temperature_profile": [
            {
              "z_mm": "number",
              "temperature_C": "number"
            }
          ]
        },
        "items": {},
        "required_columns": [],
        "units": {
          "resonant_frequency_hz": "Hz",
          "maximum_displacement_um": "µm",
          "capacitance_pF": "pF",
          "temperature_profile.z_mm": "mm",
          "temperature_profile.temperature_C": "°C"
        }
      },
      "description": "Final computed characteristics of the bolt-clamped Langevin-type transducer under natural convection. The checker compares these reported values to the paper's experimental measurements using absolute difference within hidden tolerances."
    }
  ],
  "notes": "The geometry and full material constants are described in the instruction. Only natural convection is required; forced convection is omitted. Thermal stress distribution is not scored."
}
```

## How you are scored
Your submission is evaluated by a hidden automated verifier. It reads the file `results.json` you produce and compares each reported quantity—resonant frequency, maximum displacement, capacitance, and the five temperature values—against reference values using tolerance-based scoring. Each component contributes a share of the total reward (0–1). The verifier does not have access to your code or intermediate logs; only the final numeric outputs in `results.json` are used.

To earn a high reward, your simulation must faithfully implement the coupled thermo-electromechanical pipeline and converge to values consistent with the physical transducer's measured performance, rather than simply guessing or hardcoding approximate numbers. Meeting or exceeding the reference accuracy earns full credit for each metric; larger deviations reduce the score.
