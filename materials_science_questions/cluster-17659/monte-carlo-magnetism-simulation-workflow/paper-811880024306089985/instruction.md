# Monte Carlo Proton Transport Simulation in Three-State Lattice Model

## Problem background
Proton transport through single-file water wires in transmembrane channels is a fundamental process in bioenergetics. In narrow pores such as gramicidin A, water molecules form a one-dimensional chain where protons hop from oxygen to oxygen via the Grotthuss mechanism. A discrete three-state stochastic lattice model captures the essential physics: each site can be unprotonated with a left‑pointing water dipole (σ = −1), unprotonated with a right‑pointing dipole (σ = +1), or protonated (σ = 0). Transitions among these states (proton entry, exit, hopping, and water flip) obey orientation constraints and are sensitive to energetic interactions — dipole‑aligning fields, nearest‑neighbour dipolar coupling, proton‑proton repulsion, and an external voltage. This model can reproduce a range of nonlinear current‑voltage relationships observed experimentally. The task is to compute the steady‑state proton current and occupancy under several interaction regimes and determine how the interaction parameters affect the current‑voltage behaviour.

## Approach
Implement the three‑state lattice gas (σ_i ∈ {−1, 0, +1}) on a chain of N = 10 sites. The total configurational energy is
E = −K Σ σ_i σ_{i+1} − H Σ σ_i + R Σ (1−σ_i²)(1−σ_{i+1}²) − V Σ i (1−σ_i²),
where the parameters (all in units of k_B T) represent the dipolar coupling K, an external alignment field H, proton‑proton repulsion R, and the voltage V (energy gained per proton per lattice site). Stochastic transitions are constrained: protons can enter/exit only at the ends when receiving waters are correctly oriented, and internal hops require a neighbouring water dipole pointing toward the proton. The intrinsic rate constants are α₀ (left entry), γ₀ (left exit), β₀ (right exit), δ₀ (right entry), p₀ (proton hop), and k₀ (water flip). When interactions are present, each rate ξ is modified to ξ₀ exp(ΔE/2), where ΔE is the energy difference between the final and initial configurations.

Simulate the lattice using a Metropolis Monte Carlo algorithm: repeatedly select a random site, attempt an allowed transition with probability proportional to the modified rate. After reaching steady state, compute the net proton current J by averaging proton transfers across all interfaces, normalised by the chain length, and the chain‑averaged proton occupancy ρ₀ = (1/N) Σ (1−σ_i²).

Explore a systematic parameter sweep:
- Baseline: α₀ = δ₀ = 0.4, β₀ = γ₀ = 0.05, p₀ = 1.0, k₀ = 2.0, H = K = R = 0.
- Water‑flip rate variation: k₀ = 0.5, 1.0, 5.0 (all other parameters as baseline).
- Constant alignment field: H = 1, 2, 3 (other parameters baseline).
- Orientational polarisability: H = L_HV V with L_HV = 0.5, 1.0, 2.0 (other parameters baseline).
- Proton repulsion: R = 2, 4, 6 (other parameters baseline).
- Dipolar coupling (lubrication): K = 1, 2, 3 with injection rates increased to α₀ = δ₀ = 4.0 (other parameters as baseline for this set).

For every condition, run the simulation at voltages V = 0, 0.5, 1.0, …, 5.0. Record the steady‑state current J and occupancy ρ₀ in a CSV file.

## Reproduction target
Produce a single CSV file `simulation_results.csv` containing the steady‑state proton current and average occupancy for every simulated condition. The file must have exactly four columns: `condition_id` (a string identifying the parameter set, e.g. `baseline`, `k0=0.5`, `H=1`, `L_HV=0.5`, `R=2`, `K=1`), `V` (float, voltage), `J` (float, net current), and `occupancy` (float, fraction of protonated sites). Each row corresponds to one (condition, voltage) point. The file should contain rows for all conditions listed in the Approach, spanning the full voltage sweep, with results that correctly reflect the underlying physics of the model.

## Assets
None – the simulation is self‑contained. No external datasets, models, or pre‑trained weights are needed. A standard Python environment with numerical libraries (NumPy, optionally Matplotlib for debugging) is sufficient to implement and run the Monte Carlo simulations.

## Workflow steps

### Step 1: Monte Carlo simulation of proton transport
- Role: scored
- Action: Implement the three-state lattice model (σ ∈ {-1,0,+1}) with energy functional E = -K Σ σ_i σ_{i+1} - H Σ σ_i + R Σ (1-σ_i^2)(1-σ_{i+1}^2) - V Σ i (1-σ_i^2) and Arrhenius-modified transition rates ξ = ξ_0 exp(ΔE/2). Simulate a chain of N=10 sites using Metropolis Monte Carlo for the following parameter sets (all rates in units of p0): baseline (α0=δ0=0.4, β0=γ0=0.05, p0=1.0, k0=2.0, H=K=R=0); flip-rate variations k0=0.5,1.0,5.0; constant H=1,2,3; orientational polarizability H = L_HV V with L_HV=0.5,1.0,2.0; repulsion R=2,4,6; and lubrication K=1,2,3 with α0=δ0=4.0. For each condition, run at voltage V from 0 to 5 in steps of 0.5. After reaching steady state, compute net proton current J by counting proton transfers across all interfaces (normalized by chain length) and chain-averaged proton occupancy (ρ0 = Σ_i (1-σ_i^2)/N). Write the results to simulation_results.csv.
- Output file: `/app/outputs/simulation_results.csv`
- Format: csv
- Contract: CSV with columns: condition_id (string), V (float), J (float), occupancy (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.csv
- path: `/app/outputs/simulation_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Simulation results for multiple parameter regimes. Each row corresponds to a single simulation point (condition and voltage).
- schema:
  - `type`: table
  - `required_columns`: `condition_id`, `V`, `J`, `occupancy`
  - `units`:
    - `V`: dimensionless (units of k_B T per lattice spacing)
    - `J`: dimensionless (units of p0)
    - `occupancy`: fraction (average number of protons per site)

Notes: The checker will verify qualitative structural trends: monotonic non-decreasing J(V) except for NDR conditions where a peak must be present; relative ordering of currents across parameter variations (e.g., higher k0 yields higher J, higher H yields lower J, R>0 curves more convex than R=0, and lubrication enhancement at high injection rates). Occupancy should decrease with H and increase with injection.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "condition_id",
          "V",
          "J",
          "occupancy"
        ],
        "units": {
          "V": "dimensionless (units of k_B T per lattice spacing)",
          "J": "dimensionless (units of p0)",
          "occupancy": "fraction (average number of protons per site)"
        }
      },
      "description": "Simulation results for multiple parameter regimes. Each row corresponds to a single simulation point (condition and voltage)."
    }
  ],
  "notes": "The checker will verify qualitative structural trends: monotonic non-decreasing J(V) except for NDR conditions where a peak must be present; relative ordering of currents across parameter variations (e.g., higher k0 yields higher J, higher H yields lower J, R>0 curves more convex than R=0, and lubrication enhancement at high injection rates). Occupancy should decrease with H and increase with injection."
}
```

## How you are scored
A hidden verifier will read your `simulation_results.csv` and compute a reward in [0, 1]. The verifier does NOT compare your numbers to exact reference values. Instead, it checks that (i) the required rows are present and have valid numerical data, and (ii) the current‑voltage curves exhibit physically correct qualitative behaviour consistent with the three‑state model — for example, correct relative ordering between different parameter regimes, expected monotonicity or non‑monotonicity under specific conditions, and occupancy trends that accord with the model’s rate‑limiting steps. Only correct qualitative reproduction is rewarded; simply reporting arbitrary numbers will yield a low score.
