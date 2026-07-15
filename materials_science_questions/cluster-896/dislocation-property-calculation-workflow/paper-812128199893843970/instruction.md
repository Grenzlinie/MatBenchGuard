# Screened Wedge Disclination Elastic Field and Energy Computation

## Problem background
In plastically deformed metals, wedge disclinations are mesodefects that interact with surrounding edge dislocations. Understanding how the elastic field of a disclination is screened by a system of distributed dislocations is important for explaining the stability of broken dislocation boundaries and the reduction of elastic energy. This task models a wedge disclination coupled to an ensemble of edge dislocations within a self-consistent field approximation, analogous to Debye screening in a plasma. The goal is to compute the resulting spatial distributions of the excess dislocation density and the stress tensor, as well as the deformation energy, and to quantify the effect of screening.

## Approach
The approach treats the dislocation ensemble as a continuous charge distribution whose excess density is proportional to the effective interaction energy via an effective temperature parameter. Solving the self-consistent field equations in Fourier space yields an effective Airy stress function that incorporates screening. From this function, analytic expressions for the excess dislocation density I(x,y) and the stress tensor components σ_xx, σ_yy, σ_xy are derived in terms of the zero- and first-order modified Bessel functions (Macdonald functions). The elastic energy of the screened disclination is computed analytically and compared to the energy of an unscreened disclination as a function of a screening radius and a truncation radius. All computations use fixed physical parameters typical of deformed metals.

## Reproduction target
Implement the analytic formulas to compute the excess dislocation density I(x,y) and the three stress tensor components σ_xx, σ_yy, σ_xy on a two-dimensional spatial grid covering the region [-4 r_d, 4 r_d], where r_d is the screening radius derived from the given material and dislocation parameters. From the same parameters, compute the unscreened disclination energy, the screened energy, and their ratio. Output these fields and the energy values as specified in the workflow steps and output contract.

## Assets

- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Compute dislocation charge density and stress fields
- Role: scored
- Action: Using the physical parameters: shear modulus G = 5e10 Pa, Poisson ratio ν = 0.3, disclination power ω = 0.01, truncation radius R = 2e-6 m, Burgers vector b = 2.5e-10 m, background dislocation density ρ0 = 1e14 m⁻², effective temperature T_ext = 1.6e-9 J. Compute the elastic constant D = G/(2π(1-ν)). Compute the screening radius r_d = 1/√(π ρ0 b² D / T_ext) and the scaling factor I_c = ω/(π b r_d). Evaluate the excess dislocation density I(x,y) = I_c sinh(y/r_d) K₀(r/r_d) using the zero-order Macdonald function K₀. Compute the three stress components σ_xx, σ_yy, σ_xy from the analytic formulas involving K₀ and K₁ (first-order Macdonald function) and the coordinates, where r = √(x²+y²). Build a 2D grid covering x,y in [-4 r_d, 4 r_d] with at least 500×500 points. Save the arrays x, y, I, σ_xx, σ_yy, σ_xy and the parameters r_d, I_c, D, ω, b, R in step_01_fields.json.
- Output file: `/app/outputs/step_01_fields.json`
- Format: json
- Contract: JSON object with keys: "x" (1D float array), "y" (1D float array), "I" (2D float array, shape [len(y), len(x)]), "sigma_xx" (2D float array), "sigma_yy" (2D float array), "sigma_xy" (2D float array), "r_d" (float), "I_c" (float), "D" (float), "omega" (float), "b" (float), "R" (float).
- Scoring: scored by hidden verifier

### Step 2: Calculate elastic energy and screening ratio
- Role: scored
- Action: From the same physical parameters, compute the unscreened disclination energy W = D ω² R² / 8. Compute the screened energy using the analytic approximation W^Σ ≈ (√π/4) D ω² r_d² √(R/r_d). Calculate the ratio W^Σ / W. Save these three numbers in step_02_energy.json.
- Output file: `/app/outputs/step_02_energy.json`
- Format: json
- Contract: JSON object with keys: "W_unscreened" (float), "W_screened" (float), "ratio" (float).
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/step_01_fields.json`
- `/app/outputs/step_02_energy.json`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### step_01_fields.json
- path: `/app/outputs/step_01_fields.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Gridded field distributions of excess dislocation density and stress components, plus the derived screening parameters.
- schema:
  - `type`: object
  - `required`:
    - `x`: 1D float array
    - `y`: 1D float array
    - `I`: 2D float array (Ny × Nx)
    - `sigma_xx`: 2D float array
    - `sigma_yy`: 2D float array
    - `sigma_xy`: 2D float array
    - `r_d`: float
    - `I_c`: float
    - `D`: float
    - `omega`: float
    - `b`: float
    - `R`: float

### step_02_energy.json
- path: `/app/outputs/step_02_energy.json`
- format: json
- purpose: scored
- target_policy: metric_recompute
- description: Elastic energies of unscreened and screened disclination and their ratio.
- schema:
  - `type`: object
  - `required`:
    - `W_unscreened`: float
    - `W_screened`: float
    - `ratio`: float

Notes: All computations are based on the analytic expressions from the self-consistent field approximation; no external dataset is required.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "step_01_fields.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "x": "1D float array",
          "y": "1D float array",
          "I": "2D float array (Ny × Nx)",
          "sigma_xx": "2D float array",
          "sigma_yy": "2D float array",
          "sigma_xy": "2D float array",
          "r_d": "float",
          "I_c": "float",
          "D": "float",
          "omega": "float",
          "b": "float",
          "R": "float"
        }
      },
      "description": "Gridded field distributions of excess dislocation density and stress components, plus the derived screening parameters."
    },
    {
      "file": "step_02_energy.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "metric_recompute",
      "schema": {
        "type": "object",
        "required": {
          "W_unscreened": "float",
          "W_screened": "float",
          "ratio": "float"
        }
      },
      "description": "Elastic energies of unscreened and screened disclination and their ratio."
    }
  ],
  "notes": "All computations are based on the analytic expressions from the self-consistent field approximation; no external dataset is required."
}
```

## How you are scored
A hidden verifier reads your JSON artifacts. For the field distributions (step 1), it extracts the parameters you report, recomputes the expected I and stress components from the analytic formulas and compares them to your submitted arrays using a relative tolerance. For the energy (step 2), it recomputes the energies from the same formulas and checks the ratio against a reference. The verifier also checks that the reported fields and parameters are self-consistent. The final reward is a weighted combination of the scores from the two stages; reporting the correct value from the paper is not sufficient—you must produce artifacts that pass the recomputation checks.
