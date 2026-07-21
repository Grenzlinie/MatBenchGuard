# Piezoelectric quasicrystal moving crack stress computation

## Problem background
One-dimensional hexagonal piezoelectric quasicrystals are brittle advanced materials that exhibit both quasiperiodic symmetry and piezoelectric coupling. Understanding the stress and electric field concentrations around moving cracks is essential for assessing their reliability. An extended dislocation layer method can be used to derive closed-form expressions for the phonon stress, phason stress, and electric displacement fields around a non-uniformly loaded moving antiplane shear crack. This task focuses on computing the scaled phonon stress angular distribution near the crack tip for given material parameters and crack speeds, which is a key illustrative result for the mechanical response of such materials.

## Approach
The material is a one-dimensional hexagonal piezoelectric quasicrystal with point group 6mm, under antiplane shear deformation. A Griffith-type crack of width 2c moves along its own plane with uniform speed v, while a non-uniform phonon stress load is applied to its faces. The phason stress and electric displacement loads are set to zero in the computational case of interest, corresponding to an electrically impermeable crack.

The method models the crack as a continuous planar distribution of moving piezoelectric quasicrystal screw dislocations, leading to integral equations for the dislocation densities. Solving these yields the near-tip fields in closed form. The phonon stress component $\sigma_{\psi z}(r,\psi)$ near the crack tip ($r \ll c$) scales as $1/\sqrt{r}$ and depends on the material constants, the crack speed, and the polar angle $\psi$.

To compute the scaled stress $\sqrt{r}\,10^5\,\sigma_{\psi z}/K_{\mathcal{T}}$, use the given material constants ($c_{44}$, $R$, $K$, $e_{15}$, $e_{15}'$, $\varepsilon_{11}$, $\rho$) to evaluate:

1. Piezoelectrically stiffened moduli:
   $$\bar{c}_{44}=c_{44}+\frac{e_{15}^{2}}{\varepsilon_{11}},\qquad \bar{K}=K+\frac{e_{15}^{\prime\,2}}{\varepsilon_{11}},\qquad \bar{R}=R+\frac{e_{15}e_{15}^{\prime}}{\varepsilon_{11}}.$$

2. Parameters $\alpha$, $\varepsilon_{1}$, $\varepsilon_{2}$:
   $$\alpha = \frac{\bar{c}_{44}-\bar{K}+\sqrt{(\bar{c}_{44}-\bar{K})^{2}+4\bar{R}^{2}}}{2},$$
   $$\varepsilon_{1}= \frac{\bar{c}_{44}+\bar{K}+\sqrt{(\bar{c}_{44}-\bar{K})^{2}+4\bar{R}^{2}}}{2},\quad \varepsilon_{2}= \frac{\bar{c}_{44}+\bar{K}-\sqrt{(\bar{c}_{44}-\bar{K})^{2}+4\bar{R}^{2}}}{2}.$$

3. Wave speeds: $s_{1}=\sqrt{\varepsilon_{1}/\rho}$, $s_{2}=\sqrt{\varepsilon_{2}/\rho}$.

4. For each crack speed ratio $v/s_{2}=0$ and $0.99$:
   $$\beta_{1}=\sqrt{1-\frac{v^{2}}{s_{1}^{2}}},\qquad \beta_{2}=\sqrt{1-\frac{v^{2}}{s_{2}^{2}}}.$$

5. The dimensionless $\bar{\Lambda}$ coefficients ($\bar{\Lambda}_{1}$–$\bar{\Lambda}_{8}$) are functions of $\bar{c}_{44}$, $\bar{K}$, $\bar{R}$, $\alpha$, and the piezoelectric constants:
   $$\bar{\Lambda}_{1}= \frac{(\bar{c}_{44}\alpha+\bar{R}^{2})(\alpha\bar{K}-\bar{R}^{2})}{(\alpha^{2}+\bar{R}^{2})(\bar{c}_{44}\bar{K}-\bar{R}^{2})},\quad \bar{\Lambda}_{2}= \frac{\bar{R}^{2}(\bar{c}_{44}-\alpha)(\alpha+\bar{K})}{(\alpha^{2}+\bar{R}^{2})(\bar{c}_{44}\bar{K}-\bar{R}^{2})},$$\
   $$\bar{\Lambda}_{3}= \frac{\bar{R}(\bar{c}_{44}\alpha+\bar{R}^{2})(\bar{c}_{44}-\alpha)}{(\alpha^{2}+\bar{R}^{2})(\bar{c}_{44}\bar{K}-\bar{R}^{2})},\quad \bar{\Lambda}_{4}= \frac{\bar{R}(\alpha+\bar{K})(\alpha\bar{K}-\bar{R}^{2})}{(\alpha^{2}+\bar{R}^{2})(\bar{c}_{44}\bar{K}-\bar{R}^{2})},$$\
   $$\bar{\Lambda}_{5}= \frac{(\bar{c}_{44}\alpha+\bar{R}^{2})\bigl[e_{15}^{\prime}\bar{R}(\bar{c}_{44}-\alpha)+e_{15}(\alpha\bar{K}-\bar{R}^{2})\bigr]}{\varepsilon_{11}(\alpha^{2}+\bar{R}^{2})(\bar{c}_{44}\bar{K}-\bar{R}^{2})},\quad \bar{\Lambda}_{6}= -\frac{\bar{R}(\bar{c}_{44}-\alpha)\bigl[e_{15}^{\prime}(\bar{c}_{44}\alpha+\bar{R}^{2})-e_{15}\bar{R}(\alpha+\bar{K})\bigr]}{\varepsilon_{11}(\alpha^{2}+\bar{R}^{2})(\bar{c}_{44}\bar{K}-\bar{R}^{2})},$$\
   $$\bar{\Lambda}_{7}= \frac{\bar{R}(\alpha+\bar{K})\bigl[e_{15}^{\prime}\bar{R}(\bar{c}_{44}-\alpha)+e_{15}(\alpha\bar{K}-\bar{R}^{2})\bigr]}{\varepsilon_{11}(\alpha^{2}+\bar{R}^{2})(\bar{c}_{44}\bar{K}-\bar{R}^{2})},\quad \bar{\Lambda}_{8}= \frac{(\alpha\bar{K}-\bar{R}^{2})\bigl[e_{15}^{\prime}(\bar{c}_{44}\alpha+\bar{R}^{2})-e_{15}\bar{R}(\alpha+\bar{K})\bigr]}{\varepsilon_{11}(\alpha^{2}+\bar{R}^{2})(\bar{c}_{44}\bar{K}-\bar{R}^{2})}.$$

6. For each angle $\psi$ in $[0^{\circ},180^{\circ}]$ (step $1^{\circ}$), define:
   $$k=\beta_{1}\;\text{or}\;\beta_{2},\quad \Delta_{k}=(\cos^{2}\psi+k^{2}\sin^{2}\psi)^{1/4},$$
   $$\Phi_{k}=\arctan(k\tan\psi),$$
   taking $\Phi_{k}$ as the principal value for $0\le\psi\le90^{\circ}$ and $\Phi_{k}+\pi$ for $90^{\circ}<\psi\le180^{\circ}$.

7. The scaled phonon stress for a moving crack ($\mathcal{H}=\mathcal{D}=0$) is:
   $$\sqrt{r}\,10^{5}\,\frac{\sigma_{\psi z}}{K_{\mathcal{T}}} = 10^{5}\left[ \frac{\bar{\Lambda}_{1}}{\Delta_{\beta_{1}}}\,C_{1} + \frac{\bar{\Lambda}_{2}}{\Delta_{\beta_{2}}}\,C_{2} \right],$$
   where $C_{k} = \frac{1}{\beta_{k}}\sin\!\left(\frac{\Phi_{\beta_{k}}}{2}\right)\sin\psi + \cos\!\left(\frac{\Phi_{\beta_{k}}}{2}\right)\cos\psi$.

   For the stationary case ($v=0$), the expression reduces to $\cos(\psi/2)$.

The computation proceeds by first evaluating the derived parameters for each speed, then evaluating the angular distribution at each $\psi$.

## Reproduction target
The goal is to produce a CSV file named `scaled_stress.csv` located at `/app/outputs/scaled_stress.csv` containing four columns:

- `psi_deg`: angle $\psi$ in degrees, from 0 to 180 inclusive, in 1° increments (181 rows).
- `scaled_stress_v0`: the computed value of $\sqrt{r}\,10^{5}\,\sigma_{\psi z}/K_{\mathcal{T}}$ for crack speed ratio $v/s_{2}=0$.
- `scaled_stress_v99`: the computed value for $v/s_{2}=0.99$.
- `scaled_stress_stationary`: the stationary‑crack scaled stress, equal to $\cos(\psi/2)$.

All values must be floating‑point numbers. The CSV must contain a header row with the column names exactly as specified.

## Assets

- Piezoelectric quasicrystal material constants (Li et al. 2014)

## Workflow steps

### Step 1: Compute piezoelectrically stiffened moduli and derived parameters
- Role: process
- Action: Using the provided material constants, compute the piezoelectrically stiffened elastic moduli (c̄₄₄, K̄, R̄), the wave speeds s₁ and s₂, the dimensionless quantities α, β₁, β₂, and the eight Λ̄ coefficients (Λ̄₁–Λ̄₈) for each crack speed ratio (v/s₂ = 0 and 0.99). These derived parameters are required to evaluate the crack‑tip stress expressions.
- Evidence: none

### Step 2: Compute crack‑tip phonon stress angular distribution
- Role: scored (load-bearing)
- Action: For each angle ψ from 0° to 180° in 1° increments, compute the scaled phonon stress component √r 10⁵ σψz/K_T for the two moving crack speeds (v/s₂ = 0 and 0.99) using the derived parameters and the appropriate near‑tip formulas (with ℋ = 𝒟 = 0). Also compute the stationary‑case scaled stress as cos(ψ/2). Write the results to scaled_stress.csv.
- Output file: `/app/outputs/scaled_stress.csv`
- Format: csv
- Contract: Four columns: psi_deg (float, angle in degrees), scaled_stress_v0 (float), scaled_stress_v99 (float), scaled_stress_stationary (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/scaled_stress.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### scaled_stress.csv
- path: `/app/outputs/scaled_stress.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Scaled crack‑tip phonon stress angular distribution for two crack speeds and the stationary case.
- schema:
  - `type`: table
  - `required_columns`: `psi_deg`, `scaled_stress_v0`, `scaled_stress_v99`, `scaled_stress_stationary`

Notes: The hidden checker recomputes the scaled stress values using the same algebraic expressions and material constants; the agent's submitted columns are compared to the recomputed gold with a tolerance‑based threshold. The stationary case is compared to cos(ψ/2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "scaled_stress.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "psi_deg",
          "scaled_stress_v0",
          "scaled_stress_v99",
          "scaled_stress_stationary"
        ]
      },
      "description": "Scaled crack‑tip phonon stress angular distribution for two crack speeds and the stationary case."
    }
  ],
  "notes": "The hidden checker recomputes the scaled stress values using the same algebraic expressions and material constants; the agent's submitted columns are compared to the recomputed gold with a tolerance‑based threshold. The stationary case is compared to cos(ψ/2)."
}
```

## How you are scored
A hidden verifier will load the output file and validate its format. It will independently recompute the scaled stress values using the same public formulas and material constants. For each of the three columns (`scaled_stress_v0`, `scaled_stress_v99`, `scaled_stress_stationary`), the verifier will compare the submitted values to the recomputed gold with a tolerance policy (a combination of relative and absolute error). The stationary column is compared to the exact expression $\cos(\psi/2)$. The final reward (a numeric score between 0 and 1) is a weighted combination of the agreement across the columns; columns with larger deviation from the hidden gold receive lower weight. The exact thresholds and weights are not disclosed.
