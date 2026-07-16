# Fermi-level alignment for Na-adsorbed MoS2 grain boundary defects

## Problem background
Monolayer MoS2 grain boundaries (GBs) host various atomic defect cores (Mo 5|7, Mo 6|8, S 5|7, S 4|6). Sodium atoms preferentially adsorb at these defects and donate electrons, but the effectiveness of free-electron doping depends on whether the Fermi level (EF) moves into the pristine conduction band. Calculating EF relative to the valence band maximum (EF−VBM) for each defect type with 0, 1, and 2 adsorbed Na atoms reveals how the defect type controls doping. The task is to compute these Fermi level positions and determine which configurations, if any, bring EF at or above the pristine conduction band minimum (CBM).

## Approach
Use plane-wave density functional theory (DFT) with the PBE functional and PAW pseudopotentials. First compute the band gap (CBM−VBM) of pristine monolayer MoS2 as a reference. Then construct 6×6×1 supercells containing a grain‑boundary loop for each of the four defect cores. Relax these intrinsic defect supercells, add 0, 1, and 2 Na atoms per core, and relax the combined structures. For every relaxed configuration, perform a density-of-states calculation, extract the Fermi energy EF and the valence band maximum VBM, and compute EF−VBM. Compare these values to the pristine CBM to identify whether EF enters the conduction band. The workflow is implemented with open‑source codes (Quantum ESPRESSO and the Atomic Simulation Environment).

## Reproduction target
Produce two artifacts. (1) `pristine_cbm.json`: the computed pristine MoS2 band gap (CBM−VBM in eV). (2) `ef_vs_vbm_table.csv`: a table of EF−VBM (eV) for every defect type (Mo5|7, Mo6|8, S5|7, S4|6) and Na count (0, 1, 2) — 12 data rows total. Using these, determine for which defect/Na combinations the Fermi level lies at or above the pristine CBM (i.e., EF−VBM ≥ CBM−VBM).

## Assets

- Quantum ESPRESSO (pw.x): https://www.quantum-espresso.org/
- SSSP PBE PAW pseudopotentials (efficiency version): https://www.materialscloud.org/discover/sssp/table/efficiency
- Atomic Simulation Environment (ASE): https://gitlab.com/ase/ase

## Workflow steps

### Step 1: Pristine monolayer MoS2 band‑gap reference
- Role: scored
- Action: Relax a hexagonal monolayer MoS2 unit cell using DFT (PBE, appropriate k‑point mesh and cutoff). Perform a band‑structure calculation, extract the CBM and VBM energies, and write the CBM−VBM gap as cb_minus_vbm (eV).
- Output file: `/app/outputs/pristine_cbm.json`
- Format: json
- Contract: JSON object with a single key 'cb_minus_vbm' (float, in eV).
- Scoring: scored by hidden verifier

### Step 2: Build GB‑loop supercell models for the four defect types
- Role: process
- Action: Using the relaxed lattice constant from step_01, construct 6×6×1 monolayer MoS2 supercells containing a GB loop with each of the four defect cores: Mo 5|7, Mo 6|8, S 5|7, S 4|6. The loop geometry must avoid dipole and edge effects.
- Evidence: none

### Step 3: DFT relaxation of intrinsic defect supercells
- Role: process
- Action: Perform full DFT geometry relaxation (PBE, Γ‑point sampling, force threshold <0.001 eV/Å) of each intrinsic defect supercell from step_02 to obtain stable reference structures.
- Evidence: none

### Step 4: Na adsorption and relaxation for each defect
- Role: process
- Action: For each intrinsic defect supercell from step_03, add 0, 1, and 2 Na atoms near the defect core and relax the combined structures using DFT (PBE, Γ‑point sampling, force threshold <0.001 eV/Å). This yields 12 relaxed configurations.
- Evidence: none

### Step 5: Fermi‑level analysis for Na‑adsorbed defects
- Role: scored (load-bearing)
- Action: For each of the 12 relaxed structures from step_04, perform a DOS calculation using a 6×6×1 k‑point mesh. Extract the Fermi energy EF and the valence band maximum VBM. Compute EF_minus_VBM (in eV) and write a CSV table with columns defect_type, Na_count, EF_minus_VBM.
- Output file: `/app/outputs/ef_vs_vbm_table.csv`
- Format: csv
- Contract: CSV with three columns: defect_type (string, one of Mo5|7, Mo6|8, S5|7, S4|6), Na_count (integer 0,1,2), EF_minus_VBM (float, in eV). Exactly 12 data rows.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pristine_cbm.json`
- `/app/outputs/ef_vs_vbm_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pristine_cbm.json
- path: `/app/outputs/pristine_cbm.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Pristine monolayer MoS2 band gap (CBM−VBM) in eV, used as alignment reference.
- schema:
  - `type`: object
  - `required`:
    - `cb_minus_vbm`: number

### ef_vs_vbm_table.csv
- path: `/app/outputs/ef_vs_vbm_table.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Fermi level positions relative to the valence band maximum for each defect type and Na count.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `Na_count`, `EF_minus_VBM`

Notes: The checker uses the agent's own pristine band gap to align the Fermi levels and verifies that EF_minus_VBM ≥ pristine CBM only for S5|7 with 2 Na, and never decreases with Na count for any defect. Tolerance of 0.2 eV accounts for code-to-code variation.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pristine_cbm.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "cb_minus_vbm": "number"
        }
      },
      "description": "Pristine monolayer MoS2 band gap (CBM−VBM) in eV, used as alignment reference."
    },
    {
      "file": "ef_vs_vbm_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "Na_count",
          "EF_minus_VBM"
        ]
      },
      "description": "Fermi level positions relative to the valence band maximum for each defect type and Na count."
    }
  ],
  "notes": "The checker uses the agent's own pristine band gap to align the Fermi levels and verifies that EF_minus_VBM ≥ pristine CBM only for S5|7 with 2 Na, and never decreases with Na count for any defect. Tolerance of 0.2 eV accounts for code-to-code variation."
}
```

## How you are scored
A hidden verifier examines both output files. It uses the agent‑computed pristine band gap as the alignment reference. For each defect type it checks that EF−VBM does not decrease when the Na count increases (non‑strict monotonicity). It also verifies whether any configuration has EF−VBM at or above the pristine CBM. The reward is based on the internal self‑consistency of the reported values and the correct structural trends across defect types and Na counts; the exact numerical values are assessed with tolerances that absorb legitimate methodological spread.
