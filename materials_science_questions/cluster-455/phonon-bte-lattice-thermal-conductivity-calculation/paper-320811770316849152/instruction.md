# Phonon BTE lattice thermal conductivity of RhSi and RhSn using DFT and Phono3Py

## Problem background
RhSi and RhSn crystallize in the cubic B20 structure (space group P2₁3) and are isostructural to CoSi. They are candidate materials for thermoelectric applications because a low lattice thermal conductivity is critical for high thermoelectric efficiency. Reliable experimental data on the thermal transport of these compounds are scarce, and first‑principles calculations can provide quantitative predictions of their lattice thermal conductivity. In this task, you will compute the intrinsic lattice thermal conductivity of pure RhSi and RhSn from density functional theory and the phonon Boltzmann transport equation.

## Approach
The thermal conductivity is obtained from first principles. The equilibrium crystal structures (space group P2₁3) are relaxed using density functional theory with the PBEsol functional, which accurately reproduces the experimental lattice parameters of these materials. Harmonic (second‑order) and anharmonic (third‑order) interatomic force constants are computed by finite displacements in supercells. With these force constants, the phonon Boltzmann transport equation is solved within the relaxation‑time approximation, including three‑phonon scattering, on a dense q‑point mesh. The calculation is performed for temperatures from 100 K to 1000 K for both RhSi and RhSn. Only the pure compounds are considered; solid‑solution effects and spectral analysis are outside the scope.

## Reproduction target
You must produce two deliverables:
- A CSV file (`lattice_thermal_conductivity_300K.csv`) containing the lattice thermal conductivity at 300 K for RhSi and RhSn. The file must have columns `Material` and `Kappa_300K` (unit W/(m·K)).
- A CSV file (`temperature_dependence.csv`) containing the temperature‑dependent lattice thermal conductivity from 100 K to 1000 K for both materials. The file must have columns `Temperature_K` (K), `Kappa_RhSi` (W/(m·K)), and `Kappa_RhSn` (W/(m·K)). Rows should cover the temperature range in steps no larger than 100 K.
The computed values should be physically plausible – for example, a monotonic decrease of κ with increasing temperature is expected from phonon physics. The hidden verifier will compare your results to reference values and check the temperature trend, without revealing the exact reference numbers.

## Assets

- QuantumESPRESSO: https://www.quantum-espresso.org/
- Phono3Py: https://phonopy.github.io/phono3py/
- RhSi B20 crystal structure: 10.1107/S0365110X54001342
- RhSn B20 crystal structure: 10.1515/zna-1947-0211

## Workflow steps

### Step 1: DFT geometry optimization for RhSi and RhSn
- Role: process
- Action: Perform DFT relaxation of the B20 unit cell for RhSi and RhSn using the PBEsol functional. Start from experimental lattice parameters and internal coordinates. Converge forces to <10^{-4} eV/Å and energy to <10^{-9} eV/atom. Output relaxed structures.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Second-order force constants and phonon dispersion
- Role: process
- Action: Using finite displacements in a supercell, compute second-order interatomic force constants from DFT forces. Use PhonoPy to extract phonon dispersion and projected density of states.
- Evidence: `/app/outputs/phonon_dispersion.dat`

### Step 3: Third-order force constants
- Role: process
- Action: Compute third-order interatomic force constants via finite displacements in a supercell using DFT forces. Input to Phono3Py.
- Evidence: `/app/outputs/fc3.hdf5`

### Step 4: Run Phono3Py thermal conductivity calculation
- Role: process
- Action: Using Phono3Py, solve the phonon Boltzmann transport equation in the relaxation-time approximation with three-phonon scattering. Use a converged q-point grid. Calculate lattice thermal conductivity for temperatures from 100 K to 1000 K. Output raw thermal conductivity data per material.
- Evidence: `/app/outputs/kappa_raw.json`

### Step 5: 300 K thermal conductivity extraction
- Role: scored
- Action: From the raw thermal conductivity output, extract the lattice thermal conductivity at 300 K for RhSi and RhSn and write as a CSV file.
- Output file: `/app/outputs/lattice_thermal_conductivity_300K.csv`
- Format: csv
- Contract: Columns: Material (string, 'RhSi' or 'RhSn'), Kappa_300K (float, W/(m·K)). Two rows.
- Scoring: scored by hidden verifier

### Step 6: Temperature-dependent thermal conductivity extraction
- Role: scored (load-bearing)
- Action: From the raw thermal conductivity data, extract values at temperatures from 100 K to 1000 K in increments of no more than 100 K for both RhSi and RhSn. Write a CSV file with columns Temperature_K, Kappa_RhSi, Kappa_RhSn.
- Output file: `/app/outputs/temperature_dependence.csv`
- Format: csv
- Contract: Columns: Temperature_K (float), Kappa_RhSi (float, W/(m·K)), Kappa_RhSn (float, W/(m·K)). Rows for temperatures from 100 K to 1000 K, step ≤ 100 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lattice_thermal_conductivity_300K.csv`
- `/app/outputs/temperature_dependence.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lattice_thermal_conductivity_300K.csv
- path: `/app/outputs/lattice_thermal_conductivity_300K.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Room-temperature lattice thermal conductivity of RhSi and RhSn computed with PBEsol.
- schema:
  - `type`: table
  - `required_columns`: `Material`, `Kappa_300K`
  - `units`:
    - `Kappa_300K`: W/(m·K)

### temperature_dependence.csv
- path: `/app/outputs/temperature_dependence.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Temperature-dependent lattice thermal conductivity from 100 K to 1000 K for RhSi and RhSn. Verifier checks monotonic decreasing trend and spot-checks values at specific temperatures against hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `Kappa_RhSi`, `Kappa_RhSn`
  - `units`:
    - `Temperature_K`: K
    - `Kappa_RhSi`: W/(m·K)
    - `Kappa_RhSn`: W/(m·K)

Notes: Solid-solution and spectral/cumulative thermal conductivity analyses are excluded per task scope. Only pure RhSi and RhSn with PBEsol functional are reproduced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lattice_thermal_conductivity_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Material",
          "Kappa_300K"
        ],
        "units": {
          "Kappa_300K": "W/(m·K)"
        }
      },
      "description": "Room-temperature lattice thermal conductivity of RhSi and RhSn computed with PBEsol."
    },
    {
      "file": "temperature_dependence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "Kappa_RhSi",
          "Kappa_RhSn"
        ],
        "units": {
          "Temperature_K": "K",
          "Kappa_RhSi": "W/(m·K)",
          "Kappa_RhSn": "W/(m·K)"
        }
      },
      "description": "Temperature-dependent lattice thermal conductivity from 100 K to 1000 K for RhSi and RhSn. Verifier checks monotonic decreasing trend and spot-checks values at specific temperatures against hidden reference."
    }
  ],
  "notes": "Solid-solution and spectral/cumulative thermal conductivity analyses are excluded per task scope. Only pure RhSi and RhSn with PBEsol functional are reproduced."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that examines the two output files. For `lattice_thermal_conductivity_300K.csv`, the verifier compares your κ values for RhSi and RhSn to pre‑determined reference values with a tolerance that accounts for the reproducibility of the computational workflow. For `temperature_dependence.csv`, the verifier verifies that κ decreases monotonically with temperature for both materials and performs spot‑checks at selected temperatures against expected values. The overall score is a weighted combination of the scores from both artifacts; the temperature dependence file is load‑bearing. Simply printing numbers from the literature without performing the required DFT + BTE calculations will not pass the verification.
