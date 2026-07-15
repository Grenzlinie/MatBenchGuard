# Analytic THz Emission Energy from InAs Photo-Dember Effect

## Problem background
When a femtosecond laser pulse hits an InAs surface, photoexcited electrons and holes diffuse at different rates, creating a transient photocurrent that radiates terahertz (THz) electromagnetic waves. An analytic hydrodynamic model can describe this photo‑Dember effect, yielding expressions for the local transient current and the total radiated THz energy as functions of material parameters and excitation conditions. This task asks you to implement that analytic model and compute the THz emission energy for a range of photon energies and optical fluences.

## Approach
You will implement the hydrodynamic model for the photo‑Dember effect in n‑type InAs (doping 2×10^16 cm⁻³). The model considers a simplified geometry with instantaneous (delta‑function) optical excitation. It accounts for the non‑parabolic conduction band of InAs, the relevant effective masses, dielectric constants, and an energy‑dependent momentum relaxation rate. Using the provided InAs band‑structure parameters, material parameters, absorption coefficients, and relaxation rate, you will evaluate the closed‑form expression for the time‑integrated THz energy (the full expression that reduces to different limits at low vs. high excitation density). For each combination of photon energy and fluence, you will first convert the fluence to a surface excitation density via n_exc = α × I_p, where α is the absorption coefficient at that photon energy. You will then substitute this density into the THz energy formula and output the results.

## Reproduction target
Produce a CSV file named results.csv containing the computed THz energy W_THz (in joules) for each (photon energy, optical fluence) pair. The photon energy sweeps from 0.5 to 2.0 eV in steps of 0.1 eV; the fluences are 1×10^13 cm⁻² and 1×10^14 cm⁻². The file must have a header row 'photon_energy_eV, fluence_cm-2, W_THz_J' and each subsequent row lists the three comma‑separated floats.

## Assets

- InAs band structure parameters
- InAs material parameters
- InAs absorption coefficients vs photon energy
- Momentum relaxation rate gamma for photoelectrons
- Analytic formulas for photo-Dember effect

## Workflow steps

### Step 1: Compute THz energy from analytic hydrodynamic model
- Role: scored
- Action: Using the analytic hydrodynamic model for the photo‑Dember effect, compute the total radiated THz energy W_THz for n‑type InAs (doping 2×10^16 cm⁻³) assuming an instantaneous optical pulse. Use the InAs parameters (effective masses, nonparabolicities, dielectric constants, absorption coefficient table, momentum relaxation rate) provided in the task instructions. For each combination of photon energy from 0.5 to 2.0 eV in steps of 0.1 eV and optical fluences of 1×10^13 cm⁻² and 1×10^14 cm⁻², convert fluence to surface excitation density n_exc via n_exc = α·I_p (with α the absorption coefficient at that photon energy) and compute W_THz using the full high‑excitation expression or its applicable limit. Output a CSV file with columns: photon_energy_eV, fluence_cm-2, W_THz_J.
- Output file: `/app/outputs/results.csv`
- Format: csv
- Contract: CSV with header: photon_energy_eV, fluence_cm-2, W_THz_J. Each row contains comma-separated float values.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### results.csv
- path: `/app/outputs/results.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: THz emission energy computed from the analytic hydrodynamic model for a grid of photon energies and optical fluences.
- schema:
  - `type`: table
  - `required_columns`: `photon_energy_eV`, `fluence_cm-2`, `W_THz_J`
  - `description`: Each row corresponds to a single (photon energy, fluence) pair. photon_energy_eV is a float in eV; fluence_cm-2 is a float in cm⁻²; W_THz_J is a float in J.

Notes: The checker recomputes W_THz from the same formulas and parameters and compares values with a relative tolerance. Additionally, the checker performs power‑law scaling checks on the low‑ and high‑fluence data.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "photon_energy_eV",
          "fluence_cm-2",
          "W_THz_J"
        ],
        "description": "Each row corresponds to a single (photon energy, fluence) pair. photon_energy_eV is a float in eV; fluence_cm-2 is a float in cm⁻²; W_THz_J is a float in J."
      },
      "description": "THz emission energy computed from the analytic hydrodynamic model for a grid of photon energies and optical fluences."
    }
  ],
  "notes": "The checker recomputes W_THz from the same formulas and parameters and compares values with a relative tolerance. Additionally, the checker performs power‑law scaling checks on the low‑ and high‑fluence data."
}
```

## How you are scored
A hidden verifier independently recomputes W_THz using the same analytic formulas and parameters. It compares your results against its own recomputation with a relative tolerance. In addition, it checks the functional shape of your data:

- For low fluence it verifies that log(W_THz) vs log(I_p) yields a slope between 1.5 and 2.0.
- For high fluence it verifies that the slope is less than 1 (saturation).

If your computed values satisfy both the value checks and the shape checks, you receive the full score. The verifier automatically combines these checks into a final reward between 0 and 1.
