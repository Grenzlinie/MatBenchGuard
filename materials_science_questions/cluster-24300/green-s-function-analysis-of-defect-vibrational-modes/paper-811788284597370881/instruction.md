# Zero-Phonon Line Characteristics under Joint Electron-Phonon Coupling: Debye-Van Hove Model

## Problem background
Zero-phonon lines (ZPL) are narrow, intense optical transitions in solids that are sensitive to electron-phonon coupling. When both linear and quadratic vibronic coupling are present, the ZPL's relative intensity, spectral position, and linewidth deviate from predictions of the purely linear-coupling model. Understanding these deviations requires computing renormalized quantities—the Huang-Rhys factor, the Stokes shift, and the quadratic-coupling contribution to linewidth and shift—for a specified phonon spectrum and coupling strengths. This task computes those quantities for the Debye-Van Hove model, a simple analytical phonon model, as a function of quadratic coupling strength and temperature. The output is a numerical characterisation of how the joint coupling shapes the zero-phonon line.

## Approach
The calculation uses a single effective configurational coordinate with linear coupling parameter a=1 and quadratic coupling parameter b. The phonon bath is described by the Debye-Van Hove model: a density of states ρ(ω) ∝ ω⁴√(1-ω²) for frequencies 0≤ω≤1 (top frequency taken as unity). From ρ(ω) one obtains the phonon Green's function G(ω). Temperature enters via the Bose factor n(ω,T).

For each (b,T) pair the procedure constructs an auxiliary function 𝔇(ω)=G(ω)+i·2n(|ω|,T)·Im G(ω). The quadratic coupling renormalises this to 𝔇̃(ω)=𝔇(ω)/(1−b·𝔇(ω)). The characteristic ZPL quantities are then obtained by numerically evaluating the following integrals:
- Stokes shift δ_L from the real part of 𝔇̃ at zero frequency.
- Renormalised Huang-Rhys factor for absorption from the integral of ω⁻² Im 𝔇̃(ω).
- Renormalised Huang-Rhys factor for luminescence, which involves an additional factor |1−bG(ω)|² inside the integrand.
- The linewidth γ and shift δ_Q due to quadratic coupling come from the real and imaginary parts of the integral of ln(1−b𝔇(ω)).

All integrals are evaluated with standard numerical integration, with care to handle the integrable singularity at ω=0. The computation is repeated for nine (b,T) combinations and the results are collected in a JSON file.

## Reproduction target
Compute the zero-phonon line quantities for the scalar Debye-Van Hove model with linear coupling a=1. Evaluate the following for every pair from quadratic coupling parameter b ∈ {−0.2, 0, 0.16} and reduced temperature T/ω_top ∈ {0, 0.1, 0.5}:
- Stokes shift δ_L.
- Renormalised Huang-Rhys factor for absorption, S_L_absorption.
- Renormalised Huang-Rhys factor for luminescence, S_L_luminescence.
- Quadratic-coupling contribution to the linewidth γ and shift δ_Q.
Organise the results as a JSON file that lists the parameter values and, for each (b,T) pair, an object with all computed numbers. The required output schema is provided in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define Debye-Van Hove model functions
- Role: process
- Action: Implement the phonon density of states and the phonon Green's function for the Debye-Van Hove model: ρ(ω) = (32/π) ω⁴ √(1-ω²) for 0 ≤ ω ≤ 1, Re G(ω) = -2 - 8ω² + 16ω⁴, Im G(ω) = (π/(2ω)) ρ(ω). Also implement the Bose occupation factor n(ω, T) for given temperature T (in units of top phonon frequency). These are building blocks for all subsequent integrals.
- Evidence: none

### Step 2: Compute renormalized spectral functions for each b
- Role: process
- Action: For each quadratic coupling parameter b in [-0.2, 0, 0.16], define the auxiliary matrix D(ω) = G(ω) + i 2 n(|ω|, T) Im G(ω) and the renormalized quantity D_tilde(ω) = D(ω) / (1 - b D(ω)). These will be used in the final scored step. Implement as functions that accept ω, b, T and return complex values.
- Evidence: none

### Step 3: Compute ZPL quantities and write output
- Role: scored (load-bearing)
- Action: For each combination of b ∈ [−0.2, 0, 0.16] and dimensionless temperature T ∈ [0, 0.1, 0.5] (with k_B T / ħ ω_top), compute:
- Stokes shift δ_L = (a² / (2π)) Re[ D_tilde(0) ] with a = 1.
- Renormalized Huang-Rhys factor for absorption: S_L_absorption = (a² / π) ∫_0^∞ ω^{-2} Im[ D_tilde(ω) ] dω.
- Renormalized Huang-Rhys factor for luminescence: S_L_luminescence = (a² / π) ∫_0^∞ ω^{-2} Im[ D_tilde(ω) |1 - b G(ω)|² ] dω.
- Linewidth and shift from quadratic coupling: γ - i δ_Q = (1/(2π)) ∫_0^∞ ln(1 - b D(ω)) dω; separate real (γ) and imaginary (δ_Q) parts.
Use numerical integration and handle the singularity at ω=0 properly. Output a JSON file with the computed results.
- Output file: `/app/outputs/zpl_quantities.json`
- Format: json
- Contract: JSON object with keys: 'b_values' (list of floats), 'T_values' (list of floats), 'results' (list of objects, each with fields: {b, T, delta_L, S_L_absorption, S_L_luminescence, gamma, delta_Q}). All numeric fields are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/zpl_quantities.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### zpl_quantities.json
- path: `/app/outputs/zpl_quantities.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed zero-phonon line quantities: renormalized Huang-Rhys factor (absorption and luminescence), Stokes shift, and quadratic-coupling linewidth/shift for b ∈ {-0.2, 0, 0.16} and T/ω_top ∈ {0, 0.1, 0.5} in the Debye-Van Hove model.
- schema:
  - `type`: object
  - `required`: `b_values`, `T_values`, `results`
  - `properties`:
    - `b_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `T_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `results`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `b`, `T`, `delta_L`, `S_L_absorption`, `S_L_luminescence`, `gamma`, `delta_Q`
        - `properties`:
          - `b`:
            - `type`: number
          - `T`:
            - `type`: number
          - `delta_L`:
            - `type`: number
          - `S_L_absorption`:
            - `type`: number
          - `S_L_luminescence`:
            - `type`: number
          - `gamma`:
            - `type`: number
          - `delta_Q`:
            - `type`: number

Notes: All quantities computed using the Debye-Van Hove model with top phonon frequency = 1 and linear coupling a = 1. The integrals require careful handling of the ω→0 singularity. No external data beyond the model equations is needed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "zpl_quantities.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "b_values",
          "T_values",
          "results"
        ],
        "properties": {
          "b_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "T_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "results": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "b",
                "T",
                "delta_L",
                "S_L_absorption",
                "S_L_luminescence",
                "gamma",
                "delta_Q"
              ],
              "properties": {
                "b": {
                  "type": "number"
                },
                "T": {
                  "type": "number"
                },
                "delta_L": {
                  "type": "number"
                },
                "S_L_absorption": {
                  "type": "number"
                },
                "S_L_luminescence": {
                  "type": "number"
                },
                "gamma": {
                  "type": "number"
                },
                "delta_Q": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Computed zero-phonon line quantities: renormalized Huang-Rhys factor (absorption and luminescence), Stokes shift, and quadratic-coupling linewidth/shift for b ∈ {-0.2, 0, 0.16} and T/ω_top ∈ {0, 0.1, 0.5} in the Debye-Van Hove model."
    }
  ],
  "notes": "All quantities computed using the Debye-Van Hove model with top phonon frequency = 1 and linear coupling a = 1. The integrals require careful handling of the ω→0 singularity. No external data beyond the model equations is needed."
}
```

## How you are scored
A hidden verifier independently implements the same Debye-Van Hove model and evaluates the same integrals for each (b,T) pair using its own numerical integration. It compares your reported values to its reference values. The comparison is performed with a relative tolerance (or absolute tolerance for numbers near zero). The verifier assigns a reward for the scored artifact, with the final score being a weighted combination of the individual checks. Simply reporting the expected numbers without performing the computation is not sufficient; the submitted JSON must be produced by the described computational procedure.
