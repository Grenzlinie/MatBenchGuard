# Vapor Pressure and Composition Calculation for UO2-x using Extended Blackburn Oxygen-Potential Model

## Problem background
Hypostoichiometric uranium dioxide (UO2−x) is used as nuclear reactor fuel, and understanding its vapor properties at high temperatures is critical for safety analysis. This task addresses the computation of vapor pressures and vapor compositions in equilibrium with UO2−x at temperatures from 1500 K to 6000 K. The goal is to determine the oxygen partial pressure, total pressure, and oxygen-to-uranium ratio of the vapor using thermodynamic functions and an oxygen‑potential model. The resulting quantities provide insight into the behavior of the fuel under accident conditions, where vaporization can significantly alter the composition of the condensed phase.

## Approach
The calculation combines three components:

- **Gas‑phase thermodynamic functions:** Free energies of formation for O, O₂, U, UO, UO₂, and UO₃ species as functions of temperature, used to relate partial pressures through equilibrium reactions.
- **Condensed‑phase thermodynamic functions:** Free energy of formation for solid and liquid UO₂ and a method to obtain the free energy of hypostoichiometric UO₂−x by integrating the oxygen partial pressure with respect to non‑stoichiometry x.
- **Oxygen‑potential model (Blackburn model):** An ionic equilibrium model that expresses the oxygen partial pressure p(O₂) in terms of temperature T and x. The model assumes a mixture of U²⁺, U⁴⁺, U⁶⁺, and O²⁻ ions, with two equilibria and corresponding equilibrium constants whose temperature dependence is given by simple coefficients. Separate sets of coefficients are provided for the solid and liquid phases.

The workflow proceeds as follows:
1. For a range of x values at each required temperature, compute p(O₂) using the Blackburn model, selecting the solid or liquid parameters according to the U–O phase diagram boundaries (monotectic at 2700 K, melting at 3120 K).
2. Numerically integrate ln(p(O₂)) to obtain the integral Δ(0,x), which is combined with the free energy of stoichiometric UO₂ to yield ΔGf°(UO₂−x,c) across the grid.
3. Using the gas‑phase free energies and the computed p(O₂) and ΔGf°(UO₂−x,c), solve a set of equilibrium relations to obtain the partial pressures of O, O₂, U, UO, UO₂, and UO₃. From these, compute the total pressure and the vapor‑phase O/U ratio at specified conditions.

This method is applied to a set of target temperatures and compositions to produce the final results.

## Reproduction target
Implement the Blackburn oxygen‑potential model for solid and liquid UO₂−x using the supplied coefficients. Then, for the following conditions, compute and report the specified quantities:

- Oxygen partial pressure p(O₂) (in MPa) at:
  - T = 3150 K for O/U = 1.90, 1.96, and 2.00
  - T = 6000 K for O/U = 1.90, 1.96, and 2.00
- Total pressure (in MPa) in equilibrium with UO₂.₀₀ at T = 5000 K.
- Vapor‑phase oxygen‑to‑uranium ratio (dimensionless) in equilibrium with UO₁.₉₆ at T = 5000 K.

All values must be derived from the workflow described in the approach, using the gas‑phase free‑energy coefficients and the oxygen‑potential model parameters that are listed as resources. The final output must be written to `/app/outputs/step_01_results.json` in the format specified under the output contract.

## Assets

The following data are required for the calculations. All numerical values are taken directly from the source paper and must be hardcoded in your implementation; do not attempt to read any external file.

### Data: Gas-phase thermodynamic functions

The free energy of formation \(\Delta G_f^\circ(T)\) (in kJ/mol) for each gaseous species and for condensed UO2 is given by the polynomial:

\[
\Delta G_f^\circ(T) = A + B\,T + C\,T^2 + \frac{D}{T} + E\ln(T) + F\,T^3
\]

where \(T\) is the absolute temperature in kelvins. For each species the temperature range and the corresponding coefficients are listed below. Missing coefficients are zero.

**O(g)**

| Range (K) | A | B (K⁻¹) | C (K⁻²) | D (K) | E | F (K⁻³) |
|-----------|----|---------|---------|-------|---|---------|
| 298.15 – 1400 | 252.36 | −6.2747×10⁻² | −1.3294×10⁻⁶ | −527.69 | 0 | 0 |
| 1400 – 6000 | 259.03 | −6.7710×10⁻² | −1.6525×10⁻⁸ | −3747.4 | 0 | 0 |

**U(g)**

| Range (K) | A | B (K⁻¹) | C (K⁻²) | D (K) | E | F (K⁻³) |
|-----------|----|---------|---------|-------|---|---------|
| 298.15 – 1400 | 539.11 | −1.6007×10⁻¹ | 1.7321×10⁻⁵ | −1046.4 | 0 | 0 |
| 1400 – 4435 | 749.73 | −8.3008×10⁻² | −2.0904×10⁻⁶ | 0 | −40.548 | 0 |
| 4435 – 6000 | 0.00 | 0 | 0 | 0 | 0 | 0 |

**UO(g)**

| Range (K) | A | B (K⁻¹) | C (K⁻²) | D (K) | E | F (K⁻³) |
|-----------|----|---------|---------|-------|---|---------|
| 298.15 – 1400 | 26.863 | −1.0515×10⁻¹ | 1.6100×10⁻⁵ | −1002.4 | 0 | 0 |
| 1400 – 4435 | 178.98 | −4.2342×10⁻² | 2.0064×10⁻⁶ | 0 | −29.432 | 0 |
| 4435 – 6000 | −521.65 | 5.8124×10⁻² | 2.4020×10⁻⁶ | 0 | 0 | 0 |

**UO₂(g)**

| Range (K) | A | B (K⁻¹) | C (K⁻²) | D (K) | E | F (K⁻³) |
|-----------|----|---------|---------|-------|---|---------|
| 298.15 – 1400 | −501.42 | −4.2567×10⁻² | 1.4530×10⁻⁵ | 0 | 7.5475 | 0 |
| 1400 – 4435 | −367.02 | 1.4476×10⁻² | 1.7735×10⁻⁶ | 0 | −18.571 | 0 |
| 4435 – 6000 | −989.24 | 1.1823×10⁻¹ | 2.0798×10⁻⁶ | 0 | 0 | 0 |

**UO₃(g)**

| Range (K) | A | B (K⁻¹) | C (K⁻²) | D (K) | E | F (K⁻³) |
|-----------|----|---------|---------|-------|---|---------|
| 298.15 – 1400 | −822.97 | 2.5295×10⁻² | 1.4770×10⁻⁵ | 0 | 4.9754 | 0 |
| 1400 – 4435 | −707.37 | 8.0256×10⁻² | 1.9058×10⁻⁶ | 0 | −18.131 | 0 |
| 4435 – 6000 | −1321.1 | 1.8201×10⁻¹ | 2.4230×10⁻⁶ | 0 | 0 | 0 |

**UO₂(c)** (condensed phase, used for stoichiometric UO₂)

| Range (K) | A | B (K⁻¹) | C (K⁻²) | D (K) | E | F (K⁻³) |
|-----------|----|---------|---------|-------|---|---------|
| 298.15 – 1400 | −1131.0 | 1.4405×10⁻¹ | 8.1068×10⁻⁶ | 0 | 9.7445 | 0 |
| 1400 – 2670 | −1079.8 | 1.5714×10⁻¹ | 1.2365×10⁻⁴ | 0 | 0 | −2.6564×10⁻¹ |
| 2670 – 3120 | −1167.1 | 2.4280×10⁻¹ | −1.4569×10⁻⁵ | 0 | 0 | 0 |
| 3120 – 4435 | −1002.7 | 1.6163×10⁻¹ | −5.4369×10⁻⁶ | 0 | 0 | 0 |
| 4435 – 6000 | −1453.7 | 2.5458×10⁻¹ | −3.4634×10⁻⁶ | 0 | 0 | 0 |

### Data: Oxygen‑potential model (Blackburn model)

The oxygen partial pressure \(p_{\mathrm{O}_2}\) (in MPa) is obtained from the ionic equilibria:

1. \(2\,\mathrm{U}^{4+} \rightleftharpoons \mathrm{U}^{2+} + \mathrm{U}^{6+}\), equilibrium constant \(K_1\)
2. \(2\,\mathrm{U}^{2+} + \mathrm{O}_2(\mathrm{g}) \rightleftharpoons 2\,\mathrm{U}^{4+} + 2\,\mathrm{O}^{2-}\), equilibrium constant \(K_2\)

with

\[
\ln K_1 = A_1 + B_1/T,\qquad
\ln K_2 = A_2 + B_2/T .
\]

The coefficients for solid and liquid are:

| Parameter | Solid (T ≤ 3120 K) | Liquid (T > 3120 K) |
|-----------|-------------------|---------------------|
| \(A_1\) | 7.680 | 7.680 |
| \(B_1\) (K) | −60 805 | −57 576 |
| \(A_2\) | −28 786 | −25 986 |
| \(B_2\) (K) | 159 317 | 147 352 |

The equations that relate the ion fractions and \(p_{\mathrm{O}_2}\) to \(x\) are given in the Methods section of the paper (eqs. (27)-(38)). The agent must implement them exactly.

### Data: Phase diagram boundaries

- Stoichiometric UO₂ melts at 3120 K.
- A monotectic exists at 2700 K; the solid phase has O/U ≈ 1.50 (x ≈ 0.50) and the liquid O/U ≈ 1.67 (x ≈ 0.33).
- For the target conditions – all at or above 3150 K – the condensed phase is entirely liquid (Region VI of the phase diagram). Thus only the liquid oxygen‑potential model coefficients and the liquid‑phase condensed‑phase ΔGf° coefficients (T > 3120 K) are needed.

## Workflow steps

### Step 1: Compute oxygen potential grids
- Role: process
- Action: Implement the Blackburn solid and liquid oxygen-potential models using the given coefficients. For temperatures T = 3150, 5000, 6000 K, compute the oxygen partial pressure p(O2) as a function of the non-stoichiometry parameter x (O/U = 2-x) over a fine grid from x=0 to x=0.5. Use the solid model for T < 2670 K and the liquid model for T > 3120 K, with appropriate interpolation across the solid-liquid coexistence region per the phase diagram. Save the resulting pO2 vs x data for each temperature in a CSV file.
- Evidence: `/app/outputs/pO2_grid.csv`

### Step 2: Integrate pO2 to obtain free energies
- Role: process
- Action: Numerically integrate ln(p(O2)) with respect to x at constant T (using the grids from step_1) to compute the integral Δ(0,x) required for the free-energy correction. Combine with ΔGf°(UO2,c) from the supplied thermodynamic coefficients, using the appropriate phase-region formulas (e.g., Region I–VI based on Fig. 2) to obtain ΔGf°(UO2-x,c) for all grid points. Save the integrated free-energy values in a CSV file.
- Evidence: `/app/outputs/deltaG_grid.csv`

### Step 3: Compute vapor pressures and composition at target conditions
- Role: scored (load-bearing)
- Action: For the six target conditions (3150 K at x=0.10, 0.04, 0.00; 6000 K at x=0.10, 0.04, 0.00) and the additional targets (5000 K at x=0.00 for total pressure; 5000 K at x=0.04 for vapor O/U ratio), evaluate gas-phase free-energy functions using the provided coefficients. Using p(O2) from step_1 and ΔGf°(UO2-x,c) from step_2, compute the partial pressures of O, O2, U, UO, UO2, and UO3 via the equilibrium relations. Sum the partial pressures to obtain total pressure. Compute the vapor-phase oxygen-to-uranium ratio. Write all required final values as a JSON object to /app/outputs/step_01_results.json.
- Output file: `/app/outputs/step_01_results.json`
- Format: json
- Contract: JSON object with numeric keys: pO2_3150_1_90 (MPa), pO2_3150_1_96 (MPa), pO2_3150_2_00 (MPa), pO2_6000_1_90 (MPa), pO2_6000_1_96 (MPa), pO2_6000_2_00 (MPa), total_pressure_5000_UO2 (MPa), vapor_OU_5000_UO1_96 (dimensionless).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_results.json
- path: `/app/outputs/step_01_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Scored output: the six oxygen partial pressures, total pressure at 5000 K for stoichiometric UO₂, and vapor O/U ratio at 5000 K for UO₁.₉₆. The verifier compares the reported values against reference values using relative‑error thresholds (10 % for p(O₂), 20 % for total pressure) and verifies that vapor_OU_5000_UO1_96 > 1.96.
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

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

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
A hidden verifier independently checks each workflow stage’s output. The scored artifact `step_01_results.json` is compared against expected values that are recomputed by the verifier using the same model and parameters. The verifier also performs consistency checks on the process artifacts (`pO2_grid.csv` and `deltaG_grid.csv`) to ensure the full pipeline was executed.

Scoring is based on:
- Whether the six requested p(O₂) values fall within an acceptable relative error of the reference.
- Whether the total pressure at 5000 K for UO₂.₀₀ falls within an acceptable relative error.
- Whether the vapor O/U ratio at 5000 K for UO₁.₉₆ exceeds the condensed‑phase value of 1.96 (i.e., the vapor is oxygen‑rich), which is a structural check derived from the physics.

Meeting or exceeding the acceptable thresholds yields full credit for each target; larger deviations reduce the score. The final reward is a weighted average over all targets and process evidence checks (process checks carry low weight). The verifier does not reveal its exact tolerances or reference values; you must produce results from a correct implementation of the model and integrations.
