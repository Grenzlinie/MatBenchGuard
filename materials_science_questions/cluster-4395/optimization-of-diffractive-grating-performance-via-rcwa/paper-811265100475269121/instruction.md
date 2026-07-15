# Analytical Insertion Loss of Slab-Waveguide Bi-Directional Mode Multiplexer

## Problem background
Space‑division multiplexing increases optical fiber capacity by using multiple modes in a single few‑mode fiber. A simple and compact mode‑division multiplexer/demultiplexer can be realized with a bi‑directional coupler supported by a Bragg grating (BMDM). This device uses only two waveguides: a multimode input waveguide and a single‑mode output waveguide. The first‑ and second‑order modes of the input waveguide are coupled into opposite directions of the single‑mode waveguide, while the fundamental mode stays in the input waveguide. Understanding how much power is transferred to each output port — the insertion loss — is critical for designing such a device. In this task you will analytically compute the insertion losses for the first‑order and second‑order modes of a slab‑waveguide BMDM using a perturbative coupled‑mode model.

## Approach
The device is modeled with coupled‑mode equations that account for the periodic grating perturbation. Closed‑form expressions derived from this theory give the coupling coefficients (zeta, kappa, iota, varsigma, varpi) between the waveguide modes. The grating period Λ is chosen to satisfy the phase‑matching conditions that couple the first‑order mode co‑directionally (ℓ₁ = 0) and the second‑order mode contra‑directionally (ℓ₂ = 1). With the coupling coefficients and the period, the insertion losses IL1 and IL2 are evaluated at a coupling length L = 34 × Λ_min, where Λ_min is the globally minimum grating period. The design parameters are: core refractive index n₁ = 3.473, cladding n₂ = 1.444, operating wavelength λ₀ = 1550 nm, multimode waveguide width w = 600 nm, single‑mode width d = 250 nm, coupler gap r = 136.13 nm, grating teeth depth t = r. The effective indices required for the coupling coefficient formulas are: n_eff0 = 3.32, n_eff1 = 2.83, n_eff2 = 1.9, n_eff_single = 2.93. You will implement these formulas in code, compute the coefficients, determine Λ and Λ_min, and finally evaluate the insertion losses. The specific steps are detailed in the workflow below.

## Reproduction target
Compute the coupling coefficients (zeta, kappa, iota, varsigma, varpi) from the given geometry and effective indices. Determine the grating period Λ (in nm) that satisfies the phase‑matching conditions with ℓ₁ = 0, ℓ₂ = 1, and find the global minimum period Λ_min. Then, using a coupling length L = 34 × Λ_min and assuming perfect phase matching (Δβ = 0), calculate the insertion loss IL1 for the first‑order mode (co‑directional) and IL2 for the second‑order mode (contra‑directional), both in dB. Write the grating period Λ to `/app/outputs/grating_period.txt` (a single floating‑point number with at least two decimal places) and the insertion losses to `/app/outputs/insertion_losses.csv` (header: `IL1_dB,IL2_dB`, one row with the two values).

## Assets

- Python 3 with NumPy: numpy

## Workflow steps

### Step 1: Compute coupling coefficients
- Role: process
- Action: Using the given geometry, material indices, effective indices, and wavelength, compute all coupling coefficients (zeta, kappa, iota, varsigma, varpi) from the analytical closed-form expressions derived in the paper. Save the coefficients as an intermediate JSON file for subsequent steps.
- Evidence: `/app/outputs/coefficients.json`

### Step 2: Compute grating period
- Role: scored (load-bearing)
- Action: Compute the grating period Lambda that satisfies the phase-matching conditions for the BMDM design, using the coupling coefficients and the design parameters (ell1=0, ell2=1). Additionally compute the global minimum period Lambda_min. Write the value of Lambda (in nm) to the output file.
- Output file: `/app/outputs/grating_period.txt`
- Format: txt
- Contract: A single floating-point number representing Lambda in nanometers, with at least two decimal places.
- Scoring: scored by hidden verifier

### Step 3: Compute insertion losses
- Role: scored (load-bearing)
- Action: Using the coupling coefficients and a coupling length L = 34 * Lambda_min, compute the insertion losses IL1 (for first-order mode, codirectional) and IL2 (for second-order mode, contradirectional) under phase-matching (Delta beta = 0). Write the two values (in dB) to the output CSV file.
- Output file: `/app/outputs/insertion_losses.csv`
- Format: csv
- Contract: CSV file with header: IL1_dB,IL2_dB. Each row contains two floating-point numbers with at least two decimal places.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/grating_period.txt`
- `/app/outputs/insertion_losses.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### grating_period.txt
- path: `/app/outputs/grating_period.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: The grating period that satisfies the phase-matching conditions. Checker recomputes from the same analytical formulas and compares within a hidden tolerance.
- schema:
  - `type`: text
  - `description`: Single floating-point number in nm, at least two decimal places.

### insertion_losses.csv
- path: `/app/outputs/insertion_losses.csv`
- format: csv
- purpose: scored
- target_policy: exact_match
- description: Insertion losses (dB) for the first- and second-order modes. Checker recomputes from the same analytical formulas and compares within a hidden tolerance.
- schema:
  - `type`: table
  - `required_columns`: `IL1_dB`, `IL2_dB`
  - `units`:
    - `IL1_dB`: dB
    - `IL2_dB`: dB
  - `description`: One row containing two floating-point numbers.

Notes: Only the analytical slab-waveguide Example 1 with three TE modes is reproduced. The effective indices required for computing coupling coefficients are provided directly in the task instructions, so the agent does not need to solve the waveguide dispersion equation. FDTD simulations and TM-mode Example 2 are excluded.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "grating_period.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number in nm, at least two decimal places."
      },
      "description": "The grating period that satisfies the phase-matching conditions. Checker recomputes from the same analytical formulas and compares within a hidden tolerance."
    },
    {
      "file": "insertion_losses.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "IL1_dB",
          "IL2_dB"
        ],
        "units": {
          "IL1_dB": "dB",
          "IL2_dB": "dB"
        },
        "description": "One row containing two floating-point numbers."
      },
      "description": "Insertion losses (dB) for the first- and second-order modes. Checker recomputes from the same analytical formulas and compares within a hidden tolerance."
    }
  ],
  "notes": "Only the analytical slab-waveguide Example 1 with three TE modes is reproduced. The effective indices required for computing coupling coefficients are provided directly in the task instructions, so the agent does not need to solve the waveguide dispersion equation. FDTD simulations and TM-mode Example 2 are excluded."
}
```

## How you are scored
A hidden verifier independently recomputes the same analytical quantities (coupling coefficients, grating period, insertion losses) from the same public parameters and formulas. Your output artifacts are compared to the verifier's recomputed values within pre‑determined tolerances. The grating period (step 2) and the insertion losses (step 3) each carry a share of the final reward; the weight of each stage is fixed but not disclosed. You must produce the files exactly as specified in the output contract — merely copying a reported number from an external source will not match the verifier's independent recomputation and will receive a low score. The tolerances are chosen so that a correct implementation of the required formulas will pass, while wild guesses or hard‑coded values will not.
