# Thermodynamic Properties of MgO from First-Principles and Classical Simulations

## Problem background
Magnesium oxide (MgO) is a fundamental oxide that serves as a standard for high-pressure experiments and is a major component of the Earth's lower mantle. Its thermodynamic properties — isothermal bulk modulus, its pressure derivatives, and volume thermal expansion coefficient — over wide ranges of pressure (0–200 GPa) and temperature (up to 3000 K) are essential for constructing accurate equations of state and interpreting seismic and experimental data. These quantities must be computed reliably at extreme conditions where experimental measurements are scarce.

## Approach
The thermodynamic properties are obtained by two independent routes. The first employs density functional theory (DFT) with the PBEsol exchange-correlation functional and Vanderbilt ultrasoft pseudopotentials to compute the static energy versus volume, E(V), of the rock-salt (B1) phase of MgO. This E(V) curve is then input to a quasi-harmonic Debye (QHD) model, which yields the isothermal bulk modulus K, its first and second pressure derivatives K' and K'', and the volume thermal expansion coefficient α as continuous functions of pressure and temperature.

The second route uses classical molecular dynamics (MD) simulations in the isothermal–isobaric (NPT) ensemble with two interatomic potential models: the shell model (SM) of Lewis & Catlow (1985) and the breathing shell model (BSM) of Catlow et al. (1979). Simulations are run on a 1000-ion supercell initially in the rock-salt structure. From the time-averaged volumes, the isothermal bulk modulus and thermal expansion coefficient are extracted. All results are combined into a single CSV file for scoring. The approach does not require any proprietary data; the crystal structure, pseudopotentials, and interatomic potential parameters are all publicly available.

## Reproduction target
Produce a CSV file (`thermodynamic_properties.csv`) that reports the isothermal bulk modulus K (GPa), its first pressure derivative K' (dimensionless), its second pressure derivative K'' (GPa⁻¹), and the volume thermal expansion coefficient α (10⁻⁶ K⁻¹) of MgO, computed by three methods: QHD, shell-model MD (SM-MD), and breathing-shell-model MD (BSM-MD). The file must cover:
- Pressure range 0–200 GPa at a fixed temperature of 300 K (approximately every 10 GPa for QHD, every 20 GPa for MD).
- Temperature range 0–3000 K at a fixed pressure of 0.1 MPa (approximately every 200 K).
Each row contains the method identifier, temperature (K), pressure (GPa), and the computed quantities; leave a cell empty when a quantity is not computed by that method. For example, MD results may omit K' and K''. The hidden verifier will compare the reported values to reference data and assess the low-temperature T³ scaling behaviour of α from the QHD method.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Gibbs2 (quasi-harmonic Debye model program): https://github.com/ttgump/Gibbs2
- LAMMPS: https://lammps.sandia.gov/
- Shell-model potential parameters for MgO (Lewis & Catlow 1985): 10.1088/0022-3719/18/6/020
- Breathing shell-model potential parameters for MgO (Catlow et al. 1979): 10.1088/0022-3719/12/3/020
- MgO rock-salt crystal structure
- Vanderbilt ultrasoft pseudopotentials for Mg and O (PBEsol): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: DFT static energy-volume calculation
- Role: process
- Action: Using an open-source plane-wave DFT code with the PBEsol functional and Vanderbilt ultrasoft pseudopotentials, compute the total energy of MgO in the B1 (rock-salt) phase as a function of unit cell volume for a range of volumes around the equilibrium value. Write the resulting energy-volume data table.
- Evidence: `/app/outputs/ev_data.csv`

### Step 2: Quasi-harmonic Debye model application
- Role: process
- Action: Apply the quasi-harmonic Debye model to the E(V) data from step_01. Compute the isothermal bulk modulus K, its first pressure derivative K', second pressure derivative K'', and the volume thermal expansion coefficient α at pressures 0–200 GPa (approx. every 10 GPa) at T=300 K, and at temperatures 0–3000 K (approx. every 200 K) at P=0.1 MPa. Save the results.
- Evidence: `/app/outputs/qhd_properties.csv`

### Step 3: NPT MD simulation with shell-model potential
- Role: process
- Action: Using a classical MD code, run constant-NPT simulations for MgO with the shell-model (SM) potential parameters (Lewis & Catlow 1985). Use a 1000-ion supercell initially in the rock-salt structure. Equilibrate and collect time-averaged molar volumes at pressures 0–200 GPa (approx. every 20 GPa) at 300 K, and at temperatures 0–3000 K (approx. every 200 K) at 0.1 MPa. From the molar volume data, numerically compute the isothermal bulk modulus and thermal expansion coefficient. Save the extracted properties.
- Evidence: `/app/outputs/sm_properties.csv`

### Step 4: NPT MD simulation with breathing shell-model potential
- Role: process
- Action: Repeat the MD simulation and property extraction as in step_03 but using the breathing shell-model (BSM) potential parameters (Catlow et al. 1979). Save the extracted thermodynamic properties.
- Evidence: `/app/outputs/bsm_properties.csv`

### Step 5: Final thermodynamic properties compilation
- Role: scored (load-bearing)
- Action: Combine all computed quantities from the QHD model and both MD simulations into a single CSV file. For each method and each (P,T) condition specified in the preceding steps, write one row with columns: method, temperature_K, pressure_GPa, bulk_modulus_K_GPa, K_prime, K_double_prime, thermal_expansivity_alpha_1e6_K. For quantities not computed by a particular method, leave the cell empty.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: CSV with columns: method (string: QHD, SM-MD, BSM-MD), temperature_K (float), pressure_GPa (float), bulk_modulus_K_GPa (float, optional), K_prime (float, dimensionless, optional), K_double_prime (float, GPa^-1, optional), thermal_expansivity_alpha_1e6_K (float, 10^-6 K^-1, optional). Rows cover pressures 0–200 GPa (approx every 10 GPa for QHD, every 20 GPa for MD) at 300 K, and temperatures 0–3000 K (approx every 200 K) at 0.1 MPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Compiled thermodynamic properties (isothermal bulk modulus K, pressure derivatives K' and K'', thermal expansion coefficient α) of MgO computed via QHD, SM-MD, and BSM-MD. The checker compares each value against hidden paper-derived reference values and validates the expected low-temperature T^3 scaling of α.
- schema:
  - `type`: table
  - `required_columns`: `method`, `temperature_K`, `pressure_GPa`, `bulk_modulus_K_GPa`, `K_prime`, `K_double_prime`, `thermal_expansivity_alpha_1e6_K`
  - `units`:
    - `bulk_modulus_K_GPa`: GPa
    - `K_prime`: dimensionless
    - `K_double_prime`: GPa^-1
    - `thermal_expansivity_alpha_1e6_K`: 10^-6 K^-1

Notes: The checker performs a reference-match comparison on the reported values and a structural audit on the low-temperature thermal expansion data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "temperature_K",
          "pressure_GPa",
          "bulk_modulus_K_GPa",
          "K_prime",
          "K_double_prime",
          "thermal_expansivity_alpha_1e6_K"
        ],
        "units": {
          "bulk_modulus_K_GPa": "GPa",
          "K_prime": "dimensionless",
          "K_double_prime": "GPa^-1",
          "thermal_expansivity_alpha_1e6_K": "10^-6 K^-1"
        }
      },
      "description": "Compiled thermodynamic properties (isothermal bulk modulus K, pressure derivatives K' and K'', thermal expansion coefficient α) of MgO computed via QHD, SM-MD, and BSM-MD. The checker compares each value against hidden paper-derived reference values and validates the expected low-temperature T^3 scaling of α."
    }
  ],
  "notes": "The checker performs a reference-match comparison on the reported values and a structural audit on the low-temperature thermal expansion data."
}
```

## How you are scored
A hidden verifier reads the submitted `thermodynamic_properties.csv` and scores it independently. For each row, the verifier compares the reported value for each property against reference values (derived from publicly reported thermodynamic quantities) using per-property tolerances. Additionally, for the QHD data at temperatures below 500 K, the verifier fits log(α) versus log(T) and checks that the slope is close to 3.0, verifying the expected T³ low-temperature behaviour. The final score (0 to 1) is a weighted combination of the fraction of data points that pass the tolerance checks and the structural check on the low-T slope. The scoring does not depend on matching a specific published table or figure, and it is designed so that a correct, honest computation (even with different software or minor numerical choices) can achieve full credit.
