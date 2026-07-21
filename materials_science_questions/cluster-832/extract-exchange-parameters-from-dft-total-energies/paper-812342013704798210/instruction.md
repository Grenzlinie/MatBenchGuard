# Reproduction task

## Problem background
The intermetallic compound MnPt₃ in the ordered L1₂ structure exhibits a large magneto‑optical Kerr effect, making it a candidate for magneto‑optical recording devices. The microscopic origin of the Kerr effect is tied to the magnetic ordering, because antiferromagnetic materials do not produce a Kerr signal. Resolving the magnetic ground state of bulk MnPt₃ and its (100) and (111) surfaces, and quantifying the exchange interactions and the surface‑induced changes in magnetic moments and charge transfers, is therefore essential to understand the material's functionality. This task uses ab initio electronic‑structure calculations to determine these properties.

## Approach
The computations are carried out with spin‑polarized density functional theory (DFT) using the local density approximation (LDA) and an open‑source plane‑wave pseudopotential code (Quantum ESPRESSO).

For the bulk, four magnetic configurations are considered: a full ferromagnetic (FM) order and three antiferromagnetic orderings where ferromagnetic atomic planes are stacked antiferromagnetically — AFM₁ with ferromagnetic (100) planes, AFM₂ with ferromagnetic (110) planes, and AFM₃ with ferromagnetic (111) planes. The total energies of these configurations are mapped onto an Ising model that includes nearest‑ (J₁), next‑nearest‑ (J₂), and next‑next‑nearest‑neighbor (J₃) exchange constants. Solving the linear relations between the four total energies yields the exchange parameters.

For the surfaces, periodic slab supercells with vacuum are constructed: the (100) surface is modeled with Mn‑Pt termination, and the (111) surface is modeled as a stoichiometric slab. Both ferromagnetic and antiferromagnetic arrangements of the manganese moments are relaxed. From the self‑consistent charge densities, layer‑resolved spin magnetic moments (in μ_B) are obtained and charge transfers (in electrons per atom) are computed via Bader charge analysis. The charge transfers are nearly identical for both magnetic orderings and are evaluated only for the ferromagnetic configurations.

## Reproduction target
Produce two JSON files under `/app/outputs`:

- **bulk_exchange_constants.json**: contains the extracted exchange coupling constants J₁, J₂, J₃ (in mRy) and a unit field `"units": "mRy"`.

- **surface_moments_and_charges.json**: contains the layer‑resolved spin magnetic moments (in μ_B) and charge transfers (in electrons/atom) for both magnetic orderings on the (100) and (111) surfaces. For the (100) surface layers 1 through 5 are reported; for the (111) surface layers 1 through 3 are reported. Moments are given for both the FM and AFM orderings; charge transfers are reported only for the ferromagnetic configurations.

The exact schemas are specified in the Output contract section below.

## Assets
- **Quantum ESPRESSO** – open‑source plane‑wave pseudopotential DFT code. [https://www.quantum-espresso.org/](https://www.quantum-espresso.org/)
- **Bader charge analysis code** – tool for partitioning the charge density to obtain atomic charges. [http://theory.cm.utexas.edu/henkelman/code/bader/](http://theory.cm.utexas.edu/henkelman/code/bader/)
- **MnPt₃ crystal structure** – ordered L1₂ structure (space group Pm-3m) with Mn at (0,0,0) and Pt at (0.5,0.5,0) and its cyclic permutations; lattice constant approximately 3.91 Å. No separate download is required; the structure can be constructed from standard crystallographic data.
- **Pseudopotential files** – standard LDA pseudopotentials for Mn and Pt (e.g., from PSLibrary or SSSP). [https://www.quantum-espresso.org/pseudopotentials/](https://www.quantum-espresso.org/pseudopotentials/)

## Workflow steps

### Step 1: Bulk relaxation
- Role: process
- Action: Perform variable-cell relaxation of ferromagnetic bulk MnPt3 using DFT with LDA to obtain equilibrium lattice constant. Use a conventional 4-atom cubic cell. Fit energy vs volume to a Birch–Murnaghan equation to extract the lattice constant.
- Evidence: `/app/outputs/relax.out`
- This step determines the equilibrium lattice constant for the ferromagnetic ground state, which is used for all subsequent calculations. The relaxation result is not directly scored but is essential for consistent supercells.

### Step 2: Bulk magnetic configuration energies
- Role: process
- Action: Construct 16-atom supercells for the four magnetic configurations FM, AFM₁, AFM₂, AFM₃ at the relaxed lattice constant. Run spin-polarized DFT total energy calculations with LDA and a sufficiently dense k-mesh. Record the total energies.
- Evidence: `/app/outputs/bulk_energies.csv`
- The magnetic ordering patterns are: AFM₁ ferromagnetic within (100) planes, AFM₂ within (110) planes, AFM₃ within (111) planes. This step provides the energies needed for the Ising model mapping.

### Step 3: Extract exchange constants
- Role: scored (load-bearing)
- Action: Map the total energies from Step 2 onto the Ising Hamiltonian using the Ising Hamiltonian described in the approach section to extract nearest‑neighbor (J₁), next‑nearest‑neighbor (J₂), and next‑next‑nearest‑neighbor (J₃) exchange coupling constants. Write the result to bulk_exchange_constants.json.
- Output file: `/app/outputs/bulk_exchange_constants.json`
- Format: json
- Contract: `{"J1": <float>, "J2": <float>, "J3": <float>, "units": "mRy"}`
- Scoring: scored by hidden verifier (values compared to reference Ising map decomposition)

### Step 4: Surface slab calculations
- Role: process
- Action: Build slab supercells for (100) MnPt‑terminated surface (9–13 atomic layers plus vacuum) and (111) stoichiometric surface (6–10 atomic layers plus vacuum) at the bulk relaxed lattice constant. Run spin-polarized DFT total energy calculations for both FM and AFM magnetic orderings of each surface. From the self-consistent charge densities, compute layer‑projected spin magnetic moments (in μ_B) using integrated spin density within atomic spheres, and atomic charges using Bader analysis or equivalent local integration.
- Evidence: `/app/outputs/surface_raw.out`
- This step computes the layer‑resolved moments and charges needed for Step 5.

### Step 5: Report surface properties
- Role: scored (load-bearing)
- Action: Compile the layer‑resolved spin magnetic moments (in μ_B) and charge transfers (in e/atom) for the (100) and (111) surfaces in both magnetic orderings. Charge transfers are evaluated for the FM surfaces only (they are nearly identical for AFM). Output the values to surface_moments_and_charges.json following the specified schema.
- Output file: `/app/outputs/surface_moments_and_charges.json`
- Format: json
- Contract: (see Output contract section for full schema)
- Scoring: scored by hidden verifier (layer‑by‑layer comparison to reference moments and charges)

## Output files
Write all artifacts under `/app/outputs`:

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_exchange_constants.json
- path: `/app/outputs/bulk_exchange_constants.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Exchange coupling constants J1, J2, J3 in mRy.
- schema:
  - `type`: object
  - `properties`:
    - `J1`:
      - `type`: number
    - `J2`:
      - `type`: number
    - `J3`:
      - `type`: number
    - `units`:
      - `const`: mRy
  - `required`: `J1`, `J2`, `J3`, `units`
  - `additionalProperties`: False

### surface_moments_and_charges.json
- path: `/app/outputs/surface_moments_and_charges.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Layer-resolved spin magnetic moments and charge transfers for (100) and (111) surfaces.
- schema:
  - `type`: object
  - `properties`:
    - `FM(100)`:
      - `type`: object
      - `properties`:
        - `Layer1`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
        - `Layer2`:
          - `type`: object
          - `properties`:
            - `Pt_moment`:
              - `type`: number
          - `required`: `Pt_moment`
        - `Layer3`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
        - `Layer4`:
          - `type`: object
          - `properties`:
            - `Pt_moment`:
              - `type`: number
          - `required`: `Pt_moment`
        - `Layer5`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
      - `required`: `Layer1`, `Layer2`, `Layer3`, `Layer4`, `Layer5`
    - `AFM(100)`:
      - `type`: object
      - `properties`:
        - `Layer1`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
        - `Layer2`:
          - `type`: object
          - `properties`:
            - `Pt_moment`:
              - `type`: number
          - `required`: `Pt_moment`
        - `Layer3`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
        - `Layer4`:
          - `type`: object
          - `properties`:
            - `Pt_moment`:
              - `type`: number
          - `required`: `Pt_moment`
        - `Layer5`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
      - `required`: `Layer1`, `Layer2`, `Layer3`, `Layer4`, `Layer5`
    - `FM(111)`:
      - `type`: object
      - `properties`:
        - `Layer1`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
        - `Layer2`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
        - `Layer3`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
      - `required`: `Layer1`, `Layer2`, `Layer3`
    - `AFM(111)`:
      - `type`: object
      - `properties`:
        - `Layer1`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
        - `Layer2`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
        - `Layer3`:
          - `type`: object
          - `properties`:
            - `Mn_moment`:
              - `type`: number
            - `Pt_moment`:
              - `type`: number
          - `required`: `Mn_moment`, `Pt_moment`
      - `required`: `Layer1`, `Layer2`, `Layer3`
    - `charge_transfer_FM(100)`:
      - `type`: object
      - `properties`:
        - `Layer1`:
          - `type`: object
          - `properties`:
            - `Mn_charge`:
              - `type`: number
            - `Pt_charge`:
              - `type`: number
          - `required`: `Mn_charge`, `Pt_charge`
        - `Layer2`:
          - `type`: object
          - `properties`:
            - `Pt_charge`:
              - `type`: number
          - `required`: `Pt_charge`
        - `Layer3`:
          - `type`: object
          - `properties`:
            - `Mn_charge`:
              - `type`: number
            - `Pt_charge`:
              - `type`: number
          - `required`: `Mn_charge`, `Pt_charge`
        - `Layer4`:
          - `type`: object
          - `properties`:
            - `Pt_charge`:
              - `type`: number
          - `required`: `Pt_charge`
        - `Layer5`:
          - `type`: object
          - `properties`:
            - `Mn_charge`:
              - `type`: number
            - `Pt_charge`:
              - `type`: number
          - `required`: `Mn_charge`, `Pt_charge`
      - `required`: `Layer1`, `Layer2`, `Layer3`, `Layer4`, `Layer5`
    - `charge_transfer_FM(111)`:
      - `type`: object
      - `properties`:
        - `Layer1`:
          - `type`: object
          - `properties`:
            - `Mn_charge`:
              - `type`: number
            - `Pt_charge`:
              - `type`: number
          - `required`: `Mn_charge`, `Pt_charge`
        - `Layer2`:
          - `type`: object
          - `properties`:
            - `Mn_charge`:
              - `type`: number
            - `Pt_charge`:
              - `type`: number
          - `required`: `Mn_charge`, `Pt_charge`
        - `Layer3`:
          - `type`: object
          - `properties`:
            - `Mn_charge`:
              - `type`: number
            - `Pt_charge`:
              - `type`: number
          - `required`: `Mn_charge`, `Pt_charge`
      - `required`: `Layer1`, `Layer2`, `Layer3`
  - `required`: `FM(100)`, `AFM(100)`, `FM(111)`, `AFM(111)`, `charge_transfer_FM(100)`, `charge_transfer_FM(111)`
  - `additionalProperties`: False

Notes: The exchange constants are derived from an Ising model mapping of DFT total energies; the surface moments and charges from DFT slab calculations with Bader analysis.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_exchange_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "J1": {
            "type": "number"
          },
          "J2": {
            "type": "number"
          },
          "J3": {
            "type": "number"
          },
          "units": {
            "const": "mRy"
          }
        },
        "required": [
          "J1",
          "J2",
          "J3",
          "units"
        ],
        "additionalProperties": false
      },
      "description": "Exchange coupling constants J1, J2, J3 in mRy."
    },
    {
      "file": "surface_moments_and_charges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "properties": {
          "FM(100)": {
            "type": "object",
            "properties": {
              "Layer1": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              },
              "Layer2": {
                "type": "object",
                "properties": {
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Pt_moment"
                ]
              },
              "Layer3": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              },
              "Layer4": {
                "type": "object",
                "properties": {
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Pt_moment"
                ]
              },
              "Layer5": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              }
            },
            "required": [
              "Layer1",
              "Layer2",
              "Layer3",
              "Layer4",
              "Layer5"
            ]
          },
          "AFM(100)": {
            "type": "object",
            "properties": {
              "Layer1": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              },
              "Layer2": {
                "type": "object",
                "properties": {
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Pt_moment"
                ]
              },
              "Layer3": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              },
              "Layer4": {
                "type": "object",
                "properties": {
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Pt_moment"
                ]
              },
              "Layer5": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              }
            },
            "required": [
              "Layer1",
              "Layer2",
              "Layer3",
              "Layer4",
              "Layer5"
            ]
          },
          "FM(111)": {
            "type": "object",
            "properties": {
              "Layer1": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              },
              "Layer2": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              },
              "Layer3": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              }
            },
            "required": [
              "Layer1",
              "Layer2",
              "Layer3"
            ]
          },
          "AFM(111)": {
            "type": "object",
            "properties": {
              "Layer1": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              },
              "Layer2": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              },
              "Layer3": {
                "type": "object",
                "properties": {
                  "Mn_moment": {
                    "type": "number"
                  },
                  "Pt_moment": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_moment",
                  "Pt_moment"
                ]
              }
            },
            "required": [
              "Layer1",
              "Layer2",
              "Layer3"
            ]
          },
          "charge_transfer_FM(100)": {
            "type": "object",
            "properties": {
              "Layer1": {
                "type": "object",
                "properties": {
                  "Mn_charge": {
                    "type": "number"
                  },
                  "Pt_charge": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_charge",
                  "Pt_charge"
                ]
              },
              "Layer2": {
                "type": "object",
                "properties": {
                  "Pt_charge": {
                    "type": "number"
                  }
                },
                "required": [
                  "Pt_charge"
                ]
              },
              "Layer3": {
                "type": "object",
                "properties": {
                  "Mn_charge": {
                    "type": "number"
                  },
                  "Pt_charge": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_charge",
                  "Pt_charge"
                ]
              },
              "Layer4": {
                "type": "object",
                "properties": {
                  "Pt_charge": {
                    "type": "number"
                  }
                },
                "required": [
                  "Pt_charge"
                ]
              },
              "Layer5": {
                "type": "object",
                "properties": {
                  "Mn_charge": {
                    "type": "number"
                  },
                  "Pt_charge": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_charge",
                  "Pt_charge"
                ]
              }
            },
            "required": [
              "Layer1",
              "Layer2",
              "Layer3",
              "Layer4",
              "Layer5"
            ]
          },
          "charge_transfer_FM(111)": {
            "type": "object",
            "properties": {
              "Layer1": {
                "type": "object",
                "properties": {
                  "Mn_charge": {
                    "type": "number"
                  },
                  "Pt_charge": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_charge",
                  "Pt_charge"
                ]
              },
              "Layer2": {
                "type": "object",
                "properties": {
                  "Mn_charge": {
                    "type": "number"
                  },
                  "Pt_charge": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_charge",
                  "Pt_charge"
                ]
              },
              "Layer3": {
                "type": "object",
                "properties": {
                  "Mn_charge": {
                    "type": "number"
                  },
                  "Pt_charge": {
                    "type": "number"
                  }
                },
                "required": [
                  "Mn_charge",
                  "Pt_charge"
                ]
              }
            },
            "required": [
              "Layer1",
              "Layer2",
              "Layer3"
            ]
          }
        },
        "required": [
          "FM(100)",
          "AFM(100)",
          "FM(111)",
          "AFM(111)",
          "charge_transfer_FM(100)",
          "charge_transfer_FM(111)"
        ],
        "additionalProperties": false
      },
      "description": "Layer-resolved spin magnetic moments and charge transfers for (100) and (111) surfaces."
    }
  ],
  "notes": "The exchange constants are derived from an Ising model mapping of DFT total energies; the surface moments and charges from DFT slab calculations with Bader analysis."
}
```

## How you are scored
After your workflow finishes, a hidden checker reads the files you wrote to `/app/outputs`. For each scored artifact the checker compares your reported values to expected reference quantities:

- The bulk exchange constants J₁, J₂, J₃ are compared to the values that correctly describe the magnetic orderings within the Ising model; both magnitude and sign are checked.
- The surface magnetic moments and charge transfers are compared layer‑by‑layer against the physical trends and expected absolute values within reasonable tolerance.

Your final reward is a weighted sum across the two artifacts. The exchange constants and the surface magnetic moments carry the largest weights, while the charge transfers contribute a smaller share. Reporting numbers without performing the required computations will not meet the expected accuracy, so the reward will be low.
