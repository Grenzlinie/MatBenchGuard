# Monte Carlo Simulation of Eigen Microstate Condensation in Ising Models

## Problem background
In statistical mechanics, a phase transition can be characterised by the behaviour of microstates in a statistical ensemble. Instead of looking directly at the magnetization or energy, this work investigates the correlations among microstates themselves. For an ensemble of M microstates (each a spin configuration vector), an M×M correlation matrix is constructed. Diagonalising this matrix yields eigenvectors that define “eigen microstates” and eigenvalues whose normalised values (weight factors) describe the importance of each eigen microstate in the ensemble. The central idea is that a finite limiting weight factor when M → ∞ signals a condensation of the corresponding eigen microstate, i.e. a phase transition. A finite-size scaling relation for the weight factors near the critical point is proposed, linking them to the critical exponents of the order parameter and correlation length. The goal of this task is to test whether these ideas hold for the one‑dimensional and two‑dimensional Ising models: can you compute the weight factors of the leading eigen microstates and, for the 2D model, extract the critical exponent ratio that the theory predicts should emerge from finite‑size scaling? The answer must come from first‑principles Monte Carlo simulations and matrix diagonalisation, not from a literature lookup.

## Approach
We use the Wolff cluster algorithm to sample microstates of the nearest‑neighbour Ising model with periodic boundary conditions. For each temperature and system size, an ensemble of M = 2×10⁴ microstates is collected after proper equilibration. The normalised spin vectors Aᴵ (one per microstate) are used to build the M×M correlation matrix C with entries C_IJ = (Aᴵ)·(Aᴶ). Diagonalising C gives eigenvalues λ₁ ≥ λ₂ ≥ … ; the weight factor of the I‑th eigen microstate is w_I = λ_I / M. These weight factors are the primary observable. For the 1D chain (N = 10⁵ spins) we compute w₁, w₂, w₃ at two reduced temperatures T* = 0.2 and 0.5. For the 2D square lattice (L = 32) we compute the same three weights at T* = 2.2 and 6.2. To verify the proposed finite‑size scaling relation, we further simulate the 2D model exactly at the Onsager critical temperature T*_c = 2/ln(1+√2) for three linear sizes L = 32, 64, 128, obtain the largest weight factor w₁ for each L, and perform a linear regression of ln(w₁) against ln(L). The slope s of this regression is expected to equal 2β/ν, from which the exponent ratio β/ν = s/2 is extracted. The whole pipeline – simulation, correlation matrix build, eigendecomposition, and finite‑size scaling – is implemented from scratch using open‑source tools.

## Reproduction target
Reproduce the weight factors w₁, w₂, w₃ from the eigen‑decomposition of the microstate correlation matrix for the 1D Ising model (N = 10⁵ spins, M = 2×10⁴ microstates) at reduced temperatures T* = 0.2 and 0.5. For the 2D Ising model (L = 32, M = 2×10⁴) reproduce w₁, w₂, w₃ at T* = 2.2 and 6.2. Finally, from finite‑size scaling of the largest weight factor w₁ at the exact critical temperature T*_c = 2/ln(1+√2) for lattice sizes L = 32, 64, 128, determine the critical exponent ratio β/ν. Write all results to the CSV files specified in the workflow steps.

## Assets

- Python 3: https://www.python.org/
- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Simulate 1D Ising model
- Role: process
- Action: Use the Wolff cluster algorithm to simulate the 1D nearest-neighbour Ising model with Hamiltonian H = -J Σ S_i S_{i+1} and periodic boundary conditions. Set N = 10^5 spins, reduced temperatures T* = 0.2 and 0.5. For each temperature, discard the first 10^4 microstates for equilibration, then collect M = 2×10^4 microstates at an interval of 205 Monte Carlo steps. Store the microstates for later steps.
- Evidence: `/app/outputs/1d_simulation_log.txt`

### Step 2: Simulate 2D Ising model (eigen microstate)
- Role: process
- Action: Simulate the 2D square-lattice Ising model with nearest-neighbour interactions, linear size L = 32, periodic boundary conditions. Use the Wolff algorithm at reduced temperatures T* = 2.2 and 6.2. For each temperature, discard the first 8000 microstates, then collect M = 2×10^4 microstates at an interval of 250 Monte Carlo steps. Store the microstates.
- Evidence: `/app/outputs/2d_eigen_simulation_log.txt`

### Step 3: Simulate 2D Ising model (finite-size scaling)
- Role: process
- Action: Simulate the 2D Ising model at the exact critical temperature T_c* = 2/ln(1+√2) for linear sizes L = 32, 64, 128. Use the Wolff algorithm with periodic boundaries. For each L, discard the first 8000 microstates, then collect M = 2×10^4 microstates at an interval of 250 Monte Carlo steps. Store the microstates.
- Evidence: `/app/outputs/2d_fss_simulation_log.txt`

### Step 4: Compute 1D weight factors
- Role: scored
- Action: From the microstate ensembles of step1, for each temperature separately: construct the M×M correlation matrix C_IJ = (A^I)·(A^J) where A^I is the normalized spin configuration vector of microstate I; diagonalize C (e.g., using an iterative eigensolver) to obtain eigenvalues λ₁≥λ₂≥…; compute the weight factors w_I = λ_I / M; write the largest three weights to 1d_weight_factors.csv.
- Output file: `/app/outputs/1d_weight_factors.csv`
- Format: csv
- Contract: T_star (float), w1 (float), w2 (float), w3 (float)
- Scoring: scored by hidden verifier

### Step 5: Compute 2D weight factors
- Role: scored
- Action: From the microstate ensembles of step2 (L=32), for each temperature T*=2.2 and 6.2: build the correlation matrix, diagonalize, compute the largest three weight factors, and write the results to 2d_weight_factors.csv.
- Output file: `/app/outputs/2d_weight_factors.csv`
- Format: csv
- Contract: T_star (float), L (int), w1 (float), w2 (float), w3 (float)
- Scoring: scored by hidden verifier

### Step 6: Finite-size scaling and β/ν determination
- Role: scored (load-bearing)
- Action: From the microstate ensembles of step3 for L=32,64,128 at T_c, compute the largest weight factor w1 for each L. Perform a linear regression of ln(w1) vs ln(L) to obtain the slope s = 2β/ν, then compute β/ν = s/2. Write the results to fss_results.csv: for each L a row with description='w1_at_Tc' and value=w1; and a row with L=0, description='beta_over_nu' and value=β/ν.
- Output file: `/app/outputs/fss_results.csv`
- Format: csv
- Contract: L (int), value (float), description (string)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/1d_weight_factors.csv`
- `/app/outputs/2d_weight_factors.csv`
- `/app/outputs/fss_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### 1d_weight_factors.csv
- path: `/app/outputs/1d_weight_factors.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Weight factors w1, w2, w3 for the 1D Ising model at T*=0.2 and 0.5
- schema:
  - `type`: table
  - `required_columns`: `T_star`, `w1`, `w2`, `w3`
  - `columns`:
    - `T_star`: float
    - `w1`: float
    - `w2`: float
    - `w3`: float

### 2d_weight_factors.csv
- path: `/app/outputs/2d_weight_factors.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Weight factors w1, w2, w3 for the 2D Ising model (L=32) at T*=2.2 and 6.2
- schema:
  - `type`: table
  - `required_columns`: `T_star`, `L`, `w1`, `w2`, `w3`
  - `columns`:
    - `T_star`: float
    - `L`: int
    - `w1`: float
    - `w2`: float
    - `w3`: float

### fss_results.csv
- path: `/app/outputs/fss_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: w1 at T_c for L=32,64,128 and the fitted exponent ratio β/ν
- schema:
  - `type`: table
  - `required_columns`: `L`, `value`, `description`
  - `columns`:
    - `L`: int
    - `value`: float
    - `description`: string

Notes: The hidden checker compares each reported weight factor and the exponent ratio to reference values digitized from the paper using a combined relative/absolute tolerance. All comparisons are made on the agent's reported numbers (result-level compare).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "1d_weight_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_star",
          "w1",
          "w2",
          "w3"
        ],
        "columns": {
          "T_star": "float",
          "w1": "float",
          "w2": "float",
          "w3": "float"
        }
      },
      "description": "Weight factors w1, w2, w3 for the 1D Ising model at T*=0.2 and 0.5"
    },
    {
      "file": "2d_weight_factors.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "T_star",
          "L",
          "w1",
          "w2",
          "w3"
        ],
        "columns": {
          "T_star": "float",
          "L": "int",
          "w1": "float",
          "w2": "float",
          "w3": "float"
        }
      },
      "description": "Weight factors w1, w2, w3 for the 2D Ising model (L=32) at T*=2.2 and 6.2"
    },
    {
      "file": "fss_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "value",
          "description"
        ],
        "columns": {
          "L": "int",
          "value": "float",
          "description": "string"
        }
      },
      "description": "w1 at T_c for L=32,64,128 and the fitted exponent ratio β/ν"
    }
  ],
  "notes": "The hidden checker compares each reported weight factor and the exponent ratio to reference values digitized from the paper using a combined relative/absolute tolerance. All comparisons are made on the agent's reported numbers (result-level compare)."
}
```

## How you are scored
A hidden verifier checks each output file independently. The verifier reads your CSV files and compares every reported weight factor and the exponent ratio β/ν against independently computed reference results. The comparison uses an appropriate tolerance that accounts for normal numerical and implementation‑dependent spread. In addition, the verifier validates the file format and column schema. The final reward (a number between 0 and 1) is a weighted sum of the scores from the three stages; the finite‑size scaling stage carries the largest weight. Simply writing down numbers you recall from a published table is not enough – you must genuinely execute the simulations and the eigen‑analysis to obtain the values.
