# 2D BEC Liquid Excitation Spectrum and Roton Minima

## Problem background
Ultracold quantum droplets form in a two-component Bose-Einstein condensate (BEC) when the mean‑field attraction between the components is balanced by repulsive beyond‑mean‑field quantum fluctuations (Lee‑Huang‑Yang correction). In two dimensions the LHY term takes a logarithmic form. When spin‑orbit coupling (SOC) is added, the ground‑state density landscape changes and the collective excitation spectrum can develop roton minima — local minima in the excitation energy at non‑zero momentum — instead of being purely phonon‑like. Understanding how the strength of the short‑range interaction affects the number of roton minima is important for assessing the stability and properties of 2D liquid films. The present task asks you to compute this number: for a fixed Rashba SOC strength, how many roton minima appear in the lowest excitation branch for weak, intermediate, and strong contact interactions?

## Approach
We consider a uniform two‑component BEC in two dimensions, described by coupled Gross–Pitaevskii equations that include kinetic energy, equal‑magnitude intraspecies repulsion and interspecies attraction (all of strength g), a 2D logarithmic LHY quantum‑fluctuation term, and Rashba spin‑orbit coupling of strength λ_R (the Dresselhaus component is set to zero). The ground‑state wavefunctions are obtained by imaginary‑time propagation on a sufficiently large 2D grid for N=150 atoms. Once the stationary densities are known, small perturbations are introduced and the Bogoliubov matrix (a 4×4 system for the two‑component field) is constructed. Diagonalizing this matrix for a range of quasimomentum vectors q = (q_x,0) yields the excitation spectrum. The lowest positive eigenvalue ω_lowest(q_x) is the quantity of interest; detecting local minima in ω_lowest(q_x) away from q_x=0 identifies the roton minima. The whole procedure is carried out for three interaction strengths g = 3, 10, 15, all with λ_R = 0.2 and N = 150.

## Reproduction target
For a two‑component 2D BEC with Rashba SOC (λ_R = 0.2, λ_D = 0) and N = 150 atoms, compute the lowest Bogoliubov excitation energy ω_lowest as a function of quasimomentum q_x ∈ [0, 6] (q_y = 0) for three interaction strengths: g = 3, 10, 15. From each dispersion curve, determine the number of local minima (roton minima) that occur for q_x > 0. The final deliverables are: (i) a CSV file containing the raw excitation energies for all q_x points and g values (step_03_dispersion.csv), and (ii) a CSV file with the counted number of roton minima for each g (step_04_roton_counts.csv).

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Ground state density computation
- Role: process
- Action: Solve the coupled time-dependent Gross-Pitaevskii equations for a two-component 2D BEC with Rashba SOC (λ_R=0.2, λ_D=0) using imaginary-time propagation on a sufficiently large uniform 2D grid. Run for interaction strengths g=3, 10, 15 with N=150 atoms. Obtain stationary wavefunctions ψ1, ψ2 and total density ρ.
- Evidence: `/app/outputs/ground_state_density.txt`

### Step 2: Bogoliubov excitation dispersion
- Role: scored
- Action: For each g, construct the 4×4 Bogoliubov matrix from the ground state solution and diagonalize it for q_x ranging from 0 to 6 (step ≤0.05, q_y=0). Extract the lowest positive excitation eigenvalue.
- Output file: `/app/outputs/step_03_dispersion.csv`
- Format: csv
- Contract: Columns: g (int), q_x (float), q_y (float, all 0.0), omega_lowest (float, dimensionless units).
- Scoring: scored by hidden verifier

### Step 3: Roton minima identification
- Role: scored (load-bearing)
- Action: Analyze the dispersion data in step_03_dispersion.csv. For each g, detect local minima in omega_lowest as a function of q_x (ignore the endpoint q_x=0). Count the number of minima.
- Output file: `/app/outputs/step_04_roton_counts.csv`
- Format: csv
- Contract: Columns: g (int), num_minima (int). Three rows: g=3, 10, 15.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_dispersion.csv`
- `/app/outputs/step_04_roton_counts.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_dispersion.csv
- path: `/app/outputs/step_03_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Raw excitation energies for the lowest Bogoliubov branch; checked for existence, adequate q-point density (≥100 per g), correct columns, and used for a consistency cross-check on the reported roton count.
- schema:
  - `type`: table
  - `required_columns`: `g`, `q_x`, `q_y`, `omega_lowest`

### step_04_roton_counts.csv
- path: `/app/outputs/step_04_roton_counts.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Number of local minima in the lowest excitation branch for each interaction strength; compared to the paper-reported hidden gold with exact match (0 for g=3, 1 for g=10, 2 for g=15).
- schema:
  - `type`: table
  - `required_columns`: `g`, `num_minima`

Notes: step_03_dispersion.csv is required for anti-gaming integrity: the checker will validate it exists, has sufficient q-points, and the agent's reported num_minima is consistent with a simple minima count on the submitted dispersion data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "g",
          "q_x",
          "q_y",
          "omega_lowest"
        ]
      },
      "description": "Raw excitation energies for the lowest Bogoliubov branch; checked for existence, adequate q-point density (≥100 per g), correct columns, and used for a consistency cross-check on the reported roton count."
    },
    {
      "file": "step_04_roton_counts.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "g",
          "num_minima"
        ]
      },
      "description": "Number of local minima in the lowest excitation branch for each interaction strength; compared to the paper-reported hidden gold with exact match (0 for g=3, 1 for g=10, 2 for g=15)."
    }
  ],
  "notes": "step_03_dispersion.csv is required for anti-gaming integrity: the checker will validate it exists, has sufficient q-points, and the agent's reported num_minima is consistent with a simple minima count on the submitted dispersion data."
}
```

## How you are scored
Your submission is scored by a hidden verifier that evaluates the output artifacts against a reference expectation derived from the paper’s reported trend. The scoring works as follows:

- **step_03_dispersion.csv**: The verifier checks that the file exists, contains the required columns (g, q_x, q_y, omega_lowest), covers the q_x range [0,6] with at least 100 points per g, and uses q_y=0 for all rows. No direct numeric reward is given for this file; it is required for anti‑gaming integrity.
- **step_04_roton_counts.csv**: The verifier reads the num_minima for g=3,10,15 and compares them to the hidden gold with exact matching of the integer counts. Additionally, the verifier performs a consistency cross‑check by re‑counting local minima directly from your submitted dispersion data; a mismatch between your reported count and the count derived from your own dispersion data results in a penalty.

The final reward (0–1) is a weighted combination of the roton‑count correctness and the consistency cross‑check. Simply reporting the expected counts without submitting a valid, self‑consistent dispersion file will not pass the cross‑check. No gold values or tolerances are disclosed in the instruction; you must produce the underlying physics simulation and analysis to obtain the correct answers.
