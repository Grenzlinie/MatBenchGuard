# First-principles thermodynamic properties of bcc W

## Problem background
Tungsten (W) is a body-centred cubic (bcc) refractory metal with exceptional mechanical strength and chemical resistance, widely used in aerospace and electronics. Under extreme conditions its thermodynamic properties are crucial for constructing high-pressure calibrations and for understanding material response. First-principles calculations can provide accurate thermal equations of state and property predictions when experiments are difficult. Reproducing the zero-pressure elastic constants and temperature-dependent thermodynamic properties of bcc W using density functional theory and the quasiharmonic approximation is a benchmark for such calculations.

## Approach
Use density functional theory (DFT) with the PBE exchange-correlation functional and an ultrasoft pseudopotential to compute the static total energy of bcc W as a function of volume. Fit the energy-volume data to an equation of state to obtain the equilibrium volume and zero-pressure bulk modulus. Determine the three independent elastic constants (C11, C12, C44) from total-energy calculations on volume-conserving strained unit cells. Perform density functional perturbation theory (DFPT) phonon calculations at several volumes to obtain the phonon dispersion. Within the quasiharmonic approximation (QHA), combine the static energies with the phonon free energy (zero-point and thermal) to construct the Helmholtz free energy F(V,T). From F(V,T) derive the thermal equation of state and then the zero-pressure thermodynamic properties: isothermal bulk modulus, adiabatic bulk modulus, thermal expansion coefficient, specific heat at constant volume, and entropy, as functions of temperature. Compare the computed properties with known experimental trends: C_V should approach the Dulong–Petit limit at high temperature and entropy should increase with temperature.

## Reproduction target
Produce a set of zero-pressure elastic constants (C11, C12, C44, and the bulk modulus B) for bcc tungsten. Produce a table of zero-pressure thermodynamic properties — specific heat at constant volume C_V, entropy S, thermal expansion coefficient α, and adiabatic bulk modulus B_S — at a range of temperatures from 0 to 3000 K (e.g., at 500 K intervals). The computed C_V should be monotonically increasing with temperature and approach the classical Dulong–Petit limit (3R ≈ 24.94 J/mol·K) at the highest temperatures. The entropy should increase with temperature.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- W ultrasoft pseudopotential (PBE): https://pseudopotentials.quantum-espresso.org/upf_files/W.pbe-spn-rrkjus_psl.1.0.0.UPF

## Workflow steps

### Step 1: Static total-energy calculations
- Role: process
- Action: Perform DFT static total-energy calculations for bcc W at a series of volumes (about 7–19 Å³/atom) using the PBE ultrasoft pseudopotential with adequate convergence parameters. Save the resulting energy–volume (E,V) data points.
- Evidence: `/app/outputs/e_v_data.json`

### Step 2: Fit static equation of state
- Role: process
- Action: Fit the static E–V data to a fourth-order finite-strain equation of state to obtain the equilibrium volume V0, zero-pressure bulk modulus B0, and its pressure derivative B'.
- Evidence: `/app/outputs/eos_fit_results.json`

### Step 3: Elastic constants at zero pressure
- Role: scored
- Action: At the equilibrium volume, apply volume-conserving strain matrices to the bcc W unit cell and perform DFT total-energy calculations to extract C11, C12, and C44 from the strain–energy curves. Compute the bulk modulus B = (C11+2C12)/3. Save to elastic_constants.csv.
- Output file: `/app/outputs/elastic_constants.csv`
- Format: csv
- Contract: columns: C11_GPa, C12_GPa, C44_GPa, B_GPa
- Scoring: scored by hidden verifier

### Step 4: DFPT phonon calculations
- Role: process
- Action: For at least five volumes spanning the equilibrium volume, perform DFPT phonon calculations on an appropriate q‑grid to obtain phonon frequencies ω_j(q,V). Save the frequency data for subsequent free-energy construction.
- Evidence: `/app/outputs/phonon_frequencies.npz`

### Step 5: Quasi-harmonic free energy
- Role: process
- Action: Combine the static energies E_static(V) with the phonon free energy (zero-point and thermal contributions) to compute the Helmholtz free energy F(V,T) on a grid of temperatures from 0 to 3000 K for the set of volumes.
- Evidence: `/app/outputs/free_energy_table.csv`

### Step 6: Thermodynamic properties at zero pressure
- Role: scored (load-bearing)
- Action: From F(V,T), derive the isothermal bulk modulus, thermal expansion coefficient, adiabatic bulk modulus, specific heat at constant volume, and entropy at zero pressure for temperatures 0–3000 K (at 500 K intervals, or finer). Save to thermodynamic_properties.csv.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: columns: temperature_K, pressure_GPa, Cv_J_mol_K, S_J_mol_K, alpha_per_K, Bs_GPa
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.csv`
- `/app/outputs/thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.csv
- path: `/app/outputs/elastic_constants.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zero-pressure elastic constants of bcc W: C11, C12, C44, and bulk modulus B.
- schema:
  - `type`: table
  - `required_columns`: `C11_GPa`, `C12_GPa`, `C44_GPa`, `B_GPa`
  - `units`:
    - `C11_GPa`: GPa
    - `C12_GPa`: GPa
    - `C44_GPa`: GPa
    - `B_GPa`: GPa

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Zero-pressure thermodynamic properties: specific heat C_V, entropy S, thermal expansion coefficient α, and adiabatic bulk modulus B_S as functions of temperature from 0 to 3000 K.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `pressure_GPa`, `Cv_J_mol_K`, `S_J_mol_K`, `alpha_per_K`, `Bs_GPa`
  - `units`:
    - `temperature_K`: K
    - `pressure_GPa`: GPa
    - `Cv_J_mol_K`: J/mol·K
    - `S_J_mol_K`: J/mol·K
    - `alpha_per_K`: 1/K
    - `Bs_GPa`: GPa

Notes: Only zero-pressure elastic constants and thermodynamic properties are scored; high-pressure and phonon dispersion are not required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "C11_GPa",
          "C12_GPa",
          "C44_GPa",
          "B_GPa"
        ],
        "units": {
          "C11_GPa": "GPa",
          "C12_GPa": "GPa",
          "C44_GPa": "GPa",
          "B_GPa": "GPa"
        }
      },
      "description": "Zero-pressure elastic constants of bcc W: C11, C12, C44, and bulk modulus B."
    },
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "pressure_GPa",
          "Cv_J_mol_K",
          "S_J_mol_K",
          "alpha_per_K",
          "Bs_GPa"
        ],
        "units": {
          "temperature_K": "K",
          "pressure_GPa": "GPa",
          "Cv_J_mol_K": "J/mol·K",
          "S_J_mol_K": "J/mol·K",
          "alpha_per_K": "1/K",
          "Bs_GPa": "GPa"
        }
      },
      "description": "Zero-pressure thermodynamic properties: specific heat C_V, entropy S, thermal expansion coefficient α, and adiabatic bulk modulus B_S as functions of temperature from 0 to 3000 K."
    }
  ],
  "notes": "Only zero-pressure elastic constants and thermodynamic properties are scored; high-pressure and phonon dispersion are not required."
}
```

## How you are scored
A hidden verifier reads your output files. The elastic constants in elastic_constants.csv are compared to reference values within tolerances that account for legitimate method spread. The thermodynamic_properties.csv values are compared to reference thermodynamic data at each temperature, and structural trends are checked (monotonicity, asymptotic behaviour). The two scored outputs are weighted: elastic constants carry 20% of the total reward, thermodynamic absolute values carry 60%, and trend checks carry 20%. The intermediate process steps (static E(V), EOS fit, phonon calculations, free energy table) are required to reach the scored outputs but are not directly rewarded. Reporting a number that matches a reference is not enough if the underlying calculations were not performed; the verifier's checks require the correct physical trends that can only arise from a faithful execution of the workflow.
