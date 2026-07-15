# Phonon and Thermodynamic Properties of Wurtzite BN from First-Principles

## Problem background
Wurtzite boron nitride (BN) is a III‑N semiconductor with potential electronic and optoelectronic applications. First‑principles density functional theory (DFT) can predict its structural parameters, phonon spectrum, dielectric response, and thermodynamic behaviour. Reproducing these computational predictions provides a rigorous verification of the theoretical framework and benchmarks the simulation workflow.

## Approach
The approach uses first‑principles DFT with two exchange‑correlation functionals: the local density approximation (LDA) and the generalized gradient approximation (GGA / PBE). The equilibrium lattice constants are determined by variable‑cell relaxation. The dynamical matrix at the Γ point is obtained via density functional perturbation theory (DFPT), yielding the phonon frequencies. The Born effective charges and the ionic contributions to the static dielectric tensor are extracted from the same DFPT calculation. Using the full phonon density of states computed on a q‑point mesh, the temperature‑dependent entropy and constant‑volume specific heat are derived under the quasi‑harmonic approximation. All steps are performed with the open‑source Quantum ESPRESSO suite and publicly available pseudopotentials.

## Reproduction target
The goal is to compute, for both LDA and GGA functionals: (1) the equilibrium lattice constants a and c of wurtzite BN; (2) the Γ‑point phonon frequencies for the eight modes E2_l, B1_l, A1_TO, E1_TO, E2_h, B1_h, A1_LO, and E1_LO; (3) the Born effective charges and the ionic contributions to the static dielectric tensor; and (4) the entropy S(T) and constant‑volume specific heat C_V(T) over a temperature range (e.g., 0–1000 K). The results must be written as structured CSV files as specified in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org
- SSSP pseudopotentials for B and N (LDA and GGA): https://www.materialscloud.org/discover/sssp

## Workflow steps

### Step 1: Structural optimization
- Role: scored
- Action: Perform variable-cell relaxation of wurtzite BN with both LDA and GGA functionals to obtain equilibrium lattice constants a and c. Write the resulting values into a CSV file.
- Output file: `/app/outputs/structural_parameters.csv`
- Format: csv
- Contract: functional (string), a (float, Å), c (float, Å). One row per functional (LDA, GGA).
- Scoring: scored by hidden verifier

### Step 2: Phonon frequencies at Gamma point
- Role: scored
- Action: Using the optimized structure, compute the dynamical matrix at Γ via density functional perturbation theory (DFPT) for both functionals. Extract the phonon frequencies (in cm⁻¹) for the eight modes: E2_l, B1_l, A1_TO, E1_TO, E2_h, B1_h, A1_LO, E1_LO. Write the results to a CSV.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: functional (string), mode (string: E2_l, B1_l, A1_TO, E1_TO, E2_h, B1_h, A1_LO, E1_LO), frequency (float, cm⁻¹). Eight rows per functional.
- Scoring: scored by hidden verifier

### Step 3: Born effective charges and static dielectric tensors
- Role: scored
- Action: From the DFPT calculation, extract the parallel and perpendicular components of the Born effective charge (Zp*, Z⟂*) and the static dielectric tensor (ε∥, ε⟂). Output a CSV for each functional.
- Output file: `/app/outputs/dielectric_tensors.csv`
- Format: csv
- Contract: functional (string), Zp_star (float), Zperp_star (float), epsilon_p (float), epsilon_perp (float). One row per functional.
- Scoring: scored by hidden verifier

### Step 4: Thermodynamic properties
- Role: scored (load-bearing)
- Action: Using the full phonon density of states obtained from DFPT (4×4×4 q‑mesh), compute the temperature‑dependent entropy S and constant‑volume specific heat C_V over a range of temperatures (e.g., 0–1000 K) under the quasi‑harmonic approximation. Output a CSV with the calculated values.
- Output file: `/app/outputs/thermodynamic_properties.csv`
- Format: csv
- Contract: functional (string), temperature (float, K), entropy (float, J/mol/K), specific_heat (float, J/mol/K). Multiple rows per functional for a temperature grid.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_parameters.csv`
- `/app/outputs/phonon_frequencies.csv`
- `/app/outputs/dielectric_tensors.csv`
- `/app/outputs/thermodynamic_properties.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_parameters.csv
- path: `/app/outputs/structural_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimal lattice constants a and c for LDA and GGA functionals.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `a`, `c`
  - `units`:
    - `a`: Å
    - `c`: Å

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Phonon frequencies at Gamma point for all eight modes (E2_l, B1_l, A1_TO, E1_TO, E2_h, B1_h, A1_LO, E1_LO).
- schema:
  - `type`: table
  - `required_columns`: `functional`, `mode`, `frequency`
  - `units`:
    - `frequency`: cm⁻¹

### dielectric_tensors.csv
- path: `/app/outputs/dielectric_tensors.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Born effective charges and static dielectric tensors (parallel and perpendicular components).
- schema:
  - `type`: table
  - `required_columns`: `functional`, `Zp_star`, `Zperp_star`, `epsilon_p`, `epsilon_perp`

### thermodynamic_properties.csv
- path: `/app/outputs/thermodynamic_properties.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Temperature-dependent entropy S(T) and constant-volume specific heat C_V(T). Must exhibit correct physical trend (monotonic increase) and match reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `temperature`, `entropy`, `specific_heat`
  - `units`:
    - `temperature`: K
    - `entropy`: J/mol/K
    - `specific_heat`: J/mol/K

Notes: Only scored outputs are listed; the agent must perform full DFT and DFPT calculations to generate these artifacts. The thermodynamic properties serve as a load-bearing check that the phonon calculation was genuinely executed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "a",
          "c"
        ],
        "units": {
          "a": "Å",
          "c": "Å"
        }
      },
      "description": "Optimal lattice constants a and c for LDA and GGA functionals."
    },
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "mode",
          "frequency"
        ],
        "units": {
          "frequency": "cm⁻¹"
        }
      },
      "description": "Phonon frequencies at Gamma point for all eight modes (E2_l, B1_l, A1_TO, E1_TO, E2_h, B1_h, A1_LO, E1_LO)."
    },
    {
      "file": "dielectric_tensors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "Zp_star",
          "Zperp_star",
          "epsilon_p",
          "epsilon_perp"
        ]
      },
      "description": "Born effective charges and static dielectric tensors (parallel and perpendicular components)."
    },
    {
      "file": "thermodynamic_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "temperature",
          "entropy",
          "specific_heat"
        ],
        "units": {
          "temperature": "K",
          "entropy": "J/mol/K",
          "specific_heat": "J/mol/K"
        }
      },
      "description": "Temperature-dependent entropy S(T) and constant-volume specific heat C_V(T). Must exhibit correct physical trend (monotonic increase) and match reference values within tolerance."
    }
  ],
  "notes": "Only scored outputs are listed; the agent must perform full DFT and DFPT calculations to generate these artifacts. The thermodynamic properties serve as a load-bearing check that the phonon calculation was genuinely executed."
}
```

## How you are scored
A hidden verifier evaluates each CSV artifact: structural parameters, phonon frequencies, dielectric tensors, and thermodynamic properties. Each stage is scored individually and assigned a weight; the total reward is the weighted sum. The verifier compares your reported values to reference results using appropriate tolerances, directional thresholds, and structural consistency checks. Simply reporting expected numbers without running the DFT/DFPT calculations will not receive credit—you must genuinely execute the workflow and produce the output files.
