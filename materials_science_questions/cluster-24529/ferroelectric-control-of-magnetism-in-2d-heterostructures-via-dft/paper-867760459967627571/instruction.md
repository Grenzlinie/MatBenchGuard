# Spin accumulation and torque in topological insulator heterostructures via spin diffusion

## Problem background
In topological insulator (TI)-based heterostructures, the helical spin texture of the topological surface states can generate a non-equilibrium spin accumulation when a current flows. When the TI is interfaced with a ferromagnetic metal (TI/FM) or a magnetically doped TI (TI/mdTI), this spin accumulation diffuses into the adjacent layer and exerts a torque on the magnetization through exchange coupling. Understanding the spatial profile of the spin density, the resulting integrated torque, and its efficiency is crucial for spintronic applications. This task computes these quantities within a spin-diffusion framework for both bilayer geometries under specified physical parameters.

## Approach
We model the steady-state itinerant spin density in the ferromagnetic layer using a diffusion equation that includes spin precession around the magnetization, transverse spin decoherence, and spin relaxation. In the TI/FM case, the boundary conditions are: the spin density at the TI interface is fixed to the TI surface spin polarization (taken as a reference amplitude S0), and the spin current vanishes at the outer boundary. The transverse spin density obeys a closed-form solution involving hyperbolic functions that depend on the distance from the interface and the characteristic lengths (spin diffusion length, spin precession length, and spin decoherence length). The integrated torque is obtained from the spatial change of the spin current plus spin relaxation; it can be expressed analytically in terms of these lengths. A spin-torque efficiency is then defined by normalizing the torque per unit charge current, requiring the Fermi velocity and diffusion coefficient. For the TI/mdTI bilayer, the structure hosts two topological surface states on opposite outer surfaces, each injecting a spin density. The diffusion equation is solved in a two‑layer geometry (TI and mdTI) with continuity of spin density and spin current at the internal interface. The integrated torque is computed by summing contributions over both layers after finding the piecewise spin-density profile. All calculations are performed for given sets of length‑scale parameters, layer thicknesses, and spin‑source amplitudes.

## Reproduction target
The task is to carry out the following computations and save the results as CSV files:

1. **TI/FM spin accumulation profile**: For a TI/FM bilayer with in‑plane magnetization, compute the transverse spin density components (S⊥ and S_z) as functions of the distance z from the interface, at 100 evenly spaced points between 0 and the FM thickness d=8 nm. Parameters: λ_sf=5 nm, λ_φ=1 nm, λ_J=1 nm, S0=1. Output columns: z (nm), S⊥ (arb. units), S_z (arb. units).

2. **TI/FM integrated torque vs FM thickness**: Compute the in‑plane and out‑of‑plane integrated torque components T⊥ and T_z for the same bilayer as a function of FM thickness d, scanning d from 0.5 nm to 20 nm in steps of 0.5 nm. Use S0=1 and the same λ parameters. Output columns: d (nm), T⊥ (arb. units), T_z (arb. units).

3. **TI/FM spin‑torque efficiency**: For the TI/FM bilayer, compute the dimensionless efficiency components θ⊥ and θ_z using the additional parameters v_F = 5×10⁵ m/s and diffusion coefficient D = 5 cm²/s. Output a single row with columns theta⊥ and theta_z.

4. **TI/mdTI bilayer torque vs TI thickness**: For a two‑layer structure (TI of thickness d₁ followed by a magnetically doped TI (mdTI) of thickness d₂=6 nm), assume topological surface states at the two outer surfaces with opposite spin sources (S₁ = −S₂ = 1 arb. units). Use continuity of spin density and spin current at the interface. Parameters: λ_sf=5 nm, λ_φ=1 nm, λ_J=1 nm. Compute the integrated torque components T⊥ and T_z for d₁ from 0 nm to 10 nm in steps of 0.1 nm. Output columns: d₁ (nm), T⊥ (arb. units), T_z (arb. units).

5. **TI/mdTI torque vs spin‑source ratio**: Fix d₁=3 nm and d₂=6 nm. Vary the spin‑source magnitude ratio r = |S₁|/|S₂| from 0.1 to 1.9 in steps of 0.1, keeping |S₁|+|S₂|=2. For each ratio, solve the same two‑layer setup and compute the integrated torque components. Output columns: ratio (dimensionless), T⊥ (arb. units), T_z (arb. units).

## Assets

- Python scientific computing stack: numpy scipy matplotlib

## Workflow steps

### Step 1: TI/FM spin accumulation profile
- Role: scored
- Action: For a TI/FM bilayer with in-plane magnetization, solve the steady-state spin diffusion equation for the transverse spin density using the analytic closed-form solution (hyperbolic-cosine form) with boundary conditions: spin density at the interface S(0) aligned with the TI surface spin (set S0=1) and no spin current at the outer boundary z=d. Use parameters: spin diffusion length λ_sf = 5 nm, transverse spin decoherence length λ_φ = 1 nm, spin precession length λ_J = 1 nm, and FM thickness d = 8 nm. Compute S_perp(z) = Re(Š(z)) and S_z(z) = -Im(Š(z)) at 100 evenly spaced points from z=0 to z=d. Save results as a CSV table.
- Output file: `/app/outputs/step_01_spin_density_profile.csv`
- Format: csv
- Contract: Columns: z (nm), S_perp (arb. units), S_z (arb. units). One row per spatial point.
- Scoring: scored by hidden verifier

### Step 2: TI/FM integrated torque vs FM thickness
- Role: scored
- Action: Using the analytic expression for the integrated torque derived from the spin-diffusion solution (in the large-d limit or general form), compute the in-plane torque T_perp and out-of-plane torque T_z for a TI/FM bilayer. Use S0=1 and the same λ parameters as step_01. Evaluate for FM thickness d ranging from 0.5 nm to 20 nm in steps of 0.5 nm. Save results as a CSV table.
- Output file: `/app/outputs/step_02_torque_vs_d.csv`
- Format: csv
- Contract: Columns: d (nm), T_perp (arb. units), T_z (arb. units). One row per thickness value.
- Scoring: scored by hidden verifier

### Step 3: TI/FM spin-torque efficiency
- Role: scored
- Action: Compute the dimensionless spin-torque efficiency components θ_perp (in-plane) and θ_z (out-of-plane) for the TI/FM bilayer using the analytic expression involving the diffusion coefficient, Fermi velocity, and the length scales. Use v_F = 5×10^5 m/s, diffusion coefficient D = 5 cm^2/s, and the same λ parameters as before. Output a single-row CSV table with the two values.
- Output file: `/app/outputs/step_03_torque_efficiency.csv`
- Format: csv
- Contract: Columns: theta_perp (dimensionless), theta_z (dimensionless). Single row of data.
- Scoring: scored by hidden verifier

### Step 4: TI/mdTI bilayer torque vs TI thickness
- Role: scored (load-bearing)
- Action: Solve the spin-diffusion equation for a two-layer structure consisting of a TI of thickness d1 followed by a magnetically doped TI (mdTI) of thickness d2 = 6 nm. At the two outer surfaces, spin sources S1 and S2 with opposite sign (S1 = -S2 = 1 arb. units) are injected. Use continuity of spin density and spin current at the internal interface. Take λ_sf = 5 nm, λ_φ = 1 nm, λ_J = 1 nm. Compute the total integrated torque components T_perp and T_z for d1 ranging from 0 to 10 nm in steps of 0.1 nm. Save results as a CSV table.
- Output file: `/app/outputs/step_04_TI_mdTI_torque_d1.csv`
- Format: csv
- Contract: Columns: d1 (nm), T_perp (arb. units), T_z (arb. units). One row per d1 value.
- Scoring: scored by hidden verifier

### Step 5: TI/mdTI torque vs spin-source ratio
- Role: scored
- Action: For fixed layer thicknesses d1 = 3 nm and d2 = 6 nm, vary the spin-source magnitude ratio r = |S1|/|S2| from 0.1 to 1.9 in steps of 0.1, while keeping |S1|+|S2| = 2. For each ratio, solve the same two-layer spin-diffusion setup as in step_04 and compute the integrated torque components T_perp and T_z. Save results as a CSV table.
- Output file: `/app/outputs/step_05_TI_mdTI_torque_ratio.csv`
- Format: csv
- Contract: Columns: ratio (dimensionless), T_perp (arb. units), T_z (arb. units). One row per ratio value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_spin_density_profile.csv`
- `/app/outputs/step_02_torque_vs_d.csv`
- `/app/outputs/step_03_torque_efficiency.csv`
- `/app/outputs/step_04_TI_mdTI_torque_d1.csv`
- `/app/outputs/step_05_TI_mdTI_torque_ratio.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_spin_density_profile.csv
- path: `/app/outputs/step_01_spin_density_profile.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Spatial profile of transverse spin density in a TI/FM bilayer.
- schema:
  - `type`: table
  - `required_columns`: `z`, `S_perp`, `S_z`
  - `units`:
    - `z`: nm
    - `S_perp`: arb. units
    - `S_z`: arb. units

### step_02_torque_vs_d.csv
- path: `/app/outputs/step_02_torque_vs_d.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Integrated torque vs FM thickness for TI/FM.
- schema:
  - `type`: table
  - `required_columns`: `d`, `T_perp`, `T_z`
  - `units`:
    - `d`: nm
    - `T_perp`: arb. units
    - `T_z`: arb. units

### step_03_torque_efficiency.csv
- path: `/app/outputs/step_03_torque_efficiency.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Spin-torque efficiencies for TI/FM bilayer.
- schema:
  - `type`: table
  - `required_columns`: `theta_perp`, `theta_z`
  - `units`:
    - `theta_perp`: dimensionless
    - `theta_z`: dimensionless

### step_04_TI_mdTI_torque_d1.csv
- path: `/app/outputs/step_04_TI_mdTI_torque_d1.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Integrated torque vs TI thickness for TI/mdTI bilayer.
- schema:
  - `type`: table
  - `required_columns`: `d1`, `T_perp`, `T_z`
  - `units`:
    - `d1`: nm
    - `T_perp`: arb. units
    - `T_z`: arb. units

### step_05_TI_mdTI_torque_ratio.csv
- path: `/app/outputs/step_05_TI_mdTI_torque_ratio.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Integrated torque vs spin-source ratio for TI/mdTI bilayer.
- schema:
  - `type`: table
  - `required_columns`: `ratio`, `T_perp`, `T_z`
  - `units`:
    - `ratio`: dimensionless
    - `T_perp`: arb. units
    - `T_z`: arb. units

Notes: All outputs are CSV tables. The checker will recompute the expected quantities from the same analytic expressions using the same parameters, then compare using appropriate tolerances per scoring tier.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_spin_density_profile.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "z",
          "S_perp",
          "S_z"
        ],
        "units": {
          "z": "nm",
          "S_perp": "arb. units",
          "S_z": "arb. units"
        }
      },
      "description": "Spatial profile of transverse spin density in a TI/FM bilayer."
    },
    {
      "file": "step_02_torque_vs_d.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "d",
          "T_perp",
          "T_z"
        ],
        "units": {
          "d": "nm",
          "T_perp": "arb. units",
          "T_z": "arb. units"
        }
      },
      "description": "Integrated torque vs FM thickness for TI/FM."
    },
    {
      "file": "step_03_torque_efficiency.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta_perp",
          "theta_z"
        ],
        "units": {
          "theta_perp": "dimensionless",
          "theta_z": "dimensionless"
        }
      },
      "description": "Spin-torque efficiencies for TI/FM bilayer."
    },
    {
      "file": "step_04_TI_mdTI_torque_d1.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "d1",
          "T_perp",
          "T_z"
        ],
        "units": {
          "d1": "nm",
          "T_perp": "arb. units",
          "T_z": "arb. units"
        }
      },
      "description": "Integrated torque vs TI thickness for TI/mdTI bilayer."
    },
    {
      "file": "step_05_TI_mdTI_torque_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "ratio",
          "T_perp",
          "T_z"
        ],
        "units": {
          "ratio": "dimensionless",
          "T_perp": "arb. units",
          "T_z": "arb. units"
        }
      },
      "description": "Integrated torque vs spin-source ratio for TI/mdTI bilayer."
    }
  ],
  "notes": "All outputs are CSV tables. The checker will recompute the expected quantities from the same analytic expressions using the same parameters, then compare using appropriate tolerances per scoring tier."
}
```

## How you are scored
Each of the five CSV artifacts will be examined by a hidden verifier. The verifier independently recomputes the expected numerical values using the same analytic expressions and parameters as specified in the workflow. For every artifact, the verifier compares your computed quantities (the columns containing S⊥, S_z, T⊥, T_z, θ⊥, θ_z) to the recomputed reference values. The individual stage scores reflect how closely your output matches the reference, with the main torque‑efficiency stage carrying the highest weight. The final reward is a weighted sum of these scores, scaled to the range [0,1]. Reporting a number without performing the required computations is insufficient; only artifacts that derive from the correct physical model and parameters will receive full credit.
