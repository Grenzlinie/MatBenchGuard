# Cross-plane tensile deformation of graphene helicoid and multilayer graphene

## Problem background
Multilayer graphene (MLG) and graphene helicoid (GH) are carbon‑based nanostructures that exhibit markedly different mechanical behavior under cross‑plane loading. In MLG the layers are held together only by weak van der Waals forces, so it is expected to fail at relatively low tensile strain. GH, a three‑dimensional helicoidal network of sp²‑bonded carbon, transfers load through covalent bonds and may sustain far larger elastic deformation. Understanding this contrast is important for flexible thermal‑management applications where mechanical robustness under stretching is critical. This task measures the force–strain and strain energy–strain response of both structures under cross‑plane tension at 300 K, and extracts the failure strain of MLG and the maximum sustainable strain of GH.

## Approach
Classical molecular dynamics (MD) simulations are performed with the open‑source LAMMPS package and the AIREBO interatomic potential, which accurately describes both covalent and van der Waals interactions in carbon materials. Atomic models are first constructed: an MLG slab composed of a specified number of graphene layers, and a GH structure with a uniform turn number of 6 and appropriate inner/outer radii. Both models are equilibrated at 300 K. For each structure, a cross‑plane tensile deformation is then applied by moving one end at a low constant velocity while the opposite end is kept fixed; the loading/fixed ends each consist of four adjacent atomic units. Throughout the deformation, the total force and strain energy are recorded as functions of tensile strain. After the simulations are complete, the raw data files are post‑processed to identify the MLG failure strain (the strain corresponding to the peak of the force–strain curve) and the GH maximum sustained strain.

## Reproduction target
Produce force–strain and strain energy–strain curves for both MLG and GH under cross‑plane tensile loading at 300 K. Compute the failure strain of MLG (strain at the maximum of the force–strain curve) and the maximum strain sustained by GH before failure. The target is to verify whether MLG fails at a low strain consistent with expected weak interlayer bonding, and whether the GH structure can maintain structural integrity to extremely large strains.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- AIREBO interatomic potential: Available within LAMMPS when built with the MANYBODY or MOLECULE package
- Python with numpy/pandas: https://pypi.tuna.tsinghua.edu.cn/simple

## Workflow steps

### Step 1: Generate atomic models for MLG and GH
- Role: process
- Action: Construct atomic coordinates for a multilayer graphene (MLG) slab and a graphene helicoid (GH) following the geometric description (helicoid with turn number 6, appropriate dimensions; MLG with corresponding layer count).
- Evidence: `/app/outputs/step0_model_generation.log`

### Step 2: MLG cross‑plane tensile simulation
- Role: scored (load-bearing)
- Action: Equilibrate the MLG model at 300 K, then apply cross‑plane tensile deformation at a low constant velocity with one end fixed and the loading end comprising four adjacent units. Record force and strain energy as functions of tensile strain.
- Output file: `/app/outputs/step_01_mlg_tensile.csv`
- Format: csv
- Contract: columns: strain (dimensionless), force (eV/Å or nN), strain_energy (eV)
- Scoring: scored by hidden verifier

### Step 3: GH cross‑plane tensile simulation
- Role: scored (load-bearing)
- Action: Equilibrate the GH model at 300 K, then apply cross‑plane tensile deformation at a low constant velocity with one end fixed and the loading end comprising four adjacent units. Record force and strain energy as functions of tensile strain.
- Output file: `/app/outputs/step_02_gh_tensile.csv`
- Format: csv
- Contract: columns: strain (dimensionless), force (eV/Å or nN), strain_energy (eV)
- Scoring: scored by hidden verifier

### Step 4: Determine failure strains from raw data
- Role: scored
- Action: Read step_01_mlg_tensile.csv and step_02_gh_tensile.csv. Determine the MLG failure strain as the strain at the peak of the force‑strain curve, and the GH maximum sustained strain. Write a JSON summary.
- Output file: `/app/outputs/step_03_strain_summary.json`
- Format: json
- Contract: object with two numeric keys: 'mlg_failure_strain' and 'gh_max_strain' (both dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_mlg_tensile.csv`
- `/app/outputs/step_02_gh_tensile.csv`
- `/app/outputs/step_03_strain_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_mlg_tensile.csv
- path: `/app/outputs/step_01_mlg_tensile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw force‑strain and strain energy‑strain data for MLG; the checker recomputes the failure strain from this file.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `strain`, `force`, `strain_energy`
  - `units`:
    - `strain`: dimensionless
    - `force`: eV/Å or nN
    - `strain_energy`: eV

### step_02_gh_tensile.csv
- path: `/app/outputs/step_02_gh_tensile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw force‑strain and strain energy‑strain data for GH; the checker recomputes the failure strain from this file.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `strain`, `force`, `strain_energy`
  - `units`:
    - `strain`: dimensionless
    - `force`: eV/Å or nN
    - `strain_energy`: eV

### step_03_strain_summary.json
- path: `/app/outputs/step_03_strain_summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Agent‑reported failure strains; the checker verifies that mlg_failure_strain is near 10% and gh_max_strain exceeds 1200%.
- schema:
  - `type`: object
  - `required`:
    - `mlg_failure_strain`: number
    - `gh_max_strain`: number

Notes: The primary scoring is recomputed from the CSV files; the summary JSON is an auxiliary check. All files must be placed under /app/outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_mlg_tensile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "strain",
          "force",
          "strain_energy"
        ],
        "units": {
          "strain": "dimensionless",
          "force": "eV/Å or nN",
          "strain_energy": "eV"
        }
      },
      "description": "Raw force‑strain and strain energy‑strain data for MLG; the checker recomputes the failure strain from this file."
    },
    {
      "file": "step_02_gh_tensile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "strain",
          "force",
          "strain_energy"
        ],
        "units": {
          "strain": "dimensionless",
          "force": "eV/Å or nN",
          "strain_energy": "eV"
        }
      },
      "description": "Raw force‑strain and strain energy‑strain data for GH; the checker recomputes the failure strain from this file."
    },
    {
      "file": "step_03_strain_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "mlg_failure_strain": "number",
          "gh_max_strain": "number"
        }
      },
      "description": "Agent‑reported failure strains; the checker verifies that mlg_failure_strain is near 10% and gh_max_strain exceeds 1200%."
    }
  ],
  "notes": "The primary scoring is recomputed from the CSV files; the summary JSON is an auxiliary check. All files must be placed under /app/outputs."
}
```

## How you are scored
A hidden verifier reads your submitted CSV files, recomputes the MLG failure strain as the strain at the peak force, and compares it to an expected low‑strain reference band. For GH, the verifier checks that the force–strain data extends to strains far beyond the MLG regime without an early peak, and that the reported maximum strain exceeds a required threshold. The force–strain and strain energy–strain curves must show physically reasonable behavior (force increases monotonically before failure; strain energy increases monotonically). The reward is a weighted sum over all scored artifacts; simply reporting a number without producing the underlying data will not score well.
