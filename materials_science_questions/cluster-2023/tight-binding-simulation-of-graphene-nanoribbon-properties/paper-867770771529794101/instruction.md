# Two-Orbital Anderson Impurity Model: Magnetic Anisotropy Renormalization

## Problem background
Magnetic molecules wired to electrodes are key components for spintronic devices. However, electrical addressing can alter their magnetic properties through charge fluctuations, renormalizing the magnetic anisotropy energy (MAE). This task computationally investigates this effect for an iron porphyrin molecule coupled to graphene nanoribbon electrodes by solving a two-orbital Anderson impurity model. The goal is to compute how the d-orbital filling, controlled by the on-site energy, affects the impurity occupancy and the correlation between the renormalized MAE and the energy of the spin-carrying upper Coulomb peak, as predicted by the model.

## Approach
The system is described by a two-orbital Anderson impurity model (2AIM) including an on-site uniaxial magnetic anisotropy term D S_z^2. The impurity is coupled to a conduction-electron bath. The model is solved in the one-crossing approximation (OCA) to obtain the spectral function A(ω) for a range of impurity on-site energies ε_d. From the spectral function, the impurity occupancy N_d is obtained by integration up to the Fermi level. Additionally, the position of the upper Coulomb peak (spin-unoccupied resonance) and the spin excitation energy (MAE), defined as half the separation between the inelastic step features around zero bias, are extracted. The calculations are performed at low temperature with fixed model parameters that match the physical system. The workflow proceeds by first solving the impurity model for several ε_d values, then post-processing the spectral functions to produce the requested quantities.

## Reproduction target
Produce two CSV files: (1) occupancy.csv containing the impurity d-orbital occupancy N_d as a function of on-site energy ε_d (in eV) for at least five ε_d values between -4 and -6 eV; (2) mae_peakpos.csv containing the renormalized MAE (in meV) and the upper Coulomb peak position (in meV) for each corresponding ε_d. The data should faithfully represent the predictions of the 2AIM model solved with OCA, without requiring external datasets.

## Assets

- Python 3: python3
- One-crossing approximation (OCA) algorithm for Anderson impurity model

## Workflow steps

### Step 1: Solve 2AIM using OCA
- Role: process
- Action: Implement and solve the two-orbital Anderson impurity model (2AIM) with uniaxial magnetic anisotropy D S_z^2 using the one-crossing approximation (OCA). Use parameters: D=7.14 meV, single-particle broadening Γ=30 meV, intra-orbital Coulomb U=3.5 eV, inter-orbital Coulomb U'=2.5 eV, Hund's coupling J_H=0.5 eV, temperature T=10 K. Run the solver for a range of on-site impurity energies ε_d from -4 eV to -6 eV (at least 5 distinct values). Save the full spectral function A(ω) for each ε_d in a reusable compressed NumPy file.
- Evidence: `/app/outputs/spectral_data.npz`

### Step 2: Compute impurity occupancy N_d
- Role: scored (load-bearing)
- Action: From the spectral functions obtained in the previous step, compute the d-orbital occupancy N_d by integrating each spectral function from negative infinity to the Fermi level (ω=0). Output a CSV file with one row per ε_d value, containing the on-site energy and the computed N_d.
- Output file: `/app/outputs/occupancy.csv`
- Format: csv
- Contract: columns: epsilon_d (eV), N_d (dimensionless); one row per ε_d value
- Scoring: scored by hidden verifier

### Step 3: Extract MAE and upper Coulomb peak position
- Role: scored (load-bearing)
- Action: Using the spectral functions, determine two quantities for each ε_d: (i) the energy position of the upper Coulomb peak (the first prominent peak in the positive-energy side of the spectrum, corresponding to the SU resonance), and (ii) the spin excitation energy (MAE), measured as half the distance between the inelastic step features around zero bias. Output a CSV file with columns for ε_d, the peak position (in meV), and the MAE (in meV).
- Output file: `/app/outputs/mae_peakpos.csv`
- Format: csv
- Contract: columns: epsilon_d (eV), peak_position (meV), MAE (meV); one row per ε_d value
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/occupancy.csv`
- `/app/outputs/mae_peakpos.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### occupancy.csv
- path: `/app/outputs/occupancy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Impurity occupancy N_d as a function of on-site energy ε_d. The checker compares the submitted occupancy values to hidden reference data from the paper with appropriate tolerances and verifies monotonicity.
- schema:
  - `type`: table
  - `required_columns`: `epsilon_d`, `N_d`
  - `units`:
    - `epsilon_d`: eV
    - `N_d`: dimensionless

### mae_peakpos.csv
- path: `/app/outputs/mae_peakpos.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Renormalized magnetic anisotropy energy (MAE) versus upper Coulomb peak position for each ε_d. The checker compares the agent's MAE and peak_position data to hidden reference points from the paper, tolerances of ±1 meV on MAE and ±10 meV on peak_position.
- schema:
  - `type`: table
  - `required_columns`: `epsilon_d`, `peak_position`, `MAE`
  - `units`:
    - `epsilon_d`: eV
    - `peak_position`: meV
    - `MAE`: meV

Notes: The process step produces an intermediate spectral_data.npz file which is not directly scored. All scored outputs are CSV tables with the columns and units declared above. The verifier uses a hidden set of reference points derived from the paper's model curves.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "occupancy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilon_d",
          "N_d"
        ],
        "units": {
          "epsilon_d": "eV",
          "N_d": "dimensionless"
        }
      },
      "description": "Impurity occupancy N_d as a function of on-site energy ε_d. The checker compares the submitted occupancy values to hidden reference data from the paper with appropriate tolerances and verifies monotonicity."
    },
    {
      "file": "mae_peakpos.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "epsilon_d",
          "peak_position",
          "MAE"
        ],
        "units": {
          "epsilon_d": "eV",
          "peak_position": "meV",
          "MAE": "meV"
        }
      },
      "description": "Renormalized magnetic anisotropy energy (MAE) versus upper Coulomb peak position for each ε_d. The checker compares the agent's MAE and peak_position data to hidden reference points from the paper, tolerances of ±1 meV on MAE and ±10 meV on peak_position."
    }
  ],
  "notes": "The process step produces an intermediate spectral_data.npz file which is not directly scored. All scored outputs are CSV tables with the columns and units declared above. The verifier uses a hidden set of reference points derived from the paper's model curves."
}
```

## How you are scored
A hidden verifier will independently score each output file. For occupancy.csv, the verifier will compare the occupancy curve to a hidden reference from the model, checking both the shape and the values within an appropriate tolerance. For mae_peakpos.csv, the verifier will compare the MAE and peak position values to reference data and verify the correlation pattern. The final reward is a weighted combination of the scores from both artifacts. Reporting the paper's numbers is not sufficient; the verifier expects the results to be derived from your own implementation of the solver.
