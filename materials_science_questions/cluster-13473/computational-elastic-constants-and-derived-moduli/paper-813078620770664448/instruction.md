# Nanoindentation stress analysis of a virus capsid using coarse-grained molecular dynamics

## Problem background
Understanding mechanical failure in virus capsids requires continuum stress measures—Cauchy stress, stress invariants, von Mises shear stress, and Tresca stress—that are not directly accessible from discrete molecular dynamics simulations. This task implements a computational methodology that derives these stress fields from coarse-grained (CG) Langevin dynamics trajectories and applies it to a viral capsid under nanoindentation. The goal is to quantify how mechanical stress propagates and redistributes during compressive deformation, and to identify conditions that predict structural collapse.

## Approach
The virus capsid is represented by a Cα‑based self‑organized polymer (SOP) coarse‑grained model: each residue is a single bead, backbone connectivity is described by a FENE potential, native contacts by attractive Lennard‑Jones interactions, and non‑native contacts by repulsive Lennard‑Jones terms. Dynamics are simulated with overdamped Langevin equations. Nanoindentation is performed by pressing a spherical cantilever tip onto the capsid along a two‑fold symmetry axis, with the capsid resting on a weakly adsorbing substrate. Simulations are run at two temperatures (300 K and 0 K) to probe the role of thermal fluctuations. From the resulting trajectories, a local atomic stress tensor is computed for each residue using the TensorCalculator software; it sums pairwise force contributions within a cut‑off volume. Scalar stress measures—first invariant and von Mises stress—are then derived per frame, spatially averaged over defined top and side capsid portions, and analysed as functions of the imposed deformation. The force–deformation curve is extracted separately from the cantilever force log. Critical quantities (collapse force and deformation, and the deformation where top and side von Mises stresses cross) are determined from these curves.

## Reproduction target
Produce the following from a full nanoindentation pipeline of the CCMV capsid built from PDB entry 1CWP:

- Force–deformation curves for nanoindentation along the two‑fold axis at T = 300 K and T = 0 K (CSV files).
- Stress profiles (first stress invariant I₁ and von Mises stress) for the top and side portions of the capsid as a function of deformation at T = 300 K (CSV file). Top and side portions are defined as the top 30 % and side remaining region relative to the indentation axis.
- A JSON file containing the critical force (maximum force before collapse) and the corresponding deformation at collapse for both temperatures, plus the deformation at which the von Mises stress of the top portion equals that of the side portion (crossing point) extracted from the T = 300 K stress profile.

## Assets

- CCMV capsid structure (PDB 1CWP): https://www.rcsb.org/structure/1CWP
- SOP-GPU software: https://github.com/BarsegovGroup/SOP-GPU.git
- TensorCalculator software: https://github.com/BarsegovGroup/TensorCalculator.git

## Workflow steps

### Step 1: Build coarse-grained SOP model
- Role: process
- Action: Build the SOP coarse-grained model of the empty CCMV capsid from PDB structure 1CWP using the SOP-GPU tool. Generate the necessary structure file and GROMACS topology file based on native contacts identified within an 8 Å cutoff.
- Evidence: `/app/outputs/ccmv_sop_model.pdb`

### Step 2: Run nanoindentation simulation at T=300 K
- Role: process
- Action: Run a Langevin dynamics nanoindentation of the CCMV capsid along the two-fold symmetry axis at T=300 K using SOP-GPU. Cantilever tip radius 20 nm, base velocity 1 μm/s, spring constant 50 pN/nm, surface adsorption ε_surf=0.2 kcal/mol, tip interaction ε_tip=1.0 kcal/mol, σ_tip=1.0 Å. Continue until capsid collapse (approximately 9.5 nm deformation). Record the trajectory and force-displacement log.
- Evidence: `/app/outputs/trajectory_300K.dcd`

### Step 3: Run nanoindentation simulation at T=0 K
- Role: process
- Action: Run the same nanoindentation simulation as in step_sim_300k but at T=0 K. Record the trajectory and force-displacement log.
- Evidence: `/app/outputs/trajectory_0K.dcd`

### Step 4: Compute atomic stress tensors for T=300 K trajectory
- Role: process
- Action: Using TensorCalculator in Mode 1 with the T=300 K trajectory and the structure and topology files from step_build_model, compute per-residue atomic stress tensor components for every frame and output a TNSR file.
- Evidence: `/app/outputs/stress_300K.tnsr`

### Step 5: Compute stress profiles for T=300 K
- Role: scored (load-bearing)
- Action: From the TNSR file, compute the first stress invariant and von Mises stress for each residue, average over top and side portions (30% of capsid diameter from top/bottom along indentation axis) per frame, and write a CSV with deformation and averaged stress components.
- Output file: `/app/outputs/stress_profiles_300K.csv`
- Format: csv
- Contract: Columns: deformation_nm, I1_top_MPa, I1_side_MPa, vM_top_MPa, vM_side_MPa.
- Scoring: scored by hidden verifier

### Step 6: Output force-deformation curve for T=300 K
- Role: scored (load-bearing)
- Action: Extract force versus deformation from the T=300 K simulation output log and write a CSV.
- Output file: `/app/outputs/force_deformation_300K.csv`
- Format: csv
- Contract: Columns: deformation_nm, force_nN.
- Scoring: scored by hidden verifier

### Step 7: Output force-deformation curve for T=0 K
- Role: scored (load-bearing)
- Action: Extract force versus deformation from the T=0 K simulation output log and write a CSV.
- Output file: `/app/outputs/force_deformation_0K.csv`
- Format: csv
- Contract: Columns: deformation_nm, force_nN.
- Scoring: scored by hidden verifier

### Step 8: Compile critical values
- Role: scored (load-bearing)
- Action: From the force-deformation curves and the stress profile, determine the critical force and deformation at collapse (maximum force) for both temperatures, and the deformation where von Mises stress of top and side portions become equal (crossing point) from the T=300 K stress profile. Write these values as a JSON file.
- Output file: `/app/outputs/results.json`
- Format: json
- Contract: JSON object with keys: critical_force_300K_nN, critical_deformation_300K_nm, crossing_deformation_vM_300K_nm, critical_force_0K_nN, critical_deformation_0K_nm.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_profiles_300K.csv`
- `/app/outputs/force_deformation_300K.csv`
- `/app/outputs/force_deformation_0K.csv`
- `/app/outputs/results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_profiles_300K.csv
- path: `/app/outputs/stress_profiles_300K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress invariant and von Mises stress profiles for top and side capsid portions at T=300 K, as functions of deformation. The checker will recompute the crossing deformation and verify trend shapes.
- schema:
  - `type`: table
  - `required_columns`: `deformation_nm`, `I1_top_MPa`, `I1_side_MPa`, `vM_top_MPa`, `vM_side_MPa`
  - `units`:
    - `deformation_nm`: nm
    - `I1_top_MPa`: MPa
    - `I1_side_MPa`: MPa
    - `vM_top_MPa`: MPa
    - `vM_side_MPa`: MPa

### force_deformation_300K.csv
- path: `/app/outputs/force_deformation_300K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Force-deformation curve from the T=300 K nanoindentation simulation. The checker will recompute the maximum force and the corresponding deformation.
- schema:
  - `type`: table
  - `required_columns`: `deformation_nm`, `force_nN`
  - `units`:
    - `deformation_nm`: nm
    - `force_nN`: nN

### force_deformation_0K.csv
- path: `/app/outputs/force_deformation_0K.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Force-deformation curve from the T=0 K nanoindentation simulation. The checker will recompute the maximum force and the corresponding deformation.
- schema:
  - `type`: table
  - `required_columns`: `deformation_nm`, `force_nN`
  - `units`:
    - `deformation_nm`: nm
    - `force_nN`: nN

### results.json
- path: `/app/outputs/results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Compiled critical quantities: collapse forces and deformations at both temperatures, and the crossing deformation for von Mises stress.
- schema:
  - `type`: object
  - `required`:
    - `critical_force_300K_nN`: float
    - `critical_deformation_300K_nm`: float
    - `crossing_deformation_vM_300K_nm`: float
    - `critical_force_0K_nN`: float
    - `critical_deformation_0K_nm`: float

Notes: The force-deformation curves are extracted directly from the simulation output. Stress profiles are derived from TensorCalculator output. The checker will verify that the stress profiles show the expected trend (I1_top decreasing, I1_side slightly increasing) and that the crossing deformation is within tolerance. Critical forces and deformations are compared to paper-reported values.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_profiles_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "deformation_nm",
          "I1_top_MPa",
          "I1_side_MPa",
          "vM_top_MPa",
          "vM_side_MPa"
        ],
        "units": {
          "deformation_nm": "nm",
          "I1_top_MPa": "MPa",
          "I1_side_MPa": "MPa",
          "vM_top_MPa": "MPa",
          "vM_side_MPa": "MPa"
        }
      },
      "description": "Stress invariant and von Mises stress profiles for top and side capsid portions at T=300 K, as functions of deformation. The checker will recompute the crossing deformation and verify trend shapes."
    },
    {
      "file": "force_deformation_300K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "deformation_nm",
          "force_nN"
        ],
        "units": {
          "deformation_nm": "nm",
          "force_nN": "nN"
        }
      },
      "description": "Force-deformation curve from the T=300 K nanoindentation simulation. The checker will recompute the maximum force and the corresponding deformation."
    },
    {
      "file": "force_deformation_0K.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "deformation_nm",
          "force_nN"
        ],
        "units": {
          "deformation_nm": "nm",
          "force_nN": "nN"
        }
      },
      "description": "Force-deformation curve from the T=0 K nanoindentation simulation. The checker will recompute the maximum force and the corresponding deformation."
    },
    {
      "file": "results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "critical_force_300K_nN": "float",
          "critical_deformation_300K_nm": "float",
          "crossing_deformation_vM_300K_nm": "float",
          "critical_force_0K_nN": "float",
          "critical_deformation_0K_nm": "float"
        }
      },
      "description": "Compiled critical quantities: collapse forces and deformations at both temperatures, and the crossing deformation for von Mises stress."
    }
  ],
  "notes": "The force-deformation curves are extracted directly from the simulation output. Stress profiles are derived from TensorCalculator output. The checker will verify that the stress profiles show the expected trend (I1_top decreasing, I1_side slightly increasing) and that the crossing deformation is within tolerance. Critical forces and deformations are compared to paper-reported values."
}
```

## How you are scored
An automated verifier will read your submitted CSV and JSON files. It will recompute key quantities from your raw data: the crossing deformation by interpolating where vM_top equals vM_side in stress_profiles_300K.csv, and the collapse forces and deformations by locating the maximum force in each force–deformation CSV. These recomputed values are compared against hidden reference thresholds using appropriate tolerances. In addition, the verifier will check that the stress profiles are physically self-consistent (e.g., monotonic trends in the stress measures). Each scored artifact contributes a weighted fraction of the total reward (0–1). Success requires faithfully executing the entire pipeline described in the workflow steps; guessing or fabricating numbers will not pass the verifier’s checks.
