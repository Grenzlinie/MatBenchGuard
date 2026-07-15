# Optimization of gas-cooled Peltier current leads

## Problem background
In superconducting magnet systems, current leads are a major source of parasitic heat leak. One strategy to reduce this heat leak is to insert a thermoelectric (TE) element at the warm end of a copper lead, forming a Peltier current lead (PCL). This work considers a nitrogen-gas-cooled PCL where convective cooling by evaporated gas acts on both the Cu lead and the TE element. Analytical temperature distributions are derived from the governing heat-balance equations, and the design is optimized by selecting the dimensionless geometric parameters Z1 (for the Cu segment) and Z2 (for the TE segment) that minimize the heat leak per unit current, q. The task is to determine the optimal Z1, Z2 and the resulting performance figures—junction temperature, net and total input power, and heat-leak reduction relative to an all-Cu lead—for a range of gas-cooling efficiencies.

## Approach
The current lead is modelled as a one-dimensional heat conduction problem with Joule heating and convective cooling. The Cu lead obeys the Wiedemann-Franz law, and the TE element is described by constant average properties at 250 K. The governing equations for each segment reduce to linear ordinary differential equations whose solutions give temperature profiles expressed in terms of Z1, Z2, and the boundary conditions. Under the condition of minimum heat leak, the temperature gradient at the warm end of the lead is zero, which closes the problem and yields an expression for the heat leak q as a function of Z1 and Z2. A further constraint—continuity of heat flow at the Cu-TE junction—links Z1 and Z2, turning the design into a constrained optimization: find Z1 and Z2 that minimize q for a given gas-cooling efficiency f. The optimization is performed for f = 0, 0.2, 0.4, 0.6, 0.8, 1.0 for both the PCL and a conventional all-Cu lead. From the optimal parameters, the junction temperature Tj, net input power p_net, total input power p_tot, and the percentage reduction t are computed. In a second step, the optimal Z1, Z2 and Tj are used to build the temperature profiles along the normalized coordinate (with the Cu abscissa shifted left by one unit) at the two extreme cooling efficiencies f=0 and f=1. All required physical constants (Lorenz number, TE properties, nitrogen gas specific heat and latent heat, operating temperatures 77 K and 300 K) are provided.

## Reproduction target
For each gas-cooling efficiency f in {0, 0.2, 0.4, 0.6, 0.8, 1.0}, solve the constrained optimization to find the optimal dimensionless geometric parameters Z1 (and Z2 for the PCL) that minimize the heat leak per unit current. Report the corresponding junction temperature Tj, net input power p_net, total input power p_tot, and the percentage reduction t of the heat leak relative to the all-Cu lead. Produce a CSV table with one row per f value containing all quantities for both lead types. Additionally, using the optimal Z1, Z2 and Tj from the first step, compute the temperature distribution along the normalized coordinate for the PCL and the all-Cu lead at f=0 and f=1. The normalized coordinate for the Cu segment must be shifted left by one unit. The delivered temperature profiles must be self-consistent: the junction temperature at the interface should match the reported Tj, and the heat-leak reduction percentages must be consistent with the computed q values.

## Assets

- Physical constants and material properties

## Workflow steps

### Step 1: Optimal design parameter sweep
- Role: scored (load-bearing)
- Action: For each gas‑cooling efficiency f in {0, 0.2, 0.4, 0.6, 0.8, 1.0}, solve the constrained heat‑leak equations for the PCL and the all‑Cu lead. Find the optimal dimensionless geometric parameters Z1 (and Z2 for PCL) that minimize the heat leak per unit current q, and compute the corresponding junction temperature Tj, net input power p_net, total input power p_tot, and the heat‑leak reduction percentage t relative to the all‑Cu lead. All constants (L0, M0, η, Cp, CL, Tc=77 K, Tr=300 K) must be taken from the paper.
- Output file: `/app/outputs/optimal_parameters.csv`
- Format: csv
- Contract: Columns: f (float), Z1_PCL (float), Z2_PCL (float), Tj_PCL (float), q_PCL (float), p_net_PCL (float), p_tot_PCL (float), Z1_Cu (float), q_Cu (float), p_net_Cu (float), p_tot_Cu (float), t (float, heat‑leak reduction %). One row per f.
- Scoring: scored by hidden verifier

### Step 2: Temperature profile generation
- Role: scored
- Action: Using the optimal Z1, Z2 and Tj from step_01, compute the temperature distribution along the normalized coordinate for the PCL and the all‑Cu lead at f=0 and f=1, following the analytical temperature formulas for the Cu segment and the TE element. Normalize the abscissa such that the Cu segment is shifted left by 1 unit (as in the paper's Fig. 4).
- Output file: `/app/outputs/temperature_profiles.csv`
- Format: csv
- Contract: Columns: f (integer, 0 or 1), lead_type (string, 'PCL' or 'Cu'), normalized_position (float), temperature_K (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/optimal_parameters.csv`
- `/app/outputs/temperature_profiles.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### optimal_parameters.csv
- path: `/app/outputs/optimal_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimal geometry and performance for gas‑cooled PCL and all‑Cu leads at f = 0, 0.2, 0.4, 0.6, 0.8, 1.0. Each row corresponds to one f value. Values are compared against reference values from the paper within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `f`, `Z1_PCL`, `Z2_PCL`, `Tj_PCL`, `q_PCL`, `p_net_PCL`, `p_tot_PCL`, `Z1_Cu`, `q_Cu`, `p_net_Cu`, `p_tot_Cu`, `t`
  - `units`:
    - `Z1_PCL`: V^{-1}K
    - `Z2_PCL`: V^{-1}K
    - `Tj_PCL`: K
    - `q_PCL`: mWA^{-1}
    - `p_net_PCL`: mWA^{-1}
    - `p_tot_PCL`: mWA^{-1}
    - `Z1_Cu`: V^{-1}K
    - `q_Cu`: mWA^{-1}
    - `p_net_Cu`: mWA^{-1}
    - `p_tot_Cu`: mWA^{-1}
    - `t`: %

### temperature_profiles.csv
- path: `/app/outputs/temperature_profiles.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature profiles along the normalized coordinate for PCL and all‑Cu leads at f=0 and f=1 under optimal conditions. The checker recomputes expected temperatures from the optimal parameters and compares them to the submitted values.
- schema:
  - `type`: table
  - `required_columns`: `f`, `lead_type`, `normalized_position`, `temperature_K`
  - `units`:
    - `normalized_position`: dimensionless
    - `temperature_K`: K

Notes: All constants are from the paper; the agent must implement the constrained heat‑leak equations (including the implicit equation for the gas‑cooled PCL) and the analytical temperature formulas.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "optimal_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "Z1_PCL",
          "Z2_PCL",
          "Tj_PCL",
          "q_PCL",
          "p_net_PCL",
          "p_tot_PCL",
          "Z1_Cu",
          "q_Cu",
          "p_net_Cu",
          "p_tot_Cu",
          "t"
        ],
        "units": {
          "Z1_PCL": "V^{-1}K",
          "Z2_PCL": "V^{-1}K",
          "Tj_PCL": "K",
          "q_PCL": "mWA^{-1}",
          "p_net_PCL": "mWA^{-1}",
          "p_tot_PCL": "mWA^{-1}",
          "Z1_Cu": "V^{-1}K",
          "q_Cu": "mWA^{-1}",
          "p_net_Cu": "mWA^{-1}",
          "p_tot_Cu": "mWA^{-1}",
          "t": "%"
        }
      },
      "description": "Optimal geometry and performance for gas‑cooled PCL and all‑Cu leads at f = 0, 0.2, 0.4, 0.6, 0.8, 1.0. Each row corresponds to one f value. Values are compared against reference values from the paper within tolerances."
    },
    {
      "file": "temperature_profiles.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "lead_type",
          "normalized_position",
          "temperature_K"
        ],
        "units": {
          "normalized_position": "dimensionless",
          "temperature_K": "K"
        }
      },
      "description": "Temperature profiles along the normalized coordinate for PCL and all‑Cu leads at f=0 and f=1 under optimal conditions. The checker recomputes expected temperatures from the optimal parameters and compares them to the submitted values."
    }
  ],
  "notes": "All constants are from the paper; the agent must implement the constrained heat‑leak equations (including the implicit equation for the gas‑cooled PCL) and the analytical temperature formulas."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output artifact. The optimal parameters table is compared against hidden reference values with appropriate tolerances; the temperature profiles are checked by recomputing expected temperatures from the reported optimal parameters and by verifying profile monotonicity. The verifier also confirms that the reduction percentages are consistent with the heat-leak values and that the junction temperature derived from the profiles matches the reported Tj. The rewards from the two stages are combined by weight to produce the final score. Reporting numbers alone is not sufficient—the artifacts must be self-consistent and correct under the hidden checks.
