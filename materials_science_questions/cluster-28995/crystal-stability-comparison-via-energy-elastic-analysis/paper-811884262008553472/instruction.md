# Compute strain-induced elastic interaction energies for interstitial pairs in hcp metals

## Problem background
Hydrogen and deuterium atoms dissolve interstitially in hcp rare earth metals (Sc, Y, Tb, Dy, Ho, Er, Lu). Understanding the strain‑induced (elastic) pair interaction energies between these interstitial atoms is important for predicting solid‑solution structure, ordering, and phase behaviour. This task computes the interaction energies for H‑H and D‑D pairs in the first 14 coordination shells of the hcp host lattice.

## Approach
The strain‑induced interaction energy W for a pair of identical interstitial atoms can be expressed as a quadratic function of the lattice distortion anisotropy parameter θ = L_xx / L_zz. For each host metal and each coordination shell, universal coefficients α, ε, and μ are used together with the concentration‑expansion coefficients L_zz and θ of the interstitial species. The energy is computed as:

    W = L_zz² × (α + ε·θ + μ·θ²)

Values of α, ε, and μ for 14 shells in Sc, Y, Tb, Dy, Ho, Er, and Lu are provided in `alpha_epsilon_mu.csv`. Values of L_zz and θ for H and D in the same metals are provided in `conc_expansion.csv`. The task applies this formula to every metal–isotope–shell combination where input data exist and writes the resulting energies to a CSV.

## Reproduction target
For every combination of metal (Sc, Y, Tb, Dy, Ho, Er, Lu), isotope (H, D), and coordination shell (1 through 14), compute the strain‑induced interaction energy W (in meV) using the quadratic formula with the coefficients from the supplied CSV files. Write all results to `/app/outputs/interaction_energies.csv` with columns: `metal`, `shell`, `isotope`, `W_meV`.

## Assets

- alpha_epsilon_mu.csv
- conc_expansion.csv

## Workflow steps

### Step 1: Compute strain-induced interaction energies
- Role: scored
- Action: Read the provided alpha_epsilon_mu.csv and conc_expansion.csv. For each metal (Sc, Y, Tb, Dy, Ho, Er, Lu) and isotope (H, D) combination where input data exists, and for each of the 14 coordination shells (shell order must match the paper's 14-shell enumeration), compute the elastic interaction energy W (in meV) as W = L_zz^2 * (α + ε*θ + μ*θ^2) using the corresponding coefficients and expansion parameters. Write all results to /app/outputs/interaction_energies.csv.
- Output file: `/app/outputs/interaction_energies.csv`
- Format: csv
- Contract: columns: metal (string, one of Sc,Y,Tb,Dy,Ho,Er,Lu), shell (integer 1-14), isotope (string, H or D), W_meV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/interaction_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### interaction_energies.csv
- path: `/app/outputs/interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Strain-induced elastic pair interaction energies for H-H and D-D pairs in hcp rare earth metals for 14 coordination shells.
- schema:
  - `type`: table
  - `required_columns`: `metal`, `shell`, `isotope`, `W_meV`
  - `column_types`:
    - `metal`: string
    - `shell`: integer
    - `isotope`: string
    - `W_meV`: float
  - `units`:
    - `W_meV`: meV

Notes: The checker will independently recompute expected W values from the same input data and compare each row within a tolerance; it will also verify that W < 0 for shells 1 and 2.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "metal",
          "shell",
          "isotope",
          "W_meV"
        ],
        "column_types": {
          "metal": "string",
          "shell": "integer",
          "isotope": "string",
          "W_meV": "float"
        },
        "units": {
          "W_meV": "meV"
        }
      },
      "description": "Strain-induced elastic pair interaction energies for H-H and D-D pairs in hcp rare earth metals for 14 coordination shells."
    }
  ],
  "notes": "The checker will independently recompute expected W values from the same input data and compare each row within a tolerance; it will also verify that W < 0 for shells 1 and 2."
}
```

## How you are scored
A hidden verifier independently recomputes the expected interaction energies from the same input data and compares each row of your output within a tolerance. The verifier also checks that selected coordination shells exhibit the required sign (attractive or repulsive). Your reward is proportional to the fraction of rows that pass all checks.
