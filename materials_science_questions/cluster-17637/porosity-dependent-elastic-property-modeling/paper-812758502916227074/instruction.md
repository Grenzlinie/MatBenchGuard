# Porosity-Dependent Effective Young's Modulus Prediction via 2D RVE Micromechanical Modeling

## Problem background
Fused deposition modeling (FDM) 3D printing produces polymer parts with internal pores that reduce mechanical strength and stiffness. Understanding how porosity affects the effective Young's modulus is essential for reliable design. X-ray computed tomography (XCT) can quantitatively characterize the three-dimensional size, shape, and spatial distribution of these microscopic pores. This task aims to predict the effective Young's modulus of FDM-printed PLA as a function of porosity using actual pore size statistics obtained from XCT. The predicted values will demonstrate whether a micromechanical model based on the measured pore distribution can capture the experimentally observed stiffness reduction, enabling designers to estimate part stiffness without destructive testing.

## Approach
The prediction is based on a two-dimensional micromechanical representative volume element (RVE) model. The RVE is a square elastic matrix containing N=80 circular pores whose diameters are drawn from the pore size distribution of specimen Set A (provided below). The matrix is assigned a Young's modulus of 3500 MPa and Poisson's ratio of 0.33; pores are treated as nearly void (E=1e-6 MPa, ν=1e-6). The RVE is loaded under uniaxial tension in plane stress with periodic boundary conditions. Finite element analysis computes the homogenized stress and strain via volume averaging, and the effective Young's modulus is obtained from the ratio of average axial stress to average axial strain. To account for spatial randomness, three independent random pore placements are generated for each porosity, and the final prediction is the mean modulus over the three realizations.

## Reproduction target
Produce a CSV file `predicted_E_vs_porosity.csv` containing the mean predicted Young's modulus for each of five porosity values: approximately 4.28%, 4.81%, 4.875%, 5.84%, and 6.32%. For every porosity, generate three random RVE realizations using the pore size distribution of Set A (Table 6 from the source, reproduced below), run the FE homogenization, and average the three modulus results. The CSV must have two columns: `porosity` (float, %) and `predicted_youngs_modulus` (float, MPa), one row per porosity.

## Assets

- FEniCS (or equivalent open‑source finite element solver): https://fenicsproject.org/
- Gmsh (mesh generation): https://gmsh.info/
- Python scientific stack: numpy scipy matplotlib

## Workflow steps

### Step 1: RVE geometry generation and FE homogenisation
- Role: process
- Action: For each of the five target porosity values, generate a square 2D RVE containing N=80 circular pores. Pore sizes are drawn from the supplied XCT pore‑size distribution of Set A and placed at random, non‑overlapping positions. Create a finite‑element mesh, assign matrix properties (Young's modulus 3500 MPa, Poisson's ratio 0.33) and pore properties (nearly void: E=1e-6 MPa, ν=1e-6). Apply periodic boundary conditions, solve the plane‑stress linear elasticity problem under uniaxial tension, and compute the homogenised Young's modulus from volume‑averaged stress and strain. Repeat for three independent random realisations per porosity. Write the per‑realisation moduli (optionally with additional metadata) to an evidence file.
- Evidence: `/app/outputs/simulation_raw_outputs.json`

### Step 2: Averaged Young's modulus predictions
- Role: scored (load-bearing)
- Action: For each porosity, average the homogenised Young's modulus from the three realisations obtained in the previous step. Write a CSV file with columns `porosity` (float, %) and `predicted_youngs_modulus` (float, MPa), containing one row per porosity (five rows in total).
- Output file: `/app/outputs/predicted_E_vs_porosity.csv`
- Format: csv
- Contract: Two columns: porosity (float, %), predicted_youngs_modulus (float, MPa). One row for each of the five porosity values (approximately 4.28, 4.81, 4.875, 5.84, 6.32).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/predicted_E_vs_porosity.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### predicted_E_vs_porosity.csv
- path: `/app/outputs/predicted_E_vs_porosity.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted effective Young's modulus as a function of porosity, averaged over three random realisations. The checker compares each row to hidden experimental reference values within a generous tolerance.
- schema:
  - `type`: table
  - `required_columns`: `porosity`, `predicted_youngs_modulus`
  - `units`:
    - `porosity`: %
    - `predicted_youngs_modulus`: MPa

Notes: The five porosity values are approximately 4.28%, 4.81%, 4.875%, 5.84%, 6.32% (exact values given in instruction.md). The hidden gold values are the experimental Young's modulus measurements from the source paper.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "predicted_E_vs_porosity.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "porosity",
          "predicted_youngs_modulus"
        ],
        "units": {
          "porosity": "%",
          "predicted_youngs_modulus": "MPa"
        }
      },
      "description": "Predicted effective Young's modulus as a function of porosity, averaged over three random realisations. The checker compares each row to hidden experimental reference values within a generous tolerance."
    }
  ],
  "notes": "The five porosity values are approximately 4.28%, 4.81%, 4.875%, 5.84%, 6.32% (exact values given in instruction.md). The hidden gold values are the experimental Young's modulus measurements from the source paper."
}
```

## How you are scored
A hidden verifier independently scores each workflow stage's output against reference criteria. For the scored artifact `predicted_E_vs_porosity.csv`, the verifier checks that the file has the correct format and compares the predicted moduli against hidden reference values (derived from the original study) within appropriate tolerances. The final reward is a weighted combination of all stage scores. Simply reporting numbers without running the described procedure is not sufficient; the submitted outputs must be the result of executing the workflow steps.
