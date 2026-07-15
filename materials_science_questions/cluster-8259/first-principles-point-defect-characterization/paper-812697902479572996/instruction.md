# First-principles reaction energetics and charge transition levels of N-incorporated defects in SiO₂

## Problem background
N-incorporated silicon oxide films are used as gate dielectrics in advanced semiconductor devices to reduce leakage current and improve reliability. However, the atomic-scale origins of these improvements remain unclear because nitrogen can adopt many bonding configurations and may introduce charge-trapping states in the band gap. This work investigates, by means of first-principles density-functional theory (DFT), the energetics and charge states of various nitrogen-related defects in α-quartz SiO₂. It compares structures with and without hydrogen termination to assess how they affect the presence of electrically active states within the energy gap.

## Approach
The study uses spin-polarized DFT with the generalized-gradient approximation (GGA) and a plane-wave basis. A 54-atom triclinic supercell of α-quartz is constructed, and five N-incorporated defect models are introduced: S2 (twofold N substitution), S3 (threefold N), V2 (twofold N with an O vacancy), V3 (threefold N with an O vacancy), and S2O (N–O bonding). Hydrogen-terminated counterparts (S2H, S3H, V2H, V3H, S2OH) are also considered. For each structure, total-energy calculations are performed in several charge states (Q = −1, 0, +1, and +2 where applicable), applying a monopole correction for charged defects. Additionally, total energies of perfect α-quartz, the NO molecule (doublet), the O₂ molecule (triplet), and an isolated H atom are obtained. From these raw energies, reaction energies are computed for the reactions NO + X → z O₂ + Y, where X represents the perfect quartz or the O-vacancy cell and Y is the corresponding defect structure, assuming all gas-phase molecules remain inside the oxide film. Thermodynamic charge-transition levels μ_th are then derived using Ω(Q,μ) = E(Q) + Q μ and aligned to the Si midgap via a valence-band offset of 4.3 eV between SiO₂ and Si. The analysis compares the computed μ_th values to the Si band gap to determine whether hydrogen termination eliminates active trap states.

## Reproduction target
Produce a single JSON file containing (i) all raw DFT total energies for every labelled supercell and molecule, (ii) the derived reaction energies for the specified NO + X reactions, and (iii) the thermodynamic charge-transition levels μ_th for each N-incorporated defect structure (S2, S3, V2, V3, S2O) and its H-terminated counterpart, expressed relative to the Si midgap. From these μ_th values, determine whether each H-terminated structure possesses a transition that falls within the Si band gap—i.e., whether a charge-trap state could be electrically active under device operating conditions.

## Assets

- α‑quartz crystal structure (trigonal, space group P3_2_1 or P3_1_2): Public crystallographic databases, e.g., Materials Project (mp-6930) at https://materialsproject.org/materials/mp-6930
- Pseudopotentials: ultrasoft for O, N; norm-conserving for Si, H: Standard pseudopotential libraries, e.g., Quantum ESPRESSO pseudopotential tables at https://www.quantum-espresso.org/pseudopotentials
- Plane‑wave DFT code supporting GGA and ultrasoft pseudopotentials (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Construct supercell and defect models
- Role: process
- Action: Build a 54‑atom triclinic α‑quartz supercell. Create the atomic coordinates for the N‑incorporated defect structures S2, S3, V2, V3, S2O and their H‑terminated counterparts S2H, S3H, V2H, V3H, S2OH as described in the paper.
- Evidence: `/app/outputs/defect_models.txt`

### Step 2: Perform DFT total-energy calculations
- Role: process
- Action: Run spin‑polarized GGA plane‑wave DFT calculations using appropriate pseudopotentials and plane‑wave cutoff. Relax geometries for each defect in charge states Q = -1, 0, +1 (and Q = +2 where applicable) and include monopole corrections for charged defects. Also compute total energies of perfect α‑quartz, the NO molecule, the O₂ molecule, and an isolated H atom.
- Evidence: `/app/outputs/dft.log`

### Step 3: Compute reaction energies and thermodynamic levels
- Role: scored (load-bearing)
- Action: From the total energies obtained in step02, compute the reaction energies for the NO + X → zO₂ + Y reactions (both endothermic and exothermic cases) assuming all molecules remain in the oxide film. Compute thermodynamic charge‑transition levels μ_th using Ω(Q,μ)=E(Q)+Qμ, and align them to the Si midgap using a valence‑band offset of 4.3 eV. Write all raw total energies, the resulting reaction energies, and the μ_th values into a single JSON file reproduction_results.json.
- Output file: `/app/outputs/reproduction_results.json`
- Format: json
- Contract: The JSON object must contain the keys "total_energies", "reaction_energies", "thermodynamic_levels", with exact sub-keys and structure as specified in the Output contract below.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reproduction_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reproduction_results.json
- path: `/app/outputs/reproduction_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: The agent's computed reaction energies and thermodynamic charge-transition levels; the checker recomputes these quantities from the raw total_energies and compares them to the paper's reported values.
- schema:
  - `type`: object
  - `required`: `total_energies`, `reaction_energies`, `thermodynamic_levels`
  - `properties`:
    - `total_energies`:
      - `type`: object
      - `required`: `SiO2_bulk`, `VO`, `NO`, `O2`, `H`, `S2_-1`, `S2_0`, `S2_+1`, `S3_-1`, `S3_0`, `S3_+1`, `S2O_-1`, `S2O_0`, `S2O_+1`, `V2_-1`, `V2_0`, `V2_+1`, `V3_-1`, `V3_0`, `V3_+1`, `S2H_0`, `S2H_+1`, `S3H_0`, `S3H_+1`, `V2H_0`, `V2H_+2`, `V3H_0`, `V3H_+1`, `S2OH_0`, `S2OH_+1`
      - `additionalProperties`: False
      - `properties`:
        - `SiO2_bulk`:
          - `type`: number
        - `VO`:
          - `type`: number
        - `NO`:
          - `type`: number
        - `O2`:
          - `type`: number
        - `H`:
          - `type`: number
        - `S2_-1`:
          - `type`: number
        - `S2_0`:
          - `type`: number
        - `S2_+1`:
          - `type`: number
        - `S3_-1`:
          - `type`: number
        - `S3_0`:
          - `type`: number
        - `S3_+1`:
          - `type`: number
        - `S2O_-1`:
          - `type`: number
        - `S2O_0`:
          - `type`: number
        - `S2O_+1`:
          - `type`: number
        - `V2_-1`:
          - `type`: number
        - `V2_0`:
          - `type`: number
        - `V2_+1`:
          - `type`: number
        - `V3_-1`:
          - `type`: number
        - `V3_0`:
          - `type`: number
        - `V3_+1`:
          - `type`: number
        - `S2H_0`:
          - `type`: number
        - `S2H_+1`:
          - `type`: number
        - `S3H_0`:
          - `type`: number
        - `S3H_+1`:
          - `type`: number
        - `V2H_0`:
          - `type`: number
        - `V2H_+2`:
          - `type`: number
        - `V3H_0`:
          - `type`: number
        - `V3H_+1`:
          - `type`: number
        - `S2OH_0`:
          - `type`: number
        - `S2OH_+1`:
          - `type`: number
    - `reaction_energies`:
      - `type`: array
      - `minItems`: 7
      - `maxItems`: 7
      - `items`:
        - `type`: object
        - `required`: `reaction`, `energy_eV`
        - `properties`:
          - `reaction`:
            - `type`: string
            - `enum`: `NO + SiO2 -> O2 + S2`, `NO + SiO2 -> O2 + S3`, `NO + SiO2 -> 0.5 O2 + S2O`, `NO + VO -> O2 + V2`, `NO + VO -> O2 + V3`, `NO + VO -> S2O`, `NO + VO -> 0.5 O2 + S2`
          - `energy_eV`:
            - `type`: number
    - `thermodynamic_levels`:
      - `type`: array
      - `minItems`: 15
      - `maxItems`: 15
      - `items`:
        - `type`: object
        - `required`: `structure`, `transition`, `mu_th_eV`
        - `properties`:
          - `structure`:
            - `type`: string
            - `enum`: `S2`, `S3`, `V2`, `V3`, `S2O`, `S2H`, `S3H`, `V2H`, `V3H`, `S2OH`
          - `transition`:
            - `type`: string
            - `enum`: `0/+`, `-/0`, `0/++`
          - `mu_th_eV`:
            - `type`: number

Notes: All energies are in eV and must be internally consistent. The exact set of structure labels, reactions, and transitions must match those described in the paper's method. The checker recomputes μ_th from total_energies using the stated formulas and compares against the paper's Table I within a tolerance, and checks the sign and trend of reaction energies.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reproduction_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "total_energies",
          "reaction_energies",
          "thermodynamic_levels"
        ],
        "properties": {
          "total_energies": {
            "type": "object",
            "required": [
              "SiO2_bulk",
              "VO",
              "NO",
              "O2",
              "H",
              "S2_-1",
              "S2_0",
              "S2_+1",
              "S3_-1",
              "S3_0",
              "S3_+1",
              "S2O_-1",
              "S2O_0",
              "S2O_+1",
              "V2_-1",
              "V2_0",
              "V2_+1",
              "V3_-1",
              "V3_0",
              "V3_+1",
              "S2H_0",
              "S2H_+1",
              "S3H_0",
              "S3H_+1",
              "V2H_0",
              "V2H_+2",
              "V3H_0",
              "V3H_+1",
              "S2OH_0",
              "S2OH_+1"
            ],
            "additionalProperties": false,
            "properties": {
              "SiO2_bulk": {
                "type": "number"
              },
              "VO": {
                "type": "number"
              },
              "NO": {
                "type": "number"
              },
              "O2": {
                "type": "number"
              },
              "H": {
                "type": "number"
              },
              "S2_-1": {
                "type": "number"
              },
              "S2_0": {
                "type": "number"
              },
              "S2_+1": {
                "type": "number"
              },
              "S3_-1": {
                "type": "number"
              },
              "S3_0": {
                "type": "number"
              },
              "S3_+1": {
                "type": "number"
              },
              "S2O_-1": {
                "type": "number"
              },
              "S2O_0": {
                "type": "number"
              },
              "S2O_+1": {
                "type": "number"
              },
              "V2_-1": {
                "type": "number"
              },
              "V2_0": {
                "type": "number"
              },
              "V2_+1": {
                "type": "number"
              },
              "V3_-1": {
                "type": "number"
              },
              "V3_0": {
                "type": "number"
              },
              "V3_+1": {
                "type": "number"
              },
              "S2H_0": {
                "type": "number"
              },
              "S2H_+1": {
                "type": "number"
              },
              "S3H_0": {
                "type": "number"
              },
              "S3H_+1": {
                "type": "number"
              },
              "V2H_0": {
                "type": "number"
              },
              "V2H_+2": {
                "type": "number"
              },
              "V3H_0": {
                "type": "number"
              },
              "V3H_+1": {
                "type": "number"
              },
              "S2OH_0": {
                "type": "number"
              },
              "S2OH_+1": {
                "type": "number"
              }
            }
          },
          "reaction_energies": {
            "type": "array",
            "minItems": 7,
            "maxItems": 7,
            "items": {
              "type": "object",
              "required": [
                "reaction",
                "energy_eV"
              ],
              "properties": {
                "reaction": {
                  "type": "string",
                  "enum": [
                    "NO + SiO2 -> O2 + S2",
                    "NO + SiO2 -> O2 + S3",
                    "NO + SiO2 -> 0.5 O2 + S2O",
                    "NO + VO -> O2 + V2",
                    "NO + VO -> O2 + V3",
                    "NO + VO -> S2O",
                    "NO + VO -> 0.5 O2 + S2"
                  ]
                },
                "energy_eV": {
                  "type": "number"
                }
              }
            }
          },
          "thermodynamic_levels": {
            "type": "array",
            "minItems": 15,
            "maxItems": 15,
            "items": {
              "type": "object",
              "required": [
                "structure",
                "transition",
                "mu_th_eV"
              ],
              "properties": {
                "structure": {
                  "type": "string",
                  "enum": [
                    "S2",
                    "S3",
                    "V2",
                    "V3",
                    "S2O",
                    "S2H",
                    "S3H",
                    "V2H",
                    "V3H",
                    "S2OH"
                  ]
                },
                "transition": {
                  "type": "string",
                  "enum": [
                    "0/+",
                    "-/0",
                    "0/++"
                  ]
                },
                "mu_th_eV": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "The agent's computed reaction energies and thermodynamic charge-transition levels; the checker recomputes these quantities from the raw total_energies and compares them to the paper's reported values."
    }
  ],
  "notes": "All energies are in eV and must be internally consistent. The exact set of structure labels, reactions, and transitions must match those described in the paper's method. The checker recomputes μ_th from total_energies using the stated formulas and compares against the paper's Table I within a tolerance, and checks the sign and trend of reaction energies."
}
```

## How you are scored
A hidden verifier will recompute the reaction energies and thermodynamic levels from the raw total energies you submit. It will compare your derived reaction energies (sign and relative magnitude) and your μ_th values to reference expectations, with appropriate tolerances for numerical differences that arise from different computational implementations. Your final reward is a weighted combination: correctness and trends of the reaction energies, accuracy of the thermodynamic levels, and completeness of the results across all required structures. Providing the raw total energies is mandatory; reporting only the final numbers without the underlying data will lead to a low score.
