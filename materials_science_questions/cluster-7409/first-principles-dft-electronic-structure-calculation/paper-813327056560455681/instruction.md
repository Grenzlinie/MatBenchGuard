# DFT calculation of bandgap and magnetic moment for Mo-doped TiO2 supercells

## Problem background
TiO₂ is a promising photocatalyst but its wide bandgap limits absorption to the ultraviolet region. Doping with transition metals can modify the electronic structure and potentially improve visible-light activity. This task investigates, by first-principles DFT calculations, how substitutional Mo doping alters the computed Kohn–Sham bandgap and total magnetic moment in both rutile and anatase phases of TiO₂.

## Approach
Construct 2×2×2 Ti₁₆O₃₂ supercells for rutile and anatase from their known crystal structures. For each phase, create three substitutional Mo concentrations: pure Ti₁₆O₃₂, single-Mo Ti₁₅Mo₁O₃₂, and double-Mo Ti₁₄Mo₂O₃₂ by replacing one or two Ti atoms with Mo. Perform spin-polarized plane-wave DFT calculations using the GGA-WC exchange-correlation functional. Fully relax the geometries, then compute the electronic band structure to obtain the Kohn–Sham bandgap and extract the total magnetic moment from the self-consistent field output.

## Reproduction target
For each of the six structures (pure, single-Mo, and double-Mo in both rutile and anatase), compute and report in a structured JSON file the Kohn–Sham bandgap (Eg, in eV) and total magnetic moment (in µB). The required output file is `/app/outputs/electronic_properties.json` with the structure shown in the scored step contract. The results will be evaluated by a hidden verifier against reference data and checked for consistency of the doping-concentration trends.

### Scope limitation
The defect structures (oxygen vacancies, interstitial Mo) and optical absorption spectra are excluded from this reproduction task for the following reasons:
- The exact atomic coordinates of oxygen vacancies and interstitial Mo atoms relative to the dopants are not uniquely specified in the source literature; the structural models rely on schematic representations that do not provide deterministic geometric parameters. Reconstructing them would require extensive trial-and-error sampling that goes beyond a single, deterministic computational workflow.
- The optical absorption spectra depend on the computed dielectric function, which in turn relies on the Kohn–Sham bandgap. GGA functionals are known to underestimate bandgaps by up to 50% for oxide semiconductors, and this underestimation varies across structures. Without a calibrated scissor correction based on experimental references that are not publicly available for all defect configurations, the computed absorption coefficients cannot be subjected to a tolerant numerical comparison.
Therefore, the task is scoped to the substitutional doping series whose geometries are fully defined by the known crystal structures and which provide the core evidence for the bandgap reduction trend with Mo concentration.

## Assets

- Rutile TiO2 crystal structure (space group P42/mnm): https://www.crystallography.net/cod/2101161.html
- Anatase TiO2 crystal structure (space group I41/amd): https://www.crystallography.net/cod/5000223.html
- GGA-WC pseudopotentials for Ti, O, Mo: https://www.materialscloud.org/discover/sssp/table/efficiency
- Quantum ESPRESSO: https://www.quantum-espresso.org

## Workflow steps

### Step 1: Construct supercells and substitutional Mo-doped structures
- Role: process
- Action: Build 2×2×2 Ti16O32 supercells for rutile and anatase from their crystal structures. For each phase, create substitutional Mo-doped structures at the following specific sites: (i) single Mo: replace one Ti atom at the fractional coordinate (0,0,0) with Mo; (ii) double Mo: replace the two Ti atoms at fractional coordinates (0,0,0) and (0,0,0.5) (the nearest-neighbour pair along the c-axis) with Mo. Save all six initial structures (pure Ti16O32, Ti15Mo1O32, Ti14Mo2O32 for each phase) in a tar archive `/app/outputs/initial_structures.tar.gz`.
- Evidence: `/app/outputs/initial_structures.tar.gz`

### Step 2: Relax all structures with spin-polarized GGA-WC DFT
- Role: process
- Action: Perform full geometry relaxation for each of the six structures using spin-polarized DFT with the GGA-WC exchange-correlation functional. Use an appropriate plane-wave cutoff and k-point sampling. Optimize until forces are converged. Save the final optimized coordinates and total energies.
- Evidence: `/app/outputs/optimized_geometries.tar.gz`

### Step 3: Compute bandgap and magnetic moment
- Role: scored (load-bearing)
- Action: From the relaxed structures, perform self-consistent field and band structure calculations to obtain the Kohn-Sham eigenvalues. Determine the energy gap (Eg) as the difference between the highest occupied and lowest unoccupied states. Extract the total magnetic moment from the SCF output. Report the values for all six structures in a structured JSON file.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: {
  "rutile": {
    "Ti16O32": {"Eg": <float>, "magnetic_moment": <float>},
    "Ti15Mo1O32": {"Eg": <float>, "magnetic_moment": <float>},
    "Ti14Mo2O32": {"Eg": <float>, "magnetic_moment": <float>}
  },
  "anatase": {
    "Ti16O32": {"Eg": <float>, "magnetic_moment": <float>},
    "Ti15Mo1O32": {"Eg": <float>, "magnetic_moment": <float>},
    "Ti14Mo2O32": {"Eg": <float>, "magnetic_moment": <float>}
  }
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed Kohn-Sham bandgap (Eg in eV) and total magnetic moment (μB) for substitutional Mo-doped TiO2 supercells (rutile and anatase).
- schema:
  - `type`: object
  - `required`: `rutile`, `anatase`
  - `properties`:
    - `rutile`:
      - `type`: object
      - `required`: `Ti16O32`, `Ti15Mo1O32`, `Ti14Mo2O32`
      - `properties`:
        - `Ti16O32`:
          - `type`: object
          - `required`: `Eg`, `magnetic_moment`
          - `properties`:
            - `Eg`:
              - `type`: number
              - `unit`: eV
            - `magnetic_moment`:
              - `type`: number
              - `unit`: μB
        - `Ti15Mo1O32`:
          - `type`: object
          - `required`: `Eg`, `magnetic_moment`
          - `properties`:
            - `Eg`:
              - `type`: number
              - `unit`: eV
            - `magnetic_moment`:
              - `type`: number
              - `unit`: μB
        - `Ti14Mo2O32`:
          - `type`: object
          - `required`: `Eg`, `magnetic_moment`
          - `properties`:
            - `Eg`:
              - `type`: number
              - `unit`: eV
            - `magnetic_moment`:
              - `type`: number
              - `unit`: μB
    - `anatase`:
      - `type`: object
      - `required`: `Ti16O32`, `Ti15Mo1O32`, `Ti14Mo2O32`
      - `properties`:
        - `Ti16O32`:
          - `type`: object
          - `required`: `Eg`, `magnetic_moment`
          - `properties`:
            - `Eg`:
              - `type`: number
              - `unit`: eV
            - `magnetic_moment`:
              - `type`: number
              - `unit`: μB
        - `Ti15Mo1O32`:
          - `type`: object
          - `required`: `Eg`, `magnetic_moment`
          - `properties`:
            - `Eg`:
              - `type`: number
              - `unit`: eV
            - `magnetic_moment`:
              - `type`: number
              - `unit`: μB
        - `Ti14Mo2O32`:
          - `type`: object
          - `required`: `Eg`, `magnetic_moment`
          - `properties`:
            - `Eg`:
              - `type`: number
              - `unit`: eV
            - `magnetic_moment`:
              - `type`: number
              - `unit`: μB

Notes: The scored artifact is compared against the paper's reported values (Table 2) with appropriate tolerances, and the monotonic decreasing trend of Eg with Mo concentration is verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "rutile",
          "anatase"
        ],
        "properties": {
          "rutile": {
            "type": "object",
            "required": [
              "Ti16O32",
              "Ti15Mo1O32",
              "Ti14Mo2O32"
            ],
            "properties": {
              "Ti16O32": {
                "type": "object",
                "required": [
                  "Eg",
                  "magnetic_moment"
                ],
                "properties": {
                  "Eg": {
                    "type": "number",
                    "unit": "eV"
                  },
                  "magnetic_moment": {
                    "type": "number",
                    "unit": "μB"
                  }
                }
              },
              "Ti15Mo1O32": {
                "type": "object",
                "required": [
                  "Eg",
                  "magnetic_moment"
                ],
                "properties": {
                  "Eg": {
                    "type": "number",
                    "unit": "eV"
                  },
                  "magnetic_moment": {
                    "type": "number",
                    "unit": "μB"
                  }
                }
              },
              "Ti14Mo2O32": {
                "type": "object",
                "required": [
                  "Eg",
                  "magnetic_moment"
                ],
                "properties": {
                  "Eg": {
                    "type": "number",
                    "unit": "eV"
                  },
                  "magnetic_moment": {
                    "type": "number",
                    "unit": "μB"
                  }
                }
              }
            }
          },
          "anatase": {
            "type": "object",
            "required": [
              "Ti16O32",
              "Ti15Mo1O32",
              "Ti14Mo2O32"
            ],
            "properties": {
              "Ti16O32": {
                "type": "object",
                "required": [
                  "Eg",
                  "magnetic_moment"
                ],
                "properties": {
                  "Eg": {
                    "type": "number",
                    "unit": "eV"
                  },
                  "magnetic_moment": {
                    "type": "number",
                    "unit": "μB"
                  }
                }
              },
              "Ti15Mo1O32": {
                "type": "object",
                "required": [
                  "Eg",
                  "magnetic_moment"
                ],
                "properties": {
                  "Eg": {
                    "type": "number",
                    "unit": "eV"
                  },
                  "magnetic_moment": {
                    "type": "number",
                    "unit": "μB"
                  }
                }
              },
              "Ti14Mo2O32": {
                "type": "object",
                "required": [
                  "Eg",
                  "magnetic_moment"
                ],
                "properties": {
                  "Eg": {
                    "type": "number",
                    "unit": "eV"
                  },
                  "magnetic_moment": {
                    "type": "number",
                    "unit": "μB"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Computed Kohn-Sham bandgap (Eg in eV) and total magnetic moment (μB) for substitutional Mo-doped TiO2 supercells (rutile and anatase)."
    }
  ],
  "notes": "The scored artifact is compared against the paper's reported values (Table 2) with appropriate tolerances, and the monotonic decreasing trend of Eg with Mo concentration is verified."
}
```

## How you are scored
A hidden verifier reads `/app/outputs/electronic_properties.json`. It compares each reported bandgap and magnetic moment to hidden reference values (obtained from independent calculations under the same conditions) and applies appropriate tolerances that absorb code/functional differences. Additionally, it verifies structural relations among the values: the bandgap must follow a consistent monotonic trend with Mo concentration, and the magnetic moment must behave consistently. The final reward (a float in [0,1]) is a weighted combination of these checks; reporting the paper's numbers without genuine computation will fail the structural and numerical comparisons.
