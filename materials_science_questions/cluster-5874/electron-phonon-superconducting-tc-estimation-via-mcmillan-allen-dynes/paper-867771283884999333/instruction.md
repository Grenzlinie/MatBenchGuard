# Superconducting Tc functional derivative and spectral maxima analysis

## Problem background
For electron-phonon superconductors, the functional derivative of the critical temperature Tc with respect to the Eliashberg spectral function α²F(ω), δTc/δα²F(ω), shows which phonon frequencies contribute most to superconductivity. The high-Tc hydride H₃S exhibits large changes in Tc under pressure. By computing this derivative from known α²F(ω) spectra one can determine the frequency δM where δTc/δα²F peaks, and compare it with αM, the frequency where α²F itself peaks. The relationship between δM, αM, and Tc across different pressures is the focus of this reproduction.

## Approach
The linearized Migdal–Eliashberg equations on the imaginary axis are solved using the α²F(ω) spectra and Tc values for H₃S at several pressures, together with a Coulomb pseudopotential μ*. From the converged solutions the functional derivative δTc/δα²F(ω) is computed. For each pressure, the phonon energies corresponding to the maxima of δTc/δα²F (δM) and α²F (αM) are extracted. A table of these quantities, along with Tc and the difference δM−αM, is then produced.

## Reproduction target
Implement a solver for the linearized Migdal–Eliashberg equations using the α²F(ω) spectra and Tc values for H₃S at pressures 155, 160, 165, 170, 175, 185, 195, 205, 215 GPa from the supplementary data of Camargo-Martínez et al. (2019). Compute the functional derivative δTc/δα²F(ω) for each pressure. Determine the phonon frequency δM where δTc/δα²F peaks and the frequency αM where α²F peaks. Calculate the difference δM−αM. Produce a CSV file containing one row per pressure with columns: Pressure (GPa), Tc (K), dM (meV), aM (meV), dM_minus_aM (meV). The CSV must have exactly nine rows, one for each pressure in the set above.

## Assets

- α²F(ω) spectra and Tc values for H3S (Im‾3m) at 155–215 GPa: 10.1088/1361-6668/ab3a7f

## Workflow steps

### Step 1: Load α²F(ω) data and Tc values
- Role: process
- Action: Retrieve the Eliashberg spectral functions α²F(ω) and corresponding Tc values for H3S (Im‾3m) at pressures 155, 160, 165, 170, 175, 185, 195, 205, 215 GPa from the supplementary data of Camargo-Martínez et al. (2019) (Ref. 16 of the source paper). Parse the data into a usable format for the solver.
- Evidence: `/app/outputs/a2F_data.npz`

### Step 2: Compute δTc/δα²F(ω) and extract δM, αM, δM−αM
- Role: scored (load-bearing)
- Action: Implement the linearized Migdal–Eliashberg equations on the imaginary axis using the loaded α²F(ω) spectra, Tc values, and a Coulomb pseudopotential μ* (obtain the value used in Ref. 16 or use 0.1) to compute the functional derivative δTc/δα²F(ω) for each pressure. Determine the phonon frequency δM where δTc/δα²F peaks and the frequency αM where α²F peaks; compute δM−αM. Write a CSV with one row per pressure, containing Pressure (GPa), Tc (K), dM (meV), aM (meV), dM_minus_aM (meV).
- Output file: `/app/outputs/step_03_table.csv`
- Format: csv
- Contract: CSV with columns: Pressure (GPa, float), Tc (K, float), dM (meV, float), aM (meV, float), dM_minus_aM (meV, float). 9 rows, one for each pressure in the set {155, 160, 165, 170, 175, 185, 195, 205, 215}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_03_table.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_03_table.csv
- path: `/app/outputs/step_03_table.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed δM, αM, and δM−αM values for H3S at nine pressures. The checker compares each row against a hidden gold (paper’s Table I) with appropriate tolerances and verifies monotonic trends.
- schema:
  - `type`: table
  - `required_columns`: `Pressure`, `Tc`, `dM`, `aM`, `dM_minus_aM`
  - `units`:
    - `Pressure`: GPa
    - `Tc`: K
    - `dM`: meV
    - `aM`: meV
    - `dM_minus_aM`: meV

Notes: The CSV must contain exactly nine rows (one per pressure). The hidden checker will compare the reported numbers to the paper’s gold values using tolerances that account for implementation differences; it will also check that Tc decreases and δM−αM increases with pressure, as described in the paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_03_table.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Pressure",
          "Tc",
          "dM",
          "aM",
          "dM_minus_aM"
        ],
        "units": {
          "Pressure": "GPa",
          "Tc": "K",
          "dM": "meV",
          "aM": "meV",
          "dM_minus_aM": "meV"
        }
      },
      "description": "Computed δM, αM, and δM−αM values for H3S at nine pressures. The checker compares each row against a hidden gold (paper’s Table I) with appropriate tolerances and verifies monotonic trends."
    }
  ],
  "notes": "The CSV must contain exactly nine rows (one per pressure). The hidden checker will compare the reported numbers to the paper’s gold values using tolerances that account for implementation differences; it will also check that Tc decreases and δM−αM increases with pressure, as described in the paper."
}
```

## How you are scored
A hidden verifier inspects your output table and compares the values in each row against reference values derived from the original research. It checks the accuracy of the reported Tc, dM, aM, and dM_minus_aM, and also verifies that the trends across pressures (Tc decreasing with pressure, dM_minus_aM increasing with pressure) are correctly reproduced. The final score is a weighted combination of per-row accuracy and trend conformance. Reporting the expected trends or reference numbers without genuine computation will not satisfy the verifier.
