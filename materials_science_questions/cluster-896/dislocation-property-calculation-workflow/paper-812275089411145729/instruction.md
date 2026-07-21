# Critical Radii and Coherent Elastic Energy of Nanowire Heterostructures

## Problem background
When a nanowire is grown epitaxially on a substrate of different lattice constant, the resulting mismatch strain can be accommodated by elastic deformation or by the formation of misfit dislocations. Because the nanowire has a free lateral surface, it can relax strain more effectively than a planar thin film, potentially allowing much larger coherent radii. The central quantity of interest is the critical underlayer radius: the radius below which a perfectly coherent interface is energetically preferred over an interface containing misfit dislocations. This task asks you to compute, for a given set of material parameters and lattice mismatches, the critical radii and a validation coherent elastic energy.

## Approach
We employ a variational approach that parallels the Matthews critical-thickness model for thin films. The displacement fields in the overlayer and underlayer are approximated by exponential-decay forms parameterized by variational parameters B, C, D, and a decay constant α. Strains and stresses are derived using isotropic linear elasticity (Lamé constants λ = μ = 60 GPa) and the strain energy density is integrated over the nanowire volumes to obtain a closed-form expression for the coherent elastic energy E_el. The stationary condition with respect to α is enforced analytically, leaving E_el as a function of B, C, D, which is then minimized numerically. The dislocation self-energy is added as the energy of a perpendicular edge dislocation pair (Burgers vector b = 0.23 nm, core factor β = 4, outer cutoff equal to the overlayer radius), and the residual mismatch after dislocation introduction is accounted for. For a given lattice mismatch f, the total energy of the coherent system E_0(R_u) and the dislocated system E_1(R_u) are computed as functions of the underlayer radius R_u. The critical radius R_u* is the solution of E_0 = E_1. The workflow also computes the minimized coherent elastic energy E_0* at a designated validation point (f = 0.01, R_u = 30 nm).

## Reproduction target
Compute the following two artifacts:

1. For each lattice mismatch f in {0.01, 0.02, 0.03}, determine the critical underlayer radius R_u* (in nm) where E_0(R_u) and E_1(R_u) intersect. Save the results as a CSV file with columns f and R_u_star.

2. At the validation point f = 0.01, R_u = 30 nm, compute the minimized coherent elastic energy E_0* (using the same material parameters). Save the result as a JSON object with keys f, R_u, and E0_star.

All outputs must be written to /app/outputs/ as specified in the workflow steps.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Implement variational model and energy functions
- Role: process
- Action: Implement the displacement ansatz for the overlayer and underlayer (radial and axial) as described in the paper. Derive strain and stress fields from kinematics and isotropic Hooke's law (equal Lamé constants λ=μ=60 GPa). Compute the strain energy density and integrate over the semi-infinite domains to obtain closed-form expressions for the coherent elastic energy E_el as a function of variational parameters B, C, D, and α. Derive the stationary condition for α and substitute to obtain E_el(B,C,D). Also implement the dislocation self-energy for a perpendicular edge dislocation pair (Burgers vector b=0.23 nm, core factor β=4, outer cutoff equal to overlayer radius). Package both the coherent energy minimization (over B,C,D) and the total energy functions E_0 and E_1 (coherent vs. dislocated) as callable functions of underlayer radius R_u and lattice mismatch f, with residual mismatch f_res when dislocated.
- Evidence: none

### Step 2: Compute critical radii
- Role: scored (load-bearing)
- Action: For each lattice mismatch f in {0.01, 0.02, 0.03}, use the implemented model to compute the total energy of the coherent system E_0(R_u) and the dislocated system E_1(R_u) as functions of underlayer radius R_u. Numerically solve for the radius R_u* where E_0 = E_1. Write the three pairs of (f, R_u_star) to a CSV file.
- Output file: `/app/outputs/critical_radii.csv`
- Format: csv
- Contract: Header columns: f (float, lattice mismatch), R_u_star (float, critical underlayer radius in nm). Exactly three data rows for f=0.01,0.02,0.03.
- Scoring: scored by hidden verifier

### Step 3: Compute validation coherent energy
- Role: scored (load-bearing)
- Action: Using the implemented model, compute the minimized coherent elastic energy E_0* for the specific parameters f=0.01 and R_u=30 nm. Write the result as a JSON object containing f, R_u, and E0_star.
- Output file: `/app/outputs/coherent_energy_validation.json`
- Format: json
- Contract: A JSON object with keys: 'f' (float, lattice mismatch), 'R_u' (float, underlayer radius in nm), 'E0_star' (float, minimized total coherent elastic energy).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/critical_radii.csv`
- `/app/outputs/coherent_energy_validation.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### critical_radii.csv
- path: `/app/outputs/critical_radii.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Critical underlayer radii for mismatches f=0.01,0.02,0.03. Scoring: hidden reference values compared with tolerances.
- schema:
  - `type`: table
  - `required_columns`: `f`, `R_u_star`
  - `units`:
    - `R_u_star`: nm

### coherent_energy_validation.json
- path: `/app/outputs/coherent_energy_validation.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Minimized coherent elastic energy at f=0.01, R_u=30 nm. Scoring: hidden reference value with relative tolerance.
- schema:
  - `type`: object
  - `required`:
    - `f`: float
    - `R_u`: float
    - `E0_star`: float
  - `units`:
    - `R_u`: nm
    - `E0_star`: energy per unit length (arbitrary unit; consistent with λ,μ in GPa and b in nm)

Notes: The checker compares R_u_star values to hidden references with tolerances (±0.5 nm or ±10%) and E0_star with ±2% relative error. Also verifies that R_u_star decreases monotonically with f and E0_star is positive. The planar thin-film comparison (Eq. 20) and finite element analysis (FEAP) are omitted as they are not required for the core reproduction target.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "critical_radii.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "f",
          "R_u_star"
        ],
        "units": {
          "R_u_star": "nm"
        }
      },
      "description": "Critical underlayer radii for mismatches f=0.01,0.02,0.03. Scoring: hidden reference values compared with tolerances."
    },
    {
      "file": "coherent_energy_validation.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": {
          "f": "float",
          "R_u": "float",
          "E0_star": "float"
        },
        "units": {
          "R_u": "nm",
          "E0_star": "energy per unit length (arbitrary unit; consistent with λ,μ in GPa and b in nm)"
        }
      },
      "description": "Minimized coherent elastic energy at f=0.01, R_u=30 nm. Scoring: hidden reference value with relative tolerance."
    }
  ],
  "notes": "The checker compares R_u_star values to hidden references with tolerances (±0.5 nm or ±10%) and E0_star with ±2% relative error. Also verifies that R_u_star decreases monotonically with f and E0_star is positive. The planar thin-film comparison (Eq. 20) and finite element analysis (FEAP) are omitted as they are not required for the core reproduction target."
}
```

## How you are scored
Your submission is evaluated by a hidden verifier that reads the two output files. For the critical radii, the verifier compares each R_u* value to a precomputed reference (produced by a trusted implementation of the same model). The verifier also checks that the critical radius decreases monotonically as the mismatch increases, and that the coherent energy E0_star is positive. For the validation energy, the comparison is performed similarly. The scores from each artifact are combined into a final reward between 0 and 1. The verifier’s tolerances and reference values are not disclosed; exact agreement with any particular published figure is not required—only that your implementation correctly captures the physics of the variational model.
