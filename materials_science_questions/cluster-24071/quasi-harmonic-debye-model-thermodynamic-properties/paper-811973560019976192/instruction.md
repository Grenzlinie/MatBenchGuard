# Vibrational modes and thermodynamic properties of non-stoichiometric beta-alumina from molecular dynamics

## Problem background
Na+ beta-alumina is a fast-ion conductor with a layered structure consisting of spinel blocks separated by conduction planes containing mobile Na+ ions. Understanding its lattice vibrations and associated thermodynamic properties is important for interpreting ionic transport. Molecular dynamics (MD) simulations can compute the vibrational density of states (DOS) and infrared (IR) spectra, enabling assignment of low-frequency vibrational modes to specific atomic species and crystallographic directions. The same DOS can be used to derive thermodynamic quantities such as heat capacity, entropy, internal energy, and free energy via harmonic-oscillator theory. This task aims to reproduce such computed vibrational band assignments and thermodynamic properties for the non-stoichiometric composition Na₁.₂₂Al₁₁O₁₇.₁₁.

## Approach
The approach uses classical MD in the microcanonical (NVE) ensemble with a Born-Mayer-Huggins interatomic potential. A 3×3×1 supercell is built from the published crystal structure. After equilibration, production trajectories are recorded. From the velocity time series, the velocity autocorrelation function (VACF) is computed; Fourier transform gives the vibrational DOS, normalized to 3N degrees of freedom. Similarly, the dipole moment time series yields the dipole autocorrelation function whose Fourier transform gives the IR absorption line shape, with polarization analyzed along the a(b) and c crystallographic directions. By computing species- and direction-resolved DOS (e.g., Na+, Al, O in conduction plane, O in spinel block), contributions to IR peaks can be assigned. Finally, using the total DOS and harmonic-oscillator formulas for heat capacity, entropy, internal energy, and Helmholtz free energy, the thermodynamic properties at 300 K are obtained.

## Reproduction target
For the non-stoichiometric Na₁.₂₂Al₁₁O₁₇.₁₁ system, produce: (1) a table of IR absorption peaks below 200 cm⁻¹, with each peak's frequency (cm⁻¹), its vibrational direction (in-plane, out-of-plane, or mixed), and the dominant atomic species contributing to the mode; (2) a set of thermodynamic properties at 300 K: constant-volume heat capacity Cv (J K⁻¹ mol⁻¹), entropy S (J K⁻¹ mol⁻¹), internal energy U (kJ mol⁻¹), and Helmholtz free energy F (kJ mol⁻¹).

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov
- Born-Mayer-Huggins interatomic potential parameters (Walker-Catlow): doi:10.1088/0022-3719/15/30/019
- Crystal structure of non-stoichiometric Na+ beta-alumina: doi:10.1107/S0108768190010021

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Construct the 3a×3b×1c supercell for Na₁.₂₂Al₁₁O₁₇.₁₁ using the published crystal structure (lattice parameters a=5.56 Å, c=22.56 Å, space group P6₃/mmc, atomic positions from Edström et al. 1991) and the appropriate number of ions (22 Na⁺, 198 Al³⁺, 308 O²⁻). Generate the initial configuration file for LAMMPS.
- Evidence: `/app/outputs/supercell.lmp`

### Step 2: Molecular dynamics simulation
- Role: process
- Action: Run NVE molecular dynamics at 300 K using the Born-Mayer-Huggins potential loaded into LAMMPS. Use a time-step of 2.5 fs, equilibrate for 2000 steps, then run production for 40000 steps (100 ps). Record velocities of all ions and total dipole moment of the simulation cell every 10 fs.
- Evidence: `/app/outputs/velocities.npy`

### Step 3: Compute DOS and IR spectra
- Role: process
- Action: From the velocity time series, compute the velocity autocorrelation function (VACF) for total system and for species-/direction-resolved subsets (all Na⁺, selected O in conduction plane, O in spinel block, Al in spinel block). Fourier transform to obtain the vibrational density of states ρ(ν), normalized to ∫ρ(ν)dν = 3N. From the dipole moment time series, compute the dipole autocorrelation and Fourier transform to obtain IR absorption line-shapes I(ν) for the a(b) and c directions.
- Evidence: `/app/outputs/dos_total.csv`

### Step 4: IR peak identification and vibrational band assignment
- Role: scored (load-bearing)
- Action: From the computed total and polarized IR spectra, identify the main absorption peaks below 200 cm⁻¹. Determine the vibrational direction (in-plane, out-of-plane, mixed) based on the polarization of each peak. Assign the dominant atomic species (Na, Al, Os, Op) by inspecting the species- and direction-resolved DOS. Write the results to ir_peak_assignments.csv.
- Output file: `/app/outputs/ir_peak_assignments.csv`
- Format: csv
- Contract: columns: frequency (cm⁻¹), direction (in_plane|out_of_plane|mixed), dominant_species (comma-separated string)
- Scoring: scored by hidden verifier

### Step 5: Thermodynamic properties from DOS
- Role: scored (load-bearing)
- Action: Using the total DOS, compute Cv (J K⁻¹ mol⁻¹), S (J K⁻¹ mol⁻¹), U (kJ mol⁻¹), and F (kJ mol⁻¹) at T = 300 K via the harmonic-oscillator formulas (heat capacity, entropy, internal energy, Helmholtz free energy). Write the four scalar values to thermodynamic_properties.json.
- Output file: `/app/outputs/thermodynamic_properties.json`
- Format: json
- Contract: {"Cv": float, "S": float, "U": float, "F": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ir_peak_assignments.csv`
- `/app/outputs/thermodynamic_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ir_peak_assignments.csv
- path: `/app/outputs/ir_peak_assignments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of IR absorption peaks below 200 cm⁻¹ with their vibrational direction and dominant atomic species.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `direction`, `dominant_species`
  - `units`:
    - `frequency`: cm^-1

### thermodynamic_properties.json
- path: `/app/outputs/thermodynamic_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Thermodynamic properties at 300 K derived from the vibrational density of states.
- schema:
  - `type`: object
  - `required`:
    - `Cv`: float
    - `S`: float
    - `U`: float
    - `F`: float
  - `units`:
    - `Cv`: J K^-1 mol^-1
    - `S`: J K^-1 mol^-1
    - `U`: kJ mol^-1
    - `F`: kJ mol^-1

Notes: Verification uses result-level comparison (T0) against hidden paper-reported values with tolerances for frequency and absolute tolerances for thermodynamic quantities.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ir_peak_assignments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "direction",
          "dominant_species"
        ],
        "units": {
          "frequency": "cm^-1"
        }
      },
      "description": "Table of IR absorption peaks below 200 cm⁻¹ with their vibrational direction and dominant atomic species."
    },
    {
      "file": "thermodynamic_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Cv": "float",
          "S": "float",
          "U": "float",
          "F": "float"
        },
        "units": {
          "Cv": "J K^-1 mol^-1",
          "S": "J K^-1 mol^-1",
          "U": "kJ mol^-1",
          "F": "kJ mol^-1"
        }
      },
      "description": "Thermodynamic properties at 300 K derived from the vibrational density of states."
    }
  ],
  "notes": "Verification uses result-level comparison (T0) against hidden paper-reported values with tolerances for frequency and absolute tolerances for thermodynamic quantities."
}
```

## How you are scored
A hidden verifier compares your submitted ir_peak_assignments.csv and thermodynamic_properties.json to reference values derived from the original study. For the IR peaks, it checks that the frequencies, direction assignments, and dominant species match the expected assignments; for the thermodynamic quantities, it checks that the values fall within acceptable agreement. The final score is a weighted combination of the fraction of correctly matched peaks and the accuracy of the thermodynamic values. Simply reporting numbers is not sufficient; the underlying simulation and analysis must produce artifacts that agree with the reference within the expected precision of a re-implemented workflow.
