# Free-Carrier Absorption Coefficient Evaluation in n-type GaAs

## Problem background
Free-carrier absorption is the process whereby conduction electrons absorb photons with energy below the band gap while simultaneously scattering off phonons or other imperfections. In quasi-two-dimensional structures such as thin films, carrier motion is confined and size quantization alters both the electronic states and the optical properties. This task concerns the free-carrier absorption coefficient in n-type GaAs films, where electrons occupy a non-parabolic conduction band and are scattered by acoustic phonons via two mechanisms: deformation-potential coupling and piezoelectric coupling. The absorption coefficient depends on the polarization of the incident radiation (parallel or perpendicular to the layer plane), the photon frequency, the film thickness, and the temperature. Analytic expressions for the absorption coefficient have been derived from second-order perturbation theory. The goal is to compute the coefficient numerically and to examine how it varies with these parameters, thereby elucidating the roles of the two scattering mechanisms.

## Approach
The absorption coefficient arises from quantum-mechanical transition probabilities for photon absorption assisted by phonon emission or absorption. The task implements the resulting analytic formulas, which involve infinite sums over subband indices and special functions (the exponential integral Ei). Four distinct physical cases must be treated:

- Deformation-potential coupling, radiation field polarized parallel to the film plane.
- Deformation-potential coupling, radiation field polarized perpendicular to the film plane.
- Piezoelectric coupling, radiation field polarized parallel to the film plane.
- Piezoelectric coupling, radiation field polarized perpendicular to the film plane.

The n-type GaAs material parameters are: electron concentration nₑ = 1.73×10¹⁵ cm⁻³, effective mass m* = 0.07 m₀, mass density ρ = 5.32 g/cm³, dielectric constant ε = 12.9, energy gap E_g = 1.51 eV, deformation potential E_d = 7 eV, piezoelectric constant β_p = 4.71×10⁴ esu/cm², and sound velocity vₛ = 3.6×10⁵ cm/s.

The formulas must be evaluated on a grid of photon frequencies from 10 to 100 THz, film thicknesses from 0.1 to 10 μm, and at three temperatures: 77 K, 200 K, and 300 K. The infinite sums are to be truncated when subsequent terms become negligible (e.g. relative contribution < 1×10⁻⁶). The special function Ei is available in scipy.special. The output is a CSV file containing the real part, imaginary part, and absolute value of the absorption coefficient for every combination of case, frequency, thickness, and temperature.

## Reproduction target
Produce a CSV file named free_carrier_absorption.csv in /app/outputs with the following columns:

- case (string: one of DP_parallel, DP_perpendicular, PZ_parallel, PZ_perpendicular)
- frequency_THz (float, photon frequency in THz)
- thickness_um (float, film thickness in μm)
- temperature_K (float, temperature in K)
- alpha_real (float, real part of α in cm⁻¹)
- alpha_imag (float, imaginary part of α in cm⁻¹)
- abs_alpha (float, |α| in cm⁻¹)

The file must contain rows for all combinations of the four cases, the photon frequency grid (10–100 THz), the film thickness grid (0.1–10 μm), and the three temperatures (77 K, 200 K, 300 K). A hidden structural verifier will read this CSV and check that the computed absorption coefficient obeys the expected physical dependencies: for each case it verifies monotonicity, sign of variation, oscillatory behaviour, and the relative magnitudes of real and imaginary parts, using tolerance-based comparisons between adjacent grid points. The aim is to demonstrate that the implementation correctly captures the physics encoded in the formulas, not to match any particular published numeric value exactly.

## Assets

- scipy: scipy

## Workflow steps

### Step 1: Compute free-carrier absorption coefficient grid
- Role: scored (load-bearing)
- Action: Implement the analytic expressions for the free-carrier absorption coefficient α derived for deformation-potential coupling and piezoelectric coupling, for radiation polarized both parallel and perpendicular to the layer plane. Using the material parameters for n-type GaAs (taken from Section 4 of the paper), evaluate α for a grid of photon frequencies (10–100 THz), film thicknesses (0.1–10 μm), and temperatures (77 K, 200 K, 300 K) matching the parameter regimes shown in the paper’s figures. Truncate infinite sums when contributions become negligible. Output a CSV file with the computed α values for each scattering/polarization case and parameter combination.
- Output file: `/app/outputs/free_carrier_absorption.csv`
- Format: csv
- Contract: CSV with columns: case (string: DP_parallel, DP_perpendicular, PZ_parallel, PZ_perpendicular), frequency_THz (float), thickness_um (float), temperature_K (float), alpha_real (float), alpha_imag (float), abs_alpha (float). Each row corresponds to one (case, frequency, thickness, temperature) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/free_carrier_absorption.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### free_carrier_absorption.csv
- path: `/app/outputs/free_carrier_absorption.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Free-carrier absorption coefficient values for n-type GaAs under four scattering/polarization cases across a grid of photon frequencies, film thicknesses, and temperatures. The hidden checker performs a structural audit: for each case, it verifies that the computed α obeys the monotonic trends reported in the paper (e.g., |α| decreases with frequency, increases with temperature, decreases with thickness, and for PZ_perpendicular, α_real decreases with temperature and shows oscillatory damped behavior with thickness at low T).
- schema:
  - `type`: table
  - `required_columns`: `case`, `frequency_THz`, `thickness_um`, `temperature_K`, `alpha_real`, `alpha_imag`, `abs_alpha`
  - `units`:
    - `frequency_THz`: THz
    - `thickness_um`: micrometers
    - `temperature_K`: K
    - `alpha_real`: cm^{-1}
    - `alpha_imag`: cm^{-1}
    - `abs_alpha`: cm^{-1}

Notes: The checker will validate structural trends, not exact numeric matches. The agent must ensure that the infinite sums are truncated appropriately and that the formulas are implemented correctly. Material parameters are provided in the task instructions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "free_carrier_absorption.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "frequency_THz",
          "thickness_um",
          "temperature_K",
          "alpha_real",
          "alpha_imag",
          "abs_alpha"
        ],
        "units": {
          "frequency_THz": "THz",
          "thickness_um": "micrometers",
          "temperature_K": "K",
          "alpha_real": "cm^{-1}",
          "alpha_imag": "cm^{-1}",
          "abs_alpha": "cm^{-1}"
        }
      },
      "description": "Free-carrier absorption coefficient values for n-type GaAs under four scattering/polarization cases across a grid of photon frequencies, film thicknesses, and temperatures. The hidden checker performs a structural audit: for each case, it verifies that the computed α obeys the monotonic trends reported in the paper (e.g., |α| decreases with frequency, increases with temperature, decreases with thickness, and for PZ_perpendicular, α_real decreases with temperature and shows oscillatory damped behavior with thickness at low T)."
    }
  ],
  "notes": "The checker will validate structural trends, not exact numeric matches. The agent must ensure that the infinite sums are truncated appropriately and that the formulas are implemented correctly. Material parameters are provided in the task instructions."
}
```

## How you are scored
Your submission is scored automatically by a hidden verifier. The verifier reads /app/outputs/free_carrier_absorption.csv and performs structural checks for each of the four scattering/polarization cases independently. It examines how the real part, imaginary part, and absolute value of α change as the photon frequency, film thickness, and temperature are varied. Concrete properties checked include:

- Monotonic trends (e.g., does the coefficient increase or decrease when frequency or thickness is raised?)
- The sign of the temperature dependence in each case.
- The presence or absence of damped oscillations in the thickness dependence of the perpendicular piezoelectric case at low temperature.
- Relative magnitudes of the real and imaginary parts where applicable (e.g., imaginary part nearly zero for certain cases).

These checks use numerical tolerances appropriate for floating‑point computation; exact equality with any external target is not required. The total reward is a weighted average of the per‑case scores, as defined in the hidden grading specification, ranging from 0 to 1. A higher reward indicates that the computed absorption coefficients conform more closely to the expected physical behaviour.
