# Neural Scaling Law Reproduction with LAVA Optimizer for Benzene

## Problem background
Solving the many-electron Schrödinger equation accurately is a central challenge in quantum chemistry. Neural-network quantum Monte Carlo (NNQMC) provides a promising route by representing the wavefunction with highly expressive neural networks, but optimization difficulties often prevent large networks from reaching high accuracy. The Lookahead Variational Algorithm (LAVA) addresses this by combining variational Monte Carlo updates with a projection step inspired by imaginary time evolution. This optimization scheme enables systematic improvements in energy accuracy as the neural network capacity is increased, a behavior known as neural scaling. Reproducing the scaling law for a prototypical molecule such as benzene would demonstrate that extrapolation of the power-law relationship between energy error and parameter count can yield near-exact ground-state energies without relying on traditional error cancellation.

## Approach
The approach trains neural-network wavefunctions for the benzene molecule using the LAVA optimization algorithm on the LapNet ansatz, which employs a forward Laplacian framework for efficient evaluation. An initial wavefunction guess is obtained by pretraining the network to match a reference wavefunction expanded in the aug-cc-pVDZ basis. LAVA training is then carried out for several network configurations of increasing capacity (achieved by varying layer depth, channel width, and number of determinants). For each trained wavefunction, a long Monte Carlo run is performed to estimate the total energy and the local energy variance. The scaling law is investigated by fitting the relation between energy error and number of parameters to a power law, and by fitting a linear relation between energy and variance; the intercepts of these fits provide an extrapolated estimate of the exact energy.

## Reproduction target
Produce a dataset of total energies and local energy variances for at least five distinct LapNet network sizes trained on benzene using LAVA. Fit the power law E - E_SE = α N_p^{-β} by log-log least squares and the linear variance-energy relation E = k·V + E_SE. Output the fitted scaling parameters (α, β, E_SE) and the variance-energy intercept. The extrapolated E_SE and the power-law exponent β are the core quantities to determine; additionally, verify that larger networks give lower (more negative) variational energies.

## Assets

- JAX library: https://pypi.org/project/jax/
- Benzene experimental equilibrium geometry: https://cccbdb.nist.gov/expgeom2x.asp?casno=71432
- LapNet neural-wavefunction architecture and Forward Laplacian framework: 10.1038/s42256-024-00794-x
- aug-cc-pVDZ Gaussian basis set: https://www.basissetexchange.org/

## Algorithm and Default Hyperparameters

### LAVA Algorithm
The LAVA optimization procedure is as follows (Algorithm 1 from the paper):

```
Algorithm 1: LAVA
Require: initial parameters theta, MCMC samples {x_i} (i=1..B)
1: n ← 0, m0 ← 0, v0 ← 0
2: while n ≤ N do
3:     Sample new configurations {x_i} from |psi_theta|^2
4:     Compute local energies E_L(x_i) = (H psi_theta(x_i)) / psi_theta(x_i)
5:     E_tot ← mean(E_L(x_i))
6:     g ← mean( (E_L(x_i) - E_tot) * grad_theta ln|psi_theta(x_i)| )
7:     theta_temp ← theta - eta_temp * F_KFAC^{-1} * g
8:     Sample new configurations {x_i} from |psi_{theta_temp}|^2
9:     C ← sqrt( <psi_theta|psi_theta> / <psi_{theta_temp}|psi_{theta_temp}> )
10:    E_L'(x_i) ← H(psi_theta(x_i) + C*psi_{theta_temp}(x_i)) / psi_theta(x_i)
11:    g ← -mean( < sign(E_L'(x_i)) * sign( grad_r E_L'(x_i) ), grad_theta grad_r ln|psi_theta(x_i)| > )
12:    theta ← theta - Adam(F_KFAC^{-1} g)
13:    n ← n + 1
14: end while
15: return theta, {x_i}
```

The notation `<,>` denotes inner product over electronic coordinates. F_KFAC is the Kronecker-factored approximate curvature matrix. Adam is the Adam optimizer with parameters β1=0.9, β2=0.99, ε=1e-10.

### Default Hyperparameters
The default hyperparameters used in LAVA training are as follows (Supplementary Table S1):

| Parameter | Value |
|---|---|
| **Training** | |
| Optimizer | Adam-KFAC |
| Optimizer for intermediate steps | KFAC |
| Training iterations (N) | 300000 |
| Batch size (B) | 4096 |
| Learning rate η at iteration t | 5e-4 / (1 + t / t_delay) |
| Intermediate learning rate η_temp at iteration t | 5e-3 * min(1, t/t_warmup) / (1 + max(t, t_warmup)/t_delay) |
| Learning rate decay delay (t_delay) | 10000 |
| Warmup iterations (t_warmup) | 100000 |
| Local energy clipping | 5.0 |
| **Inference** | |
| Iterations for energy evaluation | 30000 |
| **Pretraining (optional)** | |
| Optimizer | LAMB |
| Iterations | 20000 |
| Basis set | aug-cc-pVDZ |
| Learning rate | 3e-4 |
| **MCMC** | |
| Decorrelation steps | 30 |
| Proposal standard deviation | 0.02 |
| Blocks | 1 |
| **KFAC** | |
| Norm constraint | 1e-7 * (min(1, t/t_warmup) / (1 + max(t, t_warmup)/t_delay))^2 |
| Damping | 1e-3 |
| Momentum | 0 |
| Covariance moving average decay | 0.95 |
| **Adam-KFAC** | |
| Norm constraint | 1e-6 |
| Damping | 5e-3 |
| Momentum decay rate β1 | 0.9 |
| Squared gradients decay rate β2 | 0.99 |
| ε | 1e-10 |
| Covariance moving average decay | 0.95 |

## Workflow steps

### Step 1: Pretrain LapNet wavefunction for benzene
- Role: process
- Action: Initialize the LapNet neural network ansatz for the benzene molecule using the experimental equilibrium geometry. Pretrain the network parameters by fitting to a reference wavefunction expanded in the aug-cc-pVDZ basis set.
- Evidence: `/app/outputs/pretrain_checkpoint.npy`

### Step 2: Run LAVA optimization for multiple network sizes
- Role: process
- Action: For at least five distinct network sizes (e.g., (4,64,2,16), (4,96,2,24), (4,128,4,32), (4,256,4,32), (4,408,4,48)), train the LapNet wavefunction using the LAVA algorithm. Each training run must use the default hyperparameters and the pretrained checkpoint. The model size is increased by varying network width, depth, and number of determinants.
- Evidence: `/app/outputs/lava_train_log.json`

### Step 3: Evaluate total energy and variance for each trained model
- Role: scored (load-bearing)
- Action: For each trained wavefunction, perform a long MCMC run to estimate the total energy and the local energy variance. Output a CSV table containing the results for all network configurations.
- Output file: `/app/outputs/step_01_scaling_data.csv`
- Format: csv
- Contract: Columns: network_config (string), N_p (int), total_energy (float, Hartree), var_local_energy (float, Ha²). One row per trained model.
- Scoring: scored by hidden verifier

### Step 4: Fit power-law and variance-energy scaling relations
- Role: scored
- Action: From the data in step_01_scaling_data.csv, fit the power law E - E_SE = alpha * N_p^{-beta} by log-log least squares, and the linear variance-energy relation E = k * V + E_SE. Report the fitted parameters in a JSON file.
- Output file: `/app/outputs/step_02_fit_results.json`
- Format: json
- Contract: { "power_law": { "alpha": float, "beta": float, "E_SE": float (Hartree) }, "variance_energy": { "slope": float, "intercept": float (Hartree) } }
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_scaling_data.csv`
- `/app/outputs/step_02_fit_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_scaling_data.csv
- path: `/app/outputs/step_01_scaling_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Raw energy and variance results from LAVA for different network sizes, used to recompute scaling law fits.
- schema:
  - `type`: table
  - `required_columns`: `network_config`, `N_p`, `total_energy`, `var_local_energy`
  - `units`:
    - `total_energy`: Hartree
    - `var_local_energy`: Ha²

### step_02_fit_results.json
- path: `/app/outputs/step_02_fit_results.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Fitted scaling law parameters (power-law and variance-energy) reported by the agent. The checker recomputes these from the CSV for scoring.
- schema:
  - `type`: object
  - `required`:
    - `power_law`: object
    - `variance_energy`: object
  - `items`:
    - `power_law.alpha`: float
    - `power_law.beta`: float
    - `power_law.E_SE`: float (Hartree)
    - `variance_energy.slope`: float
    - `variance_energy.intercept`: float (Hartree)

Notes: The primary scoring is based on recomputing the power-law fit and variance-energy extrapolation from the CSV data. The JSON is a supplementary report; its structure must match the schema but the actual numbers are verified by recomputation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_scaling_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "network_config",
          "N_p",
          "total_energy",
          "var_local_energy"
        ],
        "units": {
          "total_energy": "Hartree",
          "var_local_energy": "Ha²"
        }
      },
      "description": "Raw energy and variance results from LAVA for different network sizes, used to recompute scaling law fits."
    },
    {
      "file": "step_02_fit_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "power_law": "object",
          "variance_energy": "object"
        },
        "items": {
          "power_law.alpha": "float",
          "power_law.beta": "float",
          "power_law.E_SE": "float (Hartree)",
          "variance_energy.slope": "float",
          "variance_energy.intercept": "float (Hartree)"
        }
      },
      "description": "Fitted scaling law parameters (power-law and variance-energy) reported by the agent. The checker recomputes these from the CSV for scoring."
    }
  ],
  "notes": "The primary scoring is based on recomputing the power-law fit and variance-energy extrapolation from the CSV data. The JSON is a supplementary report; its structure must match the schema but the actual numbers are verified by recomputation."
}
```

## How you are scored
Your work is scored by a hidden verifier that inspects the artifacts you produce. The primary scoring comes from recomputing the power-law and variance-energy fits from your raw data in step_01_scaling_data.csv. The fitted β and the extrapolated energy E_SE are compared against hidden reference values (derived from the original study) within appropriate tolerances; meeting or exceeding the expected accuracy earns full credit. The verifier also checks that the total energies are monotonically decreasing with network size and that the fit results JSON (step_02_fit_results.json) has the correct structure. The final reward is a weighted combination of these checks. Reporting numbers from the paper without producing the required raw artifacts will not pass.
