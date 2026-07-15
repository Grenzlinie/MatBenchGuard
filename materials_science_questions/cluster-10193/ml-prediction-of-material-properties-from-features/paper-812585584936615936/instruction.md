# AI-aided Virtual Screening Recipe for 2D Materials Discovery

## Problem background
Two-dimensional (2D) materials hold great promise for electronics and energy applications, but the search for new stable candidates is a massive combinatorial challenge. The chemical space of possible compositions, built from a modest set of crystal prototypes and a handful of chemical elements, easily reaches millions of candidates, far too many for exhaustive first-principles calculations. This work addresses the need for an efficient virtual screening pipeline that can navigate that enormous space and identify the subset of materials that are likely to be stable and thus experimentally relevant.

## Approach
The screening recipe has three core stages. First, a brute-force enumeration generates every possible stoichiometric combination of A-type cations and B-type anions within a curated set of 22 crystal prototypes, producing an exhaustive library of candidate compositions. Second, two structural/chemical filters are applied: a symmetry filter that removes geometrically duplicate copies, and a neutrality filter that discards compositions incapable of forming a charge-neutral compound based on standard oxidation states. Third, artificial neural networks (ANNs) trained on a public database of DFT-computed 2D materials predict three stability indicators—whether a material is stable, its heat of formation, and its energy above the convex hull—and only candidates that meet all three stability thresholds are retained. The entire workflow uses elemental-level features that require no further quantum calculations, making it feasible to screen tens of millions of candidates.

## Reproduction target
Your goal is to implement and execute the full downselection pipeline and record the per-prototype candidate counts after each filtering stage. The final output is a single CSV file, step_01_counts.csv, that contains, for each of the 22 crystal prototypes and for the total pool, the number of candidates after brute-force generation, after symmetry filtering, after neutrality filtering, and after the final stability filter. The pipeline must be run from scratch using the publicly available training data and the specified prototype and element lists; the correctness of the pipeline is judged by the distribution of final candidate counts across prototypes, not by any single number.

## Assets

- Computational 2D Materials Database (C2DB): https://cmr.ku.dk/c2db/
- V2DB generation and filtering reference code: https://doi.org/10.24433/CO.7049461.v1
- Greenwood's tabulated elemental charge states
- Python packages (numpy, pandas, scikit-learn): pip

## Workflow steps

### Step 1: Prepare training data and define screening scope
- Role: process
- Action: Download C2DB and apply filtering criteria (dynamic stability, band gap data, minimum 10 training instances per element) to obtain a curated training set of 2226 materials. Use the following 22 crystal prototypes with their unit-cell groups and symmetry types:
  - AB group: BN (Z), GeSe (Z)
  - ABB group: BiTeI (Z), CdI₂ (Y), GeS₂ (Y), MoS₂ (Y), MoSSe (Z)
  - AABB group: AuSe (Y), CH (XY), FeSe (XY), GaS (XY), GaSe (XY), ISb (XY), NiSe (XY), PbS (XY), PbSe (XY), RhO (Z), SnS (XY)
  - AABBBB group: FeOCl (XYY), MnS₂ (XYY), PdS₂ (XYY), WTe₂ (XY)
  Classify the 52 chemical elements into A-type cations (42 elements: H, Li, Na, K, Rb, Cs, Be, Mg, Ca, Sr, Ba, Ti, Zr, Hf, V, Nb, Ta, Cr, Mo, W, Mn, Re, Fe, Ru, Os, Co, Rh, Ir, Ni, Pd, Pt, Cu, Ag, Au, Zn, Cd, Hg, Al, Ga, In, Tl, Sn, Pb) and B-type anions (10 elements: C, N, O, F, Si, P, S, Cl, Se, Te).
- Evidence: `/app/outputs/training_data.csv`

### Step 2: Train stability ANN models
- Role: process
- Action: Extract element-level features (atoms per unit-cell, prototype vector, composition ratio vector, Pauling electronegativity geometric mean) from the curated training data. Train separate ANN models (MLPClassifier/MLPRegressor) to predict the binary 'is_stable' label, the heat of formation ΔH (eV/atom), and the energy above convex hull ΔH_hull (eV/atom).
- Evidence: `/app/outputs/stability_models.pkl`

### Step 3: Generate candidate compositions
- Role: process
- Action: For each of the 22 prototypes, enumerate all possible compositions by brute-force substitution: A-type sites can only be replaced by A-type elements, B-type sites only by B-type elements. Produce the raw list of 72,522,240 candidate compositions.
- Evidence: `/app/outputs/generated_candidates.csv`

### Step 4: Apply symmetry filter
- Role: process
- Action: Assign symmetry labels (Z, X, Y, XY, XYY) to each candidate based on prototype symmetry rules. Remove geometrical duplicates that share the same prototype and symmetry label, reducing the pool to the unique compositions.
- Evidence: `/app/outputs/symmetry_filtered.csv`

### Step 5: Apply neutrality filter
- Role: process
- Action: For each symmetry-unique candidate, enumerate possible formal charge combinations using Greenwood's tabulated charge states, enforcing A-type positive and B-type negative charges. Remove any composition with no neutral charge combination.
- Evidence: `/app/outputs/neutrality_filtered.csv`

### Step 6: Apply stability filter and export per‑prototype counts
- Role: scored (load-bearing)
- Action: Use the trained ANN models to predict is_stable, ΔH, and ΔH_hull for each neutrality-filtered candidate. Retain candidates that satisfy is_stable=True, ΔH < 0.2 eV/atom, and ΔH_hull < 0.2 eV/atom. Compute per‑prototype counts after each stage (total generated, after symmetry, after neutrality, after stability) and a total row. Write the results to a CSV file named step_01_counts.csv.
- Output file: `/app/outputs/step_01_counts.csv`
- Format: csv
- Contract: CSV with columns: prototype (string), total_generated (int), after_symmetry (int), after_neutrality (int), after_stability (int). One row per prototype plus a final row with prototype='Total'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_counts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_counts.csv
- path: `/app/outputs/step_01_counts.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per‑prototype candidate counts after each filtering stage, compared against hidden reference values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `prototype`, `total_generated`, `after_symmetry`, `after_neutrality`, `after_stability`
  - `column_types`:
    - `prototype`: string
    - `total_generated`: integer
    - `after_symmetry`: integer
    - `after_neutrality`: integer
    - `after_stability`: integer

Notes: The counts are verified against hidden gold values (the paper’s Table 1). The checker uses appropriate tolerances and a Spearman correlation check on the final per‑prototype distribution.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "prototype",
          "total_generated",
          "after_symmetry",
          "after_neutrality",
          "after_stability"
        ],
        "column_types": {
          "prototype": "string",
          "total_generated": "integer",
          "after_symmetry": "integer",
          "after_neutrality": "integer",
          "after_stability": "integer"
        }
      },
      "description": "Per‑prototype candidate counts after each filtering stage, compared against hidden reference values from the paper."
    }
  ],
  "notes": "The counts are verified against hidden gold values (the paper’s Table 1). The checker uses appropriate tolerances and a Spearman correlation check on the final per‑prototype distribution."
}
```

## How you are scored
A hidden verifier reads your step_01_counts.csv and compares each cell to reference values that represent the expected outcome of the pipeline. Small numerical discrepancies are allowed, and the comparison accounts for the fact that machine learning training is non-deterministic. In addition to cell-level checks, the verifier examines whether the relative distribution of final per-prototype counts matches the expected pattern, using rank-order correlation. You do not need to hit any exact target; a faithful reproduction of the screening methodology will produce a count distribution that passes the verifier’s structural and numerical checks.
