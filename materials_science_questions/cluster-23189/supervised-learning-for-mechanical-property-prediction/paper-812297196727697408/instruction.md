# Abductive Network Surrogate for Injection Moulding Runner-Gate Optimization

## Problem background
Injection moulding processes require careful design of the runner and gating system to deliver molten polymer uniformly to all cavities. Poor design can cause defects such as warpage, which degrades part quality. Finite element simulations (FEM) can accurately predict warp for a given set of parameters – the number of cavities, the injection part volume, the runner diameter, and the gate diameter – but they are computationally expensive, making it impractical to explore the design space through simulation alone.

This task addresses that gap by building a fast surrogate model. A set of 27 FEM simulation runs, created using a Taguchi orthogonal array to sample the parameter space efficiently, provides training data that relates these four input parameters to the resulting maximum warp. The goal is to train a polynomial network that can accurately predict warp for arbitrary parameter combinations. With this surrogate in hand, it becomes possible to search for the parameter combination that minimizes warp, using a global optimization algorithm – simulated annealing – that evaluates many candidate designs quickly through the network rather than through expensive FEM runs. The entire workflow mirrors a published study on this method.

## Approach
The core of this reproduction is a two‑stage computational methodology.

**Stage 1 – Abductive polynomial network (GMDH‑style)**
An abductive network is a multi‑layer polynomial network that synthesizes a compact input‑output model from data. It is constructed using a group method of data handling (GMDH) approach: simple polynomial nodes – including single‑input, double‑input, and triple‑input nodes, as well as normalizer and unitizer nodes – are evaluated and combined layer by layer. Each candidate node fits a polynomial (up to third degree) to its inputs. The predicted squared error (PSE) criterion is used to select which nodes and layers to keep, automatically balancing model accuracy against complexity to avoid over‑fitting. The result is a parsimonious polynomial expression that maps the four design parameters (cavity count N, part volume linear dimension V, runner diameter R<sub>D</sub>, gate diameter G<sub>D</sub>) to the predicted warp.

**Stage 2 – Simulated annealing optimization**
Once the network is trained, it serves as an inexpensive objective function. Simulated annealing is used to search for the design point (N, V, R<sub>D</sub>, G<sub>D</sub>) that minimizes the network‑predicted warp. The algorithm starts at a high temperature, allowing exploration of the parameter space, and gradually cools according to a geometric schedule, with a Boltzmann probability of accepting uphill moves. The search is confined to physically meaningful bounds derived from the original study. The SA parameters – initial temperature, final temperature, cooling rate, and Boltzmann constant – are fixed and must be used as specified in the workflow steps.

## Reproduction target
You are provided with the file `gate_runner_warp_training_data.csv`, which contains 27 rows of FEM simulation data. Each row gives values for N (cavity count), V (linear dimension of a cubic part in mm), R<sub>D</sub> (runner diameter in mm), G<sub>D</sub> (gate diameter in mm), and the resulting maximum warp in mm.

Your task is to:
1. **Train an abductive polynomial network** using the PSE criterion on these 27 examples to capture the mapping (N, V, R<sub>D</sub>, G<sub>D</sub>) → warp. Save the trained model so that it can be used for prediction and optimization.
2. **Predict warp for two unseen parameter combinations** that were not in the training set, and write the predictions to `step_01_test_predictions.csv`:
   - Test case 1: N = 2, V = 25 mm, R<sub>D</sub> = 3.5 mm, G<sub>D</sub> = 1.5 mm
   - Test case 2: N = 4, V = 22 mm, R<sub>D</sub> = 2.8 mm, G<sub>D</sub> = 1.5 mm
3. **Use simulated annealing** with your trained network as the objective function to find the combination (N, V, R<sub>D</sub>, G<sub>D</sub>) that minimizes predicted warp, subject to:
   - 1 ≤ N ≤ 4
   - 10 mm ≤ V ≤ 30 mm
   - 2.1 mm ≤ R<sub>D</sub> ≤ 3.9 mm
   - 0.98 mm ≤ G<sub>D</sub> ≤ 1.82 mm
   The SA parameters are: initial temperature = 100, final temperature = 0.0001, cooling rate = 0.95, Boltzmann constant = 0.00667. Write the optimal parameter set and its predicted warp to `step_02_optimal_parameters.csv`.

The two CSV files are scored; the expected formats are given in the workflow steps and output contract.

## Assets

- gate_runner_warp_training_data.csv

## Workflow steps

### Step 1: Load training data
- Role: process
- Action: Read the bundled gate_runner_warp_training_data.csv and prepare input-output pairs (N, V, R_D, G_D as features; warp as target) for model training. Verify that the dataset contains the expected 27 examples.
- Evidence: `/app/outputs/training_data_summary.txt`

### Step 2: Train abductive network
- Role: process
- Action: Implement or configure a GMDH-style polynomial network (abductive network) that automatically selects polynomial nodes (normalizer, unitizer, white, single, double, triple) using the predicted square error (PSE) criterion. Train the network on the 27 training examples to obtain a parsimonious polynomial surrogate mapping from (N, V, R_D, G_D) to maximum warp. Save the trained network model (coefficients and structure) for subsequent use.
- Evidence: `/app/outputs/trained_network.pkl`

### Step 3: Test predictions
- Role: scored (load-bearing)
- Action: Using the trained abductive network, predict the maximum warp for two unseen parameter combinations: (N=2, V=25 mm, R_D=3.5 mm, G_D=1.5 mm) and (N=4, V=22 mm, R_D=2.8 mm, G_D=1.5 mm). The volume V is the linear dimension of a cubic part (side length). Write the predictions to step_01_test_predictions.csv.
- Output file: `/app/outputs/step_01_test_predictions.csv`
- Format: csv
- Contract: Columns: N (integer), V (float, mm), R_D (float, mm), G_D (float, mm), warp_predicted (float, mm). Two rows.
- Scoring: scored by hidden verifier

### Step 4: Simulated annealing optimization
- Role: scored (load-bearing)
- Action: Implement simulated annealing using the trained abductive network as the objective function. Search for the parameter set (N, V, R_D, G_D) that minimizes warp_predicted within bounds: N ∈ [1,4], V (linear dimension) ∈ [10,30] mm, R_D ∈ [2.1,3.9] mm, G_D ∈ [0.98,1.82] mm. Use SA parameters: initial temperature=100, final temperature=0.0001, cooling rate=0.95, Boltzmann constant=0.00667. Write the optimal parameter set and its predicted warp to step_02_optimal_parameters.csv.
- Output file: `/app/outputs/step_02_optimal_parameters.csv`
- Format: csv
- Contract: Columns: N (float or integer), V (float, mm), R_D (float, mm), G_D (float, mm), warp_predicted (float, mm). One row.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_test_predictions.csv`
- `/app/outputs/step_02_optimal_parameters.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_test_predictions.csv
- path: `/app/outputs/step_01_test_predictions.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Abductive network predictions of maximum warp for two unseen test cases (N=2,V=25,R_D=3.5,G_D=1.5 and N=4,V=22,R_D=2.8,G_D=1.5).
- schema:
  - `type`: table
  - `required_columns`: `N`, `V`, `R_D`, `G_D`, `warp_predicted`
  - `units`:
    - `N`: count
    - `V`: mm
    - `R_D`: mm
    - `G_D`: mm
    - `warp_predicted`: mm

### step_02_optimal_parameters.csv
- path: `/app/outputs/step_02_optimal_parameters.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimal runner and gating system parameters (N, V, R_D, G_D) found by simulated annealing that minimize the network-predicted warp, along with the minimum warp value.
- schema:
  - `type`: table
  - `required_columns`: `N`, `V`, `R_D`, `G_D`, `warp_predicted`
  - `units`:
    - `N`: count
    - `V`: mm
    - `R_D`: mm
    - `G_D`: mm
    - `warp_predicted`: mm

Notes: The provided training data (gate_runner_warp_training_data.csv) contains the 27 cases from the paper's Table 4. The agent must implement the abductive network and simulated annealing algorithm from scratch. The verifier compares the agent's predictions and optimal warp to the paper's reported network outputs and optimum using predetermined tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_test_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "V",
          "R_D",
          "G_D",
          "warp_predicted"
        ],
        "units": {
          "N": "count",
          "V": "mm",
          "R_D": "mm",
          "G_D": "mm",
          "warp_predicted": "mm"
        }
      },
      "description": "Abductive network predictions of maximum warp for two unseen test cases (N=2,V=25,R_D=3.5,G_D=1.5 and N=4,V=22,R_D=2.8,G_D=1.5)."
    },
    {
      "file": "step_02_optimal_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "V",
          "R_D",
          "G_D",
          "warp_predicted"
        ],
        "units": {
          "N": "count",
          "V": "mm",
          "R_D": "mm",
          "G_D": "mm",
          "warp_predicted": "mm"
        }
      },
      "description": "Optimal runner and gating system parameters (N, V, R_D, G_D) found by simulated annealing that minimize the network-predicted warp, along with the minimum warp value."
    }
  ],
  "notes": "The provided training data (gate_runner_warp_training_data.csv) contains the 27 cases from the paper's Table 4. The agent must implement the abductive network and simulated annealing algorithm from scratch. The verifier compares the agent's predictions and optimal warp to the paper's reported network outputs and optimum using predetermined tolerances."
}
```

## How you are scored
Your submission will be evaluated by an automated hidden verifier. It inspects the two scored output files and compares your results against reference values derived from the original study.

- **Step 3 – test predictions**: The verifier checks that the warp predictions for the two test cases are within an acceptable tolerance of the values a correctly trained network should produce. It verifies that the predictions are plausible and consistent with the training data.
- **Step 4 – optimal parameters**: The verifier confirms that the reported optimal design point lies within the allowed bounds, and that your network‑predicted warp for that point is, within tolerance, the minimum attainable wartp consistent with a correct network and optimization process. It also checks that the simulated annealing was run with the specified parameters.

The verifier combines the performance on these two steps into a single reward score between 0 and 1. You do not need to know the exact tolerances – you only need to faithfully implement the described methodology. Simply writing down expected numbers without running the actual pipeline will not produce a valid submission, because the verifier may also perform consistency checks that are impossible to satisfy without a correctly trained network and optimization routine.
