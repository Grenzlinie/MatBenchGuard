# Oxygen diffusion in mixed-oxide nanocrystals via molecular dynamics

## Problem background
Understanding oxygen transport in mixed (Pu_xTh_1-x)O₂ oxides is essential for nuclear fuel design, where plutonium can be blended with thorium. Classical molecular dynamics with established pair potentials can predict oxygen self-diffusion coefficients and reveal composition- and temperature-dependent regimes of ionic mobility. This reproduction task recreates such simulations to compute oxygen diffusion coefficients and activation energies across the PuO₂–ThO₂ composition range.

## Approach
The approach uses molecular dynamics of isolated nanocrystals with free surfaces. Model systems are constructed as perfect octahedra of PuO₂, ThO₂, and (Pu₀.₅Th₀.₅)O₂ with 5460 particles, with a regular cation alternation for the mixed oxide. Interatomic interactions follow the MOX-07 pair potentials for Pu–O and O–O, complemented by a compatible Th–O potential. After equilibration with a Berendsen thermostat, production runs are performed at multiple temperatures (spanning superionic, transitional, and low‑temperature regimes) using a stochastic velocity rescaling thermostat. For each composition and temperature, several independent runs are collected to obtain reliable statistics. The oxygen self‑diffusion coefficient D is computed from the mean‑squared displacement of oxygen ions in the bulk central region (excluding surface) using the Einstein relation ⟨a²(t)⟩ = 6 D t. An Arrhenius analysis of ln D versus 1/kT then identifies the linear segments corresponding to the superionic, transitional (Region I), and low‑temperature (Region II) regimes; effective activation energies are extracted by fitting each segment.

## Reproduction target
Compute oxygen self‑diffusion coefficients D(T) for PuO₂, ThO₂, and (Pu₀.₅Th₀.₅)O₂ nanocrystals at a minimum of five temperatures covering the range from about 1300 K to 3200 K. From the resulting D(T) data, identify the temperature boundaries between the superionic, transitional, and low‑temperature regimes and extract effective activation energies E_D for each regime and composition. Also report, based on the computed D(T) curves, whether the diffusion coefficient increases monotonically with Pu content and whether the D values for (Pu₀.₅Th₀.₅)O₂ are close to those for pure PuO₂ throughout the temperature range.

## Assets

- MOX-07 pair potentials (Potashnikov et al., 2011): https://doi.org/10.1016/j.jnucmat.2011.07.015
- Th-O pair potential (Boyarchenkov et al., 2020): https://doi.org/10.1063/5.0013070
- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov

## Workflow steps

### Step 1: Construct model nanocrystals
- Role: process
- Action: Generate initial atomic coordinates for perfect octahedral nanocrystals of PuO₂, ThO₂, and (Pu₀.₅Th₀.₅)O₂ with 5460 particles, using a regular alternation of cation types. The structures must be neutral, built from MO₂ molecules, and have a free surface predominantly faceted by {111} planes. Write the atomic configuration files for subsequent MD simulation.
- Evidence: `/app/outputs/nanocrystal_configs.log`

### Step 2: Run molecular dynamics simulations
- Role: process
- Action: For each composition (PuO₂, ThO₂, (Pu₀.₅Th₀.₅)O₂), run multiple independent MD simulations (at least 10 per temperature) at a minimum of 5 temperatures spanning approximately 1300 K to 3200 K to cover superionic, transitional, and low‑temperature regimes. Use the MOX-07 pair potentials and compatible Th-O potential, integration time step 3 fs, a Berendsen thermostat during equilibration and a stochastic velocity rescaling thermostat during production. Simulate each run for a duration sufficient to achieve diffusive oxygen motion (varying from ~1.5 ns to up to 120 ns, longer at lower temperatures). Correct for rigid‑body rotation during post‑processing. Save atomic trajectories or processed mean-squared displacement data for analysis.
- Evidence: `/app/outputs/md_simulation_log.txt`

### Step 3: Calculate oxygen diffusion coefficients
- Role: scored (load-bearing)
- Action: From the MD trajectories, compute the mean‑squared displacement of oxygen ions located in a central spherical region at least 1.75 lattice constants from the surface. Extract the oxygen self‑diffusion coefficient D using the Einstein relation ⟨a²(t)⟩ = 6 D t. Report D and its standard error for each composition and temperature.
- Output file: `/app/outputs/step_01_diffusion_coefficients.tsv`
- Format: tsv
- Contract: composition (string), temperature_K (float), D_cm2_per_s (float), D_uncertainty_cm2_per_s (float)
- Scoring: scored by hidden verifier

### Step 4: Determine activation energies and diffusion regimes
- Role: scored
- Action: From the ln(D) vs 1/(kT) data, identify the temperature boundaries between the superionic, transitional (Region I), and low‑temperature (Region II) regimes for each composition. Fit a linear segment to each regime and extract the effective diffusion activation energy E_D and its uncertainty. Report the fitted parameters per composition and regime.
- Output file: `/app/outputs/step_02_activation_energies.tsv`
- Format: tsv
- Contract: composition (string), region (string), E_D_eV (float), E_D_uncertainty_eV (float), temperature_range_K (string)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_diffusion_coefficients.tsv`
- `/app/outputs/step_02_activation_energies.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_diffusion_coefficients.tsv
- path: `/app/outputs/step_01_diffusion_coefficients.tsv`
- format: tsv
- purpose: scored
- target_policy: reference_match
- description: Oxygen self‑diffusion coefficient D at each composition and temperature.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `temperature_K`, `D_cm2_per_s`, `D_uncertainty_cm2_per_s`
  - `units`:
    - `D_cm2_per_s`: cm^2/s
    - `D_uncertainty_cm2_per_s`: cm^2/s

### step_02_activation_energies.tsv
- path: `/app/outputs/step_02_activation_energies.tsv`
- format: tsv
- purpose: scored
- target_policy: reference_match
- description: Effective activation energy E_D fitted for each diffusion regime and composition.
- schema:
  - `type`: table
  - `required_columns`: `composition`, `region`, `E_D_eV`, `E_D_uncertainty_eV`, `temperature_range_K`
  - `units`:
    - `E_D_eV`: eV
    - `E_D_uncertainty_eV`: eV

Notes: The reported diffusion coefficients and activation energies will be compared against the hidden reference values from the source study using appropriate tolerances. Structural trends (e.g., monotonic ordering with composition) are also verified. The MD workflow is stochastic; results are accepted within a tolerance range that accounts for run‑to‑run variability.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_diffusion_coefficients.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "temperature_K",
          "D_cm2_per_s",
          "D_uncertainty_cm2_per_s"
        ],
        "units": {
          "D_cm2_per_s": "cm^2/s",
          "D_uncertainty_cm2_per_s": "cm^2/s"
        }
      },
      "description": "Oxygen self‑diffusion coefficient D at each composition and temperature."
    },
    {
      "file": "step_02_activation_energies.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "composition",
          "region",
          "E_D_eV",
          "E_D_uncertainty_eV",
          "temperature_range_K"
        ],
        "units": {
          "E_D_eV": "eV",
          "E_D_uncertainty_eV": "eV"
        }
      },
      "description": "Effective activation energy E_D fitted for each diffusion regime and composition."
    }
  ],
  "notes": "The reported diffusion coefficients and activation energies will be compared against the hidden reference values from the source study using appropriate tolerances. Structural trends (e.g., monotonic ordering with composition) are also verified. The MD workflow is stochastic; results are accepted within a tolerance range that accounts for run‑to‑run variability."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact. The diffusion coefficients in step_01_diffusion_coefficients.tsv are compared to expected values with appropriate tolerances. The activation energies in step_02_activation_energies.tsv are compared to reference values, and the identified regime boundaries are checked. In addition, structural consistency checks (monotonic ordering of D with composition, agreement between mixed and pure oxide) are enforced. The final reward is a weighted combination of the scores from these checks.
