# Theoretical Model of Piezoelectric-Induced Bending in Quartz Crystals for X-ray Diffraction

## Problem background
In x‑ray diffraction from thick single crystals, the integrated reflection coefficient (the area under the diffraction line) is proportional to the angular width of the mosaic‑block distribution. For the most perfect crystals, such as quartz, this natural mosaic width can be as small as a fraction of an arcsecond, limiting the intensity of the reflected beam. The *piezo‑quasi‑mosaic effect* is a theoretical mechanism by which an applied DC voltage across a piezoelectric quartz plate bends the reflecting planes inhomogeneously, creating an artificial angular broadening that mimics a larger mosaic width and thereby increases the integrated reflection coefficient. This task asks you to implement the theoretical model of this effect and compute the resulting gain in integrated reflection for a specific example.

## Approach
A one‑dimensional planar model is used. A plane‑parallel quartz plate of thickness \(L\) carries a DC voltage \(U_0\) across its faces. To account for space‑charge layers that develop near the electrodes, the potential inside the plate is modelled as
\[
V(y) = U_0\!\left(\frac{y}{L} + \frac{1}{2\pi}\sin\!\frac{2\pi y}{L}\right),
\qquad 0 \le y \le L,
\]
where the coefficient of the sinusoid is chosen so that the electric field vanishes at the centre (\(E(L/2)\approx0\)). From this potential the electric field \(E(y) = -dV/dy\) is obtained.

The piezoelectric shear strain \(\gamma_{yz}\) that deforms the reflecting planes is proportional to \(E(y)\) via the tensor component \(d_{24}\):
\[
\gamma_{yz} = -d_{24}\,\frac{dV}{dy}.
\]
Integration yields the shape of the deformed reflecting plane,
\[
z(y) = -d_{24} V(y) + C.
\]
The angular distribution of the plane orientations, \(W_{\mathrm{pl}}(\varepsilon)\), is derived from the curvature and takes the form
\[
W_{\mathrm{pl}}(\varepsilon) = \frac{1}{\pi}
\left[\varepsilon\!\left(\frac{2 d_{24} U_0}{L} - \varepsilon\right)\right]^{-1/2},
\qquad 0 < \varepsilon < \frac{2 U_0 d_{24}}{L}.
\]
The full angular width of this distribution is the *piezo‑quasi‑mosaic width* \(\Phi = 2 U_0 d_{24} / L\).

Under thick‑crystal conditions the integrated reflection coefficient is proportional to the total mosaic width. Hence the relative gain compared to the crystal's natural mosaic width \(\omega_g\) is
\[
R_i / R_{\delta} = \Phi / \omega_g.
\]

This task evaluates the model for the specific example from the paper:
\(U_0 = 3000\ \text{V}\), \(L = 1\ \text{mm}\), \(d_{24} = 9\times10^{-8}\ \text{CGSE}\), and \(\omega_g = 0.7\ \text{arcsec}\). Because \(d_{24}\) is given in electrostatic CGSE units, the applied voltage must be converted from volts to statvolts (1 statvolt ≈ 300 V) before computing \(\Phi\) in radians; the width is then converted to arcseconds (1 rad = 206265 arcsec).

## Reproduction target
Compute the piezo‑quasi‑mosaic width \(\Phi\) in arcseconds and the relative gain \(R_i/R_{\delta}\) for the example parameters. Write these results to `/app/outputs/relative_gain.json`. Additionally, save the angular distribution \(W_{\mathrm{pl}}(\varepsilon)\) to `/app/outputs/w_pl_distribution.csv` as supporting evidence of the full model implementation.

## Assets
No external datasets, models, or proprietary tools are required. All computations can be performed with a standard Python environment (e.g., `numpy` for arrays, and the built‑in `json` and `csv` modules for output).

## Workflow steps

### Step 1: Compute potential distribution
- Role: process
- Action: Using the model potential $V(y) = U_0 (y/L + \sin(2\pi y/L)/(2\pi))$ derived from the space-charge model with boundary condition $E(y)|_{y=L/2} \approx 0$, compute $V(y)$ and the electric field $E(y) = -dV/dy$ over the plate thickness $[0, L]$.
- Evidence: none

### Step 2: Compute piezoelectric shear strain and reflecting plane shape
- Role: process
- Action: Using the piezoelectric coefficient $d_{24}$ (the appropriate tensor component), compute the shear strain $\gamma_{yz} = -d_{24} dV/dy$ and the deformed shape of the reflecting planes $z(y) = -d_{24} V(y) + C$.
- Evidence: none

### Step 3: Compute angular distribution W_pl(ε)
- Role: process
- Action: Compute the angular distribution $W_{\mathrm{pl}}(\varepsilon) = \frac{1}{\pi}\left[\varepsilon\left(\frac{2 d_{24} U_0}{L} - \varepsilon\right)\right]^{-1/2}$ for $0 < \varepsilon < 2 d_{24} U_0 / L$. Save the array of ($\varepsilon$ in arcseconds, $W_{\mathrm{pl}}$) as 'w_pl_distribution.csv' for evidence.
- Evidence: `/app/outputs/w_pl_distribution.csv`

### Step 4: Compute piezo-quasi-mosaic width and relative gain
- Role: scored (load-bearing)
- Action: Compute the piezo-quasi-mosaic width $\Phi = 2 U_0 d_{24} / L$ in radians, convert to arcseconds (1 rad = 206265 arcsec). Compute the relative gain $R_i/R_\delta = \Phi / \omega_g$ using $\omega_g = 0.7$ arcsec. Write the results to 'relative_gain.json'.
- Output file: `/app/outputs/relative_gain.json`
- Format: json
- Contract: {"piezo_quasi_mosaic_width_arcsec": <float>, "natural_mosaic_width_arcsec": 0.7, "relative_gain": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_gain.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_gain.json
- path: `/app/outputs/relative_gain.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed width and relative gain for the example parameters (U0=3000 V, L=1 mm, d24=9e-8 CGSE, ω_g=0.7 arcsec). The checker recomputes the expected values from hidden parameter conversions and compares the agent's reported values within a tolerance.
- schema:
  - `type`: object
  - `required`:
    - `piezo_quasi_mosaic_width_arcsec`: number (float, arcseconds)
    - `natural_mosaic_width_arcsec`: number (float, arcseconds)
    - `relative_gain`: number (float, dimensionless)
  - `items`: object
  - `required_columns`:
  - `units`:
    - `piezo_quasi_mosaic_width_arcsec`: arcseconds
    - `natural_mosaic_width_arcsec`: arcseconds
    - `relative_gain`: dimensionless

Notes: The natural_mosaic_width_arcsec field must equal exactly 0.7. The piezo_quasi_mosaic_width_arcsec and relative_gain are compared to hidden recomputed reference values with tolerance. Unit conversions and parameter handling are the agent's responsibility.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_gain.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "piezo_quasi_mosaic_width_arcsec": "number (float, arcseconds)",
          "natural_mosaic_width_arcsec": "number (float, arcseconds)",
          "relative_gain": "number (float, dimensionless)"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "piezo_quasi_mosaic_width_arcsec": "arcseconds",
          "natural_mosaic_width_arcsec": "arcseconds",
          "relative_gain": "dimensionless"
        }
      },
      "description": "Computed width and relative gain for the example parameters (U0=3000 V, L=1 mm, d24=9e-8 CGSE, ω_g=0.7 arcsec). The checker recomputes the expected values from hidden parameter conversions and compares the agent's reported values within a tolerance."
    }
  ],
  "notes": "The natural_mosaic_width_arcsec field must equal exactly 0.7. The piezo_quasi_mosaic_width_arcsec and relative_gain are compared to hidden recomputed reference values with tolerance. Unit conversions and parameter handling are the agent's responsibility."
}
```

## How you are scored
A hidden verifier parses your `relative_gain.json` and compares the reported `piezo_quasi_mosaic_width_arcsec` and `relative_gain` against reference values computed from the same parameters and correct unit conversions. The comparison allows for small numerical deviations within a tolerance. The `natural_mosaic_width_arcsec` field must be exactly 0.7. The distribution CSV may be audited for structural correctness. Your final score is a weighted combination of the stage scores produced by the verifier.
