# DFT Study of Ag Modification and NO2 Adsorption on Si Nanowire

## Problem background
Surface modification by noble metal nanoparticles can enhance the gas‑sensing response of semiconductor nanowires, but the underlying theoretical mechanisms are not well understood. This task uses density functional theory (DFT) to computationally investigate the adsorption of NO₂ on Ag‑modified [100]‑oriented silicon nanowires (Ag@SiNWs). The goal is to quantify the most stable Ag‑modification structures, the adsorption energetics and geometries of NO₂ on both pristine and Ag‑modified nanowires, and the resulting charge transfers, in order to explore the nature of any Ag‑modification‑induced response enhancement.

## Approach
Build a [100]‑oriented hydrogen‑passivated SiNW model. Introduce a single Ag atom at different surface and subsurface sites to generate candidate Ag@SiNW structures. Use DFT with the GGA‑PBE functional and ultrasoft pseudopotentials to fully relax the geometries of the pristine SiNW and each Ag@SiNW, then compute modification energies, Ag–Si bond lengths, and Mulliken charge on Ag. Identify the most energetically favorable Ag configuration and construct NO₂ adsorption models on both the pristine SiNW and that Ag@SiNW, considering a range of binding sites (N‑down and O‑down orientations). Perform DFT relaxations on all adsorption complexes to obtain adsorption energies and equilibrium bond lengths, and finally carry out Mulliken population analysis on the key adsorption configurations to quantify charge transfer to the NO₂ molecule.

## Reproduction target
Produce three scored JSON files: (1) modification energies, Ag–Si bond lengths, and Mulliken charge on Ag for configurations M1–M5 (`modification_results.json`); (2) adsorption energies and equilibrium bond lengths for NO₂ on pristine SiNW (M01) and on the nine adsorption sites of the most stable Ag@SiNW (M51–M59) (`adsorption_results.json`); (3) Mulliken charge transfers for the key configurations M01, M51, and M59, including per‑atom charges (`charge_transfer_results.json`). The verifier will check the reported numbers against hidden reference data and also verify that the most stable Ag configuration (highest modification energy) and the most exothermic adsorption site (highest adsorption energy) correspond to the expected structures.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE ultrasoft pseudopotentials: https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment: https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Build pristine SiNW model
- Role: process
- Action: Construct a [100]-oriented hydrogen-passivated silicon nanowire (M0) with diameter ~1.3 nm from a 5x5x2 diamond Si supercell. Add 20 Å vacuum transverse to the wire axis. Passivate all surface dangling bonds except the sites reserved for later Ag modification with hydrogen.
- Evidence: `/app/outputs/si_nw_model.pdb`

### Step 2: Generate Ag modification configurations
- Role: process
- Action: Create five Ag@SiNW models (M1–M5) by placing a single Ag atom at the specified sites: on surface Si₁ (M1), on subsurface Si₂ (M2), on bridge between two Si₁ (M3), on mixed bridge Si₁/Si₂ (M4), and on bridge of two Si₂ (M5). Remove passivating H atoms from Si₁ sites where Ag binds.
- Evidence: `/app/outputs/ag_modified_models.xyz`

### Step 3: DFT geometry optimization of SiNW and Ag@SiNW
- Role: process
- Action: Perform full geometry relaxation using DFT (GGA-PBE, ultrasoft pseudopotentials, plane-wave cutoff 340 eV, 3×3×3 k-points, and convergence criteria) on the pristine SiNW (M0) and all five Ag@SiNW models (M1–M5). Extract total energies and relaxed coordinates.
- Evidence: `/app/outputs/relaxation.log`

### Step 4: Compute modification energies and charge transfers
- Role: scored (load-bearing)
- Action: From the total energies of the relaxed models, compute modification energies E_mod = E(SiNW) + E(Ag) - E(Ag@SiNW) for M1–M5. Extract Ag–Si bond lengths and Mulliken charge on the Ag atom. Report all in a JSON file.
- Output file: `/app/outputs/modification_results.json`
- Format: json
- Contract: {"M1": {"E_mod_eV": float, "bonds": [{"type": "Ag-Si1", "length_Ang": float}], "charge_Ag_e": float}, ... (for M1-M5)}
- Scoring: scored by hidden verifier

### Step 5: Lattice distortion analysis
- Role: process
- Action: Measure interatomic distances along [001] and [011] in relaxed M0, M1, and M5 to document the lattice distortion claimed to support the MACE etching mechanism.
- Evidence: `/app/outputs/lattice_distortion.txt`

### Step 6: Generate NO2 adsorption configurations
- Role: process
- Action: Using the relaxed M5 (Ag@SiNW) and M0 (pristine SiNW) structures, build initial adsorption models: M01 (NO2 on Si₁ of pristine SiNW) and M51–M59 (NO2 at various sites on Ag@SiNW, as shown in the paper).
- Evidence: `/app/outputs/no2_adsorption_models.xyz`

### Step 7: DFT geometry optimization of NO2 adsorption systems
- Role: process
- Action: Perform full geometry relaxations on all adsorption models M01 and M51–M59 using the same DFT settings as before. Obtain total energies and relaxed geometries.
- Evidence: `/app/outputs/adsorption_relax.log`

### Step 8: Compute adsorption energies and bond lengths
- Role: scored (load-bearing)
- Action: From the relaxed energies, compute adsorption energies E_ads = E(Ag@SiNW) + E(NO2) - E(Ag@SiNW-NO2) for M01 and M51–M59. Extract the formation bond types and lengths. Output to JSON.
- Output file: `/app/outputs/adsorption_results.json`
- Format: json
- Contract: {"M01": {"E_ads_eV": float, "bonds": [{"type": "N-Si1", "length_Ang": float}]}, "M51": {...}, ... (for M01, M51-M59)}
- Scoring: scored by hidden verifier

### Step 9: Compute Mulliken charge transfer for key adsorption configurations
- Role: scored (load-bearing)
- Action: Perform Mulliken population analysis on the relaxed electron density of M01, M51, and M59. Report total charge on the NO2 molecule and, for M51 and M59, the charge on the Ag atom and the Si₁ adsorption site. Output to JSON.
- Output file: `/app/outputs/charge_transfer_results.json`
- Format: json
- Contract: {"M01": {"NO2_charge_e": float, "delta_q_per_atom": {"N": float, "O_a": float, "O_b": float}}, "M51": {"NO2_charge_e": float, "Ag_charge_e": float, "Si1_charge_e": float, ...}, "M59": {...}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/modification_results.json`
- `/app/outputs/adsorption_results.json`
- `/app/outputs/charge_transfer_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### modification_results.json
- path: `/app/outputs/modification_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Modification energies, Ag-Si bond lengths, and Mulliken charge on Ag for the five Ag@SiNW configurations M1-M5.
- schema:
  - `type`: object
  - `required`: `M1`, `M2`, `M3`, `M4`, `M5`
  - `properties`:
    - `M1`:
      - `type`: object
      - `properties`:
        - `E_mod_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
        - `charge_Ag_e`:
          - `type`: number
    - `M2`:
      - `type`: object
      - `properties`:
        - `E_mod_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
        - `charge_Ag_e`:
          - `type`: number
    - `M3`:
      - `type`: object
      - `properties`:
        - `E_mod_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
        - `charge_Ag_e`:
          - `type`: number
    - `M4`:
      - `type`: object
      - `properties`:
        - `E_mod_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
        - `charge_Ag_e`:
          - `type`: number
    - `M5`:
      - `type`: object
      - `properties`:
        - `E_mod_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
        - `charge_Ag_e`:
          - `type`: number

### adsorption_results.json
- path: `/app/outputs/adsorption_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies E_ads and equilibrium bond lengths for NO2 on pristine SiNW (M01) and on the most stable Ag@SiNW (M51-M59).
- schema:
  - `type`: object
  - `required`: `M01`, `M51`, `M52`, `M53`, `M54`, `M55`, `M56`, `M57`, `M58`, `M59`
  - `properties`:
    - `M01`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M51`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M52`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M53`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M54`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M55`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M56`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M57`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M58`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number
    - `M59`:
      - `type`: object
      - `properties`:
        - `E_ads_eV`:
          - `type`: number
        - `bonds`:
          - `type`: array
          - `items`:
            - `type`: object
            - `properties`:
              - `type`:
                - `type`: string
              - `length_Ang`:
                - `type`: number

### charge_transfer_results.json
- path: `/app/outputs/charge_transfer_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Mulliken charge transfers for the key NO2 adsorption configurations M01, M51, M59.
- schema:
  - `type`: object
  - `required`: `M01`, `M51`, `M59`
  - `properties`:
    - `M01`:
      - `type`: object
      - `properties`:
        - `NO2_charge_e`:
          - `type`: number
        - `delta_q_per_atom`:
          - `type`: object
          - `properties`:
            - `N`:
              - `type`: number
            - `O_a`:
              - `type`: number
            - `O_b`:
              - `type`: number
    - `M51`:
      - `type`: object
      - `properties`:
        - `NO2_charge_e`:
          - `type`: number
        - `Ag_charge_e`:
          - `type`: number
        - `Si1_charge_e`:
          - `type`: number
    - `M59`:
      - `type`: object
      - `properties`:
        - `NO2_charge_e`:
          - `type`: number
        - `Ag_charge_e`:
          - `type`: number
        - `Si1_charge_e`:
          - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "modification_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "M1",
          "M2",
          "M3",
          "M4",
          "M5"
        ],
        "properties": {
          "M1": {
            "type": "object",
            "properties": {
              "E_mod_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              },
              "charge_Ag_e": {
                "type": "number"
              }
            }
          },
          "M2": {
            "type": "object",
            "properties": {
              "E_mod_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              },
              "charge_Ag_e": {
                "type": "number"
              }
            }
          },
          "M3": {
            "type": "object",
            "properties": {
              "E_mod_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              },
              "charge_Ag_e": {
                "type": "number"
              }
            }
          },
          "M4": {
            "type": "object",
            "properties": {
              "E_mod_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              },
              "charge_Ag_e": {
                "type": "number"
              }
            }
          },
          "M5": {
            "type": "object",
            "properties": {
              "E_mod_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              },
              "charge_Ag_e": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Modification energies, Ag-Si bond lengths, and Mulliken charge on Ag for the five Ag@SiNW configurations M1-M5."
    },
    {
      "file": "adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "M01",
          "M51",
          "M52",
          "M53",
          "M54",
          "M55",
          "M56",
          "M57",
          "M58",
          "M59"
        ],
        "properties": {
          "M01": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M51": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M52": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M53": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M54": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M55": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M56": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M57": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M58": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "M59": {
            "type": "object",
            "properties": {
              "E_ads_eV": {
                "type": "number"
              },
              "bonds": {
                "type": "array",
                "items": {
                  "type": "object",
                  "properties": {
                    "type": {
                      "type": "string"
                    },
                    "length_Ang": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "Adsorption energies E_ads and equilibrium bond lengths for NO2 on pristine SiNW (M01) and on the most stable Ag@SiNW (M51-M59)."
    },
    {
      "file": "charge_transfer_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "M01",
          "M51",
          "M59"
        ],
        "properties": {
          "M01": {
            "type": "object",
            "properties": {
              "NO2_charge_e": {
                "type": "number"
              },
              "delta_q_per_atom": {
                "type": "object",
                "properties": {
                  "N": {
                    "type": "number"
                  },
                  "O_a": {
                    "type": "number"
                  },
                  "O_b": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "M51": {
            "type": "object",
            "properties": {
              "NO2_charge_e": {
                "type": "number"
              },
              "Ag_charge_e": {
                "type": "number"
              },
              "Si1_charge_e": {
                "type": "number"
              }
            }
          },
          "M59": {
            "type": "object",
            "properties": {
              "NO2_charge_e": {
                "type": "number"
              },
              "Ag_charge_e": {
                "type": "number"
              },
              "Si1_charge_e": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Mulliken charge transfers for the key NO2 adsorption configurations M01, M51, M59."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently inspects each scored artifact. The final reward is a weighted sum of the scores from the three JSON files. The verifier compares your reported modification energies, bond lengths, and charge transfers to hidden gold values with tolerances that account for legitimate differences from the open‑source DFT toolchain and pseudopotentials. It also confirms that the required structural trends (which configuration is most stable, which adsorption site is most exothermic) are reproduced. Providing numbers without running the full DFT workflow will not satisfy the checks.
