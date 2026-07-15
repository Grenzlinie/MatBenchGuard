# Effective Medium Phonon Frequency Prediction for Porous 4H-SiC

## Problem background
Porous silicon carbide (4H‑SiC) layers exhibit modified optic phonon frequencies compared to bulk material. The optical properties of such inhomogeneous media can be described by an effective dielectric function when the pore size is much smaller than the wavelength of light. A generalized uniaxial Maxwell Garnett effective medium model, assuming aligned ellipsoidal pores, predicts new (Fröhlich) transverse‑optical (TO) and longitudinal‑optical (LO) frequencies that depend on the pore shape (characterized by the axial depolarization factor \(L_\parallel\)) and porosity. Computing these Fröhlich frequencies is a key step for interpreting Raman spectra of porous 4H‑SiC layers.

## Approach
Implement a uniaxial Maxwell Garnett effective medium model for aligned ellipsoidal inclusions (voids) in 4H‑SiC. Use the known bulk oscillator parameters of 4H‑SiC from Harima et al. (1995): axial TO/LO = 783/964 cm⁻¹, planar TO/LO = 798/966.4 cm⁻¹, and the corresponding damping constants. For a fixed porosity \(f = 0.12\), write the effective dielectric tensor components as functions of the axial depolarization factor \(L_\parallel\) (which ranges from 0 for extremely prolate ellipsoids to 1 for extremely oblate ellipsoids). Then, following the standard approach of Loudon (Adv. Phys. 13, 1964), obtain the primed (Fröhlich) TO and LO frequencies along the axial (c‑axis) and planar directions by solving for the poles and zeros of the relevant effective dielectric functions. The result is a set of four frequencies (\(\omega_{T\parallel}'\), \(\omega_{L\parallel}'\), \(\omega_{T\perp}'\), \(\omega_{L\perp}'\)) for each value of \(L_\parallel\).

## Reproduction target
For a porosity of 12 %, compute the primed axial and planar TO and LO frequencies of porous 4H‑SiC for at least 10 equally spaced values of the axial depolarization factor \(L_\parallel\) covering the range [0, 1]. Write the results to a CSV file with the columns L_parallel, omega_T_parallel, omega_L_parallel, omega_T_perpendicular, omega_L_perpendicular (all frequencies in reciprocal centimetres).

## Assets

- Bulk 4H-SiC oscillator parameters from Harima et al. (1995): 10.1063/1.360174

## Workflow steps

### Step 1: Compute Fröhlich frequencies
- Role: scored (load-bearing)
- Action: Implement the uniaxial Maxwell Garnett effective medium model for aligned ellipsoidal pores in 4H-SiC. Use the bulk oscillator parameters (axial TO=783 cm⁻¹, LO=964 cm⁻¹; planar TO=798 cm⁻¹, LO=966.4 cm⁻¹, and damping constants) from Harima et al. (1995). For a porosity of 12%, compute the effective dielectric tensor components and solve for the primed (Fröhlich) transverse-optical (TO) and longitudinal-optical (LO) frequencies along the axial and planar directions, for the axial depolarization factor L∥ ranging from 0 to 1 (at least 10 values). Save the results as froehlich_frequencies.csv.
- Output file: `/app/outputs/froehlich_frequencies.csv`
- Format: csv
- Contract: CSV with columns: L_parallel (float), omega_T_parallel (float, cm⁻¹), omega_L_parallel (float, cm⁻¹), omega_T_perpendicular (float, cm⁻¹), omega_L_perpendicular (float, cm⁻¹). At least 10 rows covering L_parallel from 0 to 1.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/froehlich_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### froehlich_frequencies.csv
- path: `/app/outputs/froehlich_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of computed Fröhlich frequencies; rows correspond to different values of the axial depolarization factor L∥.
- schema:
  - `type`: table
  - `required_columns`: `L_parallel`, `omega_T_parallel`, `omega_L_parallel`, `omega_T_perpendicular`, `omega_L_perpendicular`
  - `units`:
    - `L_parallel`: dimensionless
    - `omega_T_parallel`: cm^-1
    - `omega_L_parallel`: cm^-1
    - `omega_T_perpendicular`: cm^-1
    - `omega_L_perpendicular`: cm^-1

Notes: Absolute frequencies are compared to a hidden reference implementation with tolerance; a structural trend check of the effective-medium model is also performed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "froehlich_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "L_parallel",
          "omega_T_parallel",
          "omega_L_parallel",
          "omega_T_perpendicular",
          "omega_L_perpendicular"
        ],
        "units": {
          "L_parallel": "dimensionless",
          "omega_T_parallel": "cm^-1",
          "omega_L_parallel": "cm^-1",
          "omega_T_perpendicular": "cm^-1",
          "omega_L_perpendicular": "cm^-1"
        }
      },
      "description": "Table of computed Fröhlich frequencies; rows correspond to different values of the axial depolarization factor L∥."
    }
  ],
  "notes": "Absolute frequencies are compared to a hidden reference implementation with tolerance; a structural trend check of the effective-medium model is also performed."
}
```

## How you are scored
Your output file froehlich_frequencies.csv will be evaluated by a hidden verifier. It performs two types of checks:
1. **Absolute accuracy:** the computed TO and LO frequencies are compared against reference values (obtained from a correct implementation) within a tolerance. Correct values that fall within the allowed margin receive credit; values far from the reference do not.
2. **Structural trend:** the verifier checks that the relationship between \(\omega_{L\parallel}'\) and \(\omega_{T\parallel}'\) follows the expected inversion pattern predicted by the effective‑medium model across the full range of \(L_\parallel\). No further details of the condition are disclosed.
Both absolute accuracy and the trend condition must be met to earn full credit. The final reward is a weighted combination of the results for each checked aspect. Simply reporting numbers from the literature without actually computing them will not satisfy the verifier.
