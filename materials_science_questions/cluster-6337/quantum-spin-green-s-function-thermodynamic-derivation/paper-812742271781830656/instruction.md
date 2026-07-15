# Quantum Spin-1/2 XY Hamiltonian Ground-State Observables via Linear Spin-Wave Theory

## Problem background
Quantum spin models with continuous symmetry, such as the spin-1/2 XY Hamiltonian, describe physical systems including quantum lattice fluids and magnetic insulators. Understanding their ground-state properties—energy, local occupation, spin correlations, and long-range order—is a fundamental problem in condensed matter physics. Approximate methods like spin-wave theory (Holstein-Primakoff bosonization) are widely used, but conventional quantization choices have produced unsatisfactory results. A specific quantization scheme, with the axis lying in the interaction plane, has been shown to yield accurate ground-state properties. This task asks you to compute those properties for three simple bipartite lattices using linear spin-wave theory.

## Approach
Use the Holstein-Primakoff boson representation for spin-1/2 operators, choosing the quantization axis in the plane of the XY interaction. The linearized spin-wave Hamiltonian is diagonalized via a Bogoliubov transformation, which leads to closed-form expressions for the ground-state energy per site (E/(NJ)), local occupation number (n), nearest-neighbor out-of-plane correlation (⟨S₀ʸ S₁ʸ⟩), and the squared magnetization along the quantization axis (⟨M_z²⟩/N²). These quantities are computed as k-space sums over the Brillouin zone that involve the lattice structure factor S(k) = Σᵢ₌₁ᶻ cos(k·δᵢ). The task is purely numerical: implement these expressions and evaluate the sums for three bipartite lattices—linear chain (coordination z=2), square lattice (z=4), and simple cubic lattice (z=6). No external data are needed; the lattice geometry and coordination numbers are the only inputs.

## Reproduction target
Compute the four ground-state quantities (energy per site, occupation number, out-of-plane nearest-neighbor correlation, and squared magnetization) for the linear chain, square lattice, and simple cubic lattice by numerically evaluating the required k-space integrals or sums over the Brillouin zone. Write the results to a CSV file with columns: lattice, energy_per_site, occupation_number, out_of_plane_correlation, squared_magnetization. The lattice label must be a string (for example, 'linear_chain', 'square_lattice', 'simple_cubic'). All other values must be floating-point numbers, except for the linear chain where the occupation integral diverges—in that case set occupation_number to the string 'Inf'.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Numerical evaluation of spin-wave ground-state observables
- Role: scored (load-bearing)
- Action: Implement the linear spin-wave (Holstein-Primakoff) formalism for the spin-1/2 XY Hamiltonian on bipartite lattices with quantization axis in the interaction plane. Compute the ground-state energy per site (E/NJ), local occupation number (n), out-of-plane nearest-neighbor correlation (<S0_y S1_y>), and squared magnetization (<M_z^2>/N^2) for the linear chain (coordination z=2), square lattice (z=4), and simple cubic lattice (z=6) by numerically evaluating the required k-space sums over the Brillouin zone. For the one-dimensional chain the occupation integral diverges; set occupation_number to 'Inf' in that case. Write the results to results.csv.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: Header: lattice,energy_per_site,occupation_number,out_of_plane_correlation,squared_magnetization. Each row: lattice label (string), numeric values as floats (occupation_number may be string 'Inf' for the linear chain).
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
- description: Reproduced ground-state properties from the linear spin-wave calculation, to be compared against reference values from the paper using a tolerance-based comparison.
- schema:
  - `type`: table
  - `required_columns`: `lattice`, `energy_per_site`, `occupation_number`, `out_of_plane_correlation`, `squared_magnetization`
  - `notes`: lattice is a string (linear_chain, square_lattice, simple_cubic); other columns are numeric floats except occupation_number which may be the string 'Inf' for the linear chain.

Notes: Scored by result-level comparison against hidden gold values extracted from the paper's Tables I-III, using absolute tolerance 1e-4 for finite quantities; the linear chain occupation number passes automatically if set to 'Inf'.

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
          "lattice",
          "energy_per_site",
          "occupation_number",
          "out_of_plane_correlation",
          "squared_magnetization"
        ],
        "notes": "lattice is a string (linear_chain, square_lattice, simple_cubic); other columns are numeric floats except occupation_number which may be the string 'Inf' for the linear chain."
      },
      "description": "Reproduced ground-state properties from the linear spin-wave calculation, to be compared against reference values from the paper using a tolerance-based comparison."
    }
  ],
  "notes": "Scored by result-level comparison against hidden gold values extracted from the paper's Tables I-III, using absolute tolerance 1e-4 for finite quantities; the linear chain occupation number passes automatically if set to 'Inf'."
}
```

## How you are scored
A hidden verifier reads your results.csv and compares each numeric quantity against a hidden reference value (derived from standard published literature) using an appropriate tolerance. The occupation number for the linear chain is checked only that it is the string 'Inf'; if so, that row's occupation passes automatically. For finite quantities the verifier uses an absolute tolerance; each comparison is scored independently. The total reward is the fraction of those comparisons that pass tolerance. There is no partial credit for individual quantities; the verifier checks only the final output file and does not inspect your code or intermediate files.
