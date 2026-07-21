# Six Elastic Constants of Dehydrated HEW Lysozyme Crystals via Christoffel Equations

## Problem background
Tetragonal hen egg-white (HEW) lysozyme crystals belong to the 422 point group and have six independent elastic constants: C11, C12, C13, C33, C44, and C66. Determining these constants is essential for understanding defect structures, deformation, and fracture of protein crystals. By measuring ultrasonic sound velocities along specific crystallographic directions and the density of the crystal, the Christoffel equations can be solved to obtain the elastic constants. In the paper, such measurements were performed on HEW lysozyme crystals dehydrated at 42% relative humidity, yielding the set of six constants. The present task is to reproduce this computation: from the given density, sound velocities, and propagation angle, compute the six elastic constants.

## Approach
The Christoffel equations for a tetragonal 422 crystal relate the density ρ, the sound velocities v, and the elastic constants Cij. The relations between the measured velocities and the elastic constants as given in the paper’s Table II are:

- Longitudinal along [110] (v₁):  
  ρ v₁² = (C₁₁ + C₁₂ + 2 C₆₆) / 2

- Transverse along [110], polarization [001] (v₂):  
  ρ v₂² = C₄₄

- Transverse along [110], polarization [1‾10] (v₃):  
  ρ v₃² = (C₁₁ − C₁₂) / 2

- Longitudinal along [001] (v₄):  
  ρ v₄² = C₃₃

- Transverse, propagation in the (010) plane at an angle θ to the [001] axis, polarization [010] (v₅):  
  ρ v₅² = C₄₄ cos²θ + C₆₆ sin²θ

- Quasilongitudinal, propagation perpendicular to the (101) plane (same direction, at angle θ to [001]) (v₆):  
  ρ v₆² = C†, where  

  C† = ½ [ C₁₁ sin²θ + C₃₃ cos²θ + C₄₄  
          + √( (C₁₁ sin²θ − C₃₃ cos²θ + C₄₄ cos 2θ)² + (C₁₃ + C₄₄)² sin² 2θ ) ]

- Quasitransverse, same propagation direction as v₆ (v₇):  
  ρ v₇² = C‡, where  

  C‡ = ½ [ C₁₁ sin²θ + C₃₃ cos²θ + C₄₄  
          − √( (C₁₁ sin²θ − C₃₃ cos²θ + C₄₄ cos 2θ)² + (C₁₃ + C₄₄)² sin² 2θ ) ]

(The velocity v₇ is not required for determining the six elastic constants; it is listed for completeness.)

The density is given as ρ = 1.29 Mg/m³. To obtain elastic constants in GPa, use the conversion  
**C (GPa) = ρ (Mg m⁻³) × v² (m² s⁻²) / 10⁶**,  
since 1 Mg m⁻³ = 10³ kg m⁻³, 1 GPa = 10⁹ Pa, and 1 Pa = 1 kg m⁻¹ s⁻².

The overall scheme is:
1. Compute C₄₄ directly from v₂: C₄₄ = ρ v₂² / 10⁶.
2. Compute C₆₆ from v₅ using ρ v₅² / 10⁶ = C₄₄ cos²θ + C₆₆ sin²θ.
3. Use the v₃ and v₁ equations to obtain C₁₁ – C₁₂ and C₁₁ + C₁₂, then solve for C₁₁ and C₁₂.
4. Compute C₃₃ from v₄: C₃₃ = ρ v₄² / 10⁶.
5. Determine C₁₃ by solving the quasilongitudinal equation for v₆: substitute the known C₁₁, C₃₃, C₄₄, θ, and v₆ into the C† expression, set ρ v₆² / 10⁶ = C†, and solve for C₁₃. Because C₁₃ appears inside the square root as (C₁₃ + C₄₄)², the equation can be solved by isolating the square‑root term, squaring both sides, and solving the resulting quadratic equation for X = C₁₃ + C₄₄; then C₁₃ = X − C₄₄.

All required inputs (density ρ=1.29 Mg/m³, seven sound velocities in m/s, and the angle θ=22.8°) are fixed public values. No external data download is necessary. The agent must implement this scheme in a Python script that uses these constants and produces the six elastic constants in GPa.

## Reproduction target
Compute the six independent elastic constants C₁₁, C₁₂, C₁₃, C₃₃, C₄₄, and C₆₆ (in GPa) for tetragonal HEW lysozyme crystals dehydrated at 42% relative humidity. Use the following fixed inputs: density ρ = 1.29 Mg/m³, sound velocities v₁=3097, v₂=1518, v₃=1448, v₄=3149, v₅=1505, v₆=3197, v₇=1481 (all in m/s), and angle θ = 22.8°. Solve the Christoffel equations for the 422 crystal class to obtain the six constants and write them to a JSON file named `elastic_constants.json` under `/app/outputs`. Values should be expressed in GPa with sufficient precision (two decimal places are typical).

## Assets

- Python 3: python

## Workflow steps

### Step 1: Compute elastic constants from Christoffel equations
- Role: scored (load-bearing)
- Action: Write a Python script that takes as fixed inputs the density ρ=1.29 Mg/m³, sound velocities v₁=3097, v₂=1518, v₃=1448, v₄=3149, v₅=1505, v₆=3197, v₇=1481 m/s, and angle θ=22.8°. Solve the Christoffel equations listed in the Approach section to compute the six independent elastic constants. Use the unit conversion C (GPa) = ρ (Mg/m³) × v² (m/s)² / 10⁶ for each constant.

  Procedure:
  1. C₄₄ = ρ v₂² / 10⁶.
  2. C₆₆ = ( ρ v₅² / 10⁶ − C₄₄ cos²θ ) / sin²θ.
  3. C₁₁ − C₁₂ = 2 ρ v₃² / 10⁶.
  4. C₁₁ + C₁₂ = 2 ρ v₁² / 10⁶ − 2 C₆₆.
  5. Solve for C₁₁ = ((C₁₁ + C₁₂) + (C₁₁ − C₁₂)) / 2, and C₁₂ = ((C₁₁ + C₁₂) − (C₁₁ − C₁₂)) / 2.
  6. C₃₃ = ρ v₄² / 10⁶.
  7. Solve for C₁₃ using the quasilongitudinal equation for v₆.  
     Compute T = ρ v₆² / 10⁶.  
     Define the auxiliary expression  
     L = C₁₁ sin²θ + C₃₃ cos²θ + C₄₄,  
     D = C₁₁ sin²θ − C₃₃ cos²θ + C₄₄ cos 2θ.  
     Then the equality T = ½ [ L + √( D² + (C₁₃ + C₄₄)² sin² 2θ ) ] must hold.  
     Isolate the square‑root term: 2T − L = √( D² + (C₁₃ + C₄₄)² sin² 2θ ).  
     Square both sides: (2T − L)² = D² + (C₁₃ + C₄₄)² sin² 2θ.  
     Solve for X = C₁₃ + C₄₄: X² = [ (2T − L)² − D² ] / sin² 2θ, taking the positive root (since C₁₃ + C₄₄ > 0). Then C₁₃ = X − C₄₄.

  Output a JSON file with keys C11, C12, C13, C33, C44, C66 (values in GPa, sufficient precision).
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: A JSON object with keys "C11", "C12", "C13", "C33", "C44", "C66". Each value is a float representing the elastic constant in GPa, with sufficient precision.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The six independent elastic constants of dehydrated tetragonal HEW lysozyme crystals, computed from given sound velocities, density, and angle.
- schema:
  - `type`: object
  - `required`:
    - `C11`: float (GPa)
    - `C12`: float (GPa)
    - `C13`: float (GPa)
    - `C33`: float (GPa)
    - `C44`: float (GPa)
    - `C66`: float (GPa)
  - `items`: object
  - `required_columns`:
  - `units`: object

Notes: The solver must derive the constants purely from the provided public numeric inputs; no external data download is required. The hidden verifier compares the agent's computed values against the paper-reported values using relative and absolute tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float (GPa)",
          "C12": "float (GPa)",
          "C13": "float (GPa)",
          "C33": "float (GPa)",
          "C44": "float (GPa)",
          "C66": "float (GPa)"
        },
        "items": {},
        "required_columns": [],
        "units": {}
      },
      "description": "The six independent elastic constants of dehydrated tetragonal HEW lysozyme crystals, computed from given sound velocities, density, and angle."
    }
  ],
  "notes": "The solver must derive the constants purely from the provided public numeric inputs; no external data download is required. The hidden verifier compares the agent's computed values against the paper-reported values using relative and absolute tolerances."
}
```

## How you are scored
The hidden verifier will read your `elastic_constants.json`, extract the six elastic constant values, and compare each one to reference values using appropriate relative and absolute tolerances. Each constant (C11, C12, C13, C33, C44, C66) carries equal weight. The total reward is the fraction of constants that fall within the allowed tolerance. The output must be a JSON object with the keys exactly as specified and the values in GPa. There is no other scored artifact; this single stage accounts for the entire reward.