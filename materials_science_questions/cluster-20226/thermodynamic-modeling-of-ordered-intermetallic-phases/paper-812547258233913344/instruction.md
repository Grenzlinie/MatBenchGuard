# Machine-learned interatomic potential and Monte Carlo study of short-range order in a ternary fcc alloy

## Problem background
Concentrated solid solutions and high‑entropy alloys have attracted intense interest due to their exceptional mechanical properties. Among them, the equiatomic fcc VCoNi alloy exhibits remarkable strength, potentially linked to local chemical ordering. Understanding the nature and degree of short‑range order (SRO) in this alloy is key for explaining its mechanical behavior. This task investigates the SRO in fcc VCoNi by computing Warren‑Cowley SRO parameters, the order‑disorder transition temperature, and the influence of lattice relaxations on ordering.

## Approach
The reproduction uses a two‑step computational approach. First, a machine‑learned low‑rank potential (LRP) is trained on density‑functional theory (DFT) total‑energy calculations for VCoNi supercells. The LRP represents the configurational energy landscape while allowing for local lattice relaxations. Training data are generated with an active‑learning loop: an initial LRP ensemble is used in Monte Carlo (MC) simulations to identify undersampled regions of configuration space, and the corresponding DFT energies are added to the training set. Once the final LRP ensemble is converged, canonical MC simulations are performed on large supercells at temperatures spanning the expected order‑disorder transition. From the resulting trajectories, the Warren‑Cowley SRO parameters at a temperature above the transition, the specific‑heat capacity as a function of temperature, and the sublattice occupancies are extracted. In a final step, MC snapshots representing ordered, short‑range‑ordered, and random states are selected, and DFT relaxation calculations are performed on those snapshots to obtain relaxation energies and mean‑square atomic displacements.

## Reproduction target
Train an LRP on DFT supercell data for fcc VCoNi using an active‑learning workflow. Use the trained LRP ensemble in canonical Monte Carlo simulations to compute:
- Warren‑Cowley SRO parameters for Co‑V, Ni‑V, and Co‑Ni pairs at the first and second coordination shells, at 1500 K (above the transition).
- Specific‑heat capacity C_V(T) over the temperature range 1100–2000 K, from which the order‑disorder transition temperature can be located.
- Vanadium sublattice occupancy fractions at a temperature below the transition (e.g., 1000 K) that reveal the site preference responsible for L1₂‑type ordering.
- From MC snapshots at 1000 K (ordered state), 1540 K (short‑range ordered state), and 4000 K (random state), perform DFT calculations to obtain relaxation energies per atom and mean‑square atomic displacements.
The required output files with exact formats are listed in the workflow steps and output contract.

## Assets

- Low-Rank Potential (LRP) implementation (mlip-2): https://github.com/ashapeev/mlip-2
- DFT code (Quantum ESPRESSO): https://www.quantum-espresso.org/
- PBE pseudopotentials for V, Co, Ni: https://www.quantum-espresso.org/pseudopotentials/
- SQS generation tool (ATAT or custom): https://github.com/kuellc/ATAT
- Monte Carlo simulation code

## Workflow steps

### Step 1: Compute high-temperature lattice constant
- Role: process
- Action: Compute the equilibrium lattice constant of fcc VCoNi at 1175 K using DFT total-energy calculations on a 3x3x3 fcc SQS supercell, fitting the energy-volume data to a Debye-Grüneisen model.
- Evidence: `/app/outputs/lattice_constant.txt`

### Step 2: Generate initial SQS training configurations
- Role: process
- Action: Generate special quasirandom structures (SQS) for fcc VCoNi in supercell sizes of 32, 48, and 108 atoms at equimolar composition, using the lattice constant from step01.
- Evidence: `/app/outputs/initial_configurations.txt`

### Step 3: DFT calculations on initial training set
- Role: process
- Action: Perform DFT calculations with full ionic relaxation on all 226 initial SQS configurations to obtain reference total energies.
- Evidence: `/app/outputs/initial_dft_energies.csv`

### Step 4: Train initial LRP ensemble
- Role: process
- Action: Fit an ensemble of 10 low-rank potentials (tensor-train rank r=5) to the relaxed DFT energies using the alternating least squares method until convergence (~2 meV/atom).
- Evidence: `/app/outputs/initial_lrp_models`

### Step 5: Active learning Monte Carlo sampling
- Role: process
- Action: Run canonical MC simulations on a 108-atom cell with each of the 10 initial LRPs over a range of temperatures; compute enthalpy and specific heat; select 40 new configurations at temperatures where predictions diverge (active learning workflow).
- Evidence: `/app/outputs/active_learning_configurations.txt`

### Step 6: DFT calculations on active learning configurations
- Role: process
- Action: Perform DFT calculations with ionic relaxation on the 40 active-learning configurations to obtain total energies.
- Evidence: `/app/outputs/al_dft_energies.csv`

### Step 7: Train final LRP ensemble
- Role: process
- Action: Combine the DFT data from step03 and step06; train a new ensemble of 10 LRPs (rank r=5) on the combined dataset to ~2 meV/atom accuracy.
- Evidence: `/app/outputs/final_lrp_models`

### Step 8: Run final LRP Monte Carlo simulations (large cell)
- Role: process
- Action: Perform canonical MC simulations with the final LRP ensemble on a 12x12x12 fcc supercell (6912 atoms) at temperatures from 1000 K to 4000 K, recording site occupancy evolution and configurational energy traces with appropriate burn-in.
- Evidence: `/app/outputs/mc_trajectory.npy`

### Step 9: Compute vanadium sublattice occupancy
- Role: scored
- Action: From the MC trajectory at a temperature below the transition (e.g., 1000 K), compute the fraction of V atoms on each of the four primitive cubic sublattices, average over ensemble and equilibrium steps, and write the results.
- Output file: `/app/outputs/step_02_v_sublattice_occupation.csv`
- Format: csv
- Contract: CSV with columns: sublattice_number (integer 1-4), occupancy_V (float, fraction).
- Scoring: scored by hidden verifier

### Step 10: Compute Warren-Cowley SRO parameters
- Role: scored
- Action: From the MC trajectory at 1500 K (above the transition), compute Warren-Cowley short-range order parameters α for pairs Co-V, Ni-V, Co-Ni at the first and second coordination shells, average over ensemble and MC steps, and write the results.
- Output file: `/app/outputs/step_03_sro_parameters.csv`
- Format: csv
- Contract: CSV with columns: pair (string: Co-V, Ni-V, Co-Ni), shell (integer 1 or 2), alpha (float).
- Scoring: scored by hidden verifier

### Step 11: Compute specific-heat capacity
- Role: scored
- Action: From the MC energy traces, compute specific-heat capacity C_V as the variance of the configurational energy per atom divided by (k_B T^2) times the number of atoms, at temperatures evenly spaced at least every 50 K in the range 1100–2000 K.
- Output file: `/app/outputs/step_04_specific_heat.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (float), C_V_eV_per_atom (float).
- Scoring: scored by hidden verifier

### Step 12: MC snapshot selection for relaxation analysis
- Role: process
- Action: Run MC simulation on a 4x4x4 (256-atom) fcc supercell with the final LRP ensemble at temperatures 1000 K (ordered), 1540 K (SRO), and 4000 K (random); save 10 independent snapshots per temperature after burn-in.
- Evidence: `/app/outputs/relaxation_snapshots.tar.gz`

### Step 13: Compute relaxation energies and mean‐square atomic displacements
- Role: scored (load-bearing)
- Action: For each snapshot, perform DFT calculations to obtain total energies of ideal and relaxed structures; compute relaxation energy per atom as (E_ideal – E_relaxed)/N and mean-square atomic displacement (MSAD) per Eq. (10); average over the 10 snapshots for each state and write the results.
- Output file: `/app/outputs/step_06_relaxation_and_msad.csv`
- Format: csv
- Contract: CSV with columns: state (string: ordered_1000K, SRO_1540K, random_4000K), relaxation_energy_eV_per_atom (float), MSAD_A2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_v_sublattice_occupation.csv`
- `/app/outputs/step_03_sro_parameters.csv`
- `/app/outputs/step_04_specific_heat.csv`
- `/app/outputs/step_06_relaxation_and_msad.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_v_sublattice_occupation.csv
- path: `/app/outputs/step_02_v_sublattice_occupation.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Vanadium sublattice occupancy fractions at a temperature below the order-disorder transition, showing which sublattice V occupies in the ordered L1₂-like state.
- schema:
  - `type`: table
  - `required_columns`: `sublattice_number`, `occupancy_V`
  - `units`:
    - `occupancy_V`: fraction

### step_03_sro_parameters.csv
- path: `/app/outputs/step_03_sro_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Warren-Cowley short-range order parameters for pairs Co-V, Ni-V, Co-Ni at the first two coordination shells, computed at 1500 K (above the transition).
- schema:
  - `type`: table
  - `required_columns`: `pair`, `shell`, `alpha`
  - `units`:
    - `alpha`: dimensionless

### step_04_specific_heat.csv
- path: `/app/outputs/step_04_specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Specific-heat capacity as a function of temperature; the peak location identifies the order-disorder transition temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `C_V_eV_per_atom`
  - `units`:
    - `temperature_K`: K
    - `C_V_eV_per_atom`: eV/atom

### step_06_relaxation_and_msad.csv
- path: `/app/outputs/step_06_relaxation_and_msad.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relaxation energies and mean-square atomic displacements for ordered (1000 K), SRO (1540 K), and random (4000 K) states, quantifying the impact of ordering on lattice distortions.
- schema:
  - `type`: table
  - `required_columns`: `state`, `relaxation_energy_eV_per_atom`, `MSAD_A2`
  - `units`:
    - `relaxation_energy_eV_per_atom`: eV/atom
    - `MSAD_A2`: Å²

Notes: All scored outputs are compared to hidden reference values derived from the paper's figures (SRO: Fig. 4; specific heat: Fig. 2; sublattice occupancy: Fig. 3; relaxation energies/MSAD: Fig. 6). Tolerances are set to absorb run-to-run variance from DFT code differences and stochastic MC. The relaxation energies/MSAD step is load-bearing: its results can only be correct if the final LRP ensemble and MC snapshots were genuinely produced, preventing bypass of the core training and simulation stages.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_v_sublattice_occupation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sublattice_number",
          "occupancy_V"
        ],
        "units": {
          "occupancy_V": "fraction"
        }
      },
      "description": "Vanadium sublattice occupancy fractions at a temperature below the order-disorder transition, showing which sublattice V occupies in the ordered L1₂-like state."
    },
    {
      "file": "step_03_sro_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pair",
          "shell",
          "alpha"
        ],
        "units": {
          "alpha": "dimensionless"
        }
      },
      "description": "Warren-Cowley short-range order parameters for pairs Co-V, Ni-V, Co-Ni at the first two coordination shells, computed at 1500 K (above the transition)."
    },
    {
      "file": "step_04_specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "C_V_eV_per_atom"
        ],
        "units": {
          "temperature_K": "K",
          "C_V_eV_per_atom": "eV/atom"
        }
      },
      "description": "Specific-heat capacity as a function of temperature; the peak location identifies the order-disorder transition temperature."
    },
    {
      "file": "step_06_relaxation_and_msad.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "state",
          "relaxation_energy_eV_per_atom",
          "MSAD_A2"
        ],
        "units": {
          "relaxation_energy_eV_per_atom": "eV/atom",
          "MSAD_A2": "Å²"
        }
      },
      "description": "Relaxation energies and mean-square atomic displacements for ordered (1000 K), SRO (1540 K), and random (4000 K) states, quantifying the impact of ordering on lattice distortions."
    }
  ],
  "notes": "All scored outputs are compared to hidden reference values derived from the paper's figures (SRO: Fig. 4; specific heat: Fig. 2; sublattice occupancy: Fig. 3; relaxation energies/MSAD: Fig. 6). Tolerances are set to absorb run-to-run variance from DFT code differences and stochastic MC. The relaxation energies/MSAD step is load-bearing: its results can only be correct if the final LRP ensemble and MC snapshots were genuinely produced, preventing bypass of the core training and simulation stages."
}
```

## How you are scored
A hidden verifier reads each scored artifact you write under /app/outputs and compares the values to reference results derived from the original study. The verifier checks the presence and shape of every required output, then assesses the numeric quantities. For stochastic MC‑derived results and DFT calculations with a different code (e.g., Quantum ESPRESSO instead of VASP), the comparison tolerances absorb run‑to‑run variance. Each scored step contributes a weight to the final reward; the total reward (0–1) is a weighted combination of these individual checks. Simply reporting a number without executing the pipeline will not pass the verifier, because the load‑bearing relaxation‑energy step can only be correct if the LRP ensemble was genuinely trained and the MC snapshots were genuinely produced.
