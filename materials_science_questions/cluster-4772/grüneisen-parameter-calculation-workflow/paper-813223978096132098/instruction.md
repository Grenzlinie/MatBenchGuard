# Reproduce elastic constants of argon from Brillouin scattering data via cubic elastic forward model fit

## Problem background
Solid argon is a prototypical rare‑gas solid frequently used to test interatomic potentials and lattice‑dynamics theories. Measurements of its adiabatic elastic constants are critical for validating models of cohesion and anharmonicity, yet earlier experimental values from ultrasonic and neutron‑scattering methods were contradictory. Resolving these discrepancies requires an accurate, independent determination of the three cubic elastic constants near the triple point.

## Approach
The determination relies on Brillouin light scattering from small single crystals. In a cubic crystal, the three acoustic branch velocities depend on the three elastic constants C11, C12, C44 and the crystal orientation described by Euler angles. The forward model solves the 3×3 Christoffel‑type secular equation for a rotated wavevector, yielding the longitudinal and transverse mode frequencies. A least‑squares fitting procedure is then used to find the set of elastic constants that best reproduces the observed longitudinal (L) and low‑frequency transverse (T1) Brillouin shifts across multiple crystal orientations. From the fitted constants, the elastic anisotropy A and the Grüneisen parameter γ are derived using literature values for density, thermal expansivity, and specific heat.

## Reproduction target
Using the bundled Brillouin shift data (crystal Euler angles and measured L and T1 frequency shifts) and the provided physical constants, determine the adiabatic elastic constants C11, C12, C44 (in units of 10¹⁰ dyn/cm²), the elastic anisotropy parameter A = 2C44/(C11−C12), and the Grüneisen parameter γ = β Bₛ/(ρ Cₚ) with Bₛ = (C11+2C12)/3. Save these five numbers to `elastic_constants.json`. Also output a table that, for every data point used in the fit, records the measured shift and the frequency predicted by the best‑fit model; save it as `fitted_frequencies.csv`.

## Assets

- Brillouin shift data (Table I)
- Physical constants and reference data
- Python packages: numpy scipy pandas

## Workflow steps

### Step 1: Prepare experimental dataset
- Role: process
- Action: Read the bundled brillouin_data.csv and physical_constants.json. Parse the crystal orientations (Euler angles) and the measured Brillouin frequency shifts (longitudinal L and transverse T1) for each orientation. Compute the scattering wavevector magnitude q = 2 k₀ sin(θ_scat/2) using the appropriate refractive index and laser wavelength (4880 Å for crystals 2 and 3, 6328 Å for crystal 1).
- Evidence: none

### Step 2: Implement forward model (cubic dynamical matrix)
- Role: process
- Action: Implement a function that, given elastic constants (C11, C12, C44) and a crystal orientation described by Euler angles (θ,φ,χ), builds the 3×3 dynamical matrix for a cubic crystal as defined by the paper (λ_ij with components q_i from rotated wavevector), solves the eigenvalue problem, and returns the three acoustic mode frequencies. The forward model must handle the rotation of the wavevector into the crystal coordinate system.
- Evidence: none

### Step 3: Fit elastic constants and compute derived quantities
- Role: scored (load-bearing)
- Action: Using the prepared dataset and the forward model, perform a least‑squares minimization: vary C11, C12, C44 to minimize the sum of squared residuals between the measured and predicted frequency shifts for the L and T1 modes across all available crystal orientations. From the best‑fit constants, compute the elastic anisotropy A = 2C44/(C11−C12), and the Grüneisen parameter γ = β Bs / (ρ Cp) with Bs = (C11+2C12)/3, using the literature values for density, expansivity, and specific heat provided in physical_constants.json. Write the results to elastic_constants.json.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: JSON object with keys: C11 (float, units 1e10 dyn/cm²), C12 (float), C44 (float), A (float, dimensionless), gamma (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 4: Record fitted vs. measured frequencies
- Role: scored
- Action: Export the measured and predicted frequency shifts for every data point used in the fit. Each row corresponds to one mode (L or T1) at one orientation.
- Output file: `/app/outputs/fitted_frequencies.csv`
- Format: csv
- Contract: CSV with columns: crystal (int), phi_deg (float), mode (string, 'L' or 'T1'), measured_shift_GHz (float), predicted_shift_GHz (float). One row per fitting data point.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_constants.json`
- `/app/outputs/fitted_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted adiabatic elastic constants and derived quantities (anisotropy, Grüneisen parameter).
- schema:
  - `type`: object
  - `required`:
    - `C11`: float
    - `C12`: float
    - `C44`: float
    - `A`: float
    - `gamma`: float

### fitted_frequencies.csv
- path: `/app/outputs/fitted_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Table of measured and predicted Brillouin frequency shifts for each data point used in the fit. The checker computes the root-mean-square deviation (RMSD) between measured_shift_GHz and predicted_shift_GHz and compares it to a hidden threshold.
- schema:
  - `type`: table
  - `required_columns`: `crystal`, `phi_deg`, `mode`, `measured_shift_GHz`, `predicted_shift_GHz`

Notes: Elasto-optic constant ratios and uncertainty quantification are omitted from the reproduction; only the central elastic constants and derived quantities are scored. The fitted frequencies file serves as a consistency check that a genuine least-squares fit was carried out.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "float",
          "C12": "float",
          "C44": "float",
          "A": "float",
          "gamma": "float"
        }
      },
      "description": "Fitted adiabatic elastic constants and derived quantities (anisotropy, Grüneisen parameter)."
    },
    {
      "file": "fitted_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "crystal",
          "phi_deg",
          "mode",
          "measured_shift_GHz",
          "predicted_shift_GHz"
        ]
      },
      "description": "Table of measured and predicted Brillouin frequency shifts for each data point used in the fit. The checker computes the root-mean-square deviation (RMSD) between measured_shift_GHz and predicted_shift_GHz and compares it to a hidden threshold."
    }
  ],
  "notes": "Elasto-optic constant ratios and uncertainty quantification are omitted from the reproduction; only the central elastic constants and derived quantities are scored. The fitted frequencies file serves as a consistency check that a genuine least-squares fit was carried out."
}
```

## How you are scored
Your submitted `elastic_constants.json` and `fitted_frequencies.csv` are evaluated by a hidden verifier. The verifier compares the reported elastic constants, anisotropy, and Grüneisen parameter to the paper’s reference values using tolerances appropriate for an independent numerical re‑implementation. Additionally, the verifier reads `fitted_frequencies.csv` and computes the root‑mean‑square deviation between the measured and predicted shifts; this deviation must fall below a preset threshold, confirming that the least‑squares fit was genuinely carried out. The final score is a weighted combination of the accuracy of the constants and the fit quality. Supplying the paper’s numbers without executing the fitting pipeline will not satisfy the verifier.
