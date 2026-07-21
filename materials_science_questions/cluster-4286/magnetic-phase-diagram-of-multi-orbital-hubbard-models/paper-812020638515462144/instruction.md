# Magnetic phase diagram of the anisotropic J1-J2 Heisenberg model

## Problem background
Frustrated quantum spin systems can host a rich variety of magnetic phases due to the competition between different exchange interactions. The spin-1/2 Heisenberg antiferromagnet on a square lattice with nearest-neighbor (J1>0) and next-nearest-neighbor (J2) exchange couplings, known as the J1-J2 model, is a canonical example. Introducing an exchange anisotropy Δ on the nearest-neighbor bonds (the anisotropic J1-J2 model) further enriches the phase diagram. Depending on the frustration parameter α=J2/J1 and the anisotropy Δ, the system can support Néel antiferromagnetic order, collinear order, or a magnetically disordered (spin-liquid) phase. The boundaries between these phases and their evolution with temperature are of fundamental interest for strongly correlated electron systems and for understanding real materials such as layered vanadates.

## Approach

### Effective-field theory on a two-spin cluster (EFT-2)

We consider a two-spin cluster (one spin on sublattice A, one on B) embedded in the square lattice. Each spin interacts with its three nearest neighbors outside the cluster and with the next-nearest neighbors. Using the differential-operator technique, the sublattice magnetization $m_A$ at temperature $T$ is given by

$$m_A = \langle \sigma_A^z \rangle = \hat{\Lambda}_{1x}\,\hat{\Lambda}_{2y}\,\hat{\Lambda}_2\,\hat{\Lambda}_3 \, g(x,y)\big|_{x=y=0}$$

where

$$g(x,y) = \frac{\sinh(x+y) + \frac{x-y}{W}\,e^{2K_1}\sinh W}{\cosh(x+y) + e^{2K_1}\cosh W}, \qquad W(x,y) = \sqrt{(x-y)^2 + 4K_1^2(1-\Delta)^2}.$$

Here $K_1 = J_1/(k_B T)$, $K_2 = J_2/(k_B T) = \alpha K_1$. The operators $\hat{\Lambda}$ are defined through

$$\alpha_{r\nu} = \cosh(K_r D_\nu), \quad \beta_{r\nu} = \sinh(K_r D_\nu)$$
$$\alpha_{xy} = \alpha_{1x}\alpha_{2y} + \beta_{1x}\beta_{2y}, \quad \beta_{xy} = \alpha_{1x}\beta_{2y} + \beta_{1x}\alpha_{2y}$$

with $D_x = \partial/\partial x$, $D_y = \partial/\partial y$. The cluster operators are

$$\hat{\Lambda}_{1x} = (\alpha_{1x} - m_{x,B}\,\beta_{1x})^3 (\alpha_{1y} - m_{x,A}\,\beta_{1y})^3,$$
$$\hat{\Lambda}_{2y} = (\alpha_{1x} - m_{y,B}\,\beta_{1x})^3 (\alpha_{1y} - m_{y,A}\,\beta_{1y})^3,$$
$$\hat{\Lambda}_2 = (\alpha_{2x} - m_{y,A}\,\beta_{2x})^2 (\alpha_{2y} - m_{y,B}\,\beta_{2y})^2,$$
$$\hat{\Lambda}_3 = (\alpha_{xy} - m_{y,A}\,\beta_{xy})^2 (\alpha_{yx} - m_{y,B}\,\beta_{yx})^2.$$

The magnetic components depend on the phase:
- **Néel phase**: $m_{x,A}=m_A,\; m_{x,B}=-m_A,\; m_{y,A}=m_A,\; m_{y,B}=-m_A$ (staggered magnetization).
- **Collinear phase**: $m_{x,A}=m_{x,B}=m_A,\; m_{y,A}=m_{y,B}=-m_A$.
- **Spin-liquid (disordered) phase**: $m_A=0$.

Expanding the products using the binomial theorem and applying the shift property $\exp(a D_x)\,g(x,y)=g(x+a,y)$ yields a polynomial of degree up to 24 in $m_A$ whose coefficients are sums of hyperbolic functions evaluated at various shifts. The self-consistency equation $m_A = F(m_A; T,\alpha,\Delta)$ is solved numerically (e.g., by fixed-point iteration or root-finding) to obtain $m_A(T)$.

### EFRG second-order boundary

The effective-field renormalization group combines results from one‑spin and two‑spin clusters. After a scaling transformation, the condition for a continuous (second‑order) transition is the vanishing of the renormalized magnetization. This leads to the equation

$$\frac{\partial}{\partial m_A}\big[ F_{\text{2‑spin}}(m_A) - F_{\text{1‑spin}}(m_A) \big] \big|_{m_A=0} = 0,$$

where $F_{\text{1‑spin}}$ is the self‑consistency function for a single‑spin cluster (derived analogously by keeping only the NN bonds) and $F_{\text{2‑spin}}$ is the EFT‑2 function above. For a chosen $\Delta$, we sweep $\alpha$ and find the $\alpha$ that satisfies this condition together with $m_A=0$ being a solution; this gives $\alpha_2(\Delta)$.

### First-order boundary

In the collinear phase, the magnetization jumps discontinuously at a first‑order transition. Within EFT‑2, the transition temperature $T_c^*$ is identified by the condition $d m_A/dT \to \infty$, which corresponds to the fixed‑point slope reaching unity: $\partial F/\partial m_A = 1$. For a fixed $(\alpha,\Delta)$ we locate $T_c^*$ satisfying this condition. The ground‑state first‑order boundary $\alpha_1(\Delta)$ is then obtained by extrapolating $T_c^*(\alpha,\Delta) \to 0$.

### Workflow

1. Define grids: $\Delta = \{0,\,0.5,\,1.0\}$; $\alpha = 0.00,\,0.05,\,0.10,\,\dots,\,1.00$; $T$ discretized over $[0,T_{\max}]$.
2. For each $(\Delta,\alpha)$, solve the EFT‑2 self‑consistency equation to build $m_A(T)$ curves.
3. Apply the EFRG condition to obtain $\alpha_2(\Delta)$.
4. For each $(\Delta,\alpha)$ with $\alpha > \alpha_2(\Delta)$ (collinear regime), locate $T_c^*$ via the slope condition and extrapolate $T_c^*\to0$ to get $\alpha_1(\Delta)$.
5. Assemble the ground‑state boundaries $(\alpha_1,\alpha_2)$ and finite‑$T$ critical lines $T_c(\alpha)$ for $\Delta = 0, 0.5, 1.0$.

## Reproduction target
Produce two principal output files:

1. `step_02_ground_phase_boundaries.json` — a JSON array of objects, each with keys `Delta` (float), `alpha_second_order` (float, the second-order Néel–spin-liquid transition point α2(Δ)), and `alpha_first_order` (float, the first-order spin-liquid–collinear transition point α1(Δ)). Report values for Δ = 0, 0.5, 1.0 (additional Δ values are allowed).

2. `step_03_finite_T_critical_lines.json` — a JSON object whose keys are the string representations of Δ (e.g., `"0.0"`, `"0.5"`, `"1.0"`). Each value is a list of objects `{alpha, Tc, type}`, where `alpha` is a float, `Tc` is a float (in units of J1/k_B), and `type` is either `"second"` or `"first"`. Together these lists trace the finite-temperature phase boundary lines for the antiferromagnetic (J1>0) case in the (T, α) plane, covering a range from α=0 up to α=1.0 with a step of 0.05 or finer.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define parameter grid
- Role: process
- Action: Define the ranges and discretization of anisotropy Δ, frustration α=J2/J1, and temperature T to be scanned for the phase diagram calculations.
- Evidence: none

### Step 2: EFT-2 magnetization calculation
- Role: process
- Action: Implement the effective-field theory two-spin cluster (EFT-2) using the differential-operator technique. For each (Δ,α) point, solve the self-consistency equation for sublattice magnetization mA as a function of temperature T. Store the computed magnetization curves for later analysis.
- Evidence: `/app/outputs/magnetization_curves.json`

### Step 3: EFRG second-order boundary calculation
- Role: process
- Action: Implement the effective-field renormalization group (EFRG) with one- and two-spin clusters. For each anisotropy Δ, find the critical frustration α2(Δ) where renormalized magnetizations vanish, marking the continuous Néel–spin liquid transition.
- Evidence: `/app/outputs/second_order_boundary.json`

### Step 4: First-order boundary analysis
- Role: process
- Action: Process the magnetization curves from step 02. For each (Δ,α) in the collinear phase, locate the temperature Tc* where dmA/dT diverges. Extrapolate Tc* → 0 to obtain the first-order spin liquid–collinear critical frustration α1(Δ).
- Evidence: `/app/outputs/first_order_boundary.json`

### Step 5: Ground-state phase diagram compilation
- Role: scored (load-bearing)
- Action: Combine the results from steps 03 and 04 to produce the final ground-state phase boundaries for Δ = 0, 0.5, 1.0. Output a JSON file listing α2(Δ) (second-order) and α1(Δ) (first-order) for each Δ.
- Output file: `/app/outputs/step_02_ground_phase_boundaries.json`
- Format: json
- Contract: A JSON array of objects with fields 'Delta' (float), 'alpha_second_order' (float), 'alpha_first_order' (float). Values for Δ=0, 0.5, 1.0 (additional values allowed).
- Scoring: scored by hidden verifier

### Step 6: Finite-temperature phase diagram
- Role: scored
- Action: From the magnetization curves (step 02) and the EFRG results, extract the critical temperatures Tc(α) for second-order (mA → 0) and first-order (dmA/dT divergence) transitions. For each Δ (0, 0.5, 1.0), produce a list of (α, Tc, transition type) covering the relevant α range. Output a JSON file.
- Output file: `/app/outputs/step_03_finite_T_critical_lines.json`
- Format: json
- Contract: A JSON object with keys representing Δ values (as strings, e.g., '0.0', '0.5', '1.0'), each mapping to a list of objects: {'alpha': float, 'Tc': float (in units of J1/kB), 'type': 'second' or 'first'}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_ground_phase_boundaries.json`
- `/app/outputs/step_03_finite_T_critical_lines.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_ground_phase_boundaries.json
- path: `/app/outputs/step_02_ground_phase_boundaries.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ground-state critical frustration parameters α1(Δ) and α2(Δ) for Δ = 0, 0.5, 1.0.
- schema:
  - `type`: array
  - `required`: `Delta`, `alpha_second_order`, `alpha_first_order`
  - `items`:
    - `Delta`: float
    - `alpha_second_order`: float
    - `alpha_first_order`: float

### step_03_finite_T_critical_lines.json
- path: `/app/outputs/step_03_finite_T_critical_lines.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Finite-temperature phase boundaries Tc(α) for Δ = 0, 0.5, 1.0, with transition type (first or second).
- schema:
  - `type`: object
  - `required`: `0.0`, `0.5`, `1.0`
  - `items`:
    - `alpha`: float
    - `Tc`: float
    - `type`: string

Notes: Only the antiferromagnetic case (J1>0) is considered. The checker will compare the submitted boundary values and transition temperatures to reference values from the paper using a tolerance-based match.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_ground_phase_boundaries.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "required": [
          "Delta",
          "alpha_second_order",
          "alpha_first_order"
        ],
        "items": {
          "Delta": "float",
          "alpha_second_order": "float",
          "alpha_first_order": "float"
        }
      },
      "description": "Ground-state critical frustration parameters α1(Δ) and α2(Δ) for Δ = 0, 0.5, 1.0."
    },
    {
      "file": "step_03_finite_T_critical_lines.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "0.0",
          "0.5",
          "1.0"
        ],
        "items": {
          "alpha": "float",
          "Tc": "float",
          "type": "string"
        }
      },
      "description": "Finite-temperature phase boundaries Tc(α) for Δ = 0, 0.5, 1.0, with transition type (first or second)."
    }
  ],
  "notes": "Only the antiferromagnetic case (J1>0) is considered. The checker will compare the submitted boundary values and transition temperatures to reference values from the paper using a tolerance-based match."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that checks both output files. For each scored artifact, the verifier compares the reported critical frustration parameters α1(Δ), α2(Δ) and the finite-temperature critical lines Tc(α) to reference values obtained from the original study. The comparison uses tolerances appropriate for a numerical re‑implementation, so small discrepancies due to different numerical choices are accepted. In addition, the verifier inspects the overall structure of the phase diagrams (e.g., the qualitative dependence of the boundaries on the anisotropy parameter) to ensure physical consistency. The intermediate computation steps (magnetization curves, EFRG results) are required parts of the workflow, but only the two final scored JSON files contribute to your final reward. A solution that merely reproduces the output format without executing the underlying physics will receive a low score.
