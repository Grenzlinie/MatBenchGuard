# Li-ion Vacancy Migration Barriers and Electronic Properties in SEI Components

## Problem background
The solid electrolyte interphase (SEI) layer that forms on graphite anodes in lithium-ion batteries is critical for battery performance and safety. Three inorganic compounds—Li₂CO₃, Li₂O, and LiF—are major constituents of the compact, stable inner part of the SEI. Their electronic conductivity and their ability to accommodate lithium ion diffusion directly influence the overall ionic transport through the SEI and thus the rate capability of the anode. However, the intrinsic electronic properties and the lithium migration barriers in these materials remain subjects of active investigation. In this task, you will use first-principles calculations to determine these properties for all three compounds.

## Approach
You will employ plane-wave density functional theory (DFT) with the generalized gradient approximation (PBE) and projector augmented-wave (PAW) pseudopotentials, using an open‑source code such as Quantum ESPRESSO. For each compound you will:

- Fully relax the bulk crystal structure, optimizing both lattice constants and atomic positions.
- Compute the total (Kohn–Sham) density of states and extract the fundamental band gap and the width of the occupied valence band.
- Create a single lithium vacancy in a supercell of the relaxed structure and use the nudged elastic band (NEB) method to locate the minimum energy path for a lithium ion to migrate into the vacancy site. For Li₂CO₃ you will explore several symmetrically distinct migration paths; for Li₂O you will focus on the cubic‑edge direction; for LiF you will examine the nearest‑neighbor jump.

All results are to be saved in structured JSON files according to the provided schemas.

## Reproduction target
Compute the equilibrium lattice parameters, the Kohn‑Sham band gap and valence‑band width, and the minimum lithium‑vacancy migration energy barriers for Li₂CO₃, Li₂O, and LiF using the protocol described above. The target quantities are:

- For each compound: lattice constants (in Å; the monoclinic angle for Li₂CO₃).
- Electronic properties: Kohn‑Sham band gap (eV) and valence‑band width (eV).
- Migration barriers (eV): for Li₂CO₃ the minimum and maximum barrier among the distinct pathways; for Li₂O the barrier along the cubic‑edge pathway; for LiF the barrier for a nearest‑neighbor jump.

These must be written to the three JSON output files detailed in the workflow steps. The objective is to reproduce these key properties with a level of accuracy that is consistent with the chosen open‑source DFT implementation and standard computational settings.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE pseudopotentials for Li, C, O, F: https://www.materialscloud.org/sssp/

## Workflow steps

### Step 1: DFT Geometry Optimization of Bulk Li2CO3, Li2O, and LiF
- Role: scored
- Action: Perform DFT geometry optimization for bulk Li2CO3 (monoclinic C2/c), Li2O (cubic Fm-3m), and LiF (cubic Fm-3m) using plane-wave DFT with the PBE functional and PAW pseudopotentials. Optimize both lattice constants and internal atomic positions until forces are converged. Save the final relaxed lattice parameters to a JSON file.
- Output file: `/app/outputs/lattice_parameters.json`
- Format: json
- Contract: {"li2co3": {"a": <float>, "b": <float>, "c": <float>, "beta_deg": <float>}, "li2o": {"a": <float>}, "lif": {"a": <float>}}
- Scoring: scored by hidden verifier

### Step 2: Electronic Density of States and Band Gaps of Perfect Crystals
- Role: scored
- Action: Using the relaxed geometries from step 1, compute the total density of states for each compound. Extract the Kohn-Sham band gap (energy difference between the lowest unoccupied and highest occupied Kohn-Sham eigenvalue) and the valence-band width (span of occupied Kohn-Sham states). Report these for Li2CO3, Li2O, and LiF.
- Output file: `/app/outputs/electronic_properties.json`
- Format: json
- Contract: {"li2co3": {"vb_width_eV": <float>, "band_gap_eV": <float>}, "li2o": {"vb_width_eV": <float>, "band_gap_eV": <float>}, "lif": {"vb_width_eV": <float>, "band_gap_eV": <float>}}
- Scoring: scored by hidden verifier

### Step 3: Li Vacancy Migration Barriers via Nudged Elastic Band
- Role: scored (load-bearing)
- Action: Create one lithium vacancy in each optimized supercell from step 1. For Li2CO3, enumerate the symmetrically distinct vacancy migration pathways and compute the minimum-energy path using the nudged elastic band (NEB) method for each, reporting the minimum and maximum barrier heights. For Li2O, compute the NEB barrier along the cubic-edge direction. For LiF, compute the barrier for a nearest-neighbor Li jump. Report all migration barriers in eV.
- Output file: `/app/outputs/migration_barriers.json`
- Format: json
- Contract: {"li2co3": {"min_barrier_eV": <float>, "max_barrier_eV": <float>}, "li2o": {"path3_barrier_eV": <float>}, "lif": {"barrier_eV": <float>}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_parameters.json`
- `/app/outputs/electronic_properties.json`
- `/app/outputs/migration_barriers.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_parameters.json
- path: `/app/outputs/lattice_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Optimized DFT lattice constants (Å, degrees) for the three compounds.
- schema:
  - `type`: object
  - `required`: `li2co3`, `li2o`, `lif`
  - `properties`:
    - `li2co3`:
      - `type`: object
      - `required`: `a`, `b`, `c`, `beta_deg`
      - `properties`:
        - `a`:
          - `type`: number
        - `b`:
          - `type`: number
        - `c`:
          - `type`: number
        - `beta_deg`:
          - `type`: number
    - `li2o`:
      - `type`: object
      - `required`: `a`
      - `properties`:
        - `a`:
          - `type`: number
    - `lif`:
      - `type`: object
      - `required`: `a`
      - `properties`:
        - `a`:
          - `type`: number

### electronic_properties.json
- path: `/app/outputs/electronic_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Kohn-Sham band gaps and valence-band widths (eV) for the three compounds.
- schema:
  - `type`: object
  - `required`: `li2co3`, `li2o`, `lif`
  - `properties`:
    - `li2co3`:
      - `type`: object
      - `required`: `vb_width_eV`, `band_gap_eV`
      - `properties`:
        - `vb_width_eV`:
          - `type`: number
        - `band_gap_eV`:
          - `type`: number
    - `li2o`:
      - `type`: object
      - `required`: `vb_width_eV`, `band_gap_eV`
      - `properties`:
        - `vb_width_eV`:
          - `type`: number
        - `band_gap_eV`:
          - `type`: number
    - `lif`:
      - `type`: object
      - `required`: `vb_width_eV`, `band_gap_eV`
      - `properties`:
        - `vb_width_eV`:
          - `type`: number
        - `band_gap_eV`:
          - `type`: number

### migration_barriers.json
- path: `/app/outputs/migration_barriers.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: NEB Li vacancy migration energy barriers (eV) for the three compounds.
- schema:
  - `type`: object
  - `required`: `li2co3`, `li2o`, `lif`
  - `properties`:
    - `li2co3`:
      - `type`: object
      - `required`: `min_barrier_eV`, `max_barrier_eV`
      - `properties`:
        - `min_barrier_eV`:
          - `type`: number
        - `max_barrier_eV`:
          - `type`: number
    - `li2o`:
      - `type`: object
      - `required`: `path3_barrier_eV`
      - `properties`:
        - `path3_barrier_eV`:
          - `type`: number
    - `lif`:
      - `type`: object
      - `required`: `barrier_eV`
      - `properties`:
        - `barrier_eV`:
          - `type`: number

Notes: All quantities are computed using open-source plane-wave DFT with PBE pseudopotentials. The exact values depend on convergence settings; check against paper values with tolerances described in the hidden grading spec.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "li2co3",
          "li2o",
          "lif"
        ],
        "properties": {
          "li2co3": {
            "type": "object",
            "required": [
              "a",
              "b",
              "c",
              "beta_deg"
            ],
            "properties": {
              "a": {
                "type": "number"
              },
              "b": {
                "type": "number"
              },
              "c": {
                "type": "number"
              },
              "beta_deg": {
                "type": "number"
              }
            }
          },
          "li2o": {
            "type": "object",
            "required": [
              "a"
            ],
            "properties": {
              "a": {
                "type": "number"
              }
            }
          },
          "lif": {
            "type": "object",
            "required": [
              "a"
            ],
            "properties": {
              "a": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Optimized DFT lattice constants (Å, degrees) for the three compounds."
    },
    {
      "file": "electronic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "li2co3",
          "li2o",
          "lif"
        ],
        "properties": {
          "li2co3": {
            "type": "object",
            "required": [
              "vb_width_eV",
              "band_gap_eV"
            ],
            "properties": {
              "vb_width_eV": {
                "type": "number"
              },
              "band_gap_eV": {
                "type": "number"
              }
            }
          },
          "li2o": {
            "type": "object",
            "required": [
              "vb_width_eV",
              "band_gap_eV"
            ],
            "properties": {
              "vb_width_eV": {
                "type": "number"
              },
              "band_gap_eV": {
                "type": "number"
              }
            }
          },
          "lif": {
            "type": "object",
            "required": [
              "vb_width_eV",
              "band_gap_eV"
            ],
            "properties": {
              "vb_width_eV": {
                "type": "number"
              },
              "band_gap_eV": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Kohn-Sham band gaps and valence-band widths (eV) for the three compounds."
    },
    {
      "file": "migration_barriers.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "li2co3",
          "li2o",
          "lif"
        ],
        "properties": {
          "li2co3": {
            "type": "object",
            "required": [
              "min_barrier_eV",
              "max_barrier_eV"
            ],
            "properties": {
              "min_barrier_eV": {
                "type": "number"
              },
              "max_barrier_eV": {
                "type": "number"
              }
            }
          },
          "li2o": {
            "type": "object",
            "required": [
              "path3_barrier_eV"
            ],
            "properties": {
              "path3_barrier_eV": {
                "type": "number"
              }
            }
          },
          "lif": {
            "type": "object",
            "required": [
              "barrier_eV"
            ],
            "properties": {
              "barrier_eV": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "NEB Li vacancy migration energy barriers (eV) for the three compounds."
    }
  ],
  "notes": "All quantities are computed using open-source plane-wave DFT with PBE pseudopotentials. The exact values depend on convergence settings; check against paper values with tolerances described in the hidden grading spec."
}
```

## How you are scored
After you submit the three JSON files, an automatic verifier will read each file and compare every numeric field against a hidden set of reference values (the paper’s computed results). The comparison uses predetermined tolerances that account for differences between DFT codes. Each field that falls within tolerance counts as one point; the total reward is the fraction of correct fields across all three files, averaged so each file contributes equally. Reporting an approximate value without actually performing the DFT calculations is not sufficient; the scored reward will only be high if your computed numbers reflect a genuine first‑principles simulation with well‑converged settings.
