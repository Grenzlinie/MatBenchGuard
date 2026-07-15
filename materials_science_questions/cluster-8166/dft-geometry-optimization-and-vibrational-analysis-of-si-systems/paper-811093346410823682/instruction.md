# Prediction of Equilibrium Structure and Infrared Spectrum of SiC4

## Problem background
Silicon-carbon chains are of interest in astrochemistry; the molecule SiC₄ was recently detected in the circumstellar envelope of the evolved carbon star IRC+10216. To aid its further identification and characterisation in space or in the laboratory, ab initio calculations can provide predictions of its molecular geometry and vibrational spectrum. This task reproduces such a calculation, targeting the equilibrium structure and harmonic vibrational frequencies of linear SiC₄ in its ¹Σ ground state.

## Approach
The calculations use second‑order Møller‑Plesset perturbation theory (MP2) with the 6‑311G(d) basis set for carbon and the (12s,9p) contracted [621111,52111] basis with a d function (exponent 0.450) for silicon; all electrons are correlated. The geometry is optimised under the constraint of a linear (collinear) configuration in the singlet ¹Σ electronic state. From the optimised geometry, harmonic vibrational frequencies and infrared intensities are obtained by (numerical or analytic) differentiation of the MP2 energy gradients and dipole moments.

## Reproduction target
Compute the equilibrium bond lengths (SiC₁, C₁C₂, C₂C₃, C₃C₄) in angstroms and the complete set of harmonic vibrational frequencies (cm⁻¹) with associated infrared intensities (km/mol) for linear ²⁸Si¹²C₄ in the ¹Σ electronic state, using the MP2/6‑311G(d) level of theory. Report the bond lengths to three decimal places and present the vibrational modes in order of decreasing frequency, labelling each mode by its symmetry (Σ or Π).

## Assets

- Open-source quantum chemistry package (e.g., PySCF or Psi4): pyscf
- Basis Set Exchange: https://www.basissetexchange.org

## Workflow steps

### Step 1: Geometry optimization of linear SiC4 (^1Σ)
- Role: scored
- Action: Perform a constrained linear geometry optimization of SiC4 (all atoms collinear) in the singlet ^1Σ state at the MP2 level of theory. Use the 6-311G(d) basis for carbon and the (12s,9p) contracted [621111,52111] basis with a d function (exponent 0.450) for silicon. Correlate all 98 electrons. Record the optimized bond lengths (Si–C1, C1–C2, C2–C3, C3–C4) in angstroms.
- Output file: `/app/outputs/step_01_bond_lengths.csv`
- Format: csv
- Contract: Two columns: bond (string, one of SiC1, C1C2, C2C3, C3C4) and value_angstrom (float, to 3 decimal places).
- Scoring: scored by hidden verifier

### Step 2: Harmonic frequency and IR intensity calculation
- Role: scored (load-bearing)
- Action: Using the optimized geometry from step 01, compute the harmonic vibrational frequencies (cm⁻¹) and IR intensities (km/mol) at the same MP2/6-311G(d) level via numerical differentiation of gradients (or analytic Hessian). Report all seven normal modes for ^28Si^12C4, identifying symmetry (Σ or Π).
- Output file: `/app/outputs/step_02_harmonic_frequencies.csv`
- Format: csv
- Contract: Four columns: mode (integer 1–7), frequency_cm1 (float), intensity_kmol (float), symmetry (string, 'Σ' or 'Π').
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_bond_lengths.csv`
- `/app/outputs/step_02_harmonic_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_bond_lengths.csv
- path: `/app/outputs/step_01_bond_lengths.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Optimized bond lengths of linear SiC4 in the ^1Σ state at MP2/6-311G(d).
- schema:
  - `type`: table
  - `required_columns`: `bond`, `value_angstrom`
  - `units`:
    - `value_angstrom`: Å

### step_02_harmonic_frequencies.csv
- path: `/app/outputs/step_02_harmonic_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Harmonic vibrational frequencies and IR intensities of linear ^28Si^12C4 at MP2/6-311G(d).
- schema:
  - `type`: table
  - `required_columns`: `mode`, `frequency_cm1`, `intensity_kmol`, `symmetry`
  - `units`:
    - `frequency_cm1`: cm⁻¹
    - `intensity_kmol`: km/mol

Notes: The checker compares bond lengths and frequencies to the hidden paper gold with appropriate tolerances. Additional structural checks (frequency ordering, intensity of the most intense mode) are performed.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_bond_lengths.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "bond",
          "value_angstrom"
        ],
        "units": {
          "value_angstrom": "Å"
        }
      },
      "description": "Optimized bond lengths of linear SiC4 in the ^1Σ state at MP2/6-311G(d)."
    },
    {
      "file": "step_02_harmonic_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode",
          "frequency_cm1",
          "intensity_kmol",
          "symmetry"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹",
          "intensity_kmol": "km/mol"
        }
      },
      "description": "Harmonic vibrational frequencies and IR intensities of linear ^28Si^12C4 at MP2/6-311G(d)."
    }
  ],
  "notes": "The checker compares bond lengths and frequencies to the hidden paper gold with appropriate tolerances. Additional structural checks (frequency ordering, intensity of the most intense mode) are performed."
}
```

## How you are scored
A hidden automated verifier evaluates your submission. It compares your uploaded bond lengths and harmonic frequencies to a set of reference values, and also checks internal consistency properties such as the ordering of the modes and the relative magnitudes of the intensities. The two stages are weighted: geometry optimisation (step 1) contributes approximately 40 % of the total score, and the frequency calculation (step 2) contributes approximately 60 %. Each stage’s score reflects how close your values are to the reference, with tolerances that account for differences between quantum chemistry programs. You must produce all required output files in the exact format specified; the verifier will not accept deviations.
