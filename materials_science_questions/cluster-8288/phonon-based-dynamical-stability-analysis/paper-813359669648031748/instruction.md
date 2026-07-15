# Dynamical stability and electronic density of states of vanadium nitride phases

## Problem background
Vanadium nitrides exhibit interesting mechanical and electronic properties, but the experimentally observed crystal structures of stoichiometric VN conflict with simple first-principles predictions. While low-temperature experiments detect cubic, tetragonal, or triclinic phases, ground-state calculations suggest hexagonal polymorphs are more stable. This contradiction motivates a systematic first-principles investigation of the relative stability of several VN phases, including the role of lattice dynamics and of vacancies and impurities that may shift the balance. The present task computes total energies, phonon density of states, and electronic densities of states for stoichiometric and defective vanadium nitride structures, providing quantitative evidence for the structural preferences observed in experiment.

## Approach
The workflow employs density functional theory (DFT) within the generalized gradient approximation (PBE) and density functional perturbation theory (DFPT) for phonons, as implemented in the open-source QUANTUM ESPRESSO suite. Vanderbilt ultrasoft pseudopotentials are used for vanadium, nitrogen, carbon, and oxygen. The study proceeds in three stages:
- **Total energies of stoichiometric phases:** Build unit cells for the NaCl, WC, AsNi, t-VN, ZnS, and CsCl structures of VN; relax cell parameters and atomic positions until forces and stresses are negligible; extract the total energy per atom. The relative order of these energies indicates thermodynamic stability at zero temperature.
- **Dynamic stability through phonon spectra:** Compute phonon dispersions and densities of states (PHDOS) via DFPT for the four lowest-energy phases. The presence of imaginary (negative) frequency modes signals lattice instability.
- **Effect of vacancies and impurities:** Construct 64-atom supercells of NaCl-based and WC-based VN with varying concentrations of vanadium/nitrogen vacancies (x = 1.0, 0.96875, 0.9375, 0.90625, 0.875) and with carbon or oxygen substitutions. Relax these supercells and compute the electronic density of states at the Fermi level, N(E_F). The trends in N(E_F) with composition are compared to the total-energy trends to infer the electronic origin of phase stabilization.

## Reproduction target
Produce three tabular artifacts that capture the main computed results:
1. A file `step_01_total_energies.csv` listing each stoichiometric VN phase and its total energy per atom (in meV/atom). The verification will check the relative ordering of the six phases.
2. A file `step_02_phonon_stability.csv` with a boolean flag for each of the four low-energy phases indicating whether imaginary phonon modes were detected (true) or not (false).
3. A file `step_03_NofEF.csv` with columns for structure type (NaCl-based or WC-based), composition label, and N(E_F) in states/eV per unit cell. The checks will verify monotonic trends of N(E_F) with vacancy concentration and the direction of N(E_F) shifts upon carbon or oxygen substitution, all without requiring absolute numerical agreement with a particular reference.

## Assets

- QUANTUM ESPRESSO: https://www.quantum-espresso.org/
- Vanderbilt ultrasoft pseudopotential for V (PBE): https://www.quantum-espresso.org/pseudopotentials
- Pseudopotential for N (PBE): https://www.quantum-espresso.org/pseudopotentials
- Pseudopotential for C (PBE): https://www.quantum-espresso.org/pseudopotentials
- Pseudopotential for O (PBE): https://www.quantum-espresso.org/pseudopotentials

## Workflow steps

### Step 1: Generate input structures
- Role: process
- Action: Construct unit cells for the six VN phases using the following lattice parameters:

| Structure | a (Å) | b (Å) | c (Å) | α (°) | β (°) | γ (°) |
|-----------|-------|-------|-------|-------|-------|-------|
| NaCl      | 4.126 | 4.126 | 4.126 | 90 | 90 | 90 |
| WC        | 2.751 | 2.751 | 2.641 | 90 | 90 | 120 |
| AsNi      | 2.771 | 2.771 | 5.149 | 90 | 90 | 120 |
| t-VN      | 4.153 | 4.153 | 4.046 | 90 | 90 | 90 |
| ZnS       | 4.285 | 4.285 | 4.285 | 90 | 90 | 90 |
| CsCl      | 2.539 | 2.539 | 2.539 | 90 | 90 | 90 |

Build 64-atom supercells for NaCl-based and WC-based V_xN_x with vacancy concentrations x = 1.0, 0.96875, 0.9375, 0.90625, 0.875, and impurity supercells V32N29C3 and V32N29O3, by adding/removing atoms appropriately.
- Evidence: none

### Step 2: DFT geometry optimization and total energy
- Role: process
- Action: For each structure (six unit cells and all supercells), perform DFT relaxation using QUANTUM ESPRESSO with Vanderbilt ultrasoft pseudopotentials, PBE GGA, plane-wave cutoff 38 Ry, and appropriate k-point meshes. Relax cell parameters and atomic positions until forces < 1 mRy/bohr and stresses < 0.025 GPa. Record equilibrium total energies and structures.
- Evidence: none

### Step 3: Total energies of stoichiometric VN phases
- Role: scored
- Action: Extract total energy per atom (in meV/atom) for the six stoichiometric phases (WC, AsNi, t-VN, NaCl, ZnS, CsCl) from the relaxation results and write to step_01_total_energies.csv.
- Output file: `/app/outputs/step_01_total_energies.csv`
- Format: csv
- Contract: columns: phase (string), total_energy_per_atom_meV (float)
- Scoring: scored by hidden verifier

### Step 4: DFPT phonon calculations
- Role: process
- Action: For the WC, AsNi, t-VN, and NaCl relaxed structures, compute phonon dispersion and density of states using DFPT with a 6x6x6 q-mesh and interpolate to obtain PHDOS. Identify imaginary (negative) frequency modes.
- Evidence: none

### Step 5: Phonon dynamical stability flags
- Role: scored
- Action: Write a CSV file indicating for each of the four phases whether imaginary phonon modes are present (true) or not (false).
- Output file: `/app/outputs/step_02_phonon_stability.csv`
- Format: csv
- Contract: columns: phase (string), has_imaginary_modes (boolean)
- Scoring: scored by hidden verifier

### Step 6: Electronic density of states calculations
- Role: process
- Action: For all NaCl-based and WC-based supercells (stoichiometric, vacancy-containing, impurity-containing), compute total DOS using fine k-point meshes and extract N(E_F), the density of states at the Fermi level.
- Evidence: none

### Step 7: Fermi-level DOS values
- Role: scored (load-bearing)
- Action: Write step_03_NofEF.csv with N(E_F) for each configuration.
- Output file: `/app/outputs/step_03_NofEF.csv`
- Format: csv
- Contract: columns: structure_type (string, 'NaCl-based' or 'WC-based'), configuration (string, e.g., V32N32, V31N31, V30N30, V29N29, V28N28, V32N29C3, V32N29O3), N_E_F (float, units states/eV per unit cell)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_total_energies.csv`
- `/app/outputs/step_02_phonon_stability.csv`
- `/app/outputs/step_03_NofEF.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_total_energies.csv
- path: `/app/outputs/step_01_total_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Total energy per atom for each stoichiometric VN phase. The checker verifies a specific ordering among the six phases.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `total_energy_per_atom_meV`
  - `units`:
    - `total_energy_per_atom_meV`: meV/atom

### step_02_phonon_stability.csv
- path: `/app/outputs/step_02_phonon_stability.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon stability flags for the four phases; the checker verifies a specific pattern of imaginary modes.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `has_imaginary_modes`

### step_03_NofEF.csv
- path: `/app/outputs/step_03_NofEF.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Fermi-level DOS for NaCl-based and WC-based structures. The checker verifies monotonic trends and relative shifts for impurity substitutions.
- schema:
  - `type`: table
  - `required_columns`: `structure_type`, `configuration`, `N_E_F`
  - `units`:
    - `N_E_F`: states/eV/unit cell

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_total_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "total_energy_per_atom_meV"
        ],
        "units": {
          "total_energy_per_atom_meV": "meV/atom"
        }
      },
      "description": "Total energy per atom for each stoichiometric VN phase. The checker verifies a specific ordering among the six phases."
    },
    {
      "file": "step_02_phonon_stability.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "has_imaginary_modes"
        ]
      },
      "description": "Phonon stability flags for the four phases; the checker verifies a specific pattern of imaginary modes."
    },
    {
      "file": "step_03_NofEF.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure_type",
          "configuration",
          "N_E_F"
        ],
        "units": {
          "N_E_F": "states/eV/unit cell"
        }
      },
      "description": "Fermi-level DOS for NaCl-based and WC-based structures. The checker verifies monotonic trends and relative shifts for impurity substitutions."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects each required output file after your run. It does not look for exact numerical agreement with any single external value; instead, it assesses structural consistency:
- For total energies, it checks that your reported values satisfy a specific ordering among the phases.
- For phonon stability, it verifies the boolean flags against the expected pattern of imaginary modes.
- For N(E_F), it tests monotonicity as a function of vacancy concentration and the relative changes for impurity-containing supercells.
Each check contributes an independent weighted score to a final reward between 0 and 1. To obtain the full reward, you must genuinely execute the DFT and DFPT protocols; the verifier may also perform self-consistency checks across artifacts that are difficult to satisfy by fabrication alone.
