# DFT optical properties for filled tetrahedral compounds Li₃AlN₂ and Li₃GaN₂

## Problem background
Filled tetrahedral semiconductors Li₃AlN₂ and Li₃GaN₂ are wide-bandgap Nowotny-Juza compounds with potential optoelectronic applications. However, experimental optical data such as the frequency-dependent dielectric function, reflectivity, and electron energy loss are scarce. This work computes the optical properties of these compounds from first-principles, producing the full complex dielectric function (ε₁, ε₂), the static dielectric constant ε(0), and the bulk plasmon energy, while also examining whether spin-orbit coupling significantly alters these quantities.

## Approach
The calculation uses the full-potential linearized augmented plane-wave (FP-LAPW) method within density functional theory (DFT), employing the generalized gradient approximation (GGA) for the exchange-correlation functional. Both self-consistent field (SCF) calculations and linear optical response calculations are carried out without and with spin-orbit coupling (SOC). From the SCF wavefunctions and eigenvalues, the imaginary part of the dielectric function ε₂(ω) is computed via the momentum matrix element formula within the random phase approximation, and the real part ε₁(ω) is obtained through Kramers-Kronig transformation. The electron energy-loss spectrum (EELS) is then derived. Finally, the static dielectric constant is read as ε₁ at the lowest frequency, and the bulk plasmon energy is identified as the main peak in the EELS. By comparing the results with and without SOC, the influence of spin-orbit coupling on the optical properties is evaluated.

## Reproduction target
Use an open-source all-electron FP-LAPW code to (i) compute the full complex dielectric function ε(ω) for Li₃AlN₂ and Li₃GaN₂ with and without spin-orbit coupling on a frequency grid up to 75 eV; (ii) extract the static dielectric constant ε(0) and the bulk plasmon energy from the spectra; and (iii) determine the magnitude of the change in these scalar quantities when spin-orbit coupling is included.

## Assets

- Elk FP-LAPW code: https://elk.sourceforge.net/
- Crystal structures of Li3AlN2 and Li3GaN2
- Atomic muffin-tin radii
- Python with numpy, scipy, matplotlib

## Workflow steps

### Step 1: Prepare Elk input files for Li3AlN2 and Li3GaN2
- Role: process
- Action: Create Elk input files for Li3AlN2 and Li3GaN2 using the experimental crystal structures (space group Ia-3, Wyckoff positions, lattice constants) and the given atomic muffin-tin radii. Set Wu-Cohen GGA exchange-correlation functional.
- Evidence: none

### Step 2: Self-consistent field calculation without spin-orbit coupling
- Role: process
- Action: Run DFT self-consistent field calculation for both compounds using the FP-LAPW code (Elk) with the specified parameters (R_MT_min*K_max=8, l_max=10, G_max=14.0 Bohr^-1, 35 k-points in irreducible BZ, tetrahedron method). Do not include spin-orbit coupling. Obtain converged charge density, wavefunctions and eigenvalues.
- Evidence: `/app/outputs/scf_without_soc.log`

### Step 3: Self-consistent field calculation with spin-orbit coupling
- Role: process
- Action: Repeat the SCF calculation for both compounds including spin-orbit coupling. Same DFT parameters as step2. Obtain converged charge density, wavefunctions and eigenvalues with SOC.
- Evidence: `/app/outputs/scf_with_soc.log`

### Step 4: Compute optical spectra
- Role: scored (load-bearing)
- Action: Using the wavefunctions and eigenvalues from step2 (without SOC) and step3 (with SOC), compute the imaginary part of the dielectric function ε₂(ω) via the momentum matrix element formula within the random phase approximation, using a denser k-mesh of 76 points in the irreducible zone. Obtain ε₁(ω) via Kramers-Kronig transformation truncated at 75 eV. Output the full frequency-dependent spectra as a JSON file.
- Output file: `/app/outputs/dielectric_function.json`
- Format: json
- Contract: JSON object with top-level keys "Li3AlN2" and "Li3GaN2". Each value is an object with keys "without_SOC" and "with_SOC". Each of those contains "frequency" (list of floats in eV), "epsilon1" (list of floats), "epsilon2" (list of floats).
- Scoring: scored by hidden verifier

### Step 5: Extract summary scalar values
- Role: scored
- Action: From the dielectric function spectra, extract the static dielectric constant ε(0) = ε₁ at the smallest frequency and the bulk plasmon energy (energy of the highest peak in the electron energy-loss spectrum EELS). Output these scalars to a JSON file.
- Output file: `/app/outputs/optical_summary.json`
- Format: json
- Contract: JSON object with keys "Li3AlN2" and "Li3GaN2". Each value is an object with keys "without_SOC" and "with_SOC". Each of those contains "static_dielectric_constant" (float) and "plasmon_energy" (float in eV).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dielectric_function.json`
- `/app/outputs/optical_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dielectric_function.json
- path: `/app/outputs/dielectric_function.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Full frequency-dependent dielectric function enabling recomputation of static dielectric constant and plasmon energy by the checker.
- schema:
  - `type`: object
  - `required`: `Li3AlN2`, `Li3GaN2`
  - `properties`:
    - `Li3AlN2`:
      - `type`: object
      - `required`: `without_SOC`, `with_SOC`
      - `properties`:
        - `without_SOC`:
          - `type`: object
          - `required`: `frequency`, `epsilon1`, `epsilon2`
          - `properties`:
            - `frequency`:
              - `type`: array
              - `items`:
                - `type`: number
              - `description`: Frequency in eV
            - `epsilon1`:
              - `type`: array
              - `items`:
                - `type`: number
            - `epsilon2`:
              - `type`: array
              - `items`:
                - `type`: number
        - `with_SOC`:
          - `type`: object
          - `required`: `frequency`, `epsilon1`, `epsilon2`
          - `properties`:
            - `frequency`:
              - `type`: array
              - `items`:
                - `type`: number
              - `description`: Frequency in eV
            - `epsilon1`:
              - `type`: array
              - `items`:
                - `type`: number
            - `epsilon2`:
              - `type`: array
              - `items`:
                - `type`: number
    - `Li3GaN2`:
      - `type`: object
      - `required`: `without_SOC`, `with_SOC`
      - `properties`:
        - `without_SOC`:
          - `type`: object
          - `required`: `frequency`, `epsilon1`, `epsilon2`
          - `properties`:
            - `frequency`:
              - `type`: array
              - `items`:
                - `type`: number
            - `epsilon1`:
              - `type`: array
              - `items`:
                - `type`: number
            - `epsilon2`:
              - `type`: array
              - `items`:
                - `type`: number
        - `with_SOC`:
          - `type`: object
          - `required`: `frequency`, `epsilon1`, `epsilon2`
          - `properties`:
            - `frequency`:
              - `type`: array
              - `items`:
                - `type`: number
            - `epsilon1`:
              - `type`: array
              - `items`:
                - `type`: number
            - `epsilon2`:
              - `type`: array
              - `items`:
                - `type`: number

### optical_summary.json
- path: `/app/outputs/optical_summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent's own extracted static dielectric constant and plasmon energy; the checker will cross-check consistency with values recomputed from dielectric_function.json.
- schema:
  - `type`: object
  - `required`: `Li3AlN2`, `Li3GaN2`
  - `properties`:
    - `Li3AlN2`:
      - `type`: object
      - `required`: `without_SOC`, `with_SOC`
      - `properties`:
        - `without_SOC`:
          - `type`: object
          - `required`: `static_dielectric_constant`, `plasmon_energy`
          - `properties`:
            - `static_dielectric_constant`:
              - `type`: number
              - `description`: Static dielectric constant ε(0)
            - `plasmon_energy`:
              - `type`: number
              - `description`: Bulk plasmon energy in eV
        - `with_SOC`:
          - `type`: object
          - `required`: `static_dielectric_constant`, `plasmon_energy`
          - `properties`:
            - `static_dielectric_constant`:
              - `type`: number
            - `plasmon_energy`:
              - `type`: number
    - `Li3GaN2`:
      - `type`: object
      - `required`: `without_SOC`, `with_SOC`
      - `properties`:
        - `without_SOC`:
          - `type`: object
          - `required`: `static_dielectric_constant`, `plasmon_energy`
          - `properties`:
            - `static_dielectric_constant`:
              - `type`: number
            - `plasmon_energy`:
              - `type`: number
        - `with_SOC`:
          - `type`: object
          - `required`: `static_dielectric_constant`, `plasmon_energy`
          - `properties`:
            - `static_dielectric_constant`:
              - `type`: number
            - `plasmon_energy`:
              - `type`: number

Notes: The optical_summary.json is a self-reported summary; the main scoring is based on metrics recomputed from dielectric_function.json. The checker will also verify that the difference between with/without SOC for each scalar is under 0.1 eV (structural check).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dielectric_function.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "Li3AlN2",
          "Li3GaN2"
        ],
        "properties": {
          "Li3AlN2": {
            "type": "object",
            "required": [
              "without_SOC",
              "with_SOC"
            ],
            "properties": {
              "without_SOC": {
                "type": "object",
                "required": [
                  "frequency",
                  "epsilon1",
                  "epsilon2"
                ],
                "properties": {
                  "frequency": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "description": "Frequency in eV"
                  },
                  "epsilon1": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "epsilon2": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  }
                }
              },
              "with_SOC": {
                "type": "object",
                "required": [
                  "frequency",
                  "epsilon1",
                  "epsilon2"
                ],
                "properties": {
                  "frequency": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    },
                    "description": "Frequency in eV"
                  },
                  "epsilon1": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "epsilon2": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          },
          "Li3GaN2": {
            "type": "object",
            "required": [
              "without_SOC",
              "with_SOC"
            ],
            "properties": {
              "without_SOC": {
                "type": "object",
                "required": [
                  "frequency",
                  "epsilon1",
                  "epsilon2"
                ],
                "properties": {
                  "frequency": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "epsilon1": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "epsilon2": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  }
                }
              },
              "with_SOC": {
                "type": "object",
                "required": [
                  "frequency",
                  "epsilon1",
                  "epsilon2"
                ],
                "properties": {
                  "frequency": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "epsilon1": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  },
                  "epsilon2": {
                    "type": "array",
                    "items": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "Full frequency-dependent dielectric function enabling recomputation of static dielectric constant and plasmon energy by the checker."
    },
    {
      "file": "optical_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "Li3AlN2",
          "Li3GaN2"
        ],
        "properties": {
          "Li3AlN2": {
            "type": "object",
            "required": [
              "without_SOC",
              "with_SOC"
            ],
            "properties": {
              "without_SOC": {
                "type": "object",
                "required": [
                  "static_dielectric_constant",
                  "plasmon_energy"
                ],
                "properties": {
                  "static_dielectric_constant": {
                    "type": "number",
                    "description": "Static dielectric constant ε(0)"
                  },
                  "plasmon_energy": {
                    "type": "number",
                    "description": "Bulk plasmon energy in eV"
                  }
                }
              },
              "with_SOC": {
                "type": "object",
                "required": [
                  "static_dielectric_constant",
                  "plasmon_energy"
                ],
                "properties": {
                  "static_dielectric_constant": {
                    "type": "number"
                  },
                  "plasmon_energy": {
                    "type": "number"
                  }
                }
              }
            }
          },
          "Li3GaN2": {
            "type": "object",
            "required": [
              "without_SOC",
              "with_SOC"
            ],
            "properties": {
              "without_SOC": {
                "type": "object",
                "required": [
                  "static_dielectric_constant",
                  "plasmon_energy"
                ],
                "properties": {
                  "static_dielectric_constant": {
                    "type": "number"
                  },
                  "plasmon_energy": {
                    "type": "number"
                  }
                }
              },
              "with_SOC": {
                "type": "object",
                "required": [
                  "static_dielectric_constant",
                  "plasmon_energy"
                ],
                "properties": {
                  "static_dielectric_constant": {
                    "type": "number"
                  },
                  "plasmon_energy": {
                    "type": "number"
                  }
                }
              }
            }
          }
        }
      },
      "description": "Agent's own extracted static dielectric constant and plasmon energy; the checker will cross-check consistency with values recomputed from dielectric_function.json."
    }
  ],
  "notes": "The optical_summary.json is a self-reported summary; the main scoring is based on metrics recomputed from dielectric_function.json. The checker will also verify that the difference between with/without SOC for each scalar is under 0.1 eV (structural check)."
}
```

## How you are scored
A hidden verifier will independently score your output by re-deriving the static dielectric constant and plasmon energy from the spectra you provide in dielectric_function.json, then comparing them against reference values (with appropriate tolerances). It will also check that the self-reported values in optical_summary.json are consistent with the spectra. The final reward is a weighted combination of the scores from each scored artifact.
