# Nonlinear Vibration of FG-CNTR Sandwich Beams on Pasternak Foundation

## Problem background
This task addresses the nonlinear free vibration of sandwich beams composed of a homogeneous core and two face sheets reinforced by functionally graded carbon nanotubes (CNTs). The beams rest on a two-parameter Pasternak elastic foundation (Winkler modulus and shear layer). CNTs can agglomerate into clusters, and the effective properties of the nanocomposite depend on the degree of aggregation. You will compute how the CNT volume fraction profile, aggregation parameters, foundation stiffness, core-to-face-sheet thickness ratio, and boundary conditions affect the dimensionless linear and nonlinear natural frequencies of such Timoshenko beams.

## Approach
You will build a computational pipeline based on the following three stages:

1. **Homogenization** – Use the Eshelby–Mori–Tanaka method including two-parameter CNT aggregation to compute the through-thickness distributions of effective Young’s modulus, Poisson’s ratio, and density for the face sheets. CNT volume fraction in the face sheets follows a power-law profile; the core has a uniform CNT volume fraction. The inputs are material properties of the SWCNT reinforcement and the PMMA matrix, the power-law exponent q, the volume fractions Vi and Vo, and the aggregation parameters μ and η.

2. **Stiffness and inertia integration** – Integrate the profiles over the entire beam thickness to obtain the extensional, coupling, bending, and shear stiffness resultants (A11, B11, D11, A55) and the inertia resultants (I1, I2, I3). Also compute the reference values A110 and I10 for a homogeneous PMMA beam, which are used later to non-dimensionalise the equations.

3. **GDQ discretisation and iterative nonlinear solver** – Discretise the dimensionless nonlinear governing equations for a Timoshenko beam (including von Kármán geometric nonlinearity and the Pasternak foundation) using the Generalised Differential Quadrature method. Assemble the mass and stiffness matrices, apply boundary conditions (clamped and hinged supports), and solve the resulting nonlinear eigenvalue problem with a direct iterative algorithm. For a given vibration amplitude (maximum dimensionless transverse displacement), the procedure yields the dimensionless linear frequency ωₗ and nonlinear frequency ωₙₗ.

Pipeline steps 4 and 5 (see Workflow steps) use this core solver to produce the required scored CSV files for the specified parameter sets.

## Reproduction target
Your goal is to produce two CSV files under `/app/outputs` that capture the key quantitative behaviour of the beam system.

1. **Frequency table for different configurations** – For a fixed length-to-thickness ratio L/h=10 and CNT volume fractions Vi=0.05, Vo=0.1 with aggregation parameters η=0.4, μ=0.4, compute the dimensionless linear frequency ωₗ and nonlinear frequency ωₙₗ for the following parameter combinations:
   - Boundary conditions: clamped–clamped (C‑C), hinged–hinged (H‑H), clamped–hinged (C‑H).
   - Foundation coefficients (k_w, k_s): (0,0), (0.1,0), (0.1,0.2).
   - Core-to-face-sheet thickness ratio hc/hf = 2, 4.
   - Power-law exponent q = 1, 100.
   - Vibration amplitudes w_max = 0.1, 0.3, 0.5.
   Write one row per combination; columns: `boundary_condition, hc_hf, kw, ks, q, w_max, omega_l, omega_nl`.

2. **Effect of CNT aggregation on frequency ratio** – For a fixed beam with C‑C ends, L/h=15, q=1, Vi=0, Vo=0.05, and no foundation (k_w=k_s=0), compute ωₗ, ωₙₗ, and the nonlinear-to-linear frequency ratio ωₙₗ/ωₗ at amplitudes w_max = 0, 0.1, 0.2, 0.3, 0.4, 0.5 for two aggregation states:
   - fully dispersed: η=0.4, μ=0.4
   - clustered: η=0.4, μ=0.1
   Output a CSV with columns: `eta, mu, w_max, omega_l, omega_nl, ratio`.

Your outputs will be checked against hidden reference values for the same quantities; do not try to match an external table – just implement the pipeline correctly.

## Assets

- NumPy
- SciPy
- Material properties for SWCNT and PMMA

## Workflow steps

### Step 1: Micromechanical homogenization with CNT aggregation
- Role: process
- Action: Implement the Eshelby-Mori-Tanaka homogenization method accounting for CNT aggregation to compute through-thickness distributions of effective Young's modulus E(z), Poisson's ratio ν(z), and density ρ(z) for given CNT volume fractions and aggregation parameters. Use the power-law volume fraction profile for the face sheets.
- Evidence: none

### Step 2: Stiffness and inertia resultants
- Role: process
- Action: Integrate the homogenized material profiles through the beam thickness to obtain stiffness resultants (A11, B11, D11, A55) and inertia resultants (I1, I2, I3). Also compute the reference values A110 and I10 for a homogeneous PMMA beam for normalization.
- Evidence: none

### Step 3: GDQ discretization and iterative nonlinear solver
- Role: process
- Action: Implement the Generalized Differential Quadrature (GDQ) discretization of the dimensionless nonlinear governing equations (Timoshenko beam with von Kármán nonlinearity, Pasternak foundation). Assemble mass and stiffness matrices, apply boundary conditions, and solve the nonlinear eigenvalue problem using a direct iterative method to obtain dimensionless linear and nonlinear frequencies for given parameters.
- Evidence: none

### Step 4: Linear and nonlinear frequencies for sandwich beams
- Role: scored (load-bearing)
- Action: Using the implemented pipeline (homogenization, integration, GDQ solver), compute linear (omega_l) and nonlinear (omega_nl) dimensionless frequencies for a set of configurations: boundary conditions (C-C, H-H, C-H), foundation parameters (kw,ks) = (0,0), (0.1,0), (0.1,0.2), core-to-face-sheet thickness ratio hc/hf = 2, 4, power-law exponents q = 1, 100, and vibration amplitudes w_max = 0.1, 0.3, 0.5. Use the material properties and aggregation parameters as specified (CNT volume fractions Vi=0.05, Vo=0.1, η=0.4, μ=0.4, L/h=10). Output a CSV file with one row per configuration containing the boundary condition, hc/hf, kw, ks, q, w_max, omega_l, and omega_nl.
- Output file: `/app/outputs/linear_and_nonlinear_frequencies.csv`
- Format: csv
- Contract: boundary_condition (string), hc_hf (float), kw (float), ks (float), q (float or int), w_max (float), omega_l (float), omega_nl (float)
- Scoring: scored by hidden verifier

### Step 5: Effect of CNT aggregation state on frequency ratio
- Role: scored
- Action: For a fixed beam configuration (C-C boundary, L/h=15, q=1, Vi=0, Vo=0.05, no foundation) and two CNT aggregation states — fully dispersed (η=0.4, μ=0.4) and clustered (η=0.4, μ=0.1) — compute the linear frequency omega_l, nonlinear frequency omega_nl, and nonlinear-to-linear frequency ratio at several vibration amplitudes w_max (e.g., 0, 0.1, 0.2, 0.3, 0.4, 0.5). Output a CSV with columns eta, mu, w_max, omega_l, omega_nl, and ratio. The file must contain rows for both aggregation states at each amplitude.
- Output file: `/app/outputs/aggregation_effect.csv`
- Format: csv
- Contract: eta (float), mu (float), w_max (float), omega_l (float), omega_nl (float), ratio (float, omega_nl/omega_l)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/linear_and_nonlinear_frequencies.csv`
- `/app/outputs/aggregation_effect.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### linear_and_nonlinear_frequencies.csv
- path: `/app/outputs/linear_and_nonlinear_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed dimensionless linear and nonlinear frequencies for specified configurations. The checker compares omega_l and omega_nl to hidden reference values from the paper with appropriate tolerances.
- schema:
  - `type`: table
  - `required_columns`: `boundary_condition`, `hc_hf`, `kw`, `ks`, `q`, `w_max`, `omega_l`, `omega_nl`
  - `description`: Columns: boundary_condition (string), rest are float.

### aggregation_effect.csv
- path: `/app/outputs/aggregation_effect.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Computed linear and nonlinear frequencies and ratio for two aggregation states at various amplitudes. The checker verifies both absolute values and expected trends (e.g., fully dispersed state yields higher linear frequency and lower frequency ratio).
- schema:
  - `type`: table
  - `required_columns`: `eta`, `mu`, `w_max`, `omega_l`, `omega_nl`, `ratio`
  - `description`: All columns are float. Ratio = omega_nl/omega_l.

Notes: Both output files must be produced under /app/outputs. The checker will compare frequencies to paper-reported values and validate monotonic trends. Partial credit may be awarded for correct trends even if absolute values deviate.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "linear_and_nonlinear_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "boundary_condition",
          "hc_hf",
          "kw",
          "ks",
          "q",
          "w_max",
          "omega_l",
          "omega_nl"
        ],
        "description": "Columns: boundary_condition (string), rest are float."
      },
      "description": "Computed dimensionless linear and nonlinear frequencies for specified configurations. The checker compares omega_l and omega_nl to hidden reference values from the paper with appropriate tolerances."
    },
    {
      "file": "aggregation_effect.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "eta",
          "mu",
          "w_max",
          "omega_l",
          "omega_nl",
          "ratio"
        ],
        "description": "All columns are float. Ratio = omega_nl/omega_l."
      },
      "description": "Computed linear and nonlinear frequencies and ratio for two aggregation states at various amplitudes. The checker verifies both absolute values and expected trends (e.g., fully dispersed state yields higher linear frequency and lower frequency ratio)."
    }
  ],
  "notes": "Both output files must be produced under /app/outputs. The checker will compare frequencies to paper-reported values and validate monotonic trends. Partial credit may be awarded for correct trends even if absolute values deviate."
}
```

## How you are scored
A hidden verifier will independently score each of the two CSV files. It reads your submitted outputs and compares the computed frequencies to hidden reference values derived from the paper, using relative tolerances that account for numerical differences (different code, grid, solver tolerance). The verifier also checks expected monotonic trends: for the aggregation file, it verifies that the fully dispersed state gives a higher linear frequency and a lower frequency ratio than the clustered state at every amplitude. If your results are correct within the tolerances and exhibit the required trends, you will receive full credit; partial credit is awarded for correct trends even if absolute values deviate. The final reward is a weighted combination of the scores from both artefacts, with the frequency table carrying the main weight. Reporting the paper’s numbers without a correct pipeline will not pass because the verifier will detect systematic mismatches.
