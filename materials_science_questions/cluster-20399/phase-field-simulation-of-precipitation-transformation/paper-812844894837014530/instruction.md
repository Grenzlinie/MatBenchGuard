# Static precipitate chemo-mechanical benchmark: concentration profiles and scaling with coupling strength

## Problem background
In solid‑state alloys, the elastic stiffness of a material can depend on the local composition. This chemo‑mechanical coupling alters diffusion and equilibrium concentration profiles around precipitates. The benchmark problem studies a static spherical precipitate embedded in a matrix with composition‑dependent elasticity. Phase‑field simulations solve the coupled diffusion‑mechanics problem, and the numerical results are compared against an analytical perturbative solution. The goal is to validate the coupled solver implementations and to quantify how the deviation from the analytical profile scales with the strength of the chemo‑mechanical coupling.

## Approach
Use a phase‑field code (OpenPhase or DAMASK) to simulate a frozen δ′ precipitate in an Al–Li matrix. The elastic constants follow a linear composition dependence: C(c) = C₀ (1 + ϰ Δc). Two coupling strengths, ϰ = 0.01 at.%⁻¹ and ϰ = 0.04 at.%⁻¹, are investigated. For each, set up a 3D periodic simulation box with given grid, time step, temperature, and material parameters (elastic constants, misfit strain). Freeze the precipitate by disabling interface kinetics and, for OpenPhase, collapsing the diffuse interface width. Solve mechanical equilibrium and diffusion together until steady state. Extract the radial Li concentration profile in the matrix. Independently compute the analytical reference profile from the known formula c_ref(r) = c₀ − g₀ ϰ (R/r)⁶, where g₀ depends on the matrix shear modulus, molar volume, temperature, and a material constant that must be derived from the Eshelby solution. Finally, compute the L²‑norm relative deviation ζ = ||c_ref − c_num||₂ / ||c_ref||₂ for each coupling and log the chosen solver.

## Reproduction target
Run static chemo‑mechanical coupling simulations for ϰ = 0.01 at.%⁻¹ and ϰ = 0.04 at.%⁻¹ using either OpenPhase or DAMASK. Output the equilibrium radial concentration profiles as comma‑separated files. For each coupling, compute the L²‑norm relative deviation ζ between the numerical profile and the analytical reference profile c_ref(r) = c₀ − g₀ ϰ (R/r)⁶. Report both ζ values and the solver identity in a summary JSON file.

## Assets

- OpenPhase: http://www.openphase.de/
- DAMASK: https://damask.mpie.de/

## Workflow steps

### Step 1: Setup benchmark configuration
- Role: process
- Action: Define simulation parameters: domain 64³ grid cells, grid spacing dx=3 nm, time step dt=1 s, temperature T=473 K. Set material parameters: matrix elastic constants C11=107.11 GPa, C12=62.86 GPa, C44=28.47 GPa; precipitate elastic constants C11=139.8 GPa, C12=33.7 GPa, C44=40.8 GPa; volumetric misfit strain -0.975%. For coupling factor ϰ=0.01 at.%⁻¹ set initial precipitate radius=19.03 dx and matrix Li concentration=7.021 at.%; for ϰ=0.04 at.%⁻¹ set radius=17.71 dx and concentration=7.440 at.%. Configure composition-dependent elasticity as C^{ijkl}(c)=C₀^{ijkl}(1+ϰΔc) with Δc=c−c_ref. Freeze the precipitate by setting interface mobility L=0; for OpenPhase reduce diffuse interface width to one grid cell. Compute analytical solution parameters: matrix shear modulus Gₘ = C44 (assume isotropic), molar volume Vₘ = 1e-5 m³, and material constant b from the isotropic Eshelby relation using precipitate bulk modulus B_p and misfit strain. Log all numerical and analytical parameters.
- Evidence: `/app/outputs/setup_log.txt`

### Step 2: Equilibrium concentration profile for κ=0.01
- Role: scored (load-bearing)
- Action: Using either OpenPhase or DAMASK, run a coupled diffusion–mechanical equilibrium simulation for κ=0.01 at.%⁻¹ until steady state (zero net flux). Extract the radial Li concentration profile c(r) along a line from the precipitate center outward, covering the matrix region outside the precipitate. Save the profile as comma-separated values.
- Output file: `/app/outputs/concentration_profile_varkappa_0.01.csv`
- Format: csv
- Contract: CSV with header row and two columns: r (distance from precipitate center, in nm), c (Li concentration, in at.%).
- Scoring: scored by hidden verifier

### Step 3: Equilibrium concentration profile for κ=0.04
- Role: scored (load-bearing)
- Action: Using the same solver as in s1, run a coupled diffusion–mechanical equilibrium simulation for κ=0.04 at.%⁻¹ until steady state. Extract the radial Li concentration profile c(r) and save as comma-separated values.
- Output file: `/app/outputs/concentration_profile_varkappa_0.04.csv`
- Format: csv
- Contract: CSV with header row and two columns: r (distance from precipitate center, in nm), c (Li concentration, in at.%).
- Scoring: scored by hidden verifier

### Step 4: Compute L²-norm deviations
- Role: scored
- Action: From the numerical concentration profiles, compute the analytical reference profile c_ref(r) = c₀ − g₀ κ (R/r)⁶, where g₀ = 6 Gₘ Vₘ b² / (R T) using the shear modulus Gₘ, molar volume Vₘ, temperature T, and material constant b determined in s0. For each coupling strength, evaluate the L²-norm relative deviation ζ = ||c_ref − c_num||₂ / ||c_ref||₂. Write a summary JSON containing the solver identity and the two computed ζ values.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: JSON object with keys: solver (string, either 'OpenPhase' or 'DAMASK'), L2_0.01 (float, L² deviation for κ=0.01), L2_0.04 (float, L² deviation for κ=0.04), unit (string, value 'dimensionless').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/concentration_profile_varkappa_0.01.csv`
- `/app/outputs/concentration_profile_varkappa_0.04.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### concentration_profile_varkappa_0.01.csv
- path: `/app/outputs/concentration_profile_varkappa_0.01.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Agent-compared radial concentration profile at equilibrium for κ=0.01 at.%⁻¹. Checker recomputes L² deviation from this raw artifact.
- schema:
  - `type`: table
  - `required_columns`: `r`, `c`
  - `units`:
    - `r`: nm
    - `c`: at.%

### concentration_profile_varkappa_0.04.csv
- path: `/app/outputs/concentration_profile_varkappa_0.04.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Agent-compared radial concentration profile at equilibrium for κ=0.04 at.%⁻¹. Checker recomputes L² deviation from this raw artifact.
- schema:
  - `type`: table
  - `required_columns`: `r`, `c`
  - `units`:
    - `r`: nm
    - `c`: at.%

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Agent-reported solver identity and its computed L² deviations. Checker verifies solver consistency and may cross-check with its own recomputed values.
- schema:
  - `type`: object
  - `required`:
    - `solver`: string ('OpenPhase' or 'DAMASK')
    - `L2_0.01`: float
    - `L2_0.04`: float
    - `unit`: string ('dimensionless')

Notes: The checker recomputes L²-norm deviations from the submitted CSV profiles using the analytical solution with material parameters as defined in the paper. The summary.json provides the solver name needed to select the appropriate paper-reported tolerance. Agent L² values in summary.json are not trusted directly; reward comes from recomputed deviations from the raw CSVs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "concentration_profile_varkappa_0.01.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "c"
        ],
        "units": {
          "r": "nm",
          "c": "at.%"
        }
      },
      "description": "Agent-compared radial concentration profile at equilibrium for κ=0.01 at.%⁻¹. Checker recomputes L² deviation from this raw artifact."
    },
    {
      "file": "concentration_profile_varkappa_0.04.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "c"
        ],
        "units": {
          "r": "nm",
          "c": "at.%"
        }
      },
      "description": "Agent-compared radial concentration profile at equilibrium for κ=0.04 at.%⁻¹. Checker recomputes L² deviation from this raw artifact."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "solver": "string ('OpenPhase' or 'DAMASK')",
          "L2_0.01": "float",
          "L2_0.04": "float",
          "unit": "string ('dimensionless')"
        }
      },
      "description": "Agent-reported solver identity and its computed L² deviations. Checker verifies solver consistency and may cross-check with its own recomputed values."
    }
  ],
  "notes": "The checker recomputes L²-norm deviations from the submitted CSV profiles using the analytical solution with material parameters as defined in the paper. The summary.json provides the solver name needed to select the appropriate paper-reported tolerance. Agent L² values in summary.json are not trusted directly; reward comes from recomputed deviations from the raw CSVs."
}
```

## How you are scored
A hidden verifier reads the submitted concentration profile CSVs and independently recomputes the L²‑norm relative deviation ζ for each coupling. It uses the analytical solution with the material parameters you logged in the setup step and compares the recomputed deviations to known reference tolerances that are specific to the solver you declared. Your score is determined by these recomputed deviations, not by the ζ values you write in summary.json. Each coupling contributes equally to the total reward. The profile quality and solver consistency are also checked. Reporting the paper’s numbers is not enough; you must actually run the simulations and produce the raw data.
