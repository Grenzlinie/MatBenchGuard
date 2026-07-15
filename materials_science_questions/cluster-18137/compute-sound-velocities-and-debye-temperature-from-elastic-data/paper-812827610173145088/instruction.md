# Compute Elastic, Mechanical, and Thermal Properties from Cubic Elastic Constants

## Problem background
CuRh2S4 and CuRh2Se4 are spinel‑type superconductors whose mechanical stability, ductility, and thermal properties are assessed through polycrystalline elastic moduli, Peierls stress, and Debye temperature. These quantities are derived from first‑principles cubic elastic constants using standard post‑processing formulas. Computing them verifies the chain linking the elastic tensor to macroscopic observables and provides insight into the material's resistance to deformation, sound velocities, and thermal behavior.

## Approach
Use the Voigt–Reuss–Hill averaging scheme to convert the three independent cubic elastic constants (C11, C12, C44) into the polycrystalline bulk modulus B, shear modulus G, Young's modulus E, Poisson's ratio ν, Pugh ratio B/G, Zener anisotropy A, and Cauchy pressure. From G and ν, together with the Burgers vector b (taken as the lattice parameter a) and the interlayer spacing d, compute the Peierls stress σ_P. Then, using B, G, the mass density ρ, molecular weight M, and the number of atoms per formula unit n, obtain the transverse, longitudinal, and mean sound velocities, and finally the Debye temperature θ_D via the standard relation involving the Planck and Boltzmann constants and Avogadro's number. The calculation employs only the given input constants and fundamental physical constants.

## Reproduction target
For both CuRh2S4 and CuRh2Se4, produce a single JSON file, elastic_properties.json, containing the computed values of bulk modulus B (GPa), shear modulus G (GPa), Young's modulus E (GPa), Poisson's ratio ν, Pugh ratio B_over_G, Zener anisotropy A, Cauchy pressure (GPa), Peierls stress σ_P (GPa), mass density ρ (g/cm³), transverse sound velocity v_t (m/s), longitudinal sound velocity v_l (m/s), mean sound velocity v_m (m/s), and Debye temperature θ_D (K). The file must follow the exact schema described in the output contract.

## Assets

- Python 3 with standard math library: python3

## Workflow steps

### Step 1: Compute Elastic Moduli, Peierls Stress, Sound Velocities, and Debye Temperature
- Role: scored (load-bearing)
- Action: Using the provided cubic elastic constants (C11, C12, C44 in GPa), lattice parameter a (used as Burgers vector b, Å), interlayer spacing d (Å), mass density ρ (g/cm³), molecular weight M (g/mol), and number of atoms per formula unit n for CuRh2S4 and CuRh2Se4: (1) Compute Voigt–Reuss–Hill bulk modulus B = (C11+2C12)/3, shear modulus G via Voigt Gv=(C11-C12+3C44)/5 and Reuss Gr=5C44(C11-C12)/(4C44+3(C11-C12)) then G=(Gv+Gr)/2, Young's modulus E=9BG/(3B+G), Poisson's ratio ν=(3B-2G)/(2(3B+G)), Pugh ratio B/G, Zener anisotropy A=2C44/(C11-C12), and Cauchy pressure C12-C44. (2) Compute Peierls stress σ_P = G/(1-ν) * exp(-2πd/(b(1-ν))) with b,d converted to meters and output in GPa. (3) Compute transverse sound velocity vt = sqrt(G/ρ), longitudinal vl = sqrt((B+4G/3)/ρ), mean velocity vm = [1/3*(2/vt^3+1/vl^3)]^{-1/3}, then Debye temperature θ_D = (h/k)*[3n/(4π)*(NA*ρ/M)]^{1/3} * vm, with G and B in Pa, ρ in kg/m³, h=6.62607015e-34 J·s, k=1.380649e-23 J/K, NA=6.02214076e23 mol⁻¹. Write all results to elastic_properties.json.
- Output file: `/app/outputs/elastic_properties.json`
- Format: json
- Contract: Top-level keys 'CuRh2S4' and 'CuRh2Se4'. Each maps to an object with numeric fields: B (GPa), G (GPa), E (GPa), nu (dimensionless), B_over_G (dimensionless), A (dimensionless), Cauchy_pressure (GPa), sigma_P (GPa), rho (g/cm³), v_t (m/s), v_l (m/s), v_m (m/s), theta_D (K).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_properties.json
- path: `/app/outputs/elastic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains all derived mechanical and thermal properties computed from the input elastic constants and material parameters. The hidden checker compares each field to the paper-reported values within tolerances.
- schema:
  - `type`: object
  - `required`: `CuRh2S4`, `CuRh2Se4`
  - `properties`:
    - `CuRh2S4`:
      - `type`: object
      - `required`: `B`, `G`, `E`, `nu`, `B_over_G`, `A`, `Cauchy_pressure`, `sigma_P`, `rho`, `v_t`, `v_l`, `v_m`, `theta_D`
      - `properties`:
        - `B`:
          - `type`: number
          - `unit`: GPa
        - `G`:
          - `type`: number
          - `unit`: GPa
        - `E`:
          - `type`: number
          - `unit`: GPa
        - `nu`:
          - `type`: number
        - `B_over_G`:
          - `type`: number
        - `A`:
          - `type`: number
        - `Cauchy_pressure`:
          - `type`: number
          - `unit`: GPa
        - `sigma_P`:
          - `type`: number
          - `unit`: GPa
        - `rho`:
          - `type`: number
          - `unit`: g/cm³
        - `v_t`:
          - `type`: number
          - `unit`: m/s
        - `v_l`:
          - `type`: number
          - `unit`: m/s
        - `v_m`:
          - `type`: number
          - `unit`: m/s
        - `theta_D`:
          - `type`: number
          - `unit`: K
    - `CuRh2Se4`:
      - `type`: object
      - `required`: `B`, `G`, `E`, `nu`, `B_over_G`, `A`, `Cauchy_pressure`, `sigma_P`, `rho`, `v_t`, `v_l`, `v_m`, `theta_D`
      - `properties`:
        - `B`:
          - `type`: number
          - `unit`: GPa
        - `G`:
          - `type`: number
          - `unit`: GPa
        - `E`:
          - `type`: number
          - `unit`: GPa
        - `nu`:
          - `type`: number
        - `B_over_G`:
          - `type`: number
        - `A`:
          - `type`: number
        - `Cauchy_pressure`:
          - `type`: number
          - `unit`: GPa
        - `sigma_P`:
          - `type`: number
          - `unit`: GPa
        - `rho`:
          - `type`: number
          - `unit`: g/cm³
        - `v_t`:
          - `type`: number
          - `unit`: m/s
        - `v_l`:
          - `type`: number
          - `unit`: m/s
        - `v_m`:
          - `type`: number
          - `unit`: m/s
        - `theta_D`:
          - `type`: number
          - `unit`: K

Notes: The agent must perform the calculations using the given input constants (C11, C12, C44, b, d, ρ, M, n) and standard formulas. Unit conversions are required (Pa, kg/m³, m). The checker will verify numeric values by comparison to the paper's reported numbers with relative tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "CuRh2S4",
          "CuRh2Se4"
        ],
        "properties": {
          "CuRh2S4": {
            "type": "object",
            "required": [
              "B",
              "G",
              "E",
              "nu",
              "B_over_G",
              "A",
              "Cauchy_pressure",
              "sigma_P",
              "rho",
              "v_t",
              "v_l",
              "v_m",
              "theta_D"
            ],
            "properties": {
              "B": {
                "type": "number",
                "unit": "GPa"
              },
              "G": {
                "type": "number",
                "unit": "GPa"
              },
              "E": {
                "type": "number",
                "unit": "GPa"
              },
              "nu": {
                "type": "number"
              },
              "B_over_G": {
                "type": "number"
              },
              "A": {
                "type": "number"
              },
              "Cauchy_pressure": {
                "type": "number",
                "unit": "GPa"
              },
              "sigma_P": {
                "type": "number",
                "unit": "GPa"
              },
              "rho": {
                "type": "number",
                "unit": "g/cm³"
              },
              "v_t": {
                "type": "number",
                "unit": "m/s"
              },
              "v_l": {
                "type": "number",
                "unit": "m/s"
              },
              "v_m": {
                "type": "number",
                "unit": "m/s"
              },
              "theta_D": {
                "type": "number",
                "unit": "K"
              }
            }
          },
          "CuRh2Se4": {
            "type": "object",
            "required": [
              "B",
              "G",
              "E",
              "nu",
              "B_over_G",
              "A",
              "Cauchy_pressure",
              "sigma_P",
              "rho",
              "v_t",
              "v_l",
              "v_m",
              "theta_D"
            ],
            "properties": {
              "B": {
                "type": "number",
                "unit": "GPa"
              },
              "G": {
                "type": "number",
                "unit": "GPa"
              },
              "E": {
                "type": "number",
                "unit": "GPa"
              },
              "nu": {
                "type": "number"
              },
              "B_over_G": {
                "type": "number"
              },
              "A": {
                "type": "number"
              },
              "Cauchy_pressure": {
                "type": "number",
                "unit": "GPa"
              },
              "sigma_P": {
                "type": "number",
                "unit": "GPa"
              },
              "rho": {
                "type": "number",
                "unit": "g/cm³"
              },
              "v_t": {
                "type": "number",
                "unit": "m/s"
              },
              "v_l": {
                "type": "number",
                "unit": "m/s"
              },
              "v_m": {
                "type": "number",
                "unit": "m/s"
              },
              "theta_D": {
                "type": "number",
                "unit": "K"
              }
            }
          }
        }
      },
      "description": "Contains all derived mechanical and thermal properties computed from the input elastic constants and material parameters. The hidden checker compares each field to the paper-reported values within tolerances."
    }
  ],
  "notes": "The agent must perform the calculations using the given input constants (C11, C12, C44, b, d, ρ, M, n) and standard formulas. Unit conversions are required (Pa, kg/m³, m). The checker will verify numeric values by comparison to the paper's reported numbers with relative tolerances."
}
```

## How you are scored
A hidden verifier reads your elastic_properties.json and independently scores your computed quantities. Each field is compared against a reference value (the expected result for the given inputs) using pre‑defined relative tolerances that account for legitimate numerical and implementation differences. Additionally, the verifier performs structural checks, such as confirming that the Pugh ratio and Poisson's ratio fall into the expected ranges for the reported ductile/brittle classification. Simply reporting numbers that match a prior guess does not pass; the full weight is only awarded when the values are consistent with a correct execution of the described formulas.
