# High-Field Electron Transport in CdTe via Monte Carlo Simulation

## Problem background
CdTe is a polar semiconductor whose electron transport properties under high electric fields are of great interest for device applications. At high fields, electrons can be transferred from the high-mobility central Γ valley to lower-mobility satellite L valleys, leading to a phenomenon of negative differential mobility. A detailed understanding of this effect requires a simulation that accurately accounts for the band structure nonparabolicity and the various scattering mechanisms. Monte Carlo simulation of single-electron trajectories is a powerful method to compute the steady-state drift velocity and low-field mobility from first principles. The challenge is to implement such a simulation with full complexity of the conduction band and to extract the electron drift velocity as a function of electric field.

## Approach
The simulation models electron transport using a single-electron Monte Carlo method at a lattice temperature of 300 K. The conduction band is described by a nonparabolic central Γ valley using Kane's theory (neglecting spin-orbit splitting) and higher-energy satellite L valleys at the (111) Brillouin zone boundary with an energy separation of 0.51 eV above the Γ minimum. The Γ valley effective mass is 0.11 m₀; the L valley effective mass is 0.2 m₀. Intravalley scattering mechanisms include polar optical phonon scattering (optical phonon energy 21.4 meV) and acoustic phonon scattering (deformation potential 9.5 eV, acoustic phonon energy 18.9 meV) in both valleys. In the Γ valley, the admixture of p-type valence-band wavefunctions (optical deformation potential 1×10⁹ eV/cm) is included in the scattering rates. Intervalley scattering between Γ and L valleys is through LA phonons with a deformation potential of 6×10⁸ eV/cm. The static and optical dielectric constants are 9.65 and 7.21, respectively; the crystal density is 6.06 g/cm³ and the sound velocity is 3.39×10⁵ cm/s. A uniform electric field is applied, and the electron's free flights are simulated until a steady-state drift velocity is reached. The simulation should be carried out for electric field strengths from 0 to approximately 30 kV/cm, with a finer sampling near zero field to resolve the low-field mobility.

## Reproduction target
The goal is to compute the steady-state electron drift velocity as a function of the applied electric field in CdTe at 300 K using the model and parameters described above, and to derive the low-field electron mobility. The results must be saved as two artifacts: a CSV file containing the field (in kV/cm) and the corresponding drift velocity (in cm/s) for each field value; and a plain-text file containing a single floating-point number giving the low-field mobility in cm²/V·s, obtained from the slope of the velocity-field curve near zero field.

## Assets
No external datasets, models, or pre-trained weights are required. All needed physical constants are listed in the Approach section. The simulation can be implemented in Python using standard numerical libraries (numpy, scipy); these are available via the Python Package Index.

## Workflow steps

### Step 1: Monte Carlo simulation of electron drift velocity
- Role: scored (load-bearing)
- Action: Implement a Monte Carlo simulation of electron transport in CdTe at 300 K. Model the conduction band with a nonparabolic Γ valley (Kane's theory, spin-orbit neglected), L satellite valleys at the (111) zone edge with a 0.51 eV energy separation, intravalley polar optical and acoustic scattering in both valleys (including p‑type admixture in Γ), and intervalley scattering between Γ and L via LA phonons with the given deformation potential. Run for electric fields in the range 0 to ~30 kV/cm with fine steps near zero. Output a CSV file containing the steady‑state drift velocity for each field.
- Output file: `/app/outputs/step_01_drift_velocity.csv`
- Format: csv
- Contract: CSV with columns 'field_kV_per_cm' (float, electric field in kV/cm) and 'drift_velocity_cm_per_s' (float, drift velocity in cm/s). One row per field value.
- Scoring: scored by hidden verifier

### Step 2: Compute low-field mobility
- Role: scored
- Action: From the drift velocity vs. field data (step_01_drift_velocity.csv), extract the low‑field electron mobility. The mobility is the slope Δv_d / ΔE for fields near zero; for example, use a linear fit to the velocities at the smallest field points to obtain the mobility in cm²/V·s. Write the single mobility value to a text file.
- Output file: `/app/outputs/step_02_low_field_mobility.txt`
- Format: txt
- Contract: A single float value (the mobility in cm²/V·s) written as plain text.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_drift_velocity.csv`
- `/app/outputs/step_02_low_field_mobility.txt`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_drift_velocity.csv
- path: `/app/outputs/step_01_drift_velocity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Simulated electron drift velocity vs electric field for CdTe at 300 K.
- schema:
  - `type`: table
  - `required_columns`: `field_kV_per_cm`, `drift_velocity_cm_per_s`
  - `units`:
    - `field_kV_per_cm`: kV/cm
    - `drift_velocity_cm_per_s`: cm/s

### step_02_low_field_mobility.txt
- path: `/app/outputs/step_02_low_field_mobility.txt`
- format: txt
- purpose: scored
- target_policy: threshold_or_better
- description: Low-field electron mobility extracted from the drift velocity curve.
- schema:
  - `type`: text
  - `unit`: cm^2/V·s

Notes: The Monte Carlo simulation uses the physical parameters stated in the instruction; no external experimental data is required. The intervalley deformation potential is fixed to the paper's best-fit value.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_drift_velocity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "field_kV_per_cm",
          "drift_velocity_cm_per_s"
        ],
        "units": {
          "field_kV_per_cm": "kV/cm",
          "drift_velocity_cm_per_s": "cm/s"
        }
      },
      "description": "Simulated electron drift velocity vs electric field for CdTe at 300 K."
    },
    {
      "file": "step_02_low_field_mobility.txt",
      "format": "txt",
      "purpose": "scored",
      "target_policy": "threshold_or_better",
      "schema": {
        "type": "text",
        "unit": "cm^2/V·s"
      },
      "description": "Low-field electron mobility extracted from the drift velocity curve."
    }
  ],
  "notes": "The Monte Carlo simulation uses the physical parameters stated in the instruction; no external experimental data is required. The intervalley deformation potential is fixed to the paper's best-fit value."
}
```

## How you are scored
A hidden verifier will independently assess each of your scored artifacts after submission. For the drift velocity CSV, the verifier compares your drift velocity values at selected field strengths against a hidden reference; the comparison metric is directional — producing drift velocities that meet or exceed the reference threshold earns full credit for that artifact, while larger deviations receive lower scores. For the low-field mobility, the verifier checks that your submitted value meets a hidden threshold. The final score is a weighted combination of these two checks, with the drift velocity data carrying the majority of the weight. Reporting a number without a correctly simulated artifact will not pass because the verifier evaluates the entire file content.
