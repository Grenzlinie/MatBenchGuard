# Numerical Simulation of a Finite-Strain Shape Memory Alloy Constitutive Model

## Problem background
Shape memory alloys (SMAs) display complex thermomechanical responses including martensitic phase transformation, variant reorientation, and tension-compression asymmetry. These materials can undergo large deformations, making finite-strain constitutive models essential for engineering simulations. The model considered here is a three-dimensional, finite-strain formulation for polycrystalline SMAs. It uses a multiplicative decomposition of the deformation gradient into elastic and inelastic parts, introduces scalar volume fractions for stress-induced and temperature-induced martensite, and a tensorial internal variable for the preferred direction of oriented martensite. The constitutive relations are derived from a hyperelastic free energy and dissipation laws, capturing anisotropic transformation, self-accommodation, and reorientation.

## Approach
Implement the finite-strain SMA constitutive model from its formulation (elastic–inelastic decomposition, Saint-Venant–Kirchhoff hyperelasticity, evolution equations for martensite volume fractions and reorientation) using the provided material parameters for the NiTi wire (Case II). Simulate a single material point under isothermal, strain-controlled uniaxial tension at T = 20 °C. The strain path is a ramp from 0 to 8% engineering strain followed by unloading back to 0%, discretized into small increments. At each increment, the stress and the internal variables (volume fractions of stress-induced martensite xi_S, temperature-induced martensite xi_T, and the norm of the preferred direction tensor N_norm) are computed by solving the constitutive equations. The reorientation update uses an explicit forward-Euler scheme, and the transformation kinetics are solved iteratively (e.g., Newton‑Raphson). The simulation produces a CSV file recording stress and internal variable evolution throughout the loading‑unloading cycle.

## Reproduction target
Generate the file `step_01_stress_strain.csv` at `/app/outputs/`. The file represents the result of a single-material-point uniaxial tension simulation for the NiTi wire (Case II parameters) at 20 °C. The strain schedule is: increase engineering strain from 0 to 0.08, then decrease back to 0, using a sufficient number of steps to resolve the response. For each strain step, output a row with the following columns: `strain` (engineering strain, unitless), `stress_MPa` (uniaxial stress in MPa), `xi_S` (stress-induced martensite volume fraction, 0–1), `xi_T` (temperature-induced martensite volume fraction, 0–1), and `N_norm` (norm of the preferred direction tensor, ≥ 0). The CSV must have a header line with exactly these five column names. The rows should be ordered approximately by increasing strain during loading and then by decreasing strain during unloading.

## Assets

- Material parameters for case II NiTi wire: Provided in the task instruction (Table 3 of the source paper)

## Workflow steps

### Step 1: Uniaxial tension simulation for NiTi wire at T=20°C
- Role: scored (load-bearing)
- Action: Implement the finite-strain SMA constitutive model (multiplicative decomposition of the deformation gradient, hyperelastic Saint-Venant-Kirchhoff free energy, dissipation inequality, and evolution laws for martensite volume fractions and reorientation) using the Case II material parameters given in the instruction. Simulate isothermal uniaxial strain-controlled tension at 20°C: ramp engineering strain from 0 to 0.08 and back to 0. At each increment, solve for the stress and the internal variables (volume fractions of stress-induced and temperature-induced martensite, and the norm of the preferred direction tensor). Write the results to a CSV file.
- Output file: `/app/outputs/step_01_stress_strain.csv`
- Format: csv
- Contract: CSV file with header: strain,stress_MPa,xi_S,xi_T,N_norm. strain is engineering strain (unitless), stress_MPa is the uniaxial stress in MPa, xi_S and xi_T are martensite volume fractions in [0,1], and N_norm is the norm of the preferred direction tensor (≥0). Each row corresponds to one simulation time step, ordered approximately by strain.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_stress_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_stress_strain.csv
- path: `/app/outputs/step_01_stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Result of a single material point finite-strain simulation under uniaxial tension loading‑unloading at 20°C, containing the stress and internal variable evolution.
- schema:
  - `type`: table
  - `required_columns`: `strain`, `stress_MPa`, `xi_S`, `xi_T`, `N_norm`
  - `units`:
    - `strain`: unitless
    - `stress_MPa`: MPa
    - `xi_S`: unitless
    - `xi_T`: unitless
    - `N_norm`: unitless

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "strain",
          "stress_MPa",
          "xi_S",
          "xi_T",
          "N_norm"
        ],
        "units": {
          "strain": "unitless",
          "stress_MPa": "MPa",
          "xi_S": "unitless",
          "xi_T": "unitless",
          "N_norm": "unitless"
        }
      },
      "description": "Result of a single material point finite-strain simulation under uniaxial tension loading‑unloading at 20°C, containing the stress and internal variable evolution."
    }
  ],
  "notes": ""
}
```

## How you are scored
Your submission is scored by a hidden verifier that inspects the CSV file. It extracts the uniaxial stress values at a set of hidden strain points covering the complete loading and unloading path. Each extracted stress is compared against a reference solution obtained from a trusted implementation of the same finite-strain model, using a tolerance that accounts for reasonable numerical differences between independent implementations. The score is the fraction of these strain points where the stress falls within the allowed range. The verifier also checks that xi_S and xi_T are within [0,1], N_norm is non-negative, and that the final state at zero strain shows evidence of a residual stress indicating martensite transformation. These checks are combined into a single overall reward between 0 and 1. No knowledge of any specific published numerical result is required; the reference is computed independently from the model specification.
