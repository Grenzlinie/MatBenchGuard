# Single-point activation energy from criticality data

## Problem background
Spontaneous combustion of solid substrates like coal can be modelled using the Frank–Kamenetskii (F-K) theory of thermal ignition. Determining the activation energy \(E\) of the oxidation reaction normally requires measuring critical ambient temperatures for several sample sizes and performing a multi-point data fit. This work presents a method to extract \(E\) from a single criticality data point, thereby simplifying the experimental procedure. The method derives a closed-form expression that combines the F-K criticality condition with a local heat-balance relation, eliminating the need for multi-point experiments. The goal of this task is to apply that single-point formula to two bituminous coals to compute their activation energies.

## Approach
The idea is to combine two relations that hold at the critical ignition point: (1) the Frank–Kamenetskii criticality condition, and (2) a local heat‑balance equation that links the heat release rate to the measured temperature‑rise rate \([dT/dt]_o\) when the sample temperature reaches the oven temperature. Eliminating the exothermicity and pre‑exponential factor yields an expression for \(E\) that depends only on the sample geometry (\(r_o\)), the critical ambient temperature \((T_o)_{crit}\), the bulk density \(\sigma\), the thermal conductivity \(k\), the heat capacity \(c\), and the measured heating rate \([dT/dt]_o\). In this task you will use that expression with the common constants given in the step and the coal‑specific values for Rosslynlee and Dalquhandy coals to compute the activation energy for each coal.

## Reproduction target
Produce a JSON file named `activation_energies.json` containing the activation energy (kJ/mol) for Rosslynlee coal under the key `"Rosslynlee"` and for Dalquhandy coal under the key `"Dalquhandy"`, computed using the formula and data provided in Step 1.

## Assets
No external resources are required. All necessary constants and coal-specific data are supplied in the instruction. You only need a Python environment with the ability to write JSON (the standard library suffices).

## Workflow steps

### Step 1: Compute activation energies
- Role: scored (load-bearing)
- Action: Apply the formula derived from the Frank-Kamenetskii criticality condition and local heat-balance relation: E = δ_crit * ((T_o_crit)/r_o)^2 * (k R) / (σ c [dT/dt]_o) with δ_crit=2.57, r_o=0.05 m, R=8.314 J/(K·mol), k=0.143 W/(m·K), c=1260 J/(kg·K). Convert [dT/dt]_o from K/h to K/s. Use the coal-specific values: for Rosslynlee, T_o_crit=357 K, [dT/dt]_o=9 K/h (2.5e-3 K/s), σ=745 kg/m³; for Dalquhandy, T_o_crit=372.5 K, [dT/dt]_o=13.5 K/h (3.75e-3 K/s), σ=530 kg/m³. Compute E for both coals and save as a JSON object with keys 'Rosslynlee' and 'Dalquhandy' (values in kJ/mol).
- Output file: `/app/outputs/activation_energies.json`
- Format: json
- Contract: JSON object with top-level keys 'Rosslynlee' and 'Dalquhandy', each a float value in kJ/mol.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activation_energies.json
- path: `/app/outputs/activation_energies.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed activation energies for both coals from the single-point formula.
- schema:
  - `type`: object
  - `required`:
    - `Rosslynlee`: float (kJ/mol)
    - `Dalquhandy`: float (kJ/mol)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "Rosslynlee": "float (kJ/mol)",
          "Dalquhandy": "float (kJ/mol)"
        }
      },
      "description": "Computed activation energies for both coals from the single-point formula."
    }
  ],
  "notes": ""
}
```

## How you are scored
The hidden verifier independently recomputes the activation energies using the same formula and the true (hidden) critical parameters. It compares your submitted values to the expected results within an undisclosed tolerance. Each coal's activation energy contributes equally to the final reward; the better the agreement, the higher the score. The verifier does not require you to reproduce any external paper or verify against a published table.
