# Parametrization and validation of a force field for alumina using DFT fitting

## Problem background
Alumina (Al₂O₃) is a technologically important ceramic, valued for its hardness, high melting point, and electrical insulation. It is used in electronics, catalysts, protective coatings, and geological studies. Accurate atomistic simulations of alumina require an interatomic potential that captures both the ionic character and the many-body interactions that dominate oxide bonding. This task involves developing and validating a dipole-polarizable force field that reproduces key structural, vibrational, elastic, thermodynamic, and defect properties of alumina, as a demonstration that a relatively simple functional form can achieve high accuracy when fitted to first-principles data.

## Approach
The force field consists of partial charges on aluminium and oxygen ions, an oxygen dipole polarizability, and pairwise Morse–Buckingham short-range terms that include repulsion and (for Al–O) a short-range attraction. The potential parameters are determined by a force-matching procedure: using a 120-atom supercell of α‑Al₂O₃, classical molecular dynamics at high temperature is run to generate uncorrelated snapshot configurations. For each snapshot, density functional theory (DFT) reference energies, forces, and stresses are computed using Quantum ESPRESSO. The force field parameters are then optimized by minimizing a weighted sum of root-mean-square deviations between the potential and the DFT training data. This fitting cycle is repeated several times, each time updating the potential and generating new, more representative MD snapshots. After convergence, an independent set of DFT configurations is used to measure the final fit errors. The fitted potential is subsequently employed to calculate equilibrium crystal structures and energies for α, θ, κ and bixbyite Al₂O₃, the 30 zone‑center phonon frequencies and the six elastic constants of α‑Al₂O₃, the volume thermal expansion under the quasi‑harmonic approximation, and the formation energies of charge‑neutral defect aggregates (Al and O Frenkel pairs, Schottky quintet).

## Reproduction target
Produce the fitted force field parameters (charges, polarizability, and Morse–Buckingham constants for O–O, Al–O, and Al–Al pairs) and the following validation quantities, all computed with that fitted potential:
- Elastic constants c₁₁, c₃₃, c₄₄, c₁₂, c₁₃, c₁₄ of α‑Al₂O₃ (in GPa).
- The 30 zone‑center phonon frequencies of α‑Al₂O₃, sorted in ascending order (in THz).
- Equilibrium lattice parameters and energy per formula unit for α, θ, κ and bixbyite phases.
- Volume thermal expansion V(T)/V(300 K) for temperatures from 0 to 1200 K.
- Formation energies (in eV) of an Al Frenkel pair, an O Frenkel pair, and the Schottky quintet in α‑Al₂O₃.
A hidden verification step will compare your submitted artifacts against reference values to assess accuracy.

## Assets

- α-Al₂O₃ crystal structure (corundum): https://materialsproject.org/materials/mp-1143/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Vanderbilt ultrasoft pseudopotentials for Al and O (LDA generated): QE pseudopotential library (pslibrary)
- Phonopy: https://phonopy.github.io/phonopy/
- Crystal structures for θ, κ, and bixbyite Al₂O₃ phases

## Workflow steps

### Step 1: Generate DFT training configurations
- Role: process
- Action: Run molecular dynamics of a 120-atom α-Al₂O₃ supercell at 2500 K and zero pressure (NVE ensemble after NpT equilibration) to extract snapshot configurations. For each snapshot, compute energies, forces, and stresses with DFT (Quantum ESPRESSO, PBE GGA, Vanderbilt ultrasoft pseudopotentials, wavefunction cutoff 80 Ry, Γ-point sampling). Repeat for multiple iterations (approx. 4) to collect a training set of ~60,000 DFT force/stress/energy data points.
- Evidence: `/app/outputs/training_data_generation.log`

### Step 2: Fit force field parameters
- Role: scored (load-bearing)
- Action: Using the DFT training data, minimize a cost function (weighted RMS errors in forces, stresses, and energies) with the Powell algorithm to determine all potential parameters: partial charges, oxygen polarizability, and Morse-Buckingham short‑range parameters for O-O, Al-O, Al-Al pairs.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {"q_O": float, "q_Al": float, "alpha_O": float, "D_OO": float, "gamma_OO": float, "r0_OO": float, "b_OO": float, "c_OO": float, "D_AlO": float, "gamma_AlO": float, "r0_AlO": float, "b_AlO": float, "c_AlO": float, "D_AlAl": float, "gamma_AlAl": float, "r0_AlAl": float, "b_AlAl": float, "c_AlAl": float}
- Scoring: scored by hidden verifier

### Step 3: Validation RMS errors
- Role: scored
- Action: Generate an additional set of DFT configurations (not used in training) after the final fitting iteration, and compute the root‑mean‑square errors in forces (ΔF), stresses (ΔS), and energies (ΔE) between the fitted potential and DFT on that set.
- Output file: `/app/outputs/final_fit_RMS.json`
- Format: json
- Contract: {"Delta_F": float, "Delta_S": float, "Delta_E": float}
- Scoring: scored by hidden verifier

### Step 4: Crystal structure relaxation
- Role: scored
- Action: Perform geometry optimizations for α‑Al₂O₃, θ‑Al₂O₃, κ‑Al₂O₃, and bixbyite using the fitted potential. Report equilibrium lattice parameters and total energy per formula unit for each phase.
- Output file: `/app/outputs/crystal_energies.csv`
- Format: csv
- Contract: phase, a_au, b_au, c_au, beta_deg, energy_per_fu_eV
- Scoring: scored by hidden verifier

### Step 5: Phonon zone‑center frequencies
- Role: scored
- Action: Compute the 30 phonon frequencies at the Γ point for α‑Al₂O₃ using the fitted potential (e.g., via finite displacements and lattice dynamics with Phonopy). Report all 30 frequencies in ascending order.
- Output file: `/app/outputs/phonon_zone_center.csv`
- Format: csv
- Contract: mode_number, frequency_THz
- Scoring: scored by hidden verifier

### Step 6: Elastic constants of corundum
- Role: scored
- Action: Compute the six independent elastic constants of α‑Al₂O₃ (c11, c33, c44, c12, c13, c14) using the energy‑strain method with the fitted potential.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: {"c11": float, "c33": float, "c44": float, "c12": float, "c13": float, "c14": float}
- Scoring: scored by hidden verifier

### Step 7: Thermal expansion
- Role: scored
- Action: Under the quasi‑harmonic approximation, compute phonon spectra for several volumes and derive the volume thermal expansion V(T)/V(300 K) for temperatures from 0 to 1200 K using Phonopy or equivalent.
- Output file: `/app/outputs/thermal_expansion.csv`
- Format: csv
- Contract: T_K, V_over_V0
- Scoring: scored by hidden verifier

### Step 8: Defect formation energies
- Role: scored
- Action: Calculate the formation energies of an Al Frenkel pair, an O Frenkel pair, and the Schottky quintet (3V_O + 2V_Al) in α‑Al₂O₃ using supercells with the fitted potential. Apply finite‑size corrections (e.g., Makov–Payne) if necessary.
- Output file: `/app/outputs/defect_formation_energies.json`
- Format: json
- Contract: {"Al_Frenkel": float, "O_Frenkel": float, "Schottky": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/final_fit_RMS.json`
- `/app/outputs/crystal_energies.csv`
- `/app/outputs/phonon_zone_center.csv`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/thermal_expansion.csv`
- `/app/outputs/defect_formation_energies.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted force field parameters: charges, polarizability, and Morse-Buckingham parameters for all pairs.
- schema:
  - `type`: object
  - `required`:
    - `q_O`: float
    - `q_Al`: float
    - `alpha_O`: float
    - `D_OO`: float
    - `gamma_OO`: float
    - `r0_OO`: float
    - `b_OO`: float
    - `c_OO`: float
    - `D_AlO`: float
    - `gamma_AlO`: float
    - `r0_AlO`: float
    - `b_AlO`: float
    - `c_AlO`: float
    - `D_AlAl`: float
    - `gamma_AlAl`: float
    - `r0_AlAl`: float
    - `b_AlAl`: float
    - `c_AlAl`: float

### final_fit_RMS.json
- path: `/app/outputs/final_fit_RMS.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Root-mean-square errors of the final fitted potential on an independent DFT validation set.
- schema:
  - `type`: object
  - `required`:
    - `Delta_F`: float
    - `Delta_S`: float
    - `Delta_E`: float

### crystal_energies.csv
- path: `/app/outputs/crystal_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relaxed lattice parameters and energies per formula unit for α, θ, κ, and bixbyite Al₂O₃ phases.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `a_au`, `b_au`, `c_au`, `beta_deg`, `energy_per_fu_eV`
  - `units`:
    - `a_au`: atomic units
    - `b_au`: atomic units
    - `c_au`: atomic units
    - `beta_deg`: degrees
    - `energy_per_fu_eV`: eV per formula unit

### phonon_zone_center.csv
- path: `/app/outputs/phonon_zone_center.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: All 30 zone-center phonon frequencies of α-Al₂O₃, listed in ascending order.
- schema:
  - `type`: table
  - `required_columns`: `mode_number`, `frequency_THz`
  - `units`:
    - `frequency_THz`: THz

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Six independent elastic constants of α-Al₂O₃.
- schema:
  - `type`: object
  - `required`:
    - `c11`: float
    - `c33`: float
    - `c44`: float
    - `c12`: float
    - `c13`: float
    - `c14`: float
  - `units`:
    - `c11`: GPa
    - `c33`: GPa
    - `c44`: GPa
    - `c12`: GPa
    - `c13`: GPa
    - `c14`: GPa

### thermal_expansion.csv
- path: `/app/outputs/thermal_expansion.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Volume thermal expansion of α-Al₂O₃ relative to V(T=300 K), from 0 to 1200 K, at least 5 points.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `V_over_V0`
  - `units`:
    - `T_K`: Kelvin
    - `V_over_V0`: dimensionless

### defect_formation_energies.json
- path: `/app/outputs/defect_formation_energies.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Formation energies of Al Frenkel pair, O Frenkel pair, and Schottky quintet in α-Al₂O₃.
- schema:
  - `type`: object
  - `required`:
    - `Al_Frenkel`: float
    - `O_Frenkel`: float
    - `Schottky`: float
  - `units`:
    - `Al_Frenkel`: eV
    - `O_Frenkel`: eV
    - `Schottky`: eV

Notes: All artifacts are produced by the solving agent using open-source tools and publicly available crystal structures. The checker compares each artifact to the paper-reported values with appropriate tolerances; directionality defaults follow the metrics (e.g., lower RMS is better).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "q_O": "float",
          "q_Al": "float",
          "alpha_O": "float",
          "D_OO": "float",
          "gamma_OO": "float",
          "r0_OO": "float",
          "b_OO": "float",
          "c_OO": "float",
          "D_AlO": "float",
          "gamma_AlO": "float",
          "r0_AlO": "float",
          "b_AlO": "float",
          "c_AlO": "float",
          "D_AlAl": "float",
          "gamma_AlAl": "float",
          "r0_AlAl": "float",
          "b_AlAl": "float",
          "c_AlAl": "float"
        }
      },
      "description": "Fitted force field parameters: charges, polarizability, and Morse-Buckingham parameters for all pairs."
    },
    {
      "file": "final_fit_RMS.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "Delta_F": "float",
          "Delta_S": "float",
          "Delta_E": "float"
        }
      },
      "description": "Root-mean-square errors of the final fitted potential on an independent DFT validation set."
    },
    {
      "file": "crystal_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "a_au",
          "b_au",
          "c_au",
          "beta_deg",
          "energy_per_fu_eV"
        ],
        "units": {
          "a_au": "atomic units",
          "b_au": "atomic units",
          "c_au": "atomic units",
          "beta_deg": "degrees",
          "energy_per_fu_eV": "eV per formula unit"
        }
      },
      "description": "Relaxed lattice parameters and energies per formula unit for α, θ, κ, and bixbyite Al₂O₃ phases."
    },
    {
      "file": "phonon_zone_center.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_number",
          "frequency_THz"
        ],
        "units": {
          "frequency_THz": "THz"
        }
      },
      "description": "All 30 zone-center phonon frequencies of α-Al₂O₃, listed in ascending order."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "c11": "float",
          "c33": "float",
          "c44": "float",
          "c12": "float",
          "c13": "float",
          "c14": "float"
        },
        "units": {
          "c11": "GPa",
          "c33": "GPa",
          "c44": "GPa",
          "c12": "GPa",
          "c13": "GPa",
          "c14": "GPa"
        }
      },
      "description": "Six independent elastic constants of α-Al₂O₃."
    },
    {
      "file": "thermal_expansion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "V_over_V0"
        ],
        "units": {
          "T_K": "Kelvin",
          "V_over_V0": "dimensionless"
        }
      },
      "description": "Volume thermal expansion of α-Al₂O₃ relative to V(T=300 K), from 0 to 1200 K, at least 5 points."
    },
    {
      "file": "defect_formation_energies.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Al_Frenkel": "float",
          "O_Frenkel": "float",
          "Schottky": "float"
        },
        "units": {
          "Al_Frenkel": "eV",
          "O_Frenkel": "eV",
          "Schottky": "eV"
        }
      },
      "description": "Formation energies of Al Frenkel pair, O Frenkel pair, and Schottky quintet in α-Al₂O₃."
    }
  ],
  "notes": "All artifacts are produced by the solving agent using open-source tools and publicly available crystal structures. The checker compares each artifact to the paper-reported values with appropriate tolerances; directionality defaults follow the metrics (e.g., lower RMS is better)."
}
```

## How you are scored
After you write the required output files, a hidden verifier will read each scored artifact and compare its contents to a set of reference values. For each output, a partial score is computed based on how closely your result agrees with the reference, allowing for domain-appropriate tolerances. The partial scores are then combined with predetermined weighting to produce a final overall reward between 0 and 1. You do not have access to the reference values or the tolerances; the task is to carry out the computational workflow faithfully and write the computed quantities in the specified formats.
