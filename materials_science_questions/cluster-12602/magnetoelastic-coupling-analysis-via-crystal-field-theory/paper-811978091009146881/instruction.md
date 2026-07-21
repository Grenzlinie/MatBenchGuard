# Spin-lattice coupling coefficients via cubic approximation for Fe3+ in Al2O3 and Ni2+ in ZnSiF6·6H2O

## Problem background
The interaction of phonons with paramagnetic spin systems, characterized by spin-lattice coupling coefficients G_{ij}, is important for understanding relaxation processes and zero-field splitting. In trigonal crystals such as Al2O3:Fe^{3+} and ZnSiF6·6H2O:Ni^{2+}, six independent coupling coefficients (G11^t, G12^t, G13^t, G44^t, G14^t, G41^t) describe this interaction. A simplified approach expresses these trigonal coefficients in terms of the two cubic coefficients G11^c and G44^c through a coordinate rotation, then computes G11^c and G44^c from high-order perturbation formulas within a cubic symmetry approximation. This task reproduces the calculation of the six trigonal spin-lattice coupling coefficients for both crystals.

## Approach
The approach uses the point-charge-dipole model to compute the cubic spin-lattice coupling coefficients G11^c and G44^c for d^5 (Fe^{3+}) and d^8 (Ni^{2+}) ions. For Fe^{3+}, the high-order perturbation formulas involve the free-ion Racah parameters, spin-orbit coupling constant, and radial expectation values, scaled by a covalency factor N and corrected by a Trees parameter alpha. For Ni^{2+}, similar formulas require additional zero-order energy separations W_i for the d^8 configuration in octahedral symmetry, which are obtained from a publicly available reference. Once G11^c and G44^c are determined for each crystal, the six trigonal coefficients are obtained by applying the coordinate transformation that rotates the cubic axes onto the trigonal C3 axis. The two crystals are treated separately, yielding two independent sets of trigonal coefficients.

## Reproduction target
Compute the six trigonal spin-lattice coupling coefficients (G11^t, G12^t, G13^t, G44^t, G14^t, G41^t) for both Al2O3:Fe^{3+} and ZnSiF6·6H2O:Ni^{2+} crystals. For each crystal, produce a JSON file containing these six values in units of cm^{-1}. The values should be derived from the cubic coefficients obtained via the perturbation formulas and the coordinate transformation as described in the workflow steps.

## Assets

- A public reference paper (details in `resources.json`) provides the zero‑order energy separations W₁‑W₅ for d⁸ ions in an octahedral field; the necessary expressions are described in that publicly available reference.

## Formulas and parameters

### 1. Point-charge-dipole model and d⁵ Fe³⁺ formulas
For a d⁵ ion in a regular octahedron the cubic coupling coefficients are

G₁₁ᶜ = (400/3) Dq² ξd² / (P² G)  -  (18/5) e q (1 + 3p/(eR₀)) ⟨r²⟩ ξd³ / (R₀³ P² D)        (Eq. 1)

G₄₄ᶜ = -20 Dq² ξd² / (P² G)  +  (9/5) e q (1 + 3p/(eR₀)) ⟨r²⟩ ξd³ / (R₀³ P² D)           (Eq. 2)

where the crystal field splitting Dq is obtained from the point-charge-dipole model:

Dq = - e q (1 + 5p/(eR₀)) ⟨r⁴⟩ / (6 R₀⁵)            (Eq. 3)

and the energy denominators are

P = 7B + 7C + 2α ,   D = 17B + 5C + 6α ,   G = 10B + 5C + 20α .          (Eq. 4)

Covalency scaling (parameter N) is applied as

B = N⁴ B₀,   C = N⁴ C₀,   ⟨rᵏ⟩ = N² ⟨rᵏ⟩₀,   ξd = N² ξd₀ .               (Eq. 6)

### 2. Coordinate rotation to trigonal symmetry

G₁₁ᵗ = ¼ G₁₁ᶜ + G₄₄ᶜ
G₁₂ᵗ = -¼ G₁₁ᶜ - ⅓ G₄₄ᶜ
G₁₃ᵗ = -⅔ G₄₄ᶜ
G₄₄ᵗ = ½ G₁₁ᶜ + ⅓ G₄₄ᶜ
G₁₄ᵗ = G₄₁ᵗ = (√2/4) G₁₁ᶜ - (√2/3) G₄₄ᶜ      (Eq. 8)

### 3. d⁸ Ni²⁺ formulas (point-charge model, no dipole)

For d⁸ in a cubic field the cubic coefficients are

G₁₁ᶜ = (35/12) ξd² [1/W₁² - 1/W₂²] (∂Dt/∂α)₀
      - (3/2) ξd³ [1/(W₁² W₃) - 1/(W₁ W₂ W₃)] [ (∂Ds/∂α)₀ + (4/5) (∂Dt/∂α)₀ ]
      - (35/24) ξd³ [1/(W₁² W₂) - 2/(W₁ W₂²) - 1/W₁³] (∂Dt/∂α)₀        (Eq. 9)

G₄₄ᶜ = (√2/12) ξd² [1/W₂² - 1/W₁²] (∂v/∂β)₀
      + (1/2) ξd² [1/(W₁ W₃) - 1/(W₂ W₃)] (∂v'/∂β)₀
      - 2 B ξd² [1/(W₂ W₃ W₅) + 1/(W₂² W₅) - 3/(W₁ W₃ W₄) - 3/(W₂ W₃ W₄)] (∂v'/∂β)₀   (Eq. 10)

where the zero-order energy separations W₁,…,W₅ for d⁸ in an octahedral field are obtained from the Tanabe–Sugano energy matrices; the necessary expressions are described in the public reference listed in Assets.  The derivatives are

(∂Dt/∂α)₀ = (40/7) Dq ,   (∂Ds/∂α)₀ = - (12/7) e q ⟨r²⟩ / R₀³ ,          (Eq. 11)

(∂v/∂β)₀  = (18√2/7) e q ⟨r²⟩ / R₀³ + (60√2/7) Dq ,                      (Eq. 12)

(∂v'/∂β)₀ = - (12/7) e q ⟨r²⟩ / R₀³ + (30/7) Dq .

The crystal-field splitting Dq for the Ni²⁺ system is evaluated from a point-charge model (without dipole):

Dq = - e q ⟨r⁴⟩ / (6 R₀⁵) .

All symbols have their usual meaning and the signs of the ξd³ terms in Eqs. 9‑10 are the corrected ones (see the note about the misprint in the source paper).

## Workflow steps

### Step 1: Compute cubic spin-lattice coupling coefficients for Al2O3:Fe3+
- Role: process
- Action: Using the formulas and notation of the Formulas and parameters section, compute Dq from Eq. 3 with q = -2e, p = 0.059 eR₀, R₀ = 0.191 nm, ⟨r⁴⟩ = N² ⟨r⁴⟩₀ (N = 0.903, ⟨r⁴⟩₀ = 11.46485 a.u.).  Obtain P, D, G from Eq. 4 using B₀=1130.22 cm⁻¹, C₀=4111.45 cm⁻¹ and α = 43 cm⁻¹, each scaled by N as in Eq. 6.  Evaluate G₁₁ᶜ and G₄₄ᶜ from Eqs. 1‑2.  The two cubic coefficients are kept internally; no separate output file is required.

### Step 2: Transform to trigonal coefficients for Al2O3:Fe3+
- Role: scored
- Action: Apply the trigonal coordinate rotation (Eq. 8) to the computed G₁₁ᶜ and G₄₄ᶜ to obtain the six trigonal coupling coefficients (G11_t, G12_t, G13_t, G44_t, G14_t, G41_t).
- Output file: `/app/outputs/al2o3_fe3_gijt.json`
- Format: json
- Contract: Object with keys G11_t, G12_t, G13_t, G44_t, G14_t, G41_t (numeric values in cm⁻¹)
- Scoring: scored by hidden verifier

### Step 3: Compute cubic spin-lattice coupling coefficients for ZnSiF6·6H2O:Ni2+
- Role: process
- Action: Use the public reference (Assets) to obtain the zero-order energy separations W₁–W₅ for a d⁸ ion in octahedral symmetry with the parameters B = 1208 N⁴ cm⁻¹, C = 4459 N⁴ cm⁻¹, ξd = 636 N² cm⁻¹, ⟨r²⟩ = 1.9804 N² a.u., ⟨r⁴⟩ = 13.4043 N² a.u. (N = 0.9).  Compute Dq = - e q ⟨r⁴⟩ / (6 R₀⁵) with R₀ = 0.2048 nm and q = -2e.  Evaluate G₁₁ᶜ and G₄₄ᶜ from Eqs. 9‑12.  The two cubic coefficients are kept internally; no separate output file is required.

### Step 4: Transform to trigonal coefficients for ZnSiF6·6H2O:Ni2+
- Role: scored (load-bearing)
- Action: Apply the trigonal coordinate rotation (Eq. 8) to the computed G₁₁ᶜ and G₄₄ᶜ to obtain the six trigonal coupling coefficients (G11_t, G12_t, G13_t, G44_t, G14_t, G41_t).
- Output file: `/app/outputs/znsif6_ni2_gijt.json`
- Format: json
- Contract: Object with keys G11_t, G12_t, G13_t, G44_t, G14_t, G41_t (numeric values in cm⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/al2o3_fe3_gijt.json`
- `/app/outputs/znsif6_ni2_gijt.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### al2o3_fe3_gijt.json
- path: `/app/outputs/al2o3_fe3_gijt.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Trigonal spin-lattice coupling coefficients for Al2O3:Fe3+ crystal
- schema:
  - `type`: object
  - `required`: `G11_t`, `G12_t`, `G13_t`, `G44_t`, `G14_t`, `G41_t`
  - `properties`:
    - `G11_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G12_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G13_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G44_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G14_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G41_t`:
      - `type`: number
      - `unit`: cm^{-1}

### znsif6_ni2_gijt.json
- path: `/app/outputs/znsif6_ni2_gijt.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Trigonal spin-lattice coupling coefficients for ZnSiF6·6H2O:Ni2+ crystal
- schema:
  - `type`: object
  - `required`: `G11_t`, `G12_t`, `G13_t`, `G44_t`, `G14_t`, `G41_t`
  - `properties`:
    - `G11_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G12_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G13_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G44_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G14_t`:
      - `type`: number
      - `unit`: cm^{-1}
    - `G41_t`:
      - `type`: number
      - `unit`: cm^{-1}

Notes: Both output files will be compared against the paper's computed coefficients with predefined tolerances (not disclosed). The transformation equations are publicly known.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "al2o3_fe3_gijt.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "G11_t",
          "G12_t",
          "G13_t",
          "G44_t",
          "G14_t",
          "G41_t"
        ],
        "properties": {
          "G11_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G12_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G13_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G44_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G14_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G41_t": {
            "type": "number",
            "unit": "cm^{-1}"
          }
        }
      },
      "description": "Trigonal spin-lattice coupling coefficients for Al2O3:Fe3+ crystal"
    },
    {
      "file": "znsif6_ni2_gijt.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "G11_t",
          "G12_t",
          "G13_t",
          "G44_t",
          "G14_t",
          "G41_t"
        ],
        "properties": {
          "G11_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G12_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G13_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G44_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G14_t": {
            "type": "number",
            "unit": "cm^{-1}"
          },
          "G41_t": {
            "type": "number",
            "unit": "cm^{-1}"
          }
        }
      },
      "description": "Trigonal spin-lattice coupling coefficients for ZnSiF6·6H2O:Ni2+ crystal"
    }
  ],
  "notes": "Both output files will be compared against the paper's computed coefficients with predefined tolerances (not disclosed). The transformation equations are publicly known."
}
```

## How you are scored
Your submitted JSON files will be scored by a hidden verifier that compares each coefficient to a hidden reference. The verifier assigns a reward between 0 and 1 for each crystal based on how many of the six coefficients are correct within a precision determined by the verifier; the total score is the weighted sum. The verifier evaluates only the submitted coefficients; it does not inspect your intermediate computations. Producing numbers that match the reference earns full credit; inaccurate results yield lower reward. The hidden reference is derived from the paper's computed values, but you must compute the coefficients yourself from the given parameters and formulas.