# CPFEM Slip Activity in HCP-MPEA vs Pure Ti

## Problem background
This task investigates mesoscale deformation mechanisms in a single-phase hexagonal close-packed (HCP) multi-principal element alloy (MPEA) compared to a conventional HCP metal (pure Ti). The work aims to understand how differences in dislocation slip activity, particularly on pyramidal planes, influence intragranular deformation homogeneity. Crystal plasticity finite element modeling (CPFEM) is used to simulate uniaxial tension of a 1000‑grain polycrystal aggregate with a basal texture, employing published critical resolved shear stress (CRSS) and hardening parameters for both materials. The target quantities are the normalized shear contributions (total shear divided by the Burgers vector magnitude) of key slip systems—Prism ⟨a⟩, Pyr1 ⟨a⟩, and Pyr1 ⟨c+a⟩—as a function of tensile strain, to be reproduced from the described simulation protocol.

## Approach
The core approach is a computational crystal plasticity finite element simulation using the open‑source framework PRISMS‑Plasticity. A 1000‑crystal aggregate represents the polycrystal, and an initial texture is generated that matches the published basal {0002} pole figure: a peak intensity of approximately 8 multiples of random distribution (MRD) near the normal direction, with a spread towards the rolling direction. Two separate simulations are performed—one for Ti and one for the HCP‑MPEA—using the respective critical resolved shear stress (CRSS) and hardening parameters reported in the literature for these materials. Uniaxial tension is applied up to a true strain of approximately 0.15. At each output strain step, the total accumulated shear on each slip system is divided by the magnitude of its Burgers vector to obtain the normalized shear. The strain‑dependent results are recorded, and the values at a true strain of ~0.08 are interpolated for direct comparison with experimental slip‑trace statistics.

## Reproduction target
Produce two comma‑separated value (CSV) files. The first file (`step_01_shear_vs_strain.csv`) contains the strain‑dependent normalized shear values for Prism ⟨a⟩, Pyr1 ⟨a⟩, and Pyr1 ⟨c+a⟩ in both Ti and the HCP‑MPEA, covering the entire deformation history up to a true strain of ~0.15. The second file (`step_02_shear_at_strain_0.08.csv`) provides the interpolated normalized shear values for the same three slip systems in both materials at a true strain of approximately 0.08. These outputs form the minimal computational reproduction of the CPFEM prediction; the resulting values should be internally consistent with the published initial texture and hardening parameters.

## Assets

- PRISMS-Plasticity: https://github.com/prisms-center/PRISMS-Plasticity
- Python packages (numpy, pandas, scipy, matplotlib): pip install numpy pandas scipy matplotlib
- C++ compiler and CMake: apt-get install g++ cmake

## Workflow steps

### Step 1: Generate initial texture
- Role: process
- Action: Generate a set of 1000 crystal orientations for a polycrystal aggregate that reproduces the published basal texture: a {0002} pole figure with a peak intensity of approximately 8 MRD near the normal direction (ND) and a spread towards the rolling direction (RD). The same orientation set can be used for both Ti and HCP-MPEA as their textures are reported to be similar.
- Evidence: `/app/outputs/initial_orientations.txt`

### Step 2: CPFEM shear vs strain
- Role: scored
- Action: Using PRISMS-Plasticity, run uniaxial tension simulations on the 1000-grain aggregate separately for Ti (Table 1 parameters) and HCP-MPEA (Table 2 parameters) up to a true strain of approximately 0.15. At each output step, record the true strain and the normalized shear (total shear divided by the Burgers vector magnitude) for slip systems Prism ⟨a⟩, Pyr1 ⟨a⟩, and Pyr1 ⟨c+a⟩. Write the results to a CSV file.
- Output file: `/app/outputs/step_01_shear_vs_strain.csv`
- Format: csv
- Contract: Columns: material (string, 'Ti' or 'MPEA'), true_strain (float), slip_system (string, 'Prism_a', 'Pyr1_a', 'Pyr1_ca'), normalized_shear (float).
- Scoring: scored by hidden verifier

### Step 3: CPFEM shear at strain 0.08
- Role: scored (load-bearing)
- Action: From the same simulation results, interpolate or extract the normalized shear values for Prism ⟨a⟩, Pyr1 ⟨a⟩, and Pyr1 ⟨c+a⟩ at a true strain of approximately 0.08 for both Ti and HCP-MPEA. Write the six values to a CSV file.
- Output file: `/app/outputs/step_02_shear_at_strain_0.08.csv`
- Format: csv
- Contract: Columns: material (string, 'Ti' or 'MPEA'), slip_system (string, 'Prism_a', 'Pyr1_a', 'Pyr1_ca'), normalized_shear (float). One row per material–slip_system combination (6 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_shear_vs_strain.csv`
- `/app/outputs/step_02_shear_at_strain_0.08.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_shear_vs_strain.csv
- path: `/app/outputs/step_01_shear_vs_strain.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Strain-dependent normalized shear values for Prism ⟨a⟩, Pyr1 ⟨a⟩, and Pyr1 ⟨c+a⟩ in Ti and HCP‑MPEA. The checker will verify that Pyr1 ⟨a⟩ normalized shear in HCP‑MPEA increases monotonically with strain and exceeds the Ti value at every reported strain step.
- schema:
  - `type`: table
  - `required_columns`: `material`, `true_strain`, `slip_system`, `normalized_shear`
  - `units`: object

### step_02_shear_at_strain_0.08.csv
- path: `/app/outputs/step_02_shear_at_strain_0.08.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Normalized shear values at true strain ~0.08 for the three slip systems in both materials. The six numeric values will be compared against paper‑reported values with a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `material`, `slip_system`, `normalized_shear`
  - `units`: object

Notes: The first file is scored via structural trend checks; the second via value comparison with tolerance. Both must be present and well‑formed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_shear_vs_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "true_strain",
          "slip_system",
          "normalized_shear"
        ],
        "units": {}
      },
      "description": "Strain-dependent normalized shear values for Prism ⟨a⟩, Pyr1 ⟨a⟩, and Pyr1 ⟨c+a⟩ in Ti and HCP‑MPEA. The checker will verify that Pyr1 ⟨a⟩ normalized shear in HCP‑MPEA increases monotonically with strain and exceeds the Ti value at every reported strain step."
    },
    {
      "file": "step_02_shear_at_strain_0.08.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "slip_system",
          "normalized_shear"
        ],
        "units": {}
      },
      "description": "Normalized shear values at true strain ~0.08 for the three slip systems in both materials. The six numeric values will be compared against paper‑reported values with a hidden tolerance."
    }
  ],
  "notes": "The first file is scored via structural trend checks; the second via value comparison with tolerance. Both must be present and well‑formed."
}
```

## How you are scored
A hidden verifier will independently evaluate the two output files. For `step_01_shear_vs_strain.csv`, the verifier performs a structural audit: it checks that the normalized shear of Pyr1 ⟨a⟩ in the HCP‑MPEA increases monotonically with strain and that, at every reported strain step, the HCP‑MPEA value exceeds the corresponding Ti value. For `step_02_shear_at_strain_0.08.csv`, the verifier compares the six reported normalized shear values (two materials × three slip systems) against reference values derived from the published experiment and CPFEM analysis, applying a hidden tolerance to account for discretization and implementation‑specific variations. The overall score is a combination of the two checks; both files must be present, well‑formed, and produced by a simulation that follows the described texture generation and hardening parameter workflow.
