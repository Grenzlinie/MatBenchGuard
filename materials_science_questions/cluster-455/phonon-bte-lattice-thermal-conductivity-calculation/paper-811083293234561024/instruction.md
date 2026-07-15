# Thermal conductivity of width-modulated nanowires: Monte Carlo simulation and transition interpolation

## Problem background
Understanding how nanostructures with nonuniform cross-sections transport heat is crucial for applications such as thermoelectrics and nanoelectronics. In width-modulated nanowires, where periodically spaced constrictions narrow the conducting channel, earlier simulations indicated two distinct regimes: for a single narrow constriction the thermal resistance is dominated by a ballistic constriction resistance, while for many constrictions the conductivity scales with the overall transmissivity of the structure. The transition between these two regimes — as the number of constrictions increases — is not fully characterized. This task investigates that transition by having you compute the thermal conductivity and thermal resistance of silicon nanowires with rectangular width modulations, and extract a phenomenological ballisticity parameter that bridges the two extremes.

## Approach
You will implement a phonon Monte Carlo solver for the Boltzmann transport equation in the relaxation-time approximation. Phonon properties (dispersion and intrinsic scattering rates for normal, umklapp, and impurity processes) are taken from the Holland model for silicon. All boundaries are assumed to scatter phonons diffusively. The simulation is run at 300 K.

The baseline system is a uniform nanowire of width a = 100 nm. For the modulated nanowires, rectangular constrictions of width b (20, 60, or 90 nm) and length c = 10 nm are placed along the wire; the number of constrictions N ranges from 1 to 10. For each (N, b) configuration you will compute the effective thermal conductivity κ and thermal resistance R, then normalize each by the corresponding value of the uniform nanowire (same total length) to obtain relative thermal conductivity and resistance.

Finally, for the b = 20 nm case only, you will apply the phenomenological interpolation equation
R = R_w(L) [1 + (1 - χ) (Tr⁻¹ - 1)] + χ N R_C
where R_w(L) is the uniform-nanowire resistance, Tr = b/a is the transmissivity, R_C is the constriction thermal resistance (from the N = 1 simulation), and χ is the ballisticity parameter. Solve this equation for χ at each N to quantify the transition from ballistic-constriction behavior (χ ≈ 1 at N = 1) toward the fully transmissivity-controlled regime.

## Reproduction target
Produce two scored artifacts:
1. A CSV file (`step_01_thermal_properties.csv`) containing for every combination of constriction number N (1 to 10) and constriction width b (20, 60, 90 nm) the relative thermal conductivity and relative thermal resistance, normalized by the values of the uniform nanowire of the same total length.
2. A CSV file (`step_02_fitted_chi.csv`) containing, for b = 20 nm and N = 1 to 10, the ballisticity parameter χ obtained from the resistance values using the phenomenological equation given in the Approach.

## Assets

- Holland model for silicon phonon dispersion and relaxation times: 10.1103/PhysRev.132.2461
- Phonon Monte Carlo simulation code

## Workflow steps

### Step 1: Define geometry and material parameters
- Role: process
- Action: Set up silicon phonon properties using the Holland model (dispersion, relaxation times for normal, umklapp, impurity scattering). Define the nanowire geometry: wire width a = 100 nm, constriction length c = 10 nm; choose a total nanowire length L (e.g., 1000 nm) that is much longer than the phonon mean free path. Specify constriction widths b in {20, 60, 90} nm and number of constrictions N from 1 to 10.
- Evidence: `/app/outputs/geometry_material_config.txt`

### Step 2: Run reference uniform nanowire simulation
- Role: process
- Action: Run a phonon Monte Carlo simulation for a uniform (non-modulated) nanowire of width a and length L, assuming fully diffusive boundary scattering at 300 K, to obtain the baseline thermal resistance R_w(L).
- Evidence: `/app/outputs/uniform_resistance_log.txt`

### Step 3: Run modulated nanowire simulations
- Role: process
- Action: For each constriction width b and each N from 1 to 10, run the phonon MC simulation for the modulated nanowire. For each configuration, compute the effective thermal conductivity kappa and thermal resistance R, then normalize by the corresponding uniform nanowire values to obtain relative thermal conductivity and relative thermal resistance.
- Evidence: `/app/outputs/modulated_simulation_summary.json`

### Step 4: Output relative thermal properties
- Role: scored
- Action: Compile the normalized thermal properties for all (N, b) configurations into a CSV file.
- Output file: `/app/outputs/step_01_thermal_properties.csv`
- Format: csv
- Contract: columns: n_constrictions (int), constriction_width_nm (int), relative_thermal_conductivity (float), relative_thermal_resistance (float)
- Scoring: scored by hidden verifier

### Step 5: Extract constriction thermal resistance
- Role: process
- Action: From the N=1 modulated simulation data for each b, compute the constriction thermal resistance R_C = R(N=1) - R_w(L). Store R_C for b=20 nm for the subsequent chi calculation.
- Evidence: `/app/outputs/Rc_values.txt`

### Step 6: Output fitted ballisticity parameter chi
- Role: scored (load-bearing)
- Action: For b = 20 nm, for each N from 1 to 10, derive chi from the phenomenological interpolation equation linking total resistance, transmissivity, N, and R_C, where chi is the ballisticity parameter. Solve for chi and output a CSV with columns n_constrictions and chi.
- Output file: `/app/outputs/step_02_fitted_chi.csv`
- Format: csv
- Contract: columns: n_constrictions (int), chi (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thermal_properties.csv`
- `/app/outputs/step_02_fitted_chi.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thermal_properties.csv
- path: `/app/outputs/step_01_thermal_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Relative (normalized) thermal conductivity and resistance for all simulated constriction widths and numbers of constrictions.
- schema:
  - `type`: table
  - `required_columns`: `n_constrictions`, `constriction_width_nm`, `relative_thermal_conductivity`, `relative_thermal_resistance`
  - `units`:
    - `relative_thermal_conductivity`: dimensionless
    - `relative_thermal_resistance`: dimensionless

### step_02_fitted_chi.csv
- path: `/app/outputs/step_02_fitted_chi.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ballisticity parameter chi fitted for constriction width 20 nm as a function of the number of constrictions N.
- schema:
  - `type`: table
  - `required_columns`: `n_constrictions`, `chi`
  - `units`:
    - `chi`: dimensionless

Notes: Checker compares agent outputs to hidden reference values from the paper within tolerances and verifies structural trends (monotonicity, plateau) for both artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thermal_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_constrictions",
          "constriction_width_nm",
          "relative_thermal_conductivity",
          "relative_thermal_resistance"
        ],
        "units": {
          "relative_thermal_conductivity": "dimensionless",
          "relative_thermal_resistance": "dimensionless"
        }
      },
      "description": "Relative (normalized) thermal conductivity and resistance for all simulated constriction widths and numbers of constrictions."
    },
    {
      "file": "step_02_fitted_chi.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "n_constrictions",
          "chi"
        ],
        "units": {
          "chi": "dimensionless"
        }
      },
      "description": "Ballisticity parameter chi fitted for constriction width 20 nm as a function of the number of constrictions N."
    }
  ],
  "notes": "Checker compares agent outputs to hidden reference values from the paper within tolerances and verifies structural trends (monotonicity, plateau) for both artifacts."
}
```

## How you are scored
A hidden verifier will independently check your two scored CSV files. It will compare each entry to reference results obtained from a correct execution of the described Monte Carlo procedure. In addition to numerical comparison, the verifier will examine structural trends: for each constriction width, the relative resistance should increase with N and eventually saturate, while the relative thermal conductivity should decrease accordingly; for the χ values, χ should start near 1 at N = 1 and decrease toward 0 as N grows. Your final reward is a weighted sum of the scores for the two files. Reporting paper numbers without running the actual simulations will not suffice.
