# Quantitative Software Process Risk and Trustworthiness Simulation

## Problem background
Software trustworthiness depends on the quality of the development process and on effective risk management. A quantitative framework has been proposed to measure process risk and resulting trustworthiness. The model relates risk occurrence probabilities inversely to CMMI maturity, risk identification and control effectiveness to schedule time and cost, and quality trustworthiness similarly. Overall trustworthiness is the difference between quality effectiveness and aggregated process risk. This task implements the model and uses Monte Carlo simulation to explore how average trustworthiness varies with CMMI level and with risk management input (schedule time).

## Approach
The model covers five lifecycle processes (Acquisition, Supply, Development, Maintenance, Operation) and six risk categories (Requirements, Project Management, User, Development, Developer, Environment). Binary risk events occur per process and category with probability inversely proportional to the CMMI level, scaled by empirical coefficients S_ij. Each risk category has an impact weight I_i. Between consecutive processes, risk propagates via a transition matrix; the standard matrix TR_2 (6x6) is used for all transitions. Risk identification effectiveness (RI) and risk control effectiveness (RC) are modeled as sigmoid functions:
  RI = 2/(1+exp(-CMMI * T^α * C^β)) - 1
  RC = 2/(1+exp(-CMMI * T^ζ * C^ξ)) - 1
where T is schedule time, C is cost, and α,β,ζ,ξ are elasticity parameters. Quality trustworthiness T_Quality is modeled similarly as a sigmoid:
  T_Quality = 2/(1+exp(-CMMI * Sch^a * Cost^b)) - 1
Total risk R_total is computed by applying the transition matrix and effectiveness factors to the risk vectors across processes. Final trustworthiness T = T_Quality - R_total.

For this task, use the following fixed parameters: all S_ij = 1; risk impacts I_i = [5,4,3,2,1,1] for the six categories in the order above; all elasticities α=β=ζ=ξ=1; cost C=1; and the quality elasticities a=b=1. Use the published TR_2 matrix as defined in the literature (a 6x6 matrix with specific constants). Simulate Monte Carlo trials:
  (a) Fix T=1, C=1. For CMMI levels 1 through 5, run 1000 trials each. Each trial draws independent binary risk occurrences with probability P_ij = S_ij / CMMI, computes R_ij = P_ij * I_i, propagates risk through the five processes using the transition matrix and effectiveness formulas, and computes T. Average the trustworthiness over the 1000 trials.
  (b) Fix CMMI=3, C=1. Vary schedule time T from 0.5 to 3.0 in steps of 0.5 (6 values). For each T run 1000 trials and average T.

Output the results in the required JSON structure.

## Reproduction target
Produce one file `/app/outputs/trustworthiness_results.json` with two arrays:
- `cmmi_trend`: list of objects, each with `cmmi_level` (integer 1..5) and `avg_trustworthiness` (float).
- `risk_input_trend`: list of objects, each with `schedule_time` (float, 0.5 to 3.0 in steps of 0.5) and `avg_trustworthiness` (float).

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Run Monte Carlo simulation and produce trustworthiness trend data
- Role: scored (load-bearing)
- Action: Implement the risk measurement model using the given risk transition matrix TR_2 (apply for all process transitions), risk impact matrix from Table I, and default parameters: S_ij=1 for all i,j; I_i = [5,4,3,2,1,1] for the six risk categories (Requirements, Project Management, User, Development, Developer, Environment); elasticities α=β=ζ=ξ=1; cost C=1. For CMMI levels 1 to 5, run 1000 Monte Carlo trials each: generate binary risk occurrences using P_ij = S_ij / CMMI, compute total risk and trustworthiness, and average. For CMMI=3, vary schedule time T from 0.5 to 3.0 in steps of 0.5 (1000 trials each) and average trustworthiness. Output the results as a JSON file with 'cmmi_trend' and 'risk_input_trend' lists.
- Output file: `/app/outputs/trustworthiness_results.json`
- Format: json
- Contract: JSON object with keys 'cmmi_trend' (list of objects each with integer 'cmmi_level' and float 'avg_trustworthiness') and 'risk_input_trend' (list of objects each with float 'schedule_time' and float 'avg_trustworthiness').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/trustworthiness_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### trustworthiness_results.json
- path: `/app/outputs/trustworthiness_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Output of the Monte Carlo simulation: cmmi_trend shows average trustworthiness per CMMI level (1-5), risk_input_trend shows average trustworthiness for varying schedule time at CMMI=3. The checker will verify structural properties (monotonicity and diminishing returns) of the data.
- schema:
  - `type`: object
  - `required`: `cmmi_trend`, `risk_input_trend`
  - `items`:
    - `cmmi_trend`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `cmmi_level`, `avg_trustworthiness`
        - `properties`:
          - `cmmi_level`:
            - `type`: integer
          - `avg_trustworthiness`:
            - `type`: number
    - `risk_input_trend`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `schedule_time`, `avg_trustworthiness`
        - `properties`:
          - `schedule_time`:
            - `type`: number
          - `avg_trustworthiness`:
            - `type`: number

Notes: The simulation parameters (S_ij=1, I_i values, elasticities, TR_2 matrix, etc.) are specified in the instruction and must be used by the solver. The checker does not compare to exact reference values but evaluates whether the output trends satisfy the model's expected structural relationships.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "trustworthiness_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "cmmi_trend",
          "risk_input_trend"
        ],
        "items": {
          "cmmi_trend": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "cmmi_level",
                "avg_trustworthiness"
              ],
              "properties": {
                "cmmi_level": {
                  "type": "integer"
                },
                "avg_trustworthiness": {
                  "type": "number"
                }
              }
            }
          },
          "risk_input_trend": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "schedule_time",
                "avg_trustworthiness"
              ],
              "properties": {
                "schedule_time": {
                  "type": "number"
                },
                "avg_trustworthiness": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Output of the Monte Carlo simulation: cmmi_trend shows average trustworthiness per CMMI level (1-5), risk_input_trend shows average trustworthiness for varying schedule time at CMMI=3. The checker will verify structural properties (monotonicity and diminishing returns) of the data."
    }
  ],
  "notes": "The simulation parameters (S_ij=1, I_i values, elasticities, TR_2 matrix, etc.) are specified in the instruction and must be used by the solver. The checker does not compare to exact reference values but evaluates whether the output trends satisfy the model's expected structural relationships."
}
```

## How you are scored
A hidden verifier will inspect `trustworthiness_results.json`. It will verify structural properties of your computed trends:
- For `cmmi_trend`, it will check that average trustworthiness strictly increases with CMMI level (with a small tolerance for Monte Carlo noise).
- For `risk_input_trend`, it will check that average trustworthiness increases with schedule time and that the increases themselves become smaller (diminishing returns).
- It will also check that all trustworthiness values lie within a plausible numeric range (approximately -1 to 1).

The final reward is a weighted sum of scores from these structural checks. You are not required to match any specific numeric result from the literature; correct implementation of the model as described will yield the expected qualitative behavior.
