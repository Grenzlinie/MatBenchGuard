# CG-PVA Uniaxial Tensile Deformation and Microstructural Evolution

## Problem background
Solid-like polymers under uniaxial tension exhibit complex mechanical behavior including elastic, yield, strain-softening, and strain-hardening regimes. The relationship between the underlying microstructure—particularly the presence of crystalline domains and chain alignment—and the resulting mechanical response is not fully understood. This task uses large-scale molecular dynamics simulations of a coarse-grained model for polyvinyl alcohol (CG-PVA), which can form semicrystalline or glassy (amorphous) samples depending on preparation conditions. By performing tensile tests and analyzing the structural evolution of both ordered and disordered regions, we can investigate how crystalline and amorphous parts contribute to the overall stress–strain behavior.

## Approach
The CG-PVA model represents polymers as bead-spring chains with harmonic bonds, an angular bending potential, and a 6-9 Lennard-Jones non-bonded interaction; model parameters and units are given in the literature. Two polymer systems of 3600 chains of length 300 are prepared from an equilibrated melt at high temperature: a semicrystalline sample obtained by slow continuous cooling, and an amorphous (glassy) sample obtained by rapid quenching. Both samples are then subjected to uniaxial tension in one principal direction at a constant true strain rate, maintaining constant lateral pressure, up to a large strain. The true stress (derived from the virial) is recorded as a function of strain. Structural analysis is performed on saved trajectory snapshots: local nematic order parameter is computed in small cells to identify crystalline cells and obtain the volume-fraction crystallinity; the global nematic order parameter is computed from all bond vectors. The microscopic chain stretch is derived from root-mean-squared end-to-end vector components. Finally, pair distribution functions in perpendicular and parallel directions are computed separately for monomers in crystalline and amorphous regions at selected strains, allowing separate analysis of structural changes in the ordered and disordered parts.

## Reproduction target
Produce, for both the semicrystalline and amorphous samples at reduced temperature T = 0.2, the true stress-strain curve (stress vs. strain) as a CSV. Compute, for each sample, the evolution with strain of the volume fraction of crystalline cells (crystallinity) and the global nematic order parameter, and output another CSV. Compute the microscopic chain stretch versus macroscopic draw ratio and output a CSV. For the semicrystalline sample at four specified strains (ε_yy = 0.0, 0.5, 1.0, 1.6), compute the pair distribution functions g(ρ,0) and g(0,y) separately for crystalline regions and for amorphous regions, and output two CSVs (one each for crystalline and amorphous). All artifacts must follow the column schemas given in the workflow steps.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov

## Workflow steps

### Step 1: Sample preparation (semicrystalline and amorphous)
- Role: process
- Action: From an equilibrated melt of 3600 CG-PVA chains of length 300 at T=1, perform continuous cooling to T=0.2 at two rates: 10^{-6} τ^{-1} for the semicrystalline sample and 10^{-3} τ^{-1} for the amorphous (glassy) sample. Use the CG-PVA potential and NPT ensemble at P=8 reduced units. Save the final configurations.
- Evidence: `/app/outputs/sample_configs.data`

### Step 2: Uniaxial tensile deformation simulation
- Role: process
- Action: For both the semicrystalline and amorphous samples at T=0.2, run a uniaxial tension simulation in the y-direction at a constant true strain rate of 10^{-5} τ^{-1} and constant lateral pressure P=8. Continue until ε_yy ≈ 2.0. Save trajectory snapshots covering the strain range, including at least ε_yy = 0.0, 0.5, 1.0, 1.6, and record the system stress tensor at every frame.
- Evidence: `/app/outputs/tensile_trajectory.lammpstrj`

### Step 3: Stress-strain curves
- Role: scored
- Action: From the LAMMPS output, extract the true strain ε_yy and the corresponding true stress σ_yy (yy-component of the virial divided by volume). Output a CSV file with one row per saved frame for both samples.
- Output file: `/app/outputs/stress_strain.csv`
- Format: csv
- Contract: Columns: strain (unitless, float), stress (reduced units ε/σ³, float), sample_type (string, 'semicrystalline' or 'amorphous').
- Scoring: scored by hidden verifier

### Step 4: Crystallinity and global nematic order
- Role: scored (load-bearing)
- Action: For each saved snapshot, compute the local nematic order parameter S in cells of size ~2σ. Identify crystalline cells (S>0.8). Compute crystallinity X_C as the volume fraction of crystalline cells, and the global nematic order parameter S_global from the largest eigenvalue of the nematic tensor of all bond vectors. Output a CSV with columns for strain, X_C, S_global, and sample_type for both samples.
- Output file: `/app/outputs/crystallinity_and_order.csv`
- Format: csv
- Contract: Columns: strain (float), X_C (float, 0-1), S_global (float, 0-1), sample_type (string).
- Scoring: scored by hidden verifier

### Step 5: Microscopic chain stretch
- Role: scored
- Action: For each saved snapshot, compute the root-mean-squared components of the end-to-end vectors of all chains, R_α (α = x,y,z). Define the microscopic chain stretch λ_eff = R_y / R_y^0, where R_y^0 is the value in the undeformed sample. Output a CSV with columns for macroscopic stretch λ and λ_eff, and sample_type.
- Output file: `/app/outputs/microscopic_stretch.csv`
- Format: csv
- Contract: Columns: macroscopic_stretch (float, unitless), microscopic_stretch (float, unitless), sample_type (string).
- Scoring: scored by hidden verifier

### Step 6: Pair distribution in crystalline regions
- Role: scored
- Action: For the semicrystalline sample at strains ε_yy = 0.0, 0.5, 1.0, 1.6, compute the pair distribution function g_crys(ρ,y) using only monomers classified as crystalline (S>0.8 in their cell). Output a CSV with columns for strain, rho, y, g_crys(ρ,0), and g_crys(0,y).
- Output file: `/app/outputs/pair_distribution_crystalline.csv`
- Format: csv
- Contract: Columns: strain (float), rho (float, distance in σ), y (float, distance in σ), g_crys_rho0 (float), g_crys_0y (float).
- Scoring: scored by hidden verifier

### Step 7: Pair distribution in amorphous regions
- Role: scored
- Action: For the semicrystalline sample at the same strains (0.0, 0.5, 1.0, 1.6), compute g_amorph(ρ,y) for monomers in amorphous cells (S≤0.8). Output a CSV with columns for strain, rho, y, g_amorph(ρ,0), and g_amorph(0,y).
- Output file: `/app/outputs/pair_distribution_amorphous.csv`
- Format: csv
- Contract: Columns: strain (float), rho (float), y (float), g_amorph_rho0 (float), g_amorph_0y (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain.csv`
- `/app/outputs/crystallinity_and_order.csv`
- `/app/outputs/microscopic_stretch.csv`
- `/app/outputs/pair_distribution_crystalline.csv`
- `/app/outputs/pair_distribution_amorphous.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain.csv
- path: `/app/outputs/stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: True stress versus true strain for both samples at T=0.2. The checker will recompute yield stress, verify strain-softening/hardening trends.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`, `sample_type`
  - `units`:
    - `strain`: unitless
    - `stress`: reduced units (ε/σ³)
  - `description`: Stress-strain curves for semicrystalline and amorphous samples.

### crystallinity_and_order.csv
- path: `/app/outputs/crystallinity_and_order.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The checker will verify that X_C initially decreases then increases, and S_global rises above 0.5 at high strain, with tolerances bound to paper-reported values.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `X_C`, `S_global`, `sample_type`
  - `units`:
    - `strain`: unitless
    - `X_C`: fraction
    - `S_global`: unitless
  - `description`: Crystallinity fraction X_C and global nematic order parameter S_global as functions of strain.

### microscopic_stretch.csv
- path: `/app/outputs/microscopic_stretch.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The checker will verify λ_eff ≈ λ for λ ≲ 2 and sub-affine deviation beyond.
- schema:
  - `type`: table
  - `required_columns`: `macroscopic_stretch`, `microscopic_stretch`, `sample_type`
  - `units`:
    - `macroscopic_stretch`: unitless
    - `microscopic_stretch`: unitless
  - `description`: Comparison of macroscopic draw ratio λ and effective microscopic chain stretch λ_eff.

### pair_distribution_crystalline.csv
- path: `/app/outputs/pair_distribution_crystalline.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The checker will verify that the second nearest-neighbor peak in g(ρ,0) shifts to smaller distances at strains <0.8 and stabilises.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `rho`, `y`, `g_crys_rho0`, `g_crys_0y`
  - `units`:
    - `strain`: unitless
    - `rho`: distance in σ
    - `y`: distance in σ
    - `g_crys_rho0`: unitless
    - `g_crys_0y`: unitless
  - `description`: Pair distribution function g(ρ,0) and g(0,y) in crystalline regions.

### pair_distribution_amorphous.csv
- path: `/app/outputs/pair_distribution_amorphous.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The checker will verify that the amorphous g(ρ,0) second peak remains largely constant until strain ~0.8.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `rho`, `y`, `g_amorph_rho0`, `g_amorph_0y`
  - `units`:
    - `strain`: unitless
    - `rho`: distance in σ
    - `y`: distance in σ
    - `g_amorph_rho0`: unitless
    - `g_amorph_0y`: unitless
  - `description`: Pair distribution function g(ρ,0) and g(0,y) in amorphous regions.

Notes: Scoring uses metric recomputation from the raw CSV artifacts against hidden gold curves extracted from the paper at T=0.2. Tolerances are generous (±20% for stress, ±0.05 for crystallinity, ±0.1 for S_global) to absorb stochastic and implementation variance. All scored artifacts are required for a full reward.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress",
          "sample_type"
        ],
        "units": {
          "strain": "unitless",
          "stress": "reduced units (ε/σ³)"
        },
        "description": "Stress-strain curves for semicrystalline and amorphous samples."
      },
      "description": "True stress versus true strain for both samples at T=0.2. The checker will recompute yield stress, verify strain-softening/hardening trends."
    },
    {
      "file": "crystallinity_and_order.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "X_C",
          "S_global",
          "sample_type"
        ],
        "units": {
          "strain": "unitless",
          "X_C": "fraction",
          "S_global": "unitless"
        },
        "description": "Crystallinity fraction X_C and global nematic order parameter S_global as functions of strain."
      },
      "description": "The checker will verify that X_C initially decreases then increases, and S_global rises above 0.5 at high strain, with tolerances bound to paper-reported values."
    },
    {
      "file": "microscopic_stretch.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "macroscopic_stretch",
          "microscopic_stretch",
          "sample_type"
        ],
        "units": {
          "macroscopic_stretch": "unitless",
          "microscopic_stretch": "unitless"
        },
        "description": "Comparison of macroscopic draw ratio λ and effective microscopic chain stretch λ_eff."
      },
      "description": "The checker will verify λ_eff ≈ λ for λ ≲ 2 and sub-affine deviation beyond."
    },
    {
      "file": "pair_distribution_crystalline.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "rho",
          "y",
          "g_crys_rho0",
          "g_crys_0y"
        ],
        "units": {
          "strain": "unitless",
          "rho": "distance in σ",
          "y": "distance in σ",
          "g_crys_rho0": "unitless",
          "g_crys_0y": "unitless"
        },
        "description": "Pair distribution function g(ρ,0) and g(0,y) in crystalline regions."
      },
      "description": "The checker will verify that the second nearest-neighbor peak in g(ρ,0) shifts to smaller distances at strains <0.8 and stabilises."
    },
    {
      "file": "pair_distribution_amorphous.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "rho",
          "y",
          "g_amorph_rho0",
          "g_amorph_0y"
        ],
        "units": {
          "strain": "unitless",
          "rho": "distance in σ",
          "y": "distance in σ",
          "g_amorph_rho0": "unitless",
          "g_amorph_0y": "unitless"
        },
        "description": "Pair distribution function g(ρ,0) and g(0,y) in amorphous regions."
      },
      "description": "The checker will verify that the amorphous g(ρ,0) second peak remains largely constant until strain ~0.8."
    }
  ],
  "notes": "Scoring uses metric recomputation from the raw CSV artifacts against hidden gold curves extracted from the paper at T=0.2. Tolerances are generous (±20% for stress, ±0.05 for crystallinity, ±0.1 for S_global) to absorb stochastic and implementation variance. All scored artifacts are required for a full reward."
}
```

## How you are scored
A hidden verifier reads each scored CSV file and computes derived quantities (e.g., yield stress peak location and magnitude, initial crystallinity, monotonic increase of global nematic order, affine-to-subaffine transition point, peak shifts in pair distribution functions). It compares these against reference values and trends extracted from the original study. Because exact numbers depend on implementation details (LAMMPS version, random seeds, discretization), scoring uses generous tolerances and trend/shape checks; you do not need bit-level agreement. The verifier produces a combined reward from the weighted scores of all artifacts. Reporting numbers without providing the required raw CSV files will not receive full credit—the verifier recomputes metrics from your submitted data, not from a summary.
