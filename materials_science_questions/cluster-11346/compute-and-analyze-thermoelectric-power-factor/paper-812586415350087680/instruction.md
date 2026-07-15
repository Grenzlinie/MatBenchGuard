# Compute Thermoelectric Lattice Thermal Conductivity and ZT from Transport Data

## Problem background
Thermoelectric materials directly convert heat into electricity, with performance quantified by the dimensionless figure of merit ZT = S²T/(κ_total ρ), where S is the Seebeck coefficient, T the absolute temperature, κ_total the total thermal conductivity, and ρ the electrical resistivity. The total thermal conductivity comprises electronic (κ_e) and lattice (κ_L) contributions; suppressing κ_L through phonon scattering while maintaining good electronic transport is a key strategy for enhancing ZT. In Bi₂Te₃-based alloys, doping and microstructural engineering can introduce multiscale phonon-scattering centers. This task addresses the Ga-excess p-type Bi₀.₄Sb₁.₆Te₃ system. The addition of Ga is intended to create point defects, alloy disorder, and grain-boundary phases that scatter phonons. The goal is to compute, from measured transport data, the resulting lattice thermal conductivity κ_L(T) and the figure of merit ZT(T) for the Ga-excess composition, thereby evaluating the thermoelectric response.

## Approach
The calculation relies on experimental transport data for the Ga-excess sample with nominal composition Ga₀.₀₃Bi₀.₄Sb₁.₆Te₃. The provided dataset contains temperature-dependent values of the Seebeck coefficient S, electrical resistivity ρ, and total thermal conductivity κ_total. From S, the reduced chemical potential η is determined by numerically solving the single parabolic band (SPB) model relation S = (k_B/e)·(2·F₁(η)/F₀(η) – η), where Fⱼ are Fermi–Dirac integrals. The temperature-dependent Lorenz number is then obtained as L = (k_B/e)²·[3·F₂(η)/F₀(η) – (2·F₁(η)/F₀(η))²]. Using the Wiedemann–Franz law, the electronic thermal conductivity is κ_e = L·T/ρ. The lattice thermal conductivity follows as κ_L = κ_total – κ_e. Finally, the figure of merit is computed pointwise as ZT = S²·T/(κ_total·ρ). All steps are applied over the temperature range covered by the data, yielding κ_L(T), ZT(T), and the maximum ZT value within that range. The workflow is implemented in standard numerical Python libraries and outputs the required artifacts.

## Reproduction target
From the public dataset `Ga_excess_BST_transport_data.csv` (columns: Temperature_K, Seebeck_uV_per_K, Resistivity_Ohm_m, Kappa_total_W_per_mK) for the x=0.03 sample, produce three scored output files under `/app/outputs`:
1. `kappa_L_vs_T.csv`: a CSV table of lattice thermal conductivity versus temperature (columns Temperature_K and kappa_L_W_per_mK), one row per measured temperature point.
2. `ZT_vs_T.csv`: a CSV table of the dimensionless figure of merit versus temperature (columns Temperature_K and ZT), one row per measured temperature point.
3. `max_ZT.txt`: a text file containing a single floating-point number that is the maximum ZT value found across the temperature range.
The temperature range must span all data points present in the input CSV. No external resources beyond the dataset and the standard Python libraries numpy and scipy are required.

## Assets

- Ga_excess_BST_transport_data.csv
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Load transport data
- Role: process
- Action: Read the public dataset Ga_excess_BST_transport_data.csv, which contains columns: Temperature_K, Seebeck_uV_per_K, Resistivity_Ohm_m, Kappa_total_W_per_mK for the x=0.03 sample. Validate that all necessary columns are present and numeric.
- Evidence: none

### Step 2: Compute Lorenz number from Seebeck coefficient
- Role: process
- Action: For each temperature point, compute the reduced chemical potential η from the Seebeck coefficient S using the single parabolic band (SPB) model. Use the relationship S = (k_B/e) * ( (2*F_1(η)/F_0(η)) - η ), where F_j are Fermi–Dirac integrals, and solve for η numerically. Then compute the temperature-dependent Lorenz number L = (k_B/e)^2 * ( (3*F_2(η)/F_0(η)) - (2*F_1(η)/F_0(η))^2 ).
- Evidence: none

### Step 3: Compute electronic thermal conductivity
- Role: process
- Action: Calculate the electronic thermal conductivity from the Wiedemann–Franz law: κ_e = L(T) * (1/ρ(T)) * T, where T is the absolute temperature, ρ is the electrical resistivity, and L(T) is the Lorenz number obtained in the previous step.
- Evidence: none

### Step 4: Compute and save lattice thermal conductivity
- Role: scored (load-bearing)
- Action: Subtract the electronic thermal conductivity from the total thermal conductivity: κ_L = κ_total - κ_e. Save the result as a CSV file with columns Temperature_K and kappa_L_W_per_mK, one row per measured temperature point.
- Output file: `/app/outputs/kappa_L_vs_T.csv`
- Format: csv
- Contract: columns: Temperature_K (numeric in K), kappa_L_W_per_mK (numeric in W·m⁻¹·K⁻¹)
- Scoring: scored by hidden verifier

### Step 5: Compute and save thermoelectric figure of merit ZT
- Role: scored
- Action: Calculate the dimensionless figure of merit ZT = S² * T / (κ_total * ρ) at each temperature, using the Seebeck coefficient S, temperature T, total thermal conductivity κ_total, and electrical resistivity ρ. Save the results as a CSV file with columns Temperature_K and ZT.
- Output file: `/app/outputs/ZT_vs_T.csv`
- Format: csv
- Contract: columns: Temperature_K (numeric in K), ZT (numeric, dimensionless)
- Scoring: scored by hidden verifier

### Step 6: Extract maximum ZT and temperature
- Role: scored
- Action: From the computed ZT(T) array, find the maximum ZT value and note the temperature at which it occurs. Write the maximum ZT value as a single floating-point number (e.g., 1.13) to a text file.
- Output file: `/app/outputs/max_ZT.txt`
- Format: txt
- Contract: single float representing the maximum ZT value
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/kappa_L_vs_T.csv`
- `/app/outputs/ZT_vs_T.csv`
- `/app/outputs/max_ZT.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### kappa_L_vs_T.csv
- path: `/app/outputs/kappa_L_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed lattice thermal conductivity as a function of temperature for the x=0.03 sample. The curve will be compared against a gold curve digitized from the paper using a relative tolerance of 10% and an absolute tolerance of 0.1 W·m⁻¹·K⁻¹. The presence, shape, and monotonic behavior are also checked.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `kappa_L_W_per_mK`
  - `units`:
    - `Temperature_K`: K
    - `kappa_L_W_per_mK`: W·m⁻¹·K⁻¹

### ZT_vs_T.csv
- path: `/app/outputs/ZT_vs_T.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed thermoelectric figure of merit ZT as a function of temperature for the x=0.03 sample. The curve will be compared against a gold curve digitized from the paper using a relative tolerance of 10%. The temperature range should span at least 300–400 K.
- schema:
  - `type`: table
  - `required_columns`: `Temperature_K`, `ZT`
  - `units`:
    - `Temperature_K`: K
    - `ZT`: dimensionless

### max_ZT.txt
- path: `/app/outputs/max_ZT.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The maximum ZT value extracted from the computed ZT(T) curve. The value is compared to the paper's reported maximum ZT of 1.13 with an allowed margin of ±0.1; the temperature at which it occurs should be near 350 K (within ±10 K).
- schema:
  - `type`: text
  - `shape`: single float

Notes: All outputs are derived from the same provided input dataset. The agent must follow the full workflow (loading data, computing L(T), κ_e, κ_L, ZT, and extracting the maximum) to produce these artifacts. The qualitative attribution of phonon scattering mechanisms is not scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "kappa_L_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "kappa_L_W_per_mK"
        ],
        "units": {
          "Temperature_K": "K",
          "kappa_L_W_per_mK": "W·m⁻¹·K⁻¹"
        }
      },
      "description": "Computed lattice thermal conductivity as a function of temperature for the x=0.03 sample. The curve will be compared against a gold curve digitized from the paper using a relative tolerance of 10% and an absolute tolerance of 0.1 W·m⁻¹·K⁻¹. The presence, shape, and monotonic behavior are also checked."
    },
    {
      "file": "ZT_vs_T.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Temperature_K",
          "ZT"
        ],
        "units": {
          "Temperature_K": "K",
          "ZT": "dimensionless"
        }
      },
      "description": "Computed thermoelectric figure of merit ZT as a function of temperature for the x=0.03 sample. The curve will be compared against a gold curve digitized from the paper using a relative tolerance of 10%. The temperature range should span at least 300–400 K."
    },
    {
      "file": "max_ZT.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "shape": "single float"
      },
      "description": "The maximum ZT value extracted from the computed ZT(T) curve. The value is compared to the paper's reported maximum ZT of 1.13 with an allowed margin of ±0.1; the temperature at which it occurs should be near 350 K (within ±10 K)."
    }
  ],
  "notes": "All outputs are derived from the same provided input dataset. The agent must follow the full workflow (loading data, computing L(T), κ_e, κ_L, ZT, and extracting the maximum) to produce these artifacts. The qualitative attribution of phonon scattering mechanisms is not scored."
}
```

## How you are scored
Your outputs are evaluated by an automated, hidden verifier that compares your submitted artifacts against expected curves and a target value, all derived from the same underlying experimental data but not visible to you. The scoring works as follows:
- For `kappa_L_vs_T.csv` and `ZT_vs_T.csv`, the verifier checks that the files contain the required columns and cover a sufficient temperature range, then compares your computed κ_L and ZT at each temperature to a hidden gold curve using relative and absolute tolerances. The shape (e.g., κ_L should monotonically decrease with temperature) is also assessed.
- For `max_ZT.txt`, the verifier reads the single number and compares it to the hidden target maximum ZT value with an allowed deviation; the approximate temperature at which it occurs is also checked against an expected range.
All evaluation criteria are pre-defined and do not depend on network access. The final reward is a weighted combination of the scores for each artifact. Meeting the tolerances yields full credit; performance degrades only as your results deviate further from the expected curves and value.
