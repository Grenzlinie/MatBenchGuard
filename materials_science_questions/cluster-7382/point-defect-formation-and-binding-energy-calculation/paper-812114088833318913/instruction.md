# Compute vacancy interaction parameters for condensed rare gases via analytical model

## Problem background
Excited states of a bulk system of bound atoms with pair interaction can be modeled as a gas of interacting vacancies. In this model, the liquid state arises when there is a significant vacancy fraction. The energy of vacancy formation depends on an interaction potential V(v/n) and the statistical weight g(v) of vacancies. This task uses a statistical model with specified functional forms for V(v/n) and g(v), together with experimental data for condensed rare gases, to determine the vacancy interaction parameters that characterize the liquid state. The raw reduced parameters (T_m/D, ΔH_fus/D, ε0/D) for Ne, Ar, Kr, Xe are: Ne: 0.583, 0.955, 6.1; Ar: 0.585, 0.990, 6.5; Kr: 0.576, 0.980, 6.5; Xe: 0.570, 0.977, 6.4. From these, the arithmetic mean yields the average input parameters. The goal is to reproduce the set of derived vacancy parameters (vacancy fraction, interaction potential, statistical weight parameters) for a range of assumed interaction shapes parameterized by an integer k.

## Approach
Consider a system of n atoms and v vacancies. The partition function of the vacancy gas leads to an entropy function S(v) that exhibits two maxima: a solid-state maximum at small v (where vacancy interactions are neglected) and a liquid-state maximum at larger v driven by vacancy interactions. At the melting temperature T_m, the equality of entropies of the solid and liquid states gives a relation connecting the liquid-state vacancy fraction (v_liq/n), the statistical weight g, and the fusion enthalpy ΔH_fus.

The vacancy interaction potential is assumed to have the form V(v/n) = C[exp(-α n/v) - exp(-k α n/v)], and the statistical weight is g(v) = 1 + a v/n with a ≫ 1. From the conditions that S(v) has a minimum between the solid and liquid maxima and a maximum at v_liq, together with the property that the derivative of vV vanishes at the liquid maximum, one obtains a set of algebraic equations. The solution proceeds as follows:
1. Compute x_liq = ln(k) / (k-1).
2. Set the minimum vacancy volume fraction to v_min = n/12. Using the equality F(v_min) = F(v_liq), where F = d(vV)/dv, solve for the parameter α and the ratio n/v_liq.
3. Determine the interaction potential at the liquid state: V(v_liq/n) = ε0 - (ΔH_fus / T_m) · (n/v_liq).
4. Back-solve for the coefficient C from the potential form at v_liq.
5. Obtain the statistical weight parameter a from V(v_liq/n) = T_m (1 + ln a).
6. Compute g(v_liq) = 1 + a · (v_liq/n).
7. Evaluate the auxiliary quantities F(x_liq) = d(vV)/dv at v_liq (expressed in terms of x = α n/v) and x_min = 12 α.

This procedure is carried out independently for each integer k = 2, 3, 6, 10, using the experimental average input parameters T_m/D, ΔH_fus/D, ε0/D computed in Step 1.

## Reproduction target
Compute the vacancy interaction parameters (x_liq, F_x_liq, x_min, α, n/v_liq, V(v_liq/n), a, g(v_liq), C) for condensed rare gases for integer parameters k = 2, 3, 6, 10, using the experimental average input parameters T_m/D = 0.578, ΔH_fus/D = 0.98, ε0/D = 6.35 obtained from averaging the provided individual gas data. The result must be saved as an array of objects in `/app/outputs/table_ii.json`, with one object per k value containing the fields: k (int), x_liq, F_x_liq, x_min, alpha, n_over_v_liq, V_v_liq_n, a, g_v_liq, C (all floats, dimensionless or in units of D).

## Assets
No external assets are required. All necessary experimental data (the raw reduced parameters for Ne, Ar, Kr, Xe) are provided in the problem background above. Standard scientific Python libraries (e.g., numpy, scipy) may be used for the numerical computation.

## Workflow steps

### Step 1: Compute average experimental parameters
- Role: process
- Action: Given the published reduced parameters (T_m/D, ΔH_fus/D, ε0/D) for Ne, Ar, Kr, Xe, compute their arithmetic means to obtain the experimental average input parameters.
- Evidence: `/app/outputs/average_parameters.json`

### Step 2: Compute vacancy interaction parameters
- Role: scored (load-bearing)
- Action: Using the average parameters from Step 1 and assuming the vacancy interaction potential V(v/n)=C[exp(-α n/v)-exp(-k α n/v)] and statistical weight g(v)=1 + a v/n, solve the model equations to determine x_liq, F_x_liq, x_min, α, n/v_liq, V(v_liq/n), a, g(v_liq), C for integer parameters k = 2, 3, 6, 10.
- Output file: `/app/outputs/table_ii.json`
- Format: json
- Contract: Array of objects with fields: k (int), x_liq (float), F_x_liq (float), x_min (float), alpha (float), n_over_v_liq (float), V_v_liq_n (float), a (float), g_v_liq (float), C (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table_ii.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table_ii.json
- path: `/app/outputs/table_ii.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Table II parameters from the paper. The checker recomputes the expected values from the same average input parameters and the analytical model, then compares each agent-provided value within a relative tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `k`, `x_liq`, `F_x_liq`, `x_min`, `alpha`, `n_over_v_liq`, `V_v_liq_n`, `a`, `g_v_liq`, `C`
    - `properties`:
      - `k`:
        - `type`: integer
      - `x_liq`:
        - `type`: number
        - `description`: dimensionless
      - `F_x_liq`:
        - `type`: number
        - `description`: dimensionless
      - `x_min`:
        - `type`: number
        - `description`: dimensionless
      - `alpha`:
        - `type`: number
        - `description`: dimensionless
      - `n_over_v_liq`:
        - `type`: number
        - `description`: dimensionless
      - `V_v_liq_n`:
        - `type`: number
        - `description`: units of D
      - `a`:
        - `type`: number
        - `description`: dimensionless
      - `g_v_liq`:
        - `type`: number
        - `description`: dimensionless
      - `C`:
        - `type`: number
        - `description`: units of D

Notes: The checker recomputes the parameters from the average inputs T_m/D=0.578, ΔH_fus/D=0.98, ε0/D=6.35 and the same equations; it scores each parameter with a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table_ii.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "k",
            "x_liq",
            "F_x_liq",
            "x_min",
            "alpha",
            "n_over_v_liq",
            "V_v_liq_n",
            "a",
            "g_v_liq",
            "C"
          ],
          "properties": {
            "k": {
              "type": "integer"
            },
            "x_liq": {
              "type": "number",
              "description": "dimensionless"
            },
            "F_x_liq": {
              "type": "number",
              "description": "dimensionless"
            },
            "x_min": {
              "type": "number",
              "description": "dimensionless"
            },
            "alpha": {
              "type": "number",
              "description": "dimensionless"
            },
            "n_over_v_liq": {
              "type": "number",
              "description": "dimensionless"
            },
            "V_v_liq_n": {
              "type": "number",
              "description": "units of D"
            },
            "a": {
              "type": "number",
              "description": "dimensionless"
            },
            "g_v_liq": {
              "type": "number",
              "description": "dimensionless"
            },
            "C": {
              "type": "number",
              "description": "units of D"
            }
          }
        }
      },
      "description": "Table II parameters from the paper. The checker recomputes the expected values from the same average input parameters and the analytical model, then compares each agent-provided value within a relative tolerance."
    }
  ],
  "notes": "The checker recomputes the parameters from the average inputs T_m/D=0.578, ΔH_fus/D=0.98, ε0/D=6.35 and the same equations; it scores each parameter with a relative tolerance."
}
```

## How you are scored
A hidden verifier independently recomputes the expected vacancy interaction parameters from the same experimental average input parameters and the same model equations. It compares each numeric value in your `/app/outputs/table_ii.json` against the recomputed gold values using a relative tolerance (and an absolute tolerance for very small values). The score is based entirely on the accuracy of the computed parameters in this file; weights are distributed across the fields. Simply reporting numbers from the literature without performing the computational steps will not pass, because the verifier recomputes and compares, not checks against pre‑stored constants.
