# DFT Water Adsorption on ZnO Surface: Binding Energies and Geometries

## Problem background
Water adsorption on zinc oxide (ZnO) surfaces is central to humidity sensing, because the interaction between water molecules and the ZnO film determines sensor response. A key open question is whether water adsorbs via weak physisorption or stronger chemisorption, and how the binding energy changes when multiple water molecules are present. This task uses density functional theory (DFT) to compute the binding energies of 1, 4, and 10 water molecules on a ZnO(0001) slab, along with the O–Zn distance, H–O distance, and net charge transfer for a single adsorbed water molecule. The computed quantities will reveal the adsorption mechanism and the coverage dependence of the binding energy.

## Approach
The computational approach models the ZnO(0001) surface as a periodically repeated slab. A [5×3] supercell with two atomic layers is constructed; the bottom layer is fixed at bulk positions and a vacuum gap is added. Spin‑polarized DFT calculations with the Perdew–Burke–Ernzerhof (PBE) generalized gradient approximation and a suitable open‑source code are employed. Geometry optimizations are performed for the bare slab and, separately, for systems with 1, 4, and 10 water molecules placed near surface Zn atoms. In each adsorption geometry the top ZnO layer and all water molecules are allowed to relax while the bottom layer stays fixed. Total energies of the combined systems, the isolated slab, and an isolated water molecule are computed. For each coverage the total binding energy is obtained as E_slab+water − E_slab − n·E_H2O, and the average binding energy per molecule follows. For the single‑water case, the O(water)–Zn(surface) distance, the shortest H(water)–O(surface) distance, and the net charge transfer (via Hirshfeld or Mulliken population analysis) are extracted.

## Reproduction target
Produce a single JSON file, adsorption_results.json, containing the following computed quantities:
- For 1 water molecule (key `'1_WM'`): `total_binding_energy_eV` (float), `avg_binding_energy_eV` (float), `O_Zn_distance_Angstrom` (float), `H_O_distance_Angstrom` (float), `charge_transfer_e` (float).
- For 4 water molecules (key `'4_WM'`): `total_binding_energy_eV` (float), `avg_binding_energy_eV` (float).
- For 10 water molecules (key `'10_WM'`): `total_binding_energy_eV` (float), `avg_binding_energy_eV` (float).
All energies in electronvolts, distances in Ångström, charge in elementary charge.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K): https://www.quantum-espresso.org/
- ZnO wurtzite crystal structure: https://materialsproject.org/materials/mp-2133

## Workflow steps

### Step 1: ZnO slab construction and geometry optimization
- Role: process
- Action: Build a [5×3] supercell of the ZnO(0001) surface with a 10 Å vacuum gap using a two-layer slab (42 Zn and 42 O atoms). Fix the bottom layer at bulk positions. Perform a spin-polarized DFT geometry optimization to obtain the relaxed slab.
- Evidence: `/app/outputs/slab_opt.log`

### Step 2: Geometry optimization of water adsorption configurations
- Role: process
- Action: On the optimized ZnO slab, place 1, 4, and 10 H2O molecules with reasonable initial positions (e.g., near surface Zn sites). For each coverage, perform geometry optimization allowing the top ZnO layer and all water molecules to relax. Keep the bottom ZnO layer fixed. Retain the optimized structures for subsequent analysis.
- Evidence: `/app/outputs/water_geom_opt.log`

### Step 3: Compute adsorption energies and properties
- Role: scored (load-bearing)
- Action: Using the optimized structures and isolated slab/water references, calculate total energies and derive the total binding energy and average binding energy per molecule for each coverage. For the 1-H2O case, extract the O(water)–Zn(surface) distance, the shortest H(water)–O(surface) distance, and the net charge transfer (e.g., Hirshfeld or Mulliken population analysis). Write all results to adsorption_results.json.
- Output file: `/app/outputs/adsorption_results.json`
- Format: json
- Contract: JSON object with keys '1_WM', '4_WM', '10_WM'. Each key maps to an object with 'total_binding_energy_eV' (float), 'avg_binding_energy_eV' (float). The '1_WM' object additionally contains 'O_Zn_distance_Angstrom' (float), 'H_O_distance_Angstrom' (float), 'charge_transfer_e' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_results.json
- path: `/app/outputs/adsorption_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Computed DFT adsorption properties: total and average binding energies for 1, 4, 10 water molecules, and for the single-water case O-Zn distance, H-O distance, and charge transfer.
- schema:
  - `type`: object
  - `required`: `1_WM`, `4_WM`, `10_WM`
  - `properties`:
    - `1_WM`:
      - `type`: object
      - `required`: `total_binding_energy_eV`, `avg_binding_energy_eV`, `O_Zn_distance_Angstrom`, `H_O_distance_Angstrom`, `charge_transfer_e`
      - `properties`:
        - `total_binding_energy_eV`:
          - `type`: number
        - `avg_binding_energy_eV`:
          - `type`: number
        - `O_Zn_distance_Angstrom`:
          - `type`: number
        - `H_O_distance_Angstrom`:
          - `type`: number
        - `charge_transfer_e`:
          - `type`: number
    - `4_WM`:
      - `type`: object
      - `required`: `total_binding_energy_eV`, `avg_binding_energy_eV`
      - `properties`:
        - `total_binding_energy_eV`:
          - `type`: number
        - `avg_binding_energy_eV`:
          - `type`: number
    - `10_WM`:
      - `type`: object
      - `required`: `total_binding_energy_eV`, `avg_binding_energy_eV`
      - `properties`:
        - `total_binding_energy_eV`:
          - `type`: number
        - `avg_binding_energy_eV`:
          - `type`: number

Notes: The agent must use an open-source DFT code with PBE functional; small systematic shifts from the reference are absorbed by tolerances. The checker compares reported values to hidden paper-reported gold with appropriate tolerances and also checks coverage independence of average binding energy.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "1_WM",
          "4_WM",
          "10_WM"
        ],
        "properties": {
          "1_WM": {
            "type": "object",
            "required": [
              "total_binding_energy_eV",
              "avg_binding_energy_eV",
              "O_Zn_distance_Angstrom",
              "H_O_distance_Angstrom",
              "charge_transfer_e"
            ],
            "properties": {
              "total_binding_energy_eV": {
                "type": "number"
              },
              "avg_binding_energy_eV": {
                "type": "number"
              },
              "O_Zn_distance_Angstrom": {
                "type": "number"
              },
              "H_O_distance_Angstrom": {
                "type": "number"
              },
              "charge_transfer_e": {
                "type": "number"
              }
            }
          },
          "4_WM": {
            "type": "object",
            "required": [
              "total_binding_energy_eV",
              "avg_binding_energy_eV"
            ],
            "properties": {
              "total_binding_energy_eV": {
                "type": "number"
              },
              "avg_binding_energy_eV": {
                "type": "number"
              }
            }
          },
          "10_WM": {
            "type": "object",
            "required": [
              "total_binding_energy_eV",
              "avg_binding_energy_eV"
            ],
            "properties": {
              "total_binding_energy_eV": {
                "type": "number"
              },
              "avg_binding_energy_eV": {
                "type": "number"
              }
            }
          }
        }
      },
      "description": "Computed DFT adsorption properties: total and average binding energies for 1, 4, 10 water molecules, and for the single-water case O-Zn distance, H-O distance, and charge transfer."
    }
  ],
  "notes": "The agent must use an open-source DFT code with PBE functional; small systematic shifts from the reference are absorbed by tolerances. The checker compares reported values to hidden paper-reported gold with appropriate tolerances and also checks coverage independence of average binding energy."
}
```

## How you are scored
Your submission is scored by an automated verifier that reads your `adsorption_results.json`. It compares each numerical quantity against hidden reference expectations. The closer your computed binding energies, distances, and charge transfer are to the expected values, the higher your score. The verifier also checks whether the three average binding energies (for 1, 4, and 10 water molecules) are mutually consistent. The final score is a weighted combination of these checks. Simply reporting the paper’s numbers is not sufficient; you must perform the DFT calculations to generate the values.
