# Threshold displacement energies in faulted 3C-SiC from ab initio molecular dynamics

## Problem background
Cubic silicon carbide (3C-SiC) is a promising material for nuclear applications due to its high-temperature stability, corrosion resistance, and low neutron absorption. Its performance under irradiation is critically influenced by the threshold displacement energy (Ed) — the minimum kinetic energy required for a primary knock-on atom (PKA) to permanently leave its lattice site and create stable defects. Real 3C-SiC often contains stacking faults, which may alter Ed and thereby change the material's radiation tolerance. This task investigates how the presence of an intrinsic stacking fault in 3C-SiC affects the threshold displacement energies of carbon and silicon atoms, by re-running ab initio molecular dynamics simulations and comparing Ed values for perfect and faulted crystal structures.

## Approach
The reproduction employs ab initio molecular dynamics (AIMD) based on density functional theory (DFT). The workflow begins by building supercells for perfect 3C-SiC and for 3C-SiC containing a single intrinsic stacking fault (stacking sequence (ABC)(AC)(ABC)). The DFT setup uses the SIESTA code with Troullier-Martins norm-conserving pseudopotentials, the GGA-PBE exchange-correlation functional, a single-zeta basis, 1x1x1 k-point sampling, and a 90 Ry plane-wave cutoff. For the perfect supercell, a C PKA and a Si PKA near the cell center are selected; for the faulted supercell, the C1 and Si1 atoms at the fault boundary (as defined in the original experimental protocol) are selected. NVE AIMD simulations are performed with initial velocities directed perpendicular to the (111) plane — the [001] direction. Starting from low kinetic energies, simulations are repeated at increasing energies until the PKA permanently displaces, forming a stable defect. The Ed is identified as the lowest energy that leads to permanent displacement. The four Ed values are compiled and compared across the two structures to assess the influence of the stacking fault.

## Reproduction target
Using ab initio molecular dynamics, determine the threshold displacement energies for the following four PKA/condition combinations:

- C PKA in unfaulted 3C-SiC, recoil direction [001]
- Si PKA in unfaulted 3C-SiC, recoil direction [001]
- C1 PKA at the fault boundary of the intrinsic stacking fault (ISF_AC), recoil direction [001]
- Si1 PKA at the fault boundary of the intrinsic stacking fault (ISF_AC), recoil direction [001]

Report the results by writing a CSV file with columns `structure`, `pka_type`, `direction`, `ed_value`. The file must contain exactly four rows, one per combination, with `ed_value` given in eV. The CSV format, column names, and allowed values are specified in the 'Output contract' and in Step 6 of the workflow.

## Assets

- SIESTA code: https://departments.icmab.es/leem/siesta/
- Troullier-Martins norm-conserving pseudopotentials for C and Si: https://departments.icmab.es/leem/siesta/Pseudopotentials/
- Python: python3

## Workflow steps

### Step 1: DFT validation for bulk 3C-SiC
- Role: process
- Action: Run a ground-state DFT calculation for bulk 3C-SiC using SIESTA to confirm that the chosen pseudopotentials and settings reproduce the experimental lattice constant and cohesive energy within reasonable accuracy.
- Evidence: `/app/outputs/validation_output.txt`

### Step 2: Build perfect 3C-SiC supercell
- Role: process
- Action: Construct a supercell of perfect 3C-SiC (e.g., 216 atoms) with the surface normal along the [001] direction, perpendicular to the (111) plane. The atomic positions follow the zinc-blende structure with the experimental lattice constant.
- Evidence: none

### Step 3: Build intrinsic stacking fault supercell
- Role: process
- Action: Construct a supercell of 3C-SiC containing an intrinsic stacking fault with the stacking sequence (ABC)(AC)(ABC), totaling 256 atoms. Place the fault plane parallel to the (111) plane and identify the C1 and Si1 sites on the fault boundary as potential primary knock-on atoms (PKA).
- Evidence: none

### Step 4: AIMD for Ed in perfect SiC
- Role: process
- Action: For the perfect SiC supercell, select one C PKA and one Si PKA near the cell center. Starting from low kinetic energies, run NVE AIMD simulations with an initial velocity vector along the [001] direction. Repeat at increasing initial kinetic energies until the PKA permanently leaves its lattice site and forms a stable defect. Determine the threshold displacement energy Ed as the minimum energy that leads to permanent displacement.
- Evidence: none

### Step 5: AIMD for Ed in faulted SiC
- Role: process
- Action: For the intrinsic stacking fault supercell, perform AIMD simulations as in the previous step for the C1 PKA and the Si1 PKA, each along the [001] direction. Determine the threshold displacement energy for each case.
- Evidence: none

### Step 6: Compile threshold displacement energies
- Role: scored (load-bearing)
- Action: Collect the four determined Ed values and write them to a CSV file with columns: structure, pka_type, direction, ed_value. One row per (structure, pka_type) combination.
- Output file: `/app/outputs/threshold_displacement_energies.csv`
- Format: csv
- Contract: structure: string (unfaulted | ISF_AC), pka_type: string (C | Si), direction: string ([001]), ed_value: float (eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/threshold_displacement_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### threshold_displacement_energies.csv
- path: `/app/outputs/threshold_displacement_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: The file must contain four rows. The checker will compare each reported Ed value to the corresponding hidden reference value from the original study, using a tolerance appropriate for AIMD reproducibility. The score is the proportion of values that match within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `structure`, `pka_type`, `direction`, `ed_value`
  - `units`:
    - `ed_value`: eV

Notes: The scored artifact is a CSV compilation of the threshold displacement energies obtained from the AIMD simulations. The checker does not access any external datasets; all reference values are embedded in the hidden grading specification.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "threshold_displacement_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "structure",
          "pka_type",
          "direction",
          "ed_value"
        ],
        "units": {
          "ed_value": "eV"
        }
      },
      "description": "The file must contain four rows. The checker will compare each reported Ed value to the corresponding hidden reference value from the original study, using a tolerance appropriate for AIMD reproducibility. The score is the proportion of values that match within tolerance."
    }
  ],
  "notes": "The scored artifact is a CSV compilation of the threshold displacement energies obtained from the AIMD simulations. The checker does not access any external datasets; all reference values are embedded in the hidden grading specification."
}
```

## How you are scored
A hidden verifier independently reads your `/app/outputs/threshold_displacement_energies.csv` file. It compares each reported `ed_value` against a hidden reference value obtained from the original experimental study. Each comparison uses a tolerance that reflects the expected reproducibility of AIMD simulations with SIESTA and the specified computational settings (GGA-PBE, single-zeta basis, etc.). The final reward is the proportion of the four Ed values that fall within the allowed tolerance. To achieve a high score, you must genuinely run all required DFT and AIMD calculations and report the resulting Ed values; simply copying a published number without performing the computations will almost certainly not satisfy the tolerance criteria.
