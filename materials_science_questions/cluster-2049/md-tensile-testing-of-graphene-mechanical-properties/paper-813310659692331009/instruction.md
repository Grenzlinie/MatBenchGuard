# Band gaps of bent graphene nanoribbons via DFTB

## Problem background
Graphene nanoribbons (GNRs) are atomically thin and flimsy; when supported on a substrate, they may be subject to gentle planar bends due to fabrication, adhesion, and manipulations. The effect of such bending on the electronic properties remains an open question. This task investigates how bending modifies the energy gap of two common types of GNRs: armchair (AGNR) and zigzag (ZGNR). Using density-functional tight-binding (DFTB) simulations, you will compute the band gaps for ribbons of various widths under controlled bending. The goal is to quantify the gap as a function of bending and ribbon width, and to verify the behaviour against the analytical trends reported in the original study.

## Approach
You will simulate pristine hydrogen-passivated AGNR and ZGNR using the hotbit DFTB code with the pbc-0-3 parameter set. The bent geometry is modelled by revised periodic boundary conditions: the simulation cell consists of a translational unit of length L, and the symmetry operation is a rotation of angle α around an axis perpendicular to the ribbon plane. By varying α you achieve a desired bending parameter Θ = W/(2R), where W is the ribbon width and R is the mean radius of curvature. For each ribbon type you will select a set of representative widths. For each width, a range of bending parameters Θ from 0 to 0.1 will be considered. For every (width, Θ) combination, you must: (i) generate the initial atomic coordinates with the chosen curvature, (ii) perform geometry optimization with a tight force convergence criterion, (iii) compute the electronic band structure with sufficient k-point sampling, and (iv) extract the HOMO‑LUMO band gap. The computed gaps are to be compiled in a CSV file for later verification. The analytical relations presented in the paper predict how the gap depends on width and Θ; your computed numbers will be compared against those expected values.

## Reproduction target
Produce the file `bending_gap_results.csv` under `/app/outputs` containing the computed band gaps for all simulated configurations. The CSV must have exactly the following columns:
- `ribbon_type`: string, either "AGNR" or "ZGNR".
- `width`: the ribbon width in angstroms (Å).
- `bend_parameter_Theta`: the dimensionless bending parameter Θ (float).
- `computed_band_gap_eV`: the HOMO‑LUMO band gap in electronvolts (eV).
- `family`: for **AGNR** only, the family index q = N mod 3 where N is the number of dimer lines across the width. Use integer 0, 1, or 2 (e.g., 10‑AGNR → 1). For **ZGNR**, leave this field empty or write "N/A".

Your simulation set must cover at least three different widths for each ribbon type. For AGNRs, prefer widths belonging to families 0 or 1 (e.g., N=10,16,22 give q=1; N=12,18,24 give q=0) to avoid ambiguous fallback inference. For each width, include at least six values of Θ evenly distributed between 0 and 0.1 (e.g., 0.0, 0.02, 0.04, 0.06, 0.08, 0.10). Every row corresponds to one DFTB calculation. No other output files are required for scoring, but you may keep intermediate files if needed.

## Assets

- hotbit DFTB code: https://github.com/pekkosk/hotbit
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: Generate bent GNR geometries
- Role: process
- Action: For each ribbon type (AGNR and ZGNR), each selected width (at least three per type), and each bending parameter Θ from 0 to 0.1, use revised periodic boundary conditions to generate initial atomic coordinates with the desired curvature.
- Evidence: none

### Step 2: Run DFTB geometry optimization and band structure calculations
- Role: process
- Action: For each geometry, run DFTB geometry optimization with tight force criteria using hotbit with the pbc-0-3 parameter set, then compute the electronic band structure.
- Evidence: none

### Step 3: Compile band gaps into CSV
- Role: scored (load-bearing)
- Action: From the computed band structures, extract the HOMO-LUMO band gap for each configuration. Write a CSV file with columns: ribbon_type, width (Å), bend_parameter_Theta, computed_band_gap_eV, and family. Ensure at least 3 widths per ribbon type and 6 Θ values, and that the family is correctly reported for each AGNR row.
- Output file: `/app/outputs/bending_gap_results.csv`
- Format: csv
- Contract: CSV with columns: ribbon_type (string), width (float, in Angstrom), bend_parameter_Theta (float), computed_band_gap_eV (float), family (integer 0‑2 for AGNR; empty string for ZGNR). Each row corresponds to one simulation.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bending_gap_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bending_gap_results.csv
- path: `/app/outputs/bending_gap_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: CSV of band gaps for all bent GNR simulations; family column required for correct analytical gap comparison.
- schema:
  - `type`: table
  - `required_columns`: `ribbon_type`, `width`, `bend_parameter_Theta`, `computed_band_gap_eV`, `family`
  - `units`:
    - `width`: Angstrom
    - `computed_band_gap_eV`: eV
  - `notes`: family is an integer (0,1,2) for AGNR rows; empty string for ZGNR rows.

Notes: The checker will compute the expected band gap from the paper's fitted analytical relations for AGNRs and ZGNRs using the reported family where applicable, and compare within tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bending_gap_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "ribbon_type",
          "width",
          "bend_parameter_Theta",
          "computed_band_gap_eV",
          "family"
        ],
        "units": {
          "width": "Angstrom",
          "computed_band_gap_eV": "eV"
        },
        "notes": "family is an integer (0,1,2) for AGNR rows; empty string for ZGNR rows."
      },
      "description": "CSV of band gaps for all bent GNR simulations; family column required for correct analytical gap comparison."
    }
  ],
  "notes": "The checker will compute the expected band gap from the paper's fitted analytical relations for AGNRs and ZGNRs using the reported family where applicable, and compare within tolerance."
}
```

## How you are scored
Your submission is scored by a hidden verifier that evaluates the `bending_gap_results.csv` file. For each row, the verifier independently computes the expected band gap using the analytical relations derived in the original paper (which depend on `ribbon_type`, `width`, and `bend_parameter_Theta`). It then compares your `computed_band_gap_eV` to this expected value within a tolerance. Your reward is the fraction of rows that satisfy the agreement criterion, linearly scaled between 0 and 1. The verifier does not require any other files, and the reward is based solely on the agreement of your computed gaps with the paper‑derived predictions.
