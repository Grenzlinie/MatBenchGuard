# Crossover temperature and cubic/quadratic impact ionization rate ratio in direct-gap semiconductors

## Problem background
Impact ionization is a key interband process responsible for carrier multiplication in semiconductor devices. In direct-gap cubic semiconductors, the rate near threshold can be expressed as a sum of a quadratic term (anisotropic, arising from remote-band coupling) and a cubic term (isotropic, from the nearest-band coupling). Which contribution dominates depends on the effective temperature of the hot-electron distribution, with a crossover effective temperature T* marking the transition from anisotropic to isotropic behaviour. The competition between these mechanisms is particularly relevant for understanding breakdown and photodetector performance in narrow- and middle-gap materials. This task determines T* and the ratio of the averaged cubic to quadratic rates at room temperature (300 K) for eight important cubic semiconductors using analytically derived formulas and experimentally known band parameters.

## Approach
The total impact ionization rate for a hot electron with excess energy ε = E - E_th above the threshold is approximated as

W(ε, u) = A(u) ε² + B ε³ ,

where u = k₀/k₀ is the initial electron direction. The cubic coefficient B is isotropic and given by

B = (ω_B* / (18 E_g³)) × (E_g + Δ₀) / (E_g + 2Δ₀/3) × F₂(Δ₀/E_g) ,

with ω_B* = mₑ e⁴ / (2 ℏ³ κ²) the Bohr frequency (this factor cancels in all ratios and the crossover temperature, so its numerical value is not needed). The auxiliary function is

F₂(x) = (1+x)² (1+x/3)³ / [ (1+7x/9 + x²/6) (1+2x/3)² (1+x/2) ] .

The quadratic coefficient A(u) is anisotropic:

A(u) = (4/3) ω_B* (Q⁴ / (E_G² P⁴)) × K(u, β) × (E_g + Δ₀/2) / (E_g + Δ₀/3) × F₂(Δ₀/E_g) ,

where P and Q are the Kane and remote-band momentum matrix elements, E_G is the energy separation to the higher c' band, and the dimensionless parameter

β = P² Δ₀ E_G / (6 Q² E_g²) .

The function K(u, β) is a cubic invariant; its analytic approximation for arbitrary β is expressed through the polynomial invariants I(u) = ux² uy² + ux² uz² + uy² uz² and J(u) = ux² uy² uz²:

S(u,β) = √(4 I² - 12 J + β²)
K₁(u) = -4 (I² - 3 J) (4 I² - I - 3 J)
K₂(u) = -8 I³ + 2 I² + 18 I J - 4 J
K₃(u) = -2 I² + I - 3 J
K˜₂(u) = 3 J + I - 4 I²
K₁_term(u,β) = (K₁(u) + β K₂(u) + β² K₃(u)) / [ S(u,β) (β + S(u,β)) ]
K₂_term(u,β) = (K₂(u) + β K˜₂(u)) / (β + S(u,β))
K(u,β) = K₁_term(u,β) + K₂_term(u,β) .

To compare the two contributions we average over directions of u (assuming isotropic electron distribution) and over the Maxwellian energy distribution. The averaged rates are

⟨W₂⟩ = 2 ⟨A⟩ T² ,   ⟨W₃⟩ = 6 B T³ ,

where ⟨A⟩ = (4/3) ω_B* (Q⁴ / (E_G² P⁴)) ⟨K⟩(β) (E_g+Δ₀/2)/(E_g+Δ₀/3) F₂(Δ₀/E_g) and ⟨K⟩(β) = (1/4π) ∫ K(u,β) dΩ is the solid-angle average of the cubic invariant. The crossover temperature T* is defined by ⟨W₂⟩(T*) = ⟨W₃⟩(T*), leading to

T* = ⟨A⟩ / (3 B) = 8 (Q⁴ / P⁴) (E_g³ / E_G²) ⟨K⟩(β) F₁(Δ₀/E_g) ,

with F₁(x) = (1+2x/3)(1+x/2) / ((1+x)(1+x/3)) .

At a given temperature T the ratio of the averaged rates is

ratio(T) = ⟨W₃⟩ / ⟨W₂⟩ = T / T* ,

so at T = 300 K the desired ratio is simply 300 / T* .

Because the bandgap E_g itself depends on temperature, T* must be solved iteratively from T* = 8 (Q⁴/P⁴) (E_g(T*)³ / E_G²) ⟨K⟩(β(T*)) F₁(Δ₀/E_g(T*)) using the empirical temperature dependencies of E_g.

**Band parameters**

The table below lists the zero-temperature bandgap E_g(0), the spin-orbit splitting Δ₀, the Kane parameter P, the remote-band energy E_G, the remote-band matrix element Q, together with the coefficients of the temperature-dependent bandgap model. For all materials except CdTe the Varshni formula is used:
  E_g(T) = E_g(0) - α T² / (T + β_V)   (α in eV/K, β_V in K).
For CdTe the Manoogian-Woolley form is used:
  E_g(T) = E_g(0) + a [1 - coth(b/T)]   (a in eV, b in K).

| Material        | E_g(0) [eV] | Δ₀ [eV] | P [eV·Å] | E_G [eV] | Q [eV·Å] | α [eV/K]  | β_V [K] | a [eV] | b [K] |
|-----------------|------------|---------|-----------|----------|-----------|-----------|---------|--------|-------|
| InSb            | 0.24       | 0.81    | 9.64      | 3.2      | 8.13      | 3.2e-4    | 170     | ---    | ---   |
| InAs            | 0.42       | 0.39    | 9.2       | 4.4      | 8.33      | 2.76e-4   | 93      | ---    | ---   |
| GaSb            | 0.81       | 0.76    | 9.62      | 3.3      | 8.11      | 4.7e-4    | 200     | ---    | ---   |
| In₀.₅₃Ga₀.₄₇As | 0.82       | 0.33    | 9.81      | 4.4      | 8.25      | 4.77e-4   | 257     | ---    | ---   |
| InP             | 1.42       | 0.11    | 8.85      | 4.7      | 7.22      | 3.63e-4   | 162     | ---    | ---   |
| In₀.₅₂Al₀.₄₈As| 1.53       | 0.30    | 9.09      | 4.5      | 8.25      | 4.7e-4    | 300     | ---    | ---   |
| GaAs            | 1.52       | 0.34    | 10.49     | 4.5      | 8.17      | 5.405e-4  | 204     | ---    | ---   |
| CdTe            | 1.61       | 0.95    | 9.5       | 5.4      | 7.87      | ---       | ---     | 0.073 | 105   |

The derived dimensionless parameters needed internally are x = Δ₀/E_g and β = P² Δ₀ E_G / (6 Q² E_g²). All required quantities can be computed from this table and the formulas above.

## Reproduction target
For each of the eight semiconductors (InSb, InAs, GaSb, In₀.₅₃Ga₀.₄₇As, InP, In₀.₅₂Al₀.₄₈As, GaAs, CdTe) compute the crossover effective temperature T* (in Kelvin) and the ratio of the averaged cubic to quadratic rate at T = 300 K. Write the results to a CSV file crossover_and_ratio.csv with the schema:

- material : string
- T_star_K : float  (T* in K)
- ratio_300K : float  (⟨W₃⟩/⟨W₂⟩ at 300 K)
- dominant_at_300K : string  ("cubic" if ratio_300K > 1; "quadratic" if ratio_300K < 1; "equal" if 0.95 ≤ ratio_300K ≤ 1.05)

## Assets

- Band structure parameters for eight semiconductors (Table I)
- numpy: numpy

## Workflow steps

### Step 1: Evaluate analytic formulas for crossover temperature and cubic/quadratic ratio
- Role: scored (load-bearing)
- Action: Using the provided analytic expressions for the averaged quadratic and cubic impact ionization rates and the crossover temperature formula, together with the band parameters for the eight listed semiconductors (InSb, InAs, GaSb, In0.53Ga0.47As, InP, In0.52Al0.48As, GaAs, CdTe), compute for each material the crossover effective temperature T* and the ratio of the averaged cubic to quadratic rates at T = 300 K. Write results to crossover_and_ratio.csv.
- Output file: `/app/outputs/crossover_and_ratio.csv`
- Format: csv
- Contract: material (string), T_star_K (float, crossover temperature in Kelvin), ratio_300K (float, ratio of averaged cubic to quadratic rates at 300 K), dominant_at_300K (string, one of: cubic, quadratic, equal)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/crossover_and_ratio.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### crossover_and_ratio.csv
- path: `/app/outputs/crossover_and_ratio.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with one row per semiconductor, containing the computed crossover temperature T*, the cubic/quadratic rate ratio at 300 K, and the dominant term label.
- schema:
  - `type`: table
  - `required_columns`: `material`, `T_star_K`, `ratio_300K`, `dominant_at_300K`
  - `units`:
    - `T_star_K`: Kelvin
    - `ratio_300K`: dimensionless

Notes: The checker will recompute the expected T* and ratio_300K from the same analytic formulas and band parameters, then compare the agent's values within a relative tolerance of 1%. The dominant_at_300K label must be consistent with ratio_300K (cubic if >1, quadratic if <1, equal if within 5% of 1).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "crossover_and_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "T_star_K",
          "ratio_300K",
          "dominant_at_300K"
        ],
        "units": {
          "T_star_K": "Kelvin",
          "ratio_300K": "dimensionless"
        }
      },
      "description": "CSV file with one row per semiconductor, containing the computed crossover temperature T*, the cubic/quadratic rate ratio at 300 K, and the dominant term label."
    }
  ],
  "notes": "The checker will recompute the expected T* and ratio_300K from the same analytic formulas and band parameters, then compare the agent's values within a relative tolerance of 1%. The dominant_at_300K label must be consistent with ratio_300K (cubic if >1, quadratic if <1, equal if within 5% of 1)."
}
```

## How you are scored
A hidden verifier will recompute the expected T* and ratio_300K using the same analytic formulas and band parameters listed in the instruction. Your submitted CSV values are compared to the reference values with a relative tolerance; the dominant_at_300K label is checked for consistency with the ratio. Each scored artifact carries a weight, and the final reward (a float between 0 and 1) is the weighted combination of the per‑item scores. Reporting correct numbers that pass the tolerance is what matters; printing ranges or commentary does not contribute to the score.
