# Bulk and Surface Magnetic Properties of α- and γ-Ce via DFT+U

## Problem background
Cerium exists in two isostructural face-centred cubic (fcc) phases: α-Ce (smaller lattice constant, bulk non-magnetic with itinerant 4f electrons) and γ-Ce (larger lattice constant, bulk magnetic with localized 4f electrons). While experiments and earlier calculations have shown that the (111) surface of α-Ce can be magnetically ordered, the magnetic state of the γ-Ce(111) surface is less well characterised. This task reproduces a density functional theory (DFT) investigation into the magnetic properties of both α-Ce(111) and γ-Ce(111) surfaces.

## Approach
The computational approach uses plane-wave DFT with the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional, spin polarization, and spin-orbit coupling. Strong on-site Coulomb repulsion among Ce 4f electrons is treated with a Hubbard U correction (DFT+U) applied only to the γ-Ce phase. First, equilibrium lattice constants and total magnetic moments are computed for bulk α-Ce and γ-Ce to validate the chosen computational parameters. Using these bulk lattice constants, symmetric slab supercells of 5 Ce(111) layers separated by vacuum are built for each phase. The slab calculations then yield layer-resolved spin and orbital magnetic moments, enabling the magnetic state of each surface to be determined.

## Reproduction target
The objective is to compute, from first principles using the specified DFT setup, the equilibrium lattice constants and total magnetic moments per atom for bulk α-Ce and γ-Ce, and the layer-resolved spin and orbital magnetic moments for 5-layer (111) slabs of both phases. Based on the computed moments, determine whether each slab's layers exhibit a non-negligible magnetic moment (magnetically ordered surface) or essentially zero magnetic moment (magnetically dead layers).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Ce PAW pseudopotential (Ce.pbe-spn-kjpaw_psl.1.0.0.UPF): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Bulk DFT Validation
- Role: scored
- Action: Using Quantum ESPRESSO with PBE-GGA, spin polarization, spin-orbit coupling, and Hubbard U = 4.4 eV on Ce 4f states (only for γ-Ce), compute equilibrium lattice constants and total magnetic moments per atom for fcc α-Ce and γ-Ce. Write results to step_01_bulk_properties.json.
- Output file: `/app/outputs/step_01_bulk_properties.json`
- Format: json
- Contract: {"alpha-Ce": {"lattice_constant_angstrom": float, "total_magnetic_moment_muB": float}, "gamma-Ce": {"lattice_constant_angstrom": float, "total_magnetic_moment_muB": float}}
- Scoring: scored by hidden verifier

### Step 2: Surface Slab Construction
- Role: process
- Action: Using the optimized bulk lattice parameters from step_01, build symmetric supercells for α-Ce(111) and γ-Ce(111) surfaces containing 5 Ce layers and 25 bohr of vacuum. Prepare the necessary input files for subsequent DFT calculations.
- Evidence: none

### Step 3: Surface Magnetic Moment Extraction
- Role: scored (load-bearing)
- Action: Perform DFT+SP+SO+U calculations on the slab models, relaxing forces to <1 mRy/bohr. Extract spin and orbital magnetic moments per atom for each layer (1 to 5) and compute total magnetic moment per atom. Write results to step_02_surface_moments.csv.
- Output file: `/app/outputs/step_02_surface_moments.csv`
- Format: csv
- Contract: Columns: phase (string), layer (int 1..5), spin_moment_muB (float), orbital_moment_muB (float), total_moment_muB (float). Two tables (one per phase), each with 5 rows. Only the output schema is described; no thresholds are disclosed.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bulk_properties.json`
- `/app/outputs/step_02_surface_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bulk_properties.json
- path: `/app/outputs/step_01_bulk_properties.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Bulk equilibrium lattice constants and total magnetic moments per atom for α-Ce and γ-Ce, used to validate the DFT setup.
- schema:
  - `type`: object
  - `required`: `alpha-Ce`, `gamma-Ce`
  - `properties`:
    - `alpha-Ce`:
      - `type`: object
      - `required`: `lattice_constant_angstrom`, `total_magnetic_moment_muB`
      - `properties`:
        - `lattice_constant_angstrom`:
          - `type`: number
          - `unit`: angstrom
        - `total_magnetic_moment_muB`:
          - `type`: number
          - `unit`: muB
    - `gamma-Ce`:
      - `type`: object
      - `required`: `lattice_constant_angstrom`, `total_magnetic_moment_muB`
      - `properties`:
        - `lattice_constant_angstrom`:
          - `type`: number
          - `unit`: angstrom
        - `total_magnetic_moment_muB`:
          - `type`: number
          - `unit`: muB

### step_02_surface_moments.csv
- path: `/app/outputs/step_02_surface_moments.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Layer-resolved spin, orbital, and total magnetic moments for α-Ce(111) and γ-Ce(111) slabs. The checker compares the trend against a hidden reference without disclosing thresholds.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `layer`, `spin_moment_muB`, `orbital_moment_muB`, `total_moment_muB`
  - `units`:
    - `spin_moment_muB`: muB
    - `orbital_moment_muB`: muB
    - `total_moment_muB`: muB
  - `note`: Exactly 10 rows (5 layers each for alpha-Ce and gamma-Ce). Phase values: 'alpha-Ce' and 'gamma-Ce'. Layer integers 1 through 5.

Notes: All output files must be placed under /app/outputs/. The solver must fetch and use the open‑source code Quantum ESPRESSO and the specified pseudopotential. No proprietary code or data is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bulk_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "alpha-Ce",
          "gamma-Ce"
        ],
        "properties": {
          "alpha-Ce": {
            "type": "object",
            "required": [
              "lattice_constant_angstrom",
              "total_magnetic_moment_muB"
            ],
            "properties": {
              "lattice_constant_angstrom": {
                "type": "number",
                "unit": "angstrom"
              },
              "total_magnetic_moment_muB": {
                "type": "number",
                "unit": "muB"
              }
            }
          },
          "gamma-Ce": {
            "type": "object",
            "required": [
              "lattice_constant_angstrom",
              "total_magnetic_moment_muB"
            ],
            "properties": {
              "lattice_constant_angstrom": {
                "type": "number",
                "unit": "angstrom"
              },
              "total_magnetic_moment_muB": {
                "type": "number",
                "unit": "muB"
              }
            }
          }
        }
      },
      "description": "Bulk equilibrium lattice constants and total magnetic moments per atom for α-Ce and γ-Ce, used to validate the DFT setup."
    },
    {
      "file": "step_02_surface_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "layer",
          "spin_moment_muB",
          "orbital_moment_muB",
          "total_moment_muB"
        ],
        "units": {
          "spin_moment_muB": "muB",
          "orbital_moment_muB": "muB",
          "total_moment_muB": "muB"
        },
        "note": "Exactly 10 rows (5 layers each for alpha-Ce and gamma-Ce). Phase values: 'alpha-Ce' and 'gamma-Ce'. Layer integers 1 through 5."
      },
      "description": "Layer-resolved spin, orbital, and total magnetic moments for α-Ce(111) and γ-Ce(111) slabs. The checker compares the trend against a hidden reference without disclosing thresholds."
    }
  ],
  "notes": "All output files must be placed under /app/outputs/. The solver must fetch and use the open‑source code Quantum ESPRESSO and the specified pseudopotential. No proprietary code or data is required."
}
```

## How you are scored
A hidden verifier independently evaluates each scored output file. Your submitted bulk lattice constants and magnetic moments in `step_01_bulk_properties.json` are compared against a reference computed with the same DFT code and functional. For the surface results in `step_02_surface_moments.csv`, the verifier checks whether the layer-resolved total magnetic moments satisfy the physical expectations for the two phases derived from the reference calculation. The final reward is a weighted combination of the bulk and surface scores; merely writing plausible numbers is insufficient.
