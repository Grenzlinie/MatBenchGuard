# Kinetic Monte Carlo Simulation of Magnetization Reversal in Fe and Co Atomic Chains

## Problem background
Finite-size atomic chains such as Fe on Cu₂N/Cu(001) and Co on Pt(997) exhibit magnetic hysteresis and thermal magnetization reversal. The magnetic properties can be described by the classical Heisenberg Hamiltonian with uniaxial anisotropy. Kinetic Monte Carlo (kMC) simulations are a powerful tool to compute the reversal time of magnetization, but the simplest kMC model assumes that all magnetic moments are collinear with the easy axis and that the rotation of one moment does not affect others, neglecting noncollinear relaxation effects. When the magnetic anisotropy is not much larger than the exchange, noncollinear domain-wall states become important. Improved kMC models that account for these relaxation effects can yield more accurate reversal times. The central task is to compute the reversal time for antiferromagnetic Fe chains and ferromagnetic Co chains using simple kMC, improved kMC models that incorporate pre-calculated diffusion barriers, and an analytical single-domain-wall approximation, and to compare the results, thereby quantifying the influence of relaxation on the reversal time.

## Approach
The kinetic Monte Carlo method is used to simulate spontaneous magnetization reversal. For the simple kMC model, each magnetic moment is restricted to two collinear states (up/down). The transition rates are determined by the energy barrier for a single spin flip, which depends on the local exchange field and the anisotropy constant K. For the antiferromagnetic Fe chain (J = 1.3 meV, K = 3.0 meV), the improved kMC model I inherits the same set of metastable states as the simple model but replaces the analytical rates with Arrhenius rates (ν = ν₀ exp(–Eᵈ/k_B T)). The diffusion barriers Eᵈ for domain-wall formation at the edge, wall disappearance, and wall motion are provided (E₁ᴰ = 4.32 meV, E₂ᴰ = 2.76 meV, E₃ᴰ = 1.72 meV) and account for the relaxation of noncollinear magnetic moments during a spin flip. For the ferromagnetic Co chain (J = 7.5 meV, K = 2.0 meV), the domain-wall width is several atoms; therefore the improved kMC model II uses a set of etalon domain-wall states (clockwise/anti-clockwise domain walls and anti-domain walls). At each kMC step, the algorithm identifies the current metastable state by mapping the magnetization profile to these etalon states, and transitions (formation/disappearance at edges, pair formation/disappearance, domain-wall motion, clockwise↔anticlockwise flipping) are attempted with Arrhenius rates using the given barriers E₁ᴰ = 10.7 meV, E₂ᴰ = 0.0034 meV, E₃ᴰ = 0.0065 meV. Separately, an analytical estimate of the reversal time is obtained from a single‑domain-wall random-walk model, where the mean first‑passage time depends on the same barrier-coupled rates and the chain length; for the antiferromagnetic chain there are n = 2 possible edge states, while for the ferromagnetic chain the effective length is N_eff = N – 10 and n = 4. For each system, kMC simulations are run for every required temperature T and chain length N, averaging over 1000 independent remagnetization events to obtain a reliable mean reversal time.

## Reproduction target
Produce two CSV files containing computed reversal times for Fe and Co atomic chains. For the Fe chain on Cu₂N/Cu(001) (J = 1.3 meV, K = 3.0 meV), record reversal_time_s (in seconds) for the conditions: (i) chain length N = 10 at temperatures T = 4.0, 5.0, 6.0, 7.0 K; (ii) temperature T = 4.0 K at chain lengths N = 5, 10, 15, 20. For each condition, provide results for the three models: simple_kMC, improved_kMC, and analytical. For the Co chain on Pt(997) (J = 7.5 meV, K = 2.0 meV), record reversal_time_s for the conditions: (i) N = 40 at T = 10.0, 15.0, 20.0, 30.0 K; (ii) T = 10.0 K at N = 20, 25, 30, 40. Again, include results for simple_kMC, improved_kMC, and analytical. The analytical model for Co must use the effective chain length N_eff = N – 10. Each CSV must have columns: temperature_K, chain_length_N, model, reversal_time_s, with one row per condition–model combination. The files must be written to /app/outputs/fe_reversal_times.csv and /app/outputs/co_reversal_times.csv, respectively.

## Assets

- Fe chain Heisenberg parameters and diffusion barriers
- Co chain Heisenberg parameters and diffusion barriers
- Python scientific stack (numpy): numpy

## Workflow steps

### Step 1: Compute Fe chain reversal times (simple kMC, improved kMC I, analytical)
- Role: scored (load-bearing)
- Action: Implement a kinetic Monte Carlo simulator for the antiferromagnetic Fe chain (J=1.3 meV, K=3.0 meV). For the simple kMC model use the Glauber rates based on the Heisenberg Hamiltonian; for the improved kMC model I use Arrhenius rates with the provided barriers E1D=4.32 meV, E2D=2.76 meV, E3D=1.72 meV, classifying each attempted spin flip by the domain‑wall event it creates. Also compute the analytical reversal time using the single domain‑wall approximation with n=2 and the same barriers. For every required (T, N) condition, run KMC simulations averaged over 1000 remagnetizations and the analytical calculation. Write all results to fe_reversal_times.csv.
- Output file: `/app/outputs/fe_reversal_times.csv`
- Format: csv
- Contract: Columns: temperature_K (float), chain_length_N (int), model (string: simple_kMC, improved_kMC, analytical), reversal_time_s (float). One row per condition–model combination.
- Scoring: scored by hidden verifier

### Step 2: Compute Co chain reversal times (simple kMC, improved kMC II, analytical)
- Role: scored (load-bearing)
- Action: Implement a kinetic Monte Carlo simulator for the ferromagnetic Co chain (J=7.5 meV, K=2.0 meV). Use simple kMC rates based on the Heisenberg Hamiltonian. For the improved kMC model II, search metastable states via etalon domain‑wall mapping and apply Arrhenius rates with the barriers E1D=10.7 meV, E2D=0.0034 meV, E3D=0.0065 meV, interpreting each event type (formation/disappearance at edge, pair formation/disappearance, motion along chain, clockwise↔anticlockwise transition). Compute the analytical reversal time using the single domain‑wall approximation with n=4 and effective chain length Neff = N–10. For every (T, N) condition, run KMC simulations averaged over 1000 remagnetizations and the analytical calculation. Write all results to co_reversal_times.csv.
- Output file: `/app/outputs/co_reversal_times.csv`
- Format: csv
- Contract: Columns: temperature_K (float), chain_length_N (int), model (string: simple_kMC, improved_kMC, analytical), reversal_time_s (float). One row per condition–model combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fe_reversal_times.csv`
- `/app/outputs/co_reversal_times.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fe_reversal_times.csv
- path: `/app/outputs/fe_reversal_times.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reported reversal times for the Fe chain under specified temperature/chain‑length conditions by simple kMC, improved kMC I, and analytical methods.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `chain_length_N`, `model`, `reversal_time_s`
  - `units`:
    - `temperature_K`: Kelvin
    - `reversal_time_s`: seconds

### co_reversal_times.csv
- path: `/app/outputs/co_reversal_times.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reported reversal times for the Co chain under specified temperature/chain‑length conditions by simple kMC, improved kMC II, and analytical methods.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `chain_length_N`, `model`, `reversal_time_s`
  - `units`:
    - `temperature_K`: Kelvin
    - `reversal_time_s`: seconds

Notes: The agent must not implement GNEB barrier computation; listed barriers are provided directly. Reversal time values will be compared to hidden paper‑derived reference values within appropriate tolerances, and structural consistency (improved_kMC < simple_kMC, analytical within factor 2 of improved_kMC) will be verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fe_reversal_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "chain_length_N",
          "model",
          "reversal_time_s"
        ],
        "units": {
          "temperature_K": "Kelvin",
          "reversal_time_s": "seconds"
        }
      },
      "description": "Reported reversal times for the Fe chain under specified temperature/chain‑length conditions by simple kMC, improved kMC I, and analytical methods."
    },
    {
      "file": "co_reversal_times.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "chain_length_N",
          "model",
          "reversal_time_s"
        ],
        "units": {
          "temperature_K": "Kelvin",
          "reversal_time_s": "seconds"
        }
      },
      "description": "Reported reversal times for the Co chain under specified temperature/chain‑length conditions by simple kMC, improved kMC II, and analytical methods."
    }
  ],
  "notes": "The agent must not implement GNEB barrier computation; listed barriers are provided directly. Reversal time values will be compared to hidden paper‑derived reference values within appropriate tolerances, and structural consistency (improved_kMC < simple_kMC, analytical within factor 2 of improved_kMC) will be verified."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads your produced CSV files. The verifier compares each reversal_time_s value to a paper-derived reference value using a relative tolerance appropriate to the system and scoring weight. In addition, it checks that the following structural relationships hold for every condition: reversal_time_s for improved_kMC is strictly less than for simple_kMC, and the analytical reversal time lies within a factor of 2 of the improved_kMC value. The overall reward is a weighted sum that combines the accuracy of the reported reversal times and the satisfaction of the trend checks, with the main head-to-head reversal-time comparisons carrying the majority of the weight. You do not need to know the hidden reference values; simply executing the described kMC simulations and analytical calculations honestly will produce a high score. Providing only the paper's reported numbers without genuine computation will not pass the structural checks and is unlikely to meet all tolerances.
