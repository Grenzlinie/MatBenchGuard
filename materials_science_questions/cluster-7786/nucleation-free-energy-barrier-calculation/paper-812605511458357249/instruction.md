# Nucleation Free-Energy Barrier Calculation for Ionic Bridge Formation

## Problem background
Crystallization in supersaturated solutions often involves the attachment of particles to crystal surfaces. When two crystal faces are separated by a narrow gap, a capillary-condensation effect can lead to the formation of an ionic bridge — a cylindrical new phase that connects the surfaces. Understanding the thermodynamic barrier for this bridge formation is key to predicting whether attachment is more favorable than homogeneous nucleation in the bulk solution. The central question is: what is the critical radius and free‑energy barrier for such a bridge, expressed as scaling factors relative to the homogeneous nucleation case, and under what geometric condition does bridge nucleation become more favorable than homogeneous or planar heterogeneous nucleation?

## Approach
Treat the ionic bridge as a cylinder of radius r confined between two parallel flat crystal faces separated by a gap H. Define the dimensionless specific height h = H/r. The bridge has volume V_b = π r³ h and side‑wall area S_bs = 2π r² h; the crystal–bridge contact areas contribute zero interfacial term when the contact angle is 90° (m = 0). The free energy change for forming the bridge is ΔG = –(Δμ/Ω) V_b + S_bs γ_bs, where Δμ is the chemical potential driving force and γ_bs is the bridge–solution interfacial energy.

From classical nucleation theory, the homogeneous nucleation critical radius is r* = 2 γ_bs Ω / Δμ and the barrier is ΔG* = 16π γ_bs³ Ω² / (3 (Δμ)²). By setting ∂ΔG/∂r = 0, derive the bridge critical radius r*_bridge and barrier ΔG*_bridge in the form r*_bridge = w · r* and ΔG*_bridge = f · ΔG*, where w and f are geometric prefactors that depend only on h.

Separately, the standard heterogeneous nucleation factor for a flat substrate with contact angle parameter m = cos θ is f_hetero = (1-m)²(2+m)/4. Evaluate this for m = 0 to obtain the planar heterogeneous barrier reduction. Finally, compare the bridge factor f with f_hetero to determine the condition on the specific gap h for which bridge nucleation is more favorable than homogeneous nucleation. All results are to be computed symbolically or numerically, with the final scaling factors and condition written to a JSON file.

## Reproduction target
Compute the geometric scaling factor w, the expression for the bridge barrier factor f in terms of h (e.g. as a string like "2*h/9"), the heterogeneous nucleation factor f_hetero for m=0, and the condition on h (as a string such as "h < 9/4") under which bridge nucleation is more favourable than homogeneous nucleation. Write all results to `/app/outputs/bridge_factors.json`.

## Assets
No external assets (datasets, models, tools) are required. The derivation can be performed using standard mathematical or symbolic libraries available in a typical Python environment (e.g. `sympy` or `numpy`).

## Workflow steps

### Step 1: Derive bridge nucleation factors
- Role: scored (load-bearing)
- Action: Using the free-energy expression ΔG = -(Δμ/Ω)V_b + S_bs γ_bs for a cylindrical ionic bridge with V_b = π r^3 h, S_bs = 2π r^2 h, where h = H/r, perform nucleation analysis: set ∂ΔG/∂r = 0, derive the critical radius r*_bridge and barrier ΔG*_bridge in terms of the homogeneous nucleation quantities r* and ΔG*. Obtain the scaling factors w and f. Then compute the standard heterogeneous nucleation factor f_hetero for m=0 using f = (1-m)^2(2+m)/4. Compare f and f_hetero to derive the condition on h for bridge nucleation to be more favorable than homogeneous nucleation. Write all results to bridge_factors.json.
- Output file: `/app/outputs/bridge_factors.json`
- Format: json
- Contract: {"w": number, "f_expression": string, "hetero_f_for_m0": number, "condition": string}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bridge_factors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bridge_factors.json
- path: `/app/outputs/bridge_factors.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Derived geometric scaling factors and capillary-gap condition from the nucleation model.
- schema:
  - `type`: object
  - `required`: `w`, `f_expression`, `hetero_f_for_m0`, `condition`
  - `items`:
    - `w`: number
    - `f_expression`: string
    - `hetero_f_for_m0`: number
    - `condition`: string

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bridge_factors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "w",
          "f_expression",
          "hetero_f_for_m0",
          "condition"
        ],
        "items": {
          "w": "number",
          "f_expression": "string",
          "hetero_f_for_m0": "number",
          "condition": "string"
        }
      },
      "description": "Derived geometric scaling factors and capillary-gap condition from the nucleation model."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently solves the same thermodynamic nucleation model for the cylindrical bridge geometry described above. It reads your `/app/outputs/bridge_factors.json` and compares each field — `w`, `f_expression`, `hetero_f_for_m0`, and `condition` — against the correct solution. The verifier weighs the fields and returns a total reward between 0 and 1. Your score reflects how well your derived geometric prefactors and condition match the expected results; simply writing a number without performing the required derivation will not pass the checks.
