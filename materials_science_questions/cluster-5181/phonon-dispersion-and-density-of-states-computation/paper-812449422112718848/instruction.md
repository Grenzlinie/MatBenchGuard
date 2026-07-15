# Specific Heat of Andalusite from Shell Model Lattice Dynamics

## Problem background
Andalusite (Al₂SiO₅) is a geologically important aluminosilicate mineral that occurs in a wide range of metamorphic rocks. Its thermodynamic stability and phase relationships with other Al₂SiO₅ polymorphs (sillimanite, kyanite) are essential for geothermobarometry — reconstructing the pressures and temperatures at which rocks formed. A central thermodynamic property is the specific heat at constant pressure Cₚ as a function of temperature, which governs heat capacity and phase equilibrium calculations. While experimental measurements exist, computational prediction of Cₚ from first-principles lattice dynamics offers a route to understanding the underlying atomic-scale mechanisms and to extrapolating properties to conditions not easily accessed in the laboratory. The goal of this task is to compute Cₚ of andalusite using a transferable shell model interatomic potential and harmonic/quasi-harmonic lattice dynamics.

## Approach
The core idea is to treat the crystal as a set of interacting ions described by a shell model potential, with oxygen ions partitioned into a massive core and a massless shell connected by a harmonic spring. The interatomic potential parameters (Coulomb and short-range terms, plus shell-core springs) for the Al₂SiO₅ system are taken from Rao et al. (1999), Phys. Rev. B 60, 12061. Starting from the experimentally determined crystal structure (space group Pnnm, provided below), the equilibrium geometry — lattice constants and atomic coordinates — is obtained by energy minimization. From the relaxed structure, harmonic phonon frequencies, eigenvectors, and the phonon density of states g(E) are computed. The specific heat at constant volume C_V(T) is obtained by integrating the phonon DOS. To compute the specific heat at constant pressure, the correction term Cₚ − C_V = T V B α² is required, where V is the molar volume, B the bulk modulus, and α the volumetric coefficient of thermal expansion. Elastic constants and the bulk modulus can be derived from acoustic phonon slopes or by direct strain-energy calculations; α is evaluated in the quasi-harmonic approximation by computing the phonon free energy at several volumes. All calculations can be implemented with standard open-source lattice dynamics packages such as Phonopy, GULP, or LAMMPS. The workflow comprises four ordered stages: (1) equilibrium structure relaxation, (2) phonon DOS calculation, (3) elastic constants and thermal expansion, (4) evaluation of Cₚ at the requested temperatures.

## Reproduction target
Produce a CSV file named `Cp_vs_T.csv` containing the computed specific heat at constant pressure of andalusite at the following four temperatures: 300 K, 500 K, 1000 K, and 1500 K. The file must have two columns: `temperature_K` (floating-point, in kelvin) and `Cp_J_per_mol_K` (floating-point, in J/(mol·K)), with one row for each temperature.

## Assets

- Shell model interatomic potential parameters for Al2SiO5: 10.1103/PhysRevB.60.12061
- Experimental crystal structure of andalusite
- Open-source lattice dynamics software (e.g., Phonopy, GULP, LAMMPS): https://phonopy.github.io/phonopy/

## Workflow steps

### Step 1: Equilibrium crystal structure calculation
- Role: process
- Action: Using the interatomic potential parameters and the experimental starting structure, minimize the energy to obtain the equilibrium lattice parameters and atomic fractional coordinates of andalusite.
- Evidence: `/app/outputs/structure.json`

### Step 2: Phonon dispersion and density of states calculation
- Role: process
- Action: Perform harmonic lattice dynamics using the relaxed structure and the interatomic potential. Compute phonon frequencies, eigenvectors, and the total phonon density of states g(E).
- Evidence: `/app/outputs/phonon_dos.dat`

### Step 3: Elastic constants and thermal expansion
- Role: process
- Action: From the acoustic phonon slopes (or via strain-energy method) compute the elastic constants and the bulk modulus B. Compute the volumetric coefficient of thermal expansion α within the quasi-harmonic approximation by evaluating the equation of state at several volumes.
- Evidence: `/app/outputs/elastic_thermal.json`

### Step 4: Specific heat at constant pressure
- Role: scored (load-bearing)
- Action: From the phonon DOS g(E), compute C_V(T) by integration. Then calculate C_P(T) = C_V(T) + T V B α^2 using the previously determined B, α, and the molar volume V. Record C_P values at T = 300 K, 500 K, 1000 K, and 1500 K.
- Output file: `/app/outputs/Cp_vs_T.csv`
- Format: csv
- Contract: CSV with columns: temperature_K (float), Cp_J_per_mol_K (float). Rows for T=300, 500, 1000, and 1500 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/Cp_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### Cp_vs_T.csv
- path: `/app/outputs/Cp_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed specific heat at constant pressure at 300 K, 500 K, 1000 K, and 1500 K. The checker compares these values against hidden experimental gold values digitized from Fig. 6 of the paper, awarding full credit if the absolute relative error ≤ 5% with linear decay to 0 at 10% error.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `Cp_J_per_mol_K`
  - `units`:
    - `temperature_K`: K
    - `Cp_J_per_mol_K`: J/(mol*K)

Notes: Only the specific heat is scored; intermediate artifacts (structure, phonon DOS, elastic/thermal) are evidence of process execution but not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "Cp_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "Cp_J_per_mol_K"
        ],
        "units": {
          "temperature_K": "K",
          "Cp_J_per_mol_K": "J/(mol*K)"
        }
      },
      "description": "Computed specific heat at constant pressure at 300 K, 500 K, 1000 K, and 1500 K. The checker compares these values against hidden experimental gold values digitized from Fig. 6 of the paper, awarding full credit if the absolute relative error ≤ 5% with linear decay to 0 at 10% error."
    }
  ],
  "notes": "Only the specific heat is scored; intermediate artifacts (structure, phonon DOS, elastic/thermal) are evidence of process execution but not directly scored."
}
```

## How you are scored
A hidden verifier reads your `/app/outputs/Cp_vs_T.csv` and extracts the Cₚ values at the four target temperatures. It compares each value to experimental specific heat measurements (not provided to you) via the absolute relative error. For each temperature, the verifier assigns a score between 0 and 1, with full credit for very small errors and gradually decreasing credit as the error grows; large errors receive zero. The final reward is the average of the four per-temperature scores. The intermediate evidence files (structure.json, phonon_dos.dat, elastic_thermal.json) are not directly scored but must be present as documentation of the workflow execution.
