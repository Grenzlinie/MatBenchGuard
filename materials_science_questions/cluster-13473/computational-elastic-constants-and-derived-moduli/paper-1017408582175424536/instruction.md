# Chirality, flow alignment, and elastic constants in three-dimensional active nematic turbulence simulations

## Problem background
Active nematic fluids are far-from-equilibrium materials composed of anisotropic building blocks that exhibit chaotic spatiotemporal dynamics known as active turbulence. In three dimensions, the interplay between topological defect lines and the flow field determines macroscopic properties, and understanding how material parameters—elastic constants, anisotropic viscosity, and intrinsic chirality—influence the defect density and flow velocity is essential for guiding experimental design and controlling active materials. This task uses a continuum model (the Beris-Edwards approach for active nematodynamics) and a hybrid finite-difference / lattice-Boltzmann solver to investigate the effect of weak chirality on the time-averaged defect density and root-mean-square velocity in bulk three-dimensional active nematic turbulence.

## Approach
The simulation solves the coupled dynamics of a Q-tensor order parameter and an incompressible velocity field. The Q-tensor evolution is advanced with a finite-difference scheme, while the Navier–Stokes equations are solved using a D3Q19 lattice-Boltzmann method on a periodic cubic grid. The system is governed by a single elastic constant (L₁ = L, L₂ = L₃ = 0), a fixed activity (ζ = 0.2 L/(Δx)²), and a flow-aligning parameter χ = 0.2. Two simulations are performed: an achiral reference case (inverse pitch q₀ = 0) and a weakly chiral case (q₀ = 2π/(200Δx), corresponding to pitch P₀ = 200Δx). Once each run reaches a dynamic steady state, the instantaneous defect density (computed as the volume fraction where the scalar order parameter S < 0.4, then converted to a length per unit volume) and the volume-averaged mean-square velocity are recorded over time. From these time series, steady-state portions are identified and used to compute time-averaged means and standard deviations.

## Reproduction target
The objective is to produce a single JSON file containing the time-averaged mean defect density and root-mean-square velocity (derived from the volume-averaged mean-square velocity) for both the achiral (q₀ = 0) and weakly chiral (q₀ = 2π/(200Δx)) conditions. Specifically, the output must report, for each condition, the mean defect density (in units of 1/Δx), its standard deviation, the root-mean-square velocity (nondimensional), and its standard deviation. The results must be computed from the simulated steady-state dynamics using the solver implemented according to the given material and simulation parameters.

## Assets

- Hybrid LBM/FD solver for active nematodynamics

## Workflow steps

### Step 1: Develop or adapt hybrid LBM/FD solver
- Role: process
- Action: Implement a numerical solver for the Beris–Edwards Q‑tensor evolution (finite difference) and incompressible Navier–Stokes equations (D3Q19 lattice‑Boltzmann) with periodic boundary conditions on a cubic grid, using the material and simulation parameters provided in the problem background (e.g., A, B, C, L1=L, L2=0, L3=0, χ=0.2, Γ, η=1.38/Γ, Δx=1.5 χ_n, Δt=0.025 (Δx)²/(LΓ), domain size 201×201×201).
- Evidence: none

### Step 2: Run achiral active turbulence simulation
- Role: process
- Action: Run the solver with q₀=0 (no chirality) and activity ζ=0.2 L/(Δx)² until a dynamic steady state is reached. At regular intervals record the instantaneous defect density (fraction of volume with S<0.4, converted to length per unit volume) and the volume-averaged mean-square velocity ⟨v²⟩_V.
- Evidence: none

### Step 3: Run weakly chiral active turbulence simulation
- Role: process
- Action: Run the solver with inverse chiral pitch q₀=2π/(200Δx) (pitch P₀=200Δx) and activity ζ=0.2 L/(Δx)² until a dynamic steady state. Record the instantaneous defect density and volume-averaged mean-square velocity as in step_02.
- Evidence: none

### Step 4: Compute time-averaged observables and write results
- Role: scored (load-bearing)
- Action: From the recorded time series for both simulations, identify the steady-state portions (excluding initial transients), compute the time-averaged mean defect density (in units of 1/Δx) and its standard deviation, the root-mean-square velocity (√⟨v²⟩_V, nondimensional) and its standard deviation. Package the results as a JSON file named simulation_results.json.
- Output file: `/app/outputs/simulation_results.json`
- Format: json
- Contract: A JSON object with key 'results' whose value is an array of two objects. Each object has keys: 'pitch' (string, either 'achiral' or 'P0=200'), 'defect_density_mean' (float, units of 1/Δx), 'defect_density_std' (float), 'rms_velocity_mean' (float, nondimensional), 'rms_velocity_std' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/simulation_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### simulation_results.json
- path: `/app/outputs/simulation_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Time-averaged defect density and RMS velocity for the achiral (q₀=0) and weakly chiral (q₀=2π/(200Δx)) conditions.
- schema:
  - `type`: object
  - `required`: `results`
  - `properties`:
    - `results`:
      - `type`: array
      - `minItems`: 2
      - `maxItems`: 2
      - `items`:
        - `type`: object
        - `required`: `pitch`, `defect_density_mean`, `defect_density_std`, `rms_velocity_mean`, `rms_velocity_std`
        - `properties`:
          - `pitch`:
            - `type`: string
            - `enum`: `achiral`, `P0=200`
          - `defect_density_mean`:
            - `type`: number
            - `description`: mean defect density in units of 1/Δx
          - `defect_density_std`:
            - `type`: number
          - `rms_velocity_mean`:
            - `type`: number
            - `description`: root-mean-square velocity, nondimensional
          - `rms_velocity_std`:
            - `type`: number

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "simulation_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "results"
        ],
        "properties": {
          "results": {
            "type": "array",
            "minItems": 2,
            "maxItems": 2,
            "items": {
              "type": "object",
              "required": [
                "pitch",
                "defect_density_mean",
                "defect_density_std",
                "rms_velocity_mean",
                "rms_velocity_std"
              ],
              "properties": {
                "pitch": {
                  "type": "string",
                  "enum": [
                    "achiral",
                    "P0=200"
                  ]
                },
                "defect_density_mean": {
                  "type": "number",
                  "description": "mean defect density in units of 1/Δx"
                },
                "defect_density_std": {
                  "type": "number"
                },
                "rms_velocity_mean": {
                  "type": "number",
                  "description": "root-mean-square velocity, nondimensional"
                },
                "rms_velocity_std": {
                  "type": "number"
                }
              }
            }
          }
        }
      },
      "description": "Time-averaged defect density and RMS velocity for the achiral (q₀=0) and weakly chiral (q₀=2π/(200Δx)) conditions."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that reads the `simulation_results.json` file you produce. The verifier independently extracts your reported defect density and root-mean-square velocity for each pitch condition and compares them against physically correct reference values derived from the underlying physics. The reward is proportional to the number of reported quantities that match the expected values within the allowed accuracy. Simply listing numbers is not sufficient; the verifier expects the results to be consistent with a genuine numerical solution of the governing equations under the specified parameters.
