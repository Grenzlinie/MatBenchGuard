# Half-metallicity preservation in rocksalt BaC surfaces and interfaces

## Problem background
Rocksalt BaC has been predicted to be a half-metallic ferromagnet, where one spin channel is metallic and the other is insulating. For practical spintronic device applications, it is essential to know whether this half-metallicity survives at surfaces and interfaces with semiconductors. This task investigates the electronic and magnetic properties of the (001) and (111) surfaces of rocksalt BaC and the BaC/SnSe (111) interface, with the goal of determining whether half-metallicity is preserved or lost in these structures.

## Approach
The approach uses first-principles density functional theory (DFT) calculations with the generalized gradient approximation (PBE functional). A slab model is employed: 13-layer slabs for BaC surfaces with 15 Å vacuum, and a combined slab of 13 BaC layers and 9 SnSe layers for interfaces. Both Ba- and C-terminated (111) surfaces are studied, along with the (001) surface. For interfaces, four terminations (Ba-Sn, Ba-Se, C-Sn, C-Se) are constructed. After relaxing the top atomic layers, spin-polarized static calculations yield the spin-resolved density of states (DOS), from which the magnetic moments and energy gaps (where applicable) are extracted. The central layers of the slabs serve as a bulk reference. The computational workflow is carried out using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO) with standard pseudopotentials.

## Reproduction target
Compute and report the following quantities for each configuration: magnetic moments (in µB) for Ba and C atoms at the surfaces and interfaces, a boolean half-metallicity verdict (True if the spin-up channel has a gap at the Fermi level while spin-down is metallic), and for surfaces, the majority-spin energy gap (in eV). All results must be collected into a single JSON file `step_04_results.json` placed under `/app/outputs`. The file must follow the specified schema, containing entries for bulk, three surface terminations, and four interface terminations.

## Assets

- Quantum ESPRESSO (open-source DFT package): https://www.quantum-espresso.org/
- Pseudopotentials for Ba, C, Sn, Se from SSSP library (PBE): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: Bulk BaC reference DFT calculation
- Role: process
- Action: Perform spin-polarized DFT calculation for bulk rocksalt BaC (lattice constant 6.003 Å) using a plane-wave code with PBE functional to obtain bulk total energy, spin-resolved density of states, and atomic magnetic moments. This serves as a reference to verify that central layers of later slabs reproduce bulk properties.
- Evidence: none

### Step 2: BaC surface slab model construction
- Role: process
- Action: Build 13-layer slab models for the (001) surface (both Ba and C per layer) and for the Ba- and C-terminated (111) surfaces, each with a 15 Å vacuum layer.
- Evidence: none

### Step 3: BaC surface geometry relaxation
- Role: process
- Action: Relax the top five atomic layers of each surface slab using DFT (PBE functional) until forces converge. Record the relaxed geometries.
- Evidence: none

### Step 4: Surface electronic structure and magnetic moments
- Role: process
- Action: Perform static DFT calculations on the relaxed surface slabs to obtain atom-resolved spin-polarized density of states, spin-up energy gaps, and magnetic moments for surface atoms.
- Evidence: none

### Step 5: SnSe (111) slab construction and relaxation
- Role: process
- Action: Construct a 9-layer rocksalt SnSe (111) slab (lattice constant 6.02 Å) with vacuum, and relax the slab using DFT.
- Evidence: none

### Step 6: BaC/SnSe interface construction
- Role: process
- Action: Combine the relaxed BaC (111) slabs (both terminations) with the relaxed SnSe (111) slab to create the four possible interfacial terminations: Ba-Sn, Ba-Se, C-Sn, C-Se.
- Evidence: none

### Step 7: Interface geometry relaxation
- Role: process
- Action: Relax the interfacial atomic positions for each of the four interface configurations using DFT.
- Evidence: none

### Step 8: Interface electronic structure calculation
- Role: process
- Action: Perform static DFT calculations on the relaxed interface slabs to obtain interface atom-resolved spin-polarized DOS and magnetic moments.
- Evidence: none

### Step 9: Consolidate and report surface and interface results
- Role: scored (load-bearing)
- Action: Collect the computed magnetic moments for bulk, surfaces, and interfaces, together with the surface majority-spin energy gaps. Determine half-metallicity (True if spin-up channel shows a gap at the Fermi level while spin-down is metallic) from the DOS. Write all data to step_04_results.json according to the schema.
- Output file: `/app/outputs/step_04_results.json`
- Format: json
- Contract: {"surfaces": [{"name": "001", "Ba_moment": float, "C_moment": float, "half_metallic": bool, "majority_gap": float}, {"name": "111-Ba", "Ba_moment": float, "half_metallic": bool, "majority_gap": float}, {"name": "111-C", "C_moment": float, "half_metallic": bool, "majority_gap": float}], "interfaces": [{"name": "Ba-Sn", "Ba_moment": float, "C_moment": float, "half_metallic": bool}, {"name": "Ba-Se", "Ba_moment": float, "C_moment": float, "half_metallic": bool}, {"name": "C-Sn", "Ba_moment": float, "C_moment": float, "half_metallic": bool}, {"name": "C-Se", "Ba_moment": float, "C_moment": float, "half_metallic": bool}], "bulk": {"Ba_moment": float, "C_moment": float}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_04_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_04_results.json
- path: `/app/outputs/step_04_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Contains computed magnetic moments (μB), half-metallicity booleans, and majority-spin energy gaps (eV) for bulk, three surface terminations, and four interface terminations.
- schema:
  - `type`: object
  - `properties`:
    - `bulk`:
      - `type`: object
      - `properties`:
        - `Ba_moment`:
          - `type`: number
        - `C_moment`:
          - `type`: number
      - `required`: `Ba_moment`, `C_moment`
    - `surfaces`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `name`:
            - `type`: string
          - `Ba_moment`:
            - `type`: number
          - `C_moment`:
            - `type`: number
          - `half_metallic`:
            - `type`: boolean
          - `majority_gap`:
            - `type`: number
        - `required`: `name`, `half_metallic`, `majority_gap`
    - `interfaces`:
      - `type`: array
      - `items`:
        - `type`: object
        - `properties`:
          - `name`:
            - `type`: string
          - `Ba_moment`:
            - `type`: number
          - `C_moment`:
            - `type`: number
          - `half_metallic`:
            - `type`: boolean
        - `required`: `name`, `half_metallic`, `Ba_moment`, `C_moment`
  - `required`: `bulk`, `surfaces`, `interfaces`

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_04_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "bulk": {
            "type": "object",
            "properties": {
              "Ba_moment": {
                "type": "number"
              },
              "C_moment": {
                "type": "number"
              }
            },
            "required": [
              "Ba_moment",
              "C_moment"
            ]
          },
          "surfaces": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "Ba_moment": {
                  "type": "number"
                },
                "C_moment": {
                  "type": "number"
                },
                "half_metallic": {
                  "type": "boolean"
                },
                "majority_gap": {
                  "type": "number"
                }
              },
              "required": [
                "name",
                "half_metallic",
                "majority_gap"
              ]
            }
          },
          "interfaces": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {
                  "type": "string"
                },
                "Ba_moment": {
                  "type": "number"
                },
                "C_moment": {
                  "type": "number"
                },
                "half_metallic": {
                  "type": "boolean"
                }
              },
              "required": [
                "name",
                "half_metallic",
                "Ba_moment",
                "C_moment"
              ]
            }
          }
        },
        "required": [
          "bulk",
          "surfaces",
          "interfaces"
        ]
      },
      "description": "Contains computed magnetic moments (μB), half-metallicity booleans, and majority-spin energy gaps (eV) for bulk, three surface terminations, and four interface terminations."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by a hidden automated verifier. The verifier reads the `step_04_results.json` file you produce. It compares your reported magnetic moments, half-metallicity booleans, and majority-spin gaps to hidden reference values (derived from the original study) using element-wise tolerances appropriate for DFT re-runs with different implementations. Each quantity (bulk magnetic moments, surface values, interface values) contributes a weighted share to the total score. A correct half-metallicity verdict and accurate moments and gaps will earn high scores; significant deviations or missing values will reduce it. The exact tolerances and weights are not disclosed, but your results should be consistent with a faithful reproduction of the described DFT workflow.
