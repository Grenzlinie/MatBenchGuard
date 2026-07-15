# Thermodynamic Quasi-Equilibrium Evaporation Rates and Carbon Deposition Phase Boundary for the C–H–O System

## Problem background
Chemical vapour deposition (CVD) of diamond films using an oxyacetylene torch produces solid carbon and various gas‑phase species. A thermodynamic quasi‑equilibrium model has been extended from the C–H system to the C–H–O system to predict which species are present and at what rates, and to determine the temperature–O/C‑ratio conditions under which solid carbon (graphite or diamond) can deposit. The model assumes thermochemical equilibrium at the solid surface, expresses evaporation/desorption rates via equilibrium constants and conservation of H and O atoms, and is used to generate rate curves and a CVD phase diagram.

## Approach
The thermodynamic quasi‑equilibrium (QE) model for the C–H–O system assumes thermochemical equilibrium at the solid carbon surface. For each of the 23 gaseous species considered, a surface exchange reaction is written and its temperature‑dependent equilibrium constant is obtained from the JANAF Thermochemical Tables (for diamond, the free‑energy data from Bundy et al. 1961 are used). The model solves the coupled nonlinear conservation equations for hydrogen and oxygen atoms arriving at and leaving the surface; the solutions give the equilibrium partial pressures of H₂ and O₂. With these pressures, the evaporation rate of each species is computed using a standard quasi‑equilibrium rate expression with desorption coefficients set to unity. The net deposition rate of solid carbon (graphite) is then the difference between the incoming and outgoing carbon fluxes. This methodology will be applied to compute the evaporation rates of key gas‑phase species and the deposition rate of graphite at a fixed O/C ratio (0.95) and total pressure of 760 Torr as functions of temperature. It will also be used to locate the etch–growth phase boundary where the net carbon deposition rate becomes zero, by scanning a range of O/C ratios.

## Reproduction target
For a reactant mixture with O/C = 0.95 and total pressure 760 Torr, compute the evaporation rates of the gaseous species H, H₂, CH₄, C₂H₂, C₂H, H₂O, CO₂, and CO, as well as the net deposition rate of solid carbon (graphite), for temperatures from 500 K to 3500 K. Then, for O/C ratios from 0.5 to 2.5, find the temperature at which the net deposition rate of graphite becomes zero (the etch–growth boundary).

## Assets

- JANAF Thermochemical Tables: https://janaf.nist.gov/
- Diamond free energy data (Bundy et al., 1961): 10.1063/1.1733029

## Workflow steps

### Step 1: Compute evaporation and deposition rates at O/C=0.95, 760 Torr
- Role: scored (load-bearing)
- Action: Implement the thermodynamic quasi‑equilibrium model for the C–H–O system: for each temperature in 500–3500 K (step 100 K), set up surface exchange reactions for all 23 gaseous species using equilibrium constants from JANAF data and diamond thermodynamics from Bundy et al. (1961); solve the coupled nonlinear conservation equations for H and O atoms to obtain equilibrium partial pressures of H₂ and O₂ at the solid surface; compute evaporation rates of H, H₂, CH₄, C₂H₂, C₂H, H₂O, CO₂, CO and the net deposition rate of solid carbon (graphite) via the quasi‑equilibrium rate formula with desorption coefficients set to unity. Write the results to rates_R095.csv.
- Output file: `/app/outputs/rates_R095.csv`
- Format: csv
- Contract: CSV with columns: 'T(K)', 'R_H', 'R_H2', 'R_CH4', 'R_C2H2', 'R_C2H', 'R_H2O', 'R_CO2', 'R_CO', 'R_Cs'. Rates are in cm⁻² s⁻¹. Temperatures from 500 K to 3500 K inclusive in steps of 100 K.
- Scoring: scored by hidden verifier

### Step 2: Determine the etch–growth phase boundary for solid carbon
- Role: scored
- Action: Using the same model implementation, scan O/C ratios from 0.5 to 2.5 (step 0.1). For each ratio, locate the temperature where the net deposition rate of graphite transitions from positive to negative (etch–growth boundary) by exploring the model over a dense temperature grid or via root‑finding. Write each (O/C ratio, boundary temperature) pair to deposition_phase_boundary.csv.
- Output file: `/app/outputs/deposition_phase_boundary.csv`
- Format: csv
- Contract: CSV with columns: 'O/C_ratio', 'T_boundary(K)'. O/C ratios from 0.5 to 2.5 in steps of 0.1. T_boundary is the temperature (Kelvin) at which the net carbon deposition rate becomes zero.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/rates_R095.csv`
- `/app/outputs/deposition_phase_boundary.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### rates_R095.csv
- path: `/app/outputs/rates_R095.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Temperature‑dependent evaporation rates of key gaseous species and net graphite deposition rate for O/C = 0.95 at 760 Torr.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `R_H`, `R_H2`, `R_CH4`, `R_C2H2`, `R_C2H`, `R_H2O`, `R_CO2`, `R_CO`, `R_Cs`
  - `units`:
    - `T(K)`: K
    - `R_H`: cm^{-2} s^{-1}
    - `R_H2`: cm^{-2} s^{-1}
    - `R_CH4`: cm^{-2} s^{-1}
    - `R_C2H2`: cm^{-2} s^{-1}
    - `R_C2H`: cm^{-2} s^{-1}
    - `R_H2O`: cm^{-2} s^{-1}
    - `R_CO2`: cm^{-2} s^{-1}
    - `R_CO`: cm^{-2} s^{-1}
    - `R_Cs`: cm^{-2} s^{-1}

### deposition_phase_boundary.csv
- path: `/app/outputs/deposition_phase_boundary.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: O/C ratio vs. temperature at which net graphite deposition becomes zero, defining the etch–growth boundary.
- schema:
  - `type`: table
  - `required_columns`: `O/C_ratio`, `T_boundary(K)`
  - `units`:
    - `O/C_ratio`: dimensionless
    - `T_boundary(K)`: K

Notes: The hidden checker compares the reported rates and boundary temperatures to reference values derived from the paper’s Fig. 6 and Fig. 8 with appropriate tolerances. The model must solve the coupled nonlinear conservation equations using equilibrium constants from the public JANAF and Bundy sources.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "rates_R095.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "R_H",
          "R_H2",
          "R_CH4",
          "R_C2H2",
          "R_C2H",
          "R_H2O",
          "R_CO2",
          "R_CO",
          "R_Cs"
        ],
        "units": {
          "T(K)": "K",
          "R_H": "cm^{-2} s^{-1}",
          "R_H2": "cm^{-2} s^{-1}",
          "R_CH4": "cm^{-2} s^{-1}",
          "R_C2H2": "cm^{-2} s^{-1}",
          "R_C2H": "cm^{-2} s^{-1}",
          "R_H2O": "cm^{-2} s^{-1}",
          "R_CO2": "cm^{-2} s^{-1}",
          "R_CO": "cm^{-2} s^{-1}",
          "R_Cs": "cm^{-2} s^{-1}"
        }
      },
      "description": "Temperature‑dependent evaporation rates of key gaseous species and net graphite deposition rate for O/C = 0.95 at 760 Torr."
    },
    {
      "file": "deposition_phase_boundary.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "O/C_ratio",
          "T_boundary(K)"
        ],
        "units": {
          "O/C_ratio": "dimensionless",
          "T_boundary(K)": "K"
        }
      },
      "description": "O/C ratio vs. temperature at which net graphite deposition becomes zero, defining the etch–growth boundary."
    }
  ],
  "notes": "The hidden checker compares the reported rates and boundary temperatures to reference values derived from the paper’s Fig. 6 and Fig. 8 with appropriate tolerances. The model must solve the coupled nonlinear conservation equations using equilibrium constants from the public JANAF and Bundy sources."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact against reference results. For the rates file, it checks that the computed rates at selected temperatures are consistent with expected trends and magnitudes; for the phase boundary file, it checks that the boundary temperatures at specific O/C ratios are close to known values and that the boundary is monotonic. The final reward is a weighted combination of these stage scores, with greater weight on the rates stage.
