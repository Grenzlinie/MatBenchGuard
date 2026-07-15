# Molecular Dynamics Simulation of First-Order Monolayer Freezing in Confined Water

## Problem background
When water is confined to nanometre-thick films between two parallel plates, its behaviour can deviate strongly from that of bulk water. In particular, the interplay between geometric constraints and the tetrahedral hydrogen‑bonding network of water molecules may give rise to unusual phase behaviour. This study investigates whether a monolayer of water confined between two smooth walls at ambient temperature can undergo a freezing transition as the plate separation is increased, and what dynamical and structural signatures would characterise such a transition. Understanding this phenomenon sheds light on two‑dimensional phase transitions and the effect of confinement on water’s hydrogen‑bond network.

## Approach
The investigation uses classical molecular dynamics simulations with the TIP5P water model, which explicitly represents the tetrahedral coordination of water. A monolayer of 780 water molecules is placed between two parallel Lennard‑Jones walls that mimic a weakly interacting surface (e.g., quartz). Two sets of simulations are performed. In the first set, the plate separation H is varied from 0.41 nm to 0.59 nm at a constant temperature of 300 K and a lateral pressure of 1 bar. From the trajectories, the in‑plane mean‑square displacement and the transverse oxygen density profile are computed. The lateral diffusion coefficient is extracted as a function of H, and the density profiles are obtained for several characteristic separations. In a second set, at a fixed separation H = 0.50 nm the lateral area A is varied in a series of constant‑NVT simulations. From these runs, the lateral pressure and potential energy are computed as functions of A to construct an isotherm. The combined dynamical, structural, and thermodynamic data are used to characterise the phase behaviour of the monolayer.

## Reproduction target
Produce three quantitative analyses from the simulations:
1. The lateral diffusion coefficient as a function of plate separation H (from 0.41 nm to 0.59 nm), reported in `diffusion_results.csv`.
2. The transverse oxygen density profiles at H = 0.47 nm and H = 0.53 nm (optionally also 0.58 nm), reported in `density_profiles.csv`.
3. The pressure–area isotherm and energy–area curve at H = 0.50 nm over the area range 50–65 nm², reported in `isotherm_data.csv`.
The goal is to determine whether these data reveal a monolayer freezing transition and, if so, to identify its dynamical and structural fingerprints.

## Assets

- GROMACS MD simulation package: https://www.gromacs.org/
- TIP5P water model parameters: GROMACS force field library

## Workflow steps

### Step 1: Prepare initial monolayer configuration
- Role: process
- Action: Set up a system of 780 TIP5P water molecules confined between two Lennard-Jones walls at plate separation H=0.41 nm, T=300 K, lateral pressure 1 bar. Equilibrate for sufficient time to obtain a stable monolayer liquid configuration.
- Evidence: `/app/outputs/equilibrated.gro`

### Step 2: Run constant-H simulations (first set)
- Role: process
- Action: Starting from the equilibrated configuration, sequentially increase the plate separation H up to 0.59 nm in small steps. At each H, equilibrate and collect a production trajectory of the confined water at T=300 K and lateral pressure 1 bar.
- Evidence: none

### Step 3: Lateral diffusion coefficient analysis
- Role: scored (load-bearing)
- Action: From the constant-H simulation trajectories, compute the in-plane mean-square displacement and extract the lateral diffusion coefficient for each H. Report the results in a CSV file with one row per H value.
- Output file: `/app/outputs/diffusion_results.csv`
- Format: csv
- Contract: Columns: H_nm (float, plate separation in nm), diffusion_coefficient_cm2_s (float, diffusion coefficient in cm²/s).
- Scoring: scored by hidden verifier

### Step 4: Transverse oxygen density profile analysis
- Role: scored
- Action: From the constant-H trajectories, compute the oxygen atom density distribution along the axis perpendicular to the walls for at least H=0.47 nm and H=0.53 nm (optionally also 0.58 nm). Produce a CSV with profiles for each chosen H.
- Output file: `/app/outputs/density_profiles.csv`
- Format: csv
- Contract: Columns: H_nm (float), z_nm (float, coordinate normal to walls), density_g_ml (float, oxygen density in g/ml).
- Scoring: scored by hidden verifier

### Step 5: Run constant-N A H T simulations (second set)
- Role: process
- Action: At H=0.50 nm, take a liquid monolayer configuration from the first set of simulations. Run a series of NVT simulations by varying the area A in small steps. In the area range where phase coexistence is expected (approximately 54.0–60.4 nm²), use extended equilibration and production times.
- Evidence: none

### Step 6: Isotherm analysis
- Role: scored
- Action: From the constant-area simulations, compute the lateral pressure and potential energy as functions of the area A. Produce a CSV covering the area range from approximately 50 to 65 nm².
- Output file: `/app/outputs/isotherm_data.csv`
- Format: csv
- Contract: Columns: A_nm2 (float, area in nm²), lateral_pressure_bar (float, lateral pressure in bar), potential_energy_kJ_mol (float, potential energy per mole in kJ/mol).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/diffusion_results.csv`
- `/app/outputs/density_profiles.csv`
- `/app/outputs/isotherm_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### diffusion_results.csv
- path: `/app/outputs/diffusion_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Lateral diffusion coefficient as a function of plate separation. The checker will perform a structural audit.
- schema:
  - `type`: table
  - `required_columns`: `H_nm`, `diffusion_coefficient_cm2_s`
  - `units`:
    - `H_nm`: nm
    - `diffusion_coefficient_cm2_s`: cm^2/s

### density_profiles.csv
- path: `/app/outputs/density_profiles.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Transverse oxygen density profiles at selected plate separations. The checker will perform a structural audit.
- schema:
  - `type`: table
  - `required_columns`: `H_nm`, `z_nm`, `density_g_ml`
  - `units`:
    - `H_nm`: nm
    - `z_nm`: nm
    - `density_g_ml`: g/ml

### isotherm_data.csv
- path: `/app/outputs/isotherm_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pressure-area isotherm and energy-area data at H=0.50 nm. The checker will perform a structural audit.
- schema:
  - `type`: table
  - `required_columns`: `A_nm2`, `lateral_pressure_bar`, `potential_energy_kJ_mol`
  - `units`:
    - `A_nm2`: nm^2
    - `lateral_pressure_bar`: bar
    - `potential_energy_kJ_mol`: kJ/mol

Notes: Only the three specified CSV artifacts are scored. The checker performs structural audits (T3) without exact numeric match; tolerances are shape-based.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "diffusion_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "H_nm",
          "diffusion_coefficient_cm2_s"
        ],
        "units": {
          "H_nm": "nm",
          "diffusion_coefficient_cm2_s": "cm^2/s"
        }
      },
      "description": "Lateral diffusion coefficient as a function of plate separation. The checker will perform a structural audit."
    },
    {
      "file": "density_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "H_nm",
          "z_nm",
          "density_g_ml"
        ],
        "units": {
          "H_nm": "nm",
          "z_nm": "nm",
          "density_g_ml": "g/ml"
        }
      },
      "description": "Transverse oxygen density profiles at selected plate separations. The checker will perform a structural audit."
    },
    {
      "file": "isotherm_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "A_nm2",
          "lateral_pressure_bar",
          "potential_energy_kJ_mol"
        ],
        "units": {
          "A_nm2": "nm^2",
          "lateral_pressure_bar": "bar",
          "potential_energy_kJ_mol": "kJ/mol"
        }
      },
      "description": "Pressure-area isotherm and energy-area data at H=0.50 nm. The checker will perform a structural audit."
    }
  ],
  "notes": "Only the three specified CSV artifacts are scored. The checker performs structural audits (T3) without exact numeric match; tolerances are shape-based."
}
```

## How you are scored
Each of the three CSV output files is inspected independently by a hidden verifier. The verifier does not compare your numbers to an external reference value; instead, it checks structural characteristics of the data that arise from correctly executed simulations — for example, the relative magnitude of the diffusion coefficient across different plate separations, the shape (unimodal vs. bimodal) of the density profiles, and the appearance of certain features in the pressure–area curve. The scores from the three artifacts are combined (with the diffusion analysis contributing a larger share) to yield the final reward. Reporting a number that happens to match a published value is not sufficient; the data must reflect the physical behaviour expected from the prescribed system and protocol.
