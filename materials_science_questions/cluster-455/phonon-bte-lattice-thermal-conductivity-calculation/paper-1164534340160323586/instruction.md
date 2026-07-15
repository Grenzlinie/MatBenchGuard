# Phonon transport and ITC of GaN/SiC heterostructures with point defects from first-principles Monte Carlo

## Problem background
High-power-density semiconductor devices, such as GaN transistors on SiC substrates, face severe thermal challenges because the interface between dissimilar materials creates significant thermal resistance. Understanding and controlling interfacial thermal conductance (ITC) is critical for effective heat dissipation. During fabrication, point defects are inevitably introduced near the interface, but their effect on interfacial heat transport is not well understood and may not simply degrade performance. This task investigates how the type and concentration of point defects influence the ITC of a GaN/SiC heterostructure. You will compute the ITC for a defect-free interface and for interfaces with varying concentrations of vacancy defects placed either within the GaN or within the SiC, and determine the resulting ITC trends.

## Approach
You will follow a microscale thermal transport model that combines first-principles phonon properties with a Monte Carlo solution of the phonon Boltzmann transport equation. The workflow is: (1) Compute harmonic and anharmonic force constants for GaN and SiC using density functional theory (DFT). (2) From the force constants, extract phonon dispersions, group velocities, and intrinsic three-phonon scattering rates. (3) For each defect scenario (defect location and concentration), add the point-defect scattering rate via the Klemens mass-difference model to obtain total phonon relaxation times using Matthiessen's rule. (4) Run a variance-reduced Monte Carlo simulation of the deviational BTE for a GaN/SiC heterostructure, applying the computed scattering rates, an interface transmission rule, and isothermal top/bottom boundaries. (5) From the steady-state results, compute the ITC as the ratio of heat flux to temperature drop at the interface. The bulk lattice thermal conductivity of GaN and SiC at 300 K is also computed as a validation of the obtained phonon properties.

## Reproduction target
Compute the lattice thermal conductivity of bulk GaN and SiC at 300 K. Then simulate the GaN/SiC heterostructure and compute the interfacial thermal conductance (ITC) for the following configurations: a defect-free interface; and interfaces where point defects are introduced at relative concentrations of 1e-8, 1e-6, 1e-4, 0.01, 0.03, and 0.05, placed exclusively either within the GaN side or within the SiC side. Report ITC for each configuration. The objective is to determine how ITC depends on defect concentration and location (GaN vs. SiC).

## Assets

- Crystal structures of GaN (wurtzite) and 4H-SiC: https://materialsproject.org/
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Thirdorder: https://github.com/lingyuanchen/thirdorder
- almaBTE: https://github.com/jcarrete/almaBTE
- MCBTE variance-reduced Monte Carlo solver: https://github.com/abhishekpathak19/mcbte

## Workflow steps

### Step 1: DFT force constant calculation
- Role: process
- Action: Compute second- and third-order force constants for GaN (wurtzite) and 4H-SiC using density functional theory (e.g., Quantum ESPRESSO) with the LDA functional and a plane-wave basis, extracting harmonic and anharmonic force constants via Phonopy and Thirdorder. Use converged supercell sizes and interaction range consistent with the method.
- Evidence: `/app/outputs/force_constants.log`

### Step 2: Phonon property calculation
- Role: process
- Action: Using almaBTE and the force constants from step_01, compute phonon dispersions, group velocities, and three-phonon relaxation times for GaN and SiC at 300 K. Use a dense q-point mesh and the RTA solver to obtain the spectral inputs for later steps.
- Evidence: `/app/outputs/phonon_properties.hdf5`

### Step 3: Bulk lattice thermal conductivity validation
- Role: scored
- Action: From the phonon properties of step_02, compute the lattice thermal conductivity of bulk GaN and SiC at 300 K using almaBTE's RTA solver. Save the results as a JSON object with keys 'GaN' and 'SiC' (values in W/mK).
- Output file: `/app/outputs/bulk_thermal_conductivity.json`
- Format: json
- Contract: {"type": "object", "required": ["GaN", "SiC"], "properties": {"GaN": {"type": "number", "unit": "W/mK"}, "SiC": {"type": "number", "unit": "W/mK"}}}
- Scoring: scored by hidden verifier

### Step 4: Defect scattering rates
- Role: process
- Action: For each defect location (defects in GaN only, defects in SiC only) and for each target relative defect concentration (1e-8, 1e-6, 1e-4, 0.01, 0.03, 0.05), compute the point-defect scattering relaxation time using the mass-difference model (Klemens formula) with vacancy parameters, and combine it with the three-phonon relaxation times from step_02 via Matthiessen's rule to obtain the total spectral scattering rate.
- Evidence: `/app/outputs/defect_rates.hdf5`

### Step 5: Monte Carlo simulation of GaN/SiC heterostructure
- Role: process
- Action: For the defect-free case and each defect configuration from step_04, run the variance-reduced Monte Carlo solver to simulate phonon transport in a GaN/SiC heterostructure. Use the simulation domain dimensions and boundary conditions consistent with the model: fixed-temperature boundaries at top (303 K) and bottom (297 K), periodic lateral boundaries, equilibrium temperature 300 K, and spectral interface transmission rule. Record steady-state heat flux and temperature drop at the interface.
- Evidence: `/app/outputs/mc_simulation_output.hdf5`

### Step 6: Extract interfacial thermal conductance (ITC)
- Role: scored (load-bearing)
- Action: From the simulation outputs of step_05, compute the interfacial thermal conductance ITC = Q / ΔT for each defect configuration (defect-free and each concentration in GaN and in SiC). Save the results as a CSV file with columns: defect_concentration (float), defect_location (string: 'GaN', 'SiC', or 'none'), heat_flux (float, W/m²), temperature_drop (float, K), itc (float, W/m²K). Include rows for defect-free (concentration 0, location 'none') and for all simulated defect concentrations in both locations.
- Output file: `/app/outputs/itc_vs_defect_concentration.csv`
- Format: csv
- Contract: {"type": "table", "required_columns": ["defect_concentration", "defect_location", "heat_flux", "temperature_drop", "itc"], "columns": {"defect_concentration": "float (dimensionless relative concentration)", "defect_location": "string: 'GaN', 'SiC', or 'none'", "heat_flux": "float (W/m²)", "temperature_drop": "float (K)", "itc": "float (W/m²K)"}}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_thermal_conductivity.json`
- `/app/outputs/itc_vs_defect_concentration.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_thermal_conductivity.json
- path: `/app/outputs/bulk_thermal_conductivity.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed lattice thermal conductivity of GaN and SiC at 300 K for phonon property validation.
- schema:
  - `type`: object
  - `required`: `GaN`, `SiC`
  - `properties`:
    - `GaN`:
      - `type`: number
      - `unit`: W/mK
    - `SiC`:
      - `type`: number
      - `unit`: W/mK

### itc_vs_defect_concentration.csv
- path: `/app/outputs/itc_vs_defect_concentration.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file containing simulated interfacial thermal conductance (ITC) values for different defect configurations. Columns: defect_concentration (float), defect_location (string: 'GaN', 'SiC', 'none'), heat_flux (float, W/m²), temperature_drop (float, K), itc (float, W/m²K).
- schema:
  - `type`: table
  - `required_columns`: `defect_concentration`, `defect_location`, `heat_flux`, `temperature_drop`, `itc`
  - `columns`:
    - `defect_concentration`: float, dimensionless relative concentration
    - `defect_location`: string: 'GaN', 'SiC', or 'none'
    - `heat_flux`: float, W/m²
    - `temperature_drop`: float, K
    - `itc`: float, W/m²K

Notes: The hidden checker will compare the reported bulk thermal conductivity against reference values with tolerance, and for the ITC CSV it will verify the itc = heat_flux / temperature_drop consistency, the monotonic trend (decreasing for GaN defects, increasing for SiC defects), and the percent change at concentration 0.05 compared to the defect-free case.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_thermal_conductivity.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "GaN",
          "SiC"
        ],
        "properties": {
          "GaN": {
            "type": "number",
            "unit": "W/mK"
          },
          "SiC": {
            "type": "number",
            "unit": "W/mK"
          }
        }
      },
      "description": "Computed lattice thermal conductivity of GaN and SiC at 300 K for phonon property validation."
    },
    {
      "file": "itc_vs_defect_concentration.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_concentration",
          "defect_location",
          "heat_flux",
          "temperature_drop",
          "itc"
        ],
        "columns": {
          "defect_concentration": "float, dimensionless relative concentration",
          "defect_location": "string: 'GaN', 'SiC', or 'none'",
          "heat_flux": "float, W/m²",
          "temperature_drop": "float, K",
          "itc": "float, W/m²K"
        }
      },
      "description": "CSV file containing simulated interfacial thermal conductance (ITC) values for different defect configurations. Columns: defect_concentration (float), defect_location (string: 'GaN', 'SiC', 'none'), heat_flux (float, W/m²), temperature_drop (float, K), itc (float, W/m²K)."
    }
  ],
  "notes": "The hidden checker will compare the reported bulk thermal conductivity against reference values with tolerance, and for the ITC CSV it will verify the itc = heat_flux / temperature_drop consistency, the monotonic trend (decreasing for GaN defects, increasing for SiC defects), and the percent change at concentration 0.05 compared to the defect-free case."
}
```

## How you are scored
A hidden verifier will independently assess your submitted artifacts. It will check the bulk_thermal_conductivity.json against reference values for GaN and SiC. For the itc_vs_defect_concentration.csv file, it will verify that the reported ITC equals heat_flux / temperature_drop and then evaluate the overall trend of ITC vs. defect concentration for each defect location, including the magnitude of the relative change at the highest concentration relative to the defect-free case. The final reward is a weighted combination of these checks (bulk conductivity carries lower weight than the ITC trend). The verifier does not merely confirm that numbers match a specific value; it uses the expected physical trend and structural self-consistency to assign credit.
