# Carbon Potential and Equilibrium Atmosphere Calculation for Carburizing

## Problem background
In gas carburizing and cyaniding of steel parts, uncontrolled carbon potential in the furnace atmosphere can lead to the deposition of carbon black and the formation of carbide networks in the surface layer, which seriously degrades mechanical properties. This work analyzes why, under the same treatment regime in a multi-zone continuous furnace, carbides appear in some steels but not in others. It aims to determine the safe carbon potential range and to compute equilibrium atmosphere compositions that avoid carbide formation.

## Approach
The analysis proceeds in three stages.

**Carbon activity and potential.**  The carbon activity $A_C$ in each furnace zone is calculated from the partial pressures of CO, H$_2$, and H$_2$O using a water-gas equilibrium relation, with temperature-dependent equilibrium constants.  From $A_C$ and the furnace temperature, a published empirical formula gives the carbon potential $C_b$ (the carbon content of unalloyed austenite that would be in equilibrium with the atmosphere).  The theoretical boundary for carbon black deposition is defined as the carbon potential evaluated at $A_C=1$.

**Surface carbon and alloying effects.**  Carbon diffusion into the steel is modelled as one‑dimensional diffusion in unalloyed austenite following Fick's law, with a constant mass‑transfer coefficient that couples the gas atmosphere to the surface.  The diffusion coefficient follows an Arrhenius temperature dependence.  Simulating the complete time‑temperature schedule of the three furnace zones yields the surface carbon concentration $C_{\text{surf}}$ for two steels that contain different initial carbon contents.  The effect of alloying elements (Si, Mn, Cr, Ni) is then incorporated via a correction formula that relates the surface carbon content in unalloyed austenite to that in alloyed austenite, producing the alloyed surface carbon content $C_a$ and an alloying coefficient $f$.

**Optimum equilibrium atmosphere.**  Using gas equilibria (water‑gas and Boudouard reactions), several equilibrium compositions of CO, CO$_2$, H$_2$, H$_2$O, CH$_4$, and N$_2$ are calculated that maintain the carbon potential in the safe range 0.75–0.94 % at 820 °C.  Each composition is accompanied by its carbon activity, carbon potential, and dew point.

## Reproduction target
Reproduce the following three sets of computed quantities:

1.  For each of the three furnace zones (zone 1 at 810 °C, zone 2 at 830 °C, zone 3 at 820 °C): the carbon deposition boundary ($C_b$ at $A_C=1$), the actual carbon activity $A_C$, and the actual carbon potential $C_b$.
2.  For two steels with initial carbon contents 0.08 % and 0.35 %, under both the actual cyaniding regime and a modified regime: the surface carbon concentration in unalloyed austenite ($C_\text{surf}$), the alloyed surface carbon content ($C_a$), and the alloying coefficient $f$, obtained by simulating carbon diffusion through the three‑zone schedule.
3.  Six equilibrium atmosphere compositions (CO, CO$_2$, CH$_4$, H$_2$, H$_2$O, N$_2$) at 820 °C that yield a carbon potential between 0.75 % and 0.94 %, together with the corresponding carbon activity, carbon potential, and dew point.

All input data required for these calculations (gas compositions, temperatures, dew points, zone hold times, equilibrium constants, diffusion parameters, mass‑transfer coefficient, and steel compositions) are provided in this instruction.  Your task is to implement the thermodynamic and diffusion calculations described in the Approach section and write the results to the three output files listed under **Output files**.

## Assets

- Python scientific computing stack (numpy, scipy): numpy scipy

## Input data

The following numerical values are extracted from the paper and must be used for all calculations.  Write them to `/app/outputs/inputs.json` in the structured format shown.

### Zone operating parameters

| Zone | Temperature (°C) | CO (vol%) | H2 (vol%) | CO2 (vol%) | CH4 (vol%) | H2O (vol%) | N2 (vol%) | Dew point (°C) | Hold time (h) |
|------|-------------------|-----------|-----------|------------|------------|------------|-----------|----------------|---------------|
| 1    | 810               | 12.0      | 15.0      | 0.20       | 5.3        | 0.265      | 67.235    | -11            | 0.83333       |
| 2    | 830               | 15.0      | 16.0      | 0.22       | 5.35       | 0.208      | 63.222    | -14            | 0.50          |
| 3    | 820               | 17.2      | 18.0      | 0.18       | 5.6        | 0.189      | 58.831    | -15            | 0.33333       |

H2O content is computed from the dew point using the saturation vapour pressure of water at the total pressure of \(1\times10^5\) Pa.

### Equilibrium constants

- Water-gas reaction \(\mathrm{CO} + \mathrm{H_2} \rightleftharpoons [\mathrm{C}] + \mathrm{H_2O}\):
  - \(K\) at 810 °C = 0.025
  - \(K\) at 820 °C = 10.36
  - \(K\) at 830 °C = 11.85
- Boudouard reaction \(2\mathrm{CO} \rightleftharpoons \mathrm{CO_2} + [\mathrm{C}]\):
  - \(K\) at 820 °C = 10.337

### Mass transfer coefficient

- \(b_t = 0.2\ \text{mm h}^{-1}\)

### Diffusion parameters (carbon in austenite)

- Pre‑exponential factor \(D_0 = 0.05\ \text{cm}^2\!/\text{s}\)
- Activation energy \(E = 121\,000\ \text{J mol}^{-1}\)

### Steel compositions

| Steel | Initial C (%) | Si (%) | Mn (%) | Ni (%) | Cr (%) |
|-------|---------------|--------|--------|--------|--------|
| 08kp  | 0.08          | 0.03   | 0.305  | 0      | 0      |
| 35G2  | 0.35          | 0.29   | 1.50   | 0      | 0      |

### cyaniding regimes

- Actual regime: hold times exactly as given in the zone table.
- Calculated regime: same hold times for zones 1 and 2 as the actual regime; zone 3 hold time for 35G2 is 0.33 h, for 08kp is 0.50 h, and the carbon potential in zone 3 is set to 1.20 % for 35G2 and left at 1.35 % for 08kp (these correspond to the “Calculated” rows in Table 3).

## Workflow steps

### Step 1: Prepare input data
- Role: process
- Action: Read the input data provided in the Input Data section above and write a structured JSON file `/app/outputs/inputs.json` containing all the provided values.
- Evidence: `/app/outputs/inputs.json`

### Step 2: Compute carbon black boundaries and actual carbon potentials
- Role: scored
- Action: Using the gas compositions, temperatures, and equilibrium constants K from the input data, compute for each furnace zone: the carbon deposition boundary C_b at A_C=1, the actual carbon activity A_C, and the actual carbon potential C_b. Write the results to a CSV.
- Output file: `/app/outputs/table2_results.csv`
- Format: csv
- Contract: CSV with columns: zone (int), temperature_C (float), boundary_Cb (float), A_C (float), C_b (float).
- Scoring: scored by hidden verifier

### Step 3: Compute surface carbon concentrations for unalloyed and alloyed steels
- Role: scored (load-bearing)
- Action: Simulate carbon diffusion profiles using the mass transfer coefficient bt and diffusion equations, compute surface carbon C_surf for steels with initial carbon 0.08% and 0.35% under the actual and calculated cyaniding regimes (hold times from the input data). Apply the alloying correction formula to obtain alloyed surface carbon C_a and alloying coefficient f for steels 08kp and 35G2. Write the results to a CSV.
- Output file: `/app/outputs/table3_results.csv`
- Format: csv
- Contract: CSV with columns: steel (string), regime (string), C_surf (float), C_a (float), f (float).
- Scoring: scored by hidden verifier

### Step 4: Compute optimum equilibrium atmosphere compositions
- Role: scored
- Action: Using gas equilibrium equations and the target carbon potential range at 820°C, compute six equilibrium atmosphere compositions (CO, H2, CH4, CO2, H2O, N2) and their corresponding A_C, C_b, and dew point t_d. Write the results as a JSON array.
- Output file: `/app/outputs/table5_results.json`
- Format: json
- Contract: JSON array of 6 objects, each with keys: atmosphere (int), CO (float), CO2 (float), CH4 (float), H2 (float), H2O (float), N2 (float), A_C (float), C_b (float), t_d (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/table2_results.csv`
- `/app/outputs/table3_results.csv`
- `/app/outputs/table5_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### table2_results.csv
- path: `/app/outputs/table2_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reproduce the computed carbon black deposition boundary (at A_C=1) and the actual carbon activity and potential for each of the three furnace zones.
- schema:
  - `type`: table
  - `required_columns`: `zone`, `temperature_C`, `boundary_Cb`, `A_C`, `C_b`
  - `units`:
    - `temperature_C`: degree Celsius
    - `boundary_Cb`: percent
    - `A_C`: dimensionless
    - `C_b`: percent

### table3_results.csv
- path: `/app/outputs/table3_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reproduce the computed surface carbon concentrations for unalloyed (C_surf) and alloyed (C_a) steels under the actual and calculated cyaniding regimes, together with the alloying coefficient f.
- schema:
  - `type`: table
  - `required_columns`: `steel`, `regime`, `C_surf`, `C_a`, `f`
  - `units`:
    - `C_surf`: percent
    - `C_a`: percent
    - `f`: dimensionless

### table5_results.json
- path: `/app/outputs/table5_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Reproduce six optimum equilibrium atmosphere compositions that yield a carbon potential between 0.75% and 0.94% at 820°C, together with their carbon activity, carbon potential, and dew point.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `atmosphere`, `CO`, `CO2`, `CH4`, `H2`, `H2O`, `N2`, `A_C`, `C_b`, `t_d`
    - `units`:
      - `CO`: percent
      - `CO2`: percent
      - `CH4`: percent
      - `H2`: percent
      - `H2O`: percent
      - `N2`: percent
      - `A_C`: dimensionless
      - `C_b`: percent
      - `t_d`: degree Celsius

Notes: The hidden checker recomputes the required quantities from the public inputs using the same thermodynamic formulas and diffusion equations, and compares the agent's reported values to the paper's reported results within appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "table2_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "zone",
          "temperature_C",
          "boundary_Cb",
          "A_C",
          "C_b"
        ],
        "units": {
          "temperature_C": "degree Celsius",
          "boundary_Cb": "percent",
          "A_C": "dimensionless",
          "C_b": "percent"
        }
      },
      "description": "Reproduce the computed carbon black deposition boundary (at A_C=1) and the actual carbon activity and potential for each of the three furnace zones."
    },
    {
      "file": "table3_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "steel",
          "regime",
          "C_surf",
          "C_a",
          "f"
        ],
        "units": {
          "C_surf": "percent",
          "C_a": "percent",
          "f": "dimensionless"
        }
      },
      "description": "Reproduce the computed surface carbon concentrations for unalloyed (C_surf) and alloyed (C_a) steels under the actual and calculated cyaniding regimes, together with the alloying coefficient f."
    },
    {
      "file": "table5_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "atmosphere",
            "CO",
            "CO2",
            "CH4",
            "H2",
            "H2O",
            "N2",
            "A_C",
            "C_b",
            "t_d"
          ],
          "units": {
            "CO": "percent",
            "CO2": "percent",
            "CH4": "percent",
            "H2": "percent",
            "H2O": "percent",
            "N2": "percent",
            "A_C": "dimensionless",
            "C_b": "percent",
            "t_d": "degree Celsius"
          }
        }
      },
      "description": "Reproduce six optimum equilibrium atmosphere compositions that yield a carbon potential between 0.75% and 0.94% at 820°C, together with their carbon activity, carbon potential, and dew point."
    }
  ],
  "notes": "The hidden checker recomputes the required quantities from the public inputs using the same thermodynamic formulas and diffusion equations, and compares the agent's reported values to the paper's reported results within appropriate tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently recomputes the same thermodynamic and diffusion computations from the same input data and compares your output values against hidden reference values.  For each required numeric field in the three output files, the verifier checks whether your computed value matches the reference value within predetermined tolerances.  The three scored stages are weighted and their results are combined into a single reward between 0 and 1.  Simply reporting the paper's numbers is not sufficient; the verifier recalculates the quantities and judges your computed results.
