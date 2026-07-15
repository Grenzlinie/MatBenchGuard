# DFT and MD study of CO2 adsorption on defective graphene

## Problem background
Defects in graphene—such as nitrogen substitution and carbon vacancies—modify the electronic structure of the two-dimensional sheet and can alter its ability to adsorb CO₂ molecules. Understanding how each defect type changes the binding strength, the nature of charge transfer (doping), and the structural stability of the adsorbed system at room temperature is essential for evaluating graphene as a metal-free electrode for CO₂ capture and conversion. This task computes, for pristine graphene and three defective variants (graphitic‑N, pyridinic‑N, and a single vacancy), the adsorption energetics, the Fermi‑level shift relative to the Dirac point, and the time‑dependent structural response from ab initio molecular dynamics. The goal is to determine which defect yields the most stable adsorption while preserving the planar geometry of the sheet.

## Approach
We simulate four 6×6 graphene supercells: pristine, graphitic‑N (one carbon replaced by nitrogen), pyridinic‑N (one carbon removed and one replaced by nitrogen), and a single‑vacancy (one carbon removed). All calculations use dispersion‑corrected DFT (PBE‑D3) with a plane‑wave basis, as implemented in Quantum ESPRESSO. First, the bare defective sheets are relaxed and their electronic structure is computed to extract the Fermi level and the Dirac point (the latter from pristine graphene), from which the shift D – E_F (in eV) and the doping type (n‑type or p‑type) are determined. An isolated CO₂ reference energy is obtained in a large periodic box. CO₂ is then placed on each relaxed defective sheet in various initial sites and orientations; the combined systems are relaxed to locate the ground‑state adsorption geometry. From the relaxed total energies, the adsorption energy E_ads and binding energy E_bin are calculated, together with the final CO₂–surface distance. Next, starting from the optimized adsorbed geometry, ab initio molecular dynamics is run in the microcanonical ensemble with an initial temperature of 300 K for 0.8 ps. The trajectories are analysed to produce two stability measures: the root‑mean‑square deviation (RMSD) of all atomic positions versus time, and the absolute z‑displacement D(t) of a chosen reference atom (the nitrogen atom for graphitic‑N and pyridinic‑N, a carbon near the vacancy for the vacancy system, and the central carbon closest to CO₂ for pristine graphene). The four systems are compared to assess which one remains the most rigid and preserves the two‑dimensional structure under thermal motion.

## Reproduction target
For each of the four systems—pristine graphene, graphitic‑N, pyridinic‑N, and vacancy graphene—compute and report in a JSON file: system name, adsorption energy (kcal/mol), binding energy (kcal/mol), final CO₂–graphene distance (Å), the shift D – E_F (eV) from the bare electronic structure, and the doping type (‘n‑type’ or ‘p‑type’). Additionally, from the molecular dynamics trajectories, output two CSV files: one with the RMSD of all atomic positions at each saved time step (columns: system, timestep_fs, rmsd_angstrom), and another with the defect displacement D(t) at the same time points (columns: system, timestep_fs, displacement_angstrom). The results must be written to the paths specified in the workflow steps.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- C pseudopotential (PBE): https://www.quantum-espresso.org/
- N pseudopotential (PBE): https://www.quantum-espresso.org/
- O pseudopotential (PBE): https://www.quantum-espresso.org/

## Workflow steps

### Step 1: Build defective graphene supercells
- Role: process
- Action: Construct 6×6 graphene supercells for pristine graphene, graphitic-N (one C replaced by N), pyridinic-N (one C removed + one C replaced by N), and a single-vacancy (one C removed).
- Evidence: none

### Step 2: Isolated CO2 energy reference
- Role: process
- Action: Run a periodic DFT calculation (PBE-D3, same k-grid and cutoffs as later adsorption calculations) for an isolated CO2 molecule in a large enough cell to obtain its total energy E_CO2.
- Evidence: none

### Step 3: Optimize bare defective graphene
- Role: process
- Action: Perform DFT geometry optimization (PBE-D3) on the bare defective graphene supercells from step_0. Store the relaxed structures and total energies.
- Evidence: none

### Step 4: Electronic structure of bare systems (Fermi level shift)
- Role: process
- Action: Perform single-point SCF calculations on the optimized bare structures from step_2 and compute the local density of states. Extract the Dirac point (for pristine) and the Fermi level for each defective system; record D – EF (eV) for each defective graphene.
- Evidence: none

### Step 5: Optimize CO2 adsorption geometries
- Role: process
- Action: Place CO2 at various initial sites/orientations on each defective graphene from step_2 and relax the combined systems. Keep the ground-state adsorption configuration and its total energy for each system.
- Evidence: none

### Step 6: Adsorption energy and doping summary
- Role: scored
- Action: From the energies of step_4, step_2 and step_1 compute Eads and Ebin (Eq. 1) and the final CO2-graphene distance. Together with the D – EF values from step_3, compile a JSON summary for all four systems.
- Output file: `/app/outputs/adsorption_summary.json`
- Format: json
- Contract: [{"system_name": "str", "adsorption_energy_kcal_mol": float, "binding_energy_kcal_mol": float, "distance_angstrom": float, "D_minus_EF_eV": float, "doping_type": "str"}]
- Scoring: scored by hidden verifier

### Step 7: Ab initio molecular dynamics at 300 K
- Role: process
- Action: Starting from the optimized adsorption geometries of step_4, run Verlet AIMD (microcanonical, initial T=300 K, total simulation time 0.8 ps) using Quantum ESPRESSO. Save the trajectory.
- Evidence: none

### Step 8: RMSD analysis from MD
- Role: scored (load-bearing)
- Action: From the MD trajectories of step_6, compute the root-mean-square deviation of all atomic positions at each saved time step and write a CSV.
- Output file: `/app/outputs/md_rmsd.csv`
- Format: csv
- Contract: columns: system (str), timestep_fs (float), rmsd_angstrom (float).
- Scoring: scored by hidden verifier

### Step 9: Defect displacement D(t) from MD
- Role: scored (load-bearing)
- Action: From the MD trajectories, compute the absolute z-displacement of the chosen defect atom: D(t)=|z(t=0)−z(t)|. For graphitic-N and pyridinic-N use the N atom; for the vacancy system use a carbon atom near the vacancy; for pristine use a central carbon atom close to CO2. Output a CSV.
- Output file: `/app/outputs/md_defect_displacement.csv`
- Format: csv
- Contract: columns: system (str), timestep_fs (float), displacement_angstrom (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/adsorption_summary.json`
- `/app/outputs/md_rmsd.csv`
- `/app/outputs/md_defect_displacement.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### adsorption_summary.json
- path: `/app/outputs/adsorption_summary.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Summary of adsorption energies, binding energies, CO2-graphene distances, Fermi level shift, and doping type for pristine graphene, graphitic-N, pyridinic-N, and vacancy graphene.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `required`: `system_name`, `adsorption_energy_kcal_mol`, `binding_energy_kcal_mol`, `distance_angstrom`, `D_minus_EF_eV`, `doping_type`
    - `properties`:
      - `system_name`:
        - `type`: string
      - `adsorption_energy_kcal_mol`:
        - `type`: number
        - `units`: kcal/mol
      - `binding_energy_kcal_mol`:
        - `type`: number
        - `units`: kcal/mol
      - `distance_angstrom`:
        - `type`: number
        - `units`: angstrom
      - `D_minus_EF_eV`:
        - `type`: number
        - `units`: eV
      - `doping_type`:
        - `type`: string
        - `enum`: `n-type`, `p-type`

### md_rmsd.csv
- path: `/app/outputs/md_rmsd.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Root-mean-square deviation of atomic positions over the MD trajectory for each system.
- schema:
  - `type`: table
  - `required_columns`: `system`, `timestep_fs`, `rmsd_angstrom`
  - `units`:
    - `timestep_fs`: fs
    - `rmsd_angstrom`: angstrom

### md_defect_displacement.csv
- path: `/app/outputs/md_defect_displacement.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: z-displacement D(t) of the defect atom for each system during MD, used to verify structural stability.
- schema:
  - `type`: table
  - `required_columns`: `system`, `timestep_fs`, `displacement_angstrom`
  - `units`:
    - `timestep_fs`: fs
    - `displacement_angstrom`: angstrom

Notes: Scoring is result-level comparison (T0) against hidden paper reference values and ordering requirements. No raw total energies or intermediate files are scored; only the three listed artifacts.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "adsorption_summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "required": [
            "system_name",
            "adsorption_energy_kcal_mol",
            "binding_energy_kcal_mol",
            "distance_angstrom",
            "D_minus_EF_eV",
            "doping_type"
          ],
          "properties": {
            "system_name": {
              "type": "string"
            },
            "adsorption_energy_kcal_mol": {
              "type": "number",
              "units": "kcal/mol"
            },
            "binding_energy_kcal_mol": {
              "type": "number",
              "units": "kcal/mol"
            },
            "distance_angstrom": {
              "type": "number",
              "units": "angstrom"
            },
            "D_minus_EF_eV": {
              "type": "number",
              "units": "eV"
            },
            "doping_type": {
              "type": "string",
              "enum": [
                "n-type",
                "p-type"
              ]
            }
          }
        }
      },
      "description": "Summary of adsorption energies, binding energies, CO2-graphene distances, Fermi level shift, and doping type for pristine graphene, graphitic-N, pyridinic-N, and vacancy graphene."
    },
    {
      "file": "md_rmsd.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "timestep_fs",
          "rmsd_angstrom"
        ],
        "units": {
          "timestep_fs": "fs",
          "rmsd_angstrom": "angstrom"
        }
      },
      "description": "Root-mean-square deviation of atomic positions over the MD trajectory for each system."
    },
    {
      "file": "md_defect_displacement.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "timestep_fs",
          "displacement_angstrom"
        ],
        "units": {
          "timestep_fs": "fs",
          "displacement_angstrom": "angstrom"
        }
      },
      "description": "z-displacement D(t) of the defect atom for each system during MD, used to verify structural stability."
    }
  ],
  "notes": "Scoring is result-level comparison (T0) against hidden paper reference values and ordering requirements. No raw total energies or intermediate files are scored; only the three listed artifacts."
}
```

## How you are scored
A hidden verifier will independently examine each scored output artifact. For adsorption_summary.json, it will check that the reported energies, distances, and D – E_F values are physically consistent and fall within reference ranges derived from the published computational study, and that the doping types are correctly identified. For the MD CSVs, the verifier will extract the time‑series data and evaluate structural ordering: it will compare the mean defect displacement over the later part of the trajectory and the RMSD magnitudes across the four systems to determine whether the expected stability ranking is reproduced. The verifier does not rely on a single self‑reported number; it may recompute derived quantities or cross‑check trends. The final reward is the weighted sum of the scores from each stage.
