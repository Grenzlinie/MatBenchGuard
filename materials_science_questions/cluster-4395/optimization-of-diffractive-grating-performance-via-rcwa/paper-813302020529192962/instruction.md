# Minimum Grating Period for a Liquid Crystal Sinusoidal Phase Grating with Alternating Pre-tilt Angles

## Problem background
Liquid crystal (LC) diffractive optical elements (DOEs) that use inhomogeneous alignment offer an electrode-free approach to creating tunable phase profiles. A key design question is how small the grating period can be made when the phase pattern is defined solely by a spatial variation of the pre‑tilt angle under strong anchoring. Elastic coupling between LC molecules creates a transition (fly‑back) zone that limits the achievable period. This task focuses on a sinusoidal phase grating where one half of each period has a planar pre‑tilt of 2° and the other half has a homeotropic pre‑tilt of 90°. The aim is to compute the relation between the achievable phase modulation depth and the relative grating period Λ/d, and from that relationship determine the minimum period that still delivers a target retardation modulation of 0.38λ, which corresponds to zero intensity in the 0th diffraction order. The material under study is the nematic LC E44 (from Merck) at wavelength 588 nm.

## Approach
The core of the task is a two‑step computational pipeline. First, a 2D numerical model of the LC director distribution is set up. The model solves the Frank‑Oseen elastic free energy with strong anchoring boundary conditions: alternating pre‑tilt angles of 2° and 90° over half‑periods. The director field is computed for several values of the relative period Λ/d (e.g., 0.5, 1, 2, 4, 8). For each simulation, the effective extraordinary refractive index profile along the grating direction is obtained, from which a normalized phase parameter η(x) is derived. The modulation depth Δη = max(η) − min(η) is recorded. Next, a linear least‑squares fit of Δη versus Λ/d yields two coefficients, a (slope) and b (intercept). Using the fit, the minimum grating period Λ that achieves a retardation modulation of 0.38λ for a given cell gap d is given by Λ = (1/a)(0.38λ/Δn − b d), where Δn = n_e − n_o, λ = 588 nm. The cell gap at which the required period drops to zero (d_zero) is also computed as d_zero = (0.38λ)/(b Δn). All steps use the published material constants for E44: K11=1.55×10^{-11} N, K33=2.8×10^{-11} N, Δε=16.8, n_e=1.7859, n_o=1.5278.

## Reproduction target
Reproduce the linear fit coefficients a and b from the simulation data for a sinusoidal grating with alternating pre‑tilt angles under strong anchoring. From these coefficients, compute the minimum grating period Λ_min (in μm) for a cell gap d=0.86 μm and the zero‑period thickness d_zero (in μm). Write the four scalars (a, b, Λ_min, d_zero) into the output file sinusoidal_grating_results.json. The simulation step must use the specified LC material parameters and produce the intermediate Δη vs Λ/d data (delta_eta_raw.csv) as evidence that the simulation was performed.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Simulate sinusoidal grating and compute Δη vs Λ/d
- Role: process
- Action: Implement a 2D solver for the LC director orientation under strong anchoring. For a sinusoidal grating with half-period pre-tilt angle 2° and the other half 90°, simulate the director distribution for at least five values of Λ/d (e.g., 0.5, 1, 2, 4, 8). For each, compute the effective extraordinary index profile along the period, obtain the normalized phase parameter η(x), and extract the modulation Δη = max(η) - min(η). Use material parameters for E44: K11=1.55e-11 N, K33=2.8e-11 N, Δε=16.8, n_e=1.7859, n_o=1.5278.
- Evidence: `/app/outputs/delta_eta_raw.csv`

### Step 2: Linear fit and compute minimum period
- Role: scored (load-bearing)
- Action: Fit a straight line Δη = a*(Λ/d) + b using the data from step_01. Compute the minimum grating period Λ for a target retardation modulation of 0.38λ using the derived formula Λ = (1/a)*(0.38λ/Δn - b*d). Use λ=588 nm and Δn = n_e - n_o = 0.2581. Evaluate at d=0.86 μm to obtain Λ_min. Also find d_zero where Λ=0, i.e., d_zero = (0.38λ)/(b*Δn). Save a, b, Λ_min (in μm), and d_zero (in μm) to the output file.
- Output file: `/app/outputs/sinusoidal_grating_results.json`
- Format: json
- Contract: {"a": float, "b": float, "Lambda_min": float, "d_zero": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/sinusoidal_grating_results.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### sinusoidal_grating_results.json
- path: `/app/outputs/sinusoidal_grating_results.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Fitted linear coefficients a and b from simulated Δη vs Λ/d, and derived minimum grating period Lambda_min for d=0.86 um and thickness d_zero where Lambda_min becomes zero for liquid crystal material E44 at wavelength 588 nm.
- schema:
  - `type`: object
  - `required`:
    - `a`: number
    - `b`: number
    - `Lambda_min`: number
    - `d_zero`: number
  - `items`: object
  - `required_columns`:
  - `units`:
    - `a`: dimensionless
    - `b`: dimensionless
    - `Lambda_min`: um
    - `d_zero`: um

Notes: The simulation step uses LC material E44 parameters (K11, K33, Delta_epsilon, n_e, n_o). The sinusoidal grating is defined with alternating pre-tilt angles 2° and 90° under strong anchoring. The target retardation modulation is 0.38λ.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "sinusoidal_grating_results.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "a": "number",
          "b": "number",
          "Lambda_min": "number",
          "d_zero": "number"
        },
        "items": {},
        "required_columns": [],
        "units": {
          "a": "dimensionless",
          "b": "dimensionless",
          "Lambda_min": "um",
          "d_zero": "um"
        }
      },
      "description": "Fitted linear coefficients a and b from simulated Δη vs Λ/d, and derived minimum grating period Lambda_min for d=0.86 um and thickness d_zero where Lambda_min becomes zero for liquid crystal material E44 at wavelength 588 nm."
    }
  ],
  "notes": "The simulation step uses LC material E44 parameters (K11, K33, Delta_epsilon, n_e, n_o). The sinusoidal grating is defined with alternating pre-tilt angles 2° and 90° under strong anchoring. The target retardation modulation is 0.38λ."
}
```

## How you are scored
A hidden verifier inspects your submitted JSON output. It compares the values of a, b, Λ_min, and d_zero to independently derived reference numbers. The closer your computed quantities are to the expected values, the higher your score. Intermediate artifacts (delta_eta_raw.csv) may be checked for plausibility but the numerical score is determined solely from sinusoidal_grating_results.json.
