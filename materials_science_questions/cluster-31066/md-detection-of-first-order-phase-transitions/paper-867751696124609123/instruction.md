# Determining the isotope shift of a liquid-liquid phase transition in hydrogen using path integral simulations

## Problem background
Liquid hydrogen is predicted to undergo a first‑order liquid‑liquid phase transition (LLPT) from an insulating molecular phase to a conducting atomic phase at high pressures and temperatures. Nuclear quantum effects (NQE) arising from zero‑point energy can significantly influence this transition, introducing an isotope effect between H₂ and D₂. This task aims to determine the magnitude of the isotope shift in the LLPT transition pressure at 1000 K for H₂ and D₂.

## Approach
The approach uses ring‑polymer path integral molecular dynamics (PIMD) to include NQE explicitly. Simulations of 180 H₂/D₂ molecules are performed with the i‑PI driver coupled to Quantum Espresso, using the BLYP exchange‑correlation functional and a norm‑conserving pseudopotential. Runs are carried out at 1000 K across a range of pressures that span the expected transition region. From each NVT production trajectory the average volume and pressure are extracted, and the isothermal compressibility κ_T = −(ΔV/Δp)/V is estimated via finite differences. For each isotope the resulting κ_T‑vs‑pressure curve is fitted with a model comprising an exponential background plus a Gaussian peak; the peak centre identifies the transition pressure. The isotope shift ΔP = P_D₂ − P_H₂ is then obtained by comparing the two fitted transition pressures.

## Reproduction target
Produce two scored artifacts:
1. A CSV file containing the raw compressibility data (volume, pressure, and κ_T) for every pressure point and both isotopes.
2. A JSON file containing the fitted transition pressures for H₂ and D₂ and the resulting isotope shift ΔP = P_D₂ − P_H₂.
The CSV provides the basis for independent verification; the JSON reports your best estimate of the transition pressures and the isotope shift.

## Assets

- i-PI universal force engine: https://github.com/i-pi/i-pi
- Quantum Espresso: https://www.quantum-espresso.org
- Norm-conserving hydrogen pseudopotential for BLYP: https://www.quantum-espresso.org/pseudopotentials/

## Workflow steps

### Step 1: Run PIMD simulations for H2 and D2 at 1000 K
- Role: process
- Action: Generate initial configuration of 180 H2/D2 molecules in a cubic box. Using i-PI coupled to Quantum Espresso with the BLYP functional, Baldereschi mean-value k-point sampling, and a norm-conserving pseudopotential, run ring-polymer path integral molecular dynamics for both isotopes at 1000 K across a pressure sequence spanning the transition region. Use P=12 beads for H2 and P=8 beads for D2. Perform brief NPT equilibration followed by NVT production; save centroid trajectories and energies.
- Evidence: none

### Step 2: Compute isothermal compressibility data
- Role: scored (load-bearing)
- Action: From each NVT production run, compute the average volume and centroid-virial pressure. Estimate isothermal compressibility κ_T = -(ΔV/Δp)/V via finite differences. Output a CSV with the results for both isotopes.
- Output file: `/app/outputs/step_02_kappa_T_data.csv`
- Format: csv
- Contract: Columns: isotope (string), pressure_GPa (float), volume_A3_per_atom (float), kappa_T_GPa-1 (float).
- Scoring: scored by hidden verifier

### Step 3: Determine transition pressures and isotope shift
- Role: scored
- Action: Fit the κ_T vs pressure data for each isotope with an exponential background plus a Gaussian peak. Extract the transition pressure from the peak center. Compute the isotope shift ΔP = P_D2 - P_H2. Output a JSON with the fitted pressures and shift.
- Output file: `/app/outputs/step_03_phase_boundary.json`
- Format: json
- Contract: Keys: H2_transition_pressure_GPa (float), D2_transition_pressure_GPa (float), isotope_shift_GPa (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_kappa_T_data.csv`
- `/app/outputs/step_03_phase_boundary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_kappa_T_data.csv
- path: `/app/outputs/step_02_kappa_T_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw compressibility data; the checker recomputes κ_T from volume and pressure and refits the peaks.
- schema:
  - `type`: table
  - `required_columns`: `isotope`, `pressure_GPa`, `volume_A3_per_atom`, `kappa_T_GPa-1`
  - `units`:
    - `pressure_GPa`: GPa
    - `volume_A3_per_atom`: Å³/atom
    - `kappa_T_GPa-1`: 1/GPa

### step_03_phase_boundary.json
- path: `/app/outputs/step_03_phase_boundary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported transition pressures and isotope shift; checker compares shift to hidden paper gold and verifies correct trend (H2 < D2).
- schema:
  - `type`: object
  - `required`: `H2_transition_pressure_GPa`, `D2_transition_pressure_GPa`, `isotope_shift_GPa`
  - `properties`:
    - `H2_transition_pressure_GPa`:
      - `type`: number
      - `unit`: GPa
    - `D2_transition_pressure_GPa`:
      - `type`: number
      - `unit`: GPa
    - `isotope_shift_GPa`:
      - `type`: number
      - `unit`: GPa

Notes: The scored target is the isotope shift ΔP = P_D2 - P_H2 at 1000 K, determined from compressibility peaks. The CSV provides the raw data enabling independent refitting by the checker.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_kappa_T_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "isotope",
          "pressure_GPa",
          "volume_A3_per_atom",
          "kappa_T_GPa-1"
        ],
        "units": {
          "pressure_GPa": "GPa",
          "volume_A3_per_atom": "Å³/atom",
          "kappa_T_GPa-1": "1/GPa"
        }
      },
      "description": "Raw compressibility data; the checker recomputes κ_T from volume and pressure and refits the peaks."
    },
    {
      "file": "step_03_phase_boundary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "H2_transition_pressure_GPa",
          "D2_transition_pressure_GPa",
          "isotope_shift_GPa"
        ],
        "properties": {
          "H2_transition_pressure_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "D2_transition_pressure_GPa": {
            "type": "number",
            "unit": "GPa"
          },
          "isotope_shift_GPa": {
            "type": "number",
            "unit": "GPa"
          }
        }
      },
      "description": "Agent-reported transition pressures and isotope shift; checker compares shift to hidden paper gold and verifies correct trend (H2 < D2)."
    }
  ],
  "notes": "The scored target is the isotope shift ΔP = P_D2 - P_H2 at 1000 K, determined from compressibility peaks. The CSV provides the raw data enabling independent refitting by the checker."
}
```

## How you are scored
A hidden verifier independently reads your submitted CSV, recomputes κ_T from the volume‑pressure pairs, re‑fits the κ_T curves with exponential‑plus‑Gaussian models, and extracts transition pressures and the isotope shift. It then compares your reported shift (from the JSON) to the expected value from the paper. Credit is awarded based on how closely your result agrees with that reference. A secondary consistency check verifies that the shift derived from your raw CSV data is compatible with the JSON you reported. The two scored artifacts are combined with appropriate weights to produce the final reward.
