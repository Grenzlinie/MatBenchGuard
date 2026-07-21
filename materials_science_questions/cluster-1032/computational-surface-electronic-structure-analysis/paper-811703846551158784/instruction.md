# Surface mode existence and band crossing in binary metal-dielectric metamaterials

## Problem background
Binary metal-dielectric metamaterials are periodic stacks of metal and dielectric layers that support surface plasmon‑polariton (SPP) modes. When the unit cell contains two distinct coupling pathways — a normal coupling across a dielectric spacer and an anomalous coupling through a thin metal layer — the interplay of these alternating interactions can lead to rich band structures and to the formation of localized surface modes upon termination of the periodicity. The relative strength of the two couplings is captured by the asymmetry constant $\eta = C_- / C_+$, and the effect of a surface termination is described by a perturbation parameter $Z$. The nature of any resulting surface modes (whether they are Tamm‑like or Shockley‑like) and the conditions under which they exist are governed by $\eta$ and $Z$, while the bulk band dispersion may exhibit band crossing and inversion as $\eta$ varies. This task aims to compute the surface mode existence map in the $\eta$–$Z$ plane and to determine the band dispersion for a specific binary multilayer, revealing whether a Dirac point and band inversion occur.

## Approach
Coupled mode theory is used to model a semi‑infinite binary metamaterial. The complex field amplitudes of SPP modes in adjacent unit cells obey coupled differential equations parameterized by the coupling coefficients $C_+$ (dielectric‑mediated) and $C_-$ (metal‑mediated). For a terminated structure, the boundary condition at the surface introduces the perturbation $Z$. From the bulk equations and the surface boundary condition one obtains a quadratic equation for the decay parameter $r$ (see the explicit formula below). A localized surface mode exists when at least one root satisfies $|r|<1$. Evaluating this condition over a grid of $(\eta, Z)$ pairs yields the existence map. Separately, for the infinite bilayer specified in the workflow, the bulk band structure $\beta(\kappa)$ (propagation constant versus Bloch wave number $\kappa$) is computed, either by directly solving the coupled‑mode dispersion relation or via the full transfer matrix method for TM polarization. The coupling coefficients $C_+$ and $C_-$ (and hence $\eta$) are extracted first by performing an eigenmode analysis on the constituent gap‑SPP modes of the multilayer stack, using the material permittivities at the operating wavelength (1550 nm).

## Analytic expression for the decay parameter $r$
The decay parameter $r$ for a surface mode in a semi‑infinite binary metamaterial is obtained from the coupled‑mode equations and the surface boundary condition. For a given asymmetry $\eta = C_-/C_+$ and normalised surface perturbation $Z$, the possible values of $r$ satisfy the quadratic equation

$$
r^2 + \left( \frac{\eta^3}{Z^2} - \eta \right) r - \left( \frac{\eta}{Z} \right)^2 = 0,
\tag{1}
$$

where $Z \neq 0$. The two roots are

$$
r_\pm = \frac{1}{2}\left[ -\left(\frac{\eta^3}{Z^2} - \eta\right) \pm \sqrt{ \left(\frac{\eta^3}{Z^2} - \eta\right)^2 + 4\left(\frac{\eta}{Z}\right)^2 } \;\right].
\tag{2}
$$

For the special case $Z = 0$ the equation reduces to a Shockley‑type condition:

* if $\eta < -1$, a single valid solution exists, $r = -1/\eta$;
* if $\eta \ge -1$, no solution exists (no surface mode).

A given $(\eta, Z)$ pair supports a localised surface mode if at least one of the real roots (2) satisfies $|r| < 1$. The magnitude of the decay parameter for the output table $r_\text{magnitude}$ is defined as the minimum $|r|$ among all roots that satisfy $|r|<1$; if no root satisfies $|r|<1$, set `exists = 0` and $r_\text{magnitude} = \max(|r_+|, |r_-|)$ (for $Z=0$ with $\eta \ge -1$, set $r_\text{magnitude} = 1$).

## Reproduction target
Two principal quantities are produced: (1) the TM‑polarized dispersion curves for an infinite binary metamaterial composed of Au (8.4 nm) / MgF₂ (50 nm) / Si (200 nm) at $\lambda = 1550$ nm, with $\kappa$ spanning $[0, \pi]$ in at least 50 points, to confirm whether a Dirac point (near‑zero gap at $\kappa = 0$) and band inversion occur; and (2) a surface mode existence map for $\eta \in [-2.0, -0.5]$ (step 0.1) and $Z \in [-2.0, 2.0]$ (step 0.1), derived from the analytic solution of the coupled mode equations, recording for each $(\eta, Z)$ pair whether a localized mode exists and the magnitude of the decay parameter $r$ for the most localized (or least extended) branch.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Extract coupling coefficients from gap SPP modes
- Role: process
- Action: For the binary metal-dielectric multilayer with layer thicknesses Au = 8.4 nm, MgF₂ = 50 nm, Si = 200 nm at free-space wavelength 1550 nm, use the following material permittivities: for gold, $\varepsilon_\text{Au} = -115.2 + 11.2\,i$ (Johnson and Christy at 1550 nm); for MgF₂, $n = 1.34$ ($\varepsilon = 1.7956$); for Si, $n = 3.48$ ($\varepsilon = 12.1104$). Perform an eigenmode analysis (e.g. transfer matrix method or mode solver) to compute the propagation constants of symmetric and antisymmetric gap‑SPP modes for the metal‑dielectric‑metal gap (coupling through the Au layer) and for the coupling through the dielectric spacer, then calculate the coupling coefficients $C_+$ (dielectric‑mediated) and $C_-$ (metal‑mediated) and the asymmetry constant $\eta = C_-/C_+$.
- Output: intermediate (no file required for scoring); the values are used in Step 2.

### Step 2: Band dispersion calculation for the binary metamaterial
- Role: scored (load-bearing)
- Action: Using the coupling coefficients $C_+$ and $C_-$ from the previous step (or directly via the transfer matrix method for the same multilayer stack with the material parameters given above), compute the TM-polarized dispersion relation for the infinite binary metamaterial. Output propagation constants $\beta$ as a function of the Bloch wave number $\kappa \in [0, \pi]$ with at least 50 points.
- Output file: `/app/outputs/band_dispersion_dirac.csv`
- Format: csv
- Contract: CSV with columns: `kappa` (float, dimensionless, range $[0,\pi]$ with at least 50 points), `beta_upper` (float, normalized dimensionless propagation constant of the upper band), `beta_lower` (float, normalized dimensionless propagation constant of the lower band).
- Scoring: scored by hidden verifier

### Step 3: Surface mode existence map computation
- Role: scored
- Action: For each pair $(\eta, Z)$ with $\eta \in [-2.0, -0.5]$ in steps of 0.1 and $Z \in [-2.0, 2.0]$ in steps of 0.1, compute the possible values of the decay parameter $r$ using Eqs. (1)‑(2) (and the special case $Z=0$). Determine the existence flag `exists` = 1 if at least one root satisfies $|r| < 1$, else 0. Assign `r_magnitude` as the minimum $|r|$ among roots with $|r|<1$; if no root satisfies the condition set `r_magnitude = max(|r_+|, |r_-|)` (for $Z=0$, $\eta \ge -1$ set `r_magnitude = 1`).
- Output file: `/app/outputs/surface_mode_existence.csv`
- Format: csv
- Contract: CSV with columns: `eta` (float), `Z` (float), `exists` (int 0/1), `r_magnitude` (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_dispersion_dirac.csv`
- `/app/outputs/surface_mode_existence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_dispersion_dirac.csv
- path: `/app/outputs/band_dispersion_dirac.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dispersion curves for the upper and lower bands, used to verify the Dirac point and band inversion.
- schema:
  - `type`: table
  - `required_columns`: `kappa`, `beta_upper`, `beta_lower`
  - `units`:
    - `kappa`: dimensionless
    - `beta_upper`: normalized propagation constant
    - `beta_lower`: normalized propagation constant

### surface_mode_existence.csv
- path: `/app/outputs/surface_mode_existence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Existence map of surface modes as a function of asymmetry parameter eta and surface perturbation Z. The checker recomputes existence flags using the analytic formula as a structural consistency check.
- schema:
  - `type`: table
  - `required_columns`: `eta`, `Z`, `exists`, `r_magnitude`

## How you are scored
Each scored artifact is checked independently by a hidden verifier. For the band dispersion curves, the verifier examines structural properties: at $\kappa = 0$ the bandgap ($|\beta_{\text{upper}} - \beta_{\text{lower}}|$) should be nearly zero (indicating a Dirac point), and the bands should be approximately linear near $\kappa = 0$ with opposite slopes and matching intercepts. For the surface mode existence map, the verifier recomputes the existence flags from Eq. (1)‑(2) and compares them against the submitted `exists` column; the score is the fraction of matching $(\eta, Z)$ entries. The final reward is a weighted combination of the scores from both stages.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_dispersion_dirac.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "kappa",
          "beta_upper",
          "beta_lower"
        ],
        "units": {
          "kappa": "dimensionless",
          "beta_upper": "normalized propagation constant",
          "beta_lower": "normalized propagation constant"
        }
      },
      "description": "Dispersion curves for the upper and lower bands, used to verify the Dirac point and band inversion."
    },
    {
      "file": "surface_mode_existence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "Z",
          "exists",
          "r_magnitude"
        ]
      },
      "description": "Existence map of surface modes as a function of asymmetry parameter eta and surface perturbation Z. The checker recomputes existence flags using the analytic formula as a structural consistency check."
    }
  ],
  "notes": "The band dispersion step is load-bearing because its hidden reference values depend on the coupling coefficients extracted in the process step. The existence map step uses a structural audit via analytic recompute; no process dependency."
}
```