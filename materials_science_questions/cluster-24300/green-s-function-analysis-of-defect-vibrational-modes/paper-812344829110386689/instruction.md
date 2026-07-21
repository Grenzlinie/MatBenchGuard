# Resonant Acoustic Transmission through a Defect Monolayer in Anisotropic Crystals

## Problem background
Scattering of acoustic waves at a planar interface between two crystals is important for understanding phonon transport, thermal boundary resistance, and interface effects. In highly anisotropic layered crystals, a thin transition layer (e.g., an impurity monolayer) can give rise to resonant transmission of sound waves at a specific frequency where the reflection coefficient nearly vanishes and the transmission coefficient approaches unity. This resonant effect emerges from the coupling between the wave transmitted through the defect and a local vibrational mode of the impurity layer.

## Approach
Model the system as two semi-infinite body-centered tetragonal crystals separated by a single impurity monolayer. Write the harmonic equations of motion for the host lattices and the defect layer, with intralayer (α) and interlayer (γ) force constants. Impose the boundary conditions at the defect site and assume plane-wave solutions with an incident, reflected, and transmitted component. At normal incidence (kx = ky = 0), the system reduces to a pair of linear equations for the complex reflection coefficient r and transmission coefficient t as functions of the squared frequency ε = ω². The wave-vectors normal to the interface, k1z and k3z, are determined from the dispersion relations of each semi-infinite crystal. Solve these equations numerically for a dense grid of ε values to obtain the curves r(ε) and t(ε). Finally, locate the resonance squared frequency ε_res where r exhibits a deep minimum and t a maximum, and compute the resonance frequency ω_res = √(ε_res).

## Reproduction target
Produce the numerical solution for the reflection coefficient r(ε) and transmission coefficient t(ε) using the fully specified crystal and defect parameters listed in Step 1. From these curves, identify the squared frequency ε_res at which resonance occurs (ideally r ≈ 0, t ≈ 1) and compute the corresponding angular frequency ω_res = √(ε_res). Output these two values as a JSON object with keys epsilon_res and omega_res.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute reflection/transmission curves
- Role: process
- Action: Implement the lattice-dynamical model for two identical semi-infinite body-centered tetragonal crystals separated by an impurity monolayer. Using the given parameters (α1=α3=1, γ1=γ3=0.1, m1=m2=1, α2=0.5, γ2^(1)=γ2^(3)=0.07) at normal incidence (kx=0, ky=0), derive the system of equations for the reflection coefficient r and transmission coefficient t as functions of the squared frequency ε. Solve the system numerically on a dense grid of ε values around the expected resonance. Save the curves in a CSV file with columns epsilon, r, t.
- Evidence: `/app/outputs/resonance_curve.csv`

### Step 2: Extract resonance frequency
- Role: scored (load-bearing)
- Action: From resonance_curve.csv, locate the ε where the reflection coefficient r has a minimum and the transmission coefficient t has a maximum (ideally r≈0, t≈1). Record that ε as ε_res. Compute ω_res = sqrt(ε_res). Save these two values in a JSON file with keys epsilon_res and omega_res.
- Output file: `/app/outputs/resonance.json`
- Format: json
- Contract: {"epsilon_res": <float>, "omega_res": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/resonance.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### resonance.json
- path: `/app/outputs/resonance.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Scored artifact containing the numerically determined resonance frequency. The verifier compares your omega_res to a hidden reference derived from the system parameters; do not attempt to guess it, compute from the full lattice-dynamical model.
- schema:
  - `type`: object
  - `required`:
    - `epsilon_res`: number
    - `omega_res`: number
  - `description`: The resonance squared frequency epsilon_res and resonance frequency omega_res for the impurity monolayer system.

Notes: The resonance_curve.csv produced by step_01 is supporting evidence but not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "resonance.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "epsilon_res": "number",
          "omega_res": "number"
        },
        "description": "The resonance squared frequency epsilon_res and resonance frequency omega_res for the impurity monolayer system."
      },
      "description": "Scored artifact containing the numerically determined resonance frequency. The verifier compares your omega_res to a hidden reference derived from the system parameters; do not attempt to guess it, compute from the full lattice-dynamical model."
    }
  ],
  "notes": "The resonance_curve.csv produced by step_01 is supporting evidence but not directly scored."
}
```

## How you are scored
A hidden verifier reads your resonance.json file, extracts the value of omega_res, and compares it to a hidden reference resonance frequency derived from the model parameters. If the relative difference |ω_res − ω_ref| / ω_ref is within a fixed tolerance, the verification returns 1.0 for this artifact; otherwise it returns 0.0. The overall task reward is determined by the weight of this scored artifact. No other artifact is scored.
