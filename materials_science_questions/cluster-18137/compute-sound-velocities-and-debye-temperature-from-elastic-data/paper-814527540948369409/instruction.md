# Compute Lattice Thermal Conductivity and Branch Contributions of a 2D Material from First Principles

## Problem background
Penta‑graphene is a recently proposed carbon allotrope consisting entirely of pentagons, with three‑fold coordinated (sp²) and four‑fold coordinated (sp³) carbon atoms forming a buckled two‑dimensional sheet. Its unusual geometry gives rise to distinct phonon properties, and understanding heat conduction in penta‑graphene is important for thermal management and thermoelectric applications. The intrinsic lattice thermal conductivity is a key quantity that depends sensitively on the anharmonic interactions among phonons and on the contributions of different vibrational branches.

## Approach
The thermal conductivity is computed by solving the linearized phonon Boltzmann transport equation (BTE) after obtaining the harmonic (second‑order) and anharmonic (third‑order) interatomic force constants from density functional theory (DFT) calculations. The iterative solution of the BTE correctly accounts for both resistive Umklapp scattering and momentum‑conserving Normal scattering; for comparison, the relaxation‑time approximation (RTA) is also evaluated at the same temperatures. The workflow uses an open‑source DFT code to compute the force constants on supercells of the penta‑graphene primitive cell, then processes them with the ShengBTE package to run the iterative and RTA BTE solvers. From the resulting spectra the total lattice thermal conductivity as a function of temperature (300–700 K) is extracted, together with the fractional contribution of each phonon branch (ZA, TA, LA, optical) at 300 K.

## Reproduction target
Produce two artefacts that together characterise thermal transport in penta‑graphene: (1) a temperature‑dependent lattice thermal conductivity table with both iterative (K_lat) and RTA (K_RTA) values at 300, 400, 500, 600, and 700 K, and (2) the percentage contribution of each phonon branch (ZA, TA, LA, optical) to the total iterative K_lat at 300 K. From the temperature series, the power‑law exponent α of the relation K_lat ∝ 1/T^α will be derived by fitting. The calculations must be performed with an open‑source DFT engine and the publicly available ShengBTE package, using the known crystal structure of pristine penta‑graphene (space group P‑421m, lattice constant a=b=3.64 Å, six atoms per unit cell).

## Assets

- ShengBTE: https://www.shengbte.org/
- Open-source DFT code (e.g., Quantum ESPRESSO): https://www.quantum-espresso.org/
- Penta‑graphene crystal structure

## Workflow steps

### Step 1: Compute harmonic interatomic force constants
- Role: process
- Action: Using an open-source DFT code, perform total energy and force calculations on the primitive cell and an 8×8×1 supercell of penta‑graphene. Extract harmonic interatomic force constants (second‑order IFCs).
- Evidence: `/app/outputs/harmonic_ifc.dat`

### Step 2: Compute third‑order anharmonic interatomic force constants
- Role: process
- Action: Build a 5×5×1 supercell of penta‑graphene. Perform DFT finite‑displacement calculations and use the thirdorder.py tool (from ShengBTE) to extract third‑order anharmonic IFCs.
- Evidence: `/app/outputs/anharmonic_ifc.dat`

### Step 3: Calculate lattice thermal conductivity vs temperature
- Role: scored (load-bearing)
- Action: Set up ShengBTE input using the harmonic and anharmonic IFCs, including natural isotopic disorder (¹²C 98.9%, ¹³C 1.1%). Run the iterative BTE solver and the relaxation‑time approximation (RTA) solver for temperatures 300, 400, 500, 600, 700 K. Extract the iterative K_lat and RTA K_RTA values.
- Output file: `/app/outputs/thermal_conductivity_vs_temperature.csv`
- Format: csv
- Contract: Columns: Temperature_K (float), K_lat_W_mK (float), K_RTA_W_mK (float). At least 5 temperature points from 300 K to 700 K.
- Scoring: scored by hidden verifier

### Step 4: Determine branch contributions to K_lat at 300 K
- Role: scored
- Action: From the mode‑resolved thermal conductivity output of the ShengBTE iterative run at 300 K, sum the contributions by phonon branch (ZA, TA, LA, optical) and express each as a percentage of the total K_lat.
- Output file: `/app/outputs/mode_contributions_at_300K.csv`
- Format: csv
- Contract: Columns: phonon_branch (string, one of 'ZA','TA','LA','optical'), contribution_percentage (float). The contributions must sum to 100.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermal_conductivity_vs_temperature.csv`
- `/app/outputs/mode_contributions_at_300K.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermal_conductivity_vs_temperature.csv
- path: `/app/outputs/thermal_conductivity_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-dependent lattice thermal conductivity; the checker recomputes the power‑law exponent from the series, compares K_lat at 300 K to a hidden reference, and verifies that K_RTA is roughly half of K_lat at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `K_lat_W_mK`, `K_RTA_W_mK`
  - `units`:
    - `Temperature_K`: K
    - `K_lat_W_mK`: W/(m·K)
    - `K_RTA_W_mK`: W/(m·K)
  - `description`: Temperature series with iterative and RTA lattice thermal conductivity.

### mode_contributions_at_300K.csv
- path: `/app/outputs/mode_contributions_at_300K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Phonon branch contributions at 300 K; the checker verifies that the ZA contribution is within tolerance of the paper‑reported value.
- schema:
  - `type`: table
  - `required_columns`: `phonon_branch`, `contribution_percentage`
  - `units`:
    - `contribution_percentage`: percent
  - `description`: Phonon branch contributions to K_lat at 300 K.

Notes: The two CSV files are the only scored artifacts. The process steps (harmonic IFCs, anharmonic IFCs) are mandatory to produce the necessary input for ShengBTE but are not directly scored. The checker recomputes the thermal conductivity exponent and ratio, and checks the ZA contribution; all comparisons use tolerances appropriate for DFT‑code differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermal_conductivity_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "K_lat_W_mK",
          "K_RTA_W_mK"
        ],
        "units": {
          "Temperature_K": "K",
          "K_lat_W_mK": "W/(m·K)",
          "K_RTA_W_mK": "W/(m·K)"
        },
        "description": "Temperature series with iterative and RTA lattice thermal conductivity."
      },
      "description": "Temperature-dependent lattice thermal conductivity; the checker recomputes the power‑law exponent from the series, compares K_lat at 300 K to a hidden reference, and verifies that K_RTA is roughly half of K_lat at 300 K."
    },
    {
      "file": "mode_contributions_at_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "phonon_branch",
          "contribution_percentage"
        ],
        "units": {
          "contribution_percentage": "percent"
        },
        "description": "Phonon branch contributions to K_lat at 300 K."
      },
      "description": "Phonon branch contributions at 300 K; the checker verifies that the ZA contribution is within tolerance of the paper‑reported value."
    }
  ],
  "notes": "The two CSV files are the only scored artifacts. The process steps (harmonic IFCs, anharmonic IFCs) are mandatory to produce the necessary input for ShengBTE but are not directly scored. The checker recomputes the thermal conductivity exponent and ratio, and checks the ZA contribution; all comparisons use tolerances appropriate for DFT‑code differences."
}
```

## How you are scored
A hidden verifier checks the output files independently. From `thermal_conductivity_vs_temperature.csv` it reads the temperature series, recomputes the power‑law exponent α by log‑log linear regression, and compares the computed K_lat at 300 K and the K_RTA/K_lat ratio to reference values. From `mode_contributions_at_300K.csv` it reads the branch contributions and verifies the ZA percentage against a reference. Each stage’s score is combined into a final reward in [0,1]; simply copying numbers from the paper does not pass, because the verifier judges the physical consistency of the self‑consistent computation.
