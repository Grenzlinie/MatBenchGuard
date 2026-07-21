# Benchmark Evaluation of a Hybrid Taguchi Particle Swarm Optimizer

## Problem background
Global numerical optimization algorithms are evaluated on standard benchmark functions to compare their convergence speed, robustness, and ability to escape local optima. This task focuses on a hybrid optimizer that combines Taguchi-method recombination with particle swarm optimization (PSO). The central open question is whether this hybrid design achieves better solution quality and smaller variance than existing PSO variants when applied to high-dimensional functions drawn from three families: unimodal functions (which test convergence speed), a multimodal function (which tests the ability to avoid premature convergence to local optima), and rotated or shifted functions (which challenge the algorithm on non-separable, transformed landscapes). The benchmark results—the mean best objective value and its standard deviation over repeated independent trials—quantify both the optimizer's central tendency and its reliability.

## Approach
Implement a Taguchi Particle Swarm Optimizer (TPSO) that integrates three mechanisms: (1) a Taguchi recombination module that generates new candidate solutions using an orthogonal array to select factor-level combinations from the population, evaluates each combination via a signal-to-noise ratio (smaller-is-better formulation), and builds a response table to determine the best level of each factor, thereby systematically constructing improved offspring; (2) a nonlinear PSO movement mechanism in which each particle updates its velocity and position using a linearly decreasing inertia weight (from an initial maximum to a final minimum) with acceleration coefficients both set to the same constant, driving the conventional swarm dynamics; and (3) a random-movement operator applied with a small probability to the global-best particle to maintain diversity. Apply TPSO to minimize each of the following seven benchmark functions at dimension D=30 with their specified search ranges: a Sphere function (sum of squared elements), a Schwefel P2.22 function (sum of absolute values plus product of absolute values), a Noise function (sum of weighted fourth powers plus uniform random noise), a Schwefel function (shifted sum of x·sin(sqrt(|x|))), a Rotated Schwefel function (the Schwefel function applied after an orthogonal rotation and translation), a Rotated Ackley function (the Ackley function applied after an orthogonal rotation), and a Shifted Rosenbrock function (the Rosenbrock function applied after a constant-vector shift, then offset by a constant). For each function, compare the reproduced TPSO statistics against the same statistics obtained by seven published PSO variant baselines: global-best PSO, local-best PSO, fully-informed particle swarm, standard PSO, comprehensive-learning PSO, orthogonal-learning PSO, and scatter-learning PSO, all run under identical trial-count and function-evaluation budgets. The comparison reveals whether the hybrid TPSO design confers an advantage.

## Reproduction target
Implement the TPSO algorithm as described above. For each of the seven benchmark functions at dimension D=30, using the function-specific search range, a population size of 40, and a maximum of 200,000 function evaluations per trial, run 25 independent trials. In each trial, record the best (minimum) objective value found. After completing all 25 trials for a function, compute the arithmetic mean and the sample standard deviation of the 25 best values. Write the results to `/app/outputs/benchmark_results.csv` with one row per function (f1 through f7) and columns `function`, `mean`, and `std`. All values are floating-point numbers. The target is to produce these statistics through a faithful implementation of the TPSO algorithm; the quality of the reproduction is determined by how the computed means and standard deviations compare to the reference benchmark values for the same algorithm.

## Assets

- Seven benchmark optimization functions (f1-f7)

## Workflow steps

### Step 1: Implement TPSO algorithm
- Role: process
- Action: Implement the Taguchi Particle Swarm Optimizer (TPSO) combining Taguchi recombination (orthogonal array, signal-to-noise ratio, response table), nonlinear PSO velocity/position updates, and random movement operator, as described in the instruction. The optimizer must minimize a given objective function given dimension D, search bounds, population size 40, and control parameters.
- Evidence: `/app/outputs/t_pso_implementation.py`

### Step 2: Run benchmark experiments and collect results
- Role: scored (load-bearing)
- Action: For each of the seven benchmark functions (f1–f7) defined in the instruction, run the TPSO algorithm for 25 independent trials. Each trial uses D=30, function-specific search range, population size 40, and maximum function evaluations 2×10^5. Record the best objective value found in each trial. After all trials, compute the arithmetic mean and sample standard deviation of the 25 best values. Write the results to benchmark_results.csv.
- Output file: `/app/outputs/benchmark_results.csv`
- Format: csv
- Contract: CSV with header: function,mean,std. One row per function (f1, f2, f3, f4, f5, f6, f7). Values are floating-point numbers.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/benchmark_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### benchmark_results.csv
- path: `/app/outputs/benchmark_results.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Reproduced benchmark results of the TPSO algorithm on seven high-dimensional test functions. The mean and std must meet or exceed the paper-reported performance.
- schema:
  - `type`: table
  - `required_columns`: `function`, `mean`, `std`
  - `units`:
    - `mean`: fitness value (numerical)
    - `std`: fitness value (numerical)

Notes: The agent must run 25 independent trials per function to compute the statistics. The hidden checker compares the reported mean and std for each function against hidden gold values using a relative tolerance that accepts equal or better performance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "benchmark_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "function",
          "mean",
          "std"
        ],
        "units": {
          "mean": "fitness value (numerical)",
          "std": "fitness value (numerical)"
        }
      },
      "description": "Reproduced benchmark results of the TPSO algorithm on seven high-dimensional test functions. The mean and std must meet or exceed the paper-reported performance."
    }
  ],
  "notes": "The agent must run 25 independent trials per function to compute the statistics. The hidden checker compares the reported mean and std for each function against hidden gold values using a relative tolerance that accepts equal or better performance."
}
```

## How you are scored
A hidden verifier independently scores each scored workflow stage's artifact and combines them by weight into a final reward in [0,1]. For the scored step that produces `benchmark_results.csv`, the verifier reads your reported mean and standard deviation for each function and compares them against hidden reference values using an appropriate relative tolerance. The scoring is directional: meeting or exceeding the reference quality earns full credit, and credit decays only as results underperform. Only honest execution of the required 25-trial experiment followed by correct computation of the statistics can yield results within the expected tolerance band. Reporting the paper's numbers without running the experiment is not sufficient to pass.
