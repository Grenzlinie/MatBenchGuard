# Thermodynamic equilibrium calculation for austenite stabilization via paraequilibrium cementite conversion

## Problem background
Low-alloy Fe-Mn-Si steels can exhibit transformation-induced plasticity (TRIP) effects when dispersed austenite particles are sufficiently stabilized. Conventional intercritical annealing often produces austenite with inadequate stability. One potential route to improve stability is a two-step annealing treatment: a soft annealing step below the A1 temperature produces a fine dispersion of Mn‑enriched cementite in ferrite, followed by a short intercritical annealing where carbon diffusion allows austenite to nucleate on the cementite particles. Under paraequilibrium conditions (carbon partitions but substitutional elements like Mn and Si do not), the newly formed austenite can inherit the high Mn and C contents of the cementite, possibly leading to chemical stabilization. The thermodynamic feasibility of this mechanism can be assessed through CALPHAD calculations: the enrichment of Mn in cementite, the stability of equilibrium austenite, the driving forces for the paraequilibrium conversion, and the expected martensite-start (Ms) temperature of the converted austenite. This task reproduces those thermodynamic predictions from first principles.

## Approach
The calculations are performed using open-source CALPHAD software (pycalphad) with a public thermodynamic database for the Fe-Mn-Si-C system containing the relevant phases (FCC_A1, BCC_A2, CEMENTITE). The general approach consists of four stages:  
1. **Equilibrium cementite Mn content** — for the alloy Fe-1.8Mn-1.0Si-0.10C (mass%), compute the equilibrium between ferrite and cementite at several soft-annealing temperatures and extract the Mn mass fraction in cementite.  
2. **Equilibrium austenite Ms** — at a set of intercritical temperatures, determine the equilibrium austenite composition (C, Mn, Si) and then apply the Ishida thermodynamic model to estimate the Ms temperature.  
3. **Paraequilibrium model** — define a non‑partitioning fictitious element M that represents the combined Mn and Si content. Construct a constrained Gibbs energy minimization to compute the driving forces for the formation of austenite in paraequilibrium with cementite (γ_c^p) and with ferrite (γ_α^p), using the cementite composition inherited from the soft annealing at 650 °C.  
4. **Ms estimate for the paraequilibrium austenite** — apply the same Ishida model to an austenite composition that inherits 17 mass % Mn and 0.5 mass % C (representative of the cementite conversion).  
All quantities are computed and written to the required output files.

## Reproduction target
Produce the four output files that capture the thermodynamic quantities underlying the paraequilibrium cementite-to-austenite conversion:  
- `/app/outputs/cementite_Mn_vs_temperature.csv`: Mn mass content (in mass %) in cementite vs. soft‑annealing temperature.  
- `/app/outputs/equilibrium_austenite_Ms_vs_temperature.csv`: Ms temperature (in °C) of equilibrium austenite vs. intercritical annealing temperature.  
- `/app/outputs/paraequilibrium_driving_forces.csv`: driving forces (in J mol⁻¹) for the formation of γ_c^p and γ_α^p as a function of temperature.  
- `/app/outputs/paraequilibrium_austenite_Ms.txt`: a single number giving the estimated Ms temperature of the paraequilibrium austenite with 17 mass % Mn and 0.5 mass % C.  
The task is considered successful if all files are computed according to the described workflow and conform to the required formats.

## Assets

- pycalphad: https://pypi.org/project/pycalphad/
- Fe-Mn-Si-C CALPHAD database

## Workflow steps

### Step 1: Paraequilibrium phase model construction
- Role: process
- Action: Construct the paraequilibrium condition: define a non-partitioning element M that represents the combined content of Mn and Si. Implement constrained Gibbs energy minimization to compute the driving force for precipitation of austenite from cementite (γ_c^p) and from ferrite (γ_α^p) under the constraint that M does not re‑partition. The model must be able to evaluate the driving force at various intercritical temperatures with the starting cementite composition from a soft annealing at 650°C.
- Evidence: `/app/outputs/paraeq_setup.log`

### Step 2: Cementite Mn enrichment calculation
- Role: scored
- Action: For soft-annealing temperatures 500, 550, 600, 650, 700, 750°C, compute the equilibrium between ferrite (BCC) and cementite for the alloy Fe-1.8Mn-1.0Si-0.10C (mass%). Extract the Mn mass content (in mass%) in cementite and output as a function of temperature.
- Output file: `/app/outputs/cementite_Mn_vs_temperature.csv`
- Format: csv
- Contract: Columns: temperature_C (float), Mn_content_mass_pct (float). Rows for temperatures: 500, 550, 600, 650, 700, 750°C.
- Scoring: scored by hidden verifier

### Step 3: Equilibrium austenite Ms calculation
- Role: scored
- Action: For intercritical temperatures 720, 760, 800, 840, 880, 920°C, compute the equilibrium phases for the same alloy, determine the austenite composition (C, Mn, Si mass contents), and then apply the Ishida thermodynamic model to compute the Ms temperature. Output Ms versus temperature.
- Output file: `/app/outputs/equilibrium_austenite_Ms_vs_temperature.csv`
- Format: csv
- Contract: Columns: temperature_C (float), Ms_C (float). Rows for temperatures: 720, 760, 800, 840, 880, 920°C.
- Scoring: scored by hidden verifier

### Step 4: Paraequilibrium driving forces calculation
- Role: scored (load-bearing)
- Action: Using the paraequilibrium model constructed earlier, with cementite composition inherited from soft annealing at 650°C, compute the driving forces (in J/mol) for the formation of γ_c^p and γ_α^p at temperatures 750, 800, 850, 900, 950, 1000°C. Output both driving forces per temperature.
- Output file: `/app/outputs/paraequilibrium_driving_forces.csv`
- Format: csv
- Contract: Columns: temperature_C (float), driving_force_gamma_cp_J_per_mol (float), driving_force_gamma_ap_J_per_mol (float). Rows for temperatures: 750, 800, 850, 900, 950, 1000°C.
- Scoring: scored by hidden verifier

### Step 5: Ms estimate for paraequilibrium-converted austenite
- Role: scored
- Action: Apply the Ishida thermodynamic Ms model to an austenite composition of 17 mass% Mn and 0.5 mass% C. Compute the Ms temperature and output the value.
- Output file: `/app/outputs/paraequilibrium_austenite_Ms.txt`
- Format: txt
- Contract: A single line with a floating-point number, e.g., -10.5
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cementite_Mn_vs_temperature.csv`
- `/app/outputs/equilibrium_austenite_Ms_vs_temperature.csv`
- `/app/outputs/paraequilibrium_driving_forces.csv`
- `/app/outputs/paraequilibrium_austenite_Ms.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cementite_Mn_vs_temperature.csv
- path: `/app/outputs/cementite_Mn_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cementite Mn mass content vs soft-annealing temperature. The checker verifies the overall trend (Mn content increases as temperature decreases) and compares the value at 650°C to the paper's reference (~17 mass%) within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `Mn_content_mass_pct`
  - `units`:
    - `temperature_C`: Celsius
    - `Mn_content_mass_pct`: mass percent

### equilibrium_austenite_Ms_vs_temperature.csv
- path: `/app/outputs/equilibrium_austenite_Ms_vs_temperature.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium austenite Ms temperature vs intercritical annealing temperature. The checker checks that Ms decreases monotonically with temperature and compares each point to paper-derived gold within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `Ms_C`
  - `units`:
    - `temperature_C`: Celsius
    - `Ms_C`: Celsius

### paraequilibrium_driving_forces.csv
- path: `/app/outputs/paraequilibrium_driving_forces.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Driving forces for paraequilibrium austenite formation from cementite and ferrite. The checker verifies that the driving force for γ_c^p is greater than for γ_α^p at every temperature and compares values to paper-derived gold within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `temperature_C`, `driving_force_gamma_cp_J_per_mol`, `driving_force_gamma_ap_J_per_mol`
  - `units`:
    - `temperature_C`: Celsius
    - `driving_force_gamma_cp_J_per_mol`: J/mol
    - `driving_force_gamma_ap_J_per_mol`: J/mol

### paraequilibrium_austenite_Ms.txt
- path: `/app/outputs/paraequilibrium_austenite_Ms.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Ms temperature estimate for austenite that inherits 17% Mn and 0.5% C from cementite. The checker compares the value to the paper's estimate (-10°C) within a tolerance.
- schema:
  - `type`: text
  - `description`: A single floating-point number on its own line, representing Ms temperature in °C.

Notes: This task reproduces purely thermodynamic calculations supporting the claim of austenite stabilization via paraequilibrium cementite-to-austenite conversion. Experimental dilatometry, TEM, and EELS are not included. The checker uses paper-derived reference values and trend checks.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cementite_Mn_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "Mn_content_mass_pct"
        ],
        "units": {
          "temperature_C": "Celsius",
          "Mn_content_mass_pct": "mass percent"
        }
      },
      "description": "Cementite Mn mass content vs soft-annealing temperature. The checker verifies the overall trend (Mn content increases as temperature decreases) and compares the value at 650°C to the paper's reference (~17 mass%) within a tolerance."
    },
    {
      "file": "equilibrium_austenite_Ms_vs_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "Ms_C"
        ],
        "units": {
          "temperature_C": "Celsius",
          "Ms_C": "Celsius"
        }
      },
      "description": "Equilibrium austenite Ms temperature vs intercritical annealing temperature. The checker checks that Ms decreases monotonically with temperature and compares each point to paper-derived gold within a tolerance."
    },
    {
      "file": "paraequilibrium_driving_forces.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_C",
          "driving_force_gamma_cp_J_per_mol",
          "driving_force_gamma_ap_J_per_mol"
        ],
        "units": {
          "temperature_C": "Celsius",
          "driving_force_gamma_cp_J_per_mol": "J/mol",
          "driving_force_gamma_ap_J_per_mol": "J/mol"
        }
      },
      "description": "Driving forces for paraequilibrium austenite formation from cementite and ferrite. The checker verifies that the driving force for γ_c^p is greater than for γ_α^p at every temperature and compares values to paper-derived gold within tolerance."
    },
    {
      "file": "paraequilibrium_austenite_Ms.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number on its own line, representing Ms temperature in °C."
      },
      "description": "Ms temperature estimate for austenite that inherits 17% Mn and 0.5% C from cementite. The checker compares the value to the paper's estimate (-10°C) within a tolerance."
    }
  ],
  "notes": "This task reproduces purely thermodynamic calculations supporting the claim of austenite stabilization via paraequilibrium cementite-to-austenite conversion. Experimental dilatometry, TEM, and EELS are not included. The checker uses paper-derived reference values and trend checks."
}
```

## How you are scored
A hidden verifier will independently inspect each of the four scored output files. It compares your submitted numerical results against reference values and checks that expected trends (e.g., monotonicity, relative ordering between conditions) hold. Each artifact contributes a weighted share to the final reward, which is a single score between 0 and 1. The verifier does not merely read self‑reported numbers; it may re‑derive quantities from your raw data. Therefore, executing the full workflow as described is essential. The verifier uses hidden tolerances and criteria; your goal is to faithfully perform the thermodynamic calculations, not to guess a particular value.
