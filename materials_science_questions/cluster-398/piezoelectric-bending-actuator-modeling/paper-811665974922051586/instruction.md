# Three-layer electrostrictive polyurethane model simulation

## Problem background
Electroactive polymers (EAPs) such as pure polyurethane (PU) films can generate large compressive strain under moderate electric fields (<20 MV/m). Experimentally, the strain versus electric field curves show a parabolic relation at low fields followed by saturation at high fields, and the behaviour depends strongly on the film thickness: thicker films exhibit larger low-field electrostrictive coefficients, saturate at lower fields, and achieve lower saturated strains. The target is to compute these strain curves and their thickness dependence using a three-layer model that accounts for heterogeneous dielectric properties through the film thickness.

## Approach
The film is modelled as three distinct layers stacked along the thickness direction: two identical outer skin layers and a central bulk layer. The layers differ in their dielectric properties.

- The skin layers have lower permittivity (ε₁=ε₃=2.5e-11 F/m) and a lower saturation electric field (Eₛₐₜ₁=Eₛₐₜ₃=6 MV/m). Each skin layer has a fixed thickness of 7 µm, independent of the total film thickness.
- The bulk layer has higher permittivity (ε₂=9e-11 F/m) and a higher saturation field (Eₛₐₜ₂=16 MV/m). Its thickness equals the total film thickness minus twice the skin thickness.

Electric field distribution is governed by the layer capacitances and the saturable polarisation. The polarisation P in each layer follows P = ε·Eₛₐₜ·tanh(E/Eₛₐₜ), giving a nonlinear, saturating behaviour. The resulting thickness strain S₃₃ is proportional to P² in each layer.

Mechanically, the three layers are bonded together and are assumed to move in unison in the plane (no bending). A force balance among the layers yields a single uniform strain that satisfies the electrostrictive stresses from all layers simultaneously.

The simulation applies a two-cycle triangular electric field (0.1 Hz, amplitude up to 20 MV/m) across the total film thickness and computes the resulting thickness strain S₃₃ for the specified set of total film thicknesses.

## Reproduction target
Implement the three-layer model described above, simulate the thickness strain response for total film thicknesses 20, 28, 40, 60, 80, 100, 140, and 200 µm under a two-cycle triangular electric field (0.1 Hz, 0–20 MV/m). From the simulation, produce two CSV artifacts:
- `strain_vs_E.csv` with columns `thickness_um`, `field_MV_per_m`, `strain_percent` covering all simulated thicknesses and field points.
- `max_strain_vs_thickness.csv` with columns `thickness_um`, `max_strain_percent`, containing the maximum absolute strain achieved during the full field sweep for each thickness.

The hidden verifier will re-analyse `strain_vs_E.csv` to compute the low-field electrostrictive coefficient, saturation onset field, and saturated strain for each thickness, and will check the monotonic trend of `max_strain_vs_thickness.csv`. No absolute numeric targets are provided; the evaluation focuses on whether the simulated data exhibits the expected thickness-dependent structural features.

## Assets

- numpy: pip install numpy
- scipy: pip install scipy

## Workflow steps

### Step 1: Run three-layer electrostrictive simulation
- Role: process
- Action: Implement the three-layer electrostrictive model: set up the electrical and mechanical equations for three layers (two outer skin layers and one inner bulk) with saturating polarization, using parameters: skin thickness 7 μm per layer, permittivities ε1=ε3=2.5e-11 F/m, ε2=9e-11 F/m, saturation fields Esat1=Esat3=6 MV/m, Esat2=16 MV/m. Simulate the response to a two-cycle triangular electric field (0.1 Hz, amplitude up to 20 MV/m) for total film thicknesses 20, 28, 40, 60, 80, 100, 140, 200 μm. Record the resulting thickness strain S33 for each thickness and field point in a raw simulation record file.
- Evidence: `/app/outputs/simulation_record.npy`

### Step 2: Strain vs. electric field curves
- Role: scored (load-bearing)
- Action: From the simulation record, generate a CSV file containing the thickness strain S33 (in percent) as a function of applied electric field (MV/m) for all simulated thicknesses. Output one row per (thickness, field) combination.
- Output file: `/app/outputs/strain_vs_E.csv`
- Format: csv
- Contract: CSV with columns: thickness_um (numeric), field_MV_per_m (numeric), strain_percent (numeric). Rows for all simulated thicknesses and field values (0–20 MV/m).
- Scoring: scored by hidden verifier

### Step 3: Maximum strain vs. thickness
- Role: scored
- Action: From the simulation record, compute the maximum absolute strain for each thickness over the entire field sweep and output a CSV with two columns: thickness_um and max_strain_percent.
- Output file: `/app/outputs/max_strain_vs_thickness.csv`
- Format: csv
- Contract: CSV with columns: thickness_um (numeric), max_strain_percent (numeric). One row per simulated thickness.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/strain_vs_E.csv`
- `/app/outputs/max_strain_vs_thickness.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### strain_vs_E.csv
- path: `/app/outputs/strain_vs_E.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Thickness strain S33 versus applied electric field E for film thicknesses 20–200 μm; the checker recomputes low-field electrostrictive coefficient M, saturation onset field, and saturated strain, and verifies their monotonic ordering and saturation properties.
- schema:
  - `type`: table
  - `required_columns`: `thickness_um`, `field_MV_per_m`, `strain_percent`
  - `units`:
    - `thickness_um`: μm
    - `field_MV_per_m`: MV/m
    - `strain_percent`: %

### max_strain_vs_thickness.csv
- path: `/app/outputs/max_strain_vs_thickness.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Maximum absolute strain per film thickness over the field sweep; the checker verifies that maximum strain decreases monotonically with increasing thickness.
- schema:
  - `type`: table
  - `required_columns`: `thickness_um`, `max_strain_percent`
  - `units`:
    - `thickness_um`: μm
    - `max_strain_percent`: %

Notes: The simulation record (evidence) is not scored. The checker only reads the two CSVs and performs structural (ordering/threshold) checks, not absolute value matching.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "strain_vs_E.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_um",
          "field_MV_per_m",
          "strain_percent"
        ],
        "units": {
          "thickness_um": "μm",
          "field_MV_per_m": "MV/m",
          "strain_percent": "%"
        }
      },
      "description": "Thickness strain S33 versus applied electric field E for film thicknesses 20–200 μm; the checker recomputes low-field electrostrictive coefficient M, saturation onset field, and saturated strain, and verifies their monotonic ordering and saturation properties."
    },
    {
      "file": "max_strain_vs_thickness.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "thickness_um",
          "max_strain_percent"
        ],
        "units": {
          "thickness_um": "μm",
          "max_strain_percent": "%"
        }
      },
      "description": "Maximum absolute strain per film thickness over the field sweep; the checker verifies that maximum strain decreases monotonically with increasing thickness."
    }
  ],
  "notes": "The simulation record (evidence) is not scored. The checker only reads the two CSVs and performs structural (ordering/threshold) checks, not absolute value matching."
}
```

## How you are scored
Your submitted artifacts are scored by a hidden verifier that runs after your solution finishes. The verifier reads only `/app/outputs/strain_vs_E.csv` and `/app/outputs/max_strain_vs_thickness.csv`. It recomputes derived quantities (electrostrictive coefficient, saturation onset, saturated strain) from `strain_vs_E.csv` and checks the thickness‑dependent trends. It also checks the monotonic trend of `max_strain_vs_thickness.csv`. The two scored stages are combined with pre‑defined weights to produce a final reward between 0 and 1. Reporting the exact numbers from the original paper is neither required nor sufficient; you must produce consistent simulation data that passes the structural checks.
