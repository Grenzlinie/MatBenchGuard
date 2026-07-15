# MD Simulations of CNT-Cellulose Wrapped Fibers and Nanopaper Property Predictions

## Problem background
The study explores the possibility of tuning the mechanical and adhesion properties of carbon nanotubes (CNTs) by wrapping them with aligned cellulose chains, forming what is called a cellulose nanotube. The goal is to investigate how the cellulose volume fraction (Vf) affects tensile/compressive strength, stiffness, toughness, surface energy, and interfacial shear behavior, and to predict the mechanical performance of staggered nanopapers constructed from these wrapped fibers.

## Approach
The computational workflow consists of: (1) building atomistic models of a pristine CNT (10,10) and CNTs wrapped by 1–5 layers of cellulose (yielding several Vf values), as well as pure cellulose nanocrystal (CNC) and a cellulose wrap without CNT; (2) validating a reactive force field (ReaxFF with Mattsson parameters) against other common potentials for CNT; (3) performing molecular dynamics tensile and compression tests on each fiber model to obtain raw stress–strain curves; (4) conducting interfacial shear and normal separation simulations on fiber-pair configurations to obtain shear stress–strain curves and energy–separation curves; (5) post-processing the raw data to extract mechanical and adhesion properties; and (6) applying a shear-lag analytical model (with an overlap length of 50%) using the computed fiber modulus and interfacial shear modulus to predict the strength and modulus of staggered nanopapers.

## Reproduction target
Write a single CSV file `results.csv` under `/app/outputs/` containing the computed properties for each simulated system. The columns must be: Vf, tensile_strength_GPa, tensile_modulus_GPa, tensile_toughness_GJm3, tensile_failure_strain, compressive_strength_GPa, compressive_modulus_GPa, compressive_toughness_GJm3, compressive_failure_strain, surface_energy_Jm2, shear_strength_GPa, shear_modulus_GPa, nanopaper_strength_GPa, nanopaper_modulus_GPa. Rows are required for Vf = 0.0, 0.55, 0.75, 0.84, 0.89, 0.91, 1.0 (pure CNC with 36 chains and [110]/[1-10] surfaces), and 1.0 (multi-layer cellulose wrap with no CNT). The nanopaper predictions should be computed using the shear-lag model with 50% overlap length and the critical shear strain determined from the shear test.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/download.html
- ReaxFF force field parameters (Mattsson et al. 2010): 10.1103/PhysRevB.81.054103
- Cellulose Iβ crystal structure parameters: 10.1021/ja011572q

## Workflow steps

### Step 1: Build and equilibrate atomic models
- Role: process
- Action: Construct LAMMPS data files for all molecular systems: pristine CNT (10,10), CNT wrapped by 1–5 layers of cellulose (Vf = 0.55, 0.75, 0.84, 0.89, 0.91), pure CNC (Vf=1.0), cellulose wrap without CNT (Vf=1.0), and fiber-pair configurations for shear and normal tests. Use the CNT chirality, cellulose Iβ chain parameters, and the appropriate number of chains per layer. Minimize and equilibrate in NVT at 300 K with ReaxFF-Mattsson.
- Evidence: `/app/outputs/equilibration.log`

### Step 2: Force-field validation for CNT
- Role: process
- Action: Run tensile MD tests on a pristine (10,10) CNT using six force fields: Rebo, Airebo, ReaxFF-CHO, ReaxFF-Glycine, ReaxFF-RDX, and ReaxFF-Mattsson. Generate stress–strain curves and confirm that ReaxFF-Mattsson yields Young's modulus ~900–1100 GPa and failure strain ~0.2, consistent with literature, and select it for all later simulations.
- Evidence: `/app/outputs/cn_ff_validation.png`

### Step 3: Tensile MD simulations for all Vf
- Role: process
- Action: For each equilibrated single-fiber model (all Vf), run tensile MD tests with fixed boundary atoms and a constant pulling velocity along the fiber axis. Use ReaxFF-Mattsson, NVT at 300 K. Output raw engineering stress vs. engineering strain curves as separate files in tensile_raw/ directory.
- Evidence: none

### Step 4: Compression MD simulations for all Vf
- Role: process
- Action: Run compression tests on the same single-fiber models as in tensile, applying a constant compression rate. Save raw stress–strain curves under compression_raw/.
- Evidence: none

### Step 5: Interfacial shear MD simulations
- Role: process
- Action: For each Vf, use the fiber-pair shear-test configuration and apply a steering force to shear the top fiber while fixing the bottom fiber. Record shear stress vs. shear strain; save under shear_raw/.
- Evidence: none

### Step 6: Normal separation (adhesion) MD simulations
- Role: process
- Action: Perform normal pull-off simulations on the fiber-pair normal-test configuration for each Vf. Separate the two fibers and record total potential energy vs. separation distance; save data under normal_raw/.
- Evidence: none

### Step 7: Compute mechanical, adhesion, and nanopaper properties
- Role: scored (load-bearing)
- Action: From the raw stress–strain and energy data, compute for each Vf: tensile/compressive strength, Young's modulus, toughness, failure strain; surface energy; interfacial shear strength/modulus. Then use the fiber modulus and interfacial shear modulus in the shear-lag model with 50% overlap to predict nanopaper strength and modulus. Collect all values into results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: Vf, tensile_strength_GPa, tensile_modulus_GPa, tensile_toughness_GJm3, tensile_failure_strain, compressive_strength_GPa, compressive_modulus_GPa, compressive_toughness_GJm3, compressive_failure_strain, surface_energy_Jm2, shear_strength_GPa, shear_modulus_GPa, nanopaper_strength_GPa, nanopaper_modulus_GPa. One row per Vf (including Vf=0.0, 0.55, 0.75, 0.84, 0.89, 0.91, 1.0 CNC, and 1.0 cellulose-wrapped-no-CNT).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Final summary table of all MD-derived mechanical and adhesion properties and shear-lag nanopaper predictions as functions of cellulose volume fraction.
- schema:
  - `type`: table
  - `required_columns`: `Vf`, `tensile_strength_GPa`, `tensile_modulus_GPa`, `tensile_toughness_GJm3`, `tensile_failure_strain`, `compressive_strength_GPa`, `compressive_modulus_GPa`, `compressive_toughness_GJm3`, `compressive_failure_strain`, `surface_energy_Jm2`, `shear_strength_GPa`, `shear_modulus_GPa`, `nanopaper_strength_GPa`, `nanopaper_modulus_GPa`

Notes: The checker will recompute properties from the agent's raw stress-strain and energy files and compare to the agent's reported values (internal consistency) and to paper-reported reference values with tolerance. The raw simulation outputs (tensile_raw/, compression_raw/, shear_raw/, normal_raw/) are evidence, not scored artifacts, but the checker may read them for recomputation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Vf",
          "tensile_strength_GPa",
          "tensile_modulus_GPa",
          "tensile_toughness_GJm3",
          "tensile_failure_strain",
          "compressive_strength_GPa",
          "compressive_modulus_GPa",
          "compressive_toughness_GJm3",
          "compressive_failure_strain",
          "surface_energy_Jm2",
          "shear_strength_GPa",
          "shear_modulus_GPa",
          "nanopaper_strength_GPa",
          "nanopaper_modulus_GPa"
        ]
      },
      "description": "Final summary table of all MD-derived mechanical and adhesion properties and shear-lag nanopaper predictions as functions of cellulose volume fraction."
    }
  ],
  "notes": "The checker will recompute properties from the agent's raw stress-strain and energy files and compare to the agent's reported values (internal consistency) and to paper-reported reference values with tolerance. The raw simulation outputs (tensile_raw/, compression_raw/, shear_raw/, normal_raw/) are evidence, not scored artifacts, but the checker may read them for recomputation."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that inspects the generated `results.csv` and, where available, your raw simulation output files. The verifier will recompute the mechanical and adhesion properties from your raw stress–strain and energy data and check them for internal consistency with the reported values. It will also compare the reported property values against hidden reference values that define the expected results, using tolerances that account for computational variability. In addition, the verifier will examine whether the properties exhibit a consistent monotonic trend with increasing Vf, as expected from the physics. The nanopaper predictions will be checked for consistency with your own input properties and the shear-lag model. The final reward is a weighted combination of these checks; you must produce the entire pipeline to succeed.
