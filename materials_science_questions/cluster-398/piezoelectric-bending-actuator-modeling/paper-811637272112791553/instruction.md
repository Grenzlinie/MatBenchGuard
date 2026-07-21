# Acoustic Resonance Bumps in Josephson Current Prediction

## Problem background
A long Josephson junction can support electromagnetic oscillations (Josephson plasma waves) that couple to mechanical vibrations in the junction's dielectric layer and the substrate through piezoelectric or electrostrictive effects. This coupling leads to a coupled electroacoustic dispersion relation. When the junction is biased at a constant voltage, the dc Josephson current acquires a resonant structure: in addition to the usual Fiske steps, additional current bumps are predicted at frequencies corresponding to high-overtone acoustic modes of the substrate, which acts as a composite resonator. This task reproduces the predicted current versus normalized frequency curve to examine whether such acoustic resonance bumps appear.

## Approach
The approach uses a theoretical model that combines the electrodynamics of a long Josephson junction with the elasticity of a piezoelectric medium. Starting from the Josephson relations and Maxwell's equations, a generalized wave equation for the phase difference is derived, coupled to the elastic displacement field via piezoelectric polarization. For harmonic solutions, a dispersion relation for coupled electroacoustic waves is obtained. This dispersion relation, together with the electrostriction/piezoelectric coupling, modifies the effective dielectric constant and, therefore, the dc Josephson current. The uniform current component is computed as a function of normalized frequency using the paper's analytical expression that follows from the coupled dispersion relation. The computation incorporates the electromechanical coupling constant δ, the normalized damping Γ̄/Ωn, and the wave-vector ratio Im k/Re k; the term proportional to (v⊥/c̃)² is neglected because the acoustic velocity is much smaller than the electromagnetic Swihart velocity. The agent should implement the dispersion relation and the current expression, then evaluate the current numerically over the specified frequency range.

## Reproduction target
Compute the normalized Josephson current j0/j̃0 as a function of the normalized frequency ω/Ωn over the interval [0.5, 5.0] using the coupled electroacoustic model, with parameters δ = 2.5×10⁻⁷, Γ̄/Ωn = 0.03, Im k/Re k = 10⁻⁶, and neglecting the v⊥/c̃ term. Write the computed values to /app/outputs/relative_current.csv. The hidden verifier will then examine the resulting current–frequency curve to check whether it displays resonant local maxima at integer multiples of the fundamental acoustic resonance frequency (i.e., at ω/Ωn ≈ 1, 2, 3, 4) that are clearly distinguishable from the background, as predicted by the coupled electroacoustic theory.

## Assets
No external datasets, pre-trained models, or service accounts are needed. The computation requires only a standard scientific Python environment (numpy, scipy). All necessary mathematical expressions and parameter values are provided in this instruction.

## Workflow steps

### Step 1: Compute relative Josephson current vs normalized frequency
- Role: scored
- Action: Implement the theoretical model for coupled electroacoustic oscillations in a long Josephson junction, yielding a dispersion relation and an expression for the uniform (dc) Josephson current. Using the electromechanical coupling constant δ=2.5×10⁻⁷, normalized damping Γ̄/Ωn=0.03, and imaginary-to-real wave-number ratio Im k/Re k=10⁻⁶, compute the normalized current j0/j̃0 as a function of normalized frequency ω/Ωn over the interval 0.5 to 5.0 with at least 100 equally spaced points. Write the result to the output CSV.
- Output file: `/app/outputs/relative_current.csv`
- Format: csv
- Contract: Two columns: 'omega_over_Omega_n' (float, dimensionless ω/Ωn) and 'relative_current' (float, dimensionless j0/j̃0). At least 100 rows covering [0.5, 5.0].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_current.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_current.csv
- path: `/app/outputs/relative_current.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Relative Josephson current as a function of normalized frequency, showing predicted bumps at acoustic resonance frequencies.
- schema:
  - `type`: table
  - `required_columns`: `omega_over_Omega_n`, `relative_current`
  - `units`:
    - `omega_over_Omega_n`: dimensionless (ω/Ωn)
    - `relative_current`: dimensionless (j0/j̃0)

Notes: The parameters δ=2.5e-7, Γ̄/Ωn=0.03, Im k/Re k=1e-6 define the specific model instance being evaluated; these are necessary inputs to the computation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_current.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "omega_over_Omega_n",
          "relative_current"
        ],
        "units": {
          "omega_over_Omega_n": "dimensionless (ω/Ωn)",
          "relative_current": "dimensionless (j0/j̃0)"
        }
      },
      "description": "Relative Josephson current as a function of normalized frequency, showing predicted bumps at acoustic resonance frequencies."
    }
  ],
  "notes": "The parameters δ=2.5e-7, Γ̄/Ωn=0.03, Im k/Re k=1e-6 define the specific model instance being evaluated; these are necessary inputs to the computation."
}
```

## How you are scored
The verifier loads your CSV and performs a structural audit. It identifies local maxima in the relative_current column and verifies that maxima occur at approximately integer ω/Ωn values (within a small tolerance) and that their peak values are substantially above the local background. The final reward is proportional to the correctness and clarity of these structural features; no absolute reference value is required.
