# Anisotropic Disordered System Localisation Exponent

## Problem background
In disordered electronic systems, scaling theories predict that the localisation length and conductance follow power laws near the mobility edge. The standard result in isotropic three‑dimensional systems is an exponent of 1. However, experiments on highly anisotropic semiconductors have shown deviations from this value, motivating a theoretical description that can capture the effect of anisotropy.

This work develops an analytic theory based on a pairwise‑averaged transfer‑matrix approach. In the anisotropic, weak‑disorder regime the central quantity is the pair eigenvalue spectrum μ_q, determined by a self‑consistency condition involving the lattice hopping anisotropies (expressed as effective mass ratios), the on‑site energy, and the squared disorder strength δ². The inverse localisation length is defined as η⁻¹ = ln(μ_min), where μ_min is the minimum real pair eigenvalue over the two‑dimensional Brillouin zone of in‑plane momenta. The critical behaviour — i.e. how η⁻¹ scales with δ² near the localisation threshold — is characterised by a critical exponent.

Your task is to reproduce the numerical determination of this exponent for the highly anisotropic case described below.

## Approach
The core idea is to solve the pair spectrum equation F_q(μ) = δ⁻² for the symmetric anisotropic parameter set, compute the smallest allowed eigenvalue μ_min as a function of disorder strength, and then infer the exponent from the scaling of η⁻¹ = ln(μ_min) near the critical disorder.

- F_q(μ) is defined by the pair spectrum sum (Pendry 1986, Eqs. (17)-(21)). For a cubic lattice with one orbital per site, after scaling by the hopping V_z, the dimensionless parameters are:
    β_x = V_x/V_z = m_z*/m_x*,   β_y = V_y/V_z = m_z*/m_y*,
    and the on‑site energy‑like parameter is Γ.
  The function F_q(μ) for a system with L_x × L_y unit cells in the two transverse directions is:

    F_q(μ) = (1/(L_x L_y)) ∑_{k_x=1}^{L_x} ∑_{k_y=1}^{L_y}
        μ (μ² − 1) / [ (μ − μ_{k q + +})(μ − μ_{k q + −})(μ − μ_{k q − +})(μ − μ_{k q − −}) ]   (18)

  where the wavevectors are k = (k_x,k_y) and the in‑plane momentum q = (2π q_x/L_x, 2π q_y/L_y) with integer q_x,q_y ∈ [0, L−1] or equivalently q_x,q_y = 1,…,L. The complex pair eigenvalues are

    μ_{k q a b} = exp( i a K_k + i b K_{-k+q} ),   a,b ∈ {+1,−1}   (19)

  The Bloch wave‑vector K_k satisfies

    exp(i K_k) = (1/2) ( Γ_k + i √(4 − Γ_k²) ),   (20)

  where the dimensionless band‑structure parameter is

    Γ_k = Γ − 2 β_x cos(2π k_x/L_x) − 2 β_y cos(2π k_y/L_y).   (21)

  Only real values μ ≥ 1 are admissible. For μ = 1 the summand is indeterminate but the limit is finite; numerically one may evaluate F_q(μ) at μ = 1 + ε with ε ≪ 1 (e.g. 1e‑8) to avoid the singularity.

- The critical disorder δ_c² is obtained by evaluating F_q(μ=1) over a dense grid of q‑points covering the first Brillouin zone and taking δ_c² = 1 / max_q F_q(μ=1) (i.e. δ_c² = 1 / F_min where F_min = min_q F_q(μ=1)).
- For a sequence of δ² values greater than δ_c², the equation F_q(μ) = δ^{−2} is solved for μ on the same q‑grid. For each δ², the smallest real μ ≥ 1 is μ_min, giving the inverse localisation length η^{−1} = ln(μ_min).
- The critical exponent is then extracted by a log‑log linear regression of η^{−1} versus (δ² − δ_c²).

The specific regime studied here is the symmetric anisotropic case with effective mass ratios m_x*/m_z* = m_y*/m_z* = 4 (hence β_x = β_y = 0.25), on‑site parameter Γ = 0, and plane dimensions L_x = L_y = 100. You will implement the required evaluation of F_q(μ) and the root‑finding solver using standard numerical tools.

## Reproduction target
Produce a CSV file `eta_data.csv` with columns `delta_squared` (float, the squared disorder strength) and `eta_inv` (float, the inverse localisation length ln(μ_min)). The δ² values should range from the computed critical disorder δ_c² up to a point where η⁻¹ is clearly positive, with sufficient density to allow a reliable log‑log regression. The hidden checker will read this file, filter for δ² > δ_c², and perform a log‑log linear regression of η⁻¹ against (δ² − δ_c²) to extract the critical exponent. Your submission must contain the raw (δ², η⁻¹) pairs; you should NOT report the fitted exponent yourself.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute critical disorder
- Role: process
- Action: Evaluate the pair spectrum function F_q(μ=1) for the symmetric anisotropic case (effective mass ratios m_x*/m_z* = m_y*/m_z* = 4, on‑site parameter Γ = 0, plane dimensions L_x = L_y = 100) over a dense discrete grid of in‑plane momenta q covering the first Brillouin zone. Find the minimum value F_min and compute the critical disorder δ_c² = 1 / F_min.
- Evidence: `/app/outputs/critical_disorder.txt`

### Step 2: Compute inverse localisation length vs disorder
- Role: scored (load-bearing)
- Action: For a sequence of disorder strengths δ² greater than the computed critical value, numerically solve the pair spectrum equation F_q(μ) = δ^{-2} for μ on a dense q‑grid covering the first Brillouin zone. For each δ², find the smallest real μ ≥ 1 and compute η^{-1} = ln(μ_min). Output a CSV file with columns delta_squared and eta_inv.
- Output file: `/app/outputs/eta_data.csv`
- Format: csv
- Contract: Two columns: delta_squared (float), eta_inv (float). delta_squared is the squared disorder strength; eta_inv is the inverse localisation length ln(μ_min).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/eta_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### eta_data.csv
- path: `/app/outputs/eta_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Disorder‑strength vs inverse localisation length data. The hidden checker will perform a log‑log linear regression on this data and verify that the fitted exponent lies within the expected range for the symmetric anisotropic regime.
- schema:
  - `type`: table
  - `required_columns`: `delta_squared`, `eta_inv`
  - `units`:
    - `delta_squared`: dimensionless
    - `eta_inv`: dimensionless

Notes: The critical disorder from step1 is not scored, but the agent must use it to choose a valid δ² range for step2. The exact grid resolution and solver settings are left to the agent; the checker only inspects the CSV contents.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "eta_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta_squared",
          "eta_inv"
        ],
        "units": {
          "delta_squared": "dimensionless",
          "eta_inv": "dimensionless"
        }
      },
      "description": "Disorder‑strength vs inverse localisation length data. The hidden checker will perform a log‑log linear regression on this data and verify that the fitted exponent lies within the expected range for the symmetric anisotropic regime."
    }
  ],
  "notes": "The critical disorder from step1 is not scored, but the agent must use it to choose a valid δ² range for step2. The exact grid resolution and solver settings are left to the agent; the checker only inspects the CSV contents."
}
```

## How you are scored
Only the artifact `eta_data.csv` (Step 2) carries weight. A hidden verifier will load your CSV, check that it has the required columns and a sensible number of points, filter to the regime δ² > δ_c², and perform a log‑log linear regression of η⁻¹ versus (δ² − δ_c²). The fitted slope — the critical exponent — is compared to a hidden reference range that is consistent with the paper’s theoretical prediction, but which is not disclosed to you. Full credit is awarded when the exponent falls within the reference interval; partial credit may be given for data that exhibits the correct monotonic trend even if the exact slope deviates. The output of Step 1 (`critical_disorder.txt`) is not scored but is necessary for you to choose a valid δ² range; the verifier does not inspect it. Structural correctness of the CSV (headers, numeric columns, no missing entries) is a prerequisite for scoring. The verifier’s regression and scoring code are completely hidden: your goal is to supply (δ², η⁻¹) data from which the correct exponent can be reliably extracted.
