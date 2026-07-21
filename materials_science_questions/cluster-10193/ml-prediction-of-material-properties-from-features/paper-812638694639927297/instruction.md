# Adaptive Training Set Design for ExtraTrees Surrogates on a 1D Test Function

## Problem background
Approximating computationally intensive first-principles kinetic models with machine learning requires a training set that captures the function's behaviour. Conventional evenly spaced grids can demand a very large number of points to achieve good accuracy, especially when the function has sharp transitions or highly non-linear features. This task explores a procedure that adaptively designs the training set by iteratively adding points in regions where the function varies steeply and along directions that have high variable importance, aiming to reduce the number of data points needed while maintaining surrogate accuracy. As a showcase, a one-dimensional test function with a steep sigmoidal rise is used to demonstrate the procedure.

## Approach
The core method uses an ExtraTrees (Extremely Randomized Trees) regressor as the surrogate. Starting from a small set of evenly spaced points, an iterative loop is run. In each iteration: an ExtraTrees model is trained on the current training set; its out-of-bag (OOB) error and permutation-based variable importance are computed; the variable importance identifies which input directions are most influential, and the discrete derivative of the function along those directions guides where new points are added. Specifically, **midpoints of every interval that shows an absolute discrete derivative above a threshold** are appended to the training set. The process continues until two stopping criteria – based on the normalized OOB error and a **relative approximation difference (RAD)** between successive model predictions on the previously added points – are both met. The final trained ExtraTrees model and the final training set are then used to evaluate the surrogate on a large, uniformly sampled benchmark set to measure its predictive accuracy.

### Definitions of critical quantities

- **RAD – Relative Approximation Difference**  
  RAD compares the predictions of the current ExtraTrees model with those of the model from the previous iteration, evaluated **exclusively on the set of points that were added in the previous iteration** (i.e., the new training points from the immediately preceding loop).  
  `RAD = mean( |y_pred_current - y_pred_previous| / (|y_pred_current| + 1e-12) )`  
  If no previous points exist (first iteration), RAD is set to 1.0 so that the loop does not stop on the RAD condition.

- **Normalized OOB error**  
  The OOB mean squared error (MSE) of the current model divided by the OOB MSE of the very first model (iteration 1).  
  `normalized_OOB = OOB_MSE_current / OOB_MSE_first`

- **Point addition rule**  
  After training, sort the current training points by `x`. For every adjacent pair `(x_i, y_i), (x_j, y_j)`, compute the discrete derivative `d = |(y_j - y_i) / (x_j - x_i)|`. If `d > 0.5`, add the midpoint `(x_i + x_j) / 2` as a new candidate point. This is applied to **all pairs that satisfy the condition**, not just the pair with the maximum derivative. Avoid adding points that already exist in the training set (within a tolerance of 1e-12).

## Reproduction target
Implement the adaptive training set design procedure for the 1D test function  

`y = 1 / (x * (1 + exp(-150*(x-0.5))))`  

on the interval `x ∈ [0.001, 1]`. Begin with exactly 4 evenly spaced initial points, obtained from `numpy.linspace(0.001, 1, 4)`, i.e., the coordinates `[0.001, 0.334, 0.667, 1.0]`. Iteratively add points as described until the convergence criteria (normalized_OOB < 0.014 and RAD < 0.01) are satisfied, or until no new points can be added, or after a maximum of 30 iterations (whichever occurs first). Retain the final ExtraTrees model and the final training points.  

Then generate a benchmark set of 1000 random points uniformly distributed in the same interval (use a fixed random seed of 123). Using the final ExtraTrees model, predict the function values for these points and compute the **average relative error** (`mean of |y_true - y_pred| / |y_true|`) and the **maximum relative error** (`max of the same`). Also record the **size of the final training set** (number of points). Finally, report these three numbers in a JSON file as specified below.

## Assets

- scikit-learn: provides ExtraTreesRegressor and permutation_importance
- numpy: provides numerical operations and random sampling

## Workflow steps

### Step 1: Adaptive training set design
- Role: process
- Action: Implement the adaptive training set design algorithm for the 1D test function described above.  

  **Initialization**  
  - Create `x_initial = numpy.linspace(0.001, 1.0, 4)` → `[0.001, 0.334, 0.667, 1.0]`.  
  - Evaluate `y_initial = f(x_initial)` and form the training set `X = x_initial.reshape(-1,1)`, `y = y_initial`.  

  **Iterative loop** (repeat until stopped):  
  1. Train an ExtraTreesRegressor with the following parameters:  
     - n_estimators=200  
     - max_features=1 (only one variable available)  
     - min_samples_leaf=1  
     - bootstrap=True (use out-of-bag samples)  
     - max_samples=0.7 (training fraction 0.7)  
     - oob_score=True  
     - random_state=42 (for reproducibility)  
  2. Compute the OOB MSE (using `model.oob_prediction_` and the training targets).  
     - On the first iteration, store `OOB_first = current OOB MSE` and set `normalized_OOB = 1.0`.  
     - On subsequent iterations, `normalized_OOB = current OOB MSE / OOB_first`.  
  3. Compute permutation-based variable importance. Since this is a 1‑D problem, the only input variable will have importance 1.0, which exceeds the threshold of 0.2; therefore it is always selected.  
  4. Sort the current training points by `x`. For every consecutive pair `(x_i, x_j)`, calculate the absolute discrete derivative `|(y_j - y_i) / (x_j - x_i)|`. If this value is larger than 0.5, mark the midpoint `(x_i + x_j)/2` as a new candidate point. Collect all such midpoints, remove any that coincide with an already existing training point (within `1e-12`), and store the result as `X_new`.  
  5. If `X_new` is not empty, evaluate `y_new = f(X_new)` and append these points to the training set (`X = vstack([X, X_new.reshape(-1,1)])`, `y = append(y, y_new)`).  
  6. Compute RAD:  
     - If this is the first iteration (no previous model or no previous added points), set RAD = 1.0.  
     - Otherwise, use the **previous iteration’s newly added points** (the ones that were added just before this training, i.e., the model from the previous iteration and the `X_new` from that previous iteration). Evaluate the current model and the previous model on those points:  
       `RAD = mean( |y_pred_current - y_pred_previous| / (|y_pred_current| + 1e-12) )`.  
  7. Stop if **both** `normalized_OOB < 0.014` and `RAD < 0.01`. Also stop if `X_new` was empty (no new points could be added) or if a maximum of 30 iterations has been reached.  
  8. Retain the final ExtraTrees model (the one trained in the last iteration) and the final training set `(X, y)` for the next step.

### Step 2: Benchmark evaluation
- Role: scored (load-bearing)
- Action:  
  - Generate a benchmark set of 1000 `x` values uniformly distributed in `[0.001, 1]`. Use a fixed random seed of 123 (`numpy.random.seed(123)`) so that the set is reproducible.  
  - Compute the true function values `y_true = f(x_bench)`.  
  - Use the final ExtraTrees model from Step 1 to predict `y_pred = model.predict(x_bench)`.  
  - Calculate the average relative error as `mean(|y_true - y_pred| / |y_true|)` and the maximum relative error as `max(|y_true - y_pred| / |y_true|)`.  
  - Record the size of the final training set (number of rows in the combined `X` array).  
  - Write these three numbers to a JSON file.  
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