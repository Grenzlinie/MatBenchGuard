# Compute critical-isotherm pressures for a nonanalytic benzene EOS

## Problem background
Accurate equations of state (EOS) for benzene are essential in chemical engineering for calculating thermodynamic properties over wide ranges of temperature and pressure. This work develops a highly constrained, nonanalytic EOS that captures the negative curvature of high-density isochores and is anchored to the liquid–vapor coexistence boundary. A particularly sensitive test of such an EOS is its behaviour along the critical isotherm — the pressure as a function of density at the critical temperature must remain well-behaved, with no negative slopes. This task reproduces the EOS calculation along that critical isotherm, providing a stringent check of the model’s consistency in the critical region.

## Approach
The EOS is isochoric and depends on the liquid–vapor coexistence boundary. You will implement three ancillary equations that define that boundary — a vapour‑pressure equation, an orthobaric (saturated) liquid density equation, and a saturated vapour compressibility‑factor equation — all using the coefficients and critical constants supplied in this document. You will also implement the core nonanalytic EOS itself, including its density‑ and temperature‑dependent terms and the associated temperature‑dependent functions.  

For each reduced density σ = ρ / ρ_c in the given list, you will first find the corresponding coexistence temperature T_σ(ρ) by solving the appropriate orthobaric density branch: the liquid branch for σ > 1, the vapour branch for σ < 1, and a fixed value T_σ = T_c at σ = 1. From that temperature you will compute the vapour pressure P_σ at coexistence, and finally evaluate the full EOS pressure P(ρ, T_c) using the nonanalytic EOS. The calculations involve solving one non‑linear equation per density and evaluating formula combinations with double‑precision arithmetic.

## Reproduction target
Write a script that:  
1. Implements the vapour‑pressure equation, the orthobaric density equations, and the nonanalytic EOS given in this instruction, using all provided coefficients and parameters.  
2. For each of the reduced densities 0.50, 0.70, 0.90, 1.00, 1.10, 1.30, 1.50, computes the pressure in bar on the critical isotherm T = T_c.  
3. Writes a CSV file `critical_isotherm_pressures.csv` with columns `reduced_density` and `P_bar`, containing exactly one row per specified reduced density (order is free).

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute critical-isotherm pressures
- Role: scored (load-bearing)
- Action: Implement the vapor‑pressure equation (Eq. 2) with its coefficients, the orthobaric liquid density equation (Eq. 3) and the saturated vapor compressibility‑factor equation (Eq. 4) for the coexistence boundary, and the nonanalytic EOS (Eq. 6) with its supporting functions (6a‑6h) and least‑squares coefficients. For each reduced density (ρ/ρ_c) in the list 0.50, 0.70, 0.90, 1.00, 1.10, 1.30, 1.50, compute the coexistence temperature T_σ(ρ) by iterating the appropriate orthobaric density branch (liquid for σ > 1, vapor for σ < 1; at σ = 1, T_σ = T_c), then compute the vapor pressure P_σ at that temperature, and finally compute the EOS pressure P(ρ, T_c) using Eq. (6). Write a CSV file with columns reduced_density and P_bar.
- Output file: `/app/outputs/critical_isotherm_pressures.csv`
- Format: csv
- Contract: CSV with header: reduced_density (dimensionless, float), P_bar (pressure in bar, float). One row per given reduced density; order not enforced.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_isotherm_pressures.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_isotherm_pressures.csv
- path: `/app/outputs/critical_isotherm_pressures.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Pressures computed along the critical isotherm (T = T_c) of the nonanalytic EOS for benzene at the specified reduced densities.
- schema:
  - `type`: table
  - `required_columns`: `reduced_density`, `P_bar`
  - `units`:
    - `reduced_density`: dimensionless
    - `P_bar`: bar

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_isotherm_pressures.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "reduced_density",
          "P_bar"
        ],
        "units": {
          "reduced_density": "dimensionless",
          "P_bar": "bar"
        }
      },
      "description": "Pressures computed along the critical isotherm (T = T_c) of the nonanalytic EOS for benzene at the specified reduced densities."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your CSV. For each reduced density, the pressure you reported is compared to a hidden reference value extracted from the paper, using specified tolerances that may differ between the critical point (σ = 1) and away from it. The reward for this stage is the fraction of points that fall within tolerance. The final overall reward is computed by combining the weighted scores of all scored workflow stages.
