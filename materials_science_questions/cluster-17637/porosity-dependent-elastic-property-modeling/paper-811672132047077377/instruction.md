# Elastic moduli from Lamb mode frequencies in mesoporous silica spheres

## Problem background
Monodisperse spherical mesoporous silica particles (MSMSPs) are used in drug delivery, imaging, and other applications where their elastic properties at the nanoscale are critical. Standard ultrasonic methods cannot reach the GHz frequencies needed to probe individual submicrometer spheres. Picosecond pump-probe spectroscopy can excite the fundamental radial Lamb mode, yielding a frequency that depends on the sphere diameter, density, and elastic moduli. This task reproduces the conversion from the measured Lamb mode frequency to the bulk and shear moduli, assuming a constant Poisson ratio of 0.17, using a standard elasticity model.

## Approach
The core of the reproduction is to solve the radial Lamb transcendental equation for the l=0,n=1 mode numerically:

$$k_{\mathrm{T}}^2 j_0(k_{\mathrm{L}}) - 4 k_{\mathrm{L}} j_1(k_{\mathrm{L}}) = 0$$

where $k_{\mathrm{L}} = \pi f_0 D / s_{\mathrm{L}}$, $k_{\mathrm{T}} = \pi f_0 D / s_{\mathrm{T}}$, and the Poisson ratio $\nu = 0.17$ relates the sound velocities via $s_{\mathrm{T}} = s_{\mathrm{L}} \sqrt{(1-2\nu)/(2-2\nu)}$. Solving yields the longitudinal and transverse sound velocities $s_{\mathrm{L}}$ and $s_{\mathrm{T}}$. Then the bulk and shear moduli follow from standard elasticity:

$$B = \rho s_{\mathrm{L}}^2 - \frac{4}{3} G, \quad G = \rho s_{\mathrm{T}}^2$$

The solver must implement numerical root-finding with spherical Bessel functions (from SciPy) for each sample. The provided sample parameters are:

| Sample | $D$ (nm) | Porosity (% vol) | Ni filling (%) | $\rho$ (g/cm³) | $f_0$ (GHz) |
|--------|---------|------------------|----------------|----------------|------------|
| 1A | 1050 | 57 | 3 | 1.05 | 3.53 |
| 1B | 1050 | 57 | 7 | 1.25 | 3.35 |
| 1C | 1050 | 57 | 25 | 2.15 | 3.28 |
| bare_1050 | 1050 | 57 | 0 | 0.90 | 3.68 |
| 2A | 620 | 54 | 3 | 1.10 | 6.24 |
| 2B | 620 | 54 | 9 | 1.41 | 6.01 |
| bare_620 | 620 | 54 | 0 | 0.95 | 6.35 |

## Reproduction target
Given the sample parameters for seven MSMSP samples (provided inline), produce a CSV file `/app/outputs/elastic_params_msmsp.csv` containing one row per sample with columns: `sample` (string), `sL_km_s` (float, km/s), `sT_km_s` (float, km/s), `B_GPa` (float, GPa), `G_GPa` (float, GPa). The samples are: 1A, 1B, 1C, bare_1050, 2A, 2B, bare_620. The solver must obtain the sound velocities and moduli from the Lamb equation solution as described.

## Assets

- Python 3
- SciPy: scipy
- NumPy: numpy

## Workflow steps

### Step 1: Compute elastic moduli from Lamb mode frequencies
- Role: scored (load-bearing)
- Action: Write a Python script that reads the sample parameters (sample_id, D in nm, porosity, Ni filling factor, density ρ in g/cm³, measured frequency f0 in GHz) for seven samples: 1A, 1B, 1C, bare_1050, 2A, 2B, bare_620. For each sample, numerically solve the radial Lamb transcendental equation for the l=0,n=1 mode (assuming Poisson ratio ν=0.17) to obtain longitudinal sound velocity sL and transverse sound velocity sT. Then compute bulk modulus B = ρ sL² − (4/3) G and shear modulus G = ρ sT². Output a CSV file with one row per sample and columns: sample, sL_km_s, sT_km_s, B_GPa, G_GPa. The solving agent must implement the equation with spherical Bessel functions and root-finding.
- Output file: `/app/outputs/elastic_params_msmsp.csv`
- Format: csv
- Contract: CSV with header: sample, sL_km_s, sT_km_s, B_GPa, G_GPa. Rows for samples: 1A, 1B, 1C, bare_1050, 2A, 2B, bare_620. All numeric values are floats.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elastic_params_msmsp.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elastic_params_msmsp.csv
- path: `/app/outputs/elastic_params_msmsp.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Table of computed elastic parameters for the seven MSMSP samples. The checker compares each value against hidden reference values from the paper's Table 1 within specified tolerances.
- schema:
  - `type`: table
  - `required_columns`: `sample`, `sL_km_s`, `sT_km_s`, `B_GPa`, `G_GPa`
  - `units`:
    - `sL_km_s`: km/s
    - `sT_km_s`: km/s
    - `B_GPa`: GPa
    - `G_GPa`: GPa

Notes: The agent must solve the Lamb equation and convert to moduli. The hidden reference values are directly from the paper's published elastic parameters. The agent is not required to reproduce raw experimental signals or perform extrapolation to bare spheres.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elastic_params_msmsp.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sample",
          "sL_km_s",
          "sT_km_s",
          "B_GPa",
          "G_GPa"
        ],
        "units": {
          "sL_km_s": "km/s",
          "sT_km_s": "km/s",
          "B_GPa": "GPa",
          "G_GPa": "GPa"
        }
      },
      "description": "Table of computed elastic parameters for the seven MSMSP samples. The checker compares each value against hidden reference values from the paper's Table 1 within specified tolerances."
    }
  ],
  "notes": "The agent must solve the Lamb equation and convert to moduli. The hidden reference values are directly from the paper's published elastic parameters. The agent is not required to reproduce raw experimental signals or perform extrapolation to bare spheres."
}
```

## How you are scored
A hidden verifier will check your `elastic_params_msmsp.csv`. It will compare each computed value (`sL_km_s`, `sT_km_s`, `B_GPa`, `G_GPa`) for every sample against predetermined reference values, using per-field tolerances. All seven samples must be present. Full credit is awarded only if all values fall within the required tolerances. The verifier does not require any external network access; it compares your submitted CSV directly. No partial credit is given. The reference values and tolerances are not provided to you.
