# Lattice thermal conductivity of β-Ga₂O₃ from neural network potential and Green–Kubo modal analysis

## Problem background
β-Ga₂O₃ is an ultra‑wide‑bandgap semiconductor with promising applications in high‑power electronics and high‑voltage switching devices. Efficient thermal management is critical because device performance is limited by heat dissipation, yet the lattice thermal conductivity of β-Ga₂O₃ is strongly anisotropic and has been difficult to predict reliably from first principles alone. No accurate interatomic potential existed for this compound, preventing large‑scale molecular dynamics simulations of its thermal transport properties.

## Approach
First, a deep neural network potential (NNP) is trained on an ab initio molecular dynamics (AIMD) dataset of β-Ga₂O₃. The NNP maps atomic configurations to energies and forces with high fidelity and is validated by comparing its harmonic phonon dispersion against reference DFT calculations. Using the trained NNP, equilibrium molecular dynamics (EMD) simulations are performed on large supercells, and the anisotropic lattice thermal conductivity is obtained via the Green–Kubo formalism. To understand the phonon transport further, a Green–Kubo modal analysis (GKMA) is carried out: normal‑mode eigenvectors of the production supercell are computed, and the MD heat currents are decomposed into mode contributions, yielding the accumulated thermal conductivity as a function of phonon frequency for each crystallographic direction.

## Reproduction target
Train a deep neural network potential on an AIMD‑generated dataset for the β-Ga₂O₃ crystal (lattice parameters a=12.376 Å, b=3.084 Å, c=5.893 Å, β=103.83°, 2 × 4 × 2 supercell). Then, using the trained NNP in LAMMPS, run EMD simulations on a 4 × 13 × 7 supercell (7280 atoms) at temperatures of 200 K, 300 K, 400 K, and 500 K. For each temperature, perform 15 independent NVE production runs of 2 ns after NPT equilibration, collect the heat currents, and compute the directional lattice thermal conductivity κ[100], κ[010], κ[001] via the Green–Kubo formula. Write these values to `/app/outputs/thermal_conductivity_data.csv`. Additionally, perform a supercell lattice dynamics calculation on the same 4 × 13 × 7 supercell to obtain normal‑mode eigenvectors, then use the 300 K MD trajectories to run a Green–Kubo modal analysis. Produce the accumulated thermal conductivity as a function of phonon mode frequency for each direction and save it to `/app/outputs/modal_accumulation_data.csv`.

## Assets

- CP2K: https://www.cp2k.org
- deepmd-kit: https://github.com/deepmodeling/deepmd-kit
- LAMMPS: https://lammps.sandia.gov
- Alamode: https://alamode.readthedocs.io

## Workflow steps

### Step 1: AIMD training dataset generation
- Role: process
- Action: Run CP2K ab initio molecular dynamics on a 2×4×2 β‑Ga₂O₃ supercell using DFT (GPW method, TZVP basis, GTH pseudopotentials, 800 Ry cutoff, Γ‑point sampling). Perform simulations at temperatures from 50 K to 600 K with NPT (zero pressure), 1 fs timestep, 1 ps equilibration and 5 ps production collecting snapshots every 4 steps. Complement with static DFT calculations on randomly displaced 0 K structures. Produce a dataset of ~9200 snapshots with atomic coordinates, total energies, and forces.
- Evidence: none

### Step 2: NNP training with DeePot-SE
- Role: process
- Action: Train a deep neural network potential using deepmd-kit (DeePot‑SE) on the AIMD dataset. Use a two‑layer embedding network and a three‑layer fitting network with 160 nodes per layer. Optimize to minimize weighted energy and force errors. Save the trained model files.
- Evidence: none

### Step 3: Phonon dispersion validation
- Role: process
- Action: Using the trained NNP and Alamode, perform finite‑displacement calculations (displacement 0.01 Å) to obtain harmonic force constants and compute the phonon dispersion along high‑symmetry paths. Compare the dispersion with reference DFT data to verify harmonic accuracy.
- Evidence: none

### Step 4: Size convergence test for EMD
- Role: process
- Action: Run equilibrium MD with Green‑Kubo on several supercell sizes (e.g., 5040 and 7280 atoms) at 300 K using the trained NNP in LAMMPS to obtain thermal conductivity values and confirm convergence with respect to domain size.
- Evidence: none

### Step 5: EMD thermal conductivity simulation
- Role: scored (load-bearing)
- Action: Perform equilibrium MD simulations with the trained NNP in LAMMPS on a 4×13×7 supercell (7280 atoms). For each temperature (200, 300, 400, 500 K): equilibrate in NPT at zero pressure for 200 ps, then run 15 independent NVE productions of 2 ns each (1 fs timestep). From the collected heat currents compute the anisotropic lattice thermal conductivity using the Green‑Kubo formula. Output the averaged κ[100], κ[010], and κ[001] at each temperature.
- Output file: `/app/outputs/thermal_conductivity_data.csv`
- Format: csv
- Contract: Columns: temperature_K, kappa_100_W_mK, kappa_010_W_mK, kappa_001_W_mK. One row per temperature (200, 300, 400, 500 K). All values are in W m⁻¹ K⁻¹.
- Scoring: scored by hidden verifier

### Step 6: Supercell lattice dynamics calculation
- Role: process
- Action: Perform finite‑displacement calculations on the 4×13×7 supercell using the trained NNP to obtain the normal‑mode eigenvectors and eigenfrequencies of the entire supercell. This step is required for the subsequent modal analysis.
- Evidence: none

### Step 7: Green–Kubo modal analysis (GKMA)
- Role: scored
- Action: Using the MD trajectories from step 4 and the normal‑mode eigenvectors from step 5, decompose the heat current into modal contributions and compute the accumulated thermal conductivity as a function of phonon mode frequency for each direction at 300 K. Output the accumulated κ vs. frequency.
- Output file: `/app/outputs/modal_accumulation_data.csv`
- Format: csv
- Contract: Columns: frequency_THz, kappa_100_accumulated_W_mK, kappa_010_accumulated_W_mK, kappa_001_accumulated_W_mK. Rows from 0 to about 20 THz with a step ≤0.5 THz. Values are in W m⁻¹ K⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_data.csv`
- `/app/outputs/modal_accumulation_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_data.csv
- path: `/app/outputs/thermal_conductivity_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Anisotropic lattice thermal conductivity values of β‑Ga₂O₃ along three crystallographic directions at 200, 300, 400, and 500 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `kappa_100_W_mK`, `kappa_010_W_mK`, `kappa_001_W_mK`
  - `units`:
    - `temperature_K`: K
    - `kappa_100_W_mK`: W m⁻¹ K⁻¹
    - `kappa_010_W_mK`: W m⁻¹ K⁻¹
    - `kappa_001_W_mK`: W m⁻¹ K⁻¹

### modal_accumulation_data.csv
- path: `/app/outputs/modal_accumulation_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Accumulated lattice thermal conductivity as a function of phonon mode frequency at 300 K for the three crystallographic directions.
- schema:
  - `type`: table
  - `required_columns`: `frequency_THz`, `kappa_100_accumulated_W_mK`, `kappa_010_accumulated_W_mK`, `kappa_001_accumulated_W_mK`
  - `units`:
    - `frequency_THz`: THz
    - `kappa_100_accumulated_W_mK`: W m⁻¹ K⁻¹
    - `kappa_010_accumulated_W_mK`: W m⁻¹ K⁻¹
    - `kappa_001_accumulated_W_mK`: W m⁻¹ K⁻¹

Notes: The checker will compare the agent-reported thermal conductivity values and accumulated curves to the paper’s published results within appropriate tolerances. Exact gold values and tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "kappa_100_W_mK",
          "kappa_010_W_mK",
          "kappa_001_W_mK"
        ],
        "units": {
          "temperature_K": "K",
          "kappa_100_W_mK": "W m⁻¹ K⁻¹",
          "kappa_010_W_mK": "W m⁻¹ K⁻¹",
          "kappa_001_W_mK": "W m⁻¹ K⁻¹"
        }
      },
      "description": "Anisotropic lattice thermal conductivity values of β‑Ga₂O₃ along three crystallographic directions at 200, 300, 400, and 500 K."
    },
    {
      "file": "modal_accumulation_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_THz",
          "kappa_100_accumulated_W_mK",
          "kappa_010_accumulated_W_mK",
          "kappa_001_accumulated_W_mK"
        ],
        "units": {
          "frequency_THz": "THz",
          "kappa_100_accumulated_W_mK": "W m⁻¹ K⁻¹",
          "kappa_010_accumulated_W_mK": "W m⁻¹ K⁻¹",
          "kappa_001_accumulated_W_mK": "W m⁻¹ K⁻¹"
        }
      },
      "description": "Accumulated lattice thermal conductivity as a function of phonon mode frequency at 300 K for the three crystallographic directions."
    }
  ],
  "notes": "The checker will compare the agent-reported thermal conductivity values and accumulated curves to the paper’s published results within appropriate tolerances. Exact gold values and tolerances are hidden."
}
```

## How you are scored
A hidden verifier reads each output CSV file and checks that its format and required columns match the output contract exactly. For `thermal_conductivity_data.csv`, the verifier compares the reported κ[100], κ[010], and κ[001] at 200 K, 300 K, 400 K, and 500 K against reference data within a suitable tolerance. For `modal_accumulation_data.csv`, the verifier confirms that the accumulated curves are monotonically increasing and that the saturation values at the highest frequency are consistent with the expected results. The total reward is a weighted combination of the scores from the two scored artifacts; simply printing a number from a paper is not sufficient.
