# Young's Modulus of Helical Multi-Shell Au Nanowires by Molecular Dynamics

## Problem background
Understanding the mechanical properties of metallic nanowires is essential for their use in nanoscale devices and sensors. Gold (Au) nanowires, in particular, can adopt helical multi-shell (HMS) structures whose atomic arrangement differs from bulk fcc crystals. Molecular dynamics (MD) simulations allow the study of how the atomic structure influences nanomechanical properties, such as the Young's modulus, under controlled tensile loading. This task investigates two HMS Au nanowire models, differing in the interatomic spacing of the central atom row, by computing their Young's modulus from stress–strain curves obtained from MD tensile simulations with the modified embedded-atom method (MEAM) potential. The results for a range of low temperatures provide a benchmark for nanomechanics simulation protocols.

## Approach
The approach consists of three stages: building the atomic structures, performing MD tensile simulations, and extracting the Young's modulus.

- **Structure construction:** The HMS nanowires are built by rolling a triangular-lattice sheet into a helical shell of chiral vector (7,3) with a central single-atom row. Two models are considered: Model‑1 with a central interatomic distance of 2.88 Å and Model‑2 with 3.03 Å.
- **Molecular dynamics:** For each model and each temperature (25 to 200 K in 25 K steps), LAMMPS runs with the MEAM potential for Au. Equilibration proceeds in two stages: first, the central atom row is constrained to the axis to relax helical distortions; then, the atoms at both ends are constrained. After equilibration, an axial tensile force is applied. The force increases by a fixed increment every constant number of MD steps until the nanowire fractures. Axial stress and strain are recorded during elongation, yielding a stress–strain curve for each condition.
- **Modulus extraction:** From the small-strain linear regime of each stress–strain curve, the Young's modulus is computed as the slope dσ/dε.

The primary comparison is the temperature-dependent modulus for the two HMS models, which reveals the effect of the central interatomic spacing on nanoscale stiffness.

## Reproduction target
Compute the Young's modulus (in GPa) for the two HMS Au nanowire models:
- Model‑1 (central interatomic distance 2.88 Å)
- Model‑2 (central interatomic distance 3.03 Å)
at each of the following eight temperatures: 25, 50, 75, 100, 125, 150, 175, 200 K.
The moduli are obtained from the linear small‑strain regime of the stress–strain curves produced by MD tensile simulations with the MEAM potential and the equilibration/loading protocol described above.
Output all 16 values in the CSV file `/app/outputs/young_moduli.csv`. The file must contain the columns `Model`, `Temperature(K)`, and `YoungsModulus(GPa)`, with Model‑1 rows first followed by Model‑2 rows, temperature ascending within each model. No additional columns are allowed. The CSV serves as the sole scored artifact.

## Assets

- LAMMPS molecular dynamics simulator: https://lammps.sandia.gov/
- MEAM potential for Au

## Workflow steps

### Step 1: Build atomic structures of HMS Au nanowire models
- Role: process
- Action: Construct the initial atomic coordinates for Model‑1 and Model‑2 of helical multi‑shell Au nanowires using the chiral vector (7,3) and the central interatomic distances (2.88 Å for Model‑1, 3.03 Å for Model‑2). Produce structure files suitable for LAMMPS input.
- Evidence: `/app/outputs/model1.data, model2.data`

### Step 2: Run MD tensile simulations
- Role: process
- Action: For each model and each temperature (25, 50, 75, 100, 125, 150, 175, 200 K), perform molecular dynamics simulations with LAMMPS using the MEAM potential for Au. Apply two‑stage equilibration: first 2×10⁵ steps with the central single‑atom row constrained to the axis, then 10⁵ steps with the atoms at both ends constrained. Afterwards, apply an axial external force that increases by 0.005 nN every 2.5×10⁴ steps until fracture, recording axial stress and strain during elongation.
- Evidence: `/app/outputs/stress_strain_simulation_logs`

### Step 3: Extract Young's modulus and create scored output
- Role: scored (load-bearing)
- Action: From each simulated stress–strain curve, identify the linear small‑strain regime and compute Young's modulus as the slope dσ/dε. Gather all modulus values (in GPa) for Model‑1 and Model‑2 at the eight temperatures and write young_moduli.csv.
- Output file: `/app/outputs/young_moduli.csv`
- Format: csv
- Contract: Columns: Model (string, 'Model-1' or 'Model-2'), Temperature(K) (integer, ascending 25 to 200), YoungsModulus(GPa) (float, in GPa). 16 rows; temperature order ascending for each model (Model-1 rows first, then Model-2). No extra columns.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/young_moduli.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### young_moduli.csv
- path: `/app/outputs/young_moduli.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed Young's moduli from MD simulations, to be compared against hidden reference values from the paper.
- schema:
  - `type`: table
  - `required_columns`: `Model`, `Temperature(K)`, `YoungsModulus(GPa)`
  - `description`: Each row: model name, temperature in Kelvin, Young's modulus in GPa. Rows: 16 (8 temperatures for Model-1 then 8 for Model-2).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "young_moduli.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "Model",
          "Temperature(K)",
          "YoungsModulus(GPa)"
        ],
        "description": "Each row: model name, temperature in Kelvin, Young's modulus in GPa. Rows: 16 (8 temperatures for Model-1 then 8 for Model-2)."
      },
      "description": "Computed Young's moduli from MD simulations, to be compared against hidden reference values from the paper."
    }
  ],
  "notes": ""
}
```

## How you are scored
A hidden verifier reads your submitted `/app/outputs/young_moduli.csv` and possibly other intermediate evidence files. It compares your reported Young's modulus values to reference results derived from a separate implementation of the same protocol, and also checks that the temperature trend for each model is physically plausible (e.g., monotonic decrease with increasing temperature). 

Each correctly matching modulus contributes to the total reward, and the trend check acts as a bonus gate that can multiply the overall score. The verifier tolerates small deviations that arise from different numerical implementations or stochastic MD trajectories, but large systematic errors or physically inconsistent trends will reduce the reward. 

Do not attempt to hardcode or guess the expected values; the task is designed so that only a faithful execution of the described molecular dynamics protocol yields a high score. The final reward is a float between 0 and 1, where 1 represents a perfect match with the reference.
