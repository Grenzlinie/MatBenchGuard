# Coupled vibration resonance and effective coupling coefficients for finite-size piezoceramic cylinders

## Problem background
Piezoelectric cylindrical elements with electrodes on their end surfaces and polarization through the thickness exhibit coupled axial and radial vibrations. For intermediate aspect ratios (height-to-diameter ratio h/2a in the range 0.5–1.5), the first radial mode dominates the radial response, and the element can be analyzed as a two‑degree‑of‑freedom coupled system using coupled vibration theory. This task computes the resulting normalized resonance frequencies and effective electromechanical coupling coefficients for a PZT‑4 ceramic cylinder as a function of the aspect ratio in this region.

## Approach
Treat the finite‑size cylinder as a two‑degree‑of‑freedom system arising from coupling between an axial partial system (a thickness‑vibrating tall rod) and a radial partial system (a radially vibrating infinitely long cylinder). The assumed displacement distributions are a half‑wave sinusoid along the axis for the axial mode and the first Bessel function of the first kind for the radial mode. The potential, kinetic, and electromechanical energies are integrated over the cylinder volume, yielding equivalent rigidities, masses, and electromechanical turns ratios for the two partial systems, as well as a mechanical coupling coefficient (here the inertial coupling is zero). From these, the partial resonance frequencies f_a (radial) and f_h (axial) and their ratio β ∝ h/2a are obtained. The free‑vibration equations lead to a quadratic frequency equation in the normalized squared frequency Ω = (f/f_a)² whose two branches Ω₁(β) and Ω₂(β) describe the resonance frequencies. For each branch, the mode shape (ratio of radial to axial displacement) is found, and the effective coupling coefficient is computed from the energy ratio using the equivalent parameters. The effective coupling coefficients are then normalized to the corresponding tall‑rod limit for PZT‑4. The computation is carried out for a dense grid of aspect ratios h/2a ∈ [0.5, 1.5].

## Reproduction target
Implement the analytical coupled vibration model for a finite‑size cylindrical piezoelement made of PZT‑4. Using the published material constants for PZT‑4 (elastic stiffnesses, piezoelectric constants, dielectric constant, density, and the rod coupling coefficient), compute the two dimensionless resonance frequency branches Ω₁(β) and Ω₂(β) and the corresponding normalized effective electromechanical coupling coefficients (denoted keff_1_norm, keff_2_norm) as functions of the aspect ratio h/2a. Sample the aspect ratio densely (e.g., step 0.01) over the interval [0.5, 1.5] and write the results to a CSV file named coupled_vibration_results.csv with columns: aspect_ratio, omega_1, omega_2, keff_1_norm, keff_2_norm.

## Assets

- PZT-4 material constants

## Workflow steps

### Step 1: Compute analytical resonance frequencies and effective coupling coefficients
- Role: scored (load-bearing)
- Action: Implement the coupled vibration model for a finite-size cylindrical piezoelement made of PZT-4. Using the material constants specified in the resources, compute the partial resonance frequencies, coupling coefficient, and frequency ratio. Solve the frequency equation to obtain the two dimensionless resonance frequency branches Ω₁(β) and Ω₂(β). For each branch, compute the effective coupling coefficients and normalize them to the tall-rod limit. Sample the aspect ratio h/2a densely in the range [0.5, 1.5] and output a CSV.
- Output file: `/app/outputs/coupled_vibration_results.csv`
- Format: csv
- Contract: Header: aspect_ratio,omega_1,omega_2,keff_1_norm,keff_2_norm. All columns are floating‑point numbers. Rows correspond to a regular sampling of h/2a in [0.5, 1.5].
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/coupled_vibration_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### coupled_vibration_results.csv
- path: `/app/outputs/coupled_vibration_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: The computed normalized resonance frequencies and effective coupling coefficients for the two coupled vibration branches as a function of the aspect ratio h/2a.
- schema:
  - `type`: table
  - `required_columns`: `aspect_ratio`, `omega_1`, `omega_2`, `keff_1_norm`, `keff_2_norm`
  - `units`: object

Notes: The hidden checker independently recomputes the analytical curves using the same PZT-4 material constants and the same model equations, then compares the agent's submitted values within a tolerance field by field.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "coupled_vibration_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "aspect_ratio",
          "omega_1",
          "omega_2",
          "keff_1_norm",
          "keff_2_norm"
        ],
        "units": {}
      },
      "description": "The computed normalized resonance frequencies and effective coupling coefficients for the two coupled vibration branches as a function of the aspect ratio h/2a."
    }
  ],
  "notes": "The hidden checker independently recomputes the analytical curves using the same PZT-4 material constants and the same model equations, then compares the agent's submitted values within a tolerance field by field."
}
```

## How you are scored
A hidden verifier independently recomputes the same analytical model using the same PZT‑4 material constants and the same set of aspect ratios. It compares your submitted CSV values against its own recomputed values field by field, applying a relative tolerance for each numeric entry. The two frequency branches and the two coupling‑coefficient branches are weighted equally; a field that exceeds the tolerance reduces the reward proportionally. The final reward is the weighted average over all scored artifacts.
