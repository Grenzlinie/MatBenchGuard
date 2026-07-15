# Reduced Order Modeling of Mechanical Degradation in Lithium-Ion Battery Electrodes

## Problem background
Lithium-ion battery performance degrades over cycles due to mechanical damage, specifically the formation of microcracks in anode active particles during cycling. A reduced-order model (ROM) that accurately predicts the extent of microcrack density as a function of particle size and C-rate, and its impact on effective solid-state diffusivity, is needed to assess capacity fade at the electrode level.

## Approach
The reproduction is based on two computational components:

1. **1D radial diffusion model** for a single spherical active particle that undergoes delithiation with a constant surface flux. The ROM provides analytical expressions for the maximum microcrack density and the rate of damage evolution as functions of particle radius and C-rate; these determine the fraction of broken bonds, which reduces the effective solid-phase diffusivity via a power-law relation `D_s^eff = D_s * (1 - f_bb)^gamma`. The exponent `gamma` must be calibrated by comparing the 1D model predictions to reference 2D concentration gradients.

2. **1D porous electrode model** (anode / separator / cathode) that couples solid-state diffusion, electrolyte transport, and linearized Butler–Volmer kinetics. It uses the experimentally reported open-circuit potentials for hard carbon (anode) and NMC (cathode) and the electrode parameters listed in the source paper (thicknesses, porosities, diffusivities, conductivities, etc.). The ROM is coupled into this model by updating the anode's effective diffusivity at each incremental Amp-hour throughput according to the damage evolution.

The task is to implement both models, calibrate the effective-diffusivity exponent, and then simulate charge–discharge cycles to obtain the capacity evolution.

## Reproduction target
Produce two scored artifacts:

- A table of surface concentration gradients (absolute difference between lithium concentration at particle center and surface at end of delithiation) for particle radii 2.5, 5.0, 7.5, 10.0, 12.5, 15.0 µm and C‑rates 1, 2, 3, 4, 5, 6, 8, 10, calculated by the 1D radial diffusion model using the ROM with the calibrated exponent.

- A table of discharge capacities (in Ah) for each of five consecutive CCCV‑charge / CC‑discharge cycles at 2C and 4C, obtained from the full 1D electrode model with the ROM using a uniform anode particle radius of 10 µm.

## Assets

- Hard-carbon open-circuit potential curve
- NMC cathode OCP curve: 10.1149/2.084301jes
- Electrode and electrolyte parameters

## Workflow steps

### Step 1: Prepare parameters and OCP data
- Role: process
- Action: Obtain and digitize the open-circuit potential curves for hard-carbon (Gu & Wang 2000) and NMC (Awarke et al. 2013). Compile all electrode, separator, and electrolyte parameters from the source paper as listed in Table I. Implement the reduced-order model (ROM) formulas for A_max(R_s, C_rate) and m_rate(R_s, C_rate) as described, along with the effective diffusivity relation D_s^eff = D_s (1 - f_bb)^γ with γ=7.5.
- Evidence: none

### Step 2: Compute concentration gradients with ROM (γ=7.5)
- Role: scored
- Action: For each combination of particle radius R_s (2.5, 5.0, 7.5, 10.0, 12.5, 15.0 μm) and C-rate (1, 2, 3, 4, 5, 6, 8, 10 C), run a 1D radial diffusion simulation of a single delithiation (constant surface flux) using the ROM to compute microcrack density f_bb and effective diffusivity with γ=7.5. Record the absolute difference between lithium concentration at particle center and surface at the end of delithiation as the surface concentration gradient (in mol/m³).
- Output file: `/app/outputs/concentration_gradients.csv`
- Format: csv
- Contract: Columns: particle_radius_um (float), C_rate (float), surface_concentration_gradient_mol_m3 (float). One row per (R_s, C_rate) combination, 48 rows.
- Scoring: scored by hidden verifier

### Step 3: Simulate cycling with ROM and output capacity fade
- Role: scored (load-bearing)
- Action: Implement the 1D porous electrode model (anode/separator/cathode) with linearized Butler-Volmer kinetics and the ROM for anode particle degradation. Use anode particle radius 10 μm, hard-carbon OCP, and NMC cathode OCP. Simulate 5 CCCV charge / CC discharge cycles at C-rates of 2C and 4C, recording the discharge capacity (in Ah) for each cycle.
- Output file: `/app/outputs/capacity_fade.csv`
- Format: csv
- Contract: Columns: cycle_number (int), C_rate (float), discharge_capacity_Ah (float). Two groups: C_rate=2 with cycles 1–5, and C_rate=4 with cycles 1–5 (10 rows total).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/concentration_gradients.csv`
- `/app/outputs/capacity_fade.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### concentration_gradients.csv
- path: `/app/outputs/concentration_gradients.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Surface concentration gradient computed by 1D radial diffusion model with ROM. The checker will compare these values to hidden reference benchmarks using a predefined tolerance.
- schema:
  - `type`: table
  - `required_columns`: `particle_radius_um`, `C_rate`, `surface_concentration_gradient_mol_m3`
  - `units`:
    - `particle_radius_um`: micrometers
    - `C_rate`: dimensionless (1/h)
    - `surface_concentration_gradient_mol_m3`: mol/m^3

### capacity_fade.csv
- path: `/app/outputs/capacity_fade.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Discharge capacity over cycles for 2C and 4C from the full 1D electrode model with ROM. The checker will compare these values to hidden reference capacities using a predefined tolerance.
- schema:
  - `type`: table
  - `required_columns`: `cycle_number`, `C_rate`, `discharge_capacity_Ah`
  - `units`:
    - `cycle_number`: integer
    - `C_rate`: dimensionless (1/h)
    - `discharge_capacity_Ah`: Ah

Notes: No gold values or tolerances are disclosed. The hidden checker recomputes a deviation metric from the agent's submitted tables against the paper's reported 2D benchmark gradients and Figure 9b capacity values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "concentration_gradients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "particle_radius_um",
          "C_rate",
          "surface_concentration_gradient_mol_m3"
        ],
        "units": {
          "particle_radius_um": "micrometers",
          "C_rate": "dimensionless (1/h)",
          "surface_concentration_gradient_mol_m3": "mol/m^3"
        }
      },
      "description": "Surface concentration gradient computed by 1D radial diffusion model with ROM. The checker will compare these values to hidden reference benchmarks using a predefined tolerance."
    },
    {
      "file": "capacity_fade.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "cycle_number",
          "C_rate",
          "discharge_capacity_Ah"
        ],
        "units": {
          "cycle_number": "integer",
          "C_rate": "dimensionless (1/h)",
          "discharge_capacity_Ah": "Ah"
        }
      },
      "description": "Discharge capacity over cycles for 2C and 4C from the full 1D electrode model with ROM. The checker will compare these values to hidden reference capacities using a predefined tolerance."
    }
  ],
  "notes": "No gold values or tolerances are disclosed. The hidden checker recomputes a deviation metric from the agent's submitted tables against the paper's reported 2D benchmark gradients and Figure 9b capacity values."
}
```

## How you are scored
Your submission is evaluated by a hidden automatic verifier that independently recomputes a deviation metric for each scored artifact against reference values (derived from the original study). The verifier applies predefined, non‑public tolerances and combines the scores from the two artifacts according to fixed weights to compute your total reward. A careful implementation is necessary to achieve results within the acceptable bounds; merely reporting the expected numbers without executing the described workflow will not pass.
