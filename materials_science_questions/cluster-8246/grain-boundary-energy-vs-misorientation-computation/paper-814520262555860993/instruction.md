# Tensile strength of Σ5(210) grain boundaries in fcc Ni and Co under rigid grain shift and uniaxial loading

## Problem background
Grain boundaries (GBs) drastically influence the mechanical properties of polycrystalline materials, and impurities that segregate to GBs can either strengthen or embrittle the interface. Computational tensile tests are a standard tool for predicting cleavage stresses, but the choice of deformation model can significantly affect the predicted strength. This task focuses on the Σ5(210) symmetric tilt grain boundary in face-centred cubic (fcc) Ni and Co, comparing two common models of tensile deformation: rigid grain shift (RGS), where the upper grain is displaced without any relaxation, and optimized uniaxial loading (OUL), which allows Poisson contraction and full force relaxation. The objective is to compute the stress–strain response and the maximum tensile stress (σ_max) for the clean boundary in both metals and for Ni boundaries with segregated Si (interstitial) and Te (substitutional) under both deformation protocols, thereby probing the quantitative and qualitative differences between the models.

## Approach
The computational workflow begins by constructing supercells of the Σ5(210) GB for fcc Ni and fcc Co using crystallographic tools. After relaxing the supercell geometries with spin-polarised DFT (open-source plane-wave code Quantum ESPRESSO and appropriate PAW pseudopotentials), two types of tensile tests are performed along the GB normal. In the RGS model, incremental strain is applied by rigidly shifting the upper half of the supercell; the axial stress is obtained from finite differences of the total energy. In the OUL model, at each strain step the transverse cell dimensions and atomic forces are fully relaxed (converging lateral stresses and residual forces), and the axial stress is recorded. For each system and model at least 20 strain points are sampled up to and past the stress maximum, yielding a strain–stress curve and a σ_max value. The procedure is repeated for the clean GBs in Ni and Co, and for the Ni GB with Si (interstitial site) and Te (substitutional site). All computed curves and σ_max are compiled into a single JSON file.

## Reproduction target
Produce the stress–strain curves and the maximum tensile stress σ_max for the Σ5(210) grain boundary in fcc Ni and fcc Co under both the rigid grain shift (RGS) and optimized uniaxial loading (OUL) deformation models, for the clean boundary in each metal and for the Ni boundary with interstitially segregated Si and substitutionally segregated Te. The required output artifact is `results.json`, containing arrays of strain and stress (in GPa) and the extracted σ_max (float, GPa) for all eight system/model combinations as listed in the output contract. The hidden verifier will compare the submitted data to the paper’s reported results and check quantitative and qualitative properties; satisfying the verifier’s checks yields full credit.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PAW, PBE/PBEsol): https://www.materialscloud.org/discover/sssp/table/pseudopotentials
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase
- pymatgen: https://pypi.org/project/pymatgen/

## Workflow steps

### Step 1: Build Σ5(210) GB supercells
- Role: process
- Action: Construct the Σ5(210) symmetric tilt grain boundary supercell for fcc Ni (lattice constant 3.517 Å) and fcc Co (3.515 Å) with the GB plane normal to [210]. Additionally, build impurity-segregated cells: Ni with interstitial Si and substitutional Te at the GB. Use crystallographic tools (ASE/pymatgen) to generate the initial unrelaxed structures.
- Evidence: `/app/outputs/initial_structures.json`

### Step 2: Optimize supercell geometries
- Role: process
- Action: Using spin-polarized DFT (Quantum ESPRESSO) with appropriate PAW pseudopotentials, relax the supercell shape and atomic positions for all systems to obtain the equilibrium supercell length c0 and relaxed structures. Use tight convergence criteria for forces and transverse stresses.
- Evidence: `/app/outputs/relaxed_structures.json`

### Step 3: Compute tensile strength (RGS and OUL) and output results.json
- Role: scored (load-bearing)
- Action: For each system (Ni clean, Co clean, Ni+Si, Ni+Te), perform two types of computational tensile tests along the GB normal: (1) Rigid Grain Shift (RGS): apply incremental strain by rigidly shifting the upper grain without any relaxation; compute stress from energy differences and extract the strain-stress curve and maximum stress sigma_max. (2) Optimized Uniaxial Loading (OUL): at each strain increment, allow full relaxation of transverse cell dimensions and atomic forces; compute axial stress and extract sigma_max. Sample at least 20 strain points covering the range up to and beyond the stress maximum. Compile all results into a single JSON file results.json with the structure described in the output contract.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Top-level keys: Ni_clean_RGS, Ni_clean_OUL, Co_clean_RGS, Co_clean_OUL, Ni_Si_RGS, Ni_Si_OUL, Ni_Te_RGS, Ni_Te_OUL. Each value is an object with: strain (array of floats), stress (array of floats, in GPa), sigma_max (float, in GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Strain-stress data and maximum tensile stress for all GB systems under both deformation models.
- schema:
  - `type`: object
  - `required`: `Ni_clean_RGS`, `Ni_clean_OUL`, `Co_clean_RGS`, `Co_clean_OUL`, `Ni_Si_RGS`, `Ni_Si_OUL`, `Ni_Te_RGS`, `Ni_Te_OUL`
  - `properties`:
    - `Ni_clean_RGS`:
      - `type`: object
      - `required`: `strain`, `stress`, `sigma_max`
      - `properties`:
        - `strain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `stress`:
          - `type`: array
          - `items`:
            - `type`: number
        - `sigma_max`:
          - `type`: number
    - `Ni_clean_OUL`:
      - `type`: object
      - `required`: `strain`, `stress`, `sigma_max`
      - `properties`:
        - `strain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `stress`:
          - `type`: array
          - `items`:
            - `type`: number
        - `sigma_max`:
          - `type`: number
    - `Co_clean_RGS`:
      - `type`: object
      - `required`: `strain`, `stress`, `sigma_max`
      - `properties`:
        - `strain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `stress`:
          - `type`: array
          - `items`:
            - `type`: number
        - `sigma_max`:
          - `type`: number
    - `Co_clean_OUL`:
      - `type`: object
      - `required`: `strain`, `stress`, `sigma_max`
      - `properties`:
        - `strain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `stress`:
          - `type`: array
          - `items`:
            - `type`: number
        - `sigma_max`:
          - `type`: number
    - `Ni_Si_RGS`:
      - `type`: object
      - `required`: `strain`, `stress`, `sigma_max`
      - `properties`:
        - `strain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `stress`:
          - `type`: array
          - `items`:
            - `type`: number
        - `sigma_max`:
          - `type`: number
    - `Ni_Si_OUL`:
      - `type`: object
      - `required`: `strain`, `stress`, `sigma_max`
      - `properties`:
        - `strain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `stress`:
          - `type`: array
          - `items`:
            - `type`: number
        - `sigma_max`:
          - `type`: number
    - `Ni_Te_RGS`:
      - `type`: object
      - `required`: `strain`, `stress`, `sigma_max`
      - `properties`:
        - `strain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `stress`:
          - `type`: array
          - `items`:
            - `type`: number
        - `sigma_max`:
          - `type`: number
    - `Ni_Te_OUL`:
      - `type`: object
      - `required`: `strain`, `stress`, `sigma_max`
      - `properties`:
        - `strain`:
          - `type`: array
          - `items`:
            - `type`: number
        - `stress`:
          - `type`: array
          - `items`:
            - `type`: number
        - `sigma_max`:
          - `type`: number

Notes: The checker will recompute sigma_max as the maximum of the stress array, compare clean GB sigma_max values to the paper's reported results, verify that the RGS/OUL sigma_max ratio is approximately 2, and check ordering conditions for impurity-segregated systems.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "Ni_clean_RGS",
          "Ni_clean_OUL",
          "Co_clean_RGS",
          "Co_clean_OUL",
          "Ni_Si_RGS",
          "Ni_Si_OUL",
          "Ni_Te_RGS",
          "Ni_Te_OUL"
        ],
        "properties": {
          "Ni_clean_RGS": {
            "type": "object",
            "required": [
              "strain",
              "stress",
              "sigma_max"
            ],
            "properties": {
              "strain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "stress": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "sigma_max": {
                "type": "number"
              }
            }
          },
          "Ni_clean_OUL": {
            "type": "object",
            "required": [
              "strain",
              "stress",
              "sigma_max"
            ],
            "properties": {
              "strain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "stress": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "sigma_max": {
                "type": "number"
              }
            }
          },
          "Co_clean_RGS": {
            "type": "object",
            "required": [
              "strain",
              "stress",
              "sigma_max"
            ],
            "properties": {
              "strain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "stress": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "sigma_max": {
                "type": "number"
              }
            }
          },
          "Co_clean_OUL": {
            "type": "object",
            "required": [
              "strain",
              "stress",
              "sigma_max"
            ],
            "properties": {
              "strain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "stress": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "sigma_max": {
                "type": "number"
              }
            }
          },
          "Ni_Si_RGS": {
            "type": "object",
            "required": [
              "strain",
              "stress",
              "sigma_max"
            ],
            "properties": {
              "strain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "stress": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "sigma_max": {
                "type": "number"
              }
            }
          },
          "Ni_Si_OUL": {
            "type": "object",
            "required": [
              "strain",
              "stress",
              "sigma_max"
            ],
            "properties": {
              "strain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "stress": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "sigma_max": {
                "type": "number"
              }
            }
          },
          "Ni_Te_RGS": {
            "type": "object",
            "required": [
              "strain",
              "stress",
              "sigma_max"
            ],
            "properties": {
              "strain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "stress": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "sigma_max": {
                "type": "number"
              }
            }
          },
          "Ni_Te_OUL": {
            "type": "object",
            "required": [
              "strain",
              "stress",
              "sigma_max"
            ],
            "properties": {
              "strain": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "stress": {
                "type": "array",
                "items": {
                  "type": "number"
                }
              },
              "sigma_max": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Strain-stress data and maximum tensile stress for all GB systems under both deformation models."
    }
  ],
  "notes": "The checker will recompute sigma_max as the maximum of the stress array, compare clean GB sigma_max values to the paper's reported results, verify that the RGS/OUL sigma_max ratio is approximately 2, and check ordering conditions for impurity-segregated systems."
}
```

## How you are scored
A hidden verifier reads the submitted `results.json` and performs independent checks on each scored workflow stage. For the main tensile test output, the verifier recomputes σ_max from the stress array, compares the values to hidden benchmarks, and evaluates the consistency of the stress–strain curves. Additional checks may assess the correctness of intermediate artefacts (initial and relaxed structures). The final reward is a weighted combination of these checks, rewarding faithful reproduction of the target quantities. Reporting only a final number is not sufficient; the agent must produce the full stress–strain data and derived σ_max as described in the workflow steps and output contract.
