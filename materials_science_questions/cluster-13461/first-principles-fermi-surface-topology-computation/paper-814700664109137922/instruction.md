# Two-Band Model Magnetoresistance Resonance Simulation

## Problem background
Magnetoresistance (MR) is the change in a material's electrical resistance under an applied magnetic field. In semimetals where both electrons and holes contribute to transport, the two-band model can describe how the longitudinal resistivity depends on the balance of carrier densities and the field strength. Exploring this dependence helps identify conditions that lead to large, non-saturating MR, which is relevant for magnetic sensors and other devices.

## Approach
We use the isotropic semiclassical two-band model. The complex resistivity is given by the formula

\[\hat{\rho} = \frac{1 + \mu\mu' B^2 + i(\mu-\mu')B}{e\big(n\mu + p\mu' + i(p-n)\mu\mu' B\big)},\]

where \(e>0\) is the elementary charge, \(n\) and \(p\) are electron and hole densities, and \(\mu\) and \(\mu'\) are their mobilities. The longitudinal resistivity is the real part \(\rho_{xx} = \operatorname{Re}(\hat{\rho})\).

**All calculations must use the following fixed parameters in SI units:**

- Electron density: \(n = 1\times 10^{24}\,\mathrm{m}^{-3}\) (equivalent to \(1\times 10^{18}\,\mathrm{cm}^{-3}\)). For exact compensation the hole density equals this value; otherwise \(p\) is set according to the required \(p/n\) ratio.
- Electron mobility: \(\mu = 1.0\,\mathrm{m}^{2}/(\mathrm{V}\cdot\mathrm{s})\) (which is also \(1.0\,\mathrm{T}^{-1}\)).
- Hole mobility: \(\mu' = 2.0\,\mathrm{m}^{2}/(\mathrm{V}\cdot\mathrm{s})\) (which is also \(2.0\,\mathrm{T}^{-1}\); this gives \(\mu/\mu' = 2\)).
- Elementary charge: \(e = 1.602176634\times 10^{-19}\,\mathrm{C}\).

The magnetic field \(B\) is expressed in tesla (T).

Using these parameters guarantees that the simulation is well‑posed and the resulting CSV contains the structural signatures expected by the hidden verifier.

## Reproduction target
Produce a CSV file containing computed longitudinal resistivity (or magnetoresistance MR = \((\rho_{xx}(B)-\rho_0)/\rho_0\)) for each combination of \(B\) and \(p/n\). The file must include rows for magnetic fields \(B = 1, 2, 4, 8, 12\) T and for \(p/n\) ratios from 0.95 to 1.05 in steps no larger than 0.01, and must also include the exact compensation point \(p/n = 1\) for every field value. The data in the file will be examined for the structural trends it exhibits.

## Assets
No external datasets, pre-trained models, or specialized software packages are required. The two-band model can be implemented using standard numerical libraries (e.g., NumPy, SciPy) in any programming language of your choice.

## Workflow steps

### Step 1: Two-band model simulation
- Role: scored (load-bearing)
- Action: Implement the isotropic two-band semiclassical model using the complex resistivity formula and the fixed parameters listed in the Approach section. Evaluate the longitudinal resistivity (or magnetoresistance) over a grid of magnetic fields B = 1, 2, 4, 8, 12 T and hole-to-electron density ratios p/n from 0.95 to 1.05 in steps ≤0.01. Use the exact electron density n = 1×10²⁴ m⁻³ for all calculations and set the hole density as p = (p/n) × n. Save the results to step_01_two_band_results.csv.
- Output file: `/app/outputs/step_01_two_band_results.csv`
- Format: csv
- Contract: CSV with header: B, p_over_n, value. B: magnetic field (T), p_over_n: hole-to-electron density ratio (dimensionless), value: longitudinal resistivity rho_xx (Ω·cm) or magnetoresistance MR (dimensionless). Must include rows for B in {1,2,4,8,12} and p_over_n ranging 0.95 to 1.05 in steps ≤0.01, with p_over_n=1 included for each B.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_two_band_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_two_band_results.csv
- path: `/app/outputs/step_01_two_band_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Magnetoresistance resonance data: longitudinal resistivity or MR as a function of magnetic field B and compensation ratio p/n.
- schema:
  - `type`: table
  - `required_columns`: `B`, `p_over_n`, `value`
  - `units`:
    - `B`: T
    - `p_over_n`: dimensionless
    - `value`: either Ω·cm (resistivity) or dimensionless (MR)

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_two_band_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "B",
          "p_over_n",
          "value"
        ],
        "units": {
          "B": "T",
          "p_over_n": "dimensionless",
          "value": "either Ω·cm (resistivity) or dimensionless (MR)"
        }
      },
      "description": "Magnetoresistance resonance data: longitudinal resistivity or MR as a function of magnetic field B and compensation ratio p/n."
    }
  ]
}
```

## How you are scored
A hidden verifier reads the submitted CSV and assesses certain structural features. The exact scoring metrics are undisclosed, and no additional information about the expected trends is provided.