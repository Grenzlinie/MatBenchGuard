# Stress concentration factor and tensile strength reduction from topological defects in monolayer graphene

## Problem background
Graphene is exceptionally strong in its ideal, defect-free form, but real samples always contain internal defects that concentrate stress and dramatically reduce the effective tensile strength.  Among these, paired pentagon-heptagon (5-7) topological defects, which can form during synthesis or handling, are a particularly important class because they act as pseudo‑cracks.  Understanding how much a given defect configuration weakens the material is critical for interpreting experimental strength measurements and for designing graphene‑based composites.  This task isolates this question: using molecular mechanics, you will quantify the stress concentration caused by a pair of 5-7 defects in monolayer graphene and compute the implied reduction in tensile strength.

## Approach
You will model a rectangular monolayer graphene sheet of roughly 12 × 24 nm² under periodic boundary conditions.  Into this pristine lattice, insert a single pair of pentagon-heptagon rings of opposite sign (a Stone–Wales‑like defect).  The interaction between carbon atoms is described by the AIREBO potential, implemented in the LAMMPS simulator.  First, you fully relax the atomic positions and the cell dimensions to obtain the unstrained reference configuration.  Then you apply a uniaxial tensile strain by scaling the lattice constant along one direction to a total of 2 %.  At the strained geometry you relax the atom positions again and then compute the strain of every C–C bond relative to the unstrained reference.  The stress concentration factor K is defined as the maximum bond strain divided by the applied macroscopic strain (0.02).  Using the well‑known ideal tensile strength of defect‑free graphene, 130 GPa, the implied tensile strength of the defective flake is 130 GPa / K.  The result is reported as two numbers in a JSON file.

## Reproduction target
Produce a summary.json file containing the computed stress concentration factor (dimensionless) and the implied tensile strength (in GPa) for the defective graphene monolayer described above.  The file must have the exact format specified in the output contract.

## Assets

- LAMMPS: https://lammps.sandia.gov

## Workflow steps

### Step 1: Build and relax defective graphene monolayer
- Role: process
- Action: Construct a monolayer graphene supercell of approximately 12×24 nm² with periodic boundary conditions. Insert a pair of pentagon-heptagon (5-7) defects of opposite sign, forming a Stone-Wales-like configuration. Using LAMMPS with the AIREBO potential, fully relax the atomic positions and the simulation cell until residual forces are below a sufficiently small threshold (e.g. 1e-5 eV/nm). Write the relaxed atomic configuration.
- Evidence: `/app/outputs/relaxed_structure.data`

### Step 2: Compute stress concentration factor and implied tensile strength
- Role: scored (load-bearing)
- Action: Starting from the relaxed structure, apply uniaxial tensile strain to 2% by enlarging the lattice constant along one direction. Relax the atomic positions at the final strained configuration. Compute the per-bond strain for each C–C bond relative to the relaxed unstrained reference. Determine the maximum bond strain. The stress concentration factor K = max_bond_strain / 0.02. Using the ideal strength of defect-free graphene (130 GPa), compute the implied tensile strength as 130 GPa / K. Write K and the implied strength to summary.json.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: {"stress_concentration_factor": float, "implied_strength_GPa": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: JSON file containing the computed stress concentration factor (dimensionless) and the implied tensile strength (in GPa) of the defective graphene monolayer.
- schema:
  - `type`: object
  - `required`:
    - `stress_concentration_factor`: float
    - `implied_strength_GPa`: float

Notes: The checker reads the two values from summary.json and compares them against hidden paper-reported reference values within tolerances. Both values must be within tolerance to receive full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "stress_concentration_factor": "float",
          "implied_strength_GPa": "float"
        }
      },
      "description": "JSON file containing the computed stress concentration factor (dimensionless) and the implied tensile strength (in GPa) of the defective graphene monolayer."
    }
  ],
  "notes": "The checker reads the two values from summary.json and compares them against hidden paper-reported reference values within tolerances. Both values must be within tolerance to receive full credit."
}
```

## How you are scored
A hidden verifier will read your summary.json and independently compare the two quantities against reference values (obtained from the original study) within appropriate tolerances.  Both quantities must be within tolerance for you to receive full credit; larger deviations yield partial credit.  The verifier may also cross‑check internal consistency (e.g., that the implied strength equals 130 GPa divided by K).  Your score is determined solely by what you write to summary.json; no other output is scored.
