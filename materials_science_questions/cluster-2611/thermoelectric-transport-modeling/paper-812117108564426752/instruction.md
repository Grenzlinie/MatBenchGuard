# Thermoelectric Transport Modeling with DMFT and SUNCA for Doped Mott Insulator

## Problem background
Strongly correlated electron systems, such as doped Mott insulators, exhibit anomalous thermoelectric properties that challenge conventional band‑structure theories. Dynamical mean‑field theory (DMFT) combined with realistic band dispersions provides a non‑perturbative framework for describing the electronic self‑energy and thereby computing transport coefficients from first principles. Understanding how correlations modify the thermopower in materials like doped LaTiO₃ is of fundamental interest and can guide the design of improved thermoelectric compounds. In this task, you will compute the electronic contribution to the Seebeck coefficient (thermopower) for a prototypical correlated oxide at room temperature using the DMFT method with a numerically efficient impurity solver.

## Approach
The core idea is to solve a three‑orbital Hubbard model that captures the relevant Ti 3d t₂g bands. The kinetic part is parameterized by a tight‑binding dispersion with hopping parameters t, t′, and t⊥ between Ti sites, determined from a fit to density‑functional calculations. The local Coulomb repulsion among the three orbitals is taken in an SU(6)‑symmetric form with a single interaction strength U, measured in units of the half‑bandwidth. The many‑body problem is treated within single‑site DMFT, where the lattice self‑energy is approximated as momentum‑independent and obtained from an auxiliary Anderson impurity model. The impurity model is solved using the symmetrized non‑crossing approximation (SUNCA) directly on the real‑frequency axis, avoiding the need for analytical continuation. With the converged self‑energy, the field‑theoretic expression for the thermopower is evaluated via the transport function, which involves a Brillouin‑zone summation of velocity‑weighted spectral densities, and the corresponding kinetic coefficients A₀ and A₁. The calculation is repeated for several electron densities corresponding to different chemical doping levels.

## Reproduction target
Using the specified tight‑binding parameters (t = -0.3297, t′ = -0.0816, t⊥ = -0.0205 eV) and Coulomb interaction U = 5 (in units of half‑bandwidth D = 1.35 eV), carry out DMFT+SUNCA calculations at temperature T = 300 K for doping fractions x = 0.05, 0.25, 0.50, 0.75, 0.80 (i.e., electron filling n = 1 − x). For each doping level, after DMFT self‑consistency, compute the thermopower S in µV/K using the transport function formalism. Write the resulting doping fraction and computed thermopower to a CSV file thermopower_table.csv with columns `doping_fraction` (float between 0 and 1) and `S_muV_per_K` (float), exactly one row per doping level. This CSV file is the scored artifact.

## Assets

- Three-band tight-binding parameters for LaTiO₃ t₂g bands
- SUNCA impurity solver method (Haule et al. 2001): 10.1103/PhysRevB.64.155111

## Workflow steps

### Step 1: DMFT self‑consistent solution with SUNCA
- Role: process
- Action: Solve the DMFT equations for the three‑band Hubbard model with U=5 (in units of half‑bandwidth D=1.35 eV) at T=300 K using the SUNCA impurity solver on the real‑frequency axis. Achieve convergence for each doping level n = 1 - x, where x ∈ {0.05, 0.25, 0.50, 0.75, 0.80}. Save the converged self‑energy Σ(ω).
- Evidence: `/app/outputs/dmft_convergence.log`

### Step 2: Compute thermopower from transport function
- Role: scored (load-bearing)
- Action: For each doping level, use the converged self‑energy to compute the transport function φ^{xx}(ϵ) and the kinetic coefficients A₀, A₁. Then compute thermopower S = -(k_B/|e|) · A₁/A₀. Write the doping fraction and the computed S (in µV/K) to thermopower_table.csv.
- Output file: `/app/outputs/thermopower_table.csv`
- Format: csv
- Contract: CSV with columns: doping_fraction (float between 0 and 1), S_muV_per_K (float). Exactly five rows for doping fractions 0.05, 0.25, 0.50, 0.75, 0.80.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermopower_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermopower_table.csv
- path: `/app/outputs/thermopower_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with computed thermopower values for five doping levels.
- schema:
  - `type`: table
  - `required_columns`: `doping_fraction`, `S_muV_per_K`
  - `units`:
    - `S_muV_per_K`: µV/K

Notes: Only thermopower is scored; the experimental reference values from Tokura et al. (Ref. 40 of the source paper) are used as hidden gold. No intermediate numerical values or tolerances are disclosed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermopower_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "doping_fraction",
          "S_muV_per_K"
        ],
        "units": {
          "S_muV_per_K": "µV/K"
        }
      },
      "description": "CSV file with computed thermopower values for five doping levels."
    }
  ],
  "notes": "Only thermopower is scored; the experimental reference values from Tokura et al. (Ref. 40 of the source paper) are used as hidden gold. No intermediate numerical values or tolerances are disclosed."
}
```

## How you are scored
A hidden verifier will check the file `/app/outputs/thermopower_table.csv`. The verifier extracts the computed thermopower values and compares them to hidden reference values obtained from independent experimental measurements for the same doping levels and temperature. The comparison uses appropriate tolerances to account for numerical and methodological differences. Your score is the fraction of doping levels for which the computed value matches the reference within the tolerance. Neither the reference values nor the exact tolerances are provided in the instructions; you must faithfully execute the workflow and produce the most accurate thermopower values you can.
