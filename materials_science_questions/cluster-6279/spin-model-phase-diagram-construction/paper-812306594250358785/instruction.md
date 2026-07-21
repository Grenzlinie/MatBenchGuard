# Multicritical Point K-Values from Effective-Potential Solver for 1D FK Model

## Problem background
The model is a one-dimensional chain of atoms with an on-site potential V(x)=K f(x) and a nearest-neighbor interaction W(x'-x)=f(x'-x-γ), where f is a 1-periodic piecewise parabolic function: f(x)=½ x² for -¼≤x≤¼ and f(x)=1/16-½(x-½)² for ¼≤x≤¾, periodically extended. The parameters K and γ control the strength and shift of the potentials. The ground state can exhibit different winding numbers (average separation of successive atoms modulo 1) and the phase diagram in (K,γ) space contains both convex and nonconvex regions. In the nonconvex region, first-order transitions occur between phases, and at specific points the nature of the phase boundaries changes—these are bicritical (or tricritical) points, labelled C1–C8. The quantitative outcome is the set of K-coordinates of these multicritical points, which characterize the structure of the phase diagram. Your task is to compute these K values by implementing the effective-potential method.

## Approach
The effective-potential method reformulates the ground-state problem as an eigenvalue equation: V(x') + min_x[W(x'-x)+R(x)] = λ + R(x'), where λ is the ground-state energy per site and R(x) is a periodic effective potential. Discretise the configuration space x on a uniform grid of 100 points covering [0,1). Solve the eigenvalue equation by successive approximations: starting from an initial guess for R, iterate the minimisation and update until convergence to obtain λ and R. From the converged effective potential, the ground state and its winding number ω = P/Q (period Q, net displacement P) are extracted. By repeating this procedure over a dense grid of (K, γ) parameters spanning the regions of interest, you obtain a mapping of winding numbers across the parameter space. The bicritical/tricritical points C1–C8 are identified as the locations where first-order transition lines (boundaries across which ω jumps) meet continuous transition lines. The required output is the K-coordinate of each such point, derived from the phase boundaries observed in the scan.

## Reproduction target
Produce the K values for the eight multicritical points C1–C8 (C1 is tricritical; C2–C8 are bicritical). The final output must be a JSON array written to /app/outputs/critical_points.json, with each element containing at least 'id' (one of 'C1'…'C8') and 'K' (a float number). The intermediate parameter scan, documented in /app/outputs/parameter_scan.csv, serves as supporting evidence that the solver was executed and that the critical points were extracted from it, but the CSV is not directly scored. The JSON is the sole scored artifact.

## Assets

- Python (>=3.9) with NumPy and SciPy: https://www.python.org/;https://pypi.org/project/numpy/;https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Run effective-potential solver over parameter grid
- Role: process
- Action: Implement the effective-potential eigenvalue solver for the model V(x)=K f(x) and W(x'-x)=f(x'-x-γ) with f(x) the 1-periodic piecewise-parabolic function defined by f(x)=½x² for -¼≤x≤¼ and f(x)=1/16-½(x-½)² for ¼≤x≤¾, periodically extended. Discretize x on a uniform grid of 100 points on [0,1). Solve the eigenvalue equation V(x')+min_x[W(x'-x)+R(x)]=λ+R(x') by successive approximations to convergence. Execute this solver for a grid of (K, γ) parameters spanning at least K ∈ [1.3, 4.2] and γ ∈ [0.15, 0.75] to capture all relevant phases. For each (K,γ), compute the ground-state winding number ω = P/Q and the eigenvalue λ. Write a CSV file (evidence) containing columns: K, gamma, winding_number, lambda (the eigenvalue column is optional).
- Evidence: `/app/outputs/parameter_scan.csv`

### Step 2: Extract bicritical/tricritical point K values
- Role: scored (load-bearing)
- Action: Analyze the parameter_scan.csv data to identify the bicritical and tricritical points C1–C8 where first-order transition lines between winding numbers meet continuous transition lines. Determine the K coordinate of each point from the phase boundary data. Output a JSON file containing an array of objects with fields 'id' (string 'C1'..'C8'), 'K' (float), and optionally 'gamma' (float) and 'description' (string). This file must be placed at /app/outputs/critical_points.json.
- Output file: `/app/outputs/critical_points.json`
- Format: json
- Contract: Array of objects with required fields: id (string, one of 'C1'..'C8'), K (float). Optional fields: gamma (float), description (string).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_points.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_points.json
- path: `/app/outputs/critical_points.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: K values of the bicritical/tricritical points C1–C8. Each object contains the point id and its K-coordinate, compared against the hidden gold values from Table I of the source paper within an absolute tolerance of 0.005.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `id`, `K`
    - `properties`:
      - `id`:
        - `type`: string
      - `K`:
        - `type`: number
      - `gamma`:
        - `type`: number
      - `description`:
        - `type`: string

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_points.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "id",
            "K"
          ],
          "properties": {
            "id": {
              "type": "string"
            },
            "K": {
              "type": "number"
            },
            "gamma": {
              "type": "number"
            },
            "description": {
              "type": "string"
            }
          }
        }
      },
      "description": "K values of the bicritical/tricritical points C1–C8. Each object contains the point id and its K-coordinate, compared against the hidden gold values from Table I of the source paper within an absolute tolerance of 0.005."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier will read your /app/outputs/critical_points.json file and compare each reported K value to a hidden reference value for the same point ID. For each point C1–C8, the absolute difference |K_reported − K_reference| is computed. If the difference is within a preset tolerance (which is not disclosed), that point is counted as correct. The final reward is the fraction of points that are correct (all eight points have equal weight, summing to 1.0). The parameter_scan.csv is not directly scored, but its presence and consistency with the JSON may be audited by the verifier. No automated penalties are applied for extra optional fields; only the required 'id' and 'K' fields affect the score. The scoring reward will be a single float in [0,1].
