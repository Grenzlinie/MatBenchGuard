# Doping dependence of magnetic moments and electron-phonon coupling in iron-based superconductors

## Problem background
In iron-based superconductors such as LaFeAsO₁₋ₓFₓ, the coupling between the magnetic moments on Fe atoms and the vibrational modes of the lattice (phonons) is thought to be important for the superconducting mechanism. Electron doping by fluorine substitution changes the Fe magnetic moment and shifts the electronic structure, which in turn modifies the electron-phonon interaction. This task computes the doping dependence of three key quantities: the Fe magnetic moment per atom in the collinear striped antiferromagnetic state, the total electronic density of states at the Fermi level, and the electron-phonon coupling parameter λ for the As A₁g out-of-plane breathing phonon mode.

## Approach
The calculations are performed within density functional theory (DFT) using the local density approximation (LDA) and the virtual crystal approximation (VCA) to simulate fractional fluorine doping, without building supercells. Collinear striped antiferromagnetic order is imposed on the Fe sublattice. The workflow proceeds as follows: a relaxed geometry is obtained for each doping level, then the Fe magnetic moments are extracted and the electronic density of states at the Fermi level is computed. To obtain the electron-phonon coupling, frozen-phonon calculations for the As A₁g mode are performed: the As atoms are displaced symmetrically out of the Fe plane while keeping Fe atoms fixed, and the resulting band shifts (deformation potentials) are used to compute λ via the standard formula relating the band-resolved density of states at the Fermi level, the As mass, and the phonon frequency. All calculations can be carried out with an open-source DFT code (such as SIESTA or Quantum ESPRESSO) using norm-conserving pseudopotentials.

## Reproduction target
For each doping level \(x \in \{0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30\}\):
1. Perform a full geometry relaxation of LaFeAsO₁₋ₓFₓ in the collinear striped antiferromagnetic state (fixed undoped experimental lattice parameters).
2. Compute the Fe magnetic moment per atom (in \(\mu_{\mathrm{B}}\)) and write the results to `/app/outputs/magnetic_moments.csv`.
3. Compute the total density of states at the Fermi level \(N(E_{\mathrm{F}})\) (in states per eV per formula unit) and write to `/app/outputs/dos_fermi.csv`.
4. Determine the deformation potentials for the As A₁g mode by frozen-phonon band-structure calculations, then compute the electron-phonon coupling parameter \(\lambda\) (dimensionless) using a fixed phonon frequency of 25 meV and As mass of 74.92 u, and write the values to `/app/outputs/lambda.csv`.

Each CSV file must contain one row per doping level with columns as specified in the output contract.

## Assets

- SIESTA DFT code (or equivalent open-source DFT code supporting VCA and frozen-phonon): http://siesta-project.org/
- Norm-conserving pseudopotentials for La, Fe, As, O, F: SIESTA pseudopotential library or PseudoDojo
- Crystal structure of LaFeAsO (tetragonal P4/nmm)

## Workflow steps

### Step 1: Geometry relaxation for all doping levels
- Role: process
- Action: For each doping level x in {0.00, 0.05, 0.10, 0.15, 0.20, 0.25, 0.30}: build a VCA model of LaFeAsO1-xFx, impose collinear striped antiferromagnetic order, and relax the atomic positions using DFT (LDA) until residual forces are below 0.01 eV/Å. Keep lattice parameters fixed to the undoped experimental values.
- Evidence: `/app/outputs/geometry_relaxation.log`

### Step 2: Extract Fe magnetic moments
- Role: scored
- Action: From the relaxed structures obtained in step_01, extract the Fe magnetic moment per atom (in μB) for each doping level and write the results to /app/outputs/magnetic_moments.csv.
- Output file: `/app/outputs/magnetic_moments.csv`
- Format: csv
- Contract: CSV with header: x (float), magnetic_moment (float, μB). One row per doping level.
- Scoring: scored by hidden verifier

### Step 3: Compute density of states at the Fermi level
- Role: scored
- Action: For each doping level, perform a DFT DOS calculation on the relaxed collinear AFM structure from step_01. Extract the total electronic density of states at the Fermi level N(EF) in states per eV per formula unit, and write to /app/outputs/dos_fermi.csv.
- Output file: `/app/outputs/dos_fermi.csv`
- Format: csv
- Contract: CSV with header: x (float), dos_fermi (float, states/eV/f.u.). One row per doping level.
- Scoring: scored by hidden verifier

### Step 4: Frozen-phonon deformation potential calculation
- Role: process
- Action: For each doping level and the collinear AFM configuration, perform frozen-phonon calculations for the As A1g phonon mode: displace the As atoms symmetrically out of the Fe plane by ±0.02 Å while keeping Fe atoms fixed. For each displacement (zero, +0.02 Å, -0.02 Å) compute the band structure, then extract the deformation potentials dEn/du for the bands crossing the Fermi level.
- Evidence: `/app/outputs/deformation_potentials.csv`

### Step 5: Compute electron-phonon coupling parameter λ
- Role: scored (load-bearing)
- Action: Using the N(EF) values from step_03 and the deformation potentials from step_04, compute the electron-phonon coupling parameter λ for the A1g mode for each doping level using λ = (1/(2 M_As ω^2)) Σ_n N_n(EF) (dEn/du)^2, with phonon frequency ω = 25 meV and As mass M_As = 74.92 u. If band-resolved DOS is available, sum over bands; otherwise use total N(EF) and an average deformation potential. Write λ values to /app/outputs/lambda.csv.
- Output file: `/app/outputs/lambda.csv`
- Format: csv
- Contract: CSV with header: x (float), lambda (float, dimensionless). One row per doping level.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/magnetic_moments.csv`
- `/app/outputs/dos_fermi.csv`
- `/app/outputs/lambda.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### magnetic_moments.csv
- path: `/app/outputs/magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fe magnetic moment per atom (in μB) as a function of electron doping x.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `x`, `magnetic_moment`
  - `units`:
    - `magnetic_moment`: μB

### dos_fermi.csv
- path: `/app/outputs/dos_fermi.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total electronic density of states at the Fermi level (states/eV per formula unit) vs. doping x.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `x`, `dos_fermi`
  - `units`:
    - `dos_fermi`: states/eV/f.u.

### lambda.csv
- path: `/app/outputs/lambda.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Electron-phonon coupling parameter λ (dimensionless) vs. doping x.
- schema:
  - `type`: table
  - `required`: object
  - `items`: object
  - `required_columns`: `x`, `lambda`
  - `units`:
    - `lambda`: dimensionless

Notes: The checker compares the submitted CSV values to hidden reference values extracted from the paper (Table 1 and digitized Figure 5a,b) with appropriate tolerances. The λ parameter is computed from the standard expression λ = (1/(2M_As ω^2)) Σ_n N_n(EF) (dEn/du)^2 using ω = 25 meV.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "x",
          "magnetic_moment"
        ],
        "units": {
          "magnetic_moment": "μB"
        }
      },
      "description": "Fe magnetic moment per atom (in μB) as a function of electron doping x."
    },
    {
      "file": "dos_fermi.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "x",
          "dos_fermi"
        ],
        "units": {
          "dos_fermi": "states/eV/f.u."
        }
      },
      "description": "Total electronic density of states at the Fermi level (states/eV per formula unit) vs. doping x."
    },
    {
      "file": "lambda.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required": {},
        "items": {},
        "required_columns": [
          "x",
          "lambda"
        ],
        "units": {
          "lambda": "dimensionless"
        }
      },
      "description": "Electron-phonon coupling parameter λ (dimensionless) vs. doping x."
    }
  ],
  "notes": "The checker compares the submitted CSV values to hidden reference values extracted from the paper (Table 1 and digitized Figure 5a,b) with appropriate tolerances. The λ parameter is computed from the standard expression λ = (1/(2M_As ω^2)) Σ_n N_n(EF) (dEn/du)^2 using ω = 25 meV."
}
```

## How you are scored
After your run, a hidden checker reads the three CSV files from `/app/outputs`. The checker compares your reported values for magnetic moments, density of states at the Fermi level, and the electron-phonon coupling parameter λ against hidden reference values that encode the expected physical results for this system. Each of the three quantities is scored independently, and the final reward is a weighted sum (magnetic moments 40%, density of states 20%, λ 40%). The scoring tolerances account for the fact that a re-run with a different DFT implementation may yield slightly different absolute numbers. Submitting correct file formats and correct column headers is necessary but contributes negligible weight; the reward is determined primarily by the accuracy of the numerical contents.
