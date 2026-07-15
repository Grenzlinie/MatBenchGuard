# Stable configurations and binding energies of basal-plane quasidipoles in anisotropic zinc

## Problem background
Quasidipoles in hexagonal zinc are pairs of infinite, straight, parallel dislocations lying in different basal planes, with Burgers vectors that are fixed in magnitude but form an angle φ (restricted by hexagonal symmetry to 0°, 60°, 120°, and 180°). The total elastic energy per unit length of such a system can be expressed analytically using anisotropic elasticity theory. From this energy, one can determine stable configurations – characterized by an equilibrium width ratio ρ = x/y, where x is the horizontal separation between dislocations and y is the inter-plane distance – and the binding energy that keeps the pair together. The present task is to compute these quantities for quasidipoles with φ = 120° and 180° as a function of the orientation angle α of the Burgers vectors relative to the dislocation line and the inter-plane spacing y, both in the anisotropic continuum model of zinc and in an isotropic approximation.

## Approach
Implement the total energy U(α, φ, x, y) of a quasidipole using the analytic formula given in the next section (derived from anisotropic elasticity for hexagonal Zn). The formula depends on the five independent elastic constants of zinc (given below). For each combination of φ (120°, 180°), α (a set of angles spanning the possible orientations), and several fixed y (2, 5, 10, 50, 100 in units of 0.928b, where b is the Burgers vector magnitude and 0.928b is the basal plane spacing), evaluate U on a dense grid of x (or of ρ = x/y) to locate minima. The curvature at each extremum determines whether the configuration is stable or unstable, and the dominant character (edge 'E' or screw 'S') is identified by comparing the contributions from edge and screw components. For the anisotropic case, compute the binding energy Ub as the difference between the sum of the self-energies U0 and the minimum energy Ud at the stable equilibrium; for φ = 120° and 180° the self-energy sum equals the maximum of U, so Ub = U0 − Ud. The same evaluation is repeated for the isotropic polycrystalline zinc constants to obtain equilibrium positions for comparison.

## Total energy formula and input constants

The total elastic energy per unit length \(U\) (in eV/b) of the quasidipole as a function of orientation angle \(\alpha\), dipole angle \(\varphi\), and Cartesian coordinates \((x,y)\) (in units of the basal plane spacing \(0.928b\)) is

\[
\begin{aligned}
U &= \frac{b^2}{4\pi} \big[ K_e (\cos^2\alpha + \cos^2(\alpha+\varphi)) + K_s (\sin^2\alpha + \sin^2(\alpha+\varphi)) \big] \ln\frac{R}{r_0} \\
&\quad + \frac{b^2}{2\pi} \Bigg\{ \frac{1}{2} \cos\alpha \cos(\alpha+\varphi) \Bigg[ K_e \ln \left[ \frac{(R'^2 - \lambda^2 h^2)^2 + \lambda^2 d^2 R'^2 h^2}{(x^2 - \lambda^2 y^2)^2 + \lambda^2 d^2 x^2 y^2} \right]^{1/2} \\
&\qquad + K_1 \left( \arctan\frac{K_3 h^2}{R'^2 - K_2 h^2} - \arctan\frac{K_3 y^2}{x^2 - K_2 y^2} \right) \\
&\quad + \sin\alpha \sin(\alpha+\varphi) \; K_s \; \ln \left[ \frac{R'^2 + \eta^2 h^2}{x^2 + \eta^2 y^2} \right]^{1/2} \Bigg] \Bigg\},
\end{aligned}
\]

where the dimensionless auxiliary quantities are defined in terms of the anisotropic elastic constants \(c_{11},c_{12},c_{13},c_{33},c_{44}\) (units: \(10^{11}\) dyn/cm\(^2\)):

\[
\begin{aligned}
\bar{c}_{13} &= \sqrt{c_{11} c_{33}}, & \lambda^4 &= \frac{c_{11}}{c_{33}}, & \eta^2 &= \frac{c_{11} - c_{12}}{2c_{44}}, \\
C &= \frac{(\bar{c}_{13}+c_{13})(\bar{c}_{13}-c_{13}-2c_{44})}{\bar{c}_{13} c_{44}}, & d^2 &= C + 4, \\
K_e &= (\bar{c}_{13}+c_{13}) \left[ \frac{c_{44}(\bar{c}_{13}-c_{13})}{c_{33}(\bar{c}_{13}+c_{13}+2c_{44})} \right]^{1/2}, \\
K_s &= \left[ \tfrac12 (c_{11} - c_{12}) c_{44} \right]^{1/2}, \\
K_1 &= \frac{\lambda (\bar{c}_{13}^2 - c_{13}^2)}{2\bar{c}_{13} \left[ 1 - \frac{(\bar{c}_{13}+c_{13}+2c_{44})(\bar{c}_{13}-c_{13})}{4\bar{c}_{13} c_{44}} \right]^{1/2}}, \\
K_2 &= \frac{c_{13}(c_{13}+2c_{44}) - \bar{c}_{13}^2}{2c_{33}c_{44}}, \quad K_3 = \sqrt{\lambda^4 - K_2^2}.
\end{aligned}
\]

The outer boundary is a cylinder of radius \(R = 10^6 b\); the reference point for the self-energy sum is taken as \((R', h) = (R, 0)\), i.e. \(R' = 10^6 b,\; h = 0\). The dislocation core radius is \(r_0 = b/2\). The Burgers vector magnitude is \(b = 2.6649 \;\text{Å}\) (basal plane spacing \(0.928\,b = 2.4728 \;\text{Å}\)). Coordinates \(x, y\) are expressed in units of \(0.928\,b\).

**Isotropic polycrystalline Zn** is obtained by setting
\[
K_e = \frac{G}{1-\nu}, \quad K_s = G, \quad \lambda^2 = \eta^2 = 1, \quad d^2 = 4,
\]
and replacing the arctan term in the interaction part by
\[
\frac{G}{1-\nu} \cdot \frac{2 y^2}{x^2 + y^2}
\]
(see the text following Eq. (2) in Lejček 1968). The total energy then reads

\[
\begin{aligned}
U_{\text{iso}} &= \frac{b^2}{4\pi} \Big[ \frac{G}{1-\nu} (\cos^2\alpha+\cos^2(\alpha+\varphi)) + G (\sin^2\alpha+\sin^2(\alpha+\varphi)) \Big] \ln\frac{R}{r_0} \\
&\quad + \frac{b^2}{2\pi} \cos\alpha \cos(\alpha+\varphi) \Big[ \frac{G}{1-\nu} \ln\frac{R'}{\sqrt{x^2+y^2}} \\
&\qquad + \frac{G}{1-\nu} \frac{2 y^2}{x^2+y^2} \Big] + \frac{b^2}{2\pi} \sin\alpha \sin(\alpha+\varphi) G \ln\frac{R'}{\sqrt{x^2+y^2}} .
\end{aligned}
\]

However, the agent may simply evaluate the full anisotropic formula with the above substitutions to obtain isotropic results.

**Elastic constants** (in \(10^{11}\) dyn/cm\(^2\)):

- Anisotropic Zn (Huntington 1958): \(c_{11}=16.1,\; c_{12}=3.42,\; c_{13}=5.0,\; c_{33}=6.1,\; c_{44}=3.83\).
- Isotropic polycrystalline Zn (Hearmon 1961): \(G = 3.96,\; \nu = 0.33\).

To obtain \(U\) in eV/b, convert using 1 dyn·cm = \(10^{-7}\) J and 1 eV = \(1.6022\times10^{-19}\) J. The equilibrium width ratio \(\rho = x/y\) is taken from the \(x\) that minimizes \(U\) for a given \(\alpha,\varphi,y\).

## Reproduction target
Produce two CSV files under /app/outputs:

- equilibrium_positions.csv: For both isotropic (case='iso') and anisotropic (case='aniso') zinc, for φ=120° at α = 30°,45°,60°,75°,90°,105°,120° and for φ=180° at α = 0°,15°,30°,45°,60°,75°,90°, each at y = 2,5,10,50,100 (in 0.928b units), report the equilibrium width ratio ρ (dimensionless), stability ('St' or 'Unst'), and character ('E' or 'S'). The file must include every combination listed.

- binding_energies.csv: Only for the anisotropic case (case='aniso'), for the same φ and y values, report the binding energy Ub (in eV per unit of b) for the α values that appear in the binding energy part of the original study: φ=120° at α = 30°,60°,90°,120° and φ=180° at α = 0°,30°,60°,90°.

The exact column schemas and units are defined in the Output Contract.



## Workflow steps

### Step 1: Implement and evaluate total elastic energy
- Role: process
- Action: Implement the total elastic energy per unit length for a basal-plane quasidipole using the analytic expression derived from anisotropic elasticity for hexagonal Zn. For all required combinations of φ (120°, 180°), α, and y (2,5,10,50,100 in 0.928b units) evaluate the energy on a fine grid of x to locate extrema later. Save the energy evaluations to evidence.
- Evidence: `/app/outputs/energy_evaluations.npy`

### Step 2: Determine equilibrium positions and stability
- Role: scored (load-bearing)
- Action: From the energy evaluations, find for each parameter set the equilibrium width ratio ρ = x/y that minimizes total energy U. Classify each equilibrium as stable or unstable based on curvature and determine the dominant character (edge 'E' or screw 'S'). Produce the result for both isotropic and anisotropic Zn, covering φ=120° (α=30,45,60,75,90,105,120) and φ=180° (α=0,15,30,45,60,75,90) for each y listed.
- Output file: `/app/outputs/equilibrium_positions.csv`
- Format: csv
- Contract: case,phi,alpha,y,rho,stability,character
- Scoring: scored by hidden verifier

### Step 3: Compute binding energies
- Role: scored
- Action: For the anisotropic case, for each φ and α as above and for each y, compute the binding energy Ub = U0 - Ud, where U0 is the self-energy sum and Ud is the minimum energy at the stable equilibrium. Write results to binding_energies.csv.
- Output file: `/app/outputs/binding_energies.csv`
- Format: csv
- Contract: case,phi,alpha,y,Ub
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_positions.csv`
- `/app/outputs/binding_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_positions.csv
- path: `/app/outputs/equilibrium_positions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium width ratio, stability and character for quasidipoles in isotropic and anisotropic Zn.
- schema:
  - `type`: table
  - `required_columns`: `case`, `phi`, `alpha`, `y`, `rho`, `stability`, `character`
  - `units`:
    - `y`: in 0.928b units
    - `rho`: dimensionless
    - `phi`: degrees
    - `alpha`: degrees

### binding_energies.csv
- path: `/app/outputs/binding_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Binding energies for quasidipoles in anisotropic Zn.
- schema:
  - `type`: table
  - `required_columns`: `case`, `phi`, `alpha`, `y`, `Ub`
  - `units`:
    - `Ub`: eV/b
    - `y`: in 0.928b units
    - `phi`: degrees
    - `alpha`: degrees

Notes: Both outputs are checked against hidden reference values (derived from the same analytic expression with the given elastic constants) using absolute tolerances for numeric fields and exact string match for categorical fields. No gold values are disclosed in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_positions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "phi",
          "alpha",
          "y",
          "rho",
          "stability",
          "character"
        ],
        "units": {
          "y": "in 0.928b units",
          "rho": "dimensionless",
          "phi": "degrees",
          "alpha": "degrees"
        }
      },
      "description": "Equilibrium width ratio, stability and character for quasidipoles in isotropic and anisotropic Zn."
    },
    {
      "file": "binding_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "phi",
          "alpha",
          "y",
          "Ub"
        ],
        "units": {
          "Ub": "eV/b",
          "y": "in 0.928b units",
          "phi": "degrees",
          "alpha": "degrees"
        }
      },
      "description": "Binding energies for quasidipoles in anisotropic Zn."
    }
  ],
  "notes": "Both outputs are checked against hidden reference values (derived from the same analytic expression with the given elastic constants) using absolute tolerances for numeric fields and exact string match for categorical fields. No gold values are disclosed in the public contract."
}
```

## How you are scored
A hidden verifier reads your two CSV artifacts. For each row it compares your computed ρ and Ub against pre-computed reference values (derived from the same analytic energy expression with the same elastic constants) using an appropriate tolerance; the stability and character columns are checked by exact string match. The final reward is a weighted combination of per-entry scores across the two files. Simply emitting known numbers from the literature without executing the energy evaluation and minimization described in the workflow steps will not satisfy the scoring – the verifier expects the artifacts to be the output of the specified pipeline.
