# Curvature-dependent equilibrium compositions via computational thermodynamics

## Problem background
In two-phase alloys, the curvature of the precipitate interface introduces an additional pressure due to surface tension, raising the Gibbs energy of the precipitate phase and shifting the equilibrium compositions of both phases. This Gibbs–Thomson effect controls nucleation, growth, and coarsening, but traditional analytical models rely on simplifying assumptions—dilute solution, constant precipitate composition, or ideal thermodynamic behavior—that are often inaccurate for concentrated and multicomponent alloys. This task implements a generalized computational thermodynamics method that uses CALPHAD thermodynamic functions to compute curvature-dependent equilibrium phase compositions without those simplifications. You will compute the equilibrium mole fraction of Sn in the FCC matrix of a binary Pb–Sn alloy at 150 °C across a range of precipitate radii, demonstrating the quantitative relationship between interface curvature and matrix solute concentration.

## Approach
The method consists of three main computations: (1) acquire the mixing Gibbs energy curves for the FCC (Pb-rich) and BCT (Sn-rich) phases at 150 °C from a public Pb–Sn CALPHAD thermodynamic database using the open-source pycalphad toolkit; (2) for each precipitate radius r, compute the curvature excess Gibbs energy ΔG_excess(r) = 2σ V_m^β / r using the interfacial energy σ and the precipitate molar volume V_m^β, then raise the BCT mixing Gibbs energy by this excess; (3) solve the coupled chemical‑potential equalities μ_A^FCC = μ_A^BCT and μ_B^FCC = μ_B^BCT (Eq. 15 of the original work, derived from the tangent construction) to obtain the equilibrium compositions of both phases at that radius. The chemical potentials are obtained from the mixing Gibbs energy curves via the standard thermodynamic relations. The solver may use any standard nonlinear equation solver (e.g., a root‑finding algorithm) to enforce the equalities. Repeat step (2)–(3) for a logarithmically spaced set of radii from 1 nm to 1000 nm, recording the matrix Sn mole fraction at each radius. The final output is a curve of matrix solute concentration versus precipitate radius.

## Reproduction target
For the binary Pb–Sn system at 150 °C, with Sn‑rich BCT precipitates in a Pb‑rich FCC matrix, compute the equilibrium mole fraction of Sn in the matrix (X_B^FCC) as a function of precipitate radius. Use the following fixed material parameters: interfacial energy σ = 235 mJ/m², and molar volume of the BCT precipitate V_m^β = 16.26×10⁻⁶ m³/mol. Obtain the required thermodynamic mixing functions from the public Pb–Sn SGTE binary database via pycalphad. Produce a CSV file with two columns—radius_nm (precipitate radius in nanometers) and X_B_matrix (equilibrium Sn mole fraction in the FCC matrix)—covering at least 20 logarithmically spaced radii from 1.0 nm to 1000.0 nm.

## Assets

- pycalphad (open-source CALPHAD toolkit): pycalphad
- Pb–Sn thermodynamic database (SGTE binary alloy database)

## Workflow steps

### Step 1: Acquire thermodynamic mixing functions
- Role: process
- Action: Using pycalphad, load the Pb–Sn binary TDB database and obtain the mixing Gibbs energy curves ΔG_mix for the FCC (Pb-rich) and BCT (Sn-rich) phases at 150 °C. Interpolate these into callable functions of composition (mole fraction of B, X_B) that can return Gibbs energy and chemical potentials.
- Evidence: none

### Step 2: Compute Gibbs–Thomson concentration curve for Pb–Sn
- Role: scored (load-bearing)
- Action: For each precipitate radius r in a logarithmic range from 1 nm to 1000 nm (at least 20 points): compute the curvature excess Gibbs energy ΔG_excess(r)=2σV_m^β/r using σ=235 mJ/m² and V_m^β=16.26×10⁻⁶ m³/mol; raise the BCT mixing Gibbs energy by ΔG_excess(r); then solve the coupled chemical-potential equalities μ_A^FCC=μ_A^BCT and μ_B^FCC=μ_B^BCT for the equilibrium compositions of both phases. Record the matrix Sn mole fraction X_B^FCC(r). Output the results to the specified CSV file.
- Output file: `/app/outputs/step_01_gibbs_thomson_curve.csv`
- Format: csv
- Contract: Two columns: radius_nm (float, radius of precipitate in nanometers), X_B_matrix (float, equilibrium mole fraction of Sn in the FCC matrix at that radius). Include at least 20 rows covering radii from 1.0 to 1000.0 nm, logarithmically spaced.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_gibbs_thomson_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_gibbs_thomson_curve.csv
- path: `/app/outputs/step_01_gibbs_thomson_curve.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Equilibrium matrix Sn concentration vs precipitate radius for Pb-Sn binary alloy at 150 °C, computed from the paper's algorithm. The hidden checker compares this curve to the paper's reported result with tolerances and checks monotonicity.
- schema:
  - `type`: table
  - `required_columns`: `radius_nm`, `X_B_matrix`
  - `units`:
    - `radius_nm`: nm
    - `X_B_matrix`: mole fraction

Notes: The checker will verify that X_B_matrix decreases monotonically with increasing radius, and will compare the values at three hidden radii (e.g., 5 nm, 20 nm, 100 nm) to digitized gold data from the paper's Figure 3, as well as check near flat-interface equilibrium at very large radius. No gold values are provided here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_gibbs_thomson_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "radius_nm",
          "X_B_matrix"
        ],
        "units": {
          "radius_nm": "nm",
          "X_B_matrix": "mole fraction"
        }
      },
      "description": "Equilibrium matrix Sn concentration vs precipitate radius for Pb-Sn binary alloy at 150 °C, computed from the paper's algorithm. The hidden checker compares this curve to the paper's reported result with tolerances and checks monotonicity."
    }
  ],
  "notes": "The checker will verify that X_B_matrix decreases monotonically with increasing radius, and will compare the values at three hidden radii (e.g., 5 nm, 20 nm, 100 nm) to digitized gold data from the paper's Figure 3, as well as check near flat-interface equilibrium at very large radius. No gold values are provided here."
}
```

## How you are scored
A hidden verifier independently examines every scored workflow artifact listed under 'Workflow steps' and combines the stage‑level rewards into a final score between 0 and 1. For the Gibbs–Thomson concentration curve (step_01_gibbs_thomson_curve.csv), the verifier will check that the submitted values follow a physically consistent trend (e.g., monotonic decrease of solute concentration with increasing radius) and will compare key numerical results against a hidden reference derived from the published study. Each scored step carries a weight that reflects its importance to the overall reproduction. Simply stating a known number without executing the required computations will not satisfy the verifier—the submitted artifacts must demonstrably originate from the described computational procedure.
