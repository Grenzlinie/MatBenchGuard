# DFT calculations of point defect energetics in graphite

## Problem background
In graphite used for nuclear moderation and carbon nanostructures, high-energy irradiation knocks carbon atoms from the lattice, creating self-interstitial and vacancy defects. The structure and energetics of these defects govern the evolution of radiation damage, including the storage and subsequent release of Wigner energy, changes in physical properties, and interactions with dislocations. Interstitial atoms and vacancies can form bridging structures between the widely separated graphitic layers, a behavior that challenges the conventional picture of planar defects. A central goal is to understand which defect configurations are stable, how stacking-fault shear influences their formation, and what barriers control defect recombination. This task computes the formation energies, stacking fault energies, and barrier heights for a set of candidate defect structures that are believed to dominate the behavior in irradiated graphite.

## Approach
The workflow uses first-principles density functional theory (DFT) within a supercell approach. All calculations are performed with the open-source CP2K code using GTH pseudopotentials. A 4×4×1 supercell of AB-stacked hexagonal graphite (lattice parameters a = 2.46 Å, c = 6.70 Å) serves as the reference system. Defect formation energies are obtained from total energy differences: for interstitials, E_formation = E_defect − E_perfect_AB − μ_C, where μ_C is the chemical potential per carbon atom computed from the perfect cell; for vacancies, E_formation = E_defect − E_perfect_AB + n μ_C. The following defect configurations are constructed and relaxed: (i) a grafted two-bond interstitial in perfect unsheared graphite; (ii) a spiro fourfold interstitial created by shifting one layer towards ABC stacking; (iii) a threefold interstitial created by shifting towards AA stacking. The stacking fault energies of the sheared perfect cells (ABC-like and AA-like) are also computed. Two interlayer divacancies—V2^1(ββ) and V2^2(ββ)—are formed by placing vacancies in adjacent layers at specific sites. Finally, the break-up barrier of an intimate Frenkel pair (an interstitial adjacent to a vacancy in the neighboring layer) is obtained from a nudged elastic band (NEB) calculation between the bound pair and a separated state. The shear-conferred stabilization energy for each sheared interstitial is derived by combining its formation energy with the corresponding stacking fault energy. Each total-energy calculation involves full geometry relaxation; the NEB pathway uses multiple intermediate images.

## Reproduction target
Compute and report the following quantities in properly formatted CSV files:

1. The formation energies (in eV) of the grafted, spiro, and threefold interstitial defects.
2. The stacking fault energies (in meV/Å²) for the threefold (AA-type) and fourfold (ABC-type) shear directions.
3. The break-up barrier (in eV) of the intimate Frenkel pair.
4. The formation energies (in eV) of the interlayer divacancies V2^1(ββ) and V2^2(ββ).
5. The shear-conferred stabilization energies (in eV) for the threefold and spiro interstitials, computed from the results above.

All numerical values are obtained from the DFT total energies of the relaxed supercells. The required output files and column schemas are listed in the Workflow steps.

## Assets

- CP2K (open-source DFT code): https://www.cp2k.org/
- GTH pseudopotentials for CP2K: https://www.cp2k.org/pseudopotentials
- Graphite crystal structure: https://materialsproject.org/materials/mp-48/

## Workflow steps

### Step 1: Generate initial supercell structures
- Role: process
- Action: Create 4x4x1 AB-stacked graphite supercells for the perfect unsheared cell, perfect sheared cells (ABC-like and AA-like shifts of 0.71 Å), and defect configurations: grafted interstitial (unsheared), spiro interstitial (ABC-sheared), threefold interstitial (AA-sheared), V2^1(ββ) and V2^2(ββ) divacancies, the intimate Frenkel pair (interstitial adjacent to a vacancy in adjacent layers), and a separated interstitial+vacancy pair. Write the coordinate files for subsequent DFT steps.
- Evidence: none

### Step 2: Compute perfect unsheared reference energy
- Role: process
- Action: Run DFT relaxation of the perfect AB-stacked supercell to obtain the total energy E_perfect_AB and the number of atoms N. This energy serves as the reference for formation energy calculations.
- Evidence: `/app/outputs/reference_energy.txt`

### Step 3: Compute stacking fault energies
- Role: scored
- Action: Perform DFT relaxation of defect-free sheared supercells (ABC-like and AA-like) to obtain total energies E_perfect_ABC and E_perfect_AA. Compute stacking fault energies γ(3) = (E_perfect_ABC - E_perfect_AB) / A and γ(4) = (E_perfect_AA - E_perfect_AB) / A, where A = 82.64 Å².
- Output file: `/app/outputs/step_02_stack_fault_energies.csv`
- Format: csv
- Contract: columns: stacking_type (string, one of 'threefold (AA-type)', 'fourfold (ABC-type)'), energy_meV_per_Ang2 (float)
- Scoring: scored by hidden verifier

### Step 4: Compute interstitial formation energies
- Role: scored
- Action: Perform DFT relaxation of interstitial-containing supercells: (i) grafted two-bond interstitial in the unsheared AB cell, (ii) spiro interstitial in the ABC-sheared cell, (iii) threefold interstitial in the AA-sheared cell. Compute formation energies Ei = E(defect) - E_perfect_AB - μ_C, where μ_C = E_perfect_AB / N.
- Output file: `/app/outputs/step_01_interstitial_energies.csv`
- Format: csv
- Contract: columns: defect_name (string, one of 'grafted', 'spiro', 'threefold'), formation_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 5: Compute interlayer divacancy formation energies
- Role: scored
- Action: Perform DFT relaxation of the V2^1(ββ) and V2^2(ββ) supercells. Compute formation energies Ef = E(defect) - E_perfect_AB + 2μ_C.
- Output file: `/app/outputs/step_04_divacancy_energies.csv`
- Format: csv
- Contract: columns: defect_name (string, one of 'V2^1(beta beta)', 'V2^2(beta beta)'), formation_energy_eV (float)
- Scoring: scored by hidden verifier

### Step 6: Compute intimate Frenkel pair break-up barrier
- Role: scored
- Action: Construct the intimate Frenkel pair structure and a separated state. Perform a nudged elastic band (NEB) calculation to locate the minimum energy path and transition state. Report the energy barrier as the difference between the transition state energy and the intimate pair energy.
- Output file: `/app/outputs/step_03_intimate_frenkel_barrier.csv`
- Format: csv
- Contract: columns: barrier_eV (float)
- Scoring: scored by hidden verifier

### Step 7: Compute shear stabilization energies
- Role: scored
- Action: Using the formation energies from step_interstitials and stacking fault energies from step_stack_fault, compute the shear-conferred stabilization energy for the threefold interstitial: E_stab(3) = (E_grafted - E_threefold) + A * γ(3). Similarly for the spiro interstitial: E_stab(4) = (E_grafted - E_spiro) + A * γ(4).
- Output file: `/app/outputs/step_05_stabilization_energies.csv`
- Format: csv
- Contract: columns: interstitial_type (string, one of 'threefold', 'spiro'), stabilization_energy_eV (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_interstitial_energies.csv`
- `/app/outputs/step_02_stack_fault_energies.csv`
- `/app/outputs/step_03_intimate_frenkel_barrier.csv`
- `/app/outputs/step_04_divacancy_energies.csv`
- `/app/outputs/step_05_stabilization_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_interstitial_energies.csv
- path: `/app/outputs/step_01_interstitial_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation energies of the grafted, spiro, and threefold interstitial configurations.
- schema:
  - `type`: table
  - `required_columns`: `defect_name`, `formation_energy_eV`

### step_02_stack_fault_energies.csv
- path: `/app/outputs/step_02_stack_fault_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Stacking fault energies for the threefold (AA-type) and fourfold (ABC-type) stacking.
- schema:
  - `type`: table
  - `required_columns`: `stacking_type`, `energy_meV_per_Ang2`

### step_03_intimate_frenkel_barrier.csv
- path: `/app/outputs/step_03_intimate_frenkel_barrier.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Energy barrier for break-up of the intimate Frenkel pair.
- schema:
  - `type`: table
  - `required_columns`: `barrier_eV`

### step_04_divacancy_energies.csv
- path: `/app/outputs/step_04_divacancy_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Formation energies of the interlayer divacancies V2^1(ββ) and V2^2(ββ).
- schema:
  - `type`: table
  - `required_columns`: `defect_name`, `formation_energy_eV`

### step_05_stabilization_energies.csv
- path: `/app/outputs/step_05_stabilization_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Shear-conferred stabilization energies for the threefold and spiro interstitials.
- schema:
  - `type`: table
  - `required_columns`: `interstitial_type`, `stabilization_energy_eV`

Notes: All CSV artifacts must contain the required columns. The checker will compare the reported values against hidden reference within tolerances and verify relative ordering (spiro < threefold < grafted; V2^2 < V2^1; stabilization energies positive).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_interstitial_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_name",
          "formation_energy_eV"
        ]
      },
      "description": "Formation energies of the grafted, spiro, and threefold interstitial configurations."
    },
    {
      "file": "step_02_stack_fault_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "stacking_type",
          "energy_meV_per_Ang2"
        ]
      },
      "description": "Stacking fault energies for the threefold (AA-type) and fourfold (ABC-type) stacking."
    },
    {
      "file": "step_03_intimate_frenkel_barrier.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "barrier_eV"
        ]
      },
      "description": "Energy barrier for break-up of the intimate Frenkel pair."
    },
    {
      "file": "step_04_divacancy_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_name",
          "formation_energy_eV"
        ]
      },
      "description": "Formation energies of the interlayer divacancies V2^1(ββ) and V2^2(ββ)."
    },
    {
      "file": "step_05_stabilization_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "interstitial_type",
          "stabilization_energy_eV"
        ]
      },
      "description": "Shear-conferred stabilization energies for the threefold and spiro interstitials."
    }
  ],
  "notes": "All CSV artifacts must contain the required columns. The checker will compare the reported values against hidden reference within tolerances and verify relative ordering (spiro < threefold < grafted; V2^2 < V2^1; stabilization energies positive)."
}
```

## How you are scored
Each scored artifact (the five CSV files) is evaluated independently by an automated verifier. The verifier reads the reported numeric values and compares them against hidden reference data using criteria that account for the expected spread between different DFT implementations. In addition to value comparisons, the verifier checks that certain physically expected relative orderings hold (e.g., a sheared interstitial configuration should be more stable than the unsheared grafted interstitial, and one divacancy variant should be lower in energy than the other). The total reward (a number between 0 and 1) is a weighted sum of the per-artifact scores, with the main interstitial and barrier calculations carrying the highest weights. To obtain a high score, you must perform the actual DFT calculations; simply hard-coding expected numbers is unlikely to pass because the tolerance windows are narrow enough to distinguish a genuine computation from a generic guess.
