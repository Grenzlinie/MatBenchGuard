# Fit monoclinic thermal conductivity tensor from orientation-resolved TDTR data

## Problem background
The thermal conductivity of $\beta$‑Y$_2$Si$_2$O$_7$ is anisotropic due to its monoclinic crystal structure. In a polycrystalline sample, individual grains have different crystallographic orientations, leading to a spatially varying cross‑plane thermal conductivity. By measuring the thermal conductivity of many grains with known orientations, one can reconstruct the full thermal conductivity tensor, which describes direction‑dependent heat conduction. The key target is the four independent tensor components ($\kappa_{xx}$, $\kappa_{yy}$, $\kappa_{zz}$, $\kappa_{xz}$) and the effective isotropic thermal conductivity $\kappa_{\text{eff}}$ derived from the tensor determinant.

## Approach
The dataset consists of a published supplementary table that lists, for multiple $\beta$‑Y$_2$Si$_2$O$_7$ grains, the spherical orientation angles $\theta$ and $\phi$ obtained from EBSD and the corresponding cross‑plane thermal conductivity $\kappa(\theta,\phi)$ measured by TDTR. For a monoclinic crystal, the directional thermal conductivity obeys the angular dependence

$$\kappa(\theta,\phi) = \kappa_{xx}\sin^2\!\phi\cos^2\!\theta + \kappa_{yy}\sin^2\!\phi\sin^2\!\theta + \kappa_{zz}\cos^2\!\phi + 2\kappa_{xz}\sin\phi\cos\theta\cos\phi.$$

You will parse this table, then perform a least‑squares fit of the above relation to the measured $(\theta,\phi,\kappa)$ triples to recover the best‑fit values of $\kappa_{xx}$, $\kappa_{yy}$, $\kappa_{zz}$, and $\kappa_{xz}$. Finally, compute $\kappa_{\text{eff}}$ as the cube root of the determinant of the tensor: $\kappa_{\text{eff}} = (\kappa_{xx}\kappa_{yy}\kappa_{zz} - \kappa_{yy}\kappa_{xz}^2)^{1/3}$. The tensor components and $\kappa_{\text{eff}}$ are the main quantities to be reported.

## Reproduction target
Determine the four independent components of the monoclinic thermal conductivity tensor ($\kappa_{xx}$, $\kappa_{yy}$, $\kappa_{zz}$, $\kappa_{xz}$) and the effective thermal conductivity $\kappa_{\text{eff}}$ by performing a least‑squares fit of the angular dependence $\kappa(\theta,\phi)$ to the grain‑resolved measurements in the supplementary data table. Report the fitted values (optionally with uncertainties) in a JSON file following the required schema.

## Assets

- Grain‑resolved thermal conductivity and orientation data of β‑Y₂Si₂O₇: 10.1016/j.actamat.2020.02.040
- SciPy: scipy

## Workflow steps

### Step 1: Load grain‑resolved measurements
- Role: process
- Action: Download and parse the supplementary data table containing grain orientations (θ, φ) and measured cross‑plane thermal conductivities κ(θ,φ) for β‑Y₂Si₂O₇ grains. Parse into a clean table of θ, φ, and κ values suitable for the subsequent fitting step.
- Evidence: `/app/outputs/loaded_data.csv`

### Step 2: Fit monoclinic thermal conductivity tensor
- Role: scored (load-bearing)
- Action: Using the parsed grain‑resolved measurements, perform a least‑squares minimization of the monoclinic angular dependence equation κ(θ,φ) = κ_xx sin²φ cos²θ + κ_yy sin²φ sin²θ + κ_zz cos²φ + 2 κ_xz sinφ cosθ cosφ to recover the four independent thermal conductivity tensor components (κ_xx, κ_yy, κ_zz, κ_xz). Compute the effective thermal conductivity κ_eff = (det(K))^(1/3) = (κ_xx κ_yy κ_zz − κ_yy κ_xz²)^(1/3).
- Output file: `/app/outputs/fitted_tensor.json`
- Format: json
- Contract: {"type":"object","required":["kappa_xx","kappa_yy","kappa_zz","kappa_xz","kappa_eff"],"properties":{"kappa_xx":{"type":"number","unit":"W/(m*K)"},"kappa_yy":{"type":"number","unit":"W/(m*K)"},"kappa_zz":{"type":"number","unit":"W/(m*K)"},"kappa_xz":{"type":"number","unit":"W/(m*K)"},"kappa_eff":{"type":"number","unit":"W/(m*K)"},"kappa_xx_uncertainty":{"type":"number","unit":"W/(m*K)"},"kappa_yy_uncertainty":{"type":"number","unit":"W/(m*K)"},"kappa_zz_uncertainty":{"type":"number","unit":"W/(m*K)"},"kappa_xz_uncertainty":{"type":"number","unit":"W/(m*K)"}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_tensor.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_tensor.json
- path: `/app/outputs/fitted_tensor.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Fitted thermal conductivity tensor components and the derived effective thermal conductivity. The checker will independently perform the least‑squares fit on the same supplementary data and compare the agent's reported values within tolerances.
- schema:
  - `type`: object
  - `required`:
    - `kappa_xx`: number (W/(m*K))
    - `kappa_yy`: number (W/(m*K))
    - `kappa_zz`: number (W/(m*K))
    - `kappa_xz`: number (W/(m*K))
    - `kappa_eff`: number (W/(m*K))
  - `properties`:
    - `kappa_xx`: number
    - `kappa_yy`: number
    - `kappa_zz`: number
    - `kappa_xz`: number
    - `kappa_eff`: number
    - `kappa_xx_uncertainty`: number (optional)
    - `kappa_yy_uncertainty`: number (optional)
    - `kappa_zz_uncertainty`: number (optional)
    - `kappa_xz_uncertainty`: number (optional)
  - `units`:
    - `kappa_xx`: W/(m*K)
    - `kappa_yy`: W/(m*K)
    - `kappa_zz`: W/(m*K)
    - `kappa_xz`: W/(m*K)
    - `kappa_eff`: W/(m*K)

Notes: The checker recomputes the tensor from the public supplementary data and compares the agent's reported components and κ_eff to the recomputed reference. The comparison uses relative tolerances consistent with the paper's own uncertainty estimates.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_tensor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "kappa_xx": "number (W/(m*K))",
          "kappa_yy": "number (W/(m*K))",
          "kappa_zz": "number (W/(m*K))",
          "kappa_xz": "number (W/(m*K))",
          "kappa_eff": "number (W/(m*K))"
        },
        "properties": {
          "kappa_xx": "number",
          "kappa_yy": "number",
          "kappa_zz": "number",
          "kappa_xz": "number",
          "kappa_eff": "number",
          "kappa_xx_uncertainty": "number (optional)",
          "kappa_yy_uncertainty": "number (optional)",
          "kappa_zz_uncertainty": "number (optional)",
          "kappa_xz_uncertainty": "number (optional)"
        },
        "units": {
          "kappa_xx": "W/(m*K)",
          "kappa_yy": "W/(m*K)",
          "kappa_zz": "W/(m*K)",
          "kappa_xz": "W/(m*K)",
          "kappa_eff": "W/(m*K)"
        }
      },
      "description": "Fitted thermal conductivity tensor components and the derived effective thermal conductivity. The checker will independently perform the least‑squares fit on the same supplementary data and compare the agent's reported values within tolerances."
    }
  ],
  "notes": "The checker recomputes the tensor from the public supplementary data and compares the agent's reported components and κ_eff to the recomputed reference. The comparison uses relative tolerances consistent with the paper's own uncertainty estimates."
}
```

## How you are scored
A hidden verifier holds the same supplementary data. It will independently perform the least‑squares fit using the same angular dependence relation to produce its own reference values for $\kappa_{xx}$, $\kappa_{yy}$, $\kappa_{zz}$, $\kappa_{xz}$, and $\kappa_{\text{eff}}$. Your submitted numbers are compared against these reference recomputed values. The verifier evaluates how closely your fitted components match the references, checks that the JSON file conforms to the expected schema, and produces a single reward score between 0 and 1. The reward is based on the accuracy of all required quantities. Reproducing the scatter and performing the fit correctly is essential; simply reporting the paper’s published numbers will not suffice because the checker recomputes from the data.
