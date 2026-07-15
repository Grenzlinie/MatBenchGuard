# Thermomechanical Stress Analysis of a Viscoplastic Disk under Impact

## Problem background
This task addresses the nonisothermal, adiabatic axial compression of a thin homogeneous disk made of an incompressible viscoplastic material. The disk is placed between an impactor and a rigid anvil and is subjected to a mechanical impact along its axis. During the initial elastic stage the disk deforms slightly until yielding begins on the contact surface. Once plastic flow develops, the mean pressure, disk thickness, impactor velocity, and disk temperature evolve together, coupled through a pressure- and temperature-dependent yield stress, inertial effects, and plastic dissipation. As the material heats, its strength may diminish, potentially leading to rapid thermal softening. Understanding this coupled thermomechanical response is important for the analysis of material treatment by pulse loading and for assessing the sensitivity of energetic materials to impact. The aim is to compute the time evolution and the final values of the mechanical and thermal variables—pressure, temperature, disk thickness, impactor velocity, contact surface velocity—as well as characteristic time intervals (plastic onset time, plastic flow duration, and thermal softening time) for a given set of geometry, loading, and material parameters.

## Approach
The core of the model is a closed autonomous system of five ordinary differential equations for the mean pressure p, contact surface velocity w, disk thickness δ, impactor centre-of-mass velocity v, and temperature T.

**Yield stress** – The plastic flow stress depends on temperature and pressure:
σ_s = σ_s0 * ((Tm - T) / (Tm - T0))^n,   Tm = Tm0 + β p.

**Mean pressure equation** (with inertial and viscous terms; set viscosity μ = 0 for the baseline):
p = σ_s (1 + 2R / (3√3 δ)) + 3μ w/δ + (ρ R² / (8 δ²)) (1.5 w² + δ dw/dt).

**Adiabatic heat balance:**
ρ c_p dT/dt = (2 σ_s / (3√3)) (R w / δ²) + (3/2) (μ R² w² / δ⁴).

**Kinematic / dynamic relations:**
dδ/dt = -w,   dv/dt = -p π R² / M,   dp/dt = (K / (π R²)) (v - w).

**Initial conditions (plastic flow onset):**
- p_x = v0 √(M K) / (π R²),   t_x = π √(M / K).
- p0 = σ_s0 (1 + 2R / (3√3 δ0)).
- t1 = √(M / K) arcsin(p0 / p_x),   (onset time).
- v(t1) = v0 √(1 - (p0 / p_x)²).
- w(t1) = v(t1) / (1 + π R² E / (K δ0)).
- δ(t1) = δ0,   p(t1) = p0,   T(t1) = T0.

**Integration and termination:** Integrate numerically (e.g., scipy.integrate.solve_ivp with RK45) from t1 using the initial values above, with μ = 0 and other parameters as given. Terminate when v reaches zero or when T reaches the pressure-dependent melting point Tm. Record the full time series; find the instant of peak pressure after yielding, t_peak (the time where p reaches a maximum after t1).

**Characteristic quantities to extract:**
- t1, p0 (onset time and pressure).
- tm = t_peak - t1 (plastic flow duration).
- tp = t_end - t_peak (thermal softening time).
- Final values at termination:  pk = p(t_end), Tk = T(t_end), vk = v(t_end), wk = w(t_end), δk = δ(t_end).
Units conversions: times to µs, pressures to GPa, velocities to m/s, thickness to mm, temperature to K.

## Reproduction target
Your goal is to perform the numerical simulation described above for the following baseline parameter set: disk radius R = 5 mm, impactor mass M = 10 kg, initial impact velocity v0 = 2 m/s, loading system stiffness K = 200 MN/m, initial disk thickness δ0 = 0.13 mm, initial yield stress σ_s0 = 59 MPa, elastic modulus E = 10 GPa, normal melting point Tm0 = 413 K, initial temperature T0 = 293 K, pressure–temperature coefficient β = 0.2 K/MPa, hardening exponent n = 0.6, volumetric heat capacity ρc_p = 2 J/(cm³·K), and plastic viscosity μ = 0. Run the simulation, extract the following quantities at termination, and write them to `/app/outputs/final_values.json`: the plastic onset time t1 (µs), the onset pressure p0 (GPa), the plastic flow duration tm (µs), the thermal softening time tp (µs), the final pressure pk (GPa), the final temperature Tk (K), the final impactor velocity vk (m/s), the final contact surface velocity wk (m/s), and the final disk thickness δk (mm). The JSON file must contain exactly these nine keys: `t1_us`, `p0_GPa`, `tm_us`, `tp_us`, `pk_GPa`, `Tk_K`, `vk_m_per_s`, `wk_m_per_s`, `delta_k_mm`.

Optionally, repeat the simulation with the same parameters except that the initial thickness is changed to δ0 = 1 mm, and save the same set of final values to `/app/outputs/delta0_1mm_final_values.json` using the same keys.

## Assets

- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Compute onset of plastic flow
- Role: process
- Action: Using the given geometry, loading, and material parameters (R=5 mm, M=10 kg, v0=2 m/s, K=200 MN/m, δ0=0.13 mm, σ_s0=59 MPa, E=10 GPa), compute the plastic flow onset time t1, initial mean pressure p0, impactor velocity v(t1), and contact surface velocity w(t1) from the standard elastic impact formulas. Store these values for the simulation step.
- Evidence: `/app/outputs/onset_values.json`

### Step 2: Simulate baseline impact and extract final values
- Role: scored (load-bearing)
- Action: Implement the system of five ordinary differential equations that describe the nonisothermal viscoplastic compression: (i) the mean pressure relation that involves a temperature- and pressure-dependent yield stress, plastic viscosity μ=0, and inertial terms; (ii) the adiabatic heat balance including plastic and viscous dissipation; (iii) kinematic and dynamic equations for disk thickness δ, impactor centre-of-mass velocity v, and pressure p. Use the initial conditions from step_compute_onset and the baseline parameters (T_m0=413 K, T0=293 K, β=0.2 K/MPa, n=0.6, ρc_p=2 J/(cm³·K), μ=0). Integrate numerically with an explicit Runge–Kutta method until the termination condition (v=0 or T reaches the pressure-dependent melting point Tm). Extract the following quantities at termination: final pressure pk, final temperature Tk, final impactor velocity vk, final contact surface velocity wk, final disk thickness δk. Also record the plastic flow onset time t1, onset pressure p0, plastic flow duration tm (time from onset to peak pressure after yielding), and thermal softening time tp (time from peak to termination). Write all extracted values with specified units to final_values.json.
- Output file: `/app/outputs/final_values.json`
- Format: json
- Contract: JSON object with numeric keys: t1_us (time in µs), p0_GPa (pressure in GPa), tm_us (time in µs), tp_us (time in µs), pk_GPa (pressure in GPa), Tk_K (temperature in K), vk_m_per_s (velocity in m/s), wk_m_per_s (velocity in m/s), delta_k_mm (thickness in mm).
- Scoring: scored by hidden verifier

### Step 3: Optional: re-run with δ0=1 mm
- Role: scored
- Action: (Optional) Repeat the baseline simulation with the initial disk thickness changed to δ0 = 1 mm, keeping all other parameters exactly as in the baseline. Write the same set of final values to the file delta0_1mm_final_values.json. The file format and keys are the same as in final_values.json.
- Output file: `/app/outputs/delta0_1mm_final_values.json`
- Format: json
- Contract: JSON object with same keys as final_values.json.
- Scoring: scored by hidden verifier (structural trend check)

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/final_values.json`
- `/app/outputs/delta0_1mm_final_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### final_values.json
- path: `/app/outputs/final_values.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Required final characteristic values for the baseline parameter set; compared to hidden reference within tolerances.
- schema:
  - `type`: object
  - `required`: `t1_us`, `p0_GPa`, `tm_us`, `tp_us`, `pk_GPa`, `Tk_K`, `vk_m_per_s`, `wk_m_per_s`, `delta_k_mm`
  - `properties`:
    - `t1_us`:
      - `type`: number
      - `unit`: µs
    - `p0_GPa`:
      - `type`: number
      - `unit`: GPa
    - `tm_us`:
      - `type`: number
      - `unit`: µs
    - `tp_us`:
      - `type`: number
      - `unit`: µs
    - `pk_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Tk_K`:
      - `type`: number
      - `unit`: K
    - `vk_m_per_s`:
      - `type`: number
      - `unit`: m/s
    - `wk_m_per_s`:
      - `type`: number
      - `unit`: m/s
    - `delta_k_mm`:
      - `type`: number
      - `unit`: mm

### delta0_1mm_final_values.json
- path: `/app/outputs/delta0_1mm_final_values.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Optional file for the δ0=1 mm variation. If present, the checker verifies structural trends: tp should be larger and Tk should be lower than the baseline.
- schema:
  - `type`: object
  - `required`: `t1_us`, `p0_GPa`, `tm_us`, `tp_us`, `pk_GPa`, `Tk_K`, `vk_m_per_s`, `wk_m_per_s`, `delta_k_mm`
  - `properties`:
    - `t1_us`:
      - `type`: number
      - `unit`: µs
    - `p0_GPa`:
      - `type`: number
      - `unit`: GPa
    - `tm_us`:
      - `type`: number
      - `unit`: µs
    - `tp_us`:
      - `type`: number
      - `unit`: µs
    - `pk_GPa`:
      - `type`: number
      - `unit`: GPa
    - `Tk_K`:
      - `type`: number
      - `unit`: K
    - `vk_m_per_s`:
      - `type`: number
      - `unit`: m/s
    - `wk_m_per_s`:
      - `type`: number
      - `unit`: m/s
    - `delta_k_mm`:
      - `type`: number
      - `unit`: mm

Notes: The baseline simulation uses μ=0 (no viscous term). The agent decides numerical integration settings (tolerances, step sizes). The optional δ0=1 mm file is not required but provides bonus validation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "final_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "t1_us",
          "p0_GPa",
          "tm_us",
          "tp_us",
          "pk_GPa",
          "Tk_K",
          "vk_m_per_s",
          "wk_m_per_s",
          "delta_k_mm"
        ],
        "properties": {
          "t1_us": {
            "type": "number",
            "unit": "µs"
          },
          "p0_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "tm_us": {
            "type": "number",
            "unit": "µs"
          },
          "tp_us": {
            "type": "number",
            "unit": "µs"
          },
          "pk_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Tk_K": {
            "type": "number",
            "unit": "K"
          },
          "vk_m_per_s": {
            "type": "number",
            "unit": "m/s"
          },
          "wk_m_per_s": {
            "type": "number",
            "unit": "m/s"
          },
          "delta_k_mm": {
            "type": "number",
            "unit": "mm"
          }
        }
      },
      "description": "Required final characteristic values for the baseline parameter set; compared to hidden reference within tolerances."
    },
    {
      "file": "delta0_1mm_final_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "t1_us",
          "p0_GPa",
          "tm_us",
          "tp_us",
          "pk_GPa",
          "Tk_K",
          "vk_m_per_s",
          "wk_m_per_s",
          "delta_k_mm"
        ],
        "properties": {
          "t1_us": {
            "type": "number",
            "unit": "µs"
          },
          "p0_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "tm_us": {
            "type": "number",
            "unit": "µs"
          },
          "tp_us": {
            "type": "number",
            "unit": "µs"
          },
          "pk_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "Tk_K": {
            "type": "number",
            "unit": "K"
          },
          "vk_m_per_s": {
            "type": "number",
            "unit": "m/s"
          },
          "wk_m_per_s": {
            "type": "number",
            "unit": "m/s"
          },
          "delta_k_mm": {
            "type": "number",
            "unit": "mm"
          }
        }
      },
      "description": "Optional file for the δ0=1 mm variation. If present, the checker verifies structural trends: tp should be larger and Tk should be lower than the baseline."
    }
  ],
  "notes": "The baseline simulation uses μ=0 (no viscous term). The agent decides numerical integration settings (tolerances, step sizes). The optional δ0=1 mm file is not required but provides bonus validation."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that reads the contents of `/app/outputs/final_values.json` (and, if present, `/app/outputs/delta0_1mm_final_values.json`). The verifier compares each quantitative result against a hidden reference solution derived from the published results of the original study. The baseline simulation (final_values.json) is the primary scored artifact. Each value is checked against a tolerance; the main mechanical and thermal parameters (final pressure, final temperature, final thickness, and final impactor velocity) carry the largest weight, while the time intervals and onset values carry smaller but still meaningful weights. If the optional δ0 = 1 mm file is provided, the verifier additionally checks structural trends: it will verify that the thermal softening time `tp` is longer than in the baseline and that the final temperature `Tk` is lower than in the baseline, without requiring exact numerical matches for the trend check. The final score is a weighted sum of the individual checks, reported as a number between 0 and 1.
