# Compute Debye Temperature from Vibrational Spectrum for Aluminium

## Problem background
The Debye temperature Θ∞(x‑ray) characterizes the temperature dependence of Laue‑Bragg scattering in crystals. For a given material it can be computed from the vibrational frequency distribution ρ(ν) using an integral relation derived from lattice dynamics. Computing this quantity for aluminium from a published vibrational spectrum tests the integral relation and provides a numerical value for the material's vibrational behavior.

## Approach
The core computational method is to evaluate the two integrals A = ∫ρ(ν)ν² dν and B = ∫ρ(ν) dν over the full vibrational spectrum, and then combine them with Planck's constant h and Boltzmann's constant k to obtain the Debye temperature: Θ∞(x‑ray) = √3 / [ (k/h) √(A/B) ]. The normalized frequency distribution ρ(ν) for aluminium is obtained from the work of Walker (1956a). Numerically integrating the digitised spectrum yields the required temperature in Kelvin.

## Reproduction target
Retrieve the normalised vibrational frequency distribution ρ(ν) for aluminium from Walker (1956a). Numerically integrate the spectrum to compute ∫ρ(ν)ν² dν and ∫ρ(ν) dν. Calculate the Debye temperature Θ∞(x‑ray) in Kelvin using the formula Θ∞(x‑ray) = √3 / [ (k/h) √(∫ρ(ν)ν² dν / ∫ρ(ν) dν) ]. Save the computed temperature as a float value with key 'theta_infinity_K' in a JSON file named debye_temperature.json.

## Assets

- Walker's normalized frequency distribution for aluminium: https://doi.org/10.1103/PhysRev.103.547
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Obtain aluminium vibrational spectrum
- Role: process
- Action: Retrieve the normalized frequency distribution function ρ(ν) for aluminium from Walker (1956a) (Phys. Rev. 103, 547). Extract or digitise the function as a numerical array of (ν, ρ(ν)) points covering the full vibrational spectrum.
- Evidence: `/app/outputs/al_spectrum.csv`

### Step 2: Compute Debye temperature from spectrum
- Role: scored (load-bearing)
- Action: Using the numerically represented ρ(ν), integrate the whole spectrum to obtain A = ∫ρ(ν)ν² dν and B = ∫ρ(ν) dν. Compute the Debye temperature Θ∞(x-ray) using the formula that relates these integrals to physical constants. Write the computed temperature (in K) to the output file.
- Output file: `/app/outputs/debye_temperature.json`
- Format: json
- Contract: A JSON object with a single key 'theta_infinity_K' whose value is a float representing the computed Debye temperature in Kelvin.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/debye_temperature.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### debye_temperature.json
- path: `/app/outputs/debye_temperature.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: The computed Debye temperature for aluminium from its vibrational spectrum.
- schema:
  - `type`: object
  - `required`:
    - `theta_infinity_K`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `theta_infinity_K`: Kelvin

Notes: The checker compares the reported theta_infinity_K value to a hidden gold reference within a tolerance window. The target_policy is exact_match because the Debye temperature is a fixed physical constant and 'better' is undefined.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "debye_temperature.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "theta_infinity_K": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "theta_infinity_K": "Kelvin"
        }
      },
      "description": "The computed Debye temperature for aluminium from its vibrational spectrum."
    }
  ],
  "notes": "The checker compares the reported theta_infinity_K value to a hidden gold reference within a tolerance window. The target_policy is exact_match because the Debye temperature is a fixed physical constant and 'better' is undefined."
}
```

## How you are scored
A hidden verifier independently evaluates each workflow stage's artifact and combines the stage rewards into a final score. For this task the verifier will read the 'theta_infinity_K' value from your debye_temperature.json and compare it against a hidden reference. The comparison yields a numeric reward; only a correctly computed value following the prescribed protocol earns full credit. Simply reporting a number is not sufficient—the complete workflow must be executed and the artifact must be written in the exact format described in the output contract.
