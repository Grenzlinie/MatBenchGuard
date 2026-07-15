# Simulating hydraulic fracturing with Biot consolidation and smeared crack model: tip stresses and crack opening

## Problem background
Geofluids (water, magma, …) rise through the Earth's crust and can form ore deposits when they focus and mix. The intrusion of fluids can create and widen cracks in the surrounding porous rock, and the altered crack network further guides fluid flow, affecting mineralization. The paper proposes a numerical framework that couples porous skeleton deformation and pore-fluid flow (Biot's consolidation) with a smeared crack model to simulate hydraulic fracturing and the resulting crack propagation, stiffness reduction, and permeability change. The target outcome is the stress at the tips of the induced crack and the maximum crack opening width under different water pressures, which quantify the focusing and penetrating ability of the geofluid.

## Approach
You will implement a coupled numerical model that solves the Biot consolidation equations for a deformable fluid-saturated porous medium together with a smeared crack model. The smeared crack representation treats a crack not as a discrete discontinuity but as a band where stiffness is reduced and permeability becomes anisotropic and enhanced in the crack direction. Tensile cracking initiates when the minor principal stress exceeds the material tensile strength; thereafter the element's stiffness matrix is modified using reduction coefficients (μ for Young's modulus, χ for shear modulus) and the permeability along the crack is updated as a function of the effective normal stress. The problem geometry is a 2D vertical section: a gravel column on the left and a clay block containing a central weak zone on the right. You will assign the published material properties (Young's modulus, Poisson's ratio, hydraulic conductivity) for each zone and apply a water pressure to the left gravel boundary while keeping zero pore pressure on the right clay boundary. The simulation is run as a transient, fully coupled process for three applied water pressure levels: 100 kPa, 200 kPa, and 300 kPa. Any numerical method (FEM, meshless, or a hybrid) that can capture crack initiation, propagation, and opening is acceptable.

## Reproduction target
Build the 2D model described above, run the coupled simulation for water pressures of 100, 200, and 300 kPa, and then extract three quantities for each pressure: (i) the stress (kPa) at crack-tip point 1, (ii) the stress (kPa) at crack-tip point 2, and (iii) the maximum crack opening (mm). Record the results in a CSV file with columns water_pressure (kPa), stress_tip_1 (kPa), stress_tip_2 (kPa), max_opening (mm), containing one row per pressure level.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy
- FEniCS (or equivalent FEM library): https://fenicsproject.org

## Workflow steps

### Step 1: Geometry, material, and crack model setup
- Role: process
- Action: Define the 2D geometry from the problem: a gravel column (left) and a clay block containing a central weak zone (right). Assign material parameters (Young's modulus, Poisson's ratio, hydraulic conductivity) as given: gravel (E=10 MPa, ν=0.3, K=1 m/s), compacted clay (E=1 MPa, ν=0.3, K=1.0E-8 m/s), weak zone (E=0.01 MPa, ν=0.2, K=1 m/s). Set boundary conditions: water pressure applied on left gravel boundary, zero pore pressure on right clay boundary, no flow on other external boundaries, and appropriate mechanical constraints. Initialize the smeared crack model with stiffness reduction coefficients μ=0.01, χ=0.001 and the stress‑permeability relation (α=0.1/kPa, reference permeabilities derived from the given conductivities). Prepare the discretization and input files required for the simulation.
- Evidence: `/app/outputs/setup_log.txt`

### Step 2: Coupled hydraulic fracture simulation
- Role: process
- Action: Run the transient, fully coupled Biot's consolidation simulation with the smeared crack model for applied water pressures of 100, 200, and 300 kPa. The simulation couples porous skeleton deformation (elastoplasticity with crack‑induced stiffness reduction and softening) and pore‑fluid flow (Darcy's law with crack‑enhanced anisotropic permeability). Use any numerical method (FEM, meshless, or equivalent) that captures crack initiation, propagation, and opening. Record the full field results for post‑processing.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Extract tip stresses and maximum opening
- Role: scored (load-bearing)
- Action: From the simulation results, for each water pressure (100, 200, 300 kPa) extract: (i) the stress at tip point 1 (kPa), (ii) the stress at tip point 2 (kPa), and (iii) the maximum crack opening width (mm). Write the values to a CSV file with one row per pressure.
- Output file: `/app/outputs/hydraulic_fracture_results.csv`
- Format: csv
- Contract: Columns: water_pressure (kPa), stress_tip_1 (kPa), stress_tip_2 (kPa), max_opening (mm). Three rows for 100, 200, 300 kPa.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hydraulic_fracture_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hydraulic_fracture_results.csv
- path: `/app/outputs/hydraulic_fracture_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Reproduced hydraulic fracture quantities: stress at two crack‑tip points and maximum crack opening for three water pressure levels. The checker compares these values to hidden paper‑reported gold data with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `water_pressure`, `stress_tip_1`, `stress_tip_2`, `max_opening`
  - `units`:
    - `water_pressure`: kPa
    - `stress_tip_1`: kPa
    - `stress_tip_2`: kPa
    - `max_opening`: mm

Notes: The agent must re-implement the coupled Biot-smeared crack simulation; the outputs are expected to match the paper's Table 3 within tolerances that account for legitimate implementation differences. No gold values are revealed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hydraulic_fracture_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "water_pressure",
          "stress_tip_1",
          "stress_tip_2",
          "max_opening"
        ],
        "units": {
          "water_pressure": "kPa",
          "stress_tip_1": "kPa",
          "stress_tip_2": "kPa",
          "max_opening": "mm"
        }
      },
      "description": "Reproduced hydraulic fracture quantities: stress at two crack‑tip points and maximum crack opening for three water pressure levels. The checker compares these values to hidden paper‑reported gold data with appropriate tolerances."
    }
  ],
  "notes": "The agent must re-implement the coupled Biot-smeared crack simulation; the outputs are expected to match the paper's Table 3 within tolerances that account for legitimate implementation differences. No gold values are revealed here."
}
```

## How you are scored
A hidden verifier will read your CSV and compare each of the nine reported values against hidden reference values that were obtained by faithfully following the same protocol. The comparison uses tolerances that account for legitimate differences between numerical implementations. Each matched value contributes equally to a total score in the range [0,1]. Reporting the correct numbers is not sufficient by itself; the hidden verifier scores the submitted artifact directly.
