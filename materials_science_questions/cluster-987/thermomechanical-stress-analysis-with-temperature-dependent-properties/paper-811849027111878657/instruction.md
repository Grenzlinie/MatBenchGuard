# Coupled Thermal-Electric-Structural Finite Element Simulation of Aluminum Compression with Joule Heating

## Problem background
Recent experiments have shown that passing a direct electric current through metals during compressive deformation can substantially reduce the required flow stress. An open question is how much of this reduction comes from resistive (Joule) heating and how much stems from direct effects of electron flow. Separating these contributions requires a detailed coupled thermal–electric–structural finite element model that accurately predicts the temperature evolution and resulting stress–strain behavior due to resistive heating alone. This task reproduces such a model for a compression experiment on an aluminum specimen between steel fixtures: you will implement the coupled multiphysics simulation and compute the maximum specimen surface temperature over time and the true stress–strain curve for a specified current density, which together characterize the thermal influence and provide a baseline for isolating non‑thermal effects.

## Approach
### Geometry (half‑symmetry 3D model)
- Aluminum specimen: cylinder of diameter 6.35 mm and length 9.53 mm. Half‑symmetry plane cuts longitudinally through the axis, so model a semi‑cylinder of radius 3.175 mm, length 9.53 mm, with the flat face as symmetry boundary.
- Upper and lower steel platens (in direct contact with the specimen): cylindrical blocks, diameter 20 mm, thickness 5 mm each.
- Upper and lower steel cylinders: diameter 25 mm, length 10 mm each.
- Upper and lower rectangular steel plates: 40 mm × 30 mm × 10 mm (width × depth × thickness).
- All parts are arranged coaxially along the vertical axis; the symmetry plane coincides with the XZ plane (Y axis vertical). The plates, cylinders, and platens are aligned center-to-center.

### Mesh
Generate a conformal hexahedral mesh with approximately 9000 elements, refined in the specimen and at the contact interfaces. The mesh size should be chosen so that further refinement does not change the results appreciably (convergence check).

### Material properties
#### 6061‑T6511 aluminum (temperature‑dependent)
Bilinear plasticity with temperature‑dependent yield stress and elastic modulus (considered constant) and constant tangent modulus 142 MPa. Poisson’s ratio 0.33, density 2700 kg/m³. The following table gives the temperature‑dependent material data (linear interpolation between points is acceptable).

| Temperature (°C) | Elastic Modulus (GPa) | Yield Stress (MPa) | Tangent Modulus (MPa) | Thermal Conductivity (W/(m·°C)) | Specific Heat (J/(kg·°C)) | Electrical Resistivity (10⁻⁸ Ω·m) | CTE (10⁻⁶/°C) |
|------------------|-----------------------|--------------------|-----------------------|--------------------------------|---------------------------|----------------------------------|---------------|
| 20               | 73                    | 280               | 142                   | 167                            | 896                       | 3.99                             | 23.6          |
| 50               | 73                    | 274               | 142                   | 170                            | 906                       | 4.15                             | 24.0          |
| 100              | 73                    | 250               | 142                   | 180                            | 920                       | 4.60                             | 24.5          |
| 150              | 73                    | 220               | 142                   | 190                            | 940                       | 5.20                             | 25.0          |
| 200              | 73                    | 180               | 142                   | 193                            | 963                       | 5.70                             | 25.5          |

*Note:* These values approximate the experimental data used in the original study (Figs. 2–4). They are suitable for the purpose of this reproduction.

#### Steel fixtures (constant)
| Property             | Value                      |
|----------------------|----------------------------|
| Elastic modulus      | 205 GPa                    |
| Poisson’s ratio      | 0.30                       |
| Thermal expansion    | 12.6 × 10⁻⁶ /°C           |
| Thermal conductivity | 29 W/(m·°C)               |
| Specific heat        | 460 J/(kg·°C)             |
| Density              | 7810 kg/m³                |
| Electrical resistivity| 1.7 × 10⁻⁷ Ω·m          |

### Boundary conditions
- Symmetry plane (Y=0 plane): adiabatic (no heat flux) and Y‑displacement fixed.
- Electrical: apply a uniform current density on the top surface of the upper rectangular plate corresponding to 60 A/mm² through the specimen cross‑section (i.e., total current = 60 × π × (3.175 mm)² ≈ 1 899 A). The bottom surface of the lower rectangular plate is fixed at 0 V.
- Convection on all exposed surfaces to ambient air at 20 °C with a uniform film coefficient of 5 W/(m²·°C).
- Mechanical: bottom of lower plate fixed in Y direction; top of upper plate moved downward at 25.4 mm/min (0.4233 mm/s) to simulate crosshead displacement after the initial preload.
- Initial preload: 223 N compressive force applied to the top plate to engage contacts before the current is turned on.
- Contact between platens and specimen: standard surface‑to‑surface contact with penalty friction (μ=0.1) and heat/electrical conduction that depends on contact pressure (use default contact‑dependent transfer).

### Coupled simulation procedure
The simulation is carried out via a staggered iterative loop:
1. Static structural preload: apply 223 N, keep contacts closed.
2. For each 0.5 s interval up to 18 s:
   a. Transient thermal‑electric step: solve for temperature and current density distribution with the current intensity corresponding to 60 A/mm², using temperature‑dependent material properties and Joule heating, convection, and contact‑dependent heat/current transfer.
   b. Map the temperature field to the structural model and update temperature‑dependent mechanical properties.
   c. Static structural step: apply the crosshead displacement increment (0.21165 mm per 0.5 s) and thermal expansion, using bilinear plasticity.
   d. Update the thermal‑electric mesh geometry based on the structural displacements.
3. Continue until t=18 s.

## Reproduction target
Build the coupled model described above using an open‑source finite‑element solver (e.g., CalculiX, Elmer, or FEniCS) or an equivalent tool. Perform a simulation with an applied current density of 60 A/mm², an initial preload of 223 N, a crosshead displacement rate of 25.4 mm/min, and a total process time of 18 s. From the results, generate two scored output files:
- `/app/outputs/temperature_time.csv`: maximum temperature on the specimen surface at each 0.5 s time step. CSV columns: time (s), temperature (°C).
- `/app/outputs/stress_strain.csv`: true stress vs. true strain curve, computed from the structural solution (true stress = reaction force / current cross‑sectional area ; true strain = ln(initial length / current length)). CSV columns: true_strain (mm/mm), true_stress (MPa). Sample at regular intervals or output all available steps.
All required material parameters (temperature‑dependent curves for aluminum, constant values for steel) and boundary conditions are provided in the workflow steps below; no external dataset is needed.

## Assets

- CalculiX: http://www.calculix.de/
- Gmsh: https://gmsh.info/
- Python packages (numpy, pandas, scipy, matplotlib): pip

## Workflow steps

### Step 1: FE Model Setup
- Role: process
- Action: Build the finite element model according to the geometry, material data, and boundary conditions specified in the Approach section. Generate a mesh of approximately 9000 hexahedral elements, refined near the specimen. (See explicit dimensions, property tables, and boundary condition values in the Approach section.)
- Evidence: `/app/outputs/model_summary.txt`

### Step 2: Coupled Thermal-Electric-Structural Simulation
- Role: process
- Action: Implement an iterative coupling loop: for each 0.5 s interval up to 18 s, (i) run a transient thermal-electric solution with the current density and temperature-dependent Joule heating, convection, and contact-dependent heat/current transfer; (ii) map the resulting temperature field onto the structural model; (iii) run a static structural analysis applying the crosshead displacement (25.4 mm/min) and thermal expansion, using bilinear plasticity; (iv) update the thermal-electric model mesh with the deformed shape from the structural solution. Before the loop, apply an initial static load of 223 N to engage contacts.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Temperature Profile Extraction
- Role: scored (load-bearing)
- Action: From the simulation results, extract the maximum temperature on the specimen surface at each 0.5 s time step. Output time (s) and temperature (°C).
- Output file: `/app/outputs/temperature_time.csv`
- Format: csv
- Contract: CSV with columns: time (s), temperature (degC).
- Scoring: scored by hidden verifier

### Step 4: True Stress-Strain Curve Extraction
- Role: scored (load-bearing)
- Action: From the structural solution, compute true stress and true strain. True strain = ln(initial length / current length), true stress = reaction force / current cross-sectional area (assuming volume conservation). Sample the stress-strain curve at regular strain intervals or output all simulation time steps.
- Output file: `/app/outputs/stress_strain.csv`
- Format: csv
- Contract: CSV with columns: true_strain (mm/mm), true_stress (MPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/temperature_time.csv`
- `/app/outputs/stress_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### temperature_time.csv
- path: `/app/outputs/temperature_time.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Maximum temperature on the specimen surface as a function of time for the 60 A/mm² current density simulation. The checker will compute RMSE against a hidden reference curve and score by threshold_or_better.
- schema:
  - `type`: table
  - `required_columns`: `time`, `temperature`
  - `units`:
    - `time`: s
    - `temperature`: degC

### stress_strain.csv
- path: `/app/outputs/stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: True stress versus true strain curve for the 60 A/mm² current density simulation. The checker will compute RMSE against a hidden reference curve and score by threshold_or_better.
- schema:
  - `type`: table
  - `required_columns`: `true_strain`, `true_stress`
  - `units`:
    - `true_strain`: mm/mm
    - `true_stress`: MPa

Notes: The hidden checker compares the agent's temperature_time.csv and stress_strain.csv to reference curves digitized from the paper's published figures for the 60 A/mm² case. RMSE below a hidden threshold earns full credit. Both curves must be provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "temperature_time.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "temperature"
        ],
        "units": {
          "time": "s",
          "temperature": "degC"
        }
      },
      "description": "Maximum temperature on the specimen surface as a function of time for the 60 A/mm² current density simulation. The checker will compute RMSE against a hidden reference curve and score by threshold_or_better."
    },
    {
      "file": "stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "true_strain",
          "true_stress"
        ],
        "units": {
          "true_strain": "mm/mm",
          "true_stress": "MPa"
        }
      },
      "description": "True stress versus true strain curve for the 60 A/mm² current density simulation. The checker will compute RMSE against a hidden reference curve and score by threshold_or_better."
    }
  ],
  "notes": "The hidden checker compares the agent's temperature_time.csv and stress_strain.csv to reference curves digitized from the paper's published figures for the 60 A/mm² case. RMSE below a hidden threshold earns full credit. Both curves must be provided."
}
```

## How you are scored
A hidden verifier evaluates both of your output CSV files. For each file, the verifier computes the root‑mean‑square error (RMSE) between your submitted curve and a hidden reference curve derived from the original study. Full credit for that file is awarded if the RMSE meets or beats a predetermined threshold; if the error exceeds the threshold, partial credit is assigned, decreasing with larger errors. The overall reward is a weighted combination of the scores for the temperature and stress‑strain files. You must produce the curves through genuine multiphysics simulation; reporting memorized numbers will not pass the verifier's comparison.
