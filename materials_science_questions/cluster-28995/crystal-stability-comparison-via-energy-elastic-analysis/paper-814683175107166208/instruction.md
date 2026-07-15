# Electron localization distance and square-to-triangular lattice phase boundary on liquid helium

## Problem background
Electrons on the surface of liquid helium form a two-dimensional system that, under sufficient density and low temperature, crystallizes into a Wigner solid. The ground-state lattice can be square or triangular depending on the external clamping electric field E and the electron areal density ρ. Determining the spatial extent (localization distance) of an electron around its lattice site and the critical line in the E–ρ plane that separates the two lattice structures are fundamental questions for this system. The present work develops a mean-field free energy functional that captures both the direct and mediated electron-electron interactions and provides approximate analytic results for these quantities.

## Approach
The theory treats the electrons as a 2D Fermi gas arranged on a Bravais lattice and describes their distribution around each lattice site by a Gaussian profile of width s (the localization distance). The total free energy is written as the sum of the mean-field interaction energy (Coulomb repulsion, polarization of the substrate and helium, and capillary attraction caused by surface deformation) and an entropy contribution. The free energy is minimized with respect to s for both the square and triangular lattices. Evaluating the resulting expressions at low temperature yields closed-form approximate formulas for the localization distance at a given clamping field and for the difference in free energy between the two lattice geometries. The phase boundary is obtained by setting this difference to zero, which gives the critical combination A = E²/√ρ. The task implements the final analytic expressions for these two quantities using the standard physical constants and the surface tension of liquid helium.

## Reproduction target
Compute two scalar quantities using the analytic formulas derived from the free energy functional:
1. The localization distance s (in cm) of an electron on liquid helium at T = 0 for a given clamping electric field E (the field will be specified in the instruction, e.g., E = 3000 V/cm converted to statvolt/cm).
2. The critical constant A = E²/√ρ (in dyn, cgs) at which the free energies of the square and triangular Wigner lattices are equal.
Both computations must use the electron mass m_e, elementary charge e, reduced Planck constant ħ, and the surface tension of liquid helium σ = 0.37 dyn/cm. The outputs are single floating-point numbers written to plain text files.

## Assets

- Standard physical constants (m_e, e, ħ, σ)
- NumPy: numpy

## Workflow steps

### Step 1: Compute localization distance s
- Role: scored
- Action: Compute the T=0 localization distance s (in cm) of an electron on liquid helium under a clamping electric field E = 3000 V/cm (convert to statvolt/cm; 1 statvolt/cm = 299.792458 V/cm). Use the analytic expression derived from the mean-field free energy: s = sqrt(2πσħ²/(m e² E²)), with σ = 0.37 dyn/cm, m = electron mass, e = elementary charge, ħ = reduced Planck constant. Output the numeric value.
- Output file: `/app/outputs/localization_distance_s.txt`
- Format: txt
- Contract: A single floating-point number in centimeters.
- Scoring: scored by hidden verifier

### Step 2: Compute phase boundary constant A
- Role: scored
- Action: Evaluate the critical constant A = E²/√ρ at which the free energies of square and triangular Wigner lattices become equal. The analytic expression derived from the free-energy difference is A = 4(1 − √(3/4)) π² σ / ln(2 / ∜12), using σ = 0.37 dyn/cm. Output the result in cgs units of dyn.
- Output file: `/app/outputs/phase_boundary_A.txt`
- Format: txt
- Contract: A single floating-point number in dyn.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/localization_distance_s.txt`
- `/app/outputs/phase_boundary_A.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### localization_distance_s.txt
- path: `/app/outputs/localization_distance_s.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Localization distance of an electron on liquid helium at T=0 for a given clamping field.
- schema:
  - `type`: text
  - `description`: Single floating-point number representing the localization distance in centimeters.
  - `unit`: cm

### phase_boundary_A.txt
- path: `/app/outputs/phase_boundary_A.txt`
- format: txt
- purpose: scored
- target_policy: exact_match
- description: Critical constant A = E²/√ρ for the square-to-triangular lattice phase transition.
- schema:
  - `type`: text
  - `description`: Single floating-point number representing the critical constant A in dyn (cgs).
  - `unit`: dyn

Notes: Both outputs are deterministic scalar numbers obtained from analytic closed-form expressions. The checker will recompute them using the same standard physical constants and compare with relative tolerances (1% for A, 5% for s) to allow for floating-point differences. The clamping field E is now explicitly set to 3000 V/cm and must be converted to cgs units.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "localization_distance_s.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing the localization distance in centimeters.",
        "unit": "cm"
      },
      "description": "Localization distance of an electron on liquid helium at T=0 for a given clamping field."
    },
    {
      "file": "phase_boundary_A.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "text",
        "description": "Single floating-point number representing the critical constant A in dyn (cgs).",
        "unit": "dyn"
      },
      "description": "Critical constant A = E²/√ρ for the square-to-triangular lattice phase transition."
    }
  ],
  "notes": "Both outputs are deterministic scalar numbers obtained from analytic closed-form expressions. The checker will recompute them using the same standard physical constants and compare with relative tolerances (1% for A, 5% for s) to allow for floating-point differences. The clamping field E is now explicitly set to 3000 V/cm and must be converted to cgs units."
}
```

## How you are scored
Each workflow stage produces a scored artifact. A hidden verifier independently recomputes the same physical quantity from the same physical constants and compares your output to a gold reference. The final reward is the weighted sum of the individual stage scores. Simply reporting the paper's published numbers without performing the required computation will not satisfy the verifier, because the verifier can detect that the output is inconsistent with an honest re-evaluation of the analytic expressions.
