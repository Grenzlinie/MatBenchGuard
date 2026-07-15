# Slanted Grating Optimization for Unidirectional SPP Excitation

## Problem background
Unidirectional coupling of normally incident light to surface plasmon polaritons (SPPs) is desirable for integrated plasmonic on-chip signal routing. With a symmetric surface-relief grating under normal incidence, counter-propagating SPPs are excited with equal efficiency. Slanted gratings break this symmetry, allowing preferential excitation of a single SPP direction. The key numerical task is to determine the grating parameters that maximize the amplitude of the -1st diffracted evanescent order relative to the +1st order while simultaneously suppressing the reflected zeroth order, thereby enabling efficient unidirectional coupling.

## Approach
The reproduction employs rigorous coupled-wave analysis (RCWA) to model a one-dimensional slanted lamellar aluminium grating. The grating is defined by its period d = 600 nm, groove width c = 0.4d, and the aluminium refractive index n = 1.378 + i 7.616. The structure is illuminated in TM polarization at normal incidence with wavelength λ = 632.8 nm. For a grid of groove depths h (0–200 nm) and inclination angles α (0°–40°), the RCWA simulation computes the complex reflected magnetic-field amplitudes for the -1st, zeroth, and +1st diffraction orders. From these amplitudes, the ratio |H_{z,-1}^+|/|H_{z,+1}^+| and the zeroth-order amplitude |H_{z,0}^+| are evaluated. The resulting parameter map is used to locate the (h,α) that gives the highest ratio while maintaining a low zeroth-order amplitude. The workflow uses the open-source S4 RCWA tool and standard Python libraries.

## Reproduction target
Perform an RCWA sweep over the full grid of groove heights (0–200 nm) and inclination angles (0°–40°) for the specified lamellar grating geometry and material constants. Produce two scored artifacts:
1. **amplitude_ratio_map.csv** – for every (h,α) pair, the amplitude ratio |H_{z,-1}^+|/|H_{z,+1}^+| and the zeroth-order reflected amplitude |H_{z,0}^+|.
2. **optimal_parameters.json** – the (h,α) point that maximizes the ratio while keeping the zeroth-order amplitude low, together with the corresponding ratio and zeroth amplitude at that optimum.
The criterion for “low zeroth amplitude” is left to your discretion; the choice will be cross-checked against a hidden reference optimum derived from your map.

## Assets

- S4 – Rigorous Coupled-Wave Analysis software: https://github.com/slankas/S4
- NumPy: numpy
- Pandas: pandas
- SciPy: scipy

## Workflow steps

### Step 1: RCWA simulation of lamellar slanted grating
- Role: process
- Action: Set up an RCWA simulation (using S4 or equivalent) for a one-dimensional slanted lamellar grating with period d=600 nm, groove width c=0.4d, aluminium refractive index n=1.378+7.616i, TM polarization, normal incidence, wavelength λ=632.8 nm. Run the simulation for a fine grid of groove depths h (0–200 nm) and inclination angles α (0–40°). For each (h,α) pair compute the complex reflected magnetic-field amplitudes H_{z,-1}^+, H_{z,0}^+, H_{z,+1}^+.
- Evidence: `/app/outputs/raw_amplitudes.csv`

### Step 2: Amplitude ratio map
- Role: scored (load-bearing)
- Action: From the computed complex amplitudes, calculate for each (h,α) pair the amplitude ratio |H_{z,-1}^+| / |H_{z,+1}^+| and the zeroth‑order reflected amplitude |H_{z,0}^+|. Write a CSV file with columns: h_nm, alpha_deg, ratio, zeroth_amplitude.
- Output file: `/app/outputs/amplitude_ratio_map.csv`
- Format: csv
- Contract: h_nm: numeric (nm), alpha_deg: numeric (degrees), ratio: numeric (dimensionless), zeroth_amplitude: numeric (normalized)
- Scoring: scored by hidden verifier

### Step 3: Optimal grating parameters extraction
- Role: scored
- Action: Read amplitude_ratio_map.csv. Identify the (h,α) pair that yields the largest amplitude ratio while keeping the zeroth‑order amplitude low (apply a reasonable criterion). Report the optimal h, α, period, ratio, and zeroth_amplitude in a JSON file.
- Output file: `/app/outputs/optimal_parameters.json`
- Format: json
- Contract: {"optimal_h_nm": number, "optimal_alpha_deg": number, "period_nm": number, "ratio_at_optimum": number, "zeroth_at_optimum": number}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/amplitude_ratio_map.csv`
- `/app/outputs/optimal_parameters.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### amplitude_ratio_map.csv
- path: `/app/outputs/amplitude_ratio_map.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Full grid of the amplitude ratio |H_z,-1⁺|/|H_z,+1⁺| and the zeroth-order reflected amplitude |H_z,0⁺| as functions of groove depth (nm) and inclination angle (deg). The checker recomputes the optimal point from this data and scores it against the paper's optimal ranges.
- schema:
  - `type`: table
  - `required_columns`: `h_nm`, `alpha_deg`, `ratio`, `zeroth_amplitude`
  - `units`:
    - `h_nm`: nm
    - `alpha_deg`: degrees
    - `ratio`: dimensionless
    - `zeroth_amplitude`: normalized amplitude

### optimal_parameters.json
- path: `/app/outputs/optimal_parameters.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent-reported optimal grating parameters (h, α, period, and the corresponding ratio and zeroth amplitude). The checker verifies that these values are consistent with the agent’s own amplitude_ratio_map.csv.
- schema:
  - `type`: object
  - `required`:
    - `optimal_h_nm`: number
    - `optimal_alpha_deg`: number
    - `period_nm`: number
    - `ratio_at_optimum`: number
    - `zeroth_at_optimum`: number

Notes: The task focuses only on the lamellar grating case with period d=600 nm and groove width c=0.4d. Sinusoidal profiles, Poynting vector maps, and SPP effective index calculation are excluded per the reproduction scope.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "amplitude_ratio_map.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "h_nm",
          "alpha_deg",
          "ratio",
          "zeroth_amplitude"
        ],
        "units": {
          "h_nm": "nm",
          "alpha_deg": "degrees",
          "ratio": "dimensionless",
          "zeroth_amplitude": "normalized amplitude"
        }
      },
      "description": "Full grid of the amplitude ratio |H_z,-1⁺|/|H_z,+1⁺| and the zeroth-order reflected amplitude |H_z,0⁺| as functions of groove depth (nm) and inclination angle (deg). The checker recomputes the optimal point from this data and scores it against the paper's optimal ranges."
    },
    {
      "file": "optimal_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "optimal_h_nm": "number",
          "optimal_alpha_deg": "number",
          "period_nm": "number",
          "ratio_at_optimum": "number",
          "zeroth_at_optimum": "number"
        }
      },
      "description": "Agent-reported optimal grating parameters (h, α, period, and the corresponding ratio and zeroth amplitude). The checker verifies that these values are consistent with the agent’s own amplitude_ratio_map.csv."
    }
  ],
  "notes": "The task focuses only on the lamellar grating case with period d=600 nm and groove width c=0.4d. Sinusoidal profiles, Poynting vector maps, and SPP effective index calculation are excluded per the reproduction scope."
}
```

## How you are scored
A hidden verifier reads your amplitude_ratio_map.csv and independently locates the (h,α) point that yields the highest amplitude ratio while enforcing a hidden zeroth‑amplitude ceiling. The resulting optimal depth and angle are compared against a trusted reference range that reflects the paper’s reported optimum. Full credit is awarded if both parameters fall within the reference range; partial credit is given if only one does. The verifier additionally checks that your optimal_parameters.json reports a point consistent with its own recomputed optimum from your map; significant discrepancies result in a penalty. The final score is a weighted combination of these checks. Simply reporting numbers without the underlying grid map will not pass the verification.
