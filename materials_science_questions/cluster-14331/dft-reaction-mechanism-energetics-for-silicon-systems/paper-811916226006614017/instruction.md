# QCISD(T) Isomerization Energetics of RSiN ⇌ RNSi (R = H, CH₃, OH, F)

## Problem background
Compounds containing triple bonds to silicon, such as silanitriles (RSi≡N) and silaisonitriles (RN=Si), are of fundamental interest in organosilicon chemistry. Their relative thermodynamic stability and the barrier for interconversion determine whether both isomers can be kinetically trapped and experimentally observed. This task investigates how the substituent R influences these properties for R = H, CH₃, OH, and F using high-level ab initio electronic structure methods.

## Approach
Geometry optimizations of the RSiN, RNSi, and transition-state structures are carried out at the QCISD/6-31G* level. Using the optimized geometries, single-point energy evaluations are performed at the QCISD(T)/6-311G** level to obtain accurate total electronic energies. From these energies, the relative stability of the two isomers and the forward/reverse isomerization barriers are computed for each substituent. The central comparison is between the two isomeric forms (RSiN vs RNSi) and the heights of the barriers that separate them.

## Reproduction target
Produce a CSV file `relative_energies.csv` listing, for each substituent (H, CH₃, OH, F) and each isomer (RSiN, RNSi), the QCISD(T)/6-311G**//QCISD/6-31G* total energy in Hartree. A second CSV file `barriers.csv` must provide the forward (RSiN → RNSi) and reverse (RNSi → RSiN) isomerization barriers in kcal mol⁻¹ for the same set of substituents at the same level of theory. Both files must be placed under `/app/outputs`.

## Assets

- Open-source quantum chemistry package (ORCA, Psi4, or similar): https://psicode.org/ (Psi4) or https://orcaforum.kofo.mpg.de/ (ORCA, free with registration)

## Workflow steps

### Step 1: QCISD/6-31G* geometry optimizations
- Role: process
- Action: Construct initial molecular structures for all species involved: for each substituent R in {H, CH₃, OH, F}, prepare the two isomers (RSi≡N and RN=Si) and a guess for the transition state connecting them. Then perform geometry optimizations for every structure at the QCISD/6-31G* level using an open‑source quantum chemistry package. Save the optimized Cartesian coordinates.
- Evidence: `/app/outputs/optimized_geometries.xyz`

### Step 2: QCISD(T)/6-311G** single‑point energies
- Role: process
- Action: For every species whose geometry was optimized in the previous step, run a single‑point energy calculation at the QCISD(T)/6-311G** level. Collect the total energies in Hartree.
- Evidence: `/app/outputs/single_point_energies.txt`

### Step 3: Compute and report relative energies
- Role: scored (load-bearing)
- Action: From the QCISD(T) total energies (Hartree) obtained in the previous step, construct a CSV file containing, for each substituent R and each isomer (RSiN and RNSi), the total electronic energy in Hartree and the method label. The relative energy ΔE = E(RNSi) − E(RSiN) is then implicitly defined and will be derived from these reported total energies by the checker.
- Output file: `/app/outputs/relative_energies.csv`
- Format: csv
- Contract: columns: R (string, e.g., 'H', 'CH3', 'OH', 'F'), isomer (string, either 'RSiN' or 'RNSi'), total_energy_hartree (float), method (string, constant 'QCISD(T)/6-311G**//QCISD/6-31G*')
- Scoring: scored by hidden verifier

### Step 4: Compute and report isomerization barriers
- Role: scored
- Action: Using the same QCISD(T) total energies, compute the forward barrier (RSiN → RNSi) and reverse barrier (RNSi → RSiN) in kcal mol⁻¹. Write to a CSV file with columns for R, forward barrier, reverse barrier, and method.
- Output file: `/app/outputs/barriers.csv`
- Format: csv
- Contract: columns: R (string), forward_barrier_kcal_mol (float, barrier for the RSiN→RNSi direction), reverse_barrier_kcal_mol (float, barrier for the RNSi→RSiN direction), method (string, constant 'QCISD(T)/6-311G**//QCISD/6-31G*')
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_energies.csv`
- `/app/outputs/barriers.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_energies.csv
- path: `/app/outputs/relative_energies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Total QCISD(T) energies (Hartree) for each isomer; the checker derives the relative energy ΔE = E(RNSi) − E(RSiN) and compares it to the paper's reference value.
- schema:
  - `type`: table
  - `required_columns`: `R`, `isomer`, `total_energy_hartree`, `method`
  - `units`:
    - `total_energy_hartree`: Hartree

### barriers.csv
- path: `/app/outputs/barriers.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Forward and reverse isomerization barriers (kcal mol⁻¹) for the RSiN ⇌ RNSi reaction; compared to the paper's reported QCISD(T) values.
- schema:
  - `type`: table
  - `required_columns`: `R`, `forward_barrier_kcal_mol`, `reverse_barrier_kcal_mol`, `method`
  - `units`:
    - `forward_barrier_kcal_mol`: kcal mol⁻¹
    - `reverse_barrier_kcal_mol`: kcal mol⁻¹

Notes: The scored quantities are derived entirely from the agent's own QCISD(T) calculations. The checker compares relative energies (derived from total_energy_hartree) and barriers to the paper's published values with appropriate tolerances. No pre‑computed data or external datasets are needed beyond the quantum chemistry software.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "isomer",
          "total_energy_hartree",
          "method"
        ],
        "units": {
          "total_energy_hartree": "Hartree"
        }
      },
      "description": "Total QCISD(T) energies (Hartree) for each isomer; the checker derives the relative energy ΔE = E(RNSi) − E(RSiN) and compares it to the paper's reference value."
    },
    {
      "file": "barriers.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "R",
          "forward_barrier_kcal_mol",
          "reverse_barrier_kcal_mol",
          "method"
        ],
        "units": {
          "forward_barrier_kcal_mol": "kcal mol⁻¹",
          "reverse_barrier_kcal_mol": "kcal mol⁻¹"
        }
      },
      "description": "Forward and reverse isomerization barriers (kcal mol⁻¹) for the RSiN ⇌ RNSi reaction; compared to the paper's reported QCISD(T) values."
    }
  ],
  "notes": "The scored quantities are derived entirely from the agent's own QCISD(T) calculations. The checker compares relative energies (derived from total_energy_hartree) and barriers to the paper's published values with appropriate tolerances. No pre‑computed data or external datasets are needed beyond the quantum chemistry software."
}
```

## How you are scored
A hidden verifier reads your `relative_energies.csv` and `barriers.csv`. It independently computes the relative isomer energies and cross-checks the total energies and barriers against reference values determined from the published QCISD(T)/6-311G**//QCISD/6-31G* results. The overall score is a weighted combination of the agreement achieved on these two outputs. The main load-bearing check is on the total energies, because the relative energies and barriers are derived from them. The verifier uses appropriate tolerances that account for legitimate differences that arise from independent implementations and hardware. Simply reporting the correct numbers without executing the prescribed quantum calculations will not produce the required intermediate evidence and will not pass the consistency checks.
