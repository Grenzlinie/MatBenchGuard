# Generalized Thomson Problem: Continuum Theory Coefficient a1

## Problem background
The generalized Thomson problem asks for the ground state configurations of M point particles on a sphere that interact via a long-range repulsive potential of the form e^2/r^γ, where 0 < γ < 2. A continuum elastic theory of disclinations provides a quantitative route to predict the ground state energy and defect arrangements without performing direct particle simulations. In the large-M limit, the ground state energy per configuration admits an asymptotic expansion

E_G = (e^2/(2R^γ))[ a0(γ) M^2 - a1(γ) M^{1+γ/2} + a2(γ) M^{γ/2} + ... ],

where R is the sphere radius and a0, a1, a2 are potential- and configuration-dependent coefficients. The subleading coefficient a1(γ) carries the leading non-extensive contribution and depends on the arrangement of the 12 required topological defects (disclinations) that the crystal accommodates on the sphere. For the two families of icosadeltahedral lattices — denoted (n,0) and (n,n) — a1 can be evaluated from the continuum defect-interaction model. This task computes a1(γ) for both lattice types at several values of the potential exponent γ.

## Approach
The computation proceeds in two conceptual stages, grounded in the continuum elastic description of a spherical crystal with disclinations.

First, the flat-space elastic properties of the same power-law interaction must be obtained. For a two-dimensional triangular lattice, Ewald summation is used to compute the Young modulus Y(γ) and the defect‑free reference energy E0(γ) of the pair potential e^2/r^γ. This yields potential‑dependent coefficients that enter the spherical defect energy.

Second, the disclination configuration on the sphere is modelled by placing 12 topological charges (five-fold and seven-fold disclinations) at the vertices of an icosahedron — the geometry that defines the (n,0) or (n,n) icosadeltahedral lattice. The continuum energy of such a configuration consists of a pair‑wise interaction between disclinations mediated by a spherical kernel χ, which depends on the geodesic distance β between defects and involves an integral. The total energy also receives a contribution from the flat‑space reference energy and the area per particle, which for M particles on the sphere is A_C = 4πR^2/M.

By substituting the flat‑space constants and A_C into the spherical defect energy and expanding the resulting expression for large M, the term linear in M^{1+γ/2} yields the coefficient a1(γ). The agent must implement the Ewald summation, evaluate the spherical kernel, construct the disclination positions for each lattice type, perform the energy expansion, and extract a1 for each (γ, lattice_type) pair.

## Reproduction target
Compute the subleading coefficient a1(γ) in the large‑M asymptotic expansion of the ground state energy for the generalized Thomson problem on a sphere, using the continuum defect‑interaction model. The required outputs are a1 values for the five potential exponents γ ∈ {1.5, 1.25, 1.0, 0.75, 0.5} and for both (n,0) and (n,n) icosadeltahedral lattice configurations. Write the results as a CSV file `/app/outputs/a1_coefficients.csv` with columns: gamma (float), lattice_type (string, one of `n0` or `nn`), a1 (float). One row per (gamma, lattice_type) combination (10 rows total).

## Assets

- numpy/scipy: numpy scipy

## Workflow steps

### Step 1: Flat-space elastic constants and reference energy
- Role: process
- Action: Use Ewald summation on a 2D triangular lattice to compute the flat-space Young modulus Y(gamma) and defect-free reference energy E0(gamma) for the long-range pair potential e^2/r^gamma (0<gamma<2). Determine the potential-dependent coefficients required as input for the spherical defect model. Store the numerical values.
- Evidence: `/app/outputs/flat_constants.json`

### Step 2: Compute a1 coefficient for icosadeltahedral lattices
- Role: scored (load-bearing)
- Action: For each gamma in {1.5, 1.25, 1.0, 0.75, 0.5} and each lattice type ((n,0) and (n,n)), construct the icosadeltahedral disclination configuration on the sphere. Evaluate the total continuum energy using the spherical defect interaction kernel and the flat-space coefficients from the previous step. Substitute A_C = 4πR^2/M and expand the energy in asymptotic powers of M to extract the subleading coefficient a1(gamma). Write the results to a CSV file.
- Output file: `/app/outputs/a1_coefficients.csv`
- Format: csv
- Contract: Columns: gamma (float, potential exponent), lattice_type (string, one of 'n0' or 'nn'), a1 (float, the subleading coefficient). One row per (gamma, lattice_type) combination, covering gamma in {1.5,1.25,1.0,0.75,0.5} and lattice_type in ('n0','nn').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/a1_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### a1_coefficients.csv
- path: `/app/outputs/a1_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed subleading coefficient a1 for the generalized Thomson problem on a sphere, using continuum defect theory, for both (n,0) and (n,n) icosadeltahedral lattices at five values of gamma.
- schema:
  - `type`: table
  - `required_columns`: `gamma`, `lattice_type`, `a1`

Notes: The checker will compare each submitted a1 value to the paper-reported theoretical prediction, using a relative tolerance large enough to absorb legitimate numerical differences from re-implementing the Ewald method and spherical kernel.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "a1_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "gamma",
          "lattice_type",
          "a1"
        ]
      },
      "description": "Computed subleading coefficient a1 for the generalized Thomson problem on a sphere, using continuum defect theory, for both (n,0) and (n,n) icosadeltahedral lattices at five values of gamma."
    }
  ],
  "notes": "The checker will compare each submitted a1 value to the paper-reported theoretical prediction, using a relative tolerance large enough to absorb legitimate numerical differences from re-implementing the Ewald method and spherical kernel."
}
```

## How you are scored
A hidden verifier inspects your output CSV file independently. It first checks that the file is well‑formed, contains the required columns (gamma, lattice_type, a1), and includes one row for each of the five γ values and two lattice types. The core scoring then compares each a1 value you submit to a hidden reference a1 value (obtained from the paper's own theoretical prediction) using a tolerance that allows for the legitimate numerical spread introduced by re‑implementing the Ewald summation and the spherical defect kernel. For each row, if the deviation falls within the tolerance the row is considered correct. Your final reward is the fraction of rows that pass, so the reward increases smoothly as more of your computed a1 coefficients agree with the hidden reference. No other artifacts are scored.
