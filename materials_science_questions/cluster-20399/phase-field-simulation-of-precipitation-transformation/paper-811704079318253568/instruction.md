# Phase-field simulation of martensitic and strain-glass transitions in defect-containing ferroelastic systems

## Problem background
In ferroelastic materials, the presence of point defects can give rise to strain states that go beyond the familiar austenite (disordered paraelastic) and martensite (twinned ferroelastic): a precursory tweed characterised by nanosized strain domains, and a strain glass, a frozen state of local strain order. The interplay between point defects and the martensitic transformation is typically captured in a phase diagram that relates characteristic transition temperatures to defect concentration. The task is to determine, from a phase‑field model that incorporates two defect‑induced effects, the martensite start temperature, the strain‑glass transition temperature, and the nanodomain onset temperature as a function of dimensionless defect concentration, as well as the zero‑field‑cooled/field‑cooled strain curves that probe the freezing transition.

## Approach
The system is described by a Landau free‑energy functional that includes conventional chemical, gradient and elastic contributions. Point defects are modelled through two separate terms: a global transition‑temperature effect (GTTE), which makes the leading Landau coefficient depend on defect concentration, thereby shifting the overall thermodynamic stability of the martensite phase, and a local‑field effect (LFE), which introduces static, spatially random local strains that break the symmetry of the Landau potential. The microstructure evolution is obtained by solving the stochastic time‑dependent Ginzburg–Landau equation on a two‑dimensional square grid with periodic boundary conditions.

Cooling simulations are performed for a range of defect concentrations, starting from a temperature above the austenite‑stable region and cooling slowly. From the saved order‑parameter fields, the volume fraction of martensitic domains and the heat capacity are computed as functions of temperature; the transition temperatures (Ms or Tg) are identified from the heat‑capacity peaks, and the onset of static nanodomains (Tnd) is defined by a small volume‑fraction threshold. For one composition in the strain‑glass regime, separate zero‑field‑cooled and field‑cooled protocols are executed, applying a small symmetry‑breaking bias during cooling, and the temperature‑dependence of the volume fraction of one variant is recorded in both protocols to capture the ergodicity breaking.

## Reproduction target
Produce two CSV files under `/app/outputs`:
1. `transition_temperatures.csv` – contains, for each defect concentration studied, the values of Ms (martensite start), Tg (strain‑glass transition) and Tnd (nanodomain onset temperature), respecting the mutual‑exclusivity of Ms and Tg across the martensitic and strain‑glass regimes.
2. `zfc_fc_curve.csv` – provides the volume fraction of one variant (strain) as a function of temperature for the zero‑field‑cooled and field‑cooled protocols at the strain‑glass composition, covering a range that spans from above Tnd to below Tg. The data must result from running the full phase‑field simulations; copying or fabricating the output is not sufficient.

## Assets

- NumPy: numpy
- SciPy: scipy
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Model Setup
- Role: process
- Action: Implement the Landau free-energy functional incorporating global transition-temperature effect (GTTE) via concentration-dependent leading coefficient and local-field effect (LFE) via static defect fields. Implement the stochastic time-dependent Ginzburg-Landau equation solver on a 2D grid (256×256 units, periodic boundary conditions) using the specified elastic constants, gradient energy coefficient, and Landau coefficients. Set all physical and numerical parameters as defined in the model description.
- Evidence: `/app/outputs/parameters_log.txt`

### Step 2: Cooling Simulations
- Role: process
- Action: For each defect concentration c in {0, 0.025, 0.05, 0.075, 0.1, 0.125, 0.15, 0.2}, run cooling-driven phase-field simulations from a high temperature (in the austenite phase) down to a temperature where the system is fully transformed or frozen. Store the order-parameter fields η₁(r), η₂(r) at a sufficient number of temperature steps for later post-processing.
- Evidence: `/app/outputs/cooling_complete.log`

### Step 3: Determine Transition Temperatures
- Role: scored (load-bearing)
- Action: From the saved cooling-simulation fields for each c, compute the volume fraction of martensitic domains and the heat capacity as functions of temperature. Identify Ms (for c<0.05) or Tg (for c≥0.075) as the peak in heat capacity, and Tnd as the temperature where the volume fraction of martensite (including nanosized domains) reaches approximately 3%. Write transition_temperatures.csv with columns c, Ms, Tg, Tnd. For c where Ms is determined, Tg must be NaN; for c where Tg is determined, Ms must be NaN.
- Output file: `/app/outputs/transition_temperatures.csv`
- Format: csv
- Contract: columns: c (float, dimensionless defect concentration), Ms (float, normalized temperature or NaN), Tg (float, normalized temperature or NaN), Tnd (float, normalized temperature).
- Scoring: scored by hidden verifier

### Step 4: ZFC/FC Simulation and Curve for c=0.125
- Role: scored (load-bearing)
- Action: For c=0.125, run zero-field cooling (ZFC) and field cooling (FC) protocols using the same phase-field model. In ZFC, cool in zero applied field and record the volume fraction of one variant as a function of temperature. In FC, apply a small symmetry-breaking field during cooling, then measure the volume fraction on heating. Write zfc_fc_curve.csv with columns T, strain_ZFC, strain_FC. The temperature range must cover from above Tnd to below Tg for this composition.
- Output file: `/app/outputs/zfc_fc_curve.csv`
- Format: csv
- Contract: columns: T (float, normalized temperature), strain_ZFC (float, volume fraction), strain_FC (float, volume fraction).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transition_temperatures.csv`
- `/app/outputs/zfc_fc_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transition_temperatures.csv
- path: `/app/outputs/transition_temperatures.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Phase-diagram transition temperatures extracted from cooling simulations. One row per defect concentration; Ms and Tg are mutually exclusive and contain the transition temperature or NaN. The hidden checker compares the reported values against the paper's digitized reference within a tolerance, verifies NaN placement, and checks monotonicity trends.
- schema:
  - `type`: table
  - `required_columns`: `c`, `Ms`, `Tg`, `Tnd`
  - `units`:
    - `c`: dimensionless area fraction
    - `Ms`: normalized temperature
    - `Tg`: normalized temperature
    - `Tnd`: normalized temperature

### zfc_fc_curve.csv
- path: `/app/outputs/zfc_fc_curve.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Zero-field-cooling and field-cooling strain curves for c=0.125. The hidden checker verifies that FC strain lies above ZFC strain at low temperatures, that separation occurs near Tnd, and that both strains decrease smoothly with temperature, comparing against the paper's reference curve within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `T`, `strain_ZFC`, `strain_FC`
  - `units`:
    - `T`: normalized temperature
    - `strain_ZFC`: volume fraction
    - `strain_FC`: volume fraction

Notes: The transition temperatures are defined at the specific concentrations listed. For c in the martensite regime (c<0.05) Ms is reported, Tg is NaN; for strain-glass regime (c>=0.075) Tg is reported, Ms is NaN. Tnd is reported for all c. The ZFC/FC curve must demonstrate ergodicity breaking.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transition_temperatures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "c",
          "Ms",
          "Tg",
          "Tnd"
        ],
        "units": {
          "c": "dimensionless area fraction",
          "Ms": "normalized temperature",
          "Tg": "normalized temperature",
          "Tnd": "normalized temperature"
        }
      },
      "description": "Phase-diagram transition temperatures extracted from cooling simulations. One row per defect concentration; Ms and Tg are mutually exclusive and contain the transition temperature or NaN. The hidden checker compares the reported values against the paper's digitized reference within a tolerance, verifies NaN placement, and checks monotonicity trends."
    },
    {
      "file": "zfc_fc_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "strain_ZFC",
          "strain_FC"
        ],
        "units": {
          "T": "normalized temperature",
          "strain_ZFC": "volume fraction",
          "strain_FC": "volume fraction"
        }
      },
      "description": "Zero-field-cooling and field-cooling strain curves for c=0.125. The hidden checker verifies that FC strain lies above ZFC strain at low temperatures, that separation occurs near Tnd, and that both strains decrease smoothly with temperature, comparing against the paper's reference curve within tolerances."
    }
  ],
  "notes": "The transition temperatures are defined at the specific concentrations listed. For c in the martensite regime (c<0.05) Ms is reported, Tg is NaN; for strain-glass regime (c>=0.075) Tg is reported, Ms is NaN. Tnd is reported for all c. The ZFC/FC curve must demonstrate ergodicity breaking."
}
```

## How you are scored
A hidden verifier examines each required output file independently. For `transition_temperatures.csv`, it checks that the reported transition temperatures and the pattern of `NaN` values for Ms/Tg agree with the expected phase diagram within reasonable tolerances, and that the trends of the transition temperatures with defect concentration are physically consistent. For `zfc_fc_curve.csv`, it verifies that the curve shape, the separation between the ZFC and FC branches, and the overall temperature dependence match the expected ergodicity‑breaking signature. The final score is a weighted combination: 40 % for the transition temperatures, 30 % for the ZFC/FC curve match, and 30 % for trend consistency.
