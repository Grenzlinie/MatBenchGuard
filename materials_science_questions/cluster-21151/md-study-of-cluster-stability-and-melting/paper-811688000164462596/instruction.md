# Decomposition of residual heat capacity and volume derivatives into monomer and association contributions via NpT Monte Carlo simulations

## Problem background
Self-associated fluids such as alcohols exhibit complex temperature-dependent behaviour in their thermodynamic response functions, notably the isobaric heat capacity and the temperature and pressure derivatives of the volume. Understanding the separate contributions from monomeric molecules and from hydrogen‑bond‑induced association is central to rationalising these properties. This task implements a methodology that expresses a configurational property of a pure self-associated fluid as the sum of a monomer‑fluid reference term and an association perturbation, and applies it to OPLS methanol via NpT Monte Carlo simulations.

## Approach
The pure associated fluid is modelled as consisting of two hypothetical fluids: one of monomers (dissociated molecules) and one of associated molecules. Any molar configurational property M is written as a mole‑fraction‑weighted sum M = x_A M_A + x_B M_B, which leads to a perturbative form M = M_A + M_ass, where M_A is the monomer reference and M_ass the association perturbation. From this decomposition, second‑order thermodynamic response functions—residual isobaric heat capacity C_p^r, the temperature derivative of volume (∂V/∂T)_p, and the pressure derivative of volume (∂V/∂p)_T—are obtained as a sum of a monomer contribution and an association contribution. The necessary configurational properties and their derivatives are extracted from NpT Monte Carlo simulations of OPLS methanol along the 50 MPa isobar at a series of temperatures. During the production run, molecules are classified as monomers or associated using geometric hydrogen‑bond criteria (R_OO ≤ 3.5 Å, R_HO ≤ 2.6 Å, donor‑acceptor angle ≤ 30°), and molecular volumes are assigned via a Voronoi‑grid approximation. The resulting raw averages (energies, volumes, mole fractions) are then processed using the fluctuation method to compute temperature and pressure derivatives, from which the decomposed response functions are calculated.

## Reproduction target
Produce the following two output files:
1. Raw simulation averages (step_01_averages.csv) containing, for each temperature T = 220, 300, 400, 500, 600, 800, 1000, 1500 K, the total residual energy U_T^r, total volume V_T, mole fraction of associated molecules x_B, and the residual energies and volumes separately for monomers (U_mon^r, V_mon) and associated molecules (U_agg^r, V_agg).
2. Decomposed response functions (step_02_response_functions.csv) containing, for the same temperature set, the total residual isobaric heat capacity C_p^r and its monomer (C_{p,A}^r) and association (C_{p,ass}^r) contributions, the temperature derivative of volume (∂V/∂T)_p with its monomer and association contributions, and the pressure derivative of volume (∂V/∂p)_T with its monomer and association contributions. All quantities must be expressed in the units specified in the output schema.

## Assets

- OPLS force field parameters for methanol: 10.1021/j100398a020

## Workflow steps

### Step 1: Perform NpT Monte Carlo simulations and compute raw averages
- Role: process
- Action: Run NpT Monte Carlo simulations of 256 OPLS methanol molecules at pressure 50 MPa for each temperature in [220, 300, 400, 500, 600, 800, 1000, 1500] K, using periodic boundary conditions, reaction-field electrostatics, and long-range Lennard-Jones corrections. During the production run, classify every molecule as monomer or associated using geometric H-bond criteria (R_OO ≤ 3.5 Å, R_HO ≤ 2.6 Å, φ ≤ 30°), and assign molecular volumes via a Voronoi-grid approximation. Accumulate time-averaged quantities: total residual energy U_T^r, total volume V_T, mole fraction of associated molecules x_B, residual energy and volume for monomers (U_mon^r, V_mon) and for associated molecules (U_agg^r, V_agg). Save these raw averages as a CSV file (evidence: step_01_averages.csv).
- Evidence: `/app/outputs/step_01_averages.csv`

### Step 2: Compute response‑function decompositions
- Role: scored (load-bearing)
- Action: Using the configurational data from the simulations (energies, volumes, mole fractions, and their covariances), compute temperature and pressure derivatives at constant pressure by the fluctuation method. Then apply the perturbative decomposition to calculate: total residual isobaric heat capacity C_p^r, its monomer contribution C_{p,A}^r, its association contribution C_{p,ass}^r; the temperature derivative of volume (∂V/∂T)_p and its monomer and association contributions; and the pressure derivative of volume (∂V/∂p)_T and its monomer and association contributions. Save all per-temperature results in one CSV file.
- Output file: `/app/outputs/step_02_response_functions.csv`
- Format: csv
- Contract: CSV with header: T (K), Cp_r (J/mol·K), Cp_A_r (J/mol·K), Cp_ass_r (J/mol·K), dVdT (cm³/mol·K), dVdT_A (cm³/mol·K), dVdT_ass (cm³/mol·K), dVdp (cm³/mol·MPa), dVdp_A (cm³/mol·MPa), dVdp_ass (cm³/mol·MPa). One row per temperature.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_response_functions.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_response_functions.csv
- path: `/app/outputs/step_02_response_functions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Headline decomposition quantities of thermodynamic response functions at each temperature for OPLS methanol at 50 MPa.
- schema:
  - `type`: table
  - `required_columns`: `T`, `Cp_r`, `Cp_A_r`, `Cp_ass_r`, `dVdT`, `dVdT_A`, `dVdT_ass`, `dVdp`, `dVdp_A`, `dVdp_ass`
  - `units`:
    - `T`: K
    - `Cp_r`: J/mol·K
    - `Cp_A_r`: J/mol·K
    - `Cp_ass_r`: J/mol·K
    - `dVdT`: cm³/mol·K
    - `dVdT_A`: cm³/mol·K
    - `dVdT_ass`: cm³/mol·K
    - `dVdp`: cm³/mol·MPa
    - `dVdp_A`: cm³/mol·MPa
    - `dVdp_ass`: cm³/mol·MPa

Notes: The reported values are compared against hidden reference values (paper gold) using absolute tolerances: 1.0 J/mol·K for Cp derivatives, 0.5 cm³/mol·K for dVdT derivatives, 0.1 cm³/mol·MPa for dVdp derivatives. This is a result-level comparison (T0).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_response_functions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "Cp_r",
          "Cp_A_r",
          "Cp_ass_r",
          "dVdT",
          "dVdT_A",
          "dVdT_ass",
          "dVdp",
          "dVdp_A",
          "dVdp_ass"
        ],
        "units": {
          "T": "K",
          "Cp_r": "J/mol·K",
          "Cp_A_r": "J/mol·K",
          "Cp_ass_r": "J/mol·K",
          "dVdT": "cm³/mol·K",
          "dVdT_A": "cm³/mol·K",
          "dVdT_ass": "cm³/mol·K",
          "dVdp": "cm³/mol·MPa",
          "dVdp_A": "cm³/mol·MPa",
          "dVdp_ass": "cm³/mol·MPa"
        }
      },
      "description": "Headline decomposition quantities of thermodynamic response functions at each temperature for OPLS methanol at 50 MPa."
    }
  ],
  "notes": "The reported values are compared against hidden reference values (paper gold) using absolute tolerances: 1.0 J/mol·K for Cp derivatives, 0.5 cm³/mol·K for dVdT derivatives, 0.1 cm³/mol·MPa for dVdp derivatives. This is a result-level comparison (T0)."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently compares your reported values in step_02_response_functions.csv against reference values derived from the published paper. The verifier also checks structural consistency, such as the relative magnitude of association contributions to volumetric properties at low temperatures. The final reward is a weighted combination of the scores obtained for each required output. Simply reporting numbers is not sufficient; the verifier expects the outputs to follow the prescribed schemas and to originate from the described Monte Carlo simulation and decomposition pipeline.
