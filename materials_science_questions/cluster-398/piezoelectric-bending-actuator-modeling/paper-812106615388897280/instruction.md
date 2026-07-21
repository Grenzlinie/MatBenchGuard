# Dynamic Contact Problem of a Piezoelectric Strip on an Elastic Half-Space

## Problem background
The task investigates the dynamic contact problem of a thin infinite piezoelectric actuator strip bonded to an elastic half-space. The actuator undergoes harmonic oscillation due to an applied electric load, exciting surface and bulk acoustic waves in the elastic medium. The goal is to predict the stress-strain state inside the actuator and the displacement fields in the half-space. As the actuator oscillates, the contact area transfers normal and shear loads to the elastic substrate, and the resulting wave patterns depend on the oscillation frequency, geometric parameters, and material properties. Understanding this coupling is important for designing piezoelectric transducers and sensors that rely on acoustic wave generation. The challenge is to compute the modal distribution of the contact stresses and the resulting acoustic fields from first principles, without fitting to experimental data.

## Approach
The solution strategy combines analytical modelling of the thin piezoelectric strip with a classical elastodynamic treatment of the half-space. Under the assumptions that the strip is thin (its thickness much less than its width) and that in-plane stress dominates through-thickness stress, the strip's electroelastic equations are reduced to a one-dimensional model. The applied electric field is extended periodically and expanded in a Fourier cosine series. For the elastic half-space, the equilibrium equations in terms of displacements are solved using Fourier transforms and complex analysis. Auxiliary problems with unit normal and shear surface loads are solved via contour integration; the resulting formulas involve Rayleigh-pole residues and branch-cut integrals. The total displacement in the contact region is expressed as a sum of these auxiliary solutions multiplied by unknown modal amplitudes. Continuity of displacements and stresses at the interface yields a 2N×2N linear system (with N odd modes) that determines the modal amplitudes. Once the amplitudes are known, the stress and displacement fields can be computed at any point, both in the contact area and in the surrounding elastic body. The workflow is fully numerical and requires implementing the Fourier series, the contour integration for the half-space, solving the linear system, and evaluating the derived field quantities.

## Reproduction target
Your task is to reproduce the key results for the specific example described in the original study: an elastic half-space made of steel, a piezoelectric strip made of PZT-5 ceramics with width 2l = 0.02 m and thickness t = 0.001 m, oscillating at an angular frequency corresponding to 78 kHz. You must compute:
1. The modal amplitudes A_n (normal loading) and B_n (shear loading) for the first four odd modes n=1,3,5,7, and save them in `step_01_modal_coefficients.json`.
2. From the complete solution, extract the following derived quantities:
   - The ratio of the amplitude of the in-plane stress σ11 to the through-thickness stress σ33 at the centre of the contact area (x1=0, x3=0), to verify that the thin-strip stress hypothesis is satisfied.
   - A boolean flag indicating whether shear loading is dominant. Define shear dominance as max(|B_n|) / max(|A_n|) > 5.
   - The frequency (in kHz) at which the amplitude of the surface normal displacement |u3| at a point 2l away from the centre (x1=2l, x3=0) reaches its peak, by sweeping around 78 kHz.
   - The depth (in mm) at which the surface wave displacement amplitude at x1=2l decays to 1/e of its value on the surface.
Save these four metrics in `step_02_verification.json`.
All computations should use the standard publicly available material properties for steel and PZT-5. The electric load scaling factor V is arbitrary and cancels out of normalized quantities; you may set it to any convenient value.

## Assets

- Steel elastic material properties (E, ν, ρ)
- PZT-5 piezoelectric ceramic properties
- Python with numpy, scipy: numpy, scipy

## Workflow steps

### Step 1: Electric load Fourier expansion
- Role: process
- Action: Extend the electric field E3 outside the contact region according to the specified extension function (with geometry parameters l=0.01 m, t=0.001 m, and a chosen extension period L=4l; the scaling factor V cancels) and compute the Fourier cosine series coefficients φ_n for odd n up to N=7.
- Evidence: `/app/outputs/electric_fourier_coefficients.json`

### Step 2: Half-space modal displacement coefficients
- Role: process
- Action: For each odd mode n=1,3,5,7, compute the elastodynamic half-space solution for unit normal and shear surface loads at the specified frequency 78 kHz. Evaluate the Fourier integrals using contour integration (Rayleigh-pole residues and branch-cut integrals) for the contact region and obtain the displacement modal coefficients p_jn, q_jn, y_jn, z_jn.
- Evidence: `/app/outputs/halfspace_coefficients.json`

### Step 3: Solve for modal amplitudes A_n, B_n
- Role: scored (load-bearing)
- Action: Form the 2N×2N linear system from the electric coefficients and half-space coefficients, enforce the contact conditions, solve for unknown modal amplitudes A_n and B_n for n=1,3,5,7. Output the results as JSON.
- Output file: `/app/outputs/step_01_modal_coefficients.json`
- Format: json
- Contract: {"A": [float], "B": [float]} each array length 4 for n=1,3,5,7.
- Scoring: scored by hidden verifier

### Step 4: Compute verification metrics
- Role: scored
- Action: Using the solved modal amplitudes and half-space solutions, compute normalized stresses and displacements in the contact area and on the surface. Evaluate the stress ratio |σ11|/|σ33| at (x1=0, x3=0); check shear dominance by comparing max(|B_n|) and max(|A_n|); sweep angular frequency around 78 kHz to locate the peak of |u3| on the surface at x1=2l; find the depth x3 where the surface wave displacement amplitude at x1=2l drops to 1/e of its surface value. Report these four metrics.
- Output file: `/app/outputs/step_02_verification.json`
- Format: json
- Contract: {"stress_ratio_contact": float, "shear_dominant": bool, "peak_frequency_khz": float, "attenuation_depth_mm": float}
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_modal_coefficients.json`
- `/app/outputs/step_02_verification.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_modal_coefficients.json
- path: `/app/outputs/step_01_modal_coefficients.json`
- format: json
- purpose: scored
- target_policy: exact_match
- description: Modal amplitude constants A_n (normal loading) and B_n (shear loading) for the first four odd modes at 78 kHz.
- schema:
  - `type`: object
  - `required`:
    - `A`: array of 4 floats (n=1,3,5,7 order)
    - `B`: array of 4 floats (n=1,3,5,7 order)

### step_02_verification.json
- path: `/app/outputs/step_02_verification.json`
- format: json
- purpose: scored
- target_policy: structural_audit
- description: Verification metrics: stress ratio in contact area, shear dominance flag, frequency of peak surface displacement, and 1/e attenuation depth.
- schema:
  - `type`: object
  - `required`:
    - `stress_ratio_contact`: float (|σ11|/|σ33| at x1=0, x3=0)
    - `shear_dominant`: boolean
    - `peak_frequency_khz`: float
    - `attenuation_depth_mm`: float

Notes: The agent must implement the entire analytical/numerical pipeline: Fourier expansion, half-space elastodynamic solutions via Fourier integrals and contour integration, assembly and solution of the 2N×2N linear system, and post-processing of fields. All material properties (steel, PZT-5) are publicly available from standard references. The scored modal amplitudes will be checked against the paper's reported values with order-of-magnitude tolerance; the verification metrics must satisfy the stated structural thresholds.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_modal_coefficients.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "exact_match",
      "schema": {
        "type": "object",
        "required": {
          "A": "array of 4 floats (n=1,3,5,7 order)",
          "B": "array of 4 floats (n=1,3,5,7 order)"
        }
      },
      "description": "Modal amplitude constants A_n (normal loading) and B_n (shear loading) for the first four odd modes at 78 kHz."
    },
    {
      "file": "step_02_verification.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "object",
        "required": {
          "stress_ratio_contact": "float (|σ11|/|σ33| at x1=0, x3=0)",
          "shear_dominant": "boolean",
          "peak_frequency_khz": "float",
          "attenuation_depth_mm": "float"
        }
      },
      "description": "Verification metrics: stress ratio in contact area, shear dominance flag, frequency of peak surface displacement, and 1/e attenuation depth."
    }
  ],
  "notes": "The agent must implement the entire analytical/numerical pipeline: Fourier expansion, half-space elastodynamic solutions via Fourier integrals and contour integration, assembly and solution of the 2N×2N linear system, and post-processing of fields. All material properties (steel, PZT-5) are publicly available from standard references. The scored modal amplitudes will be checked against the paper's reported values with order-of-magnitude tolerance; the verification metrics must satisfy the stated structural thresholds."
}
```

## How you are scored
Your submission will be evaluated by a hidden verifier that checks the two output JSON files. The verifier compares your reported modal amplitudes A_n, B_n against hidden reference values (order-of-magnitude agreement and correct signs) and reads your verification metrics to ensure they satisfy certain structural thresholds (e.g., the stress ratio must exceed a minimum, the shear dominance flag must be true, the peak frequency must lie within a reasonable interval, and the attenuation depth must be physically plausible). The scoring is weighted across the two output artifacts, with the modal amplitudes carrying the largest share. Meeting or exceeding the thresholds earns full credit; a solution that fails to produce the correct structure or wildly different numbers receives a lower score. The verifier does not re-run your code; it trusts the reported values but performs consistency checks.
