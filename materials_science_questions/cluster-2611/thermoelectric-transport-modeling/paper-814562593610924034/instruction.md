# Bipolar Two-Band Boltzmann Transport and Callaway Model for InAs Nanowire Thermoelectric Properties

## Problem background
InAs nanowires are candidates for thermoelectric applications, and their performance is influenced by carrier concentration and microstructural defects. This work examines the effects of Si doping and planar defects (twins, stacking faults) on the thermoelectric properties of InAs nanowires. Two computational models are employed: a bipolar two-band Boltzmann transport model relates the Seebeck coefficient and electrical conductivity to the Fermi energy, and the Callaway model describes the reduction of lattice thermal conductivity due to phonon scattering at boundaries and defects. The goal is to determine the Fermi energies of undoped and Si-doped nanowires consistent with measured Seebeck coefficients, and to quantify the lattice thermal conductivity with and without planar defects at 300 K.

## Approach
The two-band Boltzmann transport approach models conduction and valence bands with given intrinsic InAs effective masses, mobilities, band gap, and a scattering exponent. The Seebeck coefficient and electrical conductivity are expressed as functions of the reduced Fermi energy. Using the reported experimental Seebeck coefficients for an undoped and a Si-doped nanowire, the Fermi energy that reproduces each measured Seebeck value is found by numerical inversion. The corresponding electrical conductivities are then computed from the same model. The Callaway model for lattice thermal conductivity integrates over phonon frequencies with contributions from Umklapp, boundary, and point-defect scattering, characterized by given InAs phonon parameters. By specifying two effective boundary scattering lengths – one representing a nanowire without planar defects and one with a high density of planar defects – the model predicts the lattice thermal conductivity in both scenarios at 300 K.

## Reproduction target
Reproduce the two-band model calculation to obtain Fermi energies (meV) and electrical conductivities (S/m) for the undoped and Si-doped nanowires at 300 K, given their measured Seebeck coefficients (-216 μV/K and -81 μV/K). Reproduce the Callaway model calculation to obtain lattice thermal conductivities (W/m·K) at 300 K for effective phonon scattering lengths of 110 nm and 28 nm. The results must be written to two CSV files with the exact columns and formats specified in the workflow steps and output contract.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Two-band model: Fermi energies and conductivities
- Role: scored
- Action: Implement the bipolar two-band Boltzmann transport model equations with given intrinsic InAs parameters (scattering exponent r=-1/2, effective masses m_e*=0.023 m0, m_p*=0.41 m0, mobilities μ_e=4×10^4 cm²/Vs, μ_p=500 cm²/Vs, reference Fermi energy E_F,ref=0.354 eV, band gap E_g=0.354 eV) at 300 K. For each sample (undoped with measured Seebeck coefficient -216 μV/K; Si-doped with -81 μV/K), numerically determine the Fermi energy that reproduces the measured Seebeck coefficient, and compute the corresponding electrical conductivity. Write results to CSV.
- Output file: `/app/outputs/two_band_model_results.csv`
- Format: csv
- Contract: Columns: sample (string: 'undoped' or 'Si-doped'), measured_Seebeck_uV_per_K (float), Fermi_energy_meV (float), electrical_conductivity_S_per_m (float).
- Scoring: scored by hidden verifier

### Step 2: Callaway model: lattice thermal conductivity
- Role: scored
- Action: Implement the Callaway model with provided InAs phonon parameters (Debye temperature θ_D=114.57 K, B=6×10^-19 s/K, b=64 K, A=0.8×10^-44 s^3, sound velocity ν=2540 m/s, boundary scattering factor F=1) at 300 K. Compute the lattice thermal conductivity for two effective phonon scattering lengths: L=110 nm (defect-free) and L=28 nm (with planar defects). Write results to CSV.
- Output file: `/app/outputs/callaway_model_results.csv`
- Format: csv
- Contract: Columns: thickness_nm (float), lattice_thermal_conductivity_W_per_m_K (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/two_band_model_results.csv`
- `/app/outputs/callaway_model_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### two_band_model_results.csv
- path: `/app/outputs/two_band_model_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Derived Fermi energies and electrical conductivities from the two-band model for the two nanowire samples.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `measured_Seebeck_uV_per_K`, `Fermi_energy_meV`, `electrical_conductivity_S_per_m`
  - `units`:
    - `sample`: string (undoped or Si-doped)
    - `measured_Seebeck_uV_per_K`: μV/K
    - `Fermi_energy_meV`: meV
    - `electrical_conductivity_S_per_m`: S/m

### callaway_model_results.csv
- path: `/app/outputs/callaway_model_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Lattice thermal conductivities from Callaway model for two effective phonon scattering lengths.
- schema:
  - `type`: table
  - `required_columns`: `thickness_nm`, `lattice_thermal_conductivity_W_per_m_K`
  - `units`:
    - `thickness_nm`: nm
    - `lattice_thermal_conductivity_W_per_m_K`: W/m·K

Notes: The outputs are compared against hidden reference values using appropriate tolerances, per the task's scoring model. The artifacts must contain exactly the specified columns and rows.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "two_band_model_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "measured_Seebeck_uV_per_K",
          "Fermi_energy_meV",
          "electrical_conductivity_S_per_m"
        ],
        "units": {
          "sample": "string (undoped or Si-doped)",
          "measured_Seebeck_uV_per_K": "μV/K",
          "Fermi_energy_meV": "meV",
          "electrical_conductivity_S_per_m": "S/m"
        }
      },
      "description": "Derived Fermi energies and electrical conductivities from the two-band model for the two nanowire samples."
    },
    {
      "file": "callaway_model_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_nm",
          "lattice_thermal_conductivity_W_per_m_K"
        ],
        "units": {
          "thickness_nm": "nm",
          "lattice_thermal_conductivity_W_per_m_K": "W/m·K"
        }
      },
      "description": "Lattice thermal conductivities from Callaway model for two effective phonon scattering lengths."
    }
  ],
  "notes": "The outputs are compared against hidden reference values using appropriate tolerances, per the task's scoring model. The artifacts must contain exactly the specified columns and rows."
}
```

## How you are scored
Each scored CSV file is evaluated independently by a hidden verifier. For each file, the verifier checks that the required columns are present and that the computed numeric values agree with expected results within predefined tolerances. The final score is a weighted combination of these per-file scores, with higher weight on the primary computed quantities (Fermi energies, electrical conductivities, and lattice thermal conductivities). Simply reporting approximate values or matching only the schema is not sufficient; your submitted numeric values must be derived from the specified models and parameters to fall within the acceptable comparison ranges.
