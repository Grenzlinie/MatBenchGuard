# Nucleation Free-Energy Barrier Calculation from Surface Energies

## Problem background
Zinc phosphide (Zn₃P₂) nanowires grown with earth-abundant catalysts display different cross-sectional morphologies — triangular, pseudo-pentagonal, and hexagonal — depending on growth temperature. The relative thermodynamic stability of these morphologies is governed by the nucleation free-energy barrier per unit height, which is derived from density functional theory (DFT) surface energies and a Wulff construction. The derivation yields geometry-dependent coefficients and barrier prefactors for the triangular and pseudo-pentagonal cross sections.

## Approach
From the published surface energies of Zn₃P₂ facets ({100}, {102}, {112}, {132}) and the Wulff construction, compute geometry-dependent coefficients α_f (total surface energy per unit length) and β_f (area-to-length scaling factor) for the triangular (f=3) and pseudo-pentagonal (f=5) cross sections. For the equilateral triangle f=3: α3 = γ_{102} + 2γ_{132}, β3 = √3/4. For f=5, use the Wulff length relations λ_{100} = d/2, λ_{102} = (γ_{102}/(2γ_{100}))d, λ_{112} = (γ_{112}/(2γ_{100}))d and the algebraic geometric derivation to obtain α5 and β5. Then, compute the per-unit-height nucleation barrier prefactor ΔG_f*/h = α_f²/(4β_f) for each morphology.

## Reproduction target
Produce two scored artifacts:

- `nucleation_constants.json` containing the geometry-dependent coefficients (alpha_3, alpha_5 in J/m²; beta_3, beta_5 dimensionless).
- `barrier_prefactors.json` containing the two barrier prefactors (G3_over_h_DeltaMu and G5_over_h_DeltaMu).

The computation uses only the provided surface energies and the Wulff geometry formulas described. The verifier will additionally confirm that the pseudo-pentagonal prefactor is lower than the triangular prefactor.

## Assets

- Zn3P2 surface energies (Table 1)

## Workflow steps

### Step 1: Compute geometry-dependent coefficients
- Role: scored (load-bearing)
- Action: From the given surface energies and the Wulff geometry for an equilateral triangle (f=3) and a pseudo-pentagon (f=5), compute the geometry-dependent coefficients α_f (total surface energy per unit length, in J/m²) and β_f (area-to-length scaling factor, dimensionless) for both morphologies. For f=3 (triangular, equilateral): α3 = γ_{102} + 2γ_{132}, β3 = √3/4. For f=5 (pseudo-pentagonal): use the length relations λ_{100} = d/2, λ_{102} = (γ_{102}/(2γ_{100}))d, λ_{112} = (γ_{112}/(2γ_{100}))d from the Wulff construction and the algebraic derivation to obtain α5 and β5. Write the computed coefficients to nucleation_constants.json.
- Output file: `/app/outputs/nucleation_constants.json`
- Format: json
- Contract: {alpha_3: float (J/m²), beta_3: float, alpha_5: float (J/m²), beta_5: float}
- Scoring: scored by hidden verifier

### Step 2: Compute nucleation barrier prefactors
- Role: scored
- Action: Using the coefficients from nucleation_constants.json, compute the per-unit-height nucleation barrier prefactor for each morphology via ΔG_f*/h = α_f²/(4β_f). The prefactor is the constant multiplying 1/Δμ. Write the two prefactors to barrier_prefactors.json. The pseudo-pentagonal prefactor must be smaller than the triangular one.
- Output file: `/app/outputs/barrier_prefactors.json`
- Format: json
- Contract: {G3_over_h_DeltaMu: float, G5_over_h_DeltaMu: float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/nucleation_constants.json`
- `/app/outputs/barrier_prefactors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### nucleation_constants.json
- path: `/app/outputs/nucleation_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Geometry-dependent coefficients derived from the surface energies and Wulff construction. α in J/m², β dimensionless.
- schema:
  - `type`: object
  - `required`: `alpha_3`, `beta_3`, `alpha_5`, `beta_5`
  - `properties`:
    - `alpha_3`:
      - `type`: number
      - `unit`: J/m²
    - `beta_3`:
      - `type`: number
    - `alpha_5`:
      - `type`: number
      - `unit`: J/m²
    - `beta_5`:
      - `type`: number

### barrier_prefactors.json
- path: `/app/outputs/barrier_prefactors.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Nucleation barrier prefactors per unit height (constants multiplying 1/Δμ). The checker will also verify that G3_over_h_DeltaMu > G5_over_h_DeltaMu.
- schema:
  - `type`: object
  - `required`: `G3_over_h_DeltaMu`, `G5_over_h_DeltaMu`
  - `properties`:
    - `G3_over_h_DeltaMu`:
      - `type`: number
    - `G5_over_h_DeltaMu`:
      - `type`: number

Notes: All values are deterministic given the provided surface energies. The derivation follows the Wulff construction and the algebraic steps described in the paper's supplementary information.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "nucleation_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "alpha_3",
          "beta_3",
          "alpha_5",
          "beta_5"
        ],
        "properties": {
          "alpha_3": {
            "type": "number",
            "unit": "J/m²"
          },
          "beta_3": {
            "type": "number"
          },
          "alpha_5": {
            "type": "number",
            "unit": "J/m²"
          },
          "beta_5": {
            "type": "number"
          }
        }
      },
      "description": "Geometry-dependent coefficients derived from the surface energies and Wulff construction. α in J/m², β dimensionless."
    },
    {
      "file": "barrier_prefactors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "G3_over_h_DeltaMu",
          "G5_over_h_DeltaMu"
        ],
        "properties": {
          "G3_over_h_DeltaMu": {
            "type": "number"
          },
          "G5_over_h_DeltaMu": {
            "type": "number"
          }
        }
      },
      "description": "Nucleation barrier prefactors per unit height (constants multiplying 1/Δμ). The checker will also verify that G3_over_h_DeltaMu > G5_over_h_DeltaMu."
    }
  ],
  "notes": "All values are deterministic given the provided surface energies. The derivation follows the Wulff construction and the algebraic steps described in the paper's supplementary information."
}
```

## How you are scored
A hidden verifier reads the two artifact files and independently recomputes the expected coefficients and barrier prefactors from the same surface energies and geometric relationships. It compares your submitted values against these recomputed values within a small tolerance appropriate for deterministic algebraic calculations. The reward is a weighted combination of the scores from each stage. The final score also includes a structural check: the triangular barrier prefactor must be strictly larger than the pseudo-pentagonal one.
