# Transient Junction Temperature Calculation for Pulsed Laser Diodes

## Problem background
In pulsed GaAs injection lasers, transient heating of the active region causes the emission wavelength to shift during a current pulse. Understanding this heating is essential for predicting spectral behaviour and for applications such as spectroscopic absorption measurements and interferometry. This task addresses the thermal side of the problem: compute the transient temperature increase at the center of the laser junction for a known current pulse shape, using a semi-infinite solid approximation and a convolution integral that accounts for the power dissipated by optical reabsorption and nonradiative recombination.

## Approach
The thermal model treats the diode crystal as a semi‑infinite solid, with one face held at a constant heat‑sink temperature. The temperature rise ΔT_c(t) at the junction centre is given by the integral equation

$$
\Delta T_{\mathrm{c}}(t)=\frac{1}{\varrho c V} \int_{0}^{t} P(\tau)\, \frac{\mathrm{d}}{\mathrm{d}\tau} \Delta T_{\mathrm{c}}(t-\tau) \,\mathrm{d}\tau \qquad (1)
$$

where  
- \(\varrho = 5370\,\mathrm{kg\,m^{-3}}\) is the density,  
- \(c = 320\,\mathrm{J\,kg^{-1}\,K^{-1}}\) the specific heat,  
- \(V = 1.4\times10^{-13}\,\mathrm{m^{3}}\) the junction volume, and  
- \(P(\tau) = 1.4\cdot I(\tau)\) is the power dissipated in the junction (optical reabsorption and nonradiative recombination).  

The current pulse is assumed to have the bell‑shaped form  

$$
I(t)=I_{\max}\left(\frac{t}{t_m}\right)^{2} \exp\!\left(-2\frac{t}{t_m}+2\right), \qquad I_{\max}=40\,\mathrm{A}.
$$

The parameter \(t_m\) (the time at which the pulse reaches its maximum) takes the values 30, 50, 70, and 90 ns.

**Numerical solution of the integral equation**

Eq. (1) is a Volterra integral equation that can be solved by time‑stepping on a uniform grid. Discretise time with step \(\Delta t\) and write \(t_n = n\Delta t\). Let \(\Delta T_n \equiv \Delta T_{\mathrm{c}}(t_n)\) and \(P_n \equiv P(t_n)\). Approximating the derivative inside the integral by a backward difference leads to the explicit recurrence

\[
\Delta T_0 = 0,\qquad
\Delta T_n = \frac{1}{\varrho c V} \sum_{j=1}^{n-1} P_j\, \bigl(\Delta T_{n-j} - \Delta T_{n-j-1}\bigr), \quad n\ge 1.
\]

This formula can be evaluated sequentially for n = 1, 2, … until the desired final time. A recommended discretisation is \(\Delta t = 0.1\,\mathrm{ns}\) and a total simulation time of \(t_{\max}=150\,\mathrm{ns}\), which comfortably covers the 100 ns sampling window and the post‑pulse cooling. Using a smaller step further improves accuracy.

The material parameters, pulse shape and the above recurrence together define a deterministic numerical integration; the computed \(\Delta T_c\) values are unambiguous.

## Reproduction target
Compute the transient junction‑centre temperature increase \(\Delta T_c(t)\) for each of the four pulse widths \(t_m = 30\,\mathrm{ns},\; 50\,\mathrm{ns},\; 70\,\mathrm{ns},\; 90\,\mathrm{ns}\). Extract the temperature values at the five time points \(t = 20\,\mathrm{ns},\; 40\,\mathrm{ns},\; 60\,\mathrm{ns},\; 80\,\mathrm{ns},\; 100\,\mathrm{ns}\) after the start of the current pulse. Save the results as a CSV file with columns `t_ns`, `tm_30_K`, `tm_50_K`, `tm_70_K`, `tm_90_K`, where each row corresponds to one time point and the columns contain the corresponding \(\Delta T_c\) in Kelvin.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Transient junction temperature calculation
- Role: scored (load-bearing)
- Action: Implement the thermal model described in the Approach section. Use the recurrence formula to numerically solve the integral equation for the junction‑center temperature increase \(\Delta T_c(t)\). Apply the specified material parameters and the bell‑shaped current pulse. Compute \(\Delta T_c(t)\) for each \(t_m = 30, 50, 70, 90\,\mathrm{ns}\) over a time range that includes the sampling points. Extract the temperature values at \(t = 20, 40, 60, 80, 100\,\mathrm{ns}\) for each \(t_m\) and save them to `temperature_values.csv`.
- Output file: `/app/outputs/temperature_values.csv`
- Format: csv
- Contract: Header: `t_ns,tm_30_K,tm_50_K,tm_70_K,tm_90_K`. Rows: one per time point (20, 40, 60, 80, 100 ns). Temperature values are floating‑point numbers in Kelvin.
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