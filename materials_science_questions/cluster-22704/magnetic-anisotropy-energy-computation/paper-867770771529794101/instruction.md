# Magnetic Anisotropy Energy Renormalization from Two-Orbital Anderson Impurity Model

## Problem background
In molecular spintronics, magnetic anisotropy energy (MAE) of a magnetic molecule can be altered when the molecule is coupled to electrodes. Charge fluctuations and orbital filling changes, induced by hybridization with the environment, can renormalize the MAE. Understanding how the MAE depends on the energy alignment of molecular orbitals is crucial for designing molecular spin systems with controlled magnetic properties. This task investigates this relationship through a two-orbital Anderson impurity model (2AIM) that includes uniaxial magnetic anisotropy. The model captures the physics of a spin-1 magnetic impurity coupled to a conduction bath, where varying the impurity on-site energy changes orbital filling and thereby affects the MAE. The goal is to compute how the MAE evolves as a function of orbital position and filling, and to map the resulting spin excitation energies.

## Approach
The core of the reproduction is solving the two-orbital Anderson impurity model (2AIM) with uniaxial magnetic anisotropy. The model is defined by the following fixed parameters: uniaxial anisotropy D = 7.14 meV, single-particle broadening Γ = 30 meV, intra-orbital Coulomb repulsion U = 3.5 eV, inter-orbital Coulomb repulsion U' = 2.5 eV, Hund's rule coupling J_H = 0.5 eV, and temperature T ≈ 10 K. The impurity system is near half-filling (expected occupancy ~2) and is solved using the one-crossing approximation (OCA) or an equivalent method that can handle the interaction and anisotropy. The control parameter is the impurity on-site energy ε_d, which is swept from -8 eV to -2 eV. For each ε_d value, the solver computes: (i) the total impurity occupancy N_d, (ii) the one-particle spectral function, from which the upper Coulomb peak position (the energy of the first peak above the Fermi level) is extracted, and (iii) the magnetic anisotropy energy (MAE) from the low-energy inelastic spin excitation steps (the spin-1 multiplet splitting). The resulting data table captures the relationship between orbital filling, the upper Coulomb peak position, and the renormalized MAE. No further experimental data or fitting is required.

## Reproduction target
Produce a CSV file named `mae_vs_peak.csv` containing the results of the Anderson impurity model simulations. The file must include the following columns: `epsilon_d` (eV, impurity on-site energy), `occupancy_Nd` (dimensionless, total d-orbital occupation), `peak_position` (meV, energy of the upper Coulomb peak relative to the Fermi level), `MAE` (meV, spin excitation energy). The table must have at least 100 rows covering epsilon_d from -8 eV to -2 eV inclusive, with values regularly spaced. The simulation must correctly implement the two-orbital Anderson impurity model with the specified parameters and solve it at each epsilon_d point to obtain the required quantities. The slope and intercept of MAE versus peak_position for small peak positions, as well as the MAE at the particle-hole symmetric point (epsilon_d = -4 eV), will be evaluated against hidden reference values.

## Assets
The workflow requires a solver capable of handling the two-orbital Anderson impurity model with uniaxial anisotropy. No pre-existing dataset or pre-trained model is needed. The required asset is:

- **Anderson impurity model solver**: A tool implementing the one-crossing approximation (OCA) or an equivalent method (e.g., numerical renormalization group, NRG) for solving the two-orbital Anderson impurity model. The solver must be able to compute the one-particle spectral function and the spin excitation energies for the given parameters. Any open-source solver or a self-implementation in a general-purpose programming language is acceptable. No specific package or URL is mandated; the agent is free to choose or implement the solver.

## Workflow steps

### Step 1: Solve two-orbital Anderson impurity model
- Role: scored (load-bearing)
- Action: Implement and solve the two-orbital Anderson impurity model with parameters: uniaxial anisotropy D = 7.14 meV, single-particle broadening Γ = 30 meV, intra-orbital Coulomb repulsion U = 3.5 eV, inter-orbital Coulomb repulsion U' = 2.5 eV, Hund's rule coupling J_H = 0.5 eV, temperature T ≈ 10 K. Use the one-crossing approximation (OCA) or an equivalent method. Sweep the impurity on-site energy ε_d from -8 eV to -2 eV in at least 100 regularly spaced points. For each ε_d, compute the impurity occupancy N_d, the upper Coulomb peak position (energy of the first peak above the Fermi level in the one-particle spectral function), and the magnetic anisotropy energy (MAE) from the low-energy inelastic spin excitation steps. Output a CSV file with columns: epsilon_d (eV), occupancy_Nd (dimensionless), peak_position (meV), MAE (meV).
- Output file: `/app/outputs/mae_vs_peak.csv`
- Format: csv
- Contract: CSV with four columns: epsilon_d (float, eV), occupancy_Nd (float, dimensionless), peak_position (float, meV), MAE (float, meV). The table must contain at least 100 rows spanning epsilon_d from -8 to -2 eV inclusive.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mae_vs_peak.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mae_vs_peak.csv
- path: `/app/outputs/mae_vs_peak.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table mapping impurity on-site energy to occupancy, upper Coulomb peak position, and magnetic anisotropy energy, obtained by solving the two-orbital Anderson impurity model.
- schema:
  - `type`: table
  - `required_columns`: `epsilon_d`, `occupancy_Nd`, `peak_position`, `MAE`
  - `units`:
    - `epsilon_d`: eV
    - `peak_position`: meV
    - `MAE`: meV

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mae_vs_peak.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilon_d",
          "occupancy_Nd",
          "peak_position",
          "MAE"
        ],
        "units": {
          "epsilon_d": "eV",
          "peak_position": "meV",
          "MAE": "meV"
        }
      },
      "description": "Table mapping impurity on-site energy to occupancy, upper Coulomb peak position, and magnetic anisotropy energy, obtained by solving the two-orbital Anderson impurity model."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your `mae_vs_peak.csv` and scores it based on physical accuracy. It performs the following checks:

1. **MAE vs. peak_position trend**: A linear regression is computed on the rows where `peak_position` is below a certain threshold. The slope and intercept of this regression are compared to hidden gold values derived from the expected physical relationship. Accuracy of both is evaluated.

2. **MAE at particle‑hole symmetry**: The MAE value at ε_d = −4 eV (the half‑filling point) is compared to a hidden reference value.

The final reward combines these checks with appropriate tolerances. Merely generating a file with plausible numbers is not enough; the computed values must correctly reflect the physics of the Anderson model with the specified parameters. The reward is higher the closer your simulation results match the hidden references.
