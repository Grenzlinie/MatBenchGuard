# Lattice Energy Calculation for Crystal Stability

## Problem background
Predicting how para-substituted N,N′-diphenylureas (pDPUs) assemble into crystalline solids requires understanding the interplay between intramolecular o‑H···Ourea contacts, molecular planarity, and the intermolecular interactions that dominate packing (π‑stacking vs. urea hydrogen‑bond ribbons). Electron‑withdrawing substituents at the para position change the electron density at the ortho hydrogens, altering the strength of these contacts and thus the preferred conformation and the resulting crystal structure. This task catalogues those energetic contributions by combining single‑molecule and periodic density functional theory.

## Approach
The computational investigation proceeds in two stages. First, gas‑phase DFT geometry optimizations at the B3LYP‑D2/pob‑TZVP level are performed for six pDPU derivatives: the disubstituted pCyDPU, pCyNDPU, pCF₃DPU, and the monosubstituted pCyHDPU, pNHDPU, pClHDPU. From each optimized geometry, the o‑H···Ourea and o‑H···Hurea distances on the substituted ring(s) and, where appropriate, ring tilt angles are extracted. Second, periodic DFT optimizations using the same functional and basis set are carried out for the corresponding experimental crystal structures (CCDC CIFs listed below), with appropriate k‑point sampling and counterpoise (BSSE) corrections. Lattice, cohesive, strain, and dominant dimer interaction energies are computed from the total energies. The results allow a comparison of how substituent identity — and mono‑ vs. disubstitution — shifts the energetic balance between molecular conformation and crystal packing.

## Reproduction target
Produce two scored CSV tables: (1) single‑molecule distances (o‑H···Ourea, o‑H···Hurea) and ring tilt angles for the six compounds, optionally including the unsubstituted DPU; (2) solid‑state lattice, cohesive, strain, and dimer interaction energies for the same six crystals. The verifier will evaluate whether the o‑H···Ourea distances on the monosubstituted ring follow a monotonic trend consistent with the electron‑withdrawing strength of the substituent (NO₂, CN, Cl) and whether the lattice energies of the disubstituted crystals (pCF₃DPU, pCyNDPU, pCyDPU) exhibit a relative ordering that indicates thermodynamic stability.

## Assets

- Experimental crystal structure CIFs for six pDPU compounds: https://www.ccdc.cam.ac.uk/structures/
- pob-TZVP basis set: https://www.basissetexchange.org/
- Open-source periodic DFT code
- Grimme D2 dispersion correction

## Workflow steps

### Step 1: Single-molecule geometry optimizations
- Role: scored (load-bearing)
- Action: Perform gas-phase DFT geometry optimizations at the B3LYP-D2/pob-TZVP level for six para-substituted DPU molecules (pCyDPU, pCyNDPU, pCF₃DPU, pCyHDPU, pNHDPU, pClHDPU) and optionally for unsubstituted DPU. For each optimized geometry extract interatomic distances o‑H···Ourea and o‑H···Hurea on the substituted ring(s) and, where applicable, ring tilt angles. Write the extracted data to step_01_single_molecule_geometries.csv.
- Output file: `/app/outputs/step_01_single_molecule_geometries.csv`
- Format: csv
- Contract: Columns: compound_id (str), substituent (str; e.g., 'none','CN','NO2','Cl','CF3'), o_H_O_distance_A (float), o_H_H_distance_A (float), ring_tilt_angle_deg (float, optional). Rows for each compound.
- Scoring: scored by hidden verifier

### Step 2: Periodic DFT optimization and energy calculation
- Role: process
- Action: Using the downloaded crystal structure CIFs, perform periodic DFT geometry optimizations (B3LYP-D2/pob-TZVP) for each DPU crystal with appropriate k‑point sampling and BSSE corrections. Compute lattice, cohesive, and strain energies from the total energies using the definitions given in the paper (Equations 1–3). Extract relevant dimers from the optimized crystals and compute dimer interaction energies (Equation 4). Log all intermediate energies for verification.
- Evidence: `/app/outputs/solid_state_calc.log`

### Step 3: Report solid-state energetic contributions
- Role: scored (load-bearing)
- Action: Collect the computed lattice, cohesive, strain, and dimer interaction energies for each crystal structure from the previous step and write them to step_02_solid_state_energies.csv.
- Output file: `/app/outputs/step_02_solid_state_energies.csv`
- Format: csv
- Contract: Columns: compound_id (str), E_lattice_kcal_mol (float), E_cohesive_kcal_mol (float), E_strain_kcal_mol (float), E_dimer_kcal_mol (float). Rows for each of the six compounds.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_single_molecule_geometries.csv`
- `/app/outputs/step_02_solid_state_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_single_molecule_geometries.csv
- path: `/app/outputs/step_01_single_molecule_geometries.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Optimized single‑molecule geometries: interatomic distances and ring tilt angles. The primary scored feature is the monotonic trend of o‑H···Ourea distances on the monosubstituted rings.
- schema:
  - `type`: table
  - `required_columns`: `compound_id`, `substituent`, `o_H_O_distance_A`, `o_H_H_distance_A`, `ring_tilt_angle_deg`
  - `units`:
    - `o_H_O_distance_A`: Ångström
    - `o_H_H_distance_A`: Ångström
    - `ring_tilt_angle_deg`: degree

### step_02_solid_state_energies.csv
- path: `/app/outputs/step_02_solid_state_energies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed solid‑state energetic contributions. The primary scored feature is the ordering of lattice energies among the three disubstituted DPUs.
- schema:
  - `type`: table
  - `required_columns`: `compound_id`, `E_lattice_kcal_mol`, `E_cohesive_kcal_mol`, `E_strain_kcal_mol`, `E_dimer_kcal_mol`
  - `units`:
    - `E_lattice_kcal_mol`: kcal/mol
    - `E_cohesive_kcal_mol`: kcal/mol
    - `E_strain_kcal_mol`: kcal/mol
    - `E_dimer_kcal_mol`: kcal/mol

Notes: The checker verifies structural trends (monotonic ordering of distances and lattice energies) as the main signal. Absolute values are compared to paper‑reported references with appropriate tolerances as a secondary consistency check. The dimer interaction energies are reported for completeness but are not required for the primary scoring trends.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_single_molecule_geometries.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound_id",
          "substituent",
          "o_H_O_distance_A",
          "o_H_H_distance_A",
          "ring_tilt_angle_deg"
        ],
        "units": {
          "o_H_O_distance_A": "Ångström",
          "o_H_H_distance_A": "Ångström",
          "ring_tilt_angle_deg": "degree"
        }
      },
      "description": "Optimized single‑molecule geometries: interatomic distances and ring tilt angles. The primary scored feature is the monotonic trend of o‑H···Ourea distances on the monosubstituted rings."
    },
    {
      "file": "step_02_solid_state_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "compound_id",
          "E_lattice_kcal_mol",
          "E_cohesive_kcal_mol",
          "E_strain_kcal_mol",
          "E_dimer_kcal_mol"
        ],
        "units": {
          "E_lattice_kcal_mol": "kcal/mol",
          "E_cohesive_kcal_mol": "kcal/mol",
          "E_strain_kcal_mol": "kcal/mol",
          "E_dimer_kcal_mol": "kcal/mol"
        }
      },
      "description": "Computed solid‑state energetic contributions. The primary scored feature is the ordering of lattice energies among the three disubstituted DPUs."
    }
  ],
  "notes": "The checker verifies structural trends (monotonic ordering of distances and lattice energies) as the main signal. Absolute values are compared to paper‑reported references with appropriate tolerances as a secondary consistency check. The dimer interaction energies are reported for completeness but are not required for the primary scoring trends."
}
```

## How you are scored
A hidden verifier parses your final CSVs and independently checks the reported quantities. Scoring is based on two structural trends: the ordering of o‑H···Ourea distances among the monosubstituted compounds and the ordering of lattice energies among the disubstituted compounds. In addition, absolute values are compared against a reference dataset with domain‑appropriate tolerances. Each trend contributes approximately half of the total reward. The verifier does not require an exact match with the paper’s numbers, but large deviations that break the expected physical trends will reduce the score.
