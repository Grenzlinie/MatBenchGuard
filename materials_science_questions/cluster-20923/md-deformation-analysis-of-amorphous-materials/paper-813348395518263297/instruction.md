# Energy model for amorphization in fcc nanowires under uniaxial tension

## Problem background
Some crystalline nanowires under tensile load can deform by nanoscale amorphization (NA), where a region of the crystal transforms directly into an amorphous phase. This process is driven by a spatially inhomogeneous multiplane shear (SIMS) and becomes barrier-free above a critical shear stress τc. An analytical energy model has been proposed that predicts τc as a function of nanowire width and material properties, and it was found to agree with molecular dynamics simulations for fcc Ni and Si nanowires. Here, you will implement that energy model and compute the critical shear stress τc for both a homogeneous (Ni) and a band‑like (Si) amorphization scenario.

## Approach
The energy change per sheared plane, ΔW, is built from several contributions: the energy of the sheared interior region (modelled via the generalized stacking fault curve γ_GSF(s)), the work done by the applied shear stress τ, the energy of free surface steps, and, for the band‑like case, an extra term from crystal–glass interfaces. The generalized stacking fault energy is a piecewise cosine function of the shear displacement s, reaching a maximum γ_m and a minimum γ_0. The critical stress τc is defined as the lowest τ for which ∂(ΔW)/∂s < 0 holds for every s in the interval [0, b], where b is the magnitude of a partial Burgers vector. For Ni (homogeneous amorphization) the interface term is omitted; for Si (band‑like amorphization) it is included with n shear planes. You must implement these energy expressions and a numerical root‑finding routine that, for a given nanowire width L (related to the nominal width L' by L = L'·√2), determines τc by scanning τ until the barrier‑free condition is met. All required material constants (lattice parameters, surface energies, stacking fault energies, excess energies, and enhancement factors) are given in the workflow steps.

## Reproduction target
Compute the critical shear stress τc for two material cases:

- Homogeneous amorphization in Ni, with λ = 0.6.
- Band‑like amorphization in Si, with n = 5 and λ = 0.1.

For each case, compute τc at five nominal nanowire widths: L' = 5, 10, 15, 20, 25 nm.  The sheared region length L is obtained from L' as L = L'·√2 and should be used inside the energy model. Output the results as two CSV files:

- `/app/outputs/ni_tau_c_vs_L.csv`
- `/app/outputs/si_tau_c_vs_L.csv`

Each file must contain two columns: `L_nm` (nanowire width in nm) and `tau_c_GPa` (critical shear stress in GPa), with one row per L' value.  Use exactly the material parameters provided in the workflow steps; they describe the lattice parameter, Burgers vector, stacking fault energies, surface energy, amorphous excess energy, crystal‑glass interface energy, and the enhancement factors.

## Assets

- Python 3
- NumPy
- SciPy

## Workflow steps

### Step 1: Implement energy model and define parameters
- Role: process
- Action: Implement the complete energy change function ΔW(s,τ,L) for homogeneous amorphization (Ni case) and band-like amorphization (Si case) using the generalized stacking fault energy γ_GSF(s) (piecewise cosine function) and the expressions for W_interior, W_AC−BD, A, and W_step as described in the paper. Set all material constants exactly as specified: for Ni: a=0.35 nm, b=0.14 nm, γ_m=0.17 J/m², γ_0=0.12 J/m², γ_s=0.12 J/m², λ=0.6, W_A=G/65 with G=76 GPa; for Si: a=0.54 nm, b=0.22 nm, γ_m=1.67 J/m², γ_0=0.075 J/m², γ_s=1.5 J/m², W_A=8.13e8 J/m³, W_cr-glass=0.23 J/m², n=5, λ=0.1. Also implement a routine that, for a given nanowire width L (where L = L'·√2), finds the critical shear stress τc: the lowest stress τ such that ∂(ΔW)/∂s < 0 for all s in [0, b]. (The derivative can be evaluated numerically; the agent may use any reliable numerical method.)
- Evidence: none

### Step 2: Compute critical shear stress for Ni nanowire (homogeneous)
- Role: scored (load-bearing)
- Action: Using the implemented homogeneous amorphization model (Ni), compute the critical shear stress τc for nanowire widths L' = [5, 10, 15, 20, 25] nm (the nanowire width L' relates to the sheared region length by L = L'·√2). For each L', find the lowest τ such that ∂(ΔW)/∂s < 0 for all s in [0,b]. Output the results as a CSV file.
- Output file: `/app/outputs/ni_tau_c_vs_L.csv`
- Format: csv
- Contract: Two columns: L_nm (float, nanowire width in nm) and tau_c_GPa (float, critical shear stress in GPa). One row per L' value.
- Scoring: scored by hidden verifier

### Step 3: Compute critical shear stress for Si nanowire (inhomogeneous)
- Role: scored (load-bearing)
- Action: Using the implemented band-like amorphization model (Si) with n=5 and λ=0.1, compute the critical shear stress τc for the same nanowire widths L' = [5, 10, 15, 20, 25] nm. For each L', find the lowest τ such that ∂(ΔW)/∂s < 0 for all s in [0,b]. Output the results as a CSV file.
- Output file: `/app/outputs/si_tau_c_vs_L.csv`
- Format: csv
- Contract: Two columns: L_nm (float, nanowire width in nm) and tau_c_GPa (float, critical shear stress in GPa). One row per L' value.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/ni_tau_c_vs_L.csv`
- `/app/outputs/si_tau_c_vs_L.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### ni_tau_c_vs_L.csv
- path: `/app/outputs/ni_tau_c_vs_L.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Critical shear stress for homogeneous amorphization in Ni nanowires as a function of nanowire width.
- schema:
  - `type`: table
  - `required_columns`: `L_nm`, `tau_c_GPa`
  - `units`:
    - `L_nm`: nm
    - `tau_c_GPa`: GPa

### si_tau_c_vs_L.csv
- path: `/app/outputs/si_tau_c_vs_L.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Critical shear stress for band-like amorphization in Si nanowires as a function of nanowire width.
- schema:
  - `type`: table
  - `required_columns`: `L_nm`, `tau_c_GPa`
  - `units`:
    - `L_nm`: nm
    - `tau_c_GPa`: GPa

Notes: The checker will independently implement the same energy model with identical parameters and recompute τc for each L'. The agent's reported τc values must match within a tolerance that accounts for numerical solver differences. The load-bearing design ensures the agent must actually run the model and cannot guess the τc values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "ni_tau_c_vs_L.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "L_nm",
          "tau_c_GPa"
        ],
        "units": {
          "L_nm": "nm",
          "tau_c_GPa": "GPa"
        }
      },
      "description": "Critical shear stress for homogeneous amorphization in Ni nanowires as a function of nanowire width."
    },
    {
      "file": "si_tau_c_vs_L.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "L_nm",
          "tau_c_GPa"
        ],
        "units": {
          "L_nm": "nm",
          "tau_c_GPa": "GPa"
        }
      },
      "description": "Critical shear stress for band-like amorphization in Si nanowires as a function of nanowire width."
    }
  ],
  "notes": "The checker will independently implement the same energy model with identical parameters and recompute τc for each L'. The agent's reported τc values must match within a tolerance that accounts for numerical solver differences. The load-bearing design ensures the agent must actually run the model and cannot guess the τc values."
}
```

## How you are scored
A hidden verifier will independently implement the same energy model with the identical material parameters, recompute τc for each L' value, and compare your submitted `tau_c_GPa` values to its own reference.  Each scored output file is evaluated separately; the per‑stage reward is based on how closely your computed critical stresses agree with the verifier’s recomputed values, within an appropriate tolerance that accounts for legitimate numerical differences.  The final reward is the weighted sum of the per‑stage rewards.  To earn full credit you must correctly implement the underlying physics described in the approach and workflow; merely copying numbers from any external source will not pass because the reference is computed afresh by the verifier and is not available to you.
