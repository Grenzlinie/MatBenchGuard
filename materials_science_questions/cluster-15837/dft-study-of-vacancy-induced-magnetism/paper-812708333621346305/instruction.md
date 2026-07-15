# DFT-predicted magnetic moments of cation-deficient and Fe-doped γ-Ga2O3

## Problem background
γ-Ga₂O₃ is a wide-bandgap semiconductor with a cation‑deficient spinel structure. Because it naturally hosts Ga vacancies, it is considered a promising host for diluted magnetic semiconductors (DMS). First-principles calculations suggest that the intrinsic cation vacancies can induce a magnetic moment, and that substituting Fe ions at Ga sites can further enhance the magnetic properties. The computational challenge is to predict the total magnetic moment per formula unit cell for the defective and Fe‑doped structures using density functional theory.

## Approach
Spin‑polarized density functional theory (DFT) is used to study the magnetic ground state of three models based on the cubic spinel γ‑Ga₂O₃ (space group Fd‑3m). The starting point is the fully‑occupied Ga₂₄O₃₂ cell, from which three Ga vacancies are introduced in an ordered arrangement along [111] to create the cation‑deficient model. Octahedral Ga sites near the vacancies are then substituted by Fe atoms to build the single‑ and double‑Fe‑doped models. For each model, geometry and cell parameters are relaxed, and a self‑consistent field calculation with a Hubbard U correction on the Fe 3d orbitals is performed to obtain the total magnetization. The final goal is to extract the total magnetic moment per formula unit cell.

## Reproduction target
Compute the total magnetic moment per formula unit cell (in μB) for the following three structural models, after geometry relaxation and a self‑consistent spin‑polarized DFT calculation:  
1. γ-Ga₂₁□₃O₃₂ (cation‑deficient, undoped)  
2. γ-Ga₂₀Fe₁□₃O₃₂ (one Fe dopant)  
3. γ-Ga₁₉Fe₂□₃O₃₂ (two Fe dopants)  
Report the three values in a single CSV file named `magnetic_moments.csv`.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials (PBE efficiency): https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment (ASE): https://wiki.fysik.dtu.dk/ase/

## Workflow steps

### Step 1: Construct unit cell models for DFT
- Role: process
- Action: Build all required unit cell models based on the cubic spinel γ-Ga2O3 (space group Fd-3m, lattice constant 8.238 Å). Construct: (1) the fully occupied γ-Ga24O32 reference cell; (2) the cation-deficient γ-Ga21□3O32 cell with three Ga vacancies ordered along [111] in tetrahedral-octahedral-tetrahedral (T-O-T) sequences; (3) the single Fe-doped cell γ-Ga20Fe1□3O32 by substituting one octahedral Ga near the vacancies with Fe; (4) the double Fe-doped cell γ-Ga19Fe2□3O32 by substituting a neighbouring octahedral Ga with Fe. Save the structures in Quantum ESPRESSO input format.
- Evidence: none

### Step 2: Perform DFT calculations for all models
- Role: process
- Action: For each of the four models (fully occupied reference and three defective models), run spin-polarized DFT using Quantum ESPRESSO with PAW pseudopotentials (PBE) and a Hubbard U correction of 5 eV on Fe 3d orbitals. Converge geometry with energy threshold 1×10⁻⁵ eV and force threshold 0.01 eV/Å, then perform self-consistent field (SCF) calculations to obtain total magnetization. Save the SCF output files containing the total magnetic moment.
- Evidence: none

### Step 3: Extract magnetic moments and write CSV
- Role: scored (load-bearing)
- Action: Parse the DFT SCF output of the three defective models to extract the total magnetic moment (in μB) per formula unit cell. Write the results to a CSV file with columns: model_name, total_magnetic_moment_muB_per_fu.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: model_name (string), total_magnetic_moment_muB_per_fu (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Total magnetic moment per formula unit cell for the three defective models: γ-Ga21□3O32, γ-Ga20Fe1□3O32, γ-Ga19Fe2□3O32. The checker compares these values against the paper's DFT predictions with appropriate tolerances and expects the trend that the undoped cell has a non-zero moment and that the moment increases with Fe doping.
- schema:
  - `type`: table
  - `required_columns`: `model_name`, `total_magnetic_moment_muB_per_fu`
  - `units`:
    - `total_magnetic_moment_muB_per_fu`: μB

Notes: The fully occupied γ-Ga24O32 reference cell is computed but not scored. The scored artifacts are the magnetic moments of the three defective models. The tolerance window for the undoped moment is tight (±0.5 μB) due to its small value; for the doped models a ±1 μB tolerance is allowed to account for code-dependent variations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "model_name",
          "total_magnetic_moment_muB_per_fu"
        ],
        "units": {
          "total_magnetic_moment_muB_per_fu": "μB"
        }
      },
      "description": "Total magnetic moment per formula unit cell for the three defective models: γ-Ga21□3O32, γ-Ga20Fe1□3O32, γ-Ga19Fe2□3O32. The checker compares these values against the paper's DFT predictions with appropriate tolerances and expects the trend that the undoped cell has a non-zero moment and that the moment increases with Fe doping."
    }
  ],
  "notes": "The fully occupied γ-Ga24O32 reference cell is computed but not scored. The scored artifacts are the magnetic moments of the three defective models. The tolerance window for the undoped moment is tight (±0.5 μB) due to its small value; for the doped models a ±1 μB tolerance is allowed to account for code-dependent variations."
}
```

## How you are scored
A hidden verifier reads your `magnetic_moments.csv` and compares each model's total magnetic moment against reference values from the original DFT predictions. Because different implementations and pseudopotentials can produce small numerical differences, the verifier allows narrow tolerances that reflect typical code‑to‑code variation. In addition, it checks that the sequence of moments follows the expected physical behaviour: the undoped defective cell should exhibit a non‑zero magnetic moment, and the moment should increase with Fe doping. The final score is a weighted combination of these checks; reporting values without meaningful computations will not earn full credit.
