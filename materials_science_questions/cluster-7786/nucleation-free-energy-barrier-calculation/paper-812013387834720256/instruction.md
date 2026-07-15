# Nucleation Free-Energy Minimum Identification

## Problem background
Classical homogeneous nucleation theory usually predicts a single free-energy maximum corresponding to the critical nucleus, ignoring the free-energy change of the parent phase. This work extends the theory to include that change for a binary ideal solution, which can produce both a maximum and a new minimum in the nucleation free-energy curve. Your task is to implement the modified free-energy expression and numerically determine the positions of both extremum.

## Approach
Implement the free-energy change per nucleus for a one-component solid nucleus in a binary ideal dilute solution. The free energy as a function of radius r is given by:

Δ_nucl G = 4π r² σ − (n_A^n R T / N) ln S_ini + (n_A − n_A^n)(R T / N) ln((1 − n_A^n / n_A) / (1 − n_A^n)) + (1 − n_A)(R T / N) ln(1 / (1 − n_A^n)),

where n_A^n = (4π r³ N) / (3 v_A), and S_ini = n_A / x_A^sat. The parameters are: σ = 1 J/m², v_A = 1×10⁻⁵ m³/mol, T = 300 K, n_A = x_A = 1×10⁻⁴, N = 1×10¹⁴, x_A^sat = 1×10⁻⁵ (giving S_ini = 10). Evaluate Δ_nucl G for radii from 0 to 10 nm on a fine grid, compute the numerical derivative, and locate the sign changes that identify the local maximum (critical radius) and the new local minimum.

## Reproduction target
Compute the nucleation free-energy curve for the given parameters, identify the local maximum and local minimum, and write their coordinates to `extremum_points.csv`. The file must contain one row with four numeric values: the radius and ΔG for the maximum, followed by the radius and ΔG for the minimum.

## Assets

- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Compute nucleation curve and identify extremum
- Role: scored (load-bearing)
- Action: Implement the nucleation free energy change per nucleus for a one-component solid nucleus in a binary ideal dilute solution. Use the parameters: σ=1 J/m², molar volume v_A=1e-5 m³/mol, temperature T=300 K, initial mole fraction n_A=x_A=1e-4, total number of nuclei N=1e14, saturated mole fraction x_A^sat=1e-5 (initial supersaturation S_ini=10). The free energy as a function of radius r is given by Δ_nucl G = 4πr²σ − (n_A^n RT/N) ln S_ini + (n_A − n_A^n)(RT/N) ln((1 − n_A^n/n_A)/(1 − n_A^n)) + (1 − n_A)(RT/N) ln(1/(1 − n_A^n)), where n_A^n = (4π r³ N)/(3 v_A). Compute Δ_nucl G for r from 0 to 10 nm at a sufficiently fine spacing. Find the critical radius (local maximum) and the new minimum by locating sign changes of the numerical derivative. Output the coordinates to extremum_points.csv.
- Output file: `/app/outputs/extremum_points.csv`
- Format: csv
- Contract: Header: r_max (nm), DeltaG_max (J), r_min (nm), DeltaG_min (J). Exactly one data row with four numeric values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/extremum_points.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### extremum_points.csv
- path: `/app/outputs/extremum_points.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV file with the coordinates of the maximum and minimum of the nucleation free-energy curve. The hidden checker recomputes the correct extremum using the same formula and parameters, and checks agreement within relative tolerances.
- schema:
  - `type`: table
  - `required_columns`: `r_max`, `DeltaG_max`, `r_min`, `DeltaG_min`
  - `units`:
    - `r_max`: nm
    - `DeltaG_max`: J
    - `r_min`: nm
    - `DeltaG_min`: J

Notes: The checker recomputes the nucleation curve independently and compares the extremum coordinates. Tolerances are set to allow for discretization differences but require a correct physical result.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "extremum_points.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_max",
          "DeltaG_max",
          "r_min",
          "DeltaG_min"
        ],
        "units": {
          "r_max": "nm",
          "DeltaG_max": "J",
          "r_min": "nm",
          "DeltaG_min": "J"
        }
      },
      "description": "CSV file with the coordinates of the maximum and minimum of the nucleation free-energy curve. The hidden checker recomputes the correct extremum using the same formula and parameters, and checks agreement within relative tolerances."
    }
  ],
  "notes": "The checker recomputes the nucleation curve independently and compares the extremum coordinates. Tolerances are set to allow for discretization differences but require a correct physical result."
}
```

## How you are scored
A hidden verifier will independently recompute the correct extremum coordinates using the same free-energy expression and parameters, then compare your submitted values to the recomputed reference. The verifier checks that exactly one maximum and one minimum exist in the scanned radius range and evaluates how closely your reported radii and ΔG values agree with the reference. Your reward is based solely on the accuracy of your computed coordinates; reporting numbers without a correct implementation yields no credit.
