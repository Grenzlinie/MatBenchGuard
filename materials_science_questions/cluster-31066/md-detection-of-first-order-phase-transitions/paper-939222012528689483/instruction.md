# Debye-Hückel Spin Ice Density Transitions

## Problem background
In spin ice materials, magnetic monopoles behave as a screened Coulomb fluid and their thermodynamics can be modelled by Debye–Hückel theory. This theory describes singly and doubly charged monopoles on a diamond lattice, interacting via a magnetic Coulomb potential, with densities controlled by a chemical potential. The key question is whether the self‑consistent Debye–Hückel treatment predicts first‑order density‑jump transitions in the monopole density as temperature and chemical potential are varied. Understanding this is important because such transitions would manifest as abrupt changes in monopole density and characteristic signatures in the specific heat, but their existence and nature in the model are unresolved.

## Approach
The magnetolyte model for spin ice is implemented using the Debye–Hückel self‑consistent framework. The system is described by a Debye length that depends on monopole density, a screened Coulomb energy per site, and a low‑density approximation for the configurational entropy. The equilibrium site densities of singly and doubly charged monopoles are obtained by solving the coupled equations that involve effective chemical potentials modified by the Debye screening. Because the free energy may exhibit metastable minima, the iteration is carried out along two protocols: a heating run (starting from zero density and increasing temperature in small steps) and a subsequent cooling run (decreasing temperature), so that both metastable and equilibrium branches are captured. From the converged densities the total monopole density and specific heat are computed at each temperature step. After simulating the curves for several values of the bare chemical potential, the resulting total density curves are analysed for discontinuities and hysteresis to classify the thermodynamic regime of each chemical potential and, where applicable, to estimate a transition temperature.

## Reproduction target
Produce CSV files containing temperature, total monopole density, and specific heat for both heating and cooling branches for three bare chemical potentials: |μ| = 1.0 K, 1.5 K, and 1.8 K. Each CSV must span the temperature range from approximately 0.01 K to 5 K in 10 mK steps, with at least 50 rows and a header row: T(K), n_tot_heating, n_tot_cooling, C_heating(J/K·site), C_cooling(J/K·site). Then analyse the n_tot curves from these files to classify each |μ| into one of three regimes: (i) metastable‑only transition, (ii) equilibrium first‑order transition with hysteresis, or (iii) no first‑order transition. For each regime assign the corresponding transition temperature or null, and write the classification as a JSON file with keys `regime_1_0K`, `regime_1_5K`, `regime_1_8K`, `transition_T_1_0K`, `transition_T_1_5K`, `transition_T_1_8K`.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: DH simulation for |μ|=1.0 K
- Role: scored
- Action: Implement the self‑consistent Debye–Hückel solver for the spin‑ice magnetolyte with material parameters a=4.34 Å, Q=4.28×10⁻¹³ A·m, μ₂=4μ, and the low‑density entropy expression. For |μ| = 1.0 K, perform a heating run (T from 0.01 K to 5 K in 10 mK steps, starting from zero density) and a cooling run (T from 5 K to 0.01 K, continuing from the final temperature of the heating run) to obtain metastable and equilibrium curves. Compute total monopole density n_tot and specific heat C at each temperature. Write a CSV file with columns: T(K), n_tot_heating, n_tot_cooling, C_heating(J/K·site), C_cooling(J/K·site).
- Output file: `/app/outputs/mu_1_0_K.csv`
- Format: csv
- Contract: CSV with header: T(K), n_tot_heating, n_tot_cooling, C_heating(J/K·site), C_cooling(J/K·site). Numeric values, at least 50 rows.
- Scoring: scored by hidden verifier

### Step 2: DH simulation for |μ|=1.5 K
- Role: scored
- Action: Same procedure as for |μ|=1.0 K but with |μ| = 1.5 K. Write CSV.
- Output file: `/app/outputs/mu_1_5_K.csv`
- Format: csv
- Contract: CSV with header: T(K), n_tot_heating, n_tot_cooling, C_heating(J/K·site), C_cooling(J/K·site). Numeric values, at least 50 rows.
- Scoring: scored by hidden verifier

### Step 3: DH simulation for |μ|=1.8 K
- Role: scored
- Action: Same procedure as for |μ|=1.0 K but with |μ| = 1.8 K. Write CSV.
- Output file: `/app/outputs/mu_1_8_K.csv`
- Format: csv
- Contract: CSV with header: T(K), n_tot_heating, n_tot_cooling, C_heating(J/K·site), C_cooling(J/K·site). Numeric values, at least 50 rows.
- Scoring: scored by hidden verifier

### Step 4: Regime classification
- Role: scored (load-bearing)
- Action: Read the CSV files produced in the previous steps. Analyze the n_tot curves to identify the presence of first‑order transitions (discontinuities, hysteresis) and classify each |μ| into regime (i): metastable‑only transition, (ii): equilibrium first‑order transition with hysteresis, or (iii): no first‑order transition. Estimate the transition temperature where applicable. Write the results to classification.json.
- Output file: `/app/outputs/classification.json`
- Format: json
- Contract: JSON object with keys: regime_1_0K (string 'i'|'ii'|'iii'), regime_1_5K, regime_1_8K, transition_T_1_0K (float or null), transition_T_1_5K, transition_T_1_8K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mu_1_0_K.csv`
- `/app/outputs/mu_1_5_K.csv`
- `/app/outputs/mu_1_8_K.csv`
- `/app/outputs/classification.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mu_1_0_K.csv
- path: `/app/outputs/mu_1_0_K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw temperature sweep data for |μ|=1.0 K; checker recomputes regime classification from this.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `n_tot_heating`, `n_tot_cooling`, `C_heating(J/K·site)`, `C_cooling(J/K·site)`
  - `units`:
    - `T(K)`: K
    - `n_tot_heating`: dimensionless (site density)
    - `n_tot_cooling`: dimensionless (site density)
    - `C_heating(J/K·site)`: J/K per site
    - `C_cooling(J/K·site)`: J/K per site

### mu_1_5_K.csv
- path: `/app/outputs/mu_1_5_K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw temperature sweep data for |μ|=1.5 K; checker recomputes regime classification from this.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `n_tot_heating`, `n_tot_cooling`, `C_heating(J/K·site)`, `C_cooling(J/K·site)`
  - `units`:
    - `T(K)`: K
    - `n_tot_heating`: dimensionless (site density)
    - `n_tot_cooling`: dimensionless (site density)
    - `C_heating(J/K·site)`: J/K per site
    - `C_cooling(J/K·site)`: J/K per site

### mu_1_8_K.csv
- path: `/app/outputs/mu_1_8_K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw temperature sweep data for |μ|=1.8 K; checker recomputes regime classification from this.
- schema:
  - `type`: table
  - `required_columns`: `T(K)`, `n_tot_heating`, `n_tot_cooling`, `C_heating(J/K·site)`, `C_cooling(J/K·site)`
  - `units`:
    - `T(K)`: K
    - `n_tot_heating`: dimensionless (site density)
    - `n_tot_cooling`: dimensionless (site density)
    - `C_heating(J/K·site)`: J/K per site
    - `C_cooling(J/K·site)`: J/K per site

### classification.json
- path: `/app/outputs/classification.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Regime assignments and transition temperatures; compared to hidden paper‑reported reference with tolerance.
- schema:
  - `type`: object
  - `required`: `regime_1_0K`, `regime_1_5K`, `regime_1_8K`, `transition_T_1_0K`, `transition_T_1_5K`, `transition_T_1_8K`
  - `properties`:
    - `regime_1_0K`:
      - `type`: string
      - `enum`: `i`, `ii`, `iii`
    - `regime_1_5K`:
      - `type`: string
      - `enum`: `i`, `ii`, `iii`
    - `regime_1_8K`:
      - `type`: string
      - `enum`: `i`, `ii`, `iii`
    - `transition_T_1_0K`:
      - `type`: `number`, `null`
    - `transition_T_1_5K`:
      - `type`: `number`, `null`
    - `transition_T_1_8K`:
      - `type`: `number`, `null`

Notes: Checkers will validate CSV schemas and physical bounds, and compare classification against hidden paper‑derived reference values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mu_1_0_K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "n_tot_heating",
          "n_tot_cooling",
          "C_heating(J/K·site)",
          "C_cooling(J/K·site)"
        ],
        "units": {
          "T(K)": "K",
          "n_tot_heating": "dimensionless (site density)",
          "n_tot_cooling": "dimensionless (site density)",
          "C_heating(J/K·site)": "J/K per site",
          "C_cooling(J/K·site)": "J/K per site"
        }
      },
      "description": "Raw temperature sweep data for |μ|=1.0 K; checker recomputes regime classification from this."
    },
    {
      "file": "mu_1_5_K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "n_tot_heating",
          "n_tot_cooling",
          "C_heating(J/K·site)",
          "C_cooling(J/K·site)"
        ],
        "units": {
          "T(K)": "K",
          "n_tot_heating": "dimensionless (site density)",
          "n_tot_cooling": "dimensionless (site density)",
          "C_heating(J/K·site)": "J/K per site",
          "C_cooling(J/K·site)": "J/K per site"
        }
      },
      "description": "Raw temperature sweep data for |μ|=1.5 K; checker recomputes regime classification from this."
    },
    {
      "file": "mu_1_8_K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T(K)",
          "n_tot_heating",
          "n_tot_cooling",
          "C_heating(J/K·site)",
          "C_cooling(J/K·site)"
        ],
        "units": {
          "T(K)": "K",
          "n_tot_heating": "dimensionless (site density)",
          "n_tot_cooling": "dimensionless (site density)",
          "C_heating(J/K·site)": "J/K per site",
          "C_cooling(J/K·site)": "J/K per site"
        }
      },
      "description": "Raw temperature sweep data for |μ|=1.8 K; checker recomputes regime classification from this."
    },
    {
      "file": "classification.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "regime_1_0K",
          "regime_1_5K",
          "regime_1_8K",
          "transition_T_1_0K",
          "transition_T_1_5K",
          "transition_T_1_8K"
        ],
        "properties": {
          "regime_1_0K": {
            "type": "string",
            "enum": [
              "i",
              "ii",
              "iii"
            ]
          },
          "regime_1_5K": {
            "type": "string",
            "enum": [
              "i",
              "ii",
              "iii"
            ]
          },
          "regime_1_8K": {
            "type": "string",
            "enum": [
              "i",
              "ii",
              "iii"
            ]
          },
          "transition_T_1_0K": {
            "type": [
              "number",
              "null"
            ]
          },
          "transition_T_1_5K": {
            "type": [
              "number",
              "null"
            ]
          },
          "transition_T_1_8K": {
            "type": [
              "number",
              "null"
            ]
          }
        }
      },
      "description": "Regime assignments and transition temperatures; compared to hidden paper‑reported reference with tolerance."
    }
  ],
  "notes": "Checkers will validate CSV schemas and physical bounds, and compare classification against hidden paper‑derived reference values."
}
```

## How you are scored
A hidden automated verifier inspects each output file independently. For the CSV files, the verifier validates the schema, checks that values are within physically reasonable bounds, and recomputes the density curves to identify any discontinuities and hysteresis. For the classification.json file, the verifier compares your regime assignments and transition temperatures against a hidden reference derived from the expected results of the Debye–Hückel model. The total reward is a weighted combination of scores from all stages: the regime labels carry the largest weight, followed by the transition temperatures, and finally the specific heat curves. Successfully reproducing the correct physical behaviour in your simulation is what earns credit; reporting numbers that match a reference without a valid underlying computation will not yield a high score.
