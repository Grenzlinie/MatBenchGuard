# Neutron mobility and effective mass from Bloch band structure in neutron star crust pasta phases

## Problem background
In the inner crust of a neutron star, unbound ('conduction') neutrons can move past the nuclear lattice, contributing to transport properties. This microscopic motion is characterised by a mobility coefficient K, which relates the neutron current density to a mean particle momentum, and by an associated macroscopic effective mass m_star. The goal is to compute these quantities from first principles using a mean-field Bloch wave model for slab-like (lasagna) and rod-like (spaghetti) nuclear phases, and to determine whether the effective mass differs significantly from the bare neutron mass.

## Approach
The unbound neutrons are treated as independent fermions moving in a periodic single-particle potential derived from the Oyamatsu-Yamada energy-density functional (Model I parameters). A zeroth-order potential U0 is obtained from the functional and smoothed by folding with a Gaussian of appropriate width to account for finite-range effects; spin-orbit coupling is neglected. The nuclear lattice is modelled as a one-dimensional periodic slab (lasagna) or as two-dimensional periodic rods (spaghetti) on square and hexagonal lattices, with exact Wigner-Seitz cells and lattice spacings a_Oy taken from the published tables. The single-particle Schrödinger equation is solved with Bloch boundary conditions using a plane-wave expansion. Energy bands and group velocities are obtained via the Hellmann-Feynman theorem. Fermi integrals over the Brillouin zone yield the occupation, the Fermi surface area, and the mobility tensor components K_parallel and K_perp. From these, the dimensionless ratios K_parallel/K_perp, m_star_perp/m, and S_F/S_gas are computed for each configuration.

## Reproduction target
Compute the neutron mobility anisotropy ratio K_parallel/K_perp, the transverse effective mass ratio m_star_perp/m, and the Fermi surface area ratio S_F/S_gas for the lasagna (slab) phase and for both hexagonal and square spaghetti (rod) phases, at the total neutron densities and lattice spacings specified in the Required configurations table. Output a CSV file at /app/outputs/results.csv with columns: phase, n_n (fm^{-3}), a_Oy (fm), K_ratio, m_star_ratio, S_F_ratio. Each row corresponds to one configuration exactly as listed in the Required configurations table.

## Assets

- K. Oyamatsu, Nuclear shapes in the inner crust of a neutron star, Nucl. Phys. A561 (1993) 431: https://doi.org/10.1016/0375-9474(93)90084-Z
- K. Oyamatsu, Y. Yamada, Shell energies of non-spherical nuclei in the inner crust of a neutron star, Nucl. Phys. A578 (1994) 184: https://doi.org/10.1016/0375-9474(94)90754-0
- NumPy: numpy
- SciPy: scipy

## Required configurations

Compute the following 12 configurations (phase, n_n (fm^{-3}), a_Oy (fm)):

- lasagna, 0.0735, 23.71
- lasagna, 0.0749, 23.07
- lasagna, 0.0773, 22.23
- lasagna, 0.0792, 21.84
- hexagonal_spaghetti, 0.0581, 27.17
- hexagonal_spaghetti, 0.0630, 25.77
- hexagonal_spaghetti, 0.0678, 24.62
- hexagonal_spaghetti, 0.0716, 23.97
- square_spaghetti, 0.0581, 27.17
- square_spaghetti, 0.0630, 25.77
- square_spaghetti, 0.0678, 24.62
- square_spaghetti, 0.0716, 23.97

For the hexagonal spaghetti, the Brillouin zone integration should use a corrected lattice spacing a = sqrt(2/sqrt(3)) * a_Oy as described in the paper.

## Workflow steps

### Step 1: Construct the single-particle potential and lattice definitions
- Role: process
- Action: Construct the single-particle potential V(r) for lasagna (1D) and spaghetti (2D, both hexagonal and square lattices) phases using the Oyamatsu-Yamada Model I parameters: derive the zeroth-order potential U0 from the energy-density functional of Oyamatsu (1993), apply Gaussian smearing with the appropriate width, and define the periodic lattice with exact Wigner-Seitz cells and lattice spacings a_Oy from the required configurations table above. Ignore spin-orbit coupling.
- Evidence: none

### Step 2: Solve band structure for each configuration
- Role: process
- Action: For each configuration listed in the Required configurations table above, solve the single-particle Schrödinger equation using a plane-wave expansion with Bloch boundary conditions. Obtain the energy bands ε_α(k) and group velocities v(k) via the Hellmann-Feynman theorem.
- Evidence: none

### Step 3: Evaluate Fermi integrals and derived quantities
- Role: process
- Action: For each configuration, determine the Fermi energy μ such that the total neutron density matches n_n; compute the conduction neutron density n, the Fermi surface area S_F, mobility components K^∥ and K^⊥, and the dimensionless ratios n/n_n, K^∥/K^⊥, m_star^⊥/m, and S_F/S_gas. Retain the required ratios (K_ratio, m_star_ratio, S_F_ratio) for final reporting.
- Evidence: none

### Step 4: Compile reported results
- Role: scored (load-bearing)
- Action: Compile the computed mobility anisotropy ratio K_ratio (= K^∥/K^⊥), effective mass ratio m_star_ratio (= m_star^⊥/m), and Fermi surface area ratio S_F_ratio (= S_F/S_gas) for all configurations into a CSV file results.csv. The file must contain exactly the configurations listed in the Required configurations table above, with columns phase, n_n, a_Oy, K_ratio, m_star_ratio, and S_F_ratio.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with header: phase, n_n (fm^{-3}), a_Oy (fm), K_ratio, m_star_ratio, S_F_ratio. One row per configuration exactly as listed in the Required configurations table.
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
- description: CSV file containing the computed mobility anisotropy ratio, effective mass ratio, and Fermi surface area ratio for lasagna and spaghetti phases at specified densities and lattice spacings, as described in the Required configurations table.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `n_n`, `a_Oy`, `K_ratio`, `m_star_ratio`, `S_F_ratio`
  - `units`:
    - `n_n`: fm^{-3}
    - `a_Oy`: fm
    - `K_ratio`: dimensionless
    - `m_star_ratio`: dimensionless
    - `S_F_ratio`: dimensionless

Notes: All ratios are dimensionless and correspond exactly to the quantities reported in the paper's Appendix A. The hidden checker compares these values to the reference gold numbers within appropriate tolerances.

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
          "phase",
          "n_n",
          "a_Oy",
          "K_ratio",
          "m_star_ratio",
          "S_F_ratio"
        ],
        "units": {
          "n_n": "fm^{-3}",
          "a_Oy": "fm",
          "K_ratio": "dimensionless",
          "m_star_ratio": "dimensionless",
          "S_F_ratio": "dimensionless"
        }
      },
      "description": "CSV file containing the computed mobility anisotropy ratio, effective mass ratio, and Fermi surface area ratio for lasagna and spaghetti phases at specified densities and lattice spacings, as described in the Required configurations table."
    }
  ],
  "notes": "All ratios are dimensionless and correspond exactly to the quantities reported in the paper's Appendix A. The hidden checker compares these values to the reference gold numbers within appropriate tolerances."
}
```

## How you are scored
A hidden verifier will read your /app/outputs/results.csv and compare each row's K_ratio, m_star_ratio, and S_F_ratio to hidden reference values. Your final score is proportional to the fraction of entries that fall within acceptable tolerances. Intermediate process steps are not individually scored, but they are required to produce accurate final ratios. Simply reporting numbers without a correct computational pipeline will not pass.
