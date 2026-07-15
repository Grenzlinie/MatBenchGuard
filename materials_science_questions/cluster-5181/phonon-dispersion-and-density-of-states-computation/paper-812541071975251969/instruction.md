# Neutron-weighted phonon density of states of ordered and disordered MgCl₂

## Problem background
MgCl₂-based Ziegler−Natta catalysts for olefin polymerization are typically prepared by ball‑milling, which introduces structural disorder and particle‑size effects that critically influence catalytic performance. Inelastic neutron scattering (INS) spectroscopy can probe the full lattice dynamics of these materials, and when combined with density‑functional theory (DFT) simulations, it can distinguish the spectral fingerprints of different types of disorder. However, interpreting the experimental INS spectra requires robust computational models of ordered and disordered MgCl₂. This task focuses on computing the neutron‑weighted phonon density of states (NWPDOS) for ordered α‑MgCl₂ and for a model that contains a translational stacking fault (δ_trans). The comparison of these spectra reveals how translational disorder modifies the vibrational fingerprint of bulk MgCl₂ in the 0–400 cm⁻¹ region.

## Approach
The approach uses plane‑wave DFT with an open‑source code to compute the full harmonic phonon dispersion of periodic supercells. Supercells are built for the ordered α‑MgCl₂ crystallographic cell and for a model that introduces a translational stacking fault (e.g., an ABCAB stacking sequence). After geometry optimisation, phonon frequencies and eigenvectors are obtained on a dense grid covering the Brillouin zone. The phonon density of states is partitioned into atomic contributions, and each species’ partial DOS is weighted by the ratio of its neutron scattering cross‑section to its atomic mass (values available from standard neutron‑scattering tables). The weighted partial DOS are summed to give the neutron‑weighted PDOS (NWPDOS), which is normalised to ∫g(ω)dω = 3N and convolved with a resolution function that approximates the instrument response. This procedure is performed for both the ordered and the disordered model to produce their NWPDOS curves. A difference spectrum (disordered minus ordered) is then computed to highlight spectral changes. Finally, the main vibrational bands in the 60–400 cm⁻¹ range are located and their relative intensities are extracted to quantify the disorder‑induced trends.

## Reproduction target
Produce the neutron‑weighted phonon density of states (NWPDOS) for ordered α‑MgCl₂ and for the translationally disordered δ_trans model, using the protocol described in the workflow steps. From these spectra, compute the difference spectrum (δ_trans minus α) and perform a peak analysis that identifies the five main bands in the 60–400 cm⁻¹ range, reporting their positions and relative intensities for each model. The submitted files are CSV files containing the NWPDOS curves and the difference spectrum, together with a JSON file that summarises the band positions, relative peak heights, and the observed differences between the two models.

## Assets

- MgCl₂ α crystal structure: ICSD 420500
- Quantum ESPRESSO: https://www.quantum-espresso.org/
- Phonopy: https://phonopy.github.io/phonopy/
- Neutron scattering cross-sections and atomic masses: https://www.ncnr.nist.gov/resources/n-lengths/

## Workflow steps

### Step 1: Model construction and DFT geometry optimization
- Role: process
- Action: Construct 3×3×3 supercells for ordered α-MgCl₂ (from public crystal structure) and for the disordered δ_trans model by introducing a translational stacking fault (e.g., ABCAB stacking). Perform DFT geometry optimization (open‑source code, e.g., Quantum ESPRESSO) to relax atomic positions and cell parameters until forces are below a tight threshold. Save the optimized structures.
- Evidence: `/app/outputs/optimized_ordered.cif, optimized_disordered.cif`

### Step 2: Phonon dispersion calculations
- Role: process
- Action: Using the optimized supercells, perform phonon calculations with Quantum ESPRESSO and Phonopy. Compute force constants (finite displacements or DFPT), then diagonalize dynamical matrices on a dense q‑point grid covering the Brillouin zone to obtain phonon frequencies and eigenvectors. Save the raw phonon data.
- Evidence: `/app/outputs/phonon_ordered.yaml, phonon_disordered.yaml`

### Step 3: Compute neutron‑weighted PDOS for ordered α‑MgCl₂
- Role: scored (load-bearing)
- Action: From the phonon frequencies and eigenvectors of the ordered model, compute the neutron‑weighted phonon density of states (NWPDOS). Use atomic masses (Mg: 24.305 u, Cl: 35.453 u) and neutron scattering cross‑sections (Mg: 3.63 barn bound coherent, Cl: 16.8 barn total bound). For each atomic species, weight the partial DOS by σ_a / M_a and sum. Normalize the spectrum to ∫g(ω)dω = 3N. Optionally apply a Gaussian convolution matching an instrument resolution function. Output a CSV covering 0–400 cm⁻¹.
- Output file: `/app/outputs/step_01_nwpdos_ordered.csv`
- Format: csv
- Contract: Two columns: energy_cm1 (float, in cm⁻¹), nwpdos (float, normalized). Rows cover the energy range 0–400 cm⁻¹.
- Scoring: scored by hidden verifier

### Step 4: Compute neutron‑weighted PDOS for disordered δ_trans model
- Role: scored (load-bearing)
- Action: Same procedure as the ordered NWPDOS step but applied to the δ_trans (translationally disordered) model using its phonon data. Ensure the same normalization, energy grid, and resolution convolution. Output CSV.
- Output file: `/app/outputs/step_02_nwpdos_disordered_delta_trans.csv`
- Format: csv
- Contract: Two columns: energy_cm1 (float, in cm⁻¹), nwpdos (float, normalized). Same energy grid as step_01.
- Scoring: scored by hidden verifier

### Step 5: Compute difference spectrum
- Role: scored
- Action: Interpolate the ordered and disordered NWPDOS spectra from the previous two steps onto a common energy grid (e.g., 0 to 400 cm⁻¹ in steps of 1 cm⁻¹). Compute delta_nwpdos = disordered_nwpdos − ordered_nwpdos. Save as CSV.
- Output file: `/app/outputs/step_03_difference_spectrum.csv`
- Format: csv
- Contract: Two columns: energy_cm1 (float, in cm⁻¹), delta_nwpdos (float).
- Scoring: scored by hidden verifier

### Step 6: Peak analysis of the main bands
- Role: scored
- Action: From the ordered and disordered NWPDOS spectra, identify the five main bands in the 60–400 cm⁻¹ range: approximately 100 cm⁻¹ doublet, 162 cm⁻¹, 200 cm⁻¹, 236 cm⁻¹, and 251 cm⁻¹. Determine the exact peak positions (local maxima within a tolerance window) and their relative intensities (peak height divided by the maximum peak height in that spectrum). Report as JSON with ordered_bands and disordered_bands arrays of objects {peak_cm1, relative_intensity} and a trends field describing the observed changes.
- Output file: `/app/outputs/step_04_peak_analysis.json`
- Format: json
- Contract: JSON object with fields: ordered_bands (array of objects with peak_cm1:float, relative_intensity:float), disordered_bands (same schema), and trends (string description of how the bands changed).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_nwpdos_ordered.csv`
- `/app/outputs/step_02_nwpdos_disordered_delta_trans.csv`
- `/app/outputs/step_03_difference_spectrum.csv`
- `/app/outputs/step_04_peak_analysis.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_nwpdos_ordered.csv
- path: `/app/outputs/step_01_nwpdos_ordered.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Neutron‑weighted phonon density of states for ordered α‑MgCl₂. The checker recomputes peak positions and relative intensities from this raw spectrum and compares them to hidden gold values.
- schema:
  - `type`: table
  - `required_columns`: `energy_cm1`, `nwpdos`
  - `units`:
    - `energy_cm1`: cm⁻¹
    - `nwpdos`: normalized (arbitrary units)

### step_02_nwpdos_disordered_delta_trans.csv
- path: `/app/outputs/step_02_nwpdos_disordered_delta_trans.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Neutron‑weighted phonon density of states for the translationally disordered δ_trans model. The checker recomputes peak positions and intensities similarly.
- schema:
  - `type`: table
  - `required_columns`: `energy_cm1`, `nwpdos`
  - `units`:
    - `energy_cm1`: cm⁻¹
    - `nwpdos`: normalized (arbitrary units)

### step_03_difference_spectrum.csv
- path: `/app/outputs/step_03_difference_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Difference spectrum (disordered minus ordered). The checker verifies that the delta at the 200, 236, and 251 cm⁻¹ bands is negative (indicating decreased intensity in the disordered model).
- schema:
  - `type`: table
  - `required_columns`: `energy_cm1`, `delta_nwpdos`
  - `units`:
    - `energy_cm1`: cm⁻¹
    - `delta_nwpdos`: arbitrary units

### step_04_peak_analysis.json
- path: `/app/outputs/step_04_peak_analysis.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Extracted peak positions and relative intensities for both models, with a textual trends summary. The checker compares these extracted values to hidden gold references.
- schema:
  - `type`: object
  - `required`:
    - `ordered_bands`: array of objects with peak_cm1 (float) and relative_intensity (float)
    - `disordered_bands`: array of objects with peak_cm1 (float) and relative_intensity (float)
    - `trends`: string

Notes: All NWPDOS spectra must be normalized to the same condition (∫g(ω)dω = 3N). The hidden checker will use the NWPDOS CSVs to locate peaks, compute relative intensities, and verify the sign of the difference. The peak analysis JSON is expected to be consistent with the CSVs.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_nwpdos_ordered.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_cm1",
          "nwpdos"
        ],
        "units": {
          "energy_cm1": "cm⁻¹",
          "nwpdos": "normalized (arbitrary units)"
        }
      },
      "description": "Neutron‑weighted phonon density of states for ordered α‑MgCl₂. The checker recomputes peak positions and relative intensities from this raw spectrum and compares them to hidden gold values."
    },
    {
      "file": "step_02_nwpdos_disordered_delta_trans.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_cm1",
          "nwpdos"
        ],
        "units": {
          "energy_cm1": "cm⁻¹",
          "nwpdos": "normalized (arbitrary units)"
        }
      },
      "description": "Neutron‑weighted phonon density of states for the translationally disordered δ_trans model. The checker recomputes peak positions and intensities similarly."
    },
    {
      "file": "step_03_difference_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "energy_cm1",
          "delta_nwpdos"
        ],
        "units": {
          "energy_cm1": "cm⁻¹",
          "delta_nwpdos": "arbitrary units"
        }
      },
      "description": "Difference spectrum (disordered minus ordered). The checker verifies that the delta at the 200, 236, and 251 cm⁻¹ bands is negative (indicating decreased intensity in the disordered model)."
    },
    {
      "file": "step_04_peak_analysis.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "ordered_bands": "array of objects with peak_cm1 (float) and relative_intensity (float)",
          "disordered_bands": "array of objects with peak_cm1 (float) and relative_intensity (float)",
          "trends": "string"
        }
      },
      "description": "Extracted peak positions and relative intensities for both models, with a textual trends summary. The checker compares these extracted values to hidden gold references."
    }
  ],
  "notes": "All NWPDOS spectra must be normalized to the same condition (∫g(ω)dω = 3N). The hidden checker will use the NWPDOS CSVs to locate peaks, compute relative intensities, and verify the sign of the difference. The peak analysis JSON is expected to be consistent with the CSVs."
}
```

## How you are scored
The submission is automatically evaluated by a hidden verifier. The verifier reads the CSV files and the JSON file, extracts the five main vibrational bands, computes their positions and relative intensities, and compares them to reference values within a predefined tolerance. The difference spectrum is checked for the expected sign of intensity changes at specific energy regions. Each scored artifact (the two NWPDOS CSVs, the difference CSV, and the peak‑analysis JSON) contributes a weighted fraction of the total reward; partial credit is awarded when only some of the expected features are correctly reproduced. The verifier does not read any intermediate model‑construction or phonon‑calculation outputs; only the specified output files are scored.
