# Dislocation Pinning Friction Stress and Hall-Petch Slope Calculation

## Problem background
The yield and flow stress of copper-1% cadmium alloy exhibits a sharp yield point and strong grain-size dependence, similar to mild steel and aluminium-magnesium alloys. The strengthening is attributed to cadmium atoms pinning dissociated dislocations. To understand this, one must model the dislocation-solute interaction forces and predict the resulting friction shear stresses and Hall-Petch slope. The underlying theory uses analytic expressions based on the atomic misfit interaction between cadmium atoms and the partial dislocations in copper, in both the Nabarro/Basinski (moderate temperature) and Fridel/Labusch (strong-pinning, low temperature) limits. The calculations aim to assess the magnitude of solid-solution pinning and its contribution to the grain-size-dependent component of strength.

## Approach
We adopt the same analytic framework as the original work. Starting from standard elastic constants of copper and the equilibrium solid solubility of cadmium (atomic fraction f=3e-3), we compute the geometry of the solute-dislocation interaction (slip plane separation h, force range w) and the edge components of the partial dislocations. The maximum pinning force between a cadmium atom and each partial is derived from the misfit interaction energy. For moderate temperatures, the friction stress is estimated using the Nabarro expression, which accounts for energy dissipation as both partials move past solute atoms. For low temperatures, we compute the Labusch parameter to confirm the strong-pinning regime, then solve the coupled Fridel equations iteratively to obtain the friction stress for a dissociated screw partial. Finally, the critical unpinning stress is computed from the maximum force expression, from which the macroscopic Hall-Petch slope k follows via a standard slip-band pile-up model using orientation factors. All computations use the given material constants and the solute fraction; no experimental data is required.

## Reproduction target
Your goal is to compute the following numerical values and output them in the requested JSON files:
- Friction shear stress τ₀ (in MN/m²) for both dissociated edge and screw partials at moderate temperature (Nabarro model).
- Labusch parameter β (dimensionless) and low-temperature friction shear stress τ₀ (MN/m²) for the dissociated screw partial (Fridel model).
- Critical unpinning shear stress τ_c (MN/m²) and the predicted Hall‑Petch slope k (MN/m^{3/2}) for the Cu‑Cd alloy.
These quantities must be computed from the analytic formulas using the material constants and solute fraction given in the assets and the intermediate geometry/force values from the process step. Report the results in the three scored output files as specified in the workflow steps.

## Assets

- Copper and cadmium elastic constants and lattice parameters
- Solute atomic fraction f for Cd in Cu at equilibrium

## Workflow steps

### Step 1: Compute interaction force and geometry parameters
- Role: process
- Action: Gather the Cu/Cd elastic constants and lattice parameters (G, b, ν, e_a, e_G, e_κ, etc.). Compute the geometry parameters: h = 3d_s/2 = √6 b/2, w = √3 h/3, the edge components b_e (edge partial: b/2, screw partial: √3 b/6). Evaluate the maximum solute-dislocation force F_max = 0.0305 (9/4) G b_e² / h² for the two partial types. Also compute the line tension T_D ≃ G b² / 4 for a dissociated screw. Store all computed intermediate values (e.g., F_max_edge, F_max_screw, T_D, h, w) in a JSON evidence file.
- Evidence: `/app/outputs/step_00_parameters.json`

### Step 2: Friction shear stress at moderate temperature (Nabarro model)
- Role: scored
- Action: Using the Nabarro-Basinski-Pascual expression for moderate-temperature friction stress τ₀ = 2 √(2 F_max w d_s f / b⁴), which includes the factor 2 for energy dissipation by both partials, compute τ₀ for the dissociated edge partial (b_e = b/2) and for the dissociated screw partial (b_e = √3 b/6). The solute fraction f = 3×10⁻³ and all geometry/force parameters are taken from the step_00 evidence file. Output the two values in MN/m².
- Output file: `/app/outputs/step_01_moderate_temp_tau0.json`
- Format: json
- Contract: {"tau0_edge": <number in MN/m²>, "tau0_screw": <number in MN/m²>}
- Scoring: scored by hidden verifier

### Step 3: Labusch parameter and low-temperature friction stress (Fridel model)
- Role: scored
- Action: Compute the Labusch parameter β = √(2 F_max / (8 T_D w² f d_s)) using the precomputed F_max and T_D. Verify β ≫ 1. Then, in the Fridel strong-pinning limit, compute the friction shear stress τ₀ for the dissociated screw partial by solving iteratively the coupled equations: τ₀ = 0.0305(9/4) G b² b_e / (h² l_e) with l_e = [2 T_D l̄² / (τ₀ b)]^{1/3} and planar spacing l̄ = 1/√(f d_s). Use b_e = √3 b/6 and f = 3×10⁻³. Output β (dimensionless) and τ₀ (MN/m²).
- Output file: `/app/outputs/step_02_low_temp_tau0.json`
- Format: json
- Contract: {"beta": <number, dimensionless>, "tau0_screw_low": <number in MN/m²>}
- Scoring: scored by hidden verifier

### Step 4: Unpinning stress and Hall-Petch slope
- Role: scored (load-bearing)
- Action: For a dissociated screw dislocation pinned by Cd atoms at spacing λ = b along the line, compute the critical unpinning shear stress τ_c using the maximum force expression τ_c = 0.0305(9/2) G b² b_e / (h² λ). Then compute the predicted Hall‑Petch slope using k = m̄ √(m̄' G τ_c b / [π (1‑ν)]). Use the average orientation factors m̄ = 2.93 and m̄' = 1.465. Output τ_c in MN/m² and k in MN/m^{3/2}.
- Output file: `/app/outputs/step_03_hall_petch_k.json`
- Format: json
- Contract: {"tau_c": <number in MN/m²>, "k": <number in MN/m^{3/2}>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_moderate_temp_tau0.json`
- `/app/outputs/step_02_low_temp_tau0.json`
- `/app/outputs/step_03_hall_petch_k.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_moderate_temp_tau0.json
- path: `/app/outputs/step_01_moderate_temp_tau0.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Friction shear stresses from the Nabarro model for dissociated edge and screw partials at moderate temperature.
- schema:
  - `type`: object
  - `required`: `tau0_edge`, `tau0_screw`
  - `properties`:
    - `tau0_edge`:
      - `type`: number
      - `units`: MN/m²
    - `tau0_screw`:
      - `type`: number
      - `units`: MN/m²

### step_02_low_temp_tau0.json
- path: `/app/outputs/step_02_low_temp_tau0.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Labusch parameter and Fridel-model friction stress for a dissociated screw dislocation at low temperature.
- schema:
  - `type`: object
  - `required`: `beta`, `tau0_screw_low`
  - `properties`:
    - `beta`:
      - `type`: number
      - `units`: dimensionless
    - `tau0_screw_low`:
      - `type`: number
      - `units`: MN/m²

### step_03_hall_petch_k.json
- path: `/app/outputs/step_03_hall_petch_k.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Critical unpinning shear stress and predicted Hall-Petch slope k for the Cu-Cd alloy.
- schema:
  - `type`: object
  - `required`: `tau_c`, `k`
  - `properties`:
    - `tau_c`:
      - `type`: number
      - `units`: MN/m²
    - `k`:
      - `type`: number
      - `units`: MN/m^{3/2}

Notes: All outputs are to be placed in /app/outputs. The hidden checker compares the reported numeric values to paper-derived reference values using absolute tolerances. The load-bearing step (step_03) ensures that the intermediate process step (step_00) has been executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_moderate_temp_tau0.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "tau0_edge",
          "tau0_screw"
        ],
        "properties": {
          "tau0_edge": {
            "type": "number",
            "units": "MN/m²"
          },
          "tau0_screw": {
            "type": "number",
            "units": "MN/m²"
          }
        }
      },
      "description": "Friction shear stresses from the Nabarro model for dissociated edge and screw partials at moderate temperature."
    },
    {
      "file": "step_02_low_temp_tau0.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "beta",
          "tau0_screw_low"
        ],
        "properties": {
          "beta": {
            "type": "number",
            "units": "dimensionless"
          },
          "tau0_screw_low": {
            "type": "number",
            "units": "MN/m²"
          }
        }
      },
      "description": "Labusch parameter and Fridel-model friction stress for a dissociated screw dislocation at low temperature."
    },
    {
      "file": "step_03_hall_petch_k.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "tau_c",
          "k"
        ],
        "properties": {
          "tau_c": {
            "type": "number",
            "units": "MN/m²"
          },
          "k": {
            "type": "number",
            "units": "MN/m^{3/2}"
          }
        }
      },
      "description": "Critical unpinning shear stress and predicted Hall-Petch slope k for the Cu-Cd alloy."
    }
  ],
  "notes": "All outputs are to be placed in /app/outputs. The hidden checker compares the reported numeric values to paper-derived reference values using absolute tolerances. The load-bearing step (step_03) ensures that the intermediate process step (step_00) has been executed."
}
```

## How you are scored
The four workflow steps comprise one process step and three scored steps. After you submit your outputs, a hidden verifier will read the scored artifacts and compare each required numeric value to a reference value derived from the paper's own computation, using pre-set tolerances. For each value, if the absolute difference is within the tolerance you receive full credit for that component; beyond the tolerance the credit decays linearly reaching zero at double the tolerance. The overall reward is a weighted combination of the component scores, with the load-bearing Hall‑Petch slope step carrying a substantial share. Simply reporting numbers is not sufficient: the verifier checks that the un-scored intermediate computation was actually performed by requiring the downstream results to be self-consistent and dependent on it. The hidden verifier's tolerances and weights are fixed and unknown to you.
