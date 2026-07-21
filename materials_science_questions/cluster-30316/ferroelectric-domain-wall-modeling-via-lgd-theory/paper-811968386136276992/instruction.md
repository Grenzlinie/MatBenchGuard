# Ferroelectric domain formation in Stockmayer droplets via Monte Carlo simulation

## Problem background
Dipolar (Stockmayer) particles in a spherical droplet can exhibit correlated dipole orientations due to the long-range nature of dipole–dipole interactions. When the interaction between nearest neighbors is larger than the thermal energy, it is an open question whether ordered ferroelectric domains emerge and how the degree of order depends on the particle dipole moment. The distance-dependent Kirkwood factor Gₖ(R) measures the orientational correlation of dipoles within a sphere of radius R around a chosen central dipole and is the primary tool to detect and characterize such domains. This task investigates the structure of a droplet containing 10 000 Stockmayer particles at two different dipole moments, one where the dipole–dipole coupling is weak relative to thermal energy and one where it is strong, by computing Gₖ(R) curves and determining whether a large, electrostatically stabilized domain is present.

## Approach
Implement a Metropolis Monte Carlo simulation of Stockmayer particles, i.e., particles that interact via a Lennard‑Jones potential plus a dipole–dipole interaction. The particles are confined to a spherical droplet by a soft wall. Run two independent simulations, differing only in the particle dipole moment: a low‑coupling case (weak dipole) and a high‑coupling case (strong dipole). In each simulation, after suitable equilibration and a production run, compute the distance‑dependent Kirkwood factor Gₖ(R) for every particle in discrete radial steps. For the weak‑coupling case, save the Gₖ(R) curve for the particle closest to the droplet center. For the strong‑coupling case, for each particle identify the first significant maximum of Gₖ(R) that is separated from short‑range packing oscillations (roughly within the first 6 Å) by at least 1.59 Å in radius; then select the particle with the highest such maximum as the central dipole of the most important domain, and save its Gₖ(R) curve. Finally, process these curves to produce a JSON summary: for the weak coupling, confirm that no significant domain maximum exists; for the strong coupling, report the radius at which the first significant maximum occurs (the domain radius) and the peak Gₖ value at that radius.

## Reproduction target
Produce three artifacts:
1. `gk_curves_mu0.635.csv` – the Gₖ(R) curve for the particle nearest to the droplet center in the weak‑coupling simulation (one row per radial step).
2. `gk_curves_mu1.651.csv` – the Gₖ(R) curve for the central dipole of the most important domain identified in the strong‑coupling simulation (same format).
3. `domain_summary.json` – a structured summary containing, for each case, a boolean indicating whether a significant domain exists, the domain radius and maximum Gₖ value if it does (or null if it does not), together with the droplet radius (40.088 Å).

## Assets

- Python 3 scientific environment: https://www.python.org/

## Workflow steps

### Step 1: Simulation and G_k curve for low dipole moment
- Role: scored
- Action: Implement Metropolis Monte Carlo simulation of 10 000 Stockmayer particles (σ=2.8893 Å, ε=0.75kT, T=315.8 K, R_drop=40.088 Å, μ=0.635 D). Equilibrate for at least 1000 MC steps/particle, collect production statistics for at least 2000 steps/particle. Then compute the distance-dependent Kirkwood factor G_k(R) for the particle closest to the droplet center, in discrete steps of 0.53 Å, and save as CSV.
- Output file: `/app/outputs/gk_curves_mu0.635.csv`
- Format: csv
- Contract: Two columns: 'R' (float, units: Å) and 'G_k' (float, dimensionless). One row per radial step from 0 to the droplet radius, with a resolution of 0.53 Å.
- Scoring: scored by hidden verifier

### Step 2: Simulation and G_k curve for high dipole moment
- Role: scored (load-bearing)
- Action: Implement Metropolis Monte Carlo simulation of 10 000 Stockmayer particles (σ=2.8893 Å, ε=0.75kT, T=315.8 K, R_drop=40.088 Å, μ=1.651 D). Equilibrate for at least 1000 MC steps/particle, collect production statistics for at least 2000 steps/particle. Compute G_k(R) for every particle, identify the particle whose curve exhibits the highest first significant maximum (separated from short-range oscillations by at least 1.59 Å in R), and save that G_k(R) curve as CSV.
- Output file: `/app/outputs/gk_curves_mu1.651.csv`
- Format: csv
- Contract: Two columns: 'R' (float, units: Å) and 'G_k' (float, dimensionless). One row per radial step from 0 to the droplet radius, with a resolution of 0.53 Å.
- Scoring: scored by hidden verifier

### Step 3: Domain summary report
- Role: scored (load-bearing)
- Action: Read the two CSV files from the previous steps. For each case, analyze the G_k(R) curve, determine whether a significant maximum exists beyond the short-range packing oscillations (first 6 Å), and if so, extract its radius (R-value) and peak G_k value; then write a JSON summary reporting these quantities.
- Output file: `/app/outputs/domain_summary.json`
- Format: json
- Contract: JSON object with top-level keys 'mu0.635' and 'mu1.651'. Each value is an object with: (mu0.635) 'domain_exists': false, 'domain_radius_angstrom': null, 'Gk_max': null; (mu1.651) 'domain_exists': true, 'domain_radius_angstrom': <float>, 'Gk_max': <float>, 'droplet_radius_angstrom': 40.088.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/gk_curves_mu0.635.csv`
- `/app/outputs/gk_curves_mu1.651.csv`
- `/app/outputs/domain_summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### gk_curves_mu0.635.csv
- path: `/app/outputs/gk_curves_mu0.635.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Distance-dependent Kirkwood factor G_k(R) for the central particle in a 10 000-particle Stockmayer droplet with μ=0.635 D. The checker verifies that no significant domain maximum appears (G_k remains low, no maximum after 6 Å), consistent with weak coupling.
- schema:
  - `type`: table
  - `required_columns`: `R`, `G_k`
  - `units`:
    - `R`: Å
    - `G_k`: dimensionless

### gk_curves_mu1.651.csv
- path: `/app/outputs/gk_curves_mu1.651.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Distance-dependent Kirkwood factor G_k(R) for the central dipole of the most important ferroelectric domain in a 10 000-particle Stockmayer droplet with μ=1.651 D. The checker verifies that the curve exhibits a clear first significant maximum at R > 20 Å with G_k > 100, confirming strong-coupling domain formation.
- schema:
  - `type`: table
  - `required_columns`: `R`, `G_k`
  - `units`:
    - `R`: Å
    - `G_k`: dimensionless

### domain_summary.json
- path: `/app/outputs/domain_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Structured summary derived from the G_k curves. For μ=0.635 D, domain_exists must be false and the numeric fields null. For μ=1.651 D, domain_exists must be true, and the reported domain radius (Å) and peak G_k are compared against the paper’s reference values for the same system size within tolerances accounting for stochastic variation.
- schema:
  - `type`: object
  - `required`: `mu0.635`, `mu1.651`
  - `properties`:
    - `mu0.635`:
      - `type`: object
      - `required`: `domain_exists`, `domain_radius_angstrom`, `Gk_max`
    - `mu1.651`:
      - `type`: object
      - `required`: `domain_exists`, `domain_radius_angstrom`, `Gk_max`, `droplet_radius_angstrom`

Notes: All outputs must be produced after the respective Monte Carlo simulations. The domain summary must be internally consistent with the CSV curves. The scoring tolerances are hidden and account for the stochastic nature of the simulations.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "gk_curves_mu0.635.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "G_k"
        ],
        "units": {
          "R": "Å",
          "G_k": "dimensionless"
        }
      },
      "description": "Distance-dependent Kirkwood factor G_k(R) for the central particle in a 10 000-particle Stockmayer droplet with μ=0.635 D. The checker verifies that no significant domain maximum appears (G_k remains low, no maximum after 6 Å), consistent with weak coupling."
    },
    {
      "file": "gk_curves_mu1.651.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "G_k"
        ],
        "units": {
          "R": "Å",
          "G_k": "dimensionless"
        }
      },
      "description": "Distance-dependent Kirkwood factor G_k(R) for the central dipole of the most important ferroelectric domain in a 10 000-particle Stockmayer droplet with μ=1.651 D. The checker verifies that the curve exhibits a clear first significant maximum at R > 20 Å with G_k > 100, confirming strong-coupling domain formation."
    },
    {
      "file": "domain_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "mu0.635",
          "mu1.651"
        ],
        "properties": {
          "mu0.635": {
            "type": "object",
            "required": [
              "domain_exists",
              "domain_radius_angstrom",
              "Gk_max"
            ]
          },
          "mu1.651": {
            "type": "object",
            "required": [
              "domain_exists",
              "domain_radius_angstrom",
              "Gk_max",
              "droplet_radius_angstrom"
            ]
          }
        }
      },
      "description": "Structured summary derived from the G_k curves. For μ=0.635 D, domain_exists must be false and the numeric fields null. For μ=1.651 D, domain_exists must be true, and the reported domain radius (Å) and peak G_k are compared against the paper’s reference values for the same system size within tolerances accounting for stochastic variation."
    }
  ],
  "notes": "All outputs must be produced after the respective Monte Carlo simulations. The domain summary must be internally consistent with the CSV curves. The scoring tolerances are hidden and account for the stochastic nature of the simulations."
}
```

## How you are scored
A hidden verifier independently examines each output artifact. The two CSV curves are checked for structural properties. The domain summary JSON is compared against hidden reference values derived from the original study for the same system size and dipole moment, with tolerances that account for stochastic spread and implementation differences. Each stage is weighted, and the combined score determines the overall reproduction reward. The verifier also inspects the internal consistency between the CSV curves and the summary.
