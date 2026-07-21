# Compute Effective Exchange Integrals for Cyanide-Bridged Dinuclear Transition Metal Complexes

## Problem background
Prussian blue analogs are a class of molecular magnetic materials whose properties arise from superexchange interactions between transition metal ions bridged by cyanide ligands. Predicting the sign and approximate magnitude of the effective exchange coupling constants (J_ab) from electronic structure methods is a key step toward understanding and designing such magnets. This task focuses on computing J_ab for a set of model M-C≡N-M' dinuclear units, representing different metal combinations, using first‑principles quantum chemical methods.

## Approach
The exchange coupling constant J_ab is obtained from the difference between the total energies of the lowest‑spin (LS) and highest‑spin (HS) states of the dinuclear unit: J_ab = E(LS) − E(HS). The LS and HS states are defined by coupling the single‑ion spins of the two metal centers (determined from their formal d‑electron counts) to give the overall minimum and maximum spin multiplicity. Total energies are computed with two electronic structure methods: unrestricted Hartree–Fock (UHF) and density functional theory (DFT) using a triple‑zeta quality basis set (e.g., cc‑pVTZ). The calculations are performed on linear model geometries for the five M-C≡N-M' systems. No experimental data are required; the target J_ab values are derived entirely from the computational procedure.

## Reproduction target
Your goal is to produce a CSV file containing the computed effective exchange integrals J_ab (in cm⁻¹) for all five metal‑pair systems with both the UHF and DFT methods. The five systems are: Cr(III)-CN-Cr(III), Cr(III)-CN-Mn(II), Cr(III)-CN-V(II), Cr(III)-CN-Ni(II), Cr(III)-CN-V(III). The file must contain exactly ten rows, each with columns: system, method, j_ab. The J_ab values must be computed by the workflow described in Steps 1–3; you will construct the linear molecular geometries, run the total energy calculations for the LS and HS states, and compute J_ab from the energy differences (converting Hartree to cm⁻¹ with 1 Hartree = 219474.63 cm⁻¹). The final CSV should be saved as `/app/outputs/j_ab_values.csv`.

## Assets

- Quantum chemistry package (e.g., PySCF, ORCA, GAMESS, Gaussian)
- Triple-zeta basis set (e.g., cc‑pVTZ from Basis Set Exchange): https://www.basissetexchange.org

## Workflow steps

### Step 1: Construct molecular geometries
- Role: process
- Action: For each of the five M-C≡N-M' units (M=Cr(III), M'=V(II), V(III), Cr(III), Mn(II), Ni(II)), build a linear molecular geometry with standard bond distances (e.g., Cr–C ~2.0 Å, C≡N ~1.15 Å, N–M' ~2.0 Å) and save coordinate files in XYZ format. Use the formal metal spins (S=3/2 for Cr(III), etc.) to determine the spin multiplicities for later calculations.
- Evidence: `/app/outputs/geometries.zip`

### Step 2: Run UHF and DFT total energy calculations
- Role: process
- Action: Using the molecular geometries from step_01, perform unrestricted Hartree-Fock (UHF) and density functional theory (DFT, e.g., B3LYP) calculations with a triple-zeta basis set to obtain total energies (in Hartree) for the lowest spin (LS) and highest spin (HS) states of each unit. Write a table of the LS and HS energies.
- Evidence: `/app/outputs/total_energies.csv`

### Step 3: Compute effective exchange integrals J_ab
- Role: scored (load-bearing)
- Action: For each system and each method (UHF/DFT), compute J_ab = E(LS) − E(HS). If energies are in Hartree, convert to cm⁻¹ (1 Hartree = 219474.63 cm⁻¹). Write a CSV file with columns: system, method, j_ab. Include all five systems and both methods.
- Output file: `/app/outputs/j_ab_values.csv`
- Format: csv
- Contract: system (string, one of: Cr(III)-CN-Cr(III), Cr(III)-CN-Mn(II), Cr(III)-CN-V(II), Cr(III)-CN-Ni(II), Cr(III)-CN-V(III)), method (string, 'UHF' or 'DFT'), j_ab (float, in cm⁻¹)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/j_ab_values.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### j_ab_values.csv
- path: `/app/outputs/j_ab_values.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Effective exchange integrals J_ab computed from the difference between lowest-spin and highest-spin total energies for five M-CN-M' model systems using both UHF and DFT methods. The file must contain ten rows (5 systems × 2 methods).
- schema:
  - `type`: table
  - `required_columns`: `system`, `method`, `j_ab`
  - `units`:
    - `j_ab`: cm⁻¹

Notes: The scoring verifier checks that the sign of each J_ab value agrees with the paper-reported sign for the corresponding system–method pair. Magnitude may be checked for approximate agreement but the primary requirement is correct sign reproduction.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "j_ab_values.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "method",
          "j_ab"
        ],
        "units": {
          "j_ab": "cm⁻¹"
        }
      },
      "description": "Effective exchange integrals J_ab computed from the difference between lowest-spin and highest-spin total energies for five M-CN-M' model systems using both UHF and DFT methods. The file must contain ten rows (5 systems × 2 methods)."
    }
  ],
  "notes": "The scoring verifier checks that the sign of each J_ab value agrees with the paper-reported sign for the corresponding system–method pair. Magnitude may be checked for approximate agreement but the primary requirement is correct sign reproduction."
}
```

## How you are scored
A hidden verifier will read your `/app/outputs/j_ab_values.csv`. It will compare the sign (positive or negative) of each J_ab entry against a set of hidden reference signs that reflect the physically expected coupling for each system‑method combination. A perfect score requires that all ten predicted signs match the hidden reference signs. Additionally, the verifier may apply a small bonus check on the approximate magnitude of the J_ab values to reward consistency with physically plausible ranges; this bonus does not affect the primary sign‑based score. Your reward is computed from all system‑method pairs together. Reporting numbers without actually performing the UHF and DFT calculations will almost certainly produce incorrect signs and will therefore yield a low reward.
