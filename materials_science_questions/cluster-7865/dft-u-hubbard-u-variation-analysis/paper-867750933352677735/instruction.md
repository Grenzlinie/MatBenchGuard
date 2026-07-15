# First-principles Calculation of Spin-Orbit Coupling ⟨L·S⟩ and XAS Branching Ratio via J-basis Projection

## Problem background
Spin-orbit coupling (SOC) profoundly affects the electronic properties of 5d transition-metal oxides, such as iridates. In these materials, the competition between SOC, crystal field, and electronic correlations can lead to novel insulating states. A key quantity characterizing SOC strength is the expectation value <L·S>. Experimental probes, notably the X-ray absorption spectroscopy (XAS) branching ratio at Ir L-edges, provide a handle on <L·S> through a known sum-rule relation. However, a direct first-principles estimation of <L·S> and the branching ratio from a material's electronic structure is not straightforward and is rarely performed. This task addresses that gap by implementing a formalism to compute <L·S> and the corresponding branching ratio from density-functional theory (DFT) calculations, and applying it to representative iridate systems.

## Approach
The method expands Kohn-Sham eigenstates from a DFT calculation (including SOC and an on-site Hubbard correction) into a basis of total angular momentum J eigenstates for the Ir-5d orbitals. The local projection onto J=5/2 and J=3/2 makes it possible to compute the expectation value <L·S> by summing the occupancies of these components weighted by the eigenvalues of the L·S operator (1.0 for J=5/2, -1.5 for J=3/2). The number of d holes, n_h, is obtained from a Mulliken population analysis. The XAS branching ratio (I_L3/I_L2) is then derived from the formula (2 - r)/(1 + r), where r = <L·S>/n_h, which follows from the dipole sum rule.

To illustrate the necessity of projecting onto the full J-basis (including both t2g and eg orbitals) rather than the commonly used jeff basis, a simple model calculation is performed: for a d^5 configuration in an octahedral crystal field, the full d-orbital Hamiltonian with SOC is diagonalized as a function of the crystal-field splitting 10Dq, and <L·S> is computed using both the full J-basis and the jeff-only basis.

For real materials, DFT+U+SOC calculations are carried out on two representative iridates: Sr2IrO4 (undoped) and the double perovskite Sr2MgIrO6. Calculation parameters include PBE exchange-correlation, U_eff = 2.0 eV, fully relativistic pseudopotentials, non-collinear spin treatment, and appropriate k-point grids. After convergence, the Kohn-Sham states are projected onto the J-basis to compute <L·S>, n_h, and the branching ratio.

## Reproduction target
1. Model calculation: For a d^5 configuration in an octahedral crystal field, compute <L·S> as a function of crystal-field splitting 10Dq (0 to 5 eV, at least 10 evenly spaced points) using both the full J-basis (t2g+eg) and the restricted jeff-basis (t2g only). Output a CSV file with columns `10Dq` (eV), `LS_J`, `LS_jeff` (both dimensionless).

2. Material results: Using DFT+U+SOC calculations (as detailed in the workflow steps) for Sr2IrO4 (x=0) and Sr2MgIrO6, perform J-basis projection to compute the spin-orbit coupling expectation value <L·S> (dimensionless), the number of d holes n_h, and the branching ratio I_L3/I_L2 via (2 - r)/(1 + r) with r = <L·S>/n_h. Output a JSON file containing these three numerical fields for each compound.

## Assets

- OpenMX software package: http://www.openmx-square.org/
- OpenMX pseudopotential library: http://www.openmx-square.org/download.html
- Crystal structure of Sr2IrO4
- Experimental lattice parameters for Sr2XIrO6

## Workflow steps

### Step 1: Geometry optimization of Sr2IrO4
- Role: process
- Action: Optimize the unit cell and internal coordinates of Sr2IrO4 using DFT (PBE, OpenMX) with a force convergence criterion of 0.01 eV/Å.
- Evidence: `/app/outputs/sr2iro4_opt.log`

### Step 2: Model calculation of ⟨L·S⟩ vs 10Dq
- Role: scored
- Action: For a d^5 configuration in an octahedral crystal field, construct the full d-orbital Hamiltonian including SOC, diagonalize it as a function of the crystal-field splitting 10Dq (ranging from 0 to 5 eV, at least 10 evenly spaced points), compute ⟨L·S⟩ using the full J-basis (t2g+eg) and the restricted jeff-basis (t2g only), and output the results.
- Output file: `/app/outputs/step_01_model_LS.csv`
- Format: csv
- Contract: columns: 10Dq (eV), LS_J (dimensionless), LS_jeff (dimensionless); one row per 10Dq value (at least 10 points evenly spaced 0–5 eV).
- Scoring: scored by hidden verifier

### Step 3: DFT+U+SOC for Sr2IrO4 (x=0)
- Role: process
- Action: Using the optimized structure from the geometry optimization step, perform a DFT+U+SOC calculation with OpenMX: PBE functional, U_eff = 2.0 eV, fully relativistic pseudopotentials, non-collinear SOC, 300 Ry energy cutoff, 5×5×2 k-mesh. This yields Kohn-Sham eigenstates and band energies.
- Evidence: `/app/outputs/sr2iro4_calc.log`

### Step 4: DFT+U+SOC for Sr2MgIrO6
- Role: process
- Action: Using the experimental lattice parameter a=3.958 Å and the standard double perovskite structure (antiferromagnetic order in a 20-atom cell), perform a DFT+U+SOC calculation with OpenMX: PBE functional, U_eff = 2.0 eV, fully relativistic pseudopotentials, non-collinear SOC, 300 Ry energy cutoff, 9×9×7 k-mesh.
- Evidence: `/app/outputs/sr2mgiro6_calc.log`

### Step 5: Compute ⟨L·S⟩, n_h, and branching ratio
- Role: scored (load-bearing)
- Action: For each of the two DFT+U+SOC calculations (Sr2IrO4 and Sr2MgIrO6), project the Kohn-Sham states onto J=5/2 and J=3/2 basis states for Ir-5d orbitals, sum over occupied states to obtain ⟨L·S⟩, count the number of d holes n_h via Mulliken population analysis, and compute the branching ratio as (2 - r)/(1 + r) with r = ⟨L·S⟩/n_h. Save the results in a single JSON file with keys identifying the compounds.
- Output file: `/app/outputs/step_02_material_results.json`
- Format: json
- Contract: Object with keys 'Sr2IrO4_x=0' and 'Sr2MgIrO6'. Each value is an object with numeric fields: LS (float), n_h (float), branching_ratio (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_model_LS.csv`
- `/app/outputs/step_02_material_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_model_LS.csv
- path: `/app/outputs/step_01_model_LS.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Model calculation of spin-orbit coupling as a function of crystal-field splitting in a d^5 atomic limit. Verification checks that LS_J > LS_jeff at all points and that the difference at 10Dq≈1.8 eV exceeds a threshold.
- schema:
  - `type`: table
  - `required_columns`: `10Dq`, `LS_J`, `LS_jeff`
  - `units`:
    - `10Dq`: eV

### step_02_material_results.json
- path: `/app/outputs/step_02_material_results.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Computed ⟨L·S⟩, hole count n_h, and branching ratio for Sr2IrO4 (x=0) and Sr2MgIrO6. Scored by comparing LS and branching_ratio to hidden reference values and verifying internal consistency.
- schema:
  - `type`: object
  - `properties`:
    - `Sr2IrO4_x=0`:
      - `type`: object
      - `properties`:
        - `LS`:
          - `type`: number
          - `description`: Spin-orbit coupling expectation value (dimensionless)
        - `n_h`:
          - `type`: number
          - `description`: Number of d holes
        - `branching_ratio`:
          - `type`: number
          - `description`: Branching ratio I_L3/I_L2
      - `required`: `LS`, `n_h`, `branching_ratio`
    - `Sr2MgIrO6`:
      - `type`: object
      - `properties`:
        - `LS`:
          - `type`: number
        - `n_h`:
          - `type`: number
        - `branching_ratio`:
          - `type`: number
      - `required`: `LS`, `n_h`, `branching_ratio`
  - `required`: `Sr2IrO4_x=0`, `Sr2MgIrO6`

Notes: The model calculation (step_01) is verified via structural properties (ordering and difference). The material results are compared against paper-extracted reference values with tolerances, and internal consistency r=LS/n_h is checked.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_model_LS.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "10Dq",
          "LS_J",
          "LS_jeff"
        ],
        "units": {
          "10Dq": "eV"
        }
      },
      "description": "Model calculation of spin-orbit coupling as a function of crystal-field splitting in a d^5 atomic limit. Verification checks that LS_J > LS_jeff at all points and that the difference at 10Dq≈1.8 eV exceeds a threshold."
    },
    {
      "file": "step_02_material_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "properties": {
          "Sr2IrO4_x=0": {
            "type": "object",
            "properties": {
              "LS": {
                "type": "number",
                "description": "Spin-orbit coupling expectation value (dimensionless)"
              },
              "n_h": {
                "type": "number",
                "description": "Number of d holes"
              },
              "branching_ratio": {
                "type": "number",
                "description": "Branching ratio I_L3/I_L2"
              }
            },
            "required": [
              "LS",
              "n_h",
              "branching_ratio"
            ]
          },
          "Sr2MgIrO6": {
            "type": "object",
            "properties": {
              "LS": {
                "type": "number"
              },
              "n_h": {
                "type": "number"
              },
              "branching_ratio": {
                "type": "number"
              }
            },
            "required": [
              "LS",
              "n_h",
              "branching_ratio"
            ]
          }
        },
        "required": [
          "Sr2IrO4_x=0",
          "Sr2MgIrO6"
        ]
      },
      "description": "Computed ⟨L·S⟩, hole count n_h, and branching ratio for Sr2IrO4 (x=0) and Sr2MgIrO6. Scored by comparing LS and branching_ratio to hidden reference values and verifying internal consistency."
    }
  ],
  "notes": "The model calculation (step_01) is verified via structural properties (ordering and difference). The material results are compared against paper-extracted reference values with tolerances, and internal consistency r=LS/n_h is checked."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's artifact and combines them by weight into the final reward.

- For the model calculation (step_01_model_LS.csv), the verifier checks structural relationships: the LS value computed with the full J-basis must exceed that from the jeff-basis at every 10Dq point, and the difference at a representative mid-range 10Dq must cross a hidden threshold.

- For the material results (step_02_material_results.json), the verifier compares your computed LS and branching_ratio for each compound to hidden reference values (with appropriate tolerances), and also verifies internal consistency: the branching_ratio you report must match the value derived from your LS and n_h via (2 - r)/(1 + r) within a small numerical tolerance.

Reporting a number is not sufficient; your artifacts must survive these structural and reference checks.
