# Water Saturation Properties from ITS‑90 Equations

## Problem background
Accurate thermodynamic properties of ordinary water, particularly on the vapor-liquid saturation line, are essential for a broad range of scientific and engineering applications.  The saturation behaviour is characterised by the vapor pressure, the densities of the coexisting liquid and vapour, and the corresponding specific enthalpies and entropies.  This task implements a set of correlation equations that express these properties as functions of temperature, adjusted to the International Temperature Scale of 1990 (ITS‑90).  The equations are valid for the entire saturation line from the triple point to the critical point, and the values they produce serve as reference data for industrial and scientific use.  The core challenge is to translate the analytical formulas and their coefficients into a correct, self‑contained computational implementation that yields accurate property values at a few specified verification temperatures.

## Approach
The method consists of implementing closed‑form analytical equations that directly give the vapor pressure, saturated‑liquid density, saturated‑vapor density, and two auxiliary quantities, as functions of temperature.  These are then combined with an analytic derivative of the vapor‑pressure equation to compute the specific enthalpies and specific entropies for both phases.

**Vapor pressure**  
The vapor pressure \(p\) follows a scaled exponential form in terms of the reduced temperature  
\(\tau = 1 - T/T_{\mathrm{c}}\):
\[
\ln\!\left(\frac{p}{p_{\mathrm{c}}}\right) = \frac{T_{\mathrm{c}}}{T}\bigl[a_{1}\tau + a_{2}\tau^{1.5} + a_{3}\tau^{3} + a_{4}\tau^{3.5} + a_{5}\tau^{4} + a_{6}\tau^{7.5}\bigr]
\]
with coefficients
\[
\begin{aligned}
a_{1} &= -7.85951783, & a_{2} &= 1.84408259, & a_{3} &= -11.7866497, \\
a_{4} &= 22.6807411,   & a_{5} &= -15.9618719,  & a_{6} &= 1.80122502 .
\end{aligned}
\]
The temperature derivative \(\mathrm{d}p/\mathrm{d}T\) must be obtained analytically from this expression (not by numerical differentiation).

**Saturated liquid density**  
The saturated‑liquid density \(\rho'\) relative to the critical density is
\[
\frac{\rho'}{\rho_{\mathrm{c}}} = 1 + b_{1}\tau^{1/3} + b_{2}\tau^{2/3} + b_{3}\tau^{5/3} + b_{4}\tau^{16/3} + b_{5}\tau^{43/3} + b_{6}\tau^{110/3}
\]
with
\[
\begin{aligned}
b_{1} &= 1.99274064,    & b_{2} &= 1.09965342,    & b_{3} &= -0.510839303, \\
b_{4} &= -1.75493479,   & b_{5} &= -45.5170352,   & b_{6} &= -6.74694450 \times 10^{5} .
\end{aligned}
\]

**Saturated vapor density**  
The saturated‑vapor density \(\rho''\) uses a similar logarithmic form:
\[
\ln\!\left(\frac{\rho''}{\rho_{\mathrm{c}}}\right) = c_{1}\tau^{2/6} + c_{2}\tau^{4/6} + c_{3}\tau^{8/6} + c_{4}\tau^{18/6} + c_{5}\tau^{37/6} + c_{6}\tau^{71/6}
\]
with
\[
\begin{aligned}
c_{1} &= -2.03150240, & c_{2} &= -2.68302940, & c_{3} &= -5.38626492, \\
c_{4} &= -17.2991605,  & c_{5} &= -44.7586581,  & c_{6} &= -63.9201063 .
\end{aligned}
\]

**Auxiliary quantities for enthalpy and entropy**  
Two auxiliary functions, \(\alpha\) and \(\phi\), are introduced:
\[
\frac{\alpha}{\alpha_{0}} = d_{\alpha} + d_{1}\theta^{-19} + d_{2}\theta + d_{3}\theta^{4.5} + d_{4}\theta^{5} + d_{5}\theta^{54.5}
\]
\[
\frac{\phi}{\phi_{0}} = d_{\phi} + \frac{19}{20}d_{1}\theta^{-20} + d_{2}\ln\theta + \frac{9}{7}d_{3}\theta^{3.5} + \frac{5}{4}d_{4}\theta^{4} + \frac{109}{107}d_{5}\theta^{53.5}
\]
where \(\theta = T/T_{\mathrm{c}}\).  The coefficients are
\[
\begin{aligned}
d_{1} &= -5.65134998 \times 10^{-8}, & d_{2} &= 2690.66631, & d_{3} &= 127.287297, \\
d_{4} &= -135.003439,               & d_{5} &= 0.981825814, \\
d_{\alpha} &= -1135.905627715,      & d_{\phi} &= 2319.5246 .
\end{aligned}
\]

**Reference constants**  
The reference constants are:
\[
\begin{aligned}
T_{\mathrm{c}} &= 647.096\;\text{K}, & p_{\mathrm{c}} &= 22.064 \times 10^{6}\;\text{Pa}, & \rho_{\mathrm{c}} &= 322\;\text{kg/m}^{3}, \\[2mm]
\alpha_{0} &= 1000\;\text{J/kg}, & \phi_{0} &= \alpha_{0}/T_{\mathrm{c}} .
\end{aligned}
\]

**Specific enthalpy and entropy**  
Once \(\rho'\), \(\rho''\), \(\alpha\), \(\phi\), and \(\mathrm{d}p/\mathrm{d}T\) have been computed at a given temperature, the specific enthalpies and entropies follow from
\[
\begin{aligned}
h'    &= \alpha + \frac{T}{\rho'}\,\frac{\mathrm{d}p}{\mathrm{d}T}, \qquad
h''   = \alpha + \frac{T}{\rho''}\,\frac{\mathrm{d}p}{\mathrm{d}T}, \\[2mm]
s'    &= \phi   + \frac{1}{\rho'}\,\frac{\mathrm{d}p}{\mathrm{d}T}, \qquad
s''   = \phi   + \frac{1}{\rho''}\,\frac{\mathrm{d}p}{\mathrm{d}T} .
\end{aligned}
\]
The overall recipe is strictly sequential: (1) compute \(\tau\) and \(\theta\); (2) evaluate \(p\) and \(\mathrm{d}p/\mathrm{d}T\); (3) evaluate \(\rho'\), \(\rho''\), \(\alpha\), \(\phi\); (4) combine to obtain \(h'\), \(h''\), \(s'\), \(s''\).  No external datasets or fitting steps are needed; all constants are hard‑coded as given above.

## Reproduction target
Compute all of the following quantities — vapor pressure \(p\), its temperature derivative \(\mathrm{d}p/\mathrm{d}T\), saturated‑liquid density \(\rho'\), saturated‑vapor density \(\rho''\), auxiliary \(\alpha\), specific enthalpy of saturated liquid \(h'\), specific enthalpy of saturated vapor \(h''\), auxiliary \(\phi\), specific entropy of saturated liquid \(s'\), and specific entropy of saturated vapor \(s''\) — at the three fixed temperatures:  
– \(T = 273.16\;\text{K}\)  
– \(T = 373.1243\;\text{K}\)  
– \(T = 647.096\;\text{K}\) .  

Write the results to the file `/app/outputs/saturation_properties.json`.  This JSON file must be an array of three objects, one per temperature, each containing the fields listed in the output contract.  The exact order of the array entries is not prescribed; each entry is identified by its `temperature` field.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Compute Saturation Property Values
- Role: scored (load-bearing)
- Action: Implement the ITS‑90 correlation equations for vapor pressure (Eq.1), saturated liquid density (Eq.2), saturated vapor density (Eq.3), auxiliary α (Eq.4) and φ (Eq.5) using the explicit coefficients and reference constants from the supplementary release. Compute dp/dT analytically from Eq.1. Then compute specific enthalpy of saturated liquid h′ (Eq.6), saturated vapor h″ (Eq.7), specific entropy of saturated liquid s′ (Eq.8) and saturated vapor s″ (Eq.9) using the computed densities and dp/dT. Evaluate all quantities at T = 273.16 K, 373.1243 K, and 647.096 K. Output the results as a JSON file.
- Output file: `/app/outputs/saturation_properties.json`
- Format: json
- Contract: Array of three objects. Each object must contain numeric fields: temperature (K), p (Pa), dp_dT (Pa/K), rho_prime (kg/m³), rho_double_prime (kg/m³), alpha (J/kg), h_prime (J/kg), h_double_prime (J/kg), phi (J/(kg·K)), s_prime (J/(kg·K)), s_double_prime (J/(kg·K)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/saturation_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### saturation_properties.json
- path: `/app/outputs/saturation_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed saturation property values at T = 273.16 K, 373.1243 K, and 647.096 K. Exact ordering of array entries does not matter; each entry is identified by its temperature field.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `temperature`, `p`, `dp_dT`, `rho_prime`, `rho_double_prime`, `alpha`, `h_prime`, `h_double_prime`, `phi`, `s_prime`, `s_double_prime`
  - `units`:
    - `temperature`: K
    - `p`: Pa
    - `dp_dT`: Pa/K
    - `rho_prime`: kg/m^3
    - `rho_double_prime`: kg/m^3
    - `alpha`: J/kg
    - `h_prime`: J/kg
    - `h_double_prime`: J/kg
    - `phi`: J/(kg·K)
    - `s_prime`: J/(kg·K)
    - `s_double_prime`: J/(kg·K)

Notes: All necessary coefficients and constants are given in the paper's appendix and must be hard‑coded into the implementation. The agent should compute dp/dT analytically from the vapor‑pressure equation (Eq.1) to avoid numerical differentiation errors.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "saturation_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "temperature",
            "p",
            "dp_dT",
            "rho_prime",
            "rho_double_prime",
            "alpha",
            "h_prime",
            "h_double_prime",
            "phi",
            "s_prime",
            "s_double_prime"
          ]
        },
        "units": {
          "temperature": "K",
          "p": "Pa",
          "dp_dT": "Pa/K",
          "rho_prime": "kg/m^3",
          "rho_double_prime": "kg/m^3",
          "alpha": "J/kg",
          "h_prime": "J/kg",
          "h_double_prime": "J/kg",
          "phi": "J/(kg·K)",
          "s_prime": "J/(kg·K)",
          "s_double_prime": "J/(kg·K)"
        }
      },
      "description": "Computed saturation property values at T = 273.16 K, 373.1243 K, and 647.096 K. Exact ordering of array entries does not matter; each entry is identified by its temperature field."
    }
  ],
  "notes": "All necessary coefficients and constants are given in the paper's appendix and must be hard‑coded into the implementation. The agent should compute dp/dT analytically from the vapor‑pressure equation (Eq.1) to avoid numerical differentiation errors."
}
```

## How you are scored
Your submission will be evaluated by a hidden, deterministic verifier that reads `/app/outputs/saturation_properties.json`.  The verifier compares every numeric field of each temperature entry to a hidden reference (which is the correct result of applying the equations given above).  No other artifact or process evidence is considered.  The overall score is the fraction of the individual numeric property values across all three temperatures that fall within a suitable tolerance; all fields contribute equally.  You do not need to know the reference values or the tolerances — just implement the equations correctly using the constants provided in the approach section, compute `dp/dT` analytically, and follow the specified output schema.
