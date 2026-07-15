# Phonon dispersion and force-constant fitting using the D²I³ lattice-dynamics model

## Problem background
The lattice dynamics of ionic crystals—how the atoms vibrate collectively—determine many of their basic physical properties, from thermal conductivity to infrared spectra. For rocksalt-structure crystals such as alkali halides and silver bromide, a successful model must account not only for the long-range Coulomb forces between ions but also for short-range pairwise interactions and many‑body effects. In particular, it has been hypothesized that certain ions, like Ag⁺, are particularly “deformable,” giving rise to large three‑body forces that alter the phonon dispersion in ways not captured by simpler models. The deformation‑dipole-indirect‑ionic‑interaction (D²I³) model incorporates deformation dipoles (short‑range polarization of nearby ions) together with an exact parametrization of the three‑body forces acting between two ions via a common polarizable neighbor. The model yields a dynamical matrix that depends on a limited set of renormalized short‑range force constants. By fitting these constants to experimental neutron‑scattering phonon frequencies for KCl, KBr, RbCl, and AgBr, one can extract numerical values for the three‑body interactions and assess whether they are indeed large for the deformable Ag⁺ ion. The task is to implement the D²I³ model, perform the weighted least‑squares fit, and produce the fitted parameters and the computed phonon frequencies at the measured wavevectors.

## Approach
The D²I³ londsale dynamical matrix is built from several contributions: (i) a long‑range dipolar part that includes the deformation‑dipole renormalization to avoid double counting, expressed in terms of the semiempirical ionic polarizabilities; (ii) short‑range central forces between first‑neighbor ions; and (iii) the indirect ionic interaction (I³) tensor, which describes the forces between two ions that share a common polarizable first neighbor. After subtracting the dipolar and deformation‑dipole parts that are already accounted for, the renormalized I³ parameters are introduced. The structure of the rocksalt lattice reduces the 6×6 short‑range dynamical matrix to a form governed by only 12 independent combinations of the physical parameters. The acoustic‑sum rule provides one additional constraint.

The experimental input consists of published neutron‑scattering phonon frequencies, each with an uncertainty, for the four materials (KCl, KBr, RbCl, AgBr) at sets of wavevectors along the principal symmetry directions. The fixed physical constants—semiempirical ionic polarizabilities, lattice constants, and ion masses—are taken from standard literature sources.

A weighted chi‑squared function quantifies the agreement between the model frequencies and the experimental data. An iterative parameter‑addition procedure is used: starting from a minimal set of the largest‑expected parameters, additional parameters are added one at a time, based on their ability to reduce chi‑squared, and the whole parameter set is re‑optimized at each stage. Parameters that never significantly reduce chi‑squared are set to zero. The outcome is a set of best‑fit short‑range force constants for each material, expressed in units of e² per unit‑cell volume, together with the model phonon frequencies at the exact wavevectors and branches of the experimental data. The entire pipeline—from reading experimental data, through constructing the dynamical matrix and performing the least‑squares fit, to outputting the final frequencies—must be implemented.

## Reproduction target
Your objective is to produce two scored artifacts:

1. **Fitted D²I³ parameters** — a JSON file (`fitted_parameters.json`) containing, for each of the four materials (KCl, KBr, RbCl, AgBr), the 15 short‑range force constants that result from the weighted least‑squares fit. The constants are specified in the output contract and include the central‑force parameters A+− and B+−, the renormalized deformation‑dipole components γ_l and γ_t for cation and anion, and the renormalized I³ parameters g₁, g₂, g₄, h₁, h₂ for both ions. Parameters that the fit procedure determines to be negligible must appear as 0.0.

2. **Computed phonon frequencies** — a CSV file (`computed_phonon_frequencies.csv`) with one row per experimental data point. Each row gives the material name, the reduced wavevector coordinates (qₓ, qᵧ, q𝓏), the phonon branch label (LA, TA, LO, or TO), the model frequency in THz obtained from the best‑fit parameters, and the experimental uncertainty in THz (copied from the input data).

The verifier holds independent (hidden) copies of the experimental neutron‑scattering data and of the reference fitted parameters. It will recompute a weighted chi‑squared goodness‑of‑fit from your computed frequencies and compare your fitted parameters to the reference values. The correctness of your fit is assessed solely through these two artifacts.

## Assets

- KCl phonon frequencies: 10.1002/pssb.19690330123
- KBr phonon frequencies: 10.1103/PhysRev.131.1025
- RbCl phonon frequencies: 10.1088/0022-3719/3/5/015
- AgBr phonon frequencies: 10.1103/PhysRevB.15.385
- Ionic polarizabilities: 10.1098/rspa.1969.0018
- Lattice constants and ion masses
- NumPy: numpy
- SciPy: scipy

## Workflow steps

### Step 1: Data preparation
- Role: process
- Action: Collect the fixed physical parameters (semiempirical polarizabilities, lattice constants, ion masses) from public literature. Obtain the experimental phonon frequencies and uncertainties for KCl, KBr, RbCl, and AgBr from the specified neutron-scattering references. Compile a clean dataset of q‑points, measured frequencies, error bars, and branch labels for each material.
- Evidence: `/app/outputs/compiled_experimental_data.csv`

### Step 2: D²I³ dynamical matrix implementation
- Role: process
- Action: Implement the D²I³ lattice-dynamics model in Python. Build the long-range dipolar + deformation-dipole part, the renormalized I³ three-body force contribution, and the short-range central-force + constraint matrices for the rocksalt structure (6×6 dynamical matrix). Enforce the acoustic-sum rule and reduce the parameter set to the 12 independent short-range coefficients.
- Evidence: none

### Step 3: Least-squares fit of D²I³ parameters
- Role: scored
- Action: Using the compiled experimental data and the D²I³ model implementation, perform a weighted least-squares fit minimizing χ² for each material separately, following an iterative parameter‑addition procedure. Output the final set of fitted short-range force constants for KCl, KBr, RbCl, and AgBr in a JSON file.
- Output file: `/app/outputs/fitted_parameters.json`
- Format: json
- Contract: {
  "KCl": { "A_+-": float, "B_+-": float, "gamma_l_plus": float, "gamma_t_plus": float, "gamma_l_minus": float, "gamma_t_minus": float, "g1_plus": float, "g2_plus": float, "g4_plus": float, "h1_plus": float, "h2_plus": float, "g1_minus": float, "g2_minus": float, "h1_minus": float, "h2_minus": float },
  "KBr": { ... },
  "RbCl": { ... },
  "AgBr": { ... }
}
- Scoring: scored by hidden verifier

### Step 4: Compute phonon frequencies at experimental q‑points
- Role: scored (load-bearing)
- Action: Using the best-fit D²I³ parameters from the previous step, compute the phonon frequencies at the exact q‑points and branches of the experimental data for each material. Write a CSV file containing the q‑coordinates, branch, computed frequency, and the experimental error for every measured point.
- Output file: `/app/outputs/computed_phonon_frequencies.csv`
- Format: csv
- Contract: columns: material (string), qx (float), qy (float), qz (float), branch (string), frequency_THz (float), error_THz (float)
- Scoring: scored by hidden verifier

## Output files
Write all artifacts under `/app/outputs`:
- `/app/outputs/fitted_parameters.json`
- `/app/outputs/computed_phonon_frequencies.csv`

## Output contract

Every file the hidden verifier reads is described below. Write each file under `/app/outputs` and follow its schema exactly.

### fitted_parameters.json
- path: `/app/outputs/fitted_parameters.json`
- format: json
- purpose: scored
- target_policy: reference_match
- description: Fitted D²I³ short-range force constants for KCl, KBr, RbCl, and AgBr in units of e²/V₀, structured as in the paper's Table IV.
- schema:
  - `type`: object
  - `required`: `KCl`, `KBr`, `RbCl`, `AgBr`
  - `properties`:
    - `KCl`:
      - `type`: object
      - `required`: `A_+-`, `B_+-`, `gamma_l_plus`, `gamma_t_plus`, `gamma_l_minus`, `gamma_t_minus`, `g1_plus`, `g2_plus`, `g4_plus`, `h1_plus`, `h2_plus`, `g1_minus`, `g2_minus`, `h1_minus`, `h2_minus`
      - `additionalProperties`: False
      - `properties`:
        - `A_+-`:
          - `type`: number
        - `B_+-`:
          - `type`: number
        - `gamma_l_plus`:
          - `type`: number
        - `gamma_t_plus`:
          - `type`: number
        - `gamma_l_minus`:
          - `type`: number
        - `gamma_t_minus`:
          - `type`: number
        - `g1_plus`:
          - `type`: number
        - `g2_plus`:
          - `type`: number
        - `g4_plus`:
          - `type`: number
        - `h1_plus`:
          - `type`: number
        - `h2_plus`:
          - `type`: number
        - `g1_minus`:
          - `type`: number
        - `g2_minus`:
          - `type`: number
        - `h1_minus`:
          - `type`: number
        - `h2_minus`:
          - `type`: number
    - `KBr`:
      - `type`: object
      - `required`: `A_+-`, `B_+-`, `gamma_l_plus`, `gamma_t_plus`, `gamma_l_minus`, `gamma_t_minus`, `g1_plus`, `g2_plus`, `g4_plus`, `h1_plus`, `h2_plus`, `g1_minus`, `g2_minus`, `h1_minus`, `h2_minus`
      - `additionalProperties`: False
    - `RbCl`:
      - `type`: object
      - `required`: `A_+-`, `B_+-`, `gamma_l_plus`, `gamma_t_plus`, `gamma_l_minus`, `gamma_t_minus`, `g1_plus`, `g2_plus`, `g4_plus`, `h1_plus`, `h2_plus`, `g1_minus`, `g2_minus`, `h1_minus`, `h2_minus`
      - `additionalProperties`: False
    - `AgBr`:
      - `type`: object
      - `required`: `A_+-`, `B_+-`, `gamma_l_plus`, `gamma_t_plus`, `gamma_l_minus`, `gamma_t_minus`, `g1_plus`, `g2_plus`, `g4_plus`, `h1_plus`, `h2_plus`, `g1_minus`, `g2_minus`, `h1_minus`, `h2_minus`
      - `additionalProperties`: False

### computed_phonon_frequencies.csv
- path: `/app/outputs/computed_phonon_frequencies.csv`
- format: csv
- purpose: scored
- target_policy: structural_audit
- description: Computed phonon frequencies at the experimental q‑points. The verifier performs a structural audit: required columns are present, frequencies are nonnegative, errors are nonnegative, and branch labels belong to {LA, TA, LO, TO}.
- schema:
  - `type`: table
  - `required_columns`: `material`, `qx`, `qy`, `qz`, `branch`, `frequency_THz`, `error_THz`
  - `columns`:
    - `material`: string
    - `qx`: float (reduced coordinate)
    - `qy`: float (reduced coordinate)
    - `qz`: float (reduced coordinate)
    - `branch`: string (LA, TA, LO, TO)
    - `frequency_THz`: float (THz)
    - `error_THz`: float (THz)

Notes: The verifier compares fitted parameters by absolute tolerance and audits the computed frequencies file for structural correctness.

## Self-check before finishing (optional, not scored)

A machine-readable copy of the output contract is below. Before you finish, write and run a small script that checks every file under `/app/outputs` against it: each declared file exists, JSON objects contain the required keys, and CSV/TSV files contain the required columns. Fix any mismatch before finishing.

This checks SHAPE ONLY (files, keys, columns) — it does NOT judge scientific correctness, and passing it does not mean your answer is correct.

```json
{
  "outputs": [
    {
      "file": "fitted_parameters.json",
      "format": "json",
      "purpose": "scored",
      "target_policy": "reference_match",
      "schema": {
        "type": "object",
        "required": [
          "KCl",
          "KBr",
          "RbCl",
          "AgBr"
        ],
        "properties": {
          "KCl": {
            "type": "object",
            "required": [
              "A_+-",
              "B_+-",
              "gamma_l_plus",
              "gamma_t_plus",
              "gamma_l_minus",
              "gamma_t_minus",
              "g1_plus",
              "g2_plus",
              "g4_plus",
              "h1_plus",
              "h2_plus",
              "g1_minus",
              "g2_minus",
              "h1_minus",
              "h2_minus"
            ],
            "additionalProperties": false,
            "properties": {
              "A_+-": {
                "type": "number"
              },
              "B_+-": {
                "type": "number"
              },
              "gamma_l_plus": {
                "type": "number"
              },
              "gamma_t_plus": {
                "type": "number"
              },
              "gamma_l_minus": {
                "type": "number"
              },
              "gamma_t_minus": {
                "type": "number"
              },
              "g1_plus": {
                "type": "number"
              },
              "g2_plus": {
                "type": "number"
              },
              "g4_plus": {
                "type": "number"
              },
              "h1_plus": {
                "type": "number"
              },
              "h2_plus": {
                "type": "number"
              },
              "g1_minus": {
                "type": "number"
              },
              "g2_minus": {
                "type": "number"
              },
              "h1_minus": {
                "type": "number"
              },
              "h2_minus": {
                "type": "number"
              }
            }
          },
          "KBr": {
            "type": "object",
            "required": [
              "A_+-",
              "B_+-",
              "gamma_l_plus",
              "gamma_t_plus",
              "gamma_l_minus",
              "gamma_t_minus",
              "g1_plus",
              "g2_plus",
              "g4_plus",
              "h1_plus",
              "h2_plus",
              "g1_minus",
              "g2_minus",
              "h1_minus",
              "h2_minus"
            ],
            "additionalProperties": false
          },
          "RbCl": {
            "type": "object",
            "required": [
              "A_+-",
              "B_+-",
              "gamma_l_plus",
              "gamma_t_plus",
              "gamma_l_minus",
              "gamma_t_minus",
              "g1_plus",
              "g2_plus",
              "g4_plus",
              "h1_plus",
              "h2_plus",
              "g1_minus",
              "g2_minus",
              "h1_minus",
              "h2_minus"
            ],
            "additionalProperties": false
          },
          "AgBr": {
            "type": "object",
            "required": [
              "A_+-",
              "B_+-",
              "gamma_l_plus",
              "gamma_t_plus",
              "gamma_l_minus",
              "gamma_t_minus",
              "g1_plus",
              "g2_plus",
              "g4_plus",
              "h1_plus",
              "h2_plus",
              "g1_minus",
              "g2_minus",
              "h1_minus",
              "h2_minus"
            ],
            "additionalProperties": false
          }
        }
      },
      "description": "Fitted D²I³ short-range force constants for KCl, KBr, RbCl, and AgBr in units of e²/V₀, structured as in the paper's Table IV."
    },
    {
      "file": "computed_phonon_frequencies.csv",
      "format": "csv",
      "purpose": "scored",
      "target_policy": "structural_audit",
      "schema": {
        "type": "table",
        "required_columns": [
          "material",
          "qx",
          "qy",
          "qz",
          "branch",
          "frequency_THz",
          "error_THz"
        ],
        "columns": {
          "material": "string",
          "qx": "float (reduced coordinate)",
          "qy": "float (reduced coordinate)",
          "qz": "float (reduced coordinate)",
          "branch": "string (LA, TA, LO, TO)",
          "frequency_THz": "float (THz)",
          "error_THz": "float (THz)"
        }
      },
      "description": "Computed phonon frequencies at the experimental q‑points. The verifier performs a structural audit: required columns are present, frequencies are nonnegative, errors are nonnegative, and branch labels belong to {LA, TA, LO, TO}."
    }
  ],
  "notes": "The verifier compares fitted parameters by absolute tolerance and audits the computed frequencies file for structural correctness."
}
```

## How you are scored
A hidden verifier independently scores each of the two output files and combines the scores by weight to produce a single reward in [0,1]. Do not attempt to guess or hardcode the paper's reported numbers; the verifier checks the actual computed quantities.

- **fitted_parameters.json**: The verifier compares each of your fitted force constants to a set of hidden reference values (obtained from a faithful re‑implementation of the fitting procedure on the same experimental data). Parameters are compared with an absolute tolerance; only a genuine least‑squares fit that converges to the correct solution will yield parameter values that match within the required tolerance.

- **computed_phonon_frequencies.csv**: The verifier performs a structural audit of the file: it checks that all required columns are present, that the phonon frequency and experimental error values are non‑negative, and that the branch labels belong to the allowed set (LA, TA, LO, TO). This step is load‑bearing; the file must be properly formatted and must contain the frequencies computed from your fitted model parameters. The structural audit alone does not test physical accuracy; combined with the parameter reference‑match, it ensures the pipeline has been executed correctly.

The verifier treats `fitted_parameters.json` by comparing parameters against hidden references (reference‑match) and treats `computed_phonon_frequencies.csv` by structural audit. Together, these two checks verify that you have correctly implemented the D²I³ model and performed the least‑squares minimization. The verifier does not require an exact reproduction of any particular published figure; it only demands that the fitted parameters match the hidden reference values within tolerance and that the phonon file is structurally valid.
