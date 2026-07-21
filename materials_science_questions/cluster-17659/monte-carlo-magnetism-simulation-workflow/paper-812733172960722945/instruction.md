# Monte Carlo Simulation of PIPS Domain Size Trends

## Problem background
Polymerization-induced phase separation (PIPS) occurs when a mixture of reactive monomers and small molecules undergoes polymerization, driving the system into an unstable region and causing phase separation at a constant temperature. The resulting domain size is crucial for applications such as polymer-dispersed liquid crystals. This task investigates PIPS via Monte Carlo simulation on a two-component Ising model. By incorporating a time-dependent quench depth derived from polymerization kinetics and mean-field Flory-Huggins theory, the simulation models the evolution of domain structure under different reaction speeds and quench temperatures. The goal is to compute quantitative measures of the phase-separated domain size and determine how they respond to the control parameters.

## Approach
The simulation uses a 200×200 square lattice with nearest-neighbor Ising interactions (J=1, k_B=1) and Metropolis Monte Carlo updates with Kawasaki exchange dynamics. The effective quench temperature evolves in time according to a schedule that mimics the reduction in quench depth caused by the advancing critical temperature during polymerization. This schedule depends on the reaction rate constant k, monomer concentration p=0.5, and reduced time t (in Monte Carlo steps). Several parameter combinations are explored: one reaction speed is varied (k=0.01 vs. 0.1) at a fixed quench temperature (T_q=0.4a), and the quench temperature is varied (T_q=0.3a vs. 0.4a) at a fixed reaction speed (k=0.01). For each condition, multiple independent runs are performed, stopping when the polymerization degree reaches a common value (N=201). From the final spin configurations, the spherically averaged structure factor S(k) and the radial autocorrelation function are computed. Domain size is quantified by the first moment k1 of S(k) and the first zero crossing (FZC) of the autocorrelation function. The comparison of these quantities across conditions reveals the qualitative effects of reaction speed and quench temperature on domain size.

## Reproduction target
Run the Monte Carlo simulation for the three parameter conditions: (k=0.01, T_q=0.4a), (k=0.1, T_q=0.4a), and (k=0.01, T_q=0.3a). For each condition, perform 5 independent repetitions and stop when the polymerization degree 1+2kp·MCS reaches 201. Analyze the final spin configurations to obtain, for each run, the first zero crossing (FZC) of the radial autocorrelation function and the first moment k1 of the structure factor. Average the results per condition and output them in a CSV file `/app/outputs/pips_trends.csv` with columns condition_id, k, T_q, MCS_at_fixed_degree, FZC_mean, k1_mean. The hidden verifier will check that the computed domain sizes (FZC and k1) are physically plausible and that the ordering across conditions is consistent with the expected physical dependencies of domain size on reaction speed and quench temperature.

## Assets

- NumPy: https://pypi.tuna.tsinghua.edu.cn/simple numpy
- SciPy: https://pypi.tuna.tsinghua.edu.cn/simple scipy

## Workflow steps

### Step 1: Monte Carlo simulation of PIPS Ising model
- Role: process
- Action: Implement a 2D Ising model on a 200×200 square lattice with nearest-neighbor interaction J=1, kB=1. Use Metropolis Monte Carlo updates with Kawasaki exchange dynamics. The quench temperature is time-dependent: T_sim(t) = T_c * (T_q/a) * [1 + sqrt(1/(1+2 k p t))]^2, with T_c = 0.567, p = 0.5, a = 1, t in Monte Carlo steps (MCS). Run simulations for the four parameter combinations: (k=0.01, T_q=0.4a), (k=0.1, T_q=0.4a), (k=0.01, T_q=0.3a). For each condition, perform 5 independent runs with different random seeds. For each run, stop when the polymerization degree N reaches 201, i.e., when 1+2*k*0.5*MCS ≈ 201. Record the spin configurations at the final MCS for analysis.
- Evidence: `/app/outputs/simulation_summary.json`

### Step 2: Domain size analysis and trend verification
- Role: scored (load-bearing)
- Action: From the final spin configurations of each independent run, compute the pair correlation function, then the spherically averaged structure factor S(k). Calculate the first moment k1 = Σ_k k S(k) / Σ_k S(k). Compute the one-dimensional radial autocorrelation function and determine its first zero crossing (FZC). Average k1 and FZC over the 5 runs for each condition. Write the averaged results to a CSV file with columns: condition_id, k, T_q, MCS_at_fixed_degree, FZC_mean, k1_mean.
- Output file: `/app/outputs/pips_trends.csv`
- Format: csv
- Contract: CSV with columns: condition_id (string, one of 'k01_T04','k1_T04','k01_T03'), k (float), T_q (float, in units of a), MCS_at_fixed_degree (int), FZC_mean (float), k1_mean (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pips_trends.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pips_trends.csv
- path: `/app/outputs/pips_trends.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Domain size measures (FZC, k1) for three simulation conditions, used to verify structural ordering trends consistent with the physical dependencies of domain size on reaction speed and quench temperature.
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `k`, `T_q`, `MCS_at_fixed_degree`, `FZC_mean`, `k1_mean`

Notes: The simulation is compute-intensive; the agent may run on external compute and return the final analyzed CSV. Verification checks the ordering of FZC_mean and k1_mean, not absolute values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pips_trends.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "k",
          "T_q",
          "MCS_at_fixed_degree",
          "FZC_mean",
          "k1_mean"
        ]
      },
      "description": "Domain size measures (FZC, k1) for three simulation conditions, used to verify structural ordering trends consistent with the physical dependencies of domain size on reaction speed and quench temperature."
    }
  ],
  "notes": "The simulation is compute-intensive; the agent may run on external compute and return the final analyzed CSV. Verification checks the ordering of FZC_mean and k1_mean, not absolute values."
}
```

## How you are scored
Your solution is scored entirely by the hidden verifier. It will check that the CSV file is correctly formatted and that the reported domain size measures satisfy the qualitative trend relationships described in the target. No external reference values are used; the reward depends solely on whether the ordering of FZC and k1 across the three conditions matches the expected dependencies on k and T_q.
