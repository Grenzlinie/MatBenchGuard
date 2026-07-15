# Pair-energy differences of hydrogen atoms at tetrahedral interstitial sites in bcc iron

## Problem background
Hydrogen solubility and diffusion in α-iron is critical for understanding steel properties, yet few electronic‑structure calculations have addressed hydrogen–hydrogen interactions. This work uses a tight‑binding band‑structure calculation based on the extended Hückel formalism to compute total electronic energies of Fe–H systems with two hydrogen atoms placed at tetrahedral interstitial sites. The computational objective is to determine the pair‑energy differences between the different relative configurations, which quantify the repulsive interactions and identify the most stable arrangement of hydrogen pairs in bcc iron.

## Approach
The method employs the tight‑binding extended Hückel Hamiltonian to compute the band‑structure total energy of a cubic unit cell containing two Fe atoms and two H atoms. The bcc lattice constant *a* is the standard value for α‑iron (≈ 2.866 Å). The Fe atoms sit at (0,0,0) and (*a*/2,*a*/2,*a*/2). One hydrogen is fixed at the tetrahedral site **T** = (*a*/4)(0,2,‑1). The second hydrogen is placed at each of four neighbouring sites: **T₁** = (*a*/4)(1,2,0), **T₂** = (*a*/4)(0,2,1), **T₃** = (*a*/4)(2,1,0), **T₄** = (*a*/4)(2,0,‑1). For each pair geometry (T,T_i) we construct the Hamiltonian with the following extended Hückel parameters:

- H 1s: on‑site energy –11.3 eV, Slater exponent 1.3
- Fe 4s: –11.0 eV, exponent 1.8
- Fe 4p: –7.0 eV, exponent 1.8
- Fe 3d: –12.5 eV, double‑zeta: exponents 5.36 (coefficient 0.604) and 1.8 (coefficient 0.604)

The off‑diagonal matrix elements *Hᵢⱼ* are obtained from the overlap elements *Sᵢⱼ* and the on‑site energies using the weighted formula. The k‑point mesh is generated from the special point *k* = (1/8)(1,1,1) with symmetry reduction (Chadi–Cohen scheme); the number of irreducible points varies with the geometry. The Hamiltonian is diagonalized at each k‑point to obtain the band energies, and the total electronic energy *E*(T,T_i) is computed by summing over occupied states. The pair‑energy differences are then Δ*E*(T₃,T_i) = *E*(T,T_i) – *E*(T,T₃).

## Reproduction target
Compute the four pair‑energy differences Δ*E*(T₃,T_i) for i = 1…4 and write them to `/app/outputs/energy_differences.csv`. The file must contain two columns, `neighbor` (integer 1–4) and `delta_E_meV` (float, in meV). Row order is arbitrary, but each neighbor index must appear exactly once. The values must be obtained from your own implementation of the tight‑binding extended Hückel method as described above; do not simply quote a known result.

## Assets
The task requires no external datasets, models, or pre‑trained weights. The Hamiltonian parameters are provided above. To implement the tight‑binding solver, you may use general‑purpose scientific libraries (NumPy, SciPy) or a dedicated open‑source package such as `pythtb` (https://www.physics.rutgers.edu/pythtb/). The lattice constant of α‑iron (≈ 2.866 Å) is a standard physical value; you may use any reliable reference.

## Workflow steps

### Step 1: Set up geometry and Hamiltonian
- Role: process
- Action: Define the bcc Fe lattice with lattice constant a, place Fe atoms, and set up the four hydrogen-pair configurations at tetrahedral interstitial sites (T,T1) through (T,T4) as specified. Construct the tight-binding Hamiltonian using the extended Hückel parameters (on-site energies, Slater exponents, double-zeta 3d for Fe) as listed in the paper.
- Evidence: none

### Step 2: Compute total electronic energies
- Role: process
- Action: For each of the four pair geometries, perform the tight-binding band-structure calculation using a k-point mesh derived from k=(1/8)(1,1,1) with symmetry reduction. Diagonalise the Hamiltonian at each k-point and obtain the total electronic band-structure energy E(T,T_i).
- Evidence: `/app/outputs/total_energies.csv`

### Step 3: Calculate pair-energy differences
- Role: scored (load-bearing)
- Action: From the computed total energies E(T,T_i) for i=1..4, calculate the pair-energy differences ΔE(T3,T_i) = E(T,T_i) − E(T,T_3) in meV. Write the four values to the output CSV.
- Output file: `/app/outputs/energy_differences.csv`
- Format: csv
- Contract: Two columns: 'neighbor' (integer 1-4) and 'delta_E_meV' (float, in meV). Row order is arbitrary but each neighbor 1..4 must appear exactly once.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/energy_differences.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### energy_differences.csv
- path: `/app/outputs/energy_differences.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The four pair-energy differences for hydrogen atoms at tetrahedral interstitial sites in bcc iron, computed as ΔE(T3,T_i) for i=1..4.
- schema:
  - `type`: table
  - `required_columns`: `neighbor`, `delta_E_meV`
  - `units`:
    - `delta_E_meV`: meV

Notes: The checker will compare the reported values to the paper-reported reference values with an absolute tolerance and verify the relative ordering ΔE(1) > ΔE(2) > ΔE(4) > ΔE(3)=0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "energy_differences.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "neighbor",
          "delta_E_meV"
        ],
        "units": {
          "delta_E_meV": "meV"
        }
      },
      "description": "The four pair-energy differences for hydrogen atoms at tetrahedral interstitial sites in bcc iron, computed as ΔE(T3,T_i) for i=1..4."
    }
  ],
  "notes": "The checker will compare the reported values to the paper-reported reference values with an absolute tolerance and verify the relative ordering ΔE(1) > ΔE(2) > ΔE(4) > ΔE(3)=0."
}
```

## How you are scored
A hidden verifier reads your `energy_differences.csv` and compares each Δ*E* value against the reference results from the original study. The comparison uses an absolute tolerance that accounts for legitimate differences due to implementation details (different code, numerical libraries). The verifier also checks that the set of values satisfies certain monotonic ordering relationships that a correct physical reproduction must exhibit. The final score is a number between 0 and 1, reflecting both the proportion of values within tolerance and the structural consistency. Simply copying a known number is not sufficient – the outputs must be produced by the full tight‑binding workflow.
