# Electronic Frequency Tuning Range of Three-Stage Grating Clinotron

## Problem background
Backward-wave oscillators (BWOs) are attractive compact sources of terahertz radiation for applications such as spectroscopy, imaging, and plasma diagnostics. A key challenge is extending the electronic frequency tuning range—the range of operating frequencies achievable by varying the accelerating voltage—without raising the start current or sacrificing output power. The use of multistage gratings, in which the groove depth varies periodically along the structure, allows coupling between volume and surface waves, potentially broadening the tuning bandwidth. This reproduction focuses on two designs of a three-stage grating clinotron operating in the surface mode of the second pass band: a 94 GHz design and a preliminary 220 GHz design. The task is to compute the electronic frequency tuning range (as a percentage of the central frequency) for each design using a mode-matching analysis of the shielded multistage grating.

## Approach
The central analysis uses the mode-matching technique for the shielded three-stage grating shown in Fig. 1. The period of the grating along the y-axis is L = 3·l, where l is the length of each stage (the distance between the centres of neighbouring slots). Every slot has the same width d; in the long-wavelength approximation (d ≪ λ) only the zeroth-order waveguide mode is significant inside each slot. The slot depths for the three stages are h₁ = h, h₂ = h, h₃ = h₃, with h₃/h₁ = 1.3. The plate is placed at a distance D above the grating surface. The structure is lossless (ε = 1 in the slots).

The total magnetic field Hₓ above the grating is expanded in Bloch–Floquet spatial harmonics:
Hₓ⁺(y,z) = ∑ᵣ Aᵣ exp[i (k_y + 2πr/L) y] exp(i qᵣ z),
where k_y is the Bloch wavenumber, qᵣ = √(k² − (k_y + 2πr/L)²) with k = 2πf/c, and the sum over r runs over all integers.

Inside the p‑th slot (p = 1, 2, 3) the field is approximated by the TEM mode:
Hₓ⁻(y,z) = Dₚ cos(k (z + hₚ)),   z ∈ [−hₚ, 0].

Matching the tangential fields (Hₓ and the y‑component of E) at the aperture z = 0 and imposing the boundary condition Hₓ = 0 at the top plate z = D yields a homogeneous linear system for the vector D = (D₁, D₂, D₃). Its elements are governed by the matrix equation

∑_{p₀=1}^{3} D_{p₀} [ δ_{p,p₀} cos(k hₚ)  +  \frac{k d}{L} sin(k h_{p₀})  Σ_{r=−∞}^{∞} \left( \frac{\sin(k_r d/2)}{k_r d/2} \right)^2 \frac{e^{i k_r (p−p₀) l}}{\tan(qᵣ D) qᵣ} ] = 0,

where k_r = k_y + 2πr/L, and δ_{p,p₀} is the Kronecker delta.

The dispersion relation of the cold structure (without electron beam) is given by det M(k_y, f) = 0. The sum over r is truncated to ±N with N ≈ 25–50 to obtain numerical convergence. The second pass band is the frequency band where phase advance per period L is between 2π and 4π, and the surface‑mode branch is the locus of points where the phase velocity v_ph = 2πf/k_y is negative (backward wave).

Once the surface‑mode dispersion curve f(k_y) has been computed, the synchronous interaction with a sheet electron beam of velocity v_e is described by the beam line
f = v_e · k_y/(2π).
For a given v_e, the operating frequency f_op is the intersection of the beam line with the surface‑mode branch. Sweeping v_e over the range where an intersection exists gives the minimum and maximum f_op. The electronic frequency tuning range is then computed as
Δf_rel = \frac{f_{max} − f_{min}}{(f_{max}+f_{min})/2} × 100 %.

## Reproduction target
Implement the mode-matching solver for a shielded three-stage grating. Using the two geometries—94 GHz: h=0.6 mm, h3=0.78 mm, D=0.8 mm, l=0.28 mm; 220 GHz: h=0.252 mm, l=0.135 mm, D=0.5 mm, h3/h=1.3—solve the dispersion equation for the second pass band and extract the surface-mode branch. For the 94 GHz design, sweep the beam velocity across the approximate range 0.094c to 0.113c (the region of surface-mode synchronism); for the 220 GHz design, determine the corresponding beam velocity range from the computed dispersion. At each beam velocity, locate the intersection of the beam line with the surface-mode dispersion curve to obtain the operating frequency. Compute the electronic frequency tuning range as a percentage for each design: (f_max - f_min) / f_center × 100%. Save the two percentages in a JSON file `/app/outputs/tuning_ranges.json` with keys `tuning_range_94GHz` and `tuning_range_220GHz`.

## Assets

- Python 3: python3
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Define grating geometries
- Role: process
- Action: Set up the geometrical parameters for the two grating designs: 94 GHz (h=0.6 mm, h3=0.78 mm, D=0.8 mm, l=0.28 mm) and 220 GHz (h=0.252 mm, l=0.135 mm, D=0.5 mm, h3/h=1.3).
- Evidence: none

### Step 2: Compute dispersion curves and identify surface mode
- Role: process
- Action: Implement the mode-matching technique for a shielded three-stage grating. Solve the dispersion equation (no beam term) to obtain dispersion curves for the 2nd pass band for both designs. Identify the surface mode branch (vph < 0) and determine the beam velocity range for surface-mode synchronism.
- Evidence: none

### Step 3: Compute electronic frequency tuning ranges
- Role: scored (load-bearing)
- Action: For the 94 GHz design, vary the beam velocity over the determined surface-mode range (approximately 0.094c to 0.113c) and find the operating frequencies at fundamental harmonic synchronism (intersection of beam line with surface-mode dispersion curve). Compute the tuning range as (f_max - f_min) / f_center × 100 %. For the 220 GHz design, similarly determine the beam velocity range from the dispersion condition and compute the tuning range percentage. Write both percentages to the output JSON file.
- Output file: `/app/outputs/tuning_ranges.json`
- Format: json
- Contract: {"tuning_range_94GHz": <float>, "tuning_range_220GHz": <float>}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/tuning_ranges.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### tuning_ranges.json
- path: `/app/outputs/tuning_ranges.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Electronic frequency tuning ranges (in percent) for the 94 GHz and 220 GHz three-stage grating clinotron designs.
- schema:
  - `type`: object
  - `required`: `tuning_range_94GHz`, `tuning_range_220GHz`
  - `items`: object
  - `units`:
    - `tuning_range_94GHz`: percent
    - `tuning_range_220GHz`: percent

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "tuning_ranges.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": [
          "tuning_range_94GHz",
          "tuning_range_220GHz"
        ],
        "items": {},
        "units": {
          "tuning_range_94GHz": "percent",
          "tuning_range_220GHz": "percent"
        }
      },
      "description": "Electronic frequency tuning ranges (in percent) for the 94 GHz and 220 GHz three-stage grating clinotron designs."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier inspects `/app/outputs/tuning_ranges.json`. It first confirms the file exists, is valid JSON, and contains the required numeric keys. It then compares each submitted tuning range percentage to the expected values derived from the paper's reported analysis, using a predefined tolerance. The final reward is determined as follows: full reward (1.0) if both percentages are within the tolerance of the expected values; half reward (0.5) if exactly one is within tolerance; zero reward (0.0) if neither is. The expected reference values and the tolerance are not disclosed in advance. The task is to faithfully implement the mode-matching calculation—not to guess or hard-code any particular number.
