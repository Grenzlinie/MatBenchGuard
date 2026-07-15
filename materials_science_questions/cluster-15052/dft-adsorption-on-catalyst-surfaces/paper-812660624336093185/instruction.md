# DFT Repair of h-BN N Vacancy by NO Molecules

## Problem background
Hexagonal boron nitride (h-BN) monolayer is an insulator, but removal of a nitrogen atom creates a vacancy that introduces metallic states and degrades its electronic properties. A two-step repair process using NO molecules has been proposed to fill the vacancy and restore the perfect monolayer. This task computationally investigates the energetics and charge redistribution of that repair mechanism: the solver must determine the adsorption energies, energy barriers, and Hirshfeld charges for each elementary step of the process.

## Approach
Perform density functional theory (DFT) calculations with an open-source code (CP2K, Quantum ESPRESSO, or GPAW). Use a 4×4×1 supercell of h-BN monolayer, 15 Å of vacuum, and the DFT‑D2 dispersion correction with a DNP‑quality basis set, a Monkhorst‑Pack k‑point mesh of 10×10×1, a global orbital cutoff of 5.0 Å, and a smearing of 0.005 Ha. First, relax the pristine supercell and then the N‑defected supercell. For the **repairing process**, place one NO molecule near the vacancy; optimize the physisorbed initial state (IS1), locate a transition state (TS1), and optimize the final state (FS1) in which the NO’s N atom fills the vacancy while the O atom remains on the surface. For the **removing process**, take FS1 and introduce a second NO molecule; optimize the initial state (IS2), locate a transition state (TS2), and optimize the final state (FS2) where the extra O is removed as NO₂ leaving a repaired h‑BN sheet. For each stationary point, compute the total energy, from which the adsorption energy (E_surf + E_NO − E_surf/NO) and energy barrier (E_TS − E_IS) are derived, and perform Hirshfeld population analysis to obtain atomic charges.

## Reproduction target
Using the DFT setup described above, calculate the stationary points for the repair and removal pathways and report the adsorption energies, energy barriers, and Hirshfeld charges in two comma‑separated CSV files: `repairing_process_results.csv` and `removing_process_results.csv`. The required columns for each file are listed in the workflow steps. The results should characterise the energetics of the repair mechanism and allow an assessment of whether the process is favourable.

## Assets

- Open-source DFT code (CP2K, Quantum ESPRESSO, or GPAW): https://www.cp2k.org, https://www.quantum-espresso.org, https://wiki.fysik.dtu.dk/gpaw

## Workflow steps

### Step 1: Relax pristine and N‑defected h‑BN supercells
- Role: process
- Action: Construct a 4×4×1 h‑BN monolayer supercell with 15 Å vacuum, relax the pristine geometry and then create and relax the N‑defected supercell using DFT‑D2 dispersion correction, a DNP‑quality basis set, and a 10×10×1 k‑point mesh. The relaxed N‑defected structure serves as the starting point for the repair pathway.
- Evidence: `/app/outputs/relaxation_output.log`

### Step 2: Compute repairing process (IS1 → TS1 → FS1)
- Role: scored
- Action: Starting from the relaxed N‑defected h‑BN, adsorb one NO molecule. Perform geometry optimization to obtain physisorbed IS1. Locate the transition state TS1 using LST/QST or NEB and optimize to FS1. For each state compute the total energy and Hirshfeld charges on the N and O atoms. Calculate adsorption energy and energy barrier.
- Output file: `/app/outputs/repairing_process_results.csv`
- Format: csv
- Contract: state (IS1/TS1/FS1), E_ad (eV), barrier (eV; empty for IS1/FS1), Hirshfeld_charge_NO (e), Hirshfeld_charge_N1 (e), Hirshfeld_charge_O1 (e)
- Scoring: scored by hidden verifier

### Step 3: Compute removing process (IS2 → TS2 → FS2)
- Role: scored (load-bearing)
- Action: Using the FS1 configuration (chemisorbed NO with extra O), introduce a second NO molecule. Optimize to obtain physisorbed IS2. Locate the transition state TS2 and optimize to FS2 (desorbed NO₂, repaired h‑BN). For each state compute adsorption/desorption energy, energy barrier, and Hirshfeld charges on all atoms.
- Output file: `/app/outputs/removing_process_results.csv`
- Format: csv
- Contract: state (IS2/TS2/FS2), E_ad (eV), barrier (eV; empty for IS2/FS2), Hirshfeld_charge_NO2_total (e), Hirshfeld_charge_N1 (e), Hirshfeld_charge_O1 (e), Hirshfeld_charge_N2 (e), Hirshfeld_charge_O2 (e)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/repairing_process_results.csv`
- `/app/outputs/removing_process_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### repairing_process_results.csv
- path: `/app/outputs/repairing_process_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies, energy barrier, and Hirshfeld charges for the three stationary points of the repairing process.
- schema:
  - `type`: table
  - `required_columns`: `state`, `E_ad`, `barrier`, `Hirshfeld_charge_NO`, `Hirshfeld_charge_N1`, `Hirshfeld_charge_O1`
  - `units`:
    - `E_ad`: eV
    - `barrier`: eV
    - `Hirshfeld_charge_NO`: e
    - `Hirshfeld_charge_N1`: e
    - `Hirshfeld_charge_O1`: e

### removing_process_results.csv
- path: `/app/outputs/removing_process_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Adsorption energies, energy barrier, and Hirshfeld charges for the three stationary points of the removing process.
- schema:
  - `type`: table
  - `required_columns`: `state`, `E_ad`, `barrier`, `Hirshfeld_charge_NO2_total`, `Hirshfeld_charge_N1`, `Hirshfeld_charge_O1`, `Hirshfeld_charge_N2`, `Hirshfeld_charge_O2`
  - `units`:
    - `E_ad`: eV
    - `barrier`: eV
    - `Hirshfeld_charge_NO2_total`: e
    - `Hirshfeld_charge_N1`: e
    - `Hirshfeld_charge_O1`: e
    - `Hirshfeld_charge_N2`: e
    - `Hirshfeld_charge_O2`: e

Notes: The hidden checker compares each reported value to the paper's gold within appropriate tolerances and verifies relative trends (e.g., strong exothermicity of FS1, barrier(TS1) > barrier(TS2), small desorption energy for FS2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "repairing_process_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "state",
          "E_ad",
          "barrier",
          "Hirshfeld_charge_NO",
          "Hirshfeld_charge_N1",
          "Hirshfeld_charge_O1"
        ],
        "units": {
          "E_ad": "eV",
          "barrier": "eV",
          "Hirshfeld_charge_NO": "e",
          "Hirshfeld_charge_N1": "e",
          "Hirshfeld_charge_O1": "e"
        }
      },
      "description": "Adsorption energies, energy barrier, and Hirshfeld charges for the three stationary points of the repairing process."
    },
    {
      "file": "removing_process_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "state",
          "E_ad",
          "barrier",
          "Hirshfeld_charge_NO2_total",
          "Hirshfeld_charge_N1",
          "Hirshfeld_charge_O1",
          "Hirshfeld_charge_N2",
          "Hirshfeld_charge_O2"
        ],
        "units": {
          "E_ad": "eV",
          "barrier": "eV",
          "Hirshfeld_charge_NO2_total": "e",
          "Hirshfeld_charge_N1": "e",
          "Hirshfeld_charge_O1": "e",
          "Hirshfeld_charge_N2": "e",
          "Hirshfeld_charge_O2": "e"
        }
      },
      "description": "Adsorption energies, energy barrier, and Hirshfeld charges for the three stationary points of the removing process."
    }
  ],
  "notes": "The hidden checker compares each reported value to the paper's gold within appropriate tolerances and verifies relative trends (e.g., strong exothermicity of FS1, barrier(TS1) > barrier(TS2), small desorption energy for FS2)."
}
```

## How you are scored
A hidden verifier reads both CSV files. For each row it compares the reported adsorption energy, barrier, and Hirshfeld charges to reference values derived from the original study, applying tolerances appropriate for DFT‑level spread. In addition, the verifier checks that the relative energies and barriers across the stationary points obey the expected structural trends (e.g., stability ordering between physisorbed and chemisorbed states, relative barrier heights). The final reward is a weighted combination of these per‑value accuracy checks and the structural consistency checks. Numbers that are not obtained from genuine DFT calculations will fail the structural checks because they will not exhibit the required internal consistency.
