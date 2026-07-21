# Electromechanical Conversion Efficiency of Biased Semiconductor Transducers

## Problem background
It is possible to convert electrical RF power to acoustic power using a thin‑film piezoelectric semiconductor transducer deposited onto a delay rod. When the semiconductor has drifting carriers, especially at supersonic velocities, acoustic amplification can occur, which may alter the electromechanical conversion efficiency G. Understanding how the efficiency depends on carrier drift and mechanical loading conditions is important for the design of high‑frequency transducers.

## Approach
The transducer is modeled as a one‑dimensional piezoelectric semiconductor. From the acoustoelectric plane‑wave equations, a dispersion relation is obtained that determines the allowed wave vectors in the medium. In the three‑wave approximation carrier diffusion is neglected, reducing the dispersion to a cubic equation. At the half‑wavelength resonance frequency, this cubic is solved to obtain three complex wave vectors. The mechanical and electrical boundary conditions (stress‑free face, loaded interface with the delay rod, and zero plane‑wave component of electric displacement at the electrodes) yield a 3×3 linear system for the amplitude ratios of the three waves. Substituting the wave vectors and amplitude ratios into the efficiency expression gives the electromechanical conversion efficiency G.

## Reproduction target
Compute the electromechanical conversion efficiency G of a 2‑μm ZnO film at its half‑wavelength resonance frequency (approximately 1.5 GHz) for two carrier drift conditions: v_D = 0 and v_D = 1.5 v_s. Use the material parameters v_s = 6000 m/s, e²/(εc) = 0.16, relative permittivity ε_r = 8.5, resistivity ρ = 1.5 Ω·m, and delay‑rod mechanical impedance Z_R = 1.5×10⁵ kg·s·m⁻². Perform the computation within the three‑wave approximation (diffusion neglected) and write the two resulting efficiency values as G_zero and G_supersonic into a JSON file.

## Assets

- numpy: numpy

## Workflow steps

### Step 1: Compute electromechanical conversion efficiency
- Role: scored (load-bearing)
- Action: Develop the three‑wave acoustoelectric model for a piezoelectric semiconductor transducer. For a 2‑μm ZnO film with given material parameters (v_s = 6000 m/s, e²/(εc) = 0.16, relative permittivity ε_r = 8.5, resistivity ρ = 1.5 Ω·m) and delay‑rod mechanical impedance Z_R = 1.5×10⁵ kg·s·m⁻², compute the electromechanical conversion efficiency G at the half‑wavelength resonance frequency (~1.5 GHz) for two carrier drift conditions: v_D = 0 and v_D = 1.5 v_s. To do this, (1) set up and solve the cubic dispersion equation (diffusion neglected) to obtain the complex wave vectors k_j; (2) formulate and solve the 3×3 linear system from the mechanical and electrical boundary conditions to find the amplitude ratios λ_j; (3) evaluate the closed-form efficiency expression using these values. Write the two resulting efficiency values into a JSON file as G_zero and G_supersonic.
- Output file: `/app/outputs/step_01_efficiency.json`
- Format: json
- Contract: A JSON object with keys 'G_zero' (float) and 'G_supersonic' (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_efficiency.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_efficiency.json
- path: `/app/outputs/step_01_efficiency.json`
- format: json
- purpose: scored
- target_policy: threshold_or_better
- description: The two computed efficiency values. The hidden checker compares each value to the corresponding paper-derived threshold and awards full credit if the agent's value meets or exceeds the threshold, using threshold_or_better policy to avoid penalising results better than the paper.
- schema:
  - `type`: object
  - `required`: `G_zero`, `G_supersonic`
  - `items`:
    - `G_zero`: float
    - `G_supersonic`: float

Notes: The threshold_or_better policy ensures that results at least as good as the paper's reference values are rewarded; better‑than‑paper results are not penalised. The hidden checker compares each value to the corresponding paper‑derived threshold and awards full credit if the agent's value meets or exceeds the threshold.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_efficiency.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "object",
        "required": [
          "G_zero",
          "G_supersonic"
        ],
        "items": {
          "G_zero": "float",
          "G_supersonic": "float"
        }
      },
      "description": "The two computed efficiency values. The hidden checker compares each value to the corresponding paper-derived threshold and awards full credit if the agent's value meets or exceeds the threshold, using threshold_or_better policy to avoid penalising results better than the paper."
    }
  ],
  "notes": "The threshold_or_better policy ensures that results at least as good as the paper's reference values are rewarded; better‑than‑paper results are not penalised. The hidden checker compares each value to the corresponding paper‑derived threshold and awards full credit if the agent's value meets or exceeds the threshold."
}
```

## How you are scored
Your submitted efficiency values will be compared to independently computed reference values by a hidden verifier. The verifier checks whether your implementation correctly solved the three‑wave model and produced accurate numbers. The reward is based solely on the correctness of the two efficiency values; simply reporting approximate numbers without performing the full computation will not succeed.
