# Classical Nucleation Theory Wilson Point Computation

## Problem background
In high-speed flows of condensing vapour, such as steam expanding through nozzles or turbomachinery, homogeneous nucleation generates vast numbers of tiny droplets in a very short distance. The point of maximum subcooling, the Wilson point, determines the total droplet number, typical sizes, and downstream wetness fraction. Accurately predicting conditions at the Wilson point is essential for two-phase flow calculations but remains challenging because direct numerical integration of the nucleation and growth equations for many droplet groups is computationally demanding. An analytical model that captures the essential physics would be immensely useful, provided it reliably computes the maximum subcooling and derived properties from the local expansion rate and fluid thermodynamic state.

## Approach
The analytical model is based on classical nucleation theory and simplified droplet growth in the free-molecule regime. The model uses a locally parabolic subcooling profile around the Wilson point, with the nucleation time scale defined by the curvature of subcooling. Key fluid properties—surface tension, densities, latent heat, specific heats—are obtained from standard steam property correlations (IAPWS-IF97). By combining the energy equation, Clausius-Clapeyron relation, and approximated wetness growth expressions, an implicit algebraic equation for the Wilson-point subcooling emerges. Solving this equation for a given constant expansion rate yields the maximum subcooling ΔT_W. From ΔT_W, the nucleation time, droplet number, mass-mean and Sauter-mean radii, and wetness fraction are computed via additional algebraic formulas. The procedure is then repeated for a range of expansion rates to map out the dependency of subcooling on expansion rate.

## Reproduction target
Compute, for water vapour expanding from dry saturated conditions at a Wilson-point pressure of 0.1 bar and a constant expansion rate k_p = 1000 s⁻¹, the following Wilson-point properties: maximum subcooling ΔT_W, droplet number N_W, mass-mean radius r_30, Sauter mean radius r_32, and wetness fraction Y_W. Also compute ΔT_W for a logarithmically spaced set of constant expansion rates (100 to 1×10⁶ s⁻¹) at the same Wilson-point pressure, to establish how subcooling depends on expansion rate.

## Assets

- iapws: https://pypi.tuna.tsinghua.edu.cn/simple
- numpy: https://pypi.tuna.tsinghua.edu.cn/simple
- scipy: https://pypi.tuna.tsinghua.edu.cn/simple

## Workflow steps

### Step 1: Compute Wilson-point properties at fixed conditions
- Role: scored (load-bearing)
- Action: Implement the analytical model (parameters γ_s, L, Θ, I_0, C_r, T_c from steam property correlations) and solve the implicit equation for the maximum subcooling ΔT_W at a Wilson-point pressure of 0.1 bar and a constant expansion rate k_p = 1000 s⁻¹. From ΔT_W compute the nucleation time τ_n, droplet number N_W, mass-mean radius r_30, Sauter mean radius r_32, and wetness fraction Y_W using the derived formulas.
- Output file: `/app/outputs/wilson_point_properties.csv`
- Format: csv
- Contract: Columns: variable (string), analytical_value (float), unit (string). Rows for ΔT_W (K), N_W (1/(s·kg)), r_30 (nm), r_32 (nm), Y_W (dimensionless fraction).
- Scoring: scored by hidden verifier

### Step 2: Compute maximum subcooling vs expansion rate
- Role: scored (load-bearing)
- Action: Using the implemented analytical model, compute the maximum subcooling ΔT_W for a range of constant expansion rates k_p (logarithmically spaced from 100 to 1e6 s⁻¹) at a fixed Wilson-point pressure of 0.1 bar.
- Output file: `/app/outputs/delta_T_vs_kp.csv`
- Format: csv
- Contract: Columns: k_p (1/s) (float), delta_T_W (K) (float). At least 10 logarithmically spaced values from 100 to 1e6 s⁻¹.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/wilson_point_properties.csv`
- `/app/outputs/delta_T_vs_kp.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### wilson_point_properties.csv
- path: `/app/outputs/wilson_point_properties.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Wilson-point properties computed from the analytical solution at p_W = 0.1 bar, k_p = 1000 s⁻¹.
- schema:
  - `type`: table
  - `required_columns`: `variable`, `analytical_value`, `unit`
  - `units`:
    - `analytical_value`: various (K, 1/(s·kg), nm, dimensionless)

### delta_T_vs_kp.csv
- path: `/app/outputs/delta_T_vs_kp.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Maximum subcooling as a function of expansion rate at p_W = 0.1 bar, with a monotonic increase.
- schema:
  - `type`: table
  - `required_columns`: `k_p`, `delta_T_W`
  - `units`:
    - `k_p`: 1/s
    - `delta_T_W`: K

Notes: All properties are derived from the analytical model. Numerical integration for validation is not part of the scored reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "wilson_point_properties.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "variable",
          "analytical_value",
          "unit"
        ],
        "units": {
          "analytical_value": "various (K, 1/(s·kg), nm, dimensionless)"
        }
      },
      "description": "Wilson-point properties computed from the analytical solution at p_W = 0.1 bar, k_p = 1000 s⁻¹."
    },
    {
      "file": "delta_T_vs_kp.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_p",
          "delta_T_W"
        ],
        "units": {
          "k_p": "1/s",
          "delta_T_W": "K"
        }
      },
      "description": "Maximum subcooling as a function of expansion rate at p_W = 0.1 bar, with a monotonic increase."
    }
  ],
  "notes": "All properties are derived from the analytical model. Numerical integration for validation is not part of the scored reproduction."
}
```

## How you are scored
Your output consists of two CSV files. A hidden verifier will independently extract the values from `wilson_point_properties.csv` and `delta_T_vs_kp.csv` and compare them against reference data (derived from standard implementations and theory). The comparison checks both the numerical values and the expected monotonic trend of increasing subcooling with expansion rate. Each file contributes a weighted fraction to your final score (roughly 60% for the single-condition properties, 40% for the sweep). The verifier does not simply check file existence or format; it verifies the correctness of the computed quantities.
