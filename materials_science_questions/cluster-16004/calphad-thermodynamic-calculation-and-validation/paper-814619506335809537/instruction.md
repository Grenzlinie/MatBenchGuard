# Thermodynamic Assessment of the Ni-Os Binary System using CALPHAD

## Problem background
The Ni–Os system is relevant for Ni-based superalloys, where alloying with Os can improve high-temperature creep resistance. Reliable knowledge of the thermodynamic phase equilibria in this binary system is essential for alloy design. The CALPHAD (CALculation of PHAse Diagrams) method provides a framework to derive a self-consistent thermodynamic description from critically evaluated experimental data. This task focuses on reproducing a CALPHAD thermodynamic optimization for the binary Ni–Os system, specifically the Gibbs energy interaction parameters for the liquid, fcc, and hcp phases, and computing the resulting phase diagram boundaries.

## Approach
Use the open-source CALPHAD tool pycalphad. Treat the liquid, fcc, and hcp phases as substitutional solutions with a Redlich–Kister excess Gibbs energy model. Use the SGTE pure element Gibbs energies (included in pycalphad). Formulate the optimization problem by constructing the total Gibbs energy of each phase, including magnetic contributions (Curie temperature and magnetic moment) for the fcc phase. Then perform a nonlinear least‑squares fit of the adjustable interaction parameters against the available experimental phase equilibria data: solubility limits of Ni and Os, the peritectic temperature, Curie temperatures, and magnetic moments from the literature. After obtaining the parameters, compute the equilibrium phase diagram to determine selected tie‑line compositions.

## Reproduction target
Produce two scored artifacts. First, a JSON file containing the optimized thermodynamic parameters: for each phase (Liquid, Hcp) a temperature‑dependent interaction parameter L0 = a + b·T (a in J/mol‑atoms, b in J/(mol‑atoms·K)); for the Fcc phase additionally the interaction terms for Curie temperature (Tc_interaction, in K) and magnetic moment (beta_interaction, in Bohr magnetons). Second, a CSV file with the computed equilibrium compositions: the fcc‑solvus and hcp‑solvus compositions at 1300 K, 1500 K, and 1700 K, and the liquid composition at the peritectic temperature 1773 K. The exact output formats are specified in the workflow steps and output contract.

## Assets

- pycalphad: https://pypi.org/project/pycalphad/
- Ni-Os experimental phase equilibria data

## Workflow steps

### Step 1: Thermodynamic optimization of Ni-Os system
- Role: scored
- Action: Using the CALPHAD method with pycalphad, optimize the Gibbs energy interaction parameters for the liquid, fcc, and hcp phases of the Ni-Os binary system. Input experimental phase equilibria data (solubility limits, peritectic temperature, Curie temperatures, magnetic moments) from the literature and SGTE pure element Gibbs energies (included in pycalphad). Perform a nonlinear least-squares optimization to determine the adjustable parameters. Write the optimized parameters to the output file.
- Output file: `/app/outputs/thermodynamic_parameters.json`
- Format: json
- Contract: JSON object with keys "Liquid", "Fcc", "Hcp". Each key holds an object with a "L0" array [a, b] for the temperature-dependent interaction parameter (a + b*T, a in J/mol-atoms, b in J/(mol-atoms·K)). For "Fcc" additionally include "Tc_interaction" (array or number, in K) and "beta_interaction" (array or number, in Bohr magnetons), representing the interaction terms for Curie temperature and magnetic moment.
- Scoring: scored by hidden verifier

### Step 2: Computation of phase diagram boundaries
- Role: scored (load-bearing)
- Action: Using the optimized thermodynamic parameters from step1 and an open-source equilibrium calculator (pycalphad), compute the equilibrium compositions of the fcc solvus, hcp solvus at temperatures 1300 K, 1500 K, 1700 K, and the liquid composition at the peritectic temperature 1773 K. Write the results as a CSV file.
- Output file: `/app/outputs/phase_boundaries.csv`
- Format: csv
- Contract: CSV with columns: phase (string), temperature_K (float), composition_Os_at_frac (float). Expected rows: fcc_solvus at 1300 K, 1500 K, 1700 K; hcp_solvus at 1300 K, 1500 K, 1700 K; and liquid composition at peritectic 1773 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermodynamic_parameters.json`
- `/app/outputs/phase_boundaries.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermodynamic_parameters.json
- path: `/app/outputs/thermodynamic_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimized thermodynamic parameters to be compared against the reference interaction coefficients and magnetic terms.
- schema:
  - `type`: object
  - `required`:
    - `Liquid`:
      - `L0`: `number`, `number`
    - `Fcc`:
      - `L0`: `number`, `number`
      - `Tc_interaction`: `number`
      - `beta_interaction`: `number`
    - `Hcp`:
      - `L0`: `number`, `number`
  - `units`:
    - `L0`: J/mol-atoms, K
    - `Tc_interaction`: K
    - `beta_interaction`: Bohr magnetons

### phase_boundaries.csv
- path: `/app/outputs/phase_boundaries.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Phase boundary compositions; the checker recomputes equilibria from the agent's parameters and compares both consistency and agreement with digitized phase diagram points.
- schema:
  - `type`: table
  - `required_columns`: `phase`, `temperature_K`, `composition_Os_at_frac`
  - `columns`:
    - `phase`: string (e.g., fcc_solvus, hcp_solvus, liquid)
    - `temperature_K`: float
    - `composition_Os_at_frac`: float

Notes: The checker will recompute equilibria using pycalphad with the agent's submitted thermodynamic parameters to verify internal consistency, then compare the recomputed boundaries against the paper's phase diagram digitized points with tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermodynamic_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "Liquid": {
            "L0": [
              "number",
              "number"
            ]
          },
          "Fcc": {
            "L0": [
              "number",
              "number"
            ],
            "Tc_interaction": [
              "number"
            ],
            "beta_interaction": [
              "number"
            ]
          },
          "Hcp": {
            "L0": [
              "number",
              "number"
            ]
          }
        },
        "units": {
          "L0": "J/mol-atoms, K",
          "Tc_interaction": "K",
          "beta_interaction": "Bohr magnetons"
        }
      },
      "description": "Optimized thermodynamic parameters to be compared against the reference interaction coefficients and magnetic terms."
    },
    {
      "file": "phase_boundaries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "phase",
          "temperature_K",
          "composition_Os_at_frac"
        ],
        "columns": {
          "phase": "string (e.g., fcc_solvus, hcp_solvus, liquid)",
          "temperature_K": "float",
          "composition_Os_at_frac": "float"
        }
      },
      "description": "Phase boundary compositions; the checker recomputes equilibria from the agent's parameters and compares both consistency and agreement with digitized phase diagram points."
    }
  ],
  "notes": "The checker will recompute equilibria using pycalphad with the agent's submitted thermodynamic parameters to verify internal consistency, then compare the recomputed boundaries against the paper's phase diagram digitized points with tolerances."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage’s artifact and combines the results into a final reward. The thermodynamic parameters are compared against a set of reference values (interaction coefficients and magnetic terms) using appropriate tolerances. The phase boundary file is evaluated by re‑computing the equilibria from your submitted parameters with pycalphad to verify internal consistency, and then checking the computed compositions against the expected phase equilibrium data. Both checks contribute to the final score; merely reporting the paper’s numbers without running the optimization will not pass.
