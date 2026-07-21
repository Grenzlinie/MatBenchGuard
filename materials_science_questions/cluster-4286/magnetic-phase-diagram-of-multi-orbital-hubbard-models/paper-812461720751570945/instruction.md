# Magnetic Phase Diagram of the Single-Band Hubbard Model on Bipartite Lattices via Slave-Boson Mean-Field Theory

## Problem background
Magnetic clusters and nanoparticles display size‑dependent magnetic properties because of reduced coordination and enhanced electron correlations. The single‑band Hubbard model captures the fundamental competition between electron delocalization (hopping) and on‑site Coulomb repulsion. This task investigates the ground‑state magnetic behaviour (paramagnetic, ferromagnetic, antiferromagnetic) and key electronic properties (local magnetic moment, average double occupation, hopping renormalization) of bipartite clusters, treated within the Kotliar–Ruckenstein slave‑boson mean‑field approximation and a third‑moment expansion of the local density of states. The goal is to determine how these quantities depend on the local coordination number z, the Coulomb interaction strength U/t, and the band filling n.

## Approach
Consider the single‑band Hubbard Hamiltonian:

H = -t Σ_{⟨i,j⟩,σ} c^†_{iσ} c_{jσ} + U Σ_i n_{i↑} n_{i↓}

Electron correlations are treated with the Kotliar–Ruckenstein slave‑boson method. In the saddle‑point approximation, the system is described by an effective Hamiltonian of independent quasiparticles with shifted site energies ε'_{iσ} and renormalised hoppings t'_{ijσ} = q^σ_{ij} t, where the factor q^σ_{ij} depends on the average boson occupations (empty, singly‑occupied, doubly‑occupied). The ground‑state averages are obtained by minimising the electronic energy

E = Σ_{iσ} ∫_{-∞}^{ε_F} (ε – ε'_{iσ}) ρ_{iσ}(ε) dε + U Σ_i d^2_i ,

where ρ_{iσ}(ε) is the local density of states (LDOS) and d^2_i is the average double occupation. The LDOS is approximated by a third‑moment real‑space expansion. On bipartite structures with equal sublattice sizes (N_A = N_B) and a staggered potential Δ (Δ_i = +Δ/2 on sublattice A and –Δ/2 on sublattice B for up spins, with opposite sign for down spins), the LDOS takes the form

ρ_{iσ}(ε) = (b/(π)) * √[1 – ((ε – σΔ_i/2)/(2b))^2] / ( σΔ_i (ε + σΔ_i/2) + b^2 ) ,

with an effective band width parameter b² = z (q^σ t)² (z is the coordination number).

For each set of parameters (n, z, U/t) and magnetic trial state (paramagnetic, ferromagnetic, antiferromagnetic) the self‑consistent equations for the electron number, magnetic moment, and double occupation are solved, and the total energy is minimised. The ground‑state magnetic order is the trial state with the lowest energy. No more complex magnetic structures are considered.

The computed quantities are: local magnetic moment μ, average double occupation d², and hopping renormalisation factor q (for AF/PM q^↑ = q^↓; for FM q^↑ and q^↓ may differ).

## Reproduction target
Implement the above approach for bipartite structures with coordination numbers z = 1,…,12, for fillings n = 1.0 and n = 1.2, and for a grid of U/t values that spans the phase boundaries. Determine the ground‑state magnetic phase (0 = PM, 1 = FM, 2 = AF) at each (n, z, U/t) point and compute the corresponding μ, d², and q. From these data produce:

- **phase_data.csv**: a table of (n, z, U/t, phase) over the full grid.
- **properties.csv**: curves of μ, d², q as functions of z for the specific parameter sets: n=1.0 with U/t = 5, 7, 10 and n=1.2 with U/t = 7, 35, 90.

All outputs must follow the schemas defined in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Run slave-boson solver
- Role: process
- Action: Implement the single-band Hubbard model on bipartite lattices with equal sublattice sizes, using the third-moment local density of states and the Kotliar-Ruckenstein saddle-point slave-boson approximation. For the parameter grids (n=1.0 and n=1.2; z=1..12; U/t = 0.0, 0.5, 1.0, …, 200.0), solve the self-consistent equations for paramagnetic, ferromagnetic, and antiferromagnetic trial states, minimize the energy to determine the ground state, and record the local magnetic moment, average double occupation, and hopping renormalization factor. Save the raw computed quantities as a JSON file.
- Evidence: `/app/outputs/raw_solver_output.json`

### Step 2: Generate magnetic phase diagram
- Role: scored
- Action: From the raw solver output, extract the ground-state magnetic order for each (n, z, U/t) point, where U/t ranges from 0.0 to 200.0 in steps of 0.5 (i.e., 0.0, 0.5, 1.0, …, 200.0), and write a CSV file with columns (n, z, U_t, phase). The phase label is 0 for paramagnetic, 1 for ferromagnetic, 2 for antiferromagnetic.
- Output file: `/app/outputs/phase_data.csv`
- Format: csv
- Contract: CSV with columns: n (float), z (int), U_t (float), phase (int: 0=PM, 1=FM, 2=AF).
- Scoring: scored by hidden verifier

### Step 3: Extract physical property curves
- Role: scored (load-bearing)
- Action: From the raw solver output, extract the local magnetic moment mu, average double occupation d2, and hopping renormalization factor q for the specified parameter sets: n=1.0 with U/t=5,7,10 and n=1.2 with U/t=7,35,90, each for z=1..12. Write the results as a CSV file with columns (n, z, U_t, mu, d2, q).
- Output file: `/app/outputs/properties.csv`
- Format: csv
- Contract: CSV with columns: n (float), z (int), U_t (float), mu (float), d2 (float), q (float). Each row corresponds to one (n, z, U_t) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_data.csv`
- `/app/outputs/properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_data.csv
- path: `/app/outputs/phase_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Magnetic phase diagram data mapping (n, z, U/t) to ground-state magnetic order.
- schema:
  - `type`: table
  - `required_columns`: `n`, `z`, `U_t`, `phase`
  - `units`:
    - `n`: electrons per site
    - `U_t`: dimensionless (U/t)
    - `phase`: integer label (0=PM, 1=FM, 2=AF)

### properties.csv
- path: `/app/outputs/properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Physical properties (local magnetic moment, average double occupation, hopping renormalization factor) for selected U/t and n values as functions of coordination number z.
- schema:
  - `type`: table
  - `required_columns`: `n`, `z`, `U_t`, `mu`, `d2`, `q`
  - `units`:
    - `n`: electrons per site
    - `U_t`: dimensionless (U/t)
    - `mu`: local magnetic moment (dimensionless or µB)
    - `d2`: average double occupation (dimensionless)
    - `q`: hopping renormalization factor (dimensionless)

Notes: Both scored artifacts are derived from the raw solver output generated in step 1. The hidden checker will compare the agent's phase labels and property values to a reference solution computed from the same Hubbard/slave-boson/third-moment protocol. Scoring tolerances are not disclosed publicly.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "z",
          "U_t",
          "phase"
        ],
        "units": {
          "n": "electrons per site",
          "U_t": "dimensionless (U/t)",
          "phase": "integer label (0=PM, 1=FM, 2=AF)"
        }
      },
      "description": "Magnetic phase diagram data mapping (n, z, U/t) to ground-state magnetic order."
    },
    {
      "file": "properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n",
          "z",
          "U_t",
          "mu",
          "d2",
          "q"
        ],
        "units": {
          "n": "electrons per site",
          "U_t": "dimensionless (U/t)",
          "mu": "local magnetic moment (dimensionless or µB)",
          "d2": "average double occupation (dimensionless)",
          "q": "hopping renormalization factor (dimensionless)"
        }
      },
      "description": "Physical properties (local magnetic moment, average double occupation, hopping renormalization factor) for selected U/t and n values as functions of coordination number z."
    }
  ],
  "notes": "Both scored artifacts are derived from the raw solver output generated in step 1. The hidden checker will compare the agent's phase labels and property values to a reference solution computed from the same Hubbard/slave-boson/third-moment protocol. Scoring tolerances are not disclosed publicly."
}
```

## How you are scored
A hidden verifier will score each output file independently using a reference solution computed from a faithful implementation of the same Hubbard/slave‑boson/third‑moment method. For `phase_data.csv`, it will compare phase labels at each grid point against the reference; agreement over the phase diagram grid contributes to your score. For `properties.csv`, it will compute the mean absolute error of μ, d², and q relative to the reference values. The final score is a weighted combination of these component scores. The verifier checks that your results are physically consistent with the model; simply reporting numbers without running the computation will not yield a good score.
