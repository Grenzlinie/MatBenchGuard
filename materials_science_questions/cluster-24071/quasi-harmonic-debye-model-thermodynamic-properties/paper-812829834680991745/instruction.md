# Quasi-harmonic Debye model thermodynamic properties and lattice thermal conductivity of half-Heusler alloys

## Problem background
TiNiSn half-Heusler alloy is a promising n-type thermoelectric material with high power factor but also high lattice thermal conductivity, which limits its thermoelectric figure of merit. Substituting transition metals (TM) on the Ti-site can alter the vibrational and structural properties, potentially reducing the lattice thermal conductivity. This task investigates how substitution of Sc, Zr, Hf, V, Nb, and Mn at various concentrations affects the thermodynamic and thermal transport properties of Ti1-xTMxNiSn.

## Approach
The workflow combines first-principles density functional theory (DFT) total-energy calculations with the quasi-harmonic Debye model. For each composition, total energy is computed over a range of lattice constants to obtain energy–volume curves. These curves are fitted to an equation of state to extract equilibrium lattice constants and bulk moduli. The quasi-harmonic Debye model then uses these parameters to compute, as functions of temperature, the Debye temperature, Grüneisen parameter, isothermal and adiabatic bulk moduli, and volume thermal expansion coefficient. Finally, the lattice thermal conductivity is evaluated using the Slack–Berman relation with Julian's parameterization, which depends on Debye temperature, Grüneisen parameter, volume, and average atomic mass. All DFT calculations are performed with the Quantum ESPRESSO package using PBE-GGA pseudopotentials. The quasi-harmonic Debye model can be implemented via the GIBBS code or an equivalent implementation of the relevant thermodynamic equations.

## Reproduction target
Compute the following quantities at 300 K for all 25 compositions Ti1-xTMxNiSn (TM = Sc, Zr, Hf, V, Nb, Mn; x = 0, 0.25, 0.5, 0.75, 1): lattice constant a0 (Å), bulk modulus B0 (GPa), Debye temperature Θ (K), Grüneisen parameter γ (dimensionless), volume thermal expansion coefficient α (K⁻¹), and lattice thermal conductivity κlat (W/m·K). Output these as a CSV file with columns: composition, a0, B0, Theta, gamma, alpha, kappa_lat_300K. Additionally, compute the temperature-dependent lattice thermal conductivity κlat as a function of temperature from 0 to 1000 K in steps of 100 K for the four compositions TiNiSn, Ti0.75Zr0.25NiSn, Ti0.75Hf0.25NiSn, and Ti0.50Mn0.50NiSn. Output this as a second CSV file with columns: composition, T, kappa_lat. All output files must be placed under /app/outputs.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- PBE-GGA pseudopotentials: https://www.quantum-espresso.org/pseudopotentials/
- GIBBS quasi-harmonic Debye code: http://qjub.usc.es/gibbs/

## Workflow steps

### Step 1: Prepare DFT input structures for Ti1-xTMxNiSn compositions
- Role: process
- Action: Generate crystal structure files for all 25 compositions Ti1-xTMxNiSn (TM = Sc, Zr, Hf, V, Nb, Mn; x = 0, 0.25, 0.5, 0.75, 1) using the half-Heusler space group (No. 216) and appropriate Wyckoff positions (Ti/4a, Ni/4c, Sn/4b) with random/substitutional placement of TM atoms.
- Evidence: `/app/outputs/structure_generation.log`

### Step 2: DFT total-energy vs volume scans
- Role: process
- Action: For each composition, perform self-consistent DFT total-energy calculations using Quantum ESPRESSO with PBE-GGA pseudopotentials. Vary the lattice constant over a range that captures the energy minimum to obtain total energy versus volume (E-V) curves. Collect the raw energy-volume data for each composition.
- Evidence: `/app/outputs/ev_curves.tar.gz`

### Step 3: Fit equations of state and extract equilibrium parameters
- Role: process
- Action: For each composition, fit the computed E-V data to an equation of state (e.g., Vinet, Birch-Murnaghan, or Spinoda) to obtain the zero-temperature equilibrium volume V0 (or lattice constant a0) and bulk modulus B0. Also determine the pressure derivative B0' if required.
- Evidence: `/app/outputs/eos_fits.csv`

### Step 4: Quasi-harmonic Debye model calculations
- Role: process
- Action: Using the fitted EOS parameters, run the quasi-harmonic Debye model (GIBBS code or equivalent implementation of the relevant equations) to compute as functions of temperature (0-1000 K): Debye temperature, isothermal bulk modulus, adiabatic bulk modulus, Grüneisen parameter, and volume thermal expansion coefficient.
- Evidence: `/app/outputs/debye_results.json`

### Step 5: Compute 300 K properties table
- Role: scored (load-bearing)
- Action: For each composition, evaluate the quasi-harmonic Debye model outputs at 300 K and compute lattice thermal conductivity using the Slack-Berman relation with Julian's parameterization. Write a CSV file containing all 25 compositions and their lattice constant a0, bulk modulus B0, Debye temperature, Grüneisen parameter, volume thermal expansion coefficient, and lattice thermal conductivity at 300 K.
- Output file: `/app/outputs/step_01_properties.csv`
- Format: csv
- Contract: CSV with columns: composition, a0 (Angstrom), B0 (GPa), Theta (K), gamma, alpha (1/K), kappa_lat_300K (W/mK). One row per composition (25 rows).
- Scoring: scored by hidden verifier

### Step 6: Compute temperature-dependent lattice thermal conductivity
- Role: scored
- Action: For the four selected compositions (TiNiSn, Ti0.75Zr0.25NiSn, Ti0.75Hf0.25NiSn, Ti0.50Mn0.50NiSn), evaluate lattice thermal conductivity at temperatures from 0 to 1000 K in steps of 100 K using the same Slack-Berman formula and the temperature-dependent properties from the quasi-harmonic Debye model. Write a CSV file with the results.
- Output file: `/app/outputs/step_02_kappa_vs_T.csv`
- Format: csv
- Contract: CSV with columns: composition, T (K), kappa_lat (W/mK). One row per (composition, T) pair (44 rows: 4 compositions * 11 temperatures).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_properties.csv`
- `/app/outputs/step_02_kappa_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_properties.csv
- path: `/app/outputs/step_01_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Structural and thermal properties at 300 K for all 25 Ti1-xTMxNiSn compositions; used as the primary reproduction target.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `a0`, `B0`, `Theta`, `gamma`, `alpha`, `kappa_lat_300K`
  - `units`:
    - `a0`: Angstrom
    - `B0`: GPa
    - `Theta`: K
    - `gamma`: dimensionless
    - `alpha`: 1/K
    - `kappa_lat_300K`: W/mK

### step_02_kappa_vs_T.csv
- path: `/app/outputs/step_02_kappa_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature-dependent lattice thermal conductivity for TiNiSn, Ti0.75Zr0.25NiSn, Ti0.75Hf0.25NiSn, and Ti0.50Mn0.50NiSn from 0 to 1000 K.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `T`, `kappa_lat`
  - `units`:
    - `T`: K
    - `kappa_lat`: W/mK

Notes: Checker compares submitted numeric values to hidden reference values from the paper with appropriate tolerances; also enforces structural ordering and reduction percentage constraints for the highlighted compositions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "a0",
          "B0",
          "Theta",
          "gamma",
          "alpha",
          "kappa_lat_300K"
        ],
        "units": {
          "a0": "Angstrom",
          "B0": "GPa",
          "Theta": "K",
          "gamma": "dimensionless",
          "alpha": "1/K",
          "kappa_lat_300K": "W/mK"
        }
      },
      "description": "Structural and thermal properties at 300 K for all 25 Ti1-xTMxNiSn compositions; used as the primary reproduction target."
    },
    {
      "file": "step_02_kappa_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "T",
          "kappa_lat"
        ],
        "units": {
          "T": "K",
          "kappa_lat": "W/mK"
        }
      },
      "description": "Temperature-dependent lattice thermal conductivity for TiNiSn, Ti0.75Zr0.25NiSn, Ti0.75Hf0.25NiSn, and Ti0.50Mn0.50NiSn from 0 to 1000 K."
    }
  ],
  "notes": "Checker compares submitted numeric values to hidden reference values from the paper with appropriate tolerances; also enforces structural ordering and reduction percentage constraints for the highlighted compositions."
}
```

## How you are scored
Your submitted CSV files will be evaluated by a hidden verifier that compares the numeric values in each column against a set of hidden reference values. The verifier applies pre-defined tolerances for each physical quantity and also checks certain structural relationships among the compositions (e.g., the ordering of thermal conductivity for particular substituted compounds). The overall score is a weighted combination of the agreement across all required outputs. It is essential that the computational workflow be executed faithfully, as merely reporting arbitrary numbers will not satisfy the hidden checks.
