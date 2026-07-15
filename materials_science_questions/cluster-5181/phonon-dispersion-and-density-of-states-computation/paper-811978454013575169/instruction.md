# Phonon Dispersion Curves for Cu and Ag

## Problem background
Phonon dispersion relations describe how lattice vibrational frequencies depend on wave vector. In fcc metals like copper and silver, a realistic model must account for central pairwise interactions, angular forces resisting bond bending, and the response of the conduction electrons. The classic Sharma-Joshi model incorporates all three contributions but originally used an approximate expression for the electron-ion coupling (Bardeen's G-function). Improved results may be obtained by replacing that approximation with an exact G-function derived for fcc crystals (the Bross-Bohn form). This task computes the phonon dispersion curves for Cu and Ag within such a modified Sharma-Joshi model.

## Approach
Use a lattice dynamical model that includes central forces up to second neighbours (constants A1, A2), angular forces up to second neighbours (parameters a^-2 K1, a^-2 K2), and a conduction-electron term proportional to a Ke multiplied by the squared Bross-Bohn G(q) function for fcc. For a given wave vector, build the 3×3 dynamical matrix from these constants and the G-function; its eigenvalues yield the squared angular frequencies. The vibrational frequencies are then ν = sqrt(eigenvalue)/(2π). All force constants, lattice constants, and atomic masses for copper and silver are provided. The computation is carried out for wave vectors along the three high-symmetry directions [100], [110], and [111].

## Reproduction target
Compute phonon frequencies for copper and silver along the [100] (qx,0,0), [110] (qx,qx,0), and [111] (qx,qx,qx) directions with reduced wave vector qx from 0.0 to 1.0 in steps of 0.1, using the provided force constants, lattice parameters, and atomic masses. Output the three frequency branches (in units of 10^12 Hz) in two TSV files: copper_dispersion.tsv and silver_dispersion.tsv.

## Assets

- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Compute copper phonon dispersion
- Role: scored
- Action: Implement the 3x3 dynamical matrix for an fcc lattice with central and angular force constants and the electron-ion term described by the exact Bross-Bohn expression for Bardeen's G(q). For copper, use the force constants A1=35.228, A2=1.875, a^-2 K1=-0.040, a^-2 K2=-0.988, a Ke=0.1113 in units of 10^3 dyn/cm, lattice constant a=3.616 Å, and atomic mass M=63.55 u (convert to grams: 1 u = 1.660539e-24 g). For wave vectors along [100] (qx,0,0), [110] (qx,qx,0), [111] (qx,qx,qx) with qx from 0.0 to 1.0 in steps of 0.1, diagonalize the dynamical matrix to obtain eigenvalues; angular frequency ω = sqrt(eigenvalue), convert to frequency ν = ω/(2π) in Hz and output in units of 10^12 Hz.
- Output file: `/app/outputs/copper_dispersion.tsv`
- Format: tsv
- Contract: TSV with header: qx, qy, qz, freq1, freq2, freq3 (all float). freq in units of 10^12 Hz. Each row represents one q-point along the three symmetry directions (33 rows).
- Scoring: scored by hidden verifier

### Step 2: Compute silver phonon dispersion
- Role: scored
- Action: Using the same dynamical matrix implementation as for copper, but with the silver force constants A1=30.030, A2=0.675, a^-2 K1=0.280, a^-2 K2=-1.402, a Ke=1.346 (10^3 dyn/cm), lattice constant a=4.08 Å, and atomic mass M=107.87 u (convert to grams), compute the phonon frequencies for the same set of q-points along [100], [110], [111] with qx from 0.0 to 1.0 in steps of 0.1. Output frequencies in 10^12 Hz.
- Output file: `/app/outputs/silver_dispersion.tsv`
- Format: tsv
- Contract: TSV with header: qx, qy, qz, freq1, freq2, freq3 (all float). freq in units of 10^12 Hz. Each row represents one q-point along the three symmetry directions (33 rows).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/copper_dispersion.tsv`
- `/app/outputs/silver_dispersion.tsv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### copper_dispersion.tsv
- path: `/app/outputs/copper_dispersion.tsv`
- format: tsv
- purpose: scored
- target_policy: exact_match
- description: Phonon frequencies for copper along high-symmetry directions.
- schema:
  - `type`: table
  - `required_columns`: `qx`, `qy`, `qz`, `freq1`, `freq2`, `freq3`
  - `units`:
    - `freq1`: 10^12 Hz
    - `freq2`: 10^12 Hz
    - `freq3`: 10^12 Hz

### silver_dispersion.tsv
- path: `/app/outputs/silver_dispersion.tsv`
- format: tsv
- purpose: scored
- target_policy: exact_match
- description: Phonon frequencies for silver along high-symmetry directions.
- schema:
  - `type`: table
  - `required_columns`: `qx`, `qy`, `qz`, `freq1`, `freq2`, `freq3`
  - `units`:
    - `freq1`: 10^12 Hz
    - `freq2`: 10^12 Hz
    - `freq3`: 10^12 Hz

Notes: Force constants and all input parameters are provided in the instruction. No external datasets are needed; the checker recomputes frequencies from the same parameters.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "copper_dispersion.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "qx",
          "qy",
          "qz",
          "freq1",
          "freq2",
          "freq3"
        ],
        "units": {
          "freq1": "10^12 Hz",
          "freq2": "10^12 Hz",
          "freq3": "10^12 Hz"
        }
      },
      "description": "Phonon frequencies for copper along high-symmetry directions."
    },
    {
      "file": "silver_dispersion.tsv",
      "format": "tsv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "qx",
          "qy",
          "qz",
          "freq1",
          "freq2",
          "freq3"
        ],
        "units": {
          "freq1": "10^12 Hz",
          "freq2": "10^12 Hz",
          "freq3": "10^12 Hz"
        }
      },
      "description": "Phonon frequencies for silver along high-symmetry directions."
    }
  ],
  "notes": "Force constants and all input parameters are provided in the instruction. No external datasets are needed; the checker recomputes frequencies from the same parameters."
}
```

## How you are scored
A hidden verifier independently recomputes phonon frequencies for both metals using the same dynamical matrix and force constants. For each metal it compares your submitted frequencies (every q-point and branch) to its recomputed values. The score is the fraction of (q-point, branch) pairs whose absolute difference falls within a hidden tolerance, averaged over copper and silver; the task is considered correct if this average fraction meets or exceeds a hidden pass threshold. Merely reporting the paper's numbers is not sufficient — the verifier checks the actual computation.
