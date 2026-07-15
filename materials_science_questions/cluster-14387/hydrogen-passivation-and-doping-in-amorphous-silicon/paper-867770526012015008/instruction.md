# Geometric and electronic properties of hydrogenated silicene via density functional theory

## Problem background
Hydrogenation of silicene strongly modifies its geometric and electronic properties through the formation of H-Si bonds. Density functional theory (DFT) calculations in chair and top hydrogen configurations at various concentrations reveal how structural parameters (bond lengths, angles) and electronic features (band gaps, density-of-states peaks) depend on H concentration. This task reproduces these computational predictions: it computes the concentration-dependent geometry and electronic structure of hydrogenated silicene, and quantifies the relationship between specific DOS peak intensities and hydrogen concentration.

## Approach
The reproduction uses density functional theory with the local density approximation (LDA) and projector augmented wave (PAW) pseudopotentials. Atomic models for hydrogenated silicene are built in chair and top configurations at several hydrogen coverages, with supercells matching the hydrogen arrangement patterns. For each structure, a geometry relaxation is performed to obtain optimized atomic positions. From these, bond lengths and angles are extracted. A subsequent static DFT calculation with a dense k-point mesh provides the band structure and total density of states. The band gap type (direct/indirect) and size are determined from the band structure, and prominent hydrogen-related DOS peaks (and, for top configurations, a peak near the Fermi level) are identified and their energies and intensities recorded. Finally, the dependence of the peak intensities on hydrogen concentration is modeled by separate linear least-squares fits for the hydrogen-related and Fermi-level peaks.

## Reproduction target
Produce the following for hydrogenated silicene in chair and top configurations at the specified H:Si ratios: (i) average geometric parameters (H-Si-Si angle, Si-Si nearest- and next-nearest-neighbor bond lengths, H-Si bond length); (ii) band gap types and values for each system; (iii) energies and intensities of prominent hydrogen-related DOS peaks and, for top configurations, a Fermi-level peak; (iv) slope and intercept from linear fits of DOS peak intensity versus hydrogen concentration for both hydrogen-related peaks and the Fermi-level peak.

## Assets

- DFT code with LDA+PAW (e.g., Quantum ESPRESSO or GPAW): https://www.quantum-espresso.org/
- PAW pseudopotentials for Si and H (SSSP library): https://www.materialscloud.org/discover/sssp/table/efficiency

## Workflow steps

### Step 1: Construct hydrogenated silicene models
- Role: process
- Action: Generate initial atomic structures for hydrogenated silicene with chair and top configurations at the following coverages: chair H:Si = 2:2, 2:8, 2:32; top H:Si = 1:2, 1:8, 1:32. Use supercells consistent with the hydrogen arrangement patterns shown in the paper.
- Evidence: none

### Step 2: DFT geometry optimization
- Role: process
- Action: For each initial structure, perform DFT geometry relaxation using LDA functional and PAW pseudopotentials. Use a plane-wave cutoff energy of 500 eV, a k-point mesh of 12×12×1, and a force convergence criterion of 0.01 eV/Å. Save the optimized coordinates.
- Evidence: none

### Step 3: Extract geometric parameters
- Role: scored
- Action: From each optimized structure, compute and output: H-Si-Si bond angle (average), Si-Si nearest-neighbor bond length (average), Si-Si next-nearest-neighbor bond length (average), and H-Si bond length (average).
- Output file: `/app/outputs/structural_params.csv`
- Format: csv
- Contract: CSV with columns: system (string, e.g., chair_2_2), HSiSi_angle (deg), SiSi_nn_length (Å), SiSi_nnn_length (Å), HSi_length (Å)
- Scoring: scored by hidden verifier

### Step 4: DFT electronic structure calculation
- Role: process
- Action: For each optimized structure, perform a static DFT calculation using a dense k-point mesh (100×100×1) to obtain band energies on a high-symmetry path and the total density of states.
- Evidence: none

### Step 5: Analyze band gaps
- Role: scored
- Action: From the computed band structures, determine whether each system has a direct or indirect band gap and extract the band gap value in eV.
- Output file: `/app/outputs/band_gaps.csv`
- Format: csv
- Contract: CSV with columns: system (string), gap_type (string: 'direct' or 'indirect'), value_eV (float)
- Scoring: scored by hidden verifier

### Step 6: Analyze DOS peaks
- Role: scored
- Action: From the total DOS of each system, identify the prominent H-related peaks (around -3 to -5 eV) and, for top configurations, the delta-function-like peak at the Fermi level (E=0). For each identified peak record its energy position (eV) and its intensity (peak height).
- Output file: `/app/outputs/dos_peaks.csv`
- Format: csv
- Contract: CSV with columns: system (string), peak_energy_eV (float), peak_type (string: 'H_related' or 'delta'), intensity (float)
- Scoring: scored by hidden verifier

### Step 7: Fit linear relationship of peak intensity vs H-concentration
- Role: scored (load-bearing)
- Action: Using the intensities from dos_peaks.csv, perform separate linear least-squares fits for H-related peaks (chair systems) and delta peaks (top systems) as a function of H-concentration (expressed as fraction of the maximum coverage). Output the slope and intercept of each fit.
- Output file: `/app/outputs/linear_fit.json`
- Format: json
- Contract: JSON object with keys: H_peak_slope (float), H_peak_intercept (float), delta_peak_slope (float), delta_peak_intercept (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/structural_params.csv`
- `/app/outputs/band_gaps.csv`
- `/app/outputs/dos_peaks.csv`
- `/app/outputs/linear_fit.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### structural_params.csv
- path: `/app/outputs/structural_params.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Table of geometric parameters per hydrogenated silicene system.
- schema:
  - `type`: table
  - `required_columns`: `system`, `HSiSi_angle`, `SiSi_nn_length`, `SiSi_nnn_length`, `HSi_length`
  - `units`:
    - `HSiSi_angle`: deg
    - `SiSi_nn_length`: Å
    - `SiSi_nnn_length`: Å
    - `HSi_length`: Å

### band_gaps.csv
- path: `/app/outputs/band_gaps.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Band gap types and values for each hydrogenated system.
- schema:
  - `type`: table
  - `required_columns`: `system`, `gap_type`, `value_eV`
  - `units`:
    - `value_eV`: eV

### dos_peaks.csv
- path: `/app/outputs/dos_peaks.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: List of identified DOS peaks with energies and intensities.
- schema:
  - `type`: table
  - `required_columns`: `system`, `peak_energy_eV`, `peak_type`, `intensity`
  - `units`:
    - `peak_energy_eV`: eV
    - `intensity`: arbitrary units

### linear_fit.json
- path: `/app/outputs/linear_fit.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fit parameters for linear scaling of DOS peak intensity with H-concentration.
- schema:
  - `type`: object
  - `required`:
    - `H_peak_slope`: float
    - `H_peak_intercept`: float
    - `delta_peak_slope`: float
    - `delta_peak_intercept`: float

Notes: The checker compares the agent's computed values to hidden reference values derived from the paper's reported numbers, applying appropriate tolerances. Bond lengths are compared within tight tolerances, angles within a few degrees, band gaps and DOS peak energies within ~0.1 eV, and intensities within ~10%. The linear fit slopes are expected to match the paper's reported slopes to within a tolerance.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "structural_params.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "HSiSi_angle",
          "SiSi_nn_length",
          "SiSi_nnn_length",
          "HSi_length"
        ],
        "units": {
          "HSiSi_angle": "deg",
          "SiSi_nn_length": "Å",
          "SiSi_nnn_length": "Å",
          "HSi_length": "Å"
        }
      },
      "description": "Table of geometric parameters per hydrogenated silicene system."
    },
    {
      "file": "band_gaps.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "gap_type",
          "value_eV"
        ],
        "units": {
          "value_eV": "eV"
        }
      },
      "description": "Band gap types and values for each hydrogenated system."
    },
    {
      "file": "dos_peaks.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "system",
          "peak_energy_eV",
          "peak_type",
          "intensity"
        ],
        "units": {
          "peak_energy_eV": "eV",
          "intensity": "arbitrary units"
        }
      },
      "description": "List of identified DOS peaks with energies and intensities."
    },
    {
      "file": "linear_fit.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "H_peak_slope": "float",
          "H_peak_intercept": "float",
          "delta_peak_slope": "float",
          "delta_peak_intercept": "float"
        }
      },
      "description": "Fit parameters for linear scaling of DOS peak intensity with H-concentration."
    }
  ],
  "notes": "The checker compares the agent's computed values to hidden reference values derived from the paper's reported numbers, applying appropriate tolerances. Bond lengths are compared within tight tolerances, angles within a few degrees, band gaps and DOS peak energies within ~0.1 eV, and intensities within ~10%. The linear fit slopes are expected to match the paper's reported slopes to within a tolerance."
}
```

## How you are scored
A hidden verifier independently evaluates each scored artifact you produce. Your submitted values are compared to confidential reference values derived from the original study, using appropriate tolerances for each quantity (structural parameters, band gaps, peak energies, intensities, and linear-fit coefficients). The scores from all stages are combined into the final reward. You must follow the outlined workflow and compute the required artifacts; simply reporting reference numbers without executing the calculations will not succeed.
