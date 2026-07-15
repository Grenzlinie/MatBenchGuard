# Compute and analyze thermoelectric power factor

## Problem background
Three-terminal thermoelectric energy harvesters convert heat to electricity via phonon-assisted electron hopping between quantum dots embedded in nanowires. A key performance metric is the thermoelectric power factor P = σ S². This work investigates a chain of N quantum dots arranged in a staircase energy configuration, where the energy step between adjacent dots is constant. The power factor is evaluated as a function of the number of dots N and the energy step dE, providing insight into how the dot arrangement influences performance.

## Approach
Implement a three-terminal hopping thermoelectric transport model for a nanowire containing a chain of N quantum dots with a staircase energy profile. The model couples inelastic hopping conduction (driven by a hot phonon bath) and elastic tunneling (pure quantum tunneling). For inelastic transport, treat the chain as a Miller‑Abrahams resistor network: compute hopping transition rates using Fermi’s golden rule with an exponential distance decay, solve Kirchhoff’s current-law equations to obtain the local electrochemical potentials of all dots, and then calculate the inelastic conductance G_in. For elastic transport, use a resonant tunneling formula where each dot contributes an independent channel with tunnel couplings that decay exponentially with distance from the electrodes. Sum these to obtain G_el. The total conductance is G = G_in + G_el. From the geometry of the nanowire and the dot arrangement, compute the electrical conductivity σ = G·l/A (l is the total length of a single nano‑thermoelectric element, A a fixed area). The Seebeck coefficient for the three‑terminal phonon‑driven effect is S = (k_B/e) · (G_in · ΔE) / (G · k_B T), where ΔE is the total energy span across the chain. Finally, compute the power factor P = σ · S². This protocol must be evaluated over the full parameter grid of dE and N specified in the workflow steps.

## Reproduction target
Produce a single CSV file, `/app/outputs/step_01_power_factor.csv`, containing the computed conductivity, Seebeck coefficient, and power factor for every combination of the energy step dE (in meV) from the set {10,20,30,40,50,60,70,80,90,100,110,120} and the number of quantum dots N from the set {2,3,5,7,10,12,15,18,21,25,30}. The file must have the columns: `dE(meV)`, `N`, `conductivity(S/m)`, `Seebeck_coefficient(V/K)`, `power_factor(W/(K^2 m))`. All values are real numbers. This file is the only scored artifact.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute power factor for staircase quantum-dot chain
- Role: scored (load-bearing)
- Action: Implement the three-terminal hopping thermoelectric transport model for a chain of N quantum dots with a staircase energy configuration. For each combination of dE and N, compute the inelastic hopping conductance G_in by solving the Miller-Abrahams resistor network linear system for the local electrochemical potentials, and the elastic tunneling conductance G_el using the resonant tunneling formula. Calculate total conductance G = G_in + G_el, electrical conductivity σ = G * l / A (with l = N*l_qd + (N-1)*d + 2*l_b and A = 10⁻¹⁵ m²), the Seebeck coefficient S = (k_B/e) * (G_in * (N-1) * dE) / (G * k_B T), and the power factor P = σ * S². Use the fixed parameters: l_qd=6 nm, d=6 nm, ξ=2 nm, l_b=6 nm, α_ep=10 meV, t₀=100 meV, k_BT=30 meV. Loop over dE values {10,20,30,40,50,60,70,80,90,100,110,120} meV and N values {2,3,5,7,10,12,15,18,21,25,30}.
- Output file: `/app/outputs/step_01_power_factor.csv`
- Format: csv
- Contract: CSV table with header: dE(meV), N, conductivity(S/m), Seebeck_coefficient(V/K), power_factor(W/(K^2 m)). Rows: one per (dE,N) pair. All values are real numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_power_factor.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_power_factor.csv
- path: `/app/outputs/step_01_power_factor.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed power factor and intermediate quantities for each (dE, N) pair. The checker will compare the power_factor values against hidden gold values from the paper and verify that for every dE the maximum power_factor among N>2 exceeds the power_factor at N=2.
- schema:
  - `type`: table
  - `required_columns`: `dE(meV)`, `N`, `conductivity(S/m)`, `Seebeck_coefficient(V/K)`, `power_factor(W/(K^2 m))`
  - `units`:
    - `dE(meV)`: meV
    - `N`: dimensionless
    - `conductivity(S/m)`: S/m
    - `Seebeck_coefficient(V/K)`: V/K
    - `power_factor(W/(K^2 m))`: W/(K^2·m)

Notes: The task is compute-driven; no external dataset is required. The scoring uses a result-level comparison (T0) with hidden paper values and an additional structural ordering check.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_power_factor.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dE(meV)",
          "N",
          "conductivity(S/m)",
          "Seebeck_coefficient(V/K)",
          "power_factor(W/(K^2 m))"
        ],
        "units": {
          "dE(meV)": "meV",
          "N": "dimensionless",
          "conductivity(S/m)": "S/m",
          "Seebeck_coefficient(V/K)": "V/K",
          "power_factor(W/(K^2 m))": "W/(K^2·m)"
        }
      },
      "description": "The computed power factor and intermediate quantities for each (dE, N) pair. The checker will compare the power_factor values against hidden gold values from the paper and verify that for every dE the maximum power_factor among N>2 exceeds the power_factor at N=2."
    }
  ],
  "notes": "The task is compute-driven; no external dataset is required. The scoring uses a result-level comparison (T0) with hidden paper values and an additional structural ordering check."
}
```

## How you are scored
A hidden verifier will read your CSV file and score it in two ways:

1. **Value comparison**: Your computed `power_factor` values will be compared against a set of hidden reference values (obtained from an independent implementation) at a subset of (dE,N) points. The comparison uses a tolerance that accounts for legitimate implementation differences.
2. **Structural consistency**: The verifier will check that your reported `power_factor` equals `conductivity × Seebeck_coefficient²` within numerical precision, and that the data exhibit physically expected trends (e.g., dependence on dE and N) without explicitly revealing what those trends are.

The final reward is a weighted combination of these checks. Note that simply reporting numbers without genuinely running the model will fail the structural consistency checks.
