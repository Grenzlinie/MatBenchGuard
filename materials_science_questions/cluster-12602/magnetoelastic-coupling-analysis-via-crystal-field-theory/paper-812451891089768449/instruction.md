# Roughness-induced surface magnetoelastic tensor components

## Problem background
Magnetic multilayers exhibit surface anisotropy and magnetostriction that are strongly influenced by interfacial roughness. The roughness, characterized by its rms amplitude and correlation length, modifies the magnetostatic energy and thereby contributes to the magnetoelastic tensor components and the surface anisotropy constant. Understanding these roughness-induced contributions is important for memory applications where surface properties control performance.

## Approach
The core idea is to model the roughness as a perturbation of a perfectly flat film and compute the resulting corrections to the magnetostatic energy within a dipolar model. The energy density can be expressed in terms of two auxiliary functions f and g, which are defined by double series over the in-plane wave numbers. These functions depend on the roughness amplitude σ, the film thickness t, and the correlation length ξ. From f and g, and using simple algebraic relations, one obtains the dimensionless surface magnetoelastic tensor components Bs_3333, Bs_3311, Bs_1111, Bs_1122 (normalized by 2π Ms²) and the surface anisotropy constant Ks. The computation involves selecting a grid of parameter points that span the physical range of interest (σ = 2–15 Å, t = 10 and 30 Å, ξ = 10 and 30 Å), summing the double series for each point with sufficient truncation to achieve convergence, and then evaluating the algebraic expressions to produce the final quantities.

## Reproduction target
Recompute the four dimensionless surface magnetoelastic tensor components and the surface anisotropy constant for at least eight parameter combinations that explore the roughness space. The results must be written to a CSV file containing columns for σ, t, ξ, f, g, and each of the B_s components and K_s. The output serves as the basis for a direct numerical comparison against a reference recomputation.

## Assets
- Python (standard library)
- NumPy (optional, provides efficient array operations; the pure Python `math` module also suffices)

## Workflow steps

### Step 1: Compute auxiliary functions f and g
- Role: process
- Action: Select at least 8 parameter combinations covering σ=2‑15 Å, t=10,30 Å, ξ=10,30 Å. For each combination, evaluate the dimensionless double series f and g defined by:
f = (16/(π⁴σ)) Σ_{k,l≥0} {1 − exp(−Pₖₗ t) + exp(−Pₖₗ(t−2σ)) − exp(−Pₖₗ 2σ)} / {Pₖₗ (2k+1)² (2l+1)²},
g = (16/(π⁴σ)) Σ_{k,l≥0} {t exp(−Pₖₗ t) − (t−2σ) exp(−Pₖₗ(t−2σ)) + 2σ exp(−Pₖₗ 2σ)} / {(2k+1)² (2l+1)²},
with Pₖₗ = (π/ξ) √((2k+1)² + (2l+1)²). Sum over k,l until convergence, using a high truncation limit (e.g., k,l up to ~3000 or higher; the reference recomputation uses KMAX=3000). Save the results to f_g.csv with columns: sigma, t, xi, f, g.

Important boundary condition: If t < 2σ, the exponential term exp(−Pₖₗ(t−2σ)) and the corresponding factor (t−2σ) in the g-series should be set to zero. This corresponds to the physically unrealistic situation where roughness exceeds half the film thickness; the checker will enforce this behavior.
- Evidence: `/app/outputs/f_g.csv`

### Step 2: Compute magnetoelastic tensor components and anisotropy constant
- Role: scored (load-bearing)
- Action: Using the previously computed f and g, obtain the dimensionless surface magnetoelastic tensor components (normalized by 2πMs²) and surface anisotropy constant:
Bs_3333 = −(1−g) σ/2,
Bs_3311 = −(1−2f+g) σ/2,
Bs_1111 = −(π σ t)/(4 ξ),
Bs_1122 =  (π σ t)/(4 ξ),
Ks = −(3/4) σ (1−f).
Write a CSV file with columns: sigma, t, xi, f, g, Bs_3333, Bs_3311, Bs_1111, Bs_1122, Ks. All quantities are dimensionless; use at least 6 decimal places.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with columns: sigma (float), t (float), xi (float), f (float), g (float), Bs_3333 (float), Bs_3311 (float), Bs_1111 (float), Bs_1122 (float), Ks (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/f_g.csv`
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### f_g.csv
- path: `/app/outputs/f_g.csv`
- format: csv
- purpose: process
- target_policy: none
- description: Intermediate computed auxiliary functions f and g.
- schema:
  - `type`: table
  - `required_columns`: `sigma`, `t`, `xi`, `f`, `g`
  - `units`:
    - `sigma`: Angstrom
    - `t`: Angstrom
    - `xi`: Angstrom
    - `f`: dimensionless
    - `g`: dimensionless

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Surface magnetoelastic tensor components (normalized by 2πMs²) and surface anisotropy constant for each roughness parameter point.
- schema:
  - `type`: table
  - `required_columns`: `sigma`, `t`, `xi`, `f`, `g`, `Bs_3333`, `Bs_3311`, `Bs_1111`, `Bs_1122`, `Ks`
  - `units`:
    - `sigma`: Angstrom
    - `t`: Angstrom
    - `xi`: Angstrom
    - `f`: dimensionless
    - `g`: dimensionless
    - `Bs_3333`: dimensionless
    - `Bs_3311`: dimensionless
    - `Bs_1111`: dimensionless
    - `Bs_1122`: dimensionless
    - `Ks`: dimensionless

Notes: The agent must choose at least 8 parameter points covering the ranges σ=2‑15 Å, t=10,30 Å, ξ=10,30 Å. The checker recomputes gold values via high‑truncation double series and compares each submitted value with absolute tolerance 1e‑6.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "f_g.csv",
      "format": "csv",
      "purpose": "process",
      "target_policy": "none",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma",
          "t",
          "xi",
          "f",
          "g"
        ],
        "units": {
          "sigma": "Angstrom",
          "t": "Angstrom",
          "xi": "Angstrom",
          "f": "dimensionless",
          "g": "dimensionless"
        }
      },
      "description": "Intermediate computed auxiliary functions f and g."
    },
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "sigma",
          "t",
          "xi",
          "f",
          "g",
          "Bs_3333",
          "Bs_3311",
          "Bs_1111",
          "Bs_1122",
          "Ks"
        ],
        "units": {
          "sigma": "Angstrom",
          "t": "Angstrom",
          "xi": "Angstrom",
          "f": "dimensionless",
          "g": "dimensionless",
          "Bs_3333": "dimensionless",
          "Bs_3311": "dimensionless",
          "Bs_1111": "dimensionless",
          "Bs_1122": "dimensionless",
          "Ks": "dimensionless"
        }
      },
      "description": "Surface magnetoelastic tensor components (normalized by 2πMs²) and surface anisotropy constant for each roughness parameter point."
    }
  ],
  "notes": "The agent must choose at least 8 parameter points covering the ranges σ=2‑15 Å, t=10,30 Å, ξ=10,30 Å. The checker recomputes gold values via high‑truncation double series and compares each submitted value with absolute tolerance 1e‑6."
}
```

## How you are scored
A hidden verifier independently recomputes the gold values for f, g, and the resulting B_s components and K_s for each parameter point, using the same formulas but with a higher truncation of the double series. Every submitted value is compared to the corresponding gold value. The score is the fraction of values that fall within the required tolerance. Reporting the paper’s original numbers without running the computation will not pass; the verifier checks the actual numeric output of your workflow.