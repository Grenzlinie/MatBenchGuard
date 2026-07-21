# 1D Active Polar Particle Model: Cluster Size and Phase Diagram

## Problem background
Collective cell migration plays a critical role in development, wound healing, and cancer. When two migrating cells come into contact, they often repolarize away from each other — a phenomenon called contact inhibition of locomotion (CIL) — which is expected to discourage the formation of large, cohesive cell clusters with sustained polarized motion. A key open question is how the competition between cell-cell adhesion (which promotes clustering) and CIL-type asymmetric repolarization (which favors cluster breakup) determines the statistical properties of cell assemblies, such as typical cluster sizes, the persistence of directed motion, and the conditions under which a population transitions between dispersed, microphase-separated, and fully clustered states. This task’s computational model addresses these questions by simulating active particles whose pairwise interactions capture the experimentally observed bias toward outward-pointing polarities.

## Approach
We consider a one-dimensional agent-based model of active Brownian particles. Each particle possesses a position and an internal binary polarity (±1). Particles interact via a truncated Lennard‑Jones potential that provides steric repulsion and tunable adhesion (cohesive strength γ), and via a polarity‑dependent pair potential that contains two contributions: a symmetric alignment term (strength β) that favours parallel polarities, and an asymmetric alignment term (strength α) of the form –α (p_i – p_j)·n_ij, where n_ij is the unit vector from particle j to i. The asymmetric term explicitly breaks the symmetry under independent rotations of polarity and space, capturing the CIL phenomenology. The polarities evolve according to Glauber (single‑spin‑flip) dynamics coupled to the positions, while the positions obey overdamped Langevin equations with a self-propulsion force proportional to the polarity vector. The strength of self-propulsion is measured by the Péclet number Pe. The model parameters α and β are set to values calibrated from binary cell‑collision experiments: α = 0.59, β = 0.31 (in units of the polarity temperature). By simulating the model across a grid of Pe and γ values (for cluster size analysis), across a range of train sizes N (for polarity persistence), and across a grid of α/β ratios and Pe/γ values (for phase classification), we obtain the data needed to extract the scaling and phase‑diagram information described under ‘Reproduction target’ below. The simulations are performed in one dimension with periodic boundary conditions, using standard numerical integration methods and Glauber spin‑flip sampling.

## Reproduction target
Your implementation must produce three scored CSV artifacts:

1. **Cluster size scaling** – `cluster_size_scaling.csv`: For a fixed ratio α/β ≈ 2, run simulations at several (Pe, γ) parameter combinations and extract the steady‑state mean and standard deviation of cluster size for each condition. Output columns: Pe (float), gamma (float), alpha (float), beta (float), mean_cluster_size (float), std_cluster_size (float).

2. **Polarity autocorrelation scaling** – `polarity_autocorrelation_scaling.csv`: At fixed Pe, γ, and α/β ≈ 2, compute the polarity persistence time τ_p (the characteristic decay time of the global polarity autocorrelation function) for train sizes N from 3 to 100. Output columns: N (int), tau_p (float, in intrinsic time units τ).

3. **Phase diagram** – `phase_diagram_simulation.csv`: Scan a grid of (α/β, Pe/γ) values. For each point, classify the steady-state regime as ‘dispersed’, ‘microphase’, or ‘clustered’ based on a quantitative criterion (e.g., cluster size distribution shape or a polar order parameter threshold). Output columns: alpha_beta_ratio (float), Pe_gamma (float), regime (string).

## Assets

- Python scientific computing stack (numpy, scipy, matplotlib): https://pypi.org/project/numpy

## Workflow steps

### Step 1: Run agent-based simulations of the 1D active polar particle model
- Role: process
- Action: Implement the 1D agent-based model as described in the paper: active Brownian particles with a truncated Lennard-Jones potential for steric repulsion/adhesion and an asymmetric aligning polarity interaction potential (including the characteristic CIL coupling). Use Glauber spin‑flip dynamics for polarities. Set the interaction parameters α = 0.59 and β = 0.31 (adopted from the paper's experimental calibration). Run simulations for a range of Péclet numbers Pe and cohesive strengths γ to probe cluster size distributions, and for varying train sizes N to track polarity autocorrelation. Produce aggregated simulation data required by the downstream scored analysis steps.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Compute cluster size scaling data
- Role: scored (load-bearing)
- Action: From the simulation results, extract steady-state average cluster size statistics for a set of (Pe, gamma) combinations at fixed α/β ≈ 2. Compute the mean and standard deviation of cluster size for each condition.
- Output file: `/app/outputs/cluster_size_scaling.csv`
- Format: csv
- Contract: Columns: Pe (float), gamma (float), alpha (float), beta (float), mean_cluster_size (float), std_cluster_size (float).
- Scoring: scored by hidden verifier

### Step 3: Compute polarity autocorrelation scaling data
- Role: scored
- Action: From simulation trajectories at fixed Pe, gamma, and α/β ≈ 2, compute the polarity persistence time τ_p for a series of train sizes N (ranging from 3 to 100).
- Output file: `/app/outputs/polarity_autocorrelation_scaling.csv`
- Format: csv
- Contract: Columns: N (int), tau_p (float, in simulation time units τ).
- Scoring: scored by hidden verifier

### Step 4: Construct phase diagram from simulation
- Role: scored
- Action: Scan a grid of (α/β ratio, Pe/γ value) combinations. For each point, classify the steady-state regime as dispersed, microphase, or clustered based on a quantitative criterion (e.g., cluster size distribution shape or polar order parameter threshold).
- Output file: `/app/outputs/phase_diagram_simulation.csv`
- Format: csv
- Contract: Columns: alpha_beta_ratio (float), Pe_gamma (float), regime (string, one of: dispersed, microphase, clustered).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/cluster_size_scaling.csv`
- `/app/outputs/polarity_autocorrelation_scaling.csv`
- `/app/outputs/phase_diagram_simulation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### cluster_size_scaling.csv
- path: `/app/outputs/cluster_size_scaling.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Mean and standard deviation of cluster size for different Pe/gamma combinations. The checker performs log‑log regression to extract the scaling exponent and compares it to the expected value within a generous tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Pe`, `gamma`, `alpha`, `beta`, `mean_cluster_size`, `std_cluster_size`
  - `units`:
    - `Pe`: dimensionless
    - `gamma`: dimensionless
    - `alpha`: dimensionless (units of T_p)
    - `beta`: dimensionless (units of T_p)
    - `mean_cluster_size`: number of particles
    - `std_cluster_size`: number of particles

### polarity_autocorrelation_scaling.csv
- path: `/app/outputs/polarity_autocorrelation_scaling.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Polarity persistence time τ_p for different train sizes N. The checker performs log‑log regression to verify τ_p ∝ N² within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `N`, `tau_p`
  - `units`:
    - `N`: number of particles
    - `tau_p`: simulation time units τ

### phase_diagram_simulation.csv
- path: `/app/outputs/phase_diagram_simulation.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Each row reports the thermodynamic regime (dispersed / microphase / clustered) for one (α/β, Pe/γ) point. The checker verifies that, for a fixed α/β >> 1, the sequence of regimes as Pe/γ increases follows a specific pattern expected from the model's phase behavior.
- schema:
  - `type`: table
  - `required_columns`: `alpha_beta_ratio`, `Pe_gamma`, `regime`
  - `units`: object

Notes: All values in the CSVs are computed by the agent. The verifier reads these self‑reported artifacts and compares the derived scaling exponents and regime ordering against paper‑derived hidden references. Tolerances are set generously to account for implementation and stochastic variations; the goal is to confirm the qualitative scaling trends and phase behaviour, not exact numeric reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "cluster_size_scaling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "Pe",
          "gamma",
          "alpha",
          "beta",
          "mean_cluster_size",
          "std_cluster_size"
        ],
        "units": {
          "Pe": "dimensionless",
          "gamma": "dimensionless",
          "alpha": "dimensionless (units of T_p)",
          "beta": "dimensionless (units of T_p)",
          "mean_cluster_size": "number of particles",
          "std_cluster_size": "number of particles"
        }
      },
      "description": "Mean and standard deviation of cluster size for different Pe/gamma combinations. The checker performs log‑log regression to extract the scaling exponent and compares it to the expected value within a generous tolerance."
    },
    {
      "file": "polarity_autocorrelation_scaling.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "N",
          "tau_p"
        ],
        "units": {
          "N": "number of particles",
          "tau_p": "simulation time units τ"
        }
      },
      "description": "Polarity persistence time τ_p for different train sizes N. The checker performs log‑log regression to verify τ_p ∝ N² within tolerance."
    },
    {
      "file": "phase_diagram_simulation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "alpha_beta_ratio",
          "Pe_gamma",
          "regime"
        ],
        "units": {}
      },
      "description": "Each row reports the thermodynamic regime (dispersed / microphase / clustered) for one (α/β, Pe/γ) point. The checker verifies that, for a fixed α/β >> 1, the sequence of regimes as Pe/γ increases follows a specific pattern expected from the model's phase behavior."
    }
  ],
  "notes": "All values in the CSVs are computed by the agent. The verifier reads these self‑reported artifacts and compares the derived scaling exponents and regime ordering against paper‑derived hidden references. Tolerances are set generously to account for implementation and stochastic variations; the goal is to confirm the qualitative scaling trends and phase behaviour, not exact numeric reproduction."
}
```

## How you are scored
A hidden verifier will independently evaluate each of the three scored artifacts. For `cluster_size_scaling.csv`, it will perform a log‑log regression of mean cluster size against Pe/γ to extract a scaling exponent, and award credit if that exponent lies within a generous tolerance of the expected physical scaling (full credit for meeting the expected trend, with credit decreasing as the exponent deviates further). For `polarity_autocorrelation_scaling.csv`, the verifier will log‑log regress tau_p against N and compare the exponent to the expected scaling. For `phase_diagram_simulation.csv`, it will check that the sequence of regimes along a line of fixed α/β ratio (e.g., as Pe/γ is increased at α/β ≫ 1) follows a specific pattern expected from the model. The verifier combines the scores from these checks (weighted roughly equally) into a final reward between 0 and 1. **Important:** Submitting values that are not backed by genuine simulations of the prescribed model — for example, numbers that merely reproduce the expected scaling exponents without the underlying data being self‑consistent — will fail the internal consistency checks and result in a low or zero score. You must execute the workflow steps in order and produce the CSV files from your own simulation output.
