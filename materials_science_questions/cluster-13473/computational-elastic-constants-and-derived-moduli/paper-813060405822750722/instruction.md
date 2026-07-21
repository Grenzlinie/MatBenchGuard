# Young's Modulus of Single-Crystal Cu Nanopillars via Molecular Dynamics

## Problem background
Nanostructured copper exhibits size-dependent mechanical properties that are critical for micro- and nano-scale devices. Molecular dynamics (MD) simulations can predict the elastic response of single-crystal Cu nanopillars under compression, complementing experimental measurements. This task explores the elastic stiffness of <111>-oriented Cu nanopillars of different diameters by recreating the MD simulation workflow.

## Approach
The simulations use an embedded atom method (EAM) potential to model Cu–Cu interactions. A face-centered cubic (FCC) Cu nanopillar with <111> orientation is constructed using a lattice constant of 0.3639 nm. Fixed layers at the ends enforce uniaxial compression along the pillar axis at a controlled strain rate and temperature. The simulation uses an integration timestep of 0.01 ps/step. The resulting atomic stress is converted into engineering stress, and the engineering strain is computed from the length change. Young’s modulus is extracted by performing a linear least-squares fit of the stress–strain data in the small-strain elastic region (strain 0.03–0.05). This procedure is repeated for nanopillars of several diameters to examine the size dependence.

## Reproduction target
Run MD compression simulations for single-crystal Cu nanopillars with diameters of 2, 3, 4, and 6 nm (length 1.8 nm, cone angle 2–3°). Maintain the system at 300 K and apply uniaxial compression at a strain rate of 10⁹ s⁻¹ using the Cu EAM potential. The integration timestep must be 0.01 ps/step. Compute the engineering stress–strain curve for each diameter. From the data in the strain interval 0.03–0.05, obtain the Young’s modulus as the slope of the linear fit. Save the raw stress–strain data (diameter, strain, stress) for all diameters in `/app/outputs/stress_strain_data.json`, and save the derived moduli in `/app/outputs/young_moduli.json`.

## Assets

- LAMMPS: https://lammps.sandia.gov
- Cu EAM potential (Cu_u3.eam): https://www.ctcms.nist.gov/potentials/Download/Cu_u3.eam

## Workflow steps

### Step 1: Run MD compression simulations
- Role: process
- Action: Set up LAMMPS input scripts for Cu nanopillars with diameters 2, 3, 4, and 6 nm. Create an FCC Cu nanopillar with <111> orientation using a lattice constant of 0.3639 nm, fix end layers, and apply uniaxial compression at 300 K using the Cu EAM potential and an integration timestep of 0.01 ps/step. Run the simulation and collect stress–strain data.

### Step 2: Extract stress–strain data
- Role: scored (load-bearing)
- Action: From the MD simulation output, compute engineering stress and engineering strain for each diameter. Save the data as a JSON array covering the strain range 0.03–0.05 for each diameter.
- Output file: `/app/outputs/stress_strain_data.json`
- Format: json
- Contract: Array of objects with diameter_nm (number), strain (number), stress_GPa (number). Must include points covering strain 0.03–0.05 for each diameter.
- Scoring: scored by hidden verifier

### Step 3: Compute Young's moduli
- Role: scored
- Action: For each diameter (2, 3, 4, 6 nm), perform a linear least-squares fit of stress_GPa vs. strain over the strain interval 0.03–0.05. The slope is the Young's modulus in GPa. Save as a JSON object mapping diameter to modulus.
- Output file: `/app/outputs/young_moduli.json`
- Format: json
- Contract: JSON object with string keys '2', '3', '4', '6' mapped to numbers (Young's modulus in GPa).
- Scoring: scored by hidden verifier (checked for internal consistency with recomputed moduli from stress_strain_data.json)

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain_data.json`
- `/app/outputs/young_moduli.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain_data.json
- path: `/app/outputs/stress_strain_data.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Raw stress–strain data points for Cu nanopillars; the checker will recompute Young's modulus from these points in the strain range 0.03–0.05.
- schema:
  - `type`: array
  - `required`:
    - `diameter_nm`: number
    - `strain`: number
    - `stress_GPa`: number
  - `items`:
    - `diameter_nm`: number
    - `strain`: number
    - `stress_GPa`: number

### young_moduli.json
- path: `/app/outputs/young_moduli.json`
- format: json
- purpose: scored
- target_policy: consistency
- description: Self-reported Young's modulus values for each diameter; the checker verifies that these values are consistent with the moduli recomputed from stress_strain_data.json.
- schema:
  - `type`: object
  - `required`:
    - `2`: number
    - `3`: number
    - `4`: number
    - `6`: number

Notes: The checker recomputes moduli from stress_strain_data.json and then checks that the self-reported values in young_moduli.json match those recomputed moduli (consistency check). Reference values derived from the target simulation are used to assess the recomputed moduli.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain_data.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "array",
        "required": {
          "diameter_nm": "number",
          "strain": "number",
          "stress_GPa": "number"
        },
        "items": {
          "diameter_nm": "number",
          "strain": "number",
          "stress_GPa": "number"
        }
      },
      "description": "Raw stress–strain data points for Cu nanopillars; the checker will recompute Young's modulus from these points in the strain range 0.03–0.05."
    },
    {
      "file": "young_moduli.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "consistency",
      "schema": {
        "type": "object",
        "required": {
          "2": "number",
          "3": "number",
          "4": "number",
          "6": "number"
        }
      },
      "description": "Self-reported Young's modulus values for each diameter; the checker verifies that these values are consistent with the moduli recomputed from stress_strain_data.json."
    }
  ],
  "notes": "The checker recomputes moduli from stress_strain_data.json and then checks that the self-reported values in young_moduli.json match those recomputed moduli (consistency check). Reference values derived from the target simulation are used to assess the recomputed moduli."
}
```

## How you are scored
A hidden verifier will independently evaluate your output artifacts. For the stress–strain data (`stress_strain_data.json`), the verifier will recompute the Young’s modulus from the points you provide within the strain range 0.03–0.05 and assess whether the resulting trend and values are physically consistent with the target simulation results. Your self-reported moduli (`young_moduli.json`) will be checked against the moduli recomputed from your stress–strain data to ensure internal consistency. The final score (0.0–1.0) is a weighted combination of these two checks. Simply stating expected modulus values without supporting simulation data will not earn credit; the verifier requires raw data that allows recalculation of the moduli.