# Numerical Homogenization of Elastic Properties of Claystone using Dilute and Mori-Tanaka Schemes

## Problem background
Heterogeneous rocks like claystone are composed of multiple mineral phases with different mechanical properties. Estimating the macroscopic elastic modulus from the properties of individual phases is important when conventional large-scale laboratory tests are impractical. This task uses analytical homogenization to upscale phase-level elastic moduli and Poisson's ratios to the macroscopic scale. You will compute the effective Young's modulus and Poisson's ratio of a claystone composite using two homogenization schemes, given the elastic constants and volume fractions of its three constituent phases (clay matrix, calcite, quartz). The computed values can be compared with experimental uniaxial compression data to assess the accuracy of the homogenization methodology.

## Approach
The claystone is modeled as a three-phase composite with a clay matrix containing spherical inclusions of calcite and quartz (matrix-inclusion morphology). Two analytical homogenization schemes are used: the dilute scheme, which neglects inclusion interactions, and the Mori–Tanaka scheme, which accounts for inclusion interactions. Each scheme provides closed-form expressions for the effective bulk modulus and shear modulus in terms of the phase properties and volume fractions. The corresponding Young's modulus and Poisson's ratio are then obtained from standard elasticity relations. The required input parameters (Young's moduli, Poisson's ratios, and volume fractions for each phase) are specified in the workflow step.

## Reproduction target
Compute the effective Young's modulus and Poisson's ratio for the claystone composite using both the dilute and Mori–Tanaka schemes, given the phase properties: clay matrix (E0 = 3.3 GPa, ν0 = 0.34), calcite (E1 = 70 GPa, ν1 = 0.27), quartz (E2 = 101 GPa, ν2 = 0.06) and volume fractions f0 = 0.7254, f1 = 0.1433, f2 = 0.1313. Output the four results (E_dil, v_dil, E_mt, v_mt) as a JSON object.

## Assets
No external datasets, models, or specialized tools are required. The computation uses standard Python with basic mathematical operations. All necessary inputs are provided in the workflow step.

## Workflow steps

### Step 1: Homogenization of elastic properties
- Role: scored (load-bearing)
- Action: Compute the macroscopic Young's modulus and Poisson's ratio of a three-phase claystone composite using the dilute and Mori–Tanaka homogenization schemes. Use the given phase properties: clay matrix (E0=3.3 GPa, ν0=0.34), calcite (E1=70 GPa, ν1=0.27), quartz (E2=101 GPa, ν2=0.06) and volume fractions f0=0.7254, f1=0.1433, f2=0.1313. Compute the effective bulk and shear moduli via the formulas described (dilute scheme and Mori–Tanaka scheme for matrix-inclusion morphology), then convert to Young's moduli and Poisson's ratios. Output the four results to homogenized_results.json.
- Output file: `/app/outputs/homogenized_results.json`
- Format: json
- Contract: object with keys E_dil, v_dil, E_mt, v_mt, each a float value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/homogenized_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### homogenized_results.json
- path: `/app/outputs/homogenized_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Homogenized elastic constants computed from phase properties and volume fractions via dilute and Mori-Tanaka schemes.
- schema:
  - `type`: object
  - `required`: `E_dil`, `v_dil`, `E_mt`, `v_mt`
  - `items`:
    - `E_dil`:
      - `description`: Young's modulus from dilute scheme (GPa)
      - `type`: number
    - `v_dil`:
      - `description`: Poisson's ratio from dilute scheme
      - `type`: number
    - `E_mt`:
      - `description`: Young's modulus from Mori-Tanaka scheme (GPa)
      - `type`: number
    - `v_mt`:
      - `description`: Poisson's ratio from Mori-Tanaka scheme
      - `type`: number

Notes: Only the homogenization computation is reproduced. The comparison with experimental data is implicitly covered by verifying the computed values against the paper-reported homogenized results. All required inputs are given in the step action.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "homogenized_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "E_dil",
          "v_dil",
          "E_mt",
          "v_mt"
        ],
        "items": {
          "E_dil": {
            "description": "Young's modulus from dilute scheme (GPa)",
            "type": "number"
          },
          "v_dil": {
            "description": "Poisson's ratio from dilute scheme",
            "type": "number"
          },
          "E_mt": {
            "description": "Young's modulus from Mori-Tanaka scheme (GPa)",
            "type": "number"
          },
          "v_mt": {
            "description": "Poisson's ratio from Mori-Tanaka scheme",
            "type": "number"
          }
        }
      },
      "description": "Homogenized elastic constants computed from phase properties and volume fractions via dilute and Mori-Tanaka schemes."
    }
  ],
  "notes": "Only the homogenization computation is reproduced. The comparison with experimental data is implicitly covered by verifying the computed values against the paper-reported homogenized results. All required inputs are given in the step action."
}
```

## How you are scored
Your output artifact, homogenized_results.json, is evaluated by an automated checker that independently recomputes the four homogenized quantities using the same formulas and inputs. The checker compares each of your values to the expected reference values. Full credit for a quantity is awarded if the relative difference is within a hidden tolerance; otherwise, partial credit is given proportionally to the relative error. The final score is the average of the scores for the four quantities. Producing the correct numbers via an honest computation is required; guessing or hard-coding will not achieve the full reward.
