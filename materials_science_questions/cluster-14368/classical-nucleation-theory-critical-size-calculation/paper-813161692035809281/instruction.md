# Surface Energy Evolution Effects in Gas Antisolvent Precipitation Simulations

## Problem background
Gas antisolvent precipitation (GASP) is a pharmaceutical particle size‑reduction technique in which a compressed antisolvent (usually CO₂) is contacted with an API‑loaded organic solvent droplet, causing the API to precipitate as a fine powder. Classical nucleation theory (CNT) is often used to predict particle birth rates, but it requires the solid–liquid interfacial energy γ, which is typically assumed constant. In GASP, the effective interfacial energy may evolve as the antisolvent dissolves into the droplet because the local environment of the growing crystal changes. This study investigates how using an evolving surface energy, estimated via a Nielsen–Sohnel–Mersmann (NSM) correlation based on the saturation composition, affects the predicted particle yield, mean size, and crystal size distribution compared to assuming that γ remains at its initial value.

## Approach
A well‑mixed single‑droplet model is employed for an isobaric, isothermal CO₂ uptake into a toluene droplet containing phenanthrene. The thermodynamics of the CO₂–toluene–phenanthrene mixture is described by the Peng–Robinson equation of state. Molar balance equations track the mole numbers of each component as the droplet expands, while a population balance equation tracks the particle number density distribution n(v,t). Particle birth is modeled by classical nucleation theory, and particle growth follows a GKO‑corrected growth law with an overall incorporation probability. Two simulations are performed: one with the dimensionless surface energy Γ held constant at its initial value, and one with Γ evolving according to the NSM correlation that links Γ to the API saturation number density. The population balance is solved using the method of characteristics together with a perturbation scheme that treats growth as a small correction. The output of the simulations includes time histories of the precipitated API volume fraction, the fraction of API precipitated, the critical nucleation volume, and the full particle size distribution.

## Reproduction target
Produce three CSV files recording the simulation results for both surface‑energy treatments:
- `precipitate_fraction.csv`: time history of precipitated API volume fraction φ_p and fraction of API precipitated ξ over dimensionless time t/t_AS (0 to 0.2).
- `sauter_spread.csv`: time history of dimensionless Sauter mean diameter (SMD/d_ref) and the relative diameter spread (σ/SMD) over the same time interval.
- `csd_snapshots.csv`: dimensionless crystal size distribution (number density w·f as a function of dimensionless particle volume w) at t/t_AS = 0.1, 0.15, and 0.2.
Each file must contain columns for both the constant‑Γ and variable‑Γ cases, following the schemas given in the workflow steps. The target is to compute these quantities by faithfully implementing the model and running the two simulation scenarios.

## Assets

- Peng-Robinson equation of state implementation: open-source thermodynamics library (e.g., CoolProp, thermo) or own implementation

## Workflow steps

### Step 1: Implement Peng–Robinson EOS and thermodynamic properties
- Role: process
- Action: Implement the Peng–Robinson equation of state for the CO₂–toluene–phenanthrene system using the pure component data and binary interaction parameters provided in the paper (Table 1, Eq. 5). Use it to compute molar volume V(x,p,T) and saturation mole fractions as functions of composition, pressure, and temperature. This step provides the thermodynamic closure needed for the droplet model.
- Evidence: `/app/outputs/eos_validation.txt`

### Step 2: Run WMD simulation for constant and variable surface energy
- Role: process
- Action: Solve the coupled molar balance ODEs and population balance PDE (Eqs. 7–12 of the paper) using the method of characteristics with a perturbation scheme. Run two complete simulations: one with constant dimensionless surface energy Γ (equal to the initial value at t=0) and one with Γ evolving according to the NSM correlation (Eq. 1). Use the GKO‑corrected growth law with n=2, k_G=1×10⁻⁴, and t_AS=0.0056 ms. Record the time series of precipitated API volume fraction φ_p(t), API precipitated fraction ξ(t), critical volume v*(t), and the particle number density distribution n(v,t) for both cases.
- Evidence: `/app/outputs/simulation_state.npz`

### Step 3: Generate precipitate fraction CSV
- Role: scored (load-bearing)
- Action: From the simulation results, extract φ_p(t) and ξ(t) for both constant‑Γ and variable‑Γ cases over dimensionless time t/t_AS from 0 to 0.2. Save the data to CSV with columns: t_over_tAS, phi_p_const, phi_p_var, xi_const, xi_var.
- Output file: `/app/outputs/precipitate_fraction.csv`
- Format: csv
- Contract: Columns: t_over_tAS, phi_p_const, phi_p_var, xi_const, xi_var
- Scoring: scored by hidden verifier

### Step 4: Generate Sauter mean diameter and spread CSV
- Role: scored
- Action: From the simulation results compute the dimensionless Sauter mean diameter (SMD/d_ref) and the relative diameter spread (σ/SMD) for both constant‑Γ and variable‑Γ cases at the same time points as in step_03. Save to CSV with columns: t_over_tAS, SMD_norm_const, SMD_norm_var, sigma_over_SMD_const, sigma_over_SMD_var.
- Output file: `/app/outputs/sauter_spread.csv`
- Format: csv
- Contract: Columns: t_over_tAS, SMD_norm_const, SMD_norm_var, sigma_over_SMD_const, sigma_over_SMD_var
- Scoring: scored by hidden verifier

### Step 5: Generate crystal size distribution snapshots CSV
- Role: scored
- Action: From the simulation results extract the dimensionless number density distribution w·f as a function of dimensionless particle volume w at three times: t/t_AS = 0.1, 0.15, 0.2, for both constant‑Γ and variable‑Γ cases. Save to CSV with columns: w, wf_const_t01, wf_var_t01, wf_const_t015, wf_var_t015, wf_const_t02, wf_var_t02.
- Output file: `/app/outputs/csd_snapshots.csv`
- Format: csv
- Contract: Columns: w, wf_const_t01, wf_var_t01, wf_const_t015, wf_var_t015, wf_const_t02, wf_var_t02
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/precipitate_fraction.csv`
- `/app/outputs/sauter_spread.csv`
- `/app/outputs/csd_snapshots.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### precipitate_fraction.csv
- path: `/app/outputs/precipitate_fraction.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time history of precipitated API volume fraction and fraction of API precipitated for constant and variable surface energy cases.
- schema:
  - `type`: table
  - `required_columns`: `t_over_tAS`, `phi_p_const`, `phi_p_var`, `xi_const`, `xi_var`
  - `units`:
    - `t_over_tAS`: dimensionless
    - `phi_p_const`: dimensionless
    - `phi_p_var`: dimensionless
    - `xi_const`: dimensionless
    - `xi_var`: dimensionless

### sauter_spread.csv
- path: `/app/outputs/sauter_spread.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time history of dimensionless Sauter mean diameter and relative spread for constant and variable surface energy cases.
- schema:
  - `type`: table
  - `required_columns`: `t_over_tAS`, `SMD_norm_const`, `SMD_norm_var`, `sigma_over_SMD_const`, `sigma_over_SMD_var`
  - `units`:
    - `t_over_tAS`: dimensionless
    - `SMD_norm_const`: dimensionless
    - `SMD_norm_var`: dimensionless
    - `sigma_over_SMD_const`: dimensionless
    - `sigma_over_SMD_var`: dimensionless

### csd_snapshots.csv
- path: `/app/outputs/csd_snapshots.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Crystal size distribution snapshots (dimensionless number density w·f vs. dimensionless volume w) at t/t_AS = 0.1, 0.15, 0.2 for constant and variable surface energy cases.
- schema:
  - `type`: table
  - `required_columns`: `w`, `wf_const_t01`, `wf_var_t01`, `wf_const_t015`, `wf_var_t015`, `wf_const_t02`, `wf_var_t02`
  - `units`:
    - `w`: dimensionless
    - `wf_const_t01`: dimensionless
    - `wf_var_t01`: dimensionless
    - `wf_const_t015`: dimensionless
    - `wf_var_t015`: dimensionless
    - `wf_const_t02`: dimensionless
    - `wf_var_t02`: dimensionless

Notes: The hidden checker will compare these curves to digitized gold from the paper's Figures 3–5 using tolerances that allow for toolchain variation. Monotonic ordering and peak locations are also verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "precipitate_fraction.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "t_over_tAS",
          "phi_p_const",
          "phi_p_var",
          "xi_const",
          "xi_var"
        ],
        "units": {
          "t_over_tAS": "dimensionless",
          "phi_p_const": "dimensionless",
          "phi_p_var": "dimensionless",
          "xi_const": "dimensionless",
          "xi_var": "dimensionless"
        }
      },
      "description": "Time history of precipitated API volume fraction and fraction of API precipitated for constant and variable surface energy cases."
    },
    {
      "file": "sauter_spread.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "t_over_tAS",
          "SMD_norm_const",
          "SMD_norm_var",
          "sigma_over_SMD_const",
          "sigma_over_SMD_var"
        ],
        "units": {
          "t_over_tAS": "dimensionless",
          "SMD_norm_const": "dimensionless",
          "SMD_norm_var": "dimensionless",
          "sigma_over_SMD_const": "dimensionless",
          "sigma_over_SMD_var": "dimensionless"
        }
      },
      "description": "Time history of dimensionless Sauter mean diameter and relative spread for constant and variable surface energy cases."
    },
    {
      "file": "csd_snapshots.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "w",
          "wf_const_t01",
          "wf_var_t01",
          "wf_const_t015",
          "wf_var_t015",
          "wf_const_t02",
          "wf_var_t02"
        ],
        "units": {
          "w": "dimensionless",
          "wf_const_t01": "dimensionless",
          "wf_var_t01": "dimensionless",
          "wf_const_t015": "dimensionless",
          "wf_var_t015": "dimensionless",
          "wf_const_t02": "dimensionless",
          "wf_var_t02": "dimensionless"
        }
      },
      "description": "Crystal size distribution snapshots (dimensionless number density w·f vs. dimensionless volume w) at t/t_AS = 0.1, 0.15, 0.2 for constant and variable surface energy cases."
    }
  ],
  "notes": "The hidden checker will compare these curves to digitized gold from the paper's Figures 3–5 using tolerances that allow for toolchain variation. Monotonic ordering and peak locations are also verified."
}
```

## How you are scored
A hidden automatic verifier independently checks each artifact. The verifier compares your output curves against reference data derived from the original study, with tolerances that allow for differences in implementation. Scoring rewards correct physical trends (for example, the expected relative ordering of the constant‑ and variable‑surface‑energy curves) as well as quantitative agreement of the time‑series values. Each scored CSV contributes a portion of the total reward; the final score is the weighted sum across all artifacts.
