# Multi-Phase-Field Simulation of Discontinuous Precipitation Growth

## Problem background
Discontinuous precipitation is a solid-state transformation in which a supersaturated mother phase decomposes into a two-phase lamellar structure at a moving grain boundary. The growth rate and lamellar spacing are controlled by solute diffusion along grain boundaries and interphase interfaces, yet a quantitative understanding of the kinetics and the validity of the local equilibrium assumption at interfaces remains challenging. This task simulates the process with a multi-phase-field model to compute the steady-state growth velocity as a function of interlamellar spacing and to probe whether chemical potential at the precipitate interface follows the classical Gibbs-Thomson relation.

## Approach
A multi-phase-field model is employed, in which three phases (mother phase, depleted α, and precipitate β) are each described by a phase field. The free energy functional couples the phase fields to a concentration field via a parabolic thermodynamics model. Three diffusion channels are included: volume diffusion, grain-boundary diffusion, and surface diffusion along each interphase boundary. Simulations are performed in a 2D half-lamella geometry with reflection boundary conditions, representing periodic lamellar arrays. By running simulations for a range of interlamellar spacings and varying the diffusivity in the α‑β interphase boundary, steady-state front velocities are extracted. Additionally, a cross-section through the α‑β interface behind the growth front is analyzed to obtain the chemical potential, interface curvature, and the Gibbs-Thomson prediction, allowing a direct test of the local equilibrium hypothesis.

## Reproduction target
The objective is to compute three scored artifacts:

1. Steady-state growth velocity versus dimensionless interlamellar spacing L/d for supersaturation Δ=0.8, with volume diffusivity D_v=10^{-6}, grain-boundary and front interphase diffusivity D_b=D_b^{α0β}=1, and rear α‑β interphase diffusivity D_b^{αβ}=10^{-3}. At least 8 spacings in the range ~50–180 should be simulated.

2. Steady-state growth velocity versus D_b^{αβ} (dimensionless) at fixed spacing L/d=81.5, with other diffusion coefficients as above, for at least 5 values of D_b^{αβ} spanning about 1×10^{-3} to 1×10^{-2}.

3. A profile across the α‑β interface at a location behind the trijunction point (e.g., halfway to the bottom boundary) from the baseline spacing case (L/d=81.5). The profile must report position x, phase field p_β, chemical potential μ, curvature κ, and the Gibbs-Thomson predicted chemical potential μ_GT = d_{αβ} κ using the known capillary length d_{αβ}.

## Assets

- Python 3: https://www.python.org/
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Run phase-field simulations for spacing series
- Role: process
- Action: Implement the multi-phase-field model for discontinuous precipitation in a 2D half-lamella geometry with reflection boundary conditions. Set supersaturation Δ=0.8, coupling strength λ̃=1, a_α=9, diffusion coefficients D_v=10^{-6}, D_b=D_b^{α0β}=1, D_b^{αβ}=10^{-3}. For a set of interlamellar spacings L/d roughly in the range 50–180 (at least 8 values), run each simulation until a steady-state front velocity is achieved. Save raw temporal data of the front position for each spacing.
- Evidence: `/app/outputs/front_positions.txt`

### Step 2: Extract steady-state velocity vs spacing
- Role: scored (load-bearing)
- Action: From the raw front trajectories produced in step_0, determine the steady-state growth velocity for each spacing (e.g., by linear regression of front position over time in the steady regime). Write a CSV file with columns: spacing (dimensionless L/d) and velocity (dimensionless V d / D_b).
- Output file: `/app/outputs/velocity_vs_spacing.csv`
- Format: csv
- Contract: Two columns: spacing (float), velocity (float). Header row recommended.
- Scoring: scored by hidden verifier

### Step 3: Run simulations for varying D_b^{αβ}
- Role: process
- Action: Using the same model implementation and parameters, fix spacing L/d=81.5, Δ=0.8, D_v=10^{-6}, D_b=D_b^{α0β}=1. Run separate simulations for several values of the interphase-boundary diffusivity D_b^{αβ} (at least 5 values, e.g., from 1×10^{-3} to 1×10^{-2}) until steady state. Save evidence of the simulation runs.
- Evidence: `/app/outputs/Db_sim_log.txt`

### Step 4: Extract velocity vs D_b^{αβ}
- Role: scored (load-bearing)
- Action: From the raw data of step_2, extract the steady-state front velocity for each D_b^{αβ} value. Write a CSV file with columns: D_b_alpha_beta (dimensionless) and velocity (dimensionless V d / D_b).
- Output file: `/app/outputs/velocity_vs_Dbαβ.csv`
- Format: csv
- Contract: Two columns: D_b_alpha_beta (float), velocity (float). Header row recommended.
- Scoring: scored by hidden verifier

### Step 5: Extract interface chemical potential and curvature profile
- Role: scored (load-bearing)
- Action: From the steady-state simulation at baseline spacing L/d=81.5 (from step_0), take a cross-section along the normal through the α‑β interface at a location behind the trijunction point (e.g., halfway between the trijunction and the bottom boundary). Compute: the phase field p_β, the chemical potential μ, the interface curvature κ derived from the phase field, and the Gibbs‑Thomson prediction μ_GT = d_{αβ} κ using the known capillary length d_{αβ}. Write a CSV file with columns: x (position along the normal), p_beta (phase field), mu (chemical potential), kappa (curvature), mu_GT (Gibbs‑Thomson value).
- Output file: `/app/outputs/interface_profile.csv`
- Format: csv
- Contract: Columns: x (float), p_beta (float), mu (float), kappa (float), mu_GT (float). Header row recommended.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/velocity_vs_spacing.csv`
- `/app/outputs/velocity_vs_Dbαβ.csv`
- `/app/outputs/interface_profile.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### velocity_vs_spacing.csv
- path: `/app/outputs/velocity_vs_spacing.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Steady‑state growth velocity as a function of lamellar spacing for Δ=0.8. The checker verifies the curve has a maximum, a steep descending branch at low spacing (fold singularity), monotonic decrease above the maximum, and velocity values within a factor of ~2 of the expected order of magnitude.
- schema:
  - `type`: table
  - `required_columns`: `spacing`, `velocity`
  - `units`:
    - `spacing`: dimensionless L/d
    - `velocity`: dimensionless V d / D_b

### velocity_vs_Dbαβ.csv
- path: `/app/outputs/velocity_vs_Dbαβ.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Steady‑state growth velocity as a function of D_b^{αβ} at fixed spacing L/d=81.5. The checker verifies that velocity decreases monotonically with increasing D_b^{αβ}.
- schema:
  - `type`: table
  - `required_columns`: `D_b_alpha_beta`, `velocity`
  - `units`:
    - `D_b_alpha_beta`: dimensionless
    - `velocity`: dimensionless V d / D_b

### interface_profile.csv
- path: `/app/outputs/interface_profile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Interface profile used to test local equilibrium. The checker recomputes μ_GT = d_{αβ} κ from the provided κ (using the known capillary length) and verifies that the chemical potential μ exhibits a dip below μ_GT in the interface region, indicating breakdown of local equilibrium.
- schema:
  - `type`: table
  - `required_columns`: `x`, `p_beta`, `mu`, `kappa`, `mu_GT`
  - `units`:
    - `x`: position along normal (in units of W or similar)
    - `p_beta`: phase field (dimensionless)
    - `mu`: chemical potential (dimensionless units consistent with paper)
    - `kappa`: curvature (1/W)
    - `mu_GT`: chemical potential (same units as mu)

Notes: The agent must implement the multi-phase-field model and run the simulations. No pre‑computed data or gold values are provided. The scored artifacts are obtained from the runs; structural trends and relative magnitudes, not exact numerical matches, are the primary scoring criteria.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "velocity_vs_spacing.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "spacing",
          "velocity"
        ],
        "units": {
          "spacing": "dimensionless L/d",
          "velocity": "dimensionless V d / D_b"
        }
      },
      "description": "Steady‑state growth velocity as a function of lamellar spacing for Δ=0.8. The checker verifies the curve has a maximum, a steep descending branch at low spacing (fold singularity), monotonic decrease above the maximum, and velocity values within a factor of ~2 of the expected order of magnitude."
    },
    {
      "file": "velocity_vs_Dbαβ.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "D_b_alpha_beta",
          "velocity"
        ],
        "units": {
          "D_b_alpha_beta": "dimensionless",
          "velocity": "dimensionless V d / D_b"
        }
      },
      "description": "Steady‑state growth velocity as a function of D_b^{αβ} at fixed spacing L/d=81.5. The checker verifies that velocity decreases monotonically with increasing D_b^{αβ}."
    },
    {
      "file": "interface_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "x",
          "p_beta",
          "mu",
          "kappa",
          "mu_GT"
        ],
        "units": {
          "x": "position along normal (in units of W or similar)",
          "p_beta": "phase field (dimensionless)",
          "mu": "chemical potential (dimensionless units consistent with paper)",
          "kappa": "curvature (1/W)",
          "mu_GT": "chemical potential (same units as mu)"
        }
      },
      "description": "Interface profile used to test local equilibrium. The checker recomputes μ_GT = d_{αβ} κ from the provided κ (using the known capillary length) and verifies that the chemical potential μ exhibits a dip below μ_GT in the interface region, indicating breakdown of local equilibrium."
    }
  ],
  "notes": "The agent must implement the multi-phase-field model and run the simulations. No pre‑computed data or gold values are provided. The scored artifacts are obtained from the runs; structural trends and relative magnitudes, not exact numerical matches, are the primary scoring criteria."
}
```

## How you are scored
Each output file is inspected by a hidden verifier that does not look for exact numerical match to any reference, but checks structural and trend properties expected from a correct physical simulation. For velocity_vs_spacing.csv, the verifier confirms the curve has a maximum, a steep descending branch at low spacing, and monotonic decrease above the maximum, while also testing that velocity values are of the correct order of magnitude. For velocity_vs_Dbαβ.csv, it checks that velocity decreases monotonically with increasing rear-interface diffusivity. For interface_profile.csv, the verifier recomputes μ_GT from the given κ and the known capillary length, then tests whether the chemical potential μ exhibits a dip below μ_GT inside the diffuse interface. The final reward is a weighted combination of the outcomes from these checks, emphasizing the physical trends and relative magnitudes rather than exact numerical values.
