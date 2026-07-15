# Compute phonon frequencies and ordering energies for Si, Ge, and SiGe using a long-range empirical interatomic potential

## Problem background
Accurate interatomic potentials for covalent semiconductors are critical for studying structural and vibrational properties. Short-range empirical potentials often fail to simultaneously reproduce the correct elastic constants and the full phonon dispersion, in particular the flattening of the transverse acoustic (TA) branches in Si and Ge. A potential that incorporates longer-range angular and dihedral interactions, analogous to those in valence force field models, has been proposed to overcome this limitation. Here, you will implement such a potential and compute key material properties to test its ability to capture the relevant physics.

## Approach
The interatomic potential expresses the total cohesive energy as a sum over pairwise interactions that combine a repulsive exponential term with a coordination-dependent attractive term, modulated by an angular correction function. This correction function includes bond-angle deviations, bond-stretching contributions, and dihedral terms that extend the interaction range. The potential parameters for Si, Ge, and the mixed Si–Ge system, as well as the valence force field (VFF) constants that enter the angular terms, are provided as bundled resource files.

Using this potential, you will:
- Build the diamond cubic unit cells of Si and Ge, and a zinc-blende SiGe unit cell, and compute elastic constants (c₁₁, c₁₂, c₄₄) by applying small strains and fitting the stress response.
- Construct supercells of Si and Ge, displace atoms to obtain force constants, build the dynamical matrix, and diagonalize it at the Γ, X, and L k‑points to extract the optical phonon frequency at Γ and the TA frequencies at X and L.
- Construct a supercell for the RH1 ordered phase of SiGe (AB layer stacking along [100]) and a random alloy supercell of equal composition, relax both structures via energy minimization, and extract the cohesive energy difference and the axial ratio c/a of the ordered phase.

## Reproduction target
Implement the described potential and compute the following quantities:

1. Elastic constants c₁₁, c₁₂, and c₄₄ for Si, Ge, and the zinc-blende SiGe compound, in units of 10¹¹ N/m², written to step_01_elastic_constants.csv.
2. The highest optical phonon frequency at the Γ point and the lowest transverse acoustic (TA) frequencies at the X and L points for Si and Ge, in cm⁻¹, written to step_02_phonon_frequencies.csv.
3. The cohesive energy per atom (in meV/atom) of the RH1 ordered phase and a random SiGe alloy, and the axial ratio c/a of the RH1 phase, written to step_03_ordering_energy.csv.

## Assets

- VFF parameters for Si and Ge from Tubino et al. (Table VII)
- Potential parameter set for Si, Ge, and Si–Ge (Table I)
- Atomic Simulation Environment (ASE): https://pypi.org/project/ase/
- NumPy: numpy

## Workflow steps

### Step 1: Implement interatomic potential
- Role: process
- Action: Implement the extended empirical interatomic potential for Si, Ge, and Si–Ge using the provided VFF parameters and potential parameter sets. Write a function/class that computes total energy and forces for a given set of atomic positions and species.
- Evidence: `/app/outputs/potential_implementation.log`

### Step 2: Compute elastic constants
- Role: scored
- Action: Construct the diamond cubic unit cells for Si and Ge, and a hypothetical zinc-blende SiGe unit cell. Apply small strains and compute the resulting stress tensor using the implemented potential; fit the stress–strain curves to obtain the elastic constants c11, c12, c44. Report the values in units of 10^11 N/m².
- Output file: `/app/outputs/step_01_elastic_constants.csv`
- Format: csv
- Contract: CSV with header: material,c11,c12,c44; one row per material (Si, Ge, SiGe).
- Scoring: scored by hidden verifier

### Step 3: Calculate phonon frequencies at high-symmetry points
- Role: scored
- Action: Build supercells for Si and Ge, displace atoms, and compute forces using the implemented potential to construct the dynamical matrix. Diagonalize the matrix at the Γ, X, and L points. Extract the highest optical frequency at Γ and the lowest transverse acoustic (TA) frequencies at X and L. Convert to cm⁻¹.
- Output file: `/app/outputs/step_02_phonon_frequencies.csv`
- Format: csv
- Contract: CSV with header: material,Gamma_optic_cm-1,X_TA_cm-1,L_TA_cm-1; one row per material (Si, Ge).
- Scoring: scored by hidden verifier

### Step 4: Relax RH1 ordered and random SiGe structures
- Role: process
- Action: Construct a supercell for the RH1 ordered phase (AB stacking of Si and Ge layers along [100]) and a random alloy supercell of equal composition. Relax both structures using energy minimization (steepest descent) with the implemented potential, allowing tetrahedral relaxation and volume relaxation.
- Evidence: `/app/outputs/relaxation_log.txt`

### Step 5: Compute ordering energy and axial ratio
- Role: scored (load-bearing)
- Action: From the relaxed structures, extract the cohesive energy per atom for the RH1 phase and the random phase. Compute the axial ratio c/a of the RH1 phase from the supercell lattice vectors. Report the energies in meV/atom and c/a dimensionless.
- Output file: `/app/outputs/step_03_ordering_energy.csv`
- Format: csv
- Contract: CSV with header: phase,energy_meV_per_atom,c_over_a; two rows with phase values 'RH1' and 'random'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_elastic_constants.csv`
- `/app/outputs/step_02_phonon_frequencies.csv`
- `/app/outputs/step_03_ordering_energy.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_elastic_constants.csv
- path: `/app/outputs/step_01_elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Elastic constants c11, c12, c44 computed for Si, Ge, and zinc-blende SiGe.
- schema:
  - `type`: table
  - `required_columns`: `material`, `c11`, `c12`, `c44`
  - `units`:
    - `c11`: 10^11 N/m²
    - `c12`: 10^11 N/m²
    - `c44`: 10^11 N/m²

### step_02_phonon_frequencies.csv
- path: `/app/outputs/step_02_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies at Γ, X, and L points for Si and Ge.
- schema:
  - `type`: table
  - `required_columns`: `material`, `Gamma_optic_cm-1`, `X_TA_cm-1`, `L_TA_cm-1`
  - `units`:
    - `Gamma_optic_cm-1`: cm⁻¹
    - `X_TA_cm-1`: cm⁻¹
    - `L_TA_cm-1`: cm⁻¹

### step_03_ordering_energy.csv
- path: `/app/outputs/step_03_ordering_energy.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cohesive energy per atom and axial ratio c/a for RH1 ordered and random SiGe phases.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `energy_meV_per_atom`, `c_over_a`
  - `units`:
    - `energy_meV_per_atom`: meV/atom
    - `c_over_a`: dimensionless

Notes: All scored artifacts are compared to hidden reference values derived from the paper's reported results, with appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "c11",
          "c12",
          "c44"
        ],
        "units": {
          "c11": "10^11 N/m²",
          "c12": "10^11 N/m²",
          "c44": "10^11 N/m²"
        }
      },
      "description": "Elastic constants c11, c12, c44 computed for Si, Ge, and zinc-blende SiGe."
    },
    {
      "file": "step_02_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "Gamma_optic_cm-1",
          "X_TA_cm-1",
          "L_TA_cm-1"
        ],
        "units": {
          "Gamma_optic_cm-1": "cm⁻¹",
          "X_TA_cm-1": "cm⁻¹",
          "L_TA_cm-1": "cm⁻¹"
        }
      },
      "description": "Phonon frequencies at Γ, X, and L points for Si and Ge."
    },
    {
      "file": "step_03_ordering_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "energy_meV_per_atom",
          "c_over_a"
        ],
        "units": {
          "energy_meV_per_atom": "meV/atom",
          "c_over_a": "dimensionless"
        }
      },
      "description": "Cohesive energy per atom and axial ratio c/a for RH1 ordered and random SiGe phases."
    }
  ],
  "notes": "All scored artifacts are compared to hidden reference values derived from the paper's reported results, with appropriate tolerances."
}
```

## How you are scored
A hidden verifier script will automatically evaluate each of your three scored output files. For every file, the verifier compares your reported values to reference values using tolerances that account for typical implementation differences (choice of finite-difference step, force convergence, etc.). The three stages are scored independently, and the overall reward is a weighted sum of these stage scores. You must produce the required CSV files with the exact column schema; printing a claimed result elsewhere will not contribute to your score.
