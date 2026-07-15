# Thermodynamic Equilibrium Gas-Phase Composition Computation

## Problem background
Radioactive graphite from decommissioned nuclear reactors contains trace actinides (uranium, americium, plutonium). When heated in steam for disposal, these elements can volatilize into the gas phase, potentially creating environmental hazards. Understanding the temperature‑dependent speciation and partitioning of these actinides between condensed and gas phases is essential for safety assessments. The goal is to compute the equilibrium composition and distribution of U, Am, and Pu species over a wide temperature range, and to determine the equilibrium constants of the key chemical reactions that govern the phase transitions.

## Approach
Use thermodynamic equilibrium modeling based on Gibbs free energy minimization. The system consists of a gas phase (steam) and a condensed phase (graphite with trace U, Am, Pu, Ca, Cl). The initial mass fractions are: gas H₂O 75 %, condensed C ~99.98 %, U ~1.15×10⁻² %, Am ~9.99×10⁻⁶ %, Pu ~7.19×10⁻⁵ %, Ca ~2.69×10⁻⁴ %, Cl ~1.88×10⁻³ %. The set of chemical species to include covers condensed and gaseous forms of U, Am, Pu, Ca, Cl, C, H, O (e.g., oxides, chlorides, carbonates, ions, elemental gases). Thermochemical data (Gibbs free energy, enthalpy, entropy) for all species are retrieved from a public database. At each temperature from 373 K to 3273 K (step ≤100 K) and total pressure 1 atm, a Gibbs free energy minimizer (e.g., Cantera or a custom entropy‑maximization solver) is used to compute the equilibrium composition. From the resulting mole numbers, the mole fractions of the major uranium, americium, and plutonium species are extracted, normalized to the total amount of each element. Finally, the equilibrium constants ln K of the reactions that govern the main speciation changes are derived from the equilibrium concentrations using an ideal‑gas/condensed‑phase activity model, and fitted to the linear form ln K = a + b/T over the temperature intervals where each reaction is dominant. The workflow yields CSV tables of species distributions and fitted reaction coefficients.

## Reproduction target
Compute the mole fraction of each major uranium, americium, and plutonium species (condensed and gaseous) as a function of temperature (373–3273 K), and provide the fitted equilibrium constant coefficients (a, b in ln K = a + b/T) for the 20 key reactions that account for the observed phase transformations. The output consists of four CSV files: u_distribution.csv, am_distribution.csv, pu_distribution.csv, and equilibrium_constants.csv, formatted according to the specified schemas.

## Assets

- Public thermochemical database (NIST-JANAF or equivalent): https://janaf.nist.gov/
- Cantera or custom Gibbs free energy minimizer: https://cantera.org
- Python packages (numpy, scipy, pandas): numpy scipy pandas

## Workflow steps

### Step 1: Thermodynamic equilibrium simulation
- Role: process
- Action: Set up the chemical system with initial phase composition (gas H2O 75 % mass; condensed 75 % mass: C 99.98 %, U 1.15e-2 %, Am 9.99e-6 %, Pu 7.19e-5 %, Ca 2.69e-4 %, Cl 1.88e-3 %). Select the set of chemical species for U, Am, Pu, Ca, Cl, C, H, O as listed in Table 2 of the paper. Retrieve necessary thermodynamic properties (Gibbs free energy, enthalpy, entropy) from a public thermochemical database (e.g., NIST-JANAF or equivalent) for all selected species. Run Gibbs free energy minimization (using Cantera or a custom entropy-maximization solver) at temperatures from 373 K to 3273 K with a step of at most 100 K at a total pressure of 1 atm to obtain equilibrium composition (mole numbers) of all species.
- Evidence: `/app/outputs/equilibrium_raw_output.json`

### Step 2: Uranium species distribution
- Role: scored
- Action: From the equilibrium results, extract the mole fractions of the main uranium-bearing species: UO2(cr), UO2Cl2(cr), CaUO4(cr), UO3(g), UO3-, UO2+, UO2(g), normalizing to total uranium at each temperature.
- Output file: `/app/outputs/u_distribution.csv`
- Format: csv
- Contract: columns: T_K (float, K), species (string), mole_fraction (float, 0-1). species values: UO2(cr), UO2Cl2(cr), CaUO4(cr), UO3(g), UO3-, UO2+, UO2(g).
- Scoring: scored by hidden verifier

### Step 3: Americium species distribution
- Role: scored
- Action: From the equilibrium results, extract the mole fractions of Am-bearing species: AmO2(cr), Am2O3(cr), Am(g), normalizing to total americium at each temperature.
- Output file: `/app/outputs/am_distribution.csv`
- Format: csv
- Contract: columns: T_K (float, K), species (string), mole_fraction (float, 0-1). species values: AmO2(cr), Am2O3(cr), Am(g).
- Scoring: scored by hidden verifier

### Step 4: Plutonium species distribution
- Role: scored
- Action: From the equilibrium results, extract the mole fractions of Pu-bearing species: PuO2(cr), PuO2(g), PuO(g), PuO+, normalizing to total plutonium at each temperature.
- Output file: `/app/outputs/pu_distribution.csv`
- Format: csv
- Contract: columns: T_K (float, K), species (string), mole_fraction (float, 0-1). species values: PuO2(cr), PuO2(g), PuO(g), PuO+.
- Scoring: scored by hidden verifier

### Step 5: Equilibrium constant fitting for key reactions
- Role: scored (load-bearing)
- Action: Identify the 20 main reactions governing speciation changes from the composition results. For each reaction, compute the equilibrium constant ln K from the equilibrium concentrations using the ideal gas/condensed phase activity model. Fit ln K = a + b/T over the temperature intervals specified in the paper using linear regression.
- Output file: `/app/outputs/equilibrium_constants.csv`
- Format: csv
- Contract: columns: reaction_number (int), reaction (string, chemical equation), temperature_range_start_K (float), temperature_range_end_K (float), coefficient_a (float), coefficient_b (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/u_distribution.csv`
- `/app/outputs/am_distribution.csv`
- `/app/outputs/pu_distribution.csv`
- `/app/outputs/equilibrium_constants.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### u_distribution.csv
- path: `/app/outputs/u_distribution.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mole fraction of each uranium species at each temperature, derived from equilibrium simulation.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `species`, `mole_fraction`
  - `units`:
    - `T_K`: K
    - `mole_fraction`: fraction (0-1)

### am_distribution.csv
- path: `/app/outputs/am_distribution.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mole fraction of each americium species at each temperature.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `species`, `mole_fraction`
  - `units`:
    - `T_K`: K
    - `mole_fraction`: fraction (0-1)

### pu_distribution.csv
- path: `/app/outputs/pu_distribution.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Mole fraction of each plutonium species at each temperature.
- schema:
  - `type`: table
  - `required_columns`: `T_K`, `species`, `mole_fraction`
  - `units`:
    - `T_K`: K
    - `mole_fraction`: fraction (0-1)

### equilibrium_constants.csv
- path: `/app/outputs/equilibrium_constants.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Fitted parameters for ln K = a + b/T for each of the 20 reactions, using the temperature intervals from the paper.
- schema:
  - `type`: table
  - `required_columns`: `reaction_number`, `reaction`, `temperature_range_start_K`, `temperature_range_end_K`, `coefficient_a`, `coefficient_b`
  - `units`:
    - `temperature_range_start_K`: K
    - `temperature_range_end_K`: K

Notes: Species distributions are compared against reference values extracted from the paper at select temperatures; equilibrium constants compared against the paper's Table 3. Tolerances are set to accommodate legitimate solver/database differences.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "u_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "species",
          "mole_fraction"
        ],
        "units": {
          "T_K": "K",
          "mole_fraction": "fraction (0-1)"
        }
      },
      "description": "Mole fraction of each uranium species at each temperature, derived from equilibrium simulation."
    },
    {
      "file": "am_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "species",
          "mole_fraction"
        ],
        "units": {
          "T_K": "K",
          "mole_fraction": "fraction (0-1)"
        }
      },
      "description": "Mole fraction of each americium species at each temperature."
    },
    {
      "file": "pu_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_K",
          "species",
          "mole_fraction"
        ],
        "units": {
          "T_K": "K",
          "mole_fraction": "fraction (0-1)"
        }
      },
      "description": "Mole fraction of each plutonium species at each temperature."
    },
    {
      "file": "equilibrium_constants.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reaction_number",
          "reaction",
          "temperature_range_start_K",
          "temperature_range_end_K",
          "coefficient_a",
          "coefficient_b"
        ],
        "units": {
          "temperature_range_start_K": "K",
          "temperature_range_end_K": "K"
        }
      },
      "description": "Fitted parameters for ln K = a + b/T for each of the 20 reactions, using the temperature intervals from the paper."
    }
  ],
  "notes": "Species distributions are compared against reference values extracted from the paper at select temperatures; equilibrium constants compared against the paper's Table 3. Tolerances are set to accommodate legitimate solver/database differences."
}
```

## How you are scored
The hidden verifier independently checks each scored output file. For the species distribution files, it compares the reported mole fractions at selected temperature points against hidden reference values, using appropriate tolerances (wider for minor species). For the equilibrium constants file, it compares the fitted coefficients a and b for each reaction against hidden reference values with specified tolerances. The reward is a weighted sum of the scores across all four artifacts, with distributions and constants each contributing a substantial share. Simply reporting the correct numbers without genuine computation is detectable by the verifier and will not receive full credit.
