# Surface segregation energy analysis of Cr in Fe(100) slabs using DFT

## Problem background
Fe-Cr ferritic steels with low Cr concentration are candidate structural materials for nuclear applications, and the segregation of Cr from the bulk to the surface affects key properties such as corrosion resistance. In this task we probe the energetic landscape of a single Cr atom substituting Fe in a Fe(100) slab. We investigate how the solution energy of Cr depends on the layer position — topmost surface (S), subsurface (S‑1), sub-subsurface (S‑2), and central (bulk-like) layer — and extract the corresponding segregation energies relative to the central layer. The goal is to reveal whether any layer exhibits a qualitatively different solution energy that would control the segregation barrier.

## Approach
We employ spin-polarized density functional theory (DFT) with plane-wave basis and the Projector Augmented Wave (PAW) method, using the GGA‑PW91 exchange‑correlation functional. Bulk reference calculations for ferromagnetic bcc Fe and antiferromagnetic bcc Cr provide per‑atom total energies and the Fe lattice constant to build the slab models. Periodic Fe(100) slabs are constructed with a 2×2 surface cell, 9 atomic layers, and a vacuum region of 4 times the lattice constant. A pure Fe slab and four Cr‑doped slabs are created: a single Cr atom is placed substitutionally in the S, S‑1, S‑2, or central layer, using mirror symmetry along the surface normal so that two Cr atoms are present (except in the central layer, which contains only one Cr). All slab geometries are fully relaxed. From the converged total energies we compute solution energies using the standard definitions that involve the total energies of the doped slab, the pure Fe slab, and the bulk elemental references. For layers with two Cr atoms the solution energy per Cr is obtained from the energy difference of the slab with two Cr and the pure slab, corrected by the reference energies of Fe and Cr; for the central layer, which hosts a single Cr, the analogous expression is applied. Segregation energies are then defined as the difference between the solution energy at a given layer and that at the central layer. The Cr magnetic moment at each layer is also extracted from the relaxed electronic structure.

## Reproduction target
The target is to compute, for the S, S‑1, S‑2, and central layers of the Fe(100) slab, the following quantities:
- the solution energy per Cr atom (in eV),
- the segregation energy relative to the central layer (in eV), and
- the Cr magnetic moment (in μ_B).
These results, together with the raw DFT total energies of all slab and bulk systems, must be written to the two CSV files specified in the output contract. The workflow produces the primary artifacts `raw_total_energies.csv` and `solution_energies.csv`; no other scored outputs are required. The hidden verifier will compare the derived segregation energies and magnetic moments to the expected physical behaviour without disclosing the expected values or trends.

## Assets

- Quantum ESPRESSO plane-wave DFT code with PAW and GGA-PW91 support: https://www.quantum-espresso.org
- SSSP efficiency pseudopotentials (PAW, PW91) for Fe and Cr: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT reference calculations for bulk Fe and bulk Cr
- Role: process
- Action: Perform spin-polarized DFT calculations for bulk ferromagnetic bcc Fe and bulk antiferromagnetic bcc Cr to obtain equilibrium lattice constants and total energies per atom.
- Evidence: `/app/outputs/bulk_reference.log`

### Step 2: Slab model construction
- Role: process
- Action: Construct periodic slab models for the Fe(100) surface with a 2×2 cell, 9 atomic layers, and 4a vacuum. Build a pure Fe slab and slabs with one Cr atom substitutionally placed in the S, S-1, S-2, and central layers, using mirror symmetry to include two Cr atoms except in the central layer.
- Evidence: `/app/outputs/slab_setup.log`

### Step 3: DFT relaxations of slab models
- Role: process
- Action: Run spin-polarized DFT geometry relaxations for all slab configurations (pure Fe, Cr in S, S-1, S-2, central). Fully relax atomic positions, record total energies, relaxed coordinates, and site magnetic moments.
- Evidence: `/app/outputs/relax_output.log`

### Step 4: Collect total energies
- Role: scored (load-bearing)
- Action: Extract the total energies from the DFT outputs for all systems (Fe_slab, Fe_slab_Cr_S, Fe_slab_Cr_Sm1, Fe_slab_Cr_Sm2, Fe_slab_Cr_central, Fe_bulk, Cr_bulk) and write them to raw_total_energies.csv.
- Output file: `/app/outputs/raw_total_energies.csv`
- Format: csv
- Contract: system_name (string), total_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 5: Calculate solution and segregation energies
- Role: scored
- Action: Using the raw total energies and the formulas for solution energy (E_sol) for layers with one or two Cr atoms, compute E_sol for the S, S-1, S-2, and central layers. Compute segregation energies (E_seg) relative to the central layer. Extract the Cr magnetic moment (m_cr_muB) for each layer from the DFT outputs. Write the results to solution_energies.csv.
- Output file: `/app/outputs/solution_energies.csv`
- Format: csv
- Contract: layer (string: S/S-1/S-2/central), e_sol_eV (float), e_seg_eV (float), m_cr_muB (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/raw_total_energies.csv`
- `/app/outputs/solution_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### raw_total_energies.csv
- path: `/app/outputs/raw_total_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw DFT total energies for all slab and bulk configurations. The checker uses this file to recompute solution and segregation energies.
- schema:
  - `type`: table
  - `required_columns`: `system_name`, `total_energy_eV`
  - `units`:
    - `total_energy_eV`: eV

### solution_energies.csv
- path: `/app/outputs/solution_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Derived solution energies, segregation energies, and Cr magnetic moments for the S, S-1, S-2, and central layers. The checker verifies the segregation energies against reference values and checks sign conditions.
- schema:
  - `type`: table
  - `required_columns`: `layer`, `e_sol_eV`, `e_seg_eV`, `m_cr_muB`
  - `units`:
    - `e_sol_eV`: eV
    - `e_seg_eV`: eV
    - `m_cr_muB`: μ_B

Notes: Both CSV files must be comma-separated with a header row. The raw_total_energies.csv must contain exactly seven rows: Fe_slab, Fe_slab_Cr_S, Fe_slab_Cr_Sm1, Fe_slab_Cr_Sm2, Fe_slab_Cr_central, Fe_bulk, Cr_bulk. solution_energies.csv must contain four rows for layers S, S-1, S-2, and central.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "raw_total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "system_name",
          "total_energy_eV"
        ],
        "units": {
          "total_energy_eV": "eV"
        }
      },
      "description": "Raw DFT total energies for all slab and bulk configurations. The checker uses this file to recompute solution and segregation energies."
    },
    {
      "file": "solution_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "layer",
          "e_sol_eV",
          "e_seg_eV",
          "m_cr_muB"
        ],
        "units": {
          "e_sol_eV": "eV",
          "e_seg_eV": "eV",
          "m_cr_muB": "μ_B"
        }
      },
      "description": "Derived solution energies, segregation energies, and Cr magnetic moments for the S, S-1, S-2, and central layers. The checker verifies the segregation energies against reference values and checks sign conditions."
    }
  ],
  "notes": "Both CSV files must be comma-separated with a header row. The raw_total_energies.csv must contain exactly seven rows: Fe_slab, Fe_slab_Cr_S, Fe_slab_Cr_Sm1, Fe_slab_Cr_Sm2, Fe_slab_Cr_central, Fe_bulk, Cr_bulk. solution_energies.csv must contain four rows for layers S, S-1, S-2, and central."
}
```

## How you are scored
A hidden verifier automatically scores your submission after it finishes. The verifier reads your `raw_total_energies.csv` and independently recalculates solution and segregation energies from the raw data, then compares them to the values you report in `solution_energies.csv`. It also checks that the segregation energies and magnetic moments satisfy certain physical relationships that a correct calculation should obey. The final reward is a weighted combination of the scores from each scored artifact; you do not need to know the weights or tolerances. Reporting any particular numerical value is not enough — the verifier evaluates the internal consistency and correctness of the entire computation.
