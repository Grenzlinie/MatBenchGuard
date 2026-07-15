# Elastic constants and phonon stability of V3X (X=Fe, Co, Ni) from first-principles DFT

## Problem background
Vanadium-based binary intermetallic compounds in the cubic A15 crystal structure (space group Pm-3n) are promising candidates for high-temperature structural applications due to their potential mechanical strength, thermal stability, and refractory nature. However, the elastic and vibrational properties of the series V₃X with X = Fe, Co, Ni have not been systematically investigated from first principles. Determining the single-crystal elastic constants and the phonon frequencies at the Brillouin zone center (Gamma point) is critical: the elastic constants allow a direct check of mechanical stability through the Born criteria for cubic crystals, while the absence of imaginary (negative) phonon frequencies confirms vibrational stability. Together, these properties also reveal ductility trends (via the B/G ratio and Cauchy pressure) and form the foundation for understanding the high-temperature performance of these materials.

## Approach
The computational workflow uses plane-wave density functional theory (DFT) within the generalized gradient approximation (PBE exchange-correlation functional). For each compound (V₃Fe, V₃Co, V₃Ni), the cubic A15 primitive cell (8 atoms, V at 6c Wyckoff positions and X at 2a) is fully relaxed to obtain the equilibrium lattice constant and atomic positions. Starting from these optimized structures, three independent elastic constants (C₁₁, C₁₂, C₄₄) are extracted via the stress-strain method. These single-crystal constants are then processed through Voigt-Reuss-Hill averaging to compute polycrystalline moduli (bulk modulus B, shear modulus G, Young's modulus E, B/G ratio, and Cauchy pressure Cₚ = C₁₂ − C₄₄). The mechanical stability of the cubic phase is assessed by verifying the four Born criteria. To evaluate vibrational stability, 2×2×2 supercells are constructed and the forces induced by small finite atomic displacements (0.02 Å) are obtained from DFT. The force constants are built with the finite-displacement method, and the phonon problem is solved at the Γ point to obtain the normal-mode frequencies. A compound is vibrationally stable only if all computed frequencies are real and positive. The DFT engine should be Quantum ESPRESSO (an open-source plane-wave code) coupled with the Phonopy package for the phonon calculations. Pseudopotentials are taken from any standard PBE library for the elements V, Fe, Co, and Ni.

## Reproduction target
For each of the three compounds V₃Fe, V₃Co, and V₃Ni, compute and report:
1. The three independent single-crystal elastic constants C₁₁, C₁₂, C₄₄ (in GPa).
2. From these, using Voigt-Reuss-Hill averaging, the derived polycrystalline moduli: bulk modulus B, shear modulus G, Young's modulus E, B/G ratio, and Cauchy pressure Cₚ (all in GPa except B/G and Cₚ, which are in GPa, and B/G dimensionless). Indicate with a Boolean flag whether the compound satisfies the cubic Born mechanical stability criteria.
3. The eight Γ-point phonon frequencies (in THz) and a Boolean flag that is true only if all frequencies are positive (no imaginary modes).

All results must be written in the structured JSON format specified in the output contract.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- PBE pseudopotentials for V, Fe, Co, Ni

## Workflow steps

### Step 1: Geometry Optimization
- Role: process
- Action: Use DFT (PBE functional, plane-wave basis) to fully relax the cubic A15 structures of V3Fe, V3Co, and V3Ni (space group Pm-3n). Obtain equilibrium lattice constants, atomic positions, and total energies. Save the optimized structures for downstream steps.
- Evidence: `/app/outputs/optimized_structures.json`

### Step 2: Elastic Constants and Polycrystalline Moduli
- Role: scored (load-bearing)
- Action: Starting from the optimized geometries, perform DFT stress-strain calculations to compute the three independent elastic constants C11, C12, C44 for each compound. Then apply Voigt-Reuss-Hill averaging to derive bulk modulus B, shear modulus G, Young's modulus E, B/G ratio, and Cauchy pressure Cp. Include a Born stability check. Output the results in the specified JSON format.
- Output file: `/app/outputs/elastic_properties.json`
- Format: json
- Contract: {"V3Fe": {"C11": float, "C12": float, "C44": float, "B": float, "G": float, "E": float, "B/G": float, "Cp": float, "Born_stable": bool}, "V3Co": {...}, "V3Ni": {...}}
- Scoring: scored by hidden verifier

### Step 3: Phonon Frequencies at Gamma Point
- Role: scored (load-bearing)
- Action: Using the optimized geometries, construct 2x2x2 supercells for each compound. Perform finite-displacement force calculations with DFT, build force constants with Phonopy, and compute phonon frequencies at the Gamma point. Verify that all frequencies are real and positive. Output the eight Gamma-point frequencies per compound and an all_positive flag.
- Output file: `/app/outputs/phonon_gamma_frequencies.json`
- Format: json
- Contract: {"V3Fe": {"frequencies_THz": [float] (8 values), "all_positive": bool}, "V3Co": {...}, "V3Ni": {...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_properties.json`
- `/app/outputs/phonon_gamma_frequencies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_properties.json
- path: `/app/outputs/elastic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed elastic constants and derived mechanical parameters for all three compounds. Scores are assigned by comparing the agent's values to hidden paper-reported reference values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`: `V3Fe`, `V3Co`, `V3Ni`
  - `properties`:
    - `V3Fe`:
      - `type`: object
      - `required`: `C11`, `C12`, `C44`, `B`, `G`, `E`, `B/G`, `Cp`, `Born_stable`
      - `properties`:
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `B`:
          - `type`: number
          - `unit`: GPa
        - `G`:
          - `type`: number
          - `unit`: GPa
        - `E`:
          - `type`: number
          - `unit`: GPa
        - `B/G`:
          - `type`: number
          - `unit`: dimensionless
        - `Cp`:
          - `type`: number
          - `unit`: GPa
        - `Born_stable`:
          - `type`: boolean
    - `V3Co`:
      - `$ref`: #/properties/V3Fe
    - `V3Ni`:
      - `$ref`: #/properties/V3Fe

### phonon_gamma_frequencies.json
- path: `/app/outputs/phonon_gamma_frequencies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Gamma-point phonon frequencies (8 values) and an all_positive flag for each compound. Scores are assigned by comparing the agent's frequencies to hidden paper-reported values with an absolute tolerance, and checking that all_positive is true.
- schema:
  - `type`: object
  - `required`: `V3Fe`, `V3Co`, `V3Ni`
  - `properties`:
    - `V3Fe`:
      - `type`: object
      - `required`: `frequencies_THz`, `all_positive`
      - `properties`:
        - `frequencies_THz`:
          - `type`: array
          - `minItems`: 8
          - `maxItems`: 8
          - `items`:
            - `type`: number
            - `unit`: THz
        - `all_positive`:
          - `type`: boolean
    - `V3Co`:
      - `$ref`: #/properties/V3Fe
    - `V3Ni`:
      - `$ref`: #/properties/V3Fe

Notes: The agent's computed values will be compared against hidden gold values from the source paper (elastic constants from Table 2, phonon frequencies from Table 7) using relative tolerances for elastic quantities and absolute tolerance for phonon frequencies. All values are treated as 'reference_match' because the instruction does not reveal the target numbers; the agent must compute them from first principles.

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
          "V3Fe",
          "V3Co",
          "V3Ni"
        ],
        "properties": {
          "V3Fe": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C44",
              "B",
              "G",
              "E",
              "B/G",
              "Cp",
              "Born_stable"
            ],
            "properties": {
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
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
              "B/G": {
                "type": "number",
                "unit": "dimensionless"
              },
              "Cp": {
                "type": "number",
                "unit": "GPa"
              },
              "Born_stable": {
                "type": "boolean"
              }
            }
          },
          "V3Co": {
            "$ref": "#/properties/V3Fe"
          },
          "V3Ni": {
            "$ref": "#/properties/V3Fe"
          }
        }
      },
      "description": "Computed elastic constants and derived mechanical parameters for all three compounds. Scores are assigned by comparing the agent's values to hidden paper-reported reference values with appropriate tolerances."
    },
    {
      "file": "phonon_gamma_frequencies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "V3Fe",
          "V3Co",
          "V3Ni"
        ],
        "properties": {
          "V3Fe": {
            "type": "object",
            "required": [
              "frequencies_THz",
              "all_positive"
            ],
            "properties": {
              "frequencies_THz": {
                "type": "array",
                "minItems": 8,
                "maxItems": 8,
                "items": {
                  "type": "number",
                  "unit": "THz"
                }
              },
              "all_positive": {
                "type": "boolean"
              }
            }
          },
          "V3Co": {
            "$ref": "#/properties/V3Fe"
          },
          "V3Ni": {
            "$ref": "#/properties/V3Fe"
          }
        }
      },
      "description": "Gamma-point phonon frequencies (8 values) and an all_positive flag for each compound. Scores are assigned by comparing the agent's frequencies to hidden paper-reported values with an absolute tolerance, and checking that all_positive is true."
    }
  ],
  "notes": "The agent's computed values will be compared against hidden gold values from the source paper (elastic constants from Table 2, phonon frequencies from Table 7) using relative tolerances for elastic quantities and absolute tolerance for phonon frequencies. All values are treated as 'reference_match' because the instruction does not reveal the target numbers; the agent must compute them from first principles."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier that reads the two scored output files (`elastic_properties.json` and `phonon_gamma_frequencies.json`). The verifier:
- checks that every required field exists and has the correct type,
- compares your computed elastic constants, derived moduli, and phonon frequencies to hidden reference values with appropriate tolerances,
- verifies that the `Born_stable` and `all_positive` flags are consistent with the computed numbers,
- computes a weighted score per stage and combines them into a final reward between 0 and 1.

Reporting the paper's literature values is not sufficient; you must produce these quantities from first-principles calculations using the described procedure. The hidden reference is derived from independent results reported in the literature for the same system and conditions; no additional information about those values is provided here.
