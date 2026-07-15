# Molecular Dynamics Simulation of Mechanical Properties of h-BN Grain Boundaries

## Problem background
Two-dimensional hexagonal boron nitride (h-BN) exhibits exceptional mechanical properties, but real samples contain grain boundaries (GBs) that can alter strength and failure behaviour. Understanding how the presence, type, and density of grain boundaries, as well as external parameters such as strain rate and temperature, affect the mechanical response of h‑BN sheets is essential for predicting performance in nanodevices and composites. Molecular dynamics simulations offer a way to investigate these influences by computing stress‑strain curves and extracting key mechanical properties. The present task asks you to systematically explore the roles of grain‑boundary linear density, strain rate, and temperature on the Young’s modulus, ultimate tensile strength, and critical failure strain of h‑BN monolayers.

## Approach
The work uses classical molecular dynamics with a Tersoff potential parametrised for h‑BN (Kinaci et al.). The potential parameters are provided explicitly in the task instructions; no external download of the potential file is required. All simulations are performed with the open‑source LAMMPS package.

Monolayer h‑BN sheets are built with periodic in‑plane boundary conditions and a vacuum layer of 100 Å to decouple periodic images. Pristine sheets and grain‑boundary models defined by pairs of translation vectors (n_L,m_L)|(n_R,m_R) are constructed. The models are first thermally relaxed at 300 K, and then uniaxial tensile tests are carried out perpendicular to the grain‑boundary line (for pristine sheets both the zigzag and armchair directions are tested). Stress–strain curves are recorded, from which Young’s modulus, ultimate tensile strength (peak stress), and critical failure strain (strain at the point of stress drop) are extracted.

A representative set of grain‑boundary configurations is chosen to cover different GB linear densities and to allow a study of the separate effects of strain rate and temperature. The approach isolates each variable: baseline mechanical properties are measured for pristine h‑BN and for GB (6,5)|(5,6) and GB (1,3)|(3,1) at a fixed temperature and strain rate; the strain‑rate dependence is obtained by varying the rate while holding temperature constant for a single GB model; the temperature dependence is obtained by varying temperature while holding the strain rate constant for the same model. This workflow makes it possible to compare the properties of pristine and GB‑containing sheets and to follow how the ultimate tensile strength responds to changes in loading rate and thermal conditions.

## Reproduction target
You must compute and report the following quantities in the specified CSV files:

1. **Baseline mechanical properties** (file `pristine_gb_properties.csv`):
   - For pristine h‑BN loaded along the zigzag (zz) and armchair (am) directions, and for the grain‑boundary models GB (6,5)|(5,6) and GB (1,3)|(3,1) loaded perpendicular to the GB line, all at 300 K and a strain rate of 1 × 10⁸ s⁻¹, extract:
     - Young’s modulus (GPa)
     - Ultimate tensile strength (GPa)
     - Critical failure strain (%)

2. **Strain‑rate effect** (file `strain_rate_effect.csv`):
   - For the grain‑boundary model GB (2,1)|(1,2) at 300 K, extract the ultimate tensile strength (GPa) at three strain rates: 1 × 10⁸, 1 × 10⁹, and 1 × 10¹⁰ s⁻¹.

3. **Temperature effect** (file `temperature_effect.csv`):
   - For the grain‑boundary model GB (2,1)|(1,2) at a strain rate of 1 × 10⁸ s⁻¹, extract the ultimate tensile strength (GPa) at three temperatures: 1 K, 300 K, and 1100 K.

The required output schemas are given in the workflow steps. All simulations must use the provided Tersoff potential and follow the relaxation and loading protocols described in the process steps.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov

### Tersoff potential parameters for h-BN (Kinaci et al.)

The potential parameters from the paper are reproduced here. You must use these exact values for all LAMMPS simulations.

| Parameter | N-N | B-B | B-N or N-B |
|-----------|-----|-----|-------------|
| m | 3.0 | 3.0 | 3.0 |
| γ | 1.0 | 1.0 | 1.0 |
| λIII (Å⁻¹) | 0.0 | 0.0 | 0.0 |
| c | 17.7959 | 0.52629 | 25000 |
| d | 5.9484 | 0.001587 | 4.3484 |
| h | 0.00000 | 0.5 | -0.89000 |
| n | 0.6184432 | 3.9929061 | 0.72751 |
| β | 0.019251 | 0.0000016 | 0.000000125724 |
| λII (Å⁻¹) | 2.6272721 | 2.0774982 | 2.199 |
| B (eV) | 138.77866 | 43.132016 | 340.0 |
| R (Å) | 2.0 | 2.0 | 1.95 |
| D (Å) | 0.1 | 0.1 | 0.05 |
| λI (Å⁻¹) | 2.8293093 | 2.2372578 | 3.568 |
| A (eV) | 128.86866 | 40.0520156 | 1380.0 |

## Workflow steps

### Step 1: Construct atomic models
- Role: process
- Action: Create LAMMPS input data files for pristine h-BN sheet and grain-boundary models (GB (6,5)|(5,6), GB (1,3)|(3,1), GB (2,1)|(1,2)) using periodic boundary conditions in-plane and a vacuum layer of 100 Å. The pristine lattice constant is 2.52 Å and B–N bond length 1.45 Å. GB models defined by their (n_L,m_L)|(n_R,m_R) vectors.
- Evidence: `/app/outputs/model_construction.log`

### Step 2: Structural relaxation via MD
- Role: process
- Action: Relax all structures at 300 K using LAMMPS with the Tersoff potential: first a constant-pressure ensemble (NPT), then a constant-temperature ensemble (NVT). Verify that the relaxed pristine h-BN has a lattice constant close to 2.52 Å and B–N bond length ~1.45 Å.
- Evidence: `/app/outputs/relaxation_output.tar.gz`

### Step 3: Baseline tensile test simulations
- Role: process
- Action: Perform uniaxial tensile tests perpendicular to the GB line (for pristine: along zigzag and armchair directions) at 300 K and constant strain rate 1×10^8 s⁻¹. For GB (2,1)|(1,2) also run at 300 K, 1×10^8 s⁻¹ (shared with baseline). Output stress-strain data (e.g., LAMMPS dump files).
- Evidence: `/app/outputs/baseline_tensile_data.log`

### Step 4: Tensile test simulations – strain rate variation
- Role: process
- Action: For GB (2,1)|(1,2) only, run uniaxial tensile tests at 300 K with strain rates 1×10^9 and 1×10^{10} s⁻¹.
- Evidence: `/app/outputs/strain_rate_tensile.log`

### Step 5: Tensile test simulations – temperature variation
- Role: process
- Action: For GB (2,1)|(1,2) only, run uniaxial tensile tests at temperatures 1 K and 1100 K with strain rate 1×10^8 s⁻¹.
- Evidence: `/app/outputs/temperature_tensile.log`

### Step 6: Extract baseline mechanical properties
- Role: scored (load-bearing)
- Action: From the baseline tensile test stress-strain curves, compute Young's modulus (from initial linear slope), ultimate tensile strength (peak stress), and critical failure strain (strain at stress drop) for pristine (zz and am), GB (6,5)|(5,6), and GB (1,3)|(3,1). For the grain-boundary models, the loading direction is perpendicular to the GB line; record it as 'ww' in the direction column. Write results to pristine_gb_properties.csv.
- Output file: `/app/outputs/pristine_gb_properties.csv`
- Format: csv
- Contract: model,direction,youngs_modulus_GPa,ultimate_tensile_strength_GPa,critical_failure_strain_pct
- Scoring: scored by hidden verifier

### Step 7: Extract strain rate effect
- Role: scored
- Action: For GB (2,1)|(1,2), extract ultimate tensile strength from the stress-strain curves at strain rates 1×10^8, 1×10^9, and 1×10^{10} s⁻¹ (300 K). Write to strain_rate_effect.csv.
- Output file: `/app/outputs/strain_rate_effect.csv`
- Format: csv
- Contract: model,strain_rate_s-1,ultimate_tensile_strength_GPa
- Scoring: scored by hidden verifier

### Step 8: Extract temperature effect
- Role: scored
- Action: For GB (2,1)|(1,2), extract ultimate tensile strength from the stress-strain curves at temperatures 1 K, 300 K, and 1100 K (strain rate 1×10^8 s⁻¹). Write to temperature_effect.csv.
- Output file: `/app/outputs/temperature_effect.csv`
- Format: csv
- Contract: model,temperature_K,ultimate_tensile_strength_GPa
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_gb_properties.csv`
- `/app/outputs/strain_rate_effect.csv`
- `/app/outputs/temperature_effect.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_gb_properties.csv
- path: `/app/outputs/pristine_gb_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Mechanical properties of pristine h-BN and two GB models under baseline conditions (300 K, 1×10^8 s⁻¹).
- schema:
  - `type`: table
  - `required_columns`: `model`, `direction`, `youngs_modulus_GPa`, `ultimate_tensile_strength_GPa`, `critical_failure_strain_pct`
  - `units`:
    - `youngs_modulus_GPa`: GPa
    - `ultimate_tensile_strength_GPa`: GPa
    - `critical_failure_strain_pct`: %

### strain_rate_effect.csv
- path: `/app/outputs/strain_rate_effect.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ultimate tensile strength of GB (2,1)|(1,2) at three strain rates.
- schema:
  - `type`: table
  - `required_columns`: `model`, `strain_rate_s-1`, `ultimate_tensile_strength_GPa`
  - `units`:
    - `strain_rate_s-1`: s⁻¹
    - `ultimate_tensile_strength_GPa`: GPa

### temperature_effect.csv
- path: `/app/outputs/temperature_effect.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ultimate tensile strength of GB (2,1)|(1,2) at three temperatures.
- schema:
  - `type`: table
  - `required_columns`: `model`, `temperature_K`, `ultimate_tensile_strength_GPa`
  - `units`:
    - `temperature_K`: K
    - `ultimate_tensile_strength_GPa`: GPa

Notes: The checker compares the reported mechanical properties to paper-reported reference values with tolerances and verifies that the ultimate tensile strength exhibits the expected monotonic trends (increasing with strain rate, decreasing with temperature). No hidden gold values or tolerances are disclosed in the public contract.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_gb_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "direction",
          "youngs_modulus_GPa",
          "ultimate_tensile_strength_GPa",
          "critical_failure_strain_pct"
        ],
        "units": {
          "youngs_modulus_GPa": "GPa",
          "ultimate_tensile_strength_GPa": "GPa",
          "critical_failure_strain_pct": "%"
        }
      },
      "description": "Mechanical properties of pristine h-BN and two GB models under baseline conditions (300 K, 1×10^8 s⁻¹)."
    },
    {
      "file": "strain_rate_effect.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "strain_rate_s-1",
          "ultimate_tensile_strength_GPa"
        ],
        "units": {
          "strain_rate_s-1": "s⁻¹",
          "ultimate_tensile_strength_GPa": "GPa"
        }
      },
      "description": "Ultimate tensile strength of GB (2,1)|(1,2) at three strain rates."
    },
    {
      "file": "temperature_effect.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "temperature_K",
          "ultimate_tensile_strength_GPa"
        ],
        "units": {
          "temperature_K": "K",
          "ultimate_tensile_strength_GPa": "GPa"
        }
      },
      "description": "Ultimate tensile strength of GB (2,1)|(1,2) at three temperatures."
    }
  ],
  "notes": "The checker compares the reported mechanical properties to paper-reported reference values with tolerances and verifies that the ultimate tensile strength exhibits the expected monotonic trends (increasing with strain rate, decreasing with temperature). No hidden gold values or tolerances are disclosed in the public contract."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the three scored CSV files (`pristine_gb_properties.csv`, `strain_rate_effect.csv`, `temperature_effect.csv`). For each output, the verifier compares your reported values to expected reference values within appropriate tolerances and checks that the data exhibit physically reasonable structural relationships (e.g., monotonic trends where expected) that a correct simulation should satisfy. The verifier does NOT disclose the reference values or tolerances.

Each output carries a weight that reflects its importance to the overall reproduction claim. The final reward is a weighted sum over the individual stage scores, normalised to the range [0, 1]. To obtain a high score you must both achieve close numerical agreement with the hidden reference and ensure that the reported values follow the physically required patterns. Simply writing numbers that appear plausible or copying values from a source will not pass the verifier’s checks; the workflow must be executed faithfully to produce the reported results.
