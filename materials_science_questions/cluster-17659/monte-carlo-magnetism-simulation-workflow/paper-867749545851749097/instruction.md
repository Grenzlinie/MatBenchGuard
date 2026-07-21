# Monte Carlo Study of Dynamic Order Parameter and Metastable Lifetime in the 2D NNN Kinetic Ising Model

## Problem background
The two-dimensional ferromagnetic kinetic Ising model with nearest-neighbor (NN) interactions, driven by an oscillating magnetic field, exhibits a dynamic phase transition, and its period-averaged magnetization (dynamic order parameter) reveals whether the system is in an ordered or disordered dynamic state. Extending the model with additional next-nearest-neighbor (NNN) ferromagnetic interactions alters the energy landscape. This task investigates the effect of the NNN interaction strength on the dynamic order parameter and on the metastable lifetime of the magnetization under field reversal.

## Approach
The model is a kinetic Ising ferromagnet on a square lattice with periodic boundary conditions, with NN coupling J_nn and NNN coupling J_nnn = p * J_nn, under a sinusoidal magnetic field. The dynamics follows Metropolis single-spin-flip Monte Carlo with time measured in Monte Carlo steps per spin (MCSS). First, for a set of NNN interaction ratios p, the system is simulated with an oscillating field; the magnetization time series is recorded and the period-averaged magnetization (dynamic order parameter Q) is computed. Second, for selected field amplitudes and p values, instantaneous field‑reversal experiments are performed: the system is prepared fully magnetized up, the field sign is reversed, and the first‑passage time until the magnetization per site crosses zero is recorded. Many independent trials are averaged to obtain the mean metastable lifetime. The results are aggregated into two CSV files.

## Reproduction target
1. Compute the average absolute dynamic order parameter ⟨|Q|⟩ as a function of the NNN interaction ratio p over the range p = 0.0 to 0.4, using system parameters: lattice size L = 128, field amplitude h0 = 0.5 J_nn, frequency f = 10⁻³, temperature T = 0.8 T_c^NN (where T_c^NN ≈ 2.269). Observe how ⟨|Q|⟩ varies as p changes.
2. Compute the mean metastable lifetime ⟨τ⟩ (and its standard deviation) after instantaneous field reversal, as a function of field amplitude h0 for several fixed NNN interaction ratios (p = 0, 0.5, 0.7, 1.0). The lattice size is L = 128 and temperature T = 0.8 T_c^NN. Determine whether and how ⟨τ⟩ depends on p for each h0. Use at least 1000 independent trials per parameter point.

## Assets
No external datasets or pre‑trained models are required. All model parameters and simulation protocols are specified in the instructions. Use a standard programming environment with a Monte Carlo simulation library or write your own implementation; typical Python libraries (NumPy, random, csv, math) suffice.

## Workflow steps

### Step 1: Simulate NNNKI model under oscillating field
- Role: process
- Action: Implement the 2D kinetic Ising model with nearest-neighbor (J_nn=1) and next-nearest-neighbor (J_nnn=p*J_nn) ferromagnetic interactions on a square lattice (L=128) with periodic boundary conditions. Use Metropolis single-spin-flip Monte Carlo with MCSS as unit time. For interaction ratios p in [0.0, 0.4] with appropriate step, run simulations with oscillating field amplitude h0=0.5, frequency f=1e-3, temperature T=0.8*Tc^NN (Tc^NN≈2.269, kB=1). Equilibrate the system, then record the magnetization per site m(t) for at least 100,000 MCSS per p.
- Evidence: `/app/outputs/magnetization_series.csv`

### Step 2: Compute dynamic order parameter ⟨|Q|⟩
- Role: scored (load-bearing)
- Action: From the magnetization time series for each p, compute the period-averaged magnetization Q = (ω/2π) ∮ m(t) dt over each field cycle. Average the absolute value ⟨|Q|⟩ over the last several steady-state cycles. Output the result for each p.
- Output file: `/app/outputs/dynamic_order_parameter.csv`
- Format: csv
- Contract: CSV with columns: p (float, interaction ratio), L (int, lattice size, value 128), Q_abs (float, average of absolute dynamic order parameter).
- Scoring: scored by hidden verifier

### Step 3: Simulate instantaneous field-reversal for metastable lifetime
- Role: process
- Action: For each field amplitude h0 in {0.2, 0.3, 0.4, 0.5, 0.6} and each interaction ratio p in {0, 0.5, 0.7, 1.0}, perform field-reversal experiments: prepare the system with all spins up (m=+1), instantaneously reverse the field sign to -h0, and apply Metropolis dynamics until the magnetization per site crosses zero. Record the first-passage time in MCSS. Repeat 1000 independent trials for each (h0, p) parameter set.
- Evidence: `/app/outputs/lifetime_raw_trials.csv`

### Step 4: Compute average metastable lifetime
- Role: scored (load-bearing)
- Action: From the collected first-passage times for each (h0, p) combination, compute the average metastable lifetime ⟨τ⟩ and its standard deviation. Output the results.
- Output file: `/app/outputs/metastable_lifetime.csv`
- Format: csv
- Contract: CSV with columns: h0 (float, field amplitude), p (float, interaction ratio), tau_avg (float, average metastable lifetime in MCSS), tau_std (float, standard deviation of lifetime in MCSS).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/dynamic_order_parameter.csv`
- `/app/outputs/metastable_lifetime.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### dynamic_order_parameter.csv
- path: `/app/outputs/dynamic_order_parameter.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Dynamic order parameter ⟨|Q|⟩ as a function of interaction ratio p at L=128, h0=0.5, f=1e-3, T=0.8*Tc^NN. The hidden checker compares Q_abs values against paper-derived references with absolute tolerance and verifies the transition from near-zero to non-zero around p≈0.2–0.3.
- schema:
  - `type`: table
  - `required_columns`: `p`, `L`, `Q_abs`
  - `units`:
    - `p`: none
    - `L`: none
    - `Q_abs`: none

### metastable_lifetime.csv
- path: `/app/outputs/metastable_lifetime.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average metastable lifetime ⟨τ⟩ and standard deviation for field amplitudes h0 and interaction ratios p at L=128, T=0.8*Tc^NN, averaged over 1000 trials. The hidden checker compares tau_avg values against paper-derived references with relative tolerance and verifies the monotonic trend that τ increases with p.
- schema:
  - `type`: table
  - `required_columns`: `h0`, `p`, `tau_avg`, `tau_std`
  - `units`:
    - `h0`: none
    - `p`: none
    - `tau_avg`: MCSS
    - `tau_std`: MCSS

Notes: All required simulation parameters are publicly stated and do not depend on external datasets. The task is compute-driven; the agent must re-implement the Metropolis algorithm and run the simulations from scratch. Scored CSVs will be compared to hidden reference values extracted from the published paper (Figures 2 and 3).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "dynamic_order_parameter.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "p",
          "L",
          "Q_abs"
        ],
        "units": {
          "p": "none",
          "L": "none",
          "Q_abs": "none"
        }
      },
      "description": "Dynamic order parameter ⟨|Q|⟩ as a function of interaction ratio p at L=128, h0=0.5, f=1e-3, T=0.8*Tc^NN. The hidden checker compares Q_abs values against paper-derived references with absolute tolerance and verifies the transition from near-zero to non-zero around p≈0.2–0.3."
    },
    {
      "file": "metastable_lifetime.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "h0",
          "p",
          "tau_avg",
          "tau_std"
        ],
        "units": {
          "h0": "none",
          "p": "none",
          "tau_avg": "MCSS",
          "tau_std": "MCSS"
        }
      },
      "description": "Average metastable lifetime ⟨τ⟩ and standard deviation for field amplitudes h0 and interaction ratios p at L=128, T=0.8*Tc^NN, averaged over 1000 trials. The hidden checker compares tau_avg values against paper-derived references with relative tolerance and verifies the monotonic trend that τ increases with p."
    }
  ],
  "notes": "All required simulation parameters are publicly stated and do not depend on external datasets. The task is compute-driven; the agent must re-implement the Metropolis algorithm and run the simulations from scratch. Scored CSVs will be compared to hidden reference values extracted from the published paper (Figures 2 and 3)."
}
```

## How you are scored
A hidden verifier will independently examine your two output CSV files. For dynamic_order_parameter.csv, your reported ⟨|Q|⟩ values for each p will be compared to reference values with appropriate tolerances, and the overall trend across p will be assessed. For metastable_lifetime.csv, your reported average lifetimes for each (h0,p) will be compared to reference values and the verifier will check whether the relationship between τ and p follows the correct pattern. Each artifact contributes a weighted portion to the final score, and the verifier may also perform structural checks (e.g., correct columns, data types). Simply reporting plausible numbers is not sufficient; your implementation must genuinely reproduce the underlying physics.
