# Electron-Lattice Interaction Energy for bcc, fcc, hcp Lattices

## Problem background
Strongly compressed matter, as found in white dwarfs, crystallizes into a lattice. The total energy of such a crystal depends on the lattice structure, and in particular the electron-lattice interaction provides a structure-dependent correction that can affect which lattice type is most stable. The purpose of this task is to compute this interaction energy for the three most symmetric cubic and hexagonal lattices (bcc, fcc, hcp) for several elements, using a second-order perturbation theory expression.

## Approach
The electron-lattice interaction energy is treated as a perturbation of the homogeneous electron gas by the periodic potential of the nuclei. The second-order result reduces to a sum over all nonzero reciprocal lattice vectors of a known analytic function weighted by a structure factor. The expression involves the atomic number Z, the number of atoms per unit cell ν, the unit cell volume, and the reciprocal lattice geometry. The sum converges numerically and can be evaluated to high precision by including a sufficiently large set of reciprocal lattice vectors. For each of the three lattice types (bcc, fcc, hcp) and four atomic numbers (Z=1 for hydrogen, 2 for helium, 6 for carbon, 26 for iron), we compute the negative of the energy per atom in the natural dimensionless units Z^2 e^4 m / h^2. The atomic positions and ideal c/a ratio for hcp are standard crystallographic inputs.

## Reproduction target
Write a CSV file named electron_lattice_energy.csv containing one row for each combination of element (hydrogen, helium, carbon, iron) and lattice type (bcc, fcc, hcp). The file must have exactly 12 rows and three columns: element (string), lattice (string), and energy (float), where energy is the negative of the electron-lattice interaction energy per atom, -E_e-l, in dimensionless units of Z^2 e^4 m / h^2.

## Assets

- Python 3: python3
- NumPy: numpy

## Workflow steps

### Step 1: Compute electron-lattice interaction energy
- Role: scored (load-bearing)
- Action: Compute the negative of the electron-lattice interaction energy per atom, -E_e-l, in dimensionless units Z^2 e^4 m / h^2, using the second-order perturbation theory formula for electrons moving in a periodic nuclear potential. The formula is a sum over nonzero reciprocal lattice vectors b: E_e-l = - (Z e^4 m) / (ν^2 6 π^2 h^2) Σ g f(π b / p_F), where the function f(x) = 1/x^4 (1 + (1-x^2)/(2x) ln|(x+1)/(x-1)| ), the structure factor g = |Σ_{r'} exp(2π i b·r')|^2 with r' the atomic positions inside the unit cell, and the Fermi momentum p_F = π (3 Z ν / π v)^{1/3} with v the unit cell volume. Use the following standard atomic positions in reduced coordinates: bcc: (0,0,0) and (1/2,1/2,1/2) with ν=2; fcc: (0,0,0), (1/2,1/2,0), (1/2,0,1/2), (0,1/2,1/2) with ν=4; hcp: (0,0,0) and (2/3,1/3,1/2) with ν=2 and ideal c/a ratio sqrt(8/3). Sum over a sufficiently large set of reciprocal lattice vectors to achieve convergence. For each combination of lattice type (bcc, fcc, hcp) and element (Z=1 for H, 2 for He, 6 for C, 26 for Fe), compute the value and output one row.
- Output file: `/app/outputs/electron_lattice_energy.csv`
- Format: csv
- Contract: columns: element (string), lattice (string), energy (float, dimensionless). Exactly 12 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/electron_lattice_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### electron_lattice_energy.csv
- path: `/app/outputs/electron_lattice_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed electron-lattice interaction energy per atom in dimensionless units Z^2 e^4 m / h^2 for bcc, fcc, and hcp lattices of H, He, C, Fe.
- schema:
  - `type`: table
  - `required_columns`: `element`, `lattice`, `energy`
  - `units`:
    - `energy`: dimensionless (units of Z^2 e^4 m / h^2)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "electron_lattice_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "element",
          "lattice",
          "energy"
        ],
        "units": {
          "energy": "dimensionless (units of Z^2 e^4 m / h^2)"
        }
      },
      "description": "Computed electron-lattice interaction energy per atom in dimensionless units Z^2 e^4 m / h^2 for bcc, fcc, and hcp lattices of H, He, C, Fe."
    }
  ],
  "notes": ""
}
```

## How you are scored
After your run, a hidden verifier reads the output CSV and independently evaluates each energy value. Each value is compared against a hidden reference that is the result of an accurate independent evaluation of the same lattice sum. The final reward is the fraction of the 12 values that fall within a hidden tolerance of the reference. The verifier does not look at any other files; only the content of electron_lattice_energy.csv matters for the score.
