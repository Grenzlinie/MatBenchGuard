# 2D Gaussian-Core Model Phase Diagram and Hexatic Phase Detection

## Problem background
The two-dimensional Gaussian-core model consists of particles interacting via a purely repulsive Gaussian pair potential, v(r)=ε exp(-r²/σ²). In two dimensions, thermal fluctuations prevent true long-range crystalline order, and melting can proceed through a continuous two-stage transition following the Kosterlitz-Thouless-Halperin-Nelson-Young (KTHNY) theory. In this scenario, a hexatic phase—with quasi-long-range orientational order but short-range translational order—intervenes between the solid and the normal fluid. The model is also known to exhibit reentrant melting (melting upon compression) and waterlike anomalies in the fluid phase. This task investigates the phase behavior of the 2D Gaussian-core model by mapping the melting line and identifying the hexatic phase and structural anomalies through direct Monte Carlo simulation.

## Approach
The central methodology is isothermal-isobaric Monte Carlo (MC) simulation using the triangular lattice as the reference solid configuration. The system is driven across the melting region by performing temperature scans at several fixed pressures. Translational and orientational order parameters (ψ_T and ψ_6) and their susceptibilities are computed to locate solid-hexatic and hexatic-fluid transitions. The orientational correlation function h6(r) is measured to verify the algebraic decay that characterizes the hexatic phase, with the decay exponent η expected to satisfy η < 1/4 in the hexatic region. The melting line is determined by identifying the transition temperatures at pressures P = 0.6, 0.2, and 0.05 (in reduced units). Additionally, the absolute pair entropy is calculated from radial distribution functions at a fixed temperature to locate the structural anomaly, where the entropy as a function of density exhibits a maximum. The simulations can be implemented with open-source tools such as LAMMPS or custom Python code.

## Reproduction target
Produce the following scored outputs derived from the Monte Carlo simulations:

1. Order parameters at P=0.6: CSV file with temperature series of ψ_T, χ_T, ψ_6, χ_6.
2. Orientational correlation function h6(r) at P=0.6 for at least three temperatures spanning solid, hexatic, and normal fluid regimes.
3. Melting line table with transition temperatures T_solid_hexatic and T_hexatic_fluid for P = 0.6, 0.2, 0.05.
4. Structural anomaly locus: pair entropy S_pair as a function of density at fixed temperature T = 0.008 (reduced units).

All data must be obtained from the agent's own simulations; the checker will recompute derived quantities (peak locations, exponent fit, entropy maximum) to assess correctness.

## Assets

- Python scientific computing stack (numpy, scipy, matplotlib): numpy scipy matplotlib
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov

## Workflow steps

### Step 1: Monte Carlo simulations
- Role: process
- Action: Implement and run isothermal-isobaric Monte Carlo simulations for the 2D Gaussian-core model using a triangular lattice initial configuration. Perform temperature scans at pressures P=0.6 (high resolution, ΔT~0.0001 ε/k_B), P=0.2 and P=0.05 (lower resolution, ΔT=0.0005). For each state point, equilibrate and collect particle configurations, average energy, density, and radial distribution functions. For the structural anomaly, also run simulations at fixed temperature T=0.008 ε/k_B over a range of densities.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Order parameters at P=0.6
- Role: scored
- Action: From the high-resolution MC configurations at P=0.6, compute the translational order parameter ψ_T and its susceptibility χ_T, as well as the orientational order parameter ψ_6 and its susceptibility χ_6, as functions of temperature. Save the data.
- Output file: `/app/outputs/order_params_p06.csv`
- Format: csv
- Contract: CSV with columns: T (reduced ε/k_B), psi_T, chi_T, psi_6, chi_6
- Scoring: scored by hidden verifier

### Step 3: Orientational correlation function at P=0.6
- Role: scored
- Action: From particle configurations at selected temperatures spanning the solid, hexatic, and fluid regimes at P=0.6, compute the orientational correlation function h6(r). Provide data for at least three temperatures: one solid, one hexatic, one normal fluid.
- Output file: `/app/outputs/ocf_data_p06.csv`
- Format: csv
- Contract: CSV with columns: T (reduced ε/k_B), r (reduced σ), h6(r)
- Scoring: scored by hidden verifier

### Step 4: Melting line at selected pressures
- Role: scored
- Action: From MC simulation data at P=0.2 and P=0.05, compute translational and orientational order parameters and their susceptibilities. Identify solid-hexatic and hexatic-fluid transition temperatures from susceptibility peaks. For P=0.6, use the results from order_params_p06.csv. Report transition temperatures for each pressure, leaving cells empty if no hexatic phase is resolved.
- Output file: `/app/outputs/melting_line.csv`
- Format: csv
- Contract: CSV with columns: P (reduced ε/σ²), T_solid_hexatic (reduced ε/k_B), T_hexatic_fluid (reduced ε/k_B)
- Scoring: scored by hidden verifier

### Step 5: Structural anomaly locus
- Role: scored (load-bearing)
- Action: From MC simulations at fixed temperature T=0.008 ε/k_B across a range of densities, compute the radial distribution function g(r) and evaluate the absolute pair entropy S_pair. Output S_pair as a function of density.
- Output file: `/app/outputs/structural_anomaly.csv`
- Format: csv
- Contract: CSV with columns: T (reduced ε/k_B), rho (reduced number density, ε/σ²), S_pair (absolute pair entropy in units of k_B)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/order_params_p06.csv`
- `/app/outputs/ocf_data_p06.csv`
- `/app/outputs/melting_line.csv`
- `/app/outputs/structural_anomaly.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### order_params_p06.csv
- path: `/app/outputs/order_params_p06.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Translational and orientational order parameters and their susceptibilities at P=0.6.
- schema:
  - `type`: table
  - `required_columns`: `T`, `psi_T`, `chi_T`, `psi_6`, `chi_6`
  - `units`:
    - `T`: ε/k_B
    - `psi_T`: dimensionless
    - `chi_T`: dimensionless
    - `psi_6`: dimensionless
    - `chi_6`: dimensionless

### ocf_data_p06.csv
- path: `/app/outputs/ocf_data_p06.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Orientational correlation function h6(r) at selected temperatures for P=0.6; the checker will fit the tail of h6(r) to a power law and verify the exponent η<1/4.
- schema:
  - `type`: table
  - `required_columns`: `T`, `r`, `h6(r)`
  - `units`:
    - `T`: ε/k_B
    - `r`: σ
    - `h6(r)`: dimensionless

### melting_line.csv
- path: `/app/outputs/melting_line.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Melting transition temperatures for pressures P=0.6, 0.2, 0.05. The checker will compare these to hidden reference values with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `P`, `T_solid_hexatic`, `T_hexatic_fluid`
  - `units`:
    - `P`: ε/σ²
    - `T_solid_hexatic`: ε/k_B
    - `T_hexatic_fluid`: ε/k_B

### structural_anomaly.csv
- path: `/app/outputs/structural_anomaly.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Pair entropy vs density at T=0.008; the checker will locate the density of maximum S_pair and compare it to the paper’s structural anomaly locus.
- schema:
  - `type`: table
  - `required_columns`: `T`, `rho`, `S_pair`
  - `units`:
    - `T`: ε/k_B
    - `rho`: ε/σ²
    - `S_pair`: k_B

Notes: The task reproduces the key quantitative results of the paper. All outputs must be derived from the MC simulations invoked in the first process step. No gold values are included in this contract; tolerances are set in the hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "order_params_p06.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "psi_T",
          "chi_T",
          "psi_6",
          "chi_6"
        ],
        "units": {
          "T": "ε/k_B",
          "psi_T": "dimensionless",
          "chi_T": "dimensionless",
          "psi_6": "dimensionless",
          "chi_6": "dimensionless"
        }
      },
      "description": "Translational and orientational order parameters and their susceptibilities at P=0.6."
    },
    {
      "file": "ocf_data_p06.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "r",
          "h6(r)"
        ],
        "units": {
          "T": "ε/k_B",
          "r": "σ",
          "h6(r)": "dimensionless"
        }
      },
      "description": "Orientational correlation function h6(r) at selected temperatures for P=0.6; the checker will fit the tail of h6(r) to a power law and verify the exponent η<1/4."
    },
    {
      "file": "melting_line.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "P",
          "T_solid_hexatic",
          "T_hexatic_fluid"
        ],
        "units": {
          "P": "ε/σ²",
          "T_solid_hexatic": "ε/k_B",
          "T_hexatic_fluid": "ε/k_B"
        }
      },
      "description": "Melting transition temperatures for pressures P=0.6, 0.2, 0.05. The checker will compare these to hidden reference values with an absolute tolerance."
    },
    {
      "file": "structural_anomaly.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "rho",
          "S_pair"
        ],
        "units": {
          "T": "ε/k_B",
          "rho": "ε/σ²",
          "S_pair": "k_B"
        }
      },
      "description": "Pair entropy vs density at T=0.008; the checker will locate the density of maximum S_pair and compare it to the paper’s structural anomaly locus."
    }
  ],
  "notes": "The task reproduces the key quantitative results of the paper. All outputs must be derived from the MC simulations invoked in the first process step. No gold values are included in this contract; tolerances are set in the hidden grading specification."
}
```

## How you are scored
Each output file is evaluated independently by a hidden verifier. The verifier recomputes key quantities from your raw data:

- From `order_params_p06.csv` it locates the susceptibility peak temperatures to identify the solid-hexatic and hexatic-fluid transition points and checks that the two peaks are distinct.
- From `ocf_data_p06.csv` it fits the tail of h6(r) in the hexatic regime to a power law r^{-η} to verify η < 0.25, and checks that solid and fluid correlation functions exhibit the expected behavior (constant and exponential, respectively).
- From `melting_line.csv` it compares the reported transition temperatures against a hidden reference for each pressure.
- From `structural_anomaly.csv` it determines the density at which S_pair is maximum and compares that to a hidden reference density.

Scores from these four stages are weighted and combined into a final reward in [0,1]. Producing the expected qualitative trends and quantitative agreement within the verifier's tolerances yields full credit; providing only a final self-reported number without the underlying artifacts will not pass.
