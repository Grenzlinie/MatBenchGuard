# Empirical linear electrostrictive coefficient prediction

## Problem background
The quadratic electrostrictive coefficients d1111, d1122, d1212 of NaCl‑type alkali halide crystals are required to evaluate the electrostrictive‑elastooptic contribution to the quadratic electrooptic effect. Experimental values exist for ten crystals (LiF, NaF, NaCl, NaBr, KCl, KBr, KI, RbCl, RbBr, RbI) but are not available for five others (LiCl, LiBr, NaI, KF, RbF). This work explores an empirical connection between these coefficients and the relative change in the bond length (Q/d) induced by an applied electric field in order to estimate the missing coefficients. The central quantity to compute is (Q/d)², derived from the material's dielectric constants, heteropolar band gap, and lattice parameter, assuming a uniform electric field.

## Approach
The approach relies on two ideas. (1) For a NaCl‑type crystal, the relative bond‑length change Q/d caused by a low‑frequency electric field can be calculated from the static and high‑frequency dielectric constants ε(0) and ε(∞), the lattice constant a, and the heteropolar band gap C, via the Szigeti effective charge formula. (2) The electrostrictive coefficients d1111, d1122, d1212 may be linearly related to (Q/d)². The workflow therefore (a) assembles the experimental d_ijkl for the ten training crystals together with their material constants; (b) computes Q/d for each (using E = 1 V m⁻¹); (c) performs ordinary least‑squares fits of the form d = slope · (Q/d)² + intercept for each coefficient; (d) computes Q/d for the five target crystals using the same material‑constant sources; and (e) applies the fitted relations to predict the missing coefficients. The method is entirely computational and uses only publicly available material parameters.

## Reproduction target
Compute (Q/d)² for the ten training alkali halides and for the five target crystals (LiCl, LiBr, NaI, KF, RbF) using the formulas and material constants from published sources: static and high‑frequency dielectric constants (Lowndes & Martin), the heteropolar band gap C (Levine), and the lattice constant a (Landolt‑Börnstein). Using the experimental d1111, d1122, d1212 values for the ten training crystals (with averaging where multiple datasets exist), perform ordinary least‑squares fits to obtain linear coefficients linking each d_ijkl to (Q/d)². Output the fitted slopes and intercepts for later verification. Then apply these linear relations to the computed (Q/d)² values of LiCl, LiBr, NaI, KF, RbF to predict their quadratic electrostrictive coefficients. The predicted values must be reported in units of 10⁻²⁰ m² V⁻². All numerical work assumes a driving electric field of E = 1 V m⁻¹.

## Assets

- Experimental electrostrictive coefficients d1111, d1122, d1212 for ten NaCl-type alkali halides
- Dielectric constants, heteropolar band gap, and lattice constant for alkali halides

## Workflow steps

### Step 1: Assemble training data
- Role: process
- Action: Collect the experimental electrostrictive coefficients d1111, d1122, d1212 for ten NaCl-type alkali halides (LiF, NaF, NaCl, NaBr, KCl, KBr, KI, RbCl, RbBr, RbI) from Bohatý and Haussühl (1977), average values for LiF and NaCl where multiple datasets exist, discarding outliers as per the paper. Also collect the material constants: static and high-frequency dielectric constants (ε(0), ε(∞)) from Lowndes and Martin (1969), the heteropolar band gap C from Levine (1973), and the lattice constant a from Landolt-Börnstein (1973).
- Evidence: `/app/outputs/training_data.csv`

### Step 2: Compute relative bond change (Q/d) for training crystals
- Role: process
- Action: For each training crystal, use the following physical constants: ε₀ = 8.854187817 × 10⁻¹² F m⁻¹, e = 1.602176634 × 10⁻¹⁹ C, ħ = 1.054571817 × 10⁻³⁴ J s, m = 9.10938356 × 10⁻³¹ kg, eV = 1.602176634 × 10⁻¹⁹ J. Convert the material constants to SI units: a (Å) → a_SI = a × 10⁻¹⁰ m; C (eV) → C_SI = C × eV. Compute:
- Plasma frequency: ω_p² = (32 e²) / (ε₀ m a_SI³)
- Szigeti effective charge: e_s = (e C_SI) / (ħ ω_p)   [in units of C; divide by e to get dimensionless e_s′ = e_s/e if needed, but Eq. (3) uses e_s in C]
- Relative bond‑length change: Q/d = [3 ε₀ (ε(0) − ε(∞)) ε(∞) a_SI³ E] / [4 e_s (ε(∞) + 2)], with E = 1 V m⁻¹.
Output (Q/d) and (Q/d)² for each crystal. All computations in SI; the resulting Q/d is dimensionless.
- Evidence: `/app/outputs/q_over_d_train.csv`

### Step 3: Fit empirical linear relations
- Role: scored (load-bearing)
- Action: Perform ordinary least-squares regression of experimental d1111, d1122, d1212 (from step 1) against (Q/d)^2 (from step 2) to obtain the slopes and intercepts for the linear relations d = slope * (Q/d)^2 + intercept.
- Output file: `/app/outputs/regression_coefficients.csv`
- Format: csv
- Contract: Header: coefficient_type,slope,intercept. All values in scientific notation. Slopes are in 10^{-20} m^2 V^{-2} per dimensionless (Q/d)^2, intercepts in 10^{-20} m^2 V^{-2}.
- Scoring: scored by hidden verifier

### Step 4: Predict electrostrictive coefficients for target crystals
- Role: scored (load-bearing)
- Action: Assemble ε(0), ε(∞), C, a for LiCl, LiBr, NaI, KF, RbF from the same literature sources. Compute Q/d for each target crystal using the exact same equations and physical constants as in Step 2: convert a to m, C to J; compute ω_p² = 32 e²/(ε₀ m a³), e_s = e C_J/(ħ ω_p), then Q/d = [3 ε₀ (ε(0)−ε(∞)) ε(∞) a³ E] / [4 e_s (ε(∞)+2)] with E = 1 V m⁻¹. Compute (Q/d)². Apply the linear relations from step 3: d1111 = slope_d1111 × (Q/d)² + intercept_d1111, etc., to predict d1111, d1122, d1212 for each crystal.
- Output file: `/app/outputs/predicted_coefficients.csv`
- Format: csv
- Contract: Header: crystal,d1111,d1122,d1212. All values in scientific notation, units 10^{-20} m^2 V^{-2}.
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/regression_coefficients.csv`
- `/app/outputs/predicted_coefficients.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### regression_coefficients.csv
- path: `/app/outputs/regression_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Linear model parameters for d1111, d1122, d1212 as functions of (Q/d)^2.
- schema:
  - `type`: table
  - `required_columns`: `coefficient_type`, `slope`, `intercept`
  - `units`:
    - `slope`: 10^{-20} m^2 V^{-2} per (Q/d)^2
    - `intercept`: 10^{-20} m^2 V^{-2}

### predicted_coefficients.csv
- path: `/app/outputs/predicted_coefficients.csv`
- format: csv
- purpose: scored
- target_policy: reference_match
- description: Predicted quadratic electrostrictive coefficients for LiCl, LiBr, NaI, KF, RbF.
- schema:
  - `type`: table
  - `required_columns`: `crystal`, `d1111`, `d1122`, `d1212`
  - `units`:
    - `d1111`: 10^{-20} m^2 V^{-2}
    - `d1122`: 10^{-20} m^2 V^{-2}
    - `d1212`: 10^{-20} m^2 V^{-2}

Notes: The checker will compare slopes/intercepts and predicted coefficients to the paper's reported values using appropriate tolerances.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "regression_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "coefficient_type",
          "slope",
          "intercept"
        ],
        "units": {
          "slope": "10^{-20} m^2 V^{-2} per (Q/d)^2",
          "intercept": "10^{-20} m^2 V^{-2}"
        }
      },
      "description": "Linear model parameters for d1111, d1122, d1212 as functions of (Q/d)^2."
    },
    {
      "file": "predicted_coefficients.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "table",
        "required_columns": [
          "crystal",
          "d1111",
          "d1122",
          "d1212"
        ],
        "units": {
          "d1111": "10^{-20} m^2 V^{-2}",
          "d1122": "10^{-20} m^2 V^{-2}",
          "d1212": "10^{-20} m^2 V^{-2}"
        }
      },
      "description": "Predicted quadratic electrostrictive coefficients for LiCl, LiBr, NaI, KF, RbF."
    }
  ],
  "notes": "The checker will compare slopes/intercepts and predicted coefficients to the paper's reported values using appropriate tolerances."
}
```

## How you are scored
A hidden verifier independently checks each required artifact. For `regression_coefficients.csv`, it compares the slope and intercept of each fitted line to a hidden reference that is consistent with the data and method; small numerical differences arising from the implementation are accepted within a tolerance. For `predicted_coefficients.csv`, it compares the predicted d1111, d1122, d1212 values for LiCl, LiBr, NaI, KF, RbF against a hidden gold standard derived from the original study. The verifier also validates file format, expected column names, and data types. The two checks are weighted and combined into a final score between 0 and 1. Reporting numbers that match the literature is not sufficient; the workflow steps must produce the results from the described computations.
