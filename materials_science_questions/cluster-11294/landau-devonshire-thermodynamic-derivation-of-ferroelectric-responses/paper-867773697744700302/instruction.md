# Nematic Liquid Crystal Splay-Bend Dynamics and Response Time Simulation

## Problem background
A nematic liquid crystal (NLC) cell sandwiched between two plates can exist in two distinct orientational states—splay and bend—separated by an energy barrier. When a voltage is applied across the cell, the director field reorients, driving a splay-to-bend transition that changes the optical transmittance through crossed polarisers. The switching speed is characterised by the response time, defined as the time for the transmittance to rise from 10% to 90% of its final value. This task investigates how the response time depends on material properties: the flexoelectric coefficient (which couples elastic distortions to the electric field) and the dielectric anisotropy (which governs the torque exerted by the field). The goal is to simulate the director dynamics and compute the response time for a range of these parameters, providing quantitative insight into the factors that control the switching behaviour.

## Approach
The director is described by a tilt angle θ(z,t) that varies with depth z and time t. The dynamics are governed by a time-dependent Ginzburg-Landau model: a free energy functional that includes Frank elasticity (splay and bend constants), flexoelectric coupling, and the interaction with an inhomogeneous electric field derived from the applied voltage and the dielectric tensor. Surface anchoring energies and a surface rotational viscosity are included as boundary conditions. The flexoelectric polarisation contributes an additional coupling term and shifts the effective voltage. The electric displacement across the cell is determined self-consistently from the voltage drop and the depth-dependent dielectric function. Optical transmittance through crossed polarisers is computed using the Jones matrix method, which involves integrating the phase difference accumulated by ordinary and extraordinary rays along the cell thickness. The workflow consists of: (i) solving the static equilibrium director profile at zero voltage to obtain the initial splay state; (ii) for each parameter set, integrating the dynamic equations with a finite-difference time-domain method to obtain θ(z,t); (iii) computing the transmittance T(t) from the instantaneous director profile; (iv) extracting the response time as the duration between 10% and 90% of the final transmittance. Two parameter sweeps are performed: one over the flexoelectric coefficient e_f, and one over the dielectric anisotropy parameter u (with e_f = 0).

## Reproduction target
Produce two sweep tables and two companion transmittance curves. First, for the flexoelectric coefficient e_f, sweep at least 10 values covering the range from -2.5e-11 C/m to 0 C/m, and for each e_f compute the response time (10–90% rise of transmittance) with an applied voltage of 20 V and the material parameters (K11=6.6e-12 N, K33/K11=3.0, cell thickness d=2.5e-6 m, symmetric anchoring strength W=4.0e-4 J/m², pretilt angles θ_L=46° and θ_U=44°, bulk rotational viscosity γ_b=0.1 N·s/m², surface rotational viscosity γ_s=3.0e-6 N·s/m, ordinary and extraordinary refractive indices n_o=1.5, n_e=1.6, wavelength λ=550 nm). Write the results to response_time_ef.csv with columns 'ef (C/m)' and 'response_time (ms)'. Additionally, for the reference flexoelectric coefficient e_f = -2.3e-11 C/m, export the full transmittance curve T(t) as a JSON file transmittance_curve_ef.json containing arrays 'time' (seconds) and 'transmittance' (values between 0 and 1). Second, for the dielectric anisotropy parameter u (where ε_par = ε_perp(1+u)), sweep at least 8 values from u=0.2 to u=1.5 with e_f set to zero, and write response_time_u.csv with columns 'u' and 'response_time (ms)'. For the reference dielectric anisotropy u = 1.0, export transmittance_curve_u.json. All outputs must be placed under /app/outputs.

## Assets

- Model parameters: K11=6.6e-12 N, K33=1.98e-11 N, d=2.5e-6 m, W=4.0e-4 J/m², θ_L=46°, θ_U=44°, γ_b=0.1 N·s/m², γ_s=3.0e-6 N·s/m, ε_perp=6.3, ε_par=12.6, e_f=-2.3e-11 C/m (reference), n_o=1.5, n_e=1.6, λ=550 nm, U=20 V
- numpy: numpy
- scipy: scipy

## Model equations

**Director**: θ(z,t) is the tilt angle from the plane.

**Free energy** per unit area: G = ∫_0^d f_b dz + f_s,

f_b = K(θ) (∂θ/∂z)^2 + D_z^2 / ε_zz(θ)

where
K(θ) = K11 cos^2θ + K33 sin^2θ + (e_f^2 sin^2θ cos^2θ) / ε_zz(θ)
ε_zz(θ) = ε_perp (1 + u sin^2θ),  u = (ε_∥ − ε_perp)/ε_perp.

The electric displacement D_z (constant across the cell) is

D_z = (U + ψ(θ1) − ψ(θ0)) / ∫_0^d dz/ε_zz(θ),
with ψ(θ) = (e_f/(2u ε_perp)) ln(1 + u sin^2θ).

Surface anchoring energy: f_anch = (W/2)[sin^2(θ0 − θ_L) + sin^2(θ1 + θ_U)].
Surface free energy: f_s = f_anch + D_z [ψ(θ0) − ψ(θ1)].

**Dynamic equations**:

γ_b ∂θ/∂t = K(θ) ∂^2θ/∂z^2 + ½ [ K'(θ)(∂θ/∂z)^2 + (D_z/ε_zz(θ))^2 ε_zz'(θ) ]   (bulk)

γ_s ∂θ_i/∂t = (−1)^i K(θ_i) ∂θ_i/∂z − ∂f_s/∂θ_i,   i=0,1   (surface, i=0 at z=0, i=1 at z=d)

**Optical transmittance** (crossed polarisers, director at 45° to input polariser):

T = sin^2(Δφ/2),
Δφ = (2π/λ) ∫_0^d (n_eff − n_o) dz,
1/n_eff^2 = sin^2θ / n_o^2 + cos^2θ / n_e^2.

**Default parameter values** (unless swept):
K11 = 6.6×10^{-12} N,   K33 = 3.0 × K11,
d = 2.5×10^{-6} m,   W = 4.0×10^{-4} J/m^2,
θ_L = 46°,   θ_U = 44°,
γ_b = 0.1 N·s/m^2,   γ_s = 3.0×10^{-6} N·s/m,
ε_perp = 6.3,   ε_∥ = 12.6  (so default u = 1.0),
e_f = e11 + e33; when sweeping e_f only the sum matters,
n_o = 1.5,   n_e = 1.6,   λ = 550 nm,   U = 20 V.

## Workflow steps

### Step 1: Compute initial splay-state director profile
- Role: process
- Action: Solve the static equilibrium director field θ(z) at zero applied voltage (U=0, hence D_z=0) by minimising the free energy functional G (with D_z=0, G = ∫_0^d [K(θ)(∂θ/∂z)^2] dz + f_anch) using the material parameters listed in Model equations and the anchoring boundary conditions (surface torque balance ∂f_anch/∂θ_i = K(θ_i) ∂θ_i/∂z at i=0,1). This profile serves as the initial condition for all dynamic runs.
- Evidence: `/app/outputs/equilibrium_theta.npy`

### Step 2: Simulate dynamics and transmittance for flexoelectric sweep
- Role: process
- Action: For each flexoelectric coefficient e_f in the range [-2.5e-11, 0] C/m (at least 10 points), integrate the dynamic equations (bulk and surface, see Model equations) with applied voltage U=20 V, starting from the initial splay profile. Use a finite-difference time-domain method. At each time step, compute the transmittance T(t) using the Jones calculus formulas given in Model equations (T = sin^2(Δφ/2), Δφ integral, effective refractive index). Save the resulting T(t) arrays and the corresponding e_f values.
- Evidence: `/app/outputs/sim_results_ef.npz`

### Step 3: Extract response time vs flexoelectric coefficient
- Role: scored
- Action: Load the sim_results_ef.npz produced by step2. For each e_f, determine the response time (time for transmittance to rise from 10% to 90% of its final value). Write the results to response_time_ef.csv with columns 'ef (C/m)' and 'response_time (ms)'.
- Output file: `/app/outputs/response_time_ef.csv`
- Format: csv
- Contract: columns: 'ef (C/m)' (float), 'response_time (ms)' (float); at least 10 rows covering the range [-2.5e-11, 0] C/m, including e_f = -2.3e-11 C/m.
- Scoring: scored by hidden verifier

### Step 4: Export reference transmittance curve for flexoelectric coefficient
- Role: scored (load-bearing)
- Action: From the simulation results (sim_results_ef.npz), extract the full transmittance vs. time curve for the reference flexoelectric coefficient e_f = -2.3e-11 C/m. Write the data as a JSON file containing arrays 'time' (in seconds) and 'transmittance' (values between 0 and 1).
- Output file: `/app/outputs/transmittance_curve_ef.json`
- Format: json
- Contract: {"time": [list of floats (seconds)], "transmittance": [list of floats (0-1)]}
- Scoring: scored by hidden verifier

### Step 5: Simulate dynamics and transmittance for dielectric anisotropy sweep
- Role: process
- Action: For each dielectric anisotropy parameter u in the range [0.2, 1.5] (at least 8 points), with flexoelectric coefficient e_f set to 0, integrate the dynamic equations (bulk and surface, see Model equations) with voltage U=20 V, starting from the initial splay profile. Compute the transmittance T(t) using the formulas in Model equations. Save the T(t) arrays and the corresponding u values.
- Evidence: `/app/outputs/sim_results_u.npz`

### Step 6: Extract response time vs dielectric anisotropy
- Role: scored
- Action: Load the sim_results_u.npz produced by step5. For each u, compute the response time (10%–90% rise of transmittance). Write the results to response_time_u.csv with columns 'u' and 'response_time (ms)'.
- Output file: `/app/outputs/response_time_u.csv`
- Format: csv
- Contract: columns: 'u' (float), 'response_time (ms)' (float); at least 8 rows covering the range [0.2, 1.5], including u = 1.0.
- Scoring: scored by hidden verifier

### Step 7: Export reference transmittance curve for dielectric anisotropy
- Role: scored (load-bearing)
- Action: From the simulation results (sim_results_u.npz), extract the full transmittance vs. time curve for the reference dielectric anisotropy u = 1.0. Write the data as a JSON file containing arrays 'time' (in seconds) and 'transmittance' (values between 0 and 1).
- Output file: `/app/outputs/transmittance_curve_u.json`
- Format: json
- Contract: {"time": [list of floats (seconds)], "transmittance": [list of floats (0-1)]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/response_time_ef.csv`
- `/app/outputs/transmittance_curve_ef.json`
- `/app/outputs/response_time_u.csv`
- `/app/outputs/transmittance_curve_u.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### response_time_ef.csv
- path: `/app/outputs/response_time_ef.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sweep of flexoelectric coefficient vs response time. The verifier compares each point against paper-derived gold values with a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `ef (C/m)`, `response_time (ms)`
  - `units`:
    - `ef (C/m)`: C/m
    - `response_time (ms)`: ms

### transmittance_curve_ef.json
- path: `/app/outputs/transmittance_curve_ef.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Reference transmittance curve at e_f=-2.3e-11 C/m. The verifier recomputes the 10%–90% response time from this curve and compares with the value in response_time_ef.csv to ensure simulation integrity.
- schema:
  - `type`: object
  - `required`: `time`, `transmittance`
  - `properties`:
    - `time`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Time points in seconds
    - `transmittance`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Transmittance values between 0 and 1

### response_time_u.csv
- path: `/app/outputs/response_time_u.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sweep of dielectric anisotropy parameter vs response time. The verifier compares each point against paper-derived gold values with a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `u`, `response_time (ms)`
  - `units`:
    - `u`: dimensionless
    - `response_time (ms)`: ms

### transmittance_curve_u.json
- path: `/app/outputs/transmittance_curve_u.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Reference transmittance curve at u=1.0. The verifier recomputes the 10%–90% response time from this curve and compares with the value in response_time_u.csv to ensure simulation integrity.
- schema:
  - `type`: object
  - `required`: `time`, `transmittance`
  - `properties`:
    - `time`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Time points in seconds
    - `transmittance`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: Transmittance values between 0 and 1

Notes: The scored CSV files provide the parameter sweeps that correspond to the paper's main claims. The companion JSON transmittance curves serve as a load‑bearing recompute check: the verifier recomputes the response time from each reference curve and cross‑checks it against the CSV entry for the same reference parameter, ensuring the agent actually ran the dynamics simulation rather than fabricating the response time values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "response_time_ef.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ef (C/m)",
          "response_time (ms)"
        ],
        "units": {
          "ef (C/m)": "C/m",
          "response_time (ms)": "ms"
        }
      },
      "description": "Sweep of flexoelectric coefficient vs response time. The verifier compares each point against paper-derived gold values with a relative tolerance."
    },
    {
      "file": "transmittance_curve_ef.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "time",
          "transmittance"
        ],
        "properties": {
          "time": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Time points in seconds"
          },
          "transmittance": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Transmittance values between 0 and 1"
          }
        }
      },
      "description": "Reference transmittance curve at e_f=-2.3e-11 C/m. The verifier recomputes the 10%–90% response time from this curve and compares with the value in response_time_ef.csv to ensure simulation integrity."
    },
    {
      "file": "response_time_u.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "u",
          "response_time (ms)"
        ],
        "units": {
          "u": "dimensionless",
          "response_time (ms)": "ms"
        }
      },
      "description": "Sweep of dielectric anisotropy parameter vs response time. The verifier compares each point against paper-derived gold values with a relative tolerance."
    },
    {
      "file": "transmittance_curve_u.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "time",
          "transmittance"
        ],
        "properties": {
          "time": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Time points in seconds"
          },
          "transmittance": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "Transmittance values between 0 and 1"
          }
        }
      },
      "description": "Reference transmittance curve at u=1.0. The verifier recomputes the 10%–90% response time from this curve and compares with the value in response_time_u.csv to ensure simulation integrity."
    }
  ],
  "notes": "The scored CSV files provide the parameter sweeps that correspond to the paper's main claims. The companion JSON transmittance curves serve as a load‑bearing recompute check: the verifier recomputes the response time from each reference curve and cross‑checks it against the CSV entry for the same reference parameter, ensuring the agent actually ran the dynamics simulation rather than fabricating the response time values."
}
```

## How you are scored
A hidden verifier evaluates each output file independently and combines the results into a weighted final reward. For the CSV sweep files, the verifier compares the computed response time values at the sampled parameter points against reference expectations derived from the scientific literature, using tolerances that account for legitimate differences in numerical implementation and discretisation. For the load-bearing JSON transmittance curves, the verifier recomputes the 10–90% response time directly from the supplied time-transmittance arrays and cross-checks that value against the corresponding row in the associated CSV file; this confirms self-consistency and ensures the dynamics were genuinely simulated. The reward is weighted approximately 30% on the recompute consistency and 70% on the sweep accuracy, with larger weight assigned to the main sweep tables. Reporting a result without producing the intermediate simulation artifacts will not receive credit, because the verifier relies on the raw transmittance curves for the recompute check. The scoring is directional: a solution that captures the correct physical trends and meets or exceeds the expected precision earns full credit; credit decreases only when the results deviate significantly from the reference behaviour.
