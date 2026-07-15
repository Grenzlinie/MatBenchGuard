# Density-of-States Effective Mass from Lattice Thermal Conductivity Fitting

## Problem background
In heavily doped compensated n‑type germanium at liquid‑helium temperatures, the lattice thermal conductivity is dominated by phonon scattering off free electrons. The strength of this electron–phonon interaction depends on the density‑of‑states effective mass m* of the electrons, which in turn reflects band‑structure details and carrier screening effects. By fitting a theoretical model for lattice thermal conductivity to experimental data, one can extract the effective mass ratio m*/m. This task computes m*/m for a set of compensated n‑Ge samples using published experimental conductivity measurements.

## Approach
The thermal conductivity is modeled within the Callaway formalism, which sums contributions from different phonon scattering channels. In the temperature range of interest (1.5–4 K) the dominant resistive channel is electron–phonon scattering; three‑phonon processes are negligible. The electron–phonon relaxation rate is taken from Ziman's unscreened expression, which depends on the phonon frequency, temperature, the longitudinal deformation potential E_l, the density‑of‑states effective mass m*, and standard material constants for germanium (average phonon velocity, atomic mass, atomic volume).

For each sample, the experimental lattice thermal conductivity curve (from Mathur and Pearlman, 1969) is obtained—if necessary by digitizing published figures. The model then treats E_l as a sample‑dependent adjustable parameter and allows m* to vary with temperature. The parameters are tuned to minimize the discrepancy between the theoretical and experimental conductivity curves, yielding best‑fit m*/m values at the five temperatures. The approach is a multi‑parameter optimization problem where the fit quality determines the extracted effective mass.

## Reproduction target
Fit the Callaway‑Ziman thermal conductivity model to the experimental data for the six compensated n‑Ge samples (PGa‑4, PGa‑5, AsGa‑4, AsGa‑5, SbIn‑4′, SbGa‑4′). Extract the best‑fit density‑of‑states effective mass ratio m*/m at each of the measured temperatures: 1.5, 2, 2.5, 3, and 4 K. Write the results to `/app/outputs/m_star_over_m.csv` in the format described under the output file section. The row for sample SbIn‑4′ at 4 K may be omitted because no experimental value was reported.

## Assets

- Mathur & Pearlman experimental thermal conductivity data for compensated n-Ge: 10.1103/PhysRev.180.833

## Workflow steps

### Step 1: Obtain experimental thermal conductivity data
- Role: process
- Action: Retrieve the low‑temperature lattice thermal conductivity data for compensated n‑Ge samples PGa-4, PGa-5, AsGa-4, AsGa-5, SbIn-4', SbGa-4' from Mathur and Pearlman (Phys. Rev. 180, 833, 1969). If only published figures are available, digitize the curves to produce a table of conductivity vs temperature for each sample.
- Evidence: `/app/outputs/experimental_conductivity.csv`

### Step 2: Fit Callaway model and extract m*/m
- Role: scored (load-bearing)
- Action: Implement the Callaway model for lattice thermal conductivity using the Ziman electron‑phonon relaxation rate (unscreened form). Use standard material constants for germanium (phonon velocity, atomic mass, atomic volume). For each sample, treat the deformation potential E_l as a sample‑dependent free parameter and allow m* to vary with temperature. Minimize the discrepancy between the model and the experimental conductivity data to obtain best‑fit m*/m values at the reported temperatures (1.5, 2, 2.5, 3, 4 K). Export the results as a CSV.
- Output file: `/app/outputs/m_star_over_m.csv`
- Format: csv
- Contract: CSV with columns: sample (string, one of PGa-4, PGa-5, AsGa-4, AsGa-5, SbIn-4', SbGa-4'), temperature_K (float, values 1.5, 2.0, 2.5, 3.0, 4.0), m_star_over_m (float). The row for SbIn-4' at 4 K may be absent.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/m_star_over_m.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### m_star_over_m.csv
- path: `/app/outputs/m_star_over_m.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Extracted density‑of‑states effective mass ratios for all measured sample‑temperature combinations. The hidden reference is the paper's Table I values; scoring uses an absolute tolerance of ±0.05 per entry.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `temperature_K`, `m_star_over_m`
  - `units`:
    - `temperature_K`: K
    - `m_star_over_m`: dimensionless

Notes: The experimental data acquisition step (process) is required but not directly scored. The fitting step is load-bearing: the reported m*/m values are compared to the paper's hidden reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "m_star_over_m.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "temperature_K",
          "m_star_over_m"
        ],
        "units": {
          "temperature_K": "K",
          "m_star_over_m": "dimensionless"
        }
      },
      "description": "Extracted density‑of‑states effective mass ratios for all measured sample‑temperature combinations. The hidden reference is the paper's Table I values; scoring uses an absolute tolerance of ±0.05 per entry."
    }
  ],
  "notes": "The experimental data acquisition step (process) is required but not directly scored. The fitting step is load-bearing: the reported m*/m values are compared to the paper's hidden reference."
}
```

## How you are scored
A hidden verifier independently evaluates your `/app/outputs/m_star_over_m.csv` file. It compares each reported `m_star_over_m` value against the reference value for that sample and temperature, using a pre‑defined absolute tolerance. The final reward is the fraction of entries that fall within tolerance, weighted by the importance of this output. Submitting values without actually performing the model fit will not satisfy the tolerance check; the reward depends on computing correct results.
