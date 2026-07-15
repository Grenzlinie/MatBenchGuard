# Infinite-N Bloch vector dynamics for central spin coupled to spin bath

## Problem background
We investigate the decoherence of a spin-1/2 central particle coupled to an interacting spin bath of many spin-1/2 particles in thermal equilibrium. The central spin is subject to a local magnetic field and couples to the bath via anisotropic Heisenberg interactions. The key quantity is the time-dependent reduced density matrix of the central spin, characterized by the Bloch vector components λ3(t) (longitudinal) and λ1(t) (transverse). In the thermodynamic limit of infinitely many bath spins and for the special case where the longitudinal coupling constant γ is zero, the dynamics can be described by analytic formulas. The goal is to compute these time-dependent Bloch vector components and extract features of decoherence, such as the asymptotic decoherence strength and the short-time decay time scale.

## Approach
The reproduction is compute‑driven. We implement the analytic infinite‑N limit derived for γ=0. The Bloch vector components λ3(t) and λ1(t) are expressed in terms of functions η(t), ζ(t), and ξ(t) that involve numerical integration or analytical forms using error functions and incomplete gamma functions. Using the specific parameter set α=1, g=1, β=5, Δ=0.5, μ=0.4, and initial conditions λ3(0)=0.5, λ1(0)=0.375, λ2(0)=0.375, we compute λ3(t) and λ1(t) at discrete time points t = 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0 (in units of 1/α). We also compute the asymptotic decoherence factor η^∞ and the short‑time decoherence time constant τ = sqrt((2+gβ)/α^2). The workflow is a single scored step that evaluates the formulas and writes a JSON output.

## Reproduction target
Produce a JSON file containing the time series of λ3(t) and λ1(t) at the specified time points, and the two derived constants η^∞ and τ. The output file `bloch_vector_results.json` must have keys `t`, `lambda3`, `lambda1`, `eta_inf`, and `tau` with the corresponding numeric values.

## Assets

- numpy and scipy: numpy scipy

## Workflow steps

### Step 1: Compute Bloch vector components and decoherence metrics
- Role: scored (load-bearing)
- Action: Implement the analytic formulas for the infinite-N, γ=0 case: compute the Bloch vector components λ3(t) and λ1(t) using the expressions involving numerical integration or the analytical forms (error/incomplete gamma functions). Use parameters α=1, g=1, β=5, Δ=0.5, μ=0.4, initial λ3(0)=0.5, λ1(0)=0.375, λ2(0)=0.375. Evaluate at times t = 0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0 (in units of 1/α). Also compute the asymptotic decoherence factor η^∞ and the short-time decoherence time constant τ = sqrt((2+gβ)/α^2). Output the results as a JSON file.
- Output file: `/app/outputs/bloch_vector_results.json`
- Format: json
- Contract: JSON object with keys: 't' (array of 9 floats, the time points), 'lambda3' (array of 9 floats, λ3(t)), 'lambda1' (array of 9 floats, λ1(t)), 'eta_inf' (float, asymptotic η^∞), 'tau' (float, decoherence time constant).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bloch_vector_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bloch_vector_results.json
- path: `/app/outputs/bloch_vector_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Agent-computed Bloch vector components and derived decoherence constants for the infinite-N limit at γ=0.
- schema:
  - `type`: object
  - `required`: `t`, `lambda3`, `lambda1`, `eta_inf`, `tau`
  - `properties`:
    - `t`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: 9 time points in units of 1/alpha
    - `lambda3`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: longitudinal Bloch vector component at each time
    - `lambda1`:
      - `type`: array
      - `items`:
        - `type`: number
      - `description`: transverse Bloch vector component at each time
    - `eta_inf`:
      - `type`: number
      - `description`: asymptotic decoherence factor
    - `tau`:
      - `type`: number
      - `description`: decoherence time constant in units of 1/alpha

Notes: Scoring compares the reported values to hidden gold values with absolute tolerances; tolerances are not revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bloch_vector_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "t",
          "lambda3",
          "lambda1",
          "eta_inf",
          "tau"
        ],
        "properties": {
          "t": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "9 time points in units of 1/alpha"
          },
          "lambda3": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "longitudinal Bloch vector component at each time"
          },
          "lambda1": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "description": "transverse Bloch vector component at each time"
          },
          "eta_inf": {
            "type": "number",
            "description": "asymptotic decoherence factor"
          },
          "tau": {
            "type": "number",
            "description": "decoherence time constant in units of 1/alpha"
          }
        }
      },
      "description": "Agent-computed Bloch vector components and derived decoherence constants for the infinite-N limit at γ=0."
    }
  ],
  "notes": "Scoring compares the reported values to hidden gold values with absolute tolerances; tolerances are not revealed here."
}
```

## How you are scored
A hidden verifier independently checks your submitted artifacts. Each scored workflow stage is assigned a weight; the final reward is a weighted combination. For this task, the verifier compares your computed values of λ3, λ1, η^∞, and τ against pre‑computed reference values (obtained from a high‑precision evaluation of the same formulas) using absolute tolerances. The tolerances are chosen to absorb legitimate implementation differences while detecting incorrect calculations. The verifier produces a reward between 0 (no match) and 1 (perfect match). Reporting numbers that look plausible is not enough; they must be correct within the hidden tolerances.
