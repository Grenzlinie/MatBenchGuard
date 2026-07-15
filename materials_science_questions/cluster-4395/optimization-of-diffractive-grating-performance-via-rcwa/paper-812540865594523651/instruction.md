# Quasi-Static Cascade ABCD/S-Matrix Frequency Response Computation

## Problem background
Multilayer dielectric structures with subwavelength strip-conductor gratings (inductive grids and capacitive patches) can act as high-performance bandpass filters. An efficient quasi-static two-port network approach models each grating as a scattering (S) matrix with closed-form admittance, and dielectrics as ABCD matrices; cascading them produces the overall filter frequency response. This task reproduces the model by implementing the cascade from scratch, computing the insertion loss and return loss over a frequency range for a specific prototype, and outputting a CSV file.

## Approach
The filter is modeled as a cascade connection of planar two-port elements: inductive grid gratings (square gaps), capacitive patch gratings (square patches), and uniform dielectric slabs. The approach uses a quasi-static approximation valid when the grating period is subwavelength. For each grating, the complex surface admittance Y is derived from closed-form expressions combining an inductive term and a capacitive term (for grids, the inductive term dominates; for patches, the capacitive term dominates; the patch inductance requires a double integral). The Y is used to form the grating's 2×2 S-matrix with the adjacent media permittivities. That S-matrix is then converted to an ABCD matrix. Each dielectric layer (given thickness h, complex permittivity) contributes its own ABCD transmission-line matrix. The cascade order is: outer inductive grid, dielectric, capacitive patch, dielectric, inner inductive grid, dielectric, capacitive patch, dielectric, inner inductive grid, dielectric, capacitive patch, dielectric, outer inductive grid. The product of all ABCD matrices is converted back to S-parameters to yield complex S21 and S11. The insertion loss and return loss in dB are computed from |S21| and |S11| over a frequency sweep.

## Reproduction target
Compute the insertion loss S21_dB and return loss S11_dB for a third-order bandpass filter prototype with the following design parameters: grid period T = 3.0 mm, dielectric layer thickness h = 1.29 mm, relative permittivity ε_r = 11.2, loss tangent tanδ = 0.0022; outer inductive grid gap s_L1 = 2.846 mm; inner inductive grid gap s_L2 = 1.570 mm; capacitive patch widths w_C1 = 1.770 mm, w_C2 = 2.205 mm. Sweep frequency from 8 GHz to 18 GHz in steps of 10 MHz, and write a CSV file /app/outputs/frequency_response.csv with columns f (Hz), S21_dB, S11_dB.

## Assets

- numpy: numpy
- scipy: scipy

## Workflow steps

### Step 1: Compute quasistatic cascade frequency response and write CSV
- Role: scored (load-bearing)
- Action: Implement the quasi-static two-port network cascade model: (a) Compute the complex surface admittance Y for each inductive grid (square gaps) and each capacitive patch (square patches) using the closed-form quasi-static expressions (include the double integral for patch inductance). (b) Form the 2×2 scattering (S) matrix for each grating using the admittance Y and the permittivities of the adjacent media. (c) Convert each grating S-matrix to an ABCD matrix using the algebraic S→ABCD conversion. (d) Compute the ABCD matrix of each dielectric layer (thickness h = 1.29 mm, relative permittivity ε_r = 11.2, loss tangent tanδ = 0.0022) using the transmission-line formula for a uniform slab with complex permittivity. (e) Multiply all ABCD matrices in the cascade order: (port 1) Inductive(s_L1) – Dielectric(h) – Capacitive(w_C1) – Dielectric(h) – Inductive(s_L2) – Dielectric(h) – Capacitive(w_C2) – Dielectric(h) – Inductive(s_L2) – Dielectric(h) – Capacitive(w_C1) – Dielectric(h) – Inductive(s_L1) (port 2). (f) Convert the overall ABCD matrix back to an S-matrix to obtain complex S21 and S11 at each frequency. (g) Sweep frequency from 8×10^9 to 18×10^9 Hz with a step of 10 MHz, compute the insertion loss S21_dB = 20 log10(|S21|) and return loss S11_dB = 20 log10(|S11|), and write the results to /app/outputs/frequency_response.csv.
- Output file: `/app/outputs/frequency_response.csv`
- Format: csv
- Contract: CSV with header: f,S21_dB,S11_dB. f (float, Hz), S21_dB (float, dB), S11_dB (float, dB). Frequency range from 8e9 to 18e9 inclusive, step no larger than 10 MHz.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/frequency_response.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### frequency_response.csv
- path: `/app/outputs/frequency_response.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Frequency response (insertion loss and return loss) of the bandpass filter computed via the quasi-static cascade ABCD/S-matrix model.
- schema:
  - `type`: table
  - `required_columns`: `f`, `S21_dB`, `S11_dB`
  - `units`:
    - `f`: Hz
    - `S21_dB`: dB
    - `S11_dB`: dB

Notes: The CSV must contain rows for frequencies from 8e9 to 18e9 Hz in 10 MHz steps (inclusive). The hidden reference CSV is generated from the same quasi-static model with the provided prototype parameters; close agreement is expected.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "frequency_response.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "S21_dB",
          "S11_dB"
        ],
        "units": {
          "f": "Hz",
          "S21_dB": "dB",
          "S11_dB": "dB"
        }
      },
      "description": "Frequency response (insertion loss and return loss) of the bandpass filter computed via the quasi-static cascade ABCD/S-matrix model."
    }
  ],
  "notes": "The CSV must contain rows for frequencies from 8e9 to 18e9 Hz in 10 MHz steps (inclusive). The hidden reference CSV is generated from the same quasi-static model with the provided prototype parameters; close agreement is expected."
}
```

## How you are scored
A hidden verifier will run after your submission. It will load your /app/outputs/frequency_response.csv and compare each row's S21_dB and S11_dB values to a reference CSV generated from the exact same quasi-static model and prototype parameters. For each frequency point, the verifier checks whether your computed losses are within acceptable agreement of the reference. If your entire frequency sweep is present and all points pass the comparison, you receive full credit (1.0). Points that are missing or deviate beyond tolerance reduce the reward proportionally. The reference values are hidden; you must produce them by correctly implementing the model, not by guessing or looking up the answer. The scoring reward is continuous between 0 and 1 based on the fraction of passing points.
