# CALPHAD Thermodynamic Assessment of Ternary Alloy Phase Equilibria

## Problem background
U-Nb-Zr alloys are studied as candidate nuclear fuels due to their high fissile density and thermal conductivity. The high-temperature bcc-γ phase stability and the evolution of its miscibility gaps (γ1+γ2, γ1+γ3, γ4+γ5) are critical for microstructural stability under irradiation. An accurate thermodynamic description of phase equilibria across the whole composition and temperature range is needed for alloy design and kinetic simulations. The present task involves the first CALPHAD (CALculation of PHAse Diagram) assessment of the U-Nb-Zr ternary system. The goal is to compute a self-consistent set of Gibbs energy parameters for the liquid, bcc-γ, βU, αU, αZr, and δ-UZr₂ phases that reproduce experimental phase diagram data, and to verify the description by calculating an isothermal section.

## Approach
The core method is a CALPHAD thermodynamic optimization. The liquid, γ, βU, αU, and αZr phases are modeled as substitutional solutions (U,Nb,Zr)₁ with Redlich–Kister–Muggianu excess terms. The δ phase is described with a two-sublattice model (U,Zr)₂/₃(Nb,Zr)₁/₃, assuming Nb substitutes for Zr. Starting from published binary descriptions for U-Zr, Nb-Zr, and U-Nb, the agent performs a stepwise optimization against experimental phase equilibrium data digitized from the literature. The optimization adjusts ternary γ interaction parameters, revises U-Nb binary γ parameters to correct the γ4+γ5 miscibility gap, introduces temperature‑dependent parameters, fits the δ end‑member energies, and finally refines liquid ternary parameters. The workflow uses the open‑source pycalphad package for Gibbs energy calculations and equilibrium computation. After obtaining the parameter set, the agent calculates the isothermal section at 700°C in the U‑rich region.

## Reproduction target
Produce a self-consistent set of assessed thermodynamic parameters (Gibbs energy expressions) for all phases in the U-Nb-Zr ternary system by performing the full stepwise CALPHAD optimization, and compute the equilibrium phase boundaries for the 700°C isothermal section in the U‑rich area (covering the αU+γ, βU+γ, and γ single‑phase regions). The output must be a JSON file containing the parameter expressions and a CSV file listing the coordinates of two‑phase boundary points at 700°C.

## Assets

- pycalphad open-source CALPHAD software: https://pypi.org/project/pycalphad/
- Phase diagram data from Dwight & Mueller (1957), ANL-5581
- Phase diagram data from Ivanov & Gomozov (1961), 'Phase diagrams of uranium alloys'
- Liquidus/solidus data from Badayeva & Kuznetsova (1971), Russ. Metall.
- U-Zr binary thermodynamic parameters from Xiong et al. (2013): 10.1016/j.jnucmat.2013.08.001
- Nb-Zr binary thermodynamic parameters from Guillermet (1991): 10.1515/ijmr-1991-820602
- U-Nb binary thermodynamic parameters from Duong et al. (2016): 10.1016/j.calphad.2016.08.001
- SGTE pure element Gibbs energy data by Dinsdale (1991): 10.1016/0364-5916(91)90030-N

## Workflow steps

### Step 1: Curate experimental data and assign weights
- Role: process
- Action: Extract phase equilibrium data from the original reference figures (Dwight & Mueller 1957, Ivanov & Gomozov 1961, Badayeva & Kuznetsova 1971) by digitization where necessary. Assign a weight to each data point reflecting its experimental uncertainty, following the paper's critical evaluation. Save the curated dataset in a structured format (CSV) for use in optimization.
- Evidence: `/app/outputs/curated_data.csv`

### Step 2: Optimize thermodynamic parameters
- Role: scored (load-bearing)
- Action: Using the curated experimental data and the initial binary Gibbs energy descriptions from Xiong et al. (U-Zr), Guilermet (Nb-Zr), and Duong et al. (U-Nb, adjusted per the paper), perform a stepwise CALPHAD optimization to obtain the final parameter set. Use an open-source optimizer (e.g., pycalphad's optimizer or a custom least-squares routine) to minimize the weighted sum of squared differences between calculated and experimental phase equilibria. Follow the stepwise strategy: fit ternary γ interaction parameters to 700°C isothermal data, adjust U-Nb binary γ parameters to correct the miscibility gap widening, introduce temperature-dependent γ and δ parameters, fit liquid ternary parameters, and final simultaneous refinement. Output the complete set of assessed thermodynamic parameters in a JSON file, including all interaction parameters and end-member energies assessed in the optimization.
- Output file: `/app/outputs/assessed_parameters.json`
- Format: json
- Contract: JSON object where each key is a parameter identifier string (e.g., 'L0_U_Nb_liquid') and the value is a string representing the parameter expression (e.g., '12345+10*T'). All temperatures in Kelvin, units J/(mol of atoms).
- Scoring: scored by hidden verifier

### Step 3: Calculate 700°C isothermal section phase boundaries
- Role: scored
- Action: Using the optimized parameters from step_02, compute the equilibrium phase boundaries for the U-Nb-Zr isothermal section at 700°C via a CALPHAD equilibrium calculation (e.g., using pycalphad). Generate a set of (U, Nb, Zr) composition coordinates for the phase boundaries covering the two-phase regions in the U-rich area (αU+γ, βU+γ, γ single-phase, etc.), covering the specified U-rich region (αU+γ, βU+γ, and γ single-phase areas). Output a CSV with columns for each two-phase boundary point.
- Output file: `/app/outputs/isothermal_700C_coords.csv`
- Format: csv
- Contract: CSV with columns: phase1 (string), phase2 (string), composition_U_at_frac (float, atomic fraction of U), composition_Nb_at_frac (float, atomic fraction of Nb), T_C (float, temperature in Celsius, constant 700). Each row represents a point on a phase boundary of a two-phase region.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/assessed_parameters.json`
- `/app/outputs/isothermal_700C_coords.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### assessed_parameters.json
- path: `/app/outputs/assessed_parameters.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Thermodynamic parameter expressions assessed in the present modeling.
- schema:
  - `type`: object
  - `key_type`: string
  - `value_type`: string
  - `units`: J/(mol atoms), T in K
  - `description`: Each entry maps a parameter identifier (e.g., 'L0_U_Nb_liquid') to its expression string (e.g., '12345+10*T').

### isothermal_700C_coords.csv
- path: `/app/outputs/isothermal_700C_coords.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Phase boundary coordinates for the 700°C isothermal section of the U-Nb-Zr system.
- schema:
  - `type`: table
  - `required_columns`: `phase1`, `phase2`, `composition_U_at_frac`, `composition_Nb_at_frac`, `T_C`
  - `columns`:
    - `phase1`: string
    - `phase2`: string
    - `composition_U_at_frac`: float
    - `composition_Nb_at_frac`: float
    - `T_C`: float
  - `units`:
    - `composition_U_at_frac`: atomic fraction
    - `composition_Nb_at_frac`: atomic fraction
    - `T_C`: Celsius

Notes: The isothermal section coordinates are validated against hidden experimental points; the parameters are compared against reference expressions using appropriate tolerances. No other phase diagrams are scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "assessed_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "key_type": "string",
        "value_type": "string",
        "units": "J/(mol atoms), T in K",
        "description": "Each entry maps a parameter identifier (e.g., 'L0_U_Nb_liquid') to its expression string (e.g., '12345+10*T')."
      },
      "description": "Thermodynamic parameter expressions assessed in the present modeling."
    },
    {
      "file": "isothermal_700C_coords.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase1",
          "phase2",
          "composition_U_at_frac",
          "composition_Nb_at_frac",
          "T_C"
        ],
        "columns": {
          "phase1": "string",
          "phase2": "string",
          "composition_U_at_frac": "float",
          "composition_Nb_at_frac": "float",
          "T_C": "float"
        },
        "units": {
          "composition_U_at_frac": "atomic fraction",
          "composition_Nb_at_frac": "atomic fraction",
          "T_C": "Celsius"
        }
      },
      "description": "Phase boundary coordinates for the 700°C isothermal section of the U-Nb-Zr system."
    }
  ],
  "notes": "The isothermal section coordinates are validated against hidden experimental points; the parameters are compared against reference expressions using appropriate tolerances. No other phase diagrams are scored."
}
```

## How you are scored
A hidden verifier independently scores each of your two output artifacts and combines them into a final reward (0 to 1). The assessed_parameters.json is compared to a reference set of parameter expressions using tolerances appropriate for CALPHAD re‑assessments. The isothermal_700C_coords.csv phase boundaries are validated by recomputing the isothermal section with your submitted parameters and measuring the mean distance to hidden experimental holdout points. The phase boundary accuracy carries a larger weight than the parameter agreement. You must genuinely execute the optimization and compute the isothermal section; reporting expected numbers is not sufficient.
