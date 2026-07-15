# Renormalized Couplings from 2D Ising MCRG via Schwinger-Dyson Equations

## Problem background
Determining the effective (renormalized) couplings of Ising spin systems from Monte Carlo data is a central task in Monte Carlo renormalization group (MCRG) studies. Given a critical spin configuration, one applies a blocking transformation to obtain coarse-grained variables, and the challenge is to extract the renormalized Hamiltonian that describes these block variables. The problem is to invert the mapping from couplings to observable expectation values, using only a single set of Monte Carlo measurements. This task addresses the determination of the renormalized couplings of the two‑dimensional square‑lattice Ising model at its critical point, using a method based on Schwinger‑Dyson equations that requires no iterative tuning of trial couplings.

## Approach
The core idea is to exploit exact relations (Schwinger‑Dyson equations) that link the expectation of a conditional spin flip to the local effective magnetic field acting on that spin. For a given lattice site, the action can be split into a term −σ_i0 W_i0, where W_i0 is a linear combination of the unknown renormalized couplings multiplied by products of neighboring spins. By classifying each site’s neighbor spin pattern into a finite set of classes (defined by the relative positions of neighbors up to fifth neighbour, plus two four‑spin operators — a plaquette and a sublattice plaquette), one obtains for each class r a relation W_r = 0.5 ln(N_r⁺/N_r⁻), where N_r⁺ (N_r⁻) count the occurrences of the central spin being +1 (−1) when the neighbors belong to class r. The local field W_r is a linear combination of the seven unknown couplings J₁,…,J₇. Instead of solving a small subset of equations, the method minimises a χ² function χ² = Σ_r (ξ_r − W_r)²/σ²(r), where ξ_r and σ(r) are measured from the simulation. This approach requires only ONE Monte Carlo simulation, from which all blocking levels and all couplings can be obtained.

The workflow proceeds as follows: (1) Run a heat‑bath Monte Carlo simulation of the 2D Ising model on a 32×32 lattice at the critical coupling Jc = 0.440687, performing 2.4×10⁶ sweeps after equilibration. From the equilibrium configurations, generate block‑spin configurations for three blocking levels using the majority rule. For each blocking level, accumulate the counts N_r⁺ and N_r⁻ for every neighbor class r. (2) From the accumulated counts, compute ξ_r = 0.5 ln(N_r⁺/N_r⁻) and its statistical uncertainty σ(r) using the binomial counting formula σ²(r) = (N_r⁺+N_r⁻)/(4 N_r⁺ N_r⁻). For each class, also record the seven linear coefficients that express W_r as ∑_i J_i·(coeff_i). Write these data, together with the level and class identifier, to a CSV file.

## Reproduction target
Produce a CSV file `expectations.csv` containing, for each blocking level (0,1,2,3) and each neighbor configuration class r encountered in the simulation, the following columns:
- level (int): blocking level
- class_r (string): a unique label for the neighbor class (e.g., a bitstring or index)
- J1_coeff, …, J7_coeff (float): the coefficients that multiply the unknown couplings J₁…J₇ in the expression W_r = Σ J_i·(coeff_i)
- Xi (float): the measured ξ_r = 0.5 ln(N_r⁺/N_r⁻)
- sigma (float): the statistical uncertainty of ξ_r (standard deviation)

The file must be saved at `/app/outputs/expectations.csv`. The hidden verifier will subsequently read this file, perform the χ² fit to obtain the seven renormalized couplings for each level, and then compare the fitted couplings to a set of hidden reference values. Your goal is to supply accurate ξ_r, σ(r), and coefficient values, so that the resulting fitted couplings are as close as possible to the hidden true couplings.

## Assets

- Python scientific stack (numpy, scipy, pandas): numpy, scipy, pandas

## Workflow steps

### Step 1: Monte Carlo simulation and neighbor count accumulation
- Role: process
- Action: Implement the heat-bath algorithm for the 2D Ising model on a 32×32 square lattice at the critical coupling Jc = 0.440687. Perform 2.4×10^6 sweeps after equilibration. For each equilibrium configuration, apply majority-rule blocking to generate block configurations for blocking levels 1, 2, and 3. For each lattice site at each blocking level, classify the neighbor configuration into one of 6863 classes based on the seven operators (nearest neighbour, next-nearest neighbour, third neighbour, fourth neighbour, fifth neighbour, four-spin plaquette, four-spin sublattice plaquette) and accumulate counts N_r^+ and N_r^-.
- Evidence: none

### Step 2: Compute expectation values and linear coefficients
- Role: scored (load-bearing)
- Action: Using the accumulated counts N_r^+ and N_r^- from the simulation, compute ξ_r = 0.5 ln(N_r^+ / N_r^-) and σ(r) using the binomial formula σ²(r) = (N_r⁺ + N_r⁻) / (4 N_r⁺ N_r⁻) for each class r at each blocking level. Also compute the linear coefficients J1_coeff,…,J7_coeff that express the local field W_r as a linear combination of the seven unknown couplings for each class r. Write a CSV file `expectations.csv` with columns: level (int), class_r (str), J1_coeff, J2_coeff, J3_coeff, J4_coeff, J5_coeff, J6_coeff, J7_coeff (float), Xi (float), sigma (float).
- Output file: `/app/outputs/expectations.csv`
- Format: csv
- Contract: level: int, class_r: string, J1_coeff: float, J2_coeff: float, J3_coeff: float, J4_coeff: float, J5_coeff: float, J6_coeff: float, J7_coeff: float, Xi: float, sigma: float
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/expectations.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### expectations.csv
- path: `/app/outputs/expectations.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw expectation data and design‑matrix coefficients that allow the hidden checker to refit the seven couplings and compute χ²/DF.
- schema:
  - `type`: table
  - `required_columns`: `level`, `class_r`, `J1_coeff`, `J2_coeff`, `J3_coeff`, `J4_coeff`, `J5_coeff`, `J6_coeff`, `J7_coeff`, `Xi`, `sigma`

Notes: The hidden checker will read expectations.csv, build the weighted design matrix for each blocking level, solve the linear least‑squares problem to obtain J₁–J₇ and χ²/DF, then compare the resulting couplings to the paper’s reported values (Table 2 row A) using tolerance = 3 × the paper’s statistical errors.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "expectations.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "level",
          "class_r",
          "J1_coeff",
          "J2_coeff",
          "J3_coeff",
          "J4_coeff",
          "J5_coeff",
          "J6_coeff",
          "J7_coeff",
          "Xi",
          "sigma"
        ]
      },
      "description": "Raw expectation data and design‑matrix coefficients that allow the hidden checker to refit the seven couplings and compute χ²/DF."
    }
  ],
  "notes": "The hidden checker will read expectations.csv, build the weighted design matrix for each blocking level, solve the linear least‑squares problem to obtain J₁–J₇ and χ²/DF, then compare the resulting couplings to the paper’s reported values (Table 2 row A) using tolerance = 3 × the paper’s statistical errors."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/expectations.csv`. For each blocking level, it will build a weighted design matrix using the rows whose σ(r) is positive, with weights 1/σ²(r). It will then solve the linear least‑squares problem to obtain the best‑fit couplings J₁,…,J₇ and compute the χ² per degree of freedom (χ²/DF). The fitted couplings will be compared against a set of hidden gold values using predefined tolerances that account for statistical fluctuations and implementation‑dependent differences. The reward is monotonic in the quality of your results: full credit is awarded when every coupling falls within its tolerance; otherwise, partial credit is proportional to the fraction of couplings that are within tolerance. The verifier does NOT require you to output the fitted couplings itself — only the raw expectation data and the linear coefficients from which the fit can be recomputed.
