# Lattice Energy and Hirshfeld Surface Analysis of Two Crystal Structures

## Problem background
Dimethyldimethoxysilane (1Si) and 2,2-dimethoxypropane (1C) are small, rigid molecules that differ only in the central atom — silicon versus carbon. Both were crystallized and their crystal structures determined by X-ray diffraction, yet they adopt different space groups and packing arrangements. To assess whether the two packing motifs could interconvert by isomorphous substitution, one must quantify the relative stability of each real crystal and of hypothetical swapped packings in which a molecule is forced into the packing pattern of its heteroanalogue. This task requires computing lattice energies, formation energies, molecular volumes, and Hirshfeld surface areas for the experimental structures, the fully optimized crystals, and the isomorphously substituted models, and comparing the resulting energetic and geometric trends.

## Approach
The computational strategy combines periodic density functional theory (DFT) with Hirshfeld surface analysis. The DFT calculations use the hybrid PBE0 functional with Grimme's D3 dispersion correction and a triple-zeta basis set. For each compound, three sets of DFT optimizations are performed: (i) geometry optimization of the atomic positions with the experimental unit cell parameters held fixed; (ii) full optimization of both atomic coordinates and lattice parameters; and (iii) optimization of the isolated molecule in the gas phase. From these runs, lattice energies (crystal minus frozen-molecule energy) and formation energies (optimized crystal minus optimized isolated molecule energy, including basis-set superposition error and zero-point vibrational corrections) are derived. Hirshfeld surface analysis, carried out on the experimental and optimized geometries, yields molecular surface areas and volumes and serves as input to estimate the packing efficiency via the lattice-energy-to-surface-area ratio. The same protocol is applied to two artificially constructed swapped-structure models, 1Si[1C] and 1C[1Si], created by replacing the central atom and adjusting bond lengths in the crystal structure of the other compound. Comparing the energies and surface ratios across all conditions reveals whether an isomorphous substitution is energetically competitive.

## Reproduction target
Produce a single JSON file, `/app/outputs/table1_results.json`, that contains the derived lattice energy (Elatt), formation energy (Eform), molecular volume, Hirshfeld surface area (HS_area), and the ratio Elatt/HS_area for both compounds under each of the evaluated conditions: the experimental crystal structure (exp), the fully DFT-optimized crystal (DFT), and the isomorphously substituted packing (DFT in [1C] for 1Si, DFT in [1Si] for 1C). All values must be computed from the raw DFT energies and Hirshfeld surface data following the workflow steps, and they must be reported in the specified units (kcal/mol for energies, Å³ for volume, Å² for area, kcal mol⁻¹ Å⁻² for the ratio).

## Assets

- Crystal structures of 1Si and 1C (CCDC 1903036–1903038): https://www.ccdc.cam.ac.uk/structures/
- Open-source periodic DFT code: CP2K or Quantum ESPRESSO
- Hirshfeld surface analysis tool: Multiwfn, CrystalExplorer, or equivalent

## Workflow steps

### Step 1: Hirshfeld surface analysis of experimental structures
- Role: process
- Action: Download the crystal structures (CCDC 1903036–1903038). Compute the Hirshfeld surface areas and molecular volumes for 1Si and 1C using the experimental geometries. Save the resulting HS areas and volumes as a JSON evidence file.
- Evidence: `/app/outputs/hirshfeld_exp.json`

### Step 2: DFT optimization of real crystals and isolated molecules
- Role: process
- Action: Perform periodic DFT calculations with PBE0-D3/triple-zeta for 1Si and 1C: (a) geometry optimization with experimental unit cell parameters fixed; (b) full geometry optimization (atoms + cell); (c) optimization of isolated molecules. Compute total energies, apply BSSE and ZPE corrections. Store raw energies and optimized geometries in a JSON evidence file.
- Evidence: `/app/outputs/dft_raw.json`

### Step 3: DFT optimization of isomorphous substitution models
- Role: process
- Action: Create swapped models 1Si[1C] and 1C[1Si] by replacing the central atom and adjusting bond lengths appropriately. Perform full periodic DFT geometry optimization for each model. Compute total energies, BSSE and ZPE corrections. Save raw energies and optimized geometries in a JSON evidence file.
- Evidence: `/app/outputs/dft_swapped.json`

### Step 4: Assemble Table 1 output
- Role: scored (load-bearing)
- Action: Combine the Hirshfeld surface data and the DFT energy results to compute the final values: Elatt, Eform, Volume, HS area, and Elatt/HS ratio for each condition (experimental, optimized, swapped models). Write the aggregated table to /app/outputs/table1_results.json.
- Output file: `/app/outputs/table1_results.json`
- Format: json
- Contract: JSON object with two top-level keys '1Si' and '1C'. Each maps to an object containing sub-keys 'exp', 'DFT', and for 1Si also 'DFT in [1C]' and for 1C also 'DFT in [1Si]'. Each sub-key is an object with fields: 'Elatt' (float, kcal/mol), 'Eform' (float, kcal/mol), 'Volume' (float, Å³), 'HS_area' (float, Å²), 'Elatt_HS_ratio' (float, kcal mol⁻¹ Å⁻²).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table1_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table1_results.json
- path: `/app/outputs/table1_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final result table with lattice energies, formation energies, volumes, Hirshfeld surface areas, and energy/area ratios for 1Si and 1C, as in Table 1 of the paper.
- schema:
  - `type`: object
  - `required`: `1Si`, `1C`
  - `properties`:
    - `1Si`:
      - `type`: object
      - `required`: `exp`, `DFT`, `DFT in [1C]`
      - `properties`:
        - `exp`:
          - `type`: object
          - `required`: `Elatt`, `Eform`, `Volume`, `HS_area`, `Elatt_HS_ratio`
        - `DFT`:
          - `type`: object
          - `required`: `Elatt`, `Eform`, `Volume`, `HS_area`, `Elatt_HS_ratio`
        - `DFT in [1C]`:
          - `type`: object
          - `required`: `Elatt`, `Eform`, `Volume`, `HS_area`, `Elatt_HS_ratio`
    - `1C`:
      - `type`: object
      - `required`: `exp`, `DFT`, `DFT in [1Si]`
      - `properties`:
        - `exp`:
          - `type`: object
          - `required`: `Elatt`, `Eform`, `Volume`, `HS_area`, `Elatt_HS_ratio`
        - `DFT`:
          - `type`: object
          - `required`: `Elatt`, `Eform`, `Volume`, `HS_area`, `Elatt_HS_ratio`
        - `DFT in [1Si]`:
          - `type`: object
          - `required`: `Elatt`, `Eform`, `Volume`, `HS_area`, `Elatt_HS_ratio`
  - `units`:
    - `Elatt`: kcal/mol
    - `Eform`: kcal/mol
    - `Volume`: Å³
    - `HS_area`: Å²
    - `Elatt_HS_ratio`: kcal mol⁻¹ Å⁻²

Notes: The checker compares each numeric field against the paper's reported values using absolute tolerances (0.5 kcal/mol for energies, 5 Å³ for volume, 5 Å² for HS area, 0.005 for ratios) and verifies relative trends and self-consistency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table1_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "1Si",
          "1C"
        ],
        "properties": {
          "1Si": {
            "type": "object",
            "required": [
              "exp",
              "DFT",
              "DFT in [1C]"
            ],
            "properties": {
              "exp": {
                "type": "object",
                "required": [
                  "Elatt",
                  "Eform",
                  "Volume",
                  "HS_area",
                  "Elatt_HS_ratio"
                ]
              },
              "DFT": {
                "type": "object",
                "required": [
                  "Elatt",
                  "Eform",
                  "Volume",
                  "HS_area",
                  "Elatt_HS_ratio"
                ]
              },
              "DFT in [1C]": {
                "type": "object",
                "required": [
                  "Elatt",
                  "Eform",
                  "Volume",
                  "HS_area",
                  "Elatt_HS_ratio"
                ]
              }
            }
          },
          "1C": {
            "type": "object",
            "required": [
              "exp",
              "DFT",
              "DFT in [1Si]"
            ],
            "properties": {
              "exp": {
                "type": "object",
                "required": [
                  "Elatt",
                  "Eform",
                  "Volume",
                  "HS_area",
                  "Elatt_HS_ratio"
                ]
              },
              "DFT": {
                "type": "object",
                "required": [
                  "Elatt",
                  "Eform",
                  "Volume",
                  "HS_area",
                  "Elatt_HS_ratio"
                ]
              },
              "DFT in [1Si]": {
                "type": "object",
                "required": [
                  "Elatt",
                  "Eform",
                  "Volume",
                  "HS_area",
                  "Elatt_HS_ratio"
                ]
              }
            }
          }
        },
        "units": {
          "Elatt": "kcal/mol",
          "Eform": "kcal/mol",
          "Volume": "Å³",
          "HS_area": "Å²",
          "Elatt_HS_ratio": "kcal mol⁻¹ Å⁻²"
        }
      },
      "description": "Final result table with lattice energies, formation energies, volumes, Hirshfeld surface areas, and energy/area ratios for 1Si and 1C, as in Table 1 of the paper."
    }
  ],
  "notes": "The checker compares each numeric field against the paper's reported values using absolute tolerances (0.5 kcal/mol for energies, 5 Å³ for volume, 5 Å² for HS area, 0.005 for ratios) and verifies relative trends and self-consistency."
}
```

## How you are scored
A hidden verifier will independently evaluate each required output artifact. For the scored file `table1_results.json`, the verifier compares the submitted numerical fields against a hidden reference dataset derived from the paper's reported values. The comparison checks both absolute agreement within defined tolerances and the consistency of relative trends among the different conditions (e.g., the ordering of lattice energies between 1Si and 1C, or the relative stability of the swapped versus original packings). Additionally, a self-consistency check verifies that the reported Elatt/HS_area equals Elatt divided by HS_area. Each checkpoint is weighted, and the combined score determines your final reward. Simply memorizing the paper's numbers is not sufficient; you must genuinely execute the computational workflow and derive the values from the raw DFT and Hirshfeld surface analysis outputs.
