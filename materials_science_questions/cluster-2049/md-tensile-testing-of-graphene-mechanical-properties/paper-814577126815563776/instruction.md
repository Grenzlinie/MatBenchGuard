# Fracture Properties and Prefracture Cracks in Disordered Polycrystalline Graphene Under Tension

## Problem background
Polycrystalline graphene (PCG) is a promising material for many applications, but the influence of grain boundaries, disorder, and thermal annealing on its mechanical strength and fracture behavior remains not fully understood. This task addresses that question by using molecular dynamics (MD) simulations to investigate how the extent of thermal annealing (graphenization) affects the tensile fracture properties of a PCG model, and to explore the role of nonpropagating prefracture cracks (PFCs) that may form during tensile loading.

## Approach
The approach is to generate a highly disordered polycrystalline graphene model through a liquid‑quench MD protocol, followed by thermal annealing at 4000 K. From this trajectory, two representative states are extracted: the as‑quenched (0 ns annealed) model and the model after 25 ns of annealing. Both models are then subjected to uniaxial tensile tests along the y‑direction at 300 K using the screened environment‑dependent REBO (SED‑REBO) interatomic potential to avoid known cutoff artifacts. Each tensile test is repeated five times with different initial velocity seeds to capture statistical variation. The resulting stress–strain curves are converted to true stress and true strain, and the fracture properties (failure strain, failure stress, fracture energy defined as the integral of the true stress–strain curve up to failure, and Young’s modulus) are extracted. Simultaneously, the trajectory of bond breakings is analyzed to count the number of nonpropagating prefracture cracks (PFCs) that occur before catastrophic failure and to identify the strain and stress at which the first nanocrack appears. The comparison of the quenched and the 25‑ns annealed systems allows an assessment of how the degree of ordering impacts fracture resistance and the prevalence of PFCs.

## Reproduction target
Produce a CSV file containing per‑run fracture metrics for the two polycrystalline graphene models (as‑quenched and 25‑ns annealed) under uniaxial tension along the y‑direction. The file must contain exactly ten rows: five independent tensile test runs for the quenched model and five for the 25‑ns annealed model. Required columns: model (string, either 'quenched' or '25ns'), direction (string, always 'y'), failure_strain (dimensionless), failure_stress (in GPa), fracture_energy (in GPa), number_of_PFCs (integer count of nonpropagating prefracture cracks), strain_first_nanocrack (dimensionless), stress_first_nanocrack (in GPa). The computed values will be checked against reference expectations (derived from the original study) and for internal consistency between the two models. The CSV file must be written to `/app/outputs/step_3_results.csv`.

## Assets

- LAMMPS Molecular Dynamics Simulator: https://www.lammps.org/
- Second-generation REBO potential: LAMMPS MANYBODY package
- Screened environment-dependent REBO (SED-REBO) potential: LAMMPS MANYBODY package (pair_style rebos)
- Python with numpy, matplotlib: pip install numpy matplotlib

## Workflow steps

### Step 1: Generate polycrystalline graphene models (quenched and 25-ns annealed)
- Role: process
- Action: Run MD simulations to create two PCG configurations: one as-quenched (0 ns annealed) and one after 25 ns of thermal annealing at 4000 K. Follow the paper’s liquid-quench method (random insertion of ~10000 atoms, REBO potential, quenching with external planar potential) and then anneal at 4000 K for the required time, followed by relaxation at 300 K with SED-REBO. Save the final relaxed atomic configurations for later tensile testing.
- Evidence: none

### Step 2: Compute fracture properties and prefracture crack statistics
- Role: scored (load-bearing)
- Action: Perform uniaxial tensile test simulations along the y-direction on both the quenched and 25-ns annealed models using the SED-REBO potential at a constant engineering strain rate, 300 K, with zero transverse stress via a Berendsen barostat/thermostat. For each model run five independent simulations with different initial velocity seeds. From the resulting stress-strain curves determine failure strain, failure stress, and fracture energy (integral of the true stress-strain curve up to failure). From bond-breaking analysis count the number of nonpropagating prefracture cracks (PFCs) before catastrophic failure and identify the strain and stress at first nanocrack. Output all per-run results as a CSV file.
- Output file: `/app/outputs/step_3_results.csv`
- Format: csv
- Contract: CSV with columns: model (quenched or 25ns), direction (y), failure_strain (dimensionless), failure_stress (GPa), fracture_energy (GPa), number_of_PFCs (integer), strain_first_nanocrack (dimensionless), stress_first_nanocrack (GPa).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_3_results.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_3_results.csv
- path: `/app/outputs/step_3_results.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Per-run fracture metrics from uniaxial tensile tests for the two polycrystalline graphene models. The checker will compute per-model averages and compare them to hidden reference values; it will also verify that the number of PFCs is lower in the 25-ns annealed system and that fracture properties decrease with annealing.
- schema:
  - `type`: table
  - `required_columns`: `model`, `direction`, `failure_strain`, `failure_stress`, `fracture_energy`, `number_of_PFCs`, `strain_first_nanocrack`, `stress_first_nanocrack`
  - `units`:
    - `failure_strain`: dimensionless
    - `failure_stress`: GPa
    - `fracture_energy`: GPa
    - `strain_first_nanocrack`: dimensionless
    - `stress_first_nanocrack`: GPa

Notes: The hidden checker also validates trend consistency: number_of_PFCs(25ns) < number_of_PFCs(quenched) and fracture_energy(25ns) < fracture_energy(quenched).

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_3_results.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "model",
          "direction",
          "failure_strain",
          "failure_stress",
          "fracture_energy",
          "number_of_PFCs",
          "strain_first_nanocrack",
          "stress_first_nanocrack"
        ],
        "units": {
          "failure_strain": "dimensionless",
          "failure_stress": "GPa",
          "fracture_energy": "GPa",
          "strain_first_nanocrack": "dimensionless",
          "stress_first_nanocrack": "GPa"
        }
      },
      "description": "Per-run fracture metrics from uniaxial tensile tests for the two polycrystalline graphene models. The checker will compute per-model averages and compare them to hidden reference values; it will also verify that the number of PFCs is lower in the 25-ns annealed system and that fracture properties decrease with annealing."
    }
  ],
  "notes": "The hidden checker also validates trend consistency: number_of_PFCs(25ns) < number_of_PFCs(quenched) and fracture_energy(25ns) < fracture_energy(quenched)."
}
```

## How you are scored
A hidden verifier will score your submission using only the `/app/outputs/step_3_results.csv` file. The verifier will parse the CSV, compute per‑model averages for each numeric column, and compare them to reference values (which are not disclosed to you). The scoring rewards results that meet or exceed the expected reference range for failure strain, failure stress, fracture energy, and first‑crack strain/stress. Additionally, the verifier will check that the numbers of PFCs and the fracture energy values satisfy the expected physical relation between the two models (derived from the study), without disclosing the direction. Meeting or surpassing these expectations earns full credit; larger deviations reduce the score. The verifier will also enforce the output contract: correct number of rows and columns, valid data types, and the presence of both models. The final reward is a weighted combination of these checks, with the main weight on the collective accuracy of the fracture metrics and PFC counts.
