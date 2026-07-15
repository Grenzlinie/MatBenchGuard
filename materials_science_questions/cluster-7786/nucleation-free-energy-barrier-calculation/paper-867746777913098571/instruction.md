# Becker–Döring scaling and Avrami’s law verification for spin-s Ising models

## Problem background
Classical nucleation theory (Becker–Döring) predicts that a ferromagnet placed in a weak antiparallel magnetic field below its critical temperature passes through a metastable state before the magnetization reverses. For the spin‑1/2 Ising model on a square lattice, the theory predicts three distinct field‑dependent regimes of decay, revealed by plotting the logarithm of the mean reversal time τ against the inverse field strength 1/|h|: a strong‑field regime, a coalescence regime, and a nucleation regime. In the coalescence and nucleation regimes ln τ should be linear in 1/|h|, with the nucleation slope larger than the coalescence slope by a factor of 3 (the dimension d+1 for d=2). In addition, Avrami's law states that the logarithm of the fraction of the system still in the metastable (positive‑spin) state decays as ∝ t^(d+1) in the late stages. The present task asks whether these predictions carry over to general integer‑ and half‑integer‑spin Ising models (spin‑s with s=1/2,2,5/2,3,7/2) when the temperature is set to 0.7 of the pseudocritical temperature T_L^*. Approximate values for T_L^* on a 100×100 lattice are known: s=0.5 → 2.27, s=1 → 1.72, s=1.5 → 1.47, s=2 → 1.34, s=2.5 → 1.26, s=3 → 1.21, s=3.5 → 1.18; you may use these directly or refine them by your own simulations. You will simulate the models and produce data that allow verification of the three‑regime Becker‑Döring scaling and the Avrami‑like decay.

## Approach
The core method is Metropolis single‑spin‑flip Monte Carlo simulation of the spin‑s Ising model on a 100×100 square lattice with periodic boundary conditions, using the normalized Hamiltonian ℋ = −(1/s²)J ∑_{⟨i,j⟩} s_i^z s_j^z − (1/s) h ∑_i s_i^z. The model is simulated at a fixed temperature T = 0.7 T_L^*, where T_L^* is the pseudocritical temperature (the peak of the magnetic susceptibility for the given spin value). You will first determine or adopt the values of T_L^*. Then, for each spin value, you prepare the system in the perfectly ordered state (all s_i^z = +1) and evolve it under a constant negative applied field h, measuring the time τ when the magnetization per spin first changes sign. By averaging over many independent runs (1000 per condition) you obtain the mean reversal time as a function of h, covering at least 10 distinct field strengths that span the strong‑field, coalescence, and nucleation regimes. For the highest spin value s=7/2, you will additionally record the time evolution of the normalized counts of the four positive spin projections (7/2, 5/2, 3/2, 1/2) at three representative fields, up to several multiples of τ. The generated raw data will be evaluated by a hidden verifier that fits piecewise linear models to ln τ vs 1/|h| and checks the linearity of the metastable‑fraction decay with respect to (t/τ)^3.

## Reproduction target
Submit two CSV files under /app/outputs: (1) `reversal_times.csv` with columns s (float), h (float, negative), tau (float, positive) for each (s, h) combination simulated, including at least 10 distinct h values per spin value for s = 0.5, 2.0, 2.5, 3.0, 3.5; the rows must be ordered by s then by increasing |h|. (2) `avrami_decay.csv` with columns h, t (integer MCSS), N_7_2, N_5_2, N_3_2, N_1_2 (all normalized counts per spin) for the s=7/2 Ising model at h = –0.2, –0.5, –0.8, with t increasing monotonically per field and extending to several multiples of the corresponding reversal time τ. The verifier will check that the reversal-time data exhibit three distinct regimes in ln(τ) versus 1/|h|, with a positive nucleation‑regime slope that is approximately a factor of 3 larger than the coalescence‑regime slope (the theoretical value for d=2). For the Avrami data, it will verify that the logarithm of the total positive fraction (sum of the four tracked spin components) decays linearly when plotted against (t/τ)^3 for t > τ, with a negative slope, and that the populations of the intermediate spin states (5/2, 3/2, 1/2) show a maximum at a time earlier than τ.

## Assets

- Python: https://www.python.org/downloads/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Obtain pseudocritical temperatures
- Role: process
- Action: Determine the pseudocritical temperature T_L^* for each spin value s=0.5, 1, 1.5, 2, 2.5, 3, 3.5 from the peak of the magnetic susceptibility, using equilibrium Monte Carlo simulations of the spin-s Ising model on a 100×100 square lattice with periodic boundary conditions at h=0. Alternatively, use the known approximate values provided in the problem background: s=0.5→2.27, 1→1.72, 1.5→1.47, 2→1.34, 2.5→1.26, 3→1.21, 3.5→1.18.
- Evidence: `/app/outputs/pseudocritical_used.csv`

### Step 2: Metastable reversal time data
- Role: scored (load-bearing)
- Action: For each spin s in {0.5, 2.0, 2.5, 3.0, 3.5}, set temperature T = 0.7 * T_L^*. Run Metropolis single spin-flip Monte Carlo simulations of the spin-s Ising model on a 100×100 square lattice with periodic boundary conditions, starting from a perfectly ordered state (all s_i^z = +1). For each s, simulate for a range of negative magnetic fields h (at least 10 distinct values per s, spanning strong-field, coalescence, and nucleation regimes). Use 1000 independent runs per (s,h) pair. For each run, compute the reversal time τ as the time in MCSS when the magnetization per spin m(t) first changes sign. Average τ over runs. Output a CSV file reversal_times.csv with columns s, h, tau.
- Output file: `/app/outputs/reversal_times.csv`
- Format: csv
- Contract: columns: s (float), h (float, negative), tau (float, positive). Each row corresponds to one (s,h) combination, ordered by s then by increasing |h|. s values must include 0.5, 2.0, 2.5, 3.0, 3.5.
- Scoring: scored by hidden verifier

### Step 3: Avrami’s law decay data
- Role: scored (load-bearing)
- Action: For the spin-7/2 Ising model (s=3.5) at temperature T = 0.7 * T_L^*, run Monte Carlo simulations for magnetic fields h = -0.2, -0.5, -0.8, using 1000 independent runs per field. Track the time evolution of the normalized spin-projection counts N_{7/2}/N, N_{5/2}/N, N_{3/2}/N, N_{1/2}/N at each Monte Carlo step per spin (MCSS) from the start until a few multiples of the reversal time τ after magnetization reversal. Average counts over runs. Output a CSV file avrami_decay.csv with columns h, t, N_7_2, N_5_2, N_3_2, N_1_2.
- Output file: `/app/outputs/avrami_decay.csv`
- Format: csv
- Contract: columns: h (float), t (integer, MCSS), N_7_2 (float, normalized count), N_5_2 (float), N_3_2 (float), N_1_2 (float). Each row is one time point for a given field. t increases monotonically per h, and extends to several multiples of the reversal time τ for that field.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reversal_times.csv`
- `/app/outputs/avrami_decay.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reversal_times.csv
- path: `/app/outputs/reversal_times.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Reversal time data for Becker-Döring scaling analysis. Checker fits piecewise linear models to ln(tau) vs 1/|h| to verify three-regime structure, nucleation-regime slope positive and greater than coalescence-regime slope, and slope ratio consistent with d=2.
- schema:
  - `type`: table
  - `required_columns`: `s`, `h`, `tau`
  - `column_types`:
    - `s`: float
    - `h`: float (negative)
    - `tau`: float (positive)

### avrami_decay.csv
- path: `/app/outputs/avrami_decay.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Time evolution of spin populations for Avrami's law verification. Checker computes total positive fraction, loads tau from reversal_times.csv, and checks linearity of ln(total_fraction/N) vs (t/tau)^3 for t>tau (negative slope, R^2 > 0.98). Also verifies peaks in N_5_2, N_3_2, N_1_2 occur at t<tau.
- schema:
  - `type`: table
  - `required_columns`: `h`, `t`, `N_7_2`, `N_5_2`, `N_3_2`, `N_1_2`
  - `column_types`:
    - `h`: float
    - `t`: integer (MCSS)
    - `N_7_2`: float (normalized count)
    - `N_5_2`: float
    - `N_3_2`: float
    - `N_1_2`: float

Notes: Both outputs are subjected to structural checks; no absolute numeric tolerances are required. The checker performs model fitting and trend verification internally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reversal_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "s",
          "h",
          "tau"
        ],
        "column_types": {
          "s": "float",
          "h": "float (negative)",
          "tau": "float (positive)"
        }
      },
      "description": "Reversal time data for Becker-Döring scaling analysis. Checker fits piecewise linear models to ln(tau) vs 1/|h| to verify three-regime structure, nucleation-regime slope positive and greater than coalescence-regime slope, and slope ratio consistent with d=2."
    },
    {
      "file": "avrami_decay.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "h",
          "t",
          "N_7_2",
          "N_5_2",
          "N_3_2",
          "N_1_2"
        ],
        "column_types": {
          "h": "float",
          "t": "integer (MCSS)",
          "N_7_2": "float (normalized count)",
          "N_5_2": "float",
          "N_3_2": "float",
          "N_1_2": "float"
        }
      },
      "description": "Time evolution of spin populations for Avrami's law verification. Checker computes total positive fraction, loads tau from reversal_times.csv, and checks linearity of ln(total_fraction/N) vs (t/tau)^3 for t>tau (negative slope, R^2 > 0.98). Also verifies peaks in N_5_2, N_3_2, N_1_2 occur at t<tau."
    }
  ],
  "notes": "Both outputs are subjected to structural checks; no absolute numeric tolerances are required. The checker performs model fitting and trend verification internally."
}
```

## How you are scored
A hidden verifier, which you do not see, evaluates each of the two output files independently. For `reversal_times.csv`, the verifier fits a three‑segment piecewise linear model to ln(tau) vs 1/|h| and checks that the nucleation‑regime slope is positive, that the ratio of the nucleation to coalescence slope lies in the theoretically expected range (approximately 3 for a two‑dimensional system), and that the overall fit quality is high. For `avrami_decay.csv`, it loads the reversal time τ for s=3.5 and each field from your `reversal_times.csv`, computes (t/τ)^3, and fits a straight line to ln(total positive fraction/spins) vs (t/τ)^3 for t > τ, requiring a high R² and a negative slope. It also checks that the columns N_5_2, N_3_2, N_1_2 each peak at a time before τ. Each check contributes a partial score, and the final reward is a weighted sum between 0 and 1. You are not required to report any aggregated metric or fit result yourself; only the raw CSV files defined in the workflow steps are submitted. Do not try to look up any paper‑reported numbers; simply perform the honest Monte‑Carlo simulations and supply the requested raw data.
