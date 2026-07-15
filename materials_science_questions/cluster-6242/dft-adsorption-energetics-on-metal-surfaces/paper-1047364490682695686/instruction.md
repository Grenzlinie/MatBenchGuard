# DFT adsorption energetics and bonding analysis of coal structural units on pyrite surfaces

## Problem background
In coal flotation desulfurization, fine pyrite (FeS2) particles can adhere to coal surfaces, contaminating clean coal with sulfur. The microscopic mechanism of this adhesion is not fully understood. This task uses density functional theory (DFT) to study the interaction between pyrite surfaces and four oxygen-containing structural units that represent coal: Ph-OH, Ph-COOH, Ph-CO-CH3, and Ph-O-CH3. The objective is to compute the adsorption energies and bonding properties for each unit on a pyrite (100) surface, and to determine whether the interactions are weak physical adsorption.

## Approach
The computational approach employs plane-wave DFT with the GGA-PW91 exchange-correlation functional and ultra-soft pseudopotentials. A slab model of the pyrite (100) surface is constructed from the bulk crystal, and the isolated geometries of the four coal structural units are optimized in large cubic cells. For each coal unit, the molecule is placed at four distinct initial adsorption sites on the slab: above an Fe atom (F), with the benzene ring perpendicular to the surface (P), above a high-position S atom (HPS), and above a low-position S atom (LPS). After DFT geometry relaxation, the adsorption energy is computed as E_ads = E_total - E_slab - E_molecule. The most stable site (lowest E_ads) is identified. For that configuration, Mulliken population analysis yields bond populations and bond lengths for the interacting atom pairs (H-S, Fe-O). Additionally, Mulliken atomic charges are extracted before and after adsorption to quantify charge transfer. All calculations are performed with an open-source DFT code such as Quantum ESPRESSO; no precomputed structures or results are provided.

## Reproduction target
Produce the following three JSON artifacts in `/app/outputs`:

1. **adsorption_energies.json** – the adsorption energy (kJ/mol) of the most stable configuration for each coal structural unit (Ph-OH, Ph-COOH, Ph-CO-CH3, Ph-O-CH3).
2. **mulliken_analysis.json** – for the most stable configuration of each unit, an array of interaction objects containing the interaction type (H-S or Fe-O), Mulliken bond population, and bond length (Å).
3. **charge_transfer.json** – for the most stable configuration, Mulliken atomic charges before and after adsorption for the key bonding atoms (H, S, Fe, O), allowing assessment of charge transfer.

The exact schemas are defined in the Output Contract. All values must be obtained by executing the DFT workflow from scratch using the public resources listed in Assets.

## Assets

- Pyrite (FeS2) crystal structure: https://materialsproject.org/materials/mp-226
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Geometry optimization of pyrite and coal units
- Role: process
- Action: Optimize the bulk pyrite unit cell using DFT (GGA-PW91 functional), construct a pyrite (100) slab with sufficient vacuum, and optimize the isolated geometries of the four coal structural units (Ph-OH, Ph-COOH, Ph-CO-CH3, Ph-O-CH3) in large cubic cells. All calculations use the plane-wave DFT code Quantum ESPRESSO with ultra-soft pseudopotentials.
- Evidence: `/app/outputs/optimized_structures.tar.gz`

### Step 2: Adsorption energy calculation
- Role: scored (load-bearing)
- Action: For each coal unit, place the molecule at the four initial adsorption sites (Fe-top, perpendicular, high-position S, low-position S) on the pyrite (100) slab, perform DFT geometry optimization, compute adsorption energy E_ads = E_total - E_slab - E_molecule, identify the most stable configuration (lowest E_ads), and output the E_ads for the most stable configuration of each unit.
- Output file: `/app/outputs/adsorption_energies.json`
- Format: json
- Contract: {"Ph-OH": number, "Ph-COOH": number, "Ph-CO-CH3": number, "Ph-O-CH3": number}
- Scoring: scored by hidden verifier

### Step 3: Mulliken bond population and bond length analysis
- Role: scored (load-bearing)
- Action: For the most stable adsorption configuration of each coal unit, perform Mulliken population analysis and extract bond populations and bond lengths for the interacting atom pairs (H-S, Fe-O). Output the data.
- Output file: `/app/outputs/mulliken_analysis.json`
- Format: json
- Contract: {"Ph-OH/FeS2": [{"interaction": "H-S", "population": number, "length_Angstrom": number}], "Ph-COOH/FeS2": [{"interaction": "H-S", ...}, {"interaction": "Fe-O", ...}], ...}
- Scoring: scored by hidden verifier

### Step 4: Mulliken charge transfer analysis
- Role: scored
- Action: For the most stable configuration, compute Mulliken atomic charges for key bonding atoms (H, S, Fe, O) before and after adsorption; report the charge difference.
- Output file: `/app/outputs/charge_transfer.json`
- Format: json
- Contract: {"Ph-OH/FeS2": [{"atom": "H" or "S", "charge_before": number, "charge_after": number}], ...}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_energies.json`
- `/app/outputs/mulliken_analysis.json`
- `/app/outputs/charge_transfer.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_energies.json
- path: `/app/outputs/adsorption_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies (kJ/mol) of the most stable configuration for each coal structural unit.
- schema:
  - `type`: object
  - `required`: `Ph-OH`, `Ph-COOH`, `Ph-CO-CH3`, `Ph-O-CH3`
  - `properties`:
    - `Ph-OH`:
      - `type`: number
    - `Ph-COOH`:
      - `type`: number
    - `Ph-CO-CH3`:
      - `type`: number
    - `Ph-O-CH3`:
      - `type`: number

### mulliken_analysis.json
- path: `/app/outputs/mulliken_analysis.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mulliken bond populations and bond lengths for interactions between coal structural units and the pyrite (100) surface.
- schema:
  - `type`: object
  - `required`: `Ph-OH/FeS2`, `Ph-COOH/FeS2`, `Ph-CO-CH3/FeS2`, `Ph-O-CH3/FeS2`
  - `properties`:
    - `Ph-OH/FeS2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `interaction`:
            - `type`: string
          - `population`:
            - `type`: number
          - `length_Angstrom`:
            - `type`: number
    - `Ph-COOH/FeS2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `interaction`:
            - `type`: string
          - `population`:
            - `type`: number
          - `length_Angstrom`:
            - `type`: number
    - `Ph-CO-CH3/FeS2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `interaction`:
            - `type`: string
          - `population`:
            - `type`: number
          - `length_Angstrom`:
            - `type`: number
    - `Ph-O-CH3/FeS2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `interaction`:
            - `type`: string
          - `population`:
            - `type`: number
          - `length_Angstrom`:
            - `type`: number

### charge_transfer.json
- path: `/app/outputs/charge_transfer.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mulliken atomic charges for bonding atoms before and after adsorption, used to assess charge transfer.
- schema:
  - `type`: object
  - `required`: `Ph-OH/FeS2`, `Ph-COOH/FeS2`, `Ph-CO-CH3/FeS2`, `Ph-O-CH3/FeS2`
  - `properties`:
    - `Ph-OH/FeS2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `atom`:
            - `type`: string
          - `charge_before`:
            - `type`: number
          - `charge_after`:
            - `type`: number
    - `Ph-COOH/FeS2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `atom`:
            - `type`: string
          - `charge_before`:
            - `type`: number
          - `charge_after`:
            - `type`: number
    - `Ph-CO-CH3/FeS2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `atom`:
            - `type`: string
          - `charge_before`:
            - `type`: number
          - `charge_after`:
            - `type`: number
    - `Ph-O-CH3/FeS2`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `atom`:
            - `type`: string
          - `charge_before`:
            - `type`: number
          - `charge_after`:
            - `type`: number

Notes: All values are computed with DFT using GGA-PW91. Units are as indicated. The checker compares submitted values to reference values from the paper with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Ph-OH",
          "Ph-COOH",
          "Ph-CO-CH3",
          "Ph-O-CH3"
        ],
        "properties": {
          "Ph-OH": {
            "type": "number"
          },
          "Ph-COOH": {
            "type": "number"
          },
          "Ph-CO-CH3": {
            "type": "number"
          },
          "Ph-O-CH3": {
            "type": "number"
          }
        }
      },
      "description": "Adsorption energies (kJ/mol) of the most stable configuration for each coal structural unit."
    },
    {
      "file": "mulliken_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Ph-OH/FeS2",
          "Ph-COOH/FeS2",
          "Ph-CO-CH3/FeS2",
          "Ph-O-CH3/FeS2"
        ],
        "properties": {
          "Ph-OH/FeS2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "interaction": {
                  "type": "string"
                },
                "population": {
                  "type": "number"
                },
                "length_Angstrom": {
                  "type": "number"
                }
              }
            }
          },
          "Ph-COOH/FeS2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "interaction": {
                  "type": "string"
                },
                "population": {
                  "type": "number"
                },
                "length_Angstrom": {
                  "type": "number"
                }
              }
            }
          },
          "Ph-CO-CH3/FeS2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "interaction": {
                  "type": "string"
                },
                "population": {
                  "type": "number"
                },
                "length_Angstrom": {
                  "type": "number"
                }
              }
            }
          },
          "Ph-O-CH3/FeS2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "interaction": {
                  "type": "string"
                },
                "population": {
                  "type": "number"
                },
                "length_Angstrom": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Mulliken bond populations and bond lengths for interactions between coal structural units and the pyrite (100) surface."
    },
    {
      "file": "charge_transfer.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Ph-OH/FeS2",
          "Ph-COOH/FeS2",
          "Ph-CO-CH3/FeS2",
          "Ph-O-CH3/FeS2"
        ],
        "properties": {
          "Ph-OH/FeS2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "atom": {
                  "type": "string"
                },
                "charge_before": {
                  "type": "number"
                },
                "charge_after": {
                  "type": "number"
                }
              }
            }
          },
          "Ph-COOH/FeS2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "atom": {
                  "type": "string"
                },
                "charge_before": {
                  "type": "number"
                },
                "charge_after": {
                  "type": "number"
                }
              }
            }
          },
          "Ph-CO-CH3/FeS2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "atom": {
                  "type": "string"
                },
                "charge_before": {
                  "type": "number"
                },
                "charge_after": {
                  "type": "number"
                }
              }
            }
          },
          "Ph-O-CH3/FeS2": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "atom": {
                  "type": "string"
                },
                "charge_before": {
                  "type": "number"
                },
                "charge_after": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Mulliken atomic charges for bonding atoms before and after adsorption, used to assess charge transfer."
    }
  ],
  "notes": "All values are computed with DFT using GGA-PW91. Units are as indicated. The checker compares submitted values to reference values from the paper with appropriate tolerances."
}
```

## How you are scored
Each scored output artifact is independently evaluated by a hidden verifier. The verifier compares your computed adsorption energies, Mulliken populations, bond lengths, and charge transfers to reference results with appropriate tolerances, and checks that the trends (e.g., ordering of adsorption strength) are physically correct. The scores from all scored artifacts are weighted and combined to produce the final reward (a float between 0 and 1). Simply reporting literature values is not sufficient; you must genuinely execute the computational workflow and produce the required outputs. The verifier's assessment is based on the accuracy and consistency of your computed data.
