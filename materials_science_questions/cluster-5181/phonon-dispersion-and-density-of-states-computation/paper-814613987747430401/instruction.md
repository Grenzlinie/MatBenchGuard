# Phonon Dispersion and Density of States of Thallium Using MAS Force-Constant Models

## Problem background
Thallium (Tl) is an hcp metal that transforms to a bcc structure at 507 K, a relatively low temperature compared with other hcp metals. Understanding how the lattice vibration frequencies change with temperature is important for probing the mechanism of the hcp-to-bcc transition, as well as for interpreting superconducting tunneling spectra that depend on the phonon density of states. This task aims to compute the phonon dispersion relations and the phonon density of states of Tl at 77 K and 296 K from force-constant models fitted to neutron inelastic scattering measurements.

## Approach
The approach is to model the lattice dynamics with the modified axially symmetric (MAS) force-constant model for hcp crystals, parameterised by central and bond-bending force constants up to sixth nearest neighbours. The dynamical matrix is block-diagonalized for symmetry directions following established formulations. Experimental phonon frequencies measured by neutron scattering along the Δ and Σ directions at 77 K and 296 K (supplied as tables) are used together with the known elastic constants to fit the model parameters by nonlinear least‑squares. The fitted models are then used to compute phonon dispersion curves along all high-symmetry directions (T, R, S, U, P) and the phonon density of states by sampling the Brillouin zone. No further external data are required – all necessary inputs are provided.

## Reproduction target
Given (i) the tabulated neutron data for Tl at 77 K and 296 K (mode, reduced wave vector, energy, and error as listed in the instruction), (ii) the hcp crystal structure (lattice parameters a=3.456 Å, c=5.525 Å at 296 K; a=3.446 Å, c=5.503 Å at 77 K), (iii) the atomic mass of Tl (204.38 amu), and (iv) the experimental elastic constants (from the reference by Ferris, Shepard, and Smith), implement the MAS force‑constant model. Fit the model to the neutron data and elastic constants to obtain the preferred parameter sets (model 1A at 77 K and model 1B at 296 K). Using the fitted parameters, compute the phonon dispersion curves along the T, R, S, U and P directions, the phonon density of states F(ω) on a 0–12 meV grid, and the phonon frequencies at the high‑symmetry points Γ, M, A, L, H, K. From the computed DOS, extract the peak positions and the high‑frequency cutoff. Report all results in the specified CSV and JSON files, including the fitted force‑constant parameters, goodness‑of‑fit χ², DOS curves, dispersion frequencies, and the extracted DOS peak positions and cutoff.

## Assets

- DeWames et al. (1965) - Dynamical matrix and force-constant definitions for hcp MAS model: 10.1103/PhysRev.138.A717
- Warren (1968) - Block-diagonalized dynamical matrix for hexagonal crystals: 10.1103/RevModPhys.40.38
- Ferris, Shepard, Smith (1963) - Elastic constants of Tl: 10.1063/1.1729354
- Python scientific computing packages (numpy, scipy, lmfit): pip

## Workflow steps

### Step 1: Fit MAS model to 77 K neutron data and elastic constants
- Role: scored
- Action: Implement the MAS model force-constant expressions and dynamical matrix for hcp crystals (following DeWames et al. and Warren). Load the 77 K neutron data (provided as input tables) and the experimental elastic constants. Perform nonlinear least-squares fitting to obtain model 1A parameters. Output the fitted force constants and χ² as a CSV file.
- Output file: `/app/outputs/fitted_params_77K.csv`
- Format: csv
- Contract: Table with columns: parameter_name, value. Rows for K1, epsilon_1x, alpha_2, beta_2x, K3, epsilon_3x, alpha_4, beta_4x, K5, epsilon_5x, alpha_6, beta_6x, sigma_B, chi_squared. Value units: dyn/cm for force constants, dimensionless for sigma_B and chi_squared.
- Scoring: scored by hidden verifier

### Step 2: Fit MAS model to 296 K neutron data and elastic constants
- Role: scored
- Action: Using the same MAS model implementation, load the 296 K neutron data (provided as input tables) and experimental elastic constants, and fit to obtain model 1B parameters. Output the fitted force constants and χ² as a CSV file.
- Output file: `/app/outputs/fitted_params_296K.csv`
- Format: csv
- Contract: Same as fitted_params_77K.csv: columns parameter_name, value. Value units: dyn/cm for force constants, dimensionless for sigma_B and chi_squared.
- Scoring: scored by hidden verifier

### Step 3: Compute phonon dispersion curves and density of states from fitted models
- Role: scored (load-bearing)
- Action: Using the fitted parameters from steps 'step_fit_77K' and 'step_fit_296K', compute the phonon dispersion curves along T, R, S, U, P directions and the phonon density of states (DOS) on a fine frequency grid (0–12 meV) for both 77 K and 296 K models. Save DOS curves as CSV files. Also compute the phonon frequencies at high-symmetry points (Γ, M, A, L, H, K) and save them.
- Output file: `/app/outputs/dos_77K.csv, dos_296K.csv, dispersion_points.csv`
- Format: csv
- Contract: dos_77K.csv: two columns frequency (meV) and dos (arbitrary units). dos_296K.csv: same. dispersion_points.csv: columns temperature, symmetry_point, mode_label, frequency (meV). All computed frequencies at high-symmetry points: Gamma, M, A, L, H, K for both temperatures.
- Scoring: scored by hidden verifier

### Step 4: Extract and report key numerical results
- Role: scored
- Action: From the computed DOS curves, extract the peak positions (local maxima) and the highest frequency (cutoff). Compile the fitted χ² values and report all quantities in a JSON file.
- Output file: `/app/outputs/reported_results.json`
- Format: json
- Contract: JSON object with keys: dos_77K_peaks (list of floats, meV), dos_77K_cutoff (float, meV), dos_296K_peaks (list of floats, meV), dos_296K_cutoff (float, meV), chi_squared_77K (float), chi_squared_296K (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_params_77K.csv`
- `/app/outputs/fitted_params_296K.csv`
- `/app/outputs/dos_77K.csv`
- `/app/outputs/dos_296K.csv`
- `/app/outputs/dispersion_points.csv`
- `/app/outputs/reported_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_params_77K.csv
- path: `/app/outputs/fitted_params_77K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Force-constant parameters for the preferred 77 K MAS model (model 1A) and the chi_squared goodness-of-fit.
- schema:
  - `type`: table
  - `required_columns`: `parameter_name`, `value`
  - `units`:
    - `value`: dyn/cm for force constants, dimensionless for sigma_B

### fitted_params_296K.csv
- path: `/app/outputs/fitted_params_296K.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Force-constant parameters for the preferred 296 K MAS model (model 1B) and the chi_squared goodness-of-fit.
- schema:
  - `type`: table
  - `required_columns`: `parameter_name`, `value`
  - `units`:
    - `value`: dyn/cm for force constants, dimensionless for sigma_B

### dos_77K.csv
- path: `/app/outputs/dos_77K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Phonon density of states computed from the 77 K MAS model. The checker will recompute peak positions and cutoff from this file.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `dos`
  - `units`:
    - `frequency`: meV
    - `dos`: arbitrary

### dos_296K.csv
- path: `/app/outputs/dos_296K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Phonon density of states computed from the 296 K MAS model. The checker will recompute peak positions and cutoff from this file.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `dos`
  - `units`:
    - `frequency`: meV
    - `dos`: arbitrary

### dispersion_points.csv
- path: `/app/outputs/dispersion_points.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Phonon frequencies at the high-symmetry points Gamma, M, A, L, H, K for both 77 K and 296 K models.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `symmetry_point`, `mode_label`, `frequency`
  - `units`:
    - `frequency`: meV

### reported_results.json
- path: `/app/outputs/reported_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reported DOS peak positions, cutoff frequencies, and chi-squared values extracted from the computed data.
- schema:
  - `type`: object
  - `required`: `dos_77K_peaks`, `dos_77K_cutoff`, `dos_296K_peaks`, `dos_296K_cutoff`, `chi_squared_77K`, `chi_squared_296K`
  - `properties`:
    - `dos_77K_peaks`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: meV
    - `dos_77K_cutoff`:
      - `type`: number
      - `unit`: meV
    - `dos_296K_peaks`:
      - `type`: array
      - `items`:
        - `type`: number
        - `unit`: meV
    - `dos_296K_cutoff`:
      - `type`: number
      - `unit`: meV
    - `chi_squared_77K`:
      - `type`: number
    - `chi_squared_296K`:
      - `type`: number

Notes: The checker recomputes peak positions and the cutoff from the dos CSV files and compares to the paper's reference values within tolerances. The fitted parameters are validated against the paper's Table III and V. For 296 K, the checker will recompute the DOS from the submitted fitted parameters using a hidden reference implementation and compare the reported peaks and cutoff to that recomputed reference.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_params_77K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter_name",
          "value"
        ],
        "units": {
          "value": "dyn/cm for force constants, dimensionless for sigma_B"
        }
      },
      "description": "Force-constant parameters for the preferred 77 K MAS model (model 1A) and the chi_squared goodness-of-fit."
    },
    {
      "file": "fitted_params_296K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "parameter_name",
          "value"
        ],
        "units": {
          "value": "dyn/cm for force constants, dimensionless for sigma_B"
        }
      },
      "description": "Force-constant parameters for the preferred 296 K MAS model (model 1B) and the chi_squared goodness-of-fit."
    },
    {
      "file": "dos_77K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "dos"
        ],
        "units": {
          "frequency": "meV",
          "dos": "arbitrary"
        }
      },
      "description": "Phonon density of states computed from the 77 K MAS model. The checker will recompute peak positions and cutoff from this file."
    },
    {
      "file": "dos_296K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "dos"
        ],
        "units": {
          "frequency": "meV",
          "dos": "arbitrary"
        }
      },
      "description": "Phonon density of states computed from the 296 K MAS model. The checker will recompute peak positions and cutoff from this file."
    },
    {
      "file": "dispersion_points.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "symmetry_point",
          "mode_label",
          "frequency"
        ],
        "units": {
          "frequency": "meV"
        }
      },
      "description": "Phonon frequencies at the high-symmetry points Gamma, M, A, L, H, K for both 77 K and 296 K models."
    },
    {
      "file": "reported_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "dos_77K_peaks",
          "dos_77K_cutoff",
          "dos_296K_peaks",
          "dos_296K_cutoff",
          "chi_squared_77K",
          "chi_squared_296K"
        ],
        "properties": {
          "dos_77K_peaks": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "meV"
            }
          },
          "dos_77K_cutoff": {
            "type": "number",
            "unit": "meV"
          },
          "dos_296K_peaks": {
            "type": "array",
            "items": {
              "type": "number",
              "unit": "meV"
            }
          },
          "dos_296K_cutoff": {
            "type": "number",
            "unit": "meV"
          },
          "chi_squared_77K": {
            "type": "number"
          },
          "chi_squared_296K": {
            "type": "number"
          }
        }
      },
      "description": "Reported DOS peak positions, cutoff frequencies, and chi-squared values extracted from the computed data."
    }
  ],
  "notes": "The checker recomputes peak positions and the cutoff from the dos CSV files and compares to the paper's reference values within tolerances. The fitted parameters are validated against the paper's Table III and V. For 296 K, the checker will recompute the DOS from the submitted fitted parameters using a hidden reference implementation and compare the reported peaks and cutoff to that recomputed reference."
}
```

## How you are scored
A hidden verifier will independently score each output file produced in the workflow steps. The verifier recomputes quantities from your raw artifacts (e.g., it reads your DOS curves, extracts peaks and the cutoff, and compares them to reference values; it reads your fitted parameters and checks them against expected values). It will not simply trust a self‑reported number unless validated. The final reward is a weighted combination of the per‑artifact scores. You must therefore generate all intermediate raw files and follow the output contract exactly.
