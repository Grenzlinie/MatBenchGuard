# Lattice Inversion for Finnis-Sinclair Potentials of fcc Metals

## Problem background
The Finnis-Sinclair model is a many-body embedded-atom approach that overcomes the limitations of simple pair potentials for cubic metals by including a term derived from a squared hopping integral. This task reconstructs, from a handful of measurable bulk properties, the individual hopping integral h(r) and the pair potential Φ(r) for the fcc metals Cu, Ag, and Au. The central open problem is to compute these two functions explicitly over a range of nearest-neighbour distances, using only the known experimental lattice constant, elastic constants, sublimation energy, unrelaxed vacancy-formation energy, and bulk modulus, together with fcc lattice inversion coefficients.

## Approach
The method first uses the Cauchy discrepancy (C12 – C44) and the difference between sublimation and vacancy-formation energies to determine two parameters: an exponential decay constant α and an equilibrium lattice sum n_e. With these, one constructs an exponential lattice-sum of the squared hopping integral and, by combining the tight-binding energy with a universal cohesive-energy function, obtains the lattice sum of the pair potential. The individual functions h(r) and Φ(r) are then recovered by applying the Möbius lattice-inversion technique for the fcc lattice, using pre‑computed shell weights and Möbius transforms. No fitting to empirical potentials is performed; everything follows from the input data through deterministic algebraic steps.

## Reproduction target
From the provided experimental data for Cu, Ag, and Au, compute the hopping integral h(r) and the pair potential Φ(r) as functions of the nearest-neighbour distance R1. Produce a CSV file containing these values at 100 equally spaced R1 points from 0.9 R1e to 1.2 R1e for each metal, where R1e is the equilibrium nearest-neighbour distance. The CSV must have columns: metal, distance_R1 (Å), hopping_integral (eV), and pair_potential (eV).

## Assets

- Experimental data for Cu, Ag, Au: a0, C12, C44, Es, Ev, B
- FCC Möbius inversion coefficients (w(n) and m(n))
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute α, n_e and derived constants
- Role: process
- Action: From the provided experimental data for Cu, Ag, Au (lattice constant a0, elastic constants C12 and C44, sublimation energy Es, unrelaxed vacancy-formation energy Ev, bulk modulus B), compute equilibrium atomic volume Ωe = a0^3/4, equilibrium nearest-neighbour distance R1e = a0/√2. Then compute α = sqrt(18 Ωe (C12 − C44) / (Es − Ev)) and n_e = 4 (Es − Ev)^2. Store the derived constants for each metal.
- Evidence: `/app/outputs/constants.json`

### Step 2: Construct energy functions and lattice sums
- Role: process
- Action: For each metal, using the derived constants, construct: (i) the exponential lattice-sum of the square hopping integral S_ρ(R1) = n_e exp[-α (R1/R1e - 1)], (ii) the tight‑binding energy E_TB(R1) = -2 (Es - Ev) exp[-½ α (R1/R1e - 1)], (iii) the RSGF universal cohesive energy E(R1) = -Es [1 + √(9 B Ωe / Es) (R1/R1e - 1)] exp[-√(9 B Ωe / Es) (R1/R1e - 1)], and (iv) the pair‑potential lattice sum ΣΦ(R_i) = 2 [E(R1) - E_TB(R1)].
- Evidence: none

### Step 3: Invert lattice sum of ρ to obtain hopping integral h(r)
- Role: process
- Action: Using the provided fcc Möbius inversion coefficients, apply the Möbius inversion formula to S_ρ(R1) to recover ρ(r) = h²(r). For a grid of nearest-neighbour distances R1, evaluate h(r) = sqrt(ρ(r)) by interpolation at the required R1 points.
- Evidence: none

### Step 4: Invert pair‑potential lattice sum to obtain Φ(r)
- Role: process
- Action: Using the same Möbius coefficients, apply the inversion to the pair‑potential sum ΣΦ(R_i) to obtain the pair potential Φ(r) at the required R1 grid points.
- Evidence: none

### Step 5: Write inverted functions CSV
- Role: scored (load-bearing)
- Action: For each metal (Cu, Ag, Au), evaluate the hopping integral h(R1) and the pair potential Φ(R1) on a grid of 100 equally spaced R1 values from 0.9 R1e to 1.2 R1e. Write a single CSV file with columns: metal, distance_R1 (angstroms), hopping_integral (eV), pair_potential (eV).
- Output file: `/app/outputs/inverted_functions.csv`
- Format: csv
- Contract: metal (string), distance_R1 (float), hopping_integral (float), pair_potential (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/inverted_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### inverted_functions.csv
- path: `/app/outputs/inverted_functions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: CSV with 300 rows (100 per metal) of inverted hopping integrals and pair potentials as functions of nearest-neighbour distance R1 for Cu, Ag, Au.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `distance_R1`, `hopping_integral`, `pair_potential`
  - `units`:
    - `distance_R1`: angstroms
    - `hopping_integral`: eV
    - `pair_potential`: eV

Notes: The deterministic procedure allows the checker to recompute the gold values using the same formulas and public data, comparing each row of the CSV within a tight tolerance. Process steps are required intermediates; their evidence is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "inverted_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "distance_R1",
          "hopping_integral",
          "pair_potential"
        ],
        "units": {
          "distance_R1": "angstroms",
          "hopping_integral": "eV",
          "pair_potential": "eV"
        }
      },
      "description": "CSV with 300 rows (100 per metal) of inverted hopping integrals and pair potentials as functions of nearest-neighbour distance R1 for Cu, Ag, Au."
    }
  ],
  "notes": "The deterministic procedure allows the checker to recompute the gold values using the same formulas and public data, comparing each row of the CSV within a tight tolerance. Process steps are required intermediates; their evidence is not scored."
}
```

## How you are scored
A hidden verifier will independently recompute the expected hopping integrals and pair potentials from the same public inputs and the same analytical formulas. It will compare your submitted CSV against the recomputed values. Your final reward is a weighted combination of checks on each workflow stage; merely reporting a single number that matches the paper is not sufficient — you must execute the full pipeline and produce the required artifacts.
