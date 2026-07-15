# First-Principles Calculation of Electronic Structure and Magnetic Properties of Mn-Doped Perovskite Crystals

## Problem background
Hybrid perovskite solar cells achieve high conversion efficiencies, and their photovoltaic performance can be further tuned by incorporating transition metals. This work investigates how manganese (Mn) doping into formamidinium lead triiodide (FAPbI3) modifies the electronic structure, optical absorption, and nuclear magnetic resonance (NMR) chemical shifts. Understanding the effect of a dilute Mn substitution on the band gap, absorption spectrum, and magnetic properties is important for designing broad-band photovoltaic materials.

## Approach
The approach uses first-principles density functional theory (DFT) calculations. A 2×2×2 supercell of cubic FAPbI3 is constructed, and one central Pb atom is replaced by Mn to model a dilute doping. Two systems are studied: pristine FAPbI3 (singlet, charge +8) and Mn-doped FAPbI3 (sextet spin state with S=5/2, charge +8). All calculations are performed with the B3LYP hybrid functional and the LANL2DZ effective core potential basis set, which provides an effective treatment of the heavy Pb, I, and Mn atoms. The workflow computes: (i) ground-state electronic structure and HOMO-LUMO gap, (ii) optical absorption spectra via time-dependent DFT, (iii) isotropic NMR chemical shieldings for 127I, 207Pb, 13C, and 14N using gauge-including atomic orbitals (GIAO), and (iv) the Mn g-tensor, electric field gradient tensor, and asymmetry parameter. The results for the doped and pristine systems are compared to reveal the effects of Mn incorporation.

## Reproduction target
Reproduce the four main computational results as JSON artifacts:
1. The HOMO-LUMO energy gap (in eV) for both the pristine and Mn-doped FAPbI3 supercells.
2. The first five excited-state wavelengths (nm) and oscillator strengths from TD-DFT for both systems.
3. Isotropic NMR shieldings (in ppm) for all 127I, 207Pb, 13C, and 14N nuclei in the pristine and doped supercells; for the doped case, each atom must be labeled with whether it is coordinated to Mn.
4. The principal components of the g-tensor (g_xx, g_yy, g_zz), the electric field gradient tensor (V_xx, V_yy, V_zz in atomic units), and the asymmetry parameter η for Mn in the doped system.
The goal is to compute these quantities from the defined supercells and DFT protocol; the hidden verifier will then assess the correctness of the results.

## Assets

- ORCA quantum chemistry package: https://www.orcasoftware.de/tutorials_orca/install.html
- FAPbI3 cubic crystal structure: 10.1016/j.jpcs.2015.06.001
- LANL2DZ effective core potential basis set: ORCA built-in or Basis Set Exchange

## Workflow steps

### Step 1: Build supercell structures
- Role: process
- Action: Construct two 2×2×2 cubic supercells of FAPbI3: one pristine (charge +8, singlet) and one Mn-doped (replace one central Pb with Mn, charge +8, spin multiplicity 6). Use the literature lattice constant a=6.36 Å and published atomic positions. Save structures as ORCA input files.
- Evidence: `/app/outputs/doped.xyz, pristine.xyz`

### Step 2: DFT ground‑state electronic structure
- Role: scored (load-bearing)
- Action: Run a single-point DFT calculation on both supercells using ORCA with B3LYP functional and LANL2DZ basis set. Extract HOMO and LUMO energies (eV) and compute the HOMO-LUMO gap. Write the results to band_gap.json.
- Output file: `/app/outputs/band_gap.json`
- Format: json
- Contract: {
  "doped": {"homo_eV": float, "lumo_eV": float, "gap_eV": float},
  "pristine": {"homo_eV": float, "lumo_eV": float, "gap_eV": float}
}
- Scoring: scored by hidden verifier

### Step 3: TD‑DFT optical absorption
- Role: scored (load-bearing)
- Action: Using the converged wavefunction from step 02, perform a TD-DFT calculation on both systems with the same functional and basis set. Compute the first five excited states: excitation energy (eV), wavelength (nm), and oscillator strength. Write the results to optical_absorption.json.
- Output file: `/app/outputs/optical_absorption.json`
- Format: json
- Contract: {
  "doped": [{"state": int, "wavelength_nm": float, "oscillator_strength": float}],
  "pristine": [{"state": int, "wavelength_nm": float, "oscillator_strength": float}]
}
- Scoring: scored by hidden verifier

### Step 4: NMR chemical shifts
- Role: scored (load-bearing)
- Action: Perform a GIAO NMR calculation on both systems using the ground‑state wavefunction, B3LYP, and LANL2DZ basis. Compute isotropic shieldings (in ppm) for all 127I, 207Pb, 13C, and 14N atoms, labeling each atom with its species and a flag indicating whether it is coordinated to Mn (for the doped case). Write the results to nmr_chemical_shifts.json.
- Output file: `/app/outputs/nmr_chemical_shifts.json`
- Format: json
- Contract: {
  "doped": {
    "127I": [{"label": str, "coordinated_to_Mn": bool, "isotropic_shielding_ppm": float}],
    "207Pb": [{"label": str, "coordinated_to_Mn": bool, "isotropic_shielding_ppm": float}],
    "13C": [{"label": str, "coordinated_to_Mn": bool, "isotropic_shielding_ppm": float}],
    "14N": [{"label": str, "coordinated_to_Mn": bool, "isotropic_shielding_ppm": float}]
  },
  "pristine": {
    "127I": [{"label": str, "isotropic_shielding_ppm": float}],
    "207Pb": [{"label": str, "isotropic_shielding_ppm": float}],
    "13C": [{"label": str, "isotropic_shielding_ppm": float}],
    "14N": [{"label": str, "isotropic_shielding_ppm": float}]
  }
}
- Scoring: scored by hidden verifier

### Step 5: Mn g‑tensor and EFG tensor
- Role: scored (load-bearing)
- Action: Using the same ground‑state calculation, compute the g‑tensor components (g_xx, g_yy, g_zz), the electric field gradient principal components (V_xx, V_yy, V_zz in atomic units), and the asymmetry parameter η = (V_xx - V_yy)/V_zz for the Mn atom in the doped system. Write the results to mn_gv_tensor.json.
- Output file: `/app/outputs/mn_gv_tensor.json`
- Format: json
- Contract: {
  "g_xx": float, "g_yy": float, "g_zz": float,
  "V_xx": float, "V_yy": float, "V_zz": float,
  "eta": float
}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/band_gap.json`
- `/app/outputs/optical_absorption.json`
- `/app/outputs/nmr_chemical_shifts.json`
- `/app/outputs/mn_gv_tensor.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### band_gap.json
- path: `/app/outputs/band_gap.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: HOMO-LUMO gap for pristine and Mn-doped FAPbI3; the checker verifies that the doped gap is narrower than the pristine gap by at least 0.2 eV.
- schema:
  - `type`: object
  - `required`: `doped`, `pristine`
  - `properties`:
    - `doped`:
      - `type`: object
      - `required`: `homo_eV`, `lumo_eV`, `gap_eV`
      - `properties`:
        - `homo_eV`:
          - `type`: number
        - `lumo_eV`:
          - `type`: number
        - `gap_eV`:
          - `type`: number
    - `pristine`:
      - `type`: object
      - `required`: `homo_eV`, `lumo_eV`, `gap_eV`
      - `properties`:
        - `homo_eV`:
          - `type`: number
        - `lumo_eV`:
          - `type`: number
        - `gap_eV`:
          - `type`: number

### optical_absorption.json
- path: `/app/outputs/optical_absorption.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: First five excited-state wavelengths and oscillator strengths for both systems; checker verifies that the doped first excitation is in the near-infrared (λ > 1000 nm) and the pristine first excitation lies in the visible range (450–600 nm).
- schema:
  - `type`: object
  - `required`: `doped`, `pristine`
  - `properties`:
    - `doped`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `state`, `wavelength_nm`, `oscillator_strength`
        - `properties`:
          - `state`:
            - `type`: integer
          - `wavelength_nm`:
            - `type`: number
          - `oscillator_strength`:
            - `type`: number
      - `minItems`: 5
    - `pristine`:
      - `type`: array
      - `items`:
        - `type`: object
        - `required`: `state`, `wavelength_nm`, `oscillator_strength`
        - `properties`:
          - `state`:
            - `type`: integer
          - `wavelength_nm`:
            - `type`: number
          - `oscillator_strength`:
            - `type`: number
      - `minItems`: 5

### nmr_chemical_shifts.json
- path: `/app/outputs/nmr_chemical_shifts.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Isotropic NMR shieldings for all 127I, 207Pb, 13C, and 14N atoms. Checker verifies qualitative trends: for doped case, 127I shieldings show at least three distinct values, the directly coordinated I differs significantly; 14N near Mn is split; average 13C shieldings show a high‑field shift relative to pristine; 207Pb shieldings remain essentially unchanged.
- schema:
  - `type`: object
  - `required`: `doped`, `pristine`
  - `properties`:
    - `doped`:
      - `type`: object
      - `required`: `127I`, `207Pb`, `13C`, `14N`
      - `properties`:
        - `127I`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `label`, `coordinated_to_Mn`, `isotropic_shielding_ppm`
            - `properties`:
              - `label`:
                - `type`: string
              - `coordinated_to_Mn`:
                - `type`: boolean
              - `isotropic_shielding_ppm`:
                - `type`: number
        - `207Pb`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `label`, `coordinated_to_Mn`, `isotropic_shielding_ppm`
            - `properties`:
              - `label`:
                - `type`: string
              - `coordinated_to_Mn`:
                - `type`: boolean
              - `isotropic_shielding_ppm`:
                - `type`: number
        - `13C`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `label`, `coordinated_to_Mn`, `isotropic_shielding_ppm`
            - `properties`:
              - `label`:
                - `type`: string
              - `coordinated_to_Mn`:
                - `type`: boolean
              - `isotropic_shielding_ppm`:
                - `type`: number
        - `14N`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `label`, `coordinated_to_Mn`, `isotropic_shielding_ppm`
            - `properties`:
              - `label`:
                - `type`: string
              - `coordinated_to_Mn`:
                - `type`: boolean
              - `isotropic_shielding_ppm`:
                - `type`: number
    - `pristine`:
      - `type`: object
      - `required`: `127I`, `207Pb`, `13C`, `14N`
      - `properties`:
        - `127I`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `label`, `isotropic_shielding_ppm`
            - `properties`:
              - `label`:
                - `type`: string
              - `isotropic_shielding_ppm`:
                - `type`: number
        - `207Pb`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `label`, `isotropic_shielding_ppm`
            - `properties`:
              - `label`:
                - `type`: string
              - `isotropic_shielding_ppm`:
                - `type`: number
        - `13C`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `label`, `isotropic_shielding_ppm`
            - `properties`:
              - `label`:
                - `type`: string
              - `isotropic_shielding_ppm`:
                - `type`: number
        - `14N`:
          - `type`: array
          - `items`:
            - `type`: object
            - `required`: `label`, `isotropic_shielding_ppm`
            - `properties`:
              - `label`:
                - `type`: string
              - `isotropic_shielding_ppm`:
                - `type`: number

### mn_gv_tensor.json
- path: `/app/outputs/mn_gv_tensor.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Principal g‑tensor components, EFG principal components, and asymmetry parameter η for Mn in the doped system. Checker verifies that g_xx, g_yy, g_zz are all distinct (anisotropic), V_zz > V_yy > V_xx, and η is between 0.2 and 0.4.
- schema:
  - `type`: object
  - `required`: `g_xx`, `g_yy`, `g_zz`, `V_xx`, `V_yy`, `V_zz`, `eta`
  - `properties`:
    - `g_xx`:
      - `type`: number
    - `g_yy`:
      - `type`: number
    - `g_zz`:
      - `type`: number
    - `V_xx`:
      - `type`: number
    - `V_yy`:
      - `type`: number
    - `V_zz`:
      - `type`: number
    - `eta`:
      - `type`: number

Notes: The agent must construct the supercells, perform the DFT/TD‑DFT/GIAO calculations with ORCA and the LANL2DZ basis, and produce the four JSON artifacts. Checker verifies structural trends and toleranced thresholds; exact numeric match to the published paper is not required. OSC and NMR shieldings are to be reported in the same units as the original work (eV, nm, dimensionless oscillator strength, ppm).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "band_gap.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "doped",
          "pristine"
        ],
        "properties": {
          "doped": {
            "type": "object",
            "required": [
              "homo_eV",
              "lumo_eV",
              "gap_eV"
            ],
            "properties": {
              "homo_eV": {
                "type": "number"
              },
              "lumo_eV": {
                "type": "number"
              },
              "gap_eV": {
                "type": "number"
              }
            }
          },
          "pristine": {
            "type": "object",
            "required": [
              "homo_eV",
              "lumo_eV",
              "gap_eV"
            ],
            "properties": {
              "homo_eV": {
                "type": "number"
              },
              "lumo_eV": {
                "type": "number"
              },
              "gap_eV": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "HOMO-LUMO gap for pristine and Mn-doped FAPbI3; the checker verifies that the doped gap is narrower than the pristine gap by at least 0.2 eV."
    },
    {
      "file": "optical_absorption.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "doped",
          "pristine"
        ],
        "properties": {
          "doped": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "state",
                "wavelength_nm",
                "oscillator_strength"
              ],
              "properties": {
                "state": {
                  "type": "integer"
                },
                "wavelength_nm": {
                  "type": "number"
                },
                "oscillator_strength": {
                  "type": "number"
                }
              }
            },
            "minItems": 5
          },
          "pristine": {
            "type": "array",
            "items": {
              "type": "object",
              "required": [
                "state",
                "wavelength_nm",
                "oscillator_strength"
              ],
              "properties": {
                "state": {
                  "type": "integer"
                },
                "wavelength_nm": {
                  "type": "number"
                },
                "oscillator_strength": {
                  "type": "number"
                }
              }
            },
            "minItems": 5
          }
        }
      },
      "description": "First five excited-state wavelengths and oscillator strengths for both systems; checker verifies that the doped first excitation is in the near-infrared (λ > 1000 nm) and the pristine first excitation lies in the visible range (450–600 nm)."
    },
    {
      "file": "nmr_chemical_shifts.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "doped",
          "pristine"
        ],
        "properties": {
          "doped": {
            "type": "object",
            "required": [
              "127I",
              "207Pb",
              "13C",
              "14N"
            ],
            "properties": {
              "127I": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "label",
                    "coordinated_to_Mn",
                    "isotropic_shielding_ppm"
                  ],
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "coordinated_to_Mn": {
                      "type": "boolean"
                    },
                    "isotropic_shielding_ppm": {
                      "type": "number"
                    }
                  }
                }
              },
              "207Pb": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "label",
                    "coordinated_to_Mn",
                    "isotropic_shielding_ppm"
                  ],
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "coordinated_to_Mn": {
                      "type": "boolean"
                    },
                    "isotropic_shielding_ppm": {
                      "type": "number"
                    }
                  }
                }
              },
              "13C": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "label",
                    "coordinated_to_Mn",
                    "isotropic_shielding_ppm"
                  ],
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "coordinated_to_Mn": {
                      "type": "boolean"
                    },
                    "isotropic_shielding_ppm": {
                      "type": "number"
                    }
                  }
                }
              },
              "14N": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "label",
                    "coordinated_to_Mn",
                    "isotropic_shielding_ppm"
                  ],
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "coordinated_to_Mn": {
                      "type": "boolean"
                    },
                    "isotropic_shielding_ppm": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "pristine": {
            "type": "object",
            "required": [
              "127I",
              "207Pb",
              "13C",
              "14N"
            ],
            "properties": {
              "127I": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "label",
                    "isotropic_shielding_ppm"
                  ],
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "isotropic_shielding_ppm": {
                      "type": "number"
                    }
                  }
                }
              },
              "207Pb": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "label",
                    "isotropic_shielding_ppm"
                  ],
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "isotropic_shielding_ppm": {
                      "type": "number"
                    }
                  }
                }
              },
              "13C": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "label",
                    "isotropic_shielding_ppm"
                  ],
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "isotropic_shielding_ppm": {
                      "type": "number"
                    }
                  }
                }
              },
              "14N": {
                "type": "array",
                "items": {
                  "type": "object",
                  "required": [
                    "label",
                    "isotropic_shielding_ppm"
                  ],
                  "properties": {
                    "label": {
                      "type": "string"
                    },
                    "isotropic_shielding_ppm": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "Isotropic NMR shieldings for all 127I, 207Pb, 13C, and 14N atoms. Checker verifies qualitative trends: for doped case, 127I shieldings show at least three distinct values, the directly coordinated I differs significantly; 14N near Mn is split; average 13C shieldings show a high‑field shift relative to pristine; 207Pb shieldings remain essentially unchanged."
    },
    {
      "file": "mn_gv_tensor.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "g_xx",
          "g_yy",
          "g_zz",
          "V_xx",
          "V_yy",
          "V_zz",
          "eta"
        ],
        "properties": {
          "g_xx": {
            "type": "number"
          },
          "g_yy": {
            "type": "number"
          },
          "g_zz": {
            "type": "number"
          },
          "V_xx": {
            "type": "number"
          },
          "V_yy": {
            "type": "number"
          },
          "V_zz": {
            "type": "number"
          },
          "eta": {
            "type": "number"
          }
        }
      },
      "description": "Principal g‑tensor components, EFG principal components, and asymmetry parameter η for Mn in the doped system. Checker verifies that g_xx, g_yy, g_zz are all distinct (anisotropic), V_zz > V_yy > V_xx, and η is between 0.2 and 0.4."
    }
  ],
  "notes": "The agent must construct the supercells, perform the DFT/TD‑DFT/GIAO calculations with ORCA and the LANL2DZ basis, and produce the four JSON artifacts. Checker verifies structural trends and toleranced thresholds; exact numeric match to the published paper is not required. OSC and NMR shieldings are to be reported in the same units as the original work (eV, nm, dimensionless oscillator strength, ppm)."
}
```

## How you are scored
A hidden verifier examines each of the four JSON output files. It checks that every file has the expected structure and that the reported numerical values are physically plausible and internally consistent. Quantitative checks verify that the computed band gap, optical absorption, NMR shieldings, and magnetic tensors are within reasonable ranges for the given methodology. The verifier combines the outcomes from all stages into a single reward score between 0 (no credit) and 1 (full credit). Simply reporting a pre‑known value from the literature without executing the required DFT calculations will not satisfy the checks; the artifacts must be produced by running the workflow.
