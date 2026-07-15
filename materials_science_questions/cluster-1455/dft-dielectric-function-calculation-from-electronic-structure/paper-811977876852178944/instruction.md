# Computation of pressure derivatives of static dielectric constant and optical mode Grüneisen parameters for alkali halides from higher-order elastic constants

## Problem background
The anharmonic behaviour of ionic crystals can be characterised through the pressure derivatives of their dielectric constants and through higher-order elastic constants. This task implements the interrelationship between these quantities and applies it to 15 NaCl-structure alkali halide crystals (LiF, LiCl, LiBr, NaF, NaCl, NaBr, NaI, KF, KCl, KBr, KI, RbF, RbCl, RbBr, RbI). Using published input data for elastic constants, dielectric constants, and crystal volumes, you will compute the volume and pressure derivatives of the static dielectric constant and the optical mode Grüneisen parameters. The goal is to produce these physical quantities from the interrelationship formulas and to demonstrate the utility of the interrelationship approach for predicting high-pressure dielectric behaviour.

## Approach
The method derives analytical links between the volume/pressure derivatives of the static dielectric constant ε₀ and the second-, third-, and fourth-order elastic constants. Starting from the Clausius‑Mosotti/Lorentz‑Lorenz relation, the ion‑displacement polarizability α_i is expressed in terms of ε₀, ε∞, and the crystal volume V. Volume derivatives of ε₀ are expressed through derivatives of α_i and derivatives of ε∞. The short‑range force constant A and its volume derivatives are obtained from the higher‑order elastic constants via the equations of state, assuming a short‑range potential and the Born model for ionic crystals. These force‑constant derivatives then give the volume derivatives of α_i (with volume‑independent effective charge) and, in turn, the volume derivatives of ε₀. Using the isothermal bulk modulus and its volume derivative, the volume derivatives are transformed to pressure derivatives. Finally, the transverse and longitudinal optical mode Grüneisen parameters γ_TO and γ_LO are obtained from the force‑constant derivative and the dielectric-constant derivatives. The entire workflow is implemented numerically for the 15 crystals using material constants compiled from published literature.

## Key formulas

The computation uses the following equations, taken directly from the published derivation.

**Clausius–Mossotti / Lorentz–Lorenz relation**
$$
\frac{\varepsilon_0-1}{\varepsilon_0+2} - \frac{\varepsilon_\infty-1}{\varepsilon_\infty+2} = \frac{4\pi}{3V}\,\alpha_i \tag{1}
$$

**First volume derivative of \(\varepsilon_0\)**
$$
V\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}V} = 
\left[
\frac{4\pi}{3}\frac{\mathrm{d}\alpha_i}{\mathrm{d}V} - \frac{4\pi}{3V}\alpha_i + \frac{3V}{(\varepsilon_\infty+2)^2}\frac{\mathrm{d}\varepsilon_\infty}{\mathrm{d}V}
\right]
\frac{(\varepsilon_0+2)^2}{3} \tag{2}
$$

**Second volume derivative of \(\varepsilon_0\)**
$$
\begin{aligned}
V^2\frac{\mathrm{d}^2\varepsilon_0}{\mathrm{d}V^2} = 
\Bigg[
& \frac{4\pi}{3} V\frac{\mathrm{d}^2\alpha_i}{\mathrm{d}V^2} - \frac{8\pi}{3}\frac{\mathrm{d}\alpha_i}{\mathrm{d}V} + \frac{8\pi}{3V}\alpha_i \\
& + \frac{6}{(\varepsilon_0+2)^2}\left(V\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}V}\right)^2
+ \frac{3}{(\varepsilon_\infty+2)^2} V^2\frac{\mathrm{d}^2\varepsilon_\infty}{\mathrm{d}V^2} \\
& - \frac{6}{(\varepsilon_\infty+2)^3}\left(V\frac{\mathrm{d}\varepsilon_\infty}{\mathrm{d}V}\right)^2
\Bigg] \frac{(\varepsilon_0+2)^2}{3} \tag{3}
\end{aligned}
$$

**Transformation from volume to pressure derivatives**
$$
\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}P} = -\frac{V}{B_T}\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}V} \tag{4}
$$
$$
\frac{\mathrm{d}^2\varepsilon_0}{\mathrm{d}P^2} = 
-\frac{1}{B_T}\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}P}
+ \frac{V}{B_T^2}\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}P}\frac{\mathrm{d}B_T}{\mathrm{d}V}
+ \frac{V^2}{B_T^2}\frac{\mathrm{d}^2\varepsilon_0}{\mathrm{d}V^2} \tag{5}
$$

**Force constant \(A\) and its volume derivatives from elastic constants**

Define \(x = 2\) for NaCl‑structure crystals, \(r = (V/2)^{1/3}\) (the nearest‑neighbour distance, because \(V\) is the volume per ion pair and \(V = 2r^3\)).  At ambient pressure (\(P = 0\)):

$$
A = -3x\,r\,V P^{\rm I} \qquad (\textrm{since }P=0) \tag{17}
$$

$$
\frac{V}{A}\frac{\mathrm{d}A}{\mathrm{d}V} = 
\frac{3V^2 P^{\rm II} + 8 V P^{\rm I}}{3 V P^{\rm I}} \tag{18}
$$

$$
\frac{V^2}{A}\frac{\mathrm{d}^2A}{\mathrm{d}V^2} = 
\frac{3V^3 P^{\rm III} + 12 V^2 P^{\rm II} + 4 V P^{\rm I}}{3 V P^{\rm I}} \tag{19}
$$

**Pressure – volume derivatives from elastic constants**
$$
P^{\rm I} = \frac{C_{11}+2C_{12}}{3V} \tag{20}
$$
$$
P^{\rm II} = \frac{3(C_{11}+2C_{12}) - (C_{111}+6C_{112}+2C_{123})}{9V^2} \tag{21}
$$
$$
\begin{aligned}
P^{\rm III} = \frac{1}{27V^3}\Big[
& (C_{11}+2C_{12}) + 3(C_{111}+6C_{112}+2C_{123}) + C_{1111} + 8C_{1112} \\
& + 6C_{1122} + 12C_{1123} - \frac{(C_{111}+6C_{112}+2C_{123})^2}{C_{11}+2C_{12}} \\
& + (C_{11}+2C_{12})\left(3 - \frac{C_{111}+6C_{112}+2C_{123}}{C_{11}+2C_{12}}\right)
\left(6 - \frac{C_{111}+6C_{112}+2C_{123}}{C_{11}+2C_{12}}\right)
\Big] \tag{22}
\end{aligned}
$$

**Volume derivative of the bulk modulus**

At \(P=0\):
$$
B_T = \frac{A}{3x r} = \frac{A}{6r} \qquad (\text{also } B_T = -V P^{\rm I}) \tag{14}
$$
$$
\frac{\mathrm{d}B_T}{\mathrm{d}V} = \frac{A}{6x r^4}\left(\frac{V}{A}\frac{\mathrm{d}A}{\mathrm{d}V} - \frac{5}{3}\right) \tag{15}\text{ with }x=2
$$

**Ion‑displacement polarizability \(\alpha_i\) and its volume derivatives**

From (1) one obtains \(\alpha_i = \frac{3V}{4\pi}\!\left[\frac{\varepsilon_0-1}{\varepsilon_0+2} - \frac{\varepsilon_\infty-1}{\varepsilon_\infty+2}\right]\).

Assuming the effective charge \(Z'\) is volume‑independent:
$$
\frac{\mathrm{d}\alpha_i}{\mathrm{d}V} = -\frac{\alpha_i}{V}\,\frac{V}{A}\frac{\mathrm{d}A}{\mathrm{d}V} \tag{9}
$$
$$
V\frac{\mathrm{d}^2\alpha_i}{\mathrm{d}V^2} = -\frac{\alpha_i}{V}\!
\left[\frac{V^2}{A}\frac{\mathrm{d}^2A}{\mathrm{d}V^2} - 2\!
\left(\frac{V}{A}\frac{\mathrm{d}A}{\mathrm{d}V}\right)^{\!2}\right] \tag{10}
$$

**Optical mode Grüneisen parameters**
$$
\gamma_{\mathrm{TO}} = -\frac12\!
\left(\frac{V}{A}\frac{\mathrm{d}A}{\mathrm{d}V} - \frac{V}{\varepsilon_0+2}\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}V} + \frac{V}{\varepsilon_\infty+2}\frac{\mathrm{d}\varepsilon_\infty}{\mathrm{d}V}\right) \tag{11}
$$
$$
\gamma_{\mathrm{LO}} = \gamma_{\mathrm{TO}} - \frac12\!
\left(\frac{V}{\varepsilon_0}\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}V} - \frac{V}{\varepsilon_\infty}\frac{\mathrm{d}\varepsilon_\infty}{\mathrm{d}V}\right) \tag{12}
$$

**Normalised output quantities**
$$
\frac{1}{\varepsilon_0}\frac{\mathrm{d}\varepsilon_0}{\mathrm{d}P} \quad \text{in }10^{-11}\,\mathrm{Pa}^{-1},\qquad
\frac{1}{\varepsilon_0^2}\frac{\mathrm{d}^2\varepsilon_0}{\mathrm{d}P^2} \quad \text{in }10^{-22}\,\mathrm{Pa}^{-2}
$$

## Reproduction target
For each of the 15 crystals produce the following three CSV files:

1. **volume_derivatives.csv** — the first volume derivative V·dε₀/dV and the second volume derivative V²·d²ε₀/dV².
2. **gruneisen_parameters.csv** — the transverse optical mode Grüneisen parameter γ_TO and the longitudinal optical mode Grüneisen parameter γ_LO.
3. **pressure_derivatives.csv** — the normalised first pressure derivative (1/ε₀)·dε₀/dP (in 10⁻¹¹ Pa⁻¹) and the normalised second pressure derivative (1/ε₀²)·d²ε₀/dP² (in 10⁻²² Pa⁻²).

All quantities are computed from the public input data using the interrelationship formulas described in the approach. The hidden verifier compares your computed values to reference calculated values.

## Assets

- Elastic constants from Bhende et al. (1985)
- Elastic constants from Garg et al. (1977)
- Dielectric data from Jones (1967)
- Dielectric data from Lowndes & Martin (1970)
- Dielectric data from Mahmud et al. (1971)
- Dielectric data from Fontanella et al. (1972)
- NumPy: numpy

## Workflow steps

### Step 1: Compile material constants from literature
- Role: process
- Action: For each of the 15 NaCl-structure alkali halide crystals (LiF, LiCl, LiBr, NaF, NaCl, NaBr, NaI, KF, KCl, KBr, KI, RbF, RbCl, RbBr, RbI), obtain the second-, third-, and fourth-order elastic constants (C11, C12, C111, C112, C123, C1111, C1112, C1122, C1123), the static (ε0) and high-frequency (ε∞) dielectric constants, the crystal volume V, the isothermal bulk modulus BT, and the volume derivatives dε∞/dV and d²ε∞/dV² from the published literature sources. Compile a single table of required input parameters.
- Evidence: `/app/outputs/compiled_input_data.csv`

### Step 2: Compute short-range force constant A and its volume derivatives
- Role: process
- Action: Using the compiled elastic constants and crystal volume, compute the short-range force constant A and the normalized volume derivatives (V/A)dA/dV and (V²/A)d²A/dV² at ambient pressure (P=0) via the interrelationship formulas that connect A to pressure-volume derivatives and elastic constants.
- Evidence: `/app/outputs/force_constant_A.csv`

### Step 3: Determine ionic polarizability and effective charge
- Role: process
- Action: From the experimental ε0, ε∞, and V, compute the ion-displacement polarizability α_i using the Clausius-Mosotti/Lorentz-Lorenz relation. Then, using the force constant A, determine the effective ionic charge Z' such that α_i = (Z'e)²/A. Report α_i and Z' for each crystal.
- Evidence: `/app/outputs/polarizability.csv`

### Step 4: Compute volume derivatives of static dielectric constant
- Role: scored
- Action: Using the previously determined α_i and its volume derivatives (computed from A derivatives assuming volume-independent Z'), together with the volume derivatives of ε∞ from literature, solve the first- and second-order volume-derivative formulas for ε0 to obtain V dε0/dV and V² d²ε0/dV² for each crystal.
- Output file: `/app/outputs/volume_derivatives.csv`
- Format: csv
- Contract: crystal (str), V_d_eps0_dV (float), V2_d2_eps0_dV2 (float)
- Scoring: scored by hidden verifier

### Step 5: Compute optical mode Grüneisen parameters
- Role: scored
- Action: Using the force constant volume derivative (V/A)dA/dV and the volume derivatives of ε0 and ε∞, calculate the transverse and longitudinal optical mode Grüneisen parameters γ_TO and γ_LO for each crystal.
- Output file: `/app/outputs/gruneisen_parameters.csv`
- Format: csv
- Contract: crystal (str), gamma_TO (float), gamma_LO (float)
- Scoring: scored by hidden verifier

### Step 6: Compute normalized pressure derivatives of static dielectric constant
- Role: scored (load-bearing)
- Action: Transform the volume derivatives of ε0 into pressure derivatives using the isothermal bulk modulus BT and its volume derivative. Report the normalized first and second pressure derivatives: (1/ε0)·dε0/dP (in 10^{-11} Pa^{-1}) and (1/ε0²)·d²ε0/dP² (in 10^{-22} Pa^{-2}) for each crystal.
- Output file: `/app/outputs/pressure_derivatives.csv`
- Format: csv
- Contract: crystal (str), d_eps0_dP_normalized (float), d2_eps0_dP2_normalized (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/volume_derivatives.csv`
- `/app/outputs/gruneisen_parameters.csv`
- `/app/outputs/pressure_derivatives.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### volume_derivatives.csv
- path: `/app/outputs/volume_derivatives.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: First and second volume derivatives of the static dielectric constant for each crystal. The hidden checker compares these values to the paper's reported calculated values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `crystal`, `V_d_eps0_dV`, `V2_d2_eps0_dV2`
  - `units`: object

### gruneisen_parameters.csv
- path: `/app/outputs/gruneisen_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Transverse and longitudinal optical mode Grüneisen parameters for each crystal, compared to paper's Table 3.
- schema:
  - `type`: table
  - `required_columns`: `crystal`, `gamma_TO`, `gamma_LO`
  - `units`: object

### pressure_derivatives.csv
- path: `/app/outputs/pressure_derivatives.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized first and second pressure derivatives of the static dielectric constant, corresponding to Table 4. These are the main headline quantities.
- schema:
  - `type`: table
  - `required_columns`: `crystal`, `d_eps0_dP_normalized`, `d2_eps0_dP2_normalized`
  - `units`:
    - `d_eps0_dP_normalized`: 10^{-11} Pa^{-1}
    - `d2_eps0_dP2_normalized`: 10^{-22} Pa^{-2}

Notes: All three outputs are CSV files with one row per crystal. The checker compares each numeric value to the paper's reported calculated results using absolute tolerances appropriate for the precision of the method.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "volume_derivatives.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crystal",
          "V_d_eps0_dV",
          "V2_d2_eps0_dV2"
        ],
        "units": {}
      },
      "description": "First and second volume derivatives of the static dielectric constant for each crystal. The hidden checker compares these values to the paper's reported calculated values with appropriate tolerances."
    },
    {
      "file": "gruneisen_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crystal",
          "gamma_TO",
          "gamma_LO"
        ],
        "units": {}
      },
      "description": "Transverse and longitudinal optical mode Grüneisen parameters for each crystal, compared to paper's Table 3."
    },
    {
      "file": "pressure_derivatives.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crystal",
          "d_eps0_dP_normalized",
          "d2_eps0_dP2_normalized"
        ],
        "units": {
          "d_eps0_dP_normalized": "10^{-11} Pa^{-1}",
          "d2_eps0_dP2_normalized": "10^{-22} Pa^{-2}"
        }
      },
      "description": "Normalized first and second pressure derivatives of the static dielectric constant, corresponding to Table 4. These are the main headline quantities."
    }
  ],
  "notes": "All three outputs are CSV files with one row per crystal. The checker compares each numeric value to the paper's reported calculated results using absolute tolerances appropriate for the precision of the method."
}
```

## How you are scored
Each of the three scored CSV files is evaluated independently by a hidden verifier. The verifier compares every computed value in your submission against a hidden reference value (the paper’s own calculated result) using an absolute tolerance. A value that falls within the tolerance earns full credit for that entry; values outside tolerance reduce the score proportionally. The final reward is the average of the per‑entry scores, with equal weight distributed across all crystals and across the three artifacts. Reporting the expected numbers without genuinely executing the calculation is not sufficient — the verifier checks that your submitted numeric results match the reference within the specified tolerance margins.
