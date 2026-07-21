# 2D Magnetic Array Cluster Simulation and Analysis

## Problem background
Understanding cluster formation in interacting magnetic nanoparticle arrays is crucial for high-density bit-patterned media. The Ising–Preisach model combines single-particle Stoner–Wohlfarth switching with long-range dipolar interactions, providing a simple yet physically rich picture. This task investigates cluster size distributions under different demagnetization protocols and magnetization processes, and how these distributions depend on interaction strength and AC field frequency.

## Approach
The approach implements a 2D Ising–Preisach model on a square lattice with periodic boundary conditions. Each lattice site represents a perpendicularly magnetized single-domain cobalt nanoparticle with a rectangular hysteresis loop whose coercive field is drawn from a Gaussian distribution. Particles interact through long-range magnetostatic dipolar fields. Monte Carlo dynamics are simulated with Metropolis acceptance using Stoner–Wohlfarth energy barriers. Four distinct demagnetization protocols are applied: AC (a decaying oscillatory field), thermal (heating and cooling), DC (a constant reverse field to reach remanence), and natural (relaxation in zero field). From each demagnetized state, first magnetization curves are recorded under an increasing external field. The effect of interaction strength is studied by varying the normalized lattice constant d, and the influence of AC frequency is also explored. Cluster sizes are identified using the Swendsen–Wang algorithm.

## Reproduction target
You must produce two output files inside `/app/outputs/`:

- `cluster_distributions.json`: cluster order histograms for every condition described in the workflow steps (demagnetization types, interaction strengths d, AC frequencies, and selected applied fields on the virgin magnetization curve).
- `magnetization_curves.json`: first magnetization curves for each demagnetized initial state and for each interaction strength.

The exact schema for both files is given in the workflow steps and the output contract.

## Assets

- Python 3: python3
- NumPy: numpy

## Workflow steps

### Step 1: Initialize 2D Ising–Preisach lattice
- Role: process
- Action: Set up a 2D square lattice of Ising–Preisach hysterons representing perpendicularly magnetized single-domain cobalt nanoparticles. Use material constants: particle radius r=5 nm (volume V=4/3πr³), saturation polarization P_S=1.78 T, anisotropy constant K=4.1e5 J/m³. The mean coercivity field is H_K0 = 2K/P_S, and individual coercive fields are sampled from a Gaussian distribution with standard deviation H_Kσ = 0.1 H_K0. Use periodic boundary conditions and a lattice size of at least 32×32 sites. Initialize spin orientation randomly up/down along the perpendicular easy axis.
- Evidence: `/app/outputs/init_log.txt`

### Step 2: Run Monte Carlo demagnetization simulations
- Role: process
- Action: For each normalized lattice constant d = a / a0 with a0 = 10 nm (d = 1.0, 1.1, 1.2, 1.3, 1.4) and each demagnetization protocol (AC, thermal, DC, natural), run Metropolis Monte Carlo dynamics at a base temperature of 300 K to obtain demagnetized spin configurations. AC demagnetization: apply a decaying oscillatory field H_AC(t)=15e5 e^{-0.015 t} cos(2π f t) [A/m] with base frequency f0=0.07 MCS^{-1}; also repeat at two higher frequencies (e.g., 2f0, 3f0) for d=1.0. Thermal demagnetization: heat to 900 K in zero field, then cool to 300 K. DC demagnetization: apply a constant reverse field from positive saturation to reach zero remanence when the field is removed. Natural demagnetization: relax the system in zero field for 5000 MCS. Energy barriers are computed via the Stoner–Wohlfarth formula using the effective field H_eff = H + H_int, where H_int is the dipolar interaction field. Save final spin configurations for each condition.
- Evidence: `/app/outputs/demagnetization_log.txt`

### Step 3: Simulate first magnetization curves
- Role: process
- Action: Starting from each demagnetized spin configuration produced in step_02, apply an increasing external magnetic field with normalized field h = H / H_K0 (from 0 to at least 1.2) in small quasi-static steps. At each field step, run Metropolis Monte Carlo updates to reach equilibrium and record the normalized magnetization m = M / M_S. Also save spin configurations at selected field values (e.g., h = 0, 0.2, 0.4, 0.6, 0.8, 1.0) for later cluster analysis on the virgin magnetization curve. All simulations use the same material constants, dipolar interactions, and temperature (300 K).
- Evidence: `/app/outputs/magnetization_sweep_log.txt`

### Step 4: Compute cluster order distributions
- Role: scored (load-bearing)
- Action: From all spin configurations saved during steps 02 and 03, apply the Swendsen–Wang cluster-identification algorithm to find connected clusters of parallel spins. For each distinct condition (demagnetization type, interaction strength d, AC frequency, and applied field on the virgin curve), produce a histogram of cluster order c (number of spins in a cluster) and its count. Aggregate the histograms into a single JSON file cluster_distributions.json with the structure described in the output contract.
- Output file: `/app/outputs/cluster_distributions.json`
- Format: json
- Contract: Top-level object with keys: demag_types (array of objects, each with demag_type string and distribution array of {cluster_order int, count int}), interaction_strengths (array of objects, each with d float and distribution array of {cluster_order int, count int}), frequencies (array of objects, each with frequency float and distribution array of {cluster_order int, count int}), virgin_curve_fields (array of objects, each with applied_field_h float and distribution array of {cluster_order int, count int}).
- Scoring: scored by hidden verifier

### Step 5: Compile magnetization curves
- Role: scored
- Action: Collect the magnetization vs applied field data recorded during the magnetization sweeps in step_03. For each demagnetized initial state and for each interaction strength d, output the series of (field_h, magnetization) pairs. Write the result as magnetization_curves.json following the format specified in the output contract.
- Output file: `/app/outputs/magnetization_curves.json`
- Format: json
- Contract: Top-level object with keys: first_magnetization_curve_demag (array of objects, each with demag_type string, field_h float, magnetization float), first_magnetization_curve_interaction (array of objects, each with d float, field_h float, magnetization float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cluster_distributions.json`
- `/app/outputs/magnetization_curves.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cluster_distributions.json
- path: `/app/outputs/cluster_distributions.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Cluster order distributions for all simulated conditions. The checker will verify that the cluster order distributions exhibit physically expected relative trends.
- schema:
  - `type`: object
  - `required`: `demag_types`, `interaction_strengths`, `frequencies`, `virgin_curve_fields`
  - `properties`:
    - `demag_types`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `demag_type`, `distribution`
        - `properties`:
          - `demag_type`:
            - `type`: string
          - `distribution`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `cluster_order`, `count`
              - `properties`:
                - `cluster_order`:
                  - `type`: integer
                - `count`:
                  - `type`: integer
    - `interaction_strengths`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `d`, `distribution`
        - `properties`:
          - `d`:
            - `type`: number
          - `distribution`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `cluster_order`, `count`
              - `properties`:
                - `cluster_order`:
                  - `type`: integer
                - `count`:
                  - `type`: integer
    - `frequencies`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `frequency`, `distribution`
        - `properties`:
          - `frequency`:
            - `type`: number
          - `distribution`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `cluster_order`, `count`
              - `properties`:
                - `cluster_order`:
                  - `type`: integer
                - `count`:
                  - `type`: integer
    - `virgin_curve_fields`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `applied_field_h`, `distribution`
        - `properties`:
          - `applied_field_h`:
            - `type`: number
          - `distribution`:
            - `type`: array
            - `items`:
              - `type`: object
              - `required`: `cluster_order`, `count`
              - `properties`:
                - `cluster_order`:
                  - `type`: integer
                - `count`:
                  - `type`: integer

### magnetization_curves.json
- path: `/app/outputs/magnetization_curves.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: First magnetization curves recorded after different demagnetization protocols and for different interaction strengths. The checker will verify that the magnetization curves exhibit physically expected relative trends.
- schema:
  - `type`: object
  - `required`: `first_magnetization_curve_demag`, `first_magnetization_curve_interaction`
  - `properties`:
    - `first_magnetization_curve_demag`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `demag_type`, `field_h`, `magnetization`
        - `properties`:
          - `demag_type`:
            - `type`: string
          - `field_h`:
            - `type`: number
          - `magnetization`:
            - `type`: number
    - `first_magnetization_curve_interaction`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `d`, `field_h`, `magnetization`
        - `properties`:
          - `d`:
            - `type`: number
          - `field_h`:
            - `type`: number
          - `magnetization`:
            - `type`: number

Notes: All magnetic field values are normalized by H_K0, and magnetizations are normalized by M_S. The exactly identity of the paper is not disclosed; the checker verifies structural trends and relative ordering, not exact numerical matches.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cluster_distributions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "demag_types",
          "interaction_strengths",
          "frequencies",
          "virgin_curve_fields"
        ],
        "properties": {
          "demag_types": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "demag_type",
                "distribution"
              ],
              "properties": {
                "demag_type": {
                  "type": "string"
                },
                "distribution": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "cluster_order",
                      "count"
                    ],
                    "properties": {
                      "cluster_order": {
                        "type": "integer"
                      },
                      "count": {
                        "type": "integer"
                      }
                    }
                  }
                }
              }
            }
          },
          "interaction_strengths": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "d",
                "distribution"
              ],
              "properties": {
                "d": {
                  "type": "number"
                },
                "distribution": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "cluster_order",
                      "count"
                    ],
                    "properties": {
                      "cluster_order": {
                        "type": "integer"
                      },
                      "count": {
                        "type": "integer"
                      }
                    }
                  }
                }
              }
            }
          },
          "frequencies": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "frequency",
                "distribution"
              ],
              "properties": {
                "frequency": {
                  "type": "number"
                },
                "distribution": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "cluster_order",
                      "count"
                    ],
                    "properties": {
                      "cluster_order": {
                        "type": "integer"
                      },
                      "count": {
                        "type": "integer"
                      }
                    }
                  }
                }
              }
            }
          },
          "virgin_curve_fields": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "applied_field_h",
                "distribution"
              ],
              "properties": {
                "applied_field_h": {
                  "type": "number"
                },
                "distribution": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "required": [
                      "cluster_order",
                      "count"
                    ],
                    "properties": {
                      "cluster_order": {
                        "type": "integer"
                      },
                      "count": {
                        "type": "integer"
                      }
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "Cluster order distributions for all simulated conditions. The checker will verify that the cluster order distributions exhibit physically expected relative trends."
    },
    {
      "file": "magnetization_curves.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "first_magnetization_curve_demag",
          "first_magnetization_curve_interaction"
        ],
        "properties": {
          "first_magnetization_curve_demag": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "demag_type",
                "field_h",
                "magnetization"
              ],
              "properties": {
                "demag_type": {
                  "type": "string"
                },
                "field_h": {
                  "type": "number"
                },
                "magnetization": {
                  "type": "number"
                }
              }
            }
          },
          "first_magnetization_curve_interaction": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "d",
                "field_h",
                "magnetization"
              ],
              "properties": {
                "d": {
                  "type": "number"
                },
                "field_h": {
                  "type": "number"
                },
                "magnetization": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "First magnetization curves recorded after different demagnetization protocols and for different interaction strengths. The checker will verify that the magnetization curves exhibit physically expected relative trends."
    }
  ],
  "notes": "All magnetic field values are normalized by H_K0, and magnetizations are normalized by M_S. The exactly identity of the paper is not disclosed; the checker verifies structural trends and relative ordering, not exact numerical matches."
}
```

## How you are scored
Your solution is evaluated by a hidden automated checker. The checker first validates that both output files are well‑formed JSON and contain all required fields. It then scores the physical content by comparing the cluster distributions and magnetization curves against expected structural and relative trends that arise from the underlying physics (e.g., the ordering of cluster sizes across different conditions, the shapes of the magnetization curves, and their systematic changes with interaction strength and frequency). The checker does not demand exact numerical matches to any reference; instead it checks whether the computed trends are physically reasonable. The final reward is a weighted combination of the scores from the two artifacts, with the cluster distributions carrying the larger weight.
