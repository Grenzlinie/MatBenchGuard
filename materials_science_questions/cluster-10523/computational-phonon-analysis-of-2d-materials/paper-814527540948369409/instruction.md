# Intrinsic Lattice Thermal Conductivity of Penta-Graphene via First-Principles Phonon Boltzmann Transport

## Problem background
Penta-graphene is a quasi-two-dimensional carbon allotrope composed entirely of pentagonal rings, with a mixture of sp² and sp³ hybridized carbon atoms. Its buckled structure gives it distinct electronic and mechanical properties. An important property for thermal management and thermoelectric applications is the lattice thermal conductivity (K_lat), which is determined by phonon transport. Understanding how the unique bonding topology of penta-graphene influences its intrinsic K_lat—and how that compares to graphene—is an open question. This task requires you to compute the intrinsic lattice thermal conductivity of penta-graphene from first principles and analyze its phonon transport characteristics.

## Approach
A first-principles approach is used combining density functional theory (DFT) and the linearized phonon Boltzmann transport equation (BTE).

1. **DFT relaxation and harmonic force constants**: Relax the penta-graphene unit cell using the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional, then compute harmonic interatomic force constants via density functional perturbation theory (DFPT). This yields phonon frequencies, group velocities, and eigenvectors.
2. **Anharmonic (third-order) force constants**: Obtain from finite-displacement calculations.
3. **Phonon BTE solution**: Feed the harmonic and anharmonic force constants into a solver that iteratively solves the linearized phonon BTE, including natural isotopic disorder. This produces lattice thermal conductivity as a function of temperature from both the exact iterative solution and the single-mode relaxation time approximation (RTA). Comparison between iterative and RTA results reveals the role of Normal scattering processes.
4. **Post-processing**: Extract the thermal conductivity at selected temperatures, fit its temperature dependence to a power law, and compute the fractional contributions of individual phonon branches (ZA, TA, LA, optical) to the total conductivity.

## Reproduction target
Produce the following outputs based on the computational workflow:

- **thermal_conductivity.csv**: Columns `T_K`, `K_lat_iterative_W_mK`, `K_lat_RTA_W_mK`, with rows for 300 K, 500 K, and 700 K. The iterative and RTA lattice thermal conductivities must be in W/(m·K).
- **temperature_exponent.txt**: A single floating-point number representing the exponent α in the power law K_lat ∝ 1/T^α fitted from the iterative K_lat vs. T data.
- **modal_contributions.csv**: Columns `branch` and `contribution_ratio`, with rows for `ZA`, `TA`, `LA`, and `OP` (optical branches). The contribution_ratio is the fraction of total iterative K_lat at 300 K carried by that branch; the four values should sum to approximately 1.0.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- ShengBTE: https://www.shengbte.org/
- Penta-graphene crystal structure parameters: 10.1073/pnas.1416591112

## Workflow steps

### Step 1: DFT relaxation and harmonic force constants
- Role: process
- Action: Perform DFT relaxation of the penta-graphene unit cell and compute harmonic interatomic force constants using density functional perturbation theory (DFPT) as implemented in Quantum ESPRESSO. Use the Perdew-Burke-Ernzerhof (PBE) exchange-correlation functional.
- Evidence: `/app/outputs/harmonic_ifcs.fc`

### Step 2: Anharmonic (third-order) force constants
- Role: process
- Action: Compute third-order anharmonic interatomic force constants for penta-graphene using Quantum ESPRESSO with a finite-difference method. Include interactions up to at least the 14th nearest neighbours (cutoff radius ~6.5 Å). Prepare the force constants file required by ShengBTE.
- Evidence: `/app/outputs/FORCE_CONSTANTS_3RD`

### Step 3: ShengBTE transport calculation
- Role: process
- Action: Run ShengBTE using the harmonic and anharmonic force constants, include natural isotopic disorder (¹²C 98.9%, ¹³C 1.1%), and solve the linearized phonon Boltzmann transport equation iteratively. Compute the lattice thermal conductivity and the phonon branch contributions for a temperature range covering at least 300–1000 K.
- Evidence: `/app/outputs/T300K.dat`

### Step 4: Extract thermal conductivity at selected temperatures
- Role: scored (load-bearing)
- Action: From the ShengBTE output, create a CSV file containing the iterative and RTA lattice thermal conductivities at 300 K, 500 K, and 700 K.
- Output file: `/app/outputs/thermal_conductivity.csv`
- Format: csv
- Contract: Columns: T_K, K_lat_iterative_W_mK, K_lat_RTA_W_mK.
- Scoring: scored by hidden verifier

### Step 5: Fit temperature exponent of lattice thermal conductivity
- Role: scored
- Action: Fit the iterative lattice thermal conductivity vs. temperature data to the relation K_lat ∝ 1/T^α and write the fitted exponent α as a single floating-point number.
- Output file: `/app/outputs/temperature_exponent.txt`
- Format: txt
- Contract: Plain text file with one floating-point number.
- Scoring: scored by hidden verifier

### Step 6: Extract modal contributions to lattice thermal conductivity
- Role: scored
- Action: Compute the fractional contribution of each phonon branch (ZA, TA, LA, optical) to the total iterative lattice thermal conductivity at 300 K from the ShengBTE output, and write the results to a CSV file.
- Output file: `/app/outputs/modal_contributions.csv`
- Format: csv
- Contract: Columns: branch, contribution_ratio.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity.csv`
- `/app/outputs/temperature_exponent.txt`
- `/app/outputs/modal_contributions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity.csv
- path: `/app/outputs/thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Lattice thermal conductivity at three temperatures (300, 500, 700 K) from the exact iterative BTE solution and the relaxation-time approximation.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `K_lat_iterative_W_mK`, `K_lat_RTA_W_mK`
  - `units`:
    - `T_K`: Kelvin
    - `K_lat_iterative_W_mK`: W/(m·K)
    - `K_lat_RTA_W_mK`: W/(m·K)

### temperature_exponent.txt
- path: `/app/outputs/temperature_exponent.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Fitted exponent α in the temperature dependence K_lat ∝ 1/T^α.
- schema:
  - `type`: text
  - `required`: object
  - `items`: object

### modal_contributions.csv
- path: `/app/outputs/modal_contributions.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Fractional contribution of the ZA, TA, LA, and optical branches to the total iterative lattice thermal conductivity at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `branch`, `contribution_ratio`
  - `units`:
    - `contribution_ratio`: dimensionless

Notes: All scored outputs are compared against the paper's reported values with generous tolerances to account for the substitution of VASP with Quantum ESPRESSO and differences in computational setup. The thermal conductivity CSV must contain the three required rows; the exponent text file must contain a single floating-point number; the modal contributions CSV must list the four branches with ratios that sum to approximately 1.0.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "K_lat_iterative_W_mK",
          "K_lat_RTA_W_mK"
        ],
        "units": {
          "T_K": "Kelvin",
          "K_lat_iterative_W_mK": "W/(m·K)",
          "K_lat_RTA_W_mK": "W/(m·K)"
        }
      },
      "description": "Lattice thermal conductivity at three temperatures (300, 500, 700 K) from the exact iterative BTE solution and the relaxation-time approximation."
    },
    {
      "file": "temperature_exponent.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required": {},
        "items": {}
      },
      "description": "Fitted exponent α in the temperature dependence K_lat ∝ 1/T^α."
    },
    {
      "file": "modal_contributions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "branch",
          "contribution_ratio"
        ],
        "units": {
          "contribution_ratio": "dimensionless"
        }
      },
      "description": "Fractional contribution of the ZA, TA, LA, and optical branches to the total iterative lattice thermal conductivity at 300 K."
    }
  ],
  "notes": "All scored outputs are compared against the paper's reported values with generous tolerances to account for the substitution of VASP with Quantum ESPRESSO and differences in computational setup. The thermal conductivity CSV must contain the three required rows; the exponent text file must contain a single floating-point number; the modal contributions CSV must list the four branches with ratios that sum to approximately 1.0."
}
```

## How you are scored
A hidden verifier will read your output artifacts and compare them against reference criteria derived from the original study. The verifier checks:

- **thermal_conductivity.csv** contains the three required rows, the thermal conductivity at 300 K is within a generous tolerance of the reference, and K_lat decreases with increasing temperature.
- **temperature_exponent.txt** contains a valid floating-point number that matches the expected exponent within a tolerance.
- **modal_contributions.csv** contains the four branches (ZA, TA, LA, OP) with contribution ratios summing to ~1.0; each branch fraction is compared to the reference within a tolerance.

The verifier converts each check into a partial score and combines them by weight to produce the final reward. Simply reporting numbers without running the workflow will not satisfy structural checks (e.g., the temperature trend). No further details about the specific tolerance or reference values are provided; your job is to faithfully execute the computational procedure to obtain physically accurate results.
