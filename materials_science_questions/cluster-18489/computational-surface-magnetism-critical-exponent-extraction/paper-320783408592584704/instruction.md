# Numerical evaluation of universal bulk fluctuation magnetization scaling function

## Problem background
The paper investigates fluctuation-induced diamagnetism in dirty superconductors above the transition temperature. Fluctuations of the superconducting order parameter produce an additional diamagnetic response in strong magnetic fields far above Tc. The central theoretical result for bulk samples is that at the zero-field critical temperature T=Tc0, the suitably scaled magnetization πM/(e^{3/2} H^{1/2} Tc0) depends only on a reduced magnetic field h=H/H* through a universal scaling function f(h). This function cannot be expressed in closed form; it incorporates short-wavelength fluctuation effects beyond the Ginzburg-Landau theory and requires numerical evaluation. The task is to compute f(h) for several values of h by numerically evaluating the analytical expression derived in the paper.

## Approach
The scaling function is obtained from a diagrammatic calculation of the fluctuation-induced current using the Keldysh Green's function technique for dirty superconductors. The result is an integral-sum representation involving a sum over Landau levels and a double integral over scaled frequency and momentum, with the digamma function ψ appearing in the auxiliary functions. The derivation yields an expression that is exact within the model but can only be evaluated numerically. To reproduce the result, implement a numerical code in Python using numpy and scipy that truncates the Landau-level sum after sufficient terms for convergence and evaluates the double integral via numerical quadrature. Compute f(h) at the specified reduced field values. No external data or proprietary software is required; the computation is self-contained and deterministic.

## Reproduction target
Compute the values of the universal scaling function f(h) for the three reduced field values h = 0.1, 0.5, 1.0. Write the results as a JSON object with keys 'h_values' (the array of h) and 'f_values' (the corresponding computed f(h) values). The output file must be /app/outputs/step_01_scaling_function.json. The computation must be based solely on the analytical expression given in the workflow step, using numerical techniques of your choice.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Numerical evaluation of universal scaling function f(h)
- Role: scored (load-bearing)
- Action: Implement the numerical evaluation of the universal scaling function f(h) = h^{1/2} Σ_{n=1}^{∞} n ∬_{-∞}^{∞} (dρ dμ/(2π)^2) coth ρ Im[K_n(ρ,μ;h)] (∂^2/∂μ_0^2)[L_n^2(μ,μ_0;h) K_{n-1}(ρ,μ_0;h)]|_{μ_0=μ}, where K_n(ρ,μ;h) = [ψ(1/2 + μ^2 + (n+1/2)h - iρ/(2π)) - ψ(1/2)]^{-1}, L_n(μ,μ_0;h) = [ψ(1/2 + μ^2 + (n+1/2)h) - ψ(1/2 + μ_0^2 + (n-1/2)h)] / (μ^2 - μ_0^2 + h), with ψ the digamma function. Truncate the sum over n and perform the double integral numerically. Compute f(h) for h = 0.1, 0.5, 1.0. Write the results to the output file.
- Output file: `/app/outputs/step_01_scaling_function.json`
- Format: json
- Contract: {"type": "object", "properties": {"h_values": {"type": "array", "items": {"type": "number"}}, "f_values": {"type": "array", "items": {"type": "number"}}}, "required": ["h_values", "f_values"]}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_scaling_function.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_scaling_function.json
- path: `/app/outputs/step_01_scaling_function.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The numerical values of the universal scaling function f(h) for h=0.1, 0.5, 1.0.
- schema:
  - `type`: object
  - `required`: `h_values`, `f_values`
  - `properties`:
    - `h_values`:
      - `type`: array
      - `items`:
        - `type`: number
    - `f_values`:
      - `type`: array
      - `items`:
        - `type`: number

Notes: The hidden checker compares the reported f_values against a high-precision gold reference derived from independent numerical evaluation of the same formula, with a relative tolerance of approximately 1e-2. The agent must write results in the specified JSON schema.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_scaling_function.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "h_values",
          "f_values"
        ],
        "properties": {
          "h_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          },
          "f_values": {
            "type": "array",
            "items": {
              "type": "number"
            }
          }
        }
      },
      "description": "The numerical values of the universal scaling function f(h) for h=0.1, 0.5, 1.0."
    }
  ],
  "notes": "The hidden checker compares the reported f_values against a high-precision gold reference derived from independent numerical evaluation of the same formula, with a relative tolerance of approximately 1e-2. The agent must write results in the specified JSON schema."
}
```

## How you are scored
A hidden verifier will independently score your submitted artifact. It will compare each f(h) value you report to a high-precision gold reference obtained from an independent numerical evaluation of the same formula. The comparison will check correctness within a specified tolerance and will also verify that f(h) decreases monotonically with increasing h (a structural requirement). The reward is a weighted combination of the correctness scores for the three h values and the structural check, producing a final score in [0,1]. Reporting the correct numerical values is required to earn full credit; intermediate logs or evidence files (if any) are not scored.
