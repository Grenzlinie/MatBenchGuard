# DFT prediction of vacancy-induced magnetism in SrTiO3

## Problem background
Non-magnetic insulating perovskites can potentially become magnetic when structural defects are present. This task investigates whether single-atom vacancies in different sublattices of cubic SrTiO3—removing one oxygen, one titanium, or one strontium atom from a 40-atom supercell—induce a net magnetic moment and, in the case of the oxygen vacancy, whether the spin-polarized state is energetically more favorable than the non-spin-polarized state. Determining these quantities helps assess the viability of vacancy-driven magnetism in such materials.

## Approach
The reproduction uses spin-polarized density functional theory (DFT) within the generalized gradient approximation (GGA) of Perdew, Burke, and Ernzerhof (PBE) to compute the electronic structure of defective supercells. For each defect type (O, Ti, Sr vacancy), a 40-atom supercell is constructed from the known cubic perovskite structure and a single atom is removed. After a geometry optimization, a spin-polarized self-consistent field (SCF) calculation yields the total magnetic moment per supercell. For the oxygen vacancy, an additional non-spin-polarized SCF calculation is performed at the same relaxed geometry to obtain the energy difference between the magnetic and non-magnetic solutions. All calculations can be carried out with an open-source plane-wave pseudopotential code such as Quantum ESPRESSO and standard PBE pseudopotentials.

## Reproduction target
Produce three comma-separated value (CSV) files under `/app/outputs` with the following contents:

1. `o_vacancy_magnetic_moments.csv`: columns `system` (string), `total_magnetic_moment_muB` (float), `energy_difference_sp_vs_nonsp_eV` (float). This file records the total magnetic moment per supercell (in µB) for the 40-atom supercell with one oxygen vacancy (SrTiO2.875) and the energy difference (in eV) between the spin-polarized and non-spin-polarized states.
2. `ti_vacancy_magnetic_moment.csv`: columns `system` (string), `total_magnetic_moment_muB` (float). Total magnetic moment per supercell for the 40-atom supercell with one titanium vacancy (SrTi0.875O3).
3. `sr_vacancy_magnetic_moment.csv`: columns `system` (string), `total_magnetic_moment_muB` (float). Total magnetic moment per supercell for the 40-atom supercell with one strontium vacancy (Sr0.875TiO3).

The `system` column may contain a descriptive identifier. The magnetic moments should be obtained from the output of the spin-polarized DFT calculations; the energy difference for the oxygen vacancy case must be computed from the total energies of the two SCF runs.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP PBE pseudopotentials: https://materialscloud.org/sssp/
- SrTiO3 cubic perovskite crystal structure: https://next-gen.materialsproject.org/materials/mp-4651

## Workflow steps

### Step 1: Supercell construction
- Role: process
- Action: Construct 40-atom supercells of pristine cubic SrTiO3 from public crystal data, then create defect supercells by removing one O, Ti, or Sr atom to obtain SrTiO2.875, SrTi0.875O3, and Sr0.875TiO3.
- Evidence: none

### Step 2: DFT calculations for oxygen-vacancy system
- Role: process
- Action: Perform geometry optimization and spin-polarized SCF calculation for the O-vacancy supercell (SrTiO2.875). Additionally, run a non-spin-polarized SCF calculation with the same relaxed geometry. Extract total energies of both spin configurations and the total magnetic moment of the spin-polarized result.
- Evidence: none

### Step 3: DFT calculation for titanium-vacancy system
- Role: process
- Action: Perform geometry optimization and spin-polarized SCF calculation for the Ti-vacancy supercell (SrTi0.875O3). Extract the total magnetic moment.
- Evidence: none

### Step 4: DFT calculation for strontium-vacancy system
- Role: process
- Action: Perform geometry optimization and spin-polarized SCF calculation for the Sr-vacancy supercell (Sr0.875TiO3). Extract the total magnetic moment.
- Evidence: none

### Step 5: Write O-vacancy magnetic moments CSV
- Role: scored (load-bearing)
- Action: From the O-vacancy calculations, write a CSV with system identifier, total magnetic moment per supercell (μB), and the energy difference between spin-polarized and non-spin-polarized states (eV).
- Output file: `/app/outputs/o_vacancy_magnetic_moments.csv`
- Format: csv
- Contract: columns: system (str), total_magnetic_moment_muB (float), energy_difference_sp_vs_nonsp_eV (float)
- Scoring: scored by hidden verifier

### Step 6: Write Ti-vacancy magnetic moment CSV
- Role: scored
- Action: From the Ti-vacancy calculation, write a CSV with system identifier and total magnetic moment per supercell (μB).
- Output file: `/app/outputs/ti_vacancy_magnetic_moment.csv`
- Format: csv
- Contract: columns: system (str), total_magnetic_moment_muB (float)
- Scoring: scored by hidden verifier

### Step 7: Write Sr-vacancy magnetic moment CSV
- Role: scored
- Action: From the Sr-vacancy calculation, write a CSV with system identifier and total magnetic moment per supercell (μB).
- Output file: `/app/outputs/sr_vacancy_magnetic_moment.csv`
- Format: csv
- Contract: columns: system (str), total_magnetic_moment_muB (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/o_vacancy_magnetic_moments.csv`
- `/app/outputs/ti_vacancy_magnetic_moment.csv`
- `/app/outputs/sr_vacancy_magnetic_moment.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### o_vacancy_magnetic_moments.csv
- path: `/app/outputs/o_vacancy_magnetic_moments.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total magnetic moment and stability energy difference for the oxygen-vacancy supercell.
- schema:
  - `type`: table
  - `required_columns`: `system`, `total_magnetic_moment_muB`, `energy_difference_sp_vs_nonsp_eV`
  - `units`:
    - `total_magnetic_moment_muB`: μB
    - `energy_difference_sp_vs_nonsp_eV`: eV

### ti_vacancy_magnetic_moment.csv
- path: `/app/outputs/ti_vacancy_magnetic_moment.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total magnetic moment for the titanium-vacancy supercell.
- schema:
  - `type`: table
  - `required_columns`: `system`, `total_magnetic_moment_muB`
  - `units`:
    - `total_magnetic_moment_muB`: μB

### sr_vacancy_magnetic_moment.csv
- path: `/app/outputs/sr_vacancy_magnetic_moment.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total magnetic moment for the strontium-vacancy supercell.
- schema:
  - `type`: table
  - `required_columns`: `system`, `total_magnetic_moment_muB`
  - `units`:
    - `total_magnetic_moment_muB`: μB

Notes: Scoring is by comparison of the reported scalar values to hidden paper gold within prescribed tolerances. The Sr-vacancy case is additionally checked for a negligibly small magnetic moment to confirm the non-magnetic state.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "o_vacancy_magnetic_moments.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "total_magnetic_moment_muB",
          "energy_difference_sp_vs_nonsp_eV"
        ],
        "units": {
          "total_magnetic_moment_muB": "μB",
          "energy_difference_sp_vs_nonsp_eV": "eV"
        }
      },
      "description": "Total magnetic moment and stability energy difference for the oxygen-vacancy supercell."
    },
    {
      "file": "ti_vacancy_magnetic_moment.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "total_magnetic_moment_muB"
        ],
        "units": {
          "total_magnetic_moment_muB": "μB"
        }
      },
      "description": "Total magnetic moment for the titanium-vacancy supercell."
    },
    {
      "file": "sr_vacancy_magnetic_moment.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "total_magnetic_moment_muB"
        ],
        "units": {
          "total_magnetic_moment_muB": "μB"
        }
      },
      "description": "Total magnetic moment for the strontium-vacancy supercell."
    }
  ],
  "notes": "Scoring is by comparison of the reported scalar values to hidden paper gold within prescribed tolerances. The Sr-vacancy case is additionally checked for a negligibly small magnetic moment to confirm the non-magnetic state."
}
```

## How you are scored
A hidden verifier independently checks each of the three CSV artifacts. It reads the scalar values you report to a reference benchmark derived from the original investigation, using appropriate tolerances that account for the expected spread from different DFT implementations while requiring genuine computation. The final reward is a weighted average of the per‑artifact scores. To obtain a high score you must follow the DFT workflow as described; simply guessing or copying assumed “correct” numbers is unlikely to match the undisclosed tolerances. The verifier does not run any DFT calculations—it only compares your final reported values—so careful extraction of the magnetic moments and energy difference from your simulation outputs is essential.
