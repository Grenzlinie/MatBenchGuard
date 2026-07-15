# Zone-center phonon frequencies and symmetry assignments for β- and γ-Ge3N4

## Problem background
Germanium nitride (Ge3N4) exists in two crystalline polymorphs: the hexagonal β phase (space group P6₃/m) and the cubic spinel γ phase (space group Fd̅3m). These two phases differ in the coordination environment of Ge atoms and in their vibrational properties. The zone-center (Γ-point) optical phonon frequencies and their symmetry assignments are important fingerprints for phase identification, especially via Raman spectroscopy. Using first-principles density functional theory (DFT) with the local density approximation (LDA), it is possible to compute the phonon modes reliably and assign them to irreducible representations, providing a basis for interpreting experimental Raman spectra. This task requires reproducing the DFT-LDA computed frequencies and symmetry labels for the Raman-active modes of both β- and γ-Ge3N4.

## Approach
The computational protocol combines group-theoretical factor analysis with plane-wave pseudopotential DFT-LDA calculations. First, a factor-group analysis is performed for each phase to determine which irreducible representations are Raman-active at the zone center, based on the crystal structure and Wyckoff positions. Then, independent DFT-LDA relaxations are carried out for both the hexagonal β-Ge3N4 (lattice constants a=8.028 Å, c=3.052 Å) and the cubic γ-Ge3N4 (a=8.2125 Å) to optimize the internal atomic coordinates. Starting from the relaxed structures, zone-center phonon frequencies and eigenvectors are obtained via a direct force-constant matrix approach (finite atomic displacements). For each phase, the computed phonon modes are inspected to identify those belonging to the Raman-active symmetry species, and their frequencies are extracted. The final output consists of two CSV tables: one for β-Ge3N4 and one for γ-Ge3N4, each listing the computed frequency (in cm⁻¹) and irreducible representation label for every Raman-active mode.

## Reproduction target
Produce the zone-center phonon frequencies and symmetry assignments for the Raman-active modes of β-Ge3N4 and γ-Ge3N4 using DFT-LDA. Write the results to two CSV files: beta_phonon_frequencies.csv (for the β phase) and gamma_phonon_frequencies.csv (for the γ phase). Each file must contain columns: mode_id (integer), computed_frequency (float, cm⁻¹), and symmetry (string). The β-phase table must include all Raman-active modes predicted by factor-group analysis for the P6₃/m structure; the γ-phase table must include all Raman-active modes predicted for the Fd̅3m structure. The computed frequencies will be compared against experimental Raman measurements using mean absolute deviation as the primary metric.

## Assets

- Quantum ESPRESSO (open-source plane-wave DFT code): https://www.quantum-espresso.org/
- SSSP efficiency pseudopotentials for Ge and N: https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Factor-group symmetry analysis of Raman-active modes
- Role: process
- Action: Perform factor-group analysis for the hexagonal β-Ge3N4 (space group P6₃/m, Z=2) and cubic spinel γ-Ge3N4 (space group Fd̅3m, Z=2) to determine the irreducible representation labels and multiplicities of the zone-center Raman-active optical phonons.
- Evidence: `/app/outputs/symmetry_analysis.txt`

### Step 2: DFT structure optimization
- Role: process
- Action: Perform DFT-LDA plane-wave pseudopotential relaxation for β-Ge3N4 (hexagonal, lattice constants a=8.028 Å, c=3.052 Å) and γ-Ge3N4 (cubic, a=8.2125 Å), optimizing internal atomic coordinates until forces are sufficiently small.
- Evidence: `/app/outputs/relaxation.log`

### Step 3: Zone-center phonon calculation
- Role: process
- Action: For each optimized structure, compute the Γ-point (zone-center) phonon frequencies and eigenvectors using a direct force-constant matrix method within DFT-LDA.
- Evidence: `/app/outputs/phonon_output.log`

### Step 4: Extract and assign Raman modes for β-Ge3N4
- Role: scored
- Action: From the phonon eigenvectors and frequencies for β-Ge3N4, identify the 11 Raman-active modes belonging to the A_g, E_{1g}, and E_{2g} irreducible representations (as predicted by factor-group analysis), extract their frequencies in cm⁻¹, and write the results to beta_phonon_frequencies.csv.
- Output file: `/app/outputs/beta_phonon_frequencies.csv`
- Format: csv
- Contract: A CSV file with columns: mode_id (integer from 1 to 11), computed_frequency (float, cm⁻¹), symmetry (string). The rows can be in any order, but all 11 modes must be present.
- Scoring: scored by hidden verifier

### Step 5: Extract and assign Raman modes for γ-Ge3N4
- Role: scored
- Action: From the phonon eigenvectors and frequencies for γ-Ge3N4, identify the 5 Raman-active modes belonging to the A_{1g}, E_g, and T_{2g} irreducible representations, extract their frequencies in cm⁻¹, and write the results to gamma_phonon_frequencies.csv.
- Output file: `/app/outputs/gamma_phonon_frequencies.csv`
- Format: csv
- Contract: A CSV file with columns: mode_id (integer from 1 to 5), computed_frequency (float, cm⁻¹), symmetry (string). The rows can be in any order, but all 5 modes must be present.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/beta_phonon_frequencies.csv`
- `/app/outputs/gamma_phonon_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### beta_phonon_frequencies.csv
- path: `/app/outputs/beta_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed zone-center Raman-active phonon frequencies and symmetry labels for β-Ge3N4. The frequencies are compared to experimental values using mean absolute deviation with a pass/fail threshold; meeting or beating the threshold earns full credit. A low-weight structural audit checks that the correct counts of irreducible representations are present.
- schema:
  - `type`: table
  - `required_columns`: `mode_id`, `computed_frequency`, `symmetry`
  - `units`:
    - `computed_frequency`: cm⁻¹

### gamma_phonon_frequencies.csv
- path: `/app/outputs/gamma_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Computed zone-center Raman-active phonon frequencies and symmetry labels for γ-Ge3N4. Same scoring policy as β: threshold_or_better on mean absolute deviation against experimental gold, plus a low-weight symmetry consistency check.
- schema:
  - `type`: table
  - `required_columns`: `mode_id`, `computed_frequency`, `symmetry`
  - `units`:
    - `computed_frequency`: cm⁻¹

Notes: The main scoring metric is the mean absolute deviation between the computed frequencies and the experimental Raman measurements from the paper, with different thresholds for each phase. Symmetry assignments are cross-checked against the factor-group prediction counts. The experimental values and tolerances are hidden.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "beta_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_id",
          "computed_frequency",
          "symmetry"
        ],
        "units": {
          "computed_frequency": "cm⁻¹"
        }
      },
      "description": "Computed zone-center Raman-active phonon frequencies and symmetry labels for β-Ge3N4. The frequencies are compared to experimental values using mean absolute deviation with a pass/fail threshold; meeting or beating the threshold earns full credit. A low-weight structural audit checks that the correct counts of irreducible representations are present."
    },
    {
      "file": "gamma_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_id",
          "computed_frequency",
          "symmetry"
        ],
        "units": {
          "computed_frequency": "cm⁻¹"
        }
      },
      "description": "Computed zone-center Raman-active phonon frequencies and symmetry labels for γ-Ge3N4. Same scoring policy as β: threshold_or_better on mean absolute deviation against experimental gold, plus a low-weight symmetry consistency check."
    }
  ],
  "notes": "The main scoring metric is the mean absolute deviation between the computed frequencies and the experimental Raman measurements from the paper, with different thresholds for each phase. Symmetry assignments are cross-checked against the factor-group prediction counts. The experimental values and tolerances are hidden."
}
```

## How you are scored
A hidden verifier reads your two CSV files (beta_phonon_frequencies.csv and gamma_phonon_frequencies.csv). For each phase, the verifier computes the mean absolute deviation (MAE) between your computed frequencies and a set of hidden experimental Raman frequencies. Full credit for that phase is awarded if the MAE meets or beats a predetermined threshold; otherwise, credit decays as the MAE worsens. In addition, the verifier performs a low-weight consistency check that your symmetry assignments match the expected counts of Raman-active irreducible representations for each phase. The final reward is a weighted combination of these checks, with the frequency agreement carrying the highest weight.
