# Universal Phase Diagram of Dimensional Crossover from Coherent Fraction Data

## Problem background
Ultracold bosonic atoms confined in anisotropic optical lattices provide a highly tunable platform to explore how quantum coherence depends on dimensionality. By varying the depths of a two-dimensional triangular lattice (in the x-y plane) and a one-dimensional lattice (along z), the system can be driven from a three-dimensional superfluid through dimensional crossovers into lower-dimensional regimes. The zero-momentum coherent fraction, extracted from time-of-flight absorption images along different directions, serves as a sensitive and directional probe of quantum coherence. The goal of this task is to map out the phase boundaries in such a system: specifically, to determine the critical lattice depths at which coherence is lost along each direction for several temperatures, and to locate the transition temperatures at which the coherent fraction vanishes for a set of representative anisotropy points.

## Approach
The analysis uses the public experimental dataset (Zenodo) containing measured zero-momentum fractions f_c^y and f_c^z as functions of the lattice depths V_2D, V_1D and temperature T. To find the critical lattice depths, for each fixed temperature we isolate one-dimensional cuts: f_c^y vs V_2D with a small, fixed V_1D (for the y-direction crossover), and f_c^z vs V_1D with a small, fixed V_2D (for the z-direction crossover). A piecewise linear fit is applied to each cut; the critical depth V_c is defined as the lattice depth where the two linear segments meet, marking the change from a rapidly falling regime to a nearly saturated plateau. For the transition temperatures, at each anisotropy point I–VI we extract temperature-dependent data for f_c^y and f_c^z and apply a similar piecewise fit (or a plateau‑detection method) to determine the temperature where the coherent fraction drops to a small, temperature-independent floor. The entire procedure relies solely on the experimental coherent fractions; no theoretical models or simulations are required.

## Reproduction target
From the Zenodo dataset (DOI 10.5281/zenodo.15308183), produce two scored artifacts:

- `critical_lattice_depths.csv`: For each of the four initial BEC temperatures (23 nK, 36 nK, 199 nK, 223 nK), the critical lattice depth V_c (in units of the recoil energy E_r) and its fitting error for both the y-direction (derived from f_c^y vs V_2D cuts at small V_1D) and the z-direction (derived from f_c^z vs V_1D cuts at small V_2D). Each row corresponds to one temperature and direction.

- `transition_temperatures.json`: For the six anisotropy points I–VI, the transition temperature and its error along both the y and z directions (all in nK). The points are defined as:
  I:   V_2D=3.0 E_r, V_1D=20.0 E_r
  II:  V_2D=7.0 E_r, V_1D=5.0 E_r
  III: V_2D=0.5 E_r, V_1D=1.0 E_r
  IV:  V_2D=3.0 E_r, V_1D=50.0 E_r
  V:   V_2D=21.0 E_r, V_1D=5.0 E_r
  VI:  V_2D=25.0 E_r, V_1D=60.0 E_r

## Assets

- Probing universal phase diagram of dimensional crossover dataset: 10.5281/zenodo.15308183

## Workflow steps

### Step 1: Load experimental dataset
- Role: process
- Action: Download the dataset from Zenodo (DOI 10.5281/zenodo.15308183) and load the data into arrays of temperature T, lattice depths V_2D, V_1D, and zero-momentum fractions f_c^y, f_c^z. Verify data coverage for the required temperature conditions (23, 36, 199, 223 nK) and the six anisotropy points (I-VI).
- Evidence: `/app/outputs/dataset_summary.log`

### Step 2: Extract critical lattice depths
- Role: scored (load-bearing)
- Action: For each of the four target temperatures (23, 36, 199, 223 nK), isolate scans of f_c^y vs V_2D at fixed small V_1D (for the 3D→1D/2D crossover) and f_c^z vs V_1D at fixed small V_2D (for the 3D→2D/1D crossover). Implement piecewise linear fitting to identify the critical lattice depth V_c at the change between the rapidly decaying and the saturated regimes. Output one row per (temperature, direction) pair with the estimated V_c and its fitting error.
- Output file: `/app/outputs/critical_lattice_depths.csv`
- Format: csv
- Contract: Columns: temperature_nK (float), direction (str, one of 'y','z'), V_c_Er (float), error_Er (float). One row per critical point determined.
- Scoring: scored by hidden verifier

### Step 3: Extract transition temperatures
- Role: scored (load-bearing)
- Action: For each of the six anisotropy points (I: V_2D=3.0 E_r, V_1D=20.0 E_r; II: V_2D=7.0 E_r, V_1D=5.0 E_r; III: V_2D=0.5 E_r, V_1D=1.0 E_r; IV: V_2D=3.0 E_r, V_1D=50.0 E_r; V: V_2D=21.0 E_r, V_1D=5.0 E_r; VI: V_2D=25.0 E_r, V_1D=60.0 E_r), extract the temperature-dependent f_c^y and f_c^z data from the dataset. Apply piecewise linear fitting (or plateau detection) to identify the transition temperatures where f_c^y and f_c^z drop to a small, temperature-independent plateau. Output the transition temperature and its error for each direction.
- Output file: `/app/outputs/transition_temperatures.json`
- Format: json
- Contract: JSON object whose keys are point labels ('I','II','III','IV','V','VI') and values are dictionaries: {'T_c_y_nK': float, 'error_y_nK': float, 'T_c_z_nK': float, 'error_z_nK': float}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_lattice_depths.csv`
- `/app/outputs/transition_temperatures.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_lattice_depths.csv
- path: `/app/outputs/critical_lattice_depths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical lattice depths determined from piecewise fits of coherent fraction vs. lattice depth. One row per (temperature, direction) pair.
- schema:
  - `type`: table
  - `required_columns`: `temperature_nK`, `direction`, `V_c_Er`, `error_Er`
  - `units`:
    - `temperature_nK`: nK
    - `V_c_Er`: E_r
    - `error_Er`: E_r

### transition_temperatures.json
- path: `/app/outputs/transition_temperatures.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Transition temperatures for six anisotropy points, determined from piecewise fits of coherent fraction vs. temperature.
- schema:
  - `type`: object
  - `required_properties`: `I`, `II`, `III`, `IV`, `V`, `VI`
  - `value_structure`:
    - `T_c_y_nK`: number (nK)
    - `error_y_nK`: number (nK)
    - `T_c_z_nK`: number (nK)
    - `error_z_nK`: number (nK)

Notes: Values are compared to hidden reference values from the paper using tolerances (±1 E_r for lattice depths, ±20 nK or experimental error for temperatures).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_lattice_depths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_nK",
          "direction",
          "V_c_Er",
          "error_Er"
        ],
        "units": {
          "temperature_nK": "nK",
          "V_c_Er": "E_r",
          "error_Er": "E_r"
        }
      },
      "description": "Critical lattice depths determined from piecewise fits of coherent fraction vs. lattice depth. One row per (temperature, direction) pair."
    },
    {
      "file": "transition_temperatures.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_properties": [
          "I",
          "II",
          "III",
          "IV",
          "V",
          "VI"
        ],
        "value_structure": {
          "T_c_y_nK": "number (nK)",
          "error_y_nK": "number (nK)",
          "T_c_z_nK": "number (nK)",
          "error_z_nK": "number (nK)"
        }
      },
      "description": "Transition temperatures for six anisotropy points, determined from piecewise fits of coherent fraction vs. temperature."
    }
  ],
  "notes": "Values are compared to hidden reference values from the paper using tolerances (±1 E_r for lattice depths, ±20 nK or experimental error for temperatures)."
}
```

## How you are scored
A hidden verifier reads your produced CSV and JSON files and compares each value to a hidden reference derived from independent analysis. For critical lattice depths, your reported V_c is checked against a reference value within a prescribed tolerance; for transition temperatures, a similar comparison is performed with an appropriate tolerance. The verifier also validates that the output schemas are correct (required columns/keys, presence of all expected conditions). The final reward is a weighted combination of the scores from the two scored steps, with each artifact contributing a substantial share. Simply reporting known literature values without re‑deriving them from the dataset will not pass the verifier.
