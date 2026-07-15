# RHF/3-21G Activation Parameter Differences for Intramolecular Diels-Alder Reactions

## Problem background
The intramolecular Diels-Alder (IDA) reactions of 1,3,8-nonatriene, 1,3,9-decatriene, and 1,3,10-undecatriene are classic test cases for computational predictions of stereoselectivity. When heated, these trienes cyclize to form fused bicyclic products with either a cis or trans ring junction. The small energy differences between the cis and trans pathways are sensitive to conformational effects, making them a stringent benchmark for quantum chemical methods. This task reproduces the ab initio predictions of the activation enthalpy and free-energy differences (ΔΔH‡ and ΔΔG‡) between the two pathways at the RHF/3-21G level of theory, a widely used reference for such systems.

## Approach
The reproduction follows a standard computational chemistry workflow. For each of the three trienes, plausible concert-ed transition-state guesses for both the cis and trans Diels-Alder pathways are generated, for example by a short force-field conformational search or by chemical intuition. These guesses serve as starting points for RHF/3-21G geometry optimizations that locate the true transition states. On each optimized structure a harmonic vibrational frequency calculation is performed, and all computed frequencies are scaled by 0.8929 to compensate for systematic errors in the harmonic approximation. From the resulting data, the activation enthalpy (ΔH‡) and Gibbs free energy (ΔG‡) at 523 K are derived using standard ideal-gas thermochemistry formulas. Finally, for each triene the differences ΔΔH‡ = ΔH‡(cis) – ΔH‡(trans) and ΔΔG‡ = ΔG‡(cis) – ΔG‡(trans) are computed, both in kcal mol⁻¹. The entire procedure can be carried out with the open-source package Psi4.

## Reproduction target
Compute, for the intramolecular Diels-Alder reactions of triene 1 (1,3,8-nonatriene → 4), triene 2 (1,3,9-decatriene → 5), and triene 3 (1,3,10-undecatriene → 6), the cis-minus-trans differences in activation enthalpy (ΔΔH‡) and Gibbs free energy (ΔΔG‡) at 523 K, using the RHF/3-21G method with vibrational frequencies scaled by 0.8929. Write the resulting six values to a CSV file named `computed_ddG_ddH.csv` with columns `triene` (values `'1'`, `'2'`, `'3'`), `DeltaDeltaH_dagger` (kcal mol⁻¹), and `DeltaDeltaG_dagger` (kcal mol⁻¹), one row per triene.

## Assets

- Psi4 quantum chemistry package: https://psicode.org/
- RDKit or Open Babel: https://www.rdkit.org/
- Molecular structures of trienes 1,2,3

## Workflow steps

### Step 1: Generate starting structures for transition states
- Role: process
- Action: Build the three trienes (1,3,8-nonatriene, 1,3,9-decatriene, 1,3,10-undecatriene) from their SMILES strings given in the task description. For each triene, generate initial guesses for both the cis and trans Diels-Alder transition-state geometries. The initial structures should be plausible concert-ed Diels-Alder transition states suitable for subsequent quantum chemical geometry optimization. You may use a conformational search, chemical intuition, or a force field pre-optimization to generate these guesses. Document the initial structures in a multi-structure file, e.g., initial_ts_structures.xyz.
- Evidence: `/app/outputs/initial_ts_structures.xyz`

### Step 2: RHF/3-21G QM calculations and ΔΔ values
- Role: scored (load-bearing)
- Action: For each triene (1→4, 2→5, 3→6), perform RHF/3-21G geometry optimizations to locate the the Diels-Alder transition states for both the cis and trans pathways. Then run vibrational frequency calculations on the optimized geometries and scale the vibrational frequencies by a factor of 0.8929. Using the computed energies and frequencies, calculate the activation enthalpy (ΔH‡) and Gibbs free energy (ΔG‡) at 523 K for each pathway. Finally, compute the cis-minus-trans differences: ΔΔH‡ = ΔH‡(cis)-ΔH‡(trans) and similarly ΔΔG‡, both in kcal mol⁻¹. Write the six difference values to a CSV file named computed_ddG_ddH.csv.
- Output file: `/app/outputs/computed_ddG_ddH.csv`
- Format: csv
- Contract: Columns: triene (str, values: '1','2','3'), DeltaDeltaH_dagger (float, kcal mol⁻¹), DeltaDeltaG_dagger (float, kcal mol⁻¹). One row per triene.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_ddG_ddH.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_ddG_ddH.csv
- path: `/app/outputs/computed_ddG_ddH.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Cis-minus-trans activation enthalpy and free-energy differences at 523 K computed from RHF/3-21G calculations with frequency scaling 0.8929. The hidden checker compares these values against the paper's reported RHF/3-21G results from Table 3 with an absolute tolerance of 0.5 kcal/mol.
- schema:
  - `type`: table
  - `required_columns`: `triene`, `DeltaDeltaH_dagger`, `DeltaDeltaG_dagger`
  - `units`:
    - `DeltaDeltaH_dagger`: kcal/mol
    - `DeltaDeltaG_dagger`: kcal/mol
  - `notes`: The triene column must contain strings '1', '2', or '3'. The numeric columns are floats.

Notes: Only the RHF/3-21G results are scored. The agent must write the six values (two per triene) in a single CSV file.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_ddG_ddH.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "triene",
          "DeltaDeltaH_dagger",
          "DeltaDeltaG_dagger"
        ],
        "units": {
          "DeltaDeltaH_dagger": "kcal/mol",
          "DeltaDeltaG_dagger": "kcal/mol"
        },
        "notes": "The triene column must contain strings '1', '2', or '3'. The numeric columns are floats."
      },
      "description": "Cis-minus-trans activation enthalpy and free-energy differences at 523 K computed from RHF/3-21G calculations with frequency scaling 0.8929. The hidden checker compares these values against the paper's reported RHF/3-21G results from Table 3 with an absolute tolerance of 0.5 kcal/mol."
    }
  ],
  "notes": "Only the RHF/3-21G results are scored. The agent must write the six values (two per triene) in a single CSV file."
}
```

## How you are scored
A hidden verifier will read `computed_ddG_ddH.csv` and extract the six reported ΔΔH‡ and ΔΔG‡ values. Each value is compared to a reference value obtained from the same protocol (RHF/3-21G with frequency scaling 0.8929 at 523 K). The reward is the proportion of the six values that fall within an allowed tolerance; values outside the tolerance do not earn credit. The verifier does not reveal the reference numbers or the tolerance, so simply reporting a literature value without performing the computation is very unlikely to pass. The scored step carries all the reward weight; the intermediate process step is not scored but is required to reach the final result.
