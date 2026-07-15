# Quantum-Chemical Energetics of SiF4 Desorption from SiO2 Surfaces

## Problem background
The wet etching of silicon dioxide (SiO2) films in hydrogen fluoride (HF) solutions is a critical step in semiconductor manufacturing, yet the atomic-scale mechanism by which SiF4 molecules detach from the surface remains incompletely understood. Previous kinetic studies suggested that the reaction is driven by nucleophilic attack of HF2⁻ ions on surface silicon atoms and electrophilic attack of H⁺ ions on oxygen atoms, but quantum-chemical evidence for a complete desorption pathway was lacking. The target of this reproduction is to compute the energetic and structural changes during SiF4 desorption from a model SiO2 surface using molecular orbital theory, and thereby to quantify the activation barrier and dissociative steps that characterise the process.

## Approach
The core method is the extended Hückel molecular orbital (EHMO) approximation, a semi-empirical quantum-chemical technique that captures covalent bonding trends with low computational cost. The approach constructs a finite cluster model (HO)₃Si–O–SiF₃ to represent the F-terminated SiO2 surface under attack. Using Slater-type atomic orbitals and standard Coulomb integrals for H, O, F, and Si, the Hamiltonian and overlap matrices are built and diagonalised to obtain molecular orbital energies and total electronic energy. The reaction is explored through a series of constrained geometry scans:
(i) an isolated SiF4 molecule to determine the equilibrium Si–F bond length;
(ii) a linear HF2⁻ ion to map the potential energy surface for its dissociation into F⁻ + HF and locate the saddle point;
(iii) the full (HO)₃SiOSiF₃ cluster with the attacking H⁺ ion held at infinite distance (i.e., absent), where the O–Si–F angle is relaxed at each grid point of the O–Si and Si–F⁻ distances;
(iv) the same cluster with the H⁺ ion placed at a fixed 0.92 Å from the back-bond oxygen, again with per-point angle relaxation.
From these scans, the minimum-energy desorption path, transition state, and activation energy are determined. Mulliken bond population analysis quantifies the Si–O back-bond weakening, and the evolution of the O–Si–F angle shows the surface reconstruction that accompanies desorption.

## Reproduction target
The goal is to produce, by explicit computation, six numerical artifacts that collectively describe the energetic and structural landscape of SiF4 desorption:
1. A binding energy curve for an isolated SiF4 molecule (r_Si_F vs. total_energy) that yields the equilibrium Si–F distance.
2. A two-dimensional potential energy surface for the HF2⁻ dissociation reaction (r_FH–F⁻, r_F⁻–HF, total_energy) from which the dissociation barrier and saddle-point geometry can be extracted.
3. A desorption energy surface WITHOUT H⁺ attack (r_O_Si, r_Si_F⁻, total_energy, optimized O–Si–F angle, Si–O bond population).
4. A desorption energy surface WITH H⁺ attack at r(O–H⁺) = 0.92 Å, providing the same quantities; this surface is the primary source for the desorption activation energy.
5. A summary report that collects the extracted key quantities: the equilibrium Si–F bond length, the HF2⁻ dissociation barrier and saddle-point H–F distance, the SiF4 desorption activation energy, the coordinates of the transition state, and the range of O–Si–F angles and Si–O bond populations observed during the reaction.
6. A trend table projecting the O–Si–F angle and Si–O bond population onto a reaction coordinate (rc = r_O_Si – r_Si_F⁻) for both the with‑H⁺ and without‑H⁺ cases, allowing verification of monotonic angle collapse and bond weakening.
All energies are in electron-volts, lengths in ångströms, and angles in degrees. No external datasets are required; all necessary atomic parameters and cluster geometries are provided in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement extended Hückel method and set up cluster
- Role: process
- Action: Implement the extended Hückel molecular orbital method using the given Slater-type orbital parameters and Coulomb integrals (H 1s: ξ=1.3, Hss=-13.6 eV; O 2s/2p: ξ=2.275, Hss=-32.3 eV, Hpp=-14.8 eV; F 2s/2p: ξ=2.425, Hss=-40.0 eV, Hpp=-18.1 eV; Si 3s/3p: ξ=1.383, Hss=-17.3 eV, Hpp=-9.2 eV) and Hückel constant K=1.75. Build the Hamiltonian matrix H_μν = (K/2)(H_μμ + H_νν) S_μν and the overlap matrix S_μν from Slater-type atomic orbitals. Solve the generalized eigenvalue problem H C = ε S C to obtain molecular orbitals and total electronic energy as the sum of occupied eigenvalues. Define the (HO)₃SiOSiF₃ cluster geometry with fixed bond lengths: R(Si–O)=1.601 Å, R(Si–F)=1.635 Å, R(O–H)=0.92 Å, and angles ∠O–Si–O=109.47°, ∠Si–O–Si=180.0°. This step must produce a reusable function that computes total electronic energy and atomic bond population for a given set of nuclear coordinates.
- Evidence: `/app/outputs/eht_implementation_check.txt`

### Step 2: SiF4 binding energy scan
- Role: scored
- Action: Build an isolated SiF4 molecule with tetrahedral geometry. For a range of Si-F bond lengths (covering the vicinity of the expected minimum), compute the total electronic energy using the implemented extended Hückel method. Save the scanned energies.
- Output file: `/app/outputs/sif4_binding_curve.csv`
- Format: csv
- Contract: Two columns: r_Si_F (Å, float), total_energy (eV, float). The grid should be dense enough to resolve the minimum.
- Scoring: scored by hidden verifier

### Step 3: HF2- dissociation potential energy surface
- Role: scored
- Action: Build the linear HF2- ion. Compute the total electronic energy on a two-dimensional grid of the two H-F distances r(FH–F⁻) and r(F⁻–HF), covering a range that includes the symmetric saddle region and the asymmetric dissociation valleys.
- Output file: `/app/outputs/hf2_dissociation_surface.csv`
- Format: csv
- Contract: Three columns: r_FH_Fminus (Å, float), r_Fminus_HF (Å, float), total_energy (eV, float). Grid resolution sufficient to capture the saddle point.
- Scoring: scored by hidden verifier

### Step 4: Desorption energy surface without H+ attack
- Role: scored
- Action: Construct the (HO)3SiOSiF3 cluster with the fixed geometry. With the H+ held infinitely far away, for each point on a grid of r(O-Si) from 1.601 to 2.651 Å and r(Si-F⁻) from 1.635 to 3.035 Å, relax the O-Si-F bond angle to minimize the total electronic energy. Record the final energy, optimized angle, and the Si-O Mulliken bond population.
- Output file: `/app/outputs/desorption_energy_surface_without_Hplus.csv`
- Format: csv
- Contract: Columns: r_O_Si (Å, float), r_Si_Fminus (Å, float), total_energy (eV, float), optimized_O_Si_F_angle (deg, float), Si_O_bond_population (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 5: Desorption energy surface with H+ attack
- Role: scored (load-bearing)
- Action: Repeat the same cluster setup and grid scan as in step_03_desorption_no_h, but now place the attacking hydrogen ion at a fixed distance r(O-H⁺) = 0.92 Å from the back-bond oxygen. For each grid point, relax the O-Si-F angle and compute total energy, optimized angle, and Si-O bond population.
- Output file: `/app/outputs/desorption_energy_surface_with_Hplus.csv`
- Format: csv
- Contract: Columns: r_O_Si (Å, float), r_Si_Fminus (Å, float), total_energy (eV, float), optimized_O_Si_F_angle (deg, float), Si_O_bond_population (float, dimensionless).
- Scoring: scored by hidden verifier

### Step 6: Activation energy report
- Role: scored
- Action: Analyze the raw energy surfaces produced in steps 01, 02 and 04. Extract the equilibrium Si-F distance from the binding curve, locate the saddle point on the HF2- surface and compute its barrier relative to the dissociation asymptotic energy, find the minimum-energy path on the desorption surface with H+ and identify the transition state. Compute the desorption activation energy as the energy difference between the transition state and the initial minimum. Compile these values into a structured JSON report.
- Output file: `/app/outputs/activation_energy_report.json`
- Format: json
- Contract: JSON object with keys: sif4_equilibrium_bond_length (Å, float), hf2_dissociation_barrier (eV, float), hf2_saddle_r (Å, float), siF4_desorption_activation_energy (eV, float), transition_state_r_O_Si (Å, float), transition_state_r_Si_Fminus (Å, float), angle_range (list of two floats: min and max optimized angle from step 04), bond_population_range (list of two floats: max and approximate min Si-O population from step 04).
- Scoring: scored by hidden verifier

### Step 7: Angle and bond population trend along reaction coordinate
- Role: scored
- Action: From the desorption energy surfaces (steps 03 and 04), extract the minimum-energy path. Project the optimized O-Si-F angle and the Si-O Mulliken bond population onto the variable rc = r(O-Si) - r(Si-F⁻). Output a table with the trend for both the 'with_Hplus' and 'without_Hplus' cases.
- Output file: `/app/outputs/angle_population_trend.csv`
- Format: csv
- Contract: Columns: case (string, 'with_Hplus' or 'without_Hplus'), reaction_coordinate_rc (Å, float), optimized_O_Si_F_angle (deg, float), Si_O_bond_population (float, dimensionless). Rows sorted by rc.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sif4_binding_curve.csv`
- `/app/outputs/hf2_dissociation_surface.csv`
- `/app/outputs/desorption_energy_surface_without_Hplus.csv`
- `/app/outputs/desorption_energy_surface_with_Hplus.csv`
- `/app/outputs/activation_energy_report.json`
- `/app/outputs/angle_population_trend.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sif4_binding_curve.csv
- path: `/app/outputs/sif4_binding_curve.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed total electronic energy of an isolated SiF4 molecule as a function of the Si-F bond length. The checker extracts the equilibrium bond length from this curve.
- schema:
  - `type`: table
  - `required_columns`: `r_Si_F`, `total_energy`
  - `units`:
    - `r_Si_F`: Å
    - `total_energy`: eV

### hf2_dissociation_surface.csv
- path: `/app/outputs/hf2_dissociation_surface.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Potential energy surface for HF2- dissociation. The checker locates the saddle point and computes the dissociation barrier.
- schema:
  - `type`: table
  - `required_columns`: `r_FH_Fminus`, `r_Fminus_HF`, `total_energy`
  - `units`:
    - `r_FH_Fminus`: Å
    - `r_Fminus_HF`: Å
    - `total_energy`: eV

### desorption_energy_surface_without_Hplus.csv
- path: `/app/outputs/desorption_energy_surface_without_Hplus.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Desorption energy surface computed without hydrogen attack. Used for reference and trend comparisons.
- schema:
  - `type`: table
  - `required_columns`: `r_O_Si`, `r_Si_Fminus`, `total_energy`, `optimized_O_Si_F_angle`, `Si_O_bond_population`
  - `units`:
    - `r_O_Si`: Å
    - `r_Si_Fminus`: Å
    - `total_energy`: eV
    - `optimized_O_Si_F_angle`: deg
    - `Si_O_bond_population`: dimensionless

### desorption_energy_surface_with_Hplus.csv
- path: `/app/outputs/desorption_energy_surface_with_Hplus.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Desorption energy surface computed with explicit H+ attack. The checker extracts the transition state and activation energy from this surface. Load-bearing: cannot be fabricated without running the core calculation.
- schema:
  - `type`: table
  - `required_columns`: `r_O_Si`, `r_Si_Fminus`, `total_energy`, `optimized_O_Si_F_angle`, `Si_O_bond_population`
  - `units`:
    - `r_O_Si`: Å
    - `r_Si_Fminus`: Å
    - `total_energy`: eV
    - `optimized_O_Si_F_angle`: deg
    - `Si_O_bond_population`: dimensionless

### activation_energy_report.json
- path: `/app/outputs/activation_energy_report.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Summary report containing the extracted key quantities. Checked against hidden reference values with tolerances.
- schema:
  - `type`: object
  - `required`:
    - `sif4_equilibrium_bond_length`: float (Å)
    - `hf2_dissociation_barrier`: float (eV)
    - `hf2_saddle_r`: float (Å)
    - `siF4_desorption_activation_energy`: float (eV)
    - `transition_state_r_O_Si`: float (Å)
    - `transition_state_r_Si_Fminus`: float (Å)
    - `angle_range`: list of two floats (min, max) in deg
    - `bond_population_range`: list of two floats (max, min) dimensionless

### angle_population_trend.csv
- path: `/app/outputs/angle_population_trend.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Trend of O-Si-F angle and Si-O bond population along the minimum-energy desorption path, for both H+ conditions. Checker verifies monotonic decrease in angle and population, with steeper collapse for the with_Hplus case.
- schema:
  - `type`: table
  - `required_columns`: `case`, `reaction_coordinate_rc`, `optimized_O_Si_F_angle`, `Si_O_bond_population`
  - `units`:
    - `reaction_coordinate_rc`: Å
    - `optimized_O_Si_F_angle`: deg
    - `Si_O_bond_population`: dimensionless

Notes: All energies are in eV, lengths in Å, angles in degrees. The desorption surface with H+ is the principal scored artifact; its activation energy must be derived from the computed grid. The angle and population trend must show the expected monotonic behavior (angle decreasing from ~109.47° to ~70.53°, population falling to zero). The checker does not require reproducing exact experimental values; it compares against the paper's own computed results.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sif4_binding_curve.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_Si_F",
          "total_energy"
        ],
        "units": {
          "r_Si_F": "Å",
          "total_energy": "eV"
        }
      },
      "description": "Computed total electronic energy of an isolated SiF4 molecule as a function of the Si-F bond length. The checker extracts the equilibrium bond length from this curve."
    },
    {
      "file": "hf2_dissociation_surface.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_FH_Fminus",
          "r_Fminus_HF",
          "total_energy"
        ],
        "units": {
          "r_FH_Fminus": "Å",
          "r_Fminus_HF": "Å",
          "total_energy": "eV"
        }
      },
      "description": "Potential energy surface for HF2- dissociation. The checker locates the saddle point and computes the dissociation barrier."
    },
    {
      "file": "desorption_energy_surface_without_Hplus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_O_Si",
          "r_Si_Fminus",
          "total_energy",
          "optimized_O_Si_F_angle",
          "Si_O_bond_population"
        ],
        "units": {
          "r_O_Si": "Å",
          "r_Si_Fminus": "Å",
          "total_energy": "eV",
          "optimized_O_Si_F_angle": "deg",
          "Si_O_bond_population": "dimensionless"
        }
      },
      "description": "Desorption energy surface computed without hydrogen attack. Used for reference and trend comparisons."
    },
    {
      "file": "desorption_energy_surface_with_Hplus.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "r_O_Si",
          "r_Si_Fminus",
          "total_energy",
          "optimized_O_Si_F_angle",
          "Si_O_bond_population"
        ],
        "units": {
          "r_O_Si": "Å",
          "r_Si_Fminus": "Å",
          "total_energy": "eV",
          "optimized_O_Si_F_angle": "deg",
          "Si_O_bond_population": "dimensionless"
        }
      },
      "description": "Desorption energy surface computed with explicit H+ attack. The checker extracts the transition state and activation energy from this surface. Load-bearing: cannot be fabricated without running the core calculation."
    },
    {
      "file": "activation_energy_report.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "sif4_equilibrium_bond_length": "float (Å)",
          "hf2_dissociation_barrier": "float (eV)",
          "hf2_saddle_r": "float (Å)",
          "siF4_desorption_activation_energy": "float (eV)",
          "transition_state_r_O_Si": "float (Å)",
          "transition_state_r_Si_Fminus": "float (Å)",
          "angle_range": "list of two floats (min, max) in deg",
          "bond_population_range": "list of two floats (max, min) dimensionless"
        }
      },
      "description": "Summary report containing the extracted key quantities. Checked against hidden reference values with tolerances."
    },
    {
      "file": "angle_population_trend.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "case",
          "reaction_coordinate_rc",
          "optimized_O_Si_F_angle",
          "Si_O_bond_population"
        ],
        "units": {
          "reaction_coordinate_rc": "Å",
          "optimized_O_Si_F_angle": "deg",
          "Si_O_bond_population": "dimensionless"
        }
      },
      "description": "Trend of O-Si-F angle and Si-O bond population along the minimum-energy desorption path, for both H+ conditions. Checker verifies monotonic decrease in angle and population, with steeper collapse for the with_Hplus case."
    }
  ],
  "notes": "All energies are in eV, lengths in Å, angles in degrees. The desorption surface with H+ is the principal scored artifact; its activation energy must be derived from the computed grid. The angle and population trend must show the expected monotonic behavior (angle decreasing from ~109.47° to ~70.53°, population falling to zero). The checker does not require reproducing exact experimental values; it compares against the paper's own computed results."
}
```

## How you are scored
Your submitted artifacts are evaluated by a hidden verifier that independently processes each file according to a pre‑set rubric, measuring how closely the quantities you computed match the reference results. The verifier does **not** simply read a single claimed number; it recomputes key figures from your raw grids (locating minima and saddle points, extracting barriers and equilibrium distances) and checks monotonic trends and structural consistency. Each scored artifact carries a weight, with the desorption energy surface under H⁺ attack (load‑bearing) receiving the largest share, followed by the HF2⁻ dissociation surface and the SiF4 binding curve; the report and trend files each contribute a smaller fraction. Reporting the paper’s numbers without the underlying computation is insufficient — the reward depends on the numerical content of the raw data files and their agreement with the expected energetic and structural behaviour.
