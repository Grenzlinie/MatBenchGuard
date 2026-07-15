# First‑principles resonant Raman tensor symmetry breakdown in a small organic molecule

## Problem background
In Raman spectroscopy, excitation approaching an electronic transition can dramatically alter the symmetry of Raman tensors and the depolarization ratios of vibrational modes. A quantitative understanding of these resonance phenomena requires first‑principles electronic structure calculations that connect the computed excited‑state properties to the wavelength‑dependent Raman response. This task focuses on the small organic molecule benzenethiol, using density functional theory (DFT) and time‑dependent DFT to compute the lowest dipole‑allowed electronic transitions, and to map out how the Raman activities and depolarization ratios of its characteristic vibrations evolve as the excitation wavelength moves from the static limit toward resonance.

## Approach
The entire experiment is computational. Geometry optimization, vibrational analysis, and excited‑state properties are obtained at the B3LYP/6‑311++G(d,p) level of theory. From the optimized geometry, a time‑dependent DFT calculation yields the lowest singlet excited states; from those results the three lowest dipole‑allowed transition wavelengths and oscillator strengths are extracted. Frequency‑dependent Raman tensors are then computed using the linear optical polarizability derivatives (the coupled‑perturbed approach) at a series of excitation wavelengths covering the off‑resonant static limit (900 nm) through the visible/UV down to near‑resonance at 240 nm. For a set of four characteristic vibrational modes, the Raman activity at each wavelength is normalized to its 900 nm value, and the depolarization ratio is calculated. The analysis reveals how the Raman activity enhancement and the depolarization ratio vary with excitation energy, thereby quantifying the breakdown of the off‑resonant tensor symmetry as resonance is approached.

## Reproduction target
Produce two output files:
- `transitions.json`: the three lowest dipole‑allowed transition wavelengths (nm) and corresponding oscillator strengths of benzenethiol from TD‑DFT.
- `raman_data.csv`: for the four vibrational modes with approximate frequencies near 706, 1025, 1092, and 1626 cm⁻¹, and for each excitation wavelength (900, 600, 400, 300, 280, 260, 250, 240 nm), the relative Raman activity (ratio to the activity at 900 nm) and the depolarization ratio.
All calculations must be performed with an open‑source quantum chemistry package capable of B3LYP/6‑311++G(d,p) and frequency‑dependent polarizability computations (ORCA is recommended). The intermediate optimized geometry and vibrational frequencies are documented in a log file.

## Assets

- ORCA quantum chemistry package: https://www.orcasoftware.de/tutorials_orca/getting_started.html

## Workflow steps

### Step 1: Geometry optimization and vibrational analysis
- Role: process
- Action: Optimize the geometry of benzenethiol at the B3LYP/6‑311++G(d,p) level and compute harmonic vibrational frequencies and normal modes.
- Evidence: `/app/outputs/geometry_freq.log`

### Step 2: TD-DFT excitation energies
- Role: scored
- Action: Perform a TD‑DFT calculation on the optimized geometry to obtain the lowest singlet excited states. Extract the three lowest dipole‑allowed transition wavelengths (nm) and oscillator strengths. Write results to transitions.json.
- Output file: `/app/outputs/transitions.json`
- Format: json
- Contract: Array of objects with keys: wavelength_nm (float), oscillator_strength (float).
- Scoring: scored by hidden verifier

### Step 3: Frequency‑dependent Raman tensors
- Role: scored (load-bearing)
- Action: For the optimized geometry and four characteristic vibrational modes (with approximate frequencies near 706, 1025, 1092, and 1626 cm⁻¹), compute Raman activities and depolarization ratios at excitation wavelengths: 900 (static limit), 600, 400, 300, 280, 260, 250, and 240 nm. For each wavelength and mode report the Raman activity relative to that at 900 nm and the depolarization ratio. Write results to raman_data.csv.
- Output file: `/app/outputs/raman_data.csv`
- Format: csv
- Contract: CSV with columns: wavelength_nm (float), mode_freq_cm1 (float), relative_raman_activity (float), depolarization_ratio (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transitions.json`
- `/app/outputs/raman_data.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transitions.json
- path: `/app/outputs/transitions.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Lowest dipole‑allowed electronic transition wavelengths and oscillator strengths of benzenethiol from TD‑DFT.
- schema:
  - `type`: array
  - `items`:
    - `type`: object
    - `properties`:
      - `wavelength_nm`:
        - `type`: number
      - `oscillator_strength`:
        - `type`: number

### raman_data.csv
- path: `/app/outputs/raman_data.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Wavelength‑dependent Raman activity enhancements and depolarization ratios for four characteristic vibrational modes, demonstrating resonance‑induced tensor symmetry breakdown.
- schema:
  - `type`: table
  - `required_columns`: `wavelength_nm`, `mode_freq_cm1`, `relative_raman_activity`, `depolarization_ratio`
  - `units`:
    - `wavelength_nm`: nm
    - `mode_freq_cm1`: cm^-1
    - `relative_raman_activity`: dimensionless (ratio to 900 nm activity)
    - `depolarization_ratio`: dimensionless

Notes: The hidden checker compares transition values to paper‑reported numbers within tolerances and verifies activity enhancement trends and depolarization ratio behaviour (e.g., ratio approaching 1/3 at resonance, non‑monotonic bump for the 1626 cm⁻¹ mode).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transitions.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "array",
        "items": {
          "type": "object",
          "properties": {
            "wavelength_nm": {
              "type": "number"
            },
            "oscillator_strength": {
              "type": "number"
            }
          }
        }
      },
      "description": "Lowest dipole‑allowed electronic transition wavelengths and oscillator strengths of benzenethiol from TD‑DFT."
    },
    {
      "file": "raman_data.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "wavelength_nm",
          "mode_freq_cm1",
          "relative_raman_activity",
          "depolarization_ratio"
        ],
        "units": {
          "wavelength_nm": "nm",
          "mode_freq_cm1": "cm^-1",
          "relative_raman_activity": "dimensionless (ratio to 900 nm activity)",
          "depolarization_ratio": "dimensionless"
        }
      },
      "description": "Wavelength‑dependent Raman activity enhancements and depolarization ratios for four characteristic vibrational modes, demonstrating resonance‑induced tensor symmetry breakdown."
    }
  ],
  "notes": "The hidden checker compares transition values to paper‑reported numbers within tolerances and verifies activity enhancement trends and depolarization ratio behaviour (e.g., ratio approaching 1/3 at resonance, non‑monotonic bump for the 1626 cm⁻¹ mode)."
}
```

## How you are scored
A hidden verifier script evaluates your submitted artifacts independently. For `transitions.json`, the verifier compares your reported wavelengths and oscillator strengths to reference values obtained from equivalent DFT/TD‑DFT calculations, allowing for tolerances that account for differences in quantum‑chemistry implementations, basis‑set handling, and numerical convergence. For `raman_data.csv`, the verifier checks that the data are well‑formed, that the relative activities and depolarization ratios follow the expected physical trends for resonance Raman scattering (large activity enhancement as the excitation approaches electronic transitions and depolarization ratios shifting toward the resonance limit), and that specific qualitative features in the depolarization ratio curves are present (e.g., non‑monotonic behaviour for certain modes). Each output artifact contributes a weighted score; the final reward is the sum. Simply reporting the paper's numbers without performing the full workflow will not produce the required files and will fail the checks.
