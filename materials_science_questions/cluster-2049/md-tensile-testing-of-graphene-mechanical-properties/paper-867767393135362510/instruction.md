# MD Tensile Testing of Graphene Nanoribbons

## Problem background
Graphene nanoribbons (GNRs) — strips of single-layer graphene with a finite width — exhibit mechanical properties that depend on the edge chirality (armchair, zigzag, or chiral). Knowing how Young's modulus, yielding strength, and breaking strain vary with chirality is crucial for potential applications as reinforcement in composites or in nano-electromechanical devices. This work uses atomistic molecular dynamics simulations to quantify these three properties for three representative GNR chiralities under uniaxial tension at 300 K, providing a benchmark for the mechanical performance of GNRs.

## Approach
The simulations are performed using the large-scale atomic/molecular massively parallel simulator (LAMMPS) with the second-generation reactive empirical bond order (REBO) potential, which accurately describes carbon–carbon interactions. Three GNR models — armchair (θ=0), chiral (θ=π/12), and zigzag (θ=π/6) — each 20 nm long and 10 nm wide, are constructed. Each ribbon is subjected to uniaxial tensile loading at a constant engineering strain rate of 0.005 %/fs at 300 K, with both ribbon ends constrained to maintain the load. The simulation records engineering stress (in GPa) and engineering strain at regular intervals, producing a stress–strain curve for each chirality. From these curves, one can extract Young's modulus from the low-strain slope, yielding strength as the maximum stress, and breaking strain as the strain at fracture.

## Reproduction target
Your task is to produce a single CSV file, `/app/outputs/stress_strain.csv`, containing the complete time series of engineering stress and strain for all three GNR types under the conditions described above. The file must include columns for `ribbon_type` (AGNR, CGNR, ZGNR), `strain`, and `stress` (GPa). From this raw data, the hidden verifier will recompute Young's modulus, yielding strength, and breaking strain for each ribbon and compare them to reference values. The correctness of your simulation directly determines the accuracy of the extracted properties.

## Assets

- LAMMPS (Molecular Dynamics Simulator): https://www.lammps.org/download.html

## Workflow steps

### Step 1: Generate GNR atomic models
- Role: process
- Action: Create atomistic structures for armchair (θ=0), zigzag (θ=π/6), and chiral (θ=π/12) graphene nanoribbons of length L=20 nm and width W=10 nm, suitable as LAMMPS input data.
- Evidence: `/app/outputs/models_generated.log`

### Step 2: MD tensile simulation and stress–strain recording
- Role: scored (load-bearing)
- Action: For each GNR type, run a uniaxial tensile MD simulation at 300 K using LAMMPS with the second-generation REBO potential (cut-off 2.0 Å). Apply a strain rate of 0.005 %/fs with both ribbon ends constrained. Record engineering stress (GPa) and engineering strain at regular intervals and write the complete (strain, stress) data for all three ribbons to a single CSV file.
- Output file: `/app/outputs/stress_strain.csv`
- Format: csv
- Contract: Columns: ribbon_type (str; values: AGNR, ZGNR, CGNR), strain (float), stress (float; units: GPa). One row per recorded time step.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/stress_strain.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### stress_strain.csv
- path: `/app/outputs/stress_strain.csv`
- format: csv
- purpose: scored
- target_policy: metric_recompute
- description: Complete time series of engineering stress and strain for three GNR types under uniaxial tension at 300 K. The checker recomputes Young's modulus (low-strain slope), yielding strength (maximum stress), and breaking strain (strain at fracture) from this raw data and compares the derived values to the paper's reported quantities.
- schema:
  - `type`: table
  - `required_columns`: `ribbon_type`, `strain`, `stress`
  - `units`:
    - `strain`: dimensionless
    - `stress`: GPa

Notes: The additional outputs for Cauchy-Born ratios, high-temperature bond-flips, and SW dislocation energies were removed because the toolchain could not provision corresponding solve blocks. The task scope reverts to the original 300 K mechanical properties, which are the main headline result.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "stress_strain.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "table",
        "required_columns": [
          "ribbon_type",
          "strain",
          "stress"
        ],
        "units": {
          "strain": "dimensionless",
          "stress": "GPa"
        }
      },
      "description": "Complete time series of engineering stress and strain for three GNR types under uniaxial tension at 300 K. The checker recomputes Young's modulus (low-strain slope), yielding strength (maximum stress), and breaking strain (strain at fracture) from this raw data and compares the derived values to the paper's reported quantities."
    }
  ],
  "notes": "The additional outputs for Cauchy-Born ratios, high-temperature bond-flips, and SW dislocation energies were removed because the toolchain could not provision corresponding solve blocks. The task scope reverts to the original 300 K mechanical properties, which are the main headline result."
}
```

## How you are scored
The hidden verifier reads your `stress_strain.csv`, separates the data by ribbon type, and computes three properties per ribbon: Young's modulus (from a linear fit at low strain, <2%), yielding strength (the maximum stress on the curve), and breaking strain (the strain at which the stress drops sharply). This yields nine values (three for each of the three ribbon types). Each property is compared to a hidden reference. Your final reward is proportional to the number of these nine values that meet the acceptance criteria; nine correct matches yield the maximum score. No credit is given for simply reporting paper numbers — the verifier recomputes the properties from your raw simulation data.
