# Ab initio molecular dynamics study of liquid Ni62Nb38 alloy local structure, dynamics and electronic properties

## Problem background
Liquid Ni₆₂Nb₃₈ alloy is a prototypical binary system with excellent glass-forming ability, attributed to strong hetero-coordination and a deep eutectic. Understanding how its local atomic structure, chemical ordering, and atomic mobility evolve as the melt is cooled from the stable liquid down to the deeply undercooled regime is crucial for rationalizing the formation of metallic glasses. Ab initio molecular dynamics provides an accurate, first‑principles description of these properties, yielding insight into the increasing short‑range order, the emergence of medium‑range order, the nature of chemical bonding, and the slowing of atomic diffusion that facilitates glass transition. In this task you will compute these structure, dynamics, and electronic properties across a temperature range of 1873 K to 1233 K.

## Approach
The study uses ab initio molecular dynamics (AIMD) based on density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional. A cubic supercell containing 62 Ni and 38 Nb atoms (100 atoms total) with periodic boundary conditions is simulated in the NVT ensemble. The system is first melted at high temperature to erase memory, then cooled at a controlled rate to four target temperatures: 1873 K, 1473 K, 1403 K, and 1233 K. At each temperature, an equilibrium trajectory is collected. From these trajectories, the total and partial pair distribution functions g(r), total structure factors S(q), bond‑angle distributions for all triple types, partial coordination numbers, Warren–Cowley chemical short‑range order parameters, and mean square displacements (from which self‑diffusion coefficients are obtained via the Einstein relation) are computed. Additionally, static DFT calculations on representative snapshots provide the total and projected electronic density of states (DOS). The goal is to compare these quantities across the temperature series and to characterize the atomic‑scale ordering and bonding trends.

## Reproduction target
Using an open‑source AIMD code (e.g., CP2K, Quantum ESPRESSO) with the PBE functional and public pseudopotentials, compute the structural, dynamic, and electronic properties of liquid Ni₆₂Nb₃₈ at four temperatures: 1873 K, 1473 K, 1403 K, and 1233 K. The final deliverable is a single JSON file (`simulation_results.json`) containing:

- **total pair distribution function g(r)** (up to 10 Å) per temperature;
- **total structure factor S(q)** (up to 10 Å⁻¹) per temperature;
- **bond‑angle distributions** for the six triple types (Ni‑Ni‑Ni, Ni‑Ni‑Nb, Nb‑Ni‑Nb, Nb‑Nb‑Nb, Nb‑Nb‑Ni, Ni‑Nb‑Ni) per temperature;
- **chemical short‑range order parameters** α(Ni‑Ni), α(Ni‑Nb), α(Nb‑Ni), α(Nb‑Nb) per temperature;
- **self‑diffusion coefficients** D_Ni, D_Nb, and D_total (in 10⁻⁴ cm²/s) per temperature, obtained from the Einstein relation applied to the mean square displacements;
- **electronic density of states** (total and projected on Ni s, p, d and Nb s, p, d) at 1873 K and 1233 K, with the Fermi level set to 0 eV.

The aim is to capture the key structural and trends that emerge as the liquid is undercooled, and to compare the computed properties with the known behaviour of this alloy.

## Assets

- Open-source AIMD/DFT software (e.g., CP2K, Quantum ESPRESSO, SIESTA)
- PBE pseudopotentials for Ni and Nb (e.g., PAW-PBE from SSSP library or GTH-PBE for CP2K)
- Scattering factor tables (Waasmaier & Kirfel, 1995 or equivalent): 10.1107/S0108767394013292

## Workflow steps

### Step 1: Generate initial random supercell
- Role: process
- Action: Create a cubic supercell containing 62 Ni atoms and 38 Nb atoms with random positions. Use periodic boundary conditions.
- Evidence: `/app/outputs/initial_cell.xyz`

### Step 2: Run AIMD simulation of liquid Ni62Nb38
- Role: process
- Action: Perform ab initio molecular dynamics in the NVT ensemble using the PBE functional and appropriate pseudopotentials. Heat the supercell to 2500 K and equilibrate, then cool to the target temperatures 1873 K, 1473 K, 1403 K, and 1233 K, collecting production trajectories at each temperature.
- Evidence: `/app/outputs/md_trajectories.tar`

### Step 3: Compute electronic density of states (DOS)
- Role: process
- Action: Using a snapshot from the production runs at 1873 K and 1233 K, run a static DFT calculation with higher plane-wave cutoff to obtain the total and projected (Ni s,p,d; Nb s,p,d) density of states.
- Evidence: `/app/outputs/dos_data.npz`

### Step 4: Analyze structure, dynamics and electronic properties
- Role: scored (load-bearing)
- Action: From the trajectories and DOS data, compute for each temperature: total pair distribution function g(r) up to 10 Å, total structure factor S(q) up to 10 Å⁻¹, bond-angle distributions for all triple types, partial coordination numbers and Warren-Cowley CSRO parameters, mean square displacements and self-diffusion coefficients via Einstein relation, and the full density of states (energy, total and projected). Package all results into a single JSON file.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: JSON object with keys: 'temperatures' (list of 4 floats in K), 'total_g_r' (list of dicts per temperature with 'r' (Å) and 'g' arrays), 'total_S_q' (list of dicts per temperature with 'q' (Å⁻¹) and 'S' arrays), 'bond_angle_distributions' (dict mapping bond type string to list of dicts per temperature with 'angle' (deg) and 'probability' arrays), 'csro_parameters' (list of dicts per temperature with keys 'Ni-Ni','Ni-Nb','Nb-Ni','Nb-Nb'), 'diffusion_coefficients' (list of dicts per temperature with keys 'D_Ni','D_Nb','D_total' in units of 1e-4 cm²/s), 'dos' (list of dicts for 1873 K and 1233 K with 'energy' (eV, Fermi level=0), 'total_dos','Ni_d','Nb_d','Ni_s','Ni_p','Nb_s','Nb_p' arrays).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled structural, dynamic, and electronic properties of liquid Ni62Nb38 at four temperatures. The checker compares peak positions, trends, and magnitudes against a hidden paper-based reference.
- schema:
  - `type`: object
  - `required`: `temperatures`, `total_g_r`, `total_S_q`, `bond_angle_distributions`, `csro_parameters`, `diffusion_coefficients`, `dos`
  - `properties`:
    - `temperatures`:
      - `type`: array
      - `items`:
        - `type`: number
      - `minItems`: 4
      - `maxItems`: 4
    - `total_g_r`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `r`, `g`
        - `properties`:
          - `r`:
            - `type`: array
            - `items`:
              - `type`: number
          - `g`:
            - `type`: array
            - `items`:
              - `type`: number
      - `minItems`: 4
      - `maxItems`: 4
    - `total_S_q`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `q`, `S`
        - `properties`:
          - `q`:
            - `type`: array
            - `items`:
              - `type`: number
          - `S`:
            - `type`: array
            - `items`:
              - `type`: number
      - `minItems`: 4
      - `maxItems`: 4
    - `bond_angle_distributions`:
      - `type`: object
      - `patternProperties`:
        - `^(Ni-Ni-Ni|Ni-Ni-Nb|Nb-Ni-Nb|Nb-Nb-Nb|Nb-Nb-Ni|Ni-Nb-Ni)$`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `angle`, `probability`
            - `properties`:
              - `angle`:
                - `type`: array
                - `items`:
                  - `type`: number
              - `probability`:
                - `type`: array
                - `items`:
                  - `type`: number
          - `minItems`: 4
          - `maxItems`: 4
      - `additionalProperties`: False
    - `csro_parameters`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `Ni-Ni`, `Ni-Nb`, `Nb-Ni`, `Nb-Nb`
        - `properties`:
          - `Ni-Ni`:
            - `type`: number
          - `Ni-Nb`:
            - `type`: number
          - `Nb-Ni`:
            - `type`: number
          - `Nb-Nb`:
            - `type`: number
      - `minItems`: 4
      - `maxItems`: 4
    - `diffusion_coefficients`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `D_Ni`, `D_Nb`, `D_total`
        - `properties`:
          - `D_Ni`:
            - `type`: number
            - `units`: 1e-4 cm²/s
          - `D_Nb`:
            - `type`: number
            - `units`: 1e-4 cm²/s
          - `D_total`:
            - `type`: number
            - `units`: 1e-4 cm²/s
      - `minItems`: 4
      - `maxItems`: 4
    - `dos`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `energy`, `total_dos`, `Ni_d`, `Nb_d`, `Ni_s`, `Ni_p`, `Nb_s`, `Nb_p`
        - `properties`:
          - `energy`:
            - `type`: array
            - `items`:
              - `type`: number
          - `total_dos`:
            - `type`: array
            - `items`:
              - `type`: number
          - `Ni_d`:
            - `type`: array
            - `items`:
              - `type`: number
          - `Nb_d`:
            - `type`: array
            - `items`:
              - `type`: number
          - `Ni_s`:
            - `type`: array
            - `items`:
              - `type`: number
          - `Ni_p`:
            - `type`: array
            - `items`:
              - `type`: number
          - `Nb_s`:
            - `type`: array
            - `items`:
              - `type`: number
          - `Nb_p`:
            - `type`: array
            - `items`:
              - `type`: number
      - `minItems`: 2
      - `maxItems`: 2

Notes: The checker will verify structural (g(r), S(q), bond angles), chemical ordering (CSRO), dynamic (diffusion coefficients), and electronic (DOS) trends and features, awarding partial credit per criterion out of six defined categories.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "temperatures",
          "total_g_r",
          "total_S_q",
          "bond_angle_distributions",
          "csro_parameters",
          "diffusion_coefficients",
          "dos"
        ],
        "properties": {
          "temperatures": {
            "type": "array",
            "items": {
              "type": "number"
            },
            "minItems": 4,
            "maxItems": 4
          },
          "total_g_r": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "r",
                "g"
              ],
              "properties": {
                "r": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "g": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            },
            "minItems": 4,
            "maxItems": 4
          },
          "total_S_q": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "q",
                "S"
              ],
              "properties": {
                "q": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "S": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            },
            "minItems": 4,
            "maxItems": 4
          },
          "bond_angle_distributions": {
            "type": "object",
            "patternProperties": {
              "^(Ni-Ni-Ni|Ni-Ni-Nb|Nb-Ni-Nb|Nb-Nb-Nb|Nb-Nb-Ni|Ni-Nb-Ni)$": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "angle",
                    "probability"
                  ],
                  "properties": {
                    "angle": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    },
                    "probability": {
                      "type": "array",
                      "items": {
                        "type": "number"
                      }
                    }
                  }
                },
                "minItems": 4,
                "maxItems": 4
              }
            },
            "additionalProperties": false
          },
          "csro_parameters": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "Ni-Ni",
                "Ni-Nb",
                "Nb-Ni",
                "Nb-Nb"
              ],
              "properties": {
                "Ni-Ni": {
                  "type": "number"
                },
                "Ni-Nb": {
                  "type": "number"
                },
                "Nb-Ni": {
                  "type": "number"
                },
                "Nb-Nb": {
                  "type": "number"
                }
              }
            },
            "minItems": 4,
            "maxItems": 4
          },
          "diffusion_coefficients": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "D_Ni",
                "D_Nb",
                "D_total"
              ],
              "properties": {
                "D_Ni": {
                  "type": "number",
                  "units": "1e-4 cm²/s"
                },
                "D_Nb": {
                  "type": "number",
                  "units": "1e-4 cm²/s"
                },
                "D_total": {
                  "type": "number",
                  "units": "1e-4 cm²/s"
                }
              }
            },
            "minItems": 4,
            "maxItems": 4
          },
          "dos": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "energy",
                "total_dos",
                "Ni_d",
                "Nb_d",
                "Ni_s",
                "Ni_p",
                "Nb_s",
                "Nb_p"
              ],
              "properties": {
                "energy": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "total_dos": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "Ni_d": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "Nb_d": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "Ni_s": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "Ni_p": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "Nb_s": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                },
                "Nb_p": {
                  "type": "array",
                  "items": {
                    "type": "number"
                  }
                }
              }
            },
            "minItems": 2,
            "maxItems": 2
          }
        }
      },
      "description": "Compiled structural, dynamic, and electronic properties of liquid Ni62Nb38 at four temperatures. The checker compares peak positions, trends, and magnitudes against a hidden paper-based reference."
    }
  ],
  "notes": "The checker will verify structural (g(r), S(q), bond angles), chemical ordering (CSRO), dynamic (diffusion coefficients), and electronic (DOS) trends and features, awarding partial credit per criterion out of six defined categories."
}
```

## How you are scored
A hidden verifier independently inspects your `simulation_results.json` and compares the reported quantities against the expected physical behaviour. The verifier checks the following categories: (1) features of the pair distribution functions, (2) features of the structure factors, (3) evolution of bond‑angle distributions, (4) sign and magnitude of CSRO parameters, (5) temperature dependence and relative ordering of self‑diffusion coefficients, and (6) shape and orbital character of the electronic density of states. Each category is assessed by matching qualitative trends and key landmark positions (e.g., peak locations, peak splitting, sign of order parameters) that are characteristic of liquid Ni₆₂Nb₃₈. Full credit is awarded when a sufficient number of categories (typically four or more) are correctly reproduced; partial credit may be given for fewer. The verifier does not require bit‑level numerical agreement, but expects the essential structural and dynamic signatures to be present. You must execute the AIMD simulation and analysis; merely reporting the reference values without performing the calculation is insufficient.
