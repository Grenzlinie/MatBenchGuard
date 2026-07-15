# Time-dependent Monte Carlo simulation of 2,4‑dinitro‑toluene hydrogenation surface ratios

## Problem background
Catalytic hydrogenation of 2,4-dinitro-toluene (2,4DNT) to 2,4-diamino-toluene on palladium/carbon catalysts is a complex process whose selectivity and activity are sensitive to the catalyst's metal dispersion and the steric hindrance of adsorbed species. A time-dependent Monte Carlo (tdMC) simulation can capture these effects by explicitly modeling the surface as a lattice of metal sites, with different adsorption configurations (fat, hindered-flag, free-flag) each occupying a different number of sites. This task focuses on using such a simulation to compute the relative populations of 2,4DNT in its flag (hindered-flag and free-flag) configurations as a function of metal dispersion, both in the absence and presence of the hydrogenation reaction. The goal is to produce the surface molar ratios that reveal how steric hindrance and metal dispersion interplay.

## Approach
The overall task consists of two stages: first, fitting the tdMC model parameters to experimental kinetic data; second, using the fitted parameters to simulate the surface ratios at different metal dispersions.

**Fitting stage:** The tdMC algorithm is linked to a multi‑parameter minimization routine (e.g. AMOEBA). The target data are the experimental appearance‑disappearance rates of 2,4‑dinitro‑toluene and its derivatives measured at ten times during a hydrogenation run on a Pd/C catalyst with D_x = 0.27 at 323.15 K (see Assets). The parameters to be fitted are the per‑site occurrence probabilities (or equivalent activation energies) for the six elementary events: r‑NO₂, r‑NHOH, d‑NO₂, d‑NHOH, d‑NH₂, d‑Φ, plus the three hitting configuration probabilities (FFC, HFC, FC). The fit minimizes the objective function F = Σ|δ|/Σ|ε|, where δ = simulated − experimental rate and ε = 0.1·|experimental rate|. After convergence the agent has a validated parameter set.

**Simulation stage:** The simulation uses a 100×100 square lattice representing a Pd{100} surface. Metal dispersion D_x is modeled by randomly removing a fraction D_x of sites as gaps. For each D_x value in {0.0, 0.3, 0.6, 0.9}, the agent simulates the surface events (adsorption, desorption, and reaction where applicable) using the *fitted* occurrence probabilities. The three adsorption configurations FC (12 sites), HFC (4 sites), and FFC (3 sites) are assigned the fitted hitting probabilities. The simulation runs until a pseudo‑steady state is reached, then the numbers of 2,4DNT molecules in FFC and HFC configurations are counted. Two quantities are computed: the ratio θ_FFC / θ_HFC and the total fraction of surface covered by flag 2,4DNT, θ_FFC+HFC. Results are recorded for each D_x and condition.

## Reproduction target
Implement the described tdMC simulation and compute the surface molar ratios θ_FFC / θ_HFC and θ_FFC+HFC for metal dispersions D_x = 0.0, 0.3, 0.6, 0.9, under two conditions: (1) absence of hydrogenation, where only adsorption and desorption of 2,4DNT are allowed, and (2) presence of hydrogenation, where reaction events (‑NO₂ → ‑NHOH and ‑NHOH → ‑NH₂) are included. Write the results as a CSV file `surface_ratios.csv` with columns D_x (float), condition (string: 'absence' or 'presence'), theta_FFC_over_HFC (float), and theta_FFC_plus_HFC (float). There will be eight rows of data.

## Assets
No external datasets, pretrained models, or specialized software are required. The simulation and fitting can be implemented in Python 3 with numpy. The experimental target data for the fitting step are provided below as an inline CSV; they consist of the appearance‑disappearance rates (per surface metal site per second, ×10²) of five species at ten reaction times, measured on a Pd/C catalyst with D_x = 0.27 at 323.15 K. Use these values as the reference to fit the tdMC parameters.

```
time_s, r_24DNT, r_HANT, r_4A2NT, r_2A4NT, r_24DAT
0.0,   -42.0,  19.7,  3.28,  1.31,  0.00
1200.0, -42.0,  19.7,  3.28,  0.66,  0.00
2400.0,   0.0,  -5.91,  1.97,  0.66,  1.31
3600.0,   0.0,  -5.91,  1.31,  0.00,  3.94
4800.0,   0.0,  -5.91,  0.66,  0.00,  3.94
6000.0,   0.0,  -5.91,  0.00,  0.66,  6.57
7200.0,   0.0,  -4.60, -1.97, -0.66,  6.57
8400.0,   0.0,  -4.60, -1.97, -0.66,  6.57
9600.0,   0.0,  -1.97, -1.97,  0.00,  6.57
10800.0,  0.0,   0.00, -1.97,  0.00,  6.57
```

r_24DNT: 2,4‑dinitro‑toluene; r_HANT: 4HA2NT + 2HA4NT; r_4A2NT: 4‑amino‑2‑nitro‑toluene; r_2A4NT: 2‑amino‑4‑nitro‑toluene; r_24DAT: 2,4‑diamino‑toluene. Positive values are appearance rates, negative values are disappearance rates. The objective function for fitting is F = Σ|δ| / Σ|ε| with ε = 0.1·|r_exp|.

## Workflow steps

### Step 1: Fit tdMC occurrence probabilities to experimental data
- Role: process
- Action: Use the experimental rate data shown in the Assets section (the ten‑time‑point table for r_24DNT, r_HANT, r_4A2NT, r_2A4NT, r_24DAT at 323.15 K). Implement the time‑dependent Monte Carlo algorithm on a 100×100 square lattice linked to a multi‑parameter minimization routine (e.g., AMOEBA). Initially set the hitting configuration probabilities to FFC=0.45, HFC=0.45, FC=0.10 and compute per‑site event occurrence probabilities from initial activation energy guesses via transition‑state theory (P = exp(‑Ea/(R·T)), R=8.314 J/(mol·K), T=323.15 K), dividing by the numbers of occupied sites (12 for FC, 4 for HFC, 3 for FFC). Run the simulation for each time point, collecting the simulated surface‑event rates, and iteratively adjust the six occurrence probabilities (or corresponding activation energies) and the hitting configuration probabilities to minimize the objective F = Σ|δ|/Σ|ε| with ε = 0.1·|r_exp|. Continue until convergence. Output the final fitted parameter set (per‑site occurrence probabilities at 323.15 K and the hitting probabilities) as a JSON file `fitted_params.json` documenting which values were obtained. This step is not scored but is a prerequisite for the following simulation.
- Evidence: fitted_params.json

### Step 2: Simulate 2,4DNT surface ratios using fitted parameters and output CSV
- Role: scored (load-bearing)
- Action: Using the fitted occurrence probabilities and hitting configuration probabilities produced in Step 1, run the tdMC simulation on a 100×100 square lattice representing a Pd{100} surface. For each metal dispersion D_x in [0.0, 0.3, 0.6, 0.9], randomly remove that fraction of sites as gaps. Simulate two conditions: (i) absence of hydrogenation (only adsorption and desorption of 2,4DNT) and (ii) presence of hydrogenation (include reaction events –NO₂→–NHOH and –NHOH→–NH₂). After each simulation reaches a pseudo‑steady state, count the numbers of 2,4DNT molecules in FFC and HFC configurations and compute the ratio θ_FFC / θ_HFC and the total surface fraction θ_(FFC+HFC). Write the results as a CSV file.
- Output file: `/app/outputs/surface_ratios.csv`
- Format: csv
- Contract: Columns: D_x (float), condition (string: 'absence' or 'presence'), theta_FFC_over_HFC (float), theta_FFC_plus_HFC (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/surface_ratios.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### surface_ratios.csv
- path: `/app/outputs/surface_ratios.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Surface molar ratio parameters for 2,4‑dinitro‑toluene at four metal dispersion values, both in the absence and presence of hydrogenation.
- schema:
  - `type`: table
  - `required_columns`: `D_x`, `condition`, `theta_FFC_over_HFC`, `theta_FFC_plus_HFC`
  - `columns`:
    - `D_x`:
      - `type`: float
      - `description`: metal dispersion fraction
    - `condition`:
      - `type`: string
      - `enum`: `absence`, `presence`
      - `description`: reaction condition: 'absence' (no hydrogenation) or 'presence' (with hydrogenation)
    - `theta_FFC_over_HFC`:
      - `type`: float
      - `description`: ratio of free‑flag to hindered‑flag 2,4DNT surface molar ratio
    - `theta_FFC_plus_HFC`:
      - `type`: float
      - `description`: total fraction of surface covered by flag 2,4DNT (FFC+HFC)

Notes: The agent must re‑implement the tdMC algorithm based on the method description; no external code package beyond a standard programming language and numerical libraries is required. The event probabilities and hitting configuration probabilities are provided as fixed constants in the instruction. The verifier compares each row's computed ratios against hidden reference values (from Table 3 of the paper) using a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "surface_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_x",
          "condition",
          "theta_FFC_over_HFC",
          "theta_FFC_plus_HFC"
        ],
        "columns": {
          "D_x": {
            "type": "float",
            "description": "metal dispersion fraction"
          },
          "condition": {
            "type": "string",
            "enum": [
              "absence",
              "presence"
            ],
            "description": "reaction condition: 'absence' (no hydrogenation) or 'presence' (with hydrogenation)"
          },
          "theta_FFC_over_HFC": {
            "type": "float",
            "description": "ratio of free‑flag to hindered‑flag 2,4DNT surface molar ratio"
          },
          "theta_FFC_plus_HFC": {
            "type": "float",
            "description": "total fraction of surface covered by flag 2,4DNT (FFC+HFC)"
          }
        }
      },
      "description": "Surface molar ratio parameters for 2,4‑dinitro‑toluene at four metal dispersion values, both in the absence and presence of hydrogenation."
    }
  ],
  "notes": "The agent must re‑implement the tdMC algorithm based on the method description; no external code package beyond a standard programming language and numerical libraries is required. The event probabilities and hitting configuration probabilities are provided as fixed constants in the instruction. The verifier compares each row's computed ratios against hidden reference values (from Table 3 of the paper) using a relative tolerance."
}
```

## How you are scored
Your submitted `surface_ratios.csv` will be evaluated by a hidden verifier. For each of the eight (D_x, condition) combinations, the verifier will compare your computed θ_FFC_over_HFC and θ_FFC_plus_HFC values to hidden reference values. The overall score is the fraction of rows for which both computed ratios agree with the reference within a reasonable tolerance (to account for stochastic variability). You must run the simulation and compute these ratios; simply reporting expected numbers without executing the workflow will not suffice. Only this CSV file contributes to your score.
