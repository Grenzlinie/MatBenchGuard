# Vibronic Intensity Ratios from Spin-Orbit Mixing with Crossing Potentials

## Problem background
In impurity centers with degenerate electronic states and non-zero spin, such as the O₂⁻-type molecular ions S₂⁻, Se₂⁻, or O₂⁻ in alkali halides, luminescence spectra often exhibit two distinct vibronic series. The origin of these two series and the peculiar redistribution of intensity between them—where one series loses intensity to the other as vibrational quantum number increases—was not adequately explained by earlier models that treated the electronic states independently of the vibrational coordinate. The open question is whether a model that includes spin-orbit mixing between crossing adiabatic potential curves, making the electronic wave functions explicitly dependent on the internuclear distance, can account for the observed intensity transfer. This task tests that hypothesis for the specific case of S₂⁻ in KI by computing the predicted intensity ratios between the two series for vibrational levels v = 1 to 5.

## Approach
The model considers two low-lying electronic states resulting from crystal-field splitting of a degenerate term in D₂h symmetry. Their 'bare' adiabatic potentials are harmonic but have different equilibrium positions (displaced by β) and are offset by a crystal-field splitting Δ. Spin-orbit coupling (parameter λ) mixes these two states. A unitary transformation is applied to the electronic Hamiltonian, producing new mixed states whose electronic wave functions are linear combinations of the two original states, with mixing coefficients that depend on the dimensionless internuclear coordinate ρ through the function η(ρ) = √(α²(ρ)+λ²) − α(ρ) where α(ρ) = ρβ + Δ. The transition from a common excited state (modeled as a single harmonic potential with Stokes shift ξ_a and vibrational quantum Ω₃) to these mixed states is described by matrix elements that are integrals of the product of harmonic oscillator wave functions and the coordinate-dependent mixing coefficients. For a vibrational quantum number v, the intensity ratio of the two series, I_v^b / I_{v-1}^a, is the squared ratio of two such integrals. The integrals involve φ₀′(ρ-ξ_a+β/2) for the initial level, and for the final levels φ_v″(ρ-β/2) (with coefficient λ/√(η²+λ²)) and φ_{v-1}″(ρ+β/2) (with coefficient η/√(η²+λ²)). The task is to implement this model numerically using the provided parameters, compute the five ratios v=1…5 via adaptive quadrature, and output them as a structured JSON file.

## Reproduction target
Using the parameters given in the workflow step (λ=0.56, Δ=0.767, ℏΩ=597.5 cm⁻¹, ℏΩ₃=362.3 cm⁻¹, ξ_a=3.9, β=−0.39), implement the spin-orbit mixing model and compute the five intensity ratios I_v^b / I_{v-1}^a for v = 1, 2, 3, 4, 5. Write these ratios as a JSON object with top-level keys "v1" through "v5" to the file `/app/outputs/intensity_ratios.json`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute vibronic intensity ratios
- Role: scored
- Action: Implement the model of spin-orbit mixing with coordinate-dependent adiabatic potentials for O2- type impurity centers in D2h symmetry. Using the provided parameters (spin-orbit coupling λ=0.56, crystal-field splitting Δ=0.767, vibrational quantum ℏΩ=597.5 cm⁻¹, excited‑state vibrational quantum ℏΩ₃=362.3 cm⁻¹, Stokes shift ξ_a=3.9, equilibrium displacement β=-0.39), construct harmonic oscillator wave functions in the dimensionless coordinate ρ. Compute η(ρ)=√(α²(ρ)+λ²)−α(ρ) with α(ρ)=ρβ+Δ. For each vibrational quantum number v=1,2,3,4,5, numerically evaluate the two integrals involving φ₀'(ρ-ξ_a+β/2), φ_v''(ρ-β/2), φ_{v-1}''(ρ+β/2) and the mixing coefficients λ/√(η²+λ²) and η/√(η²+λ²). Compute the squared ratio of these integrals to obtain the intensity ratio I_v^b / I_{v-1}^a. Write the five ratios as a JSON object with top‑level keys v1 through v5 to intensity_ratios.json.
- Output file: `/app/outputs/intensity_ratios.json`
- Format: json
- Contract: {"v1": <float>, "v2": <float>, "v3": <float>, "v4": <float>, "v5": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/intensity_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### intensity_ratios.json
- path: `/app/outputs/intensity_ratios.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Vibronic transition intensity ratios I_v^b / I_{v-1}^a for the two luminescence series.
- schema:
  - `type`: object
  - `required`:
    - `v1`: float
    - `v2`: float
    - `v3`: float
    - `v4`: float
    - `v5`: float

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "intensity_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "v1": "float",
          "v2": "float",
          "v3": "float",
          "v4": "float",
          "v5": "float"
        }
      },
      "description": "Vibronic transition intensity ratios I_v^b / I_{v-1}^a for the two luminescence series."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads your intensity_ratios.json. It compares each reported ratio to a reference value (the theoretical ratio computed with the same parameters) using a predefined absolute tolerance. The reward is the fraction of ratios that lie within tolerance. Reporting numbers without performing the required computation is unlikely to succeed—the verifier expects genuine numerical integration.
