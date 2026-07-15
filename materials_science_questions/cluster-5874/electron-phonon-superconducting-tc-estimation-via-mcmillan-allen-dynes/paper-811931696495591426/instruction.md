# Electron-Phonon Superconducting Tc Estimation via McMillan-Allen-Dynes for Binary Metallic Glasses

## Problem background
Superconducting state parameters (SSPs) – electron‑phonon coupling λ, Coulomb pseudopotential μ*, transition temperature T_C, isotope effect exponent α, and effective interaction N0V – govern the superconducting behavior of amorphous metals. Accurately computing these quantities for binary metallic glasses helps identify promising superconductors and understand composition‑property trends. This task reproduces a pseudo‑potential framework that computes SSPs for a large set of binary metallic glasses using Ashcroft's empty‑core model potential and five different local‑field correction functions, combined with the pseudo‑alloy‑atom (PAA) mixing rules.

## Approach
We treat each binary metallic glass A₁₋C B_C as a pseudo‑alloy‑atom with averaged properties Z, M, Ω₀, θ_D computed from the constituent elements (Table 1 values). The Ashcroft empty‑core pseudopotential W(q) is used together with a modified Hartree dielectric function ε(q) that incorporates one of five local‑field corrections (Hartree H, Taylor T, Ichimaru‑Utsumi IU, Farid F, and Sarkar S). The electron‑phonon coupling strength λ and the Coulomb pseudopotential μ* are obtained by numerically integrating their respective formulas over the reduced wave‑vector variable X = q/(2k_F) from 0 to 1. From λ and μ*, the transition temperature T_C (McMillan/Allen‑Dynes relation), isotope effect exponent α, and effective interaction strength N₀V are then calculated. The same fixed core‑radius r_C (from Table 1) is used for all screenings; no re‑fitting is performed. This pipeline is repeated for every metallic glass and every screening function, producing a comprehensive set of SSPs that reveals how the choice of local‑field correction influences the computed superconducting properties.

## Key Formulas

- **Phonon frequency**: $\langle\omega^2\rangle^{1/2}=0.69\,\theta_D$.
- **Electron-phonon coupling $\lambda$**:
  $$\lambda=\frac{12 m Z}{M\langle\omega^2\rangle}\int_0^1 X^3|W(X)|^2 dX$$
  where $m$ is the electron mass, $Z$ and $M$ are the alloy valence and ionic mass, $\Omega_O$ atomic volume, $k_F=(3\pi^2 Z/\Omega_O)^{1/3}$ the Fermi wave vector.
- **Screened pseudopotential $W(X)$** (Ashcroft empty core):
  $$W(X)=-\frac{2\pi Z}{\Omega_O X^2 k_F^2 \varepsilon(X)}\cos(2 k_F X r_C)$$
  $r_C$ is the core radius from Table 1.
- **Dielectric function**:
  $$\varepsilon(X)=1+(\varepsilon_H(X)-1)(1-f(X))$$
  The static Hartree dielectric function:
  $$\varepsilon_H(X)=1+\frac{m e^2}{2\pi k_F\hbar^2 X^2}\left[\frac{1-X^2}{2X}\ln\left|\frac{1+X}{1-X}\right|+1\right]$$
  (with $e$ elementary charge, $\hbar$ reduced Planck constant).
- **Local-field corrections $f(X)$**:
  - **Hartree (H)**: $f(X)=0$
  - **Taylor (T)**: $f(X)=X^2\left[1+\frac{0.1534}{\pi k_F^2}\right]$
  - **Ichimaru-Utsumi (IU)**: Let $Q=2X$,
    $$f_{\text{IU}}(X)=A_{\text{IU}} Q^4 + B_{\text{IU}} Q^2 + C_{\text{IU}} + \left[A_{\text{IU}} Q^4 + (B_{\text{IU}}+\frac{8A_{\text{IU}}}{3}) Q^2 - C_{\text{IU}}\right]\frac{4-Q^2}{4Q}\ln\left|\frac{2+Q}{2-Q}\right|$$
    The parameters $A_{\text{IU}}, B_{\text{IU}}, C_{\text{IU}}$ are functions of the electron gas parameter $r_s = \left(\frac{3}{4\pi n}\right)^{1/3}/a_B$ with $n=Z/\Omega_O$ and $a_B$ the Bohr radius; their exact expressions are given in Ichimaru & Utsumi (1981), Phys. Rev. B **24**, 3220, Eqs. (2.15)–(2.17).
  - **Farid et al. (F)**: same functional form but with $A_F, B_F, C_F, D_F$ and the logarithmic term prefactor replaced by $D_F Q^2 - C_F$:
    $$f_{\text{F}}(X)=A_F Q^4 + B_F Q^2 + C_F + \left[A_F Q^4 + D_F Q^2 - C_F\right]\frac{4-Q^2}{4Q}\ln\left|\frac{2+Q}{2-Q}\right|$$
    The parameters are defined in Farid et al. (1993), Phys. Rev. B **48**, 11602; implement them precisely as described there.
  - **Sarkar et al. (S)**:
    $$f_{\text{S}}(X)=A_S\left\{1-\left(1+B_S Q^4\right)\exp(-C_S Q^2)\right\},\quad Q=2X$$
    The parameters $A_S, B_S, C_S$ are specified in Sarkar et al. (1998), Mod. Phys. Lett. B **12**, 639; use their explicit formulas.
- **Coulomb pseudopotential $\mu^*$**:
  $$\mu^* = \frac{\frac{m}{\pi k_F}\int_0^1 \frac{dX}{\varepsilon(X)}}{1+\frac{m}{\pi k_F}\ln\left(\frac{E_F}{10\,\theta_D}\right)\int_0^1 \frac{dX}{\varepsilon(X)}}$$
  where $E_F=\frac{\hbar^2 k_F^2}{2m}$.
- **Transition temperature $T_C$** (McMillan/Allen-Dynes):
  $$T_C = \frac{\theta_D}{1.45}\exp\left[-\frac{1.04(1+\lambda)}{\lambda-\mu^*(1+0.62\lambda)}\right]$$
- **Isotope effect exponent $\alpha$**:
  $$\alpha = \frac12\left[1-\left(\mu^*\ln\frac{\theta_D}{1.45 T_C}\right)^2\frac{1+0.62\lambda}{1.04(1+\lambda)}\right]$$
- **Effective interaction strength $N_0 V$**:
  $$N_0 V = \frac{\lambda-\mu^*}{1+\frac{10}{11}\lambda}$$

Numerical integration over $X\in[0,1]$ can be performed with a standard quadrature (e.g., Simpson's rule with sufficient points).  The gold verifier uses the exact parameter definitions from the original references for the IU, F, and S local-field corrections.

## Reproduction target
For every binary metallic glass provided in the input file `data/alloy_inputs.csv` (parameters from Table 1), compute the five SSPs – λ, μ*, T_C (Kelvin), α, and N₀V – using each of the five local‑field correction functions: H, T, IU, F, S. Output a single CSV file `step_02_ssp_results.csv` containing one row per glass and screening combination. The required columns are glass (string), screening (one of 'H','T','IU','F','S'), lambda, mu_star, Tc, alpha, N0V. The computed values must be numerically consistent with the physical model described above, and the T_C ordering across the five screenings must be correctly determined for each glass.

## Assets

- Alloy input parameters (Z, r_C, Ω₀, θ_D) from Table 1: data/alloy_inputs.csv

## Workflow steps

### Step 1: Prepare alloy input parameters
- Role: process
- Action: Read the provided alloy_inputs.csv file. For each metallic glass, compute the alloy’s average ionic mass M using the pseudo-alloy-atom (PAA) mixing rule M = (1-C)*M_A + C*M_B, where M_A and M_B are the standard atomic masses of the two elements. Record the final per-glass parameters: Z, r_C, Ω_O, θ_D, M.
- Evidence: `/app/outputs/step_01_params.json`

### Step 2: Compute Superconducting State Parameters
- Role: scored (load-bearing)
- Action: For each metallic glass in the input parameter set and for each local-field correction function (H, T, IU, F, S): implement the Ashcroft empty-core pseudopotential (EMC) with the modified Hartree dielectric function incorporating the chosen local-field correction. Numerically integrate the electron-phonon coupling strength λ and Coulomb pseudopotential μ* formulas over the variable X from 0 to 1. Then compute the transition temperature T_C, isotope effect exponent α, and effective interaction strength N0V using the McMillan-style relations. Use the fixed core radius r_C given in the input; do not refit. Output all computed values as a CSV file.
- Output file: `/app/outputs/step_02_ssp_results.csv`
- Format: csv
- Contract: CSV with columns: glass (string), screening (string, one of 'H','T','IU','F','S'), lambda (float), mu_star (float), Tc (float, in Kelvin), alpha (float), N0V (float). One row per glass × screening combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_ssp_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_ssp_results.csv
- path: `/app/outputs/step_02_ssp_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The main scored artifact containing computed SSPs. The hidden checker compares each row's λ, μ*, T_C, α, N0V to the paper's reported values with per-quantity tolerances and verifies that for every glass the ordering of T_C across screenings is H < T < S < IU < F.
- schema:
  - `type`: table
  - `required_columns`: `glass`, `screening`, `lambda`, `mu_star`, `Tc`, `alpha`, `N0V`
  - `units`:
    - `Tc`: K

Notes: Only step_02_ssp_results.csv is scored. The evidence file from step 1 is for documentation and is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_ssp_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "glass",
          "screening",
          "lambda",
          "mu_star",
          "Tc",
          "alpha",
          "N0V"
        ],
        "units": {
          "Tc": "K"
        }
      },
      "description": "The main scored artifact containing computed SSPs. The hidden checker compares each row's λ, μ*, T_C, α, N0V to the paper's reported values with per-quantity tolerances and verifies that for every glass the ordering of T_C across screenings is H < T < S < IU < F."
    }
  ],
  "notes": "Only step_02_ssp_results.csv is scored. The evidence file from step 1 is for documentation and is not scored."
}
```

## How you are scored
A hidden verifier will inspect your output file `step_02_ssp_results.csv`. It compares each computed SSP to a hidden reference set (derived from the same physical model) with relative tolerances. It also checks that for each glass, the T_C values obey a specific relative ordering among the five screenings. The final reward (a real number between 0 and 1) is a weighted combination of how many glass‑screening combinations fall within the tolerance across all SSPs, plus a bonus for the correct T_C ordering. Reporting only the raw numbers is not sufficient; the verifier independently assesses the self‑consistency and accuracy of your computed results. No gold values or tolerances are disclosed in these instructions.
