# Defect free energy of cylindrical diblock copolymers in confined channels with variable top/bottom wall wetting

## Problem background
Directed self-assembly (DSA) of cylinder-forming diblock copolymers is a promising nanolithography technique, but defect formation limits pattern quality. Self-consistent field theory (SCFT) provides a mean-field framework to compute the free energy of polymer morphologies and quantify defect thermodynamics. This work considers a monolayer of cylinders confined in a thin channel, with sidewalls that attract the minority block. The top and bottom surfaces are given an adjustable affinity for the majority block. The key quantity of interest is the free energy cost to form a dislocation defect relative to the perfect cylindrical phase, as a function of the majority-block attraction strength on the top/bottom walls (denoted χ_Wall). Your task is to compute this defect free energy across a range of χ_Wall values.

## Approach
The system is modeled as an incompressible melt of AB diblock copolymers described by the standard Gaussian chain model, with a Flory-type monomer-monomer interaction parameter χ and monomer-wall interaction parameters χ_wall. The SCFT equations are solved iteratively to obtain the self-consistent fields and the segment density distributions. The simulation cell is a thin rectangular channel that is periodic along the cylinder axis (x) and the width (y), with hard, impenetrable walls at the top and bottom (z). The sidewalls (y boundaries) are made strongly attractive to the minor block (fixed high χ_wall). The top and bottom walls are attractive to the major block with a tunable interaction strength χ_Wall that is swept over a set of values. For each χ_Wall, both a perfect cylindrical reference state and a dislocation-defect state are relaxed to the mean-field saddle point, and their free energies F_perfect and F_defect are recorded. The defect free energy is then ΔF = F_defect − F_perfect, expressed in units of kT. You may implement your own SCFT solver or use an open-source library.

## Reproduction target
For the simulation parameters χN=30, minority block fraction f_A=0.258, channel width 21.0 R_g, channel depth 3.75 R_g, sidewalls fixed strong minor-block wetting, and top/bottom wall variable χ_Wall values of 0, 10, 20, 30, 40, 42, 44, 50, and 64, perform SCFT calculations to obtain the free energy of the perfect cylinder reference and a dislocation-defect configuration for each χ_Wall. Compute the defect free energy ΔF = F_defect − F_perfect in units of kT. Output the results as a CSV file containing exactly those χ_Wall values and the corresponding ΔF values. You are not given the expected answer; you must produce it through the simulation.

## Assets

- Self-Consistent Field Theory (SCFT) simulation code

## Workflow steps

### Step 1: Compute dislocation defect free energy vs χ_Wall
- Role: scored (load-bearing)
- Action: Set up a 3D SCFT simulation for a melt of AB diblock copolymers in a thin channel with periodic boundary conditions along the cylinder axis (x) and width (y), and walls at z boundaries. Use the Gaussian chain model and Flory-type monomer-monomer (χ) and monomer-wall (χ_Wall) interactions. Parameters: χN=30, minor block volume fraction f_A=0.258, channel width Ly=21.0 R_g, channel depth Lz=3.75 R_g, sidewalls minor-block attractive (fixed high χ_Wall), top/bottom walls major-block attractive with variable χ_Wall taking values 0, 10, 20, 30, 40, 42, 44, 50, 64. For each χ_Wall, compute the free energy of the perfect cylindrical reference state and a dislocation-defect state; obtain ΔF = F_defect - F_perfect in kT. Output the results as a CSV file.
- Output file: `/app/outputs/defect_free_energy_vs_chiWall.csv`
- Format: csv
- Contract: CSV with header: chi_Wall,defect_free_energy_kT. Each row contains one χ_Wall value and its corresponding defect free energy.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/defect_free_energy_vs_chiWall.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### defect_free_energy_vs_chiWall.csv
- path: `/app/outputs/defect_free_energy_vs_chiWall.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Dislocation defect free energy as a function of the top/bottom wall interaction parameter χ_Wall. The CSV must contain exactly one row per χ_Wall value from the set {0,10,20,30,40,42,44,50,64}, with the free energy in kT.
- schema:
  - `type`: table
  - `required_columns`: `chi_Wall`, `defect_free_energy_kT`
  - `units`:
    - `chi_Wall`: dimensionless
    - `defect_free_energy_kT`: kT

Notes: The checker will verify the reported CSV for structural trends: a monotonic increase to a maximum near χ_Wall=42, a plateau for χ_Wall≥44, and approximate amplitudes of the rise and plateau as described in the problem background. No gold numerical values are disclosed in this contract; the agent's result is judged against hidden criteria derived from the paper's reported findings.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "defect_free_energy_vs_chiWall.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "chi_Wall",
          "defect_free_energy_kT"
        ],
        "units": {
          "chi_Wall": "dimensionless",
          "defect_free_energy_kT": "kT"
        }
      },
      "description": "Dislocation defect free energy as a function of the top/bottom wall interaction parameter χ_Wall. The CSV must contain exactly one row per χ_Wall value from the set {0,10,20,30,40,42,44,50,64}, with the free energy in kT."
    }
  ],
  "notes": "The checker will verify the reported CSV for structural trends: a monotonic increase to a maximum near χ_Wall=42, a plateau for χ_Wall≥44, and approximate amplitudes of the rise and plateau as described in the problem background. No gold numerical values are disclosed in this contract; the agent's result is judged against hidden criteria derived from the paper's reported findings."
}
```

## How you are scored
Your submission will be evaluated by a hidden automated checker. The checker reads the CSV file you produce and compares the ΔF values against reference targets derived from the paper's published findings, using tolerances appropriate for numerical SCFT computations. It also verifies that the overall shape of the ΔF vs χ_Wall curve shows the expected physical behavior. You are not provided with the reference values; you must obtain them by performing honest SCFT simulations. A result that is fabricated, or one obtained without proper convergence, will almost certainly fail these checks. Each scored workflow step contributes a weighted share to the final reward; for this task the CSV from the single scored step determines your score.
