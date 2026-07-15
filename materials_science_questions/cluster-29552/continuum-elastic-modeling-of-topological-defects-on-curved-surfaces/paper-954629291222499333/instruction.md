# Topological Defect Analysis for Shear Transformations in Amorphous Solids

## Problem background
In amorphous solids, plasticity occurs through localized, irreversible atomic rearrangements known as shear transformations (STs). These events are characterised by quadrupolar non‑affine displacement fields that give rise to long‑range elastic deformations. A promising description interprets the centres of these transformations as topological defects in the coarse‑grained non‑affine displacement field, specifically −1 defects analogous to those in liquid crystals. Each defect can be associated with a local orientation and a proxy for its magnitude using only the atomic displacements in its immediate vicinity. The challenge is to determine whether these locally‑derived defect descriptors faithfully capture the key parameters of an Eshelby inclusion model fitted to the global displacement field, and whether they can accurately estimate the stress drops that accompany plastic events.

## Approach
Generate at least two independent two‑dimensional binary Lennard‑Jones glass samples (10 000 atoms, square box side 98.8 σ_LJ) using a slow‑quench protocol. Deform each sample under athermal quasi‑static (AQS) simple shear up to a total strain of 0.5. For each plastic event (a decrease in the global shear stress σ_xy), compute the non‑affine atomic displacements, project them onto a regular grid using a coarse‑graining function, and build a director field. Detect −1 and +1 topological defects by evaluating the winding number on local loops; locate the −1 defect centres as the centre of mass of contiguous same‑charge patches. For each −1 defect, extract a local orientation (via a phase‑shift analysis of the displacement of nearby atoms) and the average non‑affine displacement within the defect patch. Separately, fit the global displacement field of the entire event using a superposition of Eshelby inclusions (fixed core radius a = 2 σ_LJ, Poisson ratio ν = 0.46) by optimising the eigenstrain magnitude ε* and orientation φ for each defect. Compute the per‑event shear modulus from the reverted‑state stress. Using the known box volume and the defect parameters, calculate the stress drop from the global fit and from a linear mapping of the local displacement proxy to ε*. Finally, compute the pairwise correlations and a linear regression between the fitted and locally‑derived quantities, and compare the MD‑measured stress drops with the two sets of predictions.

## Reproduction target
The main output is a set of three scored artifacts:

1. `defect_analysis.csv` – a table of all detected −1 defects across all plastic events, containing the defect position, the local orientation φ_esh‑loc, the average non‑affine displacement within the defect patch, and the globally‑fitted eigenstrain ε* and orientation φ.
2. `stress_drop_predictions.csv` – one row per plastic event, listing the MD‑measured stress drop together with the stress drop predicted from the global Eshelby fit and the stress drop predicted from the local defect descriptors.
3. `summary_metrics.json` – a JSON file holding:
   - Pearson correlation between fitted orientation and local orientation (`rho_phi`),
   - slope, intercept, and R² of a linear least‑squares fit of ε* vs. the average non‑affine displacement (`slope_u_vs_eps`, `intercept_u_vs_eps`, `R2_u_vs_eps`),
   - Pearson correlation between the MD stress drop and the global‑fit prediction (`rho_stress_global`),
   - Pearson correlation between the MD stress drop and the local‑descriptor prediction (`rho_stress_local`).

All metrics are to be computed from at least two independent glass samples.

## Assets

- LAMMPS: https://lammps.sandia.gov
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Generate initial glass configurations
- Role: process
- Action: Use LAMMPS and the slow-quench protocol to create at least two independent 2D binary Lennard-Jones glass samples (square box side 98.8 σ_LJ, 10,000 atoms). Save configuration files.
- Evidence: `/app/outputs/initial_configs.log`

### Step 2: Perform AQS simple shear deformation
- Role: process
- Action: For each sample, run athermal quasi-static simple shear (δγ = 1×10⁻⁵) up to γ = 0.5 using Lees-Edwards periodic boundaries and conjugate gradient minimization. Record atomic positions before and after each plastic event, the global shear stress σ_xy, and the stress of the reverted state.
- Evidence: none

### Step 3: Compute non-affine displacements and coarse-grain
- Role: process
- Action: For each plastic event, subtract the imposed affine displacement from atomic positions to obtain non-affine displacement vectors u_i. Project these vectors onto a 100×100 regular grid using the coarse-graining function of Albaret et al. (length 1.17 σ_LJ) to build a director field.
- Evidence: `/app/outputs/coarse_grained.log`

### Step 4: Detect topological defects
- Role: process
- Action: For each grid point, compute the topological charge by evaluating the winding number on a 4×4 loop. Identify −1 and +1 defects. Define the position of each −1 defect as the centre of mass of the contiguous patch sharing the same charge.
- Evidence: `/app/outputs/defect_detection.log`

### Step 5: Extract local defect descriptors
- Role: process
- Action: For each −1 defect, compute the local orientation φ_esh-loc using the phase shift formula (atoms within 4σ_LJ of the centre) and the average atomic non-affine displacement ⟨|u_na|⟩ within the contiguous defect patch.
- Evidence: `/app/outputs/local_descriptors.log`

### Step 6: Fit Eshelby inclusion model
- Role: process
- Action: For each event, fit the global non-affine displacement field using the superposition of Eshelby inclusions with ν = 0.46 and a = 2 σ_LJ. Use conjugated direction minimisation on atoms outside all cores to extract ε* and φ for each defect. Compute the shear modulus G_i from the reverted-state stress.
- Evidence: `/app/outputs/eshelby_fit.log`

### Step 7: Write defect analysis table
- Role: scored
- Action: Compile a CSV file containing all −1 defects: event_id, sample_id, defect_x, defect_y, phi_esh_loc, u_na_avg, epsilon_star_fit, phi_fit.
- Output file: `/app/outputs/defect_analysis.csv`
- Format: csv
- Contract: columns: event_id (int), sample_id (int), defect_x (float), defect_y (float), phi_esh_loc (float), u_na_avg (float), epsilon_star_fit (float), phi_fit (float).
- Scoring: scored by hidden verifier

### Step 8: Compute stress drop predictions
- Role: process
- Action: Using the defect parameters and the stress-drop formula with box volume and per-event shear modulus G_i, compute Δσ_esh-fit from the fitted ε* and φ, and Δσ_esh-loc from the local descriptors combined with a linear mapping of u_na_avg to ε* (fit to the data).
- Evidence: `/app/outputs/stress_drop_calc.log`

### Step 9: Write stress drop predictions
- Role: scored
- Action: Compile a CSV file with rows: event_id, sample_id, Delta_sigma_MD, Delta_sigma_global_fit, Delta_sigma_local_descriptor.
- Output file: `/app/outputs/stress_drop_predictions.csv`
- Format: csv
- Contract: columns: event_id (int), sample_id (int), Delta_sigma_MD (float), Delta_sigma_global_fit (float), Delta_sigma_local_descriptor (float).
- Scoring: scored by hidden verifier

### Step 10: Compute summary metrics
- Role: scored (load-bearing)
- Action: From defect_analysis.csv, compute Pearson correlation between phi_fit and phi_esh_loc, and linear least-squares fit of epsilon_star_fit vs u_na_avg (slope, intercept, R²). From stress_drop_predictions.csv, compute Pearson correlations between Delta_sigma_MD and each of Delta_sigma_global_fit and Delta_sigma_local_descriptor. Write all metrics to summary_metrics.json.
- Output file: `/app/outputs/summary_metrics.json`
- Format: json
- Contract: JSON object with keys: rho_phi (float), slope_u_vs_eps (float), intercept_u_vs_eps (float), R2_u_vs_eps (float), rho_stress_global (float), rho_stress_local (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_analysis.csv`
- `/app/outputs/stress_drop_predictions.csv`
- `/app/outputs/summary_metrics.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_analysis.csv
- path: `/app/outputs/defect_analysis.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of all detected -1 defects across plastic events and samples. Structural checks verify expected columns, multiple samples, and a minimum event count.
- schema:
  - `type`: table
  - `required_columns`: `event_id`, `sample_id`, `defect_x`, `defect_y`, `phi_esh_loc`, `u_na_avg`, `epsilon_star_fit`, `phi_fit`

### stress_drop_predictions.csv
- path: `/app/outputs/stress_drop_predictions.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Table of stress drops per plastic event. Structural checks verify expected columns, multiple samples, and a minimum event count.
- schema:
  - `type`: table
  - `required_columns`: `event_id`, `sample_id`, `Delta_sigma_MD`, `Delta_sigma_global_fit`, `Delta_sigma_local_descriptor`

### summary_metrics.json
- path: `/app/outputs/summary_metrics.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Headline metrics comparing locally derived vs. fitted quantities: correlation of orientation, linear fit of eigenstrain vs. local displacement, and stress drop prediction correlations. Metrics compared to hidden paper reference with appropriate tolerances (threshold-or-better for correlations and R², relative tolerance for slope).
- schema:
  - `type`: object
  - `required`:
    - `rho_phi`: float
    - `slope_u_vs_eps`: float
    - `intercept_u_vs_eps`: float
    - `R2_u_vs_eps`: float
    - `rho_stress_global`: float
    - `rho_stress_local`: float

Notes: The structural audits on the CSV files have low weight. The main score comes from summary_metrics.json, where most metrics are directional (threshold_or_better) and slope is checked with a relative tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_analysis.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "event_id",
          "sample_id",
          "defect_x",
          "defect_y",
          "phi_esh_loc",
          "u_na_avg",
          "epsilon_star_fit",
          "phi_fit"
        ]
      },
      "description": "Table of all detected -1 defects across plastic events and samples. Structural checks verify expected columns, multiple samples, and a minimum event count."
    },
    {
      "file": "stress_drop_predictions.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "event_id",
          "sample_id",
          "Delta_sigma_MD",
          "Delta_sigma_global_fit",
          "Delta_sigma_local_descriptor"
        ]
      },
      "description": "Table of stress drops per plastic event. Structural checks verify expected columns, multiple samples, and a minimum event count."
    },
    {
      "file": "summary_metrics.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "rho_phi": "float",
          "slope_u_vs_eps": "float",
          "intercept_u_vs_eps": "float",
          "R2_u_vs_eps": "float",
          "rho_stress_global": "float",
          "rho_stress_local": "float"
        }
      },
      "description": "Headline metrics comparing locally derived vs. fitted quantities: correlation of orientation, linear fit of eigenstrain vs. local displacement, and stress drop prediction correlations. Metrics compared to hidden paper reference with appropriate tolerances (threshold-or-better for correlations and R², relative tolerance for slope)."
    }
  ],
  "notes": "The structural audits on the CSV files have low weight. The main score comes from summary_metrics.json, where most metrics are directional (threshold_or_better) and slope is checked with a relative tolerance."
}
```

## How you are scored
A hidden verifier scores each workflow stage’s artifact independently and combines the scores into a final reward. The primary weight rests on `summary_metrics.json`, where each headline metric is compared to a reference derived from the published results. Directional metrics (Pearson correlations and R²) are scored using a threshold‑or‑better policy: meeting or exceeding a hidden lower bound earns full credit. The slope of the linear fit is checked against a relative tolerance. The CSV files undergo low‑weight structural audits that verify the presence of the required columns, at least two distinct sample identifiers, and a minimum number of events. No single self‑reported number is sufficient; the agent must execute the full pipeline and produce all three output files. The hidden reference values and tolerances are not disclosed in these instructions.
