# Hugoniot and Grüneisen Parameter Calculation for a Two-Component Mixture

## Problem background
When a shock wave passes through a composite material, the equilibrium state behind the front determines the material's subsequent response. Computing this state requires a thermodynamically consistent mixture model that maintains pressure and temperature equilibrium among components. This task concerns the Hugoniot compression of a two-component mixture, specifically a quartz-like material and a polyethylene-like material. From the mixture state, important derived properties are the Grüneisen parameter Γ (a measure of the thermal pressure contribution), the sound velocity c, and the ratio Γ/V. A commonly used simplification is to approximate the mixture Grüneisen parameter by a simple mass-weighted average of the component parameters. The goal is to implement the full mixture thermodynamics and compute how the true mixture Γ compares to that simple average along the Hugoniot, and to examine the behavior of Γ/V for the mixture.

## Approach
The mixture thermodynamics is built from the Gibbs free energy per unit mass, which is taken as the mass-fraction-weighted sum of the component Gibbs functions (mass fraction λ for component 2, 1-λ for component 1). From this, mixture-specific volume, compressibility, thermal expansion, and heat capacity are obtained as mass-fraction-weighted linear combinations of the corresponding component properties. Each component is described by an equation of state with: (i) constant specific heat at constant volume C_V, (ii) constant ratio b = Γ/V, and (iii) a cold compression curve of Murnaghan-type form. The component parameters for polyethylene-like (component 1) and quartz-like (component 2) are given numerically. The Hugoniot jump condition is cast as a first-order differential equation in the pressure-temperature plane, which is integrated for λ=0.5 from the initial state (ambient pressure, initial specific volume, 293 K) over a range of specific volumes. For each (V,P,T) state along the Hugoniot, the mixture Grüneisen parameter Γ_mix is computed from mixture derivatives using Γ = αV²/(βV C_P − α²V²T). The sound velocity c is obtained from c² = V²/(βV − Tα²V²/C_P). For comparison, the simple mass-weighted average Γ_avg = (1−λ)Γ₁ + λΓ₂ is also computed using the individual component Grüneisen parameters evaluated at the same P and T.

## Reproduction target
Produce a CSV file at `/app/outputs/step_02_hugoniot_results.csv` with columns V, P, T, Gamma_mixture, Gamma_simple_avg, c, Gamma_over_V. V in cc/g, P in Mb, T in K, c in km/s, Gamma_over_V in g/cc. Include at least 10 points along the Hugoniot for λ=0.5, with specific volume V decreasing from the initial value (near 0.7 cc/g for the mixture) to approximately 0.25 cc/g. The file will be evaluated by a hidden verifier that checks the structural properties of the data (e.g., relationships among the columns, consistency with mixture thermodynamics) rather than requiring an exact match to any published table.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Hugoniot Integration for λ=0.5 Mixture
- Role: process
- Action: Implement component equations of state (Eqs. 23‑26): P_i(V,T) = (1/(γ_io β_io))[(V_io/V)^γ_io − 1] + b_i C_Vi (T − T_o) with constants for polyethylene (1): b=0.3887 g/cc, C_V=1.436e-5 Mbcc/g, V_io=1.035 cc/g, γ_io=10.2, β_io=19.31 Mb^{-1}; quartz (2): b=0.7832, C_V=0.56e-5, V_io=0.378, γ_io=5.58, β_io=2.70; T_o=293 K. For each component, solve for V_i(P,T) from P_i(V_i,T)=P. Mixture properties: V = (1−λ)V1 + λV2; αV = (1−λ)α1V1 + λα2V2; βV = (1−λ)β1V1 + λβ2V2; C_P = (1−λ)C_P1 + λC_P2; where α_i = (1/V_i)(∂V_i/∂T)_P, β_i = −(1/V_i)(∂V_i/∂P)_T, C_Pi = C_Vi + α_i^2 V_i T / β_i. Integrate the Hugoniot ODE: dT/dP = [(V0 − V) − βV (P − P0) + T αV] / [2 C_P − αV (P − P0)] with V0 = 0.7065 cc/g (mixture initial specific volume), P0=0, from initial (P=0, T=293 K) using scipy.integrate, varying P or V as independent variable to cover V from ~0.7065 down to 0.25 cc/g, recording V,P,T.
- Evidence: `/app/outputs/hugoniot_trajectory.npz`

### Step 2: Compute Mixture Properties and Output CSV
- Role: scored (load-bearing)
- Action: For each (V,P,T) state from the Hugoniot trajectory, compute: the mixture Grüneisen parameter Γ (from mixture thermodynamics via Γ = αV²/(βV C_P - α²V²T) using mixture derivatives), the sound velocity c, the ratio Γ/V, and the simple mass-weighted-average Grüneisen parameter (Γ_avg = (1-λ)Γ₁ + λΓ₂ using component Γ₁ and Γ₂ obtained from the individual component equations of state). Write a CSV file with columns V, P, T, Gamma_mixture, Gamma_simple_avg, c, Gamma_over_V containing at least 10 points covering the volume range from the initial specific volume down to approximately 0.25 cc/g.
- Output file: `/app/outputs/step_02_hugoniot_results.csv`
- Format: csv
- Contract: CSV with header: V,P,T,Gamma_mixture,Gamma_simple_avg,c,Gamma_over_V. V in cc/g, P in Mb, T in K, c in km/s, Gamma_over_V in g/cc. All numeric. At least 10 rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_hugoniot_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_hugoniot_results.csv
- path: `/app/outputs/step_02_hugoniot_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: CSV of Hugoniot states and derived quantities for λ=0.5 mixture. The checker will verify that the mixture Grüneisen parameter differs from the mass-weighted average and that Γ/V is not constant across the trajectory, as claimed in the paper.
- schema:
  - `type`: table
  - `required_columns`: `V`, `P`, `T`, `Gamma_mixture`, `Gamma_simple_avg`, `c`, `Gamma_over_V`
  - `units`:
    - `V`: cc/g
    - `P`: Mb
    - `T`: K
    - `c`: km/s
    - `Gamma_over_V`: g/cc

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_hugoniot_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "V",
          "P",
          "T",
          "Gamma_mixture",
          "Gamma_simple_avg",
          "c",
          "Gamma_over_V"
        ],
        "units": {
          "V": "cc/g",
          "P": "Mb",
          "T": "K",
          "c": "km/s",
          "Gamma_over_V": "g/cc"
        }
      },
      "description": "CSV of Hugoniot states and derived quantities for λ=0.5 mixture. The checker will verify that the mixture Grüneisen parameter differs from the mass-weighted average and that Γ/V is not constant across the trajectory, as claimed in the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by a hidden verifier that runs after you. It reads your output artifacts and applies a set of physical consistency checks tailored to this mixture Hugoniot problem. The checks are derived from the thermodynamics imposed by the model (including the mixture rules and the Hugoniot relation) and do not require you to hit a specific numerical benchmark. Producing a trajectory that correctly implements the prescribed equations of state, mixture relations, and Hugoniot integration will result in a high reward. Partial implementations, unconverged integrations, or data that violate basic thermodynamic expectations will receive lower scores. The final reward is a number between 0 and 1, combining the scores of all scored artifacts.
