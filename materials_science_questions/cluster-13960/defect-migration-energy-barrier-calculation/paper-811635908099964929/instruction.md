# Uranium vacancy migration barriers in UO2 with DFT+NEB

## Problem background
Uranium dioxide (UO2) is the primary fuel in many nuclear reactors. Under irradiation, fission gas evolution and fuel swelling are influenced by the mobility of uranium vacancies. Experiments on radiation‑damaged UO2 indicate a surprisingly low effective uranium migration barrier – around 2.4 eV – yet early theoretical models that consider only isolated single uranium vacancies predict much higher barriers. This discrepancy suggests that vacancy clusters may play a critical role in uranium transport. Understanding which defect configurations enable fast uranium migration is essential for predicting fuel performance.

## Approach
Density functional theory (DFT) calculations within a plane‑wave framework (Quantum ESPRESSO) are used to determine the energy landscape for uranium vacancy hopping. A 2×2×3 supercell of fluorite UO2 is constructed with antiferromagnetic spin ordering. Five distinct defect configurations are introduced: a single uranium vacancy (V_U), a uranium‑oxygen divacancy (V_UO), a uranium‑di‑oxygen trivacancy (V_UO2), a pair of nearest‑neighbour uranium vacancies (V_U2), and a V_U2O cluster (two uranium vacancies plus one oxygen vacancy). After relaxing each structure with DFT+U (LDA+U or GGA+U, with pseudopotentials appropriate for U and O), the minimum‑energy path for vacancy migration is computed using the climbing‑image nudged elastic band (CI‑NEB) method with a small number of intermediate images. The calculation reveals how the presence of additional vacancies, particularly multiple uranium vacancies, can alter the migration barrier compared with an isolated single vacancy.

## Reproduction target
For each of the five defect types (V_U, V_UO, V_UO2, V_U2, V_U2O), compute the minimum‑energy migration barrier in electron‑volts (eV) using the CI‑NEB procedure. Write the results to a CSV file named `migration_barriers.csv` with columns `defect_type` (string) and `barrier_eV` (float). The CSV must contain exactly five rows, one for each defect type. The goal is to produce a set of barriers that reflect the physical effect of vacancy clustering on uranium mobility – specifically, to determine whether certain vacancy clusters can yield migration barriers substantially lower than the single‑vacancy value and close to the experimental U migration barrier observed in damaged UO2 (~2.4 eV).

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Pseudopotentials for U and O: SSSP Efficiency 1.3.2 or PSLibrary 1.0.0
- UO2 crystal structure

## Workflow steps

### Step 1: Prepare UO2 defect supercells
- Role: process
- Action: Set up a 2×2×3 supercell of fluorite UO2 with antiferromagnetic ordering. Create initial and final atomic configurations for five defect types: (1) single uranium vacancy V_U, (2) divacancy V_UO, (3) trivacancy V_UO2 with O vacancies in linear [111] orientation, (4) di-uranium vacancy V_U2 (two nearest-neighbor U vacancies), and (5) V_U2O cluster (two nearest-neighbor U vacancies plus one O vacancy). Relax all structures using DFT (LDA+U or GGA+U; pseudopotentials suitable for U and O) to obtain relaxed positions for the NEB endpoints. Document the supercell setup and relaxation convergence in a log file.
- Evidence: `/app/outputs/supercell_relaxation.log`

### Step 2: Compute migration barriers with CI-NEB
- Role: scored (load-bearing)
- Action: For each of the five defect types (V_U, V_UO, V_UO2, V_U2, V_U2O) use the climbing-image nudged elastic band (CI-NEB) method with 3-4 intermediate images to calculate the minimum-energy path between the relaxed initial and final states. Extract the migration barrier (energy difference between saddle point and initial state) in eV.
- Output file: `/app/outputs/migration_barriers.csv`
- Format: csv
- Contract: Columns: defect_type (string, one of V_U, V_UO, V_UO2, V_U2, V_U2O), barrier_eV (float). Five rows, one per defect type.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/migration_barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### migration_barriers.csv
- path: `/app/outputs/migration_barriers.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed minimum-energy migration barriers for five U vacancy defect types in UO2 (V_U, V_UO, V_UO2, V_U2, V_U2O), obtained from DFT+CI-NEB calculations. The checker verifies that all five defect types are present, the barrier values follow the expected relative ordering, and the V_U2 and V_U2O barriers are close to the experimental U migration barrier of approximately 2.4 eV.
- schema:
  - `type`: table
  - `required_columns`: `defect_type`, `barrier_eV`
  - `units`:
    - `barrier_eV`: eV

Notes: The QE environment and pseudopotentials are not prescribed; the agent may choose a suitable LDA+U or GGA+U setup. The scoring does not require exact match with any specific reference barrier but checks the physical trends (barrier hierarchy and approximate magnitude of the low-barrier clusters).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "migration_barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect_type",
          "barrier_eV"
        ],
        "units": {
          "barrier_eV": "eV"
        }
      },
      "description": "Computed minimum-energy migration barriers for five U vacancy defect types in UO2 (V_U, V_UO, V_UO2, V_U2, V_U2O), obtained from DFT+CI-NEB calculations. The checker verifies that all five defect types are present, the barrier values follow the expected relative ordering, and the V_U2 and V_U2O barriers are close to the experimental U migration barrier of approximately 2.4 eV."
    }
  ],
  "notes": "The QE environment and pseudopotentials are not prescribed; the agent may choose a suitable LDA+U or GGA+U setup. The scoring does not require exact match with any specific reference barrier but checks the physical trends (barrier hierarchy and approximate magnitude of the low-barrier clusters)."
}
```

## How you are scored
Your submission will be evaluated by an automated checker that reads `migration_barriers.csv`. The checker verifies that:

1. Every required defect type (`V_U`, `V_UO`, `V_UO2`, `V_U2`, `V_U2O`) appears exactly once.
2. The barrier values are positive and follow the physically expected hierarchy among the different vacancy clusters (i.e., clusters with more favourable local coordination are generally expected to give lower migration barriers).
3. The computed barriers for the low‑barrier clusters fall within a reasonable range of the experimental U migration barrier (~2.4 eV) reported for radiation‑damaged UO2.

The exact tolerance windows are hidden, but the scoring rewards correct physical trends and realistic magnitudes. No credit is given for merely reproducing the paper’s numbers without performing the DFT+NEB calculations.
