# Numerical study of the unbalanced superconducting state on a square lattice within the Eliashberg formalism

## Problem background
Superconductivity can arise from the electron‑phonon interaction, but the influence of unbalanced coupling – where the strength in the diagonal (mass‑renormalisation) channel differs from that in the off‑diagonal (pairing) channel – is not fully understood in low‑dimensional systems. This task investigates whether a phonon‑induced superconducting state can exist on a two‑dimensional square lattice when the coupling constants in the two channels are unequal. The degree of unbalance is controlled by a single parameter γ = λ_D / λ_ND, and the key question is: what is the critical value γ_C below which a superconducting condensate survives when the Eliashberg equations are solved with full momentum and frequency self‑consistency? The answer must be obtained numerically, and the thermodynamic properties of the state must be compared with the expectations of BCS theory. The task is to compute γ_C and a set of dimensionless thermodynamic ratios (R_Δ, R_C, R_H) for several values of γ, thereby directly testing the model’s predictions.

## Mathematical formulation

### Eliashberg equations on the square lattice
The fully self‑consistent Eliashberg equations for the order‑parameter function φ_k(iω_n) and the wave‑function renormalisation factor Z_k(iω_n) on a square lattice are

\[
\varphi_{\mathbf{k}}(i\omega_n) = \frac{1}{\beta N} \sum_{m\mathbf{q}} K_{\mathbf{q}}(\omega_n - \omega_m) \frac{\varphi_{\mathbf{k} - \mathbf{q}}(i\omega_m)}{D_{\mathbf{k} - \mathbf{q}}(i\omega_m)},
\tag{1}
\]

\[
Z_{\mathbf{k}}(i\omega_n) = 1 + \frac{\gamma}{\beta N} \sum_{m\mathbf{q}} \frac{\omega_m}{\omega_n} K_{\mathbf{q}}(\omega_n - \omega_m) \frac{Z_{\mathbf{k} - \mathbf{q}}(i\omega_m)}{D_{\mathbf{k} - \mathbf{q}}(i\omega_m)}.
\tag{2}
\]

The physical order parameter is \(\Delta_{\mathbf{k}}(i\omega_n) = \varphi_{\mathbf{k}}(i\omega_n) / Z_{\mathbf{k}}(i\omega_n)\).  
The pairing kernel is

\[
K_{\mathbf{q}}(\omega_n - \omega_m) = 2 g_{\mathbf{q}}^2 \frac{\omega_{\mathbf{q}}}{(\omega_n - \omega_m)^2 + \omega_{\mathbf{q}}^2},
\]

and the denominator

\[
D_{\mathbf{k}}(i\omega_n) = \bigl(\omega_n Z_{\mathbf{k}}(i\omega_n)\bigr)^2 + \varepsilon_{\mathbf{k}}^2 + \varphi_{\mathbf{k}}^2(i\omega_n).
\]

The fermionic Matsubara frequencies are \(\omega_n = \frac{\pi}{\beta}(2n-1)\) with \(\beta = 1/(k_B T)\). For the present work the convention \(k_B = 1\) is used, so that \(\beta = 1/T\). All energies are expressed in units of the nearest‑neighbour hopping \(t\).

### Lattice and model parameters
- Electron dispersion (tight‑binding with nearest‑ and next‑nearest‑neighbour hopping):
  \[
  \varepsilon_{\mathbf{k}} = -2t\bigl[\cos(k_x)+\cos(k_y)\bigr] + 4t'\cos(k_x)\cos(k_y),\qquad t' = 0.1\,t.
  \]
- Acoustic phonon dispersion:
  \[
  \omega_{\mathbf{q}} = \omega_0\sqrt{2 - \cos q_x - \cos q_y},\qquad \omega_0 = 0.15\,t.
  \]
- Momentum‑dependent electron‑phonon matrix element:
  \[
  g_{\mathbf{q}} = g_0\frac{|\mathbf{q}|}{\sqrt{\omega_{\mathbf{q}}}},\qquad g_0 = 0.031\,t^{3/2}.
  \]

The momentum sums \(\sum_{\mathbf{q}}\) run over an \(N\times N\) grid with \(N = 200\), and the Matsubara sums include \(M = 200\) frequencies (\(n = 1,\dots,200\)).

### Symmetries
The solutions obey the following symmetries (for \(f = \varphi\) or \(Z\)):
\[
f_n(k_x,k_y) = f_n(-k_x,k_y) = f_n(k_x,-k_y) = f_n(-k_x,-k_y),\qquad
f_n(k_x,k_y) = f_{-n+1}(k_x,k_y).
\]

## Thermodynamic quantities
Using the self‑consistently determined \(\varphi_{\mathbf{k}}(i\omega_n)\) and \(Z_{\mathbf{k}}(i\omega_n)\) one can compute the free energy difference between the superconducting and the normal state. A standard expression derived from the Eliashberg‑Nambu formalism is

\[
\Delta F(T) = -\frac{\pi T}{N} \sum_{n} \sum_{\mathbf{k}}
\left[
\frac{2\omega_n^2 + \varphi_{\mathbf{k}}^2(i\omega_n)}
     {\sqrt{\omega_n^2 Z_{\mathbf{k}}^2(i\omega_n) + \varepsilon_{\mathbf{k}}^2 + \varphi_{\mathbf{k}}^2(i\omega_n)}}
- \frac{2\omega_n^2}{\sqrt{\omega_n^2 + \varepsilon_{\mathbf{k}}^2}}
\right],
\tag{3}
\]

where the normal‑state contribution is evaluated with \(\varphi = 0\) and \(Z = 1\) (the effect of the normal‑state renormalisation on the reference free energy is negligible for the purpose of the present ratios). The thermodynamic critical field follows from

\[
\frac{H_C^2(T)}{8\pi} = -\Delta F(T).
\]

The electronic specific heat in the superconducting state is obtained by numerical differentiation:

\[
C^S(T) = -T\,\frac{d^2 F_S}{dT^2},
\]

and analogously for the normal state \(C^N(T)\) (using the normal‑state free energy \(F_N(T)\) computed with \(\varphi = 0\) and the corresponding \(Z_N\) or the simple band‑structure free energy). The jump at \(T_C\) is

\[
\Delta C = C^S(T_C) - C^N(T_C).
\]

Finally, the three dimensionless ratios are defined as

\[
R_\Delta = \frac{2\Delta(0)}{T_C},\qquad
R_C = \frac{\Delta C}{C^N(T_C)},\qquad
R_H = \frac{T_C\, C^N(T_C)}{H_C^2(0)},
\]

with \(\Delta(0)\) taken as the average order parameter \(\langle\Delta(i\omega_{n=1})\rangle\) at the lowest temperature.

## Approach
The system is described by the tight‑binding electron dispersion, the acoustic phonon branch, and the momentum‑dependent electron‑phonon matrix element given above. The superconducting state is characterised by the order parameter Δ_k(iω_n) and the wave‑function renormalisation factor Z_k(iω_n), both of which depend on the wave vector and the Matsubara frequency. The unbalance parameter γ enters the equation for Z. The strategy is to solve these equations iteratively on a discrete momentum grid and a finite set of Matsubara frequencies. First, at a very low temperature, the average order parameter ⟨Δ⟩ on the first Matsubara frequency is computed for a range of γ to locate the critical value γ_C where ⟨Δ⟩ vanishes. Second, for selected sub‑critical γ values, the equations are solved over a range of temperatures to trace the order parameter and the renormalisation factor as functions of temperature. These temperature‑dependent solutions are then used to compute the free‑energy difference, the thermodynamic critical field, and the specific‑heat jump, from which the dimensionless ratios R_Δ, R_C, and R_H are extracted. All results are compared to hidden reference values that were obtained from the same model.

## Reproduction target
Compute the critical unbalance parameter γ_C such that the average order parameter ⟨Δ(iω_{n=1})⟩ vanishes at temperature k_B T = 0.0001 t. For γ = 0, 0.12 γ_C, 0.24 γ_C, and 0.31 γ_C, compute the dimensionless thermodynamic ratios: R_Δ = 2Δ(0) / k_B T_C, R_C = [C^S(T_C) – C^N(T_C)] / C^N(T_C), and R_H = T_C C^N(T_C) / H_C^2(0). Save γ_C as a single floating‑point number in the file `gamma_C.txt`. Save the four γ‑value results in a JSON file `thermodynamic_ratios.json` with keys ‘γ_0’, ‘γ_0.12’, ‘γ_0.24’, ‘γ_0.31’, each containing an object with the three ratios (‘R_Delta’, ‘R_C’, ‘R_H’).

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Model setup
- Role: process
- Action: Define the square-lattice electron dispersion ε_k = -2t[cos(k_x)+cos(k_y)]+4t' cos(k_x)cos(k_y) with t'=0.1 t, the acoustic phonon dispersion ω_q = ω_0 sqrt(2-cos q_x-cos q_y) with ω_0=0.15 t, and the electron-phonon matrix element g_q = g_0|q|/√(ω_q) with g_0=0.031 t^(3/2). Construct the momentum grid and the required arrays.
- Evidence: none

### Step 2: Determine critical unbalance parameter γ_C
- Role: scored (load-bearing)
- Action: Solve the fully self-consistent Eliashberg equations (order-parameter and wave-function renormalisation equations with explicit k and Matsubara frequency dependence) on a 200×200 momentum lattice with 200 Matsubara frequencies at T = 0.0001 t for a range of γ values. Compute the average order parameter <Δ(iω_{n=1})> = (1/N) Σ_k Δ_k(iω_{n=1}) and locate the γ at which it vanishes. Write the extracted γ_C to the output file.
- Output file: `/app/outputs/gamma_C.txt`
- Format: txt
- Contract: A single floating-point number.
- Scoring: scored by hidden verifier

### Step 3: Temperature-dependent Eliashberg solutions
- Role: process
- Action: For each of the four selected γ values (0, 0.12γ_C, 0.24γ_C, 0.31γ_C), solve the fully self-consistent Eliashberg equations at a series of temperatures from T = 0.0001 t up to above the critical temperature. Collect the averaged order parameter <Δ(iω_{n=1})> and the averaged renormalization factor <Z(iω_{n=1})> at each temperature. Fit the order parameter to extract T_C and Δ(0). Save the fitted T_C and Δ(0) as evidence.
- Evidence: `/app/outputs/temperature_fits.json`

### Step 4: Thermodynamic ratios
- Role: scored (load-bearing)
- Action: Using the temperature-dependent solutions from the previous step, compute the free energy difference ΔF according to Eq. (3), the thermodynamic critical field H_C, the normal‑state specific heat C^N(T), the superconducting specific heat C^S(T), and the resulting specific heat jump at T_C. Calculate the dimensionless ratios R_Δ = 2Δ(0)/k_B T_C, R_C = [C^S(T_C)-C^N(T_C)]/C^N(T_C), and R_H = T_C C^N(T_C)/H_C^2(0) for each γ. Write the results to the output file.
- Output file: `/app/outputs/thermodynamic_ratios.json`
- Format: json
- Contract: A JSON object with keys 'γ_0', 'γ_0.12', 'γ_0.24', 'γ_0.31', each containing an object with keys 'R_Delta', 'R_C', 'R_H' (floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gamma_C.txt`
- `/app/outputs/thermodynamic_ratios.json`
- `/app/outputs/temperature_fits.json`  (evidence; not scored but required for completeness)

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gamma_C.txt
- path: `/app/outputs/gamma_C.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Critical unbalance parameter γ_C at which the averaged superconducting order parameter vanishes.
- schema:
  - `type`: number
  - `unit`: dimensionless

### thermodynamic_ratios.json
- path: `/app/outputs/thermodynamic_ratios.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Dimensionless thermodynamic ratios R_Δ, R_C, R_H for γ = 0, 0.12γ_C, 0.24γ_C, 0.31γ_C.
- schema:
  - `type`: object
  - `required_keys`: `γ_0`, `γ_0.12`, `γ_0.24`, `γ_0.31`
  - `γ_0`:
    - `R_Delta`: float
    - `R_C`: float
    - `R_H`: float
  - `γ_0.12`:
    - `R_Delta`: float
    - `R_C`: float
    - `R_H`: float
  - `γ_0.24`:
    - `R_Delta`: float
    - `R_C`: float
    - `R_H`: float
  - `γ_0.31`:
    - `R_Delta`: float
    - `R_C`: float
    - `R_H`: float

### temperature_fits.json
- path: `/app/outputs/temperature_fits.json`
- format: json
- purpose: evidence
- description: Fitted critical temperature T_C and zero-temperature gap Δ(0) for each γ value.
- schema:
  - `type`: object
  - `required_keys`: `γ_0_temperature_fits`, `γ_0.12_temperature_fits`, `γ_0.24_temperature_fits`, `γ_0.31_temperature_fits`
  - each key contains an object with `T_C` (float) and `Δ(0)` (float)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gamma_C.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "number",
        "unit": "dimensionless"
      },
      "description": "Critical unbalance parameter γ_C at which the averaged superconducting order parameter vanishes."
    },
    {
      "file": "thermodynamic_ratios.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "γ_0",
          "γ_0.12",
          "γ_0.24",
          "γ_0.31"
        ],
        "γ_0": {
          "R_Delta": "float",
          "R_C": "float",
          "R_H": "float"
        },
        "γ_0.12": {
          "R_Delta": "float",
          "R_C": "float",
          "R_H": "float"
        },
        "γ_0.24": {
          "R_Delta": "float",
          "R_C": "float",
          "R_H": "float"
        },
        "γ_0.31": {
          "R_Delta": "float",
          "R_C": "float",
          "R_H": "float"
        }
      },
      "description": "Dimensionless thermodynamic ratios R_Δ, R_C, R_H for γ = 0, 0.12γ_C, 0.24γ_C, 0.31γ_C."
    },
    {
      "file": "temperature_fits.json",
      "format": "json",
      "purpose": "evidence",
      "schema": {
        "type": "object",
        "required_keys": [
          "γ_0_temperature_fits",
          "γ_0.12_temperature_fits",
          "γ_0.24_temperature_fits",
          "γ_0.31_temperature_fits"
        ],
        "γ_0_temperature_fits": {
          "T_C": "float",
          "Δ(0)": "float"
        },
        "γ_0.12_temperature_fits": {
          "T_C": "float",
          "Δ(0)": "float"
        },
        "γ_0.24_temperature_fits": {
          "T_C": "float",
          "Δ(0)": "float"
        },
        "γ_0.31_temperature_fits": {
          "T_C": "float",
          "Δ(0)": "float"
        }
      },
      "description": "Fitted T_C and Δ(0) for each γ."
    }
  ],
  "notes": "All output files must be present; temperature_fits.json is evidence and not scored, but its absence may affect the scoring if internal consistency checks are performed."
}

## How you are scored
A hidden verifier independently evaluates each of the two scored artifacts: `gamma_C.txt` and `thermodynamic_ratios.json`. The verifier compares your submitted numerical values to the correct reference values (the paper’s own reported results) using tolerances that absorb legitimate implementation differences. Each artifact contributes a score between 0 and 1, and the overall reward is a weighted sum of these per‑artifact scores. Submitting numbers that happen to match the reference without actually performing the required Eliashberg calculations will not pass, because the verifier checks the provided files and may cross‑validate internal consistency when feasible. The exact tolerances and weights are hidden; to obtain full credit you must run the full numerical solution and ensure your computed values are within the acceptable range.