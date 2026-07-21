# Thermodynamic and kinetic modeling of carbide precipitation in a refractory alloy

## Problem background
The 45Cr26Ni33Si2Nb2 refractory alloy is used in pyrolysis furnaces at operating temperatures between 800 and 1100 °C. During long‑term high‑temperature exposure the alloy's phase composition changes as carbon reacts with alloying elements, forming carbides (Cr₂₃C₆, NbC) and, under certain conditions, a complex G‑phase. Predicting the equilibrium phase composition and the time evolution of these precipitates is critical for estimating material aging and the loss of mechanical properties. This task reproduces the thermodynamic‑kinetic model that computes the equilibrium carbide concentrations and the precipitation kinetics of Cr₂₃C₆, and determines the time required for the alloy to approach its stable state.

## Approach
First, the thermodynamic equilibrium is solved from the material balance and the equilibrium constants of the carbide‑forming reactions, assuming the G‑phase is absent. The relevant reactions are:

1. C + (23/6) Cr ⇌ (1/3) Cr₂₃C₆  
2. C + Nb ⇌ NbC

The equilibrium concentrations are obtained by solving the carbon material balance together with the equilibrium relations that connect the solid‑solution concentrations of chromium, niobium, and carbon. The activity coefficients needed for the calculation are provided below (γ_Cr and γ_Nb are taken as unity; γ_C is calculated from the Wagner‑type model for doped austenite using the interaction parameters listed in the constants section).

Next, a kinetic model for Cr₂₃C₆ precipitation is set up. The model describes the rate of carbon redistribution into carbide as a function of the current concentrations, an equilibrium driving force, and a forward reaction rate constant that follows an Arrhenius form with a pre‑exponential factor k₀ and an activation energy Eₙ. Using experimental Cr₂₃C₆ mass fractions after 1000 h of aging at 800, 900, and 1000 °C, the unknown kinetic constants are estimated by solving an inverse problem. With the calibrated kinetics, the mass fraction of Cr₂₃C₆ is computed as a function of time for the four temperatures (800, 900, 1000, 1100 °C) by numerical integration of the rate equation. Finally, the stabilization time τ∗ is defined as the time needed for the Cr₂₃C₆ mass fraction to reach 99 % of its equilibrium value, and is calculated for each temperature.

## Thermodynamic equilibrium equations

The carbon material balance (assuming no G‑phase) is

\[
[C]_0 = [C]_{\text{eq}} + \frac{6}{23}\big([Cr]_0 - [Cr]_{\text{eq}}\big) + \big([Nb]_0 - [Nb]_{\text{eq}}\big),
\]

where  
- \([C]_0\) = 0.021, \([Cr]_0\) = 0.285, \([Nb]_0\) = 0.012 (atomic fractions from Table 1),  
- \([C]_{\text{eq}}\), \([Cr]_{\text{eq}}\), \([Nb]_{\text{eq}}\) are the equilibrium atomic fractions of the elements in solid solution.

The equilibrium relations for the two carbide-forming reactions are

\[
[Cr]_{\text{eq}} = \frac{1}{\gamma_{\text{Cr}}\left(K_1 \gamma_{\text{C}} [C]_{\text{eq}}\right)^{6/23}}, \qquad
[Nb]_{\text{eq}} = \frac{1}{\gamma_{\text{Nb}} K_5 \gamma_{\text{C}} [C]_{\text{eq}}},
\]

where  
- \(K_1\) and \(K_5\) are the equilibrium constants given below,  
- \(\gamma_{\text{Cr}} = 1.0\), \(\gamma_{\text{Nb}} = 1.0\),  
- \(\gamma_{\text{C}}\) is the activity coefficient of carbon in austenite, calculated from

\[
\log_{10} \gamma_{\text{C}} = \sum_i e_C^i \, [i],
\]

with the atomic fractions \([i]\) expressed on a 0–1 scale (e.g., 0.021 for carbon) and the interaction parameters \(e_C^i\) listed under “Constants and parameters”.

From the solution the molar fractions of the carbide phases are obtained as

\[
[\text{NbC}]_{\text{eq}} = [Nb]_0 - [Nb]_{\text{eq}}, \qquad
[\text{Cr}_{23}\text{C}_6]_{\text{eq}} = \frac{1}{6}\Big([C]_0 - [C]_{\text{eq}} - [\text{NbC}]_{\text{eq}}\Big).
\]

This system is solved for the unknown \([C]_{\text{eq}}\) at each temperature. Because \(\gamma_{\text{C}}\) depends on the composition, an iterative procedure is required.

## Kinetic model for Cr₂₃C₆ precipitation

The precipitation kinetics of Cr₂₃C₆ is described by the time evolution of its mass fraction \(F\). The carbon mass balance links the mass fraction of dissolved carbon \((C)\) to the carbide mass fraction:

\[
(C) = (C)_0 - \nu F,
\]

where \((C)_0 = 0.0045\) is the initial mass fraction of carbon in the alloy, and \(\nu = 0.057\) is the mass ratio (carbon fraction in Cr₂₃C₆). The rate of carbide growth is proportional to the deviation of the dissolved carbon concentration from its equilibrium value:

\[
\frac{dF}{dt} = k_0 \exp\!\left(-\frac{E_{\eta}}{RT}\right)\, (Cr)_0^{\,m} \, \frac{(C) - (C)_{\text{eq}}}{\nu},
\]

with  
- \(m = 23/6\),  
- \((Cr)_0 = 0.269\) (initial mass fraction of chromium),  
- \((C)_{\text{eq}}\) the equilibrium mass fraction of carbon in solution, obtained from the thermodynamic calculation and converted from atomic fraction using the average atomic weight of the alloy (see hints below).

The unknown kinetic constants \(k_0\) (h⁻¹) and \(E_{\eta}\) (J/mol) are determined by fitting the model to the experimental Cr₂₃C₆ mass fractions after 1000 h (see “Experimental data for kinetic fitting”).

## Constants and parameters

### 1. Alloy composition (45Cr26Ni33Si2Nb2)
The compositions in weight percent and atomic fractions (taken from the research paper) are:

| Element | Wt %   | At fraction |
|---------|--------|-------------|
| C       | 0.45   | 0.021       |
| Cr      | 26.9   | 0.285       |
| Ni      | 36.9   | 0.345       |
| Fe      | 29.8   | 0.295       |
| Mo      | 0.033  | 0.001       |
| Si      | 1.56   | 0.031       |
| Nb      | 2.0    | 0.012       |
| Mn      | 0.94   | 0.009       |
| Ti      | 0.18   | 0.002       |

Initial mass fractions of the major carbide‑forming elements are:
- C:   0.0045
- Cr:  0.269
- Nb:  0.02

### 2. Equilibrium constants (for the reactions given in the “Approach” section)
| T, °C | K₁   | K₅       |
|-------|------|----------|
| 800   | 1520 | 3.5×10⁶ |
| 1100  | 429  | 1.2×10⁵  |

### 3. Activity coefficients
- Chromium: γ_Cr = 1.0  
- Niobium: γ_Nb = 1.0  

The activity coefficient of carbon, γ_C, is computed using the Wagner‑type model for doped austenite:

\[
\log_{10} \gamma_{\text{C}} = \sum_i e_C^i \, [i],
\]

where \([i]\) denotes the atomic fraction of element \(i\) on a 0–1 scale (so for carbon \([C]=0.021\), for chromium \([Cr]=0.285\), etc.). The interaction parameters \(e_C^i\) are:

| Element i | e_C^i   |
|-----------|---------|
| C         | 0.14    |
| Cr        | -0.024  |
| Ni        | 0.012   |
| Si        | 0.08    |
| Mn        | -0.012  |
| Mo        | -0.008  |
| Nb        | -0.06   |

These values are treated as temperature‑independent over the range 800–1100 °C.

### 4. Conversion constant ν for mass fraction of Cr₂₃C₆
The mass of carbon bound in carbide and the carbide mass fraction are related by

\[
(C)_{\text{cb}} = \nu F,
\]

with

\[
\nu = \frac{n A_C}{n A_C + m A_{Cr}}.
\]

For Cr₂₃C₆, \(n=6\), \(m=23\), \(A_C = 12.011\), \(A_{Cr} = 52.00\), giving \(\nu \approx 0.057\). Use ν = 0.057 for all temperatures.

### 5. Experimental data for kinetic fitting
The experimentally measured mass fractions of Cr₂₃C₆ after 1000 h of isothermal aging are used to fit \(k_0\) and \(E_{\eta}\).

| Temperature, °C | Cr₂₃C₆ mass fraction after 1000 h |
|-----------------|----------------------------------|
| 800             | 0.0372                           |
| 900             | 0.0563                           |
| 1000            | 0.0618                           |

Additional data (not needed for fitting, but useful for consistency checks) show that the mass fractions at longer times (3200 h, 5300 h) approach a plateau.

### 6. Intensity ratio i₅/i₁
The intensity ratio i₅/i₁ characterises the relative driving force for the formation of NbC (reaction 5) and Cr₂₃C₆ (reaction 1) and is defined as

\[
\frac{i_5}{i_1} = \left(\frac{[Nb]_0}{[Nb]_{\text{eq}}}\right) \left(\frac{[Cr]_{\text{eq}}}{[Cr]_0}\right)^{23/6}.
\]

This ratio is calculated using the equilibrium concentrations obtained from the thermodynamic calculation.

## Reproduction target

1. **Equilibrium concentrations**: Compute the equilibrium atomic fractions \([C]_{\text{eq}}\), \([Cr]_{\text{eq}}\), \([Nb]_{\text{eq}}\), \([\text{NbC}]_{\text{eq}}\), and \([\text{Cr}_{23}\text{C}_6]_{\text{eq}}\) at 800 °C and 1100 °C, assuming no G‑phase, and report the intensity ratio i₅/i₁.
2. **Rate constants**: Estimate the forward reaction rate constants \(k_0\) (h⁻¹) and \(E_{\eta}\) (J/mol) for Cr₂₃C₆ precipitation by fitting the kinetic model to the experimental data above.
3. **Kinetic curves**: Using the fitted \(k_0\) and \(E_{\eta}\), numerically integrate the kinetic model to produce the Cr₂₃C₆ mass fraction as a function of time at 800, 900, 1000, and 1100 °C, covering at least the time points 1000 h, 3200 h, and 5300 h.
4. **Stabilization time**: For each of the four temperatures, determine τ∗, the time (in hours) required for the Cr₂₃C₆ mass fraction to reach 99 % of its equilibrium value.

## Workflow steps

### Step 1: Compute thermodynamic equilibrium concentrations
- Role: scored  
- Action: Solve the system of equations given in the “Thermodynamic equilibrium equations” section for 800 °C and 1100 °C. Because \(\gamma_C\) depends on the solution, use an iterative procedure: start with an initial guess for \(\gamma_C\) (e.g., 1.0), compute \([C]_{\text{eq}}\) from the material balance and equilibrium relations, then update \(\gamma_C\) from the new composition, and repeat until convergence. Compute the carbide molar fractions and the intensity ratio i₅/i₁ as defined.  
- Output file: `/app/outputs/equilibrium_concentrations.json`  
- Format: json  
- Contract: Array of objects, each with the fields `temperature_C` (number), `C_eq` (number), `Cr_eq` (number), `Nb_eq` (number), `NbC_eq` (number), `Cr23C6_eq` (number), `i5_over_i1` (number). All numeric values must be finite JSON numbers; do not use `NaN`, `Infinity`, or `undefined`. The array shall contain exactly two entries, one for 800 °C and one for 1100 °C.  
- Scoring: scored by hidden verifier.

### Step 2: Estimate kinetic rate constants k₀ and Eₙ
- Role: scored  
- Action: Implement the kinetic model described in the “Kinetic model” section. The conversion from atomic fractions to mass fractions requires the average atomic weight of the alloy:

\[
\bar{A} = \sum_i [i] A_i,
\]

where the sum runs over the major elements (C, Cr, Ni, Fe, Nb, Mn, Si, Ti) using the atomic fractions \([i]\) and atomic weights \(A_i\) (C: 12.011, Cr: 52.00, Ni: 58.69, Fe: 55.85, Nb: 92.906, Mn: 54.938, Si: 28.0855, Ti: 47.867). The equilibrium mass fraction of carbon is then

\[
(C)_{\text{eq}} = [C]_{\text{eq}} \, \frac{A_C}{\bar{A}}.
\]

Using the experimental Cr₂₃C₆ mass fractions at 800 °C, 900 °C, and 1000 °C after 1000 h, solve the inverse problem to determine \(k_0\) (h⁻¹) and \(E_{\eta}\) (J/mol). Any suitable fitting method may be used (e.g., least squares).  
- Output file: `/app/outputs/rate_constants.json`  
- Format: json  
- Contract: Object with the fields `k0` (number, h⁻¹) and `En` (number, J/mol). Both values must be finite JSON numbers.  
- Scoring: scored by hidden verifier.

### Step 3: Compute Cr₂₃C₆ kinetic curves
- Role: scored (load‑bearing)  
- Action: With the fitted \(k_0\) and \(E_{\eta}\), numerically integrate the kinetic model to obtain the mass fraction of Cr₂₃C₆ as a function of time at 800, 900, 1000, and 1100 °C, covering times up to at least 5300 h and including the specific aging times 1000 h, 3200 h, and 5300 h.  
- Output file: `/app/outputs/kinetic_curve.csv`  
- Format: csv  
- Contract: CSV with header: `temperature_C,time_h,Cr23C6_mass_fraction`. The columns must contain numeric values; `Cr23C6_mass_fraction` is a dimensionless mass fraction.  
- Scoring: scored by hidden verifier.

### Step 4: Calculate stabilization time τ∗
- Role: scored  
- Action: Define stabilization as the time required for the Cr₂₃C₆ mass fraction to reach 99 % of its equilibrium value at each temperature. Using the fitted model, compute the stabilization time (hours) for 800, 900, 1000, and 1100 °C.  
- Output file: `/app/outputs/stabilization_time.csv`  
- Format: csv  
- Contract: CSV with header: `temperature_C,tau_star_h`. Both columns must contain numeric values; `tau_star_h` is in hours.  
- Scoring: scored by hidden verifier.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_concentrations.json`
- `/app/outputs/rate_constants.json`
- `/app/outputs/kinetic_curve.csv`
- `/app/outputs/stabilization_time.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_concentrations.json
- path: `/app/outputs/equilibrium_concentrations.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Equilibrium atomic fractions and intensity ratio at 800 °C and 1100 °C. The file must be a valid JSON array of exactly two objects, one per temperature.
- schema:
  - `type`: array
  - `items`:
    - `temperature_C`: number
    - `C_eq`: number
    - `Cr_eq`: number
    - `Nb_eq`: number
    - `NbC_eq`: number
    - `Cr23C6_eq`: number
    - `i5_over_i1`: number

### rate_constants.json
- path: `/app/outputs/rate_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted forward reaction rate constants. Must be a valid JSON object with the two required numeric fields.
- schema:
  - `type`: object
  - `required`:
    - `k0`: number (h⁻¹)
    - `En`: number (J/mol)

### kinetic_curve.csv
- path: `/app/outputs/kinetic_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time evolution of Cr₂₃C₆ mass fraction at four temperatures.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `time_h`, `Cr23C6_mass_fraction`
  - `units`:
    - `temperature_C`: °C
    - `time_h`: hours
    - `Cr23C6_mass_fraction`: mass fraction (dimensionless)

### stabilization_time.csv
- path: `/app/outputs/stabilization_time.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stabilization time (τ∗) defined as time to reach 99 % equilibrium Cr₂₃C₆.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `tau_star_h`
  - `units`:
    - `temperature_C`: °C
    - `tau_star_h`: hours

## Important notes on JSON output
- Use standard JSON: **all numeric values must be finite real numbers** (no `NaN`, `Infinity`, `-Infinity`, or `undefined`). Use `0.0` for zero, ordinary decimal notation (e.g., `2.33e-3`) or scientific notation (e.g., `2.33e-3`) as produced by Python’s `json.dump`.
- The JSON files must be syntactically correct; for example, every object must be closed, arrays must be balanced, and string quotes must be properly escaped.
- If the computation yields a number smaller than `1e-12`, you may write it as `0.0` to avoid floating‑point underflow, but do not use `null` in place of a number.

## Notes
- The equilibrium calculation ignores the G‑phase.
- The kinetic model may be implemented by numerical integration or by using an analytical solution if the differential equation admits one; either approach is acceptable as long as the results are physically consistent.
- Results are compared to paper‑derived reference values within tolerances appropriate for different implementations.

## How you are scored
A hidden verifier independently evaluates each of the four required output artifacts. For the equilibrium concentrations, the verifier compares your computed atomic fractions and the intensity ratio to reference values. The kinetic rate constants are compared against expected magnitudes derived from the model. The kinetic curves are checked at selected time points (including 1000 h and longer aging times) for consistency with experimentally observed mass fractions, and the stabilization times are compared to the time ranges predicted by the model. Each artifact carries a weight; the individual scores are combined into the final reward. Artifacts that are missing, incorrectly formatted, or contain values far from the physically plausible range will receive low or zero credit.