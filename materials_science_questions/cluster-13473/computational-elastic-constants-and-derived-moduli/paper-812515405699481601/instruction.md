# Effect of van der Waals energy on Young's modulus of amorphous polycarbonate

## Problem background
The stiffness of a polymer is influenced by intermolecular forces, particularly van der Waals interactions. Understanding how the strength of these interactions affects mechanical properties like Young's modulus and density is important for polymer design. This task uses all-atom molecular dynamics simulations to systematically vary the Lennard‑Jones well‑depth parameter ε in an amorphous polycarbonate system and measure the resulting Young’s modulus and mass density.

## Approach
Molecular dynamics simulations are performed on amorphous polycarbonate (C₁₆H₁₄O₃) using the DREIDING force field. The Lennard‑Jones ε parameters for carbon, oxygen, and hydrogen are scaled by a common factor ε_norm, taking the values 0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 5.0, and 10.0. For each ε_norm, a bulk system of 9902 atoms is built and equilibrated through a multi‑stage protocol (energy minimization, NVT and NPT ensembles at high temperature and at room temperature). The equilibrated systems are then subjected to uniaxial tensile deformations along the X, Y, and Z directions at a constant engineering strain rate up to 2 % strain. The Young’s modulus is obtained from the slope of the stress–strain curve in the initial strain region, averaged over the three directions. The mass density of the equilibrated bulk cell is also recorded. The dependence of modulus and density on ε_norm is examined.

## Reproduction target
Produce the following artifacts:
- `density_vs_epsilon.csv`: a table listing the mass density of the equilibrated polycarbonate system for each ε_norm value.
- `youngs_modulus_vs_epsilon.csv`: a table containing the Young’s modulus averaged over the three tensile directions for each ε_norm.
- `tensile_data.json`: a JSON file with, for every ε_norm and direction, the full stress–strain arrays and the fitted linear slope.

The moduli must reflect the isotropic response of the simulated amorphous polycarbonate. The provided data should allow an independent verification of the relationship between Young’s modulus and ε_norm, as well as the trend of density with ε_norm.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/download.html
- DREIDING force field parameters
- Polycarbonate monomer (C16H14O3) molecular structure

## Workflow steps

### Step 1: System Preparation and Equilibration
- Role: process
- Action: For each ε_norm value in {0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0, 5.0, 10.0}, build an amorphous polycarbonate bulk cell containing 9902 atoms using the DREIDING force field with Lennard-Jones ε parameters scaled by the respective factor. Equilibrate each system via the six-stage protocol: energy minimization, NVT at 500 K, NPT at 500 K and 0 atm, cooling to 300 K at 0 atm, NVT at 300 K, NPT at 300 K and 0 atm. Record final density and total energy for each ε_norm.
- Evidence: `/app/outputs/equilibration_summary.csv`

### Step 2: Density Extraction
- Role: scored
- Action: From the final NPT equilibrated configuration at 300 K for each ε_norm, compute the mass density (total mass / simulation box volume) and write to a CSV file.
- Output file: `/app/outputs/density_vs_epsilon.csv`
- Format: csv
- Contract: Columns: epsilon_norm (float), density_g_cm3 (float). One row per ε_norm.
- Scoring: scored by hidden verifier

### Step 3: Tensile Simulation and Young's Modulus Calculation
- Role: scored (load-bearing)
- Action: For each ε_norm value, run uniaxial tensile deformations along X, Y, and Z directions at 300 K under NPT (zero transverse pressure) with a constant engineering strain rate of 1e8 s^{-1} up to 2% strain. Record stress-strain data (virial stress and engineering strain). For each direction, compute Young's modulus as the slope of the linear fit in the 0–2% strain region. Average the three directional moduli per ε_norm. Produce two output files: a JSON file containing per ε_norm and direction the strain and stress arrays and the fitted slopes, and a CSV file containing the averaged Young's modulus for each ε_norm.
- Output file: `/app/outputs/youngs_modulus_vs_epsilon.csv`
- Format: csv
- Contract: Columns: epsilon_norm (float), young_modulus_GPa (float). One row per ε_norm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/density_vs_epsilon.csv`
- `/app/outputs/youngs_modulus_vs_epsilon.csv`
- `/app/outputs/tensile_data.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### density_vs_epsilon.csv
- path: `/app/outputs/density_vs_epsilon.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Mass density of the equilibrated amorphous polycarbonate cell for each normalized epsilon.
- schema:
  - `columns`: `epsilon_norm`, `density_g_cm3`

### youngs_modulus_vs_epsilon.csv
- path: `/app/outputs/youngs_modulus_vs_epsilon.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Young's modulus (averaged over three tensile directions) for each normalized epsilon.
- schema:
  - `columns`: `epsilon_norm`, `young_modulus_GPa`

Notes: The raw stress-strain curves are stored in tensile_data.json for transparency and possible recomputation, but only the CSV files are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "density_vs_epsilon.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "epsilon_norm",
          "density_g_cm3"
        ]
      },
      "description": "Mass density of the equilibrated amorphous polycarbonate cell for each normalized epsilon."
    },
    {
      "file": "youngs_modulus_vs_epsilon.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "epsilon_norm",
          "young_modulus_GPa"
        ]
      },
      "description": "Young's modulus (averaged over three tensile directions) for each normalized epsilon."
    }
  ],
  "notes": "The raw stress-strain curves are stored in tensile_data.json for transparency and possible recomputation, but only the CSV files are scored."
}
```

## How you are scored
A hidden verifier evaluates your output files. For the density CSV, each density value is compared to a hidden reference within a tolerance. For the Young’s modulus, the verifier recomputes the modulus from the raw stress–strain curves in `tensile_data.json` and compares the result against a hidden reference; it also checks that a linear fit through your modulus‑versus‑ε_norm points has a high coefficient of determination (R²). The verifier further validates the format and internal consistency of the JSON file. The final score is a weighted sum of these checks. Submitting correct, detailed artifacts is essential; simply reporting a single number without the underlying data will not suffice.
