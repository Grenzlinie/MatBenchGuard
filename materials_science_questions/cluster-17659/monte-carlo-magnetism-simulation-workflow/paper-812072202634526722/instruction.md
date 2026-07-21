# Steplike magnetization of spin chains in a triangular lattice: Monte Carlo simulation

## Problem background
Certain one-dimensional spin-chain compounds crystallize in a triangular lattice arrangement and display intriguing magnetization behavior at low temperatures. Their magnetization versus external magnetic field often exhibits a steplike pattern—a series of plateaus separated by sharp jumps. This work proposes a two-dimensional Ising-like model in which each spin chain behaves as a rigid giant Ising spin, and the interchain coupling includes quenched randomness. The goal is to implement a Metropolis Monte Carlo simulation of this model and compute the magnetization curve for two temperatures, allowing the plateau structure and transition fields to be examined.

## Approach
The system is approximated as a 100×100 triangular lattice where each site represents an entire spin chain with effective spin ±S^e. Nearest-neighbor interactions are antiferromagnetic (J>0) and include a random component drawn from span·J·Uniform[-1,1]. The Hamiltonian contains a Zeeman term coupling the spins to an external magnetic field h. To obtain the magnetization curve, the Metropolis algorithm is used: at a fixed temperature T, the simulation starts from a random spin configuration, sweeps h from 0 to 5 T in small steps, and at each field allows the lattice to equilibrate before measuring the average magnetization. The process is repeated for multiple independent random seeds and the results are averaged. The raw magnetization is normalized by the saturation value N·S^e to yield the dimensionless quantity M/M0. The entire procedure is implemented from scratch using standard Python numerical libraries.

## Reproduction target
Produce the file `magnetization_curves.csv` containing the normalized magnetization M/M0 as a function of applied field h for temperatures T = 2 K and T = 10 K, using the model and parameter values detailed in the workflow step. The file must span h from 0 to 5 T in steps no larger than 0.1 T. This single output artifact will be inspected by a verifier that evaluates the plateau structure and transition positions.

## Assets

- NumPy: numpy

## Workflow steps

### Step 1: Monte Carlo simulation of magnetization curves
- Role: scored (load-bearing)
- Action: Implement a Metropolis Monte Carlo simulation of the 2D triangular-lattice Ising model with random interchain exchange. Each spin chain is treated as a rigid giant Ising spin with two projections ±S^e. The Hamiltonian includes nearest-neighbor antiferromagnetic coupling J>0, quenched random exchange Δ_m,n = span·J·RAM (RAM uniform in [−1,1]), and Zeeman term −h μB g S^e. Use the parameter set from the paper: kB=1.3807e-23 J/K, J=3.592e-25 J, μB=9.274e-24 J/T, g=2, S^e=32, span=0.15. Simulate a 100×100 lattice with periodic boundary conditions. For each of the two temperatures T=2 K and T=10 K, sweep the external magnetic field h from 0 to 5 T in steps no larger than 0.1 T. At each (T, h) point, equilibrate the system using the Metropolis algorithm, then measure the average magnetization over subsequent Monte Carlo steps, averaging over 10 independent random seeds. Normalize the total magnetization by the saturation value M0 = N·S^e (N=10000). Produce a single CSV file containing the resulting magnetization curves.
- Output file: `/app/outputs/magnetization_curves.csv`
- Format: csv
- Contract: CSV with columns: T (float, K), h (float, T), M_M0 (float, dimensionless). Rows cover h from 0.0 to 5.0 T in steps no larger than 0.1 T, for T values 2.0 K and 10.0 K. M_M0 is total magnetization divided by N*S^e (N=10000, S^e=32).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetization_curves.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetization_curves.csv
- path: `/app/outputs/magnetization_curves.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Simulated magnetization curves for temperatures 2 K and 10 K. The checker will compute the derivative d(M_M0)/dh, detect step transitions, and verify the number of steps and their critical field positions against the paper’s reported behavior.
- schema:
  - `type`: table
  - `required_columns`: `T`, `h`, `M_M0`
  - `columns`:
    - `T`: float (K)
    - `h`: float (T)
    - `M_M0`: float (dimensionless)

Notes: Only the magnetization curves for the two temperatures are scored. The agent is not required to produce spin configuration snapshots, phase diagrams, or analysis of varying disorder strength.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetization_curves.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "h",
          "M_M0"
        ],
        "columns": {
          "T": "float (K)",
          "h": "float (T)",
          "M_M0": "float (dimensionless)"
        }
      },
      "description": "Simulated magnetization curves for temperatures 2 K and 10 K. The checker will compute the derivative d(M_M0)/dh, detect step transitions, and verify the number of steps and their critical field positions against the paper’s reported behavior."
    }
  ],
  "notes": "Only the magnetization curves for the two temperatures are scored. The agent is not required to produce spin configuration snapshots, phase diagrams, or analysis of varying disorder strength."
}
```

## How you are scored
A hidden verifier loads your `magnetization_curves.csv`, groups the data by temperature, and examines each curve. It compares the observed pattern of plateaus and jumps to the expected behavior that follows from a correct implementation of the described model. The score reflects how closely your simulation reproduces the key qualitative and quantitative features—not simply whether a file was written. Only the final CSV is scored; intermediate logs or other artifacts are not evaluated.
