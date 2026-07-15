# Polymer Crystallization Lamellar Thickness: Extended Kinetic Model with Nonnegative Barriers

## Problem background
The Lauritzen‑Hoffman (LH) kinetic model of polymer crystallization predicts an average lamellar thickness $\bar{l}$ that diverges to infinity at a finite supercooling — the so‑called $\delta l$ catastrophe — in disagreement with experiments that show finite, monotonically decreasing thickness at high undercooling. The central question is whether imposing the physically reasonable constraint that free‑energy barriers must always be nonnegative removes this divergence, yielding finite $\bar{l}$ at every temperature.

The task is to re‑implement the extended model, compute the average lamellar thickness $\bar{l}$ as a function of temperature for two contrasting cases (the original LH model and the extended model with non‑negative barriers), and compare the resulting behaviour. All required material constants are provided; only numerical integration code needs to be written.

## Approach
The extended model modifies the rate constants of the LH theory so that the free‑energy barriers for stem formation and destruction never become negative. This introduces an apportionment parameter $\gamma$ (analogous to the LH parameter $\psi$) and, for the simplified case where the fold‑surface energy $\sigma_e'$ is zero and $\theta = \gamma$, the average lamellar thickness $\bar{l}(T)$ is obtained by numerically integrating the crystallisation rate $S(l,T)$ over all allowed stem lengths.

We compare three model variants:
- **Original LH model** with $\psi = 1/2$ and $\hat\psi = \psi$, which exhibits the $\delta l$ catastrophe (divergence near 365 K).
- **Extended model with $\gamma = 0$** (no apportionment, all barriers non‑negative).
- **Extended model with $\gamma = 1/2$**.

For each variant, the integration of the appropriate $S(l,T)$ expression (using the variable transformations that map the infinite interval to a finite domain) is performed with an open‑source integration routine (e.g., `scipy.integrate.quad`) in place of the proprietary IMSL DQDAGS subroutine originally used. The material constants are: $a = b = 5\times10^{-8}\,\text{cm}$, $\sigma = 10\,\text{erg/cm}^2$, $\sigma_e = 100\,\text{erg/cm}^2$, $T_m^\circ = 500\,\text{K}$, $\Delta h = 3\times10^9\,\text{erg/cm}^3$, with $\Delta f = (T_m^\circ - T)\Delta h / T_m^\circ$. The temperature ranges are from 485 K down to 365 K for the LH model and from 485 K down to 235 K for both extended model cases, stepping by 5 K.

## Reproduction target
Produce three CSV files containing the average lamellar thickness $\bar{l}$ (in Ångströms) as a function of temperature:

1. **Original LH model ($\psi = 1/2$)**: `lh_psi_half_l_values.csv` with columns `temperature_K` and `l_Angstrom`. Temperatures: 485.0, 480.0, …, 365.0 K. At 365 K the theoretical thickness diverges; output either a very large number ($>10^6$) or the string `inf` to indicate the catastrophe.

2. **Extended model ($\gamma = 0$, $\sigma_e' = 0$)**: `extended_gamma0_l_values.csv` with columns `temperature_K` and `l_Angstrom`. Temperatures: 485.0, 480.0, …, 235.0 K.

3. **Extended model ($\gamma = 1/2$, $\sigma_e' = 0$)**: `extended_gamma_half_l_values.csv` with columns `temperature_K` and `l_Angstrom`. Temperatures: 485.0, 480.0, …, 235.0 K.

All models use the same material constants listed above. The extended‑model cases use the integrand $S_{\text{I}}$ for $\Delta f \le 2\sigma/a$ and $S_{\text{II}}$ for $\Delta f > 2\sigma/a$ with $\sigma_e' = 0$, applying the variable transformations described in the steps. The LH model uses the $S^{(\mathrm{LH})}$ integrand with $\psi = \hat\psi = 0.5$ and its own variable transformation.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Original LH model lamellar thickness (ψ=0.5)
- Role: scored
- Action: Implement the numerical integration of the original Lauritzen‑Hoffman model (S^{LH} integrand) using apportionment parameters ψ=0.5 and ψ̂=ψ. Use the material constants a=b=5×10⁻⁸ cm, σ=10 erg/cm², σ_e=100 erg/cm², T_m°=500 K, Δh=3×10⁹ erg/cm³, and Δf = (T_m°−T)Δh/T_m°. Apply the variable transformation and integration method described in the paper for the LH model. Compute the average lamellar thickness l̄(T) for temperatures from 485 K down to 365 K (5 K decrements). For each temperature, compute l̄ and write a row with temperature_K and l_Angstrom to the CSV. At T=365 K the theoretical value diverges; output either a very large float (>1e6) or the string 'inf' to indicate divergence.
- Output file: `/app/outputs/lh_psi_half_l_values.csv`
- Format: csv
- Contract: Columns: temperature_K (float), l_Angstrom (float or string 'inf'). Rows for temperatures: 485.0, 480.0, ..., 365.0 K.
- Scoring: scored by hidden verifier

### Step 2: Extended model lamellar thickness (γ=0, σ_e'=0)
- Role: scored (load-bearing)
- Action: Implement the numerical integration of the extended LH model (nonnegative barrier constraint) for the case σ_e'=0, θ=γ, and apportionment parameter γ=0. Use the same material constants. Apply the appropriate integrand case (S_I or S_II) and variable transformations from the paper for categories (1) and (3) when σ_e'=0. Compute l̄(T) for temperatures from 485 K down to 235 K (5 K decrements). Write results to the CSV with columns temperature_K and l_Angstrom.
- Output file: `/app/outputs/extended_gamma0_l_values.csv`
- Format: csv
- Contract: Columns: temperature_K (float), l_Angstrom (float). Rows for temperatures: 485.0, 480.0, ..., 235.0 K.
- Scoring: scored by hidden verifier

### Step 3: Extended model lamellar thickness (γ=1/2, σ_e'=0)
- Role: scored
- Action: Implement the numerical integration of the extended LH model with γ=1/2, σ_e'=0, and θ=γ. Use the same material constants and integration methods as step02. Compute l̄(T) for temperatures from 485 K down to 235 K (5 K decrements). Write results to the CSV with columns temperature_K and l_Angstrom.
- Output file: `/app/outputs/extended_gamma_half_l_values.csv`
- Format: csv
- Contract: Columns: temperature_K (float), l_Angstrom (float). Rows for temperatures: 485.0, 480.0, ..., 235.0 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/lh_psi_half_l_values.csv`
- `/app/outputs/extended_gamma0_l_values.csv`
- `/app/outputs/extended_gamma_half_l_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### lh_psi_half_l_values.csv
- path: `/app/outputs/lh_psi_half_l_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average lamellar thickness vs temperature for the original LH model with ψ=1/2. At 365 K the thickness diverges; the agent may report 'inf' or a very large float.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `l_Angstrom`
  - `units`:
    - `temperature_K`: K
    - `l_Angstrom`: Angstrom (float; string 'inf' accepted for divergence at 365 K)

### extended_gamma0_l_values.csv
- path: `/app/outputs/extended_gamma0_l_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average lamellar thickness vs temperature for the extended model with γ=0 and σ_e'=0. All values remain finite.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `l_Angstrom`
  - `units`:
    - `temperature_K`: K
    - `l_Angstrom`: Angstrom (float)

### extended_gamma_half_l_values.csv
- path: `/app/outputs/extended_gamma_half_l_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Average lamellar thickness vs temperature for the extended model with γ=1/2 and σ_e'=0. All values remain finite.
- schema:
  - `type`: table
  - `required_columns`: `temperature_K`, `l_Angstrom`
  - `units`:
    - `temperature_K`: K
    - `l_Angstrom`: Angstrom (float)

Notes: The hidden gold values are the paper's reported Table I (γ=0, γ=1/2) and Table II (ψ=1/2). The verifier will compare the submitted l_Angstrom values to these references with appropriate tolerances. The original LH model at 365 K is expected to diverge; any reported value >1e6 or the string 'inf' will be accepted as indicating the catastrophe.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "lh_psi_half_l_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "l_Angstrom"
        ],
        "units": {
          "temperature_K": "K",
          "l_Angstrom": "Angstrom (float; string 'inf' accepted for divergence at 365 K)"
        }
      },
      "description": "Average lamellar thickness vs temperature for the original LH model with ψ=1/2. At 365 K the thickness diverges; the agent may report 'inf' or a very large float."
    },
    {
      "file": "extended_gamma0_l_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "l_Angstrom"
        ],
        "units": {
          "temperature_K": "K",
          "l_Angstrom": "Angstrom (float)"
        }
      },
      "description": "Average lamellar thickness vs temperature for the extended model with γ=0 and σ_e'=0. All values remain finite."
    },
    {
      "file": "extended_gamma_half_l_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "temperature_K",
          "l_Angstrom"
        ],
        "units": {
          "temperature_K": "K",
          "l_Angstrom": "Angstrom (float)"
        }
      },
      "description": "Average lamellar thickness vs temperature for the extended model with γ=1/2 and σ_e'=0. All values remain finite."
    }
  ],
  "notes": "The hidden gold values are the paper's reported Table I (γ=0, γ=1/2) and Table II (ψ=1/2). The verifier will compare the submitted l_Angstrom values to these references with appropriate tolerances. The original LH model at 365 K is expected to diverge; any reported value >1e6 or the string 'inf' will be accepted as indicating the catastrophe."
}
```

## How you are scored
Each of the three CSV files is scored independently by a hidden verifier that compares the submitted `l_Angstrom` values to a set of reference (gold) values derived from the original work. The verifier applies a tolerance that accounts for legitimate differences caused by the integration routine and floating‑point implementation. For the LH model at 365 K, the verifier checks that the reported thickness correctly indicates divergence (extremely large or flagged).

The three scores are combined with predetermined weights to produce a single reward in $[0,1]$. Simply guessing plausible numbers is not sufficient; the reward reflects how well the numerical integration reproduces the expected temperature dependence. The exact tolerances, reference values, and the divergence criterion are hidden from the solver.
