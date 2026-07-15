# Symmetrical binary fluid mixture phase behaviour

## Problem background
Liquid–vapour phase behaviour of binary fluid mixtures depends on the relative strength of interactions between particles of dissimilar and similar species. Understanding how the microscopic potential—here a square‑well—yields critical end points, triple points, tricritical points, and metastable ‘hidden’ phases is a fundamental problem in statistical mechanics. This task investigates how the interaction ratio δ, measuring the relative strength of unlike‑species interactions, controls the topology of the phase diagram.

## Approach
Two complementary approaches are used: (i) a mean‑field free energy functional that includes a hard‑sphere reference (Carnahan–Starling) and effective potentials computed with the Percus–Yevick radial distribution function; the convex envelope of the free energy gives liquid–vapour coexistence, the λ line, spinodals, and a hidden binodal. (ii) Grand‑canonical Monte Carlo simulations (optionally with multicanonical preweighting) of the square‑well binary mixture to obtain the probability density of the total number density at selected state points, revealing the structure of the coexistence region.

## Reproduction target
Compute from mean‑field theory: (a) liquid–vapour coexistence densities and the λ line for δ = 0.72 and δ = 0.65, written to mean_field_coexistence.csv as a function of temperature; (b) the three spinodal curves and the hidden liquid–vapour binodal for δ = 0.57, written to spinodals_hidden_binodal.csv. Based on these results, classify the equilibrium phase‑diagram topology for each δ (labels 'CEP', 'triple point + tricritical', 'tricritical only') in topology_classification.txt. Additionally, run a grand‑canonical Monte Carlo simulation with σ=1, J=1, δ=0.665, T=1.044, and system linear dimension 12σ (L=8 cells) to produce a normalized probability density distribution p(ρ) showing the three‑peak structure characteristic of a triple point; write it to mc_density_distribution.csv.

## Assets

- Percus–Yevick hard‑sphere radial distribution function g(r)

## Workflow steps

### Step 1: Mean-field solver implementation
- Role: process
- Action: Implement the mean-field Helmholtz free energy functional f_MF(ρ) for the symmetrical square-well binary mixture (Eq. 3.8) and the self-consistency equation for the concentration order parameter m (Eq. 3.9), using the Percus-Yevick hard-sphere radial distribution function to compute the effective potentials J±. Use the Carnahan-Starling expression for the hard-sphere reference free energy f_HS(ρ).
- Evidence: `/app/outputs/meanfield_solver_log.txt`

### Step 2: Mean-field liquid–vapour coexistence
- Role: scored
- Action: For δ = 0.72 and δ = 0.65, construct the convex envelope of f_MF(ρ) to obtain the liquid–vapour coexistence densities as a function of temperature, and locate the λ line (where a non-zero solution m≠0 appears). Write the results to mean_field_coexistence.csv.
- Output file: `/app/outputs/mean_field_coexistence.csv`
- Format: csv
- Contract: Columns: delta (float), temperature (float), rho_liquid (float), rho_vapour (float), rho_lambda_line (float, empty when no λ line at that T)
- Scoring: scored by hidden verifier

### Step 3: Spinodals and hidden binodal
- Role: scored
- Action: For δ = 0.57, compute the three spinodal curves S1, S2, S3 and the hidden (metastable) liquid–vapour binodal from the mean-field free energy. Write results to spinodals_hidden_binodal.csv.
- Output file: `/app/outputs/spinodals_hidden_binodal.csv`
- Format: csv
- Contract: Columns: delta (float), temperature (float), S1 (float), S2 (float), S3 (float), hidden_binodal_rho_liquid (float), hidden_binodal_rho_vapour (float) (empty when curve does not exist)
- Scoring: scored by hidden verifier

### Step 4: Topology classification
- Role: scored
- Action: Based on the computed mean-field phase diagrams, classify the equilibrium phase diagram topology for δ=0.72, δ=0.65, δ=0.57 (use labels 'CEP', 'triple point + tricritical', 'tricritical only'). Write to topology_classification.txt.
- Output file: `/app/outputs/topology_classification.txt`
- Format: txt
- Contract: Lines of the form 'δ=X: Y' (e.g., 'δ=0.72: CEP')
- Scoring: scored by hidden verifier

### Step 5: Grand-canonical Monte Carlo simulation
- Role: process
- Action: Implement a grand-canonical Metropolis Monte Carlo simulation for the square-well binary mixture (optionally with multicanonical preweighting). Use parameters σ=1, J=1, δ=0.665, T=1.044, system size L=8 cells (linear dimension 12σ). Run a sufficiently long simulation to accumulate a well-sampled histogram of total number density ρ.
- Evidence: `/app/outputs/mc_simulation_log.txt`

### Step 6: Monte Carlo density distribution
- Role: scored (load-bearing)
- Action: From the Monte Carlo histogram, produce the probability density distribution p(ρ) as a function of the density bin, ensuring it is normalized. Write to mc_density_distribution.csv.
- Output file: `/app/outputs/mc_density_distribution.csv`
- Format: csv
- Contract: Columns: density_bin (float), probability (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/mean_field_coexistence.csv`
- `/app/outputs/spinodals_hidden_binodal.csv`
- `/app/outputs/topology_classification.txt`
- `/app/outputs/mc_density_distribution.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### mean_field_coexistence.csv
- path: `/app/outputs/mean_field_coexistence.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Coexistence densities (liquid, vapour) and λ-line densities for δ=0.72 and δ=0.65 as a function of temperature. The hidden checker will compare each density value to paper‑reported reference values within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `delta`, `temperature`, `rho_liquid`, `rho_vapour`, `rho_lambda_line`
  - `units`:
    - `delta`: dimensionless
    - `temperature`: k_B T / J
    - `rho_liquid`: N σ^3 / V
    - `rho_vapour`: N σ^3 / V
    - `rho_lambda_line`: N σ^3 / V

### spinodals_hidden_binodal.csv
- path: `/app/outputs/spinodals_hidden_binodal.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Spinodal curves and hidden binodal coexistence densities for δ=0.57. The hidden checker compares the agent's computed densities to paper‑reported values with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `delta`, `temperature`, `S1`, `S2`, `S3`, `hidden_binodal_rho_liquid`, `hidden_binodal_rho_vapour`
  - `units`:
    - `delta`: dimensionless
    - `temperature`: k_B T / J
    - `S1`: N σ^3 / V
    - `S2`: N σ^3 / V
    - `S3`: N σ^3 / V
    - `hidden_binodal_rho_liquid`: N σ^3 / V
    - `hidden_binodal_rho_vapour`: N σ^3 / V

### topology_classification.txt
- path: `/app/outputs/topology_classification.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: One line per δ, formatted as 'δ=X: Y' where Y is a classification label. The hidden checker compares each line exactly to the expected label (e.g., 'δ=0.72: CEP').
- schema:
  - `type`: text
  - `required_columns`:
  - `items`: object

### mc_density_distribution.csv
- path: `/app/outputs/mc_density_distribution.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Probability density distribution p(ρ) for δ=0.665, T=1.044. The hidden checker will structurally audit that the distribution contains three well‑separated peaks in the expected density ranges (vapour, mixed liquid, demixed liquid).
- schema:
  - `type`: table
  - `required_columns`: `density_bin`, `probability`
  - `units`:
    - `density_bin`: N σ^3 / V
    - `probability`: normalized

Notes: The hidden checker will compare mean‑field coexistence and spinodal densities to paper‑reported reference values with tolerances set to absorb legitimate implementation spread. The MC density distribution is scored on structural grounds (three‑peak form); no exact reference values are required beyond the specified parameter point. Topology labels are matched exactly against the paper's classification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "mean_field_coexistence.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta",
          "temperature",
          "rho_liquid",
          "rho_vapour",
          "rho_lambda_line"
        ],
        "units": {
          "delta": "dimensionless",
          "temperature": "k_B T / J",
          "rho_liquid": "N σ^3 / V",
          "rho_vapour": "N σ^3 / V",
          "rho_lambda_line": "N σ^3 / V"
        }
      },
      "description": "Coexistence densities (liquid, vapour) and λ-line densities for δ=0.72 and δ=0.65 as a function of temperature. The hidden checker will compare each density value to paper‑reported reference values within tolerance."
    },
    {
      "file": "spinodals_hidden_binodal.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "delta",
          "temperature",
          "S1",
          "S2",
          "S3",
          "hidden_binodal_rho_liquid",
          "hidden_binodal_rho_vapour"
        ],
        "units": {
          "delta": "dimensionless",
          "temperature": "k_B T / J",
          "S1": "N σ^3 / V",
          "S2": "N σ^3 / V",
          "S3": "N σ^3 / V",
          "hidden_binodal_rho_liquid": "N σ^3 / V",
          "hidden_binodal_rho_vapour": "N σ^3 / V"
        }
      },
      "description": "Spinodal curves and hidden binodal coexistence densities for δ=0.57. The hidden checker compares the agent's computed densities to paper‑reported values with appropriate tolerances."
    },
    {
      "file": "topology_classification.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "required_columns": [],
        "items": {}
      },
      "description": "One line per δ, formatted as 'δ=X: Y' where Y is a classification label. The hidden checker compares each line exactly to the expected label (e.g., 'δ=0.72: CEP')."
    },
    {
      "file": "mc_density_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "density_bin",
          "probability"
        ],
        "units": {
          "density_bin": "N σ^3 / V",
          "probability": "normalized"
        }
      },
      "description": "Probability density distribution p(ρ) for δ=0.665, T=1.044. The hidden checker will structurally audit that the distribution contains three well‑separated peaks in the expected density ranges (vapour, mixed liquid, demixed liquid)."
    }
  ],
  "notes": "The hidden checker will compare mean‑field coexistence and spinodal densities to paper‑reported reference values with tolerances set to absorb legitimate implementation spread. The MC density distribution is scored on structural grounds (three‑peak form); no exact reference values are required beyond the specified parameter point. Topology labels are matched exactly against the paper's classification."
}
```

## How you are scored
A hidden verifier independently scores each scored artifact. For mean_field_coexistence.csv and spinodals_hidden_binodal.csv it will compare the reported densities to reference values with appropriate tolerances. topology_classification.txt is checked for exact label agreement. mc_density_distribution.csv is scored by a structural audit that verifies the presence of three well‑separated peaks (vapour, mixed liquid, demixed liquid). The contributions are weighted and combined into a final reward; simply reporting literature numbers is insufficient.
