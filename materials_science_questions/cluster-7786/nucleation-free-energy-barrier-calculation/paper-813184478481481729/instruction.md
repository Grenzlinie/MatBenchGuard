# Ice Nucleation Active-Site Model Threshold Computation

## Problem background
In atmospheric ice nucleation, aerosol particles often trigger freezing, but the large observed variability in activity cannot be explained by particle size or average surface properties alone. This study proposes a model in which active nucleation sites are small‑scale re‑entrant topographical features (pits, corners) on the particle surface, whose lateral dimensions are comparable to the critical ice embryo. A nucleating particle is idealized as a sphere containing a conical pit, and classical nucleation theory is combined with a log‑normal distribution of pit areas to compute the fractional activity of a particle population: the fraction of particles of a given radius that become active freezing nuclei at a given temperature. The task is to implement this model and compute the freezing‑nucleation threshold temperatures for a set of particle radii and activity fractions under a specific choice of parameters, reproducing a key quantitative result of the theory.

## Approach
The reproduction proceeds in two conceptual stages. First, classical nucleation theory for heterogeneous freezing is applied to a single spherical particle of radius R bearing a conical pit of relative surface area α. Using the Kelvin relation for the critical embryo radius, the spherical‑cap factor f(m,x) from Fletcher, and the material parameters m=0.5, σ=20 erg cm⁻², ρ=1 g cm⁻³, ΔH_f=3.34 × 10⁹ erg g⁻¹, and T_m=273 K, the free‑energy barrier ΔG* for nucleation is computed. The nucleation rate J follows from the barrier and a standard kinetic prefactor; the temperature at which J reaches the experimental threshold (nucleation within 1 s) is obtained numerically, yielding a mapping from (R,α) to a single‑particle freezing threshold temperature. In the second stage, the population of particles is described by a log‑normal distribution of pit areas with most‑probable area A₀ = 2 × 10⁻¹⁵ cm², distribution width γ = 0.8, and surface roughness parameter β = 0.001. The probability that a particle of radius R possesses at least one pit of area ≥ αR² is computed via Poisson statistics, giving the fractional activity F(R,T). For each prescribed radius R and target fraction F, the temperature T that yields that fraction is found by inverting the (R,α) map, resulting in the final (R,F,T) triples.

## Reproduction target
Compute the freezing nucleation threshold temperature T (in °C) for a model population with parameters m=0.5, β=0.001, γ=0.8. For particle radii R = 100, 316, 1000 Å and activity fractions F = 0.1, 0.5, 0.9, determine the temperature below which that fraction of particles is active. Write the nine resulting (R, F, T) combinations to a CSV file with columns R_Angstrom (integer), F_fraction (float), T_Celsius (float). This set of temperatures captures the essence of the fractional activity curves predicted by the active‑site model.

## Assets

- Fletcher (1958) Size effect in heterogeneous nucleation: 10.1063/1.1744542
- Physical constants for water/ice as used in the paper
- Fletcher (1963) Nucleation by crystalline particles: 10.1063/1.1733883

## Workflow steps

### Step 1: Single-particle freezing threshold computation
- Role: process
- Action: Implement the classical nucleation theory model to compute, for a given particle radius R and conical pit relative area α, the freezing nucleation threshold temperature T (in °C). Use the model parameters m=0.5, the water/ice physical constants (σ=20 erg/cm², ρ=1 g/cm³, ΔH_f=3.34e9 erg/g, T_m=273 K), and the spherical cap factor f(m,x) from Fletcher (1958/1963). Determine T by solving the condition that the nucleation rate J reaches the experimental threshold (nucleation within 1 second). This builds the master relationship (R,α) → T needed in the population step.
- Evidence: none

### Step 2: Population fractional activity temperature calculation
- Role: scored (load-bearing)
- Action: Using a log-normal distribution of pit areas with parameters A₀=2×10⁻¹⁵ cm², γ=0.8, β=0.001, and the single-particle threshold relationship from Step 0, compute the temperature T (in °C) below which a given fraction F of particles of radius R becomes active. Perform this calculation for the nine (R,F) combinations: (100 Å, 0.1), (100 Å, 0.5), (100 Å, 0.9), (316 Å, 0.1), (316 Å, 0.5), (316 Å, 0.9), (1000 Å, 0.1), (1000 Å, 0.5), (1000 Å, 0.9). Write the results to step_01_thresholds.csv.
- Output file: `/app/outputs/step_01_thresholds.csv`
- Format: csv
- Contract: CSV with header: R_Angstrom (int, particle radius in Å), F_fraction (float, activity fraction), T_Celsius (float, temperature in °C). Exactly nine rows covering the requested (R,F) pairs.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_thresholds.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_thresholds.csv
- path: `/app/outputs/step_01_thresholds.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of freezing nucleation threshold temperatures for the active‑site model with parameters m=0.5, β=0.001, γ=0.8, for the nine combinations of particle radius (R=100, 316, 1000 Å) and activity fraction (F=0.1, 0.5, 0.9).
- schema:
  - `type`: table
  - `required_columns`: `R_Angstrom`, `F_fraction`, `T_Celsius`
  - `units`:
    - `R_Angstrom`: Å
    - `F_fraction`: dimensionless
    - `T_Celsius`: °C
  - `description`: The CSV must contain exactly nine rows for the (R,F) pairs specified in the step description. The values are expected to be the correct model outputs computed with the given parameters.

Notes: All computations use the classical nucleation theory model and the log‑normal pit‑area distribution described in the problem. The checker recomputes the expected T values using a reference implementation of the same model and compares the agent’s reported values within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_thresholds.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R_Angstrom",
          "F_fraction",
          "T_Celsius"
        ],
        "units": {
          "R_Angstrom": "Å",
          "F_fraction": "dimensionless",
          "T_Celsius": "°C"
        },
        "description": "The CSV must contain exactly nine rows for the (R,F) pairs specified in the step description. The values are expected to be the correct model outputs computed with the given parameters."
      },
      "description": "Table of freezing nucleation threshold temperatures for the active‑site model with parameters m=0.5, β=0.001, γ=0.8, for the nine combinations of particle radius (R=100, 316, 1000 Å) and activity fraction (F=0.1, 0.5, 0.9)."
    }
  ],
  "notes": "All computations use the classical nucleation theory model and the log‑normal pit‑area distribution described in the problem. The checker recomputes the expected T values using a reference implementation of the same model and compares the agent’s reported values within a tolerance."
}
```

## How you are scored
A hidden verifier independently computes the reference freezing‑threshold temperatures for the same nine (R,F) pairs using a faithful implementation of the identical nucleation model and parameters. Your submitted CSV is read and each reported T_Celsius is compared to the corresponding hidden reference value. Credit is earned for each (R,F) combination whose deviation is within a predetermined tolerance; the final score scales proportionally with the number of correct values. Successful reproduction therefore requires that your code correctly implements the nucleation physics described in the approach and workflow steps — simply outputting numerical values you may have encountered elsewhere is not sufficient and will not match the independently computed reference.
