# Classical Nucleation Theory Critical Size Calculation

## Problem background
Atmospheric aerosol droplets, such as those containing sulfuric acid, grow by taking up water vapour. The equilibrium size of such a solution droplet depends on the ambient relative humidity, the amount of dissolved solute, and the curvature of the droplet surface (the Kelvin effect). For a given dry particle of sulfuric acid, the equilibrium radius varies with humidity in a way that can be predicted from thermodynamic data and a modified Kelvin equation that accounts for changes in surface tension and density with concentration. This task requires you to compute these equilibrium radii for several dry sizes and relative humidities, generating the growth behaviour of aqueous H₂SO₄ droplets.

## Approach
The droplet is modelled as a binary solution of H₂SO₄ and H₂O. The modified Kelvin relation expresses the water saturation ratio S_w at the droplet surface in terms of the droplet radius r, the solution composition (mass percent acid X), the density ρ, the surface tension σ, and their composition derivatives dρ/dX and dσ/dX. By setting S_w = RH/100, the equilibrium radius that satisfies water equilibrium can be found for any dry nucleus size and ambient humidity. The required thermodynamic properties (ρ, dρ/dX, σ, dσ/dX, water activity a_w, and acid activity a_o) as functions of X are provided in the bundled file h2so4_properties.csv. For each dry radius (the radius the particle would have as pure acid), you will first convert to an acid mass using the density of pure H₂SO₄ (1.84 g/cm³). Then, for each RH condition, you will solve the nonlinear equation to obtain the equilibrium droplet radius r (in µm). Numerical interpolation of the tabulated properties will be needed when the solution composition falls between tabulated points.

## Reproduction target
Compute the equilibrium radii (in µm) of aqueous H₂SO₄ droplets for the following dry radii: 0.001, 0.005, 0.05, 0.1, and 0.5 µm, at each of these relative humidities: 0, 10, 30, 50, 70, 80, 90, 100, 101, and 110 %. Write the results to /app/outputs/growth_curve.csv with columns: dry_radius_um (float, µm), rh_pct (int, %), eq_radius_um (float, µm). There must be one row for every combination of dry radius and RH.

## Assets

- h2so4_properties.csv

## Workflow steps

### Step 1: Compute equilibrium radii
- Role: scored (load-bearing)
- Action: Implement the modified Kelvin equation using the provided physical property data from h2so4_properties.csv. For each given dry radius (0.001, 0.005, 0.05, 0.1, 0.5 µm) and each relative humidity (0, 10, 30, 50, 70, 80, 90, 100, 101, 110 %), solve for the equilibrium droplet radius r (in µm) such that the water saturation ratio S_w matches RH/100 (assuming S_w = RH/100). Use interpolation of the tabular properties as needed. Output the results to /app/outputs/growth_curve.csv.
- Output file: `/app/outputs/growth_curve.csv`
- Format: csv
- Contract: Columns: dry_radius_um (float, µm), rh_pct (int, %), eq_radius_um (float, µm). One row per (dry_radius_um, rh_pct) combination.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/growth_curve.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### growth_curve.csv
- path: `/app/outputs/growth_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium radii computed by solving the modified Kelvin equation. The checker will recompute eq_radius_um from the same input data and compare against the agent's values using a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `dry_radius_um`, `rh_pct`, `eq_radius_um`
  - `units`:
    - `dry_radius_um`: µm
    - `eq_radius_um`: µm

Notes: The checker independently solves the same equations with the same provided data to compute gold radii; it scores by comparing the agent's eq_radius_um against these recomputed values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "growth_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "dry_radius_um",
          "rh_pct",
          "eq_radius_um"
        ],
        "units": {
          "dry_radius_um": "µm",
          "eq_radius_um": "µm"
        }
      },
      "description": "Equilibrium radii computed by solving the modified Kelvin equation. The checker will recompute eq_radius_um from the same input data and compare against the agent's values using a tolerance."
    }
  ],
  "notes": "The checker independently solves the same equations with the same provided data to compute gold radii; it scores by comparing the agent's eq_radius_um against these recomputed values."
}
```

## How you are scored
A hidden verifier will independently solve the same modified Kelvin equation using the same thermodynamic data and constants to compute gold equilibrium radii for every dry radius and humidity in the target set. It will then compare your eq_radius_um values against those recomputed values. Your score is based on how close your computed radii are to the verifier’s radii, using a tolerance that accounts for the typical numerical variation of a correct solution. Meeting or exceeding the required accuracy on this scored output determines the reward. There is only one scored stage, so its result fully constitutes your final score.
