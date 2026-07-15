# Lattice-gas model for order-disorder transition of chemisorbed adlayer

## Problem background
Understanding the order-disorder transition of chemisorbed hydrogen on the Ni(111) surface is fundamental to surface science and catalysis. Earlier lattice-gas models predicted a spurious peak in the transition temperature and LEED intensity at 0.25 coverage, failing to reproduce the experimentally observed asymmetric phase diagram. This work refines the model by allowing domain mixtures and using only two distinct pair interactions, aiming to demonstrate that the asymmetry can arise without three-body terms.

## Approach
The model uses three interpenetrating sublattices (A, B = equivalent 3-fold hollow sites, C = top site). Configurational entropy is approximated by Kikuchi's 3-site cluster method, which accounts for correlations among two next-nearest 3-fold sites and the top site. The internal energy is expressed as a sum over 3-site cluster energies, containing only pair interactions; the dimensionless parameter V=1.22 is the ratio of the top–3-fold pair interaction to the 3-fold–3-fold pair interaction. For each combination of H-coverage θ and temperature T, the free energy F = U − T·S is minimized numerically subject to fixed total coverage and consistency constraints, yielding equilibrium occupation probabilities PA, PB, PC. The half-order LEED intensity is then computed as I = ((PA − PB)/2 − PC)². This approach eliminates explicit three-body interactions and allows the ordered phase to involve adlayer domain mixtures (PA ≠ PB).

## Reproduction target
Compute the equilibrium occupation probabilities PA, PB, PC and the half-order LEED intensity I for coverages θ from 0.10 to 0.75 (step 0.05) and temperatures T from 50 K to 300 K (step 10 K), using the lattice-gas model with V=1.22 and the Kikuchi entropy expression. Save the results in a CSV table (occupation_and_intensity.csv) with columns theta, T, PA, PB, PC, I. From this table the order-disorder transition temperature Tc(θ) can be derived as the inflection point of I(T) at each θ. The goal is to produce a CSV that faithfully reflects the model's physics; a hidden verifier will use the CSV to assess correctness.

## Assets

- SciPy: scipy

## Workflow steps

### Step 1: Lattice-gas model free energy minimization and LEED intensity calculation
- Role: scored (load-bearing)
- Action: Implement the lattice-gas model with three interpenetrating sublattices (A, B = equivalent 3-fold hollow sites, C = top site). Use Kikuchi's 3-site cluster approximation for configurational entropy and an internal energy expression containing only pair interactions with pair parameter V=1.22 (ratio of top-3fold to 3fold-3fold interaction). For each coverage θ from 0.10 to 0.75 in steps of 0.05 and each temperature T from 50 K to 300 K in steps of 10 K, minimize the free energy F = U - T*S subject to consistency constraints and fixed coverage, obtaining equilibrium occupation probabilities PA, PB, PC. Compute the half-order LEED intensity I = ((PA - PB)/2 - PC)^2. Save the results to occupation_and_intensity.csv.
- Output file: `/app/outputs/occupation_and_intensity.csv`
- Format: csv
- Contract: CSV with columns: theta (float, coverage), T (float, temperature in K), PA (float, occupation probability on sublattice A), PB (float, occupation probability on sublattice B), PC (float, occupation probability on sublattice C), I (float, half-order LEED intensity). Rows for theta in [0.10, 0.75] step 0.05 and T in [50,300] step 10 K.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/occupation_and_intensity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### occupation_and_intensity.csv
- path: `/app/outputs/occupation_and_intensity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Half-order LEED intensity and occupation probabilities from the lattice-gas model. The checker will re-derive the order-disorder transition temperature Tc(θ) from these data and compare both the intensity values and Tc(θ) to a hidden gold reference.
- schema:
  - `type`: table
  - `required_columns`: `theta`, `T`, `PA`, `PB`, `PC`, `I`
  - `units`:
    - `theta`: coverage fraction
    - `T`: K
    - `PA`: occupation probability
    - `PB`: occupation probability
    - `PC`: occupation probability
    - `I`: arbitrary intensity units

Notes: The agent must minimize the free energy numerically (e.g., using SciPy). The output CSV must cover the specified grid. The checker will evaluate the submitted I(θ,T) values and the derived Tc(θ) against a reference implementation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "occupation_and_intensity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "theta",
          "T",
          "PA",
          "PB",
          "PC",
          "I"
        ],
        "units": {
          "theta": "coverage fraction",
          "T": "K",
          "PA": "occupation probability",
          "PB": "occupation probability",
          "PC": "occupation probability",
          "I": "arbitrary intensity units"
        }
      },
      "description": "Half-order LEED intensity and occupation probabilities from the lattice-gas model. The checker will re-derive the order-disorder transition temperature Tc(θ) from these data and compare both the intensity values and Tc(θ) to a hidden gold reference."
    }
  ],
  "notes": "The agent must minimize the free energy numerically (e.g., using SciPy). The output CSV must cover the specified grid. The checker will evaluate the submitted I(θ,T) values and the derived Tc(θ) against a reference implementation."
}
```

## How you are scored
A hidden verifier reads your occupation_and_intensity.csv and derives Tc(θ) by locating the inflection point of I(T) for each θ. It compares your computed Tc(θ) values to a gold-standard reference (obtained from a faithful calculation of the same model) and also compares your I(θ,T) values to reference intensities. Each comparison contributes to a weighted score. Full credit requires both the intensity values and the derived transition temperatures to meet the verifier's accuracy criteria. Do not attempt to reverse-engineer the gold – implement the described lattice-gas model and free-energy minimization procedure to produce the correct physical results.
