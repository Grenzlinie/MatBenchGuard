# Reproduce DFT Energy Barriers for DBT Initial Reaction Steps

## Problem background
Dibenzothiophene (DBT) is one of the most stable sulfur-containing species in petroleum. Removing DBT is critical for reducing sulfur emissions that cause acid rain, catalyst poisoning, and health problems. Understanding the initial unimolecular reaction steps of DBT pyrolysis – H-migration, S–C bond rupture, and isomerization – is essential for designing better desulfurization strategies. This task computes the energy barriers and reaction energies for all 16 initial reaction steps, providing a quantitative map of DBT reactivity.

## Approach
The approach uses density functional theory (DFT) at the UB3LYP/6-311G++(d,p) level to compute electronic energies of DBT, all intermediates, and transition states. The workflow begins by constructing molecular geometries for the 16 reactions: eight H-migration steps, two S–C bond-rupture routes leading to biradical intermediates, and six isomerization paths. For each reaction, a complete quantum chemical protocol is executed: geometry optimization of reactants/products, transition-state search, vibrational frequency analysis to confirm the nature of stationary points, and intrinsic reaction coordinate (IRC) verification. From the converged electronic energies (0 K, no zero‑point correction), the energy barrier (E(TS) – E(DBT)) and reaction energy (E(product) – E(DBT)) are computed in kcal/mol. The calculations can be carried out with any quantum chemistry package that supports the required functional and basis set, such as the open-source ORCA code.

## Reproduction target
Compute the energy barriers and reaction energies for all 16 initial unimolecular reaction steps of DBT. Output the results as a CSV file (`initial_step_energies.csv`) with columns: `Reaction`, `Energy_barrier_kcal_mol`, `Reaction_energy_kcal_mol`. The rows must follow the order: DBT-C32, DBT-C34, DBT-C43, DBT-C45, DBT-C56, DBT-C54, DBT-C65, DBT-C67, DBT-I1, DBT-I2, DBT-I3, DBT-I4, DBT-I5, DBT-I6, DBT-BIM3, DBT-BIM4. All energies are electronic energies at 0 K without zero‑point correction.

## Scope and limitations
This task reproduces only the initial reaction step energetics (Table 2). The paper also reports primary products, Gibbs free energy changes for the full pyrolysis pathways (Table 8), and a comparison with thiophene/benzothiophene. Computing Gibbs free energies for those pathways would require thermodynamic analysis (frequencies, partition functions) for many additional intermediates and transition states beyond the 16 initial steps, which is computationally infeasible within a single-agent run. The relative barrier ordering (e.g., that DBT-BIM3 has the lowest barrier) is verified by the hidden checker as a structural audit; no separate output is required.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: Construct initial molecular geometries
- Role: process
- Action: Generate molecular structures for the DBT reactant and for all intermediates and transition states corresponding to the 16 initial unimolecular reactions: eight H-migration steps (DBT-C32, DBT-C34, DBT-C43, DBT-C45, DBT-C56, DBT-C54, DBT-C65, DBT-C67), two S–C bond-rupture steps leading to biradical intermediates (DBT-BIM3, DBT-BIM4), and six isomerization steps (DBT-I1 through I6). The connectivity is described in the paper's text and figures; build the structures from the DBT scaffold.
- Evidence: `/app/outputs/geometries.xyz`

### Step 2: Perform DFT calculations
- Role: process
- Action: For each of the 16 initial reactions, carry out a complete computational workflow at the UB3LYP/6-311G++(d,p) level using a suitable quantum chemistry package: geometry optimization of the reactant (DBT), intermediates, and products; transition state optimization; vibrational frequency analysis to confirm stationary points (zero imaginary frequencies for minima, one imaginary frequency for TS); intrinsic reaction coordinate (IRC) calculations to verify that each TS connects the intended reactant and product.
- Evidence: `/app/outputs/dft_logs`

### Step 3: Compute energy barriers and reaction energies
- Role: scored (load-bearing)
- Action: Extract electronic energies (without zero-point correction) from the DFT calculations. For each reaction, compute the energy barrier as E(TS) – E(DBT) and the reaction energy as E(product) – E(DBT), both in kcal/mol. Output the results as a CSV file.
- Output file: `/app/outputs/initial_step_energies.csv`
- Format: csv
- Contract: CSV with header: Reaction,Energy_barrier_kcal_mol,Reaction_energy_kcal_mol. 16 rows in the order: DBT-C32, DBT-C34, DBT-C43, DBT-C45, DBT-C56, DBT-C54, DBT-C65, DBT-C67, DBT-I1, DBT-I2, DBT-I3, DBT-I4, DBT-I5, DBT-I6, DBT-BIM3, DBT-BIM4.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/initial_step_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### initial_step_energies.csv
- path: `/app/outputs/initial_step_energies.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Energy barriers and reaction energies for the 16 DBT initial unimolecular reaction steps listed in Table 2 of the source paper, computed at the UB3LYP/6-311++G(d,p) level without zero-point correction.
- schema:
  - `type`: table
  - `required_columns`: `Reaction`, `Energy_barrier_kcal_mol`, `Reaction_energy_kcal_mol`
  - `units`:
    - `Energy_barrier_kcal_mol`: kcal/mol
    - `Reaction_energy_kcal_mol`: kcal/mol

Notes: The energy barrier is defined as E(TS) - E(DBT); reaction energy is E(product) - E(DBT), both in kcal/mol at 0 K without ZPE correction. The CSV rows must follow the order of Table 2 (eight H-migration steps, six isomerizations, then DBT-BIM3 and DBT-BIM4).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "initial_step_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Reaction",
          "Energy_barrier_kcal_mol",
          "Reaction_energy_kcal_mol"
        ],
        "units": {
          "Energy_barrier_kcal_mol": "kcal/mol",
          "Reaction_energy_kcal_mol": "kcal/mol"
        }
      },
      "description": "Energy barriers and reaction energies for the 16 DBT initial unimolecular reaction steps listed in Table 2 of the source paper, computed at the UB3LYP/6-311++G(d,p) level without zero-point correction."
    }
  ],
  "notes": "The energy barrier is defined as E(TS) - E(DBT); reaction energy is E(product) - E(DBT), both in kcal/mol at 0 K without ZPE correction. The CSV rows must follow the order of Table 2 (eight H-migration steps, six isomerizations, then DBT-BIM3 and DBT-BIM4)."
}
```

## How you are scored
A hidden verifier compares your computed energy barriers and reaction energies against reference values (the paper's reported numbers). Each row's barrier and reaction energy must fall within an acceptable tolerance to earn credit. The verifier also checks that the relative ordering of the barriers (e.g., which step has the lowest barrier) matches expectations. Partial credit is awarded proportionally to the number of entries that satisfy the checks. Simply reporting memorised numbers without running the DFT workflow will not pass the structural audit.
