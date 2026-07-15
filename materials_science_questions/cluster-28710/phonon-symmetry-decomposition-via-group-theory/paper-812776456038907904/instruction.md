# Group-theoretical Landau theory and renormalization-group analysis of phase transitions

## Problem background
Certain layered transition-metal dichalcogenides, such as 1T‑TiSe₂ and related hypothetical compounds (e.g., 1T‑TaX₂), undergo phase transitions from a normal high‑temperature phase to modulated structures (charge‑density‑wave states) with either single‑Q or triple‑Q ordering. The critical properties near the transition depend on the dimensionality and complex/real nature of the order parameter. This task aims to reproduce the Landau free‑energy description, mean‑field phase boundaries, and renormalization‑group (RG) fixed‑point structure for both materials, and thereby determine which universality class governs the transition in each case.

## Approach
The work follows a group‑theoretic approach. Starting from the space group D3d³ (P\bar{3}m1) and the wave vectors (α, γ) that characterize the modulation, one constructs Bloch‑sum basis vectors with a particular phase convention. From the transformation properties of these vectors under the space‑group generators (S₆⁺ and σ_d), the symmetry rules for the order‑parameter components are derived. Using these rules, the most general symmetry‑invariant Landau free‑energy polynomial up to fourth order is built, with two quartic coupling coefficients u₁ and u₃. The free energy is then minimized at the mean‑field level to obtain the conditions for single‑Q and triple‑Q ordered states and the corresponding order‑parameter amplitudes. Finally, a one‑loop ε‑expansion RG analysis is performed on the quartic couplings to find all fixed points, their eigenvalues, and their stability, which reveals the critical behaviour. The analysis is carried out for two distinct scenarios: (i) a hypothetical 1T‑TaX₂‑like system where the order parameter is complex (n=6); (ii) 1T‑TiSe₂ where the order parameter is real (n=3). The required symbolic group‑theory and algebra are implemented using a Python environment with sympy.

## Reproduction target
Compute and explicitly write out:
1) The symmetry‑invariant Landau free‑energy polynomials (up to quartic order) for both 1T‑TaX₂ (complex order parameter) and 1T‑TiSe₂ (real order parameter), including the transformation rules of the order‑parameter components and the stability constraints on the quartic coefficients (u₁, u₃).
2) The mean‑field phase conditions: the inequalities in u₁, u₃ that distinguish single‑Q and triple‑Q states, and the corresponding order‑parameter amplitudes for each material.
3) The one‑loop RG β‑functions, all fixed points (their coordinates, eigenvalues, and stability) for both materials, and specifically for 1T‑TiSe₂ whether the stable fixed point corresponds to the three‑component Heisenberg universality class (flag `heisenberg_is_stable`).

## Assets

- Python with symbolic mathematics (sympy, numpy): sympy

## Workflow steps

### Step 1: Group-theoretic analysis: basis vectors and transformation rules
- Role: process
- Action: Perform group-theoretic analysis for space group D3d^3 with the specified wave vectors (α,γ) for 1T-TaX2 and 1T-TiSe2. Construct Bloch-sum basis vectors using the phase convention described in the paper, and derive transformation properties of order-parameter components under the generators S6+ and σd.
- Evidence: `/app/outputs/transformation_rules.json`

### Step 2: Construct Landau free energy functionals
- Role: scored
- Action: Using the transformation rules derived in step 01, construct the symmetry-invariant Landau free energy polynomials up to fourth order for both 1T-TaX2 and 1T-TiSe2. The free energy for TaX2 involves complex order parameters, while that for TiSe2 involves real order parameters. Write the complete expressions to free_energy_polynomials.json.
- Output file: `/app/outputs/free_energy_polynomials.json`
- Format: json
- Contract: Scored artifact containing the Landau free energy polynomials with symbolic coefficients a, u1, u3, transformation rules, and stability constraints.
- Scoring: scored by hidden verifier

### Step 3: Mean-field minimization and phase determination
- Role: scored
- Action: Minimize the Landau free energies from step 02 to find the stable (3Q) and (1Q) ordered phases for both materials. Derive the order-parameter amplitudes and the inequality conditions on u1, u3 that distinguish the phases. Write the results to mean_field_states.json.
- Output file: `/app/outputs/mean_field_states.json`
- Format: json
- Contract: Scored artifact containing mean-field phase conditions, order-parameter solutions, and phase boundaries for both TaX2 and TiSe2.
- Scoring: scored by hidden verifier

### Step 4: Renormalization-group analysis
- Role: scored (load-bearing)
- Action: Perform a one-loop epsilon-expansion renormalization-group analysis on the Landau functionals for both 1T-TaX2 (n=6) and 1T-TiSe2 (n=3). Derive the beta functions, find all fixed points, compute their eigenvalues, classify their stability, and determine whether the three-component Heisenberg fixed point is stable for TiSe2. Write the results to rg_fixed_points.json.
- Output file: `/app/outputs/rg_fixed_points.json`
- Format: json
- Contract: Load-bearing scored artifact: RG fixed points, beta functions, eigenvalues, and stability classification for both materials, verifying the Heisenberg universality class for 1T-TiSe2.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_energy_polynomials.json`
- `/app/outputs/mean_field_states.json`
- `/app/outputs/rg_fixed_points.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_energy_polynomials.json
- path: `/app/outputs/free_energy_polynomials.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Landau free energy polynomials for 1T-TaX2 (complex order parameter) and 1T-TiSe2 (real order parameter), with transformation rules and stability constraints.
- schema:
  - `type`: object
  - `required`:
    - `TaX2`:
      - `type`: object
      - `required`: `order_parameter_dim`, `transformation_rules`, `polynomial_terms`, `invariant_constraints`
    - `TiSe2`:
      - `type`: object
      - `required`: `order_parameter_dim`, `transformation_rules`, `polynomial_terms`, `invariant_constraints`

### mean_field_states.json
- path: `/app/outputs/mean_field_states.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Mean-field phase solutions: single-Q and triple-Q conditions (inequalities in u1, u3) and order-parameter amplitudes for both materials.
- schema:
  - `type`: object
  - `required`:
    - `TaX2`:
      - `type`: object
      - `required`: `single_Q_condition`, `triple_Q_condition`, `order_parameter_components`
    - `TiSe2`:
      - `type`: object
      - `required`: `single_Q_condition`, `triple_Q_condition`, `order_parameter_components`

### rg_fixed_points.json
- path: `/app/outputs/rg_fixed_points.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: RG analysis results: beta functions, fixed points (name, coordinates, eigenvalues, stability) for both materials, with a boolean flag indicating whether the stable fixed point is the Heisenberg fixed point.
- schema:
  - `type`: object
  - `required`:
    - `TaX2`:
      - `type`: object
      - `required`: `beta_functions`, `fixed_points`, `heisenberg_is_stable`
    - `TiSe2`:
      - `type`: object
      - `required`: `beta_functions`, `fixed_points`, `heisenberg_is_stable`

Notes: The solving agent must implement symbolic group-theory and algebra using sympy. The checker compares the agent's derived polynomials and inequalities to the paper-reported results (hidden gold) and audits the RG fixed point structure.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_energy_polynomials.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "TaX2": {
            "type": "object",
            "required": [
              "order_parameter_dim",
              "transformation_rules",
              "polynomial_terms",
              "invariant_constraints"
            ]
          },
          "TiSe2": {
            "type": "object",
            "required": [
              "order_parameter_dim",
              "transformation_rules",
              "polynomial_terms",
              "invariant_constraints"
            ]
          }
        }
      },
      "description": "Landau free energy polynomials for 1T-TaX2 (complex order parameter) and 1T-TiSe2 (real order parameter), with transformation rules and stability constraints."
    },
    {
      "file": "mean_field_states.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "TaX2": {
            "type": "object",
            "required": [
              "single_Q_condition",
              "triple_Q_condition",
              "order_parameter_components"
            ]
          },
          "TiSe2": {
            "type": "object",
            "required": [
              "single_Q_condition",
              "triple_Q_condition",
              "order_parameter_components"
            ]
          }
        }
      },
      "description": "Mean-field phase solutions: single-Q and triple-Q conditions (inequalities in u1, u3) and order-parameter amplitudes for both materials."
    },
    {
      "file": "rg_fixed_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "TaX2": {
            "type": "object",
            "required": [
              "beta_functions",
              "fixed_points",
              "heisenberg_is_stable"
            ]
          },
          "TiSe2": {
            "type": "object",
            "required": [
              "beta_functions",
              "fixed_points",
              "heisenberg_is_stable"
            ]
          }
        }
      },
      "description": "RG analysis results: beta functions, fixed points (name, coordinates, eigenvalues, stability) for both materials, with a boolean flag indicating whether the stable fixed point is the Heisenberg fixed point."
    }
  ],
  "notes": "The solving agent must implement symbolic group-theory and algebra using sympy. The checker compares the agent's derived polynomials and inequalities to the paper-reported results (hidden gold) and audits the RG fixed point structure."
}
```

## How you are scored
Each scored artifact (`free_energy_polynomials.json`, `mean_field_states.json`, `rg_fixed_points.json`) is evaluated independently by a hidden verifier. The verifier checks the algebraic structure of the free energy and the correctness of the mean‑field inequalities against the paper's own derived results. For the RG analysis, the verifier confirms that the reported fixed points satisfy the zero‑β‑function condition, that their stability classification is consistent, and that the `heisenberg_is_stable` flag accurately reflects whether the stable fixed point is the Heisenberg fixed point. Merely reporting the paper's published numbers is not sufficient – the verifier expects a correct derivation, and it combines the weighted scores from all three artifacts into a single final reward.
