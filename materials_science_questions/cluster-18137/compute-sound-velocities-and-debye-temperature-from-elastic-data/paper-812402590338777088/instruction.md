# Compute Polycrystalline Elastic Constants and Debye Temperature from Sound Velocities

## Problem background
The elastic constants of polycrystalline Al3Sc are important for understanding its mechanical and thermodynamic behavior, for constructing interatomic potentials, and for evaluating its potential as a high-temperature structural intermetallic. The task is to derive these polycrystalline elastic constants and the associated Debye temperature from the material's experimentally measured longitudinal and shear sound velocities and its mass density, using the well-known relationships of isotropic linear elasticity.

## Approach
The material is assumed to be an isotropic elastic solid. The shear modulus μ and Lamé's first parameter λ are first obtained from the shear wave velocity V_s and longitudinal wave velocity V_p and the density ρ via the standard elastic wave equations. From these, the polycrystalline stiffness coefficients c11, c12, c44 are computed. Engineering constants (Young's modulus E, shear modulus G, bulk modulus K, Poisson's ratio ν, and the ratio K/G) are then derived from the Lamé constants using standard isotropic elasticity relationships. The mean sound velocity V_m is calculated from V_s and V_p using the Anderson–Gilvarry formula for an isotropic polycrystal. Finally, the Debye temperature θ_D is evaluated with Anderson's formula, which uses fundamental constants (Planck's constant h, Boltzmann's constant k, Avogadro's number N), the number of atoms per formula unit q, the molar mass M of Al3Sc, the density ρ, and the mean sound velocity V_m.

## Reproduction target
Reproduce the polycrystalline elastic constants c11, c12, c44, the engineering moduli E, G, K, λ, ν, and K/G, and the Debye temperature θ_D for Al3Sc, starting from the given measured sound velocities (V_s = 4750 m/s, V_p = 7763 m/s) and density (ρ = 3.031 g/cm³ = 3031 kg/m³). Output all computed quantities as a single JSON file with the prescribed keys and units.

## Assets

- Python Standard Library

## Workflow steps

### Step 1: Compute Elastic Constants and Debye Temperature
- Role: scored
- Action: Given the polycrystalline Al3Sc experimental data: shear wave velocity V_s = 4750 m/s, longitudinal wave velocity V_p = 7763 m/s, and mass density ρ = 3.031 g/cm³ (3031 kg/m³), compute (1) Lamé constants μ and λ from the standard elastic wave equations for an isotropic solid; (2) stiffness coefficients c11, c12, c44 from the Lamé constants; (3) engineering moduli E, G, K, ν, and K/G using isotropic elasticity relationships; (4) mean sound velocity V_m from the Anderson-Gilvarry formula; (5) Debye temperature θ_D using Anderson's formula with fundamental constants (Planck's constant h, Boltzmann's constant k, Avogadro's number N, formula weight M of Al3Sc = 0.1259004 kg/mol, atoms per formula unit q = 4). Output all computed values in a JSON file.
- Output file: `/app/outputs/computed_properties.json`
- Format: json
- Contract: A JSON object with keys: c11 (GPa), c12 (GPa), c44 (GPa), E (GPa), G (GPa), K (GPa), lambda (GPa), nu (dimensionless), K_over_G (dimensionless), Debye_temperature (K). All values are numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_properties.json
- path: `/app/outputs/computed_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: All polycrystalline elastic constants and Debye temperature derived from the given sound velocities and density.
- schema:
  - `type`: object
  - `required`: `c11`, `c12`, `c44`, `E`, `G`, `K`, `lambda`, `nu`, `K_over_G`, `Debye_temperature`
  - `properties`:
    - `c11`:
      - `type`: number
      - `units`: GPa
    - `c12`:
      - `type`: number
      - `units`: GPa
    - `c44`:
      - `type`: number
      - `units`: GPa
    - `E`:
      - `type`: number
      - `units`: GPa
    - `G`:
      - `type`: number
      - `units`: GPa
    - `K`:
      - `type`: number
      - `units`: GPa
    - `lambda`:
      - `type`: number
      - `units`: GPa
    - `nu`:
      - `type`: number
      - `units`: dimensionless
    - `K_over_G`:
      - `type`: number
      - `units`: dimensionless
    - `Debye_temperature`:
      - `type`: number
      - `units`: K

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "c11",
          "c12",
          "c44",
          "E",
          "G",
          "K",
          "lambda",
          "nu",
          "K_over_G",
          "Debye_temperature"
        ],
        "properties": {
          "c11": {
            "type": "number",
            "units": "GPa"
          },
          "c12": {
            "type": "number",
            "units": "GPa"
          },
          "c44": {
            "type": "number",
            "units": "GPa"
          },
          "E": {
            "type": "number",
            "units": "GPa"
          },
          "G": {
            "type": "number",
            "units": "GPa"
          },
          "K": {
            "type": "number",
            "units": "GPa"
          },
          "lambda": {
            "type": "number",
            "units": "GPa"
          },
          "nu": {
            "type": "number",
            "units": "dimensionless"
          },
          "K_over_G": {
            "type": "number",
            "units": "dimensionless"
          },
          "Debye_temperature": {
            "type": "number",
            "units": "K"
          }
        }
      },
      "description": "All polycrystalline elastic constants and Debye temperature derived from the given sound velocities and density."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. The verifier checks that the output JSON file contains all required keys with numeric values in the correct units, and it compares your computed values against reference values using appropriate tolerances. The final reward is a weighted combination of these checks. Reporting a set of numbers without actually computing them from the given inputs will not receive full credit.
