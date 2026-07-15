# Homogeneous Nucleation of Silicon in Si–H–Cl Systems

## Problem background
Homogeneous nucleation of silicon from gas-phase Si–H–Cl mixtures is critical for both particle synthesis (chemical vapour precipitation) and microelectronics fabrication (where particle formation must be avoided). This study theoretically investigates the nucleation potential of SiH₄, SiH₂Cl₂, and SiHCl₃ in H₂ over a wide temperature and composition range. The aim is to quantify the thermodynamic driving force (conversion ratio, supersaturation, chemical potential) and the kinetic nucleation behaviour (onset temperatures, nucleation rates, critical cluster sizes, time lags) using a modified classical nucleation theory. For rapid thermal processing, the decomposition kinetics of SiH₄ are also examined to determine the temperature at which the precursor fully decomposes under various heating rates. The results serve as a screening map for designing processes that either promote or suppress particle formation.

## Approach
The calculations proceed in two stages. First, multicomponent gas-phase equilibrium is solved for each silane–hydrogen mixture over a grid of temperatures (800–2600 K) and silane mole fractions (10⁻⁵ to 1). Using a Gibbs free energy minimizer (e.g., Cantera), the silicon partial pressure is computed both without (p) and with (pₛ) condensed Si, from which the supersaturation S = p/pₛ, conversion ratio, and chemical potential to nucleate (−RT ln S) are derived. The thermochemical data for the Si–H–Cl species are obtained from the published compilation by Kruis et al. (1992). Second, nucleation rates are evaluated using two forms of classical nucleation theory: the classical thermodynamic expression and the kinetic correction (J_kin = J_cl * exp(θ)/S) that has been shown to better match experimental onsets. The dimensionless surface tension θ requires the temperature-dependent surface tension of silicon; linear fits for solid (T < 1685 K) and liquid (T > 1685 K) silicon are employed. For each composition, the onset of nucleation is defined as J = 1 cm⁻³ s⁻¹, yielding a lower and an upper onset temperature. The critical cluster size and the nucleation time lag (from the Shi et al. formula) are computed at the lower onset. Finally, for pure SiH₄, a first-order decomposition rate constant is integrated under linear heating from 10⁰ to 10⁹ K s⁻¹ to find the temperature at which 99% of the SiH₄ has decomposed.

## Reproduction target
Produce four data tables covering the full parameter space. (1) For every combination of silane (SiH₄, SiH₂Cl₂, SiHCl₃), temperature, and mole fraction, compute the silicon partial pressures, supersaturation, conversion ratio, and chemical potential; from these verify that a broad region of high deposition exists for SiH₄ and record the supersaturation at 1200 K and 1×10⁻² mole fraction. (2) For each silane and mole fraction, using the kinetic nucleation model, determine the lower and upper onset temperatures, the critical cluster size at the lower onset, and the time lag; assess how these quantities vary with dilution. (3) For the same silanes at fixed mole fractions (0.4, 1×10⁻², 1×10⁻⁴ for SiH₄, and analogous high, medium, and low dilutions for the chlorosilanes), compute the nucleation rate as a function of temperature over the range where onset occurs. (4) For pure SiH₄, tabulate the 99% decomposition temperature for heating rates from 10⁰ to 10⁹ K/s. The computed values are compared against independent reference data by the hidden verifier.

## Assets

- Thermochemical data for Si-H-Cl system (Kruis et al., 1992): 10.1111/j.1151-2916.1992.tb04363.x
- Cantera chemical equilibrium solver: https://cantera.org
- Python scientific libraries (numpy, scipy): numpy scipy

## Workflow steps

### Step 1: Prepare surface tension functions
- Role: process
- Action: Determine the coefficients for the temperature-dependent surface tension of solid and liquid silicon using the linear fits: σ(T) = 1.339 – 3.329×10⁻⁴ T J m⁻² for T < 1685 K (solid), and σ(T) = 0.912 – 1.04×10⁻⁴ T J m⁻² for T > 1685 K (liquid). Save the parameters in surface_tension_params.json.
- Evidence: `/app/outputs/surface_tension_params.json`

### Step 2: Run chemical equilibrium calculations
- Role: process
- Action: Using the thermochemical data from Kruis et al. (1992) and an open-source chemical equilibrium solver (e.g., Cantera), perform multicomponent gas-phase equilibrium calculations for SiH₄, SiH₂Cl₂, and SiHCl₃ in H₂ over a grid of temperatures (800–2600 K) and mole fractions (10⁻⁵ to 1). For each condition, compute the silicon partial pressure excluding condensed phases (p) and including condensed Si (p_s), and record the gas-phase composition. Save the results in equilibrium_data.json.
- Evidence: `/app/outputs/equilibrium_data.json`

### Step 3: Compute conversion ratio and chemical potential
- Role: scored (load-bearing)
- Action: Read equilibrium_data.json. For every grid point, calculate supersaturation S = p / p_s, conversion ratio = (initial Si – final gas-phase Si) / initial Si, and chemical potential to nucleate = –RT ln S. Write the results to conversion_ratio_and_potential.csv.
- Output file: `/app/outputs/conversion_ratio_and_potential.csv`
- Format: csv
- Contract: columns: silane (string), temperature_K (float, K), mole_fraction (float), p_Pa (float, Pa), ps_Pa (float, Pa), supersaturation (float), conversion_ratio (float), chemical_potential_kJ_per_mol (float, kJ mol⁻¹)
- Scoring: scored by hidden verifier

### Step 4: Compute nucleation onset, critical cluster size, and time lag
- Role: scored (load-bearing)
- Action: Read equilibrium_data.json and surface_tension_params.json. For each silane and mole fraction, compute monomer concentration n₁ from the equilibrium composition, dimensionless surface tension θ = σ s₁/(k_B T) with monomer surface area s₁, and nucleation rates using the classical model (J_cl) and kinetic model (J_kin = J_cl * exp(θ)/S). Determine the lower and upper onset temperatures where J = 1 cm⁻³ s⁻¹, the critical cluster size k* = (2θ/(3 ln S))³ at the lower onset, and the nucleation time lag τ using the formula from Shi et al. Write all results to nucleation_onset_and_critical.csv.
- Output file: `/app/outputs/nucleation_onset_and_critical.csv`
- Format: csv
- Contract: columns: silane (string), mole_fraction (float), model (classical or kinetic), lower_onset_T (float, K), upper_onset_T (float, K), critical_cluster_size (float), time_lag_s (float, s)
- Scoring: scored by hidden verifier

### Step 5: Compute nucleation rate vs temperature
- Role: scored
- Action: Read equilibrium_data.json and surface_tension_params.json. For each silane at fixed mole fractions (0.4, 10⁻², 10⁻⁴ for SiH₄; analogous for SiH₂Cl₂ and SiHCl₃), compute the nucleation rate using the kinetic model over a temperature range that spans both onset branches. Write the rates to nucleation_rate_vs_T.csv.
- Output file: `/app/outputs/nucleation_rate_vs_T.csv`
- Format: csv
- Contract: columns: silane (string), mole_fraction (float), temperature_K (float, K), nucleation_rate_per_cm3_per_s (float, cm⁻³ s⁻¹)
- Scoring: scored by hidden verifier

### Step 6: Compute SiH₄ decomposition curve
- Role: scored
- Action: For pure SiH₄ (mole_fraction=1), integrate the decomposition kinetics d[SiH₄]/dt = –1.26×10¹⁴ exp(–28100/T) [SiH₄] for heating rates dT/dt from 10⁰ to 10⁹ K/s. For each heating rate, determine the temperature at which 99% of SiH₄ has decomposed. Write the results to decomposition_curve.csv.
- Output file: `/app/outputs/decomposition_curve.csv`
- Format: csv
- Contract: columns: heating_rate_K_per_s (float, K s⁻¹), temperature_99pct_decomposition_K (float, K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/conversion_ratio_and_potential.csv`
- `/app/outputs/nucleation_onset_and_critical.csv`
- `/app/outputs/nucleation_rate_vs_T.csv`
- `/app/outputs/decomposition_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### conversion_ratio_and_potential.csv
- path: `/app/outputs/conversion_ratio_and_potential.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Supersaturation, conversion ratio, and chemical potential for each composition and temperature. Checker compares supersaturation at a specific condition and verifies conversion ratio trends.
- schema:
  - `type`: table
  - `required_columns`: `silane`, `temperature_K`, `mole_fraction`, `p_Pa`, `ps_Pa`, `supersaturation`, `conversion_ratio`, `chemical_potential_kJ_per_mol`
  - `units`:
    - `temperature_K`: K
    - `p_Pa`: Pa
    - `ps_Pa`: Pa
    - `chemical_potential_kJ_per_mol`: kJ mol⁻¹

### nucleation_onset_and_critical.csv
- path: `/app/outputs/nucleation_onset_and_critical.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Onset nucleation temperatures, critical cluster size, and time lag for each composition and nucleation model. Checker compares onset temperatures, cluster sizes, and time lags to reference values within tolerances.
- schema:
  - `type`: table
  - `required_columns`: `silane`, `mole_fraction`, `model`, `lower_onset_T`, `upper_onset_T`, `critical_cluster_size`, `time_lag_s`
  - `units`:
    - `lower_onset_T`: K
    - `upper_onset_T`: K
    - `time_lag_s`: s

### nucleation_rate_vs_T.csv
- path: `/app/outputs/nucleation_rate_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Nucleation rate curves for selected mole fractions. Checker verifies peak shapes and ordering of rates between conditions.
- schema:
  - `type`: table
  - `required_columns`: `silane`, `mole_fraction`, `temperature_K`, `nucleation_rate_per_cm3_per_s`
  - `units`:
    - `temperature_K`: K
    - `nucleation_rate_per_cm3_per_s`: cm⁻³ s⁻¹

### decomposition_curve.csv
- path: `/app/outputs/decomposition_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: SiH₄ decomposition temperature at 99% conversion for a range of heating rates. Checker verifies the temperature at a reference heating rate and the monotonic trend.
- schema:
  - `type`: table
  - `required_columns`: `heating_rate_K_per_s`, `temperature_99pct_decomposition_K`
  - `units`:
    - `heating_rate_K_per_s`: K s⁻¹
    - `temperature_99pct_decomposition_K`: K

Notes: All outputs are compared to reference values from the published literature with appropriate tolerances. Tolerances account for differences in equilibrium solver implementations and discretization.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "conversion_ratio_and_potential.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "silane",
          "temperature_K",
          "mole_fraction",
          "p_Pa",
          "ps_Pa",
          "supersaturation",
          "conversion_ratio",
          "chemical_potential_kJ_per_mol"
        ],
        "units": {
          "temperature_K": "K",
          "p_Pa": "Pa",
          "ps_Pa": "Pa",
          "chemical_potential_kJ_per_mol": "kJ mol⁻¹"
        }
      },
      "description": "Supersaturation, conversion ratio, and chemical potential for each composition and temperature. Checker compares supersaturation at a specific condition and verifies conversion ratio trends."
    },
    {
      "file": "nucleation_onset_and_critical.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "silane",
          "mole_fraction",
          "model",
          "lower_onset_T",
          "upper_onset_T",
          "critical_cluster_size",
          "time_lag_s"
        ],
        "units": {
          "lower_onset_T": "K",
          "upper_onset_T": "K",
          "time_lag_s": "s"
        }
      },
      "description": "Onset nucleation temperatures, critical cluster size, and time lag for each composition and nucleation model. Checker compares onset temperatures, cluster sizes, and time lags to reference values within tolerances."
    },
    {
      "file": "nucleation_rate_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "silane",
          "mole_fraction",
          "temperature_K",
          "nucleation_rate_per_cm3_per_s"
        ],
        "units": {
          "temperature_K": "K",
          "nucleation_rate_per_cm3_per_s": "cm⁻³ s⁻¹"
        }
      },
      "description": "Nucleation rate curves for selected mole fractions. Checker verifies peak shapes and ordering of rates between conditions."
    },
    {
      "file": "decomposition_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "heating_rate_K_per_s",
          "temperature_99pct_decomposition_K"
        ],
        "units": {
          "heating_rate_K_per_s": "K s⁻¹",
          "temperature_99pct_decomposition_K": "K"
        }
      },
      "description": "SiH₄ decomposition temperature at 99% conversion for a range of heating rates. Checker verifies the temperature at a reference heating rate and the monotonic trend."
    }
  ],
  "notes": "All outputs are compared to reference values from the published literature with appropriate tolerances. Tolerances account for differences in equilibrium solver implementations and discretization."
}
```

## How you are scored
Each workflow step that produces a CSV artifact is scored individually by a hidden verifier, and the scores are weighted and summed to give the final reward. The verifier reads your output files and compares the reported quantities to reference values derived from the original study, checking for agreement within tolerances that account for different equilibrium solver implementations and numerical discretisation. For conversion_ratio_and_potential.csv, the verifier confirms that SiH₄ shows a large high-conversion area, checks the supersaturation at a specific condition, and verifies that the relative ordering of supersaturation among the silanes is physically consistent. For nucleation_onset_and_critical.csv, it compares your onset temperature curves, critical cluster sizes at given mole fractions, and time lags to reference numbers. For nucleation_rate_vs_T.csv, it verifies that nucleation rates peak at finite temperatures and that the magnitude ordering between different mole fractions matches the expected trend. For decomposition_curve.csv, it checks the decomposition temperature at a reference heating rate and the monotonicity of the decomposition temperature with heating rate. A solution that merely copies values from the paper without genuinely executing the calculations will not pass, because the verifier checks structural properties and cross-consistency that cannot be guessed.
