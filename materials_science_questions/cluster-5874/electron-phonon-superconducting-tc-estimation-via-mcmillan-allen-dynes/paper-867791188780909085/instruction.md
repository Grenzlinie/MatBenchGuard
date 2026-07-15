# Superconducting Tc of CaAlH7 via Anisotropic Migdal-Eliashberg

## Problem background
High-pressure hydrides have emerged as a promising route to conventional high-temperature superconductivity. Adding a third element can chemically precompress the hydrogen lattice, stabilizing dense phases at lower pressure. The Ca-Al-H system was explored computationally, and one phase, CaAlH₇, was found to be dynamically stable down to 50 GPa and is expected to superconduct. Reproducing the predicted superconducting critical temperature (Tc) of CaAlH₇ from first principles validates the computational protocol and the role of this compound as a template for low-pressure, high-Tc ternary hydrides.

## Approach
The approach is based on first-principles calculations: (1) use density functional theory (DFT) with the PBE functional and PAW pseudopotentials to relax the crystal structures of CaAlH₇ at the target pressures; (2) compute phonon dispersions and the electron‑phonon coupling parameters using density functional perturbation theory (DFPT); (3) interpolate the electron‑phonon matrix elements onto fine k‑ and q‑point grids via Wannier functions (EPW code); (4) solve the fully anisotropic Migdal‑Eliashberg equations self‑consistently with a constant Morel‑Anderson pseudopotential μ* = 0.10; (5) extract the leading edge of the superconducting gap as a function of temperature and determine Tc as the temperature where the gap extrapolates to zero. The workflow is implemented with open‑source tools (Quantum ESPRESSO + EPW) in place of proprietary codes, and the resulting Tc values are reported for each pressure in a CSV file.

## Reproduction target
Compute the superconducting critical temperature (Tc) of CaAlH₇ at 50 GPa, 100 GPa, and 300 GPa by following the anisotropic Migdal‑Eliashberg procedure described above, using the crystal structures provided in the public arXiv supplementary material. Report the calculated Tc values in a CSV file with columns “pressure” (GPa) and “Tc” (K). The computation for 100 GPa is optional; the primary scoring is based on the values at 50 GPa and 300 GPa.

## Assets

- CaAlH7 crystal structures (arXiv supplementary material): https://arxiv.org/abs/2305.09541
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- EPW (Electron-Phonon Wannier) code: https://epw-code.org/

## Workflow steps

### Step 1: Obtain and relax CaAlH7 structures
- Role: process
- Action: Download the CaAlH7 crystal structures at 50, 100, and 300 GPa from the arXiv supplementary material (2305.09541). Perform DFT relaxation of each structure using an open-source DFT code (e.g., Quantum ESPRESSO with PAW pseudopotentials and PBE functional) to obtain the relaxed coordinates for subsequent phonon calculations.
- Evidence: `/app/outputs/relaxation.log`

### Step 2: Compute phonon dispersions and electron-phonon coupling
- Role: process
- Action: Using the relaxed structures, perform density functional perturbation theory (DFPT) calculations to obtain phonon dispersions, electron-phonon matrix elements, and the Eliashberg function α²F(ω). Generate Wannier functions and interpolate onto fine k- and q-point grids with the EPW code to prepare the anisotropic Migdal-Eliashberg input.
- Evidence: `/app/outputs/elph_output.log`

### Step 3: Calculate superconducting Tc
- Role: scored
- Action: Solve the anisotropic Migdal-Eliashberg equations self-consistently for each pressure (50, 100, 300 GPa), using a constant Morel-Anderson pseudopotential μ* = 0.10. Extract the leading edge of the superconducting gap as a function of temperature and determine Tc as the temperature where the gap extrapolates to zero. Write the resulting Tc values.
- Output file: `/app/outputs/step_03_tc_results.csv`
- Format: csv
- Contract: Columns: pressure (numeric, unit GPa), Tc (numeric, unit K)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_tc_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_tc_results.csv
- path: `/app/outputs/step_03_tc_results.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Predicted superconducting critical temperature for CaAlH7 at 50, 100, and 300 GPa. Only the 50 and 300 GPa entries are scored; the 100 GPa entry is optional.
- schema:
  - `type`: table
  - `required_columns`: `pressure`, `Tc`
  - `units`:
    - `pressure`: GPa
    - `Tc`: K

Notes: The checker compares the reported Tc at 50 and 300 GPa to hidden reference values with an acceptable tolerance to account for toolchain differences (open-source QE+EPW vs. VASP). The 100 GPa entry is not scored. The agent must run the full process; result-level comparison is used.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_tc_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "pressure",
          "Tc"
        ],
        "units": {
          "pressure": "GPa",
          "Tc": "K"
        }
      },
      "description": "Predicted superconducting critical temperature for CaAlH7 at 50, 100, and 300 GPa. Only the 50 and 300 GPa entries are scored; the 100 GPa entry is optional."
    }
  ],
  "notes": "The checker compares the reported Tc at 50 and 300 GPa to hidden reference values with an acceptable tolerance to account for toolchain differences (open-source QE+EPW vs. VASP). The 100 GPa entry is not scored. The agent must run the full process; result-level comparison is used."
}
```

## How you are scored
Your submission is scored by a hidden verifier that reads the file `/app/outputs/step_03_tc_results.csv`. The verifier extracts the Tc values for 50 GPa and 300 GPa and compares them against reference thresholds derived from independent calculations that account for the expected spread between different DFT/EPW implementations. The 100 GPa entry, if present, is not scored but may be included at your discretion. Each of the two scored pressures is checked against an allowed tolerance; the final reward is a weighted combination of these checks, ranging from 0 to 1. A perfect score requires that both Tc values fall within the acceptable range; partial credit may be awarded if only one passes. Reporting numbers that merely match the paper’s published figure without a genuine recomputation will not satisfy the verifier because the hidden tolerances are set to distinguish a correct re‑execution from a guess. The verifier operates automatically and deterministically.
