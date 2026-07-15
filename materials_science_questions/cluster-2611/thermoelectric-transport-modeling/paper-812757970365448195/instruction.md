# Thermoelectric Transport Modeling

## Problem background
ZnO nanowires are promising thermoelectric materials for converting waste heat into electricity. Recent studies have shown that under tensile loading, ZnO nanowires can transform from the regular wurtzite (W) phase to a graphitic hexagonal (H) phase. This phase transformation is predicted to alter the electronic band structure, effective mass, and thermal transport properties. Understanding how the phase change affects the key thermoelectric quantities—electrical conductivity, Seebeck coefficient, power factor, and the figure of merit ZT—is essential for designing high-efficiency ZnO-based thermoelectrics.

## Approach
The reproduction uses a combination of first-principles density-functional theory (DFT) and one-dimensional (1D) Boltzmann transport theory. First, atomic models of a ZnO nanowire (wire D) are built in both the wurtzite and hexagonal phases, and their geometries are optimized. Electronic band structures are computed along the wire axis. From the lowest conduction band, the electron effective mass is extracted. The relaxation time for electron transport is calibrated to a published experimental conductivity measurement for ZnO nanowires, and a carrier-concentration-dependent relaxation time function is derived using an empirical mobility–concentration relation for ZnO thin films. Using the rigid-band approximation, the 1D Boltzmann transport equations are solved to obtain the electrical conductivity, Seebeck coefficient, electronic thermal conductivity, power factor, and figure of merit ZT as functions of carrier concentration and temperature. Fixed phonon thermal conductivity values from the literature are used. The outputs are generated for both the H and W phases so their trends can be compared.

## Reproduction target
Produce two CSV files:

1. At T = 300 K, a sweep of electrical conductivity, Seebeck coefficient, power factor, and ZT for wire D in both the wurtzite (W) and hexagonal (H) phases as functions of electron carrier concentration n from 10^17 to 10^20 cm^-3.
2. At the doping levels that give the highest room-temperature ZT for each phase (n_H = 6.5×10^18 cm^-3, n_W = 7.1×10^18 cm^-3), produce ZT values and the ratio ZT_H / ZT_W at temperatures from 200 K to 1000 K (step 100 K).

The target is to demonstrate the relative trends between the two phases and the concentration/temperature dependence, not to match any specific published numerical values.

## Assets

- Bulk ZnO wurtzite crystal structure
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Noriega et al. (2010) experimental conductivity data: 10.1063/1.3357310
- Ellmer & Mietus (2008) mobility–concentration relation: 10.1016/j.tsf.2007.06.139
- Kulkarni & Zhou (2007) phonon thermal conductivity: 10.1088/0957-4484/18/43/435706

## Workflow steps

### Step 1: Construct nanowire atomic models
- Role: process
- Action: Generate atomic coordinates for ZnO nanowire D in both wurtzite (W) and hexagonal (H) phases using the specified diameters and supercell lengths (H phase: D = 1.754 nm, L = 0.820 nm; W phase: D = 1.400 nm, L = 1.060 nm). The wire is oriented along [0001] with hexagonal cross-section enclosed by (10-10) facets, and Zn surface atoms passivated with hydrogen.
- Evidence: `/app/outputs/nanowire_structures.json`

### Step 2: DFT geometry optimization and band structure
- Role: process
- Action: Perform DFT geometry optimization and electronic band structure calculation for both W and H nanowire models using an open-source DFT package (e.g., Quantum ESPRESSO) with PBE-GGA functional. Compute band energies along the wire axis on a 1×1×16 k-point grid.
- Evidence: `/app/outputs/dft_calculation_summary.json`

### Step 3: Extract electron effective mass
- Role: process
- Action: From the lowest conduction band of each phase, compute the electron effective mass m* along the wire axis using the curvature at the Γ point: m* = ħ² (∂²E/∂k_z²)⁻¹.
- Evidence: `/app/outputs/effective_mass.json`

### Step 4: Calibrate carrier-concentration-dependent relaxation time
- Role: process
- Action: Fit a baseline relaxation time τ₀ by matching the computed electrical conductivity (using 1D BTE with the DFT density of states and m*) to the experimental data point from Noriega et al. (σ=384.6 (Ω·cm)⁻¹ at n=8.8×10¹⁹ cm⁻³, T=300 K). Then derive a carrier‑concentration‑dependent relaxation time τ(n) using the empirical mobility–concentration relation for ZnO thin films from Ellmer & Mietus (2008).
- Evidence: `/app/outputs/tau_calibration.json`

### Step 5: Compute thermoelectric properties at 300 K vs carrier concentration
- Role: scored (load-bearing)
- Action: Implement the 1D Boltzmann transport equations using the DFT band structure, the calibrated τ(n), and the rigid-band approximation. Compute electrical conductivity σ, Seebeck coefficient S, electronic thermal conductivity κ_e, power factor P = S²σ, and figure of merit ZT (using fixed phonon thermal conductivities κ_ph_W = 8.3 W/m·K, κ_ph_H = 10.1 W/m·K) for wire D in both W and H phases as functions of carrier concentration n (log-spaced range 1×10¹⁷ to 1×10²⁰ cm⁻³) at T = 300 K.
- Output file: `/app/outputs/thermoelectric_properties_wireD_300K.csv`
- Format: csv
- Contract: CSV with columns: carrier_concentration (float, cm^-3), phase (string, 'W' or 'H'), electrical_conductivity (float, S/m), seebeck_coefficient (float, uV/K), power_factor (float, uW/mK^2), ZT (float). At least 15 log-spaced carrier concentration points per phase.
- Scoring: scored by hidden verifier

### Step 6: Compute ZT ratio vs temperature at optimal doping
- Role: scored
- Action: Using the same BTE framework and the optimal carrier concentrations (n_H = 6.5×10¹⁸ cm⁻³, n_W = 7.1×10¹⁸ cm⁻³), compute ZT for both H and W phases at temperatures T = 200, 300, 400, 500, 600, 700, 800, 900, 1000 K. Output the ZT values and the ratio ZT_H / ZT_W.
- Output file: `/app/outputs/ZT_ratio_temperature.csv`
- Format: csv
- Contract: CSV with columns: temperature (float, K), ZT_H (float), ZT_W (float), ratio (float). Rows for temperatures: 200, 300, 400, 500, 600, 700, 800, 900, 1000 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thermoelectric_properties_wireD_300K.csv`
- `/app/outputs/ZT_ratio_temperature.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thermoelectric_properties_wireD_300K.csv
- path: `/app/outputs/thermoelectric_properties_wireD_300K.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Thermoelectric transport properties of ZnO nanowire D at 300 K for a sweep of carrier concentrations, covering both W and H phases.
- schema:
  - `type`: table
  - `required_columns`: `carrier_concentration`, `phase`, `electrical_conductivity`, `seebeck_coefficient`, `power_factor`, `ZT`
  - `units`:
    - `carrier_concentration`: cm^-3
    - `electrical_conductivity`: S/m
    - `seebeck_coefficient`: uV/K
    - `power_factor`: uW/mK^2
    - `ZT`: dimensionless

### ZT_ratio_temperature.csv
- path: `/app/outputs/ZT_ratio_temperature.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: ZT values for H and W phases and their ratio as a function of temperature, at the doping levels that give maximum ZT at room temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `ZT_H`, `ZT_W`, `ratio`
  - `units`:
    - `temperature`: K
    - `ZT_H`: dimensionless
    - `ZT_W`: dimensionless
    - `ratio`: dimensionless

Notes: All scored outputs are evaluated by structural audit (T3): the verifier checks that the output data are physically consistent and obey the expected qualitative behavior for the thermoelectric model. Process steps produce evidence artifacts that must be present but are not directly scored.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thermoelectric_properties_wireD_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "carrier_concentration",
          "phase",
          "electrical_conductivity",
          "seebeck_coefficient",
          "power_factor",
          "ZT"
        ],
        "units": {
          "carrier_concentration": "cm^-3",
          "electrical_conductivity": "S/m",
          "seebeck_coefficient": "uV/K",
          "power_factor": "uW/mK^2",
          "ZT": "dimensionless"
        }
      },
      "description": "Thermoelectric transport properties of ZnO nanowire D at 300 K for a sweep of carrier concentrations, covering both W and H phases."
    },
    {
      "file": "ZT_ratio_temperature.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "ZT_H",
          "ZT_W",
          "ratio"
        ],
        "units": {
          "temperature": "K",
          "ZT_H": "dimensionless",
          "ZT_W": "dimensionless",
          "ratio": "dimensionless"
        }
      },
      "description": "ZT values for H and W phases and their ratio as a function of temperature, at the doping levels that give maximum ZT at room temperature."
    }
  ],
  "notes": "All scored outputs are evaluated by structural audit (T3): the verifier checks that the output data are physically consistent and obey the expected qualitative behavior for the thermoelectric model. Process steps produce evidence artifacts that must be present but are not directly scored."
}
```

## How you are scored
Your submission is evaluated by an automated structural verifier. The verifier reads the two CSV files and checks that the data exhibit physically reasonable trends and internal consistency appropriate for the modeled system. No further details about the exact criteria are provided in the public task description.
