# Reproduction of Ultra-Broadband High Reflectivity in Subwavelength Grating-Slab Waveguide Structures via RCWA

## Problem background
A subwavelength dielectric grating on a slab waveguide is investigated for its potential to provide high reflectivity over a wide frequency range and a broad range of incident angles. The structure consists of a periodic grating layer (period Λ, duty cycle η) on top of a uniform slab layer, both made of the same high-permittivity material. When illuminated by a TM-polarized plane wave, the interference among Fabry-Perot modes, slab waveguide modes, and waveguide-array modes can shape the reflectivity spectrum. This task reproduces the reflectivity properties of two specific designs: a thin-grating variant that reveals the mode dispersion, and an optimized thick-grating variant whose reflectivity bandwidth and angular tolerance are unknown quantities you must compute from first-principles electromagnetic simulation.

## Approach
The optical response of the periodic structure is simulated with rigorous coupled-wave analysis (RCWA), which expands the fields in Fourier series and solves the boundary-value problem in each layer. The recommended solver is the open-source S4 package, though any correct RCWA implementation is acceptable. All length scales are normalized to the grating period Λ; the absolute value of Λ does not matter because the results are expressed in normalized frequency units (2πc/Λ). Three simulation regimes are required:
- A thin-grating structure (grating thickness h1=0.167Λ) is simulated over a grid of slab thicknesses h2 (0 to 1.5Λ) and normalized frequencies (0.2 to 0.8). This produces a reflectivity contour map that visualizes the guided-mode dispersion and the three propagation regimes.
- An optimized thick-grating structure (h1=0.685Λ, h2=0.45Λ) is simulated at normal incidence over a fine frequency grid covering 0.3 to 0.7. The resulting reflectivity spectrum is used to extract the continuous frequency band where R > 0.99.
- The same thick-grating structure is simulated at a fixed normalized frequency of 0.5 over incident angles from 0° to 80° in steps of at most 1°. The angle-dependent reflectivity is used to extract the angular span where R > 0.99.
All simulations assume TM polarization, permittivity εr=11.9, and duty cycle η=0.5.

## Reproduction target
Produce the following three artifacts from your own RCWA simulations:

1) `reflectivity_contour.csv` – a table of reflectivity values for the thin-grating structure (h1=0.167Λ) spanning h2/Λ ∈ [0, 1.5] and normalized frequency ∈ [0.2, 0.8]. This map demonstrates the mode dispersion; its primary purpose is to verify the simulation setup.

2) `reflectivity_spectrum.csv` – a table of reflectivity vs. normalized frequency (0.3 to 0.7) for the thick-grating design (h1=0.685Λ, h2=0.45Λ). From this spectrum, compute the largest contiguous frequency interval where reflectivity > 0.99 and derive the fractional bandwidth Δf/f̄ (where f̄ is the midpoint of that interval). The goal is to determine whether this bandwidth meets a performance threshold.

3) `angle_scan.csv` – a table of reflectivity vs. incident angle (0° to 80°) for the same thick-grating design at a fixed normalized frequency of 0.5. From this scan, compute the contiguous angular range where reflectivity > 0.99. The goal is to determine whether this angular range meets a performance threshold.

The thresholds themselves are hidden; your job is to produce accurate simulation data from which the bandwidth and angular range can be computed. All three CSV files must follow the column schemas given in the workflow steps.

## Assets

- S4 (RCWA solver): https://github.com/victorliu529/S4

## Workflow steps

### Step 1: Reflectivity contour for thin grating slab waveguide
- Role: scored
- Action: Run RCWA simulation for the free-standing thin-grating slab waveguide structure with grating thickness h1=0.167Λ, duty cycle 0.5, permittivity 11.9, TM-polarized surface-normal incidence. Compute reflectivity over a slab thickness range (h2) from 0 to 1.5Λ and normalized frequency range 0.2 to 0.8 (units of 2πc/Λ), producing a regular grid of reflectivity values.
- Output file: `/app/outputs/reflectivity_contour.csv`
- Format: csv
- Contract: Columns: h2_over_Lambda (float, slab thickness in units of Λ), normalized_frequency (float, frequency in units of 2πc/Λ), reflectivity (float, 0–1).
- Scoring: scored by hidden verifier

### Step 2: Reflectivity spectrum for thick grating slab waveguide
- Role: scored (load-bearing)
- Action: Run RCWA simulation for the optimized grating-slab waveguide structure with h1=0.685Λ, h2=0.45Λ, duty cycle 0.5, permittivity 11.9, TM-polarized surface-normal incidence. Compute reflectivity over the normalized frequency range 0.3 to 0.7 (2πc/Λ) with sufficient resolution to resolve the high-reflectivity (R>0.99) band.
- Output file: `/app/outputs/reflectivity_spectrum.csv`
- Format: csv
- Contract: Columns: normalized_frequency (float, unitless), reflectivity (float, 0–1).
- Scoring: scored by hidden verifier

### Step 3: Angle-dependent reflectivity at fixed frequency
- Role: scored (load-bearing)
- Action: Run RCWA simulation for the same thick grating structure (h1=0.685Λ, h2=0.45Λ) at a fixed normalized frequency 0.5×2πc/Λ. Compute reflectivity for incident angles from 0° to 80° in steps ≤1°.
- Output file: `/app/outputs/angle_scan.csv`
- Format: csv
- Contract: Columns: angle_deg (float, degrees), reflectivity (float, 0–1).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/reflectivity_contour.csv`
- `/app/outputs/reflectivity_spectrum.csv`
- `/app/outputs/angle_scan.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### reflectivity_contour.csv
- path: `/app/outputs/reflectivity_contour.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Reflectivity contour map for the thin-grating structure. Verified for existence, expected columns, and data within reasonable ranges.
- schema:
  - `type`: table
  - `required_columns`: `h2_over_Lambda`, `normalized_frequency`, `reflectivity`
  - `units`:
    - `h2_over_Lambda`: unitless (fraction of Λ)
    - `normalized_frequency`: unitless (2πc/Λ)
    - `reflectivity`: fraction 0-1

### reflectivity_spectrum.csv
- path: `/app/outputs/reflectivity_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Reflectivity spectrum for the optimized structure. The checker recomputes the fractional bandwidth where reflectivity > 0.99 and compares to the hidden threshold using threshold_or_better.
- schema:
  - `type`: table
  - `required_columns`: `normalized_frequency`, `reflectivity`
  - `units`:
    - `normalized_frequency`: unitless (2πc/Λ)
    - `reflectivity`: fraction 0-1

### angle_scan.csv
- path: `/app/outputs/angle_scan.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Angle-dependent reflectivity for the optimized structure. The checker recomputes the angular range where reflectivity > 0.99 and compares to the hidden threshold using threshold_or_better.
- schema:
  - `type`: table
  - `required_columns`: `angle_deg`, `reflectivity`
  - `units`:
    - `angle_deg`: degrees
    - `reflectivity`: fraction 0-1

Notes: The solver may be S4 or any equivalent RCWA implementation. All structure parameters are fully normalized; any absolute period Λ may be chosen. The checker performs a structural audit on the contour map and recomputes bandwidth/angular range from the other two CSVs. No pixel-level comparison with the paper's figures is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "reflectivity_contour.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "h2_over_Lambda",
          "normalized_frequency",
          "reflectivity"
        ],
        "units": {
          "h2_over_Lambda": "unitless (fraction of Λ)",
          "normalized_frequency": "unitless (2πc/Λ)",
          "reflectivity": "fraction 0-1"
        }
      },
      "description": "Reflectivity contour map for the thin-grating structure. Verified for existence, expected columns, and data within reasonable ranges."
    },
    {
      "file": "reflectivity_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "normalized_frequency",
          "reflectivity"
        ],
        "units": {
          "normalized_frequency": "unitless (2πc/Λ)",
          "reflectivity": "fraction 0-1"
        }
      },
      "description": "Reflectivity spectrum for the optimized structure. The checker recomputes the fractional bandwidth where reflectivity > 0.99 and compares to the hidden threshold using threshold_or_better."
    },
    {
      "file": "angle_scan.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "angle_deg",
          "reflectivity"
        ],
        "units": {
          "angle_deg": "degrees",
          "reflectivity": "fraction 0-1"
        }
      },
      "description": "Angle-dependent reflectivity for the optimized structure. The checker recomputes the angular range where reflectivity > 0.99 and compares to the hidden threshold using threshold_or_better."
    }
  ],
  "notes": "The solver may be S4 or any equivalent RCWA implementation. All structure parameters are fully normalized; any absolute period Λ may be chosen. The checker performs a structural audit on the contour map and recomputes bandwidth/angular range from the other two CSVs. No pixel-level comparison with the paper's figures is required."
}
```

## How you are scored
A hidden verifier inspects your three output CSVs and combines the results into a single final reward.

- `reflectivity_contour.csv` receives a low weight (structural audit). The checker verifies that the file exists, has the required columns, and contains data within plausible ranges.

- `reflectivity_spectrum.csv` receives a high weight. The checker recomputes the fractional bandwidth (Δf/f̄) for the R>0.99 band directly from your data and compares it against a hidden threshold using a threshold_or_better policy: meeting or exceeding the hidden target earns full credit, while a smaller bandwidth receives a proportionally lower score.

- `angle_scan.csv` receives a high weight. The checker recomputes the angular range where R>0.99 directly from your data and evaluates it against a hidden threshold with the same threshold_or_better policy.

You must not hard-code or guess the reported numbers; only the computed metrics derived from your RCWA data are scored. Failing to produce valid CSV artifacts, or submitting data from which no meaningful bandwidth or angular range can be extracted, will result in zero credit for those components.
