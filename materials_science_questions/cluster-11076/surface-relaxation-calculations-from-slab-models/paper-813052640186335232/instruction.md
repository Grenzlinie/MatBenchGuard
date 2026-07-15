# Surface relaxation and energies of low-index Rh surfaces from plane-wave DFT

## Problem background
The atomic-scale structure of transition-metal surfaces is key to understanding their catalytic properties in processes such as hydrogenation and emission control. For rhodium (Rh), low-index surfaces exhibit surface relaxations where the interlayer spacings differ from the bulk. Previous experimental studies using LEED have reported conflicting values, especially for the Rh(100) surface. Reliable ab initio predictions are therefore needed to determine the relaxation magnitudes and surface energies. This reproduction task computes the surface relaxation and energetic properties of Rh(111), (100), and (110) using plane-wave density-functional theory (DFT).

## Approach
The method uses self-consistent DFT in the local-density approximation (LDA) with ultra-soft pseudopotentials (or PAW) to model Rh. Periodic slab geometries are constructed for each orientation using the experimental fcc lattice constant of Rh (3.80 Å). Each slab consists of 10 atomic layers separated by a vacuum region; the two central layers are fixed at bulk positions to represent the bulk interior. The atomic positions are relaxed via conjugate-gradient minimization until forces are converged. The total energy is recorded before and after relaxation, and the interlayer distances d12 through d45 are extracted. From these raw quantities, the interlayer relaxation percentages, the surface energy, and the relaxation energy per atom are derived. The calculations follow widely used plane-wave DFT protocols and can be performed with any open-source code that supports pseudopotentials and geometry relaxation.

## Reproduction target
The objective is to compute the surface relaxation characteristics of the three Rh surfaces and produce a single JSON file containing both the raw input/output data and the derived properties. Specifically, for Rh(111), Rh(100), and Rh(110) you must:

- Build symmetric 10-layer slabs with fixed central layers.
- Perform plane-wave DFT geometry optimizations and record total energies and interlayer spacings.
- Derive Δ12, Δ23, Δ34, Δ45 (percentage interlayer changes relative to the bulk spacing), the surface energy σ (in eV per surface atom), and the relaxation energy ΔE_rel (in meV per atom).
- Write the results to `/app/outputs/relaxation_output.json` following the exact schema given in the output contract.

The derived quantities will be checked by the verifier; you are not required to output any other files.

## Assets

- Open-source plane-wave DFT code (e.g., Quantum ESPRESSO or GPAW): https://www.quantum-espresso.org/
- Rh pseudopotential (ultra-soft or PAW) from SSSP precision library or equivalent: https://www.materialscloud.org/discover/sssp/table/precision

## Workflow steps

### Step 1: Build slab models
- Role: process
- Action: Construct periodic slab models for the Rh(111), Rh(100), and Rh(110) surfaces. Use the experimental fcc lattice constant (a=3.80 Å) to create symmetric 10-layer slabs with a vacuum region equivalent to 4 atomic layers. Fix the two central layers of each slab at their bulk positions. Generate the initial atomic coordinates and input files for the chosen DFT code.
- Evidence: none

### Step 2: DFT structural relaxation
- Role: process
- Action: For each slab, perform self-consistent plane-wave DFT calculations using the chosen pseudopotential and a well-converged plane-wave cutoff, k-point sampling, and smearing appropriate for metallic surfaces. Use conjugate-gradient optimization to relax the atomic positions until the forces on all movable atoms are converged. Record the total energy of the unrelaxed slab at the start and the total energy of the fully relaxed slab. Save the relaxed interlayer distances (d12, d23, d34, d45).
- Evidence: none

### Step 3: Surface relaxation analysis
- Role: scored (load-bearing)
- Action: From the relaxed and unrelaxed slab data, extract the interlayer spacings, total energies, and simulation parameters. Compute the bulk reference energy per atom from the fixed central layers. Derive the interlayer relaxation percentages Δij = (dij_relaxed − d_bulk)/d_bulk × 100%, the surface energy σ in eV per surface atom, and the relaxation energy ΔE_rel in meV per atom, using the standard formulas. Output a single JSON file containing both the raw data and the derived quantities for the three surfaces.
- Output file: `/app/outputs/relaxation_output.json`
- Format: json
- Contract: {"type":"object","required":["surfaces"],"properties":{"surfaces":{"type":"array","minItems":3,"items":{"type":"object","required":["surface","raw","derived"],"properties":{"surface":{"type":"string","pattern":"Rh\\(\\d{3}\\)"},"raw":{"type":"object","required":["interlayer_spacings","total_energy_relaxed_eV","total_energy_unrelaxed_eV","n_atoms_slab","surface_area_Ang2","n_surface_atoms","bulk_spacing_Ang","bulk_energy_per_atom_eV"],"properties":{"interlayer_spacings":{"type":"object","required":["d12_Ang","d23_Ang","d34_Ang","d45_Ang"],"properties":{"d12_Ang":{"type":"number"},"d23_Ang":{"type":"number"},"d34_Ang":{"type":"number"},"d45_Ang":{"type":"number"}}},"total_energy_relaxed_eV":{"type":"number"},"total_energy_unrelaxed_eV":{"type":"number"},"n_atoms_slab":{"type":"integer"},"surface_area_Ang2":{"type":"number"},"n_surface_atoms":{"type":"integer"},"bulk_spacing_Ang":{"type":"number"},"bulk_energy_per_atom_eV":{"type":"number"}}},"derived":{"type":"object","required":["Delta12_pct","Delta23_pct","Delta34_pct","Delta45_pct","sigma_eV_per_atom","DeltaE_rel_meV_per_atom"],"properties":{"Delta12_pct":{"type":"number"},"Delta23_pct":{"type":"number"},"Delta34_pct":{"type":"number"},"Delta45_pct":{"type":"number"},"sigma_eV_per_atom":{"type":"number"},"DeltaE_rel_meV_per_atom":{"type":"number"}}}}}}}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relaxation_output.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relaxation_output.json
- path: `/app/outputs/relaxation_output.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: JSON file containing raw interlayer spacings, total energies, and slab parameters for the three low-index Rh surfaces, together with the derived surface relaxation percentages, surface energy (eV/atom), and relaxation energy (meV/atom). The hidden checker recomputes the derived quantities from the raw data and compares them to the paper's reference values.
- schema:
  - `type`: object
  - `required`: `surfaces`
  - `properties`:
    - `surfaces`:
      - `type`: array
      - `minItems`: 3
      - `items`:
        - `type`: object
        - `required`: `surface`, `raw`, `derived`
        - `properties`:
          - `surface`:
            - `type`: string
            - `pattern`: Rh\(\d{3}\)
          - `raw`:
            - `type`: object
            - `required`: `interlayer_spacings`, `total_energy_relaxed_eV`, `total_energy_unrelaxed_eV`, `n_atoms_slab`, `surface_area_Ang2`, `n_surface_atoms`, `bulk_spacing_Ang`, `bulk_energy_per_atom_eV`
            - `properties`:
              - `interlayer_spacings`:
                - `type`: object
                - `required`: `d12_Ang`, `d23_Ang`, `d34_Ang`, `d45_Ang`
                - `properties`:
                  - `d12_Ang`:
                    - `type`: number
                  - `d23_Ang`:
                    - `type`: number
                  - `d34_Ang`:
                    - `type`: number
                  - `d45_Ang`:
                    - `type`: number
              - `total_energy_relaxed_eV`:
                - `type`: number
              - `total_energy_unrelaxed_eV`:
                - `type`: number
              - `n_atoms_slab`:
                - `type`: integer
              - `surface_area_Ang2`:
                - `type`: number
              - `n_surface_atoms`:
                - `type`: integer
              - `bulk_spacing_Ang`:
                - `type`: number
              - `bulk_energy_per_atom_eV`:
                - `type`: number
          - `derived`:
            - `type`: object
            - `required`: `Delta12_pct`, `Delta23_pct`, `Delta34_pct`, `Delta45_pct`, `sigma_eV_per_atom`, `DeltaE_rel_meV_per_atom`
            - `properties`:
              - `Delta12_pct`:
                - `type`: number
              - `Delta23_pct`:
                - `type`: number
              - `Delta34_pct`:
                - `type`: number
              - `Delta45_pct`:
                - `type`: number
              - `sigma_eV_per_atom`:
                - `type`: number
              - `DeltaE_rel_meV_per_atom`:
                - `type`: number

Notes: Electronic surface states are not scored; they are qualitative figures and lack precise numerical targets. The bulk reference energy is derived from the fixed central layers of each slab, consistent with the paper's approach.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relaxation_output.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": [
          "surfaces"
        ],
        "properties": {
          "surfaces": {
            "type": "array",
            "minItems": 3,
            "items": {
              "type": "object",
              "required": [
                "surface",
                "raw",
                "derived"
              ],
              "properties": {
                "surface": {
                  "type": "string",
                  "pattern": "Rh\\(\\d{3}\\)"
                },
                "raw": {
                  "type": "object",
                  "required": [
                    "interlayer_spacings",
                    "total_energy_relaxed_eV",
                    "total_energy_unrelaxed_eV",
                    "n_atoms_slab",
                    "surface_area_Ang2",
                    "n_surface_atoms",
                    "bulk_spacing_Ang",
                    "bulk_energy_per_atom_eV"
                  ],
                  "properties": {
                    "interlayer_spacings": {
                      "type": "object",
                      "required": [
                        "d12_Ang",
                        "d23_Ang",
                        "d34_Ang",
                        "d45_Ang"
                      ],
                      "properties": {
                        "d12_Ang": {
                          "type": "number"
                        },
                        "d23_Ang": {
                          "type": "number"
                        },
                        "d34_Ang": {
                          "type": "number"
                        },
                        "d45_Ang": {
                          "type": "number"
                        }
                      }
                    },
                    "total_energy_relaxed_eV": {
                      "type": "number"
                    },
                    "total_energy_unrelaxed_eV": {
                      "type": "number"
                    },
                    "n_atoms_slab": {
                      "type": "integer"
                    },
                    "surface_area_Ang2": {
                      "type": "number"
                    },
                    "n_surface_atoms": {
                      "type": "integer"
                    },
                    "bulk_spacing_Ang": {
                      "type": "number"
                    },
                    "bulk_energy_per_atom_eV": {
                      "type": "number"
                    }
                  }
                },
                "derived": {
                  "type": "object",
                  "required": [
                    "Delta12_pct",
                    "Delta23_pct",
                    "Delta34_pct",
                    "Delta45_pct",
                    "sigma_eV_per_atom",
                    "DeltaE_rel_meV_per_atom"
                  ],
                  "properties": {
                    "Delta12_pct": {
                      "type": "number"
                    },
                    "Delta23_pct": {
                      "type": "number"
                    },
                    "Delta34_pct": {
                      "type": "number"
                    },
                    "Delta45_pct": {
                      "type": "number"
                    },
                    "sigma_eV_per_atom": {
                      "type": "number"
                    },
                    "DeltaE_rel_meV_per_atom": {
                      "type": "number"
                    }
                  }
                }
              }
            }
          }
        }
      },
      "description": "JSON file containing raw interlayer spacings, total energies, and slab parameters for the three low-index Rh surfaces, together with the derived surface relaxation percentages, surface energy (eV/atom), and relaxation energy (meV/atom). The hidden checker recomputes the derived quantities from the raw data and compares them to the paper's reference values."
    }
  ],
  "notes": "Electronic surface states are not scored; they are qualitative figures and lack precise numerical targets. The bulk reference energy is derived from the fixed central layers of each slab, consistent with the paper's approach."
}
```

## How you are scored
A hidden verifier (not visible to you) will load your `relaxation_output.json`, extract the raw slab parameters and energies, and independently recompute the derived quantities (Δij, σ, ΔE_rel) from the same formulas. The recomputed values are then compared against reference values that represent the expected outcome of a correct calculation using the described protocol. Each derived quantity contributes to your score:

- Interlayer relaxation percentages (Δ12, Δ23, Δ34, Δ45) for each surface.
- Surface energy σ per surface atom for each surface.
- Relaxation energy ΔE_rel per atom for each surface.

The comparisons use tolerances that account for the inherent variability between different DFT implementations, pseudopotential choices, and computational parameters while still requiring a physically correct result. In addition to the numerical comparisons, the verifier may check that qualitative trends (e.g., the relative ordering of top-layer contraction among the three surfaces) are consistent with the expected physical behavior, but the primary weight is on the recomputed numeric quantities.

Your total reward is a weighted sum of passes/failures across these checks; a correct full reproduction will achieve a high score, while systematic errors or missing data will reduce the reward proportionally.
