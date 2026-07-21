# Compute ground-state magnetic phase diagrams for kagomé and pyrochlore lattices using the double-exchange model

## Problem background
The magnetic ground states of geometrically frustrated metallic lattices are central to understanding phenomena such as colossal magnetoresistance and spin-glass transitions observed in pyrochlore oxides. In the double-exchange model, itinerant electrons interact with localized spins through a ferromagnetic Hund coupling and with each other via an antiferromagnetic superexchange. The competing interactions on the kagomé (two-dimensional) and pyrochlore (three-dimensional) lattices give rise to a variety of candidate spin configurations, and the resulting phase diagram as a function of Hund coupling strength, electron filling, and antiferromagnetic exchange remains an open computational problem. Reproducing these phase diagrams from the model provides insight into the stability of different magnetic orders in such frustrated systems.

## Approach
Implement a mean-field solver for the double-exchange Hamiltonian on both the kagomé lattice (three sites per unit cell) and the pyrochlore lattice (four sites per unit cell). The Hamiltonian includes nearest-neighbour electron hopping, an on-site ferromagnetic coupling between the itinerant electron spin and the localised spin, and an antiferromagnetic coupling between neighbouring localised spins. In the mean-field approximation, the spin operators are replaced by classical vectors, leading to an effective single-particle tight-binding Hamiltonian for each candidate spin configuration: ferromagnetic (F), ferrimagnetic (FI), and chiral (CI) on the kagomé lattice, and F, antiferromagnetic (AF), FI, CI, and spin ice (SI) on the pyrochlore lattice. For the chiral configuration the canting angle is optimised numerically. The total energy at a given electron filling n, Hund coupling K/t, and antiferromagnetic coupling J/t is the sum of the band energy (obtained by integrating over the occupied states in the Brillouin zone) and the classical exchange energy of the localised spins. By sweeping the parameter space and comparing the total energies of all candidate configurations, the ground state is identified as the one with the lowest energy. The goal is to produce a complete ground-state phase diagram in the K/t–n plane at J/t = 0, 0.02, 0.04, and a K/t–J/t cross-section at n = 1.0 electrons per unit cell.

## Reproduction target
Produce a CSV file containing, for every parameter point in the prescribed sweeps (n = 0–6 for kagomé, 0–8 for pyrochlore; K/t = 0–8 in steps; J/t = 0, 0.02, 0.04; plus the J/t–K/t sweep at n=1.0), the total energy of each candidate spin configuration and the label of the ground state. The file must follow the specified schema. Your submitted energies and ground-state assignments will be compared against an independent re-computation of the energies at a set of hidden (n, K/t, J/t) points using a different implementation of the same mean-field model. The comparison checks both the correctness of the ground-state identification and the relative ordering of the energies among configurations.

## Assets

- Kagomé lattice geometry
- Pyrochlore lattice geometry
- Python numerical libraries: numpy scipy

## Workflow steps

### Step 1: Set up mean-field double-exchange solver
- Role: process
- Action: Implement a mean-field solver for the double-exchange model Hamiltonian on both the kagomé and pyrochlore lattices. Construct the tight-binding Hamiltonian matrices for the 3‑site (kagomé) and 4‑site (pyrochlore) unit cells. Include the ferromagnetic Hund coupling K and antiferromagnetic exchange J terms, mean‑field decoupled for each candidate spin configuration (F, FI, CI for kagomé; F, AF, FI, CI, SI for pyrochlore). The solver must compute the total energy (band energy + classical exchange) as a function of electron filling n, K/t, J/t, and the spin configuration. Optionally implement a minimisation loop for the chiral (CI) canting angle.
- Evidence: `/app/outputs/solver_module.py`

### Step 2: Compute ground-state phase diagrams
- Role: scored (load-bearing)
- Action: For the kagomé and pyrochlore lattices, sweep the parameter ranges: electron number n (0–6 for kagomé, 0–8 for pyrochlore), K/t (e.g., 0–8 in steps) at J/t = 0, 0.02, and 0.04. For each (lattice, n, K/t, J/t) point, compute the total energy for every candidate spin configuration. Determine the ground state as the configuration with the lowest energy. Also compute the K/t–J/t cross‑section at n = 1.0 per unit cell for both lattices. Write all results to a CSV.
- Output file: `/app/outputs/phase_diagram_data.csv`
- Format: csv
- Contract: Columns: lattice (string, 'kagome' or 'pyrochlore'), n (float, electron number per unit cell), K_over_t (float), J_over_t (float), E_F (float), E_FI (float), E_CI (float), E_AF (float, present only for pyrochlore rows, empty for kagomé), E_SI (float, present only for pyrochlore rows), ground_state (string, one of 'F','FI','CI' for kagomé; 'F','AF','FI','CI','SI' for pyrochlore). All energies in units of |t|.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_data.csv
- path: `/app/outputs/phase_diagram_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: The CSV holds the computed total energies and ground state for every (lattice, n, K_over_t, J_over_t) grid point. The hidden checker recomputes the energies at a small set of hidden points using an independent mean-field solver and verifies the ground-state assignment and energy ordering.
- schema:
  - `type`: table
  - `required_columns`: `lattice`, `n`, `K_over_t`, `J_over_t`, `E_F`, `E_FI`, `E_CI`, `E_AF`, `E_SI`, `ground_state`
  - `units`:
    - `n`: electrons per unit cell
    - `K_over_t`: dimensionless
    - `J_over_t`: dimensionless
    - `E_F`: units of |t|
    - `E_FI`: units of |t|
    - `E_CI`: units of |t|
    - `E_AF`: units of |t|
    - `E_SI`: units of |t|
    - `ground_state`: string label

Notes: The checker implements a separate mean-field solver to recompute energies at hidden (n, K/t, J/t) points. It compares the agent's reported energies and ground_state labels against those independently obtained values, using appropriate tolerances. It does not re-run the full sweep.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "lattice",
          "n",
          "K_over_t",
          "J_over_t",
          "E_F",
          "E_FI",
          "E_CI",
          "E_AF",
          "E_SI",
          "ground_state"
        ],
        "units": {
          "n": "electrons per unit cell",
          "K_over_t": "dimensionless",
          "J_over_t": "dimensionless",
          "E_F": "units of |t|",
          "E_FI": "units of |t|",
          "E_CI": "units of |t|",
          "E_AF": "units of |t|",
          "E_SI": "units of |t|",
          "ground_state": "string label"
        }
      },
      "description": "The CSV holds the computed total energies and ground state for every (lattice, n, K_over_t, J_over_t) grid point. The hidden checker recomputes the energies at a small set of hidden points using an independent mean-field solver and verifies the ground-state assignment and energy ordering."
    }
  ],
  "notes": "The checker implements a separate mean-field solver to recompute energies at hidden (n, K/t, J/t) points. It compares the agent's reported energies and ground_state labels against those independently obtained values, using appropriate tolerances. It does not re-run the full sweep."
}
```

## How you are scored
A hidden verifier independently scores each workflow step's artifact and combines the scores by weight into a final reward (0 to 1). The main scored artifact is the phase-diagram CSV. The verifier will recompute the total energies at a set of hidden parameter points using its own mean-field solver, then compare your reported energies and ground-state labels to those recomputed values. The reward depends on whether the solver-recommended ground state matches the hidden solver’s prediction and whether the energy differences among configurations are consistent within a tolerance. Reporting the paper's numerical values without a correct underlying solver will not yield a high reward, because the hidden points are not disclosed in advance. The verification does not require an exact match to the published paper’s figures; it evaluates the fidelity of the computational procedure.
