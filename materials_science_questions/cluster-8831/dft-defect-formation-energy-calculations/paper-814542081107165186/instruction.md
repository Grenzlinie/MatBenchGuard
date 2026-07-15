# DFT survey of antisite defect formation energies in perovskite heterostructures

## Problem background
Transition-metal oxide heterointerfaces can host emergent electronic properties, but the presence of cation antisite defects—in which transition-metal atoms exchange positions across the interface—may degrade these properties. Understanding which combinations of transition-metal atoms are more or less likely to form such defects is essential for the design of atomically sharp interfaces. This task focuses on computing antisite defect formation energies across a wide survey of perovskite AMO3/AM'O3 interfaces (A = La, Sr; M, M' drawn from first-row transition metals), using first-principles calculations. The target is to determine, for each chemically distinct pair, whether the rocksalt or the layered atomic configuration is energetically favored, and by how much.

## Approach
You will perform density functional theory (DFT) calculations within the supercell approach, using the generalized gradient approximation (PBE) plus a Hubbard U correction (GGA+U) to treat correlation effects. For each interfacial pair, a √2×√2×2 supercell is constructed for both the layered (L) and rocksalt (R) configurations. Structural relaxations are carried out on these cells, and the ground-state magnetic ordering is determined by comparing ferromagnetic, G-type antiferromagnetic, and (for the L configuration only) A-type antiferromagnetic spin arrangements. The defect formation energy for a given MM' pair is defined as ΔE = E(R) − E(L), where E(R) and E(L) are the lowest total energies obtained after relaxation and magnetic ordering selection. This set of energies quantifies the thermodynamic preference for defect formation across the full range of combinations.

## Reproduction target
Compute and report the antisite defect formation energy ΔE = E(rocksalt) − E(layered) for every one of the 21 LaMO₃/LaM'O₃ (M, M' = Ti, V, Cr, Mn, Fe, Co, Ni) and 15 SrMO₃/SrM'O₃ (M, M' = Ti, V, Cr, Mn, Fe, Co) combinations, following the DFT protocol and magnetic ordering selection described in the workflow steps. The results must be written to a CSV file with columns A, M, M_prime, and delta_E, where delta_E is the formation energy in eV per defect. All 36 combinations must be present.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- SSSP pseudopotential library (efficiency or PBE): https://www.materialscloud.org/discover/sssp/table

## Workflow steps

### Step 1: DFT total energy calculations
- Role: process
- Action: For each of the 21 LaMO3/LaM'O3 (M,M' = Ti,V,Cr,Mn,Fe,Co,Ni) and 15 SrMO3/SrM'O3 (M,M' = Ti,V,Cr,Mn,Fe,Co) interfaces, construct a √2×√2×2 supercell (20 atoms) for the layered (L) and rocksalt (R) configurations. Perform structural relaxation using DFT with PBE+U (U=5.0 eV on TM d orbitals, J=0.65 eV for Ti,V,Cr; J=1.0 eV for Mn,Fe,Co,Ni; U_La=9.0 eV on La f states), a plane-wave cutoff of 600 eV, and appropriate k-point mesh. For each configuration, test ferromagnetic, G-type antiferromagnetic, and (for L only) A-type antiferromagnetic orderings. Select the magnetic ordering that gives the lowest total energy. Save all lowest total energies (and optionally the winning magnetic ordering and transport classification) per pair and configuration in a structured file.
- Evidence: `/app/outputs/total_energies.json`

### Step 2: Defect formation energy compilation
- Role: scored (load-bearing)
- Action: Read the DFT total energies from Step 1. For each (A,M,M') pair, compute the defect formation energy as ΔE = E(R) - E(L), where E(R) and E(L) are the lowest total energies for the rocksalt and layered configurations. Output the results for all 36 combinations.
- Output file: `/app/outputs/defect_formation_energies.csv`
- Format: csv
- Contract: Columns: A (string, either 'La' or 'Sr'), M (string, chemical symbol of first TM), M_prime (string, chemical symbol of second TM), delta_E (float, formation energy in eV per defect). One row for each of the 21 La-based and 15 Sr-based combinations.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_formation_energies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_formation_energies.csv
- path: `/app/outputs/defect_formation_energies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Antisite defect formation energies for all 36 perovskite interface combinations (21 La-based, 15 Sr-based).
- schema:
  - `type`: table
  - `required_columns`: `A`, `M`, `M_prime`, `delta_E`
  - `units`:
    - `delta_E`: eV per defect
  - `description`: Each row is a unique (A,M,M_prime) combination. A is 'La' or 'Sr'. M and M_prime are transition-metal symbols from {Ti,V,Cr,Mn,Fe,Co} plus Ni for La. delta_E is the computed formation energy.

Notes: The checker will compare the reported delta_E values against hidden gold values from the paper's Tables II and III (eV per supercell) using mean absolute error (MAE). Full credit for MAE ≤ 0.2 eV; partial credit for MAE ≤ 0.5 eV. Sign mismatches reduce credit. Missing combinations incur a proportional penalty.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_formation_energies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "A",
          "M",
          "M_prime",
          "delta_E"
        ],
        "units": {
          "delta_E": "eV per defect"
        },
        "description": "Each row is a unique (A,M,M_prime) combination. A is 'La' or 'Sr'. M and M_prime are transition-metal symbols from {Ti,V,Cr,Mn,Fe,Co} plus Ni for La. delta_E is the computed formation energy."
      },
      "description": "Antisite defect formation energies for all 36 perovskite interface combinations (21 La-based, 15 Sr-based)."
    }
  ],
  "notes": "The checker will compare the reported delta_E values against hidden gold values from the paper's Tables II and III (eV per supercell) using mean absolute error (MAE). Full credit for MAE ≤ 0.2 eV; partial credit for MAE ≤ 0.5 eV. Sign mismatches reduce credit. Missing combinations incur a proportional penalty."
}
```

## How you are scored
A hidden verifier will compare each delta_E value in your output CSV against independently computed reference values. Your final reward is based on the accuracy of the reported formation energies: results that closely agree with the references earn full credit, while larger errors, sign discrepancies, or missing combinations reduce the score. The reward combines the performance across all required combinations into a single overall score.
