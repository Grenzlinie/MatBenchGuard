# Plasticity Model Simulation: Stepwise Tension-Torsion Stress Trend Verification

## Problem background
Classical plasticity often assumes that the plastic strain rate is proportional to the gradient of the yield function (the normality rule). This rule works well for proportional loading but can give poor predictions when the loading path changes abruptly, such as in bifurcation problems or in stepwise non-proportional experiments like tension followed by torsion. A thermodynamically consistent extension adds a term proportional to the objective stress rate to the plastic strain rate. This generalized evolution law introduces an additional material parameter and aims to better capture the transient response after sudden path changes. The present task involves implementing such a generalized plasticity model and comparing its stress predictions to those of the classical normality rule for two non-proportional loading histories on a ductile steel.

## Approach
The constitutive model consists of an elastic hypo-elastic law (using shear and bulk moduli), an isotropic hardening yield condition, evolution laws for the internal variables (a scalar hardening variable and a tensorial back-stress), and a plastic strain rate that can include a stress-rate term. Two variants are considered: the classical normality rule (no stress-rate term) and the generalized law where the plastic strain rate also contains a term proportional to the Jaumann rate of the stress deviator, scaled by a coefficient κ. The material constants for a steel (grade CK15) are provided: shear modulus, initial yield stress, hardening parameters, and the value of κ for the generalized model.

The model is used to simulate two strain-controlled stepwise loading histories:
1. Tension-first: an axial tension is applied until a prescribed plastic strain is reached; then, while holding the axial strain constant, a monotonic shear strain is applied.
2. Torsion-first: a pure shear is applied until a similar plastic shear strain is reached; then, while holding the shear strain constant, an axial tension is applied.

For each history and each model variant, the axial stress and shear stress are recorded at the end of the first loading leg (step 1) and at the end of the second loading leg (step 2). The results are saved in a structured JSON file for verification.

## Reproduction target
Produce a JSON file containing the computed axial stress (σ_zz) and shear stress (τ_θz) at the end of step 1 and step 2 for both loading histories and for both the normality-rule and generalized-law variants. The file must follow a strict schema: top-level keys `loading_history_1` (tension first) and `loading_history_2` (torsion first), each containing objects `normality` and `generalized`, which in turn contain `step_1_stresses` and `step_2_stresses`, each with numeric fields `sigma_zz` and `tau_theta_z` (in N/mm²). The exact strain endpoints may be chosen within a reasonable range (e.g., plastic strains around 2%), but the stress values will be checked for consistency and for specific relative trends between the two model variants.

## Assets

- Python numerical computation stack (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Simulate stepwise tension-torsion loading histories
- Role: scored (load-bearing)
- Action: Implement the thermo-mechanical constitutive model for isotropic plastic flow consisting of: (a) elastic hypo-elastic law with shear modulus G and bulk modulus K, (b) isotropic hardening yield condition F=0, (c) evolution laws for internal variables (scalar hardening variable and tensorial back-stress), and (d) plastic strain rate: dᵢⱼ⁽ⁱⁱ⁾ = λ̇ ∂F/∂σᵢⱼ + κ tᵢⱼ|₀ , where tᵢⱼ is the stress deviator and the objective rate is Zaremba-Jaumann. Use material constants for steel CK15: G = 81000 N/mm², k₀ = 130.5 N/mm², hardening parameters a=1.15, d=1.72×10⁻⁴, n=0.435, and κ = 3.2/(2G) for the generalized model; κ = 0 for normality. Simulate two strain-controlled loading paths: (1) Tension-first: apply axial tension until a significant plastic strain (e.g., around 2% plastic strain or up to σ_zz ≈ 350 MPa), then, while holding axial strain constant, apply monotonic shear strain up to a similar magnitude. (2) Torsion-first: apply pure shear until a similar magnitude of shear strain, then, while holding shear strain constant, apply axial tension. For each path, compute the axial stress σ_zz and shear stress τ_θz at the end of the first loading leg (step_1_stresses) and at the end of the second loading leg (step_2_stresses), for both the normality case and the generalized law case. Write the collected values to stress_values.json.
- Output file: `/app/outputs/stress_values.json`
- Format: json
- Contract: A JSON object with two top-level keys: `loading_history_1` (tension first) and `loading_history_2` (torsion first). Each value is an object with keys `normality` and `generalized`. Each model entry is an object with keys `step_1_stresses` and `step_2_stresses`. Each stress object has fields `sigma_zz` (axial stress in N/mm²) and `tau_theta_z` (shear stress in N/mm²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_values.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_values.json
- path: `/app/outputs/stress_values.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Stress values at the end of each loading leg for the two loading histories and two model variants.
- schema:
  - `$defs`:
    - `stress_point`:
      - `type`: object
      - `required`: `sigma_zz`, `tau_theta_z`
    - `step_pair`:
      - `type`: object
      - `required`: `step_1_stresses`, `step_2_stresses`
      - `properties`:
        - `step_1_stresses`:
          - `$ref`: #/$defs/stress_point
        - `step_2_stresses`:
          - `$ref`: #/$defs/stress_point
    - `model_pair`:
      - `type`: object
      - `required`: `normality`, `generalized`
      - `properties`:
        - `normality`:
          - `$ref`: #/$defs/step_pair
        - `generalized`:
          - `$ref`: #/$defs/step_pair
  - `type`: object
  - `required`: `loading_history_1`, `loading_history_2`
  - `properties`:
    - `loading_history_1`:
      - `$ref`: #/$defs/model_pair
    - `loading_history_2`:
      - `$ref`: #/$defs/model_pair

Notes: The checker performs a structural audit: for each loading history, shear stress at step 2 must be lower for the generalized law than for normality; the axial stress difference between models must follow the correct sign (tension-first: generalized axial stress lower; torsion-first: generalized axial stress higher). All stress values must be positive and within a plausible range.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_values.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "$defs": {
          "stress_point": {
            "type": "object",
            "required": [
              "sigma_zz",
              "tau_theta_z"
            ]
          },
          "step_pair": {
            "type": "object",
            "required": [
              "step_1_stresses",
              "step_2_stresses"
            ],
            "properties": {
              "step_1_stresses": {
                "$ref": "#/$defs/stress_point"
              },
              "step_2_stresses": {
                "$ref": "#/$defs/stress_point"
              }
            }
          },
          "model_pair": {
            "type": "object",
            "required": [
              "normality",
              "generalized"
            ],
            "properties": {
              "normality": {
                "$ref": "#/$defs/step_pair"
              },
              "generalized": {
                "$ref": "#/$defs/step_pair"
              }
            }
          }
        },
        "type": "object",
        "required": [
          "loading_history_1",
          "loading_history_2"
        ],
        "properties": {
          "loading_history_1": {
            "$ref": "#/$defs/model_pair"
          },
          "loading_history_2": {
            "$ref": "#/$defs/model_pair"
          }
        }
      },
      "description": "Stress values at the end of each loading leg for the two loading histories and two model variants."
    }
  ],
  "notes": "The checker performs a structural audit: for each loading history, shear stress at step 2 must be lower for the generalized law than for normality; the axial stress difference between models must follow the correct sign (tension-first: generalized axial stress lower; torsion-first: generalized axial stress higher). All stress values must be positive and within a plausible range."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that inspects the uploaded `stress_values.json`. The verifier checks that the file conforms to the schema and that all stress values are positive and physically plausible. The main scoring criteria are relative trends between the two model variants at each loading step: the generalized law must produce a different pattern of axial and shear stresses compared to the normality rule — a pattern that only a correct implementation of the generalized flow rule can reproduce. Do not attempt to guess or hardcode the expected sign or magnitude; the verifier can detect fabricated data. Each trend and each validity check contributes a weight toward a final reward in [0, 1].
