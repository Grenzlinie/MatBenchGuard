# Superposition-Induced Frequency Errors in Ultrasound Flow Meters

## Problem background
Ultrasonic flow meters measure fluid velocity by emitting ultrasound pulses upstream and downstream. In frequency‑pulse meters, the difference between the self‑circulation frequencies is proportional to the flow velocity. However, reverberation—particularly ultrasound signals that are doubly reflected by the transducer surfaces—can superimpose on the basic received signal. This superposition alters the amplitude and phase of the composite signal, causing the trigger detector to register a time‑shifted detection instant. The resulting change in the effective self‑circulation period introduces systematic errors in the measured frequency difference. The task quantifies these errors and examines how they depend on the emission frequency.

## Approach
The superposition of the basic signal and one doubly reflected signal is modelled as the addition of two sinusoidal oscillations of the same emission frequency. Closed‑form expressions yield the composite amplitude and phase. The phase change relative to the basic signal defines a phase‑induced time shift t_d', while the amplitude change at the trigger‑threshold level yields an amplitude‑induced time shift t_d''. These shifts modify the downstream self‑circulation period, giving adjusted frequency differences Δf' and Δf''. Normalising by the undisturbed frequency difference Δf produces relative errors δ' (phase‑induced) and δ'' (amplitude‑induced). The computation uses a fixed set of physically plausible parameters: a basic signal with unit amplitude and zero phase, a specified reflected‑signal phase offset, known upstream and downstream periods, and a fixed trigger‑threshold fraction. The amplitude of the reflected signal is set to two representative ratios corresponding to fluoroplastic‑protected ceramics (low reflection) and all‑metal assemblies (higher reflection). By evaluating the formulas at three different emission frequencies while keeping all other parameters constant, the dependence of the errors on frequency can be characterised.

## Reproduction target
Compute the relative errors δ' and δ'' for the fluoroplastic and metal assembly types at emission frequencies of 1 MHz, 2 MHz, and 4 MHz, using the fixed input parameters listed in Step 1. Produce a single CSV file `superposition_errors.csv` containing one row per (assembly_type, frequency) combination with columns: assembly_type, frequency_MHz, delta_prime, and delta_double_prime, ordered by increasing frequency.

## Assets

- Python 3: python3

## Workflow steps

### Step 1: Compute superposition‑induced errors
- Role: scored (load-bearing)
- Action: Implement the algebraic formulas for composite amplitude and phase, compute the phase-induced time shift t_d', amplitude-induced time shift t_d'', altered frequencies Δf' and Δf'', and relative errors δ' and δ''. Use the fixed input parameters: basic signal amplitude A_c = 1.0, basic phase φ_c = 0 rad, doubly reflected phase φ₁ = π/6 rad, self-circulation periods t_u = 1.0e-5 s and t_d = 1.01e-5 s, trigger threshold fraction m_c = 0.1, and for the reflected amplitude A₁ use ratios: 0.09 (fluoroplastic) and 0.225 (metal). For each assembly type and emission frequency f = 1.0, 2.0, 4.0 MHz, compute δ' and δ'' and write one row to superposition_errors.csv.
- Output file: `/app/outputs/superposition_errors.csv`
- Format: csv
- Contract: Columns: assembly_type (string, 'fluoroplastic' or 'metal'), frequency_MHz (float, 1.0, 2.0, or 4.0), delta_prime (float, relative phase-induced error), delta_double_prime (float, relative amplitude-induced error). One row per combination, ordered by increasing frequency.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/superposition_errors.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### superposition_errors.csv
- path: `/app/outputs/superposition_errors.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed relative phase-induced (δ') and amplitude-induced (δ'') frequency errors for two assembly types (fluoroplastic, metal) at three emission frequencies (1, 2, 4 MHz).
- schema:
  - `type`: table
  - `required_columns`: `assembly_type`, `frequency_MHz`, `delta_prime`, `delta_double_prime`
  - `units`:
    - `frequency_MHz`: MHz
    - `delta_prime`: dimensionless
    - `delta_double_prime`: dimensionless

Notes: The input parameters are fixed and provided in the step action. The agent must use the exact formulas from the paper; no external dataset is needed. The checker recomputes expected values from the same formulas and also verifies that errors decrease monotonically with increased frequency.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "superposition_errors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "assembly_type",
          "frequency_MHz",
          "delta_prime",
          "delta_double_prime"
        ],
        "units": {
          "frequency_MHz": "MHz",
          "delta_prime": "dimensionless",
          "delta_double_prime": "dimensionless"
        }
      },
      "description": "Computed relative phase-induced (δ') and amplitude-induced (δ'') frequency errors for two assembly types (fluoroplastic, metal) at three emission frequencies (1, 2, 4 MHz)."
    }
  ],
  "notes": "The input parameters are fixed and provided in the step action. The agent must use the exact formulas from the paper; no external dataset is needed. The checker recomputes expected values from the same formulas and also verifies that errors decrease monotonically with increased frequency."
}
```

## How you are scored
A hidden verifier independently evaluates your `superposition_errors.csv`. The score from the single workflow stage makes up the final reward (total weight 1.0). The verifier recomputes δ' and δ'' from the same deterministic formulas and compares your reported values to reference values using a relative tolerance (value accuracy). It also checks that within each assembly type both delta_prime and delta_double_prime never increase as frequency increases (monotonicity check). Half of the reward comes from value accuracy and half from the monotonicity check. You must perform the computation yourself; merely guessing or copying numbers is unlikely to pass both the tolerance and trend requirements.
