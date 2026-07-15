# Elastic Constants and Cohesive Energy from EGEP Potential for FCC Metals

## Problem background
Accurate interatomic potentials are essential for predicting the mechanical and cohesive properties of metals. The extended generalized exponential potential (EGEP) is a model that captures both repulsive and attractive components of interatomic forces, accounting for many-body effects (through parameter n) and exchange-correlation effects (through parameter m) without relying on empirical fitting to target elastic constants or phonon frequencies. The potential is parameterized solely from the experimental lattice constant and bulk modulus. This task involves computing the second- and third-order elastic constants, pressure derivatives of second-order elastic constants, and cohesive energy for fcc metals (Rh, Yb, Ir, Th) using the EGEP potential.

## Approach
Implement the EGEP potential function Φ(r) = D/(m−1) [ exp(−m α (r−r0)) / (α r)^n − m (α r)^n exp(−α (r−r0)) ].

For each metal and each (n,m) pair specified in the Assets, compute the potential parameters (α a0, α, β, D, r0) as follows:
1. Solve the stress-free equilibrium condition (the sum over all lattice vectors L_j of l1² d²Φ/dr² = 0) to relate β = exp(α r0) to α a0.
2. By matching the experimental bulk modulus B using the lattice sum expression (B = (r²/(9V)) d²Φ/dr² at r = r0), iteratively determine α a0 and then D.
3. Compute the remaining parameters from the lattice constant a0.

Use lattice sums over all neighbors of an fcc crystal within at least 248 atoms. Then, using these parameters, compute the second-order elastic constants (C11, C12) and third-order elastic constants (C111, C112, C123) via lattice sums of derivatives of Φ(r) (Born's formulas). Also compute the pressure derivatives ∂C11'/∂p, ∂C12'/∂p, ∂C44'/∂p, ∂B'/∂p, ∂C'/∂p following Birch's method. Finally, compute the cohesive energy per atom as the sum of the EGEP pair interactions at equilibrium. Output all values in the specified CSV.

## Reproduction target
Produce a file results.csv with columns: metal, n, m, C11, C12, C111, C112, C123, dC11dp, dC12dp, dC44dp, dBdp, dCdp, cohesive_energy. Include one row for each (metal, n, m) combination listed in the Assets section. Units: elastic constants in 10^11 N/m², pressure derivatives dimensionless, cohesive energy in eV/atom. The combination of rows must exactly match the listed inputs.

## Assets
**Input data (public constants from Kittel, Introduction to Solid State Physics):**
- Lattice constant a0 (10^-10 m): Rh 3.80, Yb 5.48, Ir 3.84, Th 5.08.
- Bulk modulus B (10^11 N/m²): Rh 2.704, Yb 0.133, Ir 3.550, Th 0.543.

**Parameter sets to evaluate (each (n,m) pair for the respective metal):**
- Rh: (n=0.5, m=1.5), (n=6.0, m=15.0)
- Yb: (n=0.5, m=5.0), (n=1.0, m=4.0)
- Ir: (n=0.5, m=2.0), (n=9.0, m=15.0)
- Th: (n=0.5, m=3.0), (n=1.0, m=2.0)

No other external datasets, models, or services are required. The agent must install any necessary numerical libraries (e.g., numpy, scipy) within the workflow.

## Workflow steps

### Step 1: Fit EGEP potential parameters
- Role: process
- Action: For each metal (Rh, Yb, Ir, Th) and each (n,m) parameter set listed in the paper's Table 2, determine the EGEP potential parameters (alpha_a0, alpha, beta, D, r0) by solving the stress-free equilibrium condition and matching the experimental bulk modulus using lattice sums over fcc crystal shells (include at least 248 atoms).
- Evidence: `/app/outputs/fitted_parameters.csv`

### Step 2: Compute elastic constants, pressure derivatives, and cohesive energy
- Role: scored (load-bearing)
- Action: Using the EGEP potential parameters from the previous step, compute for each metal and (n,m) set: (1) second-order elastic constants C11, C12; (2) third-order elastic constants C111, C112, C123; (3) pressure derivatives dC11'/dp, dC12'/dp, dC44'/dp, dB'/dp, dC'/dp; (4) cohesive energy per atom. Write all computed values to results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: Columns: metal (str), n (float), m (float), C11 (float, 10^11 N/m^2), C12 (float, 10^11 N/m^2), C111 (float, 10^11 N/m^2), C112 (float, 10^11 N/m^2), C123 (float, 10^11 N/m^2), dC11dp (float, dimensionless), dC12dp (float), dC44dp (float), dBdp (float), dCdp (float), cohesive_energy (float, eV/atom). One row per (metal, n, m) combination from the paper's Table 2.
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
- target_policy: reference_match
- description: Computed elastic constants, pressure derivatives, and cohesive energy for each metal and (n,m) parameter set.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `n`, `m`, `C11`, `C12`, `C111`, `C112`, `C123`, `dC11dp`, `dC12dp`, `dC44dp`, `dBdp`, `dCdp`, `cohesive_energy`
  - `units`:
    - `C11`: 10^11 N/m^2
    - `C12`: 10^11 N/m^2
    - `C111`: 10^11 N/m^2
    - `C112`: 10^11 N/m^2
    - `C123`: 10^11 N/m^2
    - `dC11dp`: dimensionless
    - `dC12dp`: dimensionless
    - `dC44dp`: dimensionless
    - `dBdp`: dimensionless
    - `dCdp`: dimensionless
    - `cohesive_energy`: eV/atom

Notes: All values must be provided for each (metal, n, m) combination listed in the paper's Table 2. The scoring compares the agent's reported values to hidden reference values (the paper's own computed numbers) using relative tolerances.

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
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "n",
          "m",
          "C11",
          "C12",
          "C111",
          "C112",
          "C123",
          "dC11dp",
          "dC12dp",
          "dC44dp",
          "dBdp",
          "dCdp",
          "cohesive_energy"
        ],
        "units": {
          "C11": "10^11 N/m^2",
          "C12": "10^11 N/m^2",
          "C111": "10^11 N/m^2",
          "C112": "10^11 N/m^2",
          "C123": "10^11 N/m^2",
          "dC11dp": "dimensionless",
          "dC12dp": "dimensionless",
          "dC44dp": "dimensionless",
          "dBdp": "dimensionless",
          "dCdp": "dimensionless",
          "cohesive_energy": "eV/atom"
        }
      },
      "description": "Computed elastic constants, pressure derivatives, and cohesive energy for each metal and (n,m) parameter set."
    }
  ],
  "notes": "All values must be provided for each (metal, n, m) combination listed in the paper's Table 2. The scoring compares the agent's reported values to hidden reference values (the paper's own computed numbers) using relative tolerances."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads results.csv and, for each row, compares each numerical value to a hidden reference. Scoring uses relative tolerances: larger errors reduce credit. Each column across all rows contributes to the total reward. The verifier does not check intermediate files; only the final CSV is scored. Therefore, merely printing the expected numbers without executing the actual computation will not guarantee full credit, as the tolerances are set to distinguish a genuine re-implementation from a generic guess.
