# Thermoelectric Transport Simulation for Edge-Disordered Graphene Nanoribbons

## Problem background
Graphene nanoribbons (GNRs) are promising thermoelectric materials, but their high thermal conductivity limits efficiency. Edge disorder can suppress thermal conductivity while preserving the power factor. This work investigates how edge disorder concentration and ribbon length affect the thermoelectric power factor of zigzag GNRs, using computational simulations to obtain averaged transport coefficients.

## Approach
The agent will construct zigzag GNR structures with a fixed width and controlled edge disorder by randomly adding/removing edge carbon atoms at various concentrations and ribbon lengths. For each structure, the energy-dependent transmission is computed using the non-equilibrium Green's function (NEGF) method with a tight-binding Hamiltonian based on Slater-Koster parameters for carbon. The agent may use an open-source package such as Kwant or implement NEGF from scratch. Landauer integrals (K0, K1) at the Fermi energy and room temperature yield conductance and Seebeck coefficient, from which electrical conductivity and power factor are derived. Ensemble averaging over 1,000 independent disorder realizations for each (length, concentration) combination gives the length-dependent averaged transport coefficients. From these curves, the maximum power factor and the optimum ribbon length for each disorder concentration are extracted and compared.

## Reproduction target
Compute the length-dependent averaged electrical conductivity (<σ>), Seebeck coefficient (<S>), and power factor (<PF>) for edge-disordered zigzag GNRs with width 1.78 nm and thickness 0.335 nm, at room temperature and Fermi energy ε=0, for disorder concentrations C_d = 5%, 10%, 15%, 20%. For each C_d, produce a full dataset covering at least L_g = 8.7, 50, 100, 150, 210, 250, 296.7 nm. Then, for each C_d, determine the maximum <PF> and the ribbon length at which it occurs (optimum L_g); if the data for C_d=5% shows a monotonic increase, report the longest length's value. The output must include the full ensemble-averaged table and the peak-summary table.

## Assets

- Kwant (quantum transport package): https://kwant-project.org/
- Slater-Koster tight-binding parameters for carbon: 10.1103/PhysRev.94.1498

## Workflow steps

### Step 1: Generate edge-disordered ZGNR structures
- Role: process
- Action: Create atomic configurations of zigzag graphene nanoribbons with a fixed width of 1.78 nm, lengths L_g ranging from 8.7 nm to 296.7 nm, and edge disorder concentrations C_d = 5%, 10%, 15%, 20%. For each (L_g, C_d) combination, generate an ensemble of 1,000 independent random disorder realizations by randomly adding/removing edge carbon atoms.
- Evidence: none

### Step 2: Compute transmission functions via NEGF
- Role: process
- Action: For each edge-disordered ZGNR structure sandwiched between semi-infinite pristine ZGNR leads, compute the transmission function ζ(ε) using the non-equilibrium Green's function method with a tight-binding Hamiltonian based on Slater-Koster parameters for carbon.
- Evidence: none

### Step 3: Compute per-configuration transport coefficients
- Role: process
- Action: From each transmission function, evaluate the Landauer integrals at the Fermi energy (ε=0) and temperature 300 K to obtain electrical conductance G and Seebeck coefficient S. Then compute electrical conductivity σ = (L_g/A) G, where area A = W × d with d=0.335 nm, and power factor PF = σ S² for each single disorder configuration.
- Evidence: none

### Step 4: Ensemble-averaged thermoelectric data
- Role: scored (load-bearing)
- Action: For each (L_g, C_d) combination, average the electrical conductivity, Seebeck coefficient, and power factor over the 1,000 disorder realizations to obtain <σ>, <S>, <PF>. Save the full length-dependent dataset to a CSV file.
- Output file: `/app/outputs/step_03_thermoelectric_data.csv`
- Format: csv
- Contract: CSV with columns: Lg_nm (float), Cd_percent (float), avg_sigma_S_per_m (float), avg_S_uV_per_K (float), avg_PF_mW_per_mK2 (float). One row per (Lg, Cd) combination, covering at least Lg=[8.7, 50, 100, 150, 210, 250, 296.7] nm and Cd=[5, 10, 15, 20].
- Scoring: scored by hidden verifier

### Step 5: Optimum power factor and length analysis
- Role: scored
- Action: From the data in step_03, determine for each disorder concentration C_d the maximum <PF> and the ribbon length L_g at which it occurs (optimum L_g). For C_d=5%, if <PF> is monotonic increasing, report the longest length's value. Save the summary to a CSV file.
- Output file: `/app/outputs/step_04_peak_results.csv`
- Format: csv
- Contract: CSV with columns: Cd_percent (float), max_PF_mW_per_mK2 (float), optimum_Lg_nm (float). One row per disorder concentration (5, 10, 15, 20).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_thermoelectric_data.csv`
- `/app/outputs/step_04_peak_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_thermoelectric_data.csv
- path: `/app/outputs/step_03_thermoelectric_data.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Ensemble-averaged length-dependent thermoelectric properties (conductivity, Seebeck coefficient, power factor) for each edge-disorder concentration. The hidden checker will compare these simulated values against digitized reference data from the paper and check structural trends.
- schema:
  - `type`: table
  - `required_columns`: `Lg_nm`, `Cd_percent`, `avg_sigma_S_per_m`, `avg_S_uV_per_K`, `avg_PF_mW_per_mK2`
  - `units`:
    - `Lg_nm`: nm
    - `Cd_percent`: %
    - `avg_sigma_S_per_m`: S/m
    - `avg_S_uV_per_K`: μV/K
    - `avg_PF_mW_per_mK2`: mW/(m·K^2)

### step_04_peak_results.csv
- path: `/app/outputs/step_04_peak_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum power factor and the ribbon length at which it occurs for each edge-disorder concentration. Verified against paper-reported numbers and the trend that optimum length decreases with increasing disorder.
- schema:
  - `type`: table
  - `required_columns`: `Cd_percent`, `max_PF_mW_per_mK2`, `optimum_Lg_nm`
  - `units`:
    - `Cd_percent`: %
    - `max_PF_mW_per_mK2`: mW/(m·K^2)
    - `optimum_Lg_nm`: nm

Notes: The scoring uses a combination of reference matching against hidden digitized values and structural trend checks (monotonicity, peak existence, ordering). Tolerances account for implementation differences and sampling noise. The load-bearing step_03 ensures the agent must genuinely execute the NEGF simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_thermoelectric_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Lg_nm",
          "Cd_percent",
          "avg_sigma_S_per_m",
          "avg_S_uV_per_K",
          "avg_PF_mW_per_mK2"
        ],
        "units": {
          "Lg_nm": "nm",
          "Cd_percent": "%",
          "avg_sigma_S_per_m": "S/m",
          "avg_S_uV_per_K": "μV/K",
          "avg_PF_mW_per_mK2": "mW/(m·K^2)"
        }
      },
      "description": "Ensemble-averaged length-dependent thermoelectric properties (conductivity, Seebeck coefficient, power factor) for each edge-disorder concentration. The hidden checker will compare these simulated values against digitized reference data from the paper and check structural trends."
    },
    {
      "file": "step_04_peak_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Cd_percent",
          "max_PF_mW_per_mK2",
          "optimum_Lg_nm"
        ],
        "units": {
          "Cd_percent": "%",
          "max_PF_mW_per_mK2": "mW/(m·K^2)",
          "optimum_Lg_nm": "nm"
        }
      },
      "description": "Maximum power factor and the ribbon length at which it occurs for each edge-disorder concentration. Verified against paper-reported numbers and the trend that optimum length decreases with increasing disorder."
    }
  ],
  "notes": "The scoring uses a combination of reference matching against hidden digitized values and structural trend checks (monotonicity, peak existence, ordering). Tolerances account for implementation differences and sampling noise. The load-bearing step_03 ensures the agent must genuinely execute the NEGF simulations."
}
```

## How you are scored
Your submitted artifacts are scored by a hidden verifier that reads `step_03_thermoelectric_data.csv` and `step_04_peak_results.csv`. For step_03, the verifier compares your averaged power factor values against a hidden reference (digitized from the paper) at key conditions and checks structural trends: monotonic increase for C_d=5% and presence of a single maximum for C_d≥10%. For step_04, the verifier checks that your reported maximum power factor and optimum length follow the required ordering across disorder concentrations. Reward is proportional to the correctness and closeness of these quantities, with tolerances set to account for implementation differences and stochastic sampling. Reporting the paper's numbers is not enough; the verifier validates the full set of simulated values and their relationships.
