# Grüneisen Parameter and Volume Derivative Calculation

## Problem background
The superconductor La₃S₄ has a transition temperature Tc of ~8.1 K and shows an anomalous increase of Tc under hydrostatic pressure. Thermal expansion measurements yield the pressure derivative of Tc and various Grüneisen parameters that describe the volume dependence of electronic and phononic properties. To understand why Tc increases with pressure, the pressure dependence of the electron‑phonon coupling λ, the Coulomb pseudopotential μ*, the McMillan–Hopfield parameter η, and the electron‑phonon matrix element ⟨I²⟩ need to be disentangled. The key computational step is solving a coupled system of volume‑derivative relations that provides the logarithmic volume derivatives of these quantities.

## Approach
The approach follows the differentiated McMillan analysis from the literature. Starting from the given numerical parameters: d ln Tc / d ln V, γ_G (300 K), γ_e, λ, μ*, and the Fermi energy E_F, the task implements the algebraic relations that link these to the unknown volume derivatives. By expressing the volume derivative of μ* in terms of the bare electronic Grüneisen parameter γ_e⁺ and the known parameters, and relating the bare and enhanced electronic Grüneisen parameters through the derivative of λ, a closed system is obtained. Solving this system yields d ln λ / d ln V, γ_e⁺, d ln μ* / d ln V, d ln η / d ln V, and d ln ⟨I²⟩ / d ln V. The computation is a purely algebraic substitution, requiring only arithmetic and basic algebra, with no numerical solvers. The results are produced in a single JSON file.

## Reproduction target
Given the following input parameter values:
- d ln Tc / d ln V = -13.4
- γ_G(300 K) = 2
- γ_e = -2.5
- λ = 0.77
- μ* = 0.10
- E_F = 28900 K

Implement the system of volume‑derivative relations and compute the five quantities above. Write them to `/app/outputs/derived_volume_derivatives.json` as a JSON object with numeric fields: `dln_lambda_dlnV`, `gamma_e_plus`, `dln_muplus_dlnV`, `dln_eta_dlnV`, `dln_I2_dlnV`.

## Assets
No external datasets or pre‑trained models are required. The task uses standard Python numerical libraries: `numpy`. The solving agent may install these on the fly (e.g. via `python3 -m pip install -q numpy`).

## Workflow steps

### Step 1: Compute the five volume-derivative quantities
- Role: scored (load-bearing)
- Action: Implement the system of algebraic equations from the paper's differentiated McMillan analysis using the provided input parameters to compute d ln λ/d ln V, γ_e^+, d ln μ^+/d ln V, d ln η/d ln V, and d ln ⟨I²⟩/d ln V. Write the results to the output JSON file.
- Output file: `/app/outputs/derived_volume_derivatives.json`
- Format: json
- Contract: JSON object with numeric fields: dln_lambda_dlnV, gamma_e_plus, dln_muplus_dlnV, dln_eta_dlnV, dln_I2_dlnV
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/derived_volume_derivatives.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### derived_volume_derivatives.json
- path: `/app/outputs/derived_volume_derivatives.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed volume-derivative parameters from the differentiated McMillan analysis.
- schema:
  - `type`: object
  - `required`: `dln_lambda_dlnV`, `gamma_e_plus`, `dln_muplus_dlnV`, `dln_eta_dlnV`, `dln_I2_dlnV`
  - `additionalProperties`: False
  - `properties`:
    - `dln_lambda_dlnV`:
      - `type`: number
    - `gamma_e_plus`:
      - `type`: number
    - `dln_muplus_dlnV`:
      - `type`: number
    - `dln_eta_dlnV`:
      - `type`: number
    - `dln_I2_dlnV`:
      - `type`: number

Notes: The checker independently recomputes the five values from the same input parameters and compares each within an absolute tolerance. The task requires implementation of the algebraic equations as described in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "derived_volume_derivatives.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "dln_lambda_dlnV",
          "gamma_e_plus",
          "dln_muplus_dlnV",
          "dln_eta_dlnV",
          "dln_I2_dlnV"
        ],
        "additionalProperties": false,
        "properties": {
          "dln_lambda_dlnV": {
            "type": "number"
          },
          "gamma_e_plus": {
            "type": "number"
          },
          "dln_muplus_dlnV": {
            "type": "number"
          },
          "dln_eta_dlnV": {
            "type": "number"
          },
          "dln_I2_dlnV": {
            "type": "number"
          }
        }
      },
      "description": "Computed volume-derivative parameters from the differentiated McMillan analysis."
    }
  ],
  "notes": "The checker independently recomputes the five values from the same input parameters and compares each within an absolute tolerance. The task requires implementation of the algebraic equations as described in the paper."
}
```

## How you are scored
A hidden verifier independently recomputes the same five quantities from the same input parameters. It reads your JSON file and compares each value against the recomputed reference. Each comparison is made with an absolute tolerance (the tolerance is not disclosed). Your final score is the fraction of values that fall within tolerance, weighted to emphasise the quantities directly derived from the McMillan equation. The verifier does not inspect your code or intermediate steps; only the numerical contents of the JSON file matter.
