# Molecular Dynamics Study of Elastic Modulus from Thermal Fluctuations

## Problem background
The Young’s modulus of graphene is a key mechanical property that governs its performance in nanomechanical and electronic devices. While experiments have measured the modulus by applying external strain, a complementary approach observes the intrinsic thermal out-of-plane vibrations of a free-standing graphene sheet and extracts the modulus from the vibration amplitude using continuum plate theory. Molecular dynamics (MD) simulations can “observe” these thermal fluctuations under controlled conditions, enabling systematic studies of how the modulus depends on sample size, temperature, and isotopic disorder without needing to apply artificial strain. This task recreates that computational experiment.

## Approach
The central idea is to simulate a square graphene sheet with fixed left and right edge columns and periodic boundary conditions in the perpendicular (y) direction, using classical molecular dynamics with the second-generation Brenner (AIREBO) interatomic potential. During the simulation, the out-of-plane (z) displacements of all free carbon atoms are recorded after thermal equilibration. From these trajectories the spatial and temporal average of the squared displacement, ⟨σ²⟩, is computed. Young’s modulus Y is then obtained from the continuum-plate relation

Y = 0.3 × (S / h³) × (k_B T / ⟨σ²⟩)

where S = L² is the sheet area, h = 3.35 Å is the assumed thickness, and k_B = 1.380649×10⁻²³ J/K. No external strain is applied.

To study the influences, the computation is repeated for a systematic family of conditions:
- size series: square side lengths L = 10, 20, 40, 80 Å at T = 300 K,
- temperature series: L = 40 Å at T = 100, 300, 500 K,
- isotopic disorder series: L = 40 Å, T = 300 K, with 0%, 5%, 10%, 20% of ¹²C atoms randomly replaced by ¹⁴C.

Each condition is simulated 100 independent times with different initial velocity seeds, and the per-run Y values are averaged to yield the final reported modulus. The workflow executes this procedure and writes the averaged results to a CSV file for verification.

## Reproduction target
Produce a CSV file, `youngs_modulus_results.csv`, containing the average Young’s modulus (in TPa) for the following eleven distinct conditions, all computed via MD with the AIREBO potential and the continuum-plate formula:

- Size dependence: L = 10, 20, 40, 80 Å (T = 300 K, 0% disorder)
- Temperature dependence: L = 40 Å, T = 100, 300, 500 K (0% disorder)
- Isotopic disorder dependence: L = 40 Å, T = 300 K, with 0%, 5%, 10%, 20% ¹⁴C substitution

The file must have exactly two columns, `Condition` and `Youngs_modulus_TPa`. Each row is one condition; the `Condition` field is a string that identifies the combination (e.g., “L=40_T=300_D0”), and `Youngs_modulus_TPa` is a floating-point number. The results are obtained by averaging 100 independent MD runs per condition. The output will be checked against concealed reference data and required structural dependencies.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/download.html
- Second-generation Brenner interatomic potential (AIREBO): LAMMPS

## Workflow steps

### Step 1: Prepare graphene samples
- Role: process
- Action: Generate initial atomic coordinates for square graphene sheets of side lengths L = 10, 20, 40, 80 Å (C–C bond length 1.42 Å) with fixed boundary conditions on left and right edge columns and periodic boundary in y. For isotopic disorder conditions (0%, 5%, 10%, 20% ¹⁴C), randomly substitute the required fraction of ¹²C atoms with ¹⁴C in the initial structure. Produce LAMMPS data files.
- Evidence: none

### Step 2: Run MD simulations and compute per-run Young's modulus
- Role: process
- Action: For each condition (size L, temperature T, isotopic disorder), run 100 independent LAMMPS simulations using pair_style airebo, with time step 0.5 fs, 5e5 equilibration and 5e5 production steps. Extract the thermal mean-square vibration amplitude ⟨σ²⟩ from the z-coordinate trajectories of free atoms, then compute Young's modulus Y per run using the continuum-plate formula Y = 0.3×(S/h³)×(k_B T/⟨σ²⟩) with h = 3.35 Å, S = L², and k_B = 1.380649e-23 J/K. Collect all per-run Y values in a structured evidence file.
- Evidence: `/app/outputs/per_run_Y.json`

### Step 3: Final averaged Young's modulus
- Role: scored (load-bearing)
- Action: From the per-run data generated in step_02, average the 100 Y values for each condition and write the results to youngs_modulus_results.csv.
- Output file: `/app/outputs/youngs_modulus_results.csv`
- Format: csv
- Contract: CSV with header: Condition,Youngs_modulus_TPa. Contains 11 rows corresponding to the 11 required conditions: size series (L=10,20,40,80 at T=300 K, 0% disorder), temperature series (L=40 Å at T=100,300,500 K, 0% disorder), and disorder series (L=40 Å, T=300 K, disorder 0%,5%,10%,20%). Condition is a string; Youngs_modulus_TPa is a float.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/youngs_modulus_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### youngs_modulus_results.csv
- path: `/app/outputs/youngs_modulus_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The final averaged Young's modulus values for all 11 conditions. The hidden checker compares these values to paper-reported gold references and enforces required trends.
- schema:
  - `type`: table
  - `required_columns`: `Condition`, `Youngs_modulus_TPa`
  - `row_count`: 11
  - `description`: Each row is a condition identifier and its average Young's modulus in TPa.

Notes: The evidence file per_run_Y.json is not scored; it is only for documentation of the simulation work. The agent must run all MD simulations for the 11 conditions (size, temperature, disorder) as described in the steps.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "youngs_modulus_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Condition",
          "Youngs_modulus_TPa"
        ],
        "row_count": 11,
        "description": "Each row is a condition identifier and its average Young's modulus in TPa."
      },
      "description": "The final averaged Young's modulus values for all 11 conditions. The hidden checker compares these values to paper-reported gold references and enforces required trends."
    }
  ],
  "notes": "The evidence file per_run_Y.json is not scored; it is only for documentation of the simulation work. The agent must run all MD simulations for the 11 conditions (size, temperature, disorder) as described in the steps."
}
```

## How you are scored
A hidden automated verifier reads the files you write under `/app/outputs`. Each scored artifact (`youngs_modulus_results.csv`) is evaluated by comparing its contents against concealed reference values and by verifying that the results exhibit the qualitative physical dependencies expected for the material. The final reward is a weighted combination of the scores from all scored stages. Submitting numbers copied from a paper or other external source without actually running the prescribed molecular dynamics simulations will not earn credit; the verifier expects artifacts that are the genuine output of the specified workflow.
