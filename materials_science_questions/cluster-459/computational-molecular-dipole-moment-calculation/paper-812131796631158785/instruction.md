# Compute CH4 rototranslational absorption spectrum using long-range induced dipoles and quantum dynamics

## Problem background
Collision-induced absorption (CIA) occurs when intermolecular collisions transiently distort the electron distributions of molecules, creating temporary dipole moments that absorb infrared radiation. Methane (CH4) has no permanent dipole, yet its rototranslational band in the far-infrared arises from multipole-induced and gradient-induced dipoles during CH4–CH4 collisions. This task computes the absorption coefficient α(ω) of pure CH4 gas at T=195 K over the wavenumber range 0–800 cm⁻¹, using only the leading long-range induction mechanisms—octopole and hexadecapole induction plus dipole‑quadrupole polarizability gradient terms—and an isotropic intermolecular potential. By comparing the computed spectrum with laboratory measurements, one can assess whether these long-range mechanisms alone account for the observed absorption, or whether additional induction processes (such as collisional frame distortions) are required.

## Approach
The computation follows a quantum lineshape formalism under the isotropic interaction approximation. The induced dipole is modeled by analytic long-range formulas that express the dipole amplitude B(R) in terms of the CH4 multipole moments Q3, Q4, the isotropic polarizability α, the dipole‑quadrupole polarizability element A3, and the intermolecular separation R. The radial Schrödinger equation for CH4–CH4 pairs is solved numerically using the isotropic Morse‑Spline‑van der Waals (MSV) potential of Capelletti to obtain the pair wavefunctions (free and bound). From these wavefunctions and the dipole amplitudes, the ‘translational’ spectral functions g(ω,T) are computed for each dipole component. These g‑functions are then combined with the rotational transition frequencies and nuclear‑spin statistical weights of CH4 (including selection rules for single and simultaneous transitions) to construct the total spectral profile G(ω,T). The absorption coefficient α(ω,T) follows from the standard relation containing the number density ρ (set to 1 amagat) and the detailed balance factor ω[1−exp(−ℏω/kT)]. The resulting unconvolved spectrum is finally convolved with a triangular slit function of half‑width 8.75 cm⁻¹ to match the resolution of the laboratory measurements.

## Reproduction target
Produce a CSV file `absorption_spectrum_195K.csv` containing the rototranslational absorption coefficient α(ω) of pure CH4 at T=195 K. The file must have two columns: `wavenumber` (cm⁻¹, monotonically increasing, 0–800 cm⁻¹ with step ≤ 2 cm⁻¹) and `absorption_coefficient` (cm⁻¹ amagat⁻², positive). The spectrum must be convolved with a triangular slit function of half‑width 8.75 cm⁻¹ and computed from the specified induction dipoles and the Capelletti MSV potential. This is the sole scored artifact.

## Assets

- Capelletti CH4-CH4 isotropic MSV potential: 10.1063/1.1944728
- Methane rotational constant and spin statistical weights: 10.1139/p79-198
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Gather input parameters
- Role: process
- Action: Collect the molecular parameters: squared multipole moments Q3² = 12/5*(2.6 e a0³)², Q4² = 12/7*(8.2 e a0⁴)², dipole–quadrupole polarizability element A3² = 6*(12.8 a0⁴)², isotropic polarizability α = 17.22 a0³. Obtain the rotational constant B and proton-spin statistical weights for CH4 from the literature. Retrieve the parameters of the isotropic Morse-Spline-van der Waals (MSV) intermolecular potential for CH4-CH4 from the Capelletti reference. Save all parameters in a structured JSON file for reproducibility.
- Evidence: `/app/outputs/parameters.json`

### Step 2: Solve radial Schrödinger equation for CH4 pair
- Role: process
- Action: Numerically integrate the radial Schrödinger equation for the CH4-CH4 pair using the MSV potential to obtain bound and free pair wavefunctions for s-wave and higher partial waves up to sufficient angular momentum to converge the dipole matrix elements. Save wavefunction grids as evidence.
- Evidence: `/app/outputs/wavefunctions.npz`

### Step 3: Compute translational spectral functions
- Role: process
- Action: For each distinct dipole component (octopole-induced 3034, hexadecapole-induced 4045, gradient-induced 33_5, and the combined 4346/3436), compute the translational spectral function g(ω) at T=195 K using the wavefunctions and the analytic dipole expressions: multipole-induced dipole B_{ℓ,0,ℓ,ℓ+1}(R) = (-1)^ℓ √(ℓ+1) α Q_ℓ / R^{ℓ+2}, gradient-induced for ℓ=3 as B_{3,3,_,5}(R) = (16/7) Q_3 A_3 / R⁶, and for ℓ=4 the general gradient-induced component B_{(4,3,_,5)}(R) = √(1/45·5·6·11) Q_4 A_3 / R⁷. Save g-functions as evidence.
- Evidence: `/app/outputs/g_functions.npz`

### Step 4: Compute unconvolved absorption coefficient
- Role: process
- Action: Combine the g-functions with rotational statistical weights and rotational transition frequencies (using methane selection rules and nuclear spin weights) to obtain the total spectral profile G(ω,T) at 195 K. Convert to absorption coefficient α(ω,T) via the relation α(ω,T) = (4π²/(3ℏc)) (ρ²/2) ω [1−exp(−ℏω/kT)] G(ω,T), with number density ρ corresponding to 1 amagat. Save the unconvolved spectrum as evidence.
- Evidence: `/app/outputs/unconvolved_spectrum_195K.csv`

### Step 5: Convolve and output final absorption spectrum at 195 K
- Role: scored (load-bearing)
- Action: Convolve the unconvolved absorption spectrum with a triangular slit function of half-width 8.75 cm⁻¹. Output the final convolved spectrum as a CSV file with columns wavenumber (cm⁻¹) and absorption_coefficient (cm⁻¹ amagat⁻²) at T=195 K. The wavenumber grid must cover 0 to 800 cm⁻¹ with a step ≤ 2 cm⁻¹ and be monotonically increasing.
- Output file: `/app/outputs/absorption_spectrum_195K.csv`
- Format: csv
- Contract: CSV with header: wavenumber,absorption_coefficient. wavenumber: float, monotonically increasing, 0–800 cm⁻¹ with step ≤ 2 cm⁻¹. absorption_coefficient: float, positive, in cm⁻¹ amagat⁻².
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/absorption_spectrum_195K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### absorption_spectrum_195K.csv
- path: `/app/outputs/absorption_spectrum_195K.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Rototranslational absorption coefficient α(ω) of CH4 at 195 K, convolved with triangular slit function (half-width 8.75 cm⁻¹), covering wavenumbers 0–800 cm⁻¹.
- schema:
  - `type`: table
  - `required_columns`: `wavenumber`, `absorption_coefficient`
  - `units`:
    - `wavenumber`: cm-1
    - `absorption_coefficient`: cm-1 amagat-2

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "absorption_spectrum_195K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavenumber",
          "absorption_coefficient"
        ],
        "units": {
          "wavenumber": "cm-1",
          "absorption_coefficient": "cm-1 amagat-2"
        }
      },
      "description": "Rototranslational absorption coefficient α(ω) of CH4 at 195 K, convolved with triangular slit function (half-width 8.75 cm⁻¹), covering wavenumbers 0–800 cm⁻¹."
    }
  ],
  "notes": ""
}
```

## How you are scored
The hidden verifier compares your submitted `absorption_spectrum_195K.csv` to a hidden reference curve (not shown to you). The primary metric is the normalized root‑mean‑square error (NRMSE) between your absorption coefficients and the reference over the common wavenumber domain. A threshold‑or‑better scoring policy is used: if your NRMSE is at or below a hidden threshold, you receive full marks for this stage; if the error is larger, the score decays linearly to zero at a hidden upper bound. The verifier also checks that the CSV is correctly formatted (column names, data types, monotonic wavenumber grid) and that the intermediate evidence files (`parameters.json`, `wavefunctions.npz`, `g_functions.npz`, `unconvolved_spectrum_195K.csv`) are present and plausible, but these carry only symbolic weight. Simply reporting the reference numbers without executing the computational pipeline will yield a near‑zero score because the hidden reference is not guessable.
