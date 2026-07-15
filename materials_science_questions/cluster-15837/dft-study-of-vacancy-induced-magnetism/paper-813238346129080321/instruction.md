# DFT study of vacancy-induced magnetism in zigzag SiC nanoribbons

## Problem background
Zigzag SiC nanoribbons exhibit half-metallic behavior that is promising for spintronic applications. To understand how intrinsic defects and impurities alter their electronic and magnetic characteristics, this work examines the effect of single and double silicon and carbon vacancies, as well as boron substitution, on a representative Z-SiCNR. The main physical quantities of interest are the total magnetic moment per supercell and the spin-resolved band gaps, which together indicate whether the ribbon remains half-metallic, becomes metallic, or becomes semiconducting.

## Approach
The investigation uses spin-polarized density functional theory (DFT) within the generalized gradient approximation (GGA-PBE) and norm-conserving Troullier-Martins pseudopotentials, as implemented in the SIESTA code. A supercell model of a hydrogen-passivated 6-ZSiCNR is built, and the atomic positions are relaxed. The total magnetic moment is obtained from Mulliken population analysis, and the spin-up and spin-down band gaps are extracted from the electronic band structure. These properties are computed for the pristine ribbon and for five defective configurations: a single Si vacancy, a single C vacancy, two Si vacancies, a Si+C divacancy, and a Si vacancy with a boron atom occupying the second vacant Si site. By comparing the computed magnetic moments and band gaps across these systems, the role of each defect type is assessed.

## Reproduction target
Produce a CSV file `/app/outputs/computed_results.csv` that contains, for each of the six systems (pristine, V_Si, V_C, V_Si^1V_Si^4, V_Si^1V_C^8, V_Si^1B_Si^4), the total magnetic moment (in μB) and the spin-up and spin-down band gaps (in eV). For systems that are metallic in a given spin channel (i.e., no band gap), report NaN for that gap. The values must be obtained by running the DFT workflow described in the steps below.

## Assets

- SIESTA code: https://siesta-project.org/
- Troullier-Martins pseudopotentials for Si, C, H, B, N: SIESTA pseudopotential database or Quantum ESPRESSO pseudopotential library

## Workflow steps

### Step 1: Construct supercell model
- Role: process
- Action: Build the 6Z-SiCNR supercell with width 6, H-terminated edges, and vacuum layers as described in the method. Generate a geometry file pristine.xyz containing the atomic coordinates.
- Evidence: `/app/outputs/pristine.xyz`

### Step 2: DFT for pristine nanoribbon
- Role: process
- Action: Run spin-polarized DFT relaxation and electronic structure calculation for pristine 6Z-SiCNR. Compute total magnetic moment via Mulliken analysis and band gaps from band structure. Save the DFT output log as pristine.log.
- Evidence: `/app/outputs/pristine.log`

### Step 3: DFT for single Si vacancy
- Role: process
- Action: Remove the Si atom at site 1 from the pristine supercell, relax the structure, and run DFT to obtain total magnetic moment and band gaps. Save the output log as vsi.log.
- Evidence: `/app/outputs/vsi.log`

### Step 4: DFT for single C vacancy
- Role: process
- Action: Remove the C atom at site 7 from the pristine supercell, relax, and run DFT to obtain total magnetic moment and band gaps. Save the output log as vc.log.
- Evidence: `/app/outputs/vc.log`

### Step 5: DFT for double Si vacancies (V_Si^1 V_Si^4)
- Role: process
- Action: Remove Si atoms at sites 1 and 4 from the pristine supercell, relax, and run DFT to obtain total magnetic moment and band gaps. Save the output log as vsivsi4.log.
- Evidence: `/app/outputs/vsivsi4.log`

### Step 6: DFT for Si+C divacancy (V_Si^1 V_C^8)
- Role: process
- Action: Remove Si at site 1 and C at site 8 from the pristine supercell, relax, and run DFT to obtain total magnetic moment and band gaps. Save the output log as vsivc8.log.
- Evidence: `/app/outputs/vsivc8.log`

### Step 7: DFT for V_Si with B substitution (V_Si^1 B_Si^4)
- Role: process
- Action: Create a Si vacancy at site 1 and substitute a B atom at the vacant Si site 4, relax, and run DFT to obtain total magnetic moment and band gaps. Save the output log as vsibsi4.log.
- Evidence: `/app/outputs/vsibsi4.log`

### Step 8: Compile results into CSV
- Role: scored (load-bearing)
- Action: From the DFT output logs, extract for each of the six systems (pristine, V_Si, V_C, V_Si^1V_Si^4, V_Si^1V_C^8, V_Si^1B_Si^4) the total magnetic moment (μB) from Mulliken analysis and the spin-up/spin-down band gaps (eV). For metallic systems where a band gap is not defined, use NaN. Write a CSV file computed_results.csv with columns: system, total_magnetic_moment, spin_up_gap, spin_down_gap.
- Output file: `/app/outputs/computed_results.csv`
- Format: csv
- Contract: columns: system (string), total_magnetic_moment (float, μB), spin_up_gap (float, eV), spin_down_gap (float, eV)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_results.csv
- path: `/app/outputs/computed_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total magnetic moments and spin-resolved band gaps for pristine 6Z-SiCNR and six defective configurations.
- schema:
  - `type`: table
  - `required_columns`: `system`, `total_magnetic_moment`, `spin_up_gap`, `spin_down_gap`
  - `units`:
    - `total_magnetic_moment`: μB
    - `spin_up_gap`: eV
    - `spin_down_gap`: eV

Notes: All V_Si+N substitution configurations are represented by V_Si^1N_C^8 as the representative case.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "total_magnetic_moment",
          "spin_up_gap",
          "spin_down_gap"
        ],
        "units": {
          "total_magnetic_moment": "μB",
          "spin_up_gap": "eV",
          "spin_down_gap": "eV"
        }
      },
      "description": "Total magnetic moments and spin-resolved band gaps for pristine 6Z-SiCNR and six defective configurations."
    }
  ],
  "notes": "All V_Si+N substitution configurations are represented by V_Si^1N_C^8 as the representative case."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/computed_results.csv` and compare the reported magnetic moments and band gaps to a hidden reference. The verifier checks each system's moment and spin gaps within appropriate tolerances and also validates the overall electronic character (metallic, half-metallic, or semiconducting) inferred from the gaps. Partial credit is awarded for each system based on agreement with the hidden reference; the final reward is a weighted combination of these scores. Simply reporting values without executing the correct workflow will not yield a valid solution, because the hidden reference is based on a faithful DFT reproduction.
