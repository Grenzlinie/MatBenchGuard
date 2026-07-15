# First-principles hyperfine and ODMR spectrum simulation for carbon-related spin defects in hBN

## Problem background
Hexagonal boron nitride (hBN) hosts optically active spin defects that are attractive for quantum sensing and networking. A key open challenge is identifying their atomic structure. This task addresses the computational component of structure identification by computing hyperfine coupling constants and simulating optically detected magnetic resonance (ODMR) spectra for two proposed defect candidates. Comparison of first-principles computed hyperfine parameters with experimental signatures can help assign defect chemical structures.

## Approach
First-principles density-functional theory (DFT) calculations are performed with Quantum Espresso using the HSE hybrid functional and GIPAW pseudopotentials. Periodic supercell models of the two defect candidates (C₁⁺Cₙ⁰-DAP-2 and C₁Oₙ⁺) are constructed in the hBN lattice. Geometry relaxation and hyperfine tensor calculations yield the A_zz coupling of the electron spin to its nearest ¹³C nucleus and the zero-field splitting parameters. Using these computed parameters, continuous-wave ODMR spectra are simulated via a spin Hamiltonian solver (e.g., EasySpin or QuTiP) that includes the defect electron spin, the ¹³C nuclear spin, and nearby ¹¹B/¹⁴N nuclear spins to reproduce the hyperfine splitting signatures. The workflow does not require experimental data; all inputs (crystal structure, pseudopotentials, open-source codes) are publicly available.

## Reproduction target
Produce a CSV file (`hyperfine_parameters.csv`) with the computed hyperfine coupling constant A_zz (in MHz) for each defect model: C₁⁺Cₙ⁰-DAP-2 and C₁Oₙ⁺. Then simulate and output two CSV files (`odmr_spectrum_dap2.csv` and `odmr_spectrum_cbon.csv`), each containing two columns (frequency in MHz and normalized contrast), covering the frequency region where the hyperfine structure is expected. The simulated spectra must exhibit distinct peaks whose frequency separations are consistent with the corresponding computed A_zz.

## Assets

- Quantum Espresso: https://www.quantum-espresso.org/
- GIPAW pseudopotentials for B, C, N, O: https://pseudopotentials.quantum-espresso.org/
- hBN crystal structure
- EasySpin (MATLAB toolbox) or QuTiP equivalent: https://easyspin.org

## Workflow steps

### Step 1: DFT reference calculations
- Role: process
- Action: Set up periodic supercell calculations for the two defect models: C_B^+C_N^0-DAP-2 and C_B O_N^+ in hBN. Use Quantum Espresso with HSE hybrid functional, 6×6×1 supercell, GIPAW pseudopotentials. Perform geometry relaxation and compute hyperfine tensors (A_zz) and zero-field splitting parameters. Save relevant output files for later parameter extraction.
- Evidence: `/app/outputs/dft_calculation.log`

### Step 2: Extract hyperfine parameters
- Role: scored (load-bearing)
- Action: Parse the DFT output files from Step 1 to extract the hyperfine coupling constant A_zz (in MHz) for the 13C nuclear spin at the defect site for each model. Output a CSV file with columns: defect, A_zz (MHz).
- Output file: `/app/outputs/hyperfine_parameters.csv`
- Format: csv
- Contract: Two rows, columns: defect (string), A_zz (float, MHz).
- Scoring: scored by hidden verifier

### Step 3: Simulate ODMR spectrum for DAP-2
- Role: scored
- Action: Using a spin Hamiltonian simulator (e.g., EasySpin, QuTiP, or custom Python code), set up the spin system for the C_B^+C_N^0-DAP-2 defect using the computed hyperfine parameters and ZFS from Step 1. Include the electron spin S=1/2, a 13C nuclear spin (I=1/2) with the extracted A_zz, and nearest 11B/14N nuclear spins with estimated couplings. Simulate the continuous-wave ODMR spectrum in the frequency range covering the hyperfine structure. Output a two-column CSV: frequency_MHz, normalized_contrast.
- Output file: `/app/outputs/odmr_spectrum_dap2.csv`
- Format: csv
- Contract: Two-column CSV with header 'frequency_MHz, normalized_contrast'. Values are numeric.
- Scoring: scored by hidden verifier

### Step 4: Simulate ODMR spectrum for C_B O_N
- Role: scored
- Action: Similar to Step 3, but for the C_B O_N^+ defect model. Use its hyperfine parameters and ZFS. Simulate the ODMR spectrum and output a two-column CSV.
- Output file: `/app/outputs/odmr_spectrum_cbon.csv`
- Format: csv
- Contract: Two-column CSV with header 'frequency_MHz, normalized_contrast'.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/hyperfine_parameters.csv`
- `/app/outputs/odmr_spectrum_dap2.csv`
- `/app/outputs/odmr_spectrum_cbon.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### hyperfine_parameters.csv
- path: `/app/outputs/hyperfine_parameters.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Hyperfine coupling constants for two defect models (DAP-2 and C_B O_N).
- schema:
  - `type`: table
  - `required_columns`: `defect`, `A_zz`
  - `units`:
    - `A_zz`: MHz

### odmr_spectrum_dap2.csv
- path: `/app/outputs/odmr_spectrum_dap2.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Simulated ODMR spectrum for the DAP-2 defect; the checker will extract peak separations.
- schema:
  - `type`: table
  - `required_columns`: `frequency_MHz`, `normalized_contrast`
  - `units`:
    - `frequency_MHz`: MHz
    - `normalized_contrast`: dimensionless

### odmr_spectrum_cbon.csv
- path: `/app/outputs/odmr_spectrum_cbon.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Simulated ODMR spectrum for the C_B O_N defect; the checker will extract peak separations.
- schema:
  - `type`: table
  - `required_columns`: `frequency_MHz`, `normalized_contrast`
  - `units`:
    - `frequency_MHz`: MHz
    - `normalized_contrast`: dimensionless

Notes: The hidden checker compares extracted A_zz and ODMR peak separations against reference values; tolerances are not disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "hyperfine_parameters.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "defect",
          "A_zz"
        ],
        "units": {
          "A_zz": "MHz"
        }
      },
      "description": "Hyperfine coupling constants for two defect models (DAP-2 and C_B O_N)."
    },
    {
      "file": "odmr_spectrum_dap2.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_MHz",
          "normalized_contrast"
        ],
        "units": {
          "frequency_MHz": "MHz",
          "normalized_contrast": "dimensionless"
        }
      },
      "description": "Simulated ODMR spectrum for the DAP-2 defect; the checker will extract peak separations."
    },
    {
      "file": "odmr_spectrum_cbon.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_MHz",
          "normalized_contrast"
        ],
        "units": {
          "frequency_MHz": "MHz",
          "normalized_contrast": "dimensionless"
        }
      },
      "description": "Simulated ODMR spectrum for the C_B O_N defect; the checker will extract peak separations."
    }
  ],
  "notes": "The hidden checker compares extracted A_zz and ODMR peak separations against reference values; tolerances are not disclosed here."
}
```

## How you are scored
A hidden verifier independently scores each of the three output files. For `hyperfine_parameters.csv`, the checker compares the reported A_zz values against expected reference values within an appropriate tolerance. For each simulated ODMR spectrum CSV, the checker extracts the frequency separation between prominent peaks and verifies that it matches the corresponding A_zz within a tolerance. The three stages are weighted equally to compute the final reward. You do not need to match any specific table or figure from a publication; the checker determines whether your computed results are consistent with the expected hyperfine signatures.
