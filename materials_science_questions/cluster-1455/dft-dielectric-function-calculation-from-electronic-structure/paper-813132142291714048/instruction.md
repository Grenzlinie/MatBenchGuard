# DFT calculation of electronic structure and magnetic properties of Fe-doped HfO2

## Problem background
Hafnium oxide (HfO₂) is a high‑κ dielectric that can become a candidate for spin‑based devices when doped with 3d transition metals. Incorporating an Fe dopant into cubic HfO₂ may induce a half‑metallic electronic structure and finite magnetic moment, which are key properties for spintronic applications. Density‑functional theory (DFT) can predict whether such a system exhibits spin‑polarized band features and where the magnetism originates, but the actual half‑metallic character and the size of the magnetic moment must be determined by a thorough computation.

## Approach
Use an open‑source periodic DFT code (e.g., Quantum ESPRESSO) with the PBE exchange‑correlation functional and standard pseudopotentials. Build a 1×1×1 supercell of cubic HfO₂ (space group Fm ‑3m) and substitute one Hf atom by an Fe atom. Perform a spin‑polarized structural relaxation to obtain the equilibrium geometry, then run a self‑consistent field calculation and a subsequent non‑self‑consistent band‑structure run. From the computed band structure and spin‑resolved density of states, extract the majority‑spin band gap, the metallic character of the minority‑spin channel, the total magnetic moment, and the magnetic moment localized on the Fe atom. The procedure follows the typical open‑science DFT pipeline for a substitutionally doped insulator.

## Reproduction target
For a 1×1×1 supercell of cubic HfO₂ with one Hf atom replaced by Fe, perform spin‑polarized DFT structural relaxation, then compute the electronic structure. From the results, report the following four quantities in a JSON file called electronic_results.json:

- majority_band_gap (eV): the energy gap in the majority‑spin channel.
- minority_metallic (boolean): whether the minority‑spin channel has states at the Fermi level.
- total_magnetic_moment (μB): the total magnetic moment of the supercell.
- fe_magnetic_moment (μB): the magnetic moment projected onto the Fe atom.

The calculation must be carried out with an open‑source DFT code and a suitable exchange‑correlation functional; the precise method and convergence parameters are chosen by the solver.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (PBE): https://www.materialscloud.org/discover/sssp/table/pbe

## Workflow steps

### Step 1: Prepare input for Fe-doped HfO₂ supercell
- Role: process
- Action: Generate Quantum ESPRESSO input files (crystal structure, pseudopotentials, k-point mesh, etc.) for a 1×1×1 supercell of cubic HfO₂ (space group Fm ‑3m) with one Hf atom substituted by an Fe atom.
- Evidence: none

### Step 2: Spin-polarized SCF relaxation of Fe-doped HfO₂
- Role: process
- Action: Perform spin-polarized DFT structural relaxation and self-consistent field calculation using Quantum ESPRESSO. Obtain relaxed atomic positions, lattice parameter, and converged spin‑resolved charge density.
- Evidence: `/app/outputs/scf_relaxation.log`

### Step 3: Band structure and partial density of states
- Role: process
- Action: Perform a non‑self‑consistent band‑structure calculation and compute the spin‑resolved total and partial density of states (Fe‑3d, O‑2p, Hf‑5d) using the relaxed structure and charge density from the previous step.
- Evidence: `/app/outputs/pdos_data.dat`

### Step 4: Extract half‑metallic and magnetic properties
- Role: scored (load-bearing)
- Action: Extract from the DFT results the majority‑spin band gap (eV), whether the minority‑spin channel is metallic (states at the Fermi level), the total magnetic moment per supercell (μB), and the magnetic moment on the Fe atom (μB). Write these four quantities to electronic_results.json.
- Output file: `/app/outputs/electronic_results.json`
- Format: json
- Contract: {"majority_band_gap": <float, eV>, "minority_metallic": <boolean>, "total_magnetic_moment": <float, μB>, "fe_magnetic_moment": <float, μB>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electronic_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electronic_results.json
- path: `/app/outputs/electronic_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: DFT‑computed half‑metallic character and magnetic moments of Fe‑doped HfO₂; compared to the paper’s reference values within generous tolerances.
- schema:
  - `type`: object
  - `required`: `majority_band_gap`, `minority_metallic`, `total_magnetic_moment`, `fe_magnetic_moment`
  - `properties`:
    - `majority_band_gap`:
      - `type`: number
      - `unit`: eV
    - `minority_metallic`:
      - `type`: boolean
      - `unit`: 
    - `total_magnetic_moment`:
      - `type`: number
      - `unit`: μB
    - `fe_magnetic_moment`:
      - `type`: number
      - `unit`: μB

Notes: Optical properties are omitted because their numeric reference values are not explicitly reported in the paper, making a valid hidden‑gold check infeasible without fabrication.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electronic_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "majority_band_gap",
          "minority_metallic",
          "total_magnetic_moment",
          "fe_magnetic_moment"
        ],
        "properties": {
          "majority_band_gap": {
            "type": "number",
            "unit": "eV"
          },
          "minority_metallic": {
            "type": "boolean",
            "unit": ""
          },
          "total_magnetic_moment": {
            "type": "number",
            "unit": "μB"
          },
          "fe_magnetic_moment": {
            "type": "number",
            "unit": "μB"
          }
        }
      },
      "description": "DFT‑computed half‑metallic character and magnetic moments of Fe‑doped HfO₂; compared to the paper’s reference values within generous tolerances."
    }
  ],
  "notes": "Optical properties are omitted because their numeric reference values are not explicitly reported in the paper, making a valid hidden‑gold check infeasible without fabrication."
}
```

## How you are scored
A hidden verifier reads your /app/outputs/electronic_results.json and independently compares each field to reference values derived from published results. The verifier checks the majority‑spin band gap and the magnetic moments within generous tolerances that allow for the expected spread between different DFT codes, pseudopotentials, and convergence settings. The minority_metallic flag must be true. Full credit is awarded only when all four checks pass; partial credit is not granted. The verifier does not require exact agreement with any particular code's output, only a physically reasonable numeric match. Simply reporting a number without genuinely running the DFT pipeline will not satisfy the tolerance requirements, because the acceptable ranges are not disclosed.
