# Low-energy electron range simulation and parameterization using Monte Carlo

## Problem background
The electron range in solids at low beam energies (E₀ < 10 keV) is a crucial parameter for quantitative analysis in scanning electron microscopy (SEM), yet direct experimental measurement is notoriously difficult because the shallow penetration depth makes results extremely sensitive to surface conditions and contamination. Monte Carlo simulation of electron transport provides a powerful alternative: it allows systematic, repeatable computation of the electron range for any element and reveals how the range depends on beam energy and atomic number. These simulations form the basis for developing accurate parameterizations that can predict electron range from beam energy and material properties without requiring computationally expensive simulations every time.

## Approach
This task uses the open‑source CASINO Monte Carlo program to simulate electron transport in several elemental solids. For each element and each beam energy, a large number of primary electrons (250,000) are tracked through the material, and the electron range is defined as the maximum depth reached by 99.9% of the internal electrons (i.e., excluding those that are backscattered). Simulations are performed for five elements — carbon (C), aluminum (Al), copper (Cu), silver (Ag), and gold (Au) — at a set of beam energies covering the range 1–10 keV. From the extracted ranges, a power‑law model R = k·Eⁿ (R in nm, E in keV) is fitted separately for each element, yielding a dimensionless exponent n and a coefficient k (nm/keVⁿ). Using the known densities and atomic numbers of the elements, the product k·ρ (in nm·g/cm³/keVⁿ) is computed. Finally, second‑degree polynomials are fitted to describe n and kρ as functions of atomic number Z: n(Z) = a₀ + a₁·Z + a₂·Z² and kρ(Z) = b₀ + b₁·Z + b₂·Z².

## Reproduction target
Produce two main outputs: 
1. A CSV file (`step_01_simulated_ranges.csv`) containing the simulated electron range for all five elements at each beam energy. The columns must be `element` (string, e.g., 'Al'), `beam_energy_keV` (float), and `range_nm` (float). 
2. A JSON file (`step_02_fit_parameters.json`) containing the per‑element fitted power‑law parameters (n and k) as well as the coefficients of the two second‑degree polynomials for n and kρ as functions of atomic number Z. The JSON structure must include an `elements` object keyed by element name and a `polynomials` object with the fitted coefficients (a0, a1, a2) for `n` and `k_rho`.

## Assets

- CASINO Monte Carlo program: http://www.gel.usherbrooke.ca/casino/

## Workflow steps

### Step 1: Run CASINO Monte Carlo simulations
- Role: process
- Action: Run the CASINO Monte Carlo program for the elements Al, Ag, C, Cu, Au at a set of beam energies covering 1–10 keV (e.g., 1,2,...,10 keV). Use 250,000 primary electrons per simulation. For each condition, save the raw depth distribution (transmitted, backscattered, and cumulative fractions) to files in a designated directory.
- Evidence: `/app/outputs/casino_simulation_logs.txt`

### Step 2: Extract electron ranges from simulations
- Role: scored (load-bearing)
- Action: For each simulation run, compute the electron range as the maximum depth reached by 99.9% of the 250,000 simulated internal electrons (excluding backscattered). Produce a CSV file containing columns: element (string), beam_energy_keV (float), range_nm (float). One row per condition for all five elements and all energies.
- Output file: `/app/outputs/step_01_simulated_ranges.csv`
- Format: csv
- Contract: CSV with header: element,beam_energy_keV,range_nm. element is a string (e.g., 'Al'), beam_energy_keV is a float, range_nm is a float.
- Scoring: scored by hidden verifier

### Step 3: Fit power-law parameterization
- Role: scored (load-bearing)
- Action: Using the simulated internal electron ranges from step_01_simulated_ranges.csv, fit the model R = k * E^n (R in nm, E in keV) separately for each element C, Al, Cu, Ag, Au. Report the fitted parameters n (dimensionless) and k (in nm/keV^n) for each element. Then, using the atomic numbers Z (6, 13, 29, 47, 79) and densities ρ (g/cm³) of the elements, compute the product kρ (in nm·g/cm³/keV^n) and fit second-degree polynomials n(Z) = a0 + a1·Z + a2·Z² and kρ(Z) = b0 + b1·Z + b2·Z². Output a JSON file with these results.
- Output file: `/app/outputs/step_02_fit_parameters.json`
- Format: json
- Contract: JSON object with keys: 'elements' (object mapping element name, e.g., 'Al', to an object with keys 'n' (float, dimensionless) and 'k' (float, nm/keV^n)), and 'polynomials' (object with keys 'n' and 'k_rho'; each is an object with keys 'a0', 'a1', 'a2' (all floats)).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_simulated_ranges.csv`
- `/app/outputs/step_02_fit_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_simulated_ranges.csv
- path: `/app/outputs/step_01_simulated_ranges.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated electron ranges for all five elements at multiple energies.
- schema:
  - `type`: table
  - `required_columns`: `element`, `beam_energy_keV`, `range_nm`
  - `units`:
    - `beam_energy_keV`: keV
    - `range_nm`: nm

### step_02_fit_parameters.json
- path: `/app/outputs/step_02_fit_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Power-law fit coefficients per element and polynomial coefficients for Z-dependent parameterization.
- schema:
  - `type`: object
  - `required`:
    - `elements`: object
    - `polynomials`: object
  - `properties`:
    - `elements`:
      - `type`: object
      - `additionalProperties`:
        - `type`: object
        - `required`: `n`, `k`
        - `properties`:
          - `n`:
            - `type`: number
            - `description`: dimensionless exponent
          - `k`:
            - `type`: number
            - `description`: coefficient (nm/keV^n)
    - `polynomials`:
      - `type`: object
      - `required`: `n`, `k_rho`
      - `properties`:
        - `n`:
          - `type`: object
          - `required`: `a0`, `a1`, `a2`
          - `properties`:
            - `a0`:
              - `type`: number
            - `a1`:
              - `type`: number
            - `a2`:
              - `type`: number
        - `k_rho`:
          - `type`: object
          - `required`: `a0`, `a1`, `a2`
          - `properties`:
            - `a0`:
              - `type`: number
            - `a1`:
              - `type`: number
            - `a2`:
              - `type`: number

Notes: The checker compares simulated ranges for Al and Ag against hidden reference values digitized from the paper's validation plots, and fit polynomials against Table 1. Agents must run CASINO for all five elements to obtain ranges and derive the parameterization.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_simulated_ranges.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "beam_energy_keV",
          "range_nm"
        ],
        "units": {
          "beam_energy_keV": "keV",
          "range_nm": "nm"
        }
      },
      "description": "Simulated electron ranges for all five elements at multiple energies."
    },
    {
      "file": "step_02_fit_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "elements": "object",
          "polynomials": "object"
        },
        "properties": {
          "elements": {
            "type": "object",
            "additionalProperties": {
              "type": "object",
              "required": [
                "n",
                "k"
              ],
              "properties": {
                "n": {
                  "type": "number",
                  "description": "dimensionless exponent"
                },
                "k": {
                  "type": "number",
                  "description": "coefficient (nm/keV^n)"
                }
              }
            }
          },
          "polynomials": {
            "type": "object",
            "required": [
              "n",
              "k_rho"
            ],
            "properties": {
              "n": {
                "type": "object",
                "required": [
                  "a0",
                  "a1",
                  "a2"
                ],
                "properties": {
                  "a0": {
                    "type": "number"
                  },
                  "a1": {
                    "type": "number"
                  },
                  "a2": {
                    "type": "number"
                  }
                }
              },
              "k_rho": {
                "type": "object",
                "required": [
                  "a0",
                  "a1",
                  "a2"
                ],
                "properties": {
                  "a0": {
                    "type": "number"
                  },
                  "a1": {
                    "type": "number"
                  },
                  "a2": {
                    "type": "number"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Power-law fit coefficients per element and polynomial coefficients for Z-dependent parameterization."
    }
  ],
  "notes": "The checker compares simulated ranges for Al and Ag against hidden reference values digitized from the paper's validation plots, and fit polynomials against Table 1. Agents must run CASINO for all five elements to obtain ranges and derive the parameterization."
}
```

## How you are scored
A hidden verifier will evaluate the contents of your submitted output files by comparing your simulated electron ranges (especially for Al and Ag) to expected benchmark values, and by comparing your fitted power‑law and polynomial parameters against reference ranges. Each of the two main artifacts contributes a fixed, weighted portion to your final reward; a perfect reproduction yields the maximum score. Simply reporting numbers without running the simulation and fitting pipeline is insufficient—the checker verifies that the outputs are consistent with a genuine Monte Carlo simulation workflow.
