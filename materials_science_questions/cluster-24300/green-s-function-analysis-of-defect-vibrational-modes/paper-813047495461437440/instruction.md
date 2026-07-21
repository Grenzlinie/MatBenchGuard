# Monte Carlo Study of Defect-Induced Casimir Effects in the 2D Ising Model

## Problem background
At the critical point, the two-dimensional Ising model exhibits scale invariance, and the introduction of lattice defects (vacancies) gives rise to long-range fluctuation forces known as the critical Casimir effect. This work studies two defect configurations: a curved line of vacancies and a pair consisting of a vacancy and a neighbouring occupied site (a "defect-antidefect" pair). The key quantities to compute are the specific bending energy per unit length as a function of curvature for the curved defect line, and the effective interaction energy as a function of separation for the defect-antidefect pair. Determining these quantities allows one to examine whether the defect-induced energies follow simple scaling laws and to determine the effective interaction between a defect and an antidefect.

## Approach
The central method is Monte Carlo simulation of the two-dimensional Ising model with coupling J=1, performed at the critical inverse temperature 1/T=0.44 on square lattices with periodic boundary conditions. A vacancy is a lattice site whose spin couplings to neighbours are set to zero, and a line of adjacent vacancies forms a defect line. Two simulation campaigns are carried out:

- **Curved defect lines**: For six lattice sizes (L=20,40,50,75,100,150), defect nodes are selected to form a circular arc of contour length L and varying curvature K=1/R. A reference run with a very small curvature K0 (nearly straight line) is also simulated. The total energy E_tot(K) is obtained from the Monte Carlo run, and the specific energy per unit length is extracted as e = (E_tot(K)-E_tot(K0))/L.

- **Defect-antidefect pairs**: On a 20×20 lattice, configurations containing a vacancy and an antidefect (an occupied site adjacent to the original vacancy position) are constructed for separation distances d from 1 to 10. A reference configuration is chosen where the two defects are placed at the maximum possible separation (half the lattice size). Monte Carlo runs give E_DA(d) and E_ref, and the interaction energy is computed as E_int(d)=E_DA(d)-E_ref.

All raw energy differences are saved in intermediate files, and the final reduced quantities (specific energy per length and interaction energy vs. distance) are written to the output CSV files specified below.

## Reproduction target
Produce two load-bearing output files under `/app/outputs`:

1. **`curved_line_energies.csv`** – a CSV file with columns `L`, `K`, `e_per_L`. `e_per_L` is the specific bending energy per unit length, defined as `(E_tot(K)-E_tot(K0))/L`, computed for each lattice size and a range of curvatures. The file provides the raw data that will be used to test whether a linear scaling law `E/L ∝ K L` holds at criticality.

2. **`pair_interaction_energies.csv`** – a CSV file with columns `distance`, `interaction_energy`. `interaction_energy` is defined as `E_DA(d)-E_ref`, computed for defect-antidefect separations d = 1,…,10 on a 20×20 lattice. The file provides the raw data that will be used to examine the functional form of the repulsive interaction and to extract an effective interaction strength.

## Assets
No external datasets, pre-trained models, or proprietary software are required. The entire workflow can be built from scratch using standard Python scientific packages such as `numpy`, `scipy`, and optionally `matplotlib`, all of which are publicly available via PyPI. The Monte Carlo algorithm and the defect-discretization scheme are described in the workflow steps and must be implemented by you.

## Workflow steps

### Step 1: Generate discretized defect arcs
- Role: process
- Action: For each lattice size L in {20,40,50,75,100,150} and a range of curvature values K=1/R (with integer R), generate a set of lattice nodes that approximate a circular arc of contour length L. Use the following discretization algorithm: (1) Place the circle centre at coordinates (L/2, L/2). (2) Choose the first defect node as the lattice point closest to the circle at a fixed starting angle, e.g., on the right side of the centre. (3) Continuously extend the arc by examining the two neighbour lattice points that are adjacent to the current defect position and lie in the forward direction along the contour; for each candidate, compute its Euclidean distance to the centre. Select the candidate that minimizes |distance - R|, i.e., the deviation from the circle radius. (4) Repeat until L defect nodes have been collected. (5) Treat the arc as a connected curve; the defect line consists of these L nodes. Also generate a reference arc with a very small curvature K0 using R = L * 10 (effectively a nearly straight line). Save the list of defect node coordinates for every (L,R) configuration.
- Evidence: `/app/outputs/defect_arcs.json`

### Step 2: Monte Carlo simulation for curved defect lines
- Role: process
- Action: Run a Monte Carlo simulation of the 2D Ising model with J=1 at inverse temperature 1/T=0.44, with periodic boundary conditions, for each defect configuration from Step 1 and the corresponding reference configuration. Collect the total energy E_tot(K) and E_tot(K0) for each simulation, ensuring adequate equilibration and statistics.
- Evidence: `/app/outputs/curved_line_raw_energies.json`

### Step 3: Compute specific energy for curved lines
- Role: scored (load-bearing)
- Action: For each lattice size L and curvature K, compute the specific energy per unit length e_per_L = (E_tot(K) - E_tot(K0)) / L. Write all records to curved_line_energies.csv with columns L, K, e_per_L.
- Output file: `/app/outputs/curved_line_energies.csv`
- Format: csv
- Contract: Columns: L (int), K (float), e_per_L (float)
- Scoring: scored by hidden verifier

### Step 4: Construct defect-antidefect pair configurations for multiple lattice sizes
- Role: process
- Action: For each lattice size L in {20, 30, 40, 50} with periodic boundaries, create configurations containing a defect-antidefect pair separated by distances d = 1,…,10, and a reference configuration where the defects are placed at the maximum possible separation (half the lattice size). Include the necessary discretised coordinates for all configurations.
- Evidence: `/app/outputs/pair_configs.json`

### Step 5: Monte Carlo simulations for defect-antidefect pairs
- Role: process
- Action: For each configuration from Step 4, run Monte Carlo simulations of the 2D Ising model (J=1) at a range of inverse temperatures spanning the critical region (e.g., 1/T from 0.35 to 0.50, with sufficiently small steps). Record the total energies E_DA(d, T, L) and E_ref(T, L) for every distance, temperature, and lattice size, ensuring proper equilibration and statistics.
- Evidence: `/app/outputs/pair_raw_energies.json`

### Step 6: Finite-size scaling and extrapolation to infinite volume
- Role: process
- Action: For each distance d and each lattice size L, extract the interaction energy as a function of temperature: E_int(d,T,L) = E_DA(d,T,L) – E_ref(T,L). For each fixed d and L, locate the peak (or maximum) of E_int as a function of 1/T in the simulated range (0.35 to 0.50). This peak value is the finite-size estimate of the critical interaction energy at that L. Then, for each distance d, extrapolate these peak values to infinite volume by fitting a linear function of 1/L to the peak energies across lattice sizes L=20,30,40,50. The intercept of the fit (L→∞) is the asymptotic interaction energy E_asymp(d) at the critical point 1/T=0.44. (Use linear regression of peak energies vs 1/L.)
- Evidence: none

### Step 7: Compute asymptotic defect-antidefect interaction energies
- Role: scored (load-bearing)
- Action: For each distance d, write the extrapolated asymptotic interaction energy E_asymp(d) to pair_interaction_energies.csv with columns distance and interaction_energy.
- Output file: `/app/outputs/pair_interaction_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### curved_line_energies.csv
- path: `/app/outputs/curved_line_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Specific bending energy per unit length for curved defect lines.
- schema:
  - `columns`: `L`, `K`, `e_per_L`
  - `dtypes`:
    - `L`: int
    - `K`: float
    - `e_per_L`: float

### pair_interaction_energies.csv
- path: `/app/outputs/pair_interaction_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Defect-antidefect interaction energies vs. separation.
- schema:
  - `columns`: `distance`, `interaction_energy`
  - `dtypes`:
    - `distance`: int
    - `interaction_energy`: float

Notes: The verifier will compute the linear coefficient a from the specific energy data (fit e_per_L vs KL) and the Coulomb constant a' from the pair interaction data (fit E_int vs 1/d). The agent must implement the discretization algorithm explicitly as described in step 1 and the finite-size scaling procedure as in step 6.

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/curved_line_energies.csv`
- `/app/outputs/pair_interaction_energies.csv`

## Output contract
See the machine-readable output contract rendered by the builder.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "/app/outputs/curved_line_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "L",
          "K",
          "e_per_L"
        ],
        "dtypes": {
          "L": "int",
          "K": "float",
          "e_per_L": "float"
        }
      },
      "description": "Specific bending energy per unit length for curved defect lines."
    },
    {
      "file": "/app/outputs/pair_interaction_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "columns": [
          "distance",
          "interaction_energy"
        ],
        "dtypes": {
          "distance": "int",
          "interaction_energy": "float"
        }
      },
      "description": "Defect-antidefect interaction energies vs. separation."
    }
  ],
  "notes": "The verifier will compute the linear coefficient a from the specific energy data (fit e_per_L vs KL) and the Coulomb constant a' from the pair interaction data (fit E_int vs 1/d). The agent must implement the discretization algorithm explicitly as described in step 1 and the finite-size scaling procedure as in step 6."
}
```

## How you are scored
A hidden verifier will read your two CSV files and independently assess them. The verifier will:

- Fit a linear model (no intercept) to the `(K·L, e_per_L)` pairs in `curved_line_energies.csv` and compare the fitted coefficient to a gold value extracted from the paper.
- Fit a Coulomb-like model (`interaction_energy ∝ 1/distance`) to the points in `pair_interaction_energies.csv` and compare the fitted constant to a second gold value.

Both fits are checked for the quality of agreement (e.g., R² for the first fit). The overall reward is a number between 0 and 1, with the two fits each contributing a substantial share. You do not need to perform these fits yourself; the verifier re-derives the quantities directly from your raw CSV data. No gold values or tolerance thresholds are disclosed to you.
