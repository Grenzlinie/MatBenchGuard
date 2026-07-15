# Topological indices and feature selection for CaCl₂ heat of formation prediction

## Problem background
This task explores the use of graph-theoretical topological indices to characterize the calcium chloride (CaCl₂) crystal network and to identify which indices best predict its heat of formation (HOF). In chemical graph theory, molecules are represented as graphs where vertices correspond to atoms and edges to bonds, and topological indices are numerical descriptors computed from the graph structure. By computing degree-based indices and their coindices and reverse variants, and then applying feature selection and regression analysis, we can determine the most influential descriptors for predicting a physicochemical property. The goal is to reproduce the computational pipeline that computes these indices, performs exhaustive feature selection, and ranks them by predictive performance, without assuming which indices will emerge as most important.

## Approach
The workflow begins by modeling the CaCl₂ unit cell as a graph with known edge-type frequencies as functions of the cell dimensions m and n. Using these edge counts, a set of degree-based topological indices (Randić with exponents 1, -1, 1/2, -1/2; atom-bond connectivity; geometric-arithmetic; forgotten; augmented Zagreb; first and second Zagreb; and redefined Zagreb indices 1–3) are computed by summing per-edge contributions. Coindices are computed similarly from the complement graph's edge partition, and reverse indices are computed using reverse vertex degrees (max-degree minus degree plus one). All indices are evaluated for m,n = 1,…,100, yielding a dataset of 10,000 points. The heat of formation for each cell is computed from a formula that depends only on m and n.

The index features are then normalized to zero mean and unit variance. To assess individual predictive power, exhaustive feature selection is performed using a linear regression estimator with 5-fold cross-validation and R² as the scoring metric, evaluating each index in isolation (max_features=1). The indices are ranked by their average R² score. In parallel, eight diverse regression models (Adaptive Boosting, Extra Trees, Random Forest, F-Regression, Gradient Boosting, LassoCV, RidgeCV, and Multi-Linear Regression) are trained on the full feature set to predict HOF, and the absolute feature importances are extracted. These are averaged across models to produce a second ranking. The two rankings are then examined to identify which indices consistently appear at the top.

## Reproduction target
Produce the following three artifacts:

1. A CSV file indices_values.csv containing computed values of all topological indices, coindices, and reverse indices for every (m,n) pair with m,n ∈ {1,…,100}.
2. A CSV file feature_selection_ranking.csv listing each index and its average R² score from exhaustive feature selection (max_features=1), sorted by descending score.
3. A CSV file regression_ranking.csv listing each index and its average absolute feature weight across eight regression models, sorted by descending weight.

The task is to implement the edge-partition summation, HOF calculation, normalization, feature selection, and regression models as described in the workflow steps, and to output these three files. The rankings should be determined solely by the computations; no prior knowledge of expected top indices is needed.

## Assets

- numpy: numpy
- pandas: pandas
- scikit-learn: scikit-learn
- mlxtend: mlxtend

## Workflow steps

### Step 1: Compute topological indices, coindices, and reverse indices
- Role: scored
- Action: Vertex partition of CaCl₂ (frequencies of each vertex degree):
  deg 1: 8
  deg 2: 4mn - 4m + 4n + 8
  deg 3: 2mn
  deg 4: 2mn - 2m - 2n + 2
  deg 6: 2mn
Total vertices V = 10mn - 6m + 2n + 18.

Original-graph edge partition (edge types and frequencies):
  (1,2): 4
  (1,3): 4
  (2,2): 4m + 4n - 8
  (2,3): 4m + 4n - 8
  (2,4): 4mn - 4m - 4n + 4
  (2,6): 4mn
  (3,4): 4mn - 4m - 4n + 4
  (3,6): 2mn

Compute each degree-based topological index for the original graph by summing the per-edge contribution (using the index formula) weighted by the edge-type frequency above, for every (m,n) pair from 1 to 100.

For coindices, construct the complement graph. In the complement graph each vertex degree is ξ̄ = V − 1 − ξ. The number of complement edges between two original-degree groups A and B (with original degrees a,b and frequencies f_a, f_b) equals the total possible edges between those groups minus the original edges: if a≠b: f_a·f_b − (original (a,b) edges); if a=b: f_a·(f_a−1)/2 − (original (a,a) edges). Compute each coindex by summing the per-edge contribution using the complement degrees ξ̄, weighted by the complement edge frequencies, for every (m,n) pair.

For reverse indices, define the reverse vertex degree η[ξ] = 6 − ξ + 1 (max degree is 6). The reverse vertex degree frequencies are:
  η = 6: 8
  η = 5: 4mn − 4m + 4n + 8
  η = 4: 2mn
  η = 3: 2mn − 2m − 2n + 2
  η = 1: 2mn
The reverse edge partition (by reverse-degree-pair types) is:
  (5,6): 4
  (4,6): 4
  (5,5): 4m + 4n − 8
  (4,5): 4m + 4n − 8
  (3,5): 4mn − 4m − 4n + 4
  (1,5): 4mn
  (3,4): 4mn − 4m − 4n + 4
  (1,4): 2mn
Compute each reverse index by summing the per-edge contribution using the reverse degrees η, weighted by the reverse edge frequencies, for every (m,n) pair.

Save all computed values (original indices, coindices, and reverse indices) to a CSV.
- Output file: `/app/outputs/indices_values.csv`
- Format: csv
- Contract: Header: m, n, then columns for each index (Randic indices R1, Rm1, R12, Rm12; ABC, GA, F, AZI, M1, M2, ReZG1, ReZG2, ReZG3; coindices CR1, CRm1, CR12, CRm12, CABC, CGA, CF, CAZI, CM1, CM2, CReZG1, CReZG2, CReZG3; reverse indices RR1, RRm1, RR12, RRm12, RABC, RGA, RF, RAZI, RM1, RM2, RReZG1, RReZG2, RReZG3). Each row: m (int), n (int), then float values for all indices.
- Scoring: scored by hidden verifier

### Step 2: Compute heat of formation
- Role: process
- Action: Compute HOF for each (m,n) cell using HOF(m,n) = ((m+n)^2 * (-795.8)) / 60.22.
- Evidence: `/app/outputs/hof.csv`

### Step 3: Normalize index features
- Role: process
- Action: Scale the index features (all columns except m,n,HOF) to zero mean and unit variance.
- Evidence: none

### Step 4: Exhaustive feature selection ranking
- Role: scored (load-bearing)
- Action: Perform exhaustive feature selection using mlxtend's ExhaustiveFeatureSelector with linear regression, 5-fold cross-validation, and R² scoring. Use normalized index features as predictors and HOF as target. For max_features=1, record the average R² score for each singleton index. Rank indices by descending R² and output to feature_selection_ranking.csv.
- Output file: `/app/outputs/feature_selection_ranking.csv`
- Format: csv
- Contract: Header: idx, score. Rows sorted by descending score. idx is the index name (string), score is the average R² (float).
- Scoring: scored by hidden verifier

### Step 5: Regression model feature importance ranking
- Role: scored (load-bearing)
- Action: Train eight regression models (Adaptive Boosting, Extra Trees, Random Forest, F-Regression, Gradient Boosting, LassoCV, RidgeCV, Multi-Linear Regression) on the full set of normalized index features predicting HOF. For each model, extract absolute feature weights/importances for each index. Compute the average absolute weight across models. Rank indices by descending average weight and save to regression_ranking.csv.
- Output file: `/app/outputs/regression_ranking.csv`
- Format: csv
- Contract: Header: idx, avg_weight. Rows sorted by descending avg_weight. idx is the index name (string), avg_weight is the averaged absolute weight (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/indices_values.csv`
- `/app/outputs/feature_selection_ranking.csv`
- `/app/outputs/regression_ranking.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### indices_values.csv
- path: `/app/outputs/indices_values.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed topological indices, coindices, and reverse indices for all m,n from 1 to 100.
- schema:
  - `type`: table
  - `required_columns`: `m`, `n`, `R1`, `Rm1`, `R12`, `Rm12`, `ABC`, `GA`, `F`, `AZI`, `M1`, `M2`, `ReZG1`, `ReZG2`, `ReZG3`, `CR1`, `CRm1`, `CR12`, `CRm12`, `CABC`, `CGA`, `CF`, `CAZI`, `CM1`, `CM2`, `CReZG1`, `CReZG2`, `CReZG3`, `RR1`, `RRm1`, `RR12`, `RRm12`, `RABC`, `RGA`, `RF`, `RAZI`, `RM1`, `RM2`, `RReZG1`, `RReZG2`, `RReZG3`
  - `units`:
    - `m`: dimensionless (integer)
    - `n`: dimensionless (integer)
    - `R1`: dimensionless
    - `Rm1`: dimensionless
    - `R12`: dimensionless
    - `Rm12`: dimensionless
    - `ABC`: dimensionless
    - `GA`: dimensionless
    - `F`: dimensionless
    - `AZI`: dimensionless
    - `M1`: dimensionless
    - `M2`: dimensionless
    - `ReZG1`: dimensionless
    - `ReZG2`: dimensionless
    - `ReZG3`: dimensionless
    - `CR1`: dimensionless
    - `CRm1`: dimensionless
    - `CR12`: dimensionless
    - `CRm12`: dimensionless
    - `CABC`: dimensionless
    - `CGA`: dimensionless
    - `CF`: dimensionless
    - `CAZI`: dimensionless
    - `CM1`: dimensionless
    - `CM2`: dimensionless
    - `CReZG1`: dimensionless
    - `CReZG2`: dimensionless
    - `CReZG3`: dimensionless
    - `RR1`: dimensionless
    - `RRm1`: dimensionless
    - `RR12`: dimensionless
    - `RRm12`: dimensionless
    - `RABC`: dimensionless
    - `RGA`: dimensionless
    - `RF`: dimensionless
    - `RAZI`: dimensionless
    - `RM1`: dimensionless
    - `RM2`: dimensionless
    - `RReZG1`: dimensionless
    - `RReZG2`: dimensionless
    - `RReZG3`: dimensionless

### feature_selection_ranking.csv
- path: `/app/outputs/feature_selection_ranking.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Indices ranked by R² score from exhaustive feature selection (max_features=1).
- schema:
  - `type`: table
  - `required_columns`: `idx`, `score`
  - `units`:
    - `idx`: string
    - `score`: R² score (float)

### regression_ranking.csv
- path: `/app/outputs/regression_ranking.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Indices ranked by average absolute feature weight from eight regression models.
- schema:
  - `type`: table
  - `required_columns`: `idx`, `avg_weight`
  - `units`:
    - `idx`: string
    - `avg_weight`: average absolute feature weight (float)

Notes: Scoring for indices_values.csv will recompute a sample of index values using the edge-partition method and compare with absolute tolerance. For the ranking CSVs, the top-10 indices will be compared to the expected reference sets (order not required).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "indices_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "m",
          "n",
          "R1",
          "Rm1",
          "R12",
          "Rm12",
          "ABC",
          "GA",
          "F",
          "AZI",
          "M1",
          "M2",
          "ReZG1",
          "ReZG2",
          "ReZG3",
          "CR1",
          "CRm1",
          "CR12",
          "CRm12",
          "CABC",
          "CGA",
          "CF",
          "CAZI",
          "CM1",
          "CM2",
          "CReZG1",
          "CReZG2",
          "CReZG3",
          "RR1",
          "RRm1",
          "RR12",
          "RRm12",
          "RABC",
          "RGA",
          "RF",
          "RAZI",
          "RM1",
          "RM2",
          "RReZG1",
          "RReZG2",
          "RReZG3"
        ],
        "units": {
          "m": "dimensionless (integer)",
          "n": "dimensionless (integer)",
          "R1": "dimensionless",
          "Rm1": "dimensionless",
          "R12": "dimensionless",
          "Rm12": "dimensionless",
          "ABC": "dimensionless",
          "GA": "dimensionless",
          "F": "dimensionless",
          "AZI": "dimensionless",
          "M1": "dimensionless",
          "M2": "dimensionless",
          "ReZG1": "dimensionless",
          "ReZG2": "dimensionless",
          "ReZG3": "dimensionless",
          "CR1": "dimensionless",
          "CRm1": "dimensionless",
          "CR12": "dimensionless",
          "CRm12": "dimensionless",
          "CABC": "dimensionless",
          "CGA": "dimensionless",
          "CF": "dimensionless",
          "CAZI": "dimensionless",
          "CM1": "dimensionless",
          "CM2": "dimensionless",
          "CReZG1": "dimensionless",
          "CReZG2": "dimensionless",
          "CReZG3": "dimensionless",
          "RR1": "dimensionless",
          "RRm1": "dimensionless",
          "RR12": "dimensionless",
          "RRm12": "dimensionless",
          "RABC": "dimensionless",
          "RGA": "dimensionless",
          "RF": "dimensionless",
          "RAZI": "dimensionless",
          "RM1": "dimensionless",
          "RM2": "dimensionless",
          "RReZG1": "dimensionless",
          "RReZG2": "dimensionless",
          "RReZG3": "dimensionless"
        }
      },
      "description": "Computed topological indices, coindices, and reverse indices for all m,n from 1 to 100."
    },
    {
      "file": "feature_selection_ranking.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "idx",
          "score"
        ],
        "units": {
          "idx": "string",
          "score": "R² score (float)"
        }
      },
      "description": "Indices ranked by R² score from exhaustive feature selection (max_features=1)."
    },
    {
      "file": "regression_ranking.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "idx",
          "avg_weight"
        ],
        "units": {
          "idx": "string",
          "avg_weight": "average absolute feature weight (float)"
        }
      },
      "description": "Indices ranked by average absolute feature weight from eight regression models."
    }
  ],
  "notes": "Scoring for indices_values.csv will recompute a sample of index values using the edge-partition method and compare with absolute tolerance. For the ranking CSVs, the top-10 indices will be compared to the expected reference sets (order not required)."
}
```

## How you are scored
A hidden verifier will evaluate your outputs independently. For indices_values.csv, the verifier will recompute a sample of index values using the same edge-partition formulas and compare them against your submitted values within a numerical tolerance. For feature_selection_ranking.csv and regression_ranking.csv, the verifier will compare the set of indices appearing in the top-10 positions of your rankings against predetermined reference sets. The final reward is a weighted combination of scores: the index values table carries one weight, and the two ranking files each carry a weight. Reporting plausible but incorrect values or rankings will not suffice; your computed indices and selection results must be correct according to the prescribed method.
