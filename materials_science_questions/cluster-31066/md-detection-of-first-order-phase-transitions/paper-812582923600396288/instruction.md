# Shear-induced stabilization of liquid polymorphs in silicon

## Problem background
Supercooled liquid silicon exhibits a liquid-liquid transition between two distinct polymorphs: a low-density liquid (LDL) characterized by tetrahedral ordering and a high-density liquid (HDL) with higher coordination number. At equilibrium below the melting point both forms are metastable and rapidly crystalize. This work explores whether nonequilibrium planar shear can create steady-state liquids that retain the structural and energetic signatures of the LDL and HDL polymorphs, effectively stabilizing them out of equilibrium.

## Approach
The method uses nonequilibrium molecular dynamics (NEMD) simulations of 512 silicon atoms interacting via the Stillinger-Weber potential at a temperature of 1060 K. Two bulk densities are examined: ρ=2.28 g/cm³ (representing the LDL) and ρ=2.44 g/cm³ (representing the HDL). For each density, planar Couette flow is applied along the x direction with a gradient in y, using the SLLOD algorithm and Lees-Edwards boundary conditions; a Gaussian thermostat removes the dissipated heat to reach a nonequilibrium steady-state. Three conditions are simulated: equilibrium at rest (zero shear) and steady shear at two distinct rates (a low rate and a high rate). From the production trajectories, the following quantities are computed:

- First-shell coordination number Nc (integrated radial distribution function up to the first minimum).
- Tetrahedral order parameter qt (average over all atoms of a local four-neighbor measure).
- Average two-body potential energy u2 and three-body potential energy u3 (in kcal/mol).
- Shear viscosity η = -⟨Pxy⟩/γ (from the steady-state stress tensor; defined only for γ>0).
- Two-body entropy S2 computed from the pair correlation function g(r).

The resulting data allow one to assess how the competition between externally imposed shear and intrinsic tetrahedral ordering affects the liquid structure, energetics, and rheology across different densities.

## Reproduction target
Produce a single JSON file `/app/outputs/results.json` that contains one record for each of the six (density, shear_rate) conditions studied: ρ=2.28 g/cm³ and ρ=2.44 g/cm³, each at reduced shear rates γ*=0, 1×10⁻⁴, and 1.0. Each record must include the following keys:

- `density` (float, g/cm³)
- `shear_rate` (float, reduced units)
- `Nc` (float, first-shell coordination number)
- `qt` (float, tetrahedral order parameter)
- `u2` (float, average two-body energy in kcal/mol)
- `u3` (float, average three-body energy in kcal/mol)
- `viscosity` (float or null, shear viscosity in mPa·s; for γ*=0 set it to null)
- `S2` (float, the dimensionless two-body entropy defined as S2 = −ρ/2 ∫ [g(r) ln g(r) − (g(r)−1)] dr)

The JSON array must contain exactly six objects. The objective is to reproduce, from first-principles NEMD simulations, the structural, energetic, and rheological fingerprints of the low- and high-density liquid forms under shear.

## Assets

- LAMMPS: conda install -c conda-forge lammps
- Stillinger-Weber potential for Si: 10.1103/PhysRevB.31.5262
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Equilibrium MD at rest
- Role: process
- Action: Run NVT MD simulations of 512 Si atoms using the Stillinger-Weber potential at T=1060 K for densities ρ=2.28 g/cm³ and ρ=2.44 g/cm³ with zero shear rate (γ*=0). Equilibrate and run production trajectories; save atom trajectories for subsequent analysis.
- Evidence: `/app/outputs/rest_simulation.log`

### Step 2: NEMD simulations under shear
- Role: process
- Action: For each density (2.28 and 2.44 g/cm³), run planar Couette flow NEMD using the SLLOD algorithm, Lees-Edwards boundary conditions, and a Gaussian thermostat at reduced shear rates γ*=1e-4 and γ*=1.0. Use the same equilibration/production protocol as step 1. Save shear trajectories.
- Evidence: `/app/outputs/shear_simulation.log`

### Step 3: Compute structural, energetic, and rheological properties
- Role: scored (load-bearing)
- Action: From the rest and shear trajectories (steps 1-2), calculate for each (ρ, γ*) condition: first-shell coordination number Nc, tetrahedral order parameter qt, average two-body energy u₂ (kcal/mol), average three-body energy u₃ (kcal/mol), shear viscosity η = –⟨Pxy⟩/γ (null for γ*=0), and two-body entropy S₂ (using the definition given in the problem statement). Compile all results into a single JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: Array of JSON objects, one per condition (6 entries). Each object has keys: density (float, g/cm³), shear_rate (float, reduced units), Nc (float, first-shell coordination number), qt (float, tetrahedral order parameter), u2 (float, kcal/mol), u3 (float, kcal/mol), viscosity (float, mPa·s, or null for γ*=0), S2 (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Final scored artifact containing computed Nc, qt, u2, u3, viscosity, and S2 for each condition.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `density`:
        - `type`: float
        - `unit`: g/cm³
      - `shear_rate`:
        - `type`: float
        - `unit`: reduced
      - `Nc`:
        - `type`: float
        - `description`: first-shell coordination number
      - `qt`:
        - `type`: float
        - `description`: tetrahedral order parameter
      - `u2`:
        - `type`: float
        - `unit`: kcal/mol
      - `u3`:
        - `type`: float
        - `unit`: kcal/mol
      - `viscosity`:
        - `type`: `float`, `null`
        - `unit`: mPa·s
        - `description`: null for γ*=0
      - `S2`:
        - `type`: float
        - `description`: two-body entropy (dimensionless)
    - `required`: `density`, `shear_rate`, `Nc`, `qt`, `u2`, `u3`, `viscosity`, `S2`
  - `description`: One object per (density, shear_rate) pair; 6 total objects.

Notes: The hidden checker will compare each field to paper-derived reference values using predefined relative tolerances, and will also verify that the (u2, u3) pairs for rest and low-shear conditions fall close to a linear relation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "density": {
              "type": "float",
              "unit": "g/cm³"
            },
            "shear_rate": {
              "type": "float",
              "unit": "reduced"
            },
            "Nc": {
              "type": "float",
              "description": "first-shell coordination number"
            },
            "qt": {
              "type": "float",
              "description": "tetrahedral order parameter"
            },
            "u2": {
              "type": "float",
              "unit": "kcal/mol"
            },
            "u3": {
              "type": "float",
              "unit": "kcal/mol"
            },
            "viscosity": {
              "type": [
                "float",
                "null"
              ],
              "unit": "mPa·s",
              "description": "null for γ*=0"
            },
            "S2": {
              "type": "float",
              "description": "two-body entropy (dimensionless)"
            }
          },
          "required": [
            "density",
            "shear_rate",
            "Nc",
            "qt",
            "u2",
            "u3",
            "viscosity",
            "S2"
          ]
        },
        "description": "One object per (density, shear_rate) pair; 6 total objects."
      },
      "description": "Final scored artifact containing computed Nc, qt, u2, u3, viscosity, and S2 for each condition."
    }
  ],
  "notes": "The hidden checker will compare each field to paper-derived reference values using predefined relative tolerances, and will also verify that the (u2, u3) pairs for rest and low-shear conditions fall close to a linear relation."
}
```

## How you are scored
A hidden verifier will read your submitted `/app/outputs/results.json`. For each (density, shear_rate) condition, it will compare your reported values for Nc, qt, u2, u3, viscosity, and S2 against independently determined reference values. In addition, it will check that the (u2, u3) pairs from the rest and low-shear conditions satisfy a known linear relation. Each check contributes to a weighted score, which is aggregated into a final reward between 0 and 1. Simply copying pre‑existing numbers or printing expected values without actually performing the required MD trajectory analysis is not sufficient; the verifier expects values that are consistent with the underlying physics and numerical dispersion of the simulations.
