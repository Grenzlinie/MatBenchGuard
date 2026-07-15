# Purdy solute drag model for Mn enrichment at α/γ interface

## Problem background
High-strength offshore steel requires excellent low-temperature toughness, especially at sub-zero temperatures. A specialized heat treatment (quenching + intercritical annealing + tempering) has been reported to produce a film-like retained austenite phase that significantly improves the impact toughness at -40 °C. The formation of the film-like retained austenite has been attributed to manganese enrichment at the α:γ interface, which restricts austenite growth to a one-dimensional flat morphology. To understand this growth mechanism, a solute drag model (the Purdy model) was used to calculate the Gibbs free energy dissipation caused by manganese segregation at the moving interface. This dissipation opposes interface migration, leading to a characteristic curve of dissipation versus normalized velocity. The present task reproduces that computational calculation: applying the Purdy model to compute the dissipation curve for the given steel composition, thereby verifying the underlying mechanism of film-like austenite formation.

## Approach
The approach is a two-step computational workflow: first obtain the thermodynamic driving force from a CALPHAD calculation, then implement the Purdy solute drag model to compute the dissipation. The Purdy model describes how a substitutional solute like Mn, when segregating at the α:γ interface, creates a chemical potential well that dissipates free energy as the interface moves. The essential equations involve the solute concentration profile across the interface, the interfacial binding energy, and the difference in chemical potential between the two phases. The model yields the Gibbs free energy dissipation ΔG_dis as a function of normalized interface velocity V^Mn = (vδ)/D^Mn, where v is the interface velocity, δ is half the interface thickness, and D^Mn is the diffusion coefficient. The calculation uses nominal Mn content (2.4 wt%), temperature (640 °C), interfacial binding energy (8 kJ/mol), half-thickness (0.5 nm), and the Mn diffusion coefficient (8.3e-17 m²/s). The key input is the chemical potential difference of Mn between ferrite (bcc) and austenite (fcc), which is computed in the first step using an open-source CALPHAD tool with a Fe-Mn-C thermodynamic database. In the second step, the dissipation is evaluated over a logarithmic range of normalized velocities, producing a curve that reveals the drag effect. This curve is independent of the experimental heat treatment; it is a purely thermodynamic/kinetic calculation that can be verified by direct recomputation.

## Reproduction target
Compute the Gibbs free energy dissipation ΔG_dis (kJ/mol) as a function of normalized velocity V^Mn (dimensionless) using the Purdy solute drag model with the specified parameters. Generate a CSV file with at least 20 logarithmically spaced V^Mn values from 0.01 to 100 and the corresponding ΔG_dis. The resulting curve should exhibit the characteristic shape expected from solute drag theory.

## Assets

- Enomoto 1999 paper (Mn diffusion coefficient in austenite): 10.1016/S1359-6454(99)00218-8
- OpenCalphad (thermodynamic calculation tool): opencalphad
- Fe-Mn-C thermodynamic database: https://github.com/opencalphad/databases/tree/master/fe_mn_c
- Python scientific stack (numpy, scipy, matplotlib, csv): numpy, scipy, matplotlib

## Workflow steps

### Step 1: Thermodynamic calculation of Mn chemical potential difference
- Role: process
- Action: Use an open-source CALPHAD tool (e.g., OpenCalphad) with a suitable Fe-Mn-C thermodynamic database to compute the chemical potential difference 2ΔE of Mn between ferrite (bcc) and austenite (fcc) at 640°C for the steel composition (wt%: Fe-0.1C-2.44Mn-0.42Si-0.08Nb-0.30Mo-1.27Ni-1.23Cu). Save the value for use in the next step.
- Evidence: `/app/outputs/delta_E.json`

### Step 2: Purdy solute drag model simulation
- Role: scored (load-bearing)
- Action: Implement the Purdy solute drag model to compute Gibbs free energy dissipation ΔG_dis as a function of normalized interface migration velocity V^Mn. Use parameters: nominal Mn concentration C0 = 2.4 wt%, temperature T = 640°C, interfacial binding energy E^Mn = 8 kJ/mol, interface half-thickness δ = 0.5 nm, Mn diffusion coefficient D^Mn = 8.3e-17 m²/s, and the chemical potential difference ΔE obtained in the previous step. Generate V^Mn values from 0.01 to 100 on a logarithmic scale and compute the corresponding ΔG_dis (kJ/mol). Save the resulting curve as a CSV file.
- Output file: `/app/outputs/step_01_purdy_model.csv`
- Format: csv
- Contract: CSV with two columns: V_Mn (float, dimensionless, normalized velocity) and Delta_G_dis (float, kJ/mol, Gibbs free energy dissipation). At least 20 rows spanning the range V_Mn=0.01 to 100, preferably evenly spaced on a log scale.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_purdy_model.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_purdy_model.csv
- path: `/app/outputs/step_01_purdy_model.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV containing the computed Gibbs free energy dissipation curve from the Purdy solute drag model. The hidden checker recomputes the same curve with exact parameters and compares using MAPE, with a threshold of 0.20; meeting or exceeding (MAPE ≤ 0.20) earns full credit.
- schema:
  - `type`: table
  - `required_columns`: `V_Mn`, `Delta_G_dis`
  - `units`:
    - `V_Mn`: dimensionless
    - `Delta_G_dis`: kJ/mol

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_purdy_model.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "V_Mn",
          "Delta_G_dis"
        ],
        "units": {
          "V_Mn": "dimensionless",
          "Delta_G_dis": "kJ/mol"
        }
      },
      "description": "CSV containing the computed Gibbs free energy dissipation curve from the Purdy solute drag model. The hidden checker recomputes the same curve with exact parameters and compares using MAPE, with a threshold of 0.20; meeting or exceeding (MAPE ≤ 0.20) earns full credit."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier independently scores each workflow artifact. For the scored step, the verifier recomputes the Purdy model curve using the same parameters and compares it to your submitted CSV file. The reward is based on how closely your computed ΔG_dis values match the reference curve, both in overall magnitude and in the shape (e.g., the position and height of the dissipation peak). Reporting a curve you know to be correct is not sufficient – the verifier will recompute and quantify the agreement, and the reward degrades as the discrepancy increases. The final reward is a weighted combination of the scores from all scored steps.
