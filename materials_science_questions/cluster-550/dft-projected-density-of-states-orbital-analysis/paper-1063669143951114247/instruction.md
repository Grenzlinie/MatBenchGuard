# Cellulose Vibrational Frequency Method Benchmark

## Problem background
Cellulose is an abundant, renewable natural polymer whose vibrational (IR) spectrum provides a fingerprint for structural characterization. Computational modeling of cellulose vibrational spectra is used to assign experimental bands and to assess the accuracy of different quantum chemical methods. This task investigates which of two widely used electronic-structure approaches—density functional theory with the B3LYP functional and Hartree–Fock—yields vibrational frequencies that align better with experimental FTIR data when applied to a short cellulose chain.

## Approach
Build a three-unit β-D-glucose cellulose model (cellotriose) using RDKit. Perform a geometry optimization with DFT (B3LYP functional, 3-21g** basis set) in PySCF. Using the optimized structure, carry out harmonic vibrational frequency calculations with two separate methods: (1) DFT/B3LYP/3-21g** and (2) Hartree–Fock/3-21g. From each calculation, extract the unscaled harmonic frequencies for ten characteristic cellulose bands: CH₂, C-H, C-O-C, C-CO, C-CH, split CH₃ umbrella mode, C-H near 1430 cm⁻¹, C-O, CH symmetric stretch, and O-H stretch. Identify each band by its dominant mode assignment; if multiple modes contribute, select the most representative one following standard cellulose IR assignments. The absolute accuracy of each method will be quantified by the mean absolute error between the computed frequencies and experimental reference values (held hidden).

## Reproduction target
Produce a CSV file (`computed_frequencies.csv`) that lists the computed unscaled harmonic frequencies for all ten bands, for both the DFT:B3LYP/3-21g** and HF/3-21g methods. The primary objective is a quantitative comparison: the method that achieves the lower mean absolute error relative to the experimental band positions is the more accurate model for cellulose vibrational spectra.

## Assets

- PySCF: pyscf
- RDKit: rdkit
- NumPy: numpy

## Workflow steps

### Step 1: Build and optimize cellulose model
- Role: process
- Action: Construct a three-unit β-D-glucose cellulose model (cellotriose) using RDKit. Perform geometry optimization with DFT using the B3LYP functional and 3-21g** basis set with PySCF. Save the final optimized geometry in XYZ format as evidence.
- Evidence: `/app/outputs/cellulose_opt.xyz`

### Step 2: Vibrational frequency calculation and reporting
- Role: scored
- Action: Using the optimized geometry from the previous step, perform harmonic vibrational frequency calculations with two methods: (a) DFT with B3LYP functional and 3-21g** basis set, and (b) Hartree–Fock with 3-21g basis set, both using PySCF. From each calculation, extract the unscaled vibrational frequencies (cm⁻¹) for the ten characteristic cellulose bands: CH₂, C-H, C-O-C, C-CO, C-CH, split CH₃ umbrella mode, C-H (at ~1430 cm⁻¹), C-O, CH symmetric stretch, and O-H stretch. Identify each band by its dominant mode assignment; if multiple modes contribute, select the most representative one according to standard cellulose IR assignments. Output the method, band name, and frequency for both methods in 'computed_frequencies.csv'.
- Output file: `/app/outputs/computed_frequencies.csv`
- Format: csv
- Contract: columns: method (string, either 'DFT:B3LYP/3-21g**' or 'HF/3-21g'), band_name (string, one of: 'CH2', 'C-H', 'C-O-C', 'C-CO', 'C-CH', 'CH3_umbrella', 'C-H_1430', 'C-O', 'CH_sym_stretch', 'OH_stretch'), frequency_cm1 (float, positive). Twenty rows (two methods × ten bands).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/computed_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### computed_frequencies.csv
- path: `/app/outputs/computed_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Computed vibrational frequencies for ten characteristic cellulose bands, reported for both DFT:B3LYP/3-21g** and HF/3-21g. The checker recomputes mean absolute error (MAE) against hidden experimental reference frequencies and scores the ordering condition: MAE(DFT) < MAE(HF).
- schema:
  - `type`: table
  - `required_columns`: `method`, `band_name`, `frequency_cm1`
  - `units`:
    - `frequency_cm1`: cm⁻¹

Notes: The agent must not scale the frequencies; submit unscaled harmonic frequencies directly. The ten bands are defined as in the plan: CH₂ at ~615 cm⁻¹, C-H at ~895 cm⁻¹, C-O-C in the 1160-1030 cm⁻¹ region (use a representative mode), C-CO near 1280 cm⁻¹, C-CH near 1320 cm⁻¹, split CH₃ umbrella mode in 1370-1340 cm⁻¹ (choose a dominant component), C-H at ~1430 cm⁻¹, C-O near 1640 cm⁻¹, CH symmetric stretch near 2900 cm⁻¹, and O-H stretch near 3345 cm⁻¹. All values are in cm⁻¹. The hidden experimental references are the paper's FTIR band positions.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "computed_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "method",
          "band_name",
          "frequency_cm1"
        ],
        "units": {
          "frequency_cm1": "cm⁻¹"
        }
      },
      "description": "Computed vibrational frequencies for ten characteristic cellulose bands, reported for both DFT:B3LYP/3-21g** and HF/3-21g. The checker recomputes mean absolute error (MAE) against hidden experimental reference frequencies and scores the ordering condition: MAE(DFT) < MAE(HF)."
    }
  ],
  "notes": "The agent must not scale the frequencies; submit unscaled harmonic frequencies directly. The ten bands are defined as in the plan: CH₂ at ~615 cm⁻¹, C-H at ~895 cm⁻¹, C-O-C in the 1160-1030 cm⁻¹ region (use a representative mode), C-CO near 1280 cm⁻¹, C-CH near 1320 cm⁻¹, split CH₃ umbrella mode in 1370-1340 cm⁻¹ (choose a dominant component), C-H at ~1430 cm⁻¹, C-O near 1640 cm⁻¹, CH symmetric stretch near 2900 cm⁻¹, and O-H stretch near 3345 cm⁻¹. All values are in cm⁻¹. The hidden experimental references are the paper's FTIR band positions."
}
```

## How you are scored
A hidden verifier independently examines your submitted `computed_frequencies.csv`. It recomputes the mean absolute error (MAE) of your reported frequencies against experimental reference band positions (which are not provided to you) for each method separately. It also applies sanity checks to ensure the frequencies lie within physically reasonable ranges. Your reward is determined by whether the correct ordering of MAE values is satisfied and by the correctness of the band assignments. The exact thresholds and scoring weights are part of the hidden rubric; reporting the paper's numerical results is not sufficient to earn full credit.
