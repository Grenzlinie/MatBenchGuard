# Photonic band gap evolution and guided modes in elastomer-embedded photonic crystals

## Problem background
Two-dimensional photonic crystals composed of GaAs rods embedded in silicone elastomer are studied theoretically. Under external vibrations, the rods move because of the elastomer's elasticity, and this motion alters the photonic band structure dynamically. The work models the rods as a mass–spring lattice and solves Maxwell's equations to investigate how photonic band gaps evolve over time and whether guided modes appear when the elastomer is confined to a single rod array. The open task is to compute how the bandgap-to-midgap ratio changes during one quarter of an elastic period for two different rod-displacement patterns, and to obtain the dispersion relation of guided modes that arise in the single-array configuration.

## Approach
The method combines an analytic elastic-wave model with a numerical plane-wave expansion technique for the TM (E-polarisation) mode. First, the time-dependent positions of the GaAs rods are obtained from a spring-model dispersion relation for the square lattice; the elastic period is determined by the wave vector at the zone corner. These positions become the geometric input for the photonic calculation. For the continuous-elastomer case, the photonic band structure is computed on a fine k-point mesh, the density of states (DOS) is evaluated, and photonic band gaps are identified; the bandgap-to-midgap ratio is extracted at each time step. For the single-array elastomer case, a supercell method is used and the guided modes inside the band gap are found by scanning the wave vector along the array direction. The entire workflow is computational and requires no external dataset; standard numerical libraries are sufficient to implement the plane-wave expansion (inverse-matrix HCS) method.

## Reproduction target
Produce two CSV files under `/app/outputs`.  
- `bandgap_ratios.csv`: time-dependent bandgap-to-midgap ratio for two displacement amplitudes, `u0 = (0.25a, 0.25a)` and `u0 = (0.3a, 0)`, with the time fraction `t/T` ranging from 0.0 to 0.25. The file must contain exactly 26 rows per displacement case, corresponding to `time_fraction` values 0.00, 0.01, 0.02, …, 0.25. Columns: `displacement_case` (string, either `'u0_25_25'` or `'u0_30_0'`), `time_fraction` (float), `bandgap_to_midgap_ratio` (float).  
  **Important**: For the `u0 = (0.3a, 0)` case, there are two photonic band gaps: one that opens at low frequency around 0.216 × 2πc/a, and the original gap around 0.28–0.33 × 2πc/a. This task asks for the ratio of the **original gap that exists at t=0** (the gap around 0.28–0.33).  
- `guided_modes.csv`: guided-mode dispersion relation for the single-array supercell (m=8, `u0 = (0, 0.3a)`). The file must contain exactly 51 rows with `wavevector` values 0.00, 0.01, 0.02, …, 0.50. Columns: `wavevector` (float, normalised wave vector `ka/(2πc)` from 0.0 to 0.5) and `frequency` (float, normalised frequency `ωa/(2πc)`).  
The band structures must be computed for the TM mode using the plane-wave expansion method, and the rod positions must follow the elastic motion model described above.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Generate time-dependent rod positions from elastic wave model
- Role: process
- Action: Compute the time-dependent coordinates of rods and unit cell vectors for the continuous-elastomer case (displacement amplitudes: (0.25a,0.25a) and (0.3a,0)) and the single-array case (amplitude (0,0.3a)) using the elastic dispersion relations. Generate the rod positions at discrete time steps from t=0 to T/4, where T is the elastic period. Produce an evidence file documenting the generated geometries.
- Evidence: `/app/outputs/rod_positions.json`

### Step 2: Compute bandgap-to-midgap ratios for continuous-elastomer cases
- Role: scored (load-bearing)
- Action: For each of the two continuous-elastomer displacement cases and at each time step, compute the photonic band structure (TM mode) via the plane-wave expansion method (245 plane waves). Calculate the density of states on a k-point mesh of 1521 points, identify photonic band gaps, and extract the bandgap-to-midgap ratio. Write a CSV file with the time series of ratios for both cases.
- Output file: `/app/outputs/bandgap_ratios.csv`
- Format: csv
- Contract: columns: displacement_case (string, 'u0_25_25' or 'u0_30_0'), time_fraction (float, t/T from 0.0 to 0.25), bandgap_to_midgap_ratio (float)
- Scoring: scored by hidden verifier

### Step 3: Compute guided mode dispersion for single-array elastomer case
- Role: scored
- Action: For the supercell model (m=8, displacement amplitude (0,0.3a)) with elastomer confined to a single array, compute the guided mode dispersion (TM mode) using the plane-wave expansion method (441 plane waves). Scan wavevectors ka/(2πc) from 0 to 0.5, identify eigenfrequencies of guided modes within the band gap, and write the dispersion relation to a CSV file.
- Output file: `/app/outputs/guided_modes.csv`
- Format: csv
- Contract: columns: wavevector (float, ka/(2πc) from 0.0 to 0.5), frequency (float, ωa/(2πc))
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bandgap_ratios.csv`
- `/app/outputs/guided_modes.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bandgap_ratios.csv
- path: `/app/outputs/bandgap_ratios.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time-dependent bandgap-to-midgap ratio for the two continuous-elastomer displacement patterns.
- schema:
  - `type`: table
  - `required_columns`: `displacement_case`, `time_fraction`, `bandgap_to_midgap_ratio`

### guided_modes.csv
- path: `/app/outputs/guided_modes.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Guided mode dispersion (wavevector vs frequency) for the single-array elastomer case.
- schema:
  - `type`: table
  - `required_columns`: `wavevector`, `frequency`

Notes: The agent must implement the plane-wave expansion (HCS) method for TM mode. The checker will compare the submitted bandgap ratios and guided mode frequencies against hidden reference values extracted from the paper, applying numerical tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bandgap_ratios.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "displacement_case",
          "time_fraction",
          "bandgap_to_midgap_ratio"
        ]
      },
      "description": "Time-dependent bandgap-to-midgap ratio for the two continuous-elastomer displacement patterns."
    },
    {
      "file": "guided_modes.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavevector",
          "frequency"
        ]
      },
      "description": "Guided mode dispersion (wavevector vs frequency) for the single-array elastomer case."
    }
  ],
  "notes": "The agent must implement the plane-wave expansion (HCS) method for TM mode. The checker will compare the submitted bandgap ratios and guided mode frequencies against hidden reference values extracted from the paper, applying numerical tolerances."
}
```

## How you are scored
Your solution is evaluated by a hidden verifier that independently inspects each output file. For `bandgap_ratios.csv`, the verifier compares the reported bandgap-to-midgap ratios against reference values (with a numerical tolerance). For `guided_modes.csv`, the verifier compares the reported frequencies at selected wave vectors to hidden reference frequencies (with a tolerance in frequency units). The two stages carry weights that reflect their importance; the total reward is a weighted combination. Simply reporting numbers that match the paper is not sufficient – the verifier validates the actual artefacts your code produces.
