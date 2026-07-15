# Phonon Frequency Calculation for Undistorted GdTe₃ Cmcm Structure

## Problem background
GdTe₃ is a layered rare-earth tritelluride that hosts a charge density wave (CDW) transition well above room temperature. Understanding its vibrational properties is essential for assigning the Raman-active phonon modes observed in experiments. First-principles harmonic phonon calculations in the undistorted orthorhombic structure (space group Cmcm) provide the Γ-point mode frequencies and symmetries needed to interpret the measured spectra. This task reproduces that dry‑lab computational characterization.

## Approach
The computational pipeline combines plane‑wave density functional theory (DFT) with the finite‑displacement method for phonons. Starting from the experimental lattice constants (a = 4.32 Å, b = 25.57 Å, c = 4.33 Å) and the Cmcm space group, the internal atomic positions are relaxed using the PBE exchange‑correlation functional. From the relaxed structure, a series of displaced configurations is generated, forces are computed with the same DFT settings, and the harmonic interatomic force constants are built to obtain the full set of Γ‑point phonon frequencies. Finally, the 12 Raman‑active modes (4 Ag, 4 B1g, 4 B3g) are identified by symmetry analysis.

## Reproduction target
Produce a CSV file containing the frequencies (in cm⁻¹) and symmetry labels of all 12 Raman‑active Γ‑point phonon modes of GdTe₃ in the undistorted Cmcm structure, computed with PBE and the fixed experimental lattice constants. The file must have exactly 12 rows with columns `symmetry` (one of Ag, B1g, B3g) and `frequency` (float), sorted by frequency within each symmetry.

## Assets

- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: phonopy

## Workflow steps

### Step 1: DFT structural relaxation of GdTe₃
- Role: process
- Action: Perform a DFT structural relaxation of the primitive cell of GdTe₃ in the orthorhombic Cmcm space group using an open-source plane-wave DFT code (e.g., Quantum ESPRESSO). Use the experimental lattice constants a=4.32 Å, b=25.57 Å, c=4.33 Å and relax the internal atomic positions. Use the PBE exchange-correlation functional and appropriate pseudopotentials. Save the relaxed atomic coordinates.
- Evidence: `/app/outputs/relaxed_structure.qe.in`

### Step 2: Phonon calculation via finite displacement
- Role: process
- Action: Using the relaxed structure from step 1, perform a phonon calculation with the finite-displacement method using a phonon package (e.g., Phonopy). Generate displaced configurations, compute forces for each with the same DFT code and parameters, and build the harmonic interatomic force constants to obtain Γ-point phonon frequencies for all optical modes.
- Evidence: `/app/outputs/phonon_full_frequencies.log`

### Step 3: Extract Raman-active mode frequencies
- Role: scored (load-bearing)
- Action: From the full set of Γ-point phonon frequencies obtained in step 2, identify the 12 Raman-active modes of the undistorted Cmcm structure using symmetry analysis (the allowed Raman-active representations are 4Ag, 4B1g, 4B3g). Output a CSV file with columns 'symmetry' (string, one of Ag, B1g, B3g) and 'frequency' (float, units cm⁻¹) with exactly 12 rows, sorted by frequency within each symmetry.
- Output file: `/app/outputs/phonon_frequencies.csv`
- Format: csv
- Contract: Columns: symmetry (string, allowed values Ag, B1g, B3g), frequency (float, units cm⁻¹). Exactly 12 rows: 4 Ag, 4 B1g, 4 B3g.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/phonon_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### phonon_frequencies.csv
- path: `/app/outputs/phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Scored artifact: the computed Γ‑point Raman-active phonon frequencies with symmetry labels for undistorted GdTe₃. The hidden checker compares each frequency to the paper’s reported values with an appropriate tolerance and verifies the symmetry count.
- schema:
  - `type`: table
  - `required_columns`: `symmetry`, `frequency`
  - `columns`:
    - `symmetry`:
      - `type`: string
      - `allowed`: `Ag`, `B1g`, `B3g`
    - `frequency`:
      - `type`: number
      - `unit`: cm⁻¹
  - `row_count`: 12
  - `description`: Each row is a Raman-active mode. There must be exactly 4 rows per symmetry label.

Notes: This is the sole scored artifact. The checker will verify the correct number of rows and allowed symmetry labels, then compare frequencies against hidden reference values from the paper’s Table I.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "symmetry",
          "frequency"
        ],
        "columns": {
          "symmetry": {
            "type": "string",
            "allowed": [
              "Ag",
              "B1g",
              "B3g"
            ]
          },
          "frequency": {
            "type": "number",
            "unit": "cm⁻¹"
          }
        },
        "row_count": 12,
        "description": "Each row is a Raman-active mode. There must be exactly 4 rows per symmetry label."
      },
      "description": "Scored artifact: the computed Γ‑point Raman-active phonon frequencies with symmetry labels for undistorted GdTe₃. The hidden checker compares each frequency to the paper’s reported values with an appropriate tolerance and verifies the symmetry count."
    }
  ],
  "notes": "This is the sole scored artifact. The checker will verify the correct number of rows and allowed symmetry labels, then compare frequencies against hidden reference values from the paper’s Table I."
}
```

## How you are scored
A hidden verifier inspects each workflow artifact and assigns a reward. The main scored artifact is `phonon_frequencies.csv`. The verifier checks that it contains exactly 12 rows with the required symmetry counts (4 Ag, 4 B1g, 4 B3g) and compares the reported frequencies against hidden reference values. The reward is proportional to the fraction of modes whose frequency lies within an acceptable margin of the reference. Supporting evidence from the relaxation and phonon steps is also audited, but the bulk of the score comes from the accuracy of the Raman‑mode frequencies. Note that simply reporting known numbers without executing the actual calculations will not satisfy the verifier.
