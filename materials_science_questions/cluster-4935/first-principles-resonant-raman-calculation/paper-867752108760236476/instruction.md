# Exact Diagonalization of Laughlin Liquid at ν=1/3: Spin-Magnetograviton Energy and Pair Correlation

## Problem background
In a two-dimensional electron gas under a strong perpendicular magnetic field, the Laughlin liquid at electron filling factor ν=1/3 hosts exotic neutral excitations. Among these, the zero-momentum spin-magnetograviton is a spin-1 bosonic mode that can be the lowest-energy excitation under suitable confinement. Reproducing the theoretical predictions for the spin-magnetograviton energy and its spatial correlations (pair correlation function difference relative to the ground state) provides a crucial check on the theory of the Laughlin liquid's neutral excitations.

## Approach
We use exact diagonalization of the Coulomb interaction in the lowest Landau level on a finite sphere. For N=10 electrons at filling ν=1/3 (flux N_φ=27), we solve for the ground state (total angular momentum L=0, spin S=0) and the lowest zero-momentum spin-magnetograviton state (L=0, S=1) using Haldane pseudopotentials. The excitation energy is converted from dimensionless units to meV using GaAs material constants (dielectric constant ε=12.9) and the electron density 8.4×10^10 cm⁻², which determines the magnetic length and Coulomb energy scale. We also compute the pair correlation functions g(r) for both states and their difference Δg(r) as a function of distance r in magnetic-length units.

## Reproduction target
Produce the zero-momentum spin-magnetograviton energy (in meV) from the exact diagonalization described above, written to `step_01_spin_magnetograviton_energy.txt`. Compute Δg(r) = g_excited(r) – g_ground(r) for r from 0 to 8 magnetic-length units with at least 100 equally spaced points, written as a CSV with header 'r,delta_g' to `step_02_pair_correlation_difference.csv`.

## Assets

- GaAs material constants
- Exact diagonalization library (DiagHam): https://www.nick-ux.org/diagham/

## Workflow steps

### Step 1: Exact diagonalization: spin-magnetograviton energy
- Role: scored (load-bearing)
- Action: Using the electron density n=8.4×10^10 cm⁻² and ν=1/3, compute the magnetic field B = h n / (e ν) and the magnetic length l_B = √(ħ/(eB)). Using the GaAs dielectric constant ε=12.9, compute the Coulomb energy scale E_C = e²/(4πε₀ ε l_B) in meV. Then perform exact diagonalization of the Coulomb interaction in the lowest Landau level on the sphere for N=10 electrons with total flux N_φ=27, using Haldane pseudopotentials for the pure 2D Coulomb potential. Obtain the ground state (total L=0, total spin S=0) and the lowest zero-momentum spin-magnetograviton state (L=0, S=1). Convert the excitation energy to meV using the computed energy scale, and write the result to the output file.
- Output file: `/app/outputs/step_01_spin_magnetograviton_energy.txt`
- Format: txt
- Contract: A plain text file containing a single line: the energy value in meV, formatted as a decimal number (e.g., 1.57). No additional text.
- Scoring: scored by hidden verifier

### Step 2: Pair correlation function difference
- Role: scored
- Action: Using the same ground and spin-magnetograviton states, compute the pair correlation functions g(r) in units of the magnetic length. Then compute Δg(r) = g_excited(r) − g_ground(r) for r from 0 to 8 magnetic-length units, sampled at equally spaced points with at least 100 intervals.
- Output file: `/app/outputs/step_02_pair_correlation_difference.csv`
- Format: csv
- Contract: CSV file with exact header 'r,delta_g' (no spaces, no quotes). The first column is r (magnetic-length units, float). The second column is delta_g (dimensionless float). Minimum 100 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_spin_magnetograviton_energy.txt`
- `/app/outputs/step_02_pair_correlation_difference.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_spin_magnetograviton_energy.txt
- path: `/app/outputs/step_01_spin_magnetograviton_energy.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The computed spin-magnetograviton energy, to be compared with a hidden reference value within a predefined tolerance.
- schema:
  - `type`: text
  - `units`: meV
  - `description`: A single line containing a floating-point number representing the zero-momentum spin-magnetograviton energy in meV.

### step_02_pair_correlation_difference.csv
- path: `/app/outputs/step_02_pair_correlation_difference.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Difference between the pair correlation functions of the excited (spin-magnetograviton) and ground states. The structural audit verifies row count, numeric columns, and the existence of a characteristic peak in Δg(r) within a specified r-range.
- schema:
  - `type`: table
  - `required_columns`: `r`, `delta_g`
  - `units`:
    - `r`: magnetic length
    - `delta_g`: dimensionless

Notes: The energy file is compared to a hidden gold value within an absolute tolerance; the CSV is checked for consistency (≥100 rows, numeric columns, peak location). No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_spin_magnetograviton_energy.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "units": "meV",
        "description": "A single line containing a floating-point number representing the zero-momentum spin-magnetograviton energy in meV."
      },
      "description": "The computed spin-magnetograviton energy, to be compared with a hidden reference value within a predefined tolerance."
    },
    {
      "file": "step_02_pair_correlation_difference.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "delta_g"
        ],
        "units": {
          "r": "magnetic length",
          "delta_g": "dimensionless"
        }
      },
      "description": "Difference between the pair correlation functions of the excited (spin-magnetograviton) and ground states. The structural audit verifies row count, numeric columns, and the existence of a characteristic peak in Δg(r) within a specified r-range."
    }
  ],
  "notes": "The energy file is compared to a hidden gold value within an absolute tolerance; the CSV is checked for consistency (≥100 rows, numeric columns, peak location). No gold values or tolerances are disclosed here."
}
```

## How you are scored
A hidden verifier independently scores each output artifact. The energy file is compared to a hidden reference value with an appropriate tolerance. The CSV file is audited for structural correctness (row count and numeric data) and for the presence of a characteristic feature in Δg(r) that is expected for this excitation. The scores from the two artifacts are combined (with the energy carrying most of the weight) to produce a final reward in [0,1].
