# Vapor Pressure and Composition Calculation for Hypostoichiometric Uranium Dioxide (UO2−x)

## Problem background
Hypostoichiometric uranium dioxide (UO2−x) is used as nuclear reactor fuel, and understanding its vapor properties at high temperatures is critical for safety analysis. This task addresses the computation of vapor pressures and vapor compositions in equilibrium with UO2−x at temperatures from 1500 K to 6000 K. The goal is to determine the oxygen partial pressure, total pressure, and oxygen‑to‑uranium ratio of the vapor using thermodynamic functions and an ionic oxygen‑potential model for the condensed phase. The resulting quantities provide insight into the behavior of the fuel under accident conditions, where vaporization can significantly alter the composition of the condensed phase.

## Approach
The calculation combines three components:

- **Gas‑phase thermodynamic functions:** Free energies of formation for O, O₂, U, UO, UO₂, and UO₃ species as functions of temperature, used to relate partial pressures through equilibrium reactions.
- **Condensed‑phase thermodynamic functions:** Free energy of formation for solid and liquid UO₂ and a method to obtain the free energy of hypostoichiometric UO₂−x by integrating the oxygen partial pressure with respect to non‑stoichiometry x.
- **Ionic oxygen‑potential model:** An ionic equilibrium model for the condensed phase that expresses the oxygen partial pressure p(O₂) in terms of temperature T and x. The model assumes a mixture of U²⁺, U⁴⁺, U⁶⁺, and O²⁻ ions, with two equilibria and corresponding equilibrium constants whose temperature dependence is given by simple coefficients. Separate sets of coefficients are provided for the solid and liquid phases.

The workflow proceeds as follows:
1. For a given temperature T and non‑stoichiometry x, compute p(O₂) using the ionic model with the liquid‑phase parameters (all target conditions lie in the liquid region).
2. Numerically integrate ln(p(O₂)) with respect to x to obtain the correction needed for the free energy of UO₂−x, and combine it with the free energy of stoichiometric UO₂ to yield ΔG_f°(UO₂−x,c).
3. Using the gas‑phase free energies and the computed p(O₂) and ΔG_f°(UO₂−x,c), solve the equilibrium relations to obtain the partial pressures of O, O₂, U, UO, UO₂, and UO₃. From these, compute the total pressure and the vapor‑phase O/U ratio.

This method is applied to a set of target temperatures and compositions to produce the final results.

## Reproduction target
Implement the ionic oxygen‑potential model for liquid UO₂−x using the supplied coefficients. Then, for the following conditions, compute and report the specified quantities:

- Oxygen partial pressure p(O₂) (in MPa) at:
  - T = 3150 K for O/U = 1.90, 1.96, and 2.00
  - T = 6000 K for O/U = 1.90, 1.96, and 2.00
- Total pressure (in MPa) in equilibrium with UO₂.₀₀ at T = 5000 K.
- Vapor‑phase oxygen‑to‑uranium ratio (dimensionless) in equilibrium with UO₁.₉₆ at T = 5000 K.

All values must be derived from the model and data described in this instruction. The final output must be written to `/app/outputs/step_01_results.json` in the format specified under the output contract.

## Model equations

All equations below are taken from the referenced paper; implement them exactly as written.

### 1. Ionic oxygen‑potential model (liquid phase)
The condensed phase is treated as a mixture of U²⁺, U⁴⁺, U⁶⁺, and O²⁻ ions.  
Define the ion fractions:
- y₂ = mole fraction of U²⁺ among all uranium ions
- y₄ = mole fraction of U⁴⁺
- y₆ = mole fraction of U⁶⁺

The non‑stoichiometry parameter x is defined by O/U = 2 − x.  
The site and charge balances are:

y₂ + y₄ + y₆ = 1         (1)

2 y₂ + 4 y₄ + 6 y₆ = 4 − 2 x.   (2)

The two equilibrium reactions are:

2 U⁴⁺ ⇌ U²⁺ + U⁶⁺  K₁ = y₂ y₆ / y₄²

2 U²⁺ + O₂(g) ⇌ 2 U⁴⁺ + 2 O²⁻  K₂ = y₄² (2 − x)² / [ y₂² p(O₂) ]  

with

ln K₁ = A₁ + B₁ / T,  ln K₂ = A₂ + B₂ / T.

Combining (1), (2) and the expression for K₁ yields the quadratic equation for y₄:

(4 K₁ − 1) y₄² + 2 y₄ − (1 − x²) = 0.   (3)

The physically admissible root (positive y₄) is:

y₄ = [ −1 + √( 1 + (4 K₁ − 1)(1 − x²) ) ] / (4 K₁ − 1).  (4)

Then

y₂ = (1 + x − y₄) / 2,        (5)

y₆ = 1 − y₂ − y₄.          (6)

The oxygen partial pressure (in atm) is obtained from the expression for K₂:

ln p(O₂) = 2 ln[ y₄ (2 − x) / y₂ ] − (A₂ + B₂ / T).  (7)

**Conversion to MPa:**  
p(O₂, MPa) = p(O₂, atm) × 0.101325.

### 2. Free energy of hypostoichiometric UO₂−x (single‑phase region)
For a single condensed phase (liquid) the free energy of formation is obtained by integration:

ΔG_f°(UO₂−x, c) = ΔG_f°(UO₂, c) − (R T / 2) ∫₀ˣ ln p(O₂) dx′.  (8)

The integral is evaluated numerically using the p(O₂) values calculated from the ionic model.  
For x = 0 the integral is zero, so ΔG_f°(UO₂, c) is used directly.

### 3. Partial pressures of gaseous species
Given p(O₂) in atm and all ΔG_f° values in J mol⁻¹, the partial pressures (in atm) are computed from the equilibrium relations:

ln p(O) = ½ ln p(O₂) − ΔG_f°(O, g) / (R T)    (9)

ln p(UO₂) = (x/2) ln p(O₂) + [ ΔG_f°(UO₂−x, c) − ΔG_f°(UO₂, g) ] / (R T)  (10)

ln p(UO) = ln p(UO₂) − ½ ln p(O₂) + [ ΔG_f°(UO₂, g) − ΔG_f°(UO, g) ] / (R T)  (11)

ln p(UO₃) = ln p(UO₂) + ½ ln p(O₂) + [ ΔG_f°(UO₂, g) − ΔG_f°(UO₃, g) ] / (R T)  (12)

ln p(U) = ln p(UO₂) − ln p(O₂) + [ ΔG_f°(UO₂, g) − ΔG_f°(U, g) ] / (R T).  (13)

Total pressure (atm) is the sum of all partial pressures; convert to MPa by multiplying by 0.101325.

### 4. Vapor‑phase oxygen‑to‑uranium ratio
R(vapor) = [ p(O) + 2 p(O₂) + p(UO) + 2 p(UO₂) + 3 p(UO₃) ] / [ p(U) + p(UO) + p(UO₂) + p(UO₃) ].  (14)

### 5. Gas‑phase and condensed‑phase free energies
The free energy of formation (in kJ mol⁻¹) for each species is given by the polynomial:

ΔG_f°(T) = A + B T + C T² + D / T + E ln(T) + F T³,

where T is in kelvins. Coefficients are listed in the Assets section.  
To use in the equations above, multiply the result by 1000 to obtain J mol⁻¹ and employ R = 8.314 J mol⁻¹ K⁻¹.

## Assets

All numerical values are taken directly from the source paper and must be hardcoded in your implementation.

### Gas‑phase and condensed‑phase free‑energy coefficients

**O(g)**
| T range (K) | A | B | C | D | E | F |
|-------------|----|----|----|----|----|----|
| 298.15–1400 | 252.36 | −6.2747×10⁻² | −1.3294×10⁻⁶ | −527.69 | 0 | 0 |
| 1400–6000 | 259.03 | −6.7710×10⁻² | −1.6525×10⁻⁸ | −3747.4 | 0 | 0 |

**U(g)**
| T range (K) | A | B | C | D | E | F |
|-------------|----|----|----|----|----|----|
| 298.15–1400 | 539.11 | −1.6007×10⁻¹ | 1.7321×10⁻⁵ | −1046.4 | 0 | 0 |
| 1400–4435 | 749.73 | −8.3008×10⁻² | −2.0904×10⁻⁶ | 0 | −40.548 | 0 |
| 4435–6000 | 0.00 | 0 | 0 | 0 | 0 | 0 |

**UO(g)**
| T range (K) | A | B | C | D | E | F |
|-------------|----|----|----|----|----|----|
| 298.15–1400 | 26.863 | −1.0515×10⁻¹ | 1.6100×10⁻⁵ | −1002.4 | 0 | 0 |
| 1400–4435 | 178.98 | −4.2342×10⁻² | 2.0064×10⁻⁶ | 0 | −29.432 | 0 |
| 4435–6000 | −521.65 | 5.8124×10⁻² | 2.4020×10⁻⁶ | 0 | 0 | 0 |

**UO₂(g)**
| T range (K) | A | B | C | D | E | F |
|-------------|----|----|----|----|----|----|
| 298.15–1400 | −501.42 | −4.2567×10⁻² | 1.4530×10⁻⁵ | 0 | 7.5475 | 0 |
| 1400–4435 | −367.02 | 1.4476×10⁻² | 1.7735×10⁻⁶ | 0 | −18.571 | 0 |
| 4435–6000 | −989.24 | 1.1823×10⁻¹ | 2.0798×10⁻⁶ | 0 | 0 | 0 |

**UO₃(g)**
| T range (K) | A | B | C | D | E | F |
|-------------|----|----|----|----|----|----|
| 298.15–1400 | −822.97 | 2.5295×10⁻² | 1.4770×10⁻⁵ | 0 | 4.9754 | 0 |
| 1400–4435 | −707.37 | 8.0256×10⁻² | 1.9058×10⁻⁶ | 0 | −18.131 | 0 |
| 4435–6000 | −1321.1 | 1.8201×10⁻¹ | 2.4230×10⁻⁶ | 0 | 0 | 0 |

**UO₂(c)** (stoichiometric condensed phase)
| T range (K) | A | B | C | D | E | F |
|-------------|----|----|----|----|----|----|
| 298.15–1400 | −1131.0 | 1.4405×10⁻¹ | 8.1068×10⁻⁶ | 0 | 9.7445 | 0 |
| 1400–2670 | −1079.8 | 1.5714×10⁻¹ | 1.2365×10⁻⁴ | 0 | 0 | −2.6564×10⁻¹ |
| 2670–3120 | −1167.1 | 2.4280×10⁻¹ | −1.4569×10⁻⁵ | 0 | 0 | 0 |
| 3120–4435 | −1002.7 | 1.6163×10⁻¹ | −5.4369×10⁻⁶ | 0 | 0 | 0 |
| 4435–6000 | −1453.7 | 2.5458×10⁻¹ | −3.4634×10⁻⁶ | 0 | 0 | 0 |

### Ionic oxygen‑potential model parameters (liquid)
| Parameter | Value |
|-----------|-------|
| A₁ | 7.680 |
| B₁ (K) | −57 576 |
| A₂ | −25.986 |
| B₂ (K) | 147 352 |

**Note:** The liquid‑phase parameters are valid for T > 3120 K (all target temperatures are ≥ 3150 K).

## Workflow step

### Step 1: Compute required quantities
- Role: scored
- Action: For each target condition listed in the Reproduction target, perform the calculations described in the Approach and Model equations sections. First compute p(O₂) with the liquid ionic model. For values that require ΔG_f°(UO₂−x, c) (vapor pressure and vapor O/U ratio at x ≠ 0), evaluate the integral in Eq. (8) numerically (e.g., Simpson’s rule or trapezoidal integration over a fine x‑grid from 0 to the target x). Then compute all partial pressures, total pressure, and vapor O/U ratio as defined. Assemble the results into a JSON object and write to the output file.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: JSON object with numeric keys: `pO2_3150_1_90`, `pO2_3150_1_96`, `pO2_3150_2_00`, `pO2_6000_1_90`, `pO2_6000_1_96`, `pO2_6000_2_00` (all in MPa), `total_pressure_5000_UO2` (MPa), `vapor_OU_5000_UO1_96` (dimensionless).

## Output files
Write the artifact under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored output: the six oxygen partial pressures, total pressure at 5000 K for stoichiometric UO₂, and vapor O/U ratio at 5000 K for UO₁.₉₆. The verifier compares the reported values against reference values using relative‑error thresholds (10 % for p(O₂), 20 % for total pressure) and verifies that `vapor_OU_5000_UO1_96 > 1.96`.
- schema:
  - `type`: object
  - `required`:
    - `pO2_3150_1_90`: number (MPa)
    - `pO2_3150_1_96`: number (MPa)
    - `pO2_3150_2_00`: number (MPa)
    - `pO2_6000_1_90`: number (MPa)
    - `pO2_6000_1_96`: number (MPa)
    - `pO2_6000_2_00`: number (MPa)
    - `total_pressure_5000_UO2`: number (MPa)
    - `vapor_OU_5000_UO1_96`: number (dimensionless)

Notes: All quantities are in MPa for pressures, dimensionless for O/U ratio.

## Self-check before finishing (optional, not scored)

A machine‑readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: the declared file exists, the JSON object contains the required keys. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness.

```json
{
  "outputs": [
    {
      "file": "step_01_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "pO2_3150_1_90": "number (MPa)",
          "pO2_3150_1_96": "number (MPa)",
          "pO2_3150_2_00": "number (MPa)",
          "pO2_6000_1_90": "number (MPa)",
          "pO2_6000_1_96": "number (MPa)",
          "pO2_6000_2_00": "number (MPa)",
          "total_pressure_5000_UO2": "number (MPa)",
          "vapor_OU_5000_UO1_96": "number (dimensionless)"
        }
      },
      "description": "Scored output: the six oxygen partial pressures, total pressure at 5000 K for stoichiometric UO₂, and vapor O/U ratio at 5000 K for UO₁.₉₆. The verifier compares the reported values against reference values using relative‑error thresholds (10 % for p(O₂), 20 % for total pressure) and verifies that vapor_OU_5000_UO1_96 > 1.96."
    }
  ],
  "notes": "All quantities are in MPa for pressures, dimensionless for O/U ratio."
}
```

## How you are scored
A hidden verifier independently checks your output artifact `step_01_results.json`. Scoring is based on:

- Whether the six p(O₂) values fall within a 10 % relative error of reference values.
- Whether the total pressure at 5000 K for UO₂.₀₀ falls within a 20 % relative error.
- Whether `vapor_OU_5000_UO1_96` is greater than 1.96 (the vapor is oxygen‑rich).

Meeting or exceeding the acceptable thresholds yields full credit for each target; larger deviations reduce the score. The reward is a weighted average over all targets.