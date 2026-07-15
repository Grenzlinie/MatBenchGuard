# Determine Optimal Boson Energy in Holstein Model Superconductivity

## Problem background
The Holstein model describes conduction electrons that couple locally to dispersionless Boson fields, providing the simplest framework for conventional phonon-mediated superconductivity. At half-filling and with a realistic electron-Boson coupling, the system can exhibit a superconducting state whose strength depends on the Boson energy. The interplay between the pairing interaction and polaron formation leads to a non-monotonic dependence: the superconducting gap and pairing amplitude are expected to vary with the Boson energy and may peak at some optimal value. This task computes the half-gap and pairing amplitude as functions of the Boson energy for a fixed coupling, using two complementary many-body approaches, and determines the Boson energy that maximizes superconductivity.

## Approach
Two theoretical methods are employed: Migdal-Eliashberg (ME) theory and dynamical mean-field theory (DMFT) with an exact-diagonalization impurity solver. In the ME approach, the momentum-space self-consistent equations are solved on the Matsubara axis for a semicircular density of states (bandwidth 4t, t=1) and half-filling, ignoring vertex corrections. The self-energies Z, phi, and chi are iterated until convergence, yielding the gap Delta/2 = phi(iomega_0)/Z(iomega_0) and pairing amplitude Psi = T sum_n phi(iomega_n). In the DMFT approach, the lattice problem is mapped to an impurity model with a superconducting bath, and the impurity is solved by exact diagonalization in a truncated phonon Hilbert space. A self-consistency loop updates the bath parameters from the local Green's function. The same gap and pairing amplitude are computed from the converged solution. Both solvers are run for a set of Boson energies Omega that sample the relevant range, producing curves of gap and Psi versus Omega.

## Reproduction target
Produce two CSV files: me_data.csv (ME) and dmft_data.csv (DMFT). Each file must contain rows for several Boson energies Omega (in units of t), with columns: Omega, gap (half-gap Δ/2), Psi (pairing amplitude), and optionally Z0, phi0 (the renormalization factor and off-diagonal self-energy at the lowest Matsubara frequency). The solver's numerical parameters (Matsubara cutoff, bath size, phonon truncation, convergence criteria) are chosen by you. The target is to obtain gap and pairing amplitude as functions of Omega that correctly capture the non-monotonic trend and the optimal Boson energy inherent to the Holstein model.

## Assets

- Python 3 with numpy/scipy: numpy scipy

## Workflow steps

### Step 1: Migdal-Eliashberg Simulation
- Role: scored (load-bearing)
- Action: Implement the momentum-space Migdal-Eliashberg equations for the Holstein model with semicircular density of states (bandwidth 4t, t=1), half-filling, electron-Boson coupling g=0.6, and effectively zero temperature. Do not copy exact hyperparameters from the paper; you must choose Matsubara frequency cutoff, temperature, and convergence criteria that yield a stable self-consistent solution. For a set of Boson energies Omega spanning the expected optimal region, solve for the renormalization factor Z, off-diagonal self-energy phi, and Hartree term chi. Compute the superconducting half-gap Delta/2 = phi(i omega_0) / Z(i omega_0) and pairing amplitude Psi = T sum_n phi(i omega_n). Write a CSV file with columns Omega, gap, Psi, and optional Z0, phi0.
- Output file: `/app/outputs/me_data.csv`
- Format: csv
- Contract: CSV with header: Omega, gap, Psi, Z0, phi0. Omega (float, in units of t), gap (float, half-gap Δ/2), Psi (float, dimensionless pairing amplitude), Z0 (float, mass-renormalization factor at lowest Matsubara frequency), phi0 (float, off-diagonal self-energy at lowest Matsubara frequency). One row per Omega.
- Scoring: scored by hidden verifier

### Step 2: DMFT+ED Simulation
- Role: scored (load-bearing)
- Action: Implement the Dynamical Mean Field Theory (DMFT) self-consistency loop for the Holstein model using an exact-diagonalization impurity solver. Use the same model parameters (t=1, g=0.6, half-filling, semicircular DOS). Choose appropriate bath size, phonon-state truncation, and effective temperature; do not copy exact hyperparameters. For a set of Boson energies Omega, solve the impurity problem and obtain the converged local self-energies. From them compute half-gap and pairing amplitude as above. Write a CSV file with columns Omega, gap, Psi, and optional Z0, phi0.
- Output file: `/app/outputs/dmft_data.csv`
- Format: csv
- Contract: CSV with header: Omega, gap, Psi, Z0, phi0. Omega (float, in units of t), gap (float, half-gap Δ/2), Psi (float, dimensionless pairing amplitude), Z0 (float, mass-renormalization factor at lowest Matsubara frequency), phi0 (float, off-diagonal self-energy at lowest Matsubara frequency). One row per Omega.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/me_data.csv`
- `/app/outputs/dmft_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### me_data.csv
- path: `/app/outputs/me_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw gap and pairing amplitude vs Omega from Migdal-Eliashberg theory. The checker will identify the Boson energy that maximizes the gap and verify non-monotonicity.
- schema:
  - `type`: table
  - `required_columns`: `Omega`, `gap`, `Psi`
  - `optional_columns`: `Z0`, `phi0`
  - `units`:
    - `Omega`: units of t
    - `gap`: units of t
    - `Psi`: dimensionless

### dmft_data.csv
- path: `/app/outputs/dmft_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw gap and pairing amplitude vs Omega from DMFT+ED. The checker will identify the Boson energy that maximizes the gap and verify non-monotonicity.
- schema:
  - `type`: table
  - `required_columns`: `Omega`, `gap`, `Psi`
  - `optional_columns`: `Z0`, `phi0`
  - `units`:
    - `Omega`: units of t
    - `gap`: units of t
    - `Psi`: dimensionless

Notes: The solver's choice of numerical parameters (Matsubara cutoff, bath size, phonon truncation, convergence criteria) is not prescribed; the output must exhibit a single maximum and physically plausible curves.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "me_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Omega",
          "gap",
          "Psi"
        ],
        "optional_columns": [
          "Z0",
          "phi0"
        ],
        "units": {
          "Omega": "units of t",
          "gap": "units of t",
          "Psi": "dimensionless"
        }
      },
      "description": "Raw gap and pairing amplitude vs Omega from Migdal-Eliashberg theory. The checker will identify the Boson energy that maximizes the gap and verify non-monotonicity."
    },
    {
      "file": "dmft_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Omega",
          "gap",
          "Psi"
        ],
        "optional_columns": [
          "Z0",
          "phi0"
        ],
        "units": {
          "Omega": "units of t",
          "gap": "units of t",
          "Psi": "dimensionless"
        }
      },
      "description": "Raw gap and pairing amplitude vs Omega from DMFT+ED. The checker will identify the Boson energy that maximizes the gap and verify non-monotonicity."
    }
  ],
  "notes": "The solver's choice of numerical parameters (Matsubara cutoff, bath size, phonon truncation, convergence criteria) is not prescribed; the output must exhibit a single maximum and physically plausible curves."
}
```

## How you are scored
A hidden verifier will independently read your me_data.csv and dmft_data.csv. For each file, it will interpolate the gap-versus-Omega curve to locate the Boson energy that maximizes the gap, and it will check that the gap and pairing amplitude are non-monotonic (increase then decrease). The verifier compares the peak location to a hidden reference value derived from the physics of the Holstein model, and assigns a reward based on how closely your computed peak matches the expected optimal Boson energy and on the correctness of the non-monotonic shape. The total reward is a weighted combination of both methods.
