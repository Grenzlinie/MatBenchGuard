# Compute Debye Frequencies and Recoilless Fractions from Elastic Data

## Problem background
The Mössbauer effect in non‑cubic single crystals exhibits anisotropy: the recoilless fraction (the probability of recoil‑free emission/absorption of a γ‑ray) depends on the direction of the γ‑ray momentum relative to the crystallographic axes.  For crystals of trigonal symmetry, such as tellurium (Te) and antimony (Sb), this anisotropy can be expressed through a Debye‑frequency tensor that connects the elastic properties of the crystal to the phonon spectrum.  The central aim of this task is to compute the principal Debye frequencies and the corresponding recoilless fractions for Te and Sb as functions of temperature and direction, and thereby to characterise the expected anisotropy of the Mössbauer effect in these materials.

## Approach
The calculation is built on a semiphenomenological Debye‑tensor formalism.  In this approach the thermal fluctuation tensor of a Mössbauer nucleus is expressed in terms of the Debye frequency tensor, whose principal values are determined solely by the single‑crystal elastic constants and the density.  The principal Debye‑tensor components are obtained by numerical double integration over a unit‑sphere angular domain using the elastic stiffness coefficients of the trigonal crystal.  From these components one derives the principal Debye frequencies and the associated Debye temperatures.  The recoilless fraction in a principal direction is then evaluated from the standard Debye‑model formula (involving the recoil energy of the free nucleus, the γ‑ray energy, and the Debye temperature), and the anisotropy is given by the ratio of the recoilless fractions in the basal (transverse) and axial (longitudinal) directions.  The workflow proceeds in two stages: first, the numerical integration yields the Debye‑tensor components, frequencies, and temperatures; second, these results are combined with the known γ‑ray energies and free‑nucleus recoil energies to compute the recoilless fractions at the temperatures of interest.

## Reproduction target
Your task is to produce two CSV files under `/app/outputs`.  
1. `computed_parameters.csv`: for each of tellurium (Te) and antimony (Sb), report the Debye‑tensor integrals I_t, I_l, I (in units of 10⁻⁴¹ s³), the principal Debye frequencies Ω_t, Ω_l, Ω (in 10¹³ s⁻¹), and the principal Debye temperatures Θ_t, Θ_l, Θ (in K).  These are to be computed from the elastic constants, density, and atomic mass supplied in the Assets section, using the Debye‑tensor integrals for a trigonal crystal.  
2. `recoilless_fractions.csv`: using the Debye temperatures obtained above and the γ‑ray energies (E₀ = 35.5 keV for ¹²⁵Te, 37.2 keV for ¹²¹Sb) and free‑nucleus recoil energies (R = 5.44×10⁻³ eV for Te, 6.72×10⁻³ eV for Sb), evaluate the Mössbauer recoilless fractions W_t (basal direction) and W_l (axial direction) at the temperatures 0 K, 80 K, and 300 K for Te, and at 0 K, 90 K, and 300 K for Sb.  Also compute the anisotropy A = W_t / W_l at each temperature.  The comparison between the two materials and the temperature dependence of the anisotropy are the key quantitative findings to be reproduced.

## Assets

- NumPy: numpy
- SciPy: scipy
- Elastic constants, density, and atomic masses of Te and Sb at 0 K from Table 1

## Workflow steps

### Step 1: Compute Principal Debye Frequencies and Temperatures
- Role: scored
- Action: Implement numerical integration of the Debye‑tensor integrals for trigonal crystals using the provided elastic constants, density, and atomic mass to compute the principal Debye frequency tensor components I_t, I_l, I, the principal Debye frequencies Ω_t, Ω_l, Ω, and the corresponding Debye temperatures Θ_t, Θ_l, Θ. Write the results to computed_parameters.csv.
- Output file: `/app/outputs/computed_parameters.csv`
- Format: csv
- Contract: Table with columns: material, I_t (10^{-41} s³), I_l (10^{-41} s³), I (10^{-41} s³), Omega_t (10¹³ s⁻¹), Omega_l (10¹³ s⁻¹), Omega (10¹³ s⁻¹), Theta_t (K), Theta_l (K), Theta (K). One row per material.
- Scoring: scored by hidden verifier

### Step 2: Calculate Recoilless Fractions and Anisotropy
- Role: scored
- Action: Using the computed Θ_t and Θ_l and the known γ‑ray energies (E₀=35.5 keV for ¹²⁵Te, 37.2 keV for ¹²¹Sb) and free‑nucleus recoil energies (R=5.44×10⁻³ eV for Te, 6.72×10⁻³ eV for Sb), evaluate the Mössbauer recoilless fractions W_t(T) and W_l(T) from the Debye‑tensor formula at the specified temperatures, and compute the anisotropy A=W_t/W_l. Write the results to recoilless_fractions.csv.
- Output file: `/app/outputs/recoilless_fractions.csv`
- Format: csv
- Contract: Table with columns: material, temperature (K), W_t, W_l, A (W_t/W_l). Rows: Te at 0, 80, 300 K; Sb at 0, 90, 300 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_parameters.csv`
- `/app/outputs/recoilless_fractions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_parameters.csv
- path: `/app/outputs/computed_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Debye frequency tensor components, principal Debye frequencies, and Debye temperatures for tellurium and antimony.
- schema:
  - `type`: table
  - `required_columns`: `material`, `I_t`, `I_l`, `I`, `Omega_t`, `Omega_l`, `Omega`, `Theta_t`, `Theta_l`, `Theta`
  - `units`:
    - `I_t`: 10^{-41} s^3
    - `I_l`: 10^{-41} s^3
    - `I`: 10^{-41} s^3
    - `Omega_t`: 10^13 s^{-1}
    - `Omega_l`: 10^13 s^{-1}
    - `Omega`: 10^13 s^{-1}
    - `Theta_t`: K
    - `Theta_l`: K
    - `Theta`: K

### recoilless_fractions.csv
- path: `/app/outputs/recoilless_fractions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Calculated Mössbauer recoilless fractions W_t and W_l and their ratio A = W_t/W_l for Te (T = 0, 80, 300 K) and Sb (T = 0, 90, 300 K).
- schema:
  - `type`: table
  - `required_columns`: `material`, `temperature`, `W_t`, `W_l`, `A`
  - `units`:
    - `temperature`: K
    - `W_t`: dimensionless
    - `W_l`: dimensionless
    - `A`: dimensionless

Notes: Numerical values are compared against reference benchmarks from the original study with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "I_t",
          "I_l",
          "I",
          "Omega_t",
          "Omega_l",
          "Omega",
          "Theta_t",
          "Theta_l",
          "Theta"
        ],
        "units": {
          "I_t": "10^{-41} s^3",
          "I_l": "10^{-41} s^3",
          "I": "10^{-41} s^3",
          "Omega_t": "10^13 s^{-1}",
          "Omega_l": "10^13 s^{-1}",
          "Omega": "10^13 s^{-1}",
          "Theta_t": "K",
          "Theta_l": "K",
          "Theta": "K"
        }
      },
      "description": "Computed Debye frequency tensor components, principal Debye frequencies, and Debye temperatures for tellurium and antimony."
    },
    {
      "file": "recoilless_fractions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "temperature",
          "W_t",
          "W_l",
          "A"
        ],
        "units": {
          "temperature": "K",
          "W_t": "dimensionless",
          "W_l": "dimensionless",
          "A": "dimensionless"
        }
      },
      "description": "Calculated Mössbauer recoilless fractions W_t and W_l and their ratio A = W_t/W_l for Te (T = 0, 80, 300 K) and Sb (T = 0, 90, 300 K)."
    }
  ],
  "notes": "Numerical values are compared against reference benchmarks from the original study with appropriate tolerances."
}
```

## How you are scored
Your outputs are evaluated by a hidden verifier that independently examines each scored artifact.  The verifier compares every numeric field in `computed_parameters.csv` and `recoilless_fractions.csv` against reference benchmarks (obtained from the underlying published calculations) with appropriate numerical tolerances.  Each scored workflow step (Compute Principal Debye Frequencies and Temperatures, and Calculate Recoilless Fractions and Anisotropy) contributes a portion of the final reward, and the two contributions are combined by weight.  The verifier does **not** merely check that you reported some numbers; it requires that your numerically computed values match the reference within the allowed tolerance.  You must therefore implement the integration and formulas faithfully; a result that falls outside the tolerance, or a missing or incorrectly formatted output file, will reduce your score.
