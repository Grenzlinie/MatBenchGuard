# Size-Dependent Optical Gap of Hydrogen-Passivated Silicon Quantum Dots via DFT-LDA

## Problem background
The optical band gap of silicon quantum dots (QDs) depends strongly on their size due to quantum confinement. Accurate computational prediction of the size-dependent gap remains challenging, especially with density functional theory (DFT), which is known to underestimate band gaps but is commonly used to study ground-state properties of nanostructures. This task investigates whether a DFT-LDA calculation with numerical atomic orbitals, combined with a constant exchange-correlation discontinuity correction, can capture the size-dependent HOMO-LUMO gap of hydrogen-passivated silicon quantum dots.

## Approach
The workflow uses density functional theory with the local density approximation (LDA) and the Perdew-Zunger parametrization, as implemented in the open-source package OpenMX. Norm-conserving pseudopotentials are employed, with a double-zeta polarized (DZP) basis set for silicon and a single-zeta (SZ) basis set for hydrogen.

First, the chosen computational parameters are validated on bulk silicon: an LDA band-structure calculation is performed for face-centered cubic (FCC) silicon at its standard lattice constant, and the resulting HOMO-LUMO gap is extracted. Next, spherical silicon clusters of different diameters are carved from the FCC lattice, and surface dangling bonds are saturated with hydrogen atoms to model passivated quantum dots. The atomic structures of these passivated clusters are then optimized via the Quasi-Newton BFGS method within DFT-LDA. Finally, self-consistent field calculations at the Gamma point yield the raw HOMO-LUMO gaps. A constant exchange-correlation discontinuity correction (taken from the literature) is added to each raw gap to obtain a corrected gap. Comparing the corrected gaps across at least three dot sizes reveals the size-dependence of the optical gap.

## Reproduction target
Produce two scored artifacts:

1. A text file (`bulk_si_gap.txt`) containing a single floating-point number: the raw LDA HOMO-LUMO gap (in eV) of bulk FCC silicon.
2. A CSV file (`qd_gaps.csv`) with the raw and corrected HOMO-LUMO gaps (in eV) for at least three hydrogen-passivated silicon quantum dots of different diameters. The CSV must have columns `qd_name`, `diameter_nm`, `raw_gap_eV`, `corrected_gap_eV`. The corrected gap should equal the raw gap plus the constant exchange-correlation discontinuity correction of 0.58 eV. The corrected gaps across different dot sizes should demonstrate a systematic size dependence.

## Assets

- OpenMX (Open source package for Material eXplorer): http://www.openmx-square.org/

## Workflow steps

### Step 1: Bulk Silicon LDA Gap Calculation
- Role: scored
- Action: Using OpenMX with double-zeta polarized (DZP) basis for Si, LDA-PZ exchange-correlation functional, and norm-conserving pseudopotentials, perform a DFT-LDA band-structure calculation for face-centered cubic (FCC) silicon at the standard lattice constant. Extract the ground-state HOMO-LUMO energy gap and write it as a single floating-point number (in eV) to the output file.
- Output file: `/app/outputs/bulk_si_gap.txt`
- Format: txt
- Contract: A single line containing the HOMO-LUMO gap value in eV (e.g., 0.55).
- Scoring: scored by hidden verifier

### Step 2: Construct passivated Si-QD atomic models
- Role: process
- Action: Carve spherical Si clusters of various diameters (e.g., 0.6 nm, 1.0 nm, 1.9 nm) from the FCC silicon lattice. Saturate surface dangling bonds with hydrogen atoms to create passivated quantum dots. Keep at least three distinct cluster sizes.
- Evidence: none

### Step 3: Geometry optimization of QD models
- Role: process
- Action: For each constructed cluster, perform geometry relaxation using the Quasi-Newton BFGS method within DFT-LDA (same OpenMX parameters: DZP for Si, single-zeta for H, LDA-PZ functional, norm-conserving pseudopotentials).
- Evidence: none

### Step 4: Compute and correct HOMO-LUMO gaps for passivated QDs
- Role: scored (load-bearing)
- Action: Run self-consistent field DFT-LDA calculations (Gamma-point) for each optimized QD using the same OpenMX settings (DZP basis for Si, SZ for H, LDA-PZ functional, norm-conserving pseudopotentials). Extract the raw HOMO-LUMO energy gap. Add the constant exchange-correlation discontinuity correction of 0.58 eV to each raw gap to obtain the corrected gap. Compile the results into a CSV file with columns: qd_name (string), diameter_nm (float), raw_gap_eV (float), corrected_gap_eV (float). Include at least three rows for different QD sizes.
- Output file: `/app/outputs/qd_gaps.csv`
- Format: csv
- Contract: CSV with header qd_name,diameter_nm,raw_gap_eV,corrected_gap_eV. Each row corresponds to one QD size.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/bulk_si_gap.txt`
- `/app/outputs/qd_gaps.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### bulk_si_gap.txt
- path: `/app/outputs/bulk_si_gap.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Validation of DFT-LDA parameters by reproducing the bulk silicon LDA gap.
- schema:
  - `type`: text
  - `description`: A single floating-point number representing the HOMO-LUMO gap in eV.

### qd_gaps.csv
- path: `/app/outputs/qd_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Size-dependent raw and corrected HOMO-LUMO gaps for hydrogen-passivated Si quantum dots.
- schema:
  - `type`: table
  - `required_columns`: `qd_name`, `diameter_nm`, `raw_gap_eV`, `corrected_gap_eV`
  - `units`:
    - `diameter_nm`: nm
    - `raw_gap_eV`: eV
    - `corrected_gap_eV`: eV

Notes: The checker verifies the bulk Si gap against a reference value within tolerance, and for QDs verifies that corrected_gap ≈ raw_gap + 0.58, corrected gaps monotonically decrease with increasing diameter, and match reference values for at least two sizes.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "bulk_si_gap.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "A single floating-point number representing the HOMO-LUMO gap in eV."
      },
      "description": "Validation of DFT-LDA parameters by reproducing the bulk silicon LDA gap."
    },
    {
      "file": "qd_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "qd_name",
          "diameter_nm",
          "raw_gap_eV",
          "corrected_gap_eV"
        ],
        "units": {
          "diameter_nm": "nm",
          "raw_gap_eV": "eV",
          "corrected_gap_eV": "eV"
        }
      },
      "description": "Size-dependent raw and corrected HOMO-LUMO gaps for hydrogen-passivated Si quantum dots."
    }
  ],
  "notes": "The checker verifies the bulk Si gap against a reference value within tolerance, and for QDs verifies that corrected_gap ≈ raw_gap + 0.58, corrected gaps monotonically decrease with increasing diameter, and match reference values for at least two sizes."
}
```

## How you are scored
A hidden verifier will examine both output files independently. For the bulk silicon gap, the verifier will compare your computed value to a reference within a tolerance. For the quantum dot gaps, the verifier will check that each corrected gap equals the raw gap plus the stated 0.58 eV correction, verify that the corrected gaps follow a monotonic trend with the dot diameter, and compare the corrected values to reference numbers within tolerances. Each check contributes a weighted fraction to a final reward between 0 and 1. You do not need to reproduce any specific Figure or Table of the original study; simply compute the quantities according to the described DFT protocol.
