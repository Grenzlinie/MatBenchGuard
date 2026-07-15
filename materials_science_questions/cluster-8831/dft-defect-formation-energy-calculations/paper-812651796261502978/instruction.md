# DFT-LDA Study of Electronic Structure and Optical Gaps in Delafossite Transparent Conductive Oxides

## Problem background
Delafossite compounds CuM^III O2 (M=Al, Ga, In) are promising transparent conductive oxides that can be doped p-type, yet their optical properties exhibit an anomalous band-gap trend: the measured optical gap does not follow the typical decrease with increasing group-III atomic number seen in other III-V semiconductors. Understanding the electronic-structure origin of this anomaly is critical for designing bipolarly dopable wide-gap semiconductors. First-principles calculations within density-functional theory provide a route to compute fundamental band gaps, optical absorption spectra, and band alignments, offering a quantitative explanation for this puzzle.

## Approach
We employ density-functional theory in the local density approximation (LDA) using the full-potential linearized augmented plane wave (LAPW) method. Starting from experimental crystal structures, we first relax the lattice parameters and internal coordinates for each compound. On the relaxed structures we compute the Kohn-Sham band structure along high-symmetry paths and evaluate the dipolar optical transition matrix elements between band-edge states. From the eigenvalues we extract the fundamental indirect and direct band gaps at key k-points. Next we compute the optical absorption coefficient α(hν) for light polarized parallel and perpendicular to the crystallographic c-axis. Using the resulting spectra we construct (αhν)² vs. hν Tauc plots and determine the apparent direct gaps by linear extrapolation. Finally, we calculate the natural valence band offsets via the core-level alignment method (referencing a deep core level, e.g. O 1s, relative to the valence band maximum) and derive the conduction band offsets by adding the direct gap at Γ. This computational workflow yields structural, electronic, and optical quantities that can be compared quantitatively.

## Reproduction target
Using DFT-LDA/LAPW, compute for each of CuAlO2, CuGaO2, and CuInO2: (1) the relaxed lattice constants a (Å), c (Å), and internal parameter u; (2) the fundamental indirect band gap and direct gaps at Γ, L, and F; (3) the apparent direct gap extracted from (αhν)² vs. hν Tauc analysis of the absorption spectra; and (4) the valence band maximum (VBM) and conduction band minimum (CBM) energy offsets relative to CuAlO2. Write each set of results into the corresponding CSV output file as specified in the workflow steps.

## Assets

- Elk LAPW code: http://elk.sourceforge.net
- Delafossite CuMO2 crystal structure data

## Workflow steps

### Step 1: Structural relaxation of CuMO2
- Role: scored
- Action: Perform DFT-LDA structural relaxation for CuAlO2, CuGaO2, CuInO2 in the delafossite crystal structure (space group R-3m, No. 166). Relax lattice vectors and internal coordinates until forces converge. Output the optimized lattice constants a (Å), c (Å) and internal parameter u.
- Output file: `/app/outputs/step_01_lattice_params.csv`
- Format: csv
- Contract: Columns: Compound (string), a (float, Å), c (float, Å), u (dimensionless). One row per compound.
- Scoring: scored by hidden verifier

### Step 2: Band structure and transition matrix elements
- Role: process
- Action: Calculate the electronic band structure and dipolar optical transition matrix elements between band-edge states for CuAlO2, CuGaO2, CuInO2 using DFT-LDA/LAPW. Use the relaxed lattice constants from step 1. Perform self-consistent field calculation, then compute eigenvalues and eigenvectors along the high-symmetry path Γ-F-L-Z-Γ. Record band energies and squared dipole matrix elements at each k-point. Save the raw data as evidence.
- Evidence: `/app/outputs/band_structure_data.json`

### Step 3: Extract fundamental band gaps
- Role: scored
- Action: From the computed band structures, identify the valence band maximum and conduction band minimum. Determine the indirect band gap (VBM near F to CBM at Γ) and the direct band gaps at Γ, L, and F. Record the values in eV for each compound.
- Output file: `/app/outputs/step_02_band_gaps.csv`
- Format: csv
- Contract: Columns: Compound (string), fundamental_direct_gap_Γ (float, eV), fundamental_direct_gap_L (float, eV), fundamental_direct_gap_F (float, eV), indirect_gap (float, eV). One row per compound.
- Scoring: scored by hidden verifier

### Step 4: Optical absorption spectra calculation
- Role: process
- Action: Using the Kohn-Sham eigenvalues and transition matrix elements from step 2, compute the frequency-dependent absorption coefficient α(hν) for light polarized parallel (∥) and perpendicular (⊥) to the crystallographic c axis. Generate α as a function of photon energy up to at least 5 eV, covering the range around the expected gaps. Save the spectra as evidence.
- Evidence: `/app/outputs/absorption_spectra.csv`

### Step 5: Apparent direct gaps from Tauc plots
- Role: scored (load-bearing)
- Action: From the absorption coefficient α for both polarizations, calculate (αhν)² as a function of photon energy hν. Perform a Tauc plot analysis: identify the linear region and extrapolate to zero to obtain the apparent direct band gap. Report one apparent gap per compound (using the dominant polarization if strong anisotropy exists, or an appropriate average).
- Output file: `/app/outputs/step_03_apparent_gaps.csv`
- Format: csv
- Contract: Columns: Compound (string), apparent_direct_gap (float, eV). One row per compound.
- Scoring: scored by hidden verifier

### Step 6: Natural valence band offsets calculation
- Role: process
- Action: Calculate the natural valence-band offsets between CuAlO2, CuGaO2, and CuInO2 using the core-level alignment method. For each compound, compute the energy difference between a deep core level (e.g., O 1s) and the valence band maximum. Align the core levels to obtain the VBM positions on an absolute energy scale. Then determine the conduction band minimum by adding the direct gap at Γ. Save the raw alignment data as evidence.
- Evidence: `/app/outputs/band_alignment_data.json`

### Step 7: Band offsets summary
- Role: scored
- Action: From the calculated band alignments, extract the VBM and CBM offsets of each compound relative to CuAlO2. Report the offsets in eV. Include CuAlO2 itself with offsets of 0.0.
- Output file: `/app/outputs/step_05_band_offsets.csv`
- Format: csv
- Contract: Columns: Compound (string), VBM_offset (float, eV), CBM_offset (float, eV). Offsets are relative to CuAlO2 (which has VBM_offset=0.0, CBM_offset=0.0). One row per compound.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_lattice_params.csv`
- `/app/outputs/step_02_band_gaps.csv`
- `/app/outputs/step_03_apparent_gaps.csv`
- `/app/outputs/step_05_band_offsets.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_lattice_params.csv
- path: `/app/outputs/step_01_lattice_params.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Optimized lattice parameters a, c, and internal parameter u for CuAlO2, CuGaO2, CuInO2. Compared against reference LDA relaxed values within a tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `a`, `c`, `u`
  - `units`:
    - `a`: Å
    - `c`: Å
    - `u`: dimensionless

### step_02_band_gaps.csv
- path: `/app/outputs/step_02_band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Fundamental band gaps from DFT band structures. Checked against reference LDA values with tolerance and trend verification (e.g., direct gap at Γ must decrease from Al to In).
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `fundamental_direct_gap_Γ`, `fundamental_direct_gap_L`, `fundamental_direct_gap_F`, `indirect_gap`
  - `units`:
    - `fundamental_direct_gap_Γ`: eV
    - `fundamental_direct_gap_L`: eV
    - `fundamental_direct_gap_F`: eV
    - `indirect_gap`: eV

### step_03_apparent_gaps.csv
- path: `/app/outputs/step_03_apparent_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Apparent direct band gaps extracted from (αhν)² vs. hν Tauc plots. Compared against reference LDA apparent gap values with tolerance; trend (increase from Al to In) must be reproduced.
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `apparent_direct_gap`
  - `units`:
    - `apparent_direct_gap`: eV

### step_05_band_offsets.csv
- path: `/app/outputs/step_05_band_offsets.csv`
- format: csv
- purpose: scored
- target_policy: threshold_or_better
- description: Valence band and conduction band offsets relative to CuAlO2. CBM_offset of CuInO2 must be at least -1.2 eV (i.e., ≤ -1.2 eV) to satisfy the requirement; better (more negative) is acceptable. Other offsets are verified within tolerance.
- schema:
  - `type`: table
  - `required_columns`: `Compound`, `VBM_offset`, `CBM_offset`
  - `units`:
    - `VBM_offset`: eV
    - `CBM_offset`: eV

Notes: All scored outputs are in CSV format with a header row and one data row per compound. The hidden checker reads the columns and compares against paper-derived gold values using tolerances and/or trend checks. No gold values or tolerances are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_lattice_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "a",
          "c",
          "u"
        ],
        "units": {
          "a": "Å",
          "c": "Å",
          "u": "dimensionless"
        }
      },
      "description": "Optimized lattice parameters a, c, and internal parameter u for CuAlO2, CuGaO2, CuInO2. Compared against reference LDA relaxed values within a tolerance."
    },
    {
      "file": "step_02_band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "fundamental_direct_gap_Γ",
          "fundamental_direct_gap_L",
          "fundamental_direct_gap_F",
          "indirect_gap"
        ],
        "units": {
          "fundamental_direct_gap_Γ": "eV",
          "fundamental_direct_gap_L": "eV",
          "fundamental_direct_gap_F": "eV",
          "indirect_gap": "eV"
        }
      },
      "description": "Fundamental band gaps from DFT band structures. Checked against reference LDA values with tolerance and trend verification (e.g., direct gap at Γ must decrease from Al to In)."
    },
    {
      "file": "step_03_apparent_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "apparent_direct_gap"
        ],
        "units": {
          "apparent_direct_gap": "eV"
        }
      },
      "description": "Apparent direct band gaps extracted from (αhν)² vs. hν Tauc plots. Compared against reference LDA apparent gap values with tolerance; trend (increase from Al to In) must be reproduced."
    },
    {
      "file": "step_05_band_offsets.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "table",
        "required_columns": [
          "Compound",
          "VBM_offset",
          "CBM_offset"
        ],
        "units": {
          "VBM_offset": "eV",
          "CBM_offset": "eV"
        }
      },
      "description": "Valence band and conduction band offsets relative to CuAlO2. CBM_offset of CuInO2 must be at least -1.2 eV (i.e., ≤ -1.2 eV) to satisfy the requirement; better (more negative) is acceptable. Other offsets are verified within tolerance."
    }
  ],
  "notes": "All scored outputs are in CSV format with a header row and one data row per compound. The hidden checker reads the columns and compares against paper-derived gold values using tolerances and/or trend checks. No gold values or tolerances are disclosed here."
}
```

## How you are scored
Your submitted artifacts are evaluated by an automated hidden verifier. Each scored artifact (lattice parameters, fundamental band gaps, apparent direct gaps, band offsets) is checked independently. The verifier compares your reported values against reference values using appropriate tolerances, inspects whether the qualitative trends between compounds match the expected ones, and applies threshold-based criteria for certain offsets. The final reward is a weighted combination of these scores, rewarding accuracy and physically correct trends. Simply writing down numbers without performing the full computational workflow is unlikely to yield results that simultaneously satisfy all tolerance and trend checks.
