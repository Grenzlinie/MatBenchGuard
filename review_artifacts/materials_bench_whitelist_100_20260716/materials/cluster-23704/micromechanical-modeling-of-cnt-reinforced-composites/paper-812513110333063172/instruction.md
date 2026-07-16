# FEM-Based Vibration Analysis of CNT-Reinforced Stiffened Plates

## Problem background
This task investigates the free vibration behavior of carbon nanotube-reinforced composite (CNTRC) stiffened plates under thermal environments. The plates consist of a polymer matrix reinforced with single-walled carbon nanotubes (SWCNTs) distributed through the thickness in four patterns: uniform (UD), functionally graded X-type (FG‑X), O‑type (FG‑O), and V‑type (FG‑V). Stiffeners are attached eccentrically to one face to improve stiffness-to-weight performance. The geometry is modeled using a finite element approach based on first‑order shear deformation theory (FSDT), employing eight‑noded isoparametric plate bending elements and three‑noded beam elements for the stiffeners. A constraint method ties the stiffener nodal degrees of freedom to those of the plate, avoiding an increase in global degrees of freedom. The effective temperature‑dependent properties of the CNTRC are obtained via the rule of mixtures and CNT efficiency parameters. The primary quantity of interest is the natural frequency (non‑dimensional or in Hz), and the goal is to compute how it varies with stiffener configuration, CNT distribution, volume fraction, temperature, and boundary conditions.

## Approach
The workflow builds a custom finite element solver from scratch. The plate is discretized by eight‑noded isoparametric elements, each with five degrees of freedom per node (three translations and two rotations). Stiffeners are modeled as three‑noded beam elements with four degrees of freedom per node; their nodal displacements are expressed in terms of the plate’s DOFs using a transformation matrix that accounts for the eccentricity between stiffener and plate mid‑plane. Element stiffness, mass, and thermal geometric stiffness matrices are assembled for plate and stiffeners, then combined into global matrices. The effective material properties of the CNTRC are computed via the rule of mixtures for each layer, using temperature‑dependent matrix and CNT properties and the prescribed CNT efficiency parameters corresponding to the CNT volume fraction. The thermal geometric stiffness arises from in‑plane thermal stresses due to a uniform temperature change. The natural frequencies are obtained by solving the generalized eigenvalue problem. The solver is exercised for validation cases (pure plate and stiffened plate) and then for parametric sweeps covering boundary conditions, stiffener counts, temperatures, and CNT volume fractions, producing numerical frequency values as specified in the workflow steps.

## Reproduction target
Implement the FEM solver described above and produce the following six scored CSV files:

1.  Non‑dimensional fundamental frequencies (ω = ωₙ a²/h √(ρₘ/Eₘ)) of a simply supported square CNTRC plate without stiffeners, for all four CNT distributions at three temperatures (300 K, 500 K, 700 K).
2.  Natural frequencies in Hz of a simply supported cross‑ply anti‑symmetric stiffened plate, for three mesh densities (6 × 6, 8 × 8, 10 × 10).
3.  Non‑dimensional fundamental frequency of CNTRC stiffened plates with SSSS boundaries as a function of the number of stiffeners (nₓ, nᵧ pairs) for each CNT distribution.
4.  Same as (3) but with CCCC boundaries.
5.  Natural frequency in Hz of CNTRC stiffened plates with SSSS boundaries for combinations of temperature (300 K, 500 K, 700 K) and CNT volume fraction (0.12, 0.17, 0.28) for all distributions.
6.  Same as (5) but with CCCC boundaries.

Exact geometric parameters, material constants, and efficiency parameters are given in the workflow steps. The output CSVs must adhere strictly to the column schemas listed in the steps.

## Assets

- Python 3: https://www.python.org/downloads/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: FEM solver implementation
- Role: process
- Action: Implement the complete FEM solver: compute effective material properties using rule of mixtures for given temperature, CNT distribution and volume fraction; assemble global stiffness, mass, and thermal geometric stiffness matrices using an 8-node plate element and a 3-node beam element with constraint tying; solve the generalized eigenvalue problem to obtain natural frequencies. The solver must be general enough to handle all geometries, boundary conditions, and material parameters required by the subsequent scored steps.
- Evidence: `/app/outputs/solver_implementation_log.txt`

### Step 2: Validation: CNTRC plate frequencies (Table 1)
- Role: scored (load-bearing)
- Action: Run the FEM solver for a simply supported square CNTRC plate without stiffeners using parameters: V_CNT=0.12, a/b=1, b/h=10, CNT efficiency parameters eta1=0.137, eta2=1.002, eta3=0.715. Compute the first three non-dimensional natural frequencies (omega = omega_n*(a^2/h)*sqrt(rho_m/E_m)) for the four CNT distributions (UD, FG-X, FG-O, FG-V) at temperatures 300K, 500K, 700K. Save results to a CSV file.
- Output file: `/app/outputs/step_01_validation_table1.csv`
- Format: csv
- Contract: Temperature(int), Distribution(string:UD|FG-X|FG-O|FG-V), Mode(int), Frequency(float)
- Scoring: scored by hidden verifier

### Step 3: Validation: Stiffened plate frequencies (Table 2)
- Role: scored
- Action: Run the FEM solver for a simply supported cross-ply anti-symmetric stiffened plate with dimensions: a=b=254 mm, h=12.7 mm, b_st=6.35 mm, d_st=25.4 mm, n_x=1, n_y=1. Compute the first four natural frequencies (Hz) at mesh sizes 6x6, 8x8, 10x10. Save results to a CSV file.
- Output file: `/app/outputs/step_02_validation_table2.csv`
- Format: csv
- Contract: Mode(int), Mesh(string:6x6|8x8|10x10), Frequency(float)
- Scoring: scored by hidden verifier

### Step 4: Parametric: Stiffener addition effect for SSSS (Table 3 SSSS)
- Role: scored
- Action: Run the FEM solver for CNTRC stiffened plates with SSSS boundary conditions, parameters a/b=1, a/h=100, b_st=h, d_st=2h, T=300K, V_CNT=0.12. For each stiffener configuration (n_x=0,n_y=0; n_x=1,n_y=0; n_x=0,n_y=1; n_x=1,n_y=1; n_x=2,n_y=2; n_x=3,n_y=3; n_x=4,n_y=4) and each CNT distribution (UD, FG-X, FG-O, FG-V), compute the non-dimensional fundamental frequency and save to a CSV file.
- Output file: `/app/outputs/step_03_ssss_stiffeners.csv`
- Format: csv
- Contract: BC(string:SSSS), nx_ny(string), Distribution(string:UD|FG-X|FG-O|FG-V), Frequency(float)
- Scoring: scored by hidden verifier

### Step 5: Parametric: Stiffener addition effect for CCCC (Table 3 CCCC)
- Role: scored
- Action: Run the FEM solver with CCCC boundary conditions using the same parameters and stiffener configurations as step s3. Compute the non-dimensional fundamental frequency for each case and save to a CSV file.
- Output file: `/app/outputs/step_04_cccc_stiffeners.csv`
- Format: csv
- Contract: BC(string:CCCC), nx_ny(string), Distribution(string:UD|FG-X|FG-O|FG-V), Frequency(float)
- Scoring: scored by hidden verifier

### Step 6: Parametric: Temperature and volume fraction effect for SSSS (Table 4)
- Role: scored
- Action: Run the FEM solver for CNTRC stiffened SSSS plates with a/b=1, a/h=10, n_x=1, n_y=1, b_st=h, d_st=0.25h. For each temperature (300K, 500K, 700K), each V_CNT (0.12, 0.17, 0.28), and each CNT distribution, compute the fundamental natural frequency (Hz) and save to a CSV file.
- Output file: `/app/outputs/step_05_temperature_ssss.csv`
- Format: csv
- Contract: BC(string:SSSS), Temperature(int), V_CNT(float), Distribution(string:UD|FG-X|FG-O|FG-V), Frequency(float)
- Scoring: scored by hidden verifier

### Step 7: Parametric: Temperature and volume fraction effect for CCCC (Table 5)
- Role: scored
- Action: Run the FEM solver with CCCC boundary conditions using the same plate geometry and parameter combinations as step s5. Compute the fundamental natural frequency (Hz) for each case and save to a CSV file.
- Output file: `/app/outputs/step_06_temperature_cccc.csv`
- Format: csv
- Contract: BC(string:CCCC), Temperature(int), V_CNT(float), Distribution(string:UD|FG-X|FG-O|FG-V), Frequency(float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_validation_table1.csv`
- `/app/outputs/step_02_validation_table2.csv`
- `/app/outputs/step_03_ssss_stiffeners.csv`
- `/app/outputs/step_04_cccc_stiffeners.csv`
- `/app/outputs/step_05_temperature_ssss.csv`
- `/app/outputs/step_06_temperature_cccc.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_validation_table1.csv
- path: `/app/outputs/step_01_validation_table1.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Non-dimensional fundamental frequencies of CNTRC plates for validation against reference data.
- schema:
  - `type`: table
  - `required_columns`: `Temperature`, `Distribution`, `Mode`, `Frequency`
  - `columns`:
    - `Temperature`: integer
    - `Distribution`: string (one of: UD, FG-X, FG-O, FG-V)
    - `Mode`: integer (1,2,3)
    - `Frequency`: float (non-dimensional)

### step_02_validation_table2.csv
- path: `/app/outputs/step_02_validation_table2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Natural frequencies of a stiffened laminated plate for convergence validation.
- schema:
  - `type`: table
  - `required_columns`: `Mode`, `Mesh`, `Frequency`
  - `columns`:
    - `Mode`: integer (1-4)
    - `Mesh`: string (one of: 6x6, 8x8, 10x10)
    - `Frequency`: float (Hz)

### step_03_ssss_stiffeners.csv
- path: `/app/outputs/step_03_ssss_stiffeners.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Non-dimensional fundamental frequencies for SSSS plates with varying stiffener counts.
- schema:
  - `type`: table
  - `required_columns`: `BC`, `nx_ny`, `Distribution`, `Frequency`
  - `columns`:
    - `BC`: string (SSSS)
    - `nx_ny`: string (e.g. '0,0', '1,0', ... '4,4')
    - `Distribution`: string (one of: UD, FG-X, FG-O, FG-V)
    - `Frequency`: float (non-dimensional)

### step_04_cccc_stiffeners.csv
- path: `/app/outputs/step_04_cccc_stiffeners.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Non-dimensional fundamental frequencies for CCCC plates with varying stiffener counts.
- schema:
  - `type`: table
  - `required_columns`: `BC`, `nx_ny`, `Distribution`, `Frequency`
  - `columns`:
    - `BC`: string (CCCC)
    - `nx_ny`: string (e.g. '0,0', '1,0', ... '4,4')
    - `Distribution`: string (one of: UD, FG-X, FG-O, FG-V)
    - `Frequency`: float (non-dimensional)

### step_05_temperature_ssss.csv
- path: `/app/outputs/step_05_temperature_ssss.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Natural frequencies for SSSS plates at varying temperature and CNT volume fraction.
- schema:
  - `type`: table
  - `required_columns`: `BC`, `Temperature`, `V_CNT`, `Distribution`, `Frequency`
  - `columns`:
    - `BC`: string (SSSS)
    - `Temperature`: integer (300,500,700)
    - `V_CNT`: float (0.12,0.17,0.28)
    - `Distribution`: string (one of: UD, FG-X, FG-O, FG-V)
    - `Frequency`: float (Hz)

### step_06_temperature_cccc.csv
- path: `/app/outputs/step_06_temperature_cccc.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Natural frequencies for CCCC plates at varying temperature and CNT volume fraction.
- schema:
  - `type`: table
  - `required_columns`: `BC`, `Temperature`, `V_CNT`, `Distribution`, `Frequency`
  - `columns`:
    - `BC`: string (CCCC)
    - `Temperature`: integer (300,500,700)
    - `V_CNT`: float (0.12,0.17,0.28)
    - `Distribution`: string (one of: UD, FG-X, FG-O, FG-V)
    - `Frequency`: float (Hz)

Notes: All scored artifacts are CSV tables; the hidden checker compares each frequency value against the paper's reported values using relative tolerances. The solver must implement the FEM from scratch; no external datasets or pre-trained models are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_validation_table1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature",
          "Distribution",
          "Mode",
          "Frequency"
        ],
        "columns": {
          "Temperature": "integer",
          "Distribution": "string (one of: UD, FG-X, FG-O, FG-V)",
          "Mode": "integer (1,2,3)",
          "Frequency": "float (non-dimensional)"
        }
      },
      "description": "Non-dimensional fundamental frequencies of CNTRC plates for validation against reference data."
    },
    {
      "file": "step_02_validation_table2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Mode",
          "Mesh",
          "Frequency"
        ],
        "columns": {
          "Mode": "integer (1-4)",
          "Mesh": "string (one of: 6x6, 8x8, 10x10)",
          "Frequency": "float (Hz)"
        }
      },
      "description": "Natural frequencies of a stiffened laminated plate for convergence validation."
    },
    {
      "file": "step_03_ssss_stiffeners.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "BC",
          "nx_ny",
          "Distribution",
          "Frequency"
        ],
        "columns": {
          "BC": "string (SSSS)",
          "nx_ny": "string (e.g. '0,0', '1,0', ... '4,4')",
          "Distribution": "string (one of: UD, FG-X, FG-O, FG-V)",
          "Frequency": "float (non-dimensional)"
        }
      },
      "description": "Non-dimensional fundamental frequencies for SSSS plates with varying stiffener counts."
    },
    {
      "file": "step_04_cccc_stiffeners.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "BC",
          "nx_ny",
          "Distribution",
          "Frequency"
        ],
        "columns": {
          "BC": "string (CCCC)",
          "nx_ny": "string (e.g. '0,0', '1,0', ... '4,4')",
          "Distribution": "string (one of: UD, FG-X, FG-O, FG-V)",
          "Frequency": "float (non-dimensional)"
        }
      },
      "description": "Non-dimensional fundamental frequencies for CCCC plates with varying stiffener counts."
    },
    {
      "file": "step_05_temperature_ssss.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "BC",
          "Temperature",
          "V_CNT",
          "Distribution",
          "Frequency"
        ],
        "columns": {
          "BC": "string (SSSS)",
          "Temperature": "integer (300,500,700)",
          "V_CNT": "float (0.12,0.17,0.28)",
          "Distribution": "string (one of: UD, FG-X, FG-O, FG-V)",
          "Frequency": "float (Hz)"
        }
      },
      "description": "Natural frequencies for SSSS plates at varying temperature and CNT volume fraction."
    },
    {
      "file": "step_06_temperature_cccc.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "BC",
          "Temperature",
          "V_CNT",
          "Distribution",
          "Frequency"
        ],
        "columns": {
          "BC": "string (CCCC)",
          "Temperature": "integer (300,500,700)",
          "V_CNT": "float (0.12,0.17,0.28)",
          "Distribution": "string (one of: UD, FG-X, FG-O, FG-V)",
          "Frequency": "float (Hz)"
        }
      },
      "description": "Natural frequencies for CCCC plates at varying temperature and CNT volume fraction."
    }
  ],
  "notes": "All scored artifacts are CSV tables; the hidden checker compares each frequency value against the paper's reported values using relative tolerances. The solver must implement the FEM from scratch; no external datasets or pre-trained models are required."
}
```

## How you are scored
An automated verifier inspects each scored CSV file. For every row, the verifier compares your reported frequency value against a hidden reference value from the literature. The comparison uses a relative tolerance that accounts for the small numerical differences expected when re‑implementing a finite element solver (different integration schemes, mesh, or software). The verifier also checks that the CSV structure, column names, data types, and the set of condition labels (distribution, boundary condition, mesh, etc.) match the expected schema exactly. Each scored step carries a weight; validation steps receive higher weight than parametric steps. The final reward is a weighted score in [0,1] reflecting both the accuracy of the frequency values and the structural correctness of the files. No credit is given for simply reporting a number without a properly working solver, because the verifier acts on the submitted CSV artifacts.
