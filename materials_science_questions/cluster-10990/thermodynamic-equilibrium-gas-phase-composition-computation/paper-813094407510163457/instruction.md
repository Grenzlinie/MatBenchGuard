# BN–TiH₂ Equilibrium Phase Composition via Gibbs Energy Minimization

## Problem background
This task addresses chemical phase equilibria in the cubic boron nitride–titanium hydride (cBN–TiH₂) composite system, which is of interest for designing high-performance ceramic cutting tools. During high-pressure sintering, the titanium-based activator can react with BN to form bonding phases (titanium diboride, TiB₂, and titanium nitride, TiN). The relative stability of these phases and their dependence on temperature and pressure determine the final microstructure and mechanical properties of the composite. Reproducing thermodynamic equilibrium calculations for a model 9:1 molar BN:TiH₂ mixture provides a quantitative picture of the driving forces for phase evolution during sintering and post-annealing.

## Approach
The core method is Gibbs free energy minimization, for example using the VCS (Villars–Cruise–Smith) algorithm or any equivalent open‑source chemical equilibrium solver. Given an initial feed of 9 mol BN and 1 mol TiH₂, the Gibbs free energy of the whole system is minimized subject to elemental conservation constraints at fixed temperature and pressure. This must be repeated for a logarithmic pressure sweep from approximately 1 × 10⁻³ Pa to 1 × 10⁷ Pa at two constant temperatures: 950 °C and 1750 °C. Standard thermochemical data (Gibbs free energies of formation as functions of temperature) are taken from the JANAF Thermochemical Tables (or an equivalent public source) for the full set of possible species: B(g), B₂(g), N₂(g), BN(g), Ti(g), H₂(g), BH(g), BH₂(g), BH₃(g), B₂H₆(g), B₅H₉(g), B₁₀H₁₄(g), HN(g), H₂N(g), H₂N₂(g), NH₃(g), N₂H₄(g), TiB₂(s), TiN(s), B(l), Ti(l), TiN(l), TiB₂(l), Tiα(s), Tiβ(s), BN(s), B(s), TiB(s), N₂H₄(l), B₅H₉(l), B₁₀H₁₄(l), B₁₀H₁₄(s), TiH₂(s). The computed equilibrium mole fractions of all condensed phases and partial pressures of every gas species provide a raw dataset from which phase boundaries and species stabilities are extracted.

## Reproduction target
Compute the equilibrium composition of a 9:1 molar BN:TiH₂ mixture at 950 °C and 1750 °C over a pressure range from approximately 1 × 10⁻³ Pa to 1 × 10⁷ Pa using Gibbs free energy minimization with standard thermochemical data from public JANAF tables. Produce structured CSV tables of solid‑phase mole fractions and gas partial pressures for each temperature, and determine the critical pressure at 950 °C above which TiN(s) first becomes stable (mole fraction > 10⁻⁶). The output must consist of three files: equilibrium_950C.csv, equilibrium_1750C.csv (each containing the pressure sweep data), and threshold_950C.txt (a single pressure value in Pa). This enables direct verification of the computed phase stability and the threshold for TiN appearance.

## Assets

- JANAF Thermochemical Tables: https://janaf.nist.gov/
- Cantera: https://cantera.org

## Workflow steps

### Step 1: Gibbs energy minimization pressure sweeps
- Role: process
- Action: Using Gibbs free energy minimization with standard thermochemical data (e.g., JANAF tables) for all species listed in the problem statement, compute equilibrium compositions for a system with initial 9 mol BN and 1 mol TiH₂ at temperatures 950 °C and 1750 °C. For each temperature, sweep pressure logarithmically from about 1e-3 Pa to 1e7 Pa (at least 30 points). For each condition, record equilibrium mole fractions of all solid phases and partial pressures of gas species. Store the full raw equilibrium data in a structured file for later extraction.
- Evidence: `/app/outputs/full_equilibrium_data.csv`

### Step 2: Equilibrium composition at 950 °C
- Role: scored
- Action: From the 950 °C equilibrium sweep results, extract and create equilibrium_950C.csv with columns: pressure_Pa, TiB2_mole_fraction, TiN_mole_fraction, H2_partial_pressure_Pa, N2_partial_pressure_Pa, and any other gas species whose partial pressure exceeds 1e-6 Pa at any point. Populate all pressure points.
- Output file: `/app/outputs/equilibrium_950C.csv`
- Format: csv
- Contract: Header row as described. Values are floats in SI units (pressure in Pa, dimensionless fractions for mole fractions, partial pressures in Pa). Additional columns for minor gas species are allowed.
- Scoring: scored by hidden verifier

### Step 3: Equilibrium composition at 1750 °C
- Role: scored
- Action: From the 1750 °C equilibrium sweep results, extract and create equilibrium_1750C.csv with the same column structure as the 950 °C table.
- Output file: `/app/outputs/equilibrium_1750C.csv`
- Format: csv
- Contract: Same schema as equilibrium_950C.csv.
- Scoring: scored by hidden verifier

### Step 4: TiN appearance threshold at 950 °C
- Role: scored (load-bearing)
- Action: From the 950 °C equilibrium data, identify the lowest pressure at which TiN(s) mole fraction exceeds 1e-6. Write this pressure (in Pa) as a single floating-point number to threshold_950C.txt.
- Output file: `/app/outputs/threshold_950C.txt`
- Format: txt
- Contract: A single line containing a floating-point number in Pa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/equilibrium_950C.csv`
- `/app/outputs/equilibrium_1750C.csv`
- `/app/outputs/threshold_950C.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### equilibrium_950C.csv
- path: `/app/outputs/equilibrium_950C.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium composition at 950 °C, pressure sweep.
- schema:
  - `type`: table
  - `required_columns`: `pressure_Pa`, `TiB2_mole_fraction`, `TiN_mole_fraction`, `H2_partial_pressure_Pa`, `N2_partial_pressure_Pa`
  - `units`:
    - `pressure_Pa`: Pa
    - `TiB2_mole_fraction`: dimensionless
    - `TiN_mole_fraction`: dimensionless
    - `H2_partial_pressure_Pa`: Pa
    - `N2_partial_pressure_Pa`: Pa
  - `additional_columns`: allowed

### equilibrium_1750C.csv
- path: `/app/outputs/equilibrium_1750C.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium composition at 1750 °C, pressure sweep.
- schema:
  - `type`: table
  - `required_columns`: `pressure_Pa`, `TiB2_mole_fraction`, `TiN_mole_fraction`, `H2_partial_pressure_Pa`, `N2_partial_pressure_Pa`
  - `units`:
    - `pressure_Pa`: Pa
    - `TiB2_mole_fraction`: dimensionless
    - `TiN_mole_fraction`: dimensionless
    - `H2_partial_pressure_Pa`: Pa
    - `N2_partial_pressure_Pa`: Pa
  - `additional_columns`: allowed

### threshold_950C.txt
- path: `/app/outputs/threshold_950C.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Threshold pressure for TiN appearance at 950 °C.
- schema:
  - `type`: text
  - `description`: Single floating-point number representing pressure in Pa.

Notes: The solving agent must use a Gibbs energy minimization routine and public thermochemical data. The JANAF tables provide the required species data; any equivalent source is acceptable. The threshold step is load-bearing to prevent bypassing the full equilibrium computation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "equilibrium_950C.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_Pa",
          "TiB2_mole_fraction",
          "TiN_mole_fraction",
          "H2_partial_pressure_Pa",
          "N2_partial_pressure_Pa"
        ],
        "units": {
          "pressure_Pa": "Pa",
          "TiB2_mole_fraction": "dimensionless",
          "TiN_mole_fraction": "dimensionless",
          "H2_partial_pressure_Pa": "Pa",
          "N2_partial_pressure_Pa": "Pa"
        },
        "additional_columns": "allowed"
      },
      "description": "Equilibrium composition at 950 °C, pressure sweep."
    },
    {
      "file": "equilibrium_1750C.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure_Pa",
          "TiB2_mole_fraction",
          "TiN_mole_fraction",
          "H2_partial_pressure_Pa",
          "N2_partial_pressure_Pa"
        ],
        "units": {
          "pressure_Pa": "Pa",
          "TiB2_mole_fraction": "dimensionless",
          "TiN_mole_fraction": "dimensionless",
          "H2_partial_pressure_Pa": "Pa",
          "N2_partial_pressure_Pa": "Pa"
        },
        "additional_columns": "allowed"
      },
      "description": "Equilibrium composition at 1750 °C, pressure sweep."
    },
    {
      "file": "threshold_950C.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing pressure in Pa."
      },
      "description": "Threshold pressure for TiN appearance at 950 °C."
    }
  ],
  "notes": "The solving agent must use a Gibbs energy minimization routine and public thermochemical data. The JANAF tables provide the required species data; any equivalent source is acceptable. The threshold step is load-bearing to prevent bypassing the full equilibrium computation."
}
```

## How you are scored
Your submission is evaluated by an automated hidden verifier that independently checks each scored artifact against reference data derived from the same thermodynamic model and public data. The verifier compares your computed equilibrium tables and threshold pressure with expected values, ensuring that the reported phase compositions follow the correct thermodynamic trends, that the required solid and gas species are present, and that the TiN threshold pressure is consistent with a correct Gibbs minimization sweep. Each scored file (the two CSVs and the threshold text file) contributes a weighted portion to the final reward (total = 1.0). Simply reporting the paper's numbers without performing the actual computation is insufficient; the verifier examines the full equilibrium data and may recompute metrics or pressures from your raw output. The exact scoring tolerances and weights are hidden.
