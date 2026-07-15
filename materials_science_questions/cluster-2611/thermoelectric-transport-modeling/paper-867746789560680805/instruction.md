# Thermoelectric Transport Modeling: Giant Magneto-Seebeck Effect

## Problem background
Giant magneto-Seebeck (GMS) effect refers to the large change in Seebeck coefficient of a spin valve when switching between parallel (P) and antiparallel (AP) magnetic states. In Co/Cu/Co spin valves, a generalized Mott two-spin-channel model for diffusive thermoelectric transport provides a theoretical prediction for the GMS ratio. This model relates the GMS to the spin polarization of conductivity and thermoelectric conductivity in the ferromagnetic layers. Your task is to compute the theoretical GMS ratio for a symmetric Co/Cu/Co structure using this model.

## Approach
We consider a symmetric spin valve with two identical ferromagnetic (Co) layers separated by a nonmagnetic (Cu) spacer. Assuming spin relaxation in Cu is negligible, the Mott two-spin-channel model is extended to thermoelectric transport, yielding an expression for the GMS ratio that depends only on two spin-polarization parameters: P_sigma (polarization of electrical conductivity) and P_alpha (polarization of thermoelectric conductivity). The model is evaluated in the symmetric case where both Co layers have the same transport properties. Literature values for P_sigma and P_alpha are used as input; they are specified in the workflow step below. No additional experimental data or measurements are required.

## Reproduction target
Compute the giant magneto-Seebeck (GMS) ratio for the symmetric Co/Cu/Co spin valve using the supplied model and polarization values. Express the result as a percentage and write it to the output file `theoretical_gms.json` under the key `GMS_percent`.

## Assets

- Python standard library: python3

## Workflow steps

### Step 1: Compute theoretical GMS
- Role: scored
- Action: Implement the symmetric two-layer giant magneto-Seebeck (GMS) formula: GMS = (P_sigma^2 - P_alpha^2) / (1 - P_sigma^2) using the spin polarization values P_sigma = 0.4 (conductivity) and P_alpha = 0.5 (thermoelectric conductivity). Express the result as a percentage (multiply by 100). Write the percentage value to a JSON file.
- Output file: `/app/outputs/theoretical_gms.json`
- Format: json
- Contract: { "GMS_percent": <float> }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/theoretical_gms.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### theoretical_gms.json
- path: `/app/outputs/theoretical_gms.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The theoretical giant magneto-Seebeck ratio for the Co/Cu/Co spin valve computed from the symmetric two-layer model, expressed as a percentage.
- schema:
  - `type`: object
  - `required`:
    - `GMS_percent`: float
  - `units`:
    - `GMS_percent`: percent

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "theoretical_gms.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "GMS_percent": "float"
        },
        "units": {
          "GMS_percent": "percent"
        }
      },
      "description": "The theoretical giant magneto-Seebeck ratio for the Co/Cu/Co spin valve computed from the symmetric two-layer model, expressed as a percentage."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is automatically scored by a hidden verifier. For the scored artifact `theoretical_gms.json`, the verifier independently recomputes the expected GMS percentage using the same formula and polarization values you were given. It then compares your `GMS_percent` to the expected value and awards a reward between 0 and 1 based on the closeness of your result. The tolerance used for comparison is hidden; to score well you must implement and run the actual computation. Simply reporting a known number without executing the workflow will not pass the verifier.
