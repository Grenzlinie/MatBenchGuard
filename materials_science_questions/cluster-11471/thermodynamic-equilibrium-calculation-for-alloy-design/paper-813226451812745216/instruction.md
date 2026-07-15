# Bainitic ferrite growth: Gibbs energy balance model velocity prediction

## Problem background
Bainitic ferrite growth in steels is controlled by carbon diffusion and by the interaction of substitutional alloying elements (e.g., Mn, Si) with the moving austenite–ferrite interface. In interrupted cooling experiments, the transformation kinetics can exhibit a so-called stagnant stage — an initial period of extremely slow growth followed by a sharp acceleration. This phenomenon is believed to originate from the competition between the chemical driving force for the phase transformation and the dissipation of Gibbs energy due to solute diffusion inside the interface and interface friction. A Gibbs energy balance approach that equates driving force to dissipation can predict whether and when such a stagnant stage occurs. This task asks you to implement that model and compute the interface velocity as a function of temperature during cooling for two model alloys.

## Approach
Implement a Gibbs energy balance model for the austenite-to-bainitic ferrite transformation. First, use an open-source CALPHAD package (pycalphad) together with a thermodynamic database covering Fe, Mn, C, and Si to evaluate the chemical potentials of all elements in austenite and ferrite as functions of temperature and interfacial composition. The chemical driving force ΔG_chem is computed from the interfacial chemical potentials. The carbon concentration at the interface is linked to the interface velocity v and the fraction transformed f_α via the Zener–Hillert relation. Inside the moving interface, quasi-steady solute diffusion is described by the Cahn-type equation; the associated dissipation ΔG_diff is evaluated from the solute profiles using the Hillert–Sundman integral. An additional dissipation ΔG_friction = v V_m / M accounts for interface friction with an effective mobility M obtained from literature (Wits et al.). For given temperature, alloy composition, and f_α, the admissible velocity v is the one that satisfies ΔG_chem = ΔG_diff + ΔG_friction; this non-linear equation is solved numerically at each temperature. For the Fe-Mn-C alloy only Mn diffusion inside the interface is considered; for the Fe-Mn-Si-C alloy both Mn and Si diffusion are included.

## Reproduction target
Compute the interface velocity v (m/s) as a function of temperature for the following two cases:
- Fe-3Mn-0.1C (wt%) alloy: cooling from 550 °C to 400 °C at 5 °C intervals, with fraction transformed f_α = 0.4.
- Fe-3Mn-0.1C-1.5Si (wt%) alloy: cooling from 530 °C to 400 °C at 5 °C intervals, with fraction transformed f_α = 0.4.
For each alloy, produce a CSV file containing temperature (K) and the corresponding velocity (m/s). The curve should exhibit a qualitative kinetic transition: an initial stage of very low velocity followed by a sharp increase.

## Assets

- pycalphad (Python CALPHAD library): pycalphad
- Open-source thermodynamic database for Fe-Mn-Si-C system

## Workflow steps

### Step 1: Set up thermodynamic and kinetic model for the Gibbs energy balance
- Role: process
- Action: Define the two alloy compositions (Fe-3Mn-0.1C and Fe-3Mn-0.1C-1.5Si in wt%). Load a suitable Fe-Mn-C-Si CALPHAD database using pycalphad. Implement functions to compute chemical potentials μ_i in austenite and ferrite as functions of interfacial composition and temperature. Implement the Zener-Hilleret relation to link carbon interface composition to velocity and fraction transformed. Set up physical parameters: interface half-width δ=0.25 nm, Mn binding energy 9.9 kJ/mol, Si binding energy 12.3 kJ/mol, literature diffusion coefficients for Mn and Si in austenite and interface, and an effective interface mobility from Wits et al. Implement solvers for the Cahn-type quasi-steady solute diffusion inside a moving interface and the Hillert-Sundman dissipation integral. Log the setup success as thermo_setup.log.
- Evidence: `/app/outputs/thermo_setup.log`

### Step 2: Compute interface velocity vs temperature for Fe-Mn-C alloy
- Role: scored (load-bearing)
- Action: For the Fe-3Mn-0.1C alloy, solve the energy balance equation ΔG_chem = ΔG_diff + ΔG_friction over the cooling temperature range from 550°C to 400°C at 5°C intervals, using a fixed fraction transformed f_α = 0.4 and including only Mn diffusion inside the interface. At each temperature, find the interface velocity v that satisfies the balance. Write the resulting data to step_01_FeMnC_velocity.csv.
- Output file: `/app/outputs/step_01_FeMnC_velocity.csv`
- Format: csv
- Contract: Two columns: temperature_K (float, Kelvin) and velocity_m_s (float, m/s). Sorted ascending by temperature, one row per 5 K interval over the range 823 K to 673 K.
- Scoring: scored by hidden verifier

### Step 3: Compute interface velocity vs temperature for Fe-Mn-Si-C alloy
- Role: scored (load-bearing)
- Action: For the Fe-3Mn-0.1C-1.5Si alloy, solve the energy balance equation over the cooling range from 530°C to 400°C at 5°C intervals, using f_α = 0.4 and including diffusion of both Mn and Si inside the interface. Write the data to step_02_FeMnSiC_velocity.csv.
- Output file: `/app/outputs/step_02_FeMnSiC_velocity.csv`
- Format: csv
- Contract: Two columns: temperature_K (float, Kelvin) and velocity_m_s (float, m/s). Sorted ascending by temperature, one row per 5 K interval over the range 803 K to 673 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_FeMnC_velocity.csv`
- `/app/outputs/step_02_FeMnSiC_velocity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_FeMnC_velocity.csv
- path: `/app/outputs/step_01_FeMnC_velocity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed interface velocity for Fe-Mn-C alloy as a function of cooling temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `velocity_m_s`
  - `units`:
    - `temperature_K`: Kelvin
    - `velocity_m_s`: m/s

### step_02_FeMnSiC_velocity.csv
- path: `/app/outputs/step_02_FeMnSiC_velocity.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Computed interface velocity for Fe-Mn-Si-C alloy as a function of cooling temperature.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `velocity_m_s`
  - `units`:
    - `temperature_K`: Kelvin
    - `velocity_m_s`: m/s

Notes: The hidden checker compares agent-reported velocities to digitized gold values from the paper and performs structural checks on the stagnant stage behaviour. No gold tolerances are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_FeMnC_velocity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "velocity_m_s"
        ],
        "units": {
          "temperature_K": "Kelvin",
          "velocity_m_s": "m/s"
        }
      },
      "description": "Computed interface velocity for Fe-Mn-C alloy as a function of cooling temperature."
    },
    {
      "file": "step_02_FeMnSiC_velocity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "velocity_m_s"
        ],
        "units": {
          "temperature_K": "Kelvin",
          "velocity_m_s": "m/s"
        }
      },
      "description": "Computed interface velocity for Fe-Mn-Si-C alloy as a function of cooling temperature."
    }
  ],
  "notes": "The hidden checker compares agent-reported velocities to digitized gold values from the paper and performs structural checks on the stagnant stage behaviour. No gold tolerances are revealed here."
}
```

## How you are scored
A hidden verifier independently evaluates each output file and combines the scores by weight to produce your final reward. For each alloy, the verifier compares your computed velocity curve to a hidden reference derived from the model as published. The comparison checks agreement in the log-velocity scale at each temperature and verifies structural features (a nearly zero initial velocity and a later rapid increase of at least two orders of magnitude). Simply reporting the paper’s numbers without the underlying computation will not succeed; every intermediate calculation must be executed as described in the workflow steps.
