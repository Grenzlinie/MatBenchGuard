# Equilibrium Partial Pressures and Solubility Curves for Ti–N–H–Cl and Ti–N–Cl Chemical Systems

## Problem background
Selective area chemical vapor deposition (CVD) of titanium nitride (TiN) is a challenging process of interest in semiconductor fabrication. A proposed approach is the alternating cyclic (A.C.) method, which alternates between a deposition step (using TiCl₄ and NH₃) and an etching step that relies on an embedded disproportionation reaction to remove spurious nuclei. Understanding the thermodynamic boundaries between deposition and etching regimes is critical for designing a successful A.C. process. The present task addresses this problem by computing the equilibrium solid‑vapor solubility relations for the Ti‑N‑H‑Cl (deposition) and Ti‑N‑Cl (etching) chemical systems based on published thermochemical principles. The central objective is to determine, from equilibrium calculations, how the vapor‑phase titanium‑to‑chlorine (Ti/Cl) ratio varies as a function of temperature, total pressure, and input gas composition, and thereby to map the parameter space where TiN deposition or etching is thermodynamically favorable.

## Approach
Thermodynamic equilibrium is analyzed by considering the chemical species present in the gas phase and the solid TiN. For the deposition system, eleven vapor species are included: TiCl₄, TiCl₃, TiCl₂, TiCl, NH₃, N₂, H₂, Cl₂, HCl, H, and Cl; for the etching system, seven species are considered: TiCl₄, TiCl₃, TiCl₂, TiCl, N₂, Cl₂, and Cl. The constraints are the total pressure of the system, the fixed input molar ratios of TiCl₄ to NH₃ (for deposition) or the presence of excess solid TiN with TiCl₄ as the only Ti‑bearing input gas (for etching), and a set of independent chemical equilibria whose equilibrium constants are computed from standard Gibbs free energies of formation obtained from the JANAF thermochemical tables.

The computational approach is to minimize the total Gibbs free energy of the system, or equivalently to solve the set of nonlinear equations composed of the total pressure constraint, the component conservation constraints, and the equilibrium constant expressions. From the resulting equilibrium partial pressures, an **output vapor‑phase Ti/Cl ratio** is computed using a formula that accounts for all Ti‑ and Cl‑containing species; this ratio indicates the net direction (deposition or etching) relative to the input Ti/Cl ratio. The calculations are carried out over a range of temperatures for prescribed sets of total pressures and input compositions.

### Key definitions

#### Output vapor‑phase Ti/Cl ratio
The **output Ti/Cl ratio** is the ratio of total titanium atoms to total chlorine atoms in the gas phase at equilibrium. It is computed directly from the equilibrium partial pressures (in any consistent unit, e.g., Torr) as:

**Deposition system (Ti–N–H–Cl):**
\[
\text{Ti/Cl}_{\text{output}} = \frac{p_{\mathrm{TiCl_4}} + p_{\mathrm{TiCl_3}} + p_{\mathrm{TiCl_2}} + p_{\mathrm{TiCl}}}
{4 p_{\mathrm{TiCl_4}} + 3 p_{\mathrm{TiCl_3}} + 2 p_{\mathrm{TiCl_2}} + p_{\mathrm{TiCl}} + p_{\mathrm{HCl}} + 2 p_{\mathrm{Cl_2}} + p_{\mathrm{Cl}}}
\]

**Etching system (Ti–N–Cl):**
\[
\text{Ti/Cl}_{\text{output}} = \frac{p_{\mathrm{TiCl_4}} + p_{\mathrm{TiCl_3}} + p_{\mathrm{TiCl_2}} + p_{\mathrm{TiCl}}}
{4 p_{\mathrm{TiCl_4}} + 3 p_{\mathrm{TiCl_3}} + 2 p_{\mathrm{TiCl_2}} + p_{\mathrm{TiCl}} + 2 p_{\mathrm{Cl_2}} + p_{\mathrm{Cl}}}
\]

These definitions simply count the number of Ti atoms (each TiClₓ molecule contributes one Ti atom) in the numerator, and the total number of Cl atoms (counting multiplicities per species) in the denominator. Nitrogen‑ and hydrogen‑only species (N₂, NH₃, H₂, H) do not appear because they contain no Ti or Cl.

#### Input H/Cl ratio
For the deposition system, the input molar ratio of TiCl₄ to NH₃ fixes the initial ratio of hydrogen to chlorine atoms delivered to the system. Because one TiCl₄ molecule supplies 4 Cl atoms and one NH₃ molecule supplies 3 H atoms, the input **H/Cl atomic ratio** is:
\[
\frac{\mathrm{H}}{\mathrm{Cl}} = \frac{3\,n_{\mathrm{NH_3}}}{4\,n_{\mathrm{TiCl_4}}} = \frac{3}{4 \times (\mathrm{TiCl_4}/\mathrm{NH_3})}
\]
This ratio is conserved in the vapor phase throughout equilibrium and is used as a constraint when solving the deposition system.

#### Input Ti/Cl ratio and system constraints
- **Deposition**: The source gas TiCl₄ has an intrinsic Ti/Cl atomic ratio of 1/4. If TiN precipitates, the Ti/Cl ratio in the vapor phase will differ from 1/4. The equilibrium calculation must respect the total pressure, the H/Cl ratio derived from the TiCl₄/NH₃ feed, and the thermochemical equilibria.
- **Etching**: The Ti–N–Cl system contains **excess solid TiN**. The only gaseous titanium source is TiCl₄, giving an input Ti/Cl = 1/4. N₂ gas is present but is chemically inert in this context. The equilibrium calculation is constrained by the total pressure, the presence of solid TiN (activity = 1), and the thermochemical equilibria. The resulting output Ti/Cl ratio reflects the equilibrium partitioning of Ti and Cl between the gas phase and the solid TiN.

## Reproduction target
The goal is to produce three datasets:

1. A CSV file containing the equilibrium Ti/Cl output ratios for the Ti‑N‑H‑Cl deposition system at total pressures of 100 Torr, 0.5 Torr (500 mTorr), and 0.01 Torr (10 mTorr), each evaluated at two input TiCl₄/NH₃ molar ratios (1/2 and 1/5), over the temperature range 500–1500 K (covering at least the points 500, 600, 800, 1000, 1200, and 1500 K).

2. A CSV file containing the equilibrium Ti/Cl output ratios for the Ti‑N‑Cl etching system at the same three total pressures, over the same temperature range, with **excess solid TiN present** (TiCl₄ as the only Ti‑bearing input gas). No other input ratio is needed; the system is fully defined by total pressure, temperature, and the solid TiN activity.

3. A JSON file containing the equilibrium partial pressures (in Torr) of all eleven vapor species for one representative deposition condition: total pressure 0.5 Torr, TiCl₄/NH₃ = 1/2, at temperatures 800 K, 1000 K, and 1200 K. This raw data allows independent recomputation of the Ti/Cl ratio.

The accuracy of these outputs will be judged against the thermodynamic equilibrium values expected from the JANAF data and the specified constraints; the hidden verifier will quantify how closely the computed ratios match the reference.

## Assets

- JANAF Thermochemical Tables (3rd ed., 1985): [https://janaf.nist.gov/](https://janaf.nist.gov/)

## Workflow steps

### Step 1: Deposition solubility curves
- Role: scored
- Action: Obtain JANAF thermochemical data. Set up the Ti–N–H–Cl system with eleven vapor species (TiCl4, TiCl3, TiCl2, TiCl, NH3, N2, H2, Cl2, HCl, H, Cl) and solid TiN. Implement a Gibbs free energy minimization or nonlinear equation solver to compute equilibrium partial pressures at total pressures 100 Torr, 0.5 Torr (500 mTorr), 0.01 Torr (10 mTorr), for input TiCl4/NH3 ratios 1/2 and 1/5, over the temperature range 500–1500 K (at least points at 500, 600, 800, 1000, 1200, 1500 K). For each condition compute the output vapor‑phase Ti/Cl ratio using the **deposition formula** defined in the “Key definitions” section above. Output all ratios in a CSV.
- Output file: `/app/outputs/ti_cl_output_deposition.csv`
- Format: csv
- Contract: CSV with columns: total_pressure_Torr (float), TiCl4_NH3_ratio (float), temperature_K (float), Ti_Cl_output (float). Rows for each pressure–ratio–temperature point.
- Scoring: scored by hidden verifier

### Step 2: Etching solubility curve
- Role: scored
- Action: Set up the Ti–N–Cl system (seven vapor species: TiCl4, TiCl3, TiCl2, TiCl, N2, Cl2, Cl) and solid TiN. The solid TiN is in **excess** (activity = 1). Using the same JANAF data, solve the equilibrium equations for total pressures 100 Torr, 0.5 Torr, 0.01 Torr, over the temperature range 500–1500 K (at least points at 500, 600, 800, 1000, 1200, 1500 K). For each condition compute the output vapor‑phase Ti/Cl ratio using the **etching formula** defined in the “Key definitions” section above. Output the ratios in a CSV.
- Output file: `/app/outputs/ti_cl_output_etching.csv`
- Format: csv
- Contract: CSV with columns: total_pressure_Torr (float), temperature_K (float), Ti_Cl_output (float). Rows for each pressure–temperature point.
- Scoring: scored by hidden verifier

### Step 3: Deposition species partial pressures
- Role: scored (load-bearing)
- Action: Using the same solver and JANAF data, compute equilibrium partial pressures of all eleven vapor species for the deposition condition: total pressure 0.5 Torr (500 mTorr), TiCl4/NH3 = 1/2, at temperatures 800 K, 1000 K, and 1200 K. Output the partial pressures in structured JSON.
- Output file: `/app/outputs/species_pressures_deposition.json`
- Format: json
- Contract: JSON object with keys 'total_pressure_Torr' (float, 0.5), 'TiCl4_NH3_ratio' (float, 0.5), and 'points' (array). Each element of 'points' is an object with 'temperature_K' (float) and a dictionary of species partial pressures (keys: TiCl4, TiCl3, TiCl2, TiCl, NH3, N2, H2, Cl2, HCl, H, Cl; values in Torr as floats).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ti_cl_output_deposition.csv`
- `/app/outputs/ti_cl_output_etching.csv`
- `/app/outputs/species_pressures_deposition.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ti_cl_output_deposition.csv
- path: `/app/outputs/ti_cl_output_deposition.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Deposition solubility curves: equilibrium Ti/Cl output ratio versus temperature. Scored by comparing each reported ratio at prescribed (pressure, ratio, temperature) points against hidden paper‑derived values with a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `total_pressure_Torr`, `TiCl4_NH3_ratio`, `temperature_K`, `Ti_Cl_output`
  - `units`:
    - `total_pressure_Torr`: Torr
    - `TiCl4_NH3_ratio`: dimensionless
    - `temperature_K`: K
    - `Ti_Cl_output`: dimensionless

### ti_cl_output_etching.csv
- path: `/app/outputs/ti_cl_output_etching.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Etching solubility curve: equilibrium Ti/Cl output ratio versus temperature for the Ti‑N‑Cl system with excess solid TiN. Scored by comparing at hidden reference temperatures against paper‑derived values with tolerance.
- schema:
  - `type`: table
  - `required_columns`: `total_pressure_Torr`, `temperature_K`, `Ti_Cl_output`
  - `units`:
    - `total_pressure_Torr`: Torr
    - `temperature_K`: K
    - `Ti_Cl_output`: dimensionless

### species_pressures_deposition.json
- path: `/app/outputs/species_pressures_deposition.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw partial pressures of all vapor species for the deposition condition (0.5 Torr, TiCl4/NH3=1/2) at 800, 1000, 1200 K. The checker recomputes the Ti/Cl output ratio from these partial pressures and compares it to a hidden reference.
- schema:
  - `type`: object
  - `required`:
    - `total_pressure_Torr`: float
    - `TiCl4_NH3_ratio`: float
    - `points`: array
  - `items`:
    - `temperature_K`: float
    - `species`:
      - `TiCl4`: float
      - `TiCl3`: float
      - `TiCl2`: float
      - `TiCl`: float
      - `NH3`: float
      - `N2`: float
      - `H2`: float
      - `Cl2`: float
      - `HCl`: float
      - `H`: float
      - `Cl`: float
  - `units`: all partial pressures in Torr

Notes: All required thermodynamic data are publicly available from JANAF. The solver may be implemented using any open‑source Gibbs minimization or nonlinear equation solver (e.g., scipy.optimize, Cantera, pycalphad). The hidden checker compares ratios with a tolerance that accounts for minor algorithmic differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ti_cl_output_deposition.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_pressure_Torr",
          "TiCl4_NH3_ratio",
          "temperature_K",
          "Ti_Cl_output"
        ],
        "units": {
          "total_pressure_Torr": "Torr",
          "TiCl4_NH3_ratio": "dimensionless",
          "temperature_K": "K",
          "Ti_Cl_output": "dimensionless"
        }
      },
      "description": "Deposition solubility curves: equilibrium Ti/Cl output ratio versus temperature. Scored by comparing each reported ratio at prescribed (pressure, ratio, temperature) points against hidden paper‑derived values with a tolerance."
    },
    {
      "file": "ti_cl_output_etching.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "total_pressure_Torr",
          "temperature_K",
          "Ti_Cl_output"
        ],
        "units": {
          "total_pressure_Torr": "Torr",
          "temperature_K": "K",
          "Ti_Cl_output": "dimensionless"
        }
      },
      "description": "Etching solubility curve: equilibrium Ti/Cl output ratio versus temperature for the Ti‑N‑Cl system. Scored by comparing at hidden reference temperatures against paper‑derived values with tolerance."
    },
    {
      "file": "species_pressures_deposition.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "total_pressure_Torr": "float",
          "TiCl4_NH3_ratio": "float",
          "points": "array"
        },
        "items": {
          "temperature_K": "float",
          "species": {
            "TiCl4": "float",
            "TiCl3": "float",
            "TiCl2": "float",
            "TiCl": "float",
            "NH3": "float",
            "N2": "float",
            "H2": "float",
            "Cl2": "float",
            "HCl": "float",
            "H": "float",
            "Cl": "float"
          }
        },
        "units": "all partial pressures in Torr"
      },
      "description": "Raw partial pressures of all vapor species for the deposition condition (0.5 Torr, TiCl4/NH3=1/2) at 800, 1000, 1200 K. The checker recomputes the Ti/Cl output ratio from these partial pressures and compares it to a hidden reference."
    }
  ],
  "notes": "All required thermodynamic data are publicly available from JANAF. The solver may be implemented using any open‑source Gibbs minimization or nonlinear equation solver (e.g., scipy.optimize, Cantera, pycalphad). The hidden checker compares ratios with a tolerance that accounts for minor algorithmic differences."
}
```

## How you are scored
A hidden verifier evaluates your submitted artifacts independently. For the deposition and etching CSV files, the verifier compares each reported Ti/Cl output ratio at a set of hidden reference temperatures against the reference values using a tolerance that accounts for minor algorithmic differences. You earn reward proportional to the number of points meeting this tolerance.

For the species‑pressure JSON file, the verifier recomputes the Ti/Cl output ratio from the provided partial pressures using the same formula you were instructed to use. It then checks that the recomputed ratio matches the corresponding entry in your deposition CSV and compares it to a hidden reference for that condition. This step ensures that the equilibrium equations were genuinely solved.

The final reward is a weighted sum of the scores from these three artifacts, with the two CSV files carrying the bulk of the weight and the JSON serving as a load‑bearing consistency check. To succeed, you must compute the equilibria correctly; simply reporting a number—even if it happens to match the paper—will not pass the recomputation check.