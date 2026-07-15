# G3 Energy Surface and RRKM Stabilization for SiH2 + Benzene Reaction

## Problem background
The reaction of silylene (SiH2) with substituted silanes typically proceeds by insertion into Si–H bonds. However, when the substituent contains an aromatic ring, it is not clear whether SiH2 can instead add to the ring. To examine this, the paper's computational component models the reaction of SiH2 with benzene (C6H6) as a prototype. It explores the potential energy surface for the SiC6H8 system and uses RRKM theory to predict whether possible ring‑addition products can be collisionally stabilized under experimental conditions. In this task, you will compute the energetic and kinetic quantities that underpin that mechanistic analysis.

## Approach
The method consists of two main computations. First, an ab initio quantum chemical treatment: geometry optimizations and harmonic frequency calculations at the MP2=full/6‑31G(d) level are performed for all relevant minima and transition states on the SiC6H8 surface. A composite energy scheme (e.g., the G3 method or an equivalent high‑level composite) is then applied to obtain total enthalpies at 298.15 K, and relative enthalpies (ΔH) are derived with respect to separated SiH2 + C6H6. Second, a statistical rate theory analysis: using the computed vibrational frequencies, rotational constants, and barrier heights, RRKM/master‑equation calculations are carried out to estimate the pressure‑dependence of collisional stabilization for the two plausible adducts, 7‑silanorcaradiene and 7‑silacycloheptatriene, in an SF6 bath gas. The outcome is reported as log(k/k∞) and as a percent stabilization at each pressure.

## Reproduction target
Produce two output tables:
1. A CSV file containing the G3 total enthalpy (Hartree) and the relative enthalpy (ΔH, kJ/mol) for each stationary point on the SiC6H8 surface. The species to include are: separated SiH2 + C6H6, the two van der Waals complexes C6H6···SiH2, tricyclo[4.1.0.0²,⁷]-1-sila-hept-3-ene, 7-silanorcaradiene, 7-silacycloheptatriene, phenylsilane, and the transition states TSa, TS1, TS2, TS3, TS4. Relative enthalpies are measured from the SiH2 + C6H6 asymptote.
2. A CSV file containing the RRKM stabilization efficiencies for 7-silanorcaradiene and 7-silacycloheptatriene at pressures of 1, 3, 10, 30, and 100 Torr. For each adduct and each pressure, report log(k/k∞) and the corresponding percent stabilization.

## Assets

- Open-source quantum chemistry software (e.g., ORCA, Psi4, GAMESS): https://orcaforum.kofo.mpg.de (ORCA) / https://psicode.org (Psi4) / https://www.msg.chem.iastate.edu/gamess (GAMESS)
- Gaussian basis sets (6-31G(d), 6-31+G(d), 6-31G(2df,p), 6-31G(large)): https://www.basissetexchange.org
- RRKM / Master Equation code (e.g., MESS, standalone RRKM solver): https://kinetics.nist.gov/MESS/
- Python + scientific libraries (numpy, scipy, pandas): pip

## Workflow steps

### Step 1: Compute G3 relative enthalpies for SiH2 + C6H6 stationary points
- Role: scored
- Action: Build initial guess structures for SiH2, C6H6, and all minima/TS on the SiC6H8 surface (the two van der Waals complexes, tricyclo[4.1.0.0^2,7]-1-sila-hept-3-ene, 7-silanorcaradiene, 7-silacycloheptatriene, phenylsilane, TSa, TS1, TS2, TS3, TS4). For each species: perform geometry optimization and harmonic frequency calculation at MP2=full/6-31G(d). Verify transition states have exactly one imaginary frequency and connect reactants/products via IRC. Compute G3 composite energies (or an equivalent high-level composite that yields total enthalpies at 298.15 K). Derive relative enthalpies ΔH in kJ/mol with respect to separated SiH2 + C6H6. Write the final table to /app/outputs/relative_enthalpies.csv.
- Output file: `/app/outputs/relative_enthalpies.csv`
- Format: csv
- Contract: Columns: species (string), G3_H_hartree (float), Delta_H_kJ_mol (float). Rows: SiH2 + C6H6, C6H6...SiH2 complex 1, C6H6...SiH2 complex 2, tricyclo[4.1.0.0^{2,7}]-1-sila-hept-3-ene, 7-silanorcaradiene, 7-silacycloheptatriene, phenylsilane, TSa, TS1, TS2, TS3, TS4.
- Scoring: scored by hidden verifier

### Step 2: RRKM collisional stabilization efficiencies for adducts
- Role: scored (load-bearing)
- Action: Using the vibrational frequencies, moments of inertia, and well-depth/barrier information obtained from the SiC6H8 surface (from step_01), set up RRKM/master-equation calculations for the unimolecular reactions of vibrationally excited 7-silanorcaradiene and 7-silacycloheptatriene. Use a reasonable collision model (e.g., Lennard-Jones parameters for SF6 bath gas). Compute the degree of collisional stabilization as log(k/k∞) and percent stabilization at pressures 1, 3, 10, 30, and 100 Torr for both adducts. Write the results to /app/outputs/rrkm_stabilization.csv.
- Output file: `/app/outputs/rrkm_stabilization.csv`
- Format: csv
- Contract: Columns: product (string), pressure_Torr (int), log_k_over_k_inf (float), percent_stabilization (float). Rows for '7-silanorcaradiene' and '7-silacycloheptatriene' at pressures 1, 3, 10, 30, 100.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/relative_enthalpies.csv`
- `/app/outputs/rrkm_stabilization.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### relative_enthalpies.csv
- path: `/app/outputs/relative_enthalpies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of G3 total enthalpies and relative enthalpies for stationary points on the SiC6H8 energy surface. Compared to paper's Table 3 with a hidden tolerance.
- schema:
  - `required_columns`: `species`, `G3_H_hartree`, `Delta_H_kJ_mol`
  - `units`:
    - `G3_H_hartree`: Hartree
    - `Delta_H_kJ_mol`: kJ/mol

### rrkm_stabilization.csv
- path: `/app/outputs/rrkm_stabilization.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Pressure-dependent stabilization data from RRKM calculations for 7-silanorcaradiene and 7-silacycloheptatriene. Compared to paper's Table 4 with a hidden tolerance.
- schema:
  - `required_columns`: `product`, `pressure_Torr`, `log_k_over_k_inf`, `percent_stabilization`
  - `units`:
    - `log_k_over_k_inf`: dimensionless
    - `percent_stabilization`: %

Notes: The tolerance on Delta_H_kJ_mol is ±5 kJ/mol; on log_k_over_k_inf it is ±0.3 (absolute). Both are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "relative_enthalpies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "species",
          "G3_H_hartree",
          "Delta_H_kJ_mol"
        ],
        "units": {
          "G3_H_hartree": "Hartree",
          "Delta_H_kJ_mol": "kJ/mol"
        }
      },
      "description": "Table of G3 total enthalpies and relative enthalpies for stationary points on the SiC6H8 energy surface. Compared to paper's Table 3 with a hidden tolerance."
    },
    {
      "file": "rrkm_stabilization.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "product",
          "pressure_Torr",
          "log_k_over_k_inf",
          "percent_stabilization"
        ],
        "units": {
          "log_k_over_k_inf": "dimensionless",
          "percent_stabilization": "%"
        }
      },
      "description": "Pressure-dependent stabilization data from RRKM calculations for 7-silanorcaradiene and 7-silacycloheptatriene. Compared to paper's Table 4 with a hidden tolerance."
    }
  ],
  "notes": "The tolerance on Delta_H_kJ_mol is ±5 kJ/mol; on log_k_over_k_inf it is ±0.3 (absolute). Both are hidden."
}
```

## How you are scored
A hidden verifier inspects the two CSV files in /app/outputs. Each file is scored independently:
- For relative_enthalpies.csv, the verifier compares your computed Delta_H_kJ_mol values to reference values; your values must fall within an acceptable tolerance to earn credit for this artifact.
- For rrkm_stabilization.csv, the verifier compares your log_k_over_k_inf values at each pressure to reference values, again within an acceptable tolerance.
The overall reward is a weighted combination of the scores from the two artifacts. Both artifacts must be present, correctly formatted, and contain all required rows to be evaluated.
