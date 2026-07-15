# Charge density wave binding energies and structural changes in monolayer TaX2

## Problem background
Transition‑metal dichalcogenide (TMD) monolayers can form a variety of charge density wave (CDW) states, where the lattice distorts from the high‑symmetry structure and the electronic charge redistributes. These CDW instabilities are intimately coupled to metal–insulator transitions and superconductivity. Density functional theory (DFT) is a workhorse for predicting the relative stability of competing CDW phases and the associated structural rearrangements. This task focuses on computing, from first principles, the CDW binding energies and the Ta–Ta bond‑length changes in monolayer TaS₂, TaSe₂, and TaTe₂ across the 1T and 1H polytypes, providing a quantitative benchmark of current open‑source DFT codes for layered chalcogenides.

## Approach
The computational protocol has four stages: (1) Optimise the in‑plane lattice parameter and ionic positions of the high‑symmetry 1T and 1H primitive cells of TaS₂, TaSe₂, and TaTe₂ using the local‑density approximation (LDA) functional; then evaluate the ground‑state total energy of each optimised geometry with the GGA‑PBE functional. Record the total energies, lattice constants, and the nearest‑neighbor Ta–Ta distance of each high‑symmetry structure. (2) For each chalcogen (S, Se, Te) and each polytype (1T, 1H), construct the 3×1, 4×1, 3×3 and √13×√13 supercells. Introduce small random in‑plane displacements (≈1‑3% of the lattice spacing) to all Ta atoms, then perform a fixed‑cell ionic relaxation with LDA. Afterwards evaluate the GGA‑PBE energy of the relaxed CDW structure and record the final cell volume and atomic coordinates. (3) From the high‑symmetry and CDW energies compute the CDW binding energy per formula unit (meV, defined so a positive value means the CDW is lower in energy than the high‑symmetry reference) and the fractional cell‑volume change CV (%) of the CDW supercell relative to the corresponding high‑symmetry supercell. (4) For the relaxed 1T CDW structures, extract all unique nearest‑ and next‑nearest‑neighbor Ta–Ta distances (Å) and compute their percent change relative to the high‑symmetry Ta–Ta distance of the same compound.

## Reproduction target
For every combination of chalcogenide (S, Se, Te), polytype (1T, 1H) and CDW supercell (3×1, 4×1, 3×3, √13×√13) that yields a stable CDW (binding energy greater than roughly 1 meV/f.u.), report the CDW binding energy (meV per formula unit) and the cell‑volume change (CV, %) in a JSON file named `CDW_binding_energies.json`. For the 1T CDW structures where the Ta‑atom displacement exceeds about 1% of the high‑symmetry Ta–Ta distance, extract all unique Ta–Ta neighbor distances (Å) and their percent changes, and write them to a JSON file named `Ta_Ta_distances.json`. The exact formats are given in the workflow steps below.

## Assets

- Open-source DFT code (e.g., Quantum ESPRESSO, CP2K, or ABINIT): https://www.quantum-espresso.org/
- Pseudopotentials for Ta, S, Se, Te (e.g., SSSP efficiency or PseudoDojo): https://www.materialscloud.org/discover/sssp/table/pbe/efficiency

## Workflow steps

### Step 1: Compute high-symmetry reference structures and energies
- Role: process
- Action: Optimize lattice parameters and ionic positions of the 1T and 1H primitive cells of TaS2, TaSe2, and TaTe2 using LDA. Evaluate GGA-PBE total energies at the LDA-optimized geometries. Record the total energies, lattice constants, and the nearest-neighbor Ta–Ta distance for each structure.
- Evidence: `/app/outputs/high_symmetry_ref.log`

### Step 2: Relax CDW supercells and compute their total energies
- Role: process
- Action: For each chalcogen (S, Se, Te) and each polytype (1T, 1H), construct the 3x1, 4x1, 3x3, and sqrt13xsqrt13 supercells. Introduce small random in-plane displacements (1–3%) to Ta atoms, then relax ionic positions using LDA with fixed cell. Evaluate GGA-PBE total energy. Record the final unit cell volume and relaxed atomic coordinates.
- Evidence: `/app/outputs/cdw_relaxation.log`

### Step 3: Calculate CDW binding energies and cell volume changes
- Role: scored (load-bearing)
- Action: Compute the CDW binding energy per formula unit (meV) as the difference between high-symmetry and CDW total energies (positive = CDW lower). Compute the fractional cell volume change CV (%) relative to the extrapolated high-symmetry cell. Output results for all CDW cases with binding energy > ~1 meV/f.u.
- Output file: `/app/outputs/CDW_binding_energies.json`
- Format: json
- Contract: Array of objects with keys: polytype (string: "1T"|"1H"), chalcogenide (string: "S"|"Se"|"Te"), supercell (string, e.g. "3x1","4x1","3x3","sqrt13xsqrt13"), binding_energy_meV (float), CV_percent (float).
- Scoring: scored by hidden verifier

### Step 4: Calculate Ta–Ta interatomic distances and percentage changes
- Role: scored
- Action: From the relaxed 1T CDW structures, extract all unique Ta–Ta nearest- and next-nearest-neighbor distances (Å). For each distance compute the percent change relative to the high-symmetry Ta–Ta distance. Output results for CDW structures where the distortion exceeds ~1%.
- Output file: `/app/outputs/Ta_Ta_distances.json`
- Format: json
- Contract: Array of objects with keys: chalcogenide (string: "S"|"Se"|"Te"), supercell (string, e.g. "4x1","sqrt13xsqrt13","3x1","3x3"), site_pair (string, e.g. "AB","BC","CD","AD","AC"), distance_A (float), percent_change (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/CDW_binding_energies.json`
- `/app/outputs/Ta_Ta_distances.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### CDW_binding_energies.json
- path: `/app/outputs/CDW_binding_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: CDW binding energies and cell volume changes; values are compared against hidden gold values from the paper with an appropriate tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `polytype`, `chalcogenide`, `supercell`, `binding_energy_meV`, `CV_percent`
    - `properties`:
      - `polytype`:
        - `type`: string
        - `enum`: `1T`, `1H`
      - `chalcogenide`:
        - `type`: string
        - `enum`: `S`, `Se`, `Te`
      - `supercell`:
        - `type`: string
      - `binding_energy_meV`:
        - `type`: number
      - `CV_percent`:
        - `type`: number

### Ta_Ta_distances.json
- path: `/app/outputs/Ta_Ta_distances.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Ta–Ta interatomic distances and percent changes; values are compared against hidden gold values from the paper with an appropriate tolerance.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `chalcogenide`, `supercell`, `site_pair`, `distance_A`, `percent_change`
    - `properties`:
      - `chalcogenide`:
        - `type`: string
        - `enum`: `S`, `Se`, `Te`
      - `supercell`:
        - `type`: string
      - `site_pair`:
        - `type`: string
      - `distance_A`:
        - `type`: number
      - `percent_change`:
        - `type`: number

Notes: Tolerances and exact gold values are hidden. The checker compares the submitted values to the paper-reported numbers (Tables IV, V, VI) with generous tolerances to account for code and pseudopotential variability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "CDW_binding_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "polytype",
            "chalcogenide",
            "supercell",
            "binding_energy_meV",
            "CV_percent"
          ],
          "properties": {
            "polytype": {
              "type": "string",
              "enum": [
                "1T",
                "1H"
              ]
            },
            "chalcogenide": {
              "type": "string",
              "enum": [
                "S",
                "Se",
                "Te"
              ]
            },
            "supercell": {
              "type": "string"
            },
            "binding_energy_meV": {
              "type": "number"
            },
            "CV_percent": {
              "type": "number"
            }
          }
        }
      },
      "description": "CDW binding energies and cell volume changes; values are compared against hidden gold values from the paper with an appropriate tolerance."
    },
    {
      "file": "Ta_Ta_distances.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "chalcogenide",
            "supercell",
            "site_pair",
            "distance_A",
            "percent_change"
          ],
          "properties": {
            "chalcogenide": {
              "type": "string",
              "enum": [
                "S",
                "Se",
                "Te"
              ]
            },
            "supercell": {
              "type": "string"
            },
            "site_pair": {
              "type": "string"
            },
            "distance_A": {
              "type": "number"
            },
            "percent_change": {
              "type": "number"
            }
          }
        }
      },
      "description": "Ta–Ta interatomic distances and percent changes; values are compared against hidden gold values from the paper with an appropriate tolerance."
    }
  ],
  "notes": "Tolerances and exact gold values are hidden. The checker compares the submitted values to the paper-reported numbers (Tables IV, V, VI) with generous tolerances to account for code and pseudopotential variability."
}
```

## How you are scored
A hidden verifier reads your two JSON artifact files and compares each reported quantity to reference values taken from the published scientific literature. The comparison is performed with generous tolerances that account for systematic differences between DFT codes, pseudopotentials, and numerical convergence settings. In addition, the verifier checks that certain qualitative trends hold—for example, that for each CDW the binding energy increases along the chalcogen series S → Se → Te. The reported values and trend conformities are combined into a single aggregate score between 0 and 1, with the binding‑energy and cell‑volume data carrying the largest weight. Simply providing the paper‑reported numbers without running the DFT workflow is not sufficient; the verification focuses on whether your computed results agree with independent reference data within the allowed tolerance.
