# Chemo-Mechanical Stress and Fracture in Battery Particles

## Problem background
Silicon-based anodes in lithium-ion batteries can store a very high amount of lithium, but the insertion process causes enormous volumetric expansion (up to ~270%). This expansion induces mechanical stresses that can lead to cracking, capacity fade, and eventual failure. Experiments commonly observe a sharp reaction front separating unlithiated silicon from lithiated silicon, suggesting that the initial lithiation is reaction‑limited, not diffusion‑limited. Understanding how stress develops during two‑phase lithiation, why the reaction can stop before consuming the whole particle (self‑limiting), and how particle size influences crack driving forces is crucial for designing durable nanostructured silicon electrodes. A phase‑field model that couples reaction kinetics, large inelastic deformation, and elasticity can capture these phenomena. The task is to implement such a model and compute the stress levels, the self‑limiting core sizes, and the energy release rates for surface cracks, thereby providing insight into the conditions that avoid or lead to fracture.

## Approach
The key idea is a phase‑field model for a reaction‑limited, two‑phase lithiation process. A continuous scalar phase field φ distinguishes the pristine silicon (φ=0) from the fully lithiated product (φ=1), with a thin, diffuse interface representing the reaction front. The model uses a double‑well free energy and a gradient energy to maintain a well‑defined interface of characteristic thickness, and an electrochemical driving force to promote lithiation. Large deformation is accounted for through a multiplicative decomposition of the deformation gradient into an inelastic part (caused by reaction) and an elastic part. The inelastic deformation consists of a volumetric expansion coupled to φ and a deviatoric component that evolves according to a kinetic law: the local stress deviator biases the reaction direction, relaxing shape stress while leaving the reaction rate unaffected to first order. The model is rendered dimensionless, and the resulting coupled system — a phase‑field evolution equation, mechanical equilibrium, and ordinary differential equations for the deviatoric inelastic variables — is solved numerically using an open‑source finite‑element framework. The numerical experiments span three configurations: 1D lithiation of a biaxially constrained thin film, axisymmetric lithiation of a spherical particle, and fracture analysis on a spherical particle with a pre‑existing surface crack.

## Reproduction target
Produce the following five CSV files from the implemented model (see Workflow steps for exact schemas):

1. **thin_film_stress_alpha.csv** – dimensionless biaxial compressive stress in a constrained thin film, normalized by the lithiated‑phase Young’s modulus, for at least ten values of the kinetic parameter α spanning 0.01 to 1.
2. **spherical_lithiation_evolution.csv** – time series (dimensionless time τ) of the Si core radius and outer radius (both normalized by the interface length l0) during lithiation of a spherical particle with initial radius R = 35 l0, using a constant electrochemical driving force and parameters calibrated for Li₃.₇₅Si (volumetric strain θ = 2.7, composition‑dependent modulus). Provide at least 50 time points that capture the transient and approach to equilibrium.
3. **equilibrium_core_radius.csv** – for at least five particle sizes R/l0 in the range 10–50, the equilibrium (final) core radius fraction rce/R.
4. **energy_release_rate.csv** – for a spherical particle of initial radius R = 30 l0, after lithiating to three states (core radius ratios rc/R = 0.2, 0.5, 0.8), introduce a surface crack of depth a/R and compute the normalized energy release rate G/(l0·Y0) by evaluating the change in elastic energy with crack area. Vary a/R from near 0 to at least 0.5, yielding at least 10 points per lithiation state.
5. **gmax_vs_R.csv** – for at least five particle sizes R/l0 (e.g., 10, 15, 20, 30, 40, 50), the maximum normalized energy release rate (peak of the G vs a/R curve) extracted from the fracture analysis.

## Assets

- Open-source finite-element framework with multiphysics capability (e.g., FEniCS, deal.II, MOOSE): https://fenicsproject.org/

## Workflow steps

### Step 1: Implement the phase-field finite-deformation lithiation model
- Role: process
- Action: Implement the dimensionless phase-field finite-deformation model for reaction-limited two-phase lithiation of silicon in an open-source finite-element framework (e.g., FEniCS). The implementation must include the phase-field evolution equation, mechanical equilibrium, and the ordinary differential equations for the internal deviatoric inelastic deformation variables, using the material parameters and boundary conditions described in the task. This step produces the working finite-element code that all subsequent scored simulations depend on.
- Evidence: `/app/outputs/model_implementation.log`

### Step 2: Thin-film biaxial stress vs kinetic parameter α
- Role: scored (load-bearing)
- Action: Using the implemented model, simulate 1D lithiation of a biaxially constrained thin Si film for at least ten different values of the kinetic parameter α in the range 0.01–1. For each α, after the reaction front has passed, record the dimensionless biaxial compressive stress normalized by Young's modulus in the lithiated phase. Write the pairs (α, normalized stress) to the output CSV.
- Output file: `/app/outputs/thin_film_stress_alpha.csv`
- Format: csv
- Contract: Two columns: alpha (float), sigma_film (float). sigma_film is the dimensionless biaxial compressive stress (positive for compression) normalized by the reference Young's modulus.
- Scoring: scored by hidden verifier

### Step 3: Spherical particle lithiation evolution
- Role: scored (load-bearing)
- Action: Simulate axisymmetric lithiation of a spherical Si particle of initial radius R=35*l0 under constant electrochemical driving force, using the calibrated parameters (α=0.2, volumetric strain θ=2.7 for Li₃.₇₅Si, composition-dependent Young's modulus, etc.). Track the dimensionless time τ, the current Si core radius r_c/l0, and the outer radius r_s/l0 from the start until the core radius nears an equilibrium. Write at least 50 time-series points to the output CSV.
- Output file: `/app/outputs/spherical_lithiation_evolution.csv`
- Format: csv
- Contract: Three columns: dimensionless_time (float), rc (float, current Si core radius normalized by l0), rs (float, outer radius normalized by l0).
- Scoring: scored by hidden verifier

### Step 4: Equilibrium core radius vs particle size
- Role: scored (load-bearing)
- Action: For each particle size R/l0 in the set {10, 15, 20, 30, 40, 50}, run the spherical lithiation simulation to equilibrium and record the equilibrium core radius r_ce/l0. Compute the normalized ratio r_ce/R. Write the pairs (R_over_l0, rce_over_R) to the output CSV.
- Output file: `/app/outputs/equilibrium_core_radius.csv`
- Format: csv
- Contract: Two columns: R_over_l0 (float), rce_over_R (float).
- Scoring: scored by hidden verifier

### Step 5: Energy release rate for surface cracks in a lithiated spherical particle
- Role: scored (load-bearing)
- Action: For a spherical particle of initial radius R=30*l0, simulate lithiation to three states: r_c/R = 0.2, 0.5, 0.8. At each state, introduce a surface crack of depth a/R and compute the energy release rate G by evaluating the change in elastic energy with respect to crack area. Vary a/R from near 0 to at least 0.5, producing at least 10 points per lithiation state. Write the crack depth a/R, lithiation state r_c/R, and normalized energy release rate G/(l0*Y0) to the output CSV.
- Output file: `/app/outputs/energy_release_rate.csv`
- Format: csv
- Contract: Three columns: a_over_R (float), rc_over_R (float, lithiation state indicator), G_normalized (float).
- Scoring: scored by hidden verifier

### Step 6: Maximum energy release rate vs particle size
- Role: scored (load-bearing)
- Action: Repeat the fracture analysis for several particle radii R/l0 (e.g., 10, 15, 20, 30, 40, 50). For each size, determine the maximum energy release rate G_max (peak of the G vs a/R curve at full lithiation). Write the pairs (R_over_l0, G_max_normalized) to the output CSV.
- Output file: `/app/outputs/gmax_vs_R.csv`
- Format: csv
- Contract: Two columns: R_over_l0 (float), G_max_normalized (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/thin_film_stress_alpha.csv`
- `/app/outputs/spherical_lithiation_evolution.csv`
- `/app/outputs/equilibrium_core_radius.csv`
- `/app/outputs/energy_release_rate.csv`
- `/app/outputs/gmax_vs_R.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### thin_film_stress_alpha.csv
- path: `/app/outputs/thin_film_stress_alpha.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Biaxial compressive stress in a constrained thin film as a function of the kinetic parameter α. The checker verifies the monotonic decreasing trend and spot-checks the value at α=0.2 against a hidden reference.
- schema:
  - `type`: table
  - `required_columns`: `alpha`, `sigma_film`
  - `units`:
    - `alpha`: dimensionless
    - `sigma_film`: dimensionless (compressive stress normalized by Young's modulus)

### spherical_lithiation_evolution.csv
- path: `/app/outputs/spherical_lithiation_evolution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Time evolution of core and outer radii during lithiation of a spherical particle (R=35*l0). The checker verifies that rc decreases and converges, and rs increases.
- schema:
  - `type`: table
  - `required_columns`: `dimensionless_time`, `rc`, `rs`
  - `units`:
    - `dimensionless_time`: τ
    - `rc`: core radius normalized by l0
    - `rs`: outer radius normalized by l0

### equilibrium_core_radius.csv
- path: `/app/outputs/equilibrium_core_radius.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium core radius as a function of particle size. The checker verifies monotonic increase of rce_over_R with R_over_l0 and compares values to a hidden reference curve.
- schema:
  - `type`: table
  - `required_columns`: `R_over_l0`, `rce_over_R`
  - `units`:
    - `R_over_l0`: dimensionless particle size
    - `rce_over_R`: equilibrium core radius fraction

### energy_release_rate.csv
- path: `/app/outputs/energy_release_rate.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Energy release rate for surface cracks as a function of crack depth at multiple lithiation states (rc/R=0.2,0.5,0.8). The checker verifies that each curve has a single maximum and the peak shifts to larger a/R with deeper lithiation.
- schema:
  - `type`: table
  - `required_columns`: `a_over_R`, `rc_over_R`, `G_normalized`
  - `units`:
    - `a_over_R`: crack depth ratio
    - `rc_over_R`: lithiation state (core radius ratio)
    - `G_normalized`: dimensionless energy release rate G/(l0*Y0)

### gmax_vs_R.csv
- path: `/app/outputs/gmax_vs_R.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum energy release rate as a function of particle size. The checker verifies that G_max_normalized decreases with R_over_l0 and determines the critical size where G_max crosses the hidden fracture energy Γ.
- schema:
  - `type`: table
  - `required_columns`: `R_over_l0`, `G_max_normalized`
  - `units`:
    - `R_over_l0`: dimensionless particle radius
    - `G_max_normalized`: dimensionless maximum energy release rate

Notes: All outputs are dimensionless and use the length scale l0 and reference Young's modulus Y0. The checker compares reported values to hidden gold digitized from the source work's figures, with tolerances that account for numerical simulation variability. Structural checks (monotonicity, peak existence) supplement the numeric comparison.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "thin_film_stress_alpha.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha",
          "sigma_film"
        ],
        "units": {
          "alpha": "dimensionless",
          "sigma_film": "dimensionless (compressive stress normalized by Young's modulus)"
        }
      },
      "description": "Biaxial compressive stress in a constrained thin film as a function of the kinetic parameter α. The checker verifies the monotonic decreasing trend and spot-checks the value at α=0.2 against a hidden reference."
    },
    {
      "file": "spherical_lithiation_evolution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "dimensionless_time",
          "rc",
          "rs"
        ],
        "units": {
          "dimensionless_time": "τ",
          "rc": "core radius normalized by l0",
          "rs": "outer radius normalized by l0"
        }
      },
      "description": "Time evolution of core and outer radii during lithiation of a spherical particle (R=35*l0). The checker verifies that rc decreases and converges, and rs increases."
    },
    {
      "file": "equilibrium_core_radius.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R_over_l0",
          "rce_over_R"
        ],
        "units": {
          "R_over_l0": "dimensionless particle size",
          "rce_over_R": "equilibrium core radius fraction"
        }
      },
      "description": "Equilibrium core radius as a function of particle size. The checker verifies monotonic increase of rce_over_R with R_over_l0 and compares values to a hidden reference curve."
    },
    {
      "file": "energy_release_rate.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "a_over_R",
          "rc_over_R",
          "G_normalized"
        ],
        "units": {
          "a_over_R": "crack depth ratio",
          "rc_over_R": "lithiation state (core radius ratio)",
          "G_normalized": "dimensionless energy release rate G/(l0*Y0)"
        }
      },
      "description": "Energy release rate for surface cracks as a function of crack depth at multiple lithiation states (rc/R=0.2,0.5,0.8). The checker verifies that each curve has a single maximum and the peak shifts to larger a/R with deeper lithiation."
    },
    {
      "file": "gmax_vs_R.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R_over_l0",
          "G_max_normalized"
        ],
        "units": {
          "R_over_l0": "dimensionless particle radius",
          "G_max_normalized": "dimensionless maximum energy release rate"
        }
      },
      "description": "Maximum energy release rate as a function of particle size. The checker verifies that G_max_normalized decreases with R_over_l0 and determines the critical size where G_max crosses the hidden fracture energy Γ."
    }
  ],
  "notes": "All outputs are dimensionless and use the length scale l0 and reference Young's modulus Y0. The checker compares reported values to hidden gold digitized from the source work's figures, with tolerances that account for numerical simulation variability. Structural checks (monotonicity, peak existence) supplement the numeric comparison."
}
```

## How you are scored
Your artifacts will be evaluated by a hidden verifier that does not re‑run any simulations. It reads your CSV files and compares the reported quantities against reference data (derived from independent validation) using tolerances that account for reasonable numerical variation between different finite‑element implementations. In addition, the verifier checks structural properties of the results, such as monotonic trends, the existence of a single maximum, and the relative ordering of curves. Each of the five scored outputs contributes a weighted share to a total score in [0, 1]; the primary targets (stress‑α curve, lithiation evolution, fracture energy curves) carry the largest weights. A solution that merely copies a fixed set of numbers without running the model will not match the structural checks and will receive a low score. The goal is to demonstrate that your implementation of the coupled phase‑field model produces physically consistent, numerically converged results that respect the theory described in the approach.
