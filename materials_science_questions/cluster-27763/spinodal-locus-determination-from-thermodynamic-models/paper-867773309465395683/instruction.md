# Spinodal Density Calculation for Biaxial Hard Board Monolayers

## Problem background
Colloidal board-like particles (hard bodies with three edge lengths) confined to a flat monolayer can form liquid-crystal phases: uniaxial nematic (Nu), biaxial nematic (Nb), and non-uniform phases (smectic, columnar, crystal). Using a fundamental-measure density-functional theory (DFT) for particles with six discrete orientations, the original work investigated how the particle shape—parametrised by the largest aspect ratio κ1 and a biaxiality parameter θ—affects the stability of these phases. The key quantities are spinodal densities at which the uniform Nu phase becomes linearly unstable: the Nu→Nb bifurcation point, and the instability toward density-modulated (non-uniform) phases. This task computes those spinodal densities for a grid of (κ1, θ) values that covers the main behavioural regimes, thereby revealing how particle biaxiality influences the phase diagram.

## Approach
Implement the fundamental-measure DFT for the six-orientation Zwanzig model of hard board-like particles confined to a plane. For each (κ1, θ) pair, self-consistently solve the equilibrium equations to obtain the uniform-phase molar fractions and packing fraction. Then perform two bifurcation analyses:

1. **Nu → Nb spinodal:** solve the coupled uniaxial equilibrium equations together with the determinant condition that signals biaxial symmetry breaking, yielding the density at which the biaxial nematic phase first becomes linearly unstable relative to the uniform uniaxial nematic.
2. **Spinodal to non-uniform phases:** compute the 6×6 structure-factor matrix of the uniform phase, minimise the absolute value of its determinant over the wavevector, and locate the lowest density where the determinant first vanishes — this gives the spinodal density for instabilities to smectic, columnar, or crystal phases.

All computations rely only on open-source numerical libraries (NumPy, SciPy). No external datasets are required.

## Essential equations
The excess free-energy density (scaled) for the uniform six-component mixture is

\[
\Phi_{\mathrm{exc}}^{*} = \rho^{*} \bigl[-\ln(1-\eta) + y\,\Psi_{1x}\Psi_{1y}\bigr],
\qquad
y = \frac{\rho^{*}}{1-\eta},\quad \eta = \rho^{*}\Psi_{2}.
\]

The weighted densities are

\[
\begin{aligned}
\Psi_{1x} &= (\gamma_{xy}+\gamma_{xz})\kappa_{1} + (\gamma_{yx}+\gamma_{zx})\kappa_{2} + \gamma_{zy}+\gamma_{yz},\\
\Psi_{1y} &= (\gamma_{yx}+\gamma_{yz})\kappa_{1} + (\gamma_{xy}+\gamma_{zy})\kappa_{2} + \gamma_{zx}+\gamma_{xz},\\
\Psi_{2}   &= (\gamma_{xy}+\gamma_{yx})\kappa_{1}\kappa_{2} + (\gamma_{xz}+\gamma_{yz})\kappa_{1} + (\gamma_{zx}+\gamma_{zy})\kappa_{2}.
\end{aligned}
\]

Minimising the total free energy w.r.t. the molar fractions \(\gamma_{\mu\nu}\) gives the self‑consistent equilibrium equations

\[
\gamma_{\mu\nu} = \frac{e^{-\chi_{\mu\nu}}}{\sum_{\alpha\beta} e^{-\chi_{\alpha\beta}}},
\qquad
\chi_{\mu\nu} = y\bigl[\,\Psi_{1x}\kappa_{\mu\nu}^{y} + \Psi_{1y}\kappa_{\mu\nu}^{x} + (1 + y\Psi_{1x}\Psi_{1y})\,\kappa_{\mu\nu}^{x}\kappa_{\mu\nu}^{y}\,\bigr],
\]

where \(\kappa_{\mu\nu}^{\tau} = 1 + (\kappa_{1}-1)\delta_{\tau\mu} + (\kappa_{2}-1)\delta_{\nu\tau}\).

### Nu→Nb bifurcation condition
In the uniaxial phase \(u_{-}=v_{-}=r_{-}=0\) and the equilibrium equations reduce to the pair (B12) of the paper. Adopting the notation \(u_{+}=\gamma_{zx}\), \(v_{+}=\gamma_{xz}\), the uniaxial equilibrium equations are

\[
\begin{aligned}
f_{1}(u_{+},v_{+},\rho^{*}) &= u_{+} - C^{-1} e^{-\xi_{1}(u_{+},v_{+},\rho^{*})} = 0,\\
f_{2}(u_{+},v_{+},\rho^{*}) &= v_{+} - C^{-1} e^{-\xi_{2}(u_{+},v_{+},\rho^{*})} = 0,
\end{aligned}
\]

with \(C = 2\bigl(e^{-\xi_{1}} + e^{-\xi_{2}} + e^{-\xi_{3}}\bigr)\), and

\[
\begin{aligned}
s_{+} &= \tfrac{1}{2}(\kappa_{1}+\kappa_{2}) - (\kappa_{1}-1)u_{+} - (\kappa_{2}-1)v_{+},\\
\xi_{1} &= y\bigl[\kappa_{2}(1+y s_{+}^{2}) + (\kappa_{2}+1)s_{+}\bigr],\\
\xi_{2} &= y\bigl[\kappa_{1}(1+y s_{+}^{2}) + (\kappa_{1}+1)s_{+}\bigr],\\
\xi_{3} &= y\bigl[\kappa_{1}\kappa_{2}(1+y s_{+}^{2}) + (\kappa_{1}+\kappa_{2})s_{+}\bigr].
\end{aligned}
\]

The biaxial instability is signalled by the vanishing of the determinant of the matrix \(A\) (B10), which simplifies to

\[
y^{-1} = u_{+}(\kappa_{2}-1)^{2} + v_{+}(\kappa_{1}-1)^{2} + r_{+}(\kappa_{1}-\kappa_{2})^{2}
\]

with \(r_{+} = 1/2 - u_{+} - v_{+}\).  Solving this condition together with \(f_{1}=f_{2}=0\) yields the Nu→Nb spinodal density \(\rho^{*}\).

### Spinodal to non‑uniform phases
The 6×6 structure‑factor matrix has elements

\[
\begin{aligned}
T_{\mu\nu,\tau\iota} = &\;\delta_{\mu\nu,\tau\iota}
+ y \sqrt{\gamma_{\mu\nu}\gamma_{\tau\iota}}
\Bigl\{
\langle \hat{w}_{\mu\nu}^{(0)}\hat{w}_{\tau\iota}^{(2)} \rangle
+ \langle \hat{w}_{\mu\nu}^{(1x)}\hat{w}_{\tau\iota}^{(1y)} \rangle \\
&+ y\bigl[ \Psi_{1y}\langle \hat{w}_{\mu\nu}^{(1x)}\hat{w}_{\tau\iota}^{(2)} \rangle
+ \Psi_{1x}\langle \hat{w}_{\mu\nu}^{(1y)}\hat{w}_{\tau\iota}^{(2)} \rangle \bigr] \\
&+ (1+2y\Psi_{1x}\Psi_{1y})\,
\hat{w}_{\mu\nu}^{(2)}\hat{w}_{\tau\iota}^{(2)}
\Bigr\},
\end{aligned}
\]

where \(\langle \hat{w}_{\mu\nu}^{(\alpha)}\hat{w}_{\tau\iota}^{(\beta)} \rangle
= \hat{w}_{\mu\nu}^{(\alpha)}\hat{w}_{\tau\iota}^{(\beta)} + \hat{w}_{\mu\nu}^{(\beta)}\hat{w}_{\tau\iota}^{(\alpha)}\) and the Fourier‑transformed weight functions are

\[
\begin{aligned}
\hat{w}_{\mu\nu}^{(0)}(\boldsymbol{q}^{*}) &= \prod_{\tau=x,y}\chi_{0}(q_{\tau}^{*}\kappa_{\mu\nu}^{\tau}/2),\\
\hat{w}_{\mu\nu}^{(2)}(\boldsymbol{q}^{*}) &= \prod_{\tau=x,y}\kappa_{\mu\nu}^{\tau}\,\chi_{1}(q_{\tau}^{*}\kappa_{\mu\nu}^{\tau}/2),\\
\hat{w}_{\mu\nu}^{(1x)}(\boldsymbol{q}^{*}) &= \kappa_{\mu\nu}^{x}\,\chi_{1}(q_{x}^{*}\kappa_{\mu\nu}^{x}/2)\,\chi_{0}(q_{y}^{*}\kappa_{\mu\nu}^{y}/2),\\
\hat{w}_{\mu\nu}^{(1y)}(\boldsymbol{q}^{*}) &= \kappa_{\mu\nu}^{y}\,\chi_{0}(q_{x}^{*}\kappa_{\mu\nu}^{x}/2)\,\chi_{1}(q_{y}^{*}\kappa_{\mu\nu}^{y}/2),
\end{aligned}
\]

with \(\chi_{0}(x)=\cos x\), \(\chi_{1}(x)=\sin x/x\) for \(x\neq0\) and \(\chi_{1}(0)=1\).  
The wavevector is restricted to in‑plane directions \(\boldsymbol{q}^{*}=(q_{x}^{*},0)\) or \((0,q_{y}^{*})\).  The spinodal density is the smallest \(\rho^{*}\) for which
\[
\det T(\boldsymbol{q}^{*},\rho^{*}) = 0
\]
at any wavevector \(\boldsymbol{q}^{*}\).

## Reproduction target
Compute the Nu→Nb spinodal density and the spinodal density to non-uniform phases for every combination of κ1 ∈ [5, 10, 20, 55, 70] and θ from -1 to 1 in steps of 0.2 (11 values), giving 55 grid points in total. For each grid point record the reduced spinodal density ρ* (scaled by σ₃²) and the transition type. Write all results to a CSV file with columns: kappa1, theta, rho_star, transition_type (where transition_type is either 'NuNb' or 'nonuniform'). The file must be saved as `/app/outputs/phase_diagram_data.csv`.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement DFT and solve uniform-phase properties
- Role: process
- Action: Implement the fundamental-measure DFT for the six-orientation Zwanzig model of hard board-like particles. For each (κ1, θ) pair in the grid (κ1 ∈ [5,10,20,55,70], θ from -1 to 1 in steps of 0.2), solve the self-consistent equations for equilibrium molar fractions, and compute the uniform-phase packing fraction, pressure, and chemical potentials.
- Evidence: none

### Step 2: Compute spinodal densities and compile results
- Role: scored (load-bearing)
- Action: For each (κ1, θ) grid point, (i) locate the N_u→N_b spinodal by solving the coupled uniaxial equilibrium equations and the determinant condition simultaneously; (ii) compute the spinodal density to non-uniform phases by minimizing the determinant of the 6×6 structure-factor matrix over wavevectors and finding the lowest density where it vanishes; (iii) record each transition point (κ1, θ, rho_star, transition_type). Write all results to phase_diagram_data.csv.
- Output file: `/app/outputs/phase_diagram_data.csv`
- Format: csv
- Contract: kappa1 (float), theta (float), rho_star (float), transition_type (string: 'NuNb' or 'nonuniform')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_data.csv
- path: `/app/outputs/phase_diagram_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed spinodal densities for the requested grid of (κ1, θ).
- schema:
  - `type`: table
  - `required_columns`: `kappa1`, `theta`, `rho_star`, `transition_type`
  - `description`: kappa1: float, theta: float, rho_star: float, transition_type: string ('NuNb' or 'nonuniform')

Notes: The hidden checker re-implements the same DFT and bifurcation analysis and compares the agent's reported rho_star values against its own recomputed values with a relative tolerance; qualitative trends are also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kappa1",
          "theta",
          "rho_star",
          "transition_type"
        ],
        "description": "kappa1: float, theta: float, rho_star: float, transition_type: string ('NuNb' or 'nonuniform')"
      },
      "description": "Computed spinodal densities for the requested grid of (κ1, θ)."
    }
  ],
  "notes": "The hidden checker re-implements the same DFT and bifurcation analysis and compares the agent's reported rho_star values against its own recomputed values with a relative tolerance; qualitative trends are also verified."
}
```

## How you are scored
A hidden verifier independently re-implements the same DFT and bifurcation analysis. It recomputes the spinodal densities for each (κ1, θ) point and compares the rho_star values you report against its own recomputed values using a relative tolerance and a small absolute floor. In addition, the verifier checks that the set of spinodal points you obtain satisfies qualitative structural trends expected from the physics (e.g., for certain aspect ratios the NuNb spinodal exists only for extreme negative θ; for others reentrant NuNb spinodals appear; and above a threshold aspect ratio the NuNb spinodal exists for all θ). The reward for the scored step is based solely on the contents of `phase_diagram_data.csv`. Reporting a number that happens to match the paper’s value without correctly running the DFT and bifurcation analysis is not sufficient—the artifact must be computed and written according to the workflow. The final score is a single number between 0 and 1 that combines the numerical accuracy reward and the structural trend reward.
