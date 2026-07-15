# Computation of Magnetoelastic Constants and Polycrystalline Parameters for MnPt Phases

## Problem background
Magnetoelasticity, the coupling between strain and magnetization, is critical for applications in sensors, actuators, and spin-based devices. In magnetic materials the magnetoelastic response — including anisotropic magnetostriction — arises from the dependence of magnetocrystalline anisotropy on lattice deformations. Understanding this coupling and its quantitative description through magnetoelastic constants and derived magnetostrictive coefficients is essential for modelling and exploiting these effects.

In the tetragonal MnPt system, different collinear magnetic orderings (ferromagnetic, and two antiferromagnetic configurations) are possible, and the magnetoelastic behaviour can vary substantially with magnetic structure. This work targets a first-principles computational determination of the full set of elastic and magnetoelastic constants for each magnetic phase, and from them the magnetostrictive coefficients and polycrystalline magnetostriction parameters. Computing these quantities provides insight into how the magnetic ordering governs the magnetoelastic response, and serves as a reference for interpreting experimental magnetostriction measurements in MnPt.

## Approach
The computational pipeline uses ab‑initio density‑functional theory (DFT) with spin–orbit coupling. The generalised‑gradient approximation (PBE) is employed for the exchange‑correlation functional. The approach proceeds as follows:

1. **Structure preparation:** From the tetragonal L1₀ crystal structure of MnPt, primitive‑cell models are built for three collinear spin arrangements — ferromagnetic (FM) alignment and two antiferromagnetic orders (AFM1 and AFM2) — with initial magnetic moments oriented along the c‑axis.

2. **Relaxation:** Each structure is relaxed with DFT to obtain equilibrium lattice parameters and atomic positions.

3. **Elastic constants:** The six independent elastic constants (C11, C12, C13, C33, C44, C66) are computed for each magnetic phase using a finite‑displacement approach. Symmetry‑adapted strains are applied to the relaxed cell, and the resulting stress–strain relations yield the elastic tensor referred to the FM primitive‑cell axes.

4. **Magnetoelastic constants:** The magnetoelastic constants (b21, b22, b3, b4, b3') are obtained via the strain‑energy method. For each phase, symmetry‑appropriate finite strains are applied, and for each strained configuration the magnetocrystalline anisotropy energy difference between two orthogonal magnetization directions is computed with spin‑orbit coupling. The constants are extracted by linear fitting of these energy differences versus strain.

5. **Derived magnetostrictive coefficients and polycrystalline parameters:** Using the computed elastic and magnetoelastic constants, the magnetostrictive coefficients λ are calculated from the analytic formulas for a tetragonal system. Averaging over magnetization directions for an initial demagnetized state with easy‑axis alignment yields the polycrystalline magnetostriction parameters ξ and η.

The open‑source codes Quantum ESPRESSO (DFT engine) and the AELAS/MEALAS packages are used for elastic and magnetoelastic property calculations, but alternative equivalent implementations are acceptable as long as they reproduce the same computational protocol.

## Reproduction target
Produce the following three scored artifacts:

- **elastic_constants.json** – the six independent elastic constants C11, C12, C13, C33, C44, C66 (in GPa) for each magnetic phase (FM, AFM1, AFM2).
- **magnetoelastic_constants.json** – the five magnetoelastic constants b21, b22, b3, b4, b3' (in MPa) for each magnetic phase.
- **polycrystalline_parameters.json** – the polycrystalline magnetostriction parameters ξ and η (dimensionless, in 10⁻⁶) for each magnetic phase, computed from the elastic and magnetoelastic constants assuming an easy‑axis initial demagnetized state.

The calculations must be carried out for the three collinear magnetic configurations with moments along the c‑axis: FM, AFM1, and AFM2. The elastic constants and magnetoelastic constants must refer to the axes of the FM primitive cell. The results are scored independently; details of the required output format are given in the workflow steps below.

## Assets

- SSSP pseudopotentials (PBE, PAW) for Mn and Pt: https://www.materialscloud.org/discover/sssp/
- AELAS package: https://github.com/zhangruixi/AELAS
- MEALAS package: https://github.com/nieves-pablo/MEALAS
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- MnPt L1₀ crystal structure

## Workflow steps

### Step 1: Prepare initial structures for MnPt magnetic phases
- Role: process
- Action: Obtain the L1₀ crystal structure of MnPt from public databases or construct from literature lattice parameters, and set up primitive cells for the FM, AFM1, and AFM2 magnetic configurations with appropriate initial magnetic moments and spin orientations along the c-axis. Create Quantum ESPRESSO input files for each phase.
- Evidence: `/app/outputs/initial_structures.log`

### Step 2: Relax crystal structures
- Role: process
- Action: Perform DFT structure relaxation for the FM, AFM1, and AFM2 phases using Quantum ESPRESSO with PBE functional and spin-orbit coupling (SOC) where required. Converge forces and stresses to obtain equilibrium lattice parameters and atomic positions.
- Evidence: `/app/outputs/relaxation_output.log`

### Step 3: Compute elastic constants C_ij
- Role: scored
- Action: Compute the six independent elastic constants C11, C12, C13, C33, C44, C66 (in GPa) for each magnetic phase (FM, AFM1, AFM2) using a finite-displacement approach. Use AELAS or equivalent with Quantum ESPRESSO to apply symmetry-appropriate strains and extract the elastic tensor referred to the axes of the FM primitive cell. Save results in JSON format.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"FM": {"C11": <float>, "C12": <float>, "C13": <float>, "C33": <float>, "C44": <float>, "C66": <float>}, "AFM1": {...}, "AFM2": {...}}
- Scoring: scored by hidden verifier

### Step 4: Compute magnetoelastic constants b_i
- Role: scored (load-bearing)
- Action: Compute the magnetoelastic constants b21, b22, b3, b4, b3' (in MPa) for each magnetic phase using the strain-energy method. For each relaxed structure apply symmetry-appropriate finite strains, compute the energy difference between two magnetization directions (MAE difference) via spin-orbit-coupled DFT, and extract the constants by linear fitting. Use MEALAS or equivalent script to generate strained structures and analyze data. Save results in JSON format.
- Output file: `/app/outputs/magnetoelastic_constants.json`
- Format: json
- Contract: {"FM": {"b21": <float>, "b22": <float>, "b3": <float>, "b4": <float>, "b3p": <float>}, "AFM1": {...}, "AFM2": {...}}
- Scoring: scored by hidden verifier

### Step 5: Derive magnetostrictive coefficients and polycrystalline parameters
- Role: scored
- Action: From the computed elastic constants (step_3) and magnetoelastic constants (step_4), calculate the magnetostrictive coefficients λ using the analytic formulas for a tetragonal system, and then compute the polycrystalline magnetostriction parameters ξ and η (in 10⁻⁶) for each magnetic phase assuming an initial demagnetized state with easy-axis alignment. Save ξ and η in JSON format.
- Output file: `/app/outputs/polycrystalline_parameters.json`
- Format: json
- Contract: {"FM": {"xi": <float>, "eta": <float>}, "AFM1": {...}, "AFM2": {...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/magnetoelastic_constants.json`
- `/app/outputs/polycrystalline_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Elastic constants (GPa) for the three magnetic phases computed by finite-displacement DFT, to be compared with values in Table F.4.
- schema:
  - `type`: object
  - `required`: `FM`, `AFM1`, `AFM2`
  - `properties`:
    - `FM`:
      - `type`: object
      - `required`: `C11`, `C12`, `C13`, `C33`, `C44`, `C66`
      - `additionalProperties`: False
      - `properties`:
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C13`:
          - `type`: number
          - `unit`: GPa
        - `C33`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `C66`:
          - `type`: number
          - `unit`: GPa
    - `AFM1`:
      - `type`: object
      - `required`: `C11`, `C12`, `C13`, `C33`, `C44`, `C66`
      - `additionalProperties`: False
      - `properties`:
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C13`:
          - `type`: number
          - `unit`: GPa
        - `C33`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `C66`:
          - `type`: number
          - `unit`: GPa
    - `AFM2`:
      - `type`: object
      - `required`: `C11`, `C12`, `C13`, `C33`, `C44`, `C66`
      - `additionalProperties`: False
      - `properties`:
        - `C11`:
          - `type`: number
          - `unit`: GPa
        - `C12`:
          - `type`: number
          - `unit`: GPa
        - `C13`:
          - `type`: number
          - `unit`: GPa
        - `C33`:
          - `type`: number
          - `unit`: GPa
        - `C44`:
          - `type`: number
          - `unit`: GPa
        - `C66`:
          - `type`: number
          - `unit`: GPa

### magnetoelastic_constants.json
- path: `/app/outputs/magnetoelastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Magnetoelastic constants (MPa) obtained from strained MAE calculations; to be compared with Table 1 values.
- schema:
  - `type`: object
  - `required`: `FM`, `AFM1`, `AFM2`
  - `properties`:
    - `FM`:
      - `type`: object
      - `required`: `b21`, `b22`, `b3`, `b4`, `b3p`
      - `additionalProperties`: False
      - `properties`:
        - `b21`:
          - `type`: number
          - `unit`: MPa
        - `b22`:
          - `type`: number
          - `unit`: MPa
        - `b3`:
          - `type`: number
          - `unit`: MPa
        - `b4`:
          - `type`: number
          - `unit`: MPa
        - `b3p`:
          - `type`: number
          - `unit`: MPa
    - `AFM1`:
      - `type`: object
      - `required`: `b21`, `b22`, `b3`, `b4`, `b3p`
      - `additionalProperties`: False
      - `properties`:
        - `b21`:
          - `type`: number
          - `unit`: MPa
        - `b22`:
          - `type`: number
          - `unit`: MPa
        - `b3`:
          - `type`: number
          - `unit`: MPa
        - `b4`:
          - `type`: number
          - `unit`: MPa
        - `b3p`:
          - `type`: number
          - `unit`: MPa
    - `AFM2`:
      - `type`: object
      - `required`: `b21`, `b22`, `b3`, `b4`, `b3p`
      - `additionalProperties`: False
      - `properties`:
        - `b21`:
          - `type`: number
          - `unit`: MPa
        - `b22`:
          - `type`: number
          - `unit`: MPa
        - `b3`:
          - `type`: number
          - `unit`: MPa
        - `b4`:
          - `type`: number
          - `unit`: MPa
        - `b3p`:
          - `type`: number
          - `unit`: MPa

### polycrystalline_parameters.json
- path: `/app/outputs/polycrystalline_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Polycrystalline magnetostriction parameters ξ and η (10⁻⁶), derived from elastic and magnetoelastic constants, to be compared with Table 1.
- schema:
  - `type`: object
  - `required`: `FM`, `AFM1`, `AFM2`
  - `properties`:
    - `FM`:
      - `type`: object
      - `required`: `xi`, `eta`
      - `additionalProperties`: False
      - `properties`:
        - `xi`:
          - `type`: number
          - `unit`: 10⁻⁶
        - `eta`:
          - `type`: number
          - `unit`: 10⁻⁶
    - `AFM1`:
      - `type`: object
      - `required`: `xi`, `eta`
      - `additionalProperties`: False
      - `properties`:
        - `xi`:
          - `type`: number
          - `unit`: 10⁻⁶
        - `eta`:
          - `type`: number
          - `unit`: 10⁻⁶
    - `AFM2`:
      - `type`: object
      - `required`: `xi`, `eta`
      - `additionalProperties`: False
      - `properties`:
        - `xi`:
          - `type`: number
          - `unit`: 10⁻⁶
        - `eta`:
          - `type`: number
          - `unit`: 10⁻⁶

Notes: The magnetostrictive coefficients λ are not directly submitted; the checker will recompute them from the elastic and magnetoelastic constants using formulas (B.8)–(B.12) and compare with the paper's reported λ values. Elastic and polycrystalline parameters will be compared via tolerance-based exact match.

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
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "FM",
          "AFM1",
          "AFM2"
        ],
        "properties": {
          "FM": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C13",
              "C33",
              "C44",
              "C66"
            ],
            "additionalProperties": false,
            "properties": {
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C13": {
                "type": "number",
                "unit": "GPa"
              },
              "C33": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "C66": {
                "type": "number",
                "unit": "GPa"
              }
            }
          },
          "AFM1": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C13",
              "C33",
              "C44",
              "C66"
            ],
            "additionalProperties": false,
            "properties": {
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C13": {
                "type": "number",
                "unit": "GPa"
              },
              "C33": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "C66": {
                "type": "number",
                "unit": "GPa"
              }
            }
          },
          "AFM2": {
            "type": "object",
            "required": [
              "C11",
              "C12",
              "C13",
              "C33",
              "C44",
              "C66"
            ],
            "additionalProperties": false,
            "properties": {
              "C11": {
                "type": "number",
                "unit": "GPa"
              },
              "C12": {
                "type": "number",
                "unit": "GPa"
              },
              "C13": {
                "type": "number",
                "unit": "GPa"
              },
              "C33": {
                "type": "number",
                "unit": "GPa"
              },
              "C44": {
                "type": "number",
                "unit": "GPa"
              },
              "C66": {
                "type": "number",
                "unit": "GPa"
              }
            }
          }
        }
      },
      "description": "Elastic constants (GPa) for the three magnetic phases computed by finite-displacement DFT, to be compared with values in Table F.4."
    },
    {
      "file": "magnetoelastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "FM",
          "AFM1",
          "AFM2"
        ],
        "properties": {
          "FM": {
            "type": "object",
            "required": [
              "b21",
              "b22",
              "b3",
              "b4",
              "b3p"
            ],
            "additionalProperties": false,
            "properties": {
              "b21": {
                "type": "number",
                "unit": "MPa"
              },
              "b22": {
                "type": "number",
                "unit": "MPa"
              },
              "b3": {
                "type": "number",
                "unit": "MPa"
              },
              "b4": {
                "type": "number",
                "unit": "MPa"
              },
              "b3p": {
                "type": "number",
                "unit": "MPa"
              }
            }
          },
          "AFM1": {
            "type": "object",
            "required": [
              "b21",
              "b22",
              "b3",
              "b4",
              "b3p"
            ],
            "additionalProperties": false,
            "properties": {
              "b21": {
                "type": "number",
                "unit": "MPa"
              },
              "b22": {
                "type": "number",
                "unit": "MPa"
              },
              "b3": {
                "type": "number",
                "unit": "MPa"
              },
              "b4": {
                "type": "number",
                "unit": "MPa"
              },
              "b3p": {
                "type": "number",
                "unit": "MPa"
              }
            }
          },
          "AFM2": {
            "type": "object",
            "required": [
              "b21",
              "b22",
              "b3",
              "b4",
              "b3p"
            ],
            "additionalProperties": false,
            "properties": {
              "b21": {
                "type": "number",
                "unit": "MPa"
              },
              "b22": {
                "type": "number",
                "unit": "MPa"
              },
              "b3": {
                "type": "number",
                "unit": "MPa"
              },
              "b4": {
                "type": "number",
                "unit": "MPa"
              },
              "b3p": {
                "type": "number",
                "unit": "MPa"
              }
            }
          }
        }
      },
      "description": "Magnetoelastic constants (MPa) obtained from strained MAE calculations; to be compared with Table 1 values."
    },
    {
      "file": "polycrystalline_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "FM",
          "AFM1",
          "AFM2"
        ],
        "properties": {
          "FM": {
            "type": "object",
            "required": [
              "xi",
              "eta"
            ],
            "additionalProperties": false,
            "properties": {
              "xi": {
                "type": "number",
                "unit": "10⁻⁶"
              },
              "eta": {
                "type": "number",
                "unit": "10⁻⁶"
              }
            }
          },
          "AFM1": {
            "type": "object",
            "required": [
              "xi",
              "eta"
            ],
            "additionalProperties": false,
            "properties": {
              "xi": {
                "type": "number",
                "unit": "10⁻⁶"
              },
              "eta": {
                "type": "number",
                "unit": "10⁻⁶"
              }
            }
          },
          "AFM2": {
            "type": "object",
            "required": [
              "xi",
              "eta"
            ],
            "additionalProperties": false,
            "properties": {
              "xi": {
                "type": "number",
                "unit": "10⁻⁶"
              },
              "eta": {
                "type": "number",
                "unit": "10⁻⁶"
              }
            }
          }
        }
      },
      "description": "Polycrystalline magnetostriction parameters ξ and η (10⁻⁶), derived from elastic and magnetoelastic constants, to be compared with Table 1."
    }
  ],
  "notes": "The magnetostrictive coefficients λ are not directly submitted; the checker will recompute them from the elastic and magnetoelastic constants using formulas (B.8)–(B.12) and compare with the paper's reported λ values. Elastic and polycrystalline parameters will be compared via tolerance-based exact match."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each of the three scored artifacts.

- **elastic_constants.json** – the submitted elastic constants are compared to reference values (with appropriate tolerances that account for the use of different DFT toolchains and numerical precision).
- **magnetoelastic_constants.json** – the submitted magnetoelastic constants are compared to reference values under similar tolerance conditions.
- **polycrystalline_parameters.json** – the submitted ξ and η are compared to reference values. Additionally, the verifier will recompute the magnetostrictive coefficients λ from your submitted elastic and magnetoelastic constants using the standard analytic formulas for a tetragonal system, and compare them to hidden reference λ values to reward internal consistency.

The verifier does not require an exact match to any particular published set of numbers; a result that is close to the expected values within the tolerance criteria earns full credit, and the reward degrades monotonically as deviations grow. The overall reward is a weighted combination of the scores from the individual artifacts.
