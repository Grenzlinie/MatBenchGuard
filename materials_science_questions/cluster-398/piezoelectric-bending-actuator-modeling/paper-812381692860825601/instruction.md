# Geometry selection using FEA for spurious mode avoidance in piezoelectric transformers

## Problem background
Piezoelectric transformers (PTs) are compact electromechanical devices used in power conversion. Their performance—efficiency and power density—depends critically on operating in a frequency range free of unwanted vibration modes (spurious modes). The effective electromechanical coupling coefficient $k_{\text{eff}}$ quantifies the energy conversion capability of each vibrational mode. When the PT is ring-shaped, the choice of inner and outer diameters can significantly change the distribution and strength of these spurious modes, even when the total area is fixed. This task investigates how the geometry of a ring-shaped PT affects the cleanliness of the working frequency range and the achievable coupling coefficient.

## Approach
The core idea is to perform a 2D axisymmetric finite element modal analysis of piezoelectric ring structures. You will build two axisymmetric finite element models that represent the PT geometries, using publicly available material properties for the piezoelectric ceramic Pz26. The models differ only in their outer and inner diameters while keeping the cross‑sectional area constant. Modal analysis (both short‑circuit and open‑circuit electrical boundary conditions) yields the eigenfrequencies and the effective electromechanical coupling coefficient $k_{\text{eff}}$ for every computed mode. From the $k_{\text{eff}}$ versus frequency curves you will identify the primary thickness mode (resonance $f_r$ and anti‑resonance $f_a$), compute the effective coupling coefficient $k_{\text{eff}} = \sqrt{1 - (f_r/f_a)^2}$, and detect any extra $k_{\text{eff}}$ peaks (spurious modes) that appear within the frequency window between $f_r$ and $f_a$. The comparison between the two geometries reveals how diameter selection influences spurious‑mode avoidance and coupling strength.

## Reproduction target
Produce, using any open‑source finite element tool with piezoelectric capabilities, the $k_{\text{eff}}$ vs frequency data for two ring‑shaped piezoelectric transformer designs:
- PT2a: outer diameter 19.73 mm, inner diameter 11.61 mm
- PT2b: outer diameter 24.97 mm, inner diameter 19.21 mm
The total area and layer thicknesses are fixed as in the 1D analytical design. For each design output a CSV file containing the frequency (Hz) and $k_{\text{eff}}$ for every computed eigenmode. Then analyze the results to determine for each design whether spurious modes (additional $k_{\text{eff}}$ peaks) exist inside the working frequency range and report, for the PT2b design, its resonance frequency, anti‑resonance frequency, and the corresponding $k_{\text{eff}}$. Package these findings in a summary JSON file.

## Assets
- **Pz26 piezoelectric material properties**: density, elastic stiffness, piezoelectric constants, and relative permittivity for the Ferroperm Pz26 ceramic. The datasheet is publicly available; you may obtain the needed constants from the Ferroperm catalog or equivalent open material databases.
- **Open‑source finite element analysis software with piezoelectric modal analysis**: any tool that supports 2D axisymmetric piezoelectric simulation (e.g., Elmer, FreeFEM++, or a comparable package). The tool must be able to compute eigenfrequencies and the effective electromechanical coupling coefficient. Install and configure your chosen tool at run time.

## Workflow steps

### Step 1: Run FEA modal analysis
- Role: process
- Action: Build 2D axisymmetric finite element models of the PT2a (φout=19.73 mm, φin=11.61 mm) and PT2b (φout=24.97 mm, φin=19.21 mm) ring-shaped piezoelectric transformers using Pz26 material properties. The total area and thickness are fixed and correspond to the 1D analytical design. Apply electrical boundary conditions for modal analysis (short-circuit and open-circuit). Run the analysis to obtain eigenfrequencies and effective electromechanical coupling coefficient keff for each mode.
- Evidence: `/app/outputs/fea_log.txt`

### Step 2: Output PT2a keff data
- Role: scored (load-bearing)
- Action: From the FEA results, extract the eigenfrequencies and keff for every computed mode of PT2a. Write a CSV file with columns frequency_Hz and keff.
- Output file: `/app/outputs/pt2a_keff.csv`
- Format: csv
- Contract: Columns: frequency_Hz (numeric), keff (numeric).
- Scoring: scored by hidden verifier

### Step 3: Output PT2b keff data
- Role: scored (load-bearing)
- Action: From the FEA results, extract the eigenfrequencies and keff for every computed mode of PT2b. Write a CSV file with the same format as PT2a.
- Output file: `/app/outputs/pt2b_keff.csv`
- Format: csv
- Contract: Columns: frequency_Hz (numeric), keff (numeric).
- Scoring: scored by hidden verifier

### Step 4: Generate summary of spurious modes and coupling
- Role: scored
- Action: Analyze the keff curves for PT2a and PT2b. Identify the primary thickness mode resonance (fr) and anti-resonance (fa) and compute keff_eff = sqrt(1 - (fr/fa)^2). Detect any additional keff peaks (spurious modes) within the working frequency range between fr and fa. Produce a JSON summary with Boolean flags for spurious mode presence in each design, and report fr, fa, and keff_eff for PT2b.
- Output file: `/app/outputs/summary.json`
- Format: json
- Contract: JSON object with keys: PT2a_spurious_modes_present (bool), PT2b_spurious_modes_present (bool), PT2b_resonance_frequency_Hz (float), PT2b_anti_resonance_frequency_Hz (float), PT2b_keff (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/pt2a_keff.csv`
- `/app/outputs/pt2b_keff.csv`
- `/app/outputs/summary.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### pt2a_keff.csv
- path: `/app/outputs/pt2a_keff.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Modal analysis results for PT2a design: eigenfrequencies and effective electromechanical coupling coefficient.
- schema:
  - `type`: table
  - `required_columns`: `frequency_Hz`, `keff`
  - `units`:
    - `frequency_Hz`: Hz
    - `keff`: 1

### pt2b_keff.csv
- path: `/app/outputs/pt2b_keff.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Modal analysis results for PT2b design: eigenfrequencies and effective electromechanical coupling coefficient.
- schema:
  - `type`: table
  - `required_columns`: `frequency_Hz`, `keff`
  - `units`:
    - `frequency_Hz`: Hz
    - `keff`: 1

### summary.json
- path: `/app/outputs/summary.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: Summary of spurious mode presence and key parameters for PT2b. The checker will compare the effective coupling coefficient and spurious mode flags against reference values derived from the paper's figures.
- schema:
  - `type`: object
  - `required`:
    - `PT2a_spurious_modes_present`: bool
    - `PT2b_spurious_modes_present`: bool
    - `PT2b_resonance_frequency_Hz`: float
    - `PT2b_anti_resonance_frequency_Hz`: float
    - `PT2b_keff`: float
  - `units`:
    - `PT2b_resonance_frequency_Hz`: Hz
    - `PT2b_anti_resonance_frequency_Hz`: Hz
    - `PT2b_keff`: 1

Notes: The checker reads the CSV files and recomputes the effective coupling coefficient and spurious mode presence; it then compares the summary's Boolean flags and keff to hidden gold values (paper's reported results) with appropriate tolerances. The keff target uses threshold_or_better policy (higher keff is better).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "pt2a_keff.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_Hz",
          "keff"
        ],
        "units": {
          "frequency_Hz": "Hz",
          "keff": "1"
        }
      },
      "description": "Modal analysis results for PT2a design: eigenfrequencies and effective electromechanical coupling coefficient."
    },
    {
      "file": "pt2b_keff.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "frequency_Hz",
          "keff"
        ],
        "units": {
          "frequency_Hz": "Hz",
          "keff": "1"
        }
      },
      "description": "Modal analysis results for PT2b design: eigenfrequencies and effective electromechanical coupling coefficient."
    },
    {
      "file": "summary.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": {
          "PT2a_spurious_modes_present": "bool",
          "PT2b_spurious_modes_present": "bool",
          "PT2b_resonance_frequency_Hz": "float",
          "PT2b_anti_resonance_frequency_Hz": "float",
          "PT2b_keff": "float"
        },
        "units": {
          "PT2b_resonance_frequency_Hz": "Hz",
          "PT2b_anti_resonance_frequency_Hz": "Hz",
          "PT2b_keff": "1"
        }
      },
      "description": "Summary of spurious mode presence and key parameters for PT2b. The checker will compare the effective coupling coefficient and spurious mode flags against reference values derived from the paper's figures."
    }
  ],
  "notes": "The checker reads the CSV files and recomputes the effective coupling coefficient and spurious mode presence; it then compares the summary's Boolean flags and keff to hidden gold values (paper's reported results) with appropriate tolerances. The keff target uses threshold_or_better policy (higher keff is better)."
}
```

## How you are scored
A hidden verifier will read the files you submit (`pt2a_keff.csv`, `pt2b_keff.csv`, `summary.json`) after the task finishes. It will independently check each artifact against a concealed reference that encodes the expected physical relationships and plausible ranges. The verifier assigns a score to each stage (weighting them appropriately) and combines them into a single reward between 0 and 1. To earn full credit your $k_{\text{eff}}$ curves must be physically consistent (non‑negative, frequencies in a realistic domain) and the structural properties of your curves (e.g., the presence or absence of spurious modes, the effective coupling coefficient) must align with the reference. Merely reporting numbers without a genuine modal analysis is not enough; the verifier validates that the overall shape and key indicators are consistent with a correct simulation. The scoring uses a directional policy where a better‑than‑expected coupling coefficient is never penalized.
