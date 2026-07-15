# DFT Vibrational Frequencies of Ce+SiH4 Isomers and H3CCeH

## Problem background
The reaction of cerium atoms with silane can produce several isomers whose identification is challenging when relying solely on matrix infrared spectroscopy. Computational harmonic vibrational frequency calculations provide a complementary tool for distinguishing candidate structures by comparing predicted and experimental matrix IR spectra. This reproduction focuses on the DFT frequency calculations for a set of candidate product molecules—four CeSiH4 isomers and the analogous H3CCeH—that are central to the isomer assignment.

## Approach
Density functional theory (DFT) is employed at the B3LYP/6-311++G(3df,3pd) level, using the built-in Stuttgart effective core potential ECP28MWB_SEG for cerium. For each of the five candidate molecules—Si(μ-H)3CeH, H3SiCeH, H2Si(μ-H)CeH, HSi(μ-H)2CeH, and H3CCeH—both a geometry optimization and a subsequent harmonic vibrational frequency calculation are performed in the triplet electronic state. These computations are then repeated for the fully deuterated isotopologues (H replaced by D). The unscaled harmonic frequencies (cm⁻¹) and IR intensities (km/mol) are extracted from the DFT output, and brief qualitative mode descriptions are assigned based on the normal mode displacements. The collected data are written to a CSV file. Post‑processing bonding analyses (NBO, ELF, etc.) are not part of this reproduction.

## Reproduction target
Perform geometry optimization and harmonic vibrational frequency calculation at the specified theory level for the five molecules listed above, each in the triplet state, and for their fully deuterated analogues. From the calculation outputs, produce a CSV file (`computed_frequencies.csv`) that records, for every isomer and isotopologue, each normal mode’s harmonic frequency, IR intensity, and a short descriptive label. The target is a complete set of computed vibrational frequencies that can be evaluated against experimental reference data.

## Assets

- ORCA quantum chemistry package: https://orcaforum.kofo.mpg.de/

## Workflow steps

### Step 1: DFT geometry optimization and frequency calculation
- Role: process
- Action: For each of the five molecules—Si(μ-H)3CeH, H3SiCeH, H2Si(μ-H)CeH, HSi(μ-H)2CeH, and H3CCeH—and for both hydrogen isotopologue (all H) and fully deuterated isotopologue (all D), construct initial molecular geometries based on the structural descriptions (bond lengths and angles derived from the paper’s Figure 4). Run geometry optimization followed by harmonic vibrational frequency calculation using B3LYP/6-311++G(3df,3pd) with the built-in ECP28MWB_SEG effective core potential for Ce. Ensure all final structures have no imaginary frequencies. Save the full calculation output files as evidence.
- Evidence: `/app/outputs/dft_outputs.zip`

### Step 2: Extract and format computed vibrational frequencies
- Role: scored (load-bearing)
- Action: Parse the harmonic vibrational frequencies (cm⁻¹) and infrared intensities (km/mol) from the DFT output files. For each isomer and isotopologue (H or D), record every computed normal mode with a brief description of the dominant motion (e.g., 'Ce-H stretch', 'Si-H bridge stretch'). Write the results to computed_frequencies.csv.
- Output file: `/app/outputs/computed_frequencies.csv`
- Format: csv
- Contract: Columns: isomer (string), isotopologue (string, 'H' or 'D'), mode_description (string), frequency_cm1 (float), intensity_km_mol (float). Each row corresponds to one vibrational mode.
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
- target_policy: threshold_or_better
- description: Computed harmonic vibrational frequencies and IR intensities for the five product molecules and their deuterated isotopologues.
- schema:
  - `type`: table
  - `columns`:
    - `name`: isomer
    - `type`: string
    - `description`: Name of the molecule (e.g., 'Si(mu-H)3CeH', 'H3SiCeH', 'H2Si(mu-H)CeH', 'HSi(mu-H)2CeH', or 'H3CCeH')
    - `name`: isotopologue
    - `type`: string
    - `values`: `H`, `D`
    - `description`: Isotopologue label: 'H' for all-hydrogen, 'D' for fully deuterated.
    - `name`: mode_description
    - `type`: string
    - `description`: Brief description of the vibrational mode (e.g., 'Ce-H stretch', 'Si-H bridge stretch').
    - `name`: frequency_cm1
    - `type`: float
    - `units`: cm-1
    - `description`: Harmonic vibrational frequency in wavenumbers.
    - `name`: intensity_km_mol
    - `type`: float
    - `units`: km/mol
    - `description`: IR intensity.

Notes: The hidden checker matches the computed frequencies to the paper's reported experimental modes and calculates the mean absolute percentage error (MAPE). Scoring is monotonic: MAPE ≤ 5% earns full credit; credit linearly degrades from 1.0 at 5% to 0.0 at 10%; above 10% scores 0. The checker also performs a low-weight structural check of isotopic frequency ratios, but the main score is driven by the MAPE threshold.

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
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "columns": [
          {
            "name": "isomer",
            "type": "string",
            "description": "Name of the molecule (e.g., 'Si(mu-H)3CeH', 'H3SiCeH', 'H2Si(mu-H)CeH', 'HSi(mu-H)2CeH', or 'H3CCeH')"
          },
          {
            "name": "isotopologue",
            "type": "string",
            "values": [
              "H",
              "D"
            ],
            "description": "Isotopologue label: 'H' for all-hydrogen, 'D' for fully deuterated."
          },
          {
            "name": "mode_description",
            "type": "string",
            "description": "Brief description of the vibrational mode (e.g., 'Ce-H stretch', 'Si-H bridge stretch')."
          },
          {
            "name": "frequency_cm1",
            "type": "float",
            "units": "cm-1",
            "description": "Harmonic vibrational frequency in wavenumbers."
          },
          {
            "name": "intensity_km_mol",
            "type": "float",
            "units": "km/mol",
            "description": "IR intensity."
          }
        ]
      },
      "description": "Computed harmonic vibrational frequencies and IR intensities for the five product molecules and their deuterated isotopologues."
    }
  ],
  "notes": "The hidden checker matches the computed frequencies to the paper's reported experimental modes and calculates the mean absolute percentage error (MAPE). Scoring is monotonic: MAPE ≤ 5% earns full credit; credit linearly degrades from 1.0 at 5% to 0.0 at 10%; above 10% scores 0. The checker also performs a low-weight structural check of isotopic frequency ratios, but the main score is driven by the MAPE threshold."
}
```

## How you are scored
A hidden verifier reads your `computed_frequencies.csv` and compares the harmonic vibrational frequencies you report to the experimentally observed frequencies from the original matrix isolation study. It calculates a quantitative measure of agreement (e.g., a percentage error) between your predictions and the reference experimental values for the assigned modes. A higher agreement yields a higher score, with full credit awarded when the agreement meets or exceeds a predetermined quality threshold. Additionally, the verifier checks that the relative isotopic (H/D) frequency ratios for each mode are physically reasonable, contributing a small secondary component to the total score. The final reward is a weighted combination of these checks; the primary weight rests on the accuracy of the computed frequencies. You must also save the DFT calculation output files as `dft_outputs.zip` for audit, but the CSV is the only scored artifact.
