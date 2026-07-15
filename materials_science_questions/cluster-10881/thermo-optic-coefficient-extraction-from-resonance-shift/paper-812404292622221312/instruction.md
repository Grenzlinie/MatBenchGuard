# Transient Junction Temperature Calculation for Pulsed Laser Diodes

## Problem background
In pulsed GaAs injection lasers, transient heating of the active region causes the emission wavelength to shift during a current pulse. Understanding this heating is essential for predicting spectral behaviour and for applications such as spectroscopic absorption measurements and interferometry. This task addresses the thermal side of the problem: compute the transient temperature increase at the center of the laser junction for a known current pulse shape, using a semi-infinite solid approximation and a convolution integral that accounts for the power dissipated by optical reabsorption and nonradiative recombination.

## Approach
The thermal model treats the diode crystal as a semi‑infinite solid, with one face held at a constant heat‑sink temperature. The temperature rise ΔT_c(t) at the junction centre is given by a self‑consistent convolution integral that couples the dissipated power P(τ) with the temperature response of the medium. The power is taken as P(t)=1.4·I(t), where I(t) is the drive current. For this task, the current pulse is assumed to have a bell shape of the form I(t)=I_max·(t/t_m)²·exp(−2t/t_m+2), with I_max=40 A and the peak time t_m taking the values 30, 50, 70, and 90 ns. The material parameters are the density ρ=5370 kg/m³, specific heat c=320 J/(kg·K), and junction volume V=1.4×10⁻¹³ m³. The integral equation must be solved numerically over a time window that covers the pulse and the post‑pulse cooling. The solution produces the junction temperature increase ΔT_c(t) as a function of time for each pulse width.

## Reproduction target
Compute the transient junction‑centre temperature increase ΔT_c(t) for each of the four pulse widths t_m = 30 ns, 50 ns, 70 ns, and 90 ns. Extract the temperature values at the five time points t = 20 ns, 40 ns, 60 ns, 80 ns, and 100 ns after the start of the current pulse. Save the results as a CSV file with columns t_ns, tm_30_K, tm_50_K, tm_70_K, and tm_90_K, where each row corresponds to one time point and the columns contain the corresponding ΔT_c in Kelvin.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Transient junction temperature calculation
- Role: scored (load-bearing)
- Action: Implement the thermal model: numerically solve the convolution equation for the junction‑center temperature increase ΔT_c(t) using the semi-infinite solid approximation. Use the specified material parameters (ρ=5370 kg/m³, c=320 J/(kg·K), V=1.4×10⁻¹³ m³) and the bell‑shaped current pulse I(t)=I_max·(t/t_m)²·exp(−2t/t_m+2) with I_max=40 A. The power dissipation is P(t)=1.4·I(t). Compute ΔT_c(t) for t_m = 30, 50, 70, 90 ns over a sufficient time range. Extract the temperature values at t = 20, 40, 60, 80, 100 ns for each t_m and save them to temperature_values.csv.
- Output file: `/app/outputs/temperature_values.csv`
- Format: csv
- Contract: Header: t_ns,tm_30_K,tm_50_K,tm_70_K,tm_90_K. Rows: one per time point (20, 40, 60, 80, 100 ns). Temperature values are floating‑point numbers in Kelvin.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_values.csv
- path: `/app/outputs/temperature_values.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Transient junction temperature increase ΔT_c above the heat sink at five time points for four pulse widths t_m (30, 50, 70, 90 ns).
- schema:
  - `type`: table
  - `required_columns`: `t_ns`, `tm_30_K`, `tm_50_K`, `tm_70_K`, `tm_90_K`
  - `units`:
    - `t_ns`: ns
    - `tm_30_K`: K
    - `tm_50_K`: K
    - `tm_70_K`: K
    - `tm_90_K`: K

Notes: The temperature rise is produced by a deterministic numerical integration; scoring is by exact match within a hidden tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "t_ns",
          "tm_30_K",
          "tm_50_K",
          "tm_70_K",
          "tm_90_K"
        ],
        "units": {
          "t_ns": "ns",
          "tm_30_K": "K",
          "tm_50_K": "K",
          "tm_70_K": "K",
          "tm_90_K": "K"
        }
      },
      "description": "Transient junction temperature increase ΔT_c above the heat sink at five time points for four pulse widths t_m (30, 50, 70, 90 ns)."
    }
  ],
  "notes": "The temperature rise is produced by a deterministic numerical integration; scoring is by exact match within a hidden tolerance."
}
```

## How you are scored
A hidden verifier independently scores each workflow step's output artifact and combines the weighted scores into the final reward. For the scored step, the verifier recomputes reference temperature values by solving the same thermal model with a fine‑grained numerical integration. Your submitted CSV is compared point‑by‑point against these reference values. The fraction of values whose absolute deviation falls within an undisclosed tolerance determines the step score. Reporting the paper's published numbers is not sufficient; the verifier judges correctness solely against its own reference computation.
