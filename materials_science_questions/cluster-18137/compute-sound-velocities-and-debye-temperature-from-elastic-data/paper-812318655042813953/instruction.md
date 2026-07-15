# Compute Sound Velocities and Debye Temperature from Elastic Data

## Problem background
Mixed manganese-magnesium ferrites are magnetic oxide materials used in radio and electronics applications. Understanding their elastic behaviour provides insight into interatomic binding forces and structural stability. In this task, corrected Young's modulus (E) and rigidity modulus (\mu) are available, together with bulk density, for a series of six ferrite compositions spanning the full Mn-Mg substitution range. From these measured elastic moduli one can derive the longitudinal, shear, and mean sound velocities and the Debye temperature using isotropic elasticity theory. Additionally, the provided data allow the calculation of how much the elastic moduli change upon small compositional substitutions, which reveals the effect of mixing on mechanical rigidity.

## Approach
Use the X-ray density (theoretical density) from the input CSV as the mass density ρ for all velocity and Debye temperature calculations. The shear sound velocity is V_s = sqrt(\mu/\rho). The longitudinal velocity V_l is obtained from E, \mu, and \rho: compute Poisson's ratio \sigma = (E/(2\mu)) - 1, then V_l = sqrt(E(1-\sigma)/(\rho(1+\sigma)(1-2\sigma))). The mean sound velocity V_m = [(1/3)(1/V_l^3 + 2/V_s^3)]^{-1/3}. The Debye temperature \theta is computed via Anderson's formula: \theta = (h/k_B) (3 n N_A \rho / (4\pi M))^{1/3} V_m, where h = 6.62607015e-34 J·s is Planck's constant, k_B = 1.380649e-23 J/K is Boltzmann's constant, N_A = 6.02214076e23 mol^{-1} is Avogadro's number, n is the number of atoms per formula unit, M is the molar mass in kg/mol, and \rho is the X-ray density. The necessary input data (E, \mu, bulk density) are provided in a CSV file. For the substitution analysis, compute the percentage increase in E and \mu when comparing the pure end-member ferrite with the mixed composition obtained by adding a small amount of the other end member, using the standard relative change formula.

## Reproduction target
Given the supplied CSV file containing composition, bulk density, X-ray density, Young's modulus (E), rigidity modulus (\mu), molar mass M (kg/mol), and atoms per formula unit n, produce:
1. A CSV file sound_velocities_debye.csv containing for each composition the longitudinal sound velocity V_l (m/s), shear sound velocity V_s (m/s), mean sound velocity V_m (m/s), and Debye temperature \theta (K).
2. A text file percentage_changes.txt reporting the percentage increase in Young's modulus and rigidity modulus for the following composition pairs: (a) adding 0.25 mol Mg to Mn ferrite (i.e., comparing MnFe2O4 and Mn0.75Mg0.25Fe2O4), (b) adding 0.1 mol Mn to Mg ferrite (comparing MgFe2O4 and Mn0.10Mg0.90Fe2O4). Each line must follow the format '<pair>: <percentage>%' with the percentage rounded to one decimal place.

## Assets

- ferrites_elastic_data.csv: a CSV file with columns `composition` (string), `bulk_density` (kg/m³), `xray_density` (kg/m³), `E` (N/m²), `mu` (N/m²), `M` (kg/mol), `n` (dimensionless). `xray_density` is the theoretical density and must be used as the mass density ρ for sound velocity and Debye temperature calculations. `M` is the molar mass of the formula unit in kg/mol and `n` is the number of atoms per formula unit; both are required for Anderson's Debye temperature formula.

## Workflow steps

### Step 1: Compute sound velocities and Debye temperature
- Role: scored
- Action: Read the provided CSV file (ferrites_elastic_data.csv). For each composition, extract the X-ray density ρ (xray_density column), Young's modulus E, rigidity modulus μ, molar mass M, and number of atoms per formula unit n. Compute V_s = sqrt(μ/ρ), σ = (E/(2μ)) - 1, V_l = sqrt(E(1-σ)/(ρ(1+σ)(1-2σ))), V_m = [(1/3)(1/V_l³ + 2/V_s³)]^{-1/3}, and θ = (h/k_B)(3 n N_A ρ/(4π M))^{1/3} V_m with the constants given above. Write the results to a CSV file with columns: composition, V_l (m/s), V_s (m/s), V_m (m/s), theta (K).
- Output file: `/app/outputs/sound_velocities_debye.csv`
- Format: csv
- Contract: Columns: composition, V_l (float, m/s), V_s (float, m/s), V_m (float, m/s), theta (float, K). One row per composition.
- Scoring: scored by hidden verifier

### Step 2: Compute percentage changes in elastic moduli
- Role: scored
- Action: Using the same input CSV, compute the percentage increase in Young's modulus (E) and rigidity modulus (μ) for (a) adding 0.25 mol Mg to Mn ferrite (i.e., comparing MnFe2O4 and Mn0.75Mg0.25Fe2O4) and (b) adding 0.1 mol Mn to Mg ferrite (comparing MgFe2O4 and Mn0.10Mg0.90Fe2O4). Write the results to a text file with four lines, each in the format: '<pair>: <percentage>%'.
- Output file: `/app/outputs/percentage_changes.txt`
- Format: txt
- Contract: Four lines: the first line for E increase when adding Mg to Mn ferrite, second for μ increase for same, third for E increase when adding Mn to Mg ferrite, fourth for μ increase for that addition. Each line ends with a percentage rounded to one decimal place.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sound_velocities_debye.csv`
- `/app/outputs/percentage_changes.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sound_velocities_debye.csv
- path: `/app/outputs/sound_velocities_debye.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Sound velocities and Debye temperature for each ferrite composition, computed from X-ray density and Anderson's formula.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `V_l`, `V_s`, `V_m`, `theta`
  - `units`:
    - `V_l`: m/s
    - `V_s`: m/s
    - `V_m`: m/s
    - `theta`: K

### percentage_changes.txt
- path: `/app/outputs/percentage_changes.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Percentage changes in Young's modulus and rigidity modulus upon specified composition additions.
- schema:
  - `type`: text
  - `lines`: 4
  - `pattern`: Each line: 'pair: percentage%'

Notes: All outputs are scored by the hidden verifier which recomputes using the same input data.

## Output contract

### `sound_velocities_debye.csv`
- Format: CSV
- Columns: `composition` (string), `V_l` (float, m/s), `V_s` (float, m/s), `V_m` (float, m/s), `theta` (float, K).
- One row per composition, in the same order as the input CSV.

### `percentage_changes.txt`
- Format: plain text
- Exactly four lines, each following the pattern: `<pair>: <percentage>%`
- Percentages are rounded to one decimal place (e.g., '14.9%').
- Line order: E increase for Mn→Mn0.75Mg0.25, μ increase for same, E increase for Mg→Mn0.10Mg0.90, μ increase for that addition.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sound_velocities_debye.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "V_l",
          "V_s",
          "V_m",
          "theta"
        ],
        "units": {
          "V_l": "m/s",
          "V_s": "m/s",
          "V_m": "m/s",
          "theta": "K"
        }
      },
      "description": "Sound velocities and Debye temperature for each ferrite composition, computed from X-ray density and Anderson's formula."
    },
    {
      "file": "percentage_changes.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "lines": 4,
        "pattern": "Each line: 'pair: percentage%'"
      },
      "description": "Percentage changes in Young's modulus and rigidity modulus upon specified composition additions."
    }
  ],
  "notes": "All outputs are scored by the hidden verifier which recomputes using the same input data."
}
```

## How you are scored
A hidden verifier will independently compute the expected sound velocities, Debye temperatures, and percentage changes from the same input data using the standard isotropic elasticity formulas and Anderson's method. It will compare your submitted values to the hidden reference values. For the sound_velocities_debye.csv file, each computed quantity (V_l, V_s, V_m, \theta) is compared individually; for the percentage_changes.txt file, the reported percentages are compared individually. The final reward is a weighted combination of how many values agree within preset tolerances: the sound velocities and Debye temperature contribute most of the weight, while the percentage changes contribute a smaller share. Reporting values that exactly match published numbers is not required; the verifier allows small deviations that are consistent with correct application of the formulas.
