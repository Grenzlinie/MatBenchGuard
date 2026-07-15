# Ion Hydration Compton Profile Analysis via DFT Model Clusters

## Problem background
Ion hydration is central to chemistry, biophysics, and environmental science, yet the local arrangement of water molecules around dissolved ions remains debated. X-ray Compton scattering probes the ground-state electron momentum density and, through the bond oscillation principle, is sensitive to bond-length distributions, coordination numbers, and ion pairing. In this study, synchrotron measurements are combined with density functional theory (DFT) model cluster calculations to investigate how Compton profile signatures reflect ion–oxygen distances, hydration number, and ion-pair configurations. The present task focuses on the computational component: using DFT to simulate bond-induced Compton profile differences J_bond(q) for model ion–water and ion–ion clusters, and uncovering how these profiles vary with the local geometry.

## Approach
The computational approach employs Kohn–Sham (KS) DFT to compute the isotropic Compton profile J(q) for each cluster. The isotropic Compton profile is obtained from the spherically averaged electron momentum density, which is built as the squared Fourier transform of the occupied KS orbitals (the impulse approximation). To isolate the bonding-induced changes, reference profiles are calculated for free ions (Li⁺, Cl⁻) and an isolated water monomer. For every model cluster the bond-induced difference J_bond(q) = J(q) – J_ref(q) is formed. The model systems span three classes: (i) pairwise ion–water and ion–ion dimers at several distances; (ii) first hydration shells of Cl⁻ and Li⁺ with coordination numbers n and two different short ion–oxygen distances (a ‘short’ and a ‘long’ model) plus water molecules at a large fixed distance; (iii) larger Li⁺Cl⁻(H₂O)ₙ clusters (n = 8–10) representing solvent-separated and contact ion pairs with different ion–oxygen and ion–ion distances. All calculations use gradient-corrected exchange-correlation functionals (Hammer–Hansen–Norskov / Perdew–Burke–Ernzerhof) and contracted Gaussian basis sets of triple-zeta (O,Cl), double-zeta (Li), and [3s,1p] (H) quality. The geometry generation, DFT runs, and profile differencing form an ordered pipeline that produces the final J_bond(q) curves.

## Reproduction target
Reproduce the DFT-based bond-induced Compton profile differences J_bond(q) for all model clusters described in the workflow steps. Output the results as a single CSV file with columns `model`, `q`, `J_bond`, covering the momentum range from -5 to +5 a.u. with a spacing of at most 0.1 a.u. The CSV must include all pairwise, hydration-shell, and ion-pair models listed in Step 4, as well as the reference profiles for free Li⁺, Cl⁻, and the H₂O monomer. The file must follow the naming convention and schema given in the output contract.

## Assets

- STOBE-DEMON DFT code: https://github.com/StoBE-deMon/StoBE-deMon
- Gaussian basis sets for O, Cl, Li, H: included with STOBE-DEMON or obtainable from EMSL Basis Set Exchange

## Workflow steps

### Step 1: Generate cluster geometries
- Role: process
- Action: Create atomic coordinate files for all model clusters required for the sensitivity demonstration. Use the water monomer geometry (O-H 0.970 Å, H-O-H 106.06°), the symmetry constraints (O_h for Cl⁻ hydration, T_d for Li⁺ hydration), and the distances specified below. Build the following classes of clusters: (a) pairwise Li⁺–H₂O at 2.0 Å and 2.5 Å, Cl⁻–H₂O at 3.0 Å and 4.0 Å, Li⁺–Cl⁻ at 2.0, 2.5, and 3.0 Å; (b) Cl⁻(H₂O)ₙ hydration shells with n=0..6 for model 1A (R_OCl^short=3.0 Å) and model 1B (R_OCl^short=4.0 Å), with the far oxygen at 8.0 Å; (c) Li⁺(H₂O)ₙ hydration shells with n=0..4 for model 2A (R_OLi^short=2.0 Å) and model 2B (R_OLi^short=2.5 Å), far oxygen at 8.0 Å; (d) Li⁺Cl⁻(H₂O)ₙ ion-pair clusters (n=8,9,10) for the three models 3A, 3B, 3C (see Table II for distances), with O-O distance 3.0 Å. This process step produces the geometry inputs needed for all subsequent DFT calculations.
- Evidence: `/app/outputs/geom_log.txt`

### Step 2: Compute reference Compton profiles
- Role: process
- Action: Perform DFT calculations with STOBE-DEMON for isolated Li⁺, Cl⁻, and H₂O monomer using the gradient-corrected exchange-correlation functional (Hammer-Hansen-Norskov/Perdew-Burke-Ernzerhof) and the prescribed basis sets. From each calculation, compute the isotropic Compton profile J_ref(q) via the spherically averaged projection of the ground-state electron momentum density (obtained as sum of squared Fourier transforms of Kohn-Sham orbitals). Save the profiles as plain text files.
- Evidence: `/app/outputs/ref_profiles_log.txt`

### Step 3: Compute Compton profiles for all model clusters
- Role: process
- Action: Run STOBE-DEMON DFT calculations for every model cluster defined in step_geom, using the same functional and basis sets as step_ref. For each cluster, extract the isotropic Compton profile J(q).
- Evidence: `/app/outputs/cluster_profiles_log.txt`

### Step 4: Bond-induced Compton profile differences
- Role: scored (load-bearing)
- Action: For each model cluster, compute the bond-induced Compton profile difference J_bond(q) = J(q) - J_ref(q) using the appropriate reference (free ions and water monomers). Combine all curves into a single CSV file with columns: model, q, J_bond. Include also the pure reference profiles for free Li⁺, Cl⁻, and H₂O monomer labeled as 'ref_Li', 'ref_Cl', 'ref_H₂O'. Model names must follow the naming convention: 'pair_' for pairwise interactions (e.g., 'pair_Li_H2O_d2.0'), 'Cl_shell_<model>_n<N>' for chloride hydration shells, 'Li_shell_<model>_n<N>' for lithium hydration shells, and 'LiCl_<model>_n<N>' for ion-pair clusters. Cover q from -5 to +5 a.u. with spacing ≤0.1 a.u. Use atomic units (a.u.) for q and J_bond.
- Output file: `/app/outputs/j_bond_all_models.csv`
- Format: csv
- Contract: Columns: model (string), q (float, a.u.), J_bond (float, a.u.). One row per (model, q) point. Model names: 'pair_*' (pairwise), 'Cl_shell_1A_n0'..'Cl_shell_1A_n6', 'Cl_shell_1B_n0'..'n6', 'Li_shell_2A_n0'..'n4', 'Li_shell_2B_n0'..'n4', 'LiCl_3A_n8','LiCl_3A_n9','LiCl_3A_n10', 'LiCl_3B_n8','LiCl_3B_n9','LiCl_3B_n10', 'LiCl_3C_n8','LiCl_3C_n9','LiCl_3C_n10', 'ref_Li', 'ref_Cl', 'ref_H2O'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/j_bond_all_models.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### j_bond_all_models.csv
- path: `/app/outputs/j_bond_all_models.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Bond-induced Compton profile difference J_bond(q) for all model clusters and reference fragments. The checker will recompute derived features (sign at q=0, extremum positions, linear scaling with hydration number, SSIP-to-CIP distinction) and compare against hidden gold values extracted from the paper's reported trends.
- schema:
  - `type`: table
  - `required_columns`: `model`, `q`, `J_bond`
  - `units`:
    - `q`: a.u.
    - `J_bond`: a.u.

Notes: The CSV columns 'model', 'q', and 'J_bond' must be present. The q range should be -5 to +5 a.u. with spacing ≤0.1 a.u. Model naming must follow the convention given in the step description. Failed calculations may be reported as NaN for J_bond for that model, but the model name should still appear.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "j_bond_all_models.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "q",
          "J_bond"
        ],
        "units": {
          "q": "a.u.",
          "J_bond": "a.u."
        }
      },
      "description": "Bond-induced Compton profile difference J_bond(q) for all model clusters and reference fragments. The checker will recompute derived features (sign at q=0, extremum positions, linear scaling with hydration number, SSIP-to-CIP distinction) and compare against hidden gold values extracted from the paper's reported trends."
    }
  ],
  "notes": "The CSV columns 'model', 'q', and 'J_bond' must be present. The q range should be -5 to +5 a.u. with spacing ≤0.1 a.u. Model naming must follow the convention given in the step description. Failed calculations may be reported as NaN for J_bond for that model, but the model name should still appear."
}
```

## How you are scored
A hidden verifier inspects your output artifacts and confirms that each required file exists and respects the prescribed format. For the scored CSV, the verifier extracts the J_bond(q) curves and evaluates whether they satisfy the geometric regularities expected from the bond oscillation principle. The checks include, for example: the sign of J_bond at q=0 for models with different ion–oxygen distances, the position and magnitude of the first extremum, the linearity of the oscillation amplitude with hydration number for chloride shells, and the distinction between solvent-separated and contact ion-pair configurations. Each check contributes a fraction of the total reward, and the final score is a weighted combination of these stage scores. The structural trends cannot be reproduced by simply guessing a number; they require the actual DFT calculations and correct geometry handling.
