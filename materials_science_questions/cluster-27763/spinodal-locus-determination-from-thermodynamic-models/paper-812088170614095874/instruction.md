# HNC Equation for Restricted Primitive Model: Isochore Compressibility

## Problem background
The hypernetted chain (HNC) equation is an integral equation theory for the structure and thermodynamics of fluids. When applied to the restricted primitive model (RPM) of ionic fluids—equally sized charged hard spheres in a dielectric continuum—the HNC closure yields a region in the density–temperature plane where no real solution exists. The physical origin of this no-solution boundary is not fully settled: on the liquid side it may correspond to a spinodal (diverging compressibility), while on the gas side it might be an artifact of the HNC approximation. Resolving this question requires computing thermodynamic quantities, especially the isothermal compressibility, along paths that approach the boundary. This task focuses on reproducing the behaviour of the inverse isothermal compressibility χ₀/χ along a fixed-density path approaching the HNC divergence.

## Approach
The reproduction uses a numerical solution of the renormalized Ornstein–Zernike (OZ) equation with the HNC closure. The long-range Coulombic potential is handled by splitting it into a short-range part and a long-range Yukawa-regularized part; this yields a short-range direct correlation function c^sr and total correlation function h^sr, plus a modified Debye–Hückel chain bond q(r) that captures the long-range screening. The OZ equation is transformed into a renormalized form involving only short-range functions. The nonlinear system is solved with a Newton–Raphson method applied to a coarse/fine Fourier decomposition (the Labík–Malijevský–Vonka, LMV, method), which expands the coarse part of the correlation functions in a trigonometric basis. To reduce computation, the Jacobian matrix computed for one state point is reused for neighbouring points (Kinoshita–Harada strategy). From the converged short-range direct correlation functions, the reduced inverse isothermal compressibility χ₀/χ is obtained as the k=0 limit of the appropriate Fourier transform. The solver is then run along the isochore ρσ³ = 0.05 for a series of reduced inverse temperatures Γ, and χ₀/χ is recorded for each converged state point.

## Reproduction target
Using the renormalized HNC solver, compute the reduced inverse isothermal compressibility χ₀/χ for the 1:1 restricted primitive model at fixed reduced density ρσ³ = 0.05 for a set of reduced inverse temperatures Γ spanning from 2.0 up to the solver's convergence limit (approximately 14.0). For each converged state point, output the pair (Γ, χ₀/χ) in a CSV file named chi0_over_chi_vs_Gamma.csv with columns Gamma,chi0_over_chi. The objective is to produce the compressibility values along this isochore that reflect the solution's behaviour near the HNC no-solution boundary.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Implement renormalized OZ HNC solver for RPM
- Role: process
- Action: Develop and implement a numerical solver for the hypernetted chain (HNC) equation for the 1:1 restricted primitive model (RPM) of ionic fluids. Use the renormalized Ornstein–Zernike formulation with Yukawa regularization, a Labík–Malijevský–vonka (LMV) coarse/fine decomposition (M ~ 20–30 coarse modes, up to N=1024 grid points, Δr ≈ 0.02 in ion-diameter units), and the Kinoshita–Harada strategy of reusing the Jacobian matrix across neighbouring state points. The solver must compute short-range correlation functions and the chain bond q(r) required for the closure and thermodynamic integrals.
- Evidence: `/app/outputs/solver_convergence_test.log`

### Step 2: Compute inverse compressibility along ρσ³=0.05 isochore
- Role: scored (load-bearing)
- Action: Using the implemented HNC solver, run calculations at fixed reduced density ρσ³ = 0.05 for the reduced inverse temperatures Γ = 2.0, 5.0, 7.0, 8.0, 10.0, 12.0, 14.0 (or until the solver fails to converge). For each converged state point, compute the reduced inverse isothermal compressibility χ0/χ from the short-range direct correlation functions at k=0. Output a CSV file named chi0_over_chi_vs_Gamma.csv with columns: Gamma, chi0_over_chi. Include only the points for which the solution converged.
- Output file: `/app/outputs/chi0_over_chi_vs_Gamma.csv`
- Format: csv
- Contract: Two columns: Gamma (float, dimensionless reduced inverse temperature) and chi0_over_chi (float, dimensionless reduced inverse isothermal compressibility). Header row: 'Gamma,chi0_over_chi'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/chi0_over_chi_vs_Gamma.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### chi0_over_chi_vs_Gamma.csv
- path: `/app/outputs/chi0_over_chi_vs_Gamma.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed inverse isothermal compressibility χ0/χ for the RPM at ρσ³=0.05 as a function of Γ. Used for comparison to hidden reference values and structural trend checks.
- schema:
  - `type`: table
  - `required_columns`: `Gamma`, `chi0_over_chi`
  - `columns_schema`:
    - `Gamma`: float
    - `chi0_over_chi`: float

Notes: The solving agent must reimplement the HNC solver and produce this CSV. The hidden checker compares each chi0_over_chi against reference values with a tolerance and verifies monotonic decrease. Only converged state points are required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "chi0_over_chi_vs_Gamma.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Gamma",
          "chi0_over_chi"
        ],
        "columns_schema": {
          "Gamma": "float",
          "chi0_over_chi": "float"
        }
      },
      "description": "Computed inverse isothermal compressibility χ0/χ for the RPM at ρσ³=0.05 as a function of Γ. Used for comparison to hidden reference values and structural trend checks."
    }
  ],
  "notes": "The solving agent must reimplement the HNC solver and produce this CSV. The hidden checker compares each chi0_over_chi against reference values with a tolerance and verifies monotonic decrease. Only converged state points are required."
}
```

## How you are scored
A hidden verifier reads your CSV file and compares each reported χ₀/χ to hidden reference values derived from the original study, using a tolerance. Additionally, the verifier checks that the reported values satisfy a required structural trend with respect to Γ. The process step is validated by the presence of a solver convergence log. Each check contributes to a total score; reporting a plausible-looking number without actually running the HNC solver will likely fail the detailed comparison.
