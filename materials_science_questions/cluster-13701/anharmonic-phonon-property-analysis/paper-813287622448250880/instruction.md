# DFT Phonon Calculation and Mode Assignment for LiNH2

## Problem background
LiNH2 is a hydrogen storage material with a tetragonal crystal structure (space group I\bar{4}). Understanding its lattice dynamics is essential for explaining its temperature-dependent behaviour and the weak interaction between Li and the NH2 group. A complete assignment of its Raman-active phonon modes is needed to separate external vibrations from the internal NH2 molecular vibrations and to identify anharmonic modes. This task obtains such an assignment by computing the zone-centre phonon frequencies and their irreducible representation symmetries from first principles.

## Approach
The approach combines a group-theoretic factor analysis of the LiNH2 crystal structure with a first-principles phonon calculation. The phonon calculation uses density-functional perturbation theory (DFPT) as implemented in the ABINIT package, with the local density approximation (LDA) for exchange-correlation, Troullier-Martins pseudopotentials, a plane-wave kinetic energy cutoff of 68 Ry, and a 4×4×4 Monkhorst-Pack k-point mesh. Starting from the experimental crystal structure, the atomic positions are relaxed at fixed lattice constants, and the Γ-point phonon frequencies and eigenvectors are computed. The obtained frequencies are then labelled with irreducible representations (A, B, or E) by matching the modes to the predictions of the factor group analysis.

## Reproduction target
Provide the following two files:

- `group_theory_summary.txt`: A plain-text summary of the factor group analysis, giving the number of Raman-active modes of each symmetry (A, B, E) in the phonon region (0–700 cm⁻¹) and in the NH2 molecular vibration region (bending and stretching).

- `computed_phonon_frequencies.csv`: A CSV table with 33 rows, columns: `mode_number` (integer 1–33), `symmetry` (A, B, or E), `frequency_rt` (computed frequency in cm⁻¹), `region` (I for phonon, II for bending, III for stretching). The rows must be ordered as: the 24 phonon modes (region I), the 3 bending modes (region II), the 6 stretching modes (region III).

## Assets

- ABINIT: https://www.abinit.org
- Troullier-Martins LDA pseudopotentials for Li, N, H: https://www.abinit.org/downloads/psp-links/psp-lda
- LiNH2 crystal structure (Sørby et al.)

## Workflow steps

### Step 1: Group Theory Analysis
- Role: scored
- Action: Using the crystal structure (space group I\bar{4}, atomic coordinates given), perform factor group analysis to determine the irreducible representations of the zone-center phonon modes. Count the number of Raman-active modes of each symmetry (A, B, E) in the phonon region (0-700 cm^{-1}) and in the NH2 molecular vibration region (bending and stretching).
- Output file: `/app/outputs/group_theory_summary.txt`
- Format: txt
- Contract: Text file containing the group theory analysis results: for each region (phonon, molecular vibration) list the counts of A, B, and E symmetry modes, the total number of modes, and any key selection rules.
- Scoring: scored by hidden verifier

### Step 2: DFT Phonon Calculation
- Role: process
- Action: Run ABINIT with LDA, Troullier-Martins pseudopotentials, to optimize atomic positions (with fixed experimental lattice constants) and compute Γ-point phonon frequencies via density-functional perturbation theory. Save the raw ABINIT output.
- Evidence: `/app/outputs/abinit_output.log`

### Step 3: Compile Computed Frequencies and Symmetry Assignments
- Role: scored (load-bearing)
- Action: From the ABINIT output and the group theory symmetry predictions, assign each computed phonon mode an irreducible representation (A, B, or E). Produce a CSV table with all 33 assigned modes ordered as: the 24 phonon modes (region I), then 3 bending modes (region II), then 6 stretching modes (region III).
- Output file: `/app/outputs/computed_phonon_frequencies.csv`
- Format: csv
- Contract: CSV file with columns: mode_number (integer, 1-33), symmetry (string: A, B, or E), frequency_rt (float, cm^{-1}), region (string: I, II, or III). Rows correspond to the assigned modes, ordered as described.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/group_theory_summary.txt`
- `/app/outputs/computed_phonon_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### group_theory_summary.txt
- path: `/app/outputs/group_theory_summary.txt`
- format: txt
- purpose: scored
- target_policy: reference_match
- description: Group theory mode classification for LiNH2, listing the number of Raman-active modes of A, B, and E symmetry in the phonon and molecular vibration regions.
- schema:
  - `type`: text
  - `description`: Text summary of group theory analysis containing mode counts per symmetry and region.

### computed_phonon_frequencies.csv
- path: `/app/outputs/computed_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV table of 33 assigned Γ-point phonon frequencies and symmetry labels from the first-principles calculation.
- schema:
  - `type`: table
  - `required_columns`: `mode_number`, `symmetry`, `frequency_rt`, `region`
  - `units`:
    - `frequency_rt`: cm^{-1}

Notes: Only the first-principles DFT phonon calculation and group theory analysis are reproduced. Experimental Raman data and derived analyses are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "group_theory_summary.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "text",
        "description": "Text summary of group theory analysis containing mode counts per symmetry and region."
      },
      "description": "Group theory mode classification for LiNH2, listing the number of Raman-active modes of A, B, and E symmetry in the phonon and molecular vibration regions."
    },
    {
      "file": "computed_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "mode_number",
          "symmetry",
          "frequency_rt",
          "region"
        ],
        "units": {
          "frequency_rt": "cm^{-1}"
        }
      },
      "description": "CSV table of 33 assigned Γ-point phonon frequencies and symmetry labels from the first-principles calculation."
    }
  ],
  "notes": "Only the first-principles DFT phonon calculation and group theory analysis are reproduced. Experimental Raman data and derived analyses are excluded."
}
```

## How you are scored
A hidden verifier scores your outputs by comparing them to a reference. For `group_theory_summary.txt`, it checks that the mode counts per symmetry and region match the expected numbers derived from group theory. For `computed_phonon_frequencies.csv`, each frequency is compared to a reference value (with a tolerance that accounts for the spread of different DFT implementations), and the symmetry labels are verified. The final reward is a weighted sum, with the frequency table carrying the largest weight. Reporting a number that is merely close to the paper's published value is not sufficient; the values must come from having executed the full ABINIT phonon calculation and the correct group theory assignment.
