# Spinodal Locus Determination from Thermodynamic Models

## Problem background
Predicting the thermodynamic behavior of fluid mixtures from molecular interactions is a fundamental challenge. The virial equation of state (VEOS) expresses the pressure as a density expansion whose coefficients (virial coefficients) depend only on interactions among small groups of molecules. Computing high-order mixture virial coefficients for model Lennard-Jones mixtures allows a systematic study of how far the truncated VEOS can describe vapor-liquid stability and indicate phase boundaries. This workflow computes the elementary mixture virial coefficients up to fourth order using the Mayer‑sampling Monte Carlo method, then uses those coefficients to map the spinodal (stability limit) in the density–composition plane.

## Approach
The core method is Mayer‑sampling Monte Carlo (MSMC). MSMC directly samples cluster integrals that define the virial coefficients by weighting configurations by the absolute value of the Mayer‑function integrand. Overlap sampling with Bennett’s optimization and a hard‑sphere reference (diameter 1.5 σ₁₁) is used to compute the ratios of the target Lennard‑Jones cluster integrals to the known reference integrals. For mixture I (σ₁₁=σ₂₂=1.0, ε₁₁=ε₂₂=1.0, ε₁₂=0.75), all elementary coefficients B_ij with total molecules i+j ≤ 4 are computed at four temperatures (0.7, 1.0, 1.15, 1.31 in reduced units) by enumerating all Mayer diagrams and their species‑labeled permutations. After obtaining the elementary coefficients, the composition‑dependent virial coefficients B₂(y₁), B₃(y₁), B₄(y₁) are assembled, and the virial equation of state truncated at B₄ is used to numerically locate points (density ρ, mole fraction y₁) where the thermodynamic stability condition becomes an equality—defining the spinodal curve at T=1.15.

## Reproduction target
For the symmetric Lennard‑Jones mixture described above, compute all elementary virial coefficients B_ij for n=2 to 4 (i.e., B₂₀, B₁₁, B₀₂, …, B₀₄) at the four specified temperatures using MSMC. Then, using these coefficients and the virial equation truncated to B₄, determine the spinodal curve in the density–mole‑fraction (ρ, y₁) plane at T=1.15 and report the set of (ρ, y₁) points that satisfy the stability condition as an equality.

## Assets
No external datasets, pre‑trained models, or proprietary software are required. The Lennard‑Jones pair potential and hard‑sphere reference system are fully specified by the mixture parameters given in the approach. Standard numerical and scientific computing libraries (random number generation, linear algebra, optimization) are assumed to be available. No other assets need to be fetched.

## Workflow steps

### Step 1: Compute mixture elementary virial coefficients
- Role: scored (load-bearing)
- Action: Implement the Mayer-sampling Monte Carlo (MSMC) protocol for mixture cluster integrals using a Lennard-Jones pair potential and a hard-sphere reference system of diameter 1.5 σ₁₁. For mixture I (σ₁₁=σ₂₂=1.0, ε₁₁=ε₂₂=1.0, ε₁₂=0.75), generate all Mayer diagrams and their species-labeled permutations for each elementary virial coefficient B_ij with i+j ≤ 4. Sample configurations with weight π = |γ| (the absolute value of the summed integrand) and employ the overlap-sampling estimator with Bennett's optimization. Run independent MSMC simulations for each coefficient at temperatures T = 0.7, 1.0, 1.15, 1.31 (in units of ε₁₁/k) with sufficient trial moves to obtain statistical error estimates (67% confidence half-width). Write one JSON file containing the value and error for every elementary coefficient at each temperature.
- Output file: `/app/outputs/elementary_coefficients.json`
- Format: json
- Contract: JSON object. Keys are temperature strings ("0.7", "1.0", "1.15", "1.31"). Each value is an object with keys "B20", "B11", "B02", "B30", "B21", "B12", "B03", "B40", "B31", "B22", "B13", "B04". Each coefficient object contains "value" (float) and "error" (float, 67% confidence half-width).
- Scoring: scored by hidden verifier

### Step 2: Determine spinodal curve at T=1.15
- Role: scored
- Action: From the elementary virial coefficients computed in step_elementary, assemble the composition-dependent virial coefficients B₂(y₁), B₃(y₁), B₄(y₁). Construct the virial equation of state truncated to B₄ and numerically search for points (ρ, y₁) where the thermodynamic stability condition holds as an equality at T = 1.15. Output the set of (ρ, y₁) points that define the spinodal curve.
- Output file: `/app/outputs/spinodal_T1.15.csv`
- Format: csv
- Contract: CSV file with two columns: 'rho' (float, number density made dimensionless by σ₁₁³) and 'y1' (float, mole fraction of species 1, in [0,1]). Each row is one spinodal point; points are ordered to form a smooth curve.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/elementary_coefficients.json`
- `/app/outputs/spinodal_T1.15.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### elementary_coefficients.json
- path: `/app/outputs/elementary_coefficients.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Elementary virial coefficients for mixture I at four temperatures. Compared to hidden paper-reported gold with relative tolerances.
- schema:
  - `type`: object
  - `required_keys`: `0.7`, `1.0`, `1.15`, `1.31`
  - `value_schema`:
    - `type`: object
    - `required_keys`: `B20`, `B11`, `B02`, `B30`, `B21`, `B12`, `B03`, `B40`, `B31`, `B22`, `B13`, `B04`
    - `properties`:
      - `value`:
        - `type`: float
        - `unit`: dimensionless (σ₁₁³ⁿ⁻³)
      - `error`:
        - `type`: float
        - `unit`: dimensionless (67% confidence half-width)

### spinodal_T1.15.csv
- path: `/app/outputs/spinodal_T1.15.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Spinodal curve points at T=1.15. The verifier recomputes the stability condition using the submitted elementary coefficients and checks that points satisfy the spinodal equality within tolerance; symmetry and physical range are also verified.
- schema:
  - `type`: table
  - `required_columns`: `rho`, `y1`
  - `units`:
    - `rho`: dimensionless (σ₁₁³)
    - `y1`: mole fraction

Notes: The elementary coefficients are scored by comparison to hidden gold values from the paper's EPAPS supplement using relative tolerance. The spinodal is scored by recomputing the stability condition with the agent's coefficients; self-consistency is verified.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "elementary_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required_keys": [
          "0.7",
          "1.0",
          "1.15",
          "1.31"
        ],
        "value_schema": {
          "type": "object",
          "required_keys": [
            "B20",
            "B11",
            "B02",
            "B30",
            "B21",
            "B12",
            "B03",
            "B40",
            "B31",
            "B22",
            "B13",
            "B04"
          ],
          "properties": {
            "value": {
              "type": "float",
              "unit": "dimensionless (σ₁₁³ⁿ⁻³)"
            },
            "error": {
              "type": "float",
              "unit": "dimensionless (67% confidence half-width)"
            }
          }
        }
      },
      "description": "Elementary virial coefficients for mixture I at four temperatures. Compared to hidden paper-reported gold with relative tolerances."
    },
    {
      "file": "spinodal_T1.15.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "rho",
          "y1"
        ],
        "units": {
          "rho": "dimensionless (σ₁₁³)",
          "y1": "mole fraction"
        }
      },
      "description": "Spinodal curve points at T=1.15. The verifier recomputes the stability condition using the submitted elementary coefficients and checks that points satisfy the spinodal equality within tolerance; symmetry and physical range are also verified."
    }
  ],
  "notes": "The elementary coefficients are scored by comparison to hidden gold values from the paper's EPAPS supplement using relative tolerance. The spinodal is scored by recomputing the stability condition with the agent's coefficients; self-consistency is verified."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage.
- For `elementary_coefficients.json`, the verifier compares your reported coefficient values (and their statistical errors) to reference results derived from the same model, using tolerances that account for the stochastic nature of MSMC and the expected accuracy of a correct independent implementation.
- For `spinodal_T1.15.csv`, the verifier recomputes the stability condition (Eq. 4) using your submitted elementary coefficients and checks that each reported (ρ, y₁) point satisfies the spinodal equality within a numeric tolerance. It also verifies that the curve is symmetric about y₁=0.5 and spans a physically meaningful range.
The final reward is a weighted combination of these checks; simply reporting the expected numbers without performing the required computations will not receive credit.
