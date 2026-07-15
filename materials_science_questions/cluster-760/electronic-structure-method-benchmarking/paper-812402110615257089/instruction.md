# Coupled-cluster benchmark of optical rotation predictions for chiral molecules

## Problem background
Chiral molecules rotate the plane of plane-polarized light, and the specific rotation [α]_D at the sodium D line (589.3 nm) is an experimentally measurable quantity that depends on molecular structure and absolute configuration. Quantum chemical methods can compute [α]_D from first principles, but the accuracy of different treatments of electron correlation—such as Hartree–Fock (HF), density functional theory (DFT) with the B3LYP functional, and coupled-cluster methods (CC2 and CCSD)—remains an open question. This task benchmarks these four methods on a set of 13 small-to-medium chiral organic molecules to determine their relative performance in reproducing experimental optical rotations. The central quantities of interest are the per-molecule computed [α]_D values and the average absolute deviation of each method from experiment for a subset of the molecules, as well as the behavior of one molecule (norbornenone) that is known to exhibit a large rotation and strong sensitivity to electron correlation.

## Approach
Optical rotation is obtained from the frequency-dependent mixed electric dipole–magnetic dipole polarizability tensor, evaluated using linear response theory. The calculation proceeds in two stages:

1. **Geometry optimization:** The ground-state equilibrium geometries of all 13 molecules are optimized with B3LYP and a modest basis set (6‑31G*) to provide the structures at which the specific rotation is computed.

2. **Specific rotation calculation:** For each optimized geometry, the sodium D line specific rotation [α]_D (in degrees [dm (g/cm³)]⁻¹) is computed at four levels of theory, all using the correlation-consistent aug‑cc‑pVDZ basis set:
   - HF with London orbitals (gauge-including atomic orbitals, GIAO), which yields origin-independent results.
   - B3LYP with London orbitals, also origin-independent.
   - CC2 without London orbitals, using the center of mass as the gauge origin.
   - CCSD without London orbitals, using the center of mass as the gauge origin.

The computational protocol follows the original study: gauge-origin issues are avoided for HF and B3LYP via London orbitals, while for the coupled-cluster methods a fixed origin (center of mass) is used consistently because the truncated wavefunction renders the result origin-dependent even with London orbitals. The comparison metric is the average absolute deviation between computed and experimental [α]_D values for molecules 1–11 and 13 (molecule 12 is excluded because it is too large for CC calculations). The norbornenone (molecule 14) case is also evaluated separately because its rotation is dominated by a low-lying n→π* excitation and is expected to challenge the coupled-cluster hierarchy.

## Reproduction target
Produce a CSV file (`alpha_D_table.csv`) containing the computed [α]_D values (in degrees [dm (g/cm³)]⁻¹) for every combination of molecule (IDs 1–11, 13, 14) and method (HF, B3LYP, CC2, CCSD). The hidden verifier will extract your per-molecule values and independently compute the average absolute deviation from experimental reference data for molecules 1–11 and 13, separately for each method. The verifier will then check that the relative accuracy ordering implied by these deviations is consistent with the known ranking from the literature, and that the CCSD and B3LYP values for norbornenone (molecule 14) lie within an expected range relative to experiment. The goal is to obtain a CSV whose derived average absolute deviations and norbornenone values match the expected behavior—balancing accuracy and systematic consistency across the four theoretical methods.

## Assets

- Open-source quantum chemistry package capable of HF, DFT, CC2, CCSD linear-response optical rotation calculations: https://psicode.org/ (Psi4); https://pyscf.org/ (PySCF); https://orcaforum.kofo.mpg.de/ (ORCA)
- aug-cc-pVDZ basis set
- Molecular identities of the target chiral molecules

## Workflow steps

### Step 1: Geometry optimization
- Role: process
- Action: Optimize the molecular geometries of molecules 1–11, 13, 14 at the B3LYP/6-31G* level using the chosen quantum chemistry package. Save the optimized Cartesian coordinates in a structured directory.
- Evidence: none

### Step 2: Compute optical rotations
- Role: scored (load-bearing)
- Action: For each optimized geometry, compute the sodium D line specific rotation [α]_D (degrees [dm (g/cm³)]⁻¹) using the aug-cc-pVDZ basis set: (i) HF with London orbitals; (ii) B3LYP with London orbitals; (iii) CC2 without London orbitals using the center of mass as gauge origin; (iv) CCSD without London orbitals using the center of mass as gauge origin. Write the results to the output CSV.
- Output file: `/app/outputs/alpha_D_table.csv`
- Format: csv
- Contract: Columns: molecule_id (int, values 1–11, 13, 14), HF (float), B3LYP (float), CC2 (float), CCSD (float). Exactly 13 rows matching the molecule IDs.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/alpha_D_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### alpha_D_table.csv
- path: `/app/outputs/alpha_D_table.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed specific rotations [α]_D for each molecule and method, from which the checker recomputes the average absolute deviations relative to experimental [α]_D values and verifies the relative accuracy ordering.
- schema:
  - `type`: table
  - `required_columns`: `molecule_id`, `HF`, `B3LYP`, `CC2`, `CCSD`
  - `units`:
    - `HF`: degrees [dm (g/cm3)]^-1
    - `B3LYP`: degrees [dm (g/cm3)]^-1
    - `CC2`: degrees [dm (g/cm3)]^-1
    - `CCSD`: degrees [dm (g/cm3)]^-1

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "alpha_D_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "molecule_id",
          "HF",
          "B3LYP",
          "CC2",
          "CCSD"
        ],
        "units": {
          "HF": "degrees [dm (g/cm3)]^-1",
          "B3LYP": "degrees [dm (g/cm3)]^-1",
          "CC2": "degrees [dm (g/cm3)]^-1",
          "CCSD": "degrees [dm (g/cm3)]^-1"
        }
      },
      "description": "Computed specific rotations [α]_D for each molecule and method, from which the checker recomputes the average absolute deviations relative to experimental [α]_D values and verifies the relative accuracy ordering."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier evaluates your submitted artifacts. For the main scored step (`alpha_D_table.csv`), the verifier:
- Validates the file format and that it contains exactly 13 rows with the required columns (molecule_id, HF, B3LYP, CC2, CCSD).
- Recomputes the average absolute deviation from experiment for molecules 1–11 and 13 for each method.
- Checks the norbornenone (molecule 14) CCSD and B3LYP values against hidden reference ranges.
- Awards a monotonic reward: if your derived average absolute deviations for any method are equal or better (lower) than a hidden target, you receive full credit for that method's share; worse deviations receive proportionally reduced credit. The norbornenone values similarly contribute to the reward, with full credit when they fall within an acceptable interval and partial credit otherwise.
- The total reward is a weighted sum across all evaluation checks, bounded between 0 and 1. Simply reporting values from the literature is not sufficient; the verifier computes the metrics directly from your CSV and compares them to hidden references. There are no bonus points for reproducing extraneous details—focus on obtaining correct [α]_D values for each molecule and method.
