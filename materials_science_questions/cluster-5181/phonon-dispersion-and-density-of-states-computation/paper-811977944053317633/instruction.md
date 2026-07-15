# Fit an eleven-parameter shell model to CsF phonon frequencies and compute elastic constants and density of states

## Problem background
Cesium fluoride (CsF) is an alkali halide with a particularly large contribution to the ionic polarizability from the heavy Cs⁺ ion. In contrast to most alkali halides, the electronic polarizability is dominated by the positive ion rather than the negative ion. The lattice dynamics of CsF have been studied by inelastic neutron scattering, which measures the phonon dispersion relations along high-symmetry directions of the crystal. Experimental data at 80 K are available for the [100], [110], and [111] directions, covering both acoustic and optical branches. These phonon frequencies represent the primary input for constraining a theoretical model of the interionic forces.

The measured phonon frequencies at 80 K are provided in the following table (units are 10¹³ rad/s, uncertainties are one standard deviation). The wave vector magnitude q is given in reduced units; for the [110] and [111] directions the listed q values include the respective factors √2 or √3.

| Direction | q       | T1A           | T2A           | LA            | T1O           | T2O           | LO            |
|-----------|---------|---------------|---------------|---------------|---------------|---------------|---------------|
| [100]     | 0.1     | —             | —             | —             | —             | —             | 4.640 ± 0.020 |
| [100]     | 0.2     | 0.283 ± 0.005 | —             | 0.690 ± 0.011 | 2.500 ± 0.015 | —             | 4.590 ± 0.020 |
| [100]     | 0.4     | 0.500 ± 0.006 | —             | 1.210 ± 0.011 | 2.540 ± 0.015 | —             | 4.240 ± 0.030 |
| [100]     | 0.6     | 0.659 ± 0.010 | —             | 1.460 ± 0.020 | 2.570 ± 0.015 | —             | 3.400 ± 0.015 |
| [100]     | 0.7     | —             | —             | —             | —             | —             | 3.160 ± 0.015 |
| [100]     | 0.8     | 0.709 ± 0.010 | —             | 1.480 ± 0.030 | 2.580 ± 0.010 | —             | 2.990 ± 0.020 |
| [100]     | 1.0     | 0.762 ± 0.010 | —             | 1.388 ± 0.015 | 2.600 ± 0.015 | —             | 2.780 ± 0.020 |
| [110]     | 0.2√2   | 0.390 ± 0.003 | —             | 0.835 ± 0.011 | 2.519 ± 0.015 | 2.570 ± 0.020 | 4.560 ± 0.015 |
| [110]     | 0.4     | 0.745 ± 0.006 | 0.555 ± 0.003 | 1.397 ± 0.015 | 2.610 ± 0.020 | 2.690 ± 0.020 | 4.280 ± 0.015 |
| [110]     | 0.6     | 1.066 ± 0.011 | 0.890 ± 0.008 | 1.580 ± 0.015 | 2.690 ± 0.020 | 2.720 ± 0.020 | 3.770 ± 0.030 |
| [110]     | 0.7     | —             | —             | —             | —             | —             | 3.233 ± 0.015 |
| [110]     | 0.8     | 1.308 ± 0.015 | —             | 1.190 ± 0.010 | 2.740 ± 0.020 | 2.650 ± 0.020 | 2.960 ± 0.015 |
| [111]     | 0.1√3   | 0.316 ± 0.005 | —             | 0.523 ± 0.009 | 2.510 ± 0.015 | —             | 4.650 ± 0.020 |
| [111]     | 0.2     | 0.617 ± 0.010 | —             | 0.997 ± 0.010 | 2.590 ± 0.010 | —             | 4.600 ± 0.015 |
| [111]     | 0.3     | 0.826 ± 0.009 | —             | 1.377 ± 0.010 | 2.650 ± 0.015 | —             | 4.540 ± 0.020 |
| [111]     | 0.4     | 0.930 ± 0.011 | —             | 1.680 ± 0.030 | 2.740 ± 0.015 | —             | 4.480 ± 0.030 |
| [111]     | 0.45    | —             | —             | 1.730 ± 0.015 | —             | —             | —             |
| [111]     | 0.5     | 0.981 ± 0.030 | —             | 1.750 ± 0.020 | 2.760 ± 0.015 | —             | 4.440 ± 0.030 |
| [111]     | 0       | —             | —             | —             | 2.480 ± 0.008 | —             | —             |

From these experimental frequencies, a shell model that allows both ions to be polarizable and includes short-range interactions out to second neighbours can be fitted. The fitted model yields the interionic force parameters and allows the computation of derived physical properties: the elastic constants C₁₁, C₁₂, C₄₄, and the phonon density of states (DOS). Your task is to implement this shell model, determine its parameters by fitting to the data above, and produce these derived quantities.

## Approach
A shell model represents the interaction between ions by a long-range Coulomb part and a short-range part that acts through the electron shells. The model treats each ion as a core and a massless shell coupled by a spring; the equations of motion involve the ion masses, charges, shell charges, and force-constant matrices. By setting the core-shell coupling appropriately, the number of free parameters reduces to: A12, B12 (Cs–F short-range), A11, B11 (Cs–Cs), A22, B22 (F–F), the effective ionic charge Z, the electrical polarizabilities α₁ and α₂, and the mechanical polarizabilities d₁ and d₂. The model is fitted by minimizing the χ² statistic, defined as the sum over all measured phonons of ((ω_exp – ω_model)/σ)² divided by (N – K), where σ is the experimental uncertainty, N is the number of data points, and K is the number of free parameters. Once the parameters are determined, the elastic constants are obtained from the long-wavelength (q → 0) limit of the dynamical matrix. The phonon density of states is computed by diagonalizing the dynamical matrix on a fine mesh covering the irreducible Brillouin zone, interpolating to extract approximately 6 × 10⁶ frequencies, and binning them into a histogram of width 0.02 × 10¹³ rad/s over the interval [0, 6] × 10¹³ rad/s.

## Reproduction target
Produce the following three output files:

1. **model4_parameters.json**: A JSON object containing the fitted parameters and the achieved χ². Fields: `A12`, `B12`, `A11`, `B11`, `A22`, `B22` (short-range parameters in units of e²/(2v), where v is the volume per ion pair), `Z` (ionic charge in units of e), `alpha1`, `alpha2` (electrical polarizabilities in units of Å³), `d1`, `d2` (mechanical polarizabilities in units of e), `chi_squared` (dimensionless).

2. **elastic_constants.json**: A JSON object containing the derived elastic constants `C11`, `C12`, `C44`, in units of 10¹¹ dyn/cm².

3. **dos_histogram.csv**: A CSV file with header `frequency_bin_lower, frequency_bin_upper, count`. Each row corresponds to a bin of width 0.02 × 10¹³ rad/s. Bins cover the full range from 0 to 6 × 10¹³ rad/s (300 bins). The count is the number of phonon states falling into that bin, obtained from sampling a total of 6 × 10⁶ phonon frequencies in the irreducible Brillouin zone using an interpolation scheme on a fine mesh.

## Assets

- Experimental phonon frequencies of CsF at 80 K
- Eleven-parameter shell model definition

## Workflow steps

### Step 1: Parse experimental phonon frequencies for CsF at 80 K
- Role: process
- Action: Extract and structure the experimental phonon frequencies and uncertainties from the provided Table 1 of the paper (80 K measurements along Δ, Σ, Λ directions) into a structured dataset suitable for fitting. The table includes mode labels (T1A, T2A, LA, T1O, T2O, LO), reduced wave-vector coordinates, and frequencies in units of 10^13 rad/s.
- Evidence: `/app/outputs/experimental_frequencies.json`

### Step 2: Fit the 11-parameter shell model to the experimental frequencies
- Role: scored (load-bearing)
- Action: Implement the 11-parameter shell model for CsF (both ions polarizable) as described in the paper, with short-range interactions up to second neighbours and long-range Coulomb interactions. Fit its parameters (A12, B12, A11, B11, A22, B22, Z, alpha1, alpha2, d1, d2) to the experimental 80 K phonon frequencies by minimizing χ², and output the fitted parameter values and the resulting χ² value.
- Output file: `/app/outputs/model4_parameters.json`
- Format: json
- Contract: JSON object with numeric keys: A12, B12 (Cs-F short-range), A11, B11 (Cs-Cs), A22, B22 (F-F), Z (ionic charge), alpha1, alpha2 (electrical polarizabilities in Å^3), d1, d2 (mechanical polarizabilities in e), chi_squared (dimensionless fitting error). Units: A,B in e^2/(2v); Z in e.
- Scoring: scored by hidden verifier

### Step 3: Compute elastic constants from the fitted shell model
- Role: scored
- Action: From the fitted shell model parameters, compute the elastic constants C11, C12, C44 using the long-wavelength limit of the shell model. Output the three values.
- Output file: `/app/outputs/elastic_constants.json`
- Format: json
- Contract: JSON object with numeric keys: C11, C12, C44. Units: 10^11 dyn/cm^2.
- Scoring: scored by hidden verifier

### Step 4: Compute phonon density of states histogram
- Role: scored
- Action: Using the fitted model parameters, compute the phonon density of states by sampling 6×10^6 frequencies in the irreducible Brillouin zone via an interpolation scheme on a fine mesh. Bin the frequencies into a histogram with channel width 0.02×10^13 rad/s, covering the range [0,6]×10^13 rad/s (300 bins). Output the histogram as a CSV.
- Output file: `/app/outputs/dos_histogram.csv`
- Format: csv
- Contract: CSV with columns: frequency_bin_lower (float, lower edge of bin, 10^13 rad/s), frequency_bin_upper (float, upper edge of bin, 10^13 rad/s), count (integer, number of phonon states in bin).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/model4_parameters.json`
- `/app/outputs/elastic_constants.json`
- `/app/outputs/dos_histogram.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### model4_parameters.json
- path: `/app/outputs/model4_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted shell model parameters and chi-squared error, to be compared against the paper's reported model 4 values with appropriate tolerances.
- schema:
  - `type`: object
  - `required`:
    - `A12`: number
    - `B12`: number
    - `A11`: number
    - `B11`: number
    - `A22`: number
    - `B22`: number
    - `Z`: number
    - `alpha1`: number
    - `alpha2`: number
    - `d1`: number
    - `d2`: number
    - `chi_squared`: number
  - `units`:
    - `A12`: e^2/(2v)
    - `B12`: e^2/(2v)
    - `A11`: e^2/(2v)
    - `B11`: e^2/(2v)
    - `A22`: e^2/(2v)
    - `B22`: e^2/(2v)
    - `Z`: e
    - `alpha1`: Å^3
    - `alpha2`: Å^3
    - `d1`: e
    - `d2`: e
    - `chi_squared`: dimensionless

### elastic_constants.json
- path: `/app/outputs/elastic_constants.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elastic constants derived from the fitted model, compared to the paper's reported model 4 elastic constants.
- schema:
  - `type`: object
  - `required`:
    - `C11`: number
    - `C12`: number
    - `C44`: number
  - `units`:
    - `C11`: 10^11 dyn/cm^2
    - `C12`: 10^11 dyn/cm^2
    - `C44`: 10^11 dyn/cm^2

### dos_histogram.csv
- path: `/app/outputs/dos_histogram.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon DOS histogram. The structural audit checks for a clear TO peak near 2.75×10^13 rad/s (±0.05), a gap between acoustic (below ~2.0) and optical (above ~2.4) regions, and the TO peak count within 20% of the paper's figure.
- schema:
  - `type`: table
  - `required_columns`: `frequency_bin_lower`, `frequency_bin_upper`, `count`
  - `units`:
    - `frequency_bin_lower`: 10^13 rad/s
    - `frequency_bin_upper`: 10^13 rad/s
    - `count`: integer

Notes: All outputs are produced from the fitted model parameters; the model fitting step is load-bearing. The target policies reflect the nature of the artifacts: reference matching for precise fitted and derived numbers, and a structural audit for the histogram shape.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "model4_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "A12": "number",
          "B12": "number",
          "A11": "number",
          "B11": "number",
          "A22": "number",
          "B22": "number",
          "Z": "number",
          "alpha1": "number",
          "alpha2": "number",
          "d1": "number",
          "d2": "number",
          "chi_squared": "number"
        },
        "units": {
          "A12": "e^2/(2v)",
          "B12": "e^2/(2v)",
          "A11": "e^2/(2v)",
          "B11": "e^2/(2v)",
          "A22": "e^2/(2v)",
          "B22": "e^2/(2v)",
          "Z": "e",
          "alpha1": "Å^3",
          "alpha2": "Å^3",
          "d1": "e",
          "d2": "e",
          "chi_squared": "dimensionless"
        }
      },
      "description": "Fitted shell model parameters and chi-squared error, to be compared against the paper's reported model 4 values with appropriate tolerances."
    },
    {
      "file": "elastic_constants.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "C11": "number",
          "C12": "number",
          "C44": "number"
        },
        "units": {
          "C11": "10^11 dyn/cm^2",
          "C12": "10^11 dyn/cm^2",
          "C44": "10^11 dyn/cm^2"
        }
      },
      "description": "Elastic constants derived from the fitted model, compared to the paper's reported model 4 elastic constants."
    },
    {
      "file": "dos_histogram.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_bin_lower",
          "frequency_bin_upper",
          "count"
        ],
        "units": {
          "frequency_bin_lower": "10^13 rad/s",
          "frequency_bin_upper": "10^13 rad/s",
          "count": "integer"
        }
      },
      "description": "Phonon DOS histogram. The structural audit checks for a clear TO peak near 2.75×10^13 rad/s (±0.05), a gap between acoustic (below ~2.0) and optical (above ~2.4) regions, and the TO peak count within 20% of the paper's figure."
    }
  ],
  "notes": "All outputs are produced from the fitted model parameters; the model fitting step is load-bearing. The target policies reflect the nature of the artifacts: reference matching for precise fitted and derived numbers, and a structural audit for the histogram shape."
}
```

## How you are scored
Your submission will be evaluated by an automated verifier that independently checks each of the three artifacts. The verifier has access to reference values derived from the original analysis, but these values are not disclosed to you. The scoring works as follows:

- The model parameters (A12, B12, A11, B11, A22, B22, Z, alpha1, alpha2, d1, d2, chi_squared) are compared against the reference values; agreement within appropriate tolerances earns full credit, with partial credit for larger deviations.
- The elastic constants (C11, C12, C44) are compared similarly.
- The DOS histogram is checked for structural features: the presence of a transverse optical peak near a characteristic frequency, a gap between the acoustic and optical branches, and the overall shape of the distribution. The verifier does not merely count rows or check bin boundaries; it assesses whether the histogram correctly captures the physical features expected from the fitted model.

The final score is a weighted combination of the scores for the three artifacts. Reporting numbers that appear plausible without actually performing the fitting and computation steps will not pass the verification checks, because the verifier examines the internal consistency and the structural features of the histogram that can only be obtained by running the full model.
