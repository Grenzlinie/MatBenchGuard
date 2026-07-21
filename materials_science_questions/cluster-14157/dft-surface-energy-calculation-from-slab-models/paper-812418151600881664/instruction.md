# DFT Calculation of Magnetic Properties of Cr(001) Thin Films and TM/Cr(001) Systems

## Problem background
Ultrathin chromium films and transition-metal overlayers on Cr(001) exhibit complex magnetic behavior, with potential antiferromagnetic interlayer coupling and spin-density-wave oscillations. A quantitative first-principles understanding of the surface energy, magnetic moments, and preferred magnetic coupling in these systems is important for spintronics applications. This task computes these properties using spin-polarized density-functional theory.

## Approach
We use an open-source density-functional theory (DFT) code (e.g., Elk FP-LAPW or Quantum ESPRESSO) with the Perdew–Burke–Ernzerhof (PBE) functional and collinear spin. The lateral lattice constant is fixed at a = 2.87 Å, corresponding to the experimental bcc Cr value. Clean Cr films are modeled by symmetric (001) slabs with 3, 5, and 7 layers, separated by vacuum. For transition-metal overlayers on Cr(001), we consider a monolayer of Ti, Cr, Mn, or Fe placed on a symmetric Cr half-slab. For each overlayer system we compute two initial spin configurations: ferromagnetic (FM), where the overlayer spins align parallel to the subsurface Cr layer, and antiferromagnetic (AFM), where they align antiparallel. Total energies and layer-resolved magnetic moments are extracted from self-consistent DFT calculations. The surface energy of Cr(001) is derived from the total energies of bulk bcc Cr and the symmetric slabs using the standard surface-energy formula.

## Reproduction target
Compute the (100) surface energy of Cr from the total energies of bulk bcc Cr and 3- and 5-layer symmetric Cr(001) slabs. Obtain the layer-resolved magnetic moments for the 5-layer slab in both FM and AFM configurations, and for the 7-layer slab in its antiferromagnetic ground state. For Ti, Cr, Mn, and Fe monolayers on Cr(001), determine the energy difference between the FM and AFM configurations and the sign of the layer magnetic moments. Report all results in the specified JSON and CSV files under /app/outputs.

## Assets

- Open-source DFT code (e.g., Elk FP-LAPW, Quantum ESPRESSO): https://elk.sourceforge.io

## Workflow steps

### Step 1: DFT calculations on Cr bulk and slabs
- Role: process
- Action: Perform spin-polarized DFT calculations using the PBE functional, collinear spin, lattice constant a=2.87 Å, on antiferromagnetic bcc Cr (bulk) and symmetric 3-, 5-, and 7-layer Cr(001) slabs with vacuum. Save total energies per atom and layer-resolved magnetic moments.
- Evidence: none

### Step 2: Compile Cr slab properties
- Role: scored (load-bearing)
- Action: From the DFT results, compute the surface energy γ_100 using the formula γ = (E_slab - N*E_bulk) / (2*A) where A is the surface area per cell. Compile the total energies, surface energies, and layer-resolved magnetic moments for bulk and 3-, 5-layer slab configurations into cr_slab_properties.json.
- Output file: `/app/outputs/cr_slab_properties.json`
- Format: json
- Contract: Object with keys: 'bulk_Cr': {energy, M1, M2, total_M}, '3_layer_FM': {energy, surface_energy, M1, M2, total_M}, '3_layer_AFM': {energy, surface_energy, M1, M2, total_M}, '5_layer_FM': {energy, surface_energy, M1, M2, M3, total_M}, '5_layer_AFM': {energy, surface_energy, M1, M2, M3, total_M}. Energies in Ry, moments in μ_B, surface energy in J/m².
- Scoring: scored by hidden verifier

### Step 3: Extract 7-layer slab moments
- Role: scored
- Action: Compile the layer-resolved magnetic moments for the 7-layer Cr(001) slab (ground-state antiferromagnetic configuration) into seven_layer_moments.csv.
- Output file: `/app/outputs/seven_layer_moments.csv`
- Format: csv
- Contract: Columns: layer (integer), moment (float).
- Scoring: scored by hidden verifier

### Step 4: DFT calculations on TM/Cr(001) systems
- Role: process
- Action: Perform spin-polarized DFT calculations on symmetric TM monolayer on Cr(001) half-slab for Ti, Cr, Mn, Fe. For each element, compute both ferromagnetic (FM) and antiferromagnetic (AFM) initial spin configurations. Use lattice constant 2.87 Å and same DFT settings as for clean slabs. Save total energies and layer-resolved magnetic moments (M1, M2, M3, interstitial).
- Evidence: none

### Step 5: Compile TM/Cr properties
- Role: scored (load-bearing)
- Action: Compile total energies, magnetic moments, and the energy difference ΔE = E_FM - E_AFM (in mRy per atom) for each TM system into tm_properties.json. For each TM, include the data for both FM and AFM configurations.
- Output file: `/app/outputs/tm_properties.json`
- Format: json
- Contract: Object with keys 'Ti', 'Cr', 'Mn', 'Fe'. Each value is object with 'FM': {energy, M1, M2, M3, Mint}, 'AFM': {energy, M1, M2, M3, Mint}, 'delta_E': float (in mRy per atom).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cr_slab_properties.json`
- `/app/outputs/seven_layer_moments.csv`
- `/app/outputs/tm_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cr_slab_properties.json
- path: `/app/outputs/cr_slab_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Bulk and slab energies, surface energies, and local magnetic moments for clean Cr systems.
- schema:
  - `type`: object
  - `properties`:
    - `bulk_Cr`:
      - `type`: object
      - `properties`:
        - `energy`:
          - `type`: number
          - `unit`: Ry
        - `M1`:
          - `type`: number
          - `unit`: μ_B
        - `M2`:
          - `type`: number
          - `unit`: μ_B
        - `total_M`:
          - `type`: number
          - `unit`: μ_B
      - `required`: `energy`, `M1`, `M2`, `total_M`
    - `3_layer_FM`:
      - `type`: object
      - `properties`:
        - `energy`:
          - `type`: number
          - `unit`: Ry
        - `surface_energy`:
          - `type`: number
          - `unit`: J/m²
        - `M1`:
          - `type`: number
          - `unit`: μ_B
        - `M2`:
          - `type`: number
          - `unit`: μ_B
        - `total_M`:
          - `type`: number
          - `unit`: μ_B
      - `required`: `energy`, `surface_energy`, `M1`, `M2`, `total_M`
    - `3_layer_AFM`:
      - `type`: object
      - `properties`:
        - `energy`:
          - `type`: number
          - `unit`: Ry
        - `surface_energy`:
          - `type`: number
          - `unit`: J/m²
        - `M1`:
          - `type`: number
          - `unit`: μ_B
        - `M2`:
          - `type`: number
          - `unit`: μ_B
        - `total_M`:
          - `type`: number
          - `unit`: μ_B
      - `required`: `energy`, `surface_energy`, `M1`, `M2`, `total_M`
    - `5_layer_FM`:
      - `type`: object
      - `properties`:
        - `energy`:
          - `type`: number
          - `unit`: Ry
        - `surface_energy`:
          - `type`: number
          - `unit`: J/m²
        - `M1`:
          - `type`: number
          - `unit`: μ_B
        - `M2`:
          - `type`: number
          - `unit`: μ_B
        - `M3`:
          - `type`: number
          - `unit`: μ_B
        - `total_M`:
          - `type`: number
          - `unit`: μ_B
      - `required`: `energy`, `surface_energy`, `M1`, `M2`, `M3`, `total_M`
    - `5_layer_AFM`:
      - `type`: object
      - `properties`:
        - `energy`:
          - `type`: number
          - `unit`: Ry
        - `surface_energy`:
          - `type`: number
          - `unit`: J/m²
        - `M1`:
          - `type`: number
          - `unit`: μ_B
        - `M2`:
          - `type`: number
          - `unit`: μ_B
        - `M3`:
          - `type`: number
          - `unit`: μ_B
        - `total_M`:
          - `type`: number
          - `unit`: μ_B
      - `required`: `energy`, `surface_energy`, `M1`, `M2`, `M3`, `total_M`
  - `required`: `bulk_Cr`, `3_layer_FM`, `3_layer_AFM`, `5_layer_FM`, `5_layer_AFM`

### seven_layer_moments.csv
- path: `/app/outputs/seven_layer_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Layer-resolved magnetic moments for the 7-layer Cr(001) slab.
- schema:
  - `type`: table
  - `columns`:
    - `layer`:
      - `type`: integer
      - `description`: Layer index, starting at 1
    - `moment`:
      - `type`: number
      - `unit`: μ_B
      - `description`: Local magnetic moment
  - `required_columns`: `layer`, `moment`

### tm_properties.json
- path: `/app/outputs/tm_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Total energies, local magnetic moments, and coupling energy differences for TM/Cr(001) systems.
- schema:
  - `type`: object
  - `properties`:
    - `Ti`:
      - `type`: object
      - `properties`:
        - `FM`:
          - `type`: object
          - `properties`:
            - `energy`:
              - `type`: number
              - `unit`: Ry
            - `M1`:
              - `type`: number
              - `unit`: μ_B
            - `M2`:
              - `type`: number
              - `unit`: μ_B
            - `M3`:
              - `type`: number
              - `unit`: μ_B
            - `Mint`:
              - `type`: number
              - `unit`: μ_B
          - `required`: `energy`, `M1`, `M2`, `M3`, `Mint`
        - `AFM`:
          - `type`: object
          - `properties`:
            - `energy`:
              - `type`: number
              - `unit`: Ry
            - `M1`:
              - `type`: number
              - `unit`: μ_B
            - `M2`:
              - `type`: number
              - `unit`: μ_B
            - `M3`:
              - `type`: number
              - `unit`: μ_B
            - `Mint`:
              - `type`: number
              - `unit`: μ_B
          - `required`: `energy`, `M1`, `M2`, `M3`, `Mint`
        - `delta_E`:
          - `type`: number
          - `unit`: mRy per atom
      - `required`: `FM`, `AFM`, `delta_E`
    - `Cr`:
      - `type`: object
      - `properties`:
        - `FM`:
          - `type`: object
          - `properties`:
            - `energy`:
              - `type`: number
              - `unit`: Ry
            - `M1`:
              - `type`: number
              - `unit`: μ_B
            - `M2`:
              - `type`: number
              - `unit`: μ_B
            - `M3`:
              - `type`: number
              - `unit`: μ_B
            - `Mint`:
              - `type`: number
              - `unit`: μ_B
          - `required`: `energy`, `M1`, `M2`, `M3`, `Mint`
        - `AFM`:
          - `type`: object
          - `properties`:
            - `energy`:
              - `type`: number
              - `unit`: Ry
            - `M1`:
              - `type`: number
              - `unit`: μ_B
            - `M2`:
              - `type`: number
              - `unit`: μ_B
            - `M3`:
              - `type`: number
              - `unit`: μ_B
            - `Mint`:
              - `type`: number
              - `unit`: μ_B
          - `required`: `energy`, `M1`, `M2`, `M3`, `Mint`
        - `delta_E`:
          - `type`: number
          - `unit`: mRy per atom
      - `required`: `FM`, `AFM`, `delta_E`
    - `Mn`:
      - `type`: object
      - `properties`:
        - `FM`:
          - `type`: object
          - `properties`:
            - `energy`:
              - `type`: number
              - `unit`: Ry
            - `M1`:
              - `type`: number
              - `unit`: μ_B
            - `M2`:
              - `type`: number
              - `unit`: μ_B
            - `M3`:
              - `type`: number
              - `unit`: μ_B
            - `Mint`:
              - `type`: number
              - `unit`: μ_B
          - `required`: `energy`, `M1`, `M2`, `M3`, `Mint`
        - `AFM`:
          - `type`: object
          - `properties`:
            - `energy`:
              - `type`: number
              - `unit`: Ry
            - `M1`:
              - `type`: number
              - `unit`: μ_B
            - `M2`:
              - `type`: number
              - `unit`: μ_B
            - `M3`:
              - `type`: number
              - `unit`: μ_B
            - `Mint`:
              - `type`: number
              - `unit`: μ_B
          - `required`: `energy`, `M1`, `M2`, `M3`, `Mint`
        - `delta_E`:
          - `type`: number
          - `unit`: mRy per atom
      - `required`: `FM`, `AFM`, `delta_E`
    - `Fe`:
      - `type`: object
      - `properties`:
        - `FM`:
          - `type`: object
          - `properties`:
            - `energy`:
              - `type`: number
              - `unit`: Ry
            - `M1`:
              - `type`: number
              - `unit`: μ_B
            - `M2`:
              - `type`: number
              - `unit`: μ_B
            - `M3`:
              - `type`: number
              - `unit`: μ_B
            - `Mint`:
              - `type`: number
              - `unit`: μ_B
          - `required`: `energy`, `M1`, `M2`, `M3`, `Mint`
        - `AFM`:
          - `type`: object
          - `properties`:
            - `energy`:
              - `type`: number
              - `unit`: Ry
            - `M1`:
              - `type`: number
              - `unit`: μ_B
            - `M2`:
              - `type`: number
              - `unit`: μ_B
            - `M3`:
              - `type`: number
              - `unit`: μ_B
            - `Mint`:
              - `type`: number
              - `unit`: μ_B
          - `required`: `energy`, `M1`, `M2`, `M3`, `Mint`
        - `delta_E`:
          - `type`: number
          - `unit`: mRy per atom
      - `required`: `FM`, `AFM`, `delta_E`
  - `required`: `Ti`, `Cr`, `Mn`, `Fe`

Notes: The hidden checker compares the submitted values against the paper's reported surface energy, magnetic moments, and energy differences within appropriate tolerances. No gold values are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cr_slab_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "bulk_Cr": {
            "type": "object",
            "properties": {
              "energy": {
                "type": "number",
                "unit": "Ry"
              },
              "M1": {
                "type": "number",
                "unit": "μ_B"
              },
              "M2": {
                "type": "number",
                "unit": "μ_B"
              },
              "total_M": {
                "type": "number",
                "unit": "μ_B"
              }
            },
            "required": [
              "energy",
              "M1",
              "M2",
              "total_M"
            ]
          },
          "3_layer_FM": {
            "type": "object",
            "properties": {
              "energy": {
                "type": "number",
                "unit": "Ry"
              },
              "surface_energy": {
                "type": "number",
                "unit": "J/m²"
              },
              "M1": {
                "type": "number",
                "unit": "μ_B"
              },
              "M2": {
                "type": "number",
                "unit": "μ_B"
              },
              "total_M": {
                "type": "number",
                "unit": "μ_B"
              }
            },
            "required": [
              "energy",
              "surface_energy",
              "M1",
              "M2",
              "total_M"
            ]
          },
          "3_layer_AFM": {
            "type": "object",
            "properties": {
              "energy": {
                "type": "number",
                "unit": "Ry"
              },
              "surface_energy": {
                "type": "number",
                "unit": "J/m²"
              },
              "M1": {
                "type": "number",
                "unit": "μ_B"
              },
              "M2": {
                "type": "number",
                "unit": "μ_B"
              },
              "total_M": {
                "type": "number",
                "unit": "μ_B"
              }
            },
            "required": [
              "energy",
              "surface_energy",
              "M1",
              "M2",
              "total_M"
            ]
          },
          "5_layer_FM": {
            "type": "object",
            "properties": {
              "energy": {
                "type": "number",
                "unit": "Ry"
              },
              "surface_energy": {
                "type": "number",
                "unit": "J/m²"
              },
              "M1": {
                "type": "number",
                "unit": "μ_B"
              },
              "M2": {
                "type": "number",
                "unit": "μ_B"
              },
              "M3": {
                "type": "number",
                "unit": "μ_B"
              },
              "total_M": {
                "type": "number",
                "unit": "μ_B"
              }
            },
            "required": [
              "energy",
              "surface_energy",
              "M1",
              "M2",
              "M3",
              "total_M"
            ]
          },
          "5_layer_AFM": {
            "type": "object",
            "properties": {
              "energy": {
                "type": "number",
                "unit": "Ry"
              },
              "surface_energy": {
                "type": "number",
                "unit": "J/m²"
              },
              "M1": {
                "type": "number",
                "unit": "μ_B"
              },
              "M2": {
                "type": "number",
                "unit": "μ_B"
              },
              "M3": {
                "type": "number",
                "unit": "μ_B"
              },
              "total_M": {
                "type": "number",
                "unit": "μ_B"
              }
            },
            "required": [
              "energy",
              "surface_energy",
              "M1",
              "M2",
              "M3",
              "total_M"
            ]
          }
        },
        "required": [
          "bulk_Cr",
          "3_layer_FM",
          "3_layer_AFM",
          "5_layer_FM",
          "5_layer_AFM"
        ]
      },
      "description": "Bulk and slab energies, surface energies, and local magnetic moments for clean Cr systems."
    },
    {
      "file": "seven_layer_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "columns": {
          "layer": {
            "type": "integer",
            "description": "Layer index, starting at 1"
          },
          "moment": {
            "type": "number",
            "unit": "μ_B",
            "description": "Local magnetic moment"
          }
        },
        "required_columns": [
          "layer",
          "moment"
        ]
      },
      "description": "Layer-resolved magnetic moments for the 7-layer Cr(001) slab."
    },
    {
      "file": "tm_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "Ti": {
            "type": "object",
            "properties": {
              "FM": {
                "type": "object",
                "properties": {
                  "energy": {
                    "type": "number",
                    "unit": "Ry"
                  },
                  "M1": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M2": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M3": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "Mint": {
                    "type": "number",
                    "unit": "μ_B"
                  }
                },
                "required": [
                  "energy",
                  "M1",
                  "M2",
                  "M3",
                  "Mint"
                ]
              },
              "AFM": {
                "type": "object",
                "properties": {
                  "energy": {
                    "type": "number",
                    "unit": "Ry"
                  },
                  "M1": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M2": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M3": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "Mint": {
                    "type": "number",
                    "unit": "μ_B"
                  }
                },
                "required": [
                  "energy",
                  "M1",
                  "M2",
                  "M3",
                  "Mint"
                ]
              },
              "delta_E": {
                "type": "number",
                "unit": "mRy per atom"
              }
            },
            "required": [
              "FM",
              "AFM",
              "delta_E"
            ]
          },
          "Cr": {
            "type": "object",
            "properties": {
              "FM": {
                "type": "object",
                "properties": {
                  "energy": {
                    "type": "number",
                    "unit": "Ry"
                  },
                  "M1": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M2": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M3": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "Mint": {
                    "type": "number",
                    "unit": "μ_B"
                  }
                },
                "required": [
                  "energy",
                  "M1",
                  "M2",
                  "M3",
                  "Mint"
                ]
              },
              "AFM": {
                "type": "object",
                "properties": {
                  "energy": {
                    "type": "number",
                    "unit": "Ry"
                  },
                  "M1": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M2": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M3": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "Mint": {
                    "type": "number",
                    "unit": "μ_B"
                  }
                },
                "required": [
                  "energy",
                  "M1",
                  "M2",
                  "M3",
                  "Mint"
                ]
              },
              "delta_E": {
                "type": "number",
                "unit": "mRy per atom"
              }
            },
            "required": [
              "FM",
              "AFM",
              "delta_E"
            ]
          },
          "Mn": {
            "type": "object",
            "properties": {
              "FM": {
                "type": "object",
                "properties": {
                  "energy": {
                    "type": "number",
                    "unit": "Ry"
                  },
                  "M1": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M2": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M3": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "Mint": {
                    "type": "number",
                    "unit": "μ_B"
                  }
                },
                "required": [
                  "energy",
                  "M1",
                  "M2",
                  "M3",
                  "Mint"
                ]
              },
              "AFM": {
                "type": "object",
                "properties": {
                  "energy": {
                    "type": "number",
                    "unit": "Ry"
                  },
                  "M1": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M2": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M3": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "Mint": {
                    "type": "number",
                    "unit": "μ_B"
                  }
                },
                "required": [
                  "energy",
                  "M1",
                  "M2",
                  "M3",
                  "Mint"
                ]
              },
              "delta_E": {
                "type": "number",
                "unit": "mRy per atom"
              }
            },
            "required": [
              "FM",
              "AFM",
              "delta_E"
            ]
          },
          "Fe": {
            "type": "object",
            "properties": {
              "FM": {
                "type": "object",
                "properties": {
                  "energy": {
                    "type": "number",
                    "unit": "Ry"
                  },
                  "M1": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M2": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M3": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "Mint": {
                    "type": "number",
                    "unit": "μ_B"
                  }
                },
                "required": [
                  "energy",
                  "M1",
                  "M2",
                  "M3",
                  "Mint"
                ]
              },
              "AFM": {
                "type": "object",
                "properties": {
                  "energy": {
                    "type": "number",
                    "unit": "Ry"
                  },
                  "M1": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M2": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "M3": {
                    "type": "number",
                    "unit": "μ_B"
                  },
                  "Mint": {
                    "type": "number",
                    "unit": "μ_B"
                  }
                },
                "required": [
                  "energy",
                  "M1",
                  "M2",
                  "M3",
                  "Mint"
                ]
              },
              "delta_E": {
                "type": "number",
                "unit": "mRy per atom"
              }
            },
            "required": [
              "FM",
              "AFM",
              "delta_E"
            ]
          }
        },
        "required": [
          "Ti",
          "Cr",
          "Mn",
          "Fe"
        ]
      },
      "description": "Total energies, local magnetic moments, and coupling energy differences for TM/Cr(001) systems."
    }
  ],
  "notes": "The hidden checker compares the submitted values against the paper's reported surface energy, magnetic moments, and energy differences within appropriate tolerances. No gold values are revealed here."
}
```

## How you are scored
A hidden verifier independently reads each output file. It recomputes the surface energy from the bulk and slab energies you provide, checks that the layer magnetic moments for the clean slabs alternate sign and approximate a spin-density-wave pattern, and verifies that the energy differences for the transition-metal systems correctly identify whether FM or AFM coupling is the lower-energy state. Each scored artifact contributes a weighted fraction to the final reward. The verifier uses hidden tolerances derived from the expected spread between different DFT implementations; reporting the paper’s numbers is necessary but not sufficient — the computed values must follow the correct physical trends and satisfy the structural checks.
