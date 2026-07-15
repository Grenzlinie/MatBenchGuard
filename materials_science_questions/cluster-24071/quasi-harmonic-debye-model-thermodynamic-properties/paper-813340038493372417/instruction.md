# Lattice constant, phonon softening, and heat capacity of Mg2Si1-xSnx alloy from first principles

## Problem background
Mg2Si1-xSnx alloys are promising thermoelectric materials that can achieve low lattice thermal conductivity through mass disorder scattering. To understand and tune this behaviour, it is essential to quantify how structural, vibrational, and thermodynamic properties vary with Sn content. This task investigates the variation of the equilibrium lattice constant across the composition range, the softening of optical phonon modes between the end members Mg2Si and Mg2Sn, and the temperature-dependent constant-volume heat capacity of Mg2Si.

## Approach
Use density functional theory (DFT) with the GGA-PBE exchange-correlation functional and ultrasoft pseudopotentials to relax the atomic geometry and lattice parameters of Mg2Si1-xSnx for six Sn concentrations (x = 0, 0.125, 0.25, 0.75, 0.875, 1). For each composition, construct a suitable supercell and replace Si by Sn to achieve the desired stoichiometry. After geometry optimization, compute the room‑temperature phonon frequencies at the Γ point for the pure end members (x = 0 and x = 1) using density functional perturbation theory (DFPT). Then perform a full phonon density‑of‑states calculation for Mg2Si on a q‑point grid and integrate it in the harmonic approximation to obtain the constant‑volume heat capacity C_v as a function of temperature.

## Reproduction target
Generate equilibrium lattice constants for six Sn fractions (x = 0, 0.125, 0.25, 0.75, 0.875, 1). From these data, determine whether the lattice constant follows a linear Vegard's‑law trend and extract the effective slope and intercept of that fit. Compute the highest optical phonon frequency at the Γ point for Mg2Si (x = 0) and Mg2Sn (x = 1). For Mg2Si, calculate the constant‑volume heat capacity C_v as a function of temperature from 0 to 1000 K, reporting values at least at 300 K and 1000 K. The completed artifacts (lattice constants, phonon frequencies, heat capacity) must be saved as CSV files.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotentials library: https://www.materialscloud.org/discover/sssp/

## Workflow steps

### Step 1: Structure generation
- Role: process
- Action: Generate initial atomic structures for Mg2Si1-xSnx at Sn concentrations x=0, 0.125, 0.25, 0.75, 0.875, 1 using appropriate supercell sizes: primitive cell for x=0 and x=1, conventional cell for x=0.25 and 0.75, 2x2x2 supercell for x=0.125 and 0.875. Substitute Sn for Si atoms accordingly. Represent the structures in a format suitable for DFT calculations (e.g., Quantum ESPRESSO input files).
- Evidence: `/app/outputs/structure_inputs.json`

### Step 2: DFT geometry optimization
- Role: process
- Action: Perform DFT geometry optimization for each structure using Quantum ESPRESSO with the GGA-PBE exchange-correlation functional and ultrasoft pseudopotentials. Choose appropriate plane-wave kinetic energy cutoff and k-point grids (comparable to the paper's settings: ~300 eV and 6x6x6/4x4x4/3x3x3 depending on supercell size). Relax both atomic positions and cell parameters to obtain equilibrium lattice constants.
- Evidence: `/app/outputs/optimization.log`

### Step 3: Lattice constants
- Role: scored (load-bearing)
- Action: Extract the relaxed lattice constants for each Sn concentration and save them to lattice_constants.csv.
- Output file: `/app/outputs/lattice_constants.csv`
- Format: csv
- Contract: x (float), lattice_constant (float) — one row per composition
- Scoring: scored by hidden verifier

### Step 4: Phonon Gamma-point frequencies
- Role: scored
- Action: Using density functional perturbation theory (DFPT) in Quantum ESPRESSO, compute phonon frequencies at the Gamma point for the optimized structures of pure Mg2Si (x=0) and pure Mg2Sn (x=1). Identify the highest optical phonon frequency for each and save to phonon_gamma_frequencies.csv.
- Output file: `/app/outputs/phonon_gamma_frequencies.csv`
- Format: csv
- Contract: x (float), highest_optical_frequency (float)
- Scoring: scored by hidden verifier

### Step 5: Heat capacity
- Role: scored
- Action: Compute the full phonon density of states (DOS) for pure Mg2Si using DFPT on a q-point grid. From the phonon DOS, calculate the temperature-dependent constant-volume heat capacity C_v in the harmonic approximation for T from 0 to 1000 K. Output the results to heat_capacity.csv.
- Output file: `/app/outputs/heat_capacity.csv`
- Format: csv
- Contract: T (float), C_v (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_constants.csv`
- `/app/outputs/phonon_gamma_frequencies.csv`
- `/app/outputs/heat_capacity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_constants.csv
- path: `/app/outputs/lattice_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium lattice constants for six Sn concentrations. The hidden checker will compare each submitted lattice constant to a hidden reference value within a tolerance and verify that the lattice constant increases monotonically with x.
- schema:
  - `type`: table
  - `required_columns`: `x`, `lattice_constant`
  - `units`:
    - `lattice_constant`: Angstrom

### phonon_gamma_frequencies.csv
- path: `/app/outputs/phonon_gamma_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Highest optical phonon frequency at the Gamma point for x=0 and x=1. The hidden checker will verify that the frequency for Mg2Si is greater than for Mg2Sn (trend) and compare absolute values to hidden reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `x`, `highest_optical_frequency`
  - `units`:
    - `highest_optical_frequency`: cm^{-1}

### heat_capacity.csv
- path: `/app/outputs/heat_capacity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Constant-volume heat capacity of Mg2Si as a function of temperature. The hidden checker will compare C_v at 300 K and 1000 K to hidden reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `T`, `C_v`
  - `units`:
    - `T`: K
    - `C_v`: J*mol^{-1}*K^{-1}

Notes: The task focuses on the lattice constant trend (Vegard's law), the phonon softening between pure Mg2Si and Mg2Sn, and the harmonic heat capacity of Mg2Si. Elastic constants and full phonon dispersion curves are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "lattice_constant"
        ],
        "units": {
          "lattice_constant": "Angstrom"
        }
      },
      "description": "Equilibrium lattice constants for six Sn concentrations. The hidden checker will compare each submitted lattice constant to a hidden reference value within a tolerance and verify that the lattice constant increases monotonically with x."
    },
    {
      "file": "phonon_gamma_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "highest_optical_frequency"
        ],
        "units": {
          "highest_optical_frequency": "cm^{-1}"
        }
      },
      "description": "Highest optical phonon frequency at the Gamma point for x=0 and x=1. The hidden checker will verify that the frequency for Mg2Si is greater than for Mg2Sn (trend) and compare absolute values to hidden reference values within tolerance."
    },
    {
      "file": "heat_capacity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "C_v"
        ],
        "units": {
          "T": "K",
          "C_v": "J*mol^{-1}*K^{-1}"
        }
      },
      "description": "Constant-volume heat capacity of Mg2Si as a function of temperature. The hidden checker will compare C_v at 300 K and 1000 K to hidden reference values within tolerance."
    }
  ],
  "notes": "The task focuses on the lattice constant trend (Vegard's law), the phonon softening between pure Mg2Si and Mg2Sn, and the harmonic heat capacity of Mg2Si. Elastic constants and full phonon dispersion curves are not required."
}
```

## How you are scored
A hidden verifier independently evaluates each of the three scored output artifacts: (1) lattice constants CSV – the verifier fits a linear model to your data and compares the slope and intercept against hidden reference values, also checking monotonic increase with x; (2) phonon frequencies CSV – the verifier verifies the trend (whether Mg2Si has a higher optical frequency than Mg2Sn) and compares the absolute frequencies to hidden references; (3) heat capacity CSV – the verifier compares C_v at 300 K and 1000 K to hidden reference values. The three stages carry weights of 50% (lattice), 25% (phonon frequencies), and 25% (heat capacity), and the combined score is reported as a single reward between 0 and 1.
