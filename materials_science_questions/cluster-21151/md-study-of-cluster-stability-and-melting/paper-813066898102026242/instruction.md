# Glass-to-liquid transition in 2D monatomic Lennard-Jones-Gauss system

## Problem background
The melting of a two-dimensional (2D) glassy monatomic system differs from the melting of 2D crystals and is characterized by a broad transition region. This problem investigates the thermodynamic signature of the glass-to-liquid transition during heating, using molecular dynamics (MD) simulations with a Lennard-Jones-Gauss (LJG) interaction potential. The objective is to determine how the potential energy per atom and the heat capacity per atom evolve with temperature as the system is heated from the glassy state, and to identify the glass transition temperature \(T_g\) from the peak in the heat capacity. Additionally, the temperature interval over which the potential energy curve departs from linearity must be measured.

## Approach
A 2D monatomic system of 6400 particles interacting via the LJG potential (parameters from Mizuguchi and Odagaki, 2009) is studied at a fixed density. A glassy state is prepared by equilibrating the system at a high temperature and then cooling it linearly at a controlled rate. The resulting glass is then heated back to the liquid state at two different heating rates; during these heating runs, the potential energy is recorded after a short relaxation at each temperature. From the heating trajectories, the heat capacity per atom is computed numerically as \(\Delta E/\Delta T\), and the glass transition temperature \(T_g\) is extracted as the temperature at which the heat capacity peaks. The transition temperature window is identified as the region where the potential energy clearly deviates from a linear trend. The thermodynamic curves and the derived \(T_g\) values are the quantities that must be reproduced by running the full MD protocol with an open-source MD engine (e.g., LAMMPS) and the published potential parameters.

## Reproduction target
Using the LJG potential parameters from Mizuguchi and Odagaki (2009) and an MD simulation engine, set up the 2D system, prepare a glass via cooling, and perform heating at the two specified rates. From the recorded potential energy data, produce a cleaned CSV file (`potential_energy.csv`) containing the temperature, heating rate, and potential energy per atom for all temperature points. From this file, compute the heat capacity per atom as \(\Delta E/\Delta T\) and store it in `heat_capacity.csv` with columns for temperature, heating rate, and heat capacity per atom. Finally, identify the peak positions in the heat capacity curves to obtain the glass transition temperatures for each heating rate, note the transition temperature interval where the potential energy departs from linearity, and write the results to `results.json` with the keys specified in the workflow steps. The deliverables are the three scored files with the exact schemas defined in the steps.

## Assets

- LJG potential parameters from Mizuguchi and Odagaki (2009): 10.1103/PhysRevE.79.051501
- Molecular dynamics simulation engine: https://lammps.org

## Workflow steps

### Step 1: Prepare glass and run heating simulations
- Role: process
- Action: Set up a 2D periodic system of 6400 particles interacting via the LJG potential (parameters from Mizuguchi & Odagaki 2009) at density 1.0. Equilibrate at T=2.5 for 2×10^6 MD steps (dt=0.001 LJ time units), cool linearly to T=0.1 at rate γ=1e-6 per MD step via velocity rescaling, then heat the glass to T=2.5 at two rates (γ=1e-6 and 1e-5 per MD step). For each heating run, record potential energy per atom after a 5000-step relaxation at each temperature. Save the raw potential energy vs. temperature data for both heating rates.
- Evidence: `/app/outputs/potential_raw.csv`

### Step 2: Format potential energy data
- Role: scored (load-bearing)
- Action: From the raw potential energy data, produce a clean CSV with columns: temperature, heating_rate, potential_energy_per_atom. Include all temperature points for both heating rates (γ=1e-6 and 1e-5).
- Output file: `/app/outputs/potential_energy.csv`
- Format: csv
- Contract: CSV with columns: temperature (float, LJ reduced units), heating_rate (float, e.g. 1e-6 or 1e-5), potential_energy_per_atom (float, LJ reduced units).
- Scoring: scored by hidden verifier

### Step 3: Compute heat capacity
- Role: scored
- Action: From potential_energy.csv, compute the heat capacity per atom as Cp = ΔE/ΔT between consecutive temperature points for each heating rate. Output a CSV with columns: temperature, heating_rate, heat_capacity_per_atom.
- Output file: `/app/outputs/heat_capacity.csv`
- Format: csv
- Contract: CSV with columns: temperature (float, LJ reduced units), heating_rate (float), heat_capacity_per_atom (float, LJ reduced units).
- Scoring: scored by hidden verifier

### Step 4: Extract transition temperatures and report
- Role: scored
- Action: Identify the peak of the heat capacity curve for each heating rate and record the corresponding temperature as Tg. Also note the transition region bounds (0.2 and 0.8) consistent with the observed nonlinearity in the potential energy curve. Output a JSON file with keys Tg_1e_minus_6, Tg_1e_minus_5, transition_region_low, transition_region_high.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: Tg_1e_minus_6 (float), Tg_1e_minus_5 (float), transition_region_low (float, expected 0.2), transition_region_high (float, expected 0.8).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/potential_energy.csv`
- `/app/outputs/heat_capacity.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### potential_energy.csv
- path: `/app/outputs/potential_energy.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Potential energy per atom vs. temperature for both heating rates. The checker will verify that the curve deviates from linearity in the interval 0.2 < T < 0.8.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `heating_rate`, `potential_energy_per_atom`
  - `columns`:
    - `temperature`: float (LJ reduced units)
    - `heating_rate`: float (e.g. 1e-6 or 1e-5)
    - `potential_energy_per_atom`: float (LJ reduced units)

### heat_capacity.csv
- path: `/app/outputs/heat_capacity.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Heat capacity per atom computed from potential energy differences. The checker will recompute the peak position for each heating rate.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `heating_rate`, `heat_capacity_per_atom`
  - `columns`:
    - `temperature`: float (LJ reduced units)
    - `heating_rate`: float
    - `heat_capacity_per_atom`: float (LJ reduced units)

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Agent-reported glass transition temperatures (Tg) for each heating rate and the transition region bounds. The checker will compare Tg values to the paper-reported reference within a tolerance, and verify consistency with the heat capacity data.
- schema:
  - `type`: object
  - `required`: `Tg_1e_minus_6`, `Tg_1e_minus_5`, `transition_region_low`, `transition_region_high`
  - `properties`:
    - `Tg_1e_minus_6`:
      - `type`: number
    - `Tg_1e_minus_5`:
      - `type`: number
    - `transition_region_low`:
      - `type`: number
      - `const`: 0.2
    - `transition_region_high`:
      - `type`: number
      - `const`: 0.8

Notes: The potential energy curve is checked for nonlinearity in the transition region. The heat capacity peak temperatures (Tg) are compared to reference values. The transition region bounds are structural constants derived from the paper's definition and are not expected to vary.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "potential_energy.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "heating_rate",
          "potential_energy_per_atom"
        ],
        "columns": {
          "temperature": "float (LJ reduced units)",
          "heating_rate": "float (e.g. 1e-6 or 1e-5)",
          "potential_energy_per_atom": "float (LJ reduced units)"
        }
      },
      "description": "Potential energy per atom vs. temperature for both heating rates. The checker will verify that the curve deviates from linearity in the interval 0.2 < T < 0.8."
    },
    {
      "file": "heat_capacity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "heating_rate",
          "heat_capacity_per_atom"
        ],
        "columns": {
          "temperature": "float (LJ reduced units)",
          "heating_rate": "float",
          "heat_capacity_per_atom": "float (LJ reduced units)"
        }
      },
      "description": "Heat capacity per atom computed from potential energy differences. The checker will recompute the peak position for each heating rate."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "Tg_1e_minus_6",
          "Tg_1e_minus_5",
          "transition_region_low",
          "transition_region_high"
        ],
        "properties": {
          "Tg_1e_minus_6": {
            "type": "number"
          },
          "Tg_1e_minus_5": {
            "type": "number"
          },
          "transition_region_low": {
            "type": "number",
            "const": 0.2
          },
          "transition_region_high": {
            "type": "number",
            "const": 0.8
          }
        }
      },
      "description": "Agent-reported glass transition temperatures (Tg) for each heating rate and the transition region bounds. The checker will compare Tg values to the paper-reported reference within a tolerance, and verify consistency with the heat capacity data."
    }
  ],
  "notes": "The potential energy curve is checked for nonlinearity in the transition region. The heat capacity peak temperatures (Tg) are compared to reference values. The transition region bounds are structural constants derived from the paper's definition and are not expected to vary."
}
```

## How you are scored
A hidden verifier evaluates each of the scored artifacts independently and then combines the rewards by weight. The verifier will check that the potential energy curve in `potential_energy.csv` deviates from linearity in the expected temperature interval, recompute the heat capacity peak positions from `heat_capacity.csv`, and verify that the reported \(T_g\) values in `results.json` are consistent with the heat capacity data and fall within an acceptable tolerance of hidden reference values. The transition region bounds will also be checked for consistency with the potential energy data. Each stage is assigned a weight, and the final score is the weighted sum of the stage rewards. Merely reporting the paper's numbers without producing the underlying simulation data and the derived artifacts will not earn credit.
