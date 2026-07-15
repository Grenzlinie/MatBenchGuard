# Molecular Dynamics Simulation of Uniaxial Compression of Glassy Polymethylene

## Problem background
Polymethylene (PM) is a model polymer glass. Understanding the atomic-scale mechanisms of its plastic deformation is key to predicting mechanical properties. Molecular dynamics simulations can reveal whether deformation proceeds via nonaffine chain fragment gliding or conformational unfolding, and quantify the characteristic length scale of these rearrangements.

## Approach
The workflow constructs an amorphous PM sample, equilibrates it at low temperature, and then performs an isothermal uniaxial compression MD simulation. From the simulation trajectory, the axial engineering stress and mass density are computed as functions of strain. To analyze cooperative rearrangements, the nonaffine displacement D_min is calculated for each CH2 group using the Falk-Langer method on pairs of snapshots at small strain increments. The correlation function of D_min along each chain is then computed and an exponential decay is fitted to obtain a characteristic correlation length (in number of CH2 units).

## Reproduction target
Run the molecular dynamics simulation of glassy polymethylene under uniaxial compression at 50 K and strain rate 2e8 s⁻¹ to 30% strain. Compute the axial stress and density as functions of strain and write stress_strain.csv. From the trajectory near ε = -28%, compute the nonaffine displacement correlation length along the chain and save it as correlation_length.txt. Submit these two files.

## Assets

- LAMMPS molecular dynamics simulator: https://www.lammps.org
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Prepare amorphous polymethylene sample
- Role: process
- Action: Build an amorphous cell with 64 united-atom CH2 chains of length 100 using periodic boundary conditions and the specified force field (harmonic bonds L0=1.53 Å, KL=1047.5 kJ/mol/Å²; harmonic angles θ0=113°, Kθ=167.6 kJ/mol/rad²; torsion K1=6.704, K2=1.634 kJ/mol; Lennard-Jones ε=0.503 kJ/mol, Rmin=4.2654 Å). Equilibrate via NPT MD at 50 K to ~0.996 g/cm³. Save the equilibrated configuration.
- Evidence: `/app/outputs/sample_config.lammpsdata`

### Step 2: Uniaxial compression MD simulation
- Role: process
- Action: Perform isothermal uniaxial compression on the prepared sample at T=50 K, engineering strain rate 2e8 s⁻¹ (dε/dt = -2e-4 ps⁻¹) to ε = -30%, maintaining constant transverse pressure. After reaching final strain, fix cell dimensions and relax for 1 ns. Save snapshot coordinates and stress tensor every 10 ps (0.2% strain increment).
- Evidence: `/app/outputs/compression_traj.lammpstrj`

### Step 3: Compute stress-strain and density curves
- Role: scored
- Action: From the compression trajectory, extract axial engineering stress σ (MPa) and mass density ρ (g/cm³) at each saved strain step. Output a CSV with columns: strain (negative engineering strain, %), stress (MPa), density (g/cm³).
- Output file: `/app/outputs/stress_strain.csv`
- Format: csv
- Contract: strain (%, negative), stress (MPa), density (g/cm³) with header row
- Scoring: scored by hidden verifier

### Step 4: Compute nonaffine displacement correlation length
- Role: scored (load-bearing)
- Action: For snapshot pairs separated by Δε ≈ 0.2% (10 ps) near ε ≈ -28%, compute the nonaffine displacement D_min for each CH2 group using the Falk-Langer method. Calculate the correlation function of D_min along each chain and fit an exponential decay to obtain the correlation length N_c (in CH2 groups). Output the single fitted value.
- Output file: `/app/outputs/correlation_length.txt`
- Format: txt
- Contract: one decimal number, e.g., 11.6
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain.csv`
- `/app/outputs/correlation_length.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain.csv
- path: `/app/outputs/stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Stress-strain and density-strain data from uniaxial compression simulation. The checker extracts characteristic quantities (yield stress, plateau stress, etc.) and compares them to reference values.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress`, `density`
  - `units`:
    - `strain`: % (negative engineering strain)
    - `stress`: MPa
    - `density`: g/cm³

### correlation_length.txt
- path: `/app/outputs/correlation_length.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Nonaffine displacement correlation length extracted from the simulation trajectory near ε = -28%.
- schema:
  - `type`: text
  - `description`: Single decimal number representing the nonaffine displacement correlation length along the chain, in number of CH2 groups.

Notes: The hidden checker will derive yield stress, plateau stress, and validate the stress-strain curve shape from stress_strain.csv, then compare both the derived quantities and the correlation length to the paper-reported reference.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress",
          "density"
        ],
        "units": {
          "strain": "% (negative engineering strain)",
          "stress": "MPa",
          "density": "g/cm³"
        }
      },
      "description": "Stress-strain and density-strain data from uniaxial compression simulation. The checker extracts characteristic quantities (yield stress, plateau stress, etc.) and compares them to reference values."
    },
    {
      "file": "correlation_length.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single decimal number representing the nonaffine displacement correlation length along the chain, in number of CH2 groups."
      },
      "description": "Nonaffine displacement correlation length extracted from the simulation trajectory near ε = -28%."
    }
  ],
  "notes": "The hidden checker will derive yield stress, plateau stress, and validate the stress-strain curve shape from stress_strain.csv, then compare both the derived quantities and the correlation length to the paper-reported reference."
}
```

## How you are scored
A hidden verifier will independently inspect the submitted artifacts. It will extract key features from stress_strain.csv—such as the yield stress, plateau stress, and overall curve shape—and compare them against reference values derived from the original study. The correlation_length.txt value will also be compared. The final score is a weighted combination of these checks, rewarding results that reproduce the expected physical behavior within reasonable tolerance. The exact tolerance thresholds are not disclosed, so rely on accurate execution of the protocol rather than attempting to match a specific published number.
