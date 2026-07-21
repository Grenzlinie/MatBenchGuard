# Temperature-dependent transport coefficients of bulk water from ab initio molecular dynamics and entropy scaling

## Problem background
Liquid water's transport properties—shear viscosity and self-diffusion—change dramatically with temperature, especially when entering the supercooled regime. While classical force-field simulations can describe these properties reasonably well, a complete first-principles understanding requires ab initio molecular dynamics (AIMD) based on density functional theory. Different density functionals often yield widely varying predictions for transport coefficients, and there is no consensus on which one best captures the temperature evolution. Moreover, establishing a quantitative link between the liquid's structure (as encoded by the radial distribution function) and its dynamics would allow transport properties to be inferred from structural data alone. This task examines the temperature-dependent shear viscosity and self-diffusion of bulk water using AIMD with three exchange-correlation functionals (PBE-D3, optB88-vdW, SCAN) and compares them against a state-of-the-art classical force field benchmark (TIP4P/2005). It also explores whether the two-body excess entropy, computed from the oxygen-oxygen radial distribution function, can serve as a structural descriptor that relates to transport coefficients through exponential scaling relations.

## Approach
Classical molecular dynamics (MD) using the TIP4P/2005 water model and AIMD simulations using three DFT functionals are performed for a system of 32 water molecules at the experimental density of 1 g/cm³ and five temperatures (260, 270, 300, 330, 360 K). The simulations provide atomic trajectories and stress tensor data. Shear viscosity (η_GK) is obtained from the Green-Kubo integral of the stress autocorrelation function; self-diffusion coefficient (D_GK) is derived from the long-time slope of the mean-squared displacement with a finite-size correction. From the oxygen-oxygen radial distribution function (g(r)) of each trajectory, the dimensionless two-body excess entropy (s₂/k_B) is computed via an integral involving g(r). Reduced transport coefficients (η_GK/η₀ and D_GK/D₀) are then calculated using kinetic-theory reference values, and exponential scaling relations of the form y = A exp(-B s₂/k_B) are fitted for each functional (excluding PBE-D3, which yields too few valid data points). The whole workflow is executed by running classical MD with LAMMPS and AIMD with CP2K, followed by post-processing analysis on the generated trajectories.

## Reproduction target
Produce the following quantities for the defined system and simulation regime:

1.  **Force-field transport coefficients**: using the TIP4P/2005 water model, compute shear viscosity η_GK (Pa·s) and finite-size-corrected self-diffusion coefficient D_GK (m²/s) for the five temperatures (260, 270, 300, 330, 360 K).

2.  **AIMD transport coefficients**: for each functional (PBE-D3, optB88-vdW, SCAN) and each temperature, compute the same η_GK and D_GK. If the Green-Kubo integral does not reach a plateau or the system does not enter the diffusive regime within the simulation time, record the corresponding value as NaN.

3.  **Two-body excess entropy**: from all trajectories (FF and AIMD), compute the dimensionless quantity s₂/k_B via the oxygen-oxygen radial distribution function. Report one value per functional (including FF) and temperature.

4.  **Entropy scaling fit parameters**: using the data points where both transport coefficients are available, fit the exponential scaling laws for reduced viscosity (η_GK/η₀) and reduced diffusion (D_GK/D₀) as functions of s₂/k_B to obtain prefactor and exponent parameters (A_η, B_η, A_D, B_D). Perform these fits for the optB88-vdW, SCAN, and FF datasets; PBE-D3 is excluded because at most one temperature yields valid transport coefficients.

All results must be written to the four CSV files specified in the workflow steps.

## Assets

- CP2K: https://www.cp2k.org
- LAMMPS: https://www.lammps.org
- TIP4P/2005 force field parameters: Part of LAMMPS force field package or public repository

## Workflow steps

### Step 1: Generate equilibrated initial configurations
- Role: process
- Action: Run short force-field MD simulations with TIP4P/2005 for a 32-molecule water box at ρ=1 g/cm³ and each target temperature (260,270,300,330,360 K) to obtain equilibrated starting positions and velocities for AIMD.
- Evidence: none

### Step 2: Run TIP4P/2005 benchmark MD simulations
- Role: process
- Action: Run classical molecular dynamics simulations using the TIP4P/2005 water model in the NVT ensemble for 32 water molecules (box length 9.85 Å, density 1 g/cm³) at each of the five temperatures. Simulate for at least 120 ps with a 0.5 fs timestep. Store trajectory and off-diagonal stress tensor components (p_xy, p_xz, p_yz).
- Evidence: none

### Step 3: Compute FF transport coefficients
- Role: scored
- Action: From the TIP4P/2005 trajectories, compute the shear viscosity η_GK via Green-Kubo integration of the stress autocorrelation function (take plateau value). Compute the uncorrected diffusion coefficient D_PBC from the long-time slope of the mean-squared displacement (discard first 20 ps). Apply the finite-size correction D_GK = D_PBC + 2.837 k_B T / (6π η_GK L_box) with L_box=9.85 Å. Record the temperature, η_GK, and D_GK.
- Output file: `/app/outputs/step_01_ff_transport.csv`
- Format: csv
- Contract: Columns: temperature (float, K), eta_GK (float, Pa·s), D_GK (float, m²/s). Five rows.
- Scoring: scored by hidden verifier

### Step 4: Run AIMD production simulations
- Role: process
- Action: Perform ab initio molecular dynamics (AIMD) simulations in the NVT ensemble for each density functional (PBE-D3, optB88-vdW, SCAN) at each temperature (260,270,300,330,360 K) using the initial configurations from step 1. Use a 32-molecule cubic box (9.85 Å, ρ=1 g/cm³), a timestep of 0.5 fs, and run lengths of at least 120 ps (240 ps for optB88-vdW at 260 and 270 K). Save atomic trajectories and off-diagonal stress tensor components.
- Evidence: none

### Step 5: Compute AIMD transport coefficients
- Role: scored
- Action: From each AIMD trajectory, compute η_GK and D_GK as in step 3. If the viscosity running integral does not reach a plateau within the simulation time, record η_GK as NaN. If the system does not enter the diffusive regime, record D_GK as NaN. Write one row per functional-temperature combination.
- Output file: `/app/outputs/step_02_aimd_transport.csv`
- Format: csv
- Contract: Columns: functional (string, one of PBE-D3, optB88-vdW, SCAN), temperature (float, K), eta_GK (float or NaN, Pa·s), D_GK (float or NaN, m²/s). Up to 15 rows.
- Scoring: scored by hidden verifier

### Step 6: Compute two-body excess entropy s₂
- Role: scored
- Action: From all FF and AIMD trajectories, compute the oxygen-oxygen radial distribution function g(r) and evaluate the integral s₂/k_B = -2π n ∫ r²[g(r) ln g(r) - g(r) + 1] dr, where n is the number density. Record the dimensionless value for each functional (including FF) and temperature.
- Output file: `/app/outputs/step_03_s2.csv`
- Format: csv
- Contract: Columns: functional (string, FF, PBE-D3, optB88-vdW, SCAN), temperature (float, K), s2_kB (float, dimensionless). Up to 20 rows.
- Scoring: scored by hidden verifier

### Step 7: Fit entropy scaling parameters
- Role: scored (load-bearing)
- Action: For each functional with sufficient data (optB88-vdW, SCAN, FF), compute reduced transport coefficients η_GK/η0 and D_GK/D0, where η0 = √(m k_B T) / l₀², D0 = l₀ √(k_B T / m), with l₀ = n^(-1/3). Perform exponential fits y = A exp(-B s₂/k_B) to obtain A_eta, B_eta for viscosity and A_D, B_D for diffusion. Write the fitted parameters. Exclude PBE-D3 because only one temperature point is available.
- Output file: `/app/outputs/step_04_fit_params.csv`
- Format: csv
- Contract: Columns: functional (string, optB88-vdW, SCAN, FF), A_eta (float, prefactor for viscosity), B_eta (float, exponent for viscosity), A_D (float, prefactor for diffusion), B_D (float, exponent for diffusion). Three rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_ff_transport.csv`
- `/app/outputs/step_02_aimd_transport.csv`
- `/app/outputs/step_03_s2.csv`
- `/app/outputs/step_04_fit_params.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_ff_transport.csv
- path: `/app/outputs/step_01_ff_transport.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: TIP4P/2005 force-field shear viscosity and finite-size-corrected self-diffusion coefficient at five temperatures.
- schema:
  - `type`: table
  - `required_columns`: `temperature`, `eta_GK`, `D_GK`
  - `units`:
    - `temperature`: K
    - `eta_GK`: Pa·s
    - `D_GK`: m²/s

### step_02_aimd_transport.csv
- path: `/app/outputs/step_02_aimd_transport.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: AIMD shear viscosity and corrected diffusion coefficient for each functional and temperature; NaN allowed where dynamics did not converge.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `temperature`, `eta_GK`, `D_GK`
  - `units`:
    - `temperature`: K
    - `eta_GK`: Pa·s
    - `D_GK`: m²/s

### step_03_s2.csv
- path: `/app/outputs/step_03_s2.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Two-body excess entropy (divided by kB) from oxygen-oxygen radial distribution function for each functional and temperature.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `temperature`, `s2_kB`
  - `units`:
    - `s2_kB`: dimensionless

### step_04_fit_params.csv
- path: `/app/outputs/step_04_fit_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Exponential scaling fit parameters for reduced viscosity and reduced diffusion vs two-body excess entropy. Parameters from least-squares fit of log(y) vs s2_kB.
- schema:
  - `type`: table
  - `required_columns`: `functional`, `A_eta`, `B_eta`, `A_D`, `B_D`
  - `units`:
    - `A_eta`: dimensionless
    - `B_eta`: dimensionless
    - `A_D`: dimensionless
    - `B_D`: dimensionless

Notes: All quantities are defined as in the paper's Methods section. The shear viscosity η_GK is obtained from the Green-Kubo plateau; D_GK includes the hydrodynamic finite-size correction. NaN entries in step_02 correspond to cases where the viscosity plateau or diffusive regime was not reached, consistent with the paper's report. The fit in step_04 uses only data points where both transport coefficients are available; PBE-D3 is excluded because it had at most one temperature with valid transport coefficients.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_ff_transport.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature",
          "eta_GK",
          "D_GK"
        ],
        "units": {
          "temperature": "K",
          "eta_GK": "Pa·s",
          "D_GK": "m²/s"
        }
      },
      "description": "TIP4P/2005 force-field shear viscosity and finite-size-corrected self-diffusion coefficient at five temperatures."
    },
    {
      "file": "step_02_aimd_transport.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "temperature",
          "eta_GK",
          "D_GK"
        ],
        "units": {
          "temperature": "K",
          "eta_GK": "Pa·s",
          "D_GK": "m²/s"
        }
      },
      "description": "AIMD shear viscosity and corrected diffusion coefficient for each functional and temperature; NaN allowed where dynamics did not converge."
    },
    {
      "file": "step_03_s2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "temperature",
          "s2_kB"
        ],
        "units": {
          "s2_kB": "dimensionless"
        }
      },
      "description": "Two-body excess entropy (divided by kB) from oxygen-oxygen radial distribution function for each functional and temperature."
    },
    {
      "file": "step_04_fit_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "functional",
          "A_eta",
          "B_eta",
          "A_D",
          "B_D"
        ],
        "units": {
          "A_eta": "dimensionless",
          "B_eta": "dimensionless",
          "A_D": "dimensionless",
          "B_D": "dimensionless"
        }
      },
      "description": "Exponential scaling fit parameters for reduced viscosity and reduced diffusion vs two-body excess entropy. Parameters from least-squares fit of log(y) vs s2_kB."
    }
  ],
  "notes": "All quantities are defined as in the paper's Methods section. The shear viscosity η_GK is obtained from the Green-Kubo plateau; D_GK includes the hydrodynamic finite-size correction. NaN entries in step_02 correspond to cases where the viscosity plateau or diffusive regime was not reached, consistent with the paper's report. The fit in step_04 uses only data points where both transport coefficients are available; PBE-D3 is excluded because it had at most one temperature with valid transport coefficients."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the scored output files against reference values derived from the original study. The verifier reads your submitted CSV files and compares the reported quantities (transport coefficients, two-body entropy, and scaling parameters) within pre-defined tolerances. It also checks that NaN entries are correctly placed for conditions where the simulation length was insufficient to reach a plateau or diffusive regime. The overall reward is a weighted combination of the per-file scores: transport coefficients (η_GK, D_GK) contribute 40% of the total, the two-body entropy values contribute 20%, and the fitted scaling parameters contribute the remaining 40%. The reward is a single float between 0 and 1; meeting or exceeding the required quality on each component earns full credit. Note that merely reporting numbers that are close to typical values is insufficient—the computed results must arise from the specified simulation and analysis pipeline.
