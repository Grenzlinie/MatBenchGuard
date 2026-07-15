# Electronic Raman Response in Disordered d-Wave Superconductors

## Problem background
Electronic Raman scattering in unconventional superconductors offers a way to probe the symmetry of the superconducting order parameter. In particular, the polarization dependence of the Raman response can distinguish a d_{x^2-y^2} gap from an anisotropic s‑wave gap. Impurity scattering affects the low‑frequency behavior and peak positions, providing additional signatures. The theoretical challenge is to compute the non‑resonant Raman response in the q→0 limit for a d‑wave superconductor on a cylindrical Fermi surface, incorporating impurity self‑energy effects via the T‑matrix approximation and, optionally, a phenomenological inelastic self‑energy that models the high‑frequency continuum observed in experiments.

## Approach
The Raman vertex γ(k) is related to the curvature of the band dispersion and can be expanded in symmetry channels Φ_L(k) (B1g, B2g, A1g). The electronic Raman response is computed from the BCS Green’s function dressed by an impurity self‑energy obtained from the T‑matrix approximation for s‑wave scatterers. The impurity scattering is characterized by the cotangent of the scattering phase shift c and a scattering rate Γ. Vertex corrections are neglected for non‑density channels. The clean limit (no impurities) and the unitary limit (c=0) are compared. The Raman intensity as a function of frequency ω (in units of the gap Δ0) is evaluated numerically for a cylindrical Fermi surface and a d‑wave gap Δ(k)=Δ0 cos(2φ). In a second stage, a phenomenological inelastic self‑energy of the form Σ''(ω)=α√(ω²+βT²) is added to examine its effect on the B1g channel spectrum, with a small residual impurity scattering rate.

## Reproduction target
Compute the electronic Raman response χ''(ω) for a d_{x^2-y^2} superconductor on a cylindrical Fermi surface under two impurity conditions: the clean limit and the unitary impurity limit with a scattering rate Γ/Δ0 = 0.2. Produce frequency‑dependent spectra for the B1g, B2g, and A1g symmetry channels, and save them to `impurity_spectra.csv`. Then, incorporate the inelastic self‑energy with parameters α/Δ0 = 0.25, β = 3.3 and a small unitary scattering rate Γ/Δ0 = 0.01, compute the B1g spectrum, and save to `inelastic_spectrum.csv`. All frequencies are in units of Δ0; intensity is in arbitrary units.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute impurity-dressed Raman spectra for d-wave superconductor
- Role: scored (load-bearing)
- Action: Implement the non-resonant Raman response formula for a d‑wave gap on a cylindrical Fermi surface, including T‑matrix impurity self‑energy for s‑wave scatterers. Evaluate the Matsubara sum and momentum integration numerically for the clean limit (no impurities) and for the unitary impurity limit (cotangent of scattering phase shift c=0). Produce spectra for the B1g, B2g, and A1g symmetry channels. Output a CSV file with columns: frequency (in units of Δ0), channel, impurity_type, Gamma_over_Delta0, intensity.
- Output file: `/app/outputs/impurity_spectra.csv`
- Format: csv
- Contract: frequency: float (in units of Δ0), channel: str (one of B1g, B2g, A1g), impurity_type: str (one of clean, unitary), Gamma_over_Delta0: float, intensity: float (arbitrary units)
- Scoring: scored by hidden verifier

### Step 2: Compute B1g Raman spectrum with inelastic self-energy
- Role: scored
- Action: Extend the model by including a phenomenological inelastic self‑energy. Compute the B1g channel Raman response using a small unitary impurity scattering rate. Output a CSV file with columns: frequency (in units of Δ0) and intensity.
- Output file: `/app/outputs/inelastic_spectrum.csv`
- Format: csv
- Contract: frequency: float (in units of Δ0), intensity: float (arbitrary units)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/impurity_spectra.csv`
- `/app/outputs/inelastic_spectrum.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### impurity_spectra.csv
- path: `/app/outputs/impurity_spectra.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raman intensity vs frequency for multiple symmetry channels and impurity conditions.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `channel`, `impurity_type`, `Gamma_over_Delta0`, `intensity`
  - `units`:
    - `frequency`: units of Δ0
    - `intensity`: arbitrary

### inelastic_spectrum.csv
- path: `/app/outputs/inelastic_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raman intensity vs frequency for the B1g channel with inelastic self‑energy included.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `intensity`
  - `units`:
    - `frequency`: units of Δ0
    - `intensity`: arbitrary

Notes: The checker will recompute peak positions and power‑law exponents from the raw CSVs and compare them to paper‑reported values. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "impurity_spectra.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "channel",
          "impurity_type",
          "Gamma_over_Delta0",
          "intensity"
        ],
        "units": {
          "frequency": "units of Δ0",
          "intensity": "arbitrary"
        }
      },
      "description": "Raman intensity vs frequency for multiple symmetry channels and impurity conditions."
    },
    {
      "file": "inelastic_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "intensity"
        ],
        "units": {
          "frequency": "units of Δ0",
          "intensity": "arbitrary"
        }
      },
      "description": "Raman intensity vs frequency for the B1g channel with inelastic self‑energy included."
    }
  ],
  "notes": "The checker will recompute peak positions and power‑law exponents from the raw CSVs and compare them to paper‑reported values. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that independently scores each workflow stage's output artifact. For step 1, the verifier will read `impurity_spectra.csv` and recompute peak positions and low‑frequency power‑law exponents; these are compared to reference values, and the reward reflects the accuracy of the derived physics. For step 2, the high‑frequency decay of the inelastic spectrum is similarly recomputed. The final reward is a weighted combination of the scores from the two stages. Simply reporting the expected numbers is not sufficient; the spectra must be computed from the model and conditions specified.
