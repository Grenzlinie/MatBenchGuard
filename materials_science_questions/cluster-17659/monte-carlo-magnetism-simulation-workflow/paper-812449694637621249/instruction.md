# Self-Gravitating Gas Equation of State via Monte Carlo and Mean Field Methods

## Problem background
The self-gravitating gas is a system of particles interacting solely through Newtonian gravity. Unlike ordinary gases with short-range forces, the long-range attractive potential prevents a conventional thermodynamic limit and can cause the system to collapse. When the gas is confined in a container, its macroscopic behaviour is described by a dimensionless parameter that combines particle number, temperature, gravitational strength, and container size. The key quantity of interest is the equation of state, i.e. the pressure in units of NT/V, and the identification of phase transitions where the gas collapses into a dense object. This task requires computing this equation of state as a function of the governing parameter using Monte Carlo simulations and a mean field analysis, and locating the collapse points in different thermodynamic ensembles.

## Approach
We use Monte Carlo simulations to sample configurations of N=2000 particles in a cubic box of unit side length with Newtonian gravitational interactions and a short-distance cutoff a=10^{-6}. In the canonical ensemble, the Metropolis algorithm uses the acceptance weight exp(η u), where u is the dimensionless potential energy and η = Gm^2 N/(L T) is the natural intensive variable. The equation of state f(η)=pV/(NT) and the energy fluctuations (ΔU)^2 are computed from the sampled configurations. In the microcanonical ensemble, a different Metropolis weight enforces fixed total energy, giving access to the equation of state in the collapsed branch and the specific heat. Additionally, under the assumption of spherical symmetry a mean field treatment reduces the problem to solving a single first-order nonlinear ODE for f_MF(η^R), which can be integrated numerically from the initial condition f_MF(0)=1. The resulting curves and the critical points where f_MF=1/3 or the pressure/temperature change discontinuously provide a complete description of the gas behaviour.

## Reproduction target
Reproduce the equation of state f(η) for the self-gravitating gas from canonical and microcanonical Monte Carlo simulations, and solve the mean field ODE. Specifically:
- From canonical MC simulations for η between 0 and 2 (at least 20 points), obtain f(η), the potential energy fluctuation (ΔU)^2, and locate the collapse point η_T where the pressure becomes negative.
- From microcanonical MC simulations over a corresponding range of ξ, obtain f(η), specific heat cV, and locate the collapse point η_MC where temperature and pressure jump.
- From the mean field ODE, compute f_MF(η^R) for η^R ∈ [0, 2.6] and find η_C^R where f_MF = 1/3.
- Output three JSON files with the structures specified in the workflow steps.

## Assets
No external data or pre-trained models are required. All parameters (N=2000, unit cube, cutoff a=10^{-6}, potential forms) and the ODE are fully described. The solving agent may use standard Python scientific libraries (e.g., NumPy, SciPy) and any open-source Metropolis implementation; no proprietary software is needed.

## Workflow steps

### Step 1: Canonical Monte Carlo simulation
- Role: scored (load-bearing)
- Action: Implement the Metropolis algorithm for N=2000 particles in a unit cube with Newtonian gravity and short-distance cutoff a=10^{-6} using weight exp(η u). Run simulations for η from 0 to 2 (at least 20 points) and compute the equation of state f(η)=pV/(NT), the potential energy fluctuation (ΔU)^2, and locate the collapse transition point η_T where pressure becomes negative.
- Output file: `/app/outputs/ce_mc_results.json`
- Format: json
- Contract: {"eta_values": [float], "f_values": [float], "deltaU_sq_values": [float], "eta_T": float}
- Scoring: scored by hidden verifier

### Step 2: Microcanonical Monte Carlo simulation
- Role: scored
- Action: Implement the Metropolis algorithm for the microcanonical ensemble using weight [ξ + u/N]^{3N/2-1} θ(ξ + u/N) with N=2000 particles in a unit cube and same cutoff. For a set of ξ values mapping to approximately the same η range as the canonical run, compute f(η) and specific heat cV. Identify the microcanonical collapse point η_MC where temperature and pressure jump discontinuously.
- Output file: `/app/outputs/mce_mc_results.json`
- Format: json
- Contract: {"eta_values": [float], "f_values": [float], "cV_values": [float], "eta_MC": float}
- Scoring: scored by hidden verifier

### Step 3: Mean field equation of state
- Role: scored
- Action: Solve the first-order nonlinear ODE for the spherical-symmetry mean field: η^R (3 f_MF - 1) f_MF' + (3 f_MF - 3 + η^R) f_MF = 0, with initial condition f_MF(0)=1, using numerical integration (e.g., Runge–Kutta). Compute f_MF(η^R) for η^R from 0 to at least 2.6 and locate the critical point η_C^R where f_MF = 1/3.
- Output file: `/app/outputs/mean_field_results.json`
- Format: json
- Contract: {"etaR_values": [float], "f_MF_values": [float], "etaC_R": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ce_mc_results.json`
- `/app/outputs/mce_mc_results.json`
- `/app/outputs/mean_field_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ce_mc_results.json
- path: `/app/outputs/ce_mc_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Canonical ensemble MC outputs: equation of state and identified collapse point.
- schema:
  - `type`: object
  - `required`:
    - `eta_values`: array of float
    - `f_values`: array of float
    - `deltaU_sq_values`: array of float
    - `eta_T`: float

### mce_mc_results.json
- path: `/app/outputs/mce_mc_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Microcanonical ensemble MC outputs: equation of state in the gaseous and collapsed phases and collapse point.
- schema:
  - `type`: object
  - `required`:
    - `eta_values`: array of float
    - `f_values`: array of float
    - `cV_values`: array of float
    - `eta_MC`: float

### mean_field_results.json
- path: `/app/outputs/mean_field_results.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Mean field solution: f_MF(η^R) curve and critical point η_C^R.
- schema:
  - `type`: object
  - `required`:
    - `etaR_values`: array of float
    - `f_MF_values`: array of float
    - `etaC_R`: float

Notes: The MC simulations require adequate compute resources (N=2000, multiple η/ξ points). The solver agent is expected to use external/remote compute if needed. The check will compare the reported critical points and shapes of f(η) curves against hidden paper-derived gold values with tolerances, plus an independent recomputation of the mean field ODE.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ce_mc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "eta_values": "array of float",
          "f_values": "array of float",
          "deltaU_sq_values": "array of float",
          "eta_T": "float"
        }
      },
      "description": "Canonical ensemble MC outputs: equation of state and identified collapse point."
    },
    {
      "file": "mce_mc_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "eta_values": "array of float",
          "f_values": "array of float",
          "cV_values": "array of float",
          "eta_MC": "float"
        }
      },
      "description": "Microcanonical ensemble MC outputs: equation of state in the gaseous and collapsed phases and collapse point."
    },
    {
      "file": "mean_field_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "etaR_values": "array of float",
          "f_MF_values": "array of float",
          "etaC_R": "float"
        }
      },
      "description": "Mean field solution: f_MF(η^R) curve and critical point η_C^R."
    }
  ],
  "notes": "The MC simulations require adequate compute resources (N=2000, multiple η/ξ points). The solver agent is expected to use external/remote compute if needed. The check will compare the reported critical points and shapes of f(η) curves against hidden paper-derived gold values with tolerances, plus an independent recomputation of the mean field ODE."
}
```

## How you are scored
Each output artifact is evaluated by a hidden verifier. The verifier will check that the JSON files conform to the expected schema. For the mean field step, the verifier may independently solve the ODE and compare f_MF values to the submitted curve (small RMSE expected). For the Monte Carlo steps, the verifier compares the reported critical points and the overall shape of f(η) against reference values with predefined tolerances; additionally, it may check that f(η) decreases monotonically and that the canonical collapse shows a negative pressure. The scores for the three stages are combined with weights, where the canonical MC step carries the largest weight. The reward reflects the accuracy of the computed equation of state and critical points; reporting numbers without correct underlying computations will not pass.
