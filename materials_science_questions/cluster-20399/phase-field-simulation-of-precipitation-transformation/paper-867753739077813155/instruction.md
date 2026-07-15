# Lamellar eutectoid growth velocity with solid-state diffusion

## Problem background
Lamellar eutectoid growth describes the cooperative growth of two solid phases from a parent phase, as occurs in the pearlite transformation in steel. Classical theories model solute redistribution assuming diffusion occurs only in the parent austenite; however, in solid‑state transformations the diffusion coefficients in the growing phases can be comparable to that in the parent, potentially modifying the growth kinetics. This work extends the Jackson‑Hunt analysis to account for diffusion in all three phases, and uses phase‑field simulations to test the resulting growth‑velocity predictions. The central task is to compute the lamellar growth velocity as a function of lamellar spacing and to compare the predictions of the generalized theory (with solid‑state diffusion) with the classical prediction (no solid‑state diffusion) and with direct phase‑field simulations.

## Approach

The analytical velocity is obtained from a self‑consistent solution of the steady‑state diffusion equation, the Stefan condition at the interfaces, and the Gibbs‑Thomson curvature undercooling. The generalized Jackson‑Hunt relation that accounts for diffusion in the growing phases (the “ρ‑factor” theory) is:

\[
v = \frac{\Delta T - \frac{2 T_E}{\lambda\,(m_A^{\beta\gamma} + m_B^{\alpha\gamma})}\left[\frac{m_B^{\alpha\gamma}\tilde{\sigma}_{\beta\gamma}\sin\theta_{\beta\alpha}}{\eta_\beta L_\beta} + \frac{m_A^{\beta\gamma}\tilde{\sigma}_{\alpha\gamma}\sin\theta_{\alpha\beta}}{\eta_\alpha L_\alpha}\right]}
{-\frac{\lambda}{D^\gamma \rho}\left(\frac{m_A^{\beta\gamma} m_B^{\alpha\gamma}}{m_A^{\beta\gamma}+m_B^{\alpha\gamma}}\right)\left[\frac{\mathcal{P}(\eta_\alpha)\,\Delta c_B}{\eta_\alpha} + \frac{\mathcal{P}(\eta_\beta)\,\Delta c_A}{\eta_\beta}\right]}
.
\]

Here ΔT is the undercooling (10 K), T_E the eutectoid temperature (989 K), λ the lamellar spacing, and σ̃ are the surface energies (all interfaces share the same value 0.49 J m⁻²). The latent heats L_α, L_β are derived from the grand‑potential fits (see below). The triple‑point angles θ are 30° (both angles equal), η_α = 0.88 and η_β = 0.12 are the volume fractions of ferrite and cementite. The concentration differences are

\[
\Delta c_A = c_A^\alpha - c_A^\beta, \qquad
\Delta c_B = c_B^\alpha - c_B^\beta .
\]

The correction factor that distinguishes the generalized theory from the classical one is

\[
\rho = \frac{D^\alpha}{D^\gamma}\frac{m_B^{\alpha\gamma}}{m_B^\alpha}\eta_\alpha
     + \frac{D^\beta}{D^\gamma}\frac{m_A^{\beta\gamma}}{m_A^\beta}\eta_\beta + 1 ,
\]

and the classical velocity v_classical is obtained by evaluating the same velocity expression with ρ = 1 (i.e. diffusion in the growing phases is neglected). The dimensionless function 𝒫(η) is

\[
\mathcal{P}(\eta) = \sum_{n=1}^\infty \frac{1}{(\pi n)^3} \sin^2(\pi n \eta),
\]

which can be approximated by truncating the series when the terms become negligible (e.g. keep 1000 terms).

**Material parameters (Table 1 of the source work).** The following numeric values are used throughout the workflow:

| Symbol | Value | Units |
|--------|-------|-------|
| T_E | 989 | K |
| ΔT | 10 | K |
| σ (all interfaces) | 0.49 | J m⁻² |
| D^α = D^β | 2 × 10⁻⁹ | m² s⁻¹ |
| D^γ | 1 × 10⁻⁹ | m² s⁻¹ |
| A^{\alpha,\gamma} = A^{\beta,\gamma} | –1.015385 × 10⁻¹¹ | m³ J⁻¹ |
| A^{\alpha,\beta} | –1.184616 × 10⁻¹² | m³ J⁻¹ |
| A^{\beta,\alpha} | –1.9 × 10⁻¹⁴ | m³ J⁻¹ |
| c_A^\alpha | 8.85 × 10⁻⁴ | – |
| c_A^\beta | 0.25 | – |
| c_A^\gamma | 0.034433 | – |
| c_B^\alpha | 0.999115 | – |
| c_B^\beta | 0.75 | – |
| c_B^\gamma | 0.965567 | – |
| η_α | 0.88 | – |
| η_β | 0.12 | – |
| θ_{αβ} = θ_{βα} | 30° | degrees |
| τ_{αγ} (computed) | 1.724027 × 10⁸ | J s m⁻⁴ |
| τ_{βγ} (computed) | 7.118288 × 10⁹ | J s m⁻⁴ |

**Deriving interface slopes and latent heats from grand‑potential coefficients.**  
The grand‑potential density of each phase is fitted as a quadratic function Ψ^ν(T, μ) = A^ν μ² + B^ν μ + C^ν (the coefficients A^ν, B^ν, C^ν are determined in step 1). The curvature coefficient for the ferrite (α) and cementite (β) phases in equilibrium with austenite is directly the tabulated A^{\alpha,\gamma} or A^{\beta,\gamma}. Therefore the slopes of the pure‑phase grand‑potential are

\[
m^\alpha = -\frac{1}{2 A^{\alpha,\gamma}}, \qquad
m^\beta = -\frac{1}{2 A^{\beta,\gamma}}.
\]

The slope of the γ‑ν coexistence line (ν = α, β) is obtained from the Clausius‑Clapeyron relation:

\[
m^{\nu,\gamma} = \frac{-1}{2 A^{\nu,\gamma}} \,
\frac{c^{\nu} - c^{\gamma}}{\left(\partial\Psi^{\nu}/\partial T - \partial\Psi^{\gamma}/\partial T\right)} .
\]

The temperature derivative ∂Ψ/∂T is evaluated by finite difference from the two grand‑potential fits at T_E = 989 K and T = 979 K. The latent heats are then

\[
L_\nu = T_E\left(\frac{\partial\Psi^{\nu}}{\partial T} - \frac{\partial\Psi^{\gamma}}{\partial T}\right) .
\]

All quantities needed for the velocity formula can therefore be computed from the fitted A coefficients and the tabulated compositions.

**Phase‑field model equations (used for v_phasefield).**  
The numerical simulation employs a multi‑phase grand‑potential formulation.

- Grand‑potential interpolation:  
  \( \Psi(T,\mu,\phi) = \sum_\alpha \Psi_\alpha(T,\mu)\,h_\alpha(\phi) \),  
  with \( h_\alpha(\phi) = \phi_\alpha^2 (3-2\phi_\alpha) + 2\phi_\alpha \sum_{\beta<\gamma,\,(\beta,\gamma)\neq\alpha} \phi_\beta \phi_\gamma \), \(\sum_\alpha \phi_\alpha = 1\).
- Double‑obstacle potential:  
  \( \tilde{w}(\phi) = \frac{16}{\pi^2} \sum_{\alpha<\beta} \tilde{\sigma}_{\alpha\beta} \phi_\alpha \phi_\beta \).
- Gradient energy:  
  \( \tilde{a}(\phi,\nabla\phi) = \sum_{\alpha<\beta} \tilde{\sigma}_{\alpha\beta} |q_{\alpha\beta}|^2 \),  
  \( q_{\alpha\beta} = \phi_\alpha \nabla\phi_\beta - \phi_\beta \nabla\phi_\alpha \).
- Phase‑field evolution:  
  \( \tau\epsilon\,\frac{\partial\phi_\alpha}{\partial t} = \epsilon\left(\nabla\cdot\frac{\partial \tilde{a}}{\partial\nabla\phi_\alpha} - \frac{\partial \tilde{a}}{\partial\phi_\alpha}\right) - \frac{1}{\epsilon}\frac{\partial \tilde{w}}{\partial\phi_\alpha} - \frac{\partial\Psi}{\partial\phi_\alpha} - \Lambda \),  
  with Λ enforcing \(\sum_\alpha \phi_\alpha = 1\).
- Concentration evolution:  
  \( \frac{\partial c_i}{\partial t} = \nabla\cdot\left(\sum_j M_{ij}(\phi)\nabla\mu_j \right) \),  
  where \( M_{ij}(\phi) = \sum_\alpha M_{ij}^\alpha\,h_\alpha(\phi) \) and  
  \( M_{ij}^\alpha = D_{ik}^\alpha\,\frac{\partial c_k^\alpha}{\partial\mu_j} \).
- Thin‑interface relaxation constants (to eliminate interface kinetics):  
  \( \tau_{\nu\gamma} = \frac{(c^\nu - c^\gamma)^2}{D^\gamma\,(\partial c^\gamma/\partial\mu)}\,(M+F) \),  
  with \( M+F = 0.222 \) and \( \partial c^\gamma/\partial\mu = -1/(2 A^\gamma) \). The computed values are listed above; they should be verified during step 2.

The simulation domain uses a periodic transverse direction to fix the lamellar spacing and no‑flux boundaries in the growth direction. The box is shifted in the growth direction (moving‑frame) when the front fills 10 % of the box. Steady‑state velocity is extracted from the linear portion of the triple‑junction position versus time. Simulations are performed for at least 10 spacings evenly distributed between 10 μm and 100 μm.

After completing the simulations, the agent computes for each spacing the analytical velocity v_analytical from the generalized expression (the ρ‑factor formula) and the classical velocity v_classical by setting ρ = 1 in the same formula, and then assembles the three velocities into a single table.

## Reproduction target
For a binary eutectoid system representing ferrite and cementite growing from austenite at a constant undercooling of 10 K relative to the eutectoid temperature, compute the lamellar growth velocity for at least ten lamellar spacings evenly distributed between 10 μm and 100 μm. For each spacing, provide:

- `v_analytical`: velocity computed from the generalized Jackson‑Hunt relation that accounts for diffusion in the growing phases.
- `v_classical`: velocity computed from the classical relation that assumes diffusion only in the parent austenite.
- `v_phasefield`: steady‑state growth velocity extracted from a phase‑field simulation that includes diffusion in all phases.

The outcome must be written as a CSV file with columns `lamellar_spacing` (μm), `v_analytical` (m/s), `v_classical` (m/s), `v_phasefield` (m/s).

## Assets

- CALPHAD free energy data for Fe-C system: Public thermodynamic database, e.g., OpenCalphad or equivalent Fe-C description (Gustafson 1985).
- Phase-field simulation framework: Open-source framework such as OpenPhase or FiPy.

## Workflow steps

### Step 1: Grand-potential parameterization
- Role: process
- Action: Obtain CALPHAD free energy data for austenite, ferrite, and cementite of the Fe-C system near the eutectoid temperature. Fit grand-potential densities as quadratic functions of the chemical potential (Equation 36) using the procedure from the paper (Eqs. 37-39). Determine the coefficients A, B, C for each phase at the eutectoid temperature (989 K) and at an undercooled temperature (979 K, ΔT = 10 K).
- Evidence: `/app/outputs/grand_potential_coefficients.json`

### Step 2: Thin-interface relaxation constants
- Role: process
- Action: Compute the interface relaxation coefficients τ_αγ and τ_βγ using the thin-interface analysis formula (Eq. 43), the equilibrium concentrations from Table 1, the diffusivity D^γ, the surface energies, and the solvability integral M+F = 0.222. The calculation ensures that interface kinetics are eliminated in the quantitative phase-field model.
- Evidence: `/app/outputs/relaxation_constants.json`

### Step 3: Phase-field simulation of lamellar growth
- Role: process
- Action: Set up and run a quantitative multi-phase-field model for the binary eutectoid system (ferrite/cementite growing from austenite) using the grand-potential formulation (double-obstacle potential, thin-interface relaxation constants). Use periodic boundary conditions in the transverse direction to fix the lamellar spacing, and no-flux in the growth direction. Initialize with the eutectoid chemical potential and run the simulation in a moving-frame mode until steady-state front propagation is attained. Perform independent runs for at least 10 different lamellar spacings λ evenly distributed between 10 and 100 μm. For each run, record the time evolution of the triple-point position (or the contour φ_α − φ_β = 0) to enable velocity extraction.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 4: Compute and report lamellar growth velocities
- Role: scored (load-bearing)
- Action: For each simulated lamellar spacing, determine the steady-state growth velocity v_phasefield from the linear portion of the interface-front position versus time curve. Compute the analytical velocity v_analytical using the generalized Jackson‑Hunt relation that includes diffusion in all phases (the formula containing the multiplicative factor ρ). Compute the classical velocity v_classical by evaluating the same relation with ρ = 1 (i.e., no diffusion in the growing phases). Use the same set of material and geometric parameters (Table 1, and the fitted thermodynamic coefficients from step_fit_thermo). Assemble the results into a CSV file.
- Output file: `/app/outputs/velocities.csv`
- Format: csv
- Contract: Columns: lamellar_spacing (float, μm), v_analytical (float, m/s), v_classical (float, m/s), v_phasefield (float, m/s). At least 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/velocities.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### velocities.csv
- path: `/app/outputs/velocities.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV with lamellar spacing (μm) and the three computed velocities (m/s). The checker will verify structural relationships: v_analytical > v_classical for all rows, v_phasefield within 20% of v_analytical, spacings in [10, 100] μm, and velocities decreasing with spacing.
- schema:
  - `type`: table
  - `required_columns`: `lamellar_spacing`, `v_analytical`, `v_classical`, `v_phasefield`
  - `units`:
    - `lamellar_spacing`: μm
    - `v_analytical`: m/s
    - `v_classical`: m/s
    - `v_phasefield`: m/s

Notes: The checker validates that v_analytical > v_classical for all spacings and that v_phasefield is consistent with the analytical trend (within a tolerance band). No gold values or tolerances are exposed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "velocities.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "lamellar_spacing",
          "v_analytical",
          "v_classical",
          "v_phasefield"
        ],
        "units": {
          "lamellar_spacing": "μm",
          "v_analytical": "m/s",
          "v_classical": "m/s",
          "v_phasefield": "m/s"
        }
      },
      "description": "CSV with lamellar spacing (μm) and the three computed velocities (m/s). The checker will verify structural relationships: v_analytical > v_classical for all rows, v_phasefield within 20% of v_analytical, spacings in [10, 100] μm, and velocities decreasing with spacing."
    }
  ],
  "notes": "The checker validates that v_analytical > v_classical for all spacings and that v_phasefield is consistent with the analytical trend (within a tolerance band). No gold values or tolerances are exposed here."
}
```

## How you are scored
A hidden verifier evaluates each required artifact. For the CSV file, the verifier internally recomputes the analytical and classical velocities from the same theory and parameters used in the workflow and compares them against the agent‑reported `v_analytical` and `v_classical`. The phase‑field velocities are compared to hidden reference values obtained from the paper's own phase‑field simulations, with a tolerance that reflects the expected numerical spread across different implementations. In addition, the verifier checks that the three velocities for each spacing exhibit the relationships expected from the analytical model that includes solid‑state diffusion—that is, that the influence of diffusion in the growing phases is correctly captured by the reported numbers. The score from the velocity table is combined with structural checks on intermediate evidence files to form a final reward between 0 and 1.
