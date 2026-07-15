# Soft-core binary fluid λ-line and freezing transition

## Problem background
Soft, bounded interaction potentials arise in models for polymer solutions, where the effective pair potential between macromolecular centres of mass can be accurately described by a Gaussian core model (GCM). Binary mixtures of Gaussian particles with negative non-additivity in the cross-species range may exhibit counterintuitive phase behaviour: the homogeneous fluid can become unstable with respect to periodic concentration fluctuations (microphase separation), and freezing can produce a solid in which the particles are extremely delocalised, with Lindemann ratios far exceeding typical atomic crystals. The present task reproduces the main theoretical predictions for a specific binary GCM mixture: the λ-line where the fluid becomes unstable, the crystal–liquid phase boundary, and the Lindemann ratios that quantify delocalisation.

## Approach
We employ a density functional theory (DFT) treatment based on the random-phase approximation (RPA). Within the RPA, the excess Helmholtz free energy functional is quadratic in the density profiles, and the pair direct correlation functions are simply minus the Gaussian pair potentials. For the homogeneous fluid this yields an analytic free energy. For the crystalline phase we adopt a Gaussian ansatz for the one-body density profiles, placed on a CsCl lattice (BCC with species 1 at corners and species 2 at body centres). The Helmholtz free energy per particle of the crystal is minimised with respect to the Gaussian width parameters α₁, α₂ and the lattice constant a. The crystal–liquid coexistence is then located by a common-tangent construction between the Gibbs free energies of the two phases. The λ-line is obtained by solving D(k)=0, where D(k) is the denominator of the partial structure factors evaluated within the RPA. Lindemann ratios are obtained directly from the optimised Gaussian widths and lattice constant.

## Reproduction target
Compute the λ-line (the locus of (ρR₁₁³, x) points where D(k_c)=0) for the binary GCM with interaction parameters ε₁₁=ε₂₂=2k_BT, ε₁₂=1.8877 k_BT, R₂₂=0.665 R₁₁, R₁₂=0.6 R₁₁. Compute the crystal–liquid coexistence curve (the locus where the Gibbs free energies of the homogeneous liquid and the CsCl crystal are equal) for the same system. Finally, at a fixed total density of ρR₁₁³=20, compute the Lindemann ratios L₁ and L₂ as functions of the concentration x of the smaller species.

## Assets

- Python scientific stack (NumPy, SciPy): numpy, scipy

## Workflow steps

### Step 1: Compute λ-line
- Role: scored
- Action: Solve D(k_c)=0 using the RPA direct correlation functions over a grid of total density ρ and concentration x to obtain a set of (ρ, x) points on the λ-line.
- Output file: `/app/outputs/lambda_line.json`
- Format: json
- Contract: Array of objects with keys 'density' (ρR11^3, float) and 'concentration' (x, float).
- Scoring: scored by hidden verifier

### Step 2: Minimize crystal free energy
- Role: process
- Action: For a grid of total density ρ and concentration x, minimize the Helmholtz free energy per particle of the CsCl crystal with respect to the Gaussian width parameters α1, α2 and the lattice constant a using the RPA functional. Record the optimized parameters and free energy surface.
- Evidence: `/app/outputs/crystal_minimization_results.json`

### Step 3: Compute crystal-liquid coexistence
- Role: scored (load-bearing)
- Action: Using the crystal free energies from the previous step and the liquid free energy from the bulk RPA, perform common-tangent constructions along isobars to locate the crystal-liquid phase boundary. Extract the locus of points where g_c = g_l.
- Output file: `/app/outputs/coexistence_curve.json`
- Format: json
- Contract: Array of objects with keys 'density' (ρR11^3, float) and 'concentration' (x, float).
- Scoring: scored by hidden verifier

### Step 4: Compute Lindemann ratios
- Role: scored
- Action: At fixed total density ρR11^3=20, for a range of concentrations x, calculate L1 = sqrt(2)/(a*sqrt(α1)) and L2 = sqrt(2)/(a*sqrt(α2)) using the optimized α1, α2, a from the crystal minimization step.
- Output file: `/app/outputs/lindemann_ratios.json`
- Format: json
- Contract: Array of objects with keys 'concentration' (x, float), 'L1' (float), 'L2' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lambda_line.json`
- `/app/outputs/coexistence_curve.json`
- `/app/outputs/lindemann_ratios.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lambda_line.json
- path: `/app/outputs/lambda_line.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: λ-line points; checker recomputes D(k) and verifies D(k_c) ≈ 0 within tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `density`, `concentration`
    - `properties`:
      - `density`:
        - `type`: number
        - `unit`: ρR11^3
      - `concentration`:
        - `type`: number
        - `unit`: x

### coexistence_curve.json
- path: `/app/outputs/coexistence_curve.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Crystal-liquid coexistence boundary; checker compares submitted points against hidden digitized reference data from the paper.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `density`, `concentration`
    - `properties`:
      - `density`:
        - `type`: number
        - `unit`: ρR11^3
      - `concentration`:
        - `type`: number
        - `unit`: x

### lindemann_ratios.json
- path: `/app/outputs/lindemann_ratios.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lindemann ratios at ρR11^3=20; checker compares submitted ratios to hidden digitized reference values from the paper.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `concentration`, `L1`, `L2`
    - `properties`:
      - `concentration`:
        - `type`: number
        - `unit`: x
      - `L1`:
        - `type`: number
        - `unit`: dimensionless
      - `L2`:
        - `type`: number
        - `unit`: dimensionless

Notes: The crystal minimization step is a required process step that produces intermediate data; its execution is enforced by the load-bearing coexistence step. The λ-line target uses metric_recompute to verify D(k) zero condition; coexistence and Lindemann use reference_match against hidden gold points from the paper. No tolerance or gold values are exposed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lambda_line.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "density",
            "concentration"
          ],
          "properties": {
            "density": {
              "type": "number",
              "unit": "ρR11^3"
            },
            "concentration": {
              "type": "number",
              "unit": "x"
            }
          }
        }
      },
      "description": "λ-line points; checker recomputes D(k) and verifies D(k_c) ≈ 0 within tolerance."
    },
    {
      "file": "coexistence_curve.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "density",
            "concentration"
          ],
          "properties": {
            "density": {
              "type": "number",
              "unit": "ρR11^3"
            },
            "concentration": {
              "type": "number",
              "unit": "x"
            }
          }
        }
      },
      "description": "Crystal-liquid coexistence boundary; checker compares submitted points against hidden digitized reference data from the paper."
    },
    {
      "file": "lindemann_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "concentration",
            "L1",
            "L2"
          ],
          "properties": {
            "concentration": {
              "type": "number",
              "unit": "x"
            },
            "L1": {
              "type": "number",
              "unit": "dimensionless"
            },
            "L2": {
              "type": "number",
              "unit": "dimensionless"
            }
          }
        }
      },
      "description": "Lindemann ratios at ρR11^3=20; checker compares submitted ratios to hidden digitized reference values from the paper."
    }
  ],
  "notes": "The crystal minimization step is a required process step that produces intermediate data; its execution is enforced by the load-bearing coexistence step. The λ-line target uses metric_recompute to verify D(k) zero condition; coexistence and Lindemann use reference_match against hidden gold points from the paper. No tolerance or gold values are exposed."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that independently scores the three scored artifacts (lambda_line.json, coexistence_curve.json, lindemann_ratios.json). For the λ‑line, the verifier recomputes D(k) at each submitted point and checks that D(k_c)=0 within tolerance. For the coexistence curve, the verifier compares your reported (ρ, x) points against hidden reference points digitised from the paper’s phase diagram, and additionally checks the common‑tangent condition at a few selected points. For the Lindemann ratios, your L₁(x) and L₂(x) curves at the specified density are compared to hidden digitised reference values. Each scored stage carries a fraction of the total reward; the verifier aggregates them into a single overall score. Reporting a number without genuine computation will not pass the structural and recompute checks.
