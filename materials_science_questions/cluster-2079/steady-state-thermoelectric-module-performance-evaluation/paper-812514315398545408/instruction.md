# Steady-state TE module: PV-TERs coupling and optimization

## Problem background
This work proposes a system that couples a photovoltaic (PV) panel with thermoelectric refrigerators (TERs) to achieve solar-driven cooling. The coupled electrical and thermal interactions are modeled via energy balance and diode equations, incorporating temperature‑dependent material properties and finite‑rate heat transfer. The goal is to determine the operating point (coupling voltage/current) where the PV output powers the TER, and to optimize the system’s overall energy conversion efficiency by tuning the TER number and structure parameter, as well as by varying solar irradiance.

## Approach
Implement the coupled PV-TERs numerical model. For the PV panel, solve an energy balance equation (accounting for convection and radiation to the environment) to obtain the panel temperature as a function of output voltage. Then compute the current using a single‑diode equivalent circuit model with temperature‑dependent photo‑current and reverse saturation current. For the TERs, model a stack of thermoelectric modules using heat flow equations that include Peltier, Joule, and conductive terms, coupled with Newton cooling boundary conditions at the hot and cold sides. Material properties (Seebeck coefficient, resistivity, thermal conductivity) are evaluated from empirical polynomials that depend on the average junction temperature. The coupling point is found by solving for the voltage and current where the PV and TER I‑V curves intersect. Efficiency is computed from the electrical power and the solar irradiance. Optimizations are performed by sweeping over TER number N and structure parameter β (which controls internal resistance and thermal conductance) to maximize efficiency, and then by sweeping over solar irradiance G while re‑optimizing N and β at each G to find the global maximum efficiency.

## Reproduction target
Compute the following:

1.  For the baseline parameters (G = 200 W/m², cold‑reservoir temperature T_L = 290 K, hot‑reservoir temperature T_H = 310 K, diode ideal factor m = 1, heat transfer coefficients U_H = U_L = 1000 W/m²K, thermocouples per TER n_T = 127, PV series cell count n_PV = 60, TER count N = 5, structure parameter β = 1.00×10⁻³ m), determine the coupling point (voltage V_CP, current I_CP, cold‑side junction temperature T1_CP, hot‑side junction temperature T2_CP) and the overall energy conversion efficiency η.

2.  Vary N from 1 to 10 and β over a grid spanning at least 0.5×10⁻³ m to 2.0×10⁻³ m. For each (N, β) find the coupling point and efficiency. Report the maximum efficiency η_opt and the corresponding optimal N_opt, β_opt, V_opt, I_opt.

3.  Sweep the solar irradiance G from 10 to 1000 W/m². For each G, carry out the N‑β optimization as in (2) to find the optimal efficiency η_opt(G). Report the global maximum efficiency η_max over all G and the irradiance G_η at which it occurs.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute PV panel I-V curve
- Role: process
- Action: Using the reference parameter set (G=200 W/m², n_PV=60, m=1, A_PV=1.6434 m², U_PV=5 W/m²K, PV panel electrical parameters from the datasheet), numerically solve the PV panel energy balance equation to obtain T_PV(V) for each voltage V in a suitable range. Then compute the PV current I_PV(V) using the diode equation with temperature-dependent photo-current and reverse saturation current. Save the resulting I-V curve.
- Evidence: `/app/outputs/pv_iv.csv`

### Step 2: Compute TER I-V curve and junction temperatures
- Role: process
- Action: Using the baseline parameters (N=5, n_T=127, β=1.00e-3 m, U_H=U_L=1000 W/m²K, A_H/L=3.6e-3 m² per TER, material property polynomials for Seebeck coefficient, resistivity, and thermal conductivity), solve the TER heat flow equations together with Newton cooling boundary conditions to obtain T1(I) and T2(I) for a range of TER currents I. Then compute the TER input voltage V_TERs(I) from the power balance. Save the I-V and temperature data.
- Evidence: `/app/outputs/ter_iv.csv`

### Step 3: Determine coupling point and overall efficiency
- Role: scored (load-bearing)
- Action: Read pv_iv.csv and ter_iv.csv. Numerically find the intersection (V_CP, I_CP) where the two I-V curves cross (V_PV = V_TERs, I_PV = I_TERs). Extract T1_CP and T2_CP from the TER data at I=I_CP. Compute the overall efficiency η from the electrical powers, solar irradiance, and PV front area. Write the results to step_01_coupling.json.
- Output file: `/app/outputs/step_01_coupling.json`
- Format: json
- Contract: JSON object with keys: V_CP (float), I_CP (float), T1_CP (float), T2_CP (float), eta (float)
- Scoring: scored by hidden verifier

### Step 4: Sweep TER number N and structure parameter β
- Role: process
- Action: Repeat the TER I-V curve computation (step 2) for a grid of N values (1,2,…,10) and β values (grid spanning at least 0.5e-3 m to 2.0e-3 m). For each (N,β), recompute the coupling point with the fixed PV I-V curve and calculate the efficiency η. Store the results (N, β, V_CP, I_CP, T1_CP, T2_CP, η) in optimization_grid.csv.
- Evidence: `/app/outputs/optimization_grid.csv`

### Step 5: Identify optimal parameters from N-β sweep
- Role: scored
- Action: Read optimization_grid.csv. Find the combination (N_opt, β_opt) that gives the maximum η (η_opt) and record the corresponding coupling values V_opt, I_opt. Write these results to step_02_optimal.json.
- Output file: `/app/outputs/step_02_optimal.json`
- Format: json
- Contract: JSON object with keys: eta_opt (float), beta_opt (float), N_opt (int), V_opt (float), I_opt (float)
- Scoring: scored by hidden verifier

### Step 6: Sweep solar irradiance G and optimize for each G
- Role: process
- Action: For a range of G values (10 to 1000 W/m²), for each G recompute the PV I-V curve (since T_PV depends on G) and then perform the N-β optimization (as in step 4) to obtain the maximum efficiency η_opt(G) and the corresponding optimal β, N, V_opt, I_opt, and cooling heat flow Q_L,opt. Save the optimal metrics for each G in G_sweep.csv.
- Evidence: `/app/outputs/G_sweep.csv`

### Step 7: Determine global maximum efficiency over G
- Role: scored
- Action: Read G_sweep.csv. Find the absolute maximum of η_opt(G) (η_max) and the corresponding irradiance G_η. Write the result to step_03_maximum.json.
- Output file: `/app/outputs/step_03_maximum.json`
- Format: json
- Contract: JSON object with keys: eta_max (float), G_eta (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_coupling.json`
- `/app/outputs/step_02_optimal.json`
- `/app/outputs/step_03_maximum.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_coupling.json
- path: `/app/outputs/step_01_coupling.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Baseline coupling point and overall efficiency for the reference parameter set.
- schema:
  - `type`: object
  - `required`:
    - `V_CP`: float
    - `I_CP`: float
    - `T1_CP`: float
    - `T2_CP`: float
    - `eta`: float

### step_02_optimal.json
- path: `/app/outputs/step_02_optimal.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Optimal efficiency and corresponding parameters from the N-β sweep.
- schema:
  - `type`: object
  - `required`:
    - `eta_opt`: float
    - `beta_opt`: float
    - `N_opt`: int
    - `V_opt`: float
    - `I_opt`: float

### step_03_maximum.json
- path: `/app/outputs/step_03_maximum.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Global maximum efficiency and the irradiance at which it occurs.
- schema:
  - `type`: object
  - `required`:
    - `eta_max`: float
    - `G_eta`: float

Notes: The hidden checker will recompute the coupling point from the agent's raw I‑V curves (pv_iv.csv, ter_iv.csv) and verify the reported values against the paper's published numbers with appropriate tolerances. Similarly, the optimal and maximum values will be cross-checked against the sweep grids (optimization_grid.csv, G_sweep.csv). Structural consistency (e.g., η_opt > η, η_max ≥ η_opt) is also enforced.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_coupling.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "V_CP": "float",
          "I_CP": "float",
          "T1_CP": "float",
          "T2_CP": "float",
          "eta": "float"
        }
      },
      "description": "Baseline coupling point and overall efficiency for the reference parameter set."
    },
    {
      "file": "step_02_optimal.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "eta_opt": "float",
          "beta_opt": "float",
          "N_opt": "int",
          "V_opt": "float",
          "I_opt": "float"
        }
      },
      "description": "Optimal efficiency and corresponding parameters from the N-β sweep."
    },
    {
      "file": "step_03_maximum.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "eta_max": "float",
          "G_eta": "float"
        }
      },
      "description": "Global maximum efficiency and the irradiance at which it occurs."
    }
  ],
  "notes": "The hidden checker will recompute the coupling point from the agent's raw I‑V curves (pv_iv.csv, ter_iv.csv) and verify the reported values against the paper's published numbers with appropriate tolerances. Similarly, the optimal and maximum values will be cross-checked against the sweep grids (optimization_grid.csv, G_sweep.csv). Structural consistency (e.g., η_opt > η, η_max ≥ η_opt) is also enforced."
}
```

## How you are scored
For each of the three scored stages the hidden verifier will independently inspect the corresponding raw intermediate files (pv_iv.csv, ter_iv.csv, optimization_grid.csv, G_sweep.csv) and recompute the required quantities (coupling point, optimal efficiency, global maximum). It will compare the values you report in the three JSON output files against its own recomputed values and against hidden reference tolerances. Each stage contributes a partial reward, and the final score is the weighted sum. Simply reporting the expected numbers is not sufficient; you must generate the full supporting evidence that allows the verifier to recompute the results.
