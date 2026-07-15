# Determination of hexagonal elastic constants from Brillouin frequency shifts

## Problem background
Single crystals of β‑nitrogen are hexagonal close‑packed solids whose mechanical response is governed by five independent elastic constants (c₁₁, c₁₂, c₄₄, c₃₃, c₁₃). Knowledge of these elastic constants near the triple point (63.15 K) is important for understanding intermolecular forces and lattice dynamics in simple molecular crystals. High‑resolution Brillouin spectroscopy provides a direct means to probe acoustic phonon velocities, which are linked to the elastic constants through the Brillouin equation and the crystal's elastic eigenvalue equations. This task asks you to determine the six quantities — the five elastic constants and the adiabatic bulk modulus — from a set of measured Brillouin frequency shifts obtained from oriented single crystals.

## Approach
Brillouin scattering measures the frequency shift Ω of light inelastically scattered by acoustic phonons. The shift is related to the acoustic velocity v by Ω = (2n/λ) v sin(α/2), where n is the refractive index, λ is the laser wavelength in vacuum, and α is the scattering angle. For a given crystal orientation specified by Euler angles, the sound propagation direction relative to the hexagonal c‑axis defines an angle γ. The velocities of the three acoustic modes (longitudinal L, slow transverse T₁, fast transverse T₂) are obtained from the hexagonal elastic eigenvalue expressions; these expressions involve the density ρ and the elastic constants c₁₁, c₁₂, c₄₄, c₃₃, c₁₃ (the latter is not independent for a hexagonal close‑packed crystal with a fixed c/a ratio: c₁₃ = c₁₁ + c₁₂ − c₃₃).

You will be provided with a CSV file containing, for each of 25 crystal orientations: the Euler angles (θ, φ, χ) that specify the orientation, the resulting γ value, and the measured Brillouin shifts Ω(L), Ω(T₁), Ω(T₂) for that orientation. Fixed parameters are: n = 1.235, ρ = 0.944 g/cm³, λ = 514.54 nm, and α = 90°. Your task is to implement a nonlinear least‑squares fit that adjusts c₁₁, c₁₂, c₄₄, and c₃₃ to best reproduce the observed frequency shifts. The c₁₃ constant follows from the constraint. After fitting, compute the adiabatic bulk modulus using Bₛ = [2(c₁₁ + c₁₂) − c₃₃] / 3.

## Reproduction target
Using the supplied measured Brillouin shifts and crystal orientations (data.csv), perform a nonlinear least‑squares fit to the hexagonal elastic model with the constraint c₁₃ = c₁₁ + c₁₂ − c₃₃ and the listed fixed parameters. Report your best‑fit values for the elastic constants c₁₁, c₁₂, c₄₄, c₃₃, c₁₃ and the adiabatic bulk modulus Bₛ in the file elastic_constants.json. All quantities must be expressed in units of 10¹⁰ dyn/cm².

## Assets

- Brillouin shift measurements and crystal orientations from Table I
- SciPy: scipy

## Workflow steps

### Step 1: Least-squares fit of elastic constants and bulk modulus computation
- Role: scored (load-bearing)
- Action: Load the measured Brillouin shifts and crystal orientations from data.csv. Implement the Brillouin relation (Ω = 2n/λ v sin(α/2)) and the hexagonal elastic eigenvalue equations to relate acoustic velocities to the elastic constants. Use the constraint c13 = c11 + c12 - c33. Perform a nonlinear least-squares fit of the observed frequency shifts to the model to determine c11, c12, c44, c33 (and c13 from the constraint). Compute the adiabatic bulk modulus Bs = [2(c11+c12)-c33]/3. Write the fitted constants and bulk modulus to elastic_constants.json. All constants are in units of 10¹⁰ dyn/cm².
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: JSON object with numeric fields: c11, c12, c44, c33, c13, Bs (all in units of 10^10 dyn/cm^2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted elastic constants and adiabatic bulk modulus of β-nitrogen at 63.0 K.
- schema:
  - `type`: object
  - `required`: `c11`, `c12`, `c44`, `c33`, `c13`, `Bs`
  - `items`: object
  - `required_columns`:
  - `units`:
    - `c11`: 10^10 dyn/cm^2
    - `c12`: 10^10 dyn/cm^2
    - `c44`: 10^10 dyn/cm^2
    - `c33`: 10^10 dyn/cm^2
    - `c13`: 10^10 dyn/cm^2
    - `Bs`: 10^10 dyn/cm^2

Notes: The hidden checker compares each reported constant to paper-reported values within a relative tolerance of ±2%. The agent must not hardcode the target numbers; any attempt to look up the paper's values externally is against the spirit of the task.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "c11",
          "c12",
          "c44",
          "c33",
          "c13",
          "Bs"
        ],
        "items": {},
        "required_columns": [],
        "units": {
          "c11": "10^10 dyn/cm^2",
          "c12": "10^10 dyn/cm^2",
          "c44": "10^10 dyn/cm^2",
          "c33": "10^10 dyn/cm^2",
          "c13": "10^10 dyn/cm^2",
          "Bs": "10^10 dyn/cm^2"
        }
      },
      "description": "Fitted elastic constants and adiabatic bulk modulus of β-nitrogen at 63.0 K."
    }
  ],
  "notes": "The hidden checker compares each reported constant to paper-reported values within a relative tolerance of ±2%. The agent must not hardcode the target numbers; any attempt to look up the paper's values externally is against the spirit of the task."
}
```

## How you are scored
The hidden verifier will read your elastic_constants.json and compare each of the six reported quantities (c₁₁, c₁₂, c₄₄, c₃₃, c₁₃, Bₛ) to independently determined reference values. It will also check that your reported c₁₃ satisfies the constraint c₁₃ = c₁₁ + c₁₂ − c₃₃. Your final score is the fraction of these checks that pass; each of the six quantities carries equal weight. The exact tolerance is hidden, but it is representative of the experimental uncertainty and numerical spread expected from an honest least‑squares fit with the given data. The verifier does not trust your self‑reported accuracy; it compares your outputs directly to the reference values.
