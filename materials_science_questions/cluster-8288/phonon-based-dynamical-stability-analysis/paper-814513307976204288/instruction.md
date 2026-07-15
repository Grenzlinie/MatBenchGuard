# Phonon stability and anisotropic properties of phagraphene via molecular dynamics

## Problem background
Phagraphene is a theoretically proposed two-dimensional carbon allotrope composed of an arrangement of pentagonal, heptagonal, and hexagonal carbon rings, forming a 20-atom rectangular unit cell with space-inversion symmetry. Its electronic properties have attracted interest, but its thermal transport and mechanical behavior remain unexplored. In this task we aim to compute the in-plane anisotropic thermal conductivity, effective phonon mean free path, elastic modulus, tensile strength, and dynamical stability of phagraphene through classical molecular dynamics simulations, determining whether the material is dynamically stable under an empirical potential and quantifying how thermal and mechanical properties differ along the armchair and zigzag directions.

## Approach
The interatomic forces are described by an optimized Tersoff empirical potential developed for graphene and carbon nanotubes. Dynamical stability of the phagraphene structure is assessed by computing the phonon dispersion with lattice dynamics; the absence of imaginary-frequency modes confirms stability. Thermal conductivity is obtained via non-equilibrium molecular dynamics (NEMD) simulations along armchair and zigzag directions, using nanoribbon supercells of increasing length. A temperature gradient is imposed, steady-state heat flux and temperature profiles are measured, and the length-dependent conductivity \(\kappa(L)\) is calculated. The intrinsic thermal conductivity \(\kappa_\infty\) and effective phonon mean free path \(\Lambda_\text{eff}\) are then extracted by fitting \(1/\kappa(L) = (1/\kappa_\infty)(1+\Lambda_\text{eff}/L)\). Mechanical properties are investigated via uniaxial tensile loading: periodic supercells are equilibrated at room temperature and zero pressure, then deformed at a constant engineering strain rate along each direction. For these tensile simulations, the Tersoff potential’s cutoff is increased from its default to 0.20 nm to obtain a physical stress-strain response. Stress-strain curves are recorded, from which the elastic modulus (initial linear slope) and tensile strength (maximum stress) are derived.

## Reproduction target
The objective is to execute the following computational pipeline and produce the specified artifacts:
- Construct the 20-atom rectangular unit cell of phagraphene and compute its phonon dispersion along the high-symmetry path Γ→X→Z→Y→Γ using GULP with the optimized Tersoff potential. Confirm that no phonon mode has a negative (imaginary) frequency.
- Run NEMD simulations with LAMMPS for at least four different sample lengths along both the armchair and zigzag directions. Collect the size-dependent thermal conductivity \(\kappa(L)\) and fit the data to \(1/\kappa(L) = (1/\kappa_\infty)(1+\Lambda_\text{eff}/L)\) to obtain the intrinsic thermal conductivity \(\kappa_\infty\) and effective phonon mean free path \(\Lambda_\text{eff}\) for each direction.
- Perform uniaxial tensile deformation simulations along both armchair and zigzag directions using the cutoff-modified Tersoff potential (cutoff 0.20 nm) to produce stress-strain curves. Compute the elastic modulus from the initial linear region and the tensile strength as the peak stress.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- GULP lattice dynamics code: https://gulp.curtin.edu.au/
- Optimized Tersoff potential parameters for graphene and carbon nanotubes: 10.1103/PhysRevB.81.205441
- Phagraphene 20-atom rectangular unit cell structure

## Workflow steps

### Step 1: Compute phonon dispersion
- Role: scored (load-bearing)
- Action: Construct the 20-atom rectangular unit cell of phagraphene. Using GULP with the optimized Tersoff potential, compute the phonon dispersion along the high-symmetry path Γ→X→Z→Y→Γ. Save the frequencies for all branches at each k-point.
- Output file: `/app/outputs/phonon_dispersion.csv`
- Format: csv
- Contract: CSV with columns: k_path_point (string), branch (int), frequency_THz (float). Header: k_path_point,branch,frequency_THz.
- Scoring: scored by hidden verifier

### Step 2: Assess dynamical stability
- Role: scored
- Action: Read phonon_dispersion.csv. Determine whether any frequency is less than -1e-3 THz (imaginary mode). Write a summary with boolean negative_frequencies and min/max frequency.
- Output file: `/app/outputs/dynamical_stability.json`
- Format: json
- Contract: JSON object with keys: negative_frequencies (bool), min_frequency_THz (float), max_frequency_THz (float).
- Scoring: scored by hidden verifier

### Step 3: Run NEMD simulations for thermal conductivity
- Role: scored (load-bearing)
- Action: Build phagraphene nanoribbon supercells of several lengths (at least 4 lengths) along armchair and zigzag directions. For each direction and length, run NEMD with LAMMPS using the optimized Tersoff potential (without cutoff modification). Equilibrate at 300 K, impose temperature gradient (hot 310 K, cold 290 K), reach steady state, compute thermal conductivity. Save length-dependent conductivities.
- Output file: `/app/outputs/thermal_conductivity.csv`
- Format: csv
- Contract: CSV with columns: length_nm (float), direction (string), kappa_WmK (float). Header: length_nm,direction,kappa_WmK.
- Scoring: scored by hidden verifier

### Step 4: Fit intrinsic thermal conductivity and MFP
- Role: scored
- Action: From thermal_conductivity.csv, for each direction, fit 1/kappa = (1/kappa_inf)*(1 + mfp/length) to extract intrinsic thermal conductivity and effective phonon mean free path. Save fitted parameters.
- Output file: `/app/outputs/thermal_fit.json`
- Format: json
- Contract: JSON object with keys 'armchair' and 'zigzag', each a dict with 'kappa_intrinsic_WmK' (float) and 'mfp_nm' (float).
- Scoring: scored by hidden verifier

### Step 5: Run uniaxial tensile simulations
- Role: scored (load-bearing)
- Action: Prepare phagraphene supercells with periodic in-plane boundaries. Use cutoff-modified Tersoff potential (cutoff increased from 0.18 to 0.20 nm). Equilibrate at 300 K and zero pressure. Perform uniaxial tensile deformation at constant strain rate along armchair and zigzag directions. Record stress-strain curves.
- Output file: `/app/outputs/stress_strain_data.csv`
- Format: csv
- Contract: CSV with columns: strain (float), stress_GPa (float), direction (string). Header: strain,stress_GPa,direction.
- Scoring: scored by hidden verifier

### Step 6: Extract elastic modulus and tensile strength
- Role: scored
- Action: From stress_strain_data.csv, compute elastic modulus from initial linear region (strain up to ~0.02) and tensile strength as maximum stress. Save properties.
- Output file: `/app/outputs/mechanical_properties.json`
- Format: json
- Contract: JSON object with keys 'armchair' and 'zigzag', each with 'elastic_modulus_GPa' (float) and 'tensile_strength_GPa' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_dispersion.csv`
- `/app/outputs/dynamical_stability.json`
- `/app/outputs/thermal_conductivity.csv`
- `/app/outputs/thermal_fit.json`
- `/app/outputs/stress_strain_data.csv`
- `/app/outputs/mechanical_properties.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_dispersion.csv
- path: `/app/outputs/phonon_dispersion.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Phonon dispersion frequencies along the high-symmetry path. Checked for absence of significant imaginary modes.
- schema:
  - `type`: table
  - `required_columns`: `k_path_point`, `branch`, `frequency_THz`

### dynamical_stability.json
- path: `/app/outputs/dynamical_stability.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Stability verdict derived from phonon dispersion; must be consistent with the CSV.
- schema:
  - `type`: object
  - `required`:
    - `negative_frequencies`: boolean
    - `min_frequency_THz`: number
    - `max_frequency_THz`: number

### thermal_conductivity.csv
- path: `/app/outputs/thermal_conductivity.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Length-dependent thermal conductivity data from NEMD; used to extrapolate intrinsic conductivity.
- schema:
  - `type`: table
  - `required_columns`: `length_nm`, `direction`, `kappa_WmK`

### thermal_fit.json
- path: `/app/outputs/thermal_fit.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted intrinsic thermal conductivity and effective phonon mean free path for armchair and zigzag directions.
- schema:
  - `type`: object
  - `required`:
    - `armchair`: object
    - `zigzag`: object
  - `items`:
    - `kappa_intrinsic_WmK`: number
    - `mfp_nm`: number

### stress_strain_data.csv
- path: `/app/outputs/stress_strain_data.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Stress-strain curves from uniaxial tensile MD simulations.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_GPa`, `direction`

### mechanical_properties.json
- path: `/app/outputs/mechanical_properties.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Extracted elastic modulus and tensile strength for armchair and zigzag directions.
- schema:
  - `type`: object
  - `required`:
    - `armchair`: object
    - `zigzag`: object
  - `items`:
    - `elastic_modulus_GPa`: number
    - `tensile_strength_GPa`: number

Notes: The task reproduces the paper's computational pipeline for dynamical stability, size-dependent thermal conductivity, and mechanical properties of phagraphene using public tools (LAMMPS, GULP) and the publicly known Lindsay-Broido Tersoff potential. The cutoff modification for tensile tests is a simple parameter change (0.18 -> 0.20 nm) described in the method; the agent applies it directly, no separate validation step. All scored artifacts are re-derivable from raw simulation outputs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_dispersion.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "k_path_point",
          "branch",
          "frequency_THz"
        ]
      },
      "description": "Phonon dispersion frequencies along the high-symmetry path. Checked for absence of significant imaginary modes."
    },
    {
      "file": "dynamical_stability.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "negative_frequencies": "boolean",
          "min_frequency_THz": "number",
          "max_frequency_THz": "number"
        }
      },
      "description": "Stability verdict derived from phonon dispersion; must be consistent with the CSV."
    },
    {
      "file": "thermal_conductivity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "length_nm",
          "direction",
          "kappa_WmK"
        ]
      },
      "description": "Length-dependent thermal conductivity data from NEMD; used to extrapolate intrinsic conductivity."
    },
    {
      "file": "thermal_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "armchair": "object",
          "zigzag": "object"
        },
        "items": {
          "kappa_intrinsic_WmK": "number",
          "mfp_nm": "number"
        }
      },
      "description": "Fitted intrinsic thermal conductivity and effective phonon mean free path for armchair and zigzag directions."
    },
    {
      "file": "stress_strain_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_GPa",
          "direction"
        ]
      },
      "description": "Stress-strain curves from uniaxial tensile MD simulations."
    },
    {
      "file": "mechanical_properties.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "armchair": "object",
          "zigzag": "object"
        },
        "items": {
          "elastic_modulus_GPa": "number",
          "tensile_strength_GPa": "number"
        }
      },
      "description": "Extracted elastic modulus and tensile strength for armchair and zigzag directions."
    }
  ],
  "notes": "The task reproduces the paper's computational pipeline for dynamical stability, size-dependent thermal conductivity, and mechanical properties of phagraphene using public tools (LAMMPS, GULP) and the publicly known Lindsay-Broido Tersoff potential. The cutoff modification for tensile tests is a simple parameter change (0.18 -> 0.20 nm) described in the method; the agent applies it directly, no separate validation step. All scored artifacts are re-derivable from raw simulation outputs."
}
```

## How you are scored
A hidden verifier will independently score each workflow stage's output and combine the results by weight into a final reward between 0 and 1.

- **Phonon stability**: the verifier checks that `phonon_dispersion.csv` contains no frequency more negative than −0.01 THz (no significant imaginary modes) and that the maximum frequency is plausible. The `dynamical_stability.json` verdict must be consistent with the dispersion data.
- **Thermal conductivity**: the verifier reads `thermal_conductivity.csv`, refits the \(1/\kappa(L)\) model separately for armchair and zigzag directions, and compares the refitted \(\kappa_\infty\) and \(\Lambda_\text{eff}\) to hidden reference values. Credit is based on how close the refitted quantities are to the references (better-than-reference is never penalized).
- **Mechanical properties**: the verifier reads `stress_strain_data.csv`, recomputes the elastic modulus and tensile strength for each direction, and compares them to hidden reference thresholds. Again, meeting or exceeding the reference yields full credit.

Consistency between the agent’s reported fit results (`thermal_fit.json`, `mechanical_properties.json`) and the verifier’s own recomputation from the raw data is also checked; discrepancies reduce the score. Simply reporting the reference values without producing valid underlying simulation artifacts will not earn the reward.
