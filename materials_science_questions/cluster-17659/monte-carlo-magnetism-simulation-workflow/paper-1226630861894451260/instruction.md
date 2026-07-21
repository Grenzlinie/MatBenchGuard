# 4d Heisenberg spin glass Monte Carlo simulation and finite-size scaling

## Problem background
The lower critical dimension of short-range spin glasses – whether a system orders at a finite temperature – remains controversial. For the four-dimensional isotropic Heisenberg spin glass with Gaussian nearest‑neighbour interactions, earlier numerical work gave no clear answer. Monte Carlo simulations on small hypercubic lattices, combined with finite‑size scaling, can probe the existence of a finite-temperature phase transition and, if present, determine the critical temperature and the correlation‑length and anomalous‑dimension exponents.

## Approach
We study the classical Heisenberg spin glass on four‑dimensional hypercubic lattices with periodic boundary conditions. The quenched couplings are independent standard Gaussian random variables. To overcome the slow dynamics, the simulation employs the **two‑replica Simulated Tempering** algorithm: the inverse temperature becomes a dynamical variable that jumps between a fixed grid of values, allowing the system to explore phase space efficiently. The replica overlap gives access to the spin‑glass susceptibility χ_SG and the dimensionless Binder parameter g. Finite‑size scaling relates the lattice‑size dependence of χ_SG and g to the critical temperature T_c, the correlation‑length exponent ν and the anomalous dimension η: near criticality χ_SG scales as L^{2−η} times a function of (T−T_c)L^{1/ν}, while g is a function of the same scaled variable. By simulating three system sizes (L=3,4,5) with a prescribed number of disorder samples at each size, we obtain disorder‑averaged χ_SG(L,T) and g(L,T). A two‑stage fitting procedure then extracts T_c, ν, η from the scaling forms, separating fits based on the susceptibility data and on the Binder parameter data.

## Reproduction target
Run the two‑replica Simulated Tempering Monte Carlo simulations for lattices of linear size L = 3, 4, 5 with the disorder‑sample counts (400, 200, 100) and the temperature grids specified in the workflow steps. Compute the disorder‑averaged spin‑glass susceptibility χ_SG(L,T) and Binder parameter g(L,T) at each temperature, with error estimates. Record the complete data table in `observed_data.json`. Then perform finite‑size scaling fits: one fit using the χ_SG data to obtain a set of critical parameters {T_c, ν, η}, and a second fit using the g data to obtain {T_c, ν}. Report all fitted values and their errors in `fitted_parameters.json`.

## Assets

- NumPy: https://numpy.org/
- SciPy: https://scipy.org/
- Matplotlib: https://matplotlib.org/

## Workflow steps

### Step 1: Generate disorder realizations
- Role: process
- Action: For each lattice size L=3,4,5, create the required number of disorder samples (400, 200, 100) of nearest‑neighbour couplings J_ij on a 4‑dimensional hypercubic lattice with periodic boundary conditions, drawn from a standard normal distribution N(0,1).
- Evidence: `/app/outputs/disorder_log.txt`

### Step 2: Monte Carlo Simulated Tempering simulations
- Role: process
- Action: For each disorder sample and each L, run the two‑replica Simulated Tempering algorithm with the prescribed temperature grids (ΔT=0.1 for L=3, ΔT=0.05 for L=4,5; n_T=7 or 8). Perform initial slow cooling, iterative weight tuning, thermalization, and final measurement runs. Record the spin configurations and energies needed to compute replica overlaps.
- Evidence: `/app/outputs/simulation_report.txt`

### Step 3: Compute spin glass susceptibility and Binder parameter
- Role: scored (load-bearing)
- Action: From the measurement trajectories, compute the disorder‑averaged spin glass susceptibility χ_SG(L,T) and the Binder parameter g(L,T) for every temperature and lattice size. Estimate statistical errors. Write the results to observed_data.json.
- Output file: `/app/outputs/observed_data.json`
- Format: json
- Contract: JSON object with keys 'L3', 'L4', 'L5'. Each value is an array of objects: {'T': float, 'chi_SG': float, 'chi_SG_err': float, 'g': float, 'g_err': float}.
- Scoring: scored by hidden verifier

### Step 4: Finite-size scaling and critical parameter extraction
- Role: scored
- Action: Perform finite‑size scaling fits of the χ_SG(L,T) data and the g(L,T) data to extract the critical temperature Tc, the exponent ν, and the anomalous dimension η. Produce two sets of parameters: one from the χ_SG scaling, one from the Binder parameter scaling. Save the fitted parameters and their estimated errors in fitted_parameters.json.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: JSON object with keys: 'Tc_chi', 'Tc_chi_err', 'nu_chi', 'nu_chi_err', 'eta_chi', 'eta_chi_err', 'Tc_g', 'Tc_g_err', 'nu_g', 'nu_g_err'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/observed_data.json`
- `/app/outputs/fitted_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### observed_data.json
- path: `/app/outputs/observed_data.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Disorder-averaged spin glass susceptibility and Binder parameter for each lattice size and temperature. The checker uses this data to independently recompute critical parameters.
- schema:
  - `type`: object
  - `required`:
    - `L3`: array
    - `L4`: array
    - `L5`: array
  - `items`:
    - `type`: object
    - `required`: `T`, `chi_SG`, `chi_SG_err`, `g`, `g_err`
    - `properties`:
      - `T`:
        - `type`: number
        - `unit`: dimensionless temperature
      - `chi_SG`:
        - `type`: number
      - `chi_SG_err`:
        - `type`: number
      - `g`:
        - `type`: number
      - `g_err`:
        - `type`: number

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent‑reported fitted critical parameters from finite‑size scaling. The hidden checker independently refits from observed_data.json and compares its own result to the paper’s published values; this file is required to show the scaling analysis was performed.
- schema:
  - `type`: object
  - `required`: `Tc_chi`, `Tc_chi_err`, `nu_chi`, `nu_chi_err`, `eta_chi`, `eta_chi_err`, `Tc_g`, `Tc_g_err`, `nu_g`, `nu_g_err`
  - `properties`:
    - `Tc_chi`:
      - `type`: number
    - `Tc_chi_err`:
      - `type`: number
    - `nu_chi`:
      - `type`: number
    - `nu_chi_err`:
      - `type`: number
    - `eta_chi`:
      - `type`: number
    - `eta_chi_err`:
      - `type`: number
    - `Tc_g`:
      - `type`: number
    - `Tc_g_err`:
      - `type`: number
    - `nu_g`:
      - `type`: number
    - `nu_g_err`:
      - `type`: number

Notes: The hidden checker performs its own finite‑size scaling fit using the agent’s observed_data.json and compares the resulting Tc, ν, η to the paper’s published values (hidden gold). The agent must still produce fitted_parameters.json as evidence of completing the analysis; the checker verifies its existence and structural integrity.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "observed_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "L3": "array",
          "L4": "array",
          "L5": "array"
        },
        "items": {
          "type": "object",
          "required": [
            "T",
            "chi_SG",
            "chi_SG_err",
            "g",
            "g_err"
          ],
          "properties": {
            "T": {
              "type": "number",
              "unit": "dimensionless temperature"
            },
            "chi_SG": {
              "type": "number"
            },
            "chi_SG_err": {
              "type": "number"
            },
            "g": {
              "type": "number"
            },
            "g_err": {
              "type": "number"
            }
          }
        }
      },
      "description": "Disorder-averaged spin glass susceptibility and Binder parameter for each lattice size and temperature. The checker uses this data to independently recompute critical parameters."
    },
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": [
          "Tc_chi",
          "Tc_chi_err",
          "nu_chi",
          "nu_chi_err",
          "eta_chi",
          "eta_chi_err",
          "Tc_g",
          "Tc_g_err",
          "nu_g",
          "nu_g_err"
        ],
        "properties": {
          "Tc_chi": {
            "type": "number"
          },
          "Tc_chi_err": {
            "type": "number"
          },
          "nu_chi": {
            "type": "number"
          },
          "nu_chi_err": {
            "type": "number"
          },
          "eta_chi": {
            "type": "number"
          },
          "eta_chi_err": {
            "type": "number"
          },
          "Tc_g": {
            "type": "number"
          },
          "Tc_g_err": {
            "type": "number"
          },
          "nu_g": {
            "type": "number"
          },
          "nu_g_err": {
            "type": "number"
          }
        }
      },
      "description": "Agent‑reported fitted critical parameters from finite‑size scaling. The hidden checker independently refits from observed_data.json and compares its own result to the paper’s published values; this file is required to show the scaling analysis was performed."
    }
  ],
  "notes": "The hidden checker performs its own finite‑size scaling fit using the agent’s observed_data.json and compares the resulting Tc, ν, η to the paper’s published values (hidden gold). The agent must still produce fitted_parameters.json as evidence of completing the analysis; the checker verifies its existence and structural integrity."
}
```

## How you are scored
A hidden verifier checks your submitted artifacts. For `observed_data.json`, it performs structural and consistency audits (proper format, monotonicity, scaling collapse sanity). For the critical parameters, the verifier **independently re‑fits** the scaling forms from your raw χ_SG and g data and compares its own fitted values to a hidden reference. The structure of `fitted_parameters.json` is also validated. Each scored stage contributes a weighted share to the final reward; a correct reproduction that produces consistent raw data and properly executed scaling fits earns high credit.
