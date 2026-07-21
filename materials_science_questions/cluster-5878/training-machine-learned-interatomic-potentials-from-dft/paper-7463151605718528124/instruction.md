# Training and Evaluating a Differentiable Protein Structure Refinement Algorithm

## Problem background
Protein structure refinement aims to improve the accuracy of predicted three-dimensional models, narrowing the gap between computational predictions and high-resolution experimental structures. Conventional refinement methods rely on physics-based or knowledge-based force fields combined with stochastic sampling (e.g., molecular dynamics or Monte Carlo simulations). These approaches are computationally intensive and difficult to tune, often requiring thousands of CPU‑hours for a single protein. An alternative is to replace stochastic sampling with gradient‑based optimization, provided that a differentiable model of the interaction free energy can be constructed. This task targets the development and evaluation of such a fully differentiable refinement algorithm: the core question is whether a neural network force field can guide backbone dihedral angle optimization to consistently improve the structural quality of a large set of decoy models, measured by RMSD and GDT‑HA relative to the native structures.

## Approach
The refinement method combines three conceptual components:

1. **Neural network force field (NNFF)** – A local maximum likelihood approximation of the generalized solvation free energy is implemented as a four‑layer feed‑forward network. For each residue, 22 neighboring residues are selected and their identity (one‑hot), Cα–Cα distance, and six backbone dihedral angles are extracted. Two feature representations are used: one with raw angles (638‑dimensional input) and one with sine/cosine encoding (770‑dimensional input). The NNFF outputs a 21‑class distribution over residue identities; the energy contribution of each residue environment is the negative log‑probability of the correct identity.

2. **Coordinate transformation and optimization** – The backbone of a starting structure is converted from Cartesian coordinates to internal dihedral angles while keeping bond lengths and angles fixed. The NeRF algorithm reconstructs Cartesian coordinates from the updated dihedrals. The loss function is the NNFF‑derived energy plus a smooth‑L1 regularisation that limits the structural change, and optional per‑site entropy weights. Automatic differentiation is used to compute gradients of the total loss with respect to backbone φ and ψ angles, and gradient descent updates the dihedral angles iteratively.

3. **Benchmark and comparison** – The method is applied to a large decoy set derived from the public 3Drobot resource, filtered to exclude proteins with significant sequence homology to the training set. For each decoy, five iterations of gradient descent (learning rate 0.0005) are performed. The quality of the refined structures is assessed using two standard metrics: backbone Cα RMSD and GDT‑HA, computed relative to the corresponding native structure. The primary comparison is the change in these metrics before and after refinement, testing whether the NNFF‑driven differentiable protocol can improve structure quality on average.

## Reproduction target
Carry out the following reproducibility workflow and produce the required outputs:

1. **Build a training dataset** from high‑resolution protein structures in the Protein Data Bank. Extract per‑residue features for both input representations (638‑dim and 770‑dim) and save them as `training_features.npz`.

2. **Train two NNFF models** – a 638‑input model and a 770‑input model – for 30 epochs. Save the trained parameters as `model_638.pt` and `model_770.pt`.

3. **Prepare a benchmark decoy set** from the 3Drobot decoy dataset. Filter out decoys whose native proteins have >25% sequence identity to any structure used in the training set (or select the same set of 36 native proteins used in the original study, if the list is known). Create a CSV listing the decoy and native structure identifiers.

4. **Run the differentiable refinement** on every decoy in the benchmark with both trained models. Record the initial, final (after 5 iterations), and best‑among‑5‑iterations RMSD and GDT‑HA relative to the native structure. Aggregate all results into a CSV file with one row per decoy and columns: `native_id`, `decoy_id`, `initial_RMSD`, `final_RMSD`, `best_RMSD`, `initial_GDT_HA`, `final_GDT_HA`, `best_GDT_HA`.

The primary target is to produce the required output files and verify that they are correctly formatted.

## Assets

- 3Drobot decoy dataset: http://zhanglab.ccmb.med.umich.edu/3Drobot/
- Protein Data Bank (PDB): https://www.rcsb.org/
- PyTorch: https://pytorch.org/
- NumPy: https://numpy.org/
- BioPython: https://biopython.org/

## Workflow steps

### Step 1: Build training feature dataset
- Role: process
- Action: Select a non-redundant set of high-resolution protein structures from the Protein Data Bank (PDB). For each residue in each selected structure, extract 22 neighboring residues (6 upstream, 6 downstream, 10 nonadjacent) and compute per-neighbor features: a 22-dimensional one-hot identity vector, the Cα–Cα distance, and six backbone dihedral angles (Cα, C, N, Cβ). Prepare two feature matrices: one using raw dihedral angles (638-dimensional input) and one using sin/cos encoding (770-dimensional input). Save the resulting feature arrays and the corresponding residue identity labels as a training dataset.
- Evidence: `/app/outputs/training_features.npz`

### Step 2: Train NNFF models (638 and 770)
- Role: process
- Action: Implement a four-layer feed-forward neural network with architecture 638-512-512-512-21 for the raw-angle features and 770-512-512-512-21 for the sin/cos features. Train each model on the prepared training dataset for 30 epochs with a learning rate of 0.1. Save the trained model parameters (638-NNFF and 770-NNFF) as checkpoint files.
- Evidence: `/app/outputs/model_638.pt, model_770.pt`

### Step 3: Prepare benchmark decoy set
- Role: process
- Action: Download the 3Drobot decoy dataset. Identify the 36 native protein structures that have decoys and filter out any decoy/structure pairs with more than 25% sequence homology to the training set (or use the known list of 36 natives from the paper if available). Create a CSV file listing each selected decoy PDB file path and its corresponding native structure identifier.
- Evidence: `/app/outputs/benchmark_list.csv`

### Step 4: Run refinement and evaluate on benchmark
- Role: scored (load-bearing)
- Action: For every decoy in the benchmark set, run the GSFE-refinement algorithm using both the trained 638-NNFF and 770-NNFF models (learning rate 0.0005, 5 iterations). At each iteration, compute the backbone RMSD and GDT-HA of the refined structure relative to its native structure. Record the initial (iteration 0), final (iteration 5), and best (among the 5 iterations) values for both RMSD and GDT-HA. Aggregate all per-decoy results into a single CSV file with one row per decoy and columns for native protein ID, decoy ID, and the six numeric values (initial_RMSD, final_RMSD, best_RMSD, initial_GDT_HA, final_GDT_HA, best_GDT_HA).
- Output file: `/app/outputs/refinement_results.csv`
- Format: csv
- Contract: CSV with header row. Columns: native_id (string), decoy_id (string), initial_RMSD (float), final_RMSD (float), best_RMSD (float), initial_GDT_HA (float), final_GDT_HA (float), best_GDT_HA (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/refinement_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### refinement_results.csv
- path: `/app/outputs/refinement_results.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Per-decoy refinement results: RMSD and GDT-HA values at initial (iteration 0), final (iteration 5), and best among the 5 iterations. The checker will verify that on average RMSD decreases (ΔRMSD < 0) and GDT-HA increases (ΔGDT-HA > 0), and that a majority of decoys are improved.
- schema:
  - `type`: table
  - `required_columns`: `native_id`, `decoy_id`, `initial_RMSD`, `final_RMSD`, `best_RMSD`, `initial_GDT_HA`, `final_GDT_HA`, `best_GDT_HA`

Notes: The scoring is based on the directional structural trends (average RMSD improvement, average GDT-HA improvement, and fraction of decoys with reduced RMSD) rather than exact absolute values, because the training set is rebuilt from public PDB data, which introduces unavoidable variability in the metric numbers.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "refinement_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "native_id",
          "decoy_id",
          "initial_RMSD",
          "final_RMSD",
          "best_RMSD",
          "initial_GDT_HA",
          "final_GDT_HA",
          "best_GDT_HA"
        ]
      },
      "description": "Per-decoy refinement results: RMSD and GDT-HA values at initial (iteration 0), final (iteration 5), and best among the 5 iterations. The checker will verify that on average RMSD decreases (ΔRMSD < 0) and GDT-HA increases (ΔGDT-HA > 0), and that a majority of decoys are improved."
    }
  ],
  "notes": "The scoring is based on the directional structural trends (average RMSD improvement, average GDT-HA improvement, and fraction of decoys with reduced RMSD) rather than exact absolute values, because the training set is rebuilt from public PDB data, which introduces unavoidable variability in the metric numbers."
}
```

## How you are scored
A hidden verifier reads the output files and awards points based on the quality of the delivered artifacts.
