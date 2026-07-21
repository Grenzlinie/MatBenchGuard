# MT-MAK97 Elasto-Viscoplastic Homogenization of Polycrystals

## Problem background
The accurate prediction of mechanical behavior in polycrystalline metals under deformation requires methods that simultaneously account for elastic and viscoplastic contributions. While full-field models can capture intragranular field fluctuations, they are computationally expensive. Mean-field homogenization schemes offer a more efficient alternative but must be robust during the elastoplastic transition and correctly converge to both purely elastic and viscoplastic limits. This task implements a recently proposed Mori-Tanaka elasto‑viscoplastic homogenization scheme (MT‑MAK97) designed to predict macroscopic stress‑strain curves, strain ratios, and grain‑family averaged lattice strains with their standard deviations — quantities directly comparable to diffraction experiments.

## Approach
The core idea is to approximate an elasto‑viscoplastic polycrystal as a collection of ellipsoidal grains embedded in a homogeneous matrix. Each grain's behavior is described by anisotropic linear elasticity and a power‑law viscoplastic flow rule for slip on crystallographic planes. The MT‑MAK97 scheme uses an additive interaction law that sums elastic and viscoplastic contributions, with separate Eshelby tensors defined for each regime. The matrix's elastic properties are obtained by a purely elastic self‑consistent homogenization, and its viscoplastic properties by a purely viscoplastic self‑consistent homogenization. The grain‑to‑matrix interaction is then solved via the MAK97 interaction equation, employing affine linearization of the non‑linear viscoplastic response, backward Euler time discretization, and fixed‑point iteration. Stress concentration tensors are derived consistent with the interaction law. Effective properties are computed through Mori‑Tanaka volume averaging, and second‑moment estimates yield intragranular strain rate fluctuations, from which lattice strain standard deviations are derived.

The implementation first generates a 500‑grain polycrystal with random orientations. Material parameters are set: for copper, single‑crystal elastic constants C₁₁=168.4 GPa, C₁₂=121.4 GPa, C₄₄=75.4 GPa; for stainless steel, the elastic constants and the calibrated Voce hardening parameters for MT‑MAK97 as reported in the original study. Slip is assumed on {111}<110> systems with a rate sensitivity exponent n=10. Two simulations are performed: copper compression at a strain rate of −1.0 s⁻¹ to a strain of −0.003; stainless steel tension at 0.0008 s⁻¹ to a strain of approximately 0.055. From the copper simulation, the macroscopic equivalent stress and the transverse‑to‑longitudinal strain ratio are recorded. From the stainless steel simulation, at the final strain the average and standard deviation of longitudinal and transverse lattice strains (in microstrain) are computed for grain families defined by the crystallographic planes {001}, {011}, and {111} parallel to the loading or transverse direction. All outputs are saved as CSV files for verification.

## Reproduction target
Implement the MT‑MAK97 homogenization scheme as described. Use it to simulate copper compression and stainless steel tension. Produce the following artifacts:
- `copper_stress_strain.csv`: true strain vs equivalent von Mises stress.
- `copper_strain_ratio.csv`: true strain vs transverse strain ratio.
- `stainless_lattice_averages.csv`: for each grain family ({001}, {011}, {111}) and direction (longitudinal, transverse), the mean lattice strain in microstrain at a final strain near 0.055.
- `stainless_lattice_std.csv`: for each family and direction, the standard deviation of lattice strain in microstrain.

## Assets

- Python 3.10: https://www.python.org/
- NumPy: https://pypi.org/project/numpy/
- SciPy: https://pypi.org/project/scipy/

## Workflow steps

### Step 1: Define microstructure and material parameters
- Role: process
- Action: Generate a 500‑grain polycrystal with random crystallographic orientations (uniform Euler angles). Assign single‑crystal elastic constants for Cu (C₁₁=168.4 GPa, C₁₂=121.4 GPa, C₄₄=75.4 GPa) and stainless steel (use the paper’s values). Define {111}<110> slip systems, the Voce hardening law, and set the MT‑MAK97 calibrated parameters from Table 1 of the paper. Specify boundary conditions (compression, tension) and strain increments.
- Evidence: `/app/outputs/data_prep_log.txt`

### Step 2: Implement MT‑MAK97 homogenization
- Role: process
- Action: Implement the MT‑MAK97 elasto‑viscoplastic self‑consistent scheme with affine linearization, Euler‑backward time integration, stress concentration tensors, fixed‑point iteration, and second‑moment estimation for intragranular fluctuations.
- Evidence: none

### Step 3: Copper compression stress–strain
- Role: scored
- Action: Simulate copper compression at a strain rate of −1.0 s⁻¹ to a true strain of −0.003 with a strain increment of −0.0001, using the MT‑MAK97 scheme. Record the macroscopic equivalent Von Mises stress (MPa) and true strain.
- Output file: `/app/outputs/copper_stress_strain.csv`
- Format: csv
- Contract: columns: strain (float, dimensionless), equivalent_stress (float, MPa)
- Scoring: scored by hidden verifier

### Step 4: Copper transverse strain ratio
- Role: scored
- Action: From the same copper simulation, compute the ratio of transverse strain (ε₁₁) to longitudinal strain (ε₃₃) and output as a function of strain.
- Output file: `/app/outputs/copper_strain_ratio.csv`
- Format: csv
- Contract: columns: strain (float, dimensionless), transverse_strain_ratio (float, dimensionless)
- Scoring: scored by hidden verifier

### Step 5: Stainless steel lattice strain averages
- Role: scored (load-bearing)
- Action: Simulate stainless steel tension at a strain rate of 0.0008 s⁻¹ using the MT‑MAK97 scheme and the calibrated hardening parameters. At a final macroscopic strain of ~0.055, compute the average longitudinal and transverse lattice strains (με) for the {111}, {011}, {001} grain families.
- Output file: `/app/outputs/stainless_lattice_averages.csv`
- Format: csv
- Contract: columns: family (string), direction (string), lattice_strain (float, microstrain)
- Scoring: scored by hidden verifier

### Step 6: Stainless steel lattice strain standard deviations
- Role: scored
- Action: From the same stainless steel simulation, compute the standard deviation of lattice strains (με) within each family for longitudinal and transverse directions, using the second‑moment estimation method.
- Output file: `/app/outputs/stainless_lattice_std.csv`
- Format: csv
- Contract: columns: family (string), direction (string), std_lattice_strain (float, microstrain)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/copper_stress_strain.csv`
- `/app/outputs/copper_strain_ratio.csv`
- `/app/outputs/stainless_lattice_averages.csv`
- `/app/outputs/stainless_lattice_std.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### copper_stress_strain.csv
- path: `/app/outputs/copper_stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Macroscopic true strain vs equivalent Von Mises stress for copper compression. The checker compares the curve to the paper's reference values with a relative error tolerance; meeting or exceeding the paper's accuracy (within tolerance) yields full credit.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `equivalent_stress`
  - `units`:
    - `strain`: dimensionless
    - `equivalent_stress`: MPa

### copper_strain_ratio.csv
- path: `/app/outputs/copper_strain_ratio.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Transverse-to-longitudinal strain ratio during copper compression. Checked against paper's values with an absolute tolerance.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `transverse_strain_ratio`
  - `units`:
    - `strain`: dimensionless
    - `transverse_strain_ratio`: dimensionless

### stainless_lattice_averages.csv
- path: `/app/outputs/stainless_lattice_averages.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Grain‑family averaged longitudinal and transverse lattice strains for stainless steel tension at final strain ~0.055. The checker compares to paper's values with a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `family`, `direction`, `lattice_strain`
  - `units`:
    - `lattice_strain`: microstrain

### stainless_lattice_std.csv
- path: `/app/outputs/stainless_lattice_std.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Standard deviation of lattice strains per family and direction. Compared to paper's values with a relative tolerance.
- schema:
  - `type`: table
  - `required_columns`: `family`, `direction`, `std_lattice_strain`
  - `units`:
    - `std_lattice_strain`: microstrain

Notes: All outputs are generated by the MT‑MAK97 homogenization implementation. No external experimental data files are required; the microscale geometry and material parameters are generated from public constants. The checker uses digitized reference data from the paper to evaluate accuracy within specified tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "copper_stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "equivalent_stress"
        ],
        "units": {
          "strain": "dimensionless",
          "equivalent_stress": "MPa"
        }
      },
      "description": "Macroscopic true strain vs equivalent Von Mises stress for copper compression. The checker compares the curve to the paper's reference values with a relative error tolerance; meeting or exceeding the paper's accuracy (within tolerance) yields full credit."
    },
    {
      "file": "copper_strain_ratio.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "transverse_strain_ratio"
        ],
        "units": {
          "strain": "dimensionless",
          "transverse_strain_ratio": "dimensionless"
        }
      },
      "description": "Transverse-to-longitudinal strain ratio during copper compression. Checked against paper's values with an absolute tolerance."
    },
    {
      "file": "stainless_lattice_averages.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "family",
          "direction",
          "lattice_strain"
        ],
        "units": {
          "lattice_strain": "microstrain"
        }
      },
      "description": "Grain‑family averaged longitudinal and transverse lattice strains for stainless steel tension at final strain ~0.055. The checker compares to paper's values with a relative tolerance."
    },
    {
      "file": "stainless_lattice_std.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "family",
          "direction",
          "std_lattice_strain"
        ],
        "units": {
          "std_lattice_strain": "microstrain"
        }
      },
      "description": "Standard deviation of lattice strains per family and direction. Compared to paper's values with a relative tolerance."
    }
  ],
  "notes": "All outputs are generated by the MT‑MAK97 homogenization implementation. No external experimental data files are required; the microscale geometry and material parameters are generated from public constants. The checker uses digitized reference data from the paper to evaluate accuracy within specified tolerances."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that independently checks each output CSV file. For each scored stage, the verifier compares your computed quantities against reference values derived from the original experimental and simulation study, using appropriate error metrics (e.g., relative error for stress‑strain curves, absolute difference for strain ratios). It computes a per‑stage score and combines them into a final reward, with the lattice strain averages carrying higher weight. The verifier also checks that the artifacts are well‑formed and that the stress‑strain curve is monotonic and lies within physically plausible bounds. Simply reporting the paper's numbers without genuine computation will not pass; the verifier assesses the actual calculated outputs.
