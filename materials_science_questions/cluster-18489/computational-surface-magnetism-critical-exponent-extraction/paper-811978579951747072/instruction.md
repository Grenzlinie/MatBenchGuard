# Surface Segregation and Magnetization in Binary Alloy Monolayer

## Problem background
In binary alloys with a free surface, surface segregation — the preferential enrichment of one atomic species at the surface — and spontaneous magnetization can co‑exist and influence each other. This task focuses on a simplified model of a dilute magnetic A component in a non‑magnetic B matrix forming a b.c.c. lattice with a smooth (110) surface. The goal is to determine how the equilibrium surface concentration csA depends on bulk concentration cA, surface magnetization μs, and temperature, and to characterize the nature of the magnetic phase transition at the surface.

## Approach
The system is described by a pair of coupled nonlinear equations derived from a mean‑field thermodynamic treatment. The surface layer is treated as a distinct monolayer with interaction parameters scaled by the exchange energy |J_s|. The equations relate surface concentration csA, surface magnetization μs, bulk concentration cA, and reduced temperature τ = kT/|J_s|. Given cA and either μs or τ, one solves the two equations simultaneously for the unknown csA and μs (or for a given μs, solve for csA; for a given τ, solve for μs). The reduced energy parameters are:

Surface monolayer:
    v_AA^(s) = 0.7
    v_BB^(s) = 0.9
    v_AB^(s) = 1.4
    w_s = 1.2

Surface‑volume coupling:
    v'_AA = 0.8
    v'_BB = 1.0
    v'_AB = 1.7
    w' = 1.6

Bulk:
    v_AA = 0.4
    v_BB = 0.8
    v_AB = 1.1
    w = 1.0

Numerical root‑finding (e.g., scipy.optimize.fsolve) is used to obtain the self‑consistent solutions over grids of cA, μs, and τ. The solver data is then post‑processed to extract curves for the three required datasets.

## Reproduction target
Produce three datasets as CSV files, each corresponding to a different cross‑section of the solution space:

1. csA vs cA for fixed μs. Extract surface concentration csA as a function of bulk concentration cA for three fixed surface magnetizations: μs = 0, μs = 0.5, and μs = 1.0. The CSV must have columns: cA, csA_mu0, csA_mu0p5, csA_mu1.

2. csA vs μs for fixed cA. Extract csA as a function of surface magnetization μs (over the range 0 to 1) for four fixed bulk concentrations: cA = 0.001, 0.01, 0.05, 0.1. The CSV must have columns: mu, csA_cA0p001, csA_cA0p01, csA_cA0p05, csA_cA0p1.

3. μs vs τ for fixed cA. Extract surface magnetization μs as a function of reduced temperature τ = kT/|J_s| (τ from 0 to 2) for three fixed bulk concentrations: cA = 0.01, 0.05, 0.1. The CSV must have columns: tau, mu_cA0p01, mu_cA0p05, mu_cA0p1. All quantities are dimensionless.

## Assets

- Python scientific computing libraries (NumPy, SciPy): numpy scipy

## Workflow steps

### Step 1: Solve coupled equilibrium equations
- Role: process
- Action: Implement the simplified equilibrium equations for surface concentration csA and surface magnetization μs using the given reduced energy parameters (v_AA(s)=0.7, v_BB(s)=0.9, v_AB(s)=1.4, w_s=1.2; v'_AA=0.8, v'_BB=1.0, v'_AB=1.7, w'=1.6; v_AA=0.4, v_BB=0.8, v_AB=1.1, w=1.0, all scaled by |J_s|). Solve the coupled nonlinear equations numerically for a grid of bulk concentration cA, surface magnetization μs, and reduced temperature τ = kT/|J_s| using a root-finding method (e.g., scipy.optimize.fsolve). Save the complete solution arrays (cA, μs, csA, τ) into a JSON file for later extraction.
- Evidence: `/app/outputs/solver_data.json`

### Step 2: Extract Fig.1 data: csA vs cA
- Role: scored (load-bearing)
- Action: From the solver data, extract for surface magnetization μs = 0, 0.5, and 1.0 the corresponding surface concentration csA as a function of bulk concentration cA. Output a CSV file with columns cA, csA_mu0, csA_mu0p5, csA_mu1. Use interpolation if needed to ensure consistent cA grid.
- Output file: `/app/outputs/fig1_csA_vs_cA.csv`
- Format: csv
- Contract: Columns: cA (float), csA_mu0 (float), csA_mu0p5 (float), csA_mu1 (float). Unitless reduced values.
- Scoring: scored by hidden verifier

### Step 3: Extract Fig.2 data: csA vs μs
- Role: scored (load-bearing)
- Action: From the solver data, extract for bulk concentrations cA = 0.001, 0.01, 0.05, 0.1 the surface concentration csA as a function of μs over the range 0 to 1. Output a CSV file with columns mu, csA_cA0p001, csA_cA0p01, csA_cA0p05, csA_cA0p1.
- Output file: `/app/outputs/fig2_csA_vs_mu.csv`
- Format: csv
- Contract: Columns: mu (float), csA_cA0p001 (float), csA_cA0p01 (float), csA_cA0p05 (float), csA_cA0p1 (float). Unitless.
- Scoring: scored by hidden verifier

### Step 4: Extract Fig.3 data: μs vs temperature
- Role: scored (load-bearing)
- Action: From the solver data, extract for bulk concentrations cA = 0.01, 0.05, 0.1 the surface magnetization μs as a function of reduced temperature τ = kT/|J_s| over a range that covers the first-order transition (τ from 0 to 2). Output a CSV file with columns tau, mu_cA0p01, mu_cA0p05, mu_cA0p1.
- Output file: `/app/outputs/fig3_mu_vs_T.csv`
- Format: csv
- Contract: Columns: tau (float), mu_cA0p01 (float), mu_cA0p05 (float), mu_cA0p1 (float). Unitless.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fig1_csA_vs_cA.csv`
- `/app/outputs/fig2_csA_vs_mu.csv`
- `/app/outputs/fig3_mu_vs_T.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fig1_csA_vs_cA.csv
- path: `/app/outputs/fig1_csA_vs_cA.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV containing cA and csA at fixed μs values.
- schema:
  - `type`: table
  - `required_columns`: `cA`, `csA_mu0`, `csA_mu0p5`, `csA_mu1`
  - `units`:
    - `cA`: unitless (fraction)
    - `csA_mu0`: unitless
    - `csA_mu0p5`: unitless
    - `csA_mu1`: unitless

### fig2_csA_vs_mu.csv
- path: `/app/outputs/fig2_csA_vs_mu.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV containing mu and csA at fixed cA values.
- schema:
  - `type`: table
  - `required_columns`: `mu`, `csA_cA0p001`, `csA_cA0p01`, `csA_cA0p05`, `csA_cA0p1`
  - `units`:
    - `mu`: unitless
    - `csA_cA0p001`: unitless
    - `csA_cA0p01`: unitless
    - `csA_cA0p05`: unitless
    - `csA_cA0p1`: unitless

### fig3_mu_vs_T.csv
- path: `/app/outputs/fig3_mu_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: CSV containing reduced temperature and μs at fixed cA values, showing a first-order jump.
- schema:
  - `type`: table
  - `required_columns`: `tau`, `mu_cA0p01`, `mu_cA0p05`, `mu_cA0p1`
  - `units`:
    - `tau`: unitless (reduced temperature)
    - `mu_cA0p01`: unitless
    - `mu_cA0p05`: unitless
    - `mu_cA0p1`: unitless

Notes: All quantities are in reduced dimensionless units using the energy scale |J_s|. The curves must exhibit surface enrichment (csA > cA), csA increasing with μs, and μs showing an abrupt drop at a critical temperature indicative of a first-order transition.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fig1_csA_vs_cA.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cA",
          "csA_mu0",
          "csA_mu0p5",
          "csA_mu1"
        ],
        "units": {
          "cA": "unitless (fraction)",
          "csA_mu0": "unitless",
          "csA_mu0p5": "unitless",
          "csA_mu1": "unitless"
        }
      },
      "description": "CSV containing cA and csA at fixed μs values."
    },
    {
      "file": "fig2_csA_vs_mu.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "mu",
          "csA_cA0p001",
          "csA_cA0p01",
          "csA_cA0p05",
          "csA_cA0p1"
        ],
        "units": {
          "mu": "unitless",
          "csA_cA0p001": "unitless",
          "csA_cA0p01": "unitless",
          "csA_cA0p05": "unitless",
          "csA_cA0p1": "unitless"
        }
      },
      "description": "CSV containing mu and csA at fixed cA values."
    },
    {
      "file": "fig3_mu_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "tau",
          "mu_cA0p01",
          "mu_cA0p05",
          "mu_cA0p1"
        ],
        "units": {
          "tau": "unitless (reduced temperature)",
          "mu_cA0p01": "unitless",
          "mu_cA0p05": "unitless",
          "mu_cA0p1": "unitless"
        }
      },
      "description": "CSV containing reduced temperature and μs at fixed cA values, showing a first-order jump."
    }
  ],
  "notes": "All quantities are in reduced dimensionless units using the energy scale |J_s|. The curves must exhibit surface enrichment (csA > cA), csA increasing with μs, and μs showing an abrupt drop at a critical temperature indicative of a first-order transition."
}
```

## How you are scored
A hidden verifier independently solves the same coupled equations using a trusted numerical method and generates reference curves for each of the three datasets. Your submitted CSV files are compared pointwise against the reference within an absolute tolerance. Additionally, the verifier checks structural properties: for dataset 1 that csA increases with cA and that csA > cA; for dataset 2 that csA increases with μs; and for dataset 3 that μs exhibits a discontinuity (a jump from a non‑zero value to zero) as τ increases. Each scored file contributes to the final reward according to a pre‑defined weight distribution. Reporting a single final number without producing the raw CSV data will not earn credit; the verifier recomputes the target quantities from your submitted curves.
