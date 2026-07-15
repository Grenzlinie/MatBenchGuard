# Compute Wave Speeds in Composite Elastic Media Using Volume-Averaged Equations

## Problem background
This task computes seismic wave speeds in composite elastic media. When two elastic solids are mixed at the pore scale (or a fluid saturates a solid matrix), volume‑averaged megascopic equations predict that multiple P and S waves propagate without attenuation, and in the fluid‑filled case an additional porosity‑wave arises. The paper provides numerical examples for (i) a mixture of two elastic solids and (ii) a porous medium consisting of liquid helium in a glass matrix. For each example, the wave speeds are calculated from the constituent material properties using a Helmholtz decomposition of the governing equations. Your goal is to reproduce those speeds from the given parameters.

## Approach
The megascopic equations of motion are derived by volume averaging the pore‑scale elasticity equations. A Helmholtz decomposition yields formulas for P‑wave and S‑wave speeds, expressed through matrices **D** (inertial coupling), **P** (dilatational stiffness), and **S** (shear stiffness). These matrices are constructed from the densities, bulk and shear moduli, static volume fractions (η⁰), and a porosity‑coupling vector **δ** that relates volume‑fraction changes to dilatations of the individual phases. The workflow first computes δ using an algebraic expression that involves the component bulk moduli, the volume fractions, and the composite bulk modulus, then assembles **D**, **P**, and **S** and evaluates formulas for the squared wave speeds. For the two‑elastic‑solid mixture there are two P‑wave speeds and two S‑wave speeds. For the fluid‑filled porous medium there are two P‑wave speeds, one S‑wave speed, and an additional porosity‑wave speed (whose value is supplied with the material data). All formulas are written out in the steps below so that no external reference is needed. The computation is lightweight and can be implemented in Python with numpy.

## Reproduction target
Produce a JSON file `wave_speeds.json` containing the wave speeds for both examples. For the two‑elastic‑solid mixture, report the keys `P_wave_1`, `P_wave_2`, `S_wave_1`, `S_wave_2` (in km/s). For the porous medium, report `P_wave_1`, `P_wave_2`, `S_wave`, `porosity_wave` (in km/s). The hidden verifier will compare each speed against a reference result derived from the paper’s examples.

## Assets

- Python scientific packages (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Compute porosity-bulk-modulus coupling parameters
- Role: process
- Action: For the two-elastic-solid mixture, compute the coupling parameters δ₁ and δ₂ using the formula below with the given material constants. For the fluid-filled porous medium, compute the corresponding δ parameters using the same formula with the porous‑medium constants, then prepare all computed values for the next step.

**Material constants for two-elastic-solid mixture:**
ρ₁ = 2650 kg/m³,  ρ₂ = 3400 kg/m³
K₁ = 3.3×10¹⁰ Pa,  K₂ = 5.2×10¹⁰ Pa
μ_M⁽¹⁾ = 2.0×10¹⁰ Pa,  μ_M⁽²⁾ = 3.1×10¹⁰ Pa
μ_s⁽¹⁾ = 2.3×10¹⁰ Pa,  μ_s⁽²⁾ = 3.8×10¹⁰ Pa
K_M = 3.25×10¹⁰ Pa,  ρ₁₂ = −0.86 kg/m³
η₁⁰ = 0.5,  η₂⁰ = 0.5   (static volume fractions; η₁⁰+η₂⁰ = 1)

**Material constants for fluid-filled porous medium (liquid helium in glass):**
ρ_s = 2650 kg/m³,  ρ_f = 150 kg/m³
K_s = 3.3×10¹⁰ Pa,  K_f = 5.0×10⁷ Pa
μ_s = 2.0×10⁹ Pa,  μ_f = 0 Pa
K_M = 2.65×10¹⁰ Pa   (seismic‑wave composite bulk modulus)
K_M_por = 2.15×10¹⁰ Pa (bulk modulus for the porosity‑wave process)
ρ₁₂ = −0.86 kg/m³
η_s⁰ = 0.85,  η_f⁰ = 0.15   (static volume fractions; η_s⁰+η_f⁰ = 1)

**Formula for δ (both examples):**
For a two‑phase medium with components A and B,
δ_A = K_A × (η_A⁰ K_A + η_B⁰ K_B − K_M) ÷ (K_A − K_B)²
where K_M is the appropriate composite bulk modulus.
- For the two‑solid mixture, use K_M = 3.25×10¹⁰ Pa for both δ₁ and δ₂.
- For the porous medium, use K_M = 2.65×10¹⁰ Pa for δ_s and δ_f.
  (The alternate value K_M_por is used only when reporting the porosity‑wave speed in Step 2; do **not** use it to compute δ.)
- Evidence: `/app/outputs/coupling_params.json`

### Step 2: Compute wave speeds for both examples
- Role: scored (load-bearing)
- Action: Using the coupling parameters from Step 1 and the material constants, construct the D, P, and S matrices for each example and evaluate the formulas for the squared wave speeds given below. Convert the speeds from m/s to km/s by dividing by 1000. Write the results to `/app/outputs/wave_speeds.json`.

---
**Two-elastic-solid mixture (phases 1 and 2)**

Inertial matrix D:
  D₁₁ = η₁⁰ ρ₁ − ρ₁₂
  D₁₂ = ρ₁₂
  D₂₂ = η₂⁰ ρ₂ − ρ₁₂
  D₂₁ = ρ₁₂

Dilatational stiffness matrix P:
  P₁₁ = η₁⁰ K₁ (1 − δ₁/η₁⁰) + (4/3) μ_M⁽¹⁾
  P₁₂ = K₁ δ₂
  P₂₂ = η₂⁰ K₂ (1 − δ₂/η₂⁰) + (4/3) μ_M⁽²⁾
  P₂₁ = K₂ δ₁

Shear stiffness matrix S:
  S₁₁ = μ_M⁽¹⁾
  S₁₂ = η₂⁰ μ_s⁽¹⁾ (μ_M⁽²⁾ ÷ (η₂⁰ μ_s⁽²⁾) − 1)
  S₂₂ = μ_M⁽²⁾
  S₂₁ = η₁⁰ μ_s⁽²⁾ (μ_M⁽¹⁾ ÷ (η₁⁰ μ_s⁽¹⁾) − 1)

Determinants:
  ΔD = D₁₁ D₂₂ − D₁₂ D₂₁
  ΔP = P₁₁ P₂₂ − P₁₂ P₂₁
  ΔS = S₁₁ S₂₂ − S₁₂ S₂₁

Mixed traces:
  Tr(P†D) = D₁₁ P₂₂ + D₂₂ P₁₁ − D₂₁ P₁₂ − D₁₂ P₂₁
  Tr(S†D) = D₁₁ S₂₂ + D₂₂ S₁₁ − D₂₁ S₁₂ − D₁₂ S₂₁

P‑wave squared speeds (α₁², α₂²) are the two solutions of:
  ΔD α⁴ − Tr(P†D) α² + ΔP = 0
  → α² = [Tr(P†D) ± √(Tr(P†D)² − 4 ΔP ΔD)] ÷ (2 ΔD)
  with α₁² ≥ α₂².

S‑wave squared speeds (β₁², β₂²) are the two solutions of:
  ΔD β⁴ − Tr(S†D) β² + ΔS = 0
  → β² = [Tr(S†D) ± √(Tr(S†D)² − 4 ΔS ΔD)] ÷ (2 ΔD)
  with β₁² ≥ β₂².

Report:
  two_elastic_solids.P_wave_1 = α₁ [km/s] = √(α₁²)/1000
  two_elastic_solids.P_wave_2 = α₂ [km/s] = √(α₂²)/1000
  two_elastic_solids.S_wave_1 = β₁ [km/s] = √(β₁²)/1000
  two_elastic_solids.S_wave_2 = β₂ [km/s] = √(β₂²)/1000

---
**Fluid-filled porous medium (solid s, fluid f)**

Inertial matrix D (same structure, using porous‑medium constants):
  D₁₁ = η_s⁰ ρ_s − ρ₁₂
  D₁₂ = ρ₁₂
  D₂₂ = η_f⁰ ρ_f − ρ₁₂
  D₂₁ = ρ₁₂

Dilatational stiffness matrix P (fluid has μ_f = 0):
  P₁₁ = η_s⁰ K_s (1 − δ_s/η_s⁰) + (4/3) μ_s
  P₁₂ = K_s δ_f
  P₂₂ = η_f⁰ K_f (1 − δ_f/η_f⁰)
  P₂₁ = K_f δ_s

P‑wave squared speeds are obtained from D and P using the same quadratic formula:
  α² = [Tr(P†D) ± √(Tr(P†D)² − 4 ΔP ΔD)] ÷ (2 ΔD)
  with α₁² ≥ α₂².

S‑wave speed (only the solid phase supports shear):
  β² = μ_s ÷ (η_s⁰ ρ_s − ρ₁₂)
  (this is the effective shear‑wave velocity in the solid skeleton)

Report:
  porous_medium.P_wave_1 = α₁ [km/s] = √(α₁²)/1000
  porous_medium.P_wave_2 = α₂ [km/s] = √(α₂²)/1000
  porous_medium.S_wave   = β [km/s]  = √(β²)/1000

Porosity‑wave speed:
  The porosity wave arises from the incompressible limit of fluid motion coupled to elastic deformation of the matrix and requires the alternate bulk modulus K_M_por = 2.15×10¹⁰ Pa.  The value determined from that analysis is:
  porous_medium.porosity_wave = 2.92 km/s
  (supply this numeric value directly; do not attempt to compute it from D/P/S)

---
- Output file: `/app/outputs/wave_speeds.json`
- Format: json
- Contract: A JSON object with two keys: 'two_elastic_solids' (object with keys 'P_wave_1', 'P_wave_2', 'S_wave_1', 'S_wave_2') and 'porous_medium' (object with keys 'P_wave_1', 'P_wave_2', 'S_wave', 'porosity_wave'). All values are numbers in km/s.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/wave_speeds.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### wave_speeds.json
- path: `/app/outputs/wave_speeds.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Wave speeds in km/s for the two-elastic-solid mixture and the liquid-helium-in-glass porous medium. Each speed is accepted if |reported − gold| ≤ 0.05 km/s or relative difference ≤ 1 %.
- schema:
  - `type`: object
  - `required`: `two_elastic_solids`, `porous_medium`
  - `properties`:
    - `two_elastic_solids`:
      - `type`: object
      - `required`: `P_wave_1`, `P_wave_2`, `S_wave_1`, `S_wave_2`
      - `properties`:
        - `P_wave_1`:
          - `type`: number
        - `P_wave_2`:
          - `type`: number
        - `S_wave_1`:
          - `type`: number
        - `S_wave_2`:
          - `type`: number
    - `porous_medium`:
      - `type`: object
      - `required`: `P_wave_1`, `P_wave_2`, `S_wave`, `porosity_wave`
      - `properties`:
        - `P_wave_1`:
          - `type`: number
        - `P_wave_2`:
          - `type`: number
        - `S_wave`:
          - `type`: number
        - `porosity_wave`:
          - `type`: number

Notes: The hidden verifier uses a tolerance‑based comparison (0.05 km/s absolute or 1 % relative) rather than bit‑exact matching. The target_policy is set to threshold_or_better to reflect this. The porosity_wave value for the porous medium is supplied directly (2.92 km/s) because its full derivation lies outside the Helmholtz decomposition used for the other speeds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "wave_speeds.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "two_elastic_solids",
          "porous_medium"
        ],
        "properties": {
          "two_elastic_solids": {
            "type": "object",
            "required": [
              "P_wave_1",
              "P_wave_2",
              "S_wave_1",
              "S_wave_2"
            ],
            "properties": {
              "P_wave_1": {
                "type": "number"
              },
              "P_wave_2": {
                "type": "number"
              },
              "S_wave_1": {
                "type": "number"
              },
              "S_wave_2": {
                "type": "number"
              }
            }
          },
          "porous_medium": {
            "type": "object",
            "required": [
              "P_wave_1",
              "P_wave_2",
              "S_wave",
              "porosity_wave"
            ],
            "properties": {
              "P_wave_1": {
                "type": "number"
              },
              "P_wave_2": {
                "type": "number"
              },
              "S_wave": {
                "type": "number"
              },
              "porosity_wave": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Wave speeds in km/s for the two-elastic-solid mixture and the liquid-helium-in-glass porous medium. Each speed is accepted if |reported − gold| ≤ 0.05 km/s or relative difference ≤ 1 %."
    }
  ],
  "notes": "The hidden verifier uses a tolerance‑based comparison (0.05 km/s absolute or 1 % relative) rather than bit‑exact matching. The target_policy is set to threshold_or_better to reflect this. The porosity_wave value for the porous medium is supplied directly (2.92 km/s) because its full derivation lies outside the Helmholtz decomposition used for the other speeds."
}
```

## How you are scored
A hidden verifier independently scores each of the eight wave speeds. For each speed, your reported value is compared to a hidden reference (the paper’s computed value) and accepted if it lies within an appropriate tolerance. Full credit is earned only when all speeds are matched; partial credit is proportional to the number of correctly matched speeds. The verifier does not check whether you merely printed known numbers — it requires that the file contains the correctly computed results. Therefore you must implement the computation faithfully to obtain maximum credit.
