# Compute Debye Temperatures from Elastic Constants using Blackman's Method

## Problem background
Accurate calculation of specific heat of crystals depends on knowing the Debye temperature θD. Computing θD directly from elastic constants and structural parameters has historically required evaluating complex integrals over all wave directions. This work addresses that difficulty by introducing a simpler, geometrically motivated method for cubic crystals. The key idea is to exploit the periodic lattice structure to approximate the wave surfaces as ellipsoids in the low-frequency limit, leading to a closed-form relation for the Debye maximum frequency. The approach is demonstrated by computing θD for four cubic substances from their published elastic and structural data.

## Approach
The method treats the crystal as composed of unit cells containing s particles. In the long-wavelength (low-frequency) limit, the vibrational wave surfaces in wave-vector space are approximated. For small values of the ratio of shear to longitudinal elastic constants (c44 / c11 ≤ 0.1), the wave surfaces become three ellipsoids, yielding a simple formula for the Debye maximum frequency vD that depends on the lattice constant a, mass density ρ, number of particles per cell s, and the elastic constants c11 and c44. For larger ratios (up to the isotropic limit c44 / c11 = 1/3), the prefactor in the frequency expression is obtained by linear interpolation between the ellipsoid limit at c44 / c11 = 0.1 and the spherical limit at c44 / c11 = 1/3. The Debye temperature is then computed as θD = (h/kB) · vD, with Planck’s constant h and Boltzmann’s constant kB. The procedure for each substance is to: (a) compute c44 / c11; (b) choose or interpolate the correct prefactor; (c) compute vD and then θD, using all quantities in consistent CGS units.

## Reproduction target
Compute the Debye temperatures θD (in Kelvin) for the four substances KCl, NaCl, CaF2, and FeS2 using their elastic constants and structural parameters provided in the bundled CSV file. For KCl (c44 / c11 ≤ 0.1) use the ellipsoid-limit prefactor 3/(4π). For NaCl, CaF2, and FeS2, determine the prefactor by linear interpolation between the values at c44 / c11 = 0.1 (prefactor = 3/(4π)) and c44 / c11 = 1/3 (prefactor = 3/(3.57√3π)). Write the final θD values to the output file /app/outputs/theta_D_results.csv with columns 'substance' (string) and 'theta_D' (float).

## Assets

- Elastic constants and structural parameters for KCl, NaCl, CaF2, FeS2

## Workflow steps

### Step 1: Load input parameters
- Role: process
- Action: Read the bundled file 'elastic_constants.csv' containing the required parameters (substance, a, rho, s, c11, c44) for KCl, NaCl, CaF2, and FeS2.
- Evidence: none

### Step 2: Calculate Debye temperatures
- Role: scored (load-bearing)
- Action: Implement the Debye maximum frequency formulas from the paper. For each substance, (a) compute the ratio c44/c11; (b) if c44/c11 ≤ 0.1 use prefactor = 3/(4π); otherwise, linearly interpolate between prefactors at c44/c11 = 0.1 (3/(4π)) and 1/3 (3/(3.57√3π)). (c) Compute v_D³ = prefactor * (s / (a³ * ρ^(2/3))) * sqrt(c11 * c44²), ensuring consistent CGS units. (d) Calculate θD = (h/k_B) * v_D, where h = 6.62607015e-27 erg·s and k_B = 1.380649e-16 erg/K. Write the results to theta_D_results.csv with columns 'substance' (string) and 'theta_D' (float, in Kelvin).
- Output file: `/app/outputs/theta_D_results.csv`
- Format: csv
- Contract: Columns: substance (string), theta_D (float, in Kelvin)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/theta_D_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### theta_D_results.csv
- path: `/app/outputs/theta_D_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Debye temperatures for KCl, NaCl, CaF2, and FeS2. The hidden checker compares each value to the paper's reported values using a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `substance`, `theta_D`
  - `units`:
    - `theta_D`: K

Notes: The required input constants (elastic constants and structural parameters) are from Voigt's measurements, which are publicly available in the literature; the solver does not need to locate them because they are bundled. The computational workload is minimal (a few arithmetic operations) and can be performed in any Python environment within seconds. All constants are used in CGS units as in the original derivation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "theta_D_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "substance",
          "theta_D"
        ],
        "units": {
          "theta_D": "K"
        }
      },
      "description": "Computed Debye temperatures for KCl, NaCl, CaF2, and FeS2. The hidden checker compares each value to the paper's reported values using a relative tolerance."
    }
  ],
  "notes": "The required input constants (elastic constants and structural parameters) are from Voigt's measurements, which are publicly available in the literature; the solver does not need to locate them because they are bundled. The computational workload is minimal (a few arithmetic operations) and can be performed in any Python environment within seconds. All constants are used in CGS units as in the original derivation."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/theta_D_results.csv and compares each substance's calculated θD to a set of reference values derived from the original work. The verifier computes a relative error for each substance and awards a fraction of the total reward for each substance whose error falls within an acceptable tolerance. The individual shares are summed to produce your final reward score between 0 and 1. To earn full credit you must correctly implement the interpolation scheme and perform the computation; simply hard-coding expected numbers is not sufficient.
