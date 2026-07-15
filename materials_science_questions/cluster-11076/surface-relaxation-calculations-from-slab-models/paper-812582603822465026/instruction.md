# Surface reconstruction of rocksalt (001) surfaces of MoC, WC, MoN, and WN

## Problem background
Rocksalt (cubic, Fm\overline{3}m) polymorphs of MoC, WC, MoN, and WN are metastable with respect to their most stable hexagonal bulk phases. It is hypothesized that this bulk instability drives the (001) surfaces to reconstruct — i.e., to break the symmetry of the ideal bulk truncation — when modelled with sufficiently large lateral periodicity. Small simulation cells may artificially preserve the bulk symmetry and mask the reconstruction. The goal of this task is to computationally probe this hypothesis by determining the relaxed surface energies, geometric distortions, and dynamical stability of these surfaces as a function of supercell size, and by measuring the energy difference between the rocksalt and hexagonal bulk structures.

## Approach
Density functional theory (DFT) with the Perdew–Burke–Ernzerhof (PBE) exchange‑correlation functional is used to optimise the bulk rocksalt and hexagonal crystal structures for each compound. (001)-oriented slab models are cut from the optimised rocksalt bulk and constructed with four atomic layers in a 2+2 scheme (top two layers free to relax, bottom two fixed) and a vacuum gap of at least 15 Å. Supercells of increasing size — (1×1), (2×2), (3×3), (4×4) — are built to systematically release lateral constraints. Each slab is relaxed, and for MoC the vibrational stability is checked by finite‑displacement phonon calculations: imaginary frequencies indicate a kinetically unstable structure and the slab is then distorted along the soft modes and re‑relaxed until only real frequencies remain. From the total energies of the fixed and relaxed slabs, together with the bulk energies, surface energies are computed in a two‑step procedure: first a bulk‑truncated surface energy is obtained from the fixed slab, and then the relaxed surface energy is derived by removing the bulk‑truncated contribution from the energy change upon relaxation. For the reconstructed (2×2) surfaces, metal–nonmetal distance variations and in‑plane bond‑angle deviations are extracted relative to the ideal bulk‑truncated slab. Finally, the bulk energy difference per formula unit between the rocksalt and the most stable hexagonal polymorph is computed.

## Reproduction target
Produce a single JSON file containing:
- The relaxed surface energies γ\^rel (in J/m²) for the (001) surfaces of MoC, WC, MoN and WN in each of the four supercells (1×1, 2×2, 3×3, 4×4).
- A boolean flag indicating the presence (true) or absence (false) of imaginary vibrational frequencies for the relaxed MoC (1×1) and (2×2) slabs.
- The metal–nonmetal distance variations d(MC) (in Å) and the in‑plane angle deviations α (in °) for the surface layer and the first subsurface layer of the reconstructed (2×2) surface of each material.
- The bulk energy difference ΔE (in eV per formula unit) between the optimised rocksalt and the most stable hexagonal phase for each compound.
The quantities must be computed from DFT relaxations as described, and the reported values should allow evaluating whether the surface reconstructions emerge only in large enough supercells.

## Assets

- DFT code (Quantum ESPRESSO, VASP, GPAW, or equivalent): https://www.quantum-espresso.org/
- PAW pseudopotentials for Mo, W, C, N (e.g., PseudoDojo): https://www.pseudo-dojo.org/
- ASE and NumPy: ase

## Workflow steps

### Step 1: Bulk structure optimization
- Role: process
- Action: For each material (MoC, WC, MoN, WN), optimize the rocksalt cubic (Fm3m) and the most stable hexagonal bulk unit cell using DFT with PBE functional. Record the total energy per formula unit and optimized lattice parameters.
- Evidence: `/app/outputs/bulk_energies.json`

### Step 2: Slab model generation
- Role: process
- Action: From the optimized rocksalt bulk cells, cut (001)-oriented slab models with four atomic layers (2+2 scheme: top two layers free, bottom two fixed) and a vacuum gap ≥ 15 Å. Build supercells for (1×1), (2×2), (3×3), and (4×4) for each material.
- Evidence: `/app/outputs/slab_geometries.extxyz`

### Step 3: Surface relaxation and reconstruction search
- Role: process
- Action: For each slab model, perform ionic relaxation of the free layers using DFT. For MoC (1×1) and (2×2), compute phonon frequencies via finite displacements; if imaginary modes are found, distort along the eigenvectors and re-relax until only positive frequencies remain. For other materials, the (2×2) relaxation is expected to directly yield the reconstructed minimum; verify absence of imaginary frequencies.
- Evidence: `/app/outputs/relaxation_summary.json`

### Step 4: Compile and report scored results
- Role: scored (load-bearing)
- Action: From the total energies of relaxed and unrelaxed slabs, bulk energies, and slab surface areas, compute the relaxed surface energy γ^rel (J/m²) for every material and supercell. Extract metal–nonmetal distance variations d(MC) (Å) and in-plane angle deviations α (°) for the surface and subsurface layers of the (2×2) reconstructed surfaces. Compute the bulk energy difference per formula unit ΔE (eV) between rocksalt and the most stable hexagonal phase. Record whether imaginary vibrational frequencies were found for MoC (1×1) and (2×2). Assemble all quantities into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: {
  "materials": ["MoC", "WC", "MoN", "WN"],
  "supercells": ["1x1", "2x2", "3x3", "4x4"],
  "surface_energies": {
    "<material>": {
      "<supercell>": {"gamma_rel": <float>, "units": "J/m2"}
    }
  },
  "imaginary_frequencies_MoC": {
    "1x1": <boolean>,
    "2x2": <boolean>
  },
  "geometric_parameters": {
    "<material>": {
      "d_MC_surface": <float>,
      "d_MC_subsurface": <float>,
      "alpha_surface": <float>,
      "alpha_subsurface": <float>,
      "units": {"distance": "angstrom", "angle": "deg"}
    }
  },
  "bulk_energy_diff": {
    "<material>": {"Delta_E": <float>, "units": "eV/f.u."}
  }
}
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
- target_policy: reference_match
- description: The scored artifact containing relaxed surface energies, geometric distortions, imaginary frequency flags, and bulk energy differences. The hidden checker compares each value against paper-reported gold values with tolerances and verifies the trend that (2×2) and (4×4) surface energies are lower than (1×1).
- schema:
  - `type`: object
  - `required`: `materials`, `supercells`, `surface_energies`, `imaginary_frequencies_MoC`, `geometric_parameters`, `bulk_energy_diff`
  - `properties`:
    - `materials`:
      - `type`: array
      - `items`:
        - `type`: string
    - `supercells`:
      - `type`: array
      - `items`:
        - `type`: string
    - `surface_energies`:
      - `type`: object
      - `patternProperties`:
        - `.*`:
          - `type`: object
          - `patternProperties`:
            - `.*`:
              - `type`: object
              - `properties`:
                - `gamma_rel`:
                  - `type`: number
                - `units`:
                  - `type`: string
              - `required`: `gamma_rel`, `units`
    - `imaginary_frequencies_MoC`:
      - `type`: object
      - `properties`:
        - `1x1`:
          - `type`: boolean
        - `2x2`:
          - `type`: boolean
      - `required`: `1x1`, `2x2`
    - `geometric_parameters`:
      - `type`: object
      - `patternProperties`:
        - `.*`:
          - `type`: object
          - `properties`:
            - `d_MC_surface`:
              - `type`: number
            - `d_MC_subsurface`:
              - `type`: number
            - `alpha_surface`:
              - `type`: number
            - `alpha_subsurface`:
              - `type`: number
            - `units`:
              - `type`: object
              - `properties`:
                - `distance`:
                  - `type`: string
                - `angle`:
                  - `type`: string
              - `required`: `distance`, `angle`
          - `required`: `d_MC_surface`, `d_MC_subsurface`, `alpha_surface`, `alpha_subsurface`, `units`
    - `bulk_energy_diff`:
      - `type`: object
      - `patternProperties`:
        - `.*`:
          - `type`: object
          - `properties`:
            - `Delta_E`:
              - `type`: number
            - `units`:
              - `type`: string
          - `required`: `Delta_E`, `units`

Notes: All quantities are computed from DFT slab relaxations. The checker uses result-level comparison (T0) with physical tolerances: surface energies ±0.05 J/m², distances ±0.05 Å, angles ±2°, ΔE ±0.05 eV, and exact boolean matches for imaginary frequencies.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "materials",
          "supercells",
          "surface_energies",
          "imaginary_frequencies_MoC",
          "geometric_parameters",
          "bulk_energy_diff"
        ],
        "properties": {
          "materials": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "supercells": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "surface_energies": {
            "type": "object",
            "patternProperties": {
              ".*": {
                "type": "object",
                "patternProperties": {
                  ".*": {
                    "type": "object",
                    "properties": {
                      "gamma_rel": {
                        "type": "number"
                      },
                      "units": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "gamma_rel",
                      "units"
                    ]
                  }
                }
              }
            }
          },
          "imaginary_frequencies_MoC": {
            "type": "object",
            "properties": {
              "1x1": {
                "type": "boolean"
              },
              "2x2": {
                "type": "boolean"
              }
            },
            "required": [
              "1x1",
              "2x2"
            ]
          },
          "geometric_parameters": {
            "type": "object",
            "patternProperties": {
              ".*": {
                "type": "object",
                "properties": {
                  "d_MC_surface": {
                    "type": "number"
                  },
                  "d_MC_subsurface": {
                    "type": "number"
                  },
                  "alpha_surface": {
                    "type": "number"
                  },
                  "alpha_subsurface": {
                    "type": "number"
                  },
                  "units": {
                    "type": "object",
                    "properties": {
                      "distance": {
                        "type": "string"
                      },
                      "angle": {
                        "type": "string"
                      }
                    },
                    "required": [
                      "distance",
                      "angle"
                    ]
                  }
                },
                "required": [
                  "d_MC_surface",
                  "d_MC_subsurface",
                  "alpha_surface",
                  "alpha_subsurface",
                  "units"
                ]
              }
            }
          },
          "bulk_energy_diff": {
            "type": "object",
            "patternProperties": {
              ".*": {
                "type": "object",
                "properties": {
                  "Delta_E": {
                    "type": "number"
                  },
                  "units": {
                    "type": "string"
                  }
                },
                "required": [
                  "Delta_E",
                  "units"
                ]
              }
            }
          }
        }
      },
      "description": "The scored artifact containing relaxed surface energies, geometric distortions, imaginary frequency flags, and bulk energy differences. The hidden checker compares each value against paper-reported gold values with tolerances and verifies the trend that (2×2) and (4×4) surface energies are lower than (1×1)."
    }
  ],
  "notes": "All quantities are computed from DFT slab relaxations. The checker uses result-level comparison (T0) with physical tolerances: surface energies ±0.05 J/m², distances ±0.05 Å, angles ±2°, ΔE ±0.05 eV, and exact boolean matches for imaginary frequencies."
}
```

## How you are scored
Every step in the workflow that produces a scored artifact is evaluated by a hidden verifier that holds reference values derived from the original study. The verifier checks the reported surface energies, geometric parameters, bulk energy differences, and imaginary‑frequency flags against these reference values with physically motivated tolerances. For the surface energies, the verifier also checks the relative trend across supercell sizes. Each scored artifact contributes a weighted portion to the final reward; the sum is a single float between 0 and 1. Reporting values that have not been produced by the required computational pipeline will not satisfy the verifier's checks.
