# Bragg-Williams Modeling of Two-Step Ordering in Pt-Based Alloys

## Problem background
Pt-based alloys with compositions CuMnPt6, MnPt7, and CuPt7 undergo a two-step ordering transition from a disordered face-centered cubic (fcc) solid solution, first to a Cu3Au-type (L12) intermediate ordered phase and then to a novel ABC6-type ordered structure. The two-step ordering can be described by a statistical thermodynamic model within the Bragg-Williams approximation. The model introduces long-range order parameters S1 (quantifying the degree of Cu3Au-type sublattice ordering) and S3 (capturing additional order among the corner sublattice atoms) and predicts their equilibrium values as functions of temperature by minimizing the free energy. This task reproduces the computational thermodynamic analysis of the two-step ordering for CuMnPt6 and MnPt7, requiring the computation of the equilibrium order parameter curves S1(T) and S3(T) from the Bragg-Williams free-energy model using the published pair interaction energies.

## Approach
The free energy F = U - Tφ is expressed in terms of S1 and S3 for each alloy. For CuMnPt6, the internal energy per atom (in units of the Boltzmann constant k) is

U/k = (3/32)[ A * S1² + 4 (W_CuMn/k) S3² ] + constant

where A/k = -6053 K and W_CuMn/k = -395 K. The configurational entropy per atom is

φ/k = -(1/32)[ (1+3S1+4S3) ln(1+3S1+4S3) + (1+3S1-4S3) ln(1+3S1-4S3) + 12(1-S1) ln(1-S1) + 6(3+S1) ln(3+S1) ] - (1/4)(3 ln3 - ln8 - 3 ln4).

For MnPt7, the order parameters are defined as S1 = 4(x - P_C) with x=1/8 and S3 = P_A - P_B, where P_A, P_B, P_C are the probabilities of finding an Mn atom on sublattices A, B, C (A and B each contain 4 sites, C contains 24 sites in the 32-atom unit cell). The probabilities are expressed in terms of S1 and S3 as

P_C = 1/8 - S1/4,
P_A = (1/4 + 3S1/2 + S3)/2,
P_B = (1/4 + 3S1/2 - S3)/2.

The internal energy per atom is

U/k = (3/32)[ (4 V_MnPt/k - 6 W_MnPt/k) S1² + 4 (W_MnPt/k) S3² ] + constant,

with V_MnPt/k = -1517 K, W_MnPt/k = -318 K. The configurational entropy per atom is

φ/k = -(1/32)[ 4 (P_A ln P_A + (1-P_A) ln(1-P_A)) + 4 (P_B ln P_B + (1-P_B) ln(1-P_B)) + 24 (P_C ln P_C + (1-P_C) ln(1-P_C)) ].

For each alloy, implement the free energy F(S1,S3,T) = k * (U/k - T * (φ/k)) (up to an additive constant that does not affect the equilibrium values) and numerically minimize F with respect to S1 and S3 at each temperature. The minimization should respect S1 ≥ 0, S3 ≥ 0, and the equilibrium state corresponds to the global minimum (the physically meaningful solution). Compute S1(T) and S3(T) for 800 K to 1300 K in steps of 10 K.

## Reproduction target
Produce two CSV files:

- CuMnPt6_order.csv with columns T (K), S1, S3 for CuMnPt6.
- MnPt7_order.csv with columns T (K), S1, S3 for MnPt7.

The computed order parameter curves must capture the two-step ordering character: S1 should show a discontinuous (first-order) transition at the higher transition temperature, and S3 should emerge below a lower characteristic temperature, consistent with the Bragg-Williams analysis.

## Assets

- numpy: https://pypi.org/project/numpy/
- scipy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Implement Bragg-Williams free energy model
- Role: process
- Action: Write Python code that defines the internal energy U and entropy φ as functions of order parameters S1, S3 (and alloy composition) using the analytical expressions provided in the paper. Hardcode the published interatomic interaction energies (in units of k) and the fixed composition ratios. Provide a function that returns the Helmholtz free energy F = U - T*φ for a given temperature T.
- Evidence: `/app/outputs/model_implementation.py`

### Step 2: Calculate order parameters for CuMnPt6
- Role: scored (load-bearing)
- Action: For CuMnPt6, using the free-energy function from step1, minimise F with respect to S1 and S3 at each temperature from 800 K to 1300 K (step 10 K). Solve for the equilibrium S1, S3 by starting from appropriate initial guesses and selecting the physically meaningful minimum (S1 ≥ 0, S3 ≥ 0). Write the results as a CSV file.
- Output file: `/app/outputs/CuMnPt6_order.csv`
- Format: csv
- Contract: T (float, in K), S1 (float), S3 (float). Each row corresponds to one temperature step.
- Scoring: scored by hidden verifier

### Step 3: Calculate order parameters for MnPt7
- Role: scored (load-bearing)
- Action: For MnPt7, similarly minimise the free energy (using the appropriate energy parameters and alloy composition) over the same temperature range and write the resulting S1, S3 curves.
- Output file: `/app/outputs/MnPt7_order.csv`
- Format: csv
- Contract: T (float, in K), S1 (float), S3 (float). Each row corresponds to one temperature step.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/CuMnPt6_order.csv`
- `/app/outputs/MnPt7_order.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### CuMnPt6_order.csv
- path: `/app/outputs/CuMnPt6_order.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium order parameters S1 and S3 for CuMnPt6 as functions of temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `S1`, `S3`
  - `units`:
    - `T`: K

### MnPt7_order.csv
- path: `/app/outputs/MnPt7_order.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Equilibrium order parameters S1 and S3 for MnPt7 as functions of temperature.
- schema:
  - `type`: table
  - `required_columns`: `T`, `S1`, `S3`
  - `units`:
    - `T`: K

Notes: The checker recomputes S1 and S3 from the same Bragg-Williams free energy model and compares the agent's values within tolerance; also verifies transition temperatures within 5% of paper-reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "CuMnPt6_order.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "S1",
          "S3"
        ],
        "units": {
          "T": "K"
        }
      },
      "description": "Equilibrium order parameters S1 and S3 for CuMnPt6 as functions of temperature."
    },
    {
      "file": "MnPt7_order.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "T",
          "S1",
          "S3"
        ],
        "units": {
          "T": "K"
        }
      },
      "description": "Equilibrium order parameters S1 and S3 for MnPt7 as functions of temperature."
    }
  ],
  "notes": "The checker recomputes S1 and S3 from the same Bragg-Williams free energy model and compares the agent's values within tolerance; also verifies transition temperatures within 5% of paper-reported values."
}
```

## How you are scored
A hidden verifier independently re-implements the same Bragg-Williams free-energy model for each alloy using the published interaction energies, recomputes the equilibrium S1 and S3 at the same temperature points, and compares your output CSV values element-wise against this recomputed reference. The verifier also extracts the transition temperatures (where S1 jumps and S3 begins to rise from zero) from your data and checks that they agree with the paper-reported values within a relative tolerance. The final reward is the weighted combination of the scores for the two scored output files, with larger weight on correct replication of the order parameter curves and transition temperatures.
