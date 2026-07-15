# Classical Nucleation Theory Critical Size Calculation

## Problem background
Nucleation of new particles from sulfuric acid and water vapor is a critical atmospheric process. Predictions from classical binary nucleation theory have historically varied by orders of magnitude, partly due to uncertainty in the equilibrium vapor pressure of pure sulfuric acid and to the common neglect of hydrate formation in the gas phase. This task addresses the question of how updated thermodynamic inputs and the inclusion of hydration equilibria change the required sulfuric acid gas-phase concentration to achieve a unit nucleation rate, and how the composition of the critical nucleus depends on temperature and humidity.

## Approach
You will implement the classical theory of binary homogeneous nucleation for the H2SO4–H2O system. The nucleation rate J depends exponentially on the free energy required to form a critical nucleus, which is obtained from the capillarity approximation. The free energy surface is a function of the composition and size of the nucleus; the critical nucleus corresponds to a saddle point. To build this implementation you need thermodynamic property functions (surface tension, liquid-phase chemical potentials, partial molar volumes, saturation vapor pressures) as functions of temperature and acid mole fraction. These must be derived from public data using polynomial fits and interpolations as described in the literature. Gas-phase hydration of sulfuric acid by successive water molecules is handled via hydration equilibrium constants. You will then solve for the total gas-phase acid number density, Na, that gives exactly J=1 nucleus cm⁻³ s⁻¹ under a set of prescribed conditions: at 298 K and five relative humidities (20%–100%), for three different scenarios: (a) using a high vapor pressure with no hydrates, (b) an intermediate vapor pressure with no hydrates, and (c) a lower vapor pressure while including hydrate formation. In addition, you will determine the mole fraction of H2SO4 in the critical nucleus at the same unit nucleation rate for a range of temperatures and humidities.

## Reproduction target
You must produce two CSV tables. (1) unit_rate_threshold.csv: for relative humidities 20, 40, 60, 80, 100%, compute the total sulfuric acid number density Na (molecules/cm³) required to achieve a nucleation rate of 1 nucleus cm⁻³ s⁻¹ at 298 K under each of three scenarios: (a) P° = 3.6×10⁻⁴ torr and no hydrates; (b) P° = 3.1×10⁻⁵ torr and no hydrates; (c) P° = 1.4×10⁻⁵ torr and with hydration equilibria from the provided constants. (2) critical_composition.csv: for each temperature in {223 K, 273 K, 323 K, 373 K} and each relative humidity in {20, 40, 60, 80, 100%}, compute the mole fraction of H2SO4 in the critical nucleus (saddle-point composition) at the conditions where J=1 nucleus cm⁻³ s⁻¹. All computations must be performed with your own implementation of the nucleation solver; simply reporting numbers that appear in the literature is not sufficient.

## Assets

- Chemical potentials of H2SO4-H2O mixtures (Giauque et al. 1960)
- Surface tension data for H2SO4-H2O (Sabinina and Terpugow 1935)
- Molar volumes of H2SO4-H2O mixtures (Chemical Engineer's Handbook)
- Pure H2SO4 vapor pressure equation (Ayers et al. 1980)
- Water vapor pressure equations (Lowe 1977 and Landolt-Börnstein)
- Hydration equilibrium constants H2SO4·(H2O)h for h=1..10

## Workflow steps

### Step 1: Prepare thermodynamic property functions
- Role: process
- Action: Implement functions that return surface tension, molar/partial molar volumes, chemical potentials, and vapor pressures of the H2SO4-H2O system as a function of temperature and composition, based on the literature data described in the method. Fit polynomials and apply interpolation as needed to obtain continuous representations.
- Evidence: `/app/outputs/thermo_functions.log`

### Step 2: Load hydration equilibrium constants
- Role: process
- Action: Read the bundled hydration equilibrium constants CSV and prepare them for use in the nucleation model.
- Evidence: none

### Step 3: Implement nucleation rate solver
- Role: process
- Action: Implement the classical binary nucleation theory: free energy surface, saddle-point determination, nucleation rate calculation J (nuclei cm⁻³ s⁻¹). The implementation must support options for including/omitting hydrate equilibria and for setting different pure H₂SO₄ vapor pressures. All necessary equations are described in the paper.
- Evidence: `/app/outputs/nucleation_solver.py`

### Step 4: Compute unit-rate threshold Na at 298 K
- Role: scored (load-bearing)
- Action: For each relative humidity in [20,40,60,80,100]% and for each of the three scenarios: (a) P°=3.6e-4 torr, no hydrates; (b) P°=3.1e-5 torr, no hydrates; (c) P°=1.4e-5 torr, with hydrates, find the total H₂SO₄ number density Nₐ (molecules/cm³) that gives a nucleation rate J=1 nucleus cm⁻³ s⁻¹ at T=298 K.
- Output file: `/app/outputs/unit_rate_threshold.csv`
- Format: csv
- Contract: Columns: rh (integer), case_a (float, sci. notation), case_b (float, sci. notation), case_c (float, sci. notation). Each row corresponds to one relative humidity.
- Scoring: scored by hidden verifier

### Step 5: Compute critical nucleus composition at unit rate
- Role: scored (load-bearing)
- Action: For each temperature in [223,273,323,373] K and each relative humidity in [20,40,60,80,100]%, compute the mole fraction of H₂SO₄ in the critical nucleus (saddle-point composition) at the conditions where the nucleation rate equals 1 nucleus cm⁻³ s⁻¹.
- Output file: `/app/outputs/critical_composition.csv`
- Format: csv
- Contract: Columns: temperature (integer, K), rh (integer), mole_fraction_H2SO4 (float, between 0 and 1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/unit_rate_threshold.csv`
- `/app/outputs/critical_composition.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### unit_rate_threshold.csv
- path: `/app/outputs/unit_rate_threshold.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Total acid number density needed for unit nucleation rate for three scenarios. Values compared to paper's curves with threshold tolerance.
- schema:
  - `type`: table
  - `required_columns`: `rh`, `case_a`, `case_b`, `case_c`
  - `units`:
    - `rh`: percent
    - `case_a`: molecules/cm^3
    - `case_b`: molecules/cm^3
    - `case_c`: molecules/cm^3

### critical_composition.csv
- path: `/app/outputs/critical_composition.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mole fraction of H2SO4 in the critical nucleus at unit nucleation rate. Compared to paper's Fig. 6 with absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `rh`, `mole_fraction_H2SO4`
  - `units`:
    - `temperature`: K
    - `rh`: percent
    - `mole_fraction_H2SO4`: dimensionless mole fraction

Notes: All required physical property data are public; the hydration constants CSV is bundled. The solver must be implemented from the described equations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "unit_rate_threshold.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "rh",
          "case_a",
          "case_b",
          "case_c"
        ],
        "units": {
          "rh": "percent",
          "case_a": "molecules/cm^3",
          "case_b": "molecules/cm^3",
          "case_c": "molecules/cm^3"
        }
      },
      "description": "Total acid number density needed for unit nucleation rate for three scenarios. Values compared to paper's curves with threshold tolerance."
    },
    {
      "file": "critical_composition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "rh",
          "mole_fraction_H2SO4"
        ],
        "units": {
          "temperature": "K",
          "rh": "percent",
          "mole_fraction_H2SO4": "dimensionless mole fraction"
        }
      },
      "description": "Mole fraction of H2SO4 in the critical nucleus at unit nucleation rate. Compared to paper's Fig. 6 with absolute tolerance."
    }
  ],
  "notes": "All required physical property data are public; the hydration constants CSV is bundled. The solver must be implemented from the described equations."
}
```

## How you are scored
A hidden verifier will independently evaluate each scored artifact. For unit_rate_threshold.csv, it will compare your computed Na values against reference targets; you must match or surpass a quality threshold derived from the expected accuracy of a correct implementation. For critical_composition.csv, it will compare each mole fraction entry against a hidden reference within a tolerance window. The total reward is a weighted combination of the two artifact scores; simply printing values from the literature will not achieve a passing score, as the verifier expects results obtained by running a complete nucleation solver. Detailed scoring rules and tolerances are hidden.
