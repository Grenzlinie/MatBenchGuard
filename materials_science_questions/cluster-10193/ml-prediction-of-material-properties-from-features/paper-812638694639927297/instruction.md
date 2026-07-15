# Adaptive Training Set Design for ExtraTrees Surrogates on a 1D Test Function

## Problem background
Approximating computationally intensive first-principles kinetic models with machine learning requires a training set that captures the function's behaviour. Conventional evenly spaced grids can demand a very large number of points to achieve good accuracy, especially when the function has sharp transitions or highly non-linear features. This task explores a procedure that adaptively designs the training set by iteratively adding points in regions where the function varies steeply and along directions that have high variable importance, aiming to reduce the number of data points needed while maintaining surrogate accuracy. As a showcase, a one-dimensional test function with a steep sigmoidal rise is used to demonstrate the procedure.

## Approach
The core method uses an ExtraTrees (Extremely Randomized Trees) regressor as the surrogate. Starting from a small set of evenly spaced points, an iterative loop is run. In each iteration: an ExtraTrees model is trained on the current training set; its out-of-bag (OOB) error and permutation-based variable importance are computed; the variable importance identifies which input directions are most influential, and the discrete derivative of the function along those directions guides where new points are added. Specifically, midpoints of intervals that show large absolute derivatives are appended to the training set. The process continues until two stopping criteria based on the normalized OOB error and a relative approximation difference (RAD) between successive model predictions on the newly added points are both met. The final training set and the trained ExtraTrees model are then used to evaluate the surrogate on a large, uniformly sampled benchmark set to measure its predictive accuracy.

## Reproduction target
Implement the adaptive training set design procedure for the 1D test function y = 1/(x*(1+exp(-150*(x-0.5)))) on the interval x in [0.001, 1]. Begin with 4 evenly spaced points. Iteratively add points as described until the convergence criteria (based on normalized OOB error and RAD) are satisfied. Then generate a benchmark set of 1000 random points uniformly distributed in the same interval. Using the final ExtraTrees model, predict the function values for these points and compute the average relative error (mean of |y_true - y_pred|/|y_true|) and the maximum relative error (maximum of the same). Finally, report these two error metrics and the size of the final training set. The required output is a JSON file containing the three numbers.

## Assets

- scikit-learn: scikit-learn
- numpy: numpy

## Workflow steps

### Step 1: Adaptive training set design
- Role: process
- Action: Implement the adaptive training set design algorithm for the 1D test function y = 1/(x*(1+exp(-150*(x-0.5)))) on x in [0.001,1]. Start with 4 evenly spaced initial points (e.g., 0.001, 0.333..., 0.666..., 1.0) and evaluate y. Iteratively: (i) train an ExtraTrees regressor with 200 trees, leaf size 1, training fraction 0.7, splitting variables = 1, using bootstrapping; (ii) compute OOB MSE and permutation importance; (iii) select directions with importance > 0.2 (for 1D this is the only direction); (iv) compute discrete derivatives between consecutive training points and add midpoints of intervals where max absolute derivative > 0.5; (v) evaluate y at new points and append to training set; (vi) recompute ExtraTrees and compute normalized OOB (OOB/OOB^(1)) and RAD (relative approximation difference between current and previous iteration evaluated on newly added points). Terminate when normalized OOB < 0.014 and RAD < 0.01. Save the final training set (x and y values) as a CSV file.
- Evidence: `/app/outputs/final_training_set.csv`

### Step 2: Benchmark evaluation
- Role: scored (load-bearing)
- Action: Generate a benchmark set of 1000 random points uniformly distributed in [0.001,1]. Compute the true function values y = 1/(x*(1+exp(-150*(x-0.5)))). Use the final ExtraTrees model trained in the adaptive procedure to predict y for these points. Calculate the average relative error (mean of |y_true - y_pred|/|y_true|) and the maximum relative error (max of the same). Also record the size of the final training set (number of points). Write these three numbers to a JSON file.
- Output file: `/app/outputs/benchmark_errors.json`
- Format: json
- Contract: {"average_relative_error": "float", "max_relative_error": "float", "training_set_size": "int"}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/benchmark_errors.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### benchmark_errors.json
- path: `/app/outputs/benchmark_errors.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Contains the average relative error, maximum relative error on a 1000-point random benchmark, and the size of the final training set produced by the adaptive procedure.
- schema:
  - `type`: object
  - `required`:
    - `average_relative_error`: float
    - `max_relative_error`: float
    - `training_set_size`: int

Notes: The tolerance thresholds for the errors and the acceptable range for the training set size are hidden; the policy threshold_or_better means that meeting or beating the reference performance earns full credit.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "benchmark_errors.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "average_relative_error": "float",
          "max_relative_error": "float",
          "training_set_size": "int"
        }
      },
      "description": "Contains the average relative error, maximum relative error on a 1000-point random benchmark, and the size of the final training set produced by the adaptive procedure."
    }
  ],
  "notes": "The tolerance thresholds for the errors and the acceptable range for the training set size are hidden; the policy threshold_or_better means that meeting or beating the reference performance earns full credit."
}
```

## How you are scored
A hidden verifier will automatically examine your produced file `/app/outputs/benchmark_errors.json`. It will extract the reported average relative error, maximum relative error, and training set size, and compare each against expected thresholds that reflect a successful execution of the adaptive procedure on this function. The comparison uses a threshold-or-better policy: meeting or exceeding the hidden performance criteria yields full credit for that metric. The three scores are combined into a single overall reward. The specific numeric thresholds are not disclosed; you must faithfully implement the described adaptive design and benchmark evaluation to produce results that match the expected behaviour. Simply guessing or reporting numbers without running the procedure will not satisfy the verifier.
