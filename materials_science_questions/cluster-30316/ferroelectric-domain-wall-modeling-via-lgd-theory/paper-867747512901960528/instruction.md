# Phononic torque and force on a magnetic domain wall via elastic wave scattering

## Problem background
In a one-dimensional magnetic wire, a static domain wall breaks both rotational and translational symmetry. This means that transverse elastic waves (phonons) can exchange angular and linear momentum with the domain wall, resulting in a torque and a force that can drive domain-wall motion. The underlying physical mechanism is a local modification of the effective tension for the two transverse displacement components $u$ and $v$ caused by the magnetic anisotropy, which makes the domain wall birefringent for elastic waves. Circularly-polarized waves therefore change their polarization upon transmission and reflection, transferring spin angular momentum to the wall; linearly-polarized waves are partially reflected, transferring linear momentum. The objective of this task is to quantitatively compute the phononic torque and force on the domain wall, and from them the resulting steady-state domain-wall velocities in ferromagnetic and antiferromagnetic systems.

## Approach
The approach is a numerical wave-scattering calculation followed by momentum-current subtraction.\n\n1. **Static domain-wall profile.** The magnetic texture is a head-to-head domain wall described by a hyperbolic-tangent profile $n_z(\zeta) = -\tanh(\zeta/\lambda)$ and an in-plane component $n_\perp(\zeta) = \operatorname{sech}(\zeta/\lambda)$ with a constant azimuthal angle $\Phi$. The wall width $\lambda$ and the dimensionless anisotropy parameter $\kappa = K/\mathcal{T}$ (where $K$ is the anisotropy constant and $\mathcal{T}$ the applied tension) are the essential material parameters.\n\n2. **Wave equations.** Transverse displacements $u(\zeta,t)$ and $v(\zeta,t)$ obey the linearised equations\n   $$-k^2 u = \bigl[\{1-2\tilde\kappa\operatorname{sech}^2(\zeta/\lambda)\} u'\bigr]', \qquad -k^2 v = \bigl[\{1-\tilde\kappa\operatorname{sech}^2(\zeta/\lambda)\} v'\bigr]',$$\n   with $\tilde\kappa=\kappa/(1+\kappa)$ and $k$ the dimensionless wavenumber (in units of $1/\lambda$). These are solved for a range of $k\lambda\in[0.1,10]$ for an incoming monochromatic right‑travelling wave of unit amplitude incident from the left.\n\n3. **Scattering parameters.** From the numerical solutions we extract the real transmission and reflection amplitudes $t_u,t_v,r_u,r_v$ and the corresponding phase shifts $\phi_{u,t},\phi_{v,t},\phi_{u,r},\phi_{v,r}$. The quantities of interest are the relative phase shifts $\Delta\phi_t = \phi_{u,t}-\phi_{v,t}$ and $\Delta\phi_r = \phi_{u,r}-\phi_{v,r}$.\n\n4. **Dimensionless torque and force.** The time‑averaged torque and force (per unit incident energy flux) are obtained from the scattering parameters via\n   $$\tilde\tau = 1 - t_u t_v \cos\Delta\phi_t - r_u r_v \cos\Delta\phi_r, \qquad \tilde F = r_u^2 + r_v^2.$$\n   These are compared with simple analytic approximations:\n   - high-energy WKB torque: $\tilde\tau_{\text{approx}} = 1 - \cos[k\lambda\ln(1-\kappa)]$,\n   - low-energy force: $\tilde F_{\text{approx}} = \kappa^2 (k\lambda)^2$.\n\n5. **Physical domain-wall velocities.** The steady-state velocity for a ferromagnetic wall (zero damping) driven by the torque is\n   $$V_{\text{FM}} = \frac{\tau_{\text{phys}}}{2s}, \qquad s = \frac{M_s}{\gamma} A,$$\n   where $M_s$ is the saturation magnetisation, $\gamma$ the gyromagnetic ratio, and $A$ the wire cross‑sectional area. For an antiferromagnetic wall (damping $\alpha=0.01$) driven by the force,\n   $$V_{\text{AFM}} = \frac{\lambda F_{\text{phys}}}{2\alpha s}.$$\n   The physical torque and force are obtained from the dimensionless quantities by multiplying with the appropriate powers of $\mathcal{T}_\kappa$, $a$, and $k$ (given in the reproduction target).

## Reproduction target
Reproduce the entire computational pipeline for the parameter set $\kappa=0.2$, domain‑wall width $\lambda=1\times10^{-9}$ m, and wave amplitude $a=\lambda/10$. Specifically:\n\n- Compute the scattering amplitudes and phase shifts for the two transverse polarisations $u$ and $v$ for dimensionless wavenumbers $k\lambda$ from $0.1$ to $10$ (step 1).\n- From these, calculate the dimensionless torque $\tilde\tau$ (circularly‑polarised input) and the dimensionless force $\tilde F$ (linearly‑polarised input), together with the analytic approximations $\tilde\tau_{\text{approx}}$ and $\tilde F_{\text{approx}}$ (step 2).\n- Using the material parameters $\mathcal{T}_\kappa = 10^{-3}$ N, $M_s = 2\times10^6$ A/m, $\gamma = 1.76\times10^{11}$ rad/(s T), and $A = 2\times10^{-17}$ m², convert the torque at $k\lambda=5.0$ and the force at $k\lambda=0.5$ into physical steady‑state domain‑wall velocities for the ferromagnetic ($\alpha=0$) and antiferromagnetic ($\alpha=0.01$) cases, respectively (step 3).

## Assets

- Python scientific stack (NumPy, SciPy, Matplotlib): numpy scipy matplotlib

## Workflow steps

### Step 1: Solve elastic wave scattering and extract scattering parameters
- Role: scored
- Action: Solve the reduced 1D wave equations for the transverse displacements u(ζ) and v(ζ) with the static domain-wall profile for a range of dimensionless wavenumbers kλ ∈ [0.1, 10]. Use an incoming monochromatic right‑travelling wave of unit amplitude from the left. Numerically extract the real transmission amplitudes t_u, t_v, reflection amplitudes r_u, r_v, and the relative phase shifts Δϕ_t = phase(t_u) − phase(t_v) and Δϕ_r = phase(r_u) − phase(r_v). Output the results as a structured JSON file.
- Output file: `/app/outputs/scattering_parameters.json`
- Format: json
- Contract: JSON object with keys 'k_lambda' (list of floats, ascending), 'u_trans_amplitude' (list), 'u_trans_phase' (list, radians), 'u_refl_amplitude' (list), 'u_refl_phase' (list, radians), 'v_trans_amplitude' (list), 'v_trans_phase' (list, radians), 'v_refl_amplitude' (list), 'v_refl_phase' (list, radians). All lists same length, aligned element‑wise with k_lambda.
- Scoring: scored by hidden verifier

### Step 2: Compute phononic torque and force from scattering parameters
- Role: scored
- Action: Using the scattering parameters from the previous step, compute the dimensionless time‑averaged torque τ̃ (for a circularly‑polarized incoming wave) and dimensionless force F̃ (for a linearly‑polarized incoming wave) via the standard current‑subtraction formulas: τ̃ = 1 − t_u t_v cos Δϕ_t − r_u r_v cos Δϕ_r and F̃ = r_u² + r_v², for the same kλ values. Also provide approximate dimensionless τ̃_approx and F̃_approx using the WKB and low‑energy analytic expressions. Write all data to a CSV file.
- Output file: `/app/outputs/torque_force_values.csv`
- Format: csv
- Contract: CSV with columns: k_lambda (float), tau_dimless (float), F_dimless (float), tau_approx_dimless (float), F_approx_dimless (float). All numeric; k_lambda in ascending order.
- Scoring: scored by hidden verifier

### Step 3: Compute steady-state domain-wall velocities
- Role: scored (load-bearing)
- Action: From the CSV of the previous step, extract the dimensionless torque at kλ = 5.0 and the dimensionless force at kλ = 0.5. Convert to physical torque and force using the material parameters: effective tension T_κ = 1e-3 N, wave amplitude a = λ/10 = 1e-10 m, λ = 1e-9 m, cross‑sectional area A = 2e-17 m², saturation magnetization M_s = 2×10⁶ A/m, gyromagnetic ratio γ = 1.76×10¹¹ rad/(s·T). Compute the ferromagnetic steady‑state velocity (zero damping) and the antiferromagnetic velocity (damping α = 0.01) using the formulas V_FM = τ_phys / (2 s) and V_AFM = λ F_phys / (2 α s), where s = (M_s / γ) × A. Output a JSON with the velocities in m/s.
- Output file: `/app/outputs/domain_wall_velocities.json`
- Format: json
- Contract: JSON object with keys: 'k_lambda_torque' (float, 5.0), 'ferromagnetic_velocity_ms' (float), 'k_lambda_force' (float, 0.5), 'antiferromagnetic_velocity_ms' (float). All values in SI (m/s).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scattering_parameters.json`
- `/app/outputs/torque_force_values.csv`
- `/app/outputs/domain_wall_velocities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scattering_parameters.json
- path: `/app/outputs/scattering_parameters.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Numerical scattering amplitudes and phase shifts for u and v polarizations, used for structural audits (unitarity, WKB phase consistency).
- schema:
  - `type`: object
  - `required`:
    - `k_lambda`: list of floats
    - `u_trans_amplitude`: list of floats
    - `u_trans_phase`: list of floats (radians)
    - `u_refl_amplitude`: list of floats
    - `u_refl_phase`: list of floats (radians)
    - `v_trans_amplitude`: list of floats
    - `v_trans_phase`: list of floats (radians)
    - `v_refl_amplitude`: list of floats
    - `v_refl_phase`: list of floats (radians)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `u_trans_phase`: radian
    - `v_trans_phase`: radian
    - `u_refl_phase`: radian
    - `v_refl_phase`: radian

### torque_force_values.csv
- path: `/app/outputs/torque_force_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Tabulated dimensionless torque and force, compared against analytic approximations (windowed tolerance).
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `k_lambda`, `tau_dimless`, `F_dimless`, `tau_approx_dimless`, `F_approx_dimless`
  - `units`:
    - `k_lambda`: dimensionless
    - `tau_dimless`: dimensionless
    - `F_dimless`: dimensionless
    - `tau_approx_dimless`: dimensionless
    - `F_approx_dimless`: dimensionless

### domain_wall_velocities.json
- path: `/app/outputs/domain_wall_velocities.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Steady-state domain-wall velocities recomputed from the agent's own torque/force data and checked against hidden reference values derived from the paper's formulas.
- schema:
  - `type`: object
  - `required`:
    - `k_lambda_torque`: float
    - `ferromagnetic_velocity_ms`: float
    - `k_lambda_force`: float
    - `antiferromagnetic_velocity_ms`: float
  - `items`: object
  - `required_columns`:
  - `units`:
    - `ferromagnetic_velocity_ms`: m/s
    - `antiferromagnetic_velocity_ms`: m/s

Notes: The checker will verify scattering parameters structurally (no gold values). Torque and force are compared to the paper's analytic approximations. Velocities are recomputed from the agent's submitted torque/force values and then compared to hidden reference velocities derived from the paper's own formulas to ensure end-to-end consistency of the physics pipeline.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scattering_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "k_lambda": "list of floats",
          "u_trans_amplitude": "list of floats",
          "u_trans_phase": "list of floats (radians)",
          "u_refl_amplitude": "list of floats",
          "u_refl_phase": "list of floats (radians)",
          "v_trans_amplitude": "list of floats",
          "v_trans_phase": "list of floats (radians)",
          "v_refl_amplitude": "list of floats",
          "v_refl_phase": "list of floats (radians)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "u_trans_phase": "radian",
          "v_trans_phase": "radian",
          "u_refl_phase": "radian",
          "v_refl_phase": "radian"
        }
      },
      "description": "Numerical scattering amplitudes and phase shifts for u and v polarizations, used for structural audits (unitarity, WKB phase consistency)."
    },
    {
      "file": "torque_force_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "k_lambda",
          "tau_dimless",
          "F_dimless",
          "tau_approx_dimless",
          "F_approx_dimless"
        ],
        "units": {
          "k_lambda": "dimensionless",
          "tau_dimless": "dimensionless",
          "F_dimless": "dimensionless",
          "tau_approx_dimless": "dimensionless",
          "F_approx_dimless": "dimensionless"
        }
      },
      "description": "Tabulated dimensionless torque and force, compared against analytic approximations (windowed tolerance)."
    },
    {
      "file": "domain_wall_velocities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "k_lambda_torque": "float",
          "ferromagnetic_velocity_ms": "float",
          "k_lambda_force": "float",
          "antiferromagnetic_velocity_ms": "float"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "ferromagnetic_velocity_ms": "m/s",
          "antiferromagnetic_velocity_ms": "m/s"
        }
      },
      "description": "Steady-state domain-wall velocities recomputed from the agent's own torque/force data and checked against hidden reference values derived from the paper's formulas."
    }
  ],
  "notes": "The checker will verify scattering parameters structurally (no gold values). Torque and force are compared to the paper's analytic approximations. Velocities are recomputed from the agent's submitted torque/force values and then compared to hidden reference velocities derived from the paper's own formulas to ensure end-to-end consistency of the physics pipeline."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each of the three scored artifacts.\n\n- **Scattering parameters** are checked for structural consistency (e.g. unitarity, expected WKB phase-shift trends).\n- **Torque and force curves** are compared against the provided analytic approximations with appropriate tolerances; they must exhibit the correct oscillation period and low‑wavenumber power‑law.\n- **Domain‑wall velocities** are recomputed by the verifier from your own submitted torque/force values and then compared with hidden reference values derived from the paper’s formulas, ensuring the entire physics pipeline is correctly executed.\n\nEach artifact receives a partial score, and the final reward is a weighted sum. Reporting a number without producing the required raw artifacts does not earn credit.
