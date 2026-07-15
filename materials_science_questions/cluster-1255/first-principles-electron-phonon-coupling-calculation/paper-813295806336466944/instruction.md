# Correlated squeezed-state variational ansatz for electron-phonon system ground state

## Problem background
The system under study is an electron‑phonon system with strong electron‑phonon interaction and a weak on‑site Coulomb repulsion, described by the Hubbard–Holstein model. The key challenge is to accurately determine the ground‑state properties of such a system, because the interplay of electron itinerancy, local attraction, and polaron formation strongly affects the resulting electronic and superconducting behaviour. The goal is to compute the ground‑state energy per site, the superconducting energy gap, and the condensation energy for both a square lattice and a simple cubic lattice, and to assess the role of intersite phonon correlations beyond previous uncorrelated treatments.

## Approach
The variational treatment begins with the Hubbard–Holstein Hamiltonian. A Lang–Firsov unitary displacement transformation is applied, followed by a single‑mode squeezing transformation that introduces the variational parameter τ = exp(−2α). To go beyond the Hartree approximation and capture correlations between different phonon modes, a correlated multimode squeezed vacuum state is introduced, characterized by an additional nearest‑neighbor correlation parameter β. Averaging the transformed Hamiltonian over this phonon state produces an effective electronic Hamiltonian that is an attractive (negative‑U) Hubbard model. This effective model is solved within a BCS mean‑field theory, assuming a square density of states for the electrons. The ground‑state energy is then minimized numerically with respect to τ and β, separately for the normal state (superconducting order parameter Δ₀ = 0) and for the superconducting state (Δ₀ ≠ 0). From the optimized parameters the energy per site, the gap Δ₀, and the condensation energy (the energy difference between the two states) are obtained.

## Reproduction target
Compute the optimal variational parameters (τ, β) and the corresponding ground‑state energy per site for both the normal state (Δ₀ = 0) and the superconducting state (Δ₀ ≠ 0), the superconducting gap Δ₀, and the condensation energy δ. Perform this computation for two lattice types: a square lattice and a simple cubic lattice. The physical parameters are fixed as follows: phonon energy ħω = 0.08, electron‑phonon coupling strength J = 0.3, on‑site Coulomb repulsion U = 0.3, electron density n = 0.8, and band half‑width D = 1 (setting the energy unit). Use a square density of states for the electrons. Report the results in two CSV files, one for each lattice.

## Assets

- Python 3 (runtime)
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute ground-state properties for square lattice
- Role: scored
- Action: Implement the variational energy minimization for the square lattice. Use a square density of states. For the given parameters (ħω=0.08, J=0.3, U=0.3, n=0.8, D=1), minimize the ground-state energy per site over the variational parameters τ=exp(-2α) and β (nearest-neighbor correlation). At each (τ,β) evaluate the superconducting (Δ0≠0) and normal (Δ0=0) energies, the gap Δ0, and the condensation energy. Report the optimal parameters and the corresponding energies, gap, and condensation energy.
- Output file: `/app/outputs/results_square.csv`
- Format: csv
- Contract: Columns: τ_opt, β_opt, energy_normal, energy_superconducting, gap, condensation_energy. All numeric. Energies and gap in units of D=1.
- Scoring: scored by hidden verifier

### Step 2: Compute ground-state properties for simple cubic lattice
- Role: scored
- Action: Implement the same variational minimization for the simple cubic lattice. The density of states and the nearest-neighbor sum change accordingly. Output the optimal parameters and the same set of properties.
- Output file: `/app/outputs/results_cubic.csv`
- Format: csv
- Contract: Columns: τ_opt, β_opt, energy_normal, energy_superconducting, gap, condensation_energy. All numeric. Energies and gap in units of D=1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results_square.csv`
- `/app/outputs/results_cubic.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results_square.csv
- path: `/app/outputs/results_square.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed optimal variational parameters and ground-state properties for the square lattice. The checker compares each numeric column against hidden reference values; energies are scored on a threshold-or-better basis, gap and condensation energy on exact match within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `τ_opt`, `β_opt`, `energy_normal`, `energy_superconducting`, `gap`, `condensation_energy`
  - `units`:
    - `energy_normal`: D=1
    - `energy_superconducting`: D=1
    - `gap`: D=1
    - `condensation_energy`: D=1

### results_cubic.csv
- path: `/app/outputs/results_cubic.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed optimal variational parameters and ground-state properties for the simple cubic lattice. The checker compares each numeric column against hidden reference values; energies are scored on a threshold-or-better basis, gap and condensation energy on exact match within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `τ_opt`, `β_opt`, `energy_normal`, `energy_superconducting`, `gap`, `condensation_energy`
  - `units`:
    - `energy_normal`: D=1
    - `energy_superconducting`: D=1
    - `gap`: D=1
    - `condensation_energy`: D=1

Notes: The checker compares each column to hidden reference values derived from the paper's reported results. The optimal τ and β are sanity-checked but not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results_square.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "τ_opt",
          "β_opt",
          "energy_normal",
          "energy_superconducting",
          "gap",
          "condensation_energy"
        ],
        "units": {
          "energy_normal": "D=1",
          "energy_superconducting": "D=1",
          "gap": "D=1",
          "condensation_energy": "D=1"
        }
      },
      "description": "Computed optimal variational parameters and ground-state properties for the square lattice. The checker compares each numeric column against hidden reference values; energies are scored on a threshold-or-better basis, gap and condensation energy on exact match within tolerance."
    },
    {
      "file": "results_cubic.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "τ_opt",
          "β_opt",
          "energy_normal",
          "energy_superconducting",
          "gap",
          "condensation_energy"
        ],
        "units": {
          "energy_normal": "D=1",
          "energy_superconducting": "D=1",
          "gap": "D=1",
          "condensation_energy": "D=1"
        }
      },
      "description": "Computed optimal variational parameters and ground-state properties for the simple cubic lattice. The checker compares each numeric column against hidden reference values; energies are scored on a threshold-or-better basis, gap and condensation energy on exact match within tolerance."
    }
  ],
  "notes": "The checker compares each column to hidden reference values derived from the paper's reported results. The optimal τ and β are sanity-checked but not directly scored."
}
```

## How you are scored
A hidden verifier reads each of the two output CSV files and independently checks the computed quantities. For the ground‑state energies, a threshold‑or‑better policy is applied: an energy that meets or improves upon the reference value (lower is better) earns full credit, while a higher energy results in a reduced score. For the superconducting gap and the condensation energy, an exact‑match tolerance is used. The scores from both lattice results are combined by weight into a final reward between 0 and 1. Simply reporting the paper’s numbers without actually executing the variational minimization will not pass; the verifier expects a solution that is generated by a genuine numerical optimization run.
