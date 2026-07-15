# Lattice Gas Quasichemical Model: Spinodal and Density Maxima in 3D

## Problem background
Supercooled liquids can potentially encounter two fundamental limits: the Kauzmann temperature, where the liquid would have lower entropy than the crystal, and a spinodal curve, where the liquid becomes mechanically unstable. The conditions under which a spinodal can appear are constrained by the virial theorem. Microscopically, core softening—a curvature change in the repulsive part of the pair potential—allows the formation of open structures that can collapse to denser arrangements upon heating or compression, leading to density anomalies (negative thermal expansion) and possible mechanical instability upon supercooling. A minimal model exhibiting these features is a lattice gas with attractive nearest-neighbour interactions and repulsive next-nearest-neighbour interactions, treated in the quasichemical approximation. Within this model, it is predicted that a three-dimensional simple cubic lattice can display density maxima and a reentrant spinodal under certain parameter choices. The goal of this task is to compute these thermodynamic features from first principles using the quasichemical equations.

## Approach
You will implement the quasichemical approximation for a three-dimensional lattice gas on a simple cubic lattice with nearest-neighbour attraction of strength ε and next-nearest-neighbour repulsion λε, using λ = 1. In this approximation, the equation of state and chemical potential are given parametrically through a variable r that is related to the fractional coverage ρ = M/N. For a given temperature T* (kT/ε) and density ρ, you will solve for r numerically, then compute the dimensionless pressure P* (Pv₀/ε) and chemical potential μ* (μ/ε). Using this EOS, you will: (a) compute the binodal (liquid–vapour coexistence) curve by performing a Maxwell construction—solving for pairs of densities at each temperature that have equal pressure and equal chemical potential; (b) locate the spinodal curve by tracing points where ∂P*/∂ρ = 0, which bounds the region of mechanical stability; (c) determine the locus of density maxima by scanning isobars and locating points where ∂ρ/∂T* = 0. All these calculations must be carried out for λ = 1 over a range of temperatures and pressures sufficient to capture the full shape of each curve.

## Reproduction target
Your concrete deliverable consists of two CSV files:
- phase_diagram_3d.csv: columns curve_type (either 'binodal' or 'spinodal'), T_star (dimensionless temperature), P_star (dimensionless pressure). Provide at least 20 points for each curve type, with resolution high enough to resolve all features of the phase diagram.
- density_maxima_3d.csv: columns T_star, P_star, and rho (fractional coverage). Provide at least 10 points spanning the entire locus of density maxima.
The successful computation of these curves from the model equations will demonstrate an independent reproduction of the thermodynamic predictions of the core-softened lattice gas in three dimensions.

## Assets

- Python 3 with NumPy and SciPy: numpy, scipy

## Workflow steps

### Step 1: Implement quasichemical approximation for the 3D lattice gas
- Role: process
- Action: Implement the parametric quasichemical equations for a simple cubic lattice gas with nearest‑neighbour attraction and next‑nearest‑neighbour repulsion (λ=1). Build numerical routines to evaluate the equation of state: pressure P*(ρ,T*) and chemical potential μ*(ρ,T*) by solving for the parameter r at given density ρ and temperature T*. Validate that isotherms and isobars behave qualitatively as expected.
- Evidence: none

### Step 2: Compute binodal and spinodal curves
- Role: scored (load-bearing)
- Action: Using the implemented EOS, find the binodal (coexistence) curve by solving for pairs of densities at each temperature such that the pressures and chemical potentials of the two phases are equal (Maxwell construction). Determine the spinodal points where the mechanical stability condition ∂P*/∂ρ = 0. For each binodal point record T_star and P_star; for each spinodal point record T_star and P_star. Ensure both curves cover the full coexistence region and the spinodal branches (including the reentrant shape).
- Output file: `/app/outputs/phase_diagram_3d.csv`
- Format: csv
- Contract: Columns: curve_type (string: 'binodal' or 'spinodal'), T_star (float, dimensionless temperature kT/ε), P_star (float, dimensionless pressure Pv₀/ε). At least 20 points per curve type, with sufficient resolution to capture all features.
- Scoring: scored by hidden verifier

### Step 3: Compute density maxima locus
- Role: scored
- Action: From the EOS, generate isobars ρ(T*) at various constant pressures. For each isobar, find points where ∂ρ/∂T* = 0 (density maxima). Scan a range of pressures to map the entire locus of density maxima. Record T_star, P_star, and the corresponding density rho (fractional coverage).
- Output file: `/app/outputs/density_maxima_3d.csv`
- Format: csv
- Contract: Columns: T_star (float), P_star (float), rho (float, dimensionless density M/N). At least 10 points covering the full extent of the locus.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phase_diagram_3d.csv`
- `/app/outputs/density_maxima_3d.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phase_diagram_3d.csv
- path: `/app/outputs/phase_diagram_3d.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV containing binodal and spinodal points. The agent's curves must fall within a pre‑set tolerance of independently computed reference curves, with lower RMS deviation being better.
- schema:
  - `type`: table
  - `required_columns`: `curve_type`, `T_star`, `P_star`
  - `units`:
    - `T_star`: dimensionless (kT/ε)
    - `P_star`: dimensionless (Pv₀/ε)

### density_maxima_3d.csv
- path: `/app/outputs/density_maxima_3d.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: CSV containing points on the density‑maxima locus. The agent's points must lie within tolerance of reference points, with lower deviation scoring higher.
- schema:
  - `type`: table
  - `required_columns`: `T_star`, `P_star`, `rho`
  - `units`:
    - `T_star`: dimensionless (kT/ε)
    - `P_star`: dimensionless (Pv₀/ε)
    - `rho`: dimensionless fractional coverage

Notes: The checker will compare the submitted curves to independently derived reference curves using tolerance‑based metrics (e.g., RMS deviation) and will also verify structural properties (e.g., reentrant spinodal shape, location of density‑maxima locus). Scoring is monotonic in quality: better agreement with the reference (within tolerance) yields full credit; deviation beyond tolerance reduces credit proportionally.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phase_diagram_3d.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "curve_type",
          "T_star",
          "P_star"
        ],
        "units": {
          "T_star": "dimensionless (kT/ε)",
          "P_star": "dimensionless (Pv₀/ε)"
        }
      },
      "description": "CSV containing binodal and spinodal points. The agent's curves must fall within a pre‑set tolerance of independently computed reference curves, with lower RMS deviation being better."
    },
    {
      "file": "density_maxima_3d.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_star",
          "P_star",
          "rho"
        ],
        "units": {
          "T_star": "dimensionless (kT/ε)",
          "P_star": "dimensionless (Pv₀/ε)",
          "rho": "dimensionless fractional coverage"
        }
      },
      "description": "CSV containing points on the density‑maxima locus. The agent's points must lie within tolerance of reference points, with lower deviation scoring higher."
    }
  ],
  "notes": "The checker will compare the submitted curves to independently derived reference curves using tolerance‑based metrics (e.g., RMS deviation) and will also verify structural properties (e.g., reentrant spinodal shape, location of density‑maxima locus). Scoring is monotonic in quality: better agreement with the reference (within tolerance) yields full credit; deviation beyond tolerance reduces credit proportionally."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that has access to independently generated reference curves for the same model. For the phase diagram file, the verifier will compare your binodal and spinodal points to the reference, calculating deviation metrics for each curve type separately. For the density maxima file, it will compare your points along the locus to the reference. The verifier will also examine the topological structure of the curves (e.g., the shape of the spinodal, the relative location of the density maxima) to ensure physical consistency. Each scored artifact receives a partial reward, and the total reward is a weighted combination. The closer your computed points are to the reference curves, the higher your score. Simply reporting expected numbers without correct underlying computations will not pass the structural checks.
