# Activities of Na-K and Al-Mg Liquid Alloys via Pseudopotential Theory

## Problem background
Thermodynamic activities of components in liquid metal alloys are fundamental for understanding alloy phase stability, corrosion behaviour, and high-temperature processing. Modern microscopic electron theory, based on the pseudopotential formalism, provides a route to compute these activities from first principles using only the constituent elements' fundamental physical constants. This task asks you to compute the activity of Na in liquid Na-K at 384 K and the activity of Al in liquid Al-Mg at 1073 K by implementing such a pseudopotential-based theory. The produced activity values can later be compared with independent experimental measurements to assess the predictive power of the approach.

## Approach
The calculation framework combines the Gibbs‑Bogoliubov inequality with a hard‑sphere reference system and a pseudopotential treatment of the electron‑ion interactions. The total free energy is split into a hard‑sphere part and an electronic part. The hard‑sphere contribution is evaluated from the standard hard‑sphere model using a packing fraction of 0.45 and hard‑sphere diameters from the literature. The electronic part includes kinetic, exchange, correlation, uniform, Madelung, band‑structure, and core‑core terms. The band‑structure and Madelung contributions are built from pair interaction energies Φ_ij = R_ij + φ_ij + ξ_ij, where R_ij is an electrostatic integral involving the alloy partial structure factors computed within the hard‑sphere model, φ_ij is a band‑structure integral that depends on the empty‑core pseudopotential and the dielectric function with the Hubbard‑Sham exchange‑correlation factor, and ξ_ij is a core‑core repulsion integral using Born‑Mayer type potentials. The chemical potential of a component is obtained by differentiating the free energy expressions, and its activity follows from the difference between the chemical potential in the alloy and in the pure liquid. The required integrals are one‑dimensional over wave‑vector magnitude q and inter‑particle distance r.

## Reproduction target
Compute the activity of Na in liquid Na-K at T = 384 K for mole fractions x_Na = 0.1, 0.3, 0.5, 0.7, 0.9, and the activity of Al in liquid Al-Mg at T = 1073 K for x_Al = 0.1, 0.3, 0.5, 0.7, 0.9. Use the Hubbard‑Sham exchange‑correlation factor for the dielectric function throughout. Write the results to two CSV files: `/app/outputs/activities_NaK.csv` with columns `x_Na` and `a_Na`, and `/app/outputs/activities_AlMg.csv` with columns `x_Al` and `a_Al`. Both activities are dimensionless.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Evaluate pseudopotential integrals
- Role: process
- Action: Compute the electrostatic integral R_ij, band-structure integral φ_ij, and core-core integral ξ_ij for the Na-K and Al-Mg alloy systems using the empty-core pseudopotential, the Hubbard-Sham exchange-correlation factor for the dielectric function, hard-sphere partial structure factors (packing density 0.45, diameters as specified), and Born-Mayer core repulsion parameters. Combine these to obtain the composite interaction Φ_ij = R_ij + φ_ij + ξ_ij.
- Evidence: `/app/outputs/pseudopotential_integrals.json`

### Step 2: Compute activity of Na in Na-K alloy
- Role: scored (load-bearing)
- Action: At temperature 384 K and compositions x_Na = 0.1, 0.3, 0.5, 0.7, 0.9, compute the hard-sphere chemical potential μ_Na^hs and the electronic contributions using the previously computed Φ_ij, then obtain the activity a_Na. Write results to a CSV file.
- Output file: `/app/outputs/activities_NaK.csv`
- Format: csv
- Contract: Two columns: x_Na (mole fraction of Na) and a_Na (activity, dimensionless)
- Scoring: scored by hidden verifier

### Step 3: Compute activity of Al in Al-Mg alloy
- Role: scored (load-bearing)
- Action: At temperature 1073 K and compositions x_Al = 0.1, 0.3, 0.5, 0.7, 0.9, compute the hard-sphere chemical potential μ_Al^hs and the electronic contributions using the previously computed Φ_ij, then obtain the activity a_Al. Write results to a CSV file.
- Output file: `/app/outputs/activities_AlMg.csv`
- Format: csv
- Contract: Two columns: x_Al (mole fraction of Al) and a_Al (activity, dimensionless)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/activities_NaK.csv`
- `/app/outputs/activities_AlMg.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### activities_NaK.csv
- path: `/app/outputs/activities_NaK.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Activity of Na in liquid Na-K alloy at 384 K. The checker compares each reported activity to a hidden gold value; absolute deviation ≤ 0.05 earns full credit, larger deviation earns partial credit.
- schema:
  - `type`: table
  - `required_columns`: `x_Na`, `a_Na`
  - `units`:
    - `x_Na`: dimensionless
    - `a_Na`: dimensionless

### activities_AlMg.csv
- path: `/app/outputs/activities_AlMg.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Activity of Al in liquid Al-Mg alloy at 1073 K. The checker compares each reported activity to a hidden gold value; absolute deviation ≤ 0.05 earns full credit, larger deviation earns partial credit.
- schema:
  - `type`: table
  - `required_columns`: `x_Al`, `a_Al`
  - `units`:
    - `x_Al`: dimensionless
    - `a_Al`: dimensionless

Notes: Only the Hubbard-Sham dielectric function is required. The agent must implement the full hard-sphere and pseudopotential formalism; no pre-computed parameters are provided.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "activities_NaK.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_Na",
          "a_Na"
        ],
        "units": {
          "x_Na": "dimensionless",
          "a_Na": "dimensionless"
        }
      },
      "description": "Activity of Na in liquid Na-K alloy at 384 K. The checker compares each reported activity to a hidden gold value; absolute deviation ≤ 0.05 earns full credit, larger deviation earns partial credit."
    },
    {
      "file": "activities_AlMg.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "x_Al",
          "a_Al"
        ],
        "units": {
          "x_Al": "dimensionless",
          "a_Al": "dimensionless"
        }
      },
      "description": "Activity of Al in liquid Al-Mg alloy at 1073 K. The checker compares each reported activity to a hidden gold value; absolute deviation ≤ 0.05 earns full credit, larger deviation earns partial credit."
    }
  ],
  "notes": "Only the Hubbard-Sham dielectric function is required. The agent must implement the full hard-sphere and pseudopotential formalism; no pre-computed parameters are provided."
}
```

## How you are scored
A hidden verifier will independently evaluate each of your scored output files. For every composition point, it compares your computed activity to a hidden reference value. Small deviations earn full credit for that point; larger deviations earn partial credit. The verifier also checks that your results satisfy expected physical trends (e.g., the sign of deviation from ideal‑solution behaviour). The final score is a weighted combination of all points. Simply reporting the paper's numbers without performing the actual computation will not satisfy the requirement — you must implement the full pipeline.
