# Grain boundary energy prediction with machine learning for Cu symmetric tilt boundaries

## Problem background
Grain boundaries, the interfaces between differently oriented crystals, dictate many mechanical, thermal, and electrical properties of polycrystalline materials. Finding the most stable atomic arrangement and energy of a grain boundary is challenging because even for a simplified coincidence-site-lattice (CSL) boundary hundreds to thousands of rigid-body translations of one grain relative to the other must be evaluated, each requiring a costly static-lattice or first-principles calculation. This exhaustive search makes systematic studies across many boundary types prohibitively expensive. Here we focus on [001]-axis symmetric-tilt CSL grain boundaries in face-centred cubic copper. The central question is whether machine learning can reduce the computational cost dramatically by predicting the most stable rigid-body translation state and the boundary energy from a rapid analysis of the initial, pre-relaxation atomic geometry alone.

## Approach
We use support vector regression (SVR) trained on geometric descriptors computed from pre-relaxation atomic configurations. The training data are generated for four reference grain boundaries: Σ5[001]/(210), Σ5[001]/(310), Σ17[001]/(410), and Σ17[001]/(350). For each of these boundaries, a large set of rigid-body translation configurations is created by stepping through the three translation components (X, Z, and Y) within physically plausible ranges. Each configuration is relaxed with static-lattice calculations using an embedded-atom method (EAM) potential for Cu, yielding the ground-state grain boundary energy. From every initial (unrelaxed) configuration, 12 primary geometric descriptors—such as atomic density, shortest and longest bond length, and other local structural measures—are computed. Those 12 descriptors are then expanded through squares, inverses, exponentials, and exponential inverses to produce a total of 83 descriptors. The descriptor vectors are standardized to zero mean and unit variance.

An SVR model with a Gaussian (RBF) kernel is trained to map the 83 pre-relaxation descriptors to the relaxed grain boundary energy. Hyperparameters (epsilon-tube radius, cost, kernel variance) are selected via cross-validation to balance accuracy and generalisation. For an unseen boundary, e.g., Σ13[001]/(230), the same translation configurations are generated, descriptors are computed, and the trained model predicts the boundary energy for each translation. The translation with the lowest predicted energy is taken as the most stable state. A single static-lattice relaxation is then carried out for that predicted state to obtain the true relaxed energy. The same prediction‑plus‑relaxation protocol is applied to 12 additional unseen boundaries: Σ25, Σ29, Σ37, Σ41, Σ53, Σ61, and Σ125, each with two distinct boundary planes. The atomic supercells are built from the standard FCC Cu lattice (a ≈ 3.615 Å) using CSL theory and the specified plane indices. All static-lattice calculations are performed with LAMMPS and the Cleri & Rosato EAM potential.

## Reproduction target
Your task is to implement the full pipeline described above and produce two scored output files:

1. **Σ13 targeted prediction** — `/app/outputs/sigma13_predictions.json`: Use the four training boundaries to train the SVR model. Then, for the Σ13[001]/(230) test boundary, identify the rigid-body translation that minimises the predicted energy, record that translation and both the pre‑relaxation predicted energy and the energy obtained after one static-lattice relaxation. Follow the JSON contract exactly.

2. **Energy‑versus‑misorientation curve** — `/app/outputs/all_unseen_energies.csv`: Extend the prediction‑and‑relaxation procedure to all 12 additional unseen boundaries listed above, and also include the Σ13 result. Compute the misorientation angle for each boundary from its CSL Σ value. Write a CSV containing one row per boundary with columns `boundary`, `misorientation_angle_deg`, `pre_relaxation_energy`, and `relaxed_energy`, covering all 13 boundaries. The set of relaxed energies, when plotted against misorientation angle, must exhibit a convex shape with a maximum near 45°, and the curve must show local energy drops (cusps) at misorientation angles of 36.87° and 53.13°, which correspond to the training boundaries. The pre‑relaxation energies should follow the same qualitative trend.

## Assets

- LAMMPS molecular dynamics package: https://www.lammps.org/
- scikit-learn: scikit-learn
- Cu EAM potential (Cleri & Rosato 1991)
- NumPy, SciPy, pandas: numpy scipy pandas
- Grain boundary geometry definitions (CSL parameters)

## Workflow steps

### Step 1: Generate training data and train SVR model
- Role: process
- Action: For the four training grain boundaries (Σ5[001]/(210), Σ5[001]/(310), Σ17[001]/(410), Σ17[001]/(350)), generate atomic supercells and perform static‑lattice relaxations for many rigid‑body translation states using LAMMPS and the Cu EAM potential. From each initial configuration, compute the 12 geometric descriptors and their transformations to obtain 83 standardized descriptors. Train an SVR model with Gaussian kernel on these descriptors to predict grain‑boundary energy. Save the trained model, scaler, and descriptor code for reuse.
- Evidence: `/app/outputs/training_log.txt`

### Step 2: Predict Σ13 most stable state and relaxed energy
- Role: scored (load-bearing)
- Action: Generate initial atomic configurations for the Σ13[001]/(230) test boundary by varying rigid‑body translations. Compute the standardized 83 descriptors and use the trained SVR model to predict the most stable translation state (minimum predicted energy) and its pre‑relaxation energy. Then perform a single static‑lattice relaxation of that predicted state using LAMMPS to obtain the relaxed grain‑boundary energy. Write a JSON file containing the boundary name, the three translation coordinates, and both energies.
- Output file: `/app/outputs/sigma13_predictions.json`
- Format: json
- Contract: {"type": "object", "required": {"boundary": "string", "predicted_translation_X": "float", "predicted_translation_Y": "float", "predicted_translation_Z": "float", "pre_relaxation_energy": "float", "relaxed_energy": "float"}, "units": {"pre_relaxation_energy": "J/m²", "relaxed_energy": "J/m²"}}
- Scoring: scored by hidden verifier

### Step 3: Predict energies for all 13 unseen boundaries
- Role: scored (load-bearing)
- Action: Repeat the prediction‑and‑relaxation procedure for the remaining 12 unseen boundaries (Σ25, Σ29, Σ37, Σ41, Σ53, Σ61, Σ125 with two plane indices each) and include the Σ13 results. For each boundary, identify the most stable state via the SVR model, record the pre‑relaxation predicted energy, run one static‑lattice relaxation, and record the relaxed energy. Compute the misorientation angle from the CSL Σ value. Write a CSV file with columns: 'boundary', 'misorientation_angle_deg', 'pre_relaxation_energy', 'relaxed_energy', covering all 13 boundaries.
- Output file: `/app/outputs/all_unseen_energies.csv`
- Format: csv
- Contract: columns: boundary (string), misorientation_angle_deg (float, degrees), pre_relaxation_energy (float, J/m²), relaxed_energy (float, J/m²)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sigma13_predictions.json`
- `/app/outputs/all_unseen_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sigma13_predictions.json
- path: `/app/outputs/sigma13_predictions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Predicted most-stable rigid-body translation and pre-/post-relaxation energies for Σ13[001]/(230). Subject to hidden gold comparison and self-consistency check.
- schema:
  - `type`: object
  - `required`:
    - `boundary`: string
    - `predicted_translation_X`: float
    - `predicted_translation_Y`: float
    - `predicted_translation_Z`: float
    - `pre_relaxation_energy`: float
    - `relaxed_energy`: float
  - `units`:
    - `pre_relaxation_energy`: J/m²
    - `relaxed_energy`: J/m²

### all_unseen_energies.csv
- path: `/app/outputs/all_unseen_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Pre-relaxation and relaxed grain-boundary energies vs misorientation angle for all 13 unseen boundaries. Used to verify the energy-versus-misorientation profile.
- schema:
  - `type`: table
  - `required_columns`: `boundary`, `misorientation_angle_deg`, `pre_relaxation_energy`, `relaxed_energy`
  - `units`:
    - `misorientation_angle_deg`: degrees
    - `pre_relaxation_energy`: J/m²
    - `relaxed_energy`: J/m²

Notes: The agent must implement the full pipeline from atomic configurations to SVR training and predictions. The checker will validate the JSON and CSV formats and perform structural and hidden reference checks as appropriate.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sigma13_predictions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "boundary": "string",
          "predicted_translation_X": "float",
          "predicted_translation_Y": "float",
          "predicted_translation_Z": "float",
          "pre_relaxation_energy": "float",
          "relaxed_energy": "float"
        },
        "units": {
          "pre_relaxation_energy": "J/m²",
          "relaxed_energy": "J/m²"
        }
      },
      "description": "Predicted most-stable rigid-body translation and pre-/post-relaxation energies for Σ13[001]/(230). Subject to hidden gold comparison and self-consistency check."
    },
    {
      "file": "all_unseen_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "boundary",
          "misorientation_angle_deg",
          "pre_relaxation_energy",
          "relaxed_energy"
        ],
        "units": {
          "misorientation_angle_deg": "degrees",
          "pre_relaxation_energy": "J/m²",
          "relaxed_energy": "J/m²"
        }
      },
      "description": "Pre-relaxation and relaxed grain-boundary energies vs misorientation angle for all 13 unseen boundaries. Used to verify the energy-versus-misorientation profile."
    }
  ],
  "notes": "The agent must implement the full pipeline from atomic configurations to SVR training and predictions. The checker will validate the JSON and CSV formats and perform structural and hidden reference checks as appropriate."
}
```

## How you are scored
A hidden verifier inspects your two output files and computes a reward value between 0 and 1.

- For `sigma13_predictions.json`: the verifier compares your `pre_relaxation_energy` and `relaxed_energy` to paper‑reported reference values (hidden from you) using appropriate tolerances. Additionally, it checks that the pre‑relaxation predicted energy is within about 10% of the relaxed energy (self‑consistency). The predicted translation coordinates are checked for physically plausible ranges but carry relatively light weight.

- For `all_unseen_energies.csv`: the verifier examines the energy‑versus‑misorientation curve. It confirms that the relaxed energies form a convex profile peaking near 45°. The same qualitative shape must be seen in the pre‑relaxation energies. Deviations from these structural requirements reduce the reward.

The final reward is a weighted sum of the individual checks. Simply writing the paper’s numbers without executing the pipeline will not satisfy the self‑consistency and structural checks, as those can only be met by genuinely training the SVR model and performing the relaxation steps.
