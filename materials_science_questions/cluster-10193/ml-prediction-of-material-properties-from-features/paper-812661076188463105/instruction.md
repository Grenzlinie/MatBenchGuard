# Predicting Tracer Self‑Diffusion in Triblock Copolymer Pores from Minkowski Functionals via Random Forest Regression

## Problem background
Block copolymers self-assemble into nanostructured porous membranes with potential applications in water purification and batteries. A central engineering challenge is predicting solute transport (self-diffusion coefficient D) from the morphology of the pores. This problem is especially complex for ABC triblock copolymers, which form both equilibrium and nonequilibrium, kinetically trapped structures. The morphological descriptors known as Minkowski functionals — volume (v), surface area (s), integrated mean curvature (h), and integrated Gaussian curvature (g) — offer a compact geometric characterization of the pore network. The key hypothesis is that D correlates strongly with a subset of these functionals, enabling accurate prediction from morphology alone via machine learning.

## Approach
A computational pipeline is employed to test this hypothesis. First, self-consistent field theory (SCFT) is used to generate a library of ABC triblock copolymer morphologies under specified interaction parameters and block fractions, focusing on nonequilibrium quenches in the lamella-forming region. Each continuous morphology is digitized onto a cubic lattice and a pore map is defined by thresholding the local composition. For each percolated morphology, the tracer self-diffusion coefficient D is obtained from unbiased lattice random walk simulations, while the four intensive Minkowski functionals are computed on the same digitized pore lattice using a voxel-counting algorithm. A random forest regressor is trained on the (v,s,h,g) features and D/D0 labels from an ensemble of morphologies, and its predictive performance is evaluated on a held-out test set.

## Reproduction target
Implement the full pipeline to generate a set of nonequilibrium triblock copolymer morphologies, compute their tracer self-diffusion coefficients, and compute their four intensive Minkowski functionals. Train a random forest regression model to predict D/D0 from (v,s,h,g) using an 80/20 train/test split of the generated data. Report the mean absolute error (MAE) on the held-out test set and the feature importance scores of the four descriptors. Write the results to /app/outputs/regression_results.json.

## Assets

- Polymer Self‑Consistent Field Theory (PSCF) software: https://pscf.ce.ucsb.edu/
- scikit‑learn: scikit-learn
- NetworkX: networkx

## Workflow steps

### Step 1: SCFT Morphology Generation
- Role: process
- Action: Generate equilibrium and nonequilibrium ABC triblock copolymer morphologies using self‑consistent field theory (SCFT). Use interaction parameters χ_AC N=35, χ_AB N=χ_BC N=13. Generate at least 5 independent nonequilibrium morphologies for each of a few state points in the lamella‑forming region (e.g., fB=0.05 and fA=0.35,0.40,0.45) by quenching fields from random initial conditions and relaxing to a saddle point. Use cubic simulation cells with edge length around 14Rg or 16Rg and a field‑grid resolution of approximately 0.25Rg. Output continuous volume‑fraction fields φ_i(r) for each morphology.
- Evidence: `/app/outputs/scft_output_log.txt`

### Step 2: Digitization and Pore Definition
- Role: process
- Action: Digitize each continuous morphology onto a simple cubic lattice with spacing a=0.25Rg (where Rg is the polymer radius of gyration). Label each lattice site as pore if φ_B(r)+φ_C(r) ≥ 0.5, else solid. Produce a binary pore map (3‑D array of 0/1) for every morphology.
- Evidence: `/app/outputs/digitization_log.txt`

### Step 3: Percolation Analysis and Lattice Random Walk
- Role: process
- Action: For each digitized morphology, find connected clusters of pore sites under periodic boundary conditions and test percolation along each Cartesian axis. Discard any morphology that lacks a percolated pore cluster. For each retained morphology, simulate unbiased lattice random walks: 5000 walkers initialized uniformly in the percolated pore sites, each attempting one displacement per step to one of six adjacent sites (displacement accepted only if the target is a pore site). Time step τ = a²/(6D0), where D0 is the free‑lattice diffusion coefficient. Generate trajectories of up to 4×10⁵ steps, compute the ensemble‑averaged three‑dimensional mean‑squared displacement, and extract the diffusion coefficient D from the long‑time slope (t ≥ 512 τ). Record D/D0 for each morphology.
- Evidence: `/app/outputs/random_walk_log.txt`

### Step 4: Minkowski Functional Computation
- Role: process
- Action: For each percolated morphology, compute the four intensive Minkowski functionals (volume v, surface area s, integrated mean curvature h, integrated Gaussian curvature g) from the binary pore lattice using a voxel‑counting algorithm (e.g., the Michielsen–De Raedt method). Normalize all functionals by the total simulation cell volume. Store the feature vector (v,s,h,g) and the corresponding D/D0 label for each morphology.
- Evidence: `/app/outputs/minkowski_features.csv`

### Step 5: Random Forest Regression and Evaluation
- Role: scored (load-bearing)
- Action: Assemble the (v,s,h,g) features and D/D0 labels for all nonequilibrium morphologies. Shuffle the data and split into 80% training and 20% held‑out test sets. Train a random forest regressor (from scikit‑learn) on the training set. Predict D/D0 on the test set, compute the mean absolute error (MAE) in D/D0 units, and extract the feature importance scores (e.g., mean decrease in impurity). Write the results to /app/outputs/regression_results.json.
- Output file: `/app/outputs/regression_results.json`
- Format: json
- Contract: JSON object with keys 'test_mae' (float, D/D0 units) and 'feature_importance' (object with keys 'v','s','h','g', each a float value).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/regression_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### regression_results.json
- path: `/app/outputs/regression_results.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The regression result is scored by checking that the reported test MAE meets a hidden reference threshold (lower is better) and that the feature importance ranking corresponds to the expected order of importance.
- schema:
  - `type`: object
  - `required`:
    - `test_mae`: float
    - `feature_importance`: object
  - `properties`:
    - `feature_importance`:
      - `type`: object
      - `required`:
        - `v`: float
        - `s`: float
        - `h`: float
        - `g`: float

Notes: The workflow must re‑derive the complete pipeline; no pre‑made morphological dataset or pre‑trained model is provided. The random forest hyperparameters and exact implementation are the agent's choice. The checker verifies only the final regression_results.json.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "regression_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "test_mae": "float",
          "feature_importance": "object"
        },
        "properties": {
          "feature_importance": {
            "type": "object",
            "required": {
              "v": "float",
              "s": "float",
              "h": "float",
              "g": "float"
            }
          }
        }
      },
      "description": "The regression result is scored by checking that the reported test MAE meets a hidden reference threshold (lower is better) and that the feature importance ranking corresponds to the expected order of importance."
    }
  ],
  "notes": "The workflow must re‑derive the complete pipeline; no pre‑made morphological dataset or pre‑trained model is provided. The random forest hyperparameters and exact implementation are the agent's choice. The checker verifies only the final regression_results.json."
}
```

## How you are scored
The hidden verifier independently scores the regression_results.json artifact. It compares the reported test MAE against a hidden performance threshold and checks that the feature importance ranking matches the expected ordering. Full credit is awarded only if both conditions are satisfied. The process steps (SCFT, digitization, random walk, Minkowski calculations) are not directly scored, but their execution is enforced because the regression step can only succeed with the generated features and labels.
