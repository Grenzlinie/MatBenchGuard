# Chemo-Mechanical Phase Field Model for Fracture in Battery Electrodes

## Problem background
Lithium-ion batteries (LIBs) with high-capacity anode materials like silicon undergo large volume changes (up to ~300%) during lithiation, which generates high mechanical stresses and can lead to fracture, reducing battery lifetime. Phase field fracture models are a powerful tool for simulating crack initiation and propagation under such chemomechanical loading. The present work compares two phase field formulations for fracture coupled with lithium diffusion and stress evolution: a conventional isotropic model and a hybrid model designed to avoid physically unrealistic crack growth in compressive regions. The task is to implement both formulations for a silicon nanowire electrode cross‑section and compute the time‑evolution of crack length to assess the difference between the two models.

## Approach
The model couples three fields: displacement (quasi‑static mechanical equilibrium), lithium concentration (mass conservation), and a fracture phase field (Ginzburg‑Landau evolution). The total free energy includes elastic, chemical, and fracture contributions, with the elastic energy degraded by a function of the fracture field to model stiffness loss. Chemical strain is introduced as a hydrostatic dilatation proportional to lithium concentration, and elastic properties (Young’s modulus, Poisson’s ratio) are linearly dependent on concentration. The key difference between the two formulations lies in the fracture driving force. In the isotropic model, the full elastic energy density drives crack evolution. In the hybrid model, only the tension part of the elastic energy density (derived from the largest principal effective stress) enters the fracture equation, while the momentum balance remains isotropic, reducing unphysical cracking in compression. The coupled partial differential equations are solved with a finite element code using standard isoparametric elements, a Newmark time integration scheme for the diffusion and fracture equations, and a Newton‑Raphson iterative solver. The simulation domain is a two‑dimensional plane‑strain circular plate (radius 60 nm) representing a nanowire cross‑section. An initial central crack of length 60 nm is introduced. Boundary conditions apply a constant maximum lithium concentration on the outer surface, and the initial concentration inside the electrode is a low uniform value. The time step is 0.0025 s and the total simulation time is 6 s. The crack length is extracted post‑process from the fracture field φ by measuring the distance between crack faces.

## Reproduction target
Implement both the isotropic and hybrid phase field models described above. Generate a finite element mesh for a 2D plane‑strain circular domain of radius 60 nm with a centered initial crack of length 60 nm, using mesh refinement near the crack tip. Use the material properties listed in the paper (Young’s modulus of Si and lithiated Si, Poisson’s ratios, partial molar volume, molecular mobility, etc.), concentration‑dependent elastic moduli, and the baseline fracture parameters G_cr = 7 N/m, l₀ = 10 nm. Initialize concentration c₀ = 1.0 Kmol/m³ and fracture field φ = 1 (intact) everywhere, with a smooth initial crack degradation. Apply a constant lithium concentration c_max = 88.67 Kmol/m³ on the outer boundary. Run the simulation for both models from t = 0 to t = 6 s with a time step Δt = 0.0025 s. At output time steps (sufficient to capture the crack length evolution), compute the crack length (distance between crack faces derived from the φ field) for both formulations. Produce a single CSV file `step_01_crack_lengths.csv` with columns: time (s), isotropic_crack_length_nm, hybrid_crack_length_nm. Include at least the initial time (t = 0 s) and the final time (t = 6 s). The primary objective is to quantify the crack length evolution and compare the two models at t = 6 s.

## Assets

- NumPy: numpy
- SciPy: scipy
- scikit-fem (finite element library): scikit-fem
- Matplotlib: matplotlib

## Workflow steps

### Step 1: Model configuration and mesh generation
- Role: process
- Action: Define the geometry (circular plate radius=60 nm, centered initial crack length=60 nm), set material properties (Young’s modulus, Poisson’s ratio, etc., including concentration-dependent elastic constants), generate a finite element mesh with refinement near the crack, initialize fields (c=c0, phi=1 with a smooth crack degradation), and set simulation parameters (time step Δt=0.0025 s, solver settings).
- Evidence: `/app/outputs/mesh_info.txt`

### Step 2: Coupled chemo-mechanical-fracture simulation
- Role: process
- Action: Solve the coupled PDEs (mechanical equilibrium, Li mass conservation, fracture evolution) using the finite element method for both the isotropic and hybrid hybrid phase field models. Advance the solution in time from t=0 to t=6 s with Δt=0.0025 s, and at each output time step record the crack length for both models.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 3: Crack length post-processing
- Role: scored (load-bearing)
- Action: From the simulation results, extract the crack length (distance between crack faces derived from the fracture field φ) as a function of time for both isotropic and hybrid models. Output a CSV file with columns: time (s), isotropic_crack_length_nm, hybrid_crack_length_nm. Include rows starting from t=0 to t=6 s at a sufficiently fine output interval, ensuring at least t=0 and t=6 s are present.
- Output file: `/app/outputs/step_01_crack_lengths.csv`
- Format: csv
- Contract: time (s) column header, isotropic_crack_length_nm (float) column header, hybrid_crack_length_nm (float) column header; one row per output time step including t=0 and t=6s
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_crack_lengths.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_crack_lengths.csv
- path: `/app/outputs/step_01_crack_lengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Crack length evolution from t=0 to t=6 s for the baseline case. The checker will verify that at t=6 s, hybrid_crack_length_nm < isotropic_crack_length_nm (ordering), and compare the reported isotropic and hybrid crack lengths at t=6 s against hidden paper-derived reference values with an appropriate tolerance.
- schema:
  - `type`: table
  - `required_columns`: `time`, `isotropic_crack_length_nm`, `hybrid_crack_length_nm`
  - `units`:
    - `time`: s
    - `isotropic_crack_length_nm`: nm
    - `hybrid_crack_length_nm`: nm

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_crack_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "time",
          "isotropic_crack_length_nm",
          "hybrid_crack_length_nm"
        ],
        "units": {
          "time": "s",
          "isotropic_crack_length_nm": "nm",
          "hybrid_crack_length_nm": "nm"
        }
      },
      "description": "Crack length evolution from t=0 to t=6 s for the baseline case. The checker will verify that at t=6 s, hybrid_crack_length_nm < isotropic_crack_length_nm (ordering), and compare the reported isotropic and hybrid crack lengths at t=6 s against hidden paper-derived reference values with an appropriate tolerance."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads `step_01_crack_lengths.csv`. It first validates that the file exists, has the required three columns with the correct names, and contains rows for t = 0 s and t = 6 s. It then examines the crack length values at t = 6 s for the isotropic and hybrid models. The verifier compares the reported values against hidden reference values obtained from a rigorous implementation of the described models and also checks the relative relationship (ordering) between the two crack lengths. Full credit requires that the quantitative relationship between the isotropic and hybrid crack lengths matches the expected physical behavior and that the absolute values lie within an acceptable tolerance of the reference. Partial credit may be awarded if the ordering is correct but the values deviate. Structural checks (file existence, column format) carry a small weight. The final reward is a weighted sum of these checks, reported as a float in [0,1].
