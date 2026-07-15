# Transmittance and Angular Beaming from a Single Slit with Asymmetric Groove Arrays via Modal Expansion

## Problem background
Controlling light at subwavelength scales with patterned metal films is a key challenge in nanophotonics. One geometry of interest is a single slit in a thin metallic film (treated as a perfect conductor) flanked by periodic arrays of rectangular grooves. The input-side corrugations can selectively enhance transmission at chosen wavelengths, while the output-side corrugations can shape the transmitted light into narrow beams. This task investigates an asymmetric structure containing four finite groove arrays (two on the input side, two on the output side) that demonstrates dual‑wavelength transmission and angular beaming. The goal is to compute the normalized transmittance spectrum and the far‑field angular distribution for a specific set of geometrical parameters using a modal expansion formalism.

## Approach
The computation uses a modal expansion approach for p‑polarized light. The metal is approximated as a perfect conductor, so the electromagnetic fields inside the slit and grooves are expanded in simple waveguide modes; only the fundamental propagative mode is kept at subwavelength openings. In the vacuum regions the fields are expanded in plane waves. Matching the tangential field components at the interfaces yields a set of coupled linear equations for the complex amplitudes of the modes in all indentations. These equations involve projected two‑dimensional Green’s functions (Hankel functions) that account for radiative coupling between indentations. Once the modal amplitudes are obtained by solving the linear system, the normalized transmittance follows from the slit amplitudes, and the far‑field angular transmission distribution (normalized radial Poynting vector) is evaluated from the output‑side amplitudes using the Green’s function. The geometry includes four periodic arrays (left/right on input and output sides) with user‑specified periods and depths, and the solver must be capable of evaluating the system at arbitrary visible wavelengths.

## Reproduction target
Consider the specific structure with four arrays (IL, IR, OL, OR) and the following fixed parameters: all indentation widths a = 40 nm, number of grooves per array N = 10, metal thickness W = 200 nm. The left‑side groove period is d_L = 470 nm and depth h_L = 75 nm; the right‑side groove period is d_R = 560 nm and depth h_R = 95 nm. Under these conditions:

- Compute the normalized‑to‑area transmittance T(λ) for wavelengths from 400 nm to 800 nm, with a step no larger than 5 nm. Save the result as `transmittance_spectrum.csv` with columns `wavelength_nm` and `transmittance_T`.
- Compute the far‑field angular transmission distribution I(θ) (normalized radial Poynting vector) at λ = 500 nm and λ = 600 nm, for angles θ from 0° to 90° with a step no larger than 1°. Save the result as `far_field_angular.csv` with columns `wavelength_nm`, `angle_deg`, and `intensity_I`.

The outputs must reflect the physical effects of the groove arrays: the transmittance spectrum should exhibit resonant features, and the angular distributions should display narrow beaming at the targeted wavelengths.

## Assets

- Python 3.x
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement modal expansion solver
- Role: process
- Action: Write a program implementing the coupled modal expansion formalism for p-polarized light incident on a thin perfect-metal film pierced by a single slit and flanked by finite one-dimensional arrays of rectangular grooves on both input and output surfaces. The geometry parameters are: all indentation widths a = 40 nm, number of grooves per array N = 10, metal thickness W = 200 nm. The program must compute the complex modal amplitudes E_α^I (input side) and E_β^O (output side) by assembling and solving the linear system that couples all indentations via projected two-dimensional Green's functions. The only external inputs are the wavelength and the fixed geometry. The solver must be able to evaluate the system at arbitrary wavelengths in the visible range.
- Evidence: `/app/outputs/solver_log.txt`

### Step 2: Compute transmittance spectrum
- Role: scored (load-bearing)
- Action: Using the implemented solver, compute the normalized-to-area transmittance T(λ) for the full four-array structure (IL, IR, OL, OR) with groove parameters d_L = 470 nm, h_L = 75 nm (left side) and d_R = 560 nm, h_R = 95 nm (right side) on both input and output surfaces. Sweep wavelengths from 400 nm to 800 nm with a step no larger than 5 nm. For each wavelength, obtain the slit modal amplitudes and evaluate T = Im(E_0^I E_0^{O*}) / sin(kW). Save the complete spectrum.
- Output file: `/app/outputs/transmittance_spectrum.csv`
- Format: csv
- Contract: Two columns: wavelength_nm (float, range 400‑800, step ≤5 nm) and transmittance_T (float, dimensionless, normalized as defined in the formalism).
- Scoring: scored by hidden verifier

### Step 3: Compute far-field angular distribution
- Role: scored
- Action: Using the implemented solver, compute the far‑field angular transmission distribution I(θ) (normalized radial Poynting vector) at the two resonant wavelengths λ = 500 nm and λ = 600 nm for the same structure. Evaluate θ from 0° to 90° with a step no larger than 1°. Save the results for both wavelengths in one file.
- Output file: `/app/outputs/far_field_angular.csv`
- Format: csv
- Contract: Three columns: wavelength_nm (float, value 500 or 600), angle_deg (float, 0 to 90°, step ≤1°), intensity_I (float, dimensionless, normalized radial Poynting vector).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/transmittance_spectrum.csv`
- `/app/outputs/far_field_angular.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### transmittance_spectrum.csv
- path: `/app/outputs/transmittance_spectrum.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Normalized transmittance spectrum for the four-array structure. Checked against hidden reference peak positions and peak heights.
- schema:
  - `required_columns`: `wavelength_nm`, `transmittance_T`
  - `units`:
    - `wavelength_nm`: nm
    - `transmittance_T`: dimensionless (normalized)
  - `description`: Two-column CSV: wavelength_nm (float) and transmittance_T (float).

### far_field_angular.csv
- path: `/app/outputs/far_field_angular.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Far‑field angular distribution at the two resonant wavelengths. Main lobe direction and relative side‑lobe suppression checked against hidden references.
- schema:
  - `required_columns`: `wavelength_nm`, `angle_deg`, `intensity_I`
  - `units`:
    - `wavelength_nm`: nm
    - `angle_deg`: degrees
    - `intensity_I`: dimensionless (normalized radial Poynting vector)
  - `description`: Three-column CSV: wavelength_nm (float, 500 or 600), angle_deg (float, 0‑90), intensity_I (float).

Notes: The hidden checker will verify that the transmittance spectrum shows two distinct resonant peaks near the target wavelengths with adequate height, and that the angular distributions exhibit narrow beaming near the expected directions with appropriate lobe suppression. No gold values are disclosed here.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "transmittance_spectrum.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "wavelength_nm",
          "transmittance_T"
        ],
        "units": {
          "wavelength_nm": "nm",
          "transmittance_T": "dimensionless (normalized)"
        },
        "description": "Two-column CSV: wavelength_nm (float) and transmittance_T (float)."
      },
      "description": "Normalized transmittance spectrum for the four-array structure. Checked against hidden reference peak positions and peak heights."
    },
    {
      "file": "far_field_angular.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "required_columns": [
          "wavelength_nm",
          "angle_deg",
          "intensity_I"
        ],
        "units": {
          "wavelength_nm": "nm",
          "angle_deg": "degrees",
          "intensity_I": "dimensionless (normalized radial Poynting vector)"
        },
        "description": "Three-column CSV: wavelength_nm (float, 500 or 600), angle_deg (float, 0‑90), intensity_I (float)."
      },
      "description": "Far‑field angular distribution at the two resonant wavelengths. Main lobe direction and relative side‑lobe suppression checked against hidden references."
    }
  ],
  "notes": "The hidden checker will verify that the transmittance spectrum shows two distinct resonant peaks near the target wavelengths with adequate height, and that the angular distributions exhibit narrow beaming near the expected directions with appropriate lobe suppression. No gold values are disclosed here."
}
```

## How you are scored
A hidden verifier independently checks your submitted artifacts. The verifier compares the transmittance spectrum and the angular distributions to reference characteristics that are derived from the expected physical behaviour (the presence and location of transmission resonances, their relative strengths, the direction and narrowness of the beaming lobes). The scoring is based on how closely your computed quantities reproduce those target features, not on reporting a specific number. The exact tolerances and criteria are kept hidden, so you must implement the solver correctly and produce the full data files described in the workflow steps. Each scored artifact contributes a weight to the final reward; the combined score reflects the overall fidelity of the reproduction.
