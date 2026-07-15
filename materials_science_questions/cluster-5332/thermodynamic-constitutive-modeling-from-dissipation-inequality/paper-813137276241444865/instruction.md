# Thermo-Mechanical Gradient Plasticity Necking Simulation

## Problem background
In metallic structures, size effects and thermo‑mechanical coupling play a significant role during plastic deformation. Standard local plasticity theories cannot capture size‑dependent hardening and often exhibit pathological mesh sensitivity when simulating localized processes such as necking. To overcome these issues, gradient‑extended plasticity models incorporate an internal length scale that regularizes the problem and reflects microstructure‑based size effects. Here we consider a micromorphic gradient‑enhanced thermo‑plasticity model at finite strains. The computational experiment simulates the necking of a cylindrical bar under tension. The goal is to compute the load–displacement response for two conditions—local plasticity (zero length scale) and gradient plasticity (finite length scale)—as well as the temperature evolution at the specimen centre for the gradient case.

## Approach
You will implement a coupled thermo‑mechanical gradient plasticity model in a finite element code. The constitutive framework is built in the logarithmic strain space. The total logarithmic strain is split additively into elastic, plastic, and thermal parts. The elastic strain energy includes volumetric (bulk) and isochoric (shear) contributions. Plasticity is governed by a von Mises yield function with temperature‑dependent yield strength, hardening, and saturation. Viscoplastic flow follows a Perzyna‑type law. To regularise the localisation, a micromorphic scheme is used: a local equivalent plastic strain is linked to a global micromorphic hardening field via a quadratic penalty term. This coupling yields a modified Helmholtz equation that introduces the plastic length scale and allows the micromorphic variable to be defined in the entire domain, not only the plastic zone. Thermal effects are included through Fourier heat conduction and heat generation from plastic dissipation. The solution is obtained by a staggered algorithm that alternates between a mechanical step (frozen temperature) and a thermal step (fixed deformation).

Two cases must be simulated:
- Local plasticity: length scale parameter l_p = 0.
- Gradient plasticity: l_p = 0.2 mm.

The boundary value problem is axisymmetric necking of a cylindrical bar (radius 6.4135 mm, length 26.6 mm). To trigger localisation, the yield strength at the specimen centre is reduced by 10 %. A prescribed vertical displacement of up to 10 mm is applied at the top boundary. From the simulation histories you will extract the reaction force on the top boundary and the temperature at the geometric centre of the specimen. Further details are provided in the workflow steps.

## Reproduction target
The task requires you to produce the following three artefacts by running your own finite element simulation:

1. Load–displacement curve for the local plasticity case (l_p = 0).
2. Load–displacement curve for the gradient plasticity case (l_p = 0.2 mm).
3. Temperature–time curve at the specimen centre for the gradient case.

The curves must be direct outputs of the simulation. The format and file names are specified in the workflow steps. The submitted data will be evaluated by its agreement with the expected physical response obtained from a re‑implementation of the described model.

## Assets

- Open-source finite element library for coupled thermo-mechanical problems

## Material parameters

All parameters required for the simulation are listed below. These values correspond to metals, as provided in the original model. The yield stress y0 is reduced by 10 % at the centre of the bar to trigger localization; the base value is given.

- Bulk modulus κ = 164.2 GPa
- Shear modulus μ = 80.2 GPa
- Hardening modulus h = 0.13 GPa
- Penalty parameter ε_p = 4.0 GPa
- Initial yield stress y0 = 0.45 GPa (reduced to 0.405 GPa at the centre)
- Viscosity η_p = 1×10⁻⁷ GPa s
- Thermal expansion coefficient α_t = 1×10⁻⁵ K⁻¹
- Thermal conductivity K = 0.045 kN s⁻¹ K⁻¹ (equivalent to 45 N s⁻¹ K⁻¹)
- Heat capacity c = 3.588×10⁻³ GPa K⁻¹
- Thermal softening parameter w_h = 0.002 K⁻¹
- Flow stress softening parameter w_0 = 0.002 K⁻¹
- Saturation yield stress y_∞ = 1.165 GPa
- Saturation exponent δ = 16.96 (dimensionless)
- Reference temperature θ_0 = 300 K

The plastic length scale l_p is set to 0 mm for the local case and 0.2 mm for the gradient case.

## Workflow steps

### Step 1: Finite-element simulation of necking problem
- Role: process
- Action: Implement the coupled thermo-mechanical gradient plasticity model with micromorphic regularization in a finite element code. Set up the axisymmetric cylindrical bar problem (radius 6.4135 mm, length 26.6 mm, 10% reduced yield strength in the centre) and apply a prescribed vertical displacement up to 10 mm. Run the simulation for both l_p=0 (local) and l_p=0.2 mm (gradient) cases, recording the reaction force history and the temperature at the specimen centre.
- Evidence: `/app/outputs/none`

### Step 2: Load-displacement curve for local plasticity
- Role: scored (load-bearing)
- Action: From the l_p=0 simulation results, extract the reaction force at the top boundary versus the applied displacement and write a CSV file.
- Output file: `/app/outputs/step_01_ld_local.csv`
- Format: csv
- Contract: Columns: displacement_mm (float), load_kN (float). At least 100 equally spaced points from 0 to 10 mm.
- Scoring: scored by hidden verifier

### Step 3: Load-displacement curve for gradient plasticity
- Role: scored (load-bearing)
- Action: From the l_p=0.2 mm simulation results, extract the reaction force at the top boundary versus the applied displacement and write a CSV file.
- Output file: `/app/outputs/step_02_ld_gradient.csv`
- Format: csv
- Contract: Columns: displacement_mm (float), load_kN (float). At least 100 equally spaced points from 0 to 10 mm.
- Scoring: scored by hidden verifier

### Step 4: Temperature-time curve at centre for gradient case
- Role: scored (load-bearing)
- Action: From the l_p=0.2 mm simulation results, extract the temperature at the centre of the specimen versus time and write a CSV file.
- Output file: `/app/outputs/step_03_temp_time_center.csv`
- Format: csv
- Contract: Columns: time_s (float), temperature_K (float). At least 50 equally spaced points from 0 to 30 s.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_ld_local.csv`
- `/app/outputs/step_02_ld_gradient.csv`
- `/app/outputs/step_03_temp_time_center.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_ld_local.csv
- path: `/app/outputs/step_01_ld_local.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Load-displacement curve for local plasticity (l_p=0).
- schema:
  - `columns`:
    - `name`: displacement_mm
    - `type`: float
    - `name`: load_kN
    - `type`: float
  - `min_rows`: 100

### step_02_ld_gradient.csv
- path: `/app/outputs/step_02_ld_gradient.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Load-displacement curve for gradient plasticity (l_p=0.2 mm).
- schema:
  - `columns`:
    - `name`: displacement_mm
    - `type`: float
    - `name`: load_kN
    - `type`: float
  - `min_rows`: 100

### step_03_temp_time_center.csv
- path: `/app/outputs/step_03_temp_time_center.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Temperature-time curve at the centre of the specimen for the gradient case.
- schema:
  - `columns`:
    - `name`: time_s
    - `type`: float
    - `name`: temperature_K
    - `type`: float
  - `min_rows`: 50

Notes: All outputs are CSV files with a header row and floating-point numeric values. The verifier will recompute similarity metrics against reference curves. The instruction now contains all material constants needed to run the simulation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_ld_local.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          {
            "name": "displacement_mm",
            "type": "float"
          },
          {
            "name": "load_kN",
            "type": "float"
          }
        ],
        "min_rows": 100
      },
      "description": "Load-displacement curve for local plasticity (l_p=0)."
    },
    {
      "file": "step_02_ld_gradient.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          {
            "name": "displacement_mm",
            "type": "float"
          },
          {
            "name": "load_kN",
            "type": "float"
          }
        ],
        "min_rows": 100
      },
      "description": "Load-displacement curve for gradient plasticity (l_p=0.2 mm)."
    },
    {
      "file": "step_03_temp_time_center.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          {
            "name": "time_s",
            "type": "float"
          },
          {
            "name": "temperature_K",
            "type": "float"
          }
        ],
        "min_rows": 50
      },
      "description": "Temperature-time curve at the centre of the specimen for the gradient case."
    }
  ],
  "notes": "All outputs are CSV files with a header row and floating-point numeric values. The verifier will recompute similarity metrics against reference curves. The instruction now contains all material constants needed to run the simulation."
}
```

## How you are scored
A hidden verifier scores each scored CSV file independently. It compares your data against reference curves that represent the correct solution of the boundary value problem. The comparison checks both quantitative deviation (within tolerances appropriate for a re‑implementation) and qualitative trends (e.g., monotonicity of the load and temperature, correct ordering of peak loads between the local and gradient cases). The individual stage scores are combined to yield the final reward. Merely reporting a number is insufficient; the curves must be a faithful result of your own simulation that reproduces the expected behaviour of the model and the specified physical setup.
