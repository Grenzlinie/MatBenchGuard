# Finite-size scaling analysis of magnetic hard hexagon model via Monte Carlo simulation

## Problem background
The magnetic hard hexagon model on a triangular lattice extends the usual nearest-neighbour exclusion by two-body restrictions that depend on the orientation (up/down) of occupied sites. A site can be empty, occupied by an up magnetic hard hexagon, or occupied by a down one. The model is defined by a partition function with activity z and a restriction factor that penalises certain nearest-, next-nearest- and third-nearest-neighbour pair configurations. Varying z is expected to drive the system through different collective behaviours. A finite-size scaling analysis of the sublattice squared-sum observable A_z (Eq. (13)) provides a diagnostic: the behaviour of the correlation exponent η, extracted from the scaling A_z ∝ L^{2‑η}, distinguishes a disordered regime, a critical regime where η takes a finite value less than ½, and an ordered regime where η tends to zero. The objective here is to compute A_z for a grid of activities and system sizes and to let a hidden checker decide, from those A_z values, which phase each simulated point belongs to.

## Approach
The workhorse is a Metropolis Monte Carlo simulation of the magnetic hard hexagon model on a triangular lattice with periodic boundary conditions. The effective temperature is set to T = 1/ln(z) (kB = 1). At each MC step a site is selected and the algorithm proposes to change its occupation (insert, remove, or flip sign). The trial move is accepted with probability min(1, z^{Δn} R{ζ}_proposed / R{ζ}_old), where Δn is the change in the number of occupied sites and R{ζ} is the product of restriction factors given in the paper (Eq. (11)). After a long equilibration period, the observable A_z = (1/L²) ⟨(∑_{i∈A} ζ_i)² + (∑_{j∈B} ζ_j)² + (∑_{k∈C} ζ_k)²⟩ is measured over a large number of MC steps; A, B, C are the three triangular sublattices. Simulations are carried out for a preset list of activities z and linear system sizes L. The raw collected values of A_z are then used by the checker to extract η via pairwise finite-size scaling and to draw conclusions about the phase behaviour.

## Reproduction target
Run the Monte Carlo simulation outlined above for each activity z ∈ {1, 2, 3, 3.5, 4, 5, 5.5, 6, 6.5, 7} and each linear system size L ∈ {24, 36, 48, 60, 90, 120}. For every (z, L) pair, after equilibration compute the time-averaged A_z and write a CSV file `az_data.csv` with columns: `z` (int), `L` (int), `A_z` (float). One row per (z, L) pair. The hidden checker will read this file, compute pairwise η estimates from the A_z values, and assess whether the resulting η trends are consistent with the expected phase diagram (disordered, critical, ordered) within hidden tolerances.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Monte Carlo simulation and A_z measurement
- Role: scored (load-bearing)
- Action: Implement a Metropolis Monte Carlo simulation for the magnetic hard hexagon model on a triangular lattice with periodic boundary conditions, using the occupation variables and restriction factor defined in the paper. For each activity z in {1,2,3,3.5,4,5,5.5,6,6.5,7} and each linear system size L in {24,36,48,60,90,120}, run the simulation using at least 10^5 Monte Carlo steps per site. After equilibration, compute the sublattice squared‑sum observable A_z = (1/L²)⟨(∑_{i∈A} ζ_i)² + (∑_{j∈B} ζ_j)² + (∑_{k∈C} ζ_k)²⟩ where A, B, C are the three triangular sublattices. Write the resulting A_z values for all (z, L) pairs to az_data.csv.
- Output file: `/app/outputs/az_data.csv`
- Format: csv
- Contract: Columns: z (int), L (int), A_z (float). One row per (z, L) pair.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/az_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### az_data.csv
- path: `/app/outputs/az_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Monte Carlo estimate of the sublattice squared‑sum observable A_z for all specified (z, L) pairs. The hidden checker recomputes the correlation‑decay exponent eta from these values and scores the phase‑classification consistency.
- schema:
  - `type`: table
  - `required_columns`: `z`, `L`, `A_z`
  - `units`:
    - `A_z`: dimensionless

Notes: The solver must compute A_z from its own simulation; numerical values are determined by the MC run. The checker will recompute eta using pairwise finite‑size scaling and compare against hidden tolerance bands derived from the paper’s reported trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "az_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "L",
          "A_z"
        ],
        "units": {
          "A_z": "dimensionless"
        }
      },
      "description": "Monte Carlo estimate of the sublattice squared‑sum observable A_z for all specified (z, L) pairs. The hidden checker recomputes the correlation‑decay exponent eta from these values and scores the phase‑classification consistency."
    }
  ],
  "notes": "The solver must compute A_z from its own simulation; numerical values are determined by the MC run. The checker will recompute eta using pairwise finite‑size scaling and compare against hidden tolerance bands derived from the paper’s reported trends."
}
```

## How you are scored
A hidden verifier automatically evaluates the submitted `az_data.csv`. It recomputes the correlation exponent η for each activity z using finite-size scaling: η(L_{i+1}) = 2 − ln(A_z(L_{i+1})/A_z(L_i)) / ln(L_{i+1}/L_i). The resulting η values are compared to hidden tolerance bands and threshold windows derived from the paper's reported phase classification. The final score reflects how closely the computed A_z values reproduce the expected phase behaviour—disordered, critical, or ordered—as inferred from η. The verifier's reference values and tolerances are not disclosed in the instructions.
