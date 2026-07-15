# Monte Carlo Electron Transport Simulation for Backscattering, Transmission, and Energy Deposition

## Problem background
Electron transport in matter is central to radiation detector design and dosimetry. Simulating every individual interaction is prohibitive at MeV energies, so many codes adopt the continuous slowing down approximation (CSDA). In the CSDA, an electron's energy loss along its trajectory is treated deterministically via the Bethe stopping power, while only the angular scattering is handled stochastically using a multiple-scattering theory. This task investigates the accuracy of such a CSDA transport model for backscattering, transmission, and energy deposition in several elements over a range of incident energies and foil thicknesses. You will implement the model, run simulations, and extract quantitative coefficients that characterise the transport.

## Approach
You will build a Monte Carlo electron transport code from first principles. The core physics consists of:
- Discretizing the electron's energy loss using the Bethe formula (with relativistic, density, shell, and radiative corrections) to establish a one-to-one mapping between energy and path length.
- Dividing the continuous slowing down into a set of energy steps {E_n} according to the scaling law E_n = E_{n-1} / 2^{1/16} and computing the corresponding path-length steps d_n.
- For each energy step, precomputing the cumulative Molière multiple-scattering distribution (extended to all angles via the Bethe correction) to describe the probability of polar deflection θ.
- During transport, sampling an azimuthal scattering angle uniformly and a polar angle from the precomputed distribution, advancing the electron position using the path-length correction factor (1+cosθ)/2.
Material-specific tables of {E_n, d_n, F_n^i} are built for graphite (Z=6), aluminium (Z=13), silver (Z=47), and lead (Z=82). These tables are reused for all simulations.
The transport simulation tallies backscattered and transmitted electrons and deposits energy in depth bins. Simulation conditions cover perpendicular incidence on plane-parallel foils of various thicknesses (including semi-infinite) and incident energies of 0.25 MeV and 1 MeV. The required outputs capture the backscattering coefficient, transmission coefficient, and normalized energy deposition profile.

## Reproduction target
Your goal is to produce three scored CSV files:
1. **Backscattering coefficients** for four elements at 1 MeV on semi-infinite foils, and for aluminium at 0.25 MeV for foil thicknesses ranging from 0.1 to 1.0 times the total electron path length s₀ (step 0.1).
2. **Transmission coefficients** for aluminium at 0.25 MeV for the same thickness grid.
3. **Energy deposition profile** for aluminium at 1 MeV in a semi-infinite foil, normalized to a maximum of 100, sampled at regular depth intervals from 0 up to approximately 0.6 s₀.
Each file must follow the column specifications given in the workflow steps, and the values must be computed by the Monte Carlo simulation described above.

## Assets

- Python scientific libraries: numpy, scipy, matplotlib

## Workflow steps

### Step 1: Precompute material energy grid and scattering distributions
- Role: process
- Action: Precompute material-specific lookup tables of energy steps E_n, path-length steps d_n, and cumulative Molière multiple-scattering probability distributions F_n^i for graphite, aluminium, silver, and lead using the Bethe stopping power formula and the scaling law E_n = E_{n-1} / 2^{1/16}.
- Evidence: `/app/outputs/precomputed_tables.log`

### Step 2: Monte Carlo electron transport simulations
- Role: process
- Action: Using the precomputed tables, run Monte Carlo transport simulations for: (a) backscattering coefficient for semi-infinite foils at 1 MeV incident energy for graphite, aluminium, silver, and lead (6000 histories each); (b) backscattering coefficient vs. foil thickness for aluminium at 0.25 MeV, thickness multiples of total electron path length s0 from 0.1 to 1.0 in steps of 0.1 (6000 histories per thickness); (c) transmission coefficient vs. foil thickness for aluminium at 0.25 MeV, same thickness grid (6000 histories per thickness); (d) energy deposition profile for aluminium at 1 MeV in a semi-infinite foil (4500 histories). Record all tallied coefficients and the energy deposition histogram as a function of depth in s0 units.
- Evidence: `/app/outputs/simulation_raw.json`

### Step 3: Extract backscattering coefficients
- Role: scored (load-bearing)
- Action: Read the raw simulation tallies from simulation_raw.json, extract the backscattering coefficient for graphite, Al, Ag, Pb at 1 MeV semi-infinite, and for Al at 0.25 MeV at each thickness, and write them to a CSV file.
- Output file: `/app/outputs/backscattering_coefficients.csv`
- Format: csv
- Contract: Columns: material (str), foil_thickness_in_s0_or_inf (float or 'inf'), incident_energy_MeV (float), backscattering_coefficient (float).
- Scoring: scored by hidden verifier

### Step 4: Extract transmission coefficients
- Role: scored
- Action: Read simulation_raw.json, extract the transmission coefficient for aluminium at 0.25 MeV for each thickness, and write them to a CSV file.
- Output file: `/app/outputs/transmission_coefficients.csv`
- Format: csv
- Contract: Columns: material (str), foil_thickness_in_s0_units (float), incident_energy_MeV (float), transmission_coefficient (float).
- Scoring: scored by hidden verifier

### Step 5: Extract energy deposition profile
- Role: scored
- Action: Read simulation_raw.json, obtain the energy deposition histogram for aluminium at 1 MeV, normalize the maximum to 100, and write the depth-dependent profile to a CSV file.
- Output file: `/app/outputs/energy_deposition_al_1MeV.csv`
- Format: csv
- Contract: Columns: depth_in_s0_units (float), energy_deposition_normalized (float). Depth sampling from 0.0 to approximately 0.6 s0 at regular intervals.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/backscattering_coefficients.csv`
- `/app/outputs/transmission_coefficients.csv`
- `/app/outputs/energy_deposition_al_1MeV.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### backscattering_coefficients.csv
- path: `/app/outputs/backscattering_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Backscattering coefficient (albedo) for the specified materials, energies, and foil thicknesses.
- schema:
  - `type`: table
  - `required_columns`: `material`, `foil_thickness_in_s0_or_inf`, `incident_energy_MeV`, `backscattering_coefficient`
  - `units`:
    - `incident_energy_MeV`: MeV
    - `foil_thickness_in_s0_or_inf`: multiple of total electron path length s0, or string 'inf'
    - `backscattering_coefficient`: dimensionless

### transmission_coefficients.csv
- path: `/app/outputs/transmission_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Transmission coefficient for aluminium at 0.25 MeV as a function of foil thickness.
- schema:
  - `type`: table
  - `required_columns`: `material`, `foil_thickness_in_s0_units`, `incident_energy_MeV`, `transmission_coefficient`
  - `units`:
    - `incident_energy_MeV`: MeV
    - `foil_thickness_in_s0_units`: multiple of total electron path length s0
    - `transmission_coefficient`: dimensionless

### energy_deposition_al_1MeV.csv
- path: `/app/outputs/energy_deposition_al_1MeV.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Normalized energy deposition profile for aluminium at 1 MeV, depth in s0 units.
- schema:
  - `type`: table
  - `required_columns`: `depth_in_s0_units`, `energy_deposition_normalized`
  - `units`:
    - `depth_in_s0_units`: multiple of total electron path length s0
    - `energy_deposition_normalized`: arbitrary units (max = 100)

Notes: All scored quantities are compared to hidden gold values from the paper with tolerances. The checker uses threshold_or_better scoring: results within tolerance receive full credit; larger deviations receive reduced credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "backscattering_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "foil_thickness_in_s0_or_inf",
          "incident_energy_MeV",
          "backscattering_coefficient"
        ],
        "units": {
          "incident_energy_MeV": "MeV",
          "foil_thickness_in_s0_or_inf": "multiple of total electron path length s0, or string 'inf'",
          "backscattering_coefficient": "dimensionless"
        }
      },
      "description": "Backscattering coefficient (albedo) for the specified materials, energies, and foil thicknesses."
    },
    {
      "file": "transmission_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "foil_thickness_in_s0_units",
          "incident_energy_MeV",
          "transmission_coefficient"
        ],
        "units": {
          "incident_energy_MeV": "MeV",
          "foil_thickness_in_s0_units": "multiple of total electron path length s0",
          "transmission_coefficient": "dimensionless"
        }
      },
      "description": "Transmission coefficient for aluminium at 0.25 MeV as a function of foil thickness."
    },
    {
      "file": "energy_deposition_al_1MeV.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "depth_in_s0_units",
          "energy_deposition_normalized"
        ],
        "units": {
          "depth_in_s0_units": "multiple of total electron path length s0",
          "energy_deposition_normalized": "arbitrary units (max = 100)"
        }
      },
      "description": "Normalized energy deposition profile for aluminium at 1 MeV, depth in s0 units."
    }
  ],
  "notes": "All scored quantities are compared to hidden gold values from the paper with tolerances. The checker uses threshold_or_better scoring: results within tolerance receive full credit; larger deviations receive reduced credit."
}
```

## How you are scored
A hidden verifier will independently inspect the three CSV files you produce. For each artifact it will compare your computed quantities against reference values using a tolerance designed to accept a correct re‑implementation while rejecting results that did not faithfully run the required simulation. The verifier will combine scores from the three artifacts into a single total reward, with each artifact contributing a pre‑defined weight. Reporting numbers that match the paper's published values without executing the transport code is not sufficient; the checker may also examine internal consistency or request additional intermediate evidence. Only results that originate from a correctly executed simulation, as reflected by agreement within the tolerance, will earn full credit.
