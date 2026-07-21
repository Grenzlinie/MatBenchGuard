# Charge density and surface potential in twisted hBN bilayer

## Problem background
When two monolayers of hexagonal boron nitride (hBN) are stacked with a small twist angle, the interface reconstructs into alternating AB and BA domains, forming a moiré superlattice. In the parallel alignment, the domain structure produces a layer-opposite interfacial charge polarization. The goal is to compute the resulting net surface charge density modulation and the corresponding surface potential variation, starting from the atomic structure and a tight-binding electronic model.

## Approach
First relax the twisted bilayer geometry using classical atomistic energy minimization: the LAMMPS code with an interlayer potential (ILP) and a Tersoff intralayer potential. The configuration is a parallel-aligned hBN bilayer at a chosen marginal twist angle (e.g., ~0.5°). On the relaxed atomic positions, construct a tight-binding Hamiltonian with nearest-neighbour in-layer hopping (2.33 eV) and exponential Koster–Slater interlayer hoppings. Diagonalize the Hamiltonian, sum over occupied states to obtain layer-resolved charge density, and compute the net surface charge density (excess charge per unit area) in mC/m². From that charge density, estimate the surface potential modulation in eV using the parallel-plate capacitor approximation with interlayer dielectric constant of 1.

## Reproduction target
Reproduce the theoretical surface charge density modulation (in mC/m²) and the surface potential modulation (in eV) for a parallel-aligned twisted hBN bilayer at a marginal twist angle (e.g., ~0.5°). The workflow must produce the following two files with single numeric values: `/app/outputs/charge_density.txt` and `/app/outputs/surface_potential.txt`.

## Assets

- LAMMPS (Large-scale Atomic/Molecular Massively Parallel Simulator): https://lammps.sandia.gov/
- Interlayer potential (ILP) parameters for graphene/hBN: 10.1021/acs.jctc.6b00148
- Tersoff potential for hBN (in-layer): 10.1103/PhysRevB.37.6991

## Workflow steps

### Step 1: Classical atomistic relaxation of twisted hBN bilayer
- Role: process
- Action: Use LAMMPS with the interlayer potential (ILP) and Tersoff intralayer potential to energy-minimize a parallel-aligned twisted hBN bilayer at a chosen marginal twist angle (e.g., ~0.5°). This produces a relaxed atomic configuration.
- Evidence: `/app/outputs/relaxed_structure.xyz`

### Step 2: Tight-binding charge density calculation
- Role: scored (load-bearing)
- Action: Construct a tight-binding model on the relaxed atomic configuration. Use nearest-neighbor in-layer hopping of 2.33 eV and exponential Koster-Slater interlayer hoppings. Diagonalize the Hamiltonian, sum over occupied states to compute layer-resolved charge density, and derive the net surface charge density modulation (excess charge per unit area) in units of mC/m². Output the value.
- Output file: `/app/outputs/charge_density.txt`
- Format: txt
- Contract: A single floating-point number (e.g., 3.0).
- Scoring: scored by hidden verifier

### Step 3: Surface potential estimation from charge density
- Role: scored (load-bearing)
- Action: Using the charge density modulation from the previous step, apply the parallel-plate capacitor approximation with interlayer dielectric constant of 1 to compute the surface potential modulation in eV. Output the value.
- Output file: `/app/outputs/surface_potential.txt`
- Format: txt
- Contract: A single floating-point number (e.g., 0.2).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/charge_density.txt`
- `/app/outputs/surface_potential.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### charge_density.txt
- path: `/app/outputs/charge_density.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Computed surface charge density modulation in mC/m².
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: mC/m^2

### surface_potential.txt
- path: `/app/outputs/surface_potential.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Estimated surface potential modulation in eV.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object
  - `required_columns`:
  - `units`:
    - `value`: eV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "charge_density.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "mC/m^2"
        }
      },
      "description": "Computed surface charge density modulation in mC/m²."
    },
    {
      "file": "surface_potential.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {},
        "required_columns": [],
        "units": {
          "value": "eV"
        }
      },
      "description": "Estimated surface potential modulation in eV."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently reads the two output files (`charge_density.txt` and `surface_potential.txt`) and compares your computed numeric values against a hidden reference with tolerances that account for legitimate toolchain spread (different implementation, discretization, or convergence). Each scored artifact contributes a fraction of the total reward; the final score is the weighted sum. Submitting the right numbers alone is not sufficient—the values must come from the full computational pipeline described in the workflow steps.
