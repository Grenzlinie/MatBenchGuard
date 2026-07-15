# Phonon Density of States and Specific Heat of Vacancy-Disordered Graphane via Forced Vibrational Method

## Problem background
Graphane is a two-dimensional hydrocarbon obtained by reversible hydrogenation of graphene. Vacancies—created by removing carbon atoms together with their attached hydrogen atoms—alter its vibrational spectrum. Understanding how the vacancy concentration changes the phonon density of states (PDOS), shifts the Raman-active E₂g mode, and affects the constant-volume specific heat capacity is essential for graphane-based electronics and thermal management.

## Approach
We use the forced vibrational method to compute the phonon density of states for large finite graphane clusters. A chair-conformer graphane supercell of ~21000 atoms is built with free boundary conditions. Random vacancy defects are introduced at concentrations of 0%, 10%, 20%, and 30% by removing carbon–hydrogen pairs. Harmonic force constants up to the fourth nearest neighbour are assigned, with the C–H bond strength set to 445 N m⁻¹. For each driving frequency, random periodic forces are applied to every atom, the equations of motion are solved numerically, and the averaged total energy yields the PDOS. From the PDOS we locate the Raman‑active E₂g peak near 1350 cm⁻¹ and track its frequency as a function of vacancy concentration. Finally, the constant‑volume specific heat capacity is obtained from the PDOS via the standard thermodynamic relation.

## Reproduction target
For graphane with vacancy concentrations of 0%, 10%, 20%, and 30%:

- Compute the phonon density of states over the range 0–3000 cm⁻¹ and supply the curves for the pristine (0%) and the 30% vacancy cases together in a CSV file.
- Extract the frequency of the Raman‑active E₂g peak near 1350 cm⁻¹ for each concentration and report them in a CSV file.
- Calculate the constant‑volume specific heat capacity C_V as a function of temperature from 50 K to 700 K for all four concentrations and report the results in a CSV file.

The hidden verifier will independently assess the outputs for physical correctness and consistency.

## Assets

- jishi_force_constants.json
- graphane_unit_cell.xyz
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Build graphane structures with vacancy defects
- Role: process
- Action: Construct the chair-conformer graphane supercell of ~21000 atoms with free boundary conditions using the provided graphane_unit_cell.xyz. Introduce random vacancy defects at concentrations 0%, 10%, 20%, 30% by removing carbon atoms together with their attached hydrogen atoms. Assign force constants up to 4th nearest neighbor from jishi_force_constants.json and set the C-H bond force constant to 445 N/m.
- Evidence: `/app/outputs/graphane_systems.pkl`

### Step 2: Compute phonon density of states via forced vibrational method
- Role: process
- Action: Implement the forced vibrational method: apply random periodic forces to each atom, solve the equations of motion numerically for each driving frequency, accumulate the averaged total energy, and extract the PDOS g(Ω) from the formula. Run this for every vacancy concentration (0%, 10%, 20%, 30%) over the frequency interval 0–3000 cm⁻¹ with a fine grid (step ≤ 5 cm⁻¹). Save the computed PDOS arrays (frequency grid and g(Ω) values for each concentration) for later steps.
- Evidence: `/app/outputs/pdos_arrays.npz`

### Step 3: Export PDOS curves for pristine and 30% vacancy graphane
- Role: scored
- Action: From the computed PDOS arrays, extract the frequency grid and the PDOS for pristine (0%) graphane and for 30% vacancy graphane. Write a CSV file with columns: frequency (cm⁻¹), PDOS_pristine, PDOS_30. The frequency range must cover 0–3000 cm⁻¹ with a step no larger than 5 cm⁻¹.
- Output file: `/app/outputs/pdos_pristine_30.csv`
- Format: csv
- Contract: Columns: frequency (float, cm⁻¹), PDOS_pristine (float), PDOS_30 (float). Rows cover 0–3000 cm⁻¹ with spacing ≤5 cm⁻¹.
- Scoring: scored by hidden verifier

### Step 4: Extract E2g Raman peak frequencies
- Role: scored (load-bearing)
- Action: For each vacancy concentration (0%, 10%, 20%, 30%), locate the Raman-active E2g peak (in-plane transverse optical mode near 1350 cm⁻¹) in the PDOS. Record the exact frequency of that peak. If the peak has disappeared or is reduced to a shoulder for high vacancy concentrations, record the frequency at the maximum of the remaining shoulder feature. Write a CSV file with columns: vacancy_concentration, e2g_frequency.
- Output file: `/app/outputs/e2g_peaks.csv`
- Format: csv
- Contract: Columns: vacancy_concentration (float, percent), e2g_frequency (float, cm⁻¹). Rows: 0, 10, 20, 30.
- Scoring: scored by hidden verifier

### Step 5: Calculate constant-volume specific heat capacity
- Role: scored
- Action: Using the PDOS arrays for all four vacancy concentrations, evaluate the constant-volume specific heat C_V(T) via the expression from Lee and Gonze for T from 50 K to 700 K with a step no larger than 50 K. Write a CSV file with columns: temperature_K, C_V_pristine, C_V_10, C_V_20, C_V_30.
- Output file: `/app/outputs/specific_heat.csv`
- Format: csv
- Contract: Columns: temperature_K (float, K), C_V_pristine (float, J/(mol·K)), C_V_10 (float), C_V_20 (float), C_V_30 (float). Rows from 50 K to 700 K with spacing ≤50 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pdos_pristine_30.csv`
- `/app/outputs/e2g_peaks.csv`
- `/app/outputs/specific_heat.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pdos_pristine_30.csv
- path: `/app/outputs/pdos_pristine_30.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: PDOS curves for pristine and 30% vacancy graphane. The checker will verify a downward shift in the intermediate-frequency region (500–1500 cm⁻¹) via normalized cumulative difference.
- schema:
  - `type`: table
  - `required_columns`: `frequency`, `PDOS_pristine`, `PDOS_30`
  - `units`:
    - `frequency`: cm^-1
    - `PDOS_pristine`: arbitrary
    - `PDOS_30`: arbitrary

### e2g_peaks.csv
- path: `/app/outputs/e2g_peaks.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: E2g Raman peak frequencies for each vacancy concentration. The checker compares these values against digitized reference results and verifies monotonic decrease.
- schema:
  - `type`: table
  - `required_columns`: `vacancy_concentration`, `e2g_frequency`
  - `units`:
    - `vacancy_concentration`: %
    - `e2g_frequency`: cm^-1

### specific_heat.csv
- path: `/app/outputs/specific_heat.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Constant-volume specific heat capacity vs temperature for all four structures. The checker verifies monotonic decrease of C_V with vacancy concentration at selected temperatures.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `C_V_pristine`, `C_V_10`, `C_V_20`, `C_V_30`
  - `units`:
    - `temperature_K`: K
    - `C_V_pristine`: J/(mol·K)
    - `C_V_10`: J/(mol·K)
    - `C_V_20`: J/(mol·K)
    - `C_V_30`: J/(mol·K)

Notes: The PDOS CSV provides raw curves for structural analysis; the E2g peak CSV is compared to reference values from the paper with hidden tolerances; the specific heat CSV is structurally audited for monotonic trends with a relative error bound. All outputs are derived from the PDOS arrays computed in the process steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pdos_pristine_30.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency",
          "PDOS_pristine",
          "PDOS_30"
        ],
        "units": {
          "frequency": "cm^-1",
          "PDOS_pristine": "arbitrary",
          "PDOS_30": "arbitrary"
        }
      },
      "description": "PDOS curves for pristine and 30% vacancy graphane. The checker will verify a downward shift in the intermediate-frequency region (500–1500 cm⁻¹) via normalized cumulative difference."
    },
    {
      "file": "e2g_peaks.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "vacancy_concentration",
          "e2g_frequency"
        ],
        "units": {
          "vacancy_concentration": "%",
          "e2g_frequency": "cm^-1"
        }
      },
      "description": "E2g Raman peak frequencies for each vacancy concentration. The checker compares these values against digitized reference results and verifies monotonic decrease."
    },
    {
      "file": "specific_heat.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "C_V_pristine",
          "C_V_10",
          "C_V_20",
          "C_V_30"
        ],
        "units": {
          "temperature_K": "K",
          "C_V_pristine": "J/(mol·K)",
          "C_V_10": "J/(mol·K)",
          "C_V_20": "J/(mol·K)",
          "C_V_30": "J/(mol·K)"
        }
      },
      "description": "Constant-volume specific heat capacity vs temperature for all four structures. The checker verifies monotonic decrease of C_V with vacancy concentration at selected temperatures."
    }
  ],
  "notes": "The PDOS CSV provides raw curves for structural analysis; the E2g peak CSV is compared to reference values from the paper with hidden tolerances; the specific heat CSV is structurally audited for monotonic trends with a relative error bound. All outputs are derived from the PDOS arrays computed in the process steps."
}
```

## How you are scored
Your submitted artifacts (`pdos_pristine_30.csv`, `e2g_peaks.csv`, `specific_heat.csv`) are evaluated by a hidden verifier that checks structural relationships and physical trends—without requiring you to match a pre‑given number. The PDOS curves must reflect the expected spectral redistribution caused by vacancies; the E₂g peak frequencies must exhibit the correct dependence on defect concentration; and the specific heat capacities must behave appropriately with temperature and vacancy level. Each scored artifact carries a weight, and the final reward is the weighted sum. Reproducing the underlying physics through a correct simulation is necessary; simply reporting values from the literature will not pass.
