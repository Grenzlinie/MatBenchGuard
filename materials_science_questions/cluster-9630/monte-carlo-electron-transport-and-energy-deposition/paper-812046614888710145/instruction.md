# Monte Carlo Simulation of X-ray Source Distribution in Pt Foil

## Problem background
The X-ray ultraMicroscope (XuM) is a projection X-ray microscope that uses a focused electron beam on a metal target to generate a sub‑micron X‑ray source. The finite spatial extent of the X‑ray generation volume acts as a blurring kernel for the recorded projection images, limiting the achievable resolution. To restore image sharpness via deconvolution, the X‑ray source distribution within the target must be accurately modeled. This task implements the core Monte Carlo simulation that computes the energy‑resolved X‑ray production for a thin foil target, providing the input needed for downstream image restoration.

## Approach
The simulation uses a single‑scattering Monte Carlo method to track electrons as they travel through a pure Pt foil. For each electron, elastic scattering is modeled (e.g., screened Rutherford) and energy loss is treated with the Bethe stopping power. At each interaction point, the code evaluates the probability of producing characteristic K, L, and M X‑rays or bremsstrahlung X‑rays (discretised into 60 energy bins) and accounts for X‑ray absorption within the target using mass attenuation coefficients. The generated X‑rays are projected onto a plane normal to the beam‑detector direction to build the 2D source distribution, and simultaneously tallied in depth slices to obtain the depth‑resolved generation profile.

## Reproduction target
Implement a single‑scattering Monte Carlo electron‑transport simulation for a 50 nm thick pure Pt foil target, irradiated by a 30 keV electron beam at normal incidence. Model the production of K, L, M characteristic X‑rays and bremsstrahlung X‑rays (60 energy bins), include electron energy loss (Bethe stopping power), and account for X‑ray absorption within the target. From the simulation, compute: (1) the projected X‑ray source distribution sampled on a 401×401 grid on a plane normal to the beam‑detector direction, centered on the beam axis; (2) the depth‑resolved X‑ray generation in 100 equal‑thickness slices spanning the full 50 nm thickness. Save the projected distribution as `projected_source_distribution.csv` (no header, 401 rows of 401 comma‑separated floating‑point numbers) and the depth‑resolved generation as `depth_resolved_generation.csv` (header: slice_index,depth_midpoint_nm,generation_intensity_arbunits, 100 rows). Do not apply any detector‑efficiency correction (assume ideal unity efficiency).

## Assets
The simulation relies on publicly known physical constants for platinum: atomic number (78), density (21.45 g/cm³), K/L/M shell binding energies, and mass attenuation coefficients for X‑ray absorption. These values are available from standard references such as NIST. No additional datasets, pre‑trained models, or proprietary tools are required.

## Workflow steps

### Step 1: Run SS_MC electron transport simulation
- Role: process
- Action: Implement a single-scattering Monte Carlo electron transport simulation for a 50 nm thick pure Pt foil target with a 30 keV electron beam at normal incidence. Model elastic scattering, electron energy loss (Bethe stopping power), production of K, L, M characteristic X-rays, bremsstrahlung X-rays (60 energy bins), and X-ray absorption within the target. Accumulate the projected X-ray source distribution on a 401x401 grid (plane normal to beam-detector direction, detector far away) and the depth-resolved X-ray generation in 100 depth slices across the foil thickness. Store the resulting arrays for later extraction.
- Evidence: `/app/outputs/simulation_arrays.npz`

### Step 2: Write projected source distribution
- Role: scored (load-bearing)
- Action: From the stored simulation data, write the projected X-ray source distribution to projected_source_distribution.csv as a 401x401 array of floating-point numbers (comma-separated, no header).
- Output file: `/app/outputs/projected_source_distribution.csv`
- Format: csv
- Contract: CSV file with 401 rows and 401 columns of floating-point numbers, no header row.
- Scoring: scored by hidden verifier

### Step 3: Write depth-resolved generation
- Role: scored (load-bearing)
- Action: From the stored simulation data, write the depth-resolved X-ray generation to depth_resolved_generation.csv with header: slice_index,depth_midpoint_nm,generation_intensity_arbunits, containing 100 rows.
- Output file: `/app/outputs/depth_resolved_generation.csv`
- Format: csv
- Contract: CSV file with header 'slice_index,depth_midpoint_nm,generation_intensity_arbunits', 100 rows (slice_index 1..100, depth_midpoint_nm in nm, generation_intensity_arbunits total X-ray generation per slice).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/projected_source_distribution.csv`
- `/app/outputs/depth_resolved_generation.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### projected_source_distribution.csv
- path: `/app/outputs/projected_source_distribution.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: 2D projected X-ray source distribution; checker computes MAPE against a hidden reference array.
- schema:
  - `type`: other
  - `shape`: `401`, `401`
  - `dtype`: float
  - `description`: 401x401 array of X-ray intensity values, no header, comma-separated.

### depth_resolved_generation.csv
- path: `/app/outputs/depth_resolved_generation.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: 1D depth-resolved X-ray generation profile; checker compares total integrated generation to a hidden reference value.
- schema:
  - `type`: table
  - `required_columns`: `slice_index`, `depth_midpoint_nm`, `generation_intensity_arbunits`
  - `units`:
    - `depth_midpoint_nm`: nm
    - `generation_intensity_arbunits`: arbitrary units

Notes: Both outputs are scored by comparison to pre-bundled reference arrays (hidden). Tolerances mirror legitimate inter-code variability of different Monte Carlo implementations. No detector-efficiency correction is applied.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "projected_source_distribution.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "other",
        "shape": [
          401,
          401
        ],
        "dtype": "float",
        "description": "401x401 array of X-ray intensity values, no header, comma-separated."
      },
      "description": "2D projected X-ray source distribution; checker computes MAPE against a hidden reference array."
    },
    {
      "file": "depth_resolved_generation.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "slice_index",
          "depth_midpoint_nm",
          "generation_intensity_arbunits"
        ],
        "units": {
          "depth_midpoint_nm": "nm",
          "generation_intensity_arbunits": "arbitrary units"
        }
      },
      "description": "1D depth-resolved X-ray generation profile; checker compares total integrated generation to a hidden reference value."
    }
  ],
  "notes": "Both outputs are scored by comparison to pre-bundled reference arrays (hidden). Tolerances mirror legitimate inter-code variability of different Monte Carlo implementations. No detector-efficiency correction is applied."
}
```

## How you are scored
A hidden verifier independently examines your two scored output files. For `projected_source_distribution.csv`, the verifier computes a mean absolute percentage error (MAPE) against a hidden reference array produced by a trusted Monte Carlo implementation for the identical geometry and beam parameters; your score reflects how closely your distribution matches the reference only on pixels with intensity above a specified threshold. For `depth_resolved_generation.csv`, the verifier sums the `generation_intensity_arbunits` over all 100 slices and compares this total integrated generation to a hidden reference total. The final reward is a combination of the scores from both artifacts. Reporting the paper’s numbers without actually running the simulation will not receive credit.
