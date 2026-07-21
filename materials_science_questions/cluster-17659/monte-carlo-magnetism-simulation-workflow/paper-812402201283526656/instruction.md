# Zero-temperature interface properties of the 2D random sine-Gordon model

## Problem background
In the study of surface growth on disordered substrates, the two-dimensional random sine-Gordon model (RsGM) serves as a paradigmatic model for many glassy systems. At zero temperature, theoretical predictions differ on the scaling of the height-difference correlation function: one approach suggests a logarithmic law, while another predicts a squared-logarithmic law. Resolving this issue and understanding the finite-size behavior of the interface are essential for clarifying the nature of the disordered phase.

## Approach
The model is defined on a square lattice with periodic boundary conditions. The Hamiltonian is 
H = 0.5 ∑_{⟨i,j⟩} (φ_i – φ_j)² – V₀ ∑_i cos(φ_i – φ_i⁰),
where φ_i is a continuous height variable, V₀ is the pinning strength (taken as 1.0), and the quenched random phases φ_i⁰ are independent and uniformly distributed in (0,2π]. The zero-temperature overdamped Langevin dynamics is given by
φ̇_i = ∑_{j∈nn(i)} (φ_i – φ_j) + V₀ sin(φ_i – φ_i⁰).

Simulations are performed starting from random initial configurations, integrating until the squared interface width saturates. The squared interface width is defined as W² = ⟨⟨(φ_i – ⟨φ_i⟩)²⟩⟩_d, where ⟨·⟩ denotes a spatial average and ⟨·⟩_d the disorder average over at least 10 independent realizations. For L=128, 256, and 512, we compute the disorder-averaged saturated W². From the final configurations of the L=256 runs we compute the height-difference correlation function C(r) = ⟨⟨(φ_i – φ_{i+r})²⟩⟩_d for integer r up to L/2.

## Reproduction target
Simulate the zero-temperature Langevin dynamics of the 2D random sine-Gordon model on lattices of sizes L=128, 256, and 512. From the final configurations, compute the disorder-averaged saturated squared interface width W² for each size, and compute the height-difference correlation function C(r) for L=256. Deliver the results in the designated CSV files. The results are evaluated by a hidden verifier using structural consistency checks.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Generate disorder and run zero-temperature Langevin dynamics
- Role: process
- Action: For lattice sizes L=128, 256, and 512, generate N≥10 independent realizations of the quenched disorder φ⁰ (uniform in (0,2π]) and evolve the zero-temperature overdamped Langevin dynamics from random initial configurations until the squared interface width W² saturates. Save a log of the runs as evidence.
- Evidence: `/app/outputs/simulation_log.txt`

### Step 2: Verify initial-condition independence
- Role: process
- Action: Choose one lattice size (e.g., L=256) and run a few additional simulations starting from markedly different initial conditions. Compare the asymptotic W² values; they should be statistically the same to within a small tolerance. Document the result.
- Evidence: `/app/outputs/initial_condition_check.json`

### Step 3: Finite-size independence of saturated width
- Role: scored (load-bearing)
- Action: From the final configurations of the simulations, compute the disorder-averaged saturated squared interface width W² for each L and save the mean and standard deviation.
- Output file: `/app/outputs/step_02_saturation_widths.csv`
- Format: csv
- Contract: Columns: L (int), saturated_W2 (float), std_W2 (float)
- Scoring: scored by hidden verifier

### Step 4: Height-difference correlation function
- Role: scored (load-bearing)
- Action: From the final configurations of the L=256 simulations (averaged over disorder realizations), compute the height-difference correlation function C(r) for integer r=1 up to L/2. Save r and the disorder-averaged C(r).
- Output file: `/app/outputs/step_03_correlation_function.csv`
- Format: csv
- Contract: Columns: r (int), C_r (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_02_saturation_widths.csv`
- `/app/outputs/step_03_correlation_function.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_02_saturation_widths.csv
- path: `/app/outputs/step_02_saturation_widths.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The finite-size independence check: three rows for L=128, 256, 512 giving the disorder-averaged saturated squared interface width and its standard deviation. The checker verifies that the three values are within a small relative tolerance of each other.
- schema:
  - `type`: table
  - `required_columns`: `L`, `saturated_W2`, `std_W2`

### step_03_correlation_function.csv
- path: `/app/outputs/step_03_correlation_function.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: The height-difference correlation function for L=256, averaged over disorder realizations. The checker will assess the scaling behavior of C(r) using a hidden validation function to determine whether the predicted correlation law holds.
- schema:
  - `type`: table
  - `required_columns`: `r`, `C_r`

Notes: No gold values from the paper are disclosed. The checker only verifies intra-artifact consistency (finite-size independence) and functional form (log-squared scaling).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_02_saturation_widths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "L",
          "saturated_W2",
          "std_W2"
        ]
      },
      "description": "The finite-size independence check: three rows for L=128, 256, 512 giving the disorder-averaged saturated squared interface width and its standard deviation. The checker verifies that the three values are within a small relative tolerance of each other."
    },
    {
      "file": "step_03_correlation_function.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "r",
          "C_r"
        ]
      },
      "description": "The height-difference correlation function for L=256, averaged over disorder realizations. The checker will assess the scaling behavior of C(r) using a hidden validation function to determine whether the predicted correlation law holds."
    }
  ],
  "notes": "No gold values from the paper are disclosed. The checker only verifies intra-artifact consistency (finite-size independence) and functional form (log-squared scaling)."
}
```

## How you are scored
The hidden verifier independently scores each output file. For `step_02_saturation_widths.csv`, it checks that the three saturated W² values are consistent across lattice sizes (their relative deviation from the mean must be below a threshold). For `step_03_correlation_function.csv`, it computes the Pearson correlation between C(r) and an appropriate function of r over a defined range of r to assess functional-form agreement. Each scored artifact receives a weight, and the final score is a weighted sum. Simply reporting numbers without running genuine simulations will not satisfy these checks.
